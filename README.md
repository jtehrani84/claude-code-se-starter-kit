# Claude Code SE Starter Kit

**Day 5 with compound loops activated.**

This kit gives you the persistent context architecture that took 60 days of trial-and-error to build. Clone it, run setup, and the system starts compounding from session one. Every correction you make becomes permanent. Every mistake develops an immune response.

## What You Get

| Layer | What | Impact |
|-------|------|--------|
| **Identity** | Template CLAUDE.md with routing table | Claude knows your role, projects, and constraints from session 1 |
| **Rules** | 3 governance files (voice, security, architecture) | Standards enforced automatically — no re-explaining |
| **Hooks** | 4 scripts (session-init, guardrail, product-verification, output-quality-gate) | Context routes itself; mistakes get blocked or flagged |
| **Skills** | 11 SE-specific workflows | From meeting prep to content quality to meta-skills |
| **Wiki** | Starter knowledge base with entity pages | Architecture decisions, people, reference docs — all organized |
| **Crons** | Intelligence automation pipeline | Overnight Exa + HN scanning -> morning digest |
| **Examples** | Compound loop walkthrough | See exactly how one mistake becomes a permanent fix |

## Prerequisites (Do These FIRST)

**You MUST have Claude Code installed and working via LLMGW before installing this kit.**

1. **If you were on Embark/Vertex AI** — run the cleanup script first:
   ```bash
   curl -fsSL https://sf-claude-cleanup-8969fb1c0934.herokuapp.com/install.sh | bash
   ```
   Quit and reopen Terminal after cleanup.

2. **Install Claude Code via LLMGW** (if not already done):
   ```bash
   curl -fsSL https://plugins.codegen.salesforceresearch.ai/claude/install.sh | bash
   ```
   Complete the Google SSO login. Quit and reopen Terminal.

3. **Verify Claude Code works:**
   ```bash
   mkdir -p ~/claude-projects && cd ~/claude-projects && claude
   ```
   You should see the Claude Code welcome banner. Type "hello" and confirm you get a response. Exit with `/exit`.

4. **THEN install this starter kit** (below).

> **Why this order matters:** The LLMGW installer writes your auth key to `~/.claude/settings.json`. This kit adds hooks and rules to that same directory. If you install the kit first, everything still works — but if you accidentally overwrite `settings.json` with the reference file from this kit, your auth key is erased and Claude Code shows "not logged in." If that happens, re-run the LLMGW installer (step 2) to restore your auth.

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
4. Install hooks, rules, and skills
5. Set up the wiki structure
6. Optionally configure crons for overnight intelligence

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
- Product verification hook catches hallucinated Salesforce names

### Week 2-3: Growth
- Memory files accumulate from corrections and decisions
- Wiki grows as Claude writes reference pages from your work
- Skills save 30+ minutes of instruction per use
- Morning brief arrives if you enable crons
- Use `/skillify` to extract new workflows from sessions

### Week 4+: Compound Effects
- Output quality gate catches the last 1% of slip-throughs
- Entity graph connects related knowledge automatically
- `/validate` provides cross-check before shipping content
- The system builds itself from here

## What Each Skill Does

| Skill | Purpose |
|-------|---------|
| `/account-prep` | Pre-meeting intelligence: company snapshot, relationship history, their priorities, your angle |
| `/deal-strategy` | Competitive positioning, objection handling, talk tracks for active opportunities |
| `/email-draft` | Customer email with anti-slop enforcement and 70/30 customer-centric structure |
| `/post-meeting` | Capture outcomes, action items, CRM updates, and schedule next steps |
| `/demo-prep` | Demo script tailored to the prospect's industry, pain points, and persona |
| `/system-health` | Infrastructure and configuration health check across your Claude setup |
| `/skillify` | Meta-skill: extract any repeatable workflow from the current session into a new command |
| `/validate` | Cross-model quality gate: scores content 1-10 on 5 dimensions, verdicts SHIP/FIX/REWRITE |
| `/voice-check` | Anti-slop scanner: finds all 50+ banned words/phrases with line numbers and replacements |
| `/content-review` | 6-dimension reviewer: accuracy, voice, specificity, customer focus, actionability, credibility |
| `/weekly-report` | Status report from git log, memory files, and session activity |
| `/morning-brief` | Daily context load: overnight intel, yesterday's work, today's focus, suggested actions |
| `/gas-deploy` | Apps Script deploy: push + deploy + verify, prevents the clasp push-only gotcha |

## Hooks (4 Scripts)

| Hook | Type | What It Does |
|------|------|-------------|
| `session-init.py` | SessionStart | Routes context based on working directory and git branch |
| `guardrail.py` | PreToolUse (Bash) | Blocks dangerous commands: force-push, --set-env-vars, rm -rf, secrets |
| `product-verification.py` | PreToolUse (Edit/Write) | Flags hallucinated Salesforce product names before they reach output |
| `output-quality-gate.py` | PostToolUse (Write) | Scans written content for AI-slop words and reports violations |

