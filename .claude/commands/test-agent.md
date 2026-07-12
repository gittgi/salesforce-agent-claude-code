# 테스트 에이전트

MCP/CLI 우선 오케스트레이션으로 Salesforce 테스트 에이전트 MVP를 실행한다.

## 지시사항

1. Read `CLAUDE.md`.
2. Read `docs/MCP_CLI_FIRST_RUNBOOK.md`.
3. Use Salesforce DX MCP tools first.
4. Use `sf` CLI fallback when MCP does not expose the needed operation.
5. Do not use `salesforce-*` private skills.
6. Do not use the Python executor unless the user explicitly asks.
7. Enforce the three approval gates.
8. Write outputs under `test-results/<session-id>/`.
9. 사용자-facing Markdown 리포트, 승인 요청, 요약, workbook/CSV 표시 문구, JSON 설명 문자열은 한국어로 작성한다.
10. schema key, 파일명, 경로, Apex/API 식별자, SOQL, CLI 명령, metadata 이름, record ID, schema enum 값은 원문을 유지한다.
