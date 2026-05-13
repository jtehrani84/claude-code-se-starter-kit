Scan for the latest AI, Claude Code, and Salesforce developments. This is a daily intelligence sweep combining X feed + Exa search.

## Source 1: X "For You" Feed (authenticated)

Pull your authenticated X timeline using the feed fetcher script (if configured):

```bash
python3 ~/.claude/hooks/scripts/x-feed-fetcher.py > /tmp/x-feed-today.json
```

This returns up to 40 tweets from the "For You" algorithm. Parse the JSON and filter for tweets relevant to:
- Claude Code, Anthropic, Claude API
- AI agents, MCP, agent frameworks
- Salesforce, Agentforce, Data Cloud
- Developer productivity, coding tools
- Crypto/DeFi agents (secondary interest)

Ignore: politics, general news, spam, low-engagement promotional content.

## Source 2: Exa Search (topic-based)

Run 4-5 Exa searches in parallel using curl:

```
curl -s "https://api.exa.ai/search" \
  -H "x-api-key: [YOUR-EXA-API-KEY]" \
  -H "Content-Type: application/json" \
  -d '{"query": "QUERY_HERE", "type": "neural", "numResults": 15, "startPublishedDate": "LAST_7_DAYS", "contents": {"text": {"maxCharacters": 500}}}'
```

### Search Queries:
1. "Claude Code new features hooks MCP servers skills workflows"
2. "Anthropic Claude announcements releases updates"
3. "Agentforce Salesforce AI agent updates features"
4. "AI agent development patterns tools productivity"
5. "MCP Model Context Protocol servers integrations"
6. "Salesforce Agent Script DSL agentforce hybrid reasoning deterministic"

Set `startPublishedDate` to 7 days ago from today.

## For Each Finding, Report:
1. **Source** — X feed or Exa (with @handle or URL)
2. **Title/Summary** — what was found
3. **Why it matters** — specifically for your role, your accounts, or your technical setup
4. **Action item** (if any):
   - New skill to create
   - CLAUDE.md update needed
   - Configuration change (hooks, MCP, commands)
   - New pattern to adopt

## Categorize Findings:
- **ADOPT NOW** — Immediately useful, implement today
- **EVALUATE** — Interesting, needs investigation
- **WATCH** — Good to know, not actionable yet

## Output:
Save results to `~/[YOUR-PROJECT]/intel-digests/YYYY-MM-DD.md` with the date of the scan.

If the intel-digests directory doesn't exist, create it.

After saving, print a summary of top 5 findings with action items.

## Auto-Wiki Ingest (for ADOPT NOW items only)

For each finding categorized as **ADOPT NOW**, automatically update the relevant wiki page:

1. **New tool/skill** → update `wiki/tools/claude-code-setup.md` or create a new page in `wiki/tools/`
2. **Anthropic/Claude update** → update `wiki/entities/anthropic.md`
3. **Salesforce/Agentforce update** → update `wiki/entities/salesforce.md`
4. **New pattern/concept** → update or create page in `wiki/concepts/`
5. **Project-relevant** → update the relevant page in `wiki/projects/`

For each wiki update:
- Add the new information to the relevant section
- Add a link to the source (URL or X handle)
- Update `wiki/log.md` with: `[DATE] Auto-ingested from /scan-intel: [brief description]`
- Update `wiki/index.md` if a new page was created

Do NOT auto-ingest EVALUATE or WATCH items — only ADOPT NOW.

## Auto-Append to Action Plan

After categorizing all findings, append ADOPT NOW action items to `wiki/inbox.md`:

1. Add each ADOPT NOW item with source link and suggested action
2. These will be reviewed during the next `/curate` or `/morning-brief` run

This ensures intel flows into the weekly planning workflow instead of sitting in a digest file.

## Save Time-Sensitive Memories

For any ADOPT NOW finding with a **deadline or expiration date** (model deprecations, key rotations, feature sunset dates, event dates):

1. Save a memory file to `~/.claude/projects/[YOUR-PROJECT-PATH]/memory/` with:
   - `type: project`
   - Name pattern: `deadline-[topic].md`
   - Content: what's happening, the date, and what action to take
   - Include **Why:** and **How to apply:** lines
2. Add to MEMORY.md index

This ensures future sessions get warned about approaching deadlines even if nobody reads the digest.

## Write Nudge Timestamp

```bash
echo "YYYY-MM-DDTHH:MM:SS" > ~/.claude/projects/[YOUR-PROJECT-PATH]/memory/.last-scan-intel
```