## The Compound Loop

```
Mistake --> Correction --> Memory File --> Rule --> Hook --> Prevention
                                                             |
                                                  That error class is gone forever
```

See `examples/compound-loop/` for a complete walkthrough showing one real correction evolving from memory to rule to hook enforcement.

## Directory Structure

```
~/.claude/
|-- CLAUDE.md                        # Your identity + routing table (from template)
|-- settings.json                    # Hook config, permissions, env vars (from settings.json.example)
|-- rules/                           # Always-loaded governance
|   |-- communication.md             # Voice standards, anti-slop, banned words
|   |-- security-governance.md       # CRUD/FLS, sharing, secrets
|   +-- architecture.md              # Decision framework, patterns
|-- hooks/
|   +-- scripts/
|       |-- session-init.py          # Context routing on start
|       |-- guardrail.py             # PreToolUse: block dangerous commands
|       |-- product-verification.py  # PreToolUse: catch hallucinated product names
|       +-- output-quality-gate.py   # PostToolUse: scan for AI-slop in written files
|-- commands/                        # Custom /commands (skills)
|   |-- account-prep.md
|   |-- deal-strategy.md
|   |-- email-draft.md
|   |-- post-meeting.md
|   |-- demo-prep.md
|   |-- system-health.md
|   |-- skillify.md
|   |-- validate.md
|   |-- voice-check.md
|   |-- content-review.md
|   |-- weekly-report.md
|   +-- morning-brief.md
|-- projects/
|   +-- [your-project]/
|       +-- memory/                  # Auto-populated by Claude
|           |-- MEMORY.md            # Index (auto-loaded)
|           +-- *.md                 # Topic files
+-- wiki/
    |-- index.md                     # Wiki entry point
    +-- people/                      # Entity pages
        |-- _template-internal.md    # Colleague template
        |-- _template-external.md    # Customer/partner template
        +-- [name].md                # Individual profiles

crons/                               # Optional: overnight intelligence
|-- manage.sh                        # Install/uninstall/status/test
|-- gather/
|   |-- exa-scan.py                  # Web intelligence via Exa API
|   |-- hn-scan.py                   # Developer sentiment via HN Algolia
|   +-- channel-roster.md            # Slack channels to monitor
|-- synthesize/
|   +-- morning-digest.sh           # Claude synthesizes raw -> wiki/inbox.md
|-- plists/
|   +-- com.claude.gather.exa.plist  # macOS launchd schedule (4:30 AM)
+-- raw/                             # Raw gather output (date-stamped)
```

## Google Apps Script

The kit includes a full Apps Script setup for automating Google Workspace. See `docs/apps-script-setup.md` for the complete guide.

**Starter templates** in `templates/apps-script/`:

| Template | What It Does |
|----------|-------------|
| `slides-from-sheet.gs` | Reads Sheet rows, generates a Slides deck with one slide per row |
| `sheet-data-puller.gs` | HTTP endpoint that returns Sheet data as JSON — connect to Claude or middleware |
| `email-merge.gs` | Sends personalized emails from a Sheet of contacts with merge fields |

**Skill:** `/gas-deploy` wraps the push + deploy + verify workflow so you never hit the "clasp push doesn't update the web app" trap.

## Configuration

Copy `settings.json.example` to `~/.claude/settings.json` and customize:
- Hook paths and matcher patterns
- Permission allowlists (reduce permission prompts)
- Environment variables
- Model selection

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

### Entity pages
Start with 3-5 key people (your manager, your top customer, your cross-functional partner). The wiki grows from there. See `wiki/people/README.md`.

## How It Works

Every correction you make gets saved as a memory file. Repeated corrections become rules (auto-loaded every session). Critical rules become hooks (mechanically enforced). The system develops immunity to its own failure modes.

After 30 days, a typical setup has:
- 40-60 memory files (corrections, decisions, preferences)
- 8-12 rules (governance, voice, domain constraints)
- 4-6 hooks (hard enforcement of critical patterns)
- 10-15 skills (workflow automation)
- 20-30 entity pages (people knowledge)

That's ~100 persistent context items working silently in every session.

## FAQ

**Do I need to be a developer?**
No. Tell Claude what you want enforced, what workflow to automate, what mistake to prevent. Claude writes the hooks, skills, and rules. Your job is direction and domain expertise.

**Will this overwrite my existing Claude config?**
No. The setup script checks for existing files and skips them. You can also run it in dry-run mode first.

**How much does this cost?**
Nothing beyond your existing Claude Code subscription. No external services required. Crons are optional (Exa API has a free tier; HN Algolia is free).

