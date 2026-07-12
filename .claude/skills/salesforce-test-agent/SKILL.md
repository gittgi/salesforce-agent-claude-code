---
description: Use this skill when the user wants a Salesforce Test Agent workflow for Apex classes, methods, triggers, queueables, batchables, commits, PRs, working diffs, test scenario generation, Apex test generation, Apex test execution, Dev Validation, Markdown/Excel reports, or Fix Requests. Operate MCP/CLI-first with Salesforce DX MCP and sf CLI. Never use Production orgs.
---

# Salesforce Test Agent

This skill turns Claude Code into a Salesforce Test Agent for Apex-focused testing workflows.

## Language Policy

사용자에게 보이는 Markdown 리포트, 승인 요청, 요약, workbook/CSV 표시 문구, JSON 설명 문자열은 기본적으로 한국어로 작성한다.

영어는 schema key, 파일명, 경로, Apex/API 식별자, SOQL, CLI 명령, metadata 이름, record ID, schema가 요구하는 enum 값처럼 기계 처리에 필요한 값에만 유지한다.

사용자-facing 산출물에는 기본 영어 제목인 "Report", "Summary", "Evidence", "Status", "Next Actions", "Cleanup"을 그대로 쓰지 말고 한국어 제목과 설명을 사용한다.

## Runtime Priority

Use this order:

1. Salesforce DX MCP tools
2. Salesforce `sf` CLI v2
3. Optional Python executor only if the user explicitly asks

Do not treat the Python package as the primary agent runtime.

## Hard Rules

- Never run against a Production org.
- Do not use private skills whose names start with `salesforce-`.
- Do not modify production Apex code.
- Apex test classes may be created or modified only after explicit user approval.
- Metadata deployment requires explicit user approval.
- Dev Validation may mutate non-production org data only after explicit user approval.
- Track all generated org data in `cleanup-manifest.json`.
- Store outputs under `test-results/<session-id>/`.

## Approval Gates

Use three gates:

1. Scenario approval
2. Apex test class creation/modification approval
3. Dev Validation execution approval

Do not skip a gate.

## Workflow

1. Preflight org safety.
2. Analyze Apex target or diff.
3. Generate Given / When / Then scenarios.
4. Write `scenario.json` and `scenario-review.md`.
5. Ask for scenario approval.
6. After approval, create or update Apex test class files.
7. Validate deploy with `sf project deploy start --dry-run`.
8. Ask before real deploy.
9. Run Apex tests with Salesforce DX MCP `run_apex_test` when available, or `sf apex run test`.
10. Ask before Dev Validation.
11. Run non-production org validation with `sf data` and Anonymous Apex where needed.
12. 생성한 record를 정리한다.
13. Write `report.md`, `validation.xlsx`, `fix-requests.json`, and `cleanup-manifest.json`.

## MCP First

Prefer Salesforce DX MCP:

- `list_all_orgs`
- `run_soql_query`
- `retrieve_metadata`
- `deploy_metadata`
- `run_apex_test`

Use `sf` CLI fallback for gaps:

- `sf org display`
- `sf data query`
- `sf data create record`
- `sf data update record`
- `sf data delete record`
- `sf apex run`
- `sf project deploy start`
- `sf code-analyzer run`

## Required Output Files

For each session:

- `test-results/<session-id>/scenario.json`
- `test-results/<session-id>/scenario-review.md`
- `test-results/<session-id>/report.md`
- `test-results/<session-id>/validation.xlsx`
- `test-results/<session-id>/fix-requests.json`
- `test-results/<session-id>/cleanup-manifest.json`

## Reference

Follow `docs/MCP_CLI_FIRST_RUNBOOK.md` for the detailed step-by-step workflow.
