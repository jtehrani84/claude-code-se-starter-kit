# /content-review

Universal 6-dimension content reviewer. Works on any document type.

## Trigger
When the user says: "review this", "content review", "is this good?", "critique this", "review [file]"

## Workflow

### 1. Identify the content
Read the file or use the provided text. Note the content type (email, deck, brief, doc, proposal).

### 2. Score across 6 dimensions

Rate each dimension 1-10. For each, explain what would make it a 10 and what's currently holding it back.

---

**Dimension 1: Accuracy (Weight: Critical)**
- Are all factual claims verifiable?
- Product names correct and current?
- Numbers sourced? Dates accurate?
- Any fabricated references, quotes, or case studies?
- Red flag: anything stated with confidence that can't be verified

**Dimension 2: Voice (Weight: High)**
- Does it sound like a human SE wrote it, or like AI generated it?
- Scan for banned words and phrases (full anti-slop list)
- Mixed sentence lengths? Contractions used naturally?
- Direct and opinionated, or hedging and corporate?
- Red flag: three or more AI-slop words in one document

**Dimension 3: Specificity (Weight: High)**
- Numbers over adjectives? ("saved 14 hours/week" vs "significant time savings")
- Named examples over generic claims?
- Specific tools, features, or capabilities named?
- Concrete timelines and milestones?
- Red flag: paragraphs with zero specific data points

**Dimension 4: Customer Centricity (Weight: High)**
- Leads with their world, their metrics, their challenges?
- 70/30 ratio (their priorities vs Salesforce)?
- References their KPIs, not ours?
- Shows understanding of their specific situation?
- Red flag: first paragraph is about Salesforce, not about them

**Dimension 5: Actionability (Weight: Medium)**
- Clear next step stated?
- Specific owner, date, or mechanism for the action?
- Reader knows exactly what to do after reading?
- Not just informational — drives a decision or motion?
- Red flag: ends with "let me know if you have questions"

**Dimension 6: Credibility (Weight: Medium)**
- Would a C-suite exec take this seriously?
- Demonstrates expertise, not just awareness?
- Appropriate tone for the audience seniority?
- No overstatements, superlatives, or claims that stretch trust?
- Red flag: promises results without evidence

### 3. Produce the review

```
## Content Review

**Document:** [name/type]
**Audience:** [inferred or stated]
**Word count:** [X]

### Scores

| Dimension | Score | What Would Make It a 10 |
|-----------|-------|------------------------|
| Accuracy | X/10 | [one sentence] |
| Voice | X/10 | [one sentence] |
| Specificity | X/10 | [one sentence] |
| Customer Centricity | X/10 | [one sentence] |
| Actionability | X/10 | [one sentence] |
| Credibility | X/10 | [one sentence] |

**Overall: X/10**

### What's Working
- [2-3 specific things done well — quote the actual text]

### What Needs Work
- [Prioritized list of fixes, most impactful first]
- [Include the specific text that needs changing]
- [Suggest the rewrite for each fix]

### Verdict: [SHIP / NEEDS EDITING / REWRITE]
```

### 4. Fix offer
If NEEDS EDITING or REWRITE, offer to make the changes. Apply fixes in priority order.

## Verdict Thresholds
- SHIP: Average 8+, no dimension below 6, no Critical (Accuracy) below 8
- NEEDS EDITING: Average 6-7, or one dimension below 5
- REWRITE: Average below 6, or Accuracy below 5, or Voice below 4

## Rules
- Be honest. "This is great" without specifics is useless. Quote what's working.
- Be constructive. "This is bad" without a fix is useless. Show the rewrite.
- Accuracy is non-negotiable. One hallucinated fact = review fails regardless of other scores.
- Match feedback to content type: an internal memo has different standards than a customer email.
- Don't over-index on formatting — substance beats structure.
