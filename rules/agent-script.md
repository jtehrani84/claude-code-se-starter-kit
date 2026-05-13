# Agent Script Rules (Verified May 2026)

## File Structure
- ONE file per agent. All topics, variables, config, system, start_agent in a SINGLE `.agent` file.
- Bundle directory: `aiAuthoringBundles/Agent_Name/Agent_Name.agent` + `Agent_Name.bundle-meta.xml`
- Use 4-space indentation (not tabs — server rejects tabs despite what some docs say)
- Boolean capitalization: `True`/`False` (not `true`/`false`)

## The Two-Level Action Pattern (CRITICAL)

Every topic has TWO blocks for actions:

```yaml
topic my_topic:
    # LEVEL 1: Define actions (sibling of reasoning:)
    actions:
        my_action:
            description: "What it does"
            inputs:
                param1: string
                param2: string
            outputs:
                result: string
                success: boolean
            target: "flow://My_Flow_Api_Name"

    # LEVEL 2: Reference as LLM tools (inside reasoning:)
    reasoning:
        actions:
            my_tool: @actions.my_action
                with param1 = ...
                with param2 = ...
        instructions: ->
            | Use the tool when needed.
```

## What WILL NOT Compile (Don't Try These)

- `action_name: flow://FlowName` directly in reasoning.actions (unexpected `://`)
- `target: apex://Class` inside reasoning.actions (wrong location)
- Top-level `actions:` block outside any topic (server ignores it)
- Actions without `with` clauses for every input (missing required input error)
- Reserved field name `model` in inputs (rename to `llmModel`)

## Target Syntax

Targets MUST be quoted strings:
- `target: "flow://Flow_Api_Name"` — Flow-backed (use for actions that have Agent Action flows)
- `target: "apex://ApexClassName"` — Direct Apex (use for actions without flows)
- `target: "prompt://TemplateName"` — Prompt Template
- `target: "retriever://IndexName"` — Data Cloud Search Index

## Input/Output Names Must Match the Flow/Apex

The output field names in your `.agent` file must EXACTLY match what the Flow exposes (not what the Apex class returns). Flows often rename outputs:
- Apex `financialSummary` → Flow exposes as `financialDataJson`
- Apex `newsSummary` → Flow exposes as `newsJson`
- Apex `filingSummary` → Flow exposes as `filingsJson`

If publish fails with "property X was not found in available list [Y, Z]" — use the names from the available list.

## CLI Workflow

```bash
# Validate (server-side compilation)
sf agent validate authoring-bundle --api-name My_Agent --target-org myorg

# Publish (creates live agent in org)
sf agent publish authoring-bundle --api-name My_Agent --target-org myorg --skip-retrieve

# Preview (test conversations)
sf agent preview --api-name My_Agent --target-org myorg
```

## Prerequisites

- sf CLI version 2.133.4+ (older versions 404 on Agent Script APIs)
- Permissions: `AgentPlatformBuilder` + `CopilotSalesforceAdmin` assigned to your user
- For publish: `Modify All Data` + `Manage AI Agents`
- OAuth scopes: `chatbot_api`, `sfap_api`, `web` (re-auth if CLI was recently updated)

## Employee vs Service Agent

- Employee Agent: `agent_type: "AgentforceEmployeeAgent"` — runs as logged-in user, no `default_agent_user`
- Service Agent: needs `default_agent_user` — runs as a specific agent user

## Use the Salesforce Docs MCP

When stuck on syntax, search the live docs:
```
mcp__salesforce-docs__salesforce_docs_search("Agent Script action target syntax")
```
This finds patterns that don't exist in any model's training data.
