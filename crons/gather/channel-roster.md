# Slack Channel Intelligence Roster

Configure which Slack channels to monitor for overnight intelligence gathering.
Replace placeholder channel IDs with your OU's actual channels.

## How This Works

The morning synthesis script (`claude -p`) reads these channels via the Slack MCP
and produces a categorized digest. You need to have authenticated Slack in at least
one interactive Claude Code session first (the OAuth token caches).

## Channel Categories

### Competitive Intelligence
| Channel | ID | What to Extract |
|---------|-----|----------------|
| #[your-OU]-solutions | [YOUR_ID] | CI drops, competitor announcements |
| #analyst-coverage | [YOUR_ID] | IDC/ISG/Gartner reports, market share |
| [your-OU]-competitive | [YOUR_ID] | OU-specific competitive intel |

### AI & Tooling
| Channel | ID | What to Extract |
|---------|-----|----------------|
| #ai-club | [YOUR_ID] | Internal AI experiments, techniques |
| #ai-engineering-productivity | [YOUR_ID] | AI dev tools, productivity hacks |
| #solutions-ai-tooling | [YOUR_ID] | SE-specific AI tooling |
| #pop-ai | [YOUR_ID] | AI product updates |

### Territory & Leadership
| Channel | ID | What to Extract |
|---------|-----|----------------|
| [your-OU]-everyone | [YOUR_ID] | OU announcements, priorities |
| [your-OU]-solutions | [YOUR_ID] | SE team updates |
| #broadcast-solutions | [YOUR_ID] | Solutions org-wide announcements |
| #broadcast-us | [YOUR_ID] | US-wide Salesforce announcements |

### Product & Platform
| Channel | ID | What to Extract |
|---------|-----|----------------|
| #all-technology | [YOUR_ID] | Product launches, updates |
| #all-salesforce | [YOUR_ID] | Company-wide announcements |
| [product-specific] | [YOUR_ID] | Product you demo most |

### Industry
| Channel | ID | What to Extract |
|---------|-----|----------------|
| [your-industry] | [YOUR_ID] | Vertical news, use cases |

## Setup Instructions

1. Find your channel IDs: Open Slack, right-click channel name → "Copy link" → ID is the last segment
2. Replace [YOUR_ID] placeholders above with real IDs
3. Remove channels you don't care about
4. Add channels specific to your OU/vertical

## Synthesis Categories

The morning digest groups findings into:
- **Salesforce Product** — what shipped, what's GA, deprecations
- **Competitive Intel** — competitor moves, analyst reports
- **Territory Mentions** — your accounts or OU mentioned
- **AI/Tooling** — internal tools and techniques
- **Industry Trends** — vertical-specific signals
- **Leadership** — priorities, metric changes, enablement
