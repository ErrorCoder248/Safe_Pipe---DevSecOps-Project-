import os
import re
from collections import Counter
import json

# ---------- Secret Patterns ----------
SECRET_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws(.{0,20})?['\"][0-9a-zA-Z/+]{40}['\"]?",
    "Private Key": r"['\"]?-----BEGIN PRIVATE KEY-----['\"]?",
    "Password": r"(?i)password\s*=\s*['\"].+?['\"]",
    "Token": r"['\"]?[A-Za-z0-9]{20,40}(\.[A-Za-z0-9]{20,40}){0,2}['\"]?"
}



# ---------- Severity Mapping ----------
SEVERITY_MAP = {
    "Private Key": "Critical",
    "AWS Access Key": "Medium",
    "AWS Secret Key": "Medium",
    "Password": "Low",
    "Token": "Low"
}

# ---------- Scan Function ----------
def scan_file(file_path):
    findings = []
    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.read()
            for secret_name, pattern in SECRET_PATTERNS.items():
                matches = re.findall(pattern, content)
                for match in matches:
                    severity = SEVERITY_MAP.get(secret_name, "Low")
                    findings.append({
                        "type": secret_name,
                        "value": match,
                        "file": file_path,
                        "severity": severity
                    })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return findings

# ---------- Summarize Function ----------
def summarize_findings(findings):
    total = len(findings)
    types = [item["type"] for item in findings]
    type_counts = Counter(types)
    files = set([item["file"] for item in findings])
    severity_counts = Counter([item["severity"] for item in findings])
    return total, type_counts, files, severity_counts

# ---------- Run Scanner on Folder ----------
def scan_folder(folder_path, output_file="scan_results.json"):
    all_findings = []
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        findings = scan_file(file_path)
        all_findings.extend(findings)

    # Save to JSON
    with open(output_file, "w") as f:
        json.dump(all_findings, f, indent=4)
    print(f"Scan complete! {len(all_findings)} secrets found. Results saved to {output_file}")
    return all_findings