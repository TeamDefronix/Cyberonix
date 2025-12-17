"""
JS-Voyager main entrypoint
"""
import argparse
import os
import sys
from typing import List

# Add the tool's own directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Optional imports
try:
    from crawler import Crawler
except ImportError:
    Crawler = None

try:
    from downloader import JSDownloader
except ImportError:
    JSDownloader = None

try:
    from endpoint_extractor import EndpointExtractor
except ImportError:
    EndpointExtractor = None

try:
    from graph_visualizer import GraphVisualizer
except ImportError:
    GraphVisualizer = None

try:
    from reporter import Reporter
except ImportError:
    Reporter = None

try:
    from secrets_finder import SecretsFinder
except ImportError:
    SecretsFinder = None


def is_js_url(u: str) -> bool:
    if not isinstance(u, str):
        return False
    s = u.strip().lower()
    return s.endswith(".js") or ".js?" in s


def read_file_lines(path: str) -> List[str]:
    items = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                s = line.strip()
                if s:
                    items.append(s)
    except Exception as e:
        print(f"[-] Failed to read file {path}: {e}")
    return items


def normalize_protocol_relative(url: str) -> str:
    if not isinstance(url, str):
        return url
    u = url.strip()
    if u.startswith("//"):
        return "https:" + u
    return u


def pretty_print_secrets(results: dict):
    """Console-friendly summary of secrets scan results."""
    for target, info in results.items():
        print(f"\n=== {target} ===")
        if info.get("error"):
            print(f"  ERROR: {info['error']}")
            continue
        findings = info.get("findings", [])
        if not findings:
            print("  No findings.")
            continue
        for f in findings:
            if "entropy" in f:
                print(f"  - {f['type']} (len={f.get('length')}, ent={f.get('entropy')}) -> {f['match'][:160]}")
            else:
                print(f"  - {f['type']} -> {f['match'][:160]}")
    print("\n[+] Secrets scan display complete.")


def dedupe_keep_order(items: List[str]) -> List[str]:
    seen = set()
    out = []
    for it in items:
        if it not in seen:
            seen.add(it)
            out.append(it)
    return out


def main():
    parser = argparse.ArgumentParser(
        description="JS-Voyager — scan provided .js URLs (or crawl pages) for secrets; save only with --report"
    )
    parser.add_argument("-u", "--url", help="Single target URL (page or direct .js).")
    parser.add_argument("-f", "--file", help="Text file with one JS URL or local path per line.")
    parser.add_argument("--secrets", action="store_true", help="Run secrets scan on JS targets.")
    parser.add_argument("--report", action="store_true", help="Save reports to disk.")
    parser.add_argument("--graph", action="store_true", help="Generate interactive graph.")
    parser.add_argument("--no-download", action="store_true", help="Do not download JS files; scan remote URLs directly.")
    parser.add_argument("--limit", type=int, default=0, help="Process only first N JS targets (0 for no limit).")
    parser.add_argument("--out-dir", default="outputs", help="Directory to save reports.")

    args = parser.parse_args()

    if not args.url and not args.file:
        print("[-] Provide a URL (-u) or a file (-f). Use -h for help.")
        return

    os.makedirs(args.out_dir, exist_ok=True)

    raw_items = []
    if args.url:
        raw_items.append(args.url.strip())
    if args.file:
        raw_items.extend(read_file_lines(args.file))

    if not raw_items:
        print("[-] No input items found. Exiting.")
        return

    normalized = [normalize_protocol_relative(x) for x in raw_items]
    items = dedupe_keep_order(normalized)

    js_targets = []
    pages_to_crawl = []
    for it in items:
        if is_js_url(it) or os.path.isfile(it):
            js_targets.append(it)
        else:
            pages_to_crawl.append(it)

    if pages_to_crawl:
        if Crawler is None:
            print("[-] Crawler not present in project. Skipping page crawl.")
        else:
            for page in pages_to_crawl:
                try:
                    print(f"[+] Crawling page: {page}")
                    found = Crawler(page).crawl()
                    for f in found:
                        f2 = normalize_protocol_relative(f)
                        if f2 not in js_targets:
                            js_targets.append(f2)
                    print(f"[+] Found {len(found)} JS file(s) on {page}")
                except Exception as e:
                    print(f"[-] Error crawling {page}: {e}")

    if not js_targets:
        print("[-] No JS targets discovered to scan. Exiting.")
        return

    if args.limit and args.limit > 0:
        orig_count = len(js_targets)
        js_targets = js_targets[: args.limit]
        print(f"[*] Limit in effect: processing first {len(js_targets)} of {orig_count} JS targets.")

    print(f"[+] Total JS targets to process: {len(js_targets)}")

    local_files = []
    if not args.no_download and JSDownloader:
        dl_dir = os.path.join(args.out_dir, "downloads")
        os.makedirs(dl_dir, exist_ok=True)
        try:
            print("[*] Downloading JS files...")
            downloader = JSDownloader(js_targets)
            local_files = downloader.download(dl_dir)
            local_files = [os.path.abspath(p) for p in local_files if p and os.path.exists(p)]
            print(f"[+] Downloaded {len(local_files)} file(s).")
        except Exception as e:
            print(f"[-] Downloader error: {e}")
            local_files = []
    else:
        if args.no_download:
            print("[*] Skipping download (--no-download).")
        else:
            print("[*] JSDownloader not present; skipping download.")

    if args.secrets:
        if SecretsFinder is None:
            print("[-] secrets_finder.py not found.")
        else:
            scan_targets = local_files if local_files else js_targets
            print(f"[+] Running secrets scan on {len(scan_targets)} item(s)...")
            sf = SecretsFinder(scan_targets)
            try:
                results = sf.run()
            except Exception as e:
                print(f"[-] SecretsFinder.run() raised an exception: {e}")
                results = {}
            pretty_print_secrets(results)
            if args.report:
                json_path, txt_path = sf.save_reports(filename_prefix=os.path.join(args.out_dir, "secrets_report"))
                print(f"[+] Secrets reports saved: {json_path}, {txt_path}")
    
    # Other sections like Endpoint extraction, Graphing, and Reporting would follow...
    
    print("\n[+] Run complete.")


if __name__ == "__main__":
    main()
