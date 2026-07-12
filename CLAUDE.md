# Claude Code Instructions

This project is a Salesforce Test Agent MVP.

## Claude Code Assets

This project provides:

- Project skill: `.claude/skills/salesforce-test-agent/SKILL.md`
- Project subagent: `.claude/agents/salesforce-test-orchestration-agent.md`
- Optional slash command: `.claude/commands/test-agent.md`

Prefer the project skill/subagent flow when Claude Code supports it.

## Primary Runtime

Use Claude Code as the orchestrating agent.

The primary execution layer is:

1. Salesforce DX MCP tools
2. Salesforce `sf` CLI v2
3. Official Salesforce-oriented skills/instructions

For this project, use only the `salesforce_dx` MCP server by default. Do not use other configured MCP servers such as NotebookLM for the normal Salesforce agent workflow unless the user explicitly changes this policy.

For the Salesforce agent being built, include only the base Salesforce-oriented skills in its runtime design. Google `agents-cli` may be used as a local build/scaffold/reference tool while creating the agent, but do not bake Google `agents-cli` skills into the Salesforce agent itself. Do not use private `salesforce-*` skills unless the user explicitly changes this policy.

Do not treat the Python package as the primary agent runtime. It is an optional local executor/prototype only, available when the user explicitly asks for deterministic helper commands.

Do not build a multi-platform adapter layer for Codex and Claude Code. Keep definitions simple; if a Codex-tested draft must move to Claude Code later, translate the agent definition manually.

## Hard Rules

- Never run against a Production org.
- Use only the `salesforce_dx` MCP server for this project's default workflow.
- Use only base Salesforce-oriented skills inside the Salesforce agent being built.
- Do not introduce a Codex-to-Claude or multi-platform adapter abstraction.
- Do not use private skills whose names start with `salesforce-`.
- Google `agents-cli` is allowed as an external build/scaffold/reference tool, but must not be included as part of the built Salesforce agent's runtime skill set.
- Do not modify production Apex code.
- Apex test classes may be created or modified only after explicit user approval.
- Dev Validation may mutate non-production org data only after explicit user approval.
- All generated test data must use a `TEST_AGENT_` or scenario-specific test prefix and must be tracked in a cleanup manifest.
- Keep outputs under `test-results/<session-id>/`.

## Output Language Policy

- 사용자에게 보이는 Markdown 리포트, 승인 요청, 요약, workbook/CSV 표시 문구, JSON 설명 문자열은 한국어로 작성한다.
- 영어는 schema key, 파일명, 경로, Apex/API 식별자, SOQL, CLI 명령, metadata 이름, record ID, schema enum 값처럼 기계 처리에 필요한 값에만 유지한다.
- 사용자-facing 산출물에는 기본 영어 제목인 "Report", "Summary", "Evidence", "Status", "Next Actions", "Cleanup"을 그대로 쓰지 말고 한국어 제목과 설명을 사용한다.
- 최종 완료 전 `final-report.md`, `e2e-validation-report.md`, `unit-test-report.md`, `scenario-review.md`, workbook/CSV 대체 산출물, JSON의 사람이 읽는 설명 문자열을 점검해 영어 문장을 한국어로 정리한다.

## Approval Gates

Use three explicit gates:

1. Scenario approval
2. Apex test class creation/modification approval
3. Dev Validation execution approval

Do not skip a gate.

## MCP First

Prefer Salesforce DX MCP tools when available:

- `list_all_orgs` for available orgs
- `run_soql_query` for read-only SOQL
- `retrieve_metadata` for missing local Apex/metadata context
- `deploy_metadata` for targeted metadata deployment
- `run_apex_test` for Apex test execution

Use `sf` CLI fallback for gaps, especially:

- `sf org display`
- `sf data query`
- `sf data create record`
- `sf data update record`
- `sf data delete record`
- `sf apex run`
- `sf project deploy start`
- `sf code-analyzer run`

## Default Org Policy

The current local non-production test org is `lab-hub`.

Before mutating org metadata or data:

1. Confirm the org alias.
2. Query/check org type.
3. Block Production.
4. Confirm the relevant approval gate.

## Output Files

For each session, write:

- `scenario.json`
- `scenario-review.md`
- `report.md`
- `validation.xlsx`
- `fix-requests.json`
- `cleanup-manifest.json`

## Python Executor

The Python package in `salesforce_agent_framework/` exists only as an optional helper implementation.

Use it only when:

- the user explicitly asks to run the local executor, or
- you need to compare behavior against the prototype.

For normal Claude Code operation, use the `salesforce-test-agent` skill or the `salesforce-test-orchestration-agent` subagent and follow `docs/MCP_CLI_FIRST_RUNBOOK.md`.
