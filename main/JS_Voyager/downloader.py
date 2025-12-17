# downloader.py
import requests
import os
import hashlib
from urllib.parse import urlparse, urljoin
import time
import re

class JSDownloader:
    def __init__(self, js_files, download_dir="downloads", timeout=10, retries=2):
        """
        js_files: list of JS URLs (strings)
        download_dir: base downloads folder
        """
        self.js_files = js_files
        self.download_dir = download_dir
        self.timeout = timeout
        self.retries = retries
        os.makedirs(self.download_dir, exist_ok=True)

    def _normalize_url(self, url: str) -> str:
        url = url.strip()
        if url.startswith("//"):
            return "https:" + url
        return url

    def _get_subdomain_folder(self, url: str) -> str:
        """
        Create and return folder path like: downloads/<Subdomain> JS
        Uses the first label of the hostname (subdomain or domain).
        Examples:
          https://defronix.com -> downloads/Defronix JS
          https://analytics.jp.budgetair.com -> downloads/Analytics JS
          https://www.travix.com -> downloads/Www JS
        """
        try:
            parsed = urlparse(url)
            host = parsed.hostname or "unknown"
        except Exception:
            host = "unknown"

        label = host.split(".")[0] if host else "unknown"
        # sanitize label to be filesystem-friendly
        label = re.sub(r"[^A-Za-z0-9\-]", "_", label).strip("_")
        folder_name = f"{label.capitalize()} JS"
        folder_path = os.path.join(self.download_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def _safe_filename(self, url: str) -> str:
        """
        Create a safe filename from URL: basename + __<sha8>.js
        """
        parsed = urlparse(url)
        base = os.path.basename(parsed.path) or "script.js"
        # remove query strings from base if any (shouldn't be there)
        base = base.split("?")[0]
        # sanitize base
        base = re.sub(r"[^A-Za-z0-9\-\._]", "_", base)
        if not base.lower().endswith(".js"):
            base = base + ".js"
        short_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
        filename = f"{base}__{short_hash}.js"
        return filename

    def _download_one(self, url: str, dest_path: str) -> bool:
        last_exc = None
        for attempt in range(1, self.retries + 1):
            try:
                with requests.get(url, timeout=self.timeout, stream=True) as r:
                    r.raise_for_status()
                    with open(dest_path, "wb") as fh:
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                fh.write(chunk)
                return True
            except Exception as e:
                last_exc = e
                time.sleep(0.5)
        print(f"[-] Failed to download {url}: {last_exc}")
        return False

    def download(self):
        """
        Download all URLs into per-subdomain folders under download_dir.
        Returns list of local file paths (successful downloads only).
        """
        local_files = []
        for js in self.js_files:
            try:
                url = self._normalize_url(js)
                parsed = urlparse(url)
                if not parsed.scheme or not parsed.netloc:
                    print(f"[-] Skipping invalid URL: {js}")
                    continue

                folder = self._get_subdomain_folder(url)
                filename = self._safe_filename(url)
                path = os.path.join(folder, filename)

                # skip if already exists and non-zero
                if os.path.exists(path) and os.path.getsize(path) > 0:
                    print(f"[~] Already exists, skipping: {path}")
                    local_files.append(path)
                    continue

                success = self._download_one(url, path)
                if success:
                    print(f"[+] Downloaded {url} -> {path}")
                    local_files.append(path)
            except Exception as e:
                print(f"[-] Error processing {js}: {e}")

        return local_files
