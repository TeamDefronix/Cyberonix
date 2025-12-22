import re

class EndpointExtractor:
    def __init__(self, local_files):
        self.local_files = local_files

    def extract(self):
        endpoints = []
        pattern = re.compile(r"https?://[\w./-]+")
        for file in self.local_files:
            try:
                with open(file, "r", errors="ignore") as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    endpoints.extend(matches)
            except Exception as e:
                print(f"[-] Error reading {file}: {e}")
        print(f"[+] Extracted {len(endpoints)} endpoints")
        return list(set(endpoints))
