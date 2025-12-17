# crawler.py
"""
Crawler for JS-Voyager

Capabilities:
 - Accepts a single page URL, a .js URL, or a .txt file containing URLs (one per line).
 - If input is a .txt and lines are .js URLs -> treats as JS list and downloads them.
 - If input is a .txt and lines are pages -> crawls each page for <script src="..."> and downloads those scripts.
 - Normalizes protocol-relative URLs (//example.com/...) and relative URLs via urljoin.
 - Downloads .js files to `download_dir` and returns list of local file paths.
"""

from typing import List
import os
import re
import requests
from urllib.parse import urljoin, urlparse
import hashlib
import time

DEFAULT_USER_AGENT = "JS-Voyager-Crawler/1.0"
DEFAULT_TIMEOUT = 10
DOWNLOAD_RETRY = 2
CHUNK_SIZE = 4096

class Crawler:
    def __init__(self, target: str, download_dir: str = "downloads", timeout: int = DEFAULT_TIMEOUT, user_agent: str = DEFAULT_USER_AGENT):
        """
        target: page URL, .js URL, or path to .txt list
        download_dir: where to save downloaded .js files
        """
        self.raw_target = target
        self.download_dir = download_dir
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})
        os.makedirs(self.download_dir, exist_ok=True)

    @staticmethod
    def is_js_url(u: str) -> bool:
        if not isinstance(u, str):
            return False
        s = u.strip().lower()
        if s.startswith("//"):
            return True
        if s.startswith("http://") or s.startswith("https://"):
            return s.split("?")[0].endswith(".js")
        if s.endswith(".js"):
            return True
        # some URLs contain .js?param
        return ".js?" in s

    @staticmethod
    def read_list_file(path: str) -> List[str]:
        out = []
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                for ln in fh:
                    s = ln.strip()
                    if s:
                        out.append(s)
        except Exception as e:
            print(f"[-] Error reading list file {path}: {e}")
        return out

    @staticmethod
    def extract_js_urls_from_html(html: str, base_url: str) -> List[str]:
        """
        Extracts <script src="..."> and other script src occurrences.
        Returns absolute URLs when possible.
        """
        scripts = []
        # match src="..." or src='...' or src= without quotes
        for m in re.finditer(r'<script[^>]+src\s*=\s*["\']?([^"\'\s>]+)', html, flags=re.IGNORECASE):
            src = m.group(1).strip()
            if src:
                scripts.append(urljoin(base_url, src))
        # also search for dynamic imports or .js references in text (best-effort)
        for m in re.finditer(r'["\'](https?:\/\/[^"\']+\.js[^\s"\']*)["\']', html, flags=re.IGNORECASE):
            scripts.append(m.group(1).strip())
        # de-duplicate preserving order
        seen = set()
        out = []
        for s in scripts:
            if s not in seen:
                seen.add(s)
                out.append(s)
        return out

    def fetch_page(self, url: str) -> (str, str):
        """
        Return (text, error) where error is None on success.
        """
        try:
            url = url.strip()
            if url.startswith("//"):
                url = "https:" + url
            r = self.session.get(url, timeout=self.timeout)
            r.raise_for_status()
            return r.text, None
        except Exception as e:
            return None, str(e)

    def _safe_filename_from_url(self, url: str) -> str:
        """
        Create a safe filename for saving the JS file.
        Use last path segment + short hash to avoid collisions.
        """
        parsed = urlparse(url)
        path = parsed.path or ""
        name = os.path.basename(path) or "script.js"
        # sanitize name (keep alnum, - _ .)
        name = re.sub(r'[^A-Za-z0-9\-\._]', '_', name)
        # add short hash of full url to avoid name clashes
        h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
        filename = f"{name}__{h}.js"
        return filename

    def download_js(self, js_url: str) -> (str, str):
        """
        Download js_url to self.download_dir, return (local_path, error)
        If error is None, local_path is path to saved file.
        """
        try:
            url = js_url.strip()
            if url.startswith("//"):
                url = "https:" + url
            # ensure scheme for relative urls - caller should have normalized
            if not urlparse(url).scheme:
                # can't download non-absolute URL
                return None, "Non-absolute URL (no scheme)"
            fname = self._safe_filename_from_url(url)
            outpath = os.path.join(self.download_dir, fname)
            # if file exists already, skip download
            if os.path.exists(outpath) and os.path.getsize(outpath) > 0:
                return outpath, None
            last_exc = None
            for attempt in range(1, DOWNLOAD_RETRY + 1):
                try:
                    with self.session.get(url, timeout=self.timeout, stream=True) as r:
                        r.raise_for_status()
                        with open(outpath, "wb") as fh:
                            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                                if chunk:
                                    fh.write(chunk)
                    return outpath, None
                except Exception as e:
                    last_exc = e
                    time.sleep(0.5)
                    continue
            return None, str(last_exc)
        except Exception as e:
            return None, str(e)

    def crawl(self) -> List[str]:
        """
        Main entry: inspects self.raw_target. Behavior:
         - if target is a file path ending with .txt: read lines; if lines are .js urls -> download them.
           else treat lines as pages and crawl each page for <script src>.
         - if target is a single .js URL: download it.
         - if target is a single page URL (non-.js): crawl and download found js files.
        Returns list of local downloaded file paths (successful only).
        """
        t = self.raw_target
        results = []

        # If it's a file path and exists:
        if isinstance(t, str) and os.path.isfile(t):
            # treat as list file
            entries = self.read_list_file(t)
            if not entries:
                print(f"[-] List file {t} is empty or could not be read.")
                return results
            # check if entries look like .js URLs
            if any(self.is_js_url(x) for x in entries):
                # treat as JS list: download each .js URL
                print(f"[+] Detected .js list file with {len(entries)} entries. Downloading JS files to '{self.download_dir}'...")
                for url in entries:
                    url = url.strip()
                    if not url:
                        continue
                    local, err = self.download_js(url)
                    if err:
                        print(f"[-] Failed to download {url}: {err}")
                    else:
                        print(f"[+] Downloaded {url}")
                        results.append(local)
                return results
            else:
                # treat entries as page URLs to crawl
                pages = entries
                print(f"[+] Detected list of {len(pages)} pages to crawl from {t}.")
                for page in pages:
                    page = page.strip()
                    if not page:
                        continue
                    text, err = self.fetch_page(page)
                    if err:
                        print(f"[-] Failed to fetch page {page}: {err}")
                        continue
                    js_urls = self.extract_js_urls_from_html(text, page)
                    if not js_urls:
                        print(f"[+] No JS files found on {page}")
                        continue
                    print(f"[+] Found {len(js_urls)} JS files on {page}; downloading...")
                    for js in js_urls:
                        local, derr = self.download_js(js)
                        if derr:
                            print(f"[-] Failed to download {js}: {derr}")
                        else:
                            print(f"[+] Downloaded {js}")
                            results.append(local)
                return results

        # If target is a string URL:
        if isinstance(t, str):
            t = t.strip()
            # direct js url?
            if self.is_js_url(t):
                print(f"[+] Single JS URL provided. Downloading {t} ...")
                local, err = self.download_js(t)
                if err:
                    print(f"[-] Failed to download {t}: {err}")
                else:
                    print(f"[+] Downloaded {t}")
                    results.append(local)
                return results
            else:
                # treat as page URL to crawl
                print(f"[+] Crawling page {t} for JS files...")
                text, err = self.fetch_page(t)
                if err:
                    print(f"[-] Failed to fetch page {t}: {err}")
                    return results
                js_urls = self.extract_js_urls_from_html(text, t)
                if not js_urls:
                    print(f"[+] No JS files found on {t}")
                    return results
                print(f"[+] Found {len(js_urls)} JS files on {t}; downloading...")
                for js in js_urls:
                    local, derr = self.download_js(js)
                    if derr:
                        print(f"[-] Failed to download {js}: {derr}")
                    else:
                        print(f"[+] Downloaded {js}")
                        results.append(local)
                return results

        print("[-] Unsupported target type. Provide a URL string or a path to a .txt file.")
        return results
