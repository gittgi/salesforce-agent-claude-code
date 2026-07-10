# Salesforce Agent Claude Code

Claude Code agent definitions for a Salesforce testing workflow.

This repository is being built around four cooperating agents. The first two are currently defined under `.claude/agents/`; the remaining agents are planned next.

## Agents

| Agent | Status | Responsibility |
| --- | --- | --- |
| `salesforce-test-scenario-agent` | Defined | Understand changed or explicitly selected Salesforce code and produce shared test scenarios. |
| `salesforce-apex-unit-test-agent` | Defined | Reuse, create, or update Apex test code from approved scenarios, deploy test-only metadata, run Apex tests, and report results. |
| `salesforce-e2e-validation-agent` | Planned | Validate approved scenarios against a real non-production org through UI/API/SOQL observations and cleanup. |
| `salesforce-test-orchestration-agent` | Planned | Coordinate the other agents, enforce approvals, collect artifacts, and decide the next step. |

## Orchestration Flow

```text
User request
  |
  v
Orchestration Agent
  |
  |-- 1. Scenario Agent
  |      - Resolve target code or diff
  |      - Inspect relevant Salesforce source and org context
  |      - Write scenario artifacts
  |      - Wait for scenario approval
  |
  |-- 2. Apex Unit Test Agent
  |      - Read approved scenario.json
  |      - Reuse or update existing *_Test.cls where possible
  |      - Create new *_Test.cls only when needed
  |      - Deploy test-only metadata
  |      - Run Apex tests with coverage
  |      - Write unit-test artifacts or fix requests
  |
  |-- 3. E2E Validation Agent
  |      - Read the same approved scenario.json independently
  |      - Create approved test data only in non-production orgs
  |      - Execute org-level validation steps
  |      - Capture observations and cleanup records
  |
  v
Orchestration Agent
  |
  |-- Combine scenario, unit-test, and E2E results
  |-- Route production-code or metadata issues as fix requests
  |-- Ask for user approval before each gated stage
  v
Final report
```

## Artifact Contract

All generated outputs should live under:

```text
test-results/<session-id>/
```

The scenario agent writes:

- `scenario.json`
- `scenario-review.md`
- `context-summary.md`
- `handoff-notes.md`

The Apex unit test agent writes:

- `unit-test-result.json`
- `unit-test-report.md`
- `fix-requests.json` when needed
- `generated-test-diff.patch` when useful

The future E2E validation agent is expected to write:

- `e2e-validation-result.json`
- `e2e-validation-report.md`
- `cleanup-manifest.json`
- optional evidence files

## Approval Gates

The orchestration agent should enforce three gates:

1. Scenario approval
2. Apex test code creation/modification approval
3. E2E validation and org data mutation approval

No agent should skip its gate.

## Runtime Policy

- Use Salesforce DX MCP first.
- Use Salesforce `sf` CLI v2 only as fallback.
- Use only the `salesforce_dx` MCP server by default.
- Do not modify production Apex from test agents.
- Do not run against Production orgs.
- Keep E2E validation independent from Apex unit test execution; the orchestration agent coordinates both.

## Current Files

- `.claude/agents/salesforce-test-scenario-agent.md`
- `.claude/agents/salesforce-apex-unit-test-agent.md`
- `schemas/scenario.schema.json`
- `schemas/unit-test-result.schema.json`
- `templates/`
- `examples/`
