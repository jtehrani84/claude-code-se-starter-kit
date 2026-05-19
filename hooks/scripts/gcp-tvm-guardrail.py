#!/usr/bin/env python3
"""
GCP TVM Compliance Guardrail (PreToolUse - Bash)
=================================================

Intercepts gcloud commands and warns when they would create TVM violations.
Based on Salesforce Embark/TVM policy catalog (wiki/concepts/gcp-security-compliance.md).

Advisory only — never blocks. Surfaces the violation and the fix command.

Policy coverage:
  P1 ade7005f — Cloud Run permissive ingress (--ingress=all)
  P1 7c2101a4 — Cloud Run permissive ingress (duplicate policy)
  P1 ab8c8102 — Compute instance public IP
  P1 04f695bf — Compute instance public IP (duplicate)
  P1 ff7fa09c — Cloud Run using default Compute Engine SA
  P1 8127e9ca — VM with network path from untrusted internet on high-risk ports
  P1 23e1e1b1 — Cloud SQL public IP
  P1 d47fa186 — Overly permissive IAM bindings
"""

import json
import re
import sys

try:
    from stdin_utils import read_stdin_safe
except ImportError:
    def read_stdin_safe(timeout_seconds=0.1):
        if sys.stdin.isatty():
            return {}
        try:
            return json.load(sys.stdin)
        except Exception:
            return {}


VIOLATIONS = [
    # Cloud Run ingress
    {
        "pattern": r"gcloud\s+run\s+(deploy|services\s+update).*--ingress[= ]all",
        "policy": "ade7005f",
        "severity": "P1",
        "message": "Cloud Run ingress=all creates TVM violation. Use --ingress=internal-and-cloud-load-balancing instead.",
        "fix": "Add --ingress=internal-and-cloud-load-balancing to the deploy command.",
    },
    # Cloud Run allow-unauthenticated
    {
        "pattern": r"gcloud\s+run\s+deploy.*--allow-unauthenticated",
        "policy": "ff7fa09c/org-policy",
        "severity": "P1",
        "message": "Org policy blocks allUsers on Cloud Run. --allow-unauthenticated will fail or create a violation. Use app-level auth (Google OAuth) on a VM behind LB instead.",
        "fix": "Remove --allow-unauthenticated. Deploy on VM with app-level Google OAuth if browser access needed.",
    },
    # Cloud Run without explicit service account
    {
        "pattern": r"gcloud\s+run\s+deploy\s+(?!.*--service-account)",
        "policy": "ff7fa09c",
        "severity": "P1",
        "message": "Cloud Run deploy without --service-account uses default Compute Engine SA. Always specify a dedicated SA.",
        "fix": "Add --service-account=<name>@<your-project-id>.iam.gserviceaccount.com",
    },
    # Compute instance with public IP (no --no-address flag)
    {
        "pattern": r"gcloud\s+compute\s+instances\s+create(?!.*--no-address)(?!.*--network-interface=no-address)",
        "policy": "ab8c8102",
        "severity": "P1",
        "message": "VM created without --no-address will get a public IP (TVM violation). VMs should be behind a Load Balancer with no external IP.",
        "fix": "Add --no-address to the create command. Use GEALB for external access.",
    },
    # create-with-container also gets public IP by default
    {
        "pattern": r"gcloud\s+compute\s+instances\s+create-with-container(?!.*--no-address)",
        "policy": "ab8c8102",
        "severity": "P1",
        "message": "Container VM created without --no-address will get a public IP (TVM violation).",
        "fix": "Add --no-address. Route external traffic through GEALB.",
    },
    # Cloud SQL public IP
    {
        "pattern": r"gcloud\s+sql\s+instances\s+(create|patch).*--assign-ip",
        "policy": "23e1e1b1",
        "severity": "P1",
        "message": "Cloud SQL with public IP creates TVM violation. Use private IP only.",
        "fix": "Use --no-assign-ip. Access via VPC connector from Cloud Run or VM.",
    },
    # Overly permissive firewall rules
    {
        "pattern": r"gcloud\s+compute\s+firewall-rules\s+create.*--source-ranges[= ]0\.0\.0\.0/0",
        "policy": "f6a76e84",
        "severity": "P1",
        "message": "Firewall rule with 0.0.0.0/0 source range exposes to entire internet. Restrict to LB health check ranges (130.211.0.0/22, 35.191.0.0/16) or specific CIDRs.",
        "fix": "Use --source-ranges=130.211.0.0/22,35.191.0.0/16 for LB-only access.",
    },
    # IAM allUsers / allAuthenticatedUsers
    {
        "pattern": r"gcloud\s+.*add-iam-policy-binding.*--member[= ](allUsers|allAuthenticatedUsers)",
        "policy": "d47fa186/org-policy",
        "severity": "P1",
        "message": "Org policy blocks allUsers/allAuthenticatedUsers IAM bindings. This will fail. Use app-level auth instead.",
        "fix": "Use specific user:, group:, or serviceAccount: members. For browser-facing: VM + Google OAuth.",
    },
]


def get_command(input_data: dict) -> str:
    tool_input = input_data.get("tool_input", {})
    if isinstance(tool_input, str):
        try:
            tool_input = json.loads(tool_input)
        except json.JSONDecodeError:
            return ""
    return tool_input.get("command", "")


def check_violations(command: str) -> list:
    if "gcloud" not in command:
        return []

    matches = []
    for v in VIOLATIONS:
        if re.search(v["pattern"], command, re.IGNORECASE | re.DOTALL):
            matches.append(v)
    return matches


def main():
    input_data = read_stdin_safe(timeout_seconds=0.1)
    command = get_command(input_data)

    if not command:
        sys.exit(0)

    matches = check_violations(command)
    if not matches:
        sys.exit(0)

    lines = ["GCP TVM COMPLIANCE WARNING", ""]
    for m in matches:
        lines.append(f"  [{m['severity']}] Policy {m['policy']}: {m['message']}")
        lines.append(f"  Fix: {m['fix']}")
        lines.append("")

    lines.append("  Reference: wiki/concepts/gcp-security-compliance.md")
    lines.append("  SLA: P1 = 30 days. Violations trigger daily TVM alerts.")

    print("\n".join(lines))
    sys.exit(0)


if __name__ == "__main__":
    main()
