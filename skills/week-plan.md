Weekly planning command. Reviews open deals, recent intelligence, project status, and creates a prioritized plan for the week.

Run this Monday morning after `/morning-brief`.

## Step 1: Gather Data (run ALL in parallel)

### 1. Opportunities Closing This Month
```bash
sf data query --query "SELECT Account.Name, Name, StageName, Amount, CloseDate FROM Opportunity WHERE IsClosed = false AND CloseDate = THIS_MONTH ORDER BY CloseDate ASC" --target-org [YOUR-TARGET-ORG] --json
```

### 2. Opportunities Closing Next 30 Days
```bash
sf data query --query "SELECT Account.Name, Name, StageName, Amount, CloseDate FROM Opportunity WHERE IsClosed = false AND CloseDate = NEXT_N_DAYS:30 ORDER BY Amount DESC LIMIT 10" --target-org [YOUR-TARGET-ORG] --json
```

### 3. Overdue Tasks
```bash
sf data query --query "SELECT Subject, Account.Name, ActivityDate FROM Task WHERE OwnerId = '[USER_ID]' AND Status != 'Completed' AND ActivityDate < TODAY ORDER BY ActivityDate ASC" --target-org [YOUR-TARGET-ORG] --json
```

### 4. Git Activity (last 7 days across all projects)
```bash
cd ~/Claude-Demo-Apps && git log --all --oneline --since="7 days ago" --author="[YOUR-GIT-USER]" 2>/dev/null | head -20
```

### 5. Recent Intelligence Digests — Pull ADOPT NOW Items
```bash
ls -la ~/[YOUR-PROJECT]/intel-digests/ | tail -5
```
Read the most recent digest file(s) from the past 7 days.

**Critical:** Extract ALL items from the `## ADOPT NOW` section that have unresolved action items. Cross-reference against the action plan — if an ADOPT NOW item already has a corresponding action plan entry (marked with `Source: /scan-intel`), skip it. If it's new, surface it as a candidate P1 or P2 item in the week plan.

Also check for time-sensitive deadline memories:
```bash
ls ~/.claude/projects/[YOUR-PROJECT-PATH]/memory/deadline-*.md 2>/dev/null
```
Read any deadline memory files and surface approaching deadlines (< 30 days out) as P0 or P1 items.

### 6. Service Health (if applicable)
```bash
curl -s https://[YOUR-SERVICE-URL]/health 2>/dev/null | python3 -m json.tool 2>/dev/null || echo "Service: unreachable"
```

### 7. Wiki Recent Changes
```bash
cd ~/[YOUR-PROJECT]/wiki && git log --oneline --since="7 days ago" 2>/dev/null | head -10
```

## Step 2: Analyze & Prioritize

### Priority Framework
- **P0 (TODAY):** Deals closing this week, overdue tasks, broken infrastructure
- **P1 (THIS WEEK):** Deals closing this month needing prep, scheduled meetings, active project milestones
- **P2 (THIS WEEK IF TIME):** Intelligence follow-ups, wiki maintenance, project enhancements
- **P3 (BACKLOG):** Nice-to-haves, research, future project planning

### For Each Open Deal
- Does this need a `/deal-strategy` run?
- Is there a meeting scheduled? Need `/account-prep`?
- Is the close date realistic or should it be pushed?
- What's the single most important action to advance this deal?

## Step 3: Output

```
====================================
  WEEK PLAN — Week of [date]
====================================

DEAL PIPELINE SNAPSHOT
  Closing this month: [count] deals, $[total]
  Nearest close: [account] — [date] — [stage]
  Largest open: [account] — $[amount] — [stage]

P0 — DO TODAY
  [ ] [Action] — [account/project] — [why urgent]
  [ ] [Action] — [account/project] — [why urgent]

P1 — THIS WEEK
  [ ] [Action] — [account/project] — [context]
  [ ] [Action] — [account/project] — [context]
  [ ] [Action] — [account/project] — [context]

P2 — IF TIME
  [ ] [Action] — [context]
  [ ] [Action] — [context]

P3 — BACKLOG
  - [Item]
  - [Item]

INFRASTRUCTURE STATUS
  Services: [status]
  Last deploy: [date/rev]
  SA key: [days until expiration]

INTELLIGENCE HIGHLIGHTS (from /scan-intel ADOPT NOW)
  [Unresolved ADOPT NOW items from recent digests]
  [Approaching deadlines from deadline-*.md memories]

PROJECT STATUS
  [Active projects with current phase/milestone]
====================================
```

Save to `~/[YOUR-PROJECT]/week-plans/[YYYY-MM-DD].md`
Create the directory if it doesn't exist.

## Step 4: Write Nudge Timestamp

```bash
echo "YYYY-MM-DDTHH:MM:SS" > ~/.claude/projects/[YOUR-PROJECT-PATH]/memory/.last-week-plan
```
