# Claude Code SE Starter Kit

**Go from Day 0 to Day 30 in 30 minutes.**

This kit gives you the persistent context architecture that took 60 days of trial-and-error to build. Clone it, run setup, and start compounding immediately.

## What You Get

| Layer | What | Impact |
|-------|------|--------|
| **Identity** | Template CLAUDE.md with routing table | Claude knows your role, projects, and constraints from session 1 |
| **Rules** | 3 governance files (voice, security, architecture) | Standards enforced automatically — no re-explaining |
| **Hooks** | Session-init + guardrail script | Context routes itself; your worst mistake gets blocked |
| **Skills** | 5 SE-specific workflows | /account-prep, /deal-strategy, /email-draft, /post-meeting, /demo-prep |
| **Wiki** | Starter knowledge base | Architecture decisions, corrections, reference docs — all organized |
| **Crons** | Intelligence automation template | Overnight Slack + web scanning → morning brief |

## Quick Start (30 minutes)

### Option A: One-command setup

```bash
git clone https://github.com/jtehrani84/claude-code-se-starter-kit.git
cd claude-code-se-starter-kit
./setup.sh
```

The setup script will:
1. Copy templates to your `~/.claude/` directory (won't overwrite existing files)
2. Ask your role, OU, and top constraint
3. Generate your personalized CLAUDE.md
4. Install hooks and rules
5. Set up the wiki structure

### Option B: Let Claude build it

Open Claude Code and paste:

```
I want to set up persistent context architecture. Read the setup instructions at ~/claude-code-se-starter-kit/QUICKSTART-PROMPT.md and build my personalized setup.
```

Claude will scaffold everything interactively.

## After Setup

### Week 1: Foundation
- Claude routes context automatically on session start
- Rules enforce your voice and security standards
- Run `/account-prep [company]` before any meeting
- When Claude makes a mistake, say "remember this" — it saves a memory file

### Week 2-3: Growth
- Memory files accumulate from corrections and decisions
- Wiki grows as Claude writes reference pages from your work
- Skills save 30+ minutes of instruction per use
- Morning brief starts arriving if you enable crons

### Week 4+: Compound Effects
- Guardrails prevent entire classes of errors
- Entity graph connects related knowledge automatically
- Skills call MCP servers for real data
- The system builds itself from here

## Directory Structure

```
~/.claude/
├── CLAUDE.md                    # Your identity + routing table (from template)
├── rules/                       # Always-loaded governance
│   ├── communication.md         # Voice standards, anti-slop
│   ├── security-governance.md   # CRUD/FLS, sharing, secrets
│   └── architecture.md          # Decision framework, patterns
├── hooks/
│   └── scripts/
│       ├── session-init.py      # Context routing on start
│       └── guardrail.py         # PreToolUse enforcement
├── commands/                    # Custom /commands (skills)
│   ├── account-prep.md
│   ├── deal-strategy.md
│   ├── email-draft.md
│   ├── post-meeting.md
│   └── demo-prep.md
├── projects/
│   └── [your-project]/
│       └── memory/              # Auto-populated by Claude
│           ├── MEMORY.md        # Index (auto-loaded)
│           └── *.md             # Topic files
└── crons/                       # Optional: overnight intelligence
    └── gather/
        └── channel-roster.md    # Slack channels to monitor
```

## Customization

### For your role
Edit `CLAUDE.md` — replace the placeholder sections with YOUR:
- Role and title
- Current projects
- Key constraints (org-specific, compliance, etc.)
- Routing table (what wiki pages to load for what tasks)

### For your OU
The Slack channel roster in `crons/gather/channel-roster.md` has placeholder channels. Replace with your OU's channels.

### For your domain
Skills are templates. Edit them to match YOUR workflows, YOUR CRM fields, YOUR customer segments.

## How It Works (The Compound Loop)

```
Mistake → Correction → Memory File → Rule → Hook → Prevention
                                                        ↓
                                            That error class is gone forever
```

Every correction you make gets saved. Repeated mistakes become rules. Ignored rules become enforcement hooks. The system develops immunity to its own failure modes.

## FAQ

**Do I need to be a developer?**
No. Tell Claude what you want enforced, what workflow to automate, what mistake to prevent. Claude writes the hooks, skills, and rules. Your job is direction and domain expertise.

**Will this overwrite my existing Claude config?**
No. The setup script checks for existing files and skips them. You can also run it in dry-run mode first.

**How much does this cost?**
Nothing beyond your existing Claude Code subscription. No external services required. Crons are optional and use the same Claude session.

**Can I share my setup with my team?**
Yes — that's how this kit was created. Once your system matures, you can export your rules and skills for others.

## Origin

This architecture was built over 60 days by John Tehrani (Principal Solutions Engineer, TMT) starting from a blank Claude Code install. The full story: [From Memory to Operating System](https://jtehrani84.github.io/claude-context-architecture/from-memory-to-operating-system.html)

## Questions?

- **Slack:** #solutions-ai-tooling
- **Author:** John Tehrani (jtehrani@salesforce.com)
