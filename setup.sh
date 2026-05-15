#!/bin/bash
# Claude Code SE Starter Kit — Setup Script
# Run this after cloning the repo to install the foundation.
#
# What it does:
#   1. Creates ~/.claude/ directory structure (won't overwrite existing)
#   2. Copies rules, hooks, and skill templates
#   3. Asks for your info to personalize CLAUDE.md
#   4. Wires hooks into settings
#
# Usage: ./setup.sh [--dry-run] [--check] [--uninstall]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
DRY_RUN=false

# Colors (defined early for --check and --uninstall)
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "=== DRY RUN MODE — no files will be written ==="
    echo ""
fi

# --- Health Check Mode ---
if [[ "${1:-}" == "--check" ]]; then
    echo -e "${CYAN}Claude Code SE Starter Kit — Health Check${NC}"
    echo ""
    FAIL=0

    # 1. ~/.claude/ directory
    if [[ -d "$CLAUDE_DIR" ]]; then
        echo -e "  ${GREEN}✓${NC} ~/.claude/ directory exists"
    else
        echo -e "  ${RED}✗${NC} ~/.claude/ directory missing"
        FAIL=1
    fi

    # 2. settings.json exists and is configured
    if [[ -f "$CLAUDE_DIR/settings.json" ]]; then
        if grep -qiE "apiKey|Key|model|permissions" "$CLAUDE_DIR/settings.json" 2>/dev/null; then
            echo -e "  ${GREEN}✓${NC} ~/.claude/settings.json exists and is configured"
        else
            echo -e "  ${YELLOW}⚠${NC} ~/.claude/settings.json exists but looks empty or unconfigured"
        fi
    else
        echo -e "  ${RED}✗${NC} ~/.claude/settings.json missing"
        FAIL=1
    fi

    # 3. Hook scripts exist and are executable
    for hook_file in "$SCRIPT_DIR/hooks/scripts/"*.py; do
        filename=$(basename "$hook_file")
        dest="$CLAUDE_DIR/hooks/scripts/$filename"
        if [[ -x "$dest" ]]; then
            echo -e "  ${GREEN}✓${NC} Hook: $filename installed and executable"
        elif [[ -f "$dest" ]]; then
            echo -e "  ${YELLOW}⚠${NC} Hook: $filename installed but not executable"
        else
            echo -e "  ${RED}✗${NC} Hook: $filename not installed"
            FAIL=1
        fi
    done

    # 4. python3
    if command -v python3 &>/dev/null; then
        echo -e "  ${GREEN}✓${NC} python3 available ($(python3 --version 2>&1))"
    else
        echo -e "  ${RED}✗${NC} python3 not found"
        FAIL=1
    fi

    # 5. git
    if command -v git &>/dev/null; then
        echo -e "  ${GREEN}✓${NC} git available"
    else
        echo -e "  ${RED}✗${NC} git not found"
        FAIL=1
    fi

    # 6. sf CLI (non-critical)
    if command -v sf &>/dev/null; then
        echo -e "  ${GREEN}✓${NC} sf CLI available"
    else
        echo -e "  ${YELLOW}⚠${NC} sf CLI not found (hooks degrade gracefully)"
    fi

    # 7. ZScaler / VPN reachability
    HEALTH_URL="https://eng-ai-model-gateway.sfproxy.devx-preprod.aws-esvc1-useast2.aws.sfdc.cl/health"
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$HEALTH_URL" 2>/dev/null || echo "000")
    if [[ "$HTTP_CODE" == "000" ]]; then
        echo -e "  ${YELLOW}⚠${NC} LLMGW health check timed out — is ZScaler/VPN active?"
    elif [[ "$HTTP_CODE" =~ ^2 ]]; then
        echo -e "  ${GREEN}✓${NC} LLMGW reachable (HTTP $HTTP_CODE)"
    else
        echo -e "  ${YELLOW}⚠${NC} LLMGW returned HTTP $HTTP_CODE — check VPN"
    fi

    echo ""
    if [[ $FAIL -eq 0 ]]; then
        echo -e "${GREEN}All critical checks passed.${NC}"
        exit 0
    else
        echo -e "${RED}Some critical checks failed. Run ./setup.sh to install missing components.${NC}"
        exit 1
    fi
fi

