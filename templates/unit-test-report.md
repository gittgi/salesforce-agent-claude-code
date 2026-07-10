# Apex Unit Test Report

## 입력 시나리오

- 세션 ID: `<sessionId>`
- Scenario JSON: `<scenarioInput.path>`
- Scenario approval: `<scenarioInput.approvalStatus>`
- Org Alias: `<orgAlias>`
- 대상: `<target.component>`
- Entry Point: `<target.entryPoint>`

## 생성 또는 수정한 테스트 파일

### Generated

- `<generatedFiles.path>`: `<generatedFiles.purpose>`

### Modified

- `<modifiedFiles.path>`: `<modifiedFiles.purpose>`

## 시나리오별 테스트 매핑

| Scenario | Status | Test Class | Test Methods | Notes |
| --- | --- | --- | --- | --- |
| `<scenarioId>` | `<status>` | `<testClass>` | `<testMethods>` | `<notes>` |

## 배포 검증 결과

- Attempted: `<deployment.attempted>`
- Status: `<deployment.status>`
- Method: `<deployment.method>`
- Job ID: `<deployment.jobId>`
- Details:
  - `<deployment.details>`

## Apex Test 실행 결과

- Attempted: `<testRun.attempted>`
- Status: `<testRun.status>`
- Test Run ID: `<testRun.testRunId>`
- Tests Ran: `<testRun.testsRan>`
- Passing: `<testRun.passing>`
- Failing: `<testRun.failing>`
- Skipped: `<testRun.skipped>`
- Duration Ms: `<testRun.durationMs>`

## Coverage 결과

| Name | Type | Coverage | Covered Lines | Uncovered Lines |
| --- | --- | --- | --- | --- |
| `<coverage.name>` | `<coverage.type>` | `<coverage.percentage>` | `<coverage.coveredLines>` | `<coverage.uncoveredLines>` |

## 실패 분석

| Class | Method | Classification | Message |
| --- | --- | --- | --- |
| `<failure.className>` | `<failure.methodName>` | `<failure.classification>` | `<failure.message>` |

## Fix Request 요약

| ID | Type | Target | Severity | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| `<fixRequest.id>` | `<fixRequest.type>` | `<fixRequest.target>` | `<fixRequest.severity>` | `<fixRequest.recommendedOwner>` | `<fixRequest.status>` |

## 남은 리스크와 다음 단계

### 가정

- `<assumptions>`

### 불확실한 점

- `<unknowns>`

### 다음 단계

- 실패가 없으면 E2E Validation Agent로 넘긴다.
- `fixRequests`가 있으면 Development/Fix Agent가 먼저 처리한다.