**Can I share my setup with my team?**
Yes — that's how this kit was created. Once your system matures, you can export your rules and skills for others. Use `/skillify` to package workflows.

**What's the difference between a rule and a hook?**
Rules are instructions Claude reads at session start. They're soft — they can be forgotten in very long conversations. Hooks are code that runs mechanically before or after tool calls. They can't be forgotten because they execute outside the model's context.

## Recommended Plugins

These extend the base kit significantly. Install from Claude Code marketplace:

| Plugin | What It Does | Install |
|--------|-------------|---------|
| **context-mode** | 98% context compression, FTS5 search — extends long sessions massively | `/context-mode:ctx-upgrade` |
| **hookify** | Generate hooks from conversation patterns — "never do X again" becomes code | Marketplace → hookify |
| **session-report** | End-of-session summary with token usage and work done | Marketplace → session-report |

## SE Grounding Service

Verified Salesforce product knowledge — 3,200+ FCD chunks with slide citations, competitive intel, field SE insights, and a 323-entity knowledge graph. One source of truth for every SE.

**URL:** `https://grounding.35-186-235-101.sslip.io`
**Setup guide:** `https://grounding.35-186-235-101.sslip.io/setup`

### Browser Access (any SE)

1. Connect to ZScaler VPN
2. Go to `https://grounding.35-186-235-101.sslip.io`
3. Click "Sign in with Google"
4. Use your `@salesforce.com` Google Workspace account
5. Search — results include FCD slide citations

No approval needed, no API key, no setup. Non-salesforce.com accounts are rejected.

### Claude Code MCP (SEs running Claude Code)

1. ZScaler must be on
2. Add to `~/.claude/.mcp.json` (create if it doesn't exist):
```json
{
  "mcpServers": {
    "salesforce-grounding": {
      "type": "url",
      "url": "https://grounding.35-186-235-101.sslip.io/mcp"
    }
  }
}
```
Or run: `claude mcp add --transport http salesforce-grounding https://grounding.35-186-235-101.sslip.io/mcp`

3. Restart Claude Code — you'll be prompted to approve on first use
4. MCP tools are available:

| Tool | What it does |
|------|-------------|
| `grounding_search` | Semantic search over verified FCD corpus |
| `grounding_search_narrowed` | Graph-narrowed search (filter by product/competitor entities) |
| `kg_lookup` | Find entities by name or type |
| `kg_traverse` | Follow relationships through the knowledge graph |
| `kg_related_chunks` | Get chunks linked to an entity |
| `product_clouds` | List available product clouds with counts |
| `corpus_stats` | Corpus and KG statistics |

The MCP endpoint uses ZScaler as the network gate — no additional auth token needed.

### REST API

1. ZScaler on
2. Sign in via browser (get session cookie) or call from authenticated context
3. Endpoints:
   - `POST /api/v1/search` — semantic vector search
   - `POST /api/v1/search/entity-narrowed` — graph-narrowed search
   - `POST /api/v1/search/bm25` — keyword fallback
   - `GET /api/v1/kg/entities?q=&type=` — entity search
   - `GET /api/v1/kg/traverse?from=&depth=` — graph traversal
   - `GET /api/v1/search/stats` — corpus statistics

### What's in the corpus

- **20 FY27 First Call Decks** — Agentforce, Data 360, Commerce, MuleSoft, Tableau, Slack, Revenue, Sales, Service, Marketing, Platform, Headless 360
- **Competitive intel** — positioning, objection handling, where we win/lose
- **Field SE insights** — what's working, pricing/packaging Q&A, gotchas
- **Customer stories** — proof points with metrics
- **Knowledge graph** — 323 entities with relationships (has_feature, competes_with, in_industry, strong_product_fit)

---

## Recommended MCP Servers

Add these to `~/.claude/.mcp.json` under `mcpServers`:

| Server | What It Does | Setup |
|--------|-------------|-------|
| **salesforce-grounding** | Verified FCD product knowledge, competitive intel, KG | ZScaler only — see above |
| **salesforce-docs** | Official Trailhead, dev guides, release notes, help articles | No auth — [details](https://labs.agentforce.com/docs/salesforce-docs-mcp) |
| **GitHub** | PR creation, code search, issue management | `gh auth login` then add to settings |
| **Exa** | Real-time web intelligence (powers /scan-intel crons) | Get API key at exa.ai |
| **Context7** | Current documentation lookup for any framework | Free, no auth needed |

## Origin

This architecture was built over 60 days by John Tehrani (Principal Solutions Engineer, TMT) starting from a blank Claude Code install. The full story: [From Memory to Operating System](https://jtehrani84.github.io/claude-context-architecture/from-memory-to-operating-system.html)

## Questions?

- **Slack:** #solutions-ai-tooling
- **Author:** John Tehrani (jtehrani@salesforce.com)
