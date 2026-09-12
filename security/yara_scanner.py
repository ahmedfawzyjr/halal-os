#!/usr/bin/env python3
"""
Halal OS Sovereign Security Guard - Offline YARA & Telemetry Scanner
Scans filesystem objects against rules.yara and strict Shariah/Privacy-protective heuristic rules.
Supports both native yara-python (if installed) and robust built-in sovereign pattern matching.
"""

import os
import sys
import argparse
import re

RULES_FILE = os.path.join(os.path.dirname(__file__), "rules.yara")

# Sovereign built-in pattern heuristics mirroring rules.yara
BUILTIN_RULES = [
    {
        "name": "HalalGuard_Keylogger_Behavior",
        "description": "Direct hardware keyboard device grabbing or keylogging",
        "severity": "CRITICAL",
        "patterns": [b"/dev/input/event", b"EVIOCGRAB", b"readkey"],
        "match_type": "all_or_key_and_grab"
    },
    {
        "name": "HalalGuard_Telemetry_Collector",
        "description": "Background telemetry, metrics harvesting, or analytics pinging",
        "severity": "HIGH",
        "patterns": [b"telemetry.org", b"metrics_uploader", b"/ping/analytics", b"google-analytics.com", b"telemetry."],
        "match_type": "any"
    },
    {
        "name": "HalalGuard_Covert_Reverse_Shell",
        "description": "Socket connection spawning bash/sh interactive shell",
        "severity": "CRITICAL",
        "patterns": [b"/bin/sh", b"/bin/bash", b"socket", b"connect", b"dup2"],
        "match_type": "min_3"
    }
]

def scan_buffer(data: bytes, filename: str):
    matches = []
    
    # 1. Try native YARA if available
    try:
        import yara
        if os.path.exists(RULES_FILE):
            rules = yara.compile(RULES_FILE)
            yara_matches = rules.match(data=data)
            for m in yara_matches:
                matches.append({
                    "rule": m.rule,
                    "severity": m.meta.get("severity", "MEDIUM"),
                    "description": m.meta.get("description", "YARA signature match"),
                    "source": "yara_engine"
                })
            return matches
    except Exception:
        pass # Fallback to sovereign internal matcher

    # 2. Sovereign built-in pattern scanner
    lower_data = data.lower()
    for rule in BUILTIN_RULES:
        match_count = 0
        hit_patterns = []
        for pat in rule["patterns"]:
            if pat.lower() in lower_data:
                match_count += 1
                hit_patterns.append(pat.decode("utf-8", errors="ignore"))
        
        triggered = False
        if rule["match_type"] == "any" and match_count > 0:
            triggered = True
        elif rule["match_type"] == "all_or_key_and_grab":
            if b"/dev/input/event" in lower_data and (b"eviocgrab" in lower_data or b"readkey" in lower_data):
                triggered = True
        elif rule["match_type"] == "min_3" and match_count >= 3:
            triggered = True

        if triggered:
            matches.append({
                "rule": rule["name"],
                "severity": rule["severity"],
                "description": rule["description"],
                "hits": hit_patterns,
                "source": "sovereign_heuristic"
            })

    return matches

def scan_file(filepath: str):
    try:
        with open(filepath, "rb") as f:
            data = f.read(10 * 1024 * 1024) # Scan up to 10MB
        return scan_buffer(data, filepath)
    except Exception as e:
        return [{"rule": "READ_ERROR", "severity": "WARN", "description": str(e)}]

def main():
    parser = argparse.ArgumentParser(description="Halal OS Sovereign YARA Scanner")
    parser.add_argument("target", help="File or directory path to scan")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    target = os.path.abspath(args.target)
    if not os.path.exists(target):
        print(f"Error: Target path '{target}' not found.", file=sys.stderr)
        sys.exit(1)

    all_results = {}
    total_scanned = 0
    total_threats = 0

    if os.path.isfile(target):
        files_to_scan = [target]
    else:
        files_to_scan = []
        for root, _, files in os.walk(target):
            for file in files:
                files_to_scan.append(os.path.join(root, file))

    print(f"===============================================================")
    print(f"🛡️  Halal OS Sovereign YARA & Telemetry Scanner")
    print(f"Target: {target} ({len(files_to_scan)} files)")
    print(f"Engine: Offline Air-Gapped Heuristics + YARA Compiler")
    print(f"===============================================================\n")

    for fpath in files_to_scan:
        total_scanned += 1
        matches = scan_file(fpath)
        if matches:
            total_threats += len(matches)
            all_results[fpath] = matches
            print(f"⚠️  [FLAGGED] {fpath}")
            for m in matches:
                print(f"    - Rule: {m.get('rule')} [{m.get('severity')}]")
                print(f"      Desc: {m.get('description')}")
        else:
            print(f"✔  [SAFE] {fpath}")

    print("\n---------------------------------------------------------------")
    print(f"Scan Finished: {total_scanned} files inspected | {total_threats} violations detected.")
    if total_threats == 0:
        print("✅ Environment is Verified Halal & Free of Prohibited Telemetry.")
        sys.exit(0)
    else:
        print("🚨 Warning: Banned telemetry or suspicious behaviors detected!")
        sys.exit(2)

if __name__ == "__main__":
    main()
