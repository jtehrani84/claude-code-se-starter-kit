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
# Usage: ./setup.sh [--dry-run]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
DRY_RUN=false

if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "=== DRY RUN MODE — no files will be written ==="
    echo ""
fi

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

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

# --- Step 5: Personalization ---
echo -e "${GREEN}[5/5]${NC} Personalization..."
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
echo "    • 3 rules files (communication, security, architecture)"
echo "    • 2 hook scripts (session-init, guardrail)"
echo "    • 5 SE skills (account-prep, deal-strategy, email-draft, post-meeting, demo-prep)"
echo ""
echo "  Next steps:"
echo "    1. Open Claude Code in your project directory"
echo "    2. Paste: Read ~/claude-code-se-starter-kit/QUICKSTART-PROMPT.md and follow the instructions."
echo "    3. Answer Claude's 5 questions"
echo "    4. Start using /account-prep before your next meeting"
echo ""
echo "  Questions? → #solutions-ai-tooling or jtehrani@salesforce.com"
echo -e "${GREEN}════════════════════════════════════════════════${NC}"
