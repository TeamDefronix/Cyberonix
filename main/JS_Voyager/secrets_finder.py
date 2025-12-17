# secrets_finder.py
import os
import re
import json
import math
import requests

class SecretsFinder:
    def __init__(self, targets, regex_file="patterns.json"):
        self.targets = targets
        self.patterns = self._load_patterns(regex_file)

    def _load_patterns(self, regex_file):
        # Load regex patterns from JSON
        try:
            import json
            with open(regex_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[-] Could not load regex patterns ({regex_file}): {e}")
            return {}

    def _shannon_entropy(self, data):
        if not data:
            return 0
        entropy = 0
        for x in set(data):
            p_x = data.count(x) / len(data)
            entropy -= p_x * math.log2(p_x)
        return round(entropy, 3)

    def _scan_content(self, content):
        findings = []
        for name, pattern in self.patterns.items():
            try:
                for m in re.finditer(pattern, content, re.IGNORECASE):
                    match = m.group(0)
                    findings.append({
                        "type": name,
                        "match": match,
                        "length": len(match),
                        "entropy": self._shannon_entropy(match)
                    })
            except re.error as e:
                print(f"[-] Invalid regex for {name}: {e}")
        return findings

    def _read_target(self, target):
        if os.path.isfile(target):
            with open(target, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        elif target.startswith("http://") or target.startswith("https://"):
            try:
                r = requests.get(target, timeout=10)
                if r.status_code == 200:
                    return r.text
                return ""
            except Exception as e:
                print(f"[-] Error fetching {target}: {e}")
                return ""
        return ""

    def run(self):
        results = {}
        for t in self.targets:
            try:
                content = self._read_target(t)
                if not content:
                    results[t] = {"error": "empty or failed fetch"}
                    continue
                findings = self._scan_content(content)
                results[t] = {"findings": findings}
            except Exception as e:
                results[t] = {"error": str(e)}
        return results

    def save_reports(self, filename_prefix="secrets_report"):
        json_path = f"{filename_prefix}.json"
        txt_path = f"{filename_prefix}.txt"

        results = self.run()

        # Save JSON
        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(results, jf, indent=2)

        # Save TXT (pretty)
        with open(txt_path, "w", encoding="utf-8") as tf:
            for target, info in results.items():
                tf.write(f"\n=== {target} ===\n")
                if "error" in info:
                    tf.write(f"  ERROR: {info['error']}\n")
                else:
                    if not info["findings"]:
                        tf.write("  No findings.\n")
                    for f in info["findings"]:
                        tf.write(f"  - {f['type']} -> {f['match'][:100]}\n")

        return json_path, txt_path
