# reports.py
"""
Reporter for JS-Voyager

Provides:
 - generate_report(results, out_dir, meta)
Inputs:
 - results: dict mapping target -> {"error":..., "findings": [ {type, match, length?, entropy?}, ... ]}
 - out_dir: directory to save reports
 - meta: optional dict (e.g. {"targets_count": int, "args": "...", "timestamp": "..."})
Outputs (saved):
 - JSON (full structured)
 - TXT (human readable)
 - CSV (flat rows)
 - simple summary printed to console
"""
from __future__ import annotations
import os
import json
import csv
from datetime import datetime
from typing import Dict, Any, List, Optional

def _ensure_dir(d: str):
    os.makedirs(d, exist_ok=True)

def _ts():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def _flatten_findings(target: str, info: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows = []
    if info is None:
        return rows
    if "error" in info:
        rows.append({"target": target, "type": "ERROR", "match": info["error"], "length": "", "entropy": ""})
        return rows
    findings = info.get("findings", [])
    if not findings:
        rows.append({"target": target, "type": "NO_FINDINGS", "match": "", "length": "", "entropy": ""})
        return rows
    for f in findings:
        # f may be dict or tuple or string, normalize
        if isinstance(f, dict):
            typ = f.get("type") or f.get("name") or ""
            match = f.get("match") or f.get("value") or ""
            length = f.get("length", len(match) if match else "")
            entropy = f.get("entropy", "")
        else:
            # assume tuple (name, match) or simple string
            if isinstance(f, (list, tuple)) and len(f) >= 2:
                typ, match = f[0], f[1]
                length = len(match)
                entropy = ""
            else:
                typ = "match"
                match = str(f)
                length = len(match)
                entropy = ""
        rows.append({"target": target, "type": typ, "match": match, "length": length, "entropy": entropy})
    return rows

def generate_report(results: Dict[str, Any],
                    out_dir: str = "outputs",
                    meta: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
    """
    Save reports in JSON, TXT, CSV formats.
    Returns dict of saved file paths.
    """
    _ensure_dir(out_dir)
    ts = _ts()
    base = os.path.join(out_dir, f"secrets_report_{ts}")

    json_path = base + ".json"
    txt_path = base + ".txt"
    csv_path = base + ".csv"

    # Write JSON (full)
    with open(json_path, "w", encoding="utf-8") as jf:
        wrapper = {"meta": meta or {}, "results": results}
        json.dump(wrapper, jf, indent=2, ensure_ascii=False)

    # Write TXT (human readable)
    with open(txt_path, "w", encoding="utf-8") as tf:
        header = f"JS-Voyager Secrets Report — {ts}\n"
        tf.write(header)
        tf.write("=" * len(header) + "\n\n")
        if meta:
            tf.write("Meta:\n")
            for k, v in (meta.items() if isinstance(meta, dict) else []):
                tf.write(f"  {k}: {v}\n")
            tf.write("\n")
        for target, info in results.items():
            tf.write(f"=== {target} ===\n")
            if info is None:
                tf.write("  [ERROR] No data\n\n")
                continue
            if info.get("error"):
                tf.write(f"  [ERROR] {info.get('error')}\n\n")
                continue
            findings = info.get("findings", [])
            if not findings:
                tf.write("  [-] No findings\n\n")
                continue
            # print grouped by type
            by_type = {}
            for f in findings:
                typ = f.get("type") if isinstance(f, dict) else (f[0] if isinstance(f, (list, tuple)) else "match")
                by_type.setdefault(typ, []).append(f)
            for typ, items in by_type.items():
                tf.write(f"  >> {typ} ({len(items)})\n")
                for item in items:
                    if isinstance(item, dict):
                        match = item.get("match", "")
                        ent = item.get("entropy", "")
                        tf.write(f"     - {match[:200]}{(' ...' if len(match)>200 else '')} {('(ent='+str(ent)+')') if ent!='' else ''}\n")
                    else:
                        # tuple or string
                        if isinstance(item, (list, tuple)) and len(item) >= 2:
                            tf.write(f"     - {item[1]}\n")
                        else:
                            tf.write(f"     - {str(item)}\n")
                tf.write("\n")
        tf.write("\nEnd of report.\n")

    # Write CSV (flat)
    rows = []
    for target, info in results.items():
        rows.extend(_flatten_findings(target, info))
    # ensure at least header
    fieldnames = ["target", "type", "match", "length", "entropy"]
    with open(csv_path, "w", encoding="utf-8", newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    # Print summary to console
    total_targets = len(results)
    total_findings = sum(len(info.get("findings", [])) if info and isinstance(info, dict) else 0 for info in results.values())
    summary = {
        "json": json_path,
        "txt": txt_path,
        "csv": csv_path,
        "targets": total_targets,
        "findings": total_findings
    }
    print(f"[+] Reports saved to: {out_dir}")
    print(f"    JSON: {json_path}")
    print(f"    TXT : {txt_path}")
    print(f"    CSV : {csv_path}")
    print(f"    Targets processed: {total_targets}")
    print(f"    Total findings: {total_findings}")

    return summary
