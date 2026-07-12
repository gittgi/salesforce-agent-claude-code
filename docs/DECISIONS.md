# MVP Decisions

This document captures implementation decisions confirmed before coding.

## Interface

The final target runtime is Claude Code using Salesforce DX MCP tools and Salesforce `sf` CLI.

During MVP construction, author and smoke test the agents first as Codex custom agents under `.codex/agents/`. Translate the stabilized definitions to Claude Code manually when ready.

The user reviews outputs in terminal text, Markdown, and Excel-compatible files.

The Python package is an optional deterministic executor/prototype. It is not the primary agent runtime.

## Portability

Do not build a Codex-to-Claude or multi-platform adapter layer for this MVP.

Keep the workflow simple and define the agent behavior in plain instructions, runbooks, schemas, and session artifacts. If any Codex-tested draft needs to move to Claude Code later, translate the agent definitions manually instead of maintaining a shared adapter abstraction.

## Outputs

All generated artifacts are stored under `test-results/<session-id>/`.

Scenario agent artifacts:

- `scenario.json`
- `scenario-review.md`
- `context-summary.md`
- `handoff-notes.md`

Apex unit test agent artifacts:

- `unit-test-result.json`
- `unit-test-report.md`
- `fix-requests.json` when production code, metadata, or org configuration appears to be the root cause
- `generated-test-diff.patch` when useful for review

E2E validation agent artifacts:

- `e2e-validation-result.json`
- `e2e-validation-report.md`
- `validation-workbook.xlsx` when org data is created, updated, queried, or compared
- `workbook-fallback/*.csv` when Excel MCP is unavailable or workbook creation fails
- `cleanup-manifest.json`
- `fix-requests.json` when production code, metadata, permissions, automation, data setup, or org configuration appears to be the root cause
- `evidence/` when useful for SOQL, API, UI, log, or manual observation evidence

Future orchestration artifacts:

- `fix-requests.json`
- `report.md`
- `validation.xlsx`

## Approval Gates

The agent uses three explicit approval gates:

1. Scenario approval
2. Apex test class creation/modification approval
3. E2E validation and org data mutation approval

No execution step can skip its approval gate.

## Apex Code Boundary

The Test Agent can create or modify Apex test classes after approval.

The Test Agent must not modify production Apex code. When production code appears to be the issue, it emits a Fix Request for a separate Development Agent.

## Org Safety

Production orgs are always blocked.

Non-production orgs are allowed, including Developer Edition, scratch orgs, and sandboxes. Unknown non-sandbox orgs are treated as production-like unless explicitly classified as non-production in configuration.

E2E validation may mutate org data after approval. Test data must be tagged with a `TEST_AGENT_` or scenario-specific prefix when possible, and cleanup manifests must be written.

When E2E validation creates, updates, queries, or compares org data, the agent writes a before/after Excel workbook with scenario summary, before data, inserted test data, after data, diff, cleanup result, and evidence sheets.

If Excel MCP is unavailable or workbook creation fails, the agent writes equivalent CSV fallback files under `test-results/<session-id>/workbook-fallback/` and records the fallback details in `e2e-validation-result.json`.

## Skills

Private skills whose names start with `salesforce-` are excluded from this project unless the user explicitly changes the policy.

Google `agents-cli` is allowed as an external build, scaffold, and reference tool while creating the Salesforce agent.

Google `agents-cli` skills must not be included in the Salesforce agent's own runtime skill set.

The Salesforce agent's primary runtime instruction set uses only base Salesforce-oriented skills/instructions:

- `generating-apex-test`
- `running-apex-tests`
- `querying-soql`
- `debugging-apex-logs`
- `running-code-analyzer`
- `deploying-metadata`

Missing data-operation skill coverage is handled by Salesforce DX MCP when available and `sf data` CLI fallback otherwise.

## Execution Priority

Use this order:

1. Salesforce DX MCP tools
2. Salesforce `sf` CLI v2
3. Optional Python executor only on explicit request

The Python executor must not obscure that the intended agent is Claude Code itself.

## MCP Scope

The default MCP server for Salesforce operations is `salesforce_dx`.

The E2E validation agent may also use the `excel` MCP server for local workbook artifacts.

When the `excel` MCP server is unavailable, E2E validation falls back to local CSV artifacts instead of dropping before/after comparison evidence.

Other configured MCP servers, such as NotebookLM and internal utility runtimes, are not part of the default Salesforce agent workflow unless the user explicitly changes the policy.