# --- Uninstall Mode ---
if [[ "${1:-}" == "--uninstall" ]]; then
    echo -e "${CYAN}Claude Code SE Starter Kit — Uninstall${NC}"
    echo ""

    # Build list of files this kit would have installed
    FILES_TO_REMOVE=()

    for rule_file in "$SCRIPT_DIR/rules/"*.md; do
        filename=$(basename "$rule_file")
        target="$CLAUDE_DIR/rules/$filename"
        [[ -f "$target" ]] && FILES_TO_REMOVE+=("$target")
    done

    for hook_file in "$SCRIPT_DIR/hooks/scripts/"*.py; do
        filename=$(basename "$hook_file")
        target="$CLAUDE_DIR/hooks/scripts/$filename"
        [[ -f "$target" ]] && FILES_TO_REMOVE+=("$target")
    done

    for skill_file in "$SCRIPT_DIR/skills/"*.md; do
        filename=$(basename "$skill_file")
        target="$CLAUDE_DIR/commands/$filename"
        [[ -f "$target" ]] && FILES_TO_REMOVE+=("$target")
    done

    if [[ ${#FILES_TO_REMOVE[@]} -eq 0 ]]; then
        echo "  No starter kit files found in ~/.claude/. Nothing to remove."
        exit 0
    fi

    echo "  Files to remove:"
    for f in "${FILES_TO_REMOVE[@]}"; do
        echo "    $f"
    done
    echo ""
    echo "  Note: ~/.claude/settings.json will NOT be touched."
    echo ""

    read -p "  Remove these ${#FILES_TO_REMOVE[@]} files? (Y/n) " confirm
    if [[ "${confirm:-Y}" =~ ^[Yy]$ ]]; then
        for f in "${FILES_TO_REMOVE[@]}"; do
            rm "$f"
            echo -e "  ${GREEN}✓${NC} Removed: $f"
        done
        echo ""
        echo -e "${GREEN}Uninstall complete. ${#FILES_TO_REMOVE[@]} files removed.${NC}"
    else
        echo "  Cancelled. No files were removed."
    fi
    exit 0
fi

echo -e "${CYAN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  Claude Code SE Starter Kit — Setup          ║${NC}"
echo -e "${CYAN}║  From Day 0 to Day 30 in 30 minutes         ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════╝${NC}"
echo ""

# --- Step 0: CLI environment check ---
echo -e "${GREEN}[0/5]${NC} Checking CLI environment..."
echo ""

if ! bash "$SCRIPT_DIR/scripts/check-cli.sh"; then
    echo ""
    echo -e "${RED}Required CLIs are missing. Install them and re-run setup.${NC}"
    echo ""
    exit 1
fi

echo ""

# --- Step 1: Create directory structure ---
echo -e "${GREEN}[1/5]${NC} Creating directory structure..."

DIRS=(
    "$CLAUDE_DIR/rules"
    "$CLAUDE_DIR/hooks/scripts"
    "$CLAUDE_DIR/commands"
)

for dir in "${DIRS[@]}"; do
    if [[ "$DRY_RUN" == false ]]; then
        mkdir -p "$dir"
    fi
    echo "  ✓ $dir"
done
echo ""

# --- Step 2: Copy rules ---
echo -e "${GREEN}[2/5]${NC} Installing rules..."

for rule_file in "$SCRIPT_DIR/rules/"*.md; do
    filename=$(basename "$rule_file")
    dest="$CLAUDE_DIR/rules/$filename"
    if [[ -f "$dest" ]]; then
        echo -e "  ${YELLOW}⚠ $filename already exists — skipping${NC}"
    else
        if [[ "$DRY_RUN" == false ]]; then
            cp "$rule_file" "$dest"
        fi
        echo "  ✓ $filename installed"
    fi
done
echo ""

# --- Step 3: Copy hooks ---
echo -e "${GREEN}[3/5]${NC} Installing hooks..."

for hook_file in "$SCRIPT_DIR/hooks/scripts/"*.py; do
    filename=$(basename "$hook_file")
    dest="$CLAUDE_DIR/hooks/scripts/$filename"
    if [[ -f "$dest" ]]; then
        echo -e "  ${YELLOW}⚠ $filename already exists — skipping${NC}"
    else
        if [[ "$DRY_RUN" == false ]]; then
            cp "$hook_file" "$dest"
            chmod +x "$dest"
        fi
        echo "  ✓ $filename installed"
    fi
done
echo ""

# --- Step 4: Copy skills ---
echo -e "${GREEN}[4/5]${NC} Installing SE skills..."

for skill_file in "$SCRIPT_DIR/skills/"*.md; do
    filename=$(basename "$skill_file")
    dest="$CLAUDE_DIR/commands/$filename"
    if [[ -f "$dest" ]]; then
        echo -e "  ${YELLOW}⚠ $filename already exists — skipping${NC}"
    else
        if [[ "$DRY_RUN" == false ]]; then
            cp "$skill_file" "$dest"
        fi
        echo "  ✓ $filename installed"
    fi
done
echo ""

# --- Step 5: Wire hooks into settings.json (merge-safe) ---
echo -e "${GREEN}[5/6]${NC} Wiring hooks into settings.json..."

SETTINGS_FILE="$CLAUDE_DIR/settings.json"
if [[ -f "$SETTINGS_FILE" ]]; then
    # Check if hooks are already wired
    if grep -q "session-init.py" "$SETTINGS_FILE" 2>/dev/null; then
        echo -e "  ${YELLOW}⚠ Hooks already wired in settings.json — skipping${NC}"
    else
        if [[ "$DRY_RUN" == false ]]; then
            # Use python3 to safely merge hooks into existing settings.json
            # Format: {"hooks": {"EventName": [{"matcher": "ToolName", "hooks": [{"type": "command", "command": "..."}]}]}}
            python3 -c "
import json, sys

settings_path = '$SETTINGS_FILE'
try:
    with open(settings_path) as f:
        lines = f.readlines()
        clean = ''.join(l for l in lines if not l.strip().startswith('//'))
        settings = json.loads(clean)
except Exception:
    print('  Could not parse settings.json — skipping hook wiring.', file=sys.stderr)
    print('  Wire hooks manually using the REFERENCE file.', file=sys.stderr)
    sys.exit(0)

if 'hooks' not in settings:
    settings['hooks'] = {}

hooks = settings['hooks']

def add_hook(event, matcher, command):
    if event not in hooks:
        hooks[event] = []
    script_name = command.split('/')[-1]
    if any(script_name in json.dumps(h) for h in hooks[event]):
        return
    entry = {'hooks': [{'type': 'command', 'command': command}]}
    if matcher:
        entry['matcher'] = matcher
    hooks[event].append(entry)

add_hook('SessionStart', '', 'python3 ~/.claude/hooks/scripts/session-init.py')
add_hook('PreToolUse', 'Bash', 'python3 ~/.claude/hooks/scripts/guardrail.py')
add_hook('PreToolUse', 'Edit|Write', 'python3 ~/.claude/hooks/scripts/product-verification.py')
add_hook('PreToolUse', 'Bash', 'python3 ~/.claude/hooks/scripts/soql-schema-check.py')
add_hook('PostToolUse', 'Write', 'python3 ~/.claude/hooks/scripts/output-quality-gate.py')

with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=2)

print('  Hooks merged into settings.json successfully.')
" 2>&1
            if [[ $? -ne 0 ]]; then
                echo -e "  ${YELLOW}⚠ Could not auto-wire hooks. Wire them manually from settings.json.REFERENCE-ONLY${NC}"
            else
                echo "  ✓ Hooks wired into settings.json (auth key preserved)"
            fi
        else
            echo "  [dry-run] Would merge hooks into settings.json"
        fi
    fi
else
    echo -e "  ${YELLOW}⚠ No settings.json found — install LLMGW first, then re-run setup${NC}"
fi
echo ""

# --- Step 6: Personalization ---
echo -e "${GREEN}[6/6]${NC} Personalization..."
echo ""
echo "  To complete setup, open Claude Code and paste:"
echo ""
echo -e "  ${CYAN}Read ~/claude-code-se-starter-kit/QUICKSTART-PROMPT.md and follow the instructions.${NC}"
echo ""
echo "  Claude will ask you 5 questions and build your personalized CLAUDE.md."
echo ""

# --- Summary ---
echo -e "${GREEN}════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Setup complete!${NC}"
echo ""
echo "  Installed:"
echo "    • Rules, hook scripts, and skills copied to ~/.claude/"
echo "    • Hooks wired into settings.json (auth key preserved)"
echo ""
echo "  Next steps:"
echo "    1. Open Claude Code in your project directory"
echo "    2. Paste: Read ~/claude-code-se-starter-kit/QUICKSTART-PROMPT.md and follow the instructions."
echo "    3. Answer Claude's 5 questions"
echo "    4. Start using /account-prep before your next meeting"
echo ""
echo "  Questions? → #solutions-ai-tooling or jtehrani@salesforce.com"
echo -e "${GREEN}════════════════════════════════════════════════${NC}"
