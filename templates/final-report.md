# Salesforce Test Final Report

## 요청 및 실행 모드

- Session ID: `<sessionId>`
- Run Mode: `<runMode>`
- Overall Status: `<overallStatus>`
- Target Type: `<target.type>`
- Target Component: `<target.component>`
- Entry Point: `<target.entryPoint>`
- Source Ref: `<target.sourceRef>`
- Scenario Input: `<target.scenarioInput>`

## 대상 Org 및 안전성 확인

- Checked: `<orgSafety.checked>`
- Status: `<orgSafety.status>`
- Org Alias: `<orgSafety.orgAlias>`
- Org Type: `<orgSafety.orgType>`
- Is Sandbox: `<orgSafety.isSandbox>`
- Production Blocked: `<orgSafety.productionBlocked>`
- Details:
  - `<orgSafety.details>`

## 승인 게이트 결과

| Gate | Required | Status | Approved By | Approved At | Notes |
| --- | --- | --- | --- | --- | --- |
| `<gate>` | `<required>` | `<status>` | `<approvedBy>` | `<approvedAt>` | `<notes>` |

## 단계별 결과

| Phase | Agent | Status | Summary | Blocking Reasons |
| --- | --- | --- | --- | --- |
| `<phase.name>` | `<phase.agent>` | `<phase.status>` | `<phase.summary>` | `<phase.blockingReasons>` |

## 시나리오 요약

- Scenario JSON: `<scenario.json path>`
- Scenario Review: `<scenario-review.md path>`
- Context Summary: `<context-summary.md path>`
- Handoff Notes: `<handoff-notes.md path>`
- 주요 시나리오:
  - `<scenario summary>`

## Apex Unit Test 결과

- Result JSON: `<unit-test-result.json path>`
- Report: `<unit-test-report.md path>`
- Test Run Status: `<unit-test-result.testRun.status>`
- Tests Ran: `<unit-test-result.testRun.testsRan>`
- Passing: `<unit-test-result.testRun.passing>`
- Failing: `<unit-test-result.testRun.failing>`
- Coverage Summary:
  - `<coverage summary>`

## E2E Validation 결과

- Result JSON: `<e2e-validation-result.json path>`
- Report: `<e2e-validation-report.md path>`
- Execution Mode: `<e2e-validation-result.validationScope.executionMode>`
- Validation Status:
  - `<scenario status summary>`
- Cleanup Status: `<e2e-validation-result.cleanup.status>`

## Evidence 상태

- Workbook: `<e2e-validation-result.workbook.path>`
- Workbook Status: `<e2e-validation-result.workbook.status>`
- CSV Fallback Used: `<e2e-validation-result.workbook.fallback.used>`
- CSV Fallback Directory: `<e2e-validation-result.workbook.fallback.directory>`
- Evidence:
  - `<evidence summary>`

## 통합 Fix Request 요약

| ID | Type | Target | Severity | Source Phases | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `<fixRequest.id>` | `<fixRequest.type>` | `<fixRequest.target>` | `<fixRequest.severity>` | `<fixRequest.sourcePhases>` | `<fixRequest.recommendedOwner>` | `<fixRequest.status>` |

## 전체 판정

- Status: `<overallStatus>`
- Reason:
  - `<decision reason>`

## 남은 리스크와 다음 단계

### Risks

- `<risks>`

### Unknowns

- `<unknowns>`

### Next Actions

- `<nextActions>`

## Artifact Index

| Type | Path | Status | Source Phase |
| --- | --- | --- | --- |
| `<artifact.type>` | `<artifact.path>` | `<artifact.status>` | `<artifact.sourcePhase>` |
