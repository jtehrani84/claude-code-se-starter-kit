#!/usr/bin/env python3
"""
Product Verification Hook — PreToolUse on Edit/Write operations.

Catches hallucinated or outdated Salesforce product names before they reach
the output. LLMs frequently invent plausible-sounding product names that
don't exist or use deprecated terminology.

Fires on: Edit, Write
Reads: tool_input from stdin (JSON)
Outputs: JSON with result "continue" (with optional warning) or "block"
"""

import json
import re
import sys


# Product name corrections: wrong_name -> guidance
# Add your org's common hallucinations here
PRODUCT_CORRECTIONS = {
    "agentforce script": (
        "The product is called 'Agent Script' (the DSL) or "
        "'Agent Actions & Topics' (the Builder feature). "
        "'Agentforce Script' is not a real product name."
    ),
    "einstein copilot": (
        "Einstein Copilot was renamed to 'Agentforce' in late 2024. "
        "Use 'Agentforce' unless referring to the historical product."
    ),
    "data cloud 360": (
        "This product does not exist. Use 'Data Cloud' (the platform) "
        "or 'Salesforce Data 360' (the vision/framework). Never combine them."
    ),
    "einstein gpt": (
        "Einstein GPT was rebranded. The current product is 'Agentforce' "
        "for conversational AI and 'Einstein' for predictive AI features."
    ),
    "salesforce copilot": (
        "There is no 'Salesforce Copilot'. The product is 'Agentforce'. "
        "Copilot is a Microsoft term."
    ),
    "agentforce studio": (
        "The correct name is 'Agent Builder' (for building agents) or "
        "'Agentforce' (the platform). 'Agentforce Studio' may be "
        "confused with the older 'Bot Builder'."
    ),
    "einstein bot": (
        "Einstein Bots still exist but are legacy. For new work, "
        "the product is 'Agentforce'. Clarify which you mean."
    ),
    "data cloud intelligence": (
        "This is not an official product name. Use 'Data Cloud' "
        "for the platform or specify the feature (segments, calculated "
        "insights, identity resolution)."
    ),
    "salesforce ai cloud": (
        "The product is 'Einstein 1 Platform' or just 'Salesforce Platform'. "
        "'AI Cloud' was a brief marketing term, not a product."
    ),
    "flow orchestrator": (
        "The correct name is 'Flow Orchestration' (not Orchestrator). "
        "Small difference, but it matters in official docs."
    ),
}

# Patterns that might indicate a hallucinated product (not definitive)
SUSPICIOUS_PATTERNS = [
    r"Salesforce\s+[A-Z][a-z]+\s+(?:Cloud|AI|360|Studio|Hub|Engine)",
    r"Einstein\s+[A-Z][a-z]+\s+(?:Agent|Bot|Cloud|Platform)",
    r"Agentforce\s+[A-Z][a-z]+\s+(?:Studio|Hub|Platform|Engine|Cloud)",
]


def check_content(text):
    """Check text for known product name errors."""
    warnings = []
    text_lower = text.lower()

    for wrong_name, guidance in PRODUCT_CORRECTIONS.items():
        if wrong_name in text_lower:
            warnings.append(f"PRODUCT NAME: '{wrong_name}' found. {guidance}")

    # Check suspicious patterns (informational only)
    for pattern in SUSPICIOUS_PATTERNS:
        matches = re.findall(pattern, text)
        for match in matches:
            # Don't flag known-good names
            known_good = [
                "Salesforce Data Cloud", "Salesforce Platform",
                "Einstein AI", "Agentforce Agent",
                "Einstein 1 Platform", "Data Cloud",
            ]
            if match not in known_good:
                warnings.append(
                    f"VERIFY: '{match}' — confirm this is an official "
                    f"Salesforce product name at salesforce.com before using."
                )

    return warnings


def main():
    hook_input = json.loads(sys.stdin.read())

    tool_name = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input", {})

    # Only check Edit and Write operations
    if tool_name not in ("Edit", "Write"):
        print(json.dumps({"result": "continue"}))
        return

    # Get the content being written
    content = ""
    if tool_name == "Write":
        content = tool_input.get("content", "")
    elif tool_name == "Edit":
        content = tool_input.get("new_string", "")

    if not content:
        print(json.dumps({"result": "continue"}))
        return

    warnings = check_content(content)

    if warnings:
        # Don't block — just warn. Product names might be in quoted
        # historical context or comparisons.
        combined = " | ".join(warnings[:3])  # Cap at 3 warnings
        output = {
            "result": "continue",
            "warning": f"Product Verification: {combined}",
        }
    else:
        output = {"result": "continue"}

    print(json.dumps(output))


if __name__ == "__main__":
    main()
