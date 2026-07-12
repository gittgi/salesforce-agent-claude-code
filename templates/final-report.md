# Salesforce 테스트 최종 리포트

## 요청 및 실행 모드

- 세션 ID: `<sessionId>`
- 실행 모드: `<runMode>`
- 전체 상태: `<overallStatus>`
- 대상 유형: `<target.type>`
- 대상 컴포넌트: `<target.component>`
- 진입점: `<target.entryPoint>`
- 소스 참조: `<target.sourceRef>`
- 시나리오 입력: `<target.scenarioInput>`

## 대상 Org 및 안전성 확인

- 확인 여부: `<orgSafety.checked>`
- 상태: `<orgSafety.status>`
- Org Alias: `<orgSafety.orgAlias>`
- Org 유형: `<orgSafety.orgType>`
- Sandbox 여부: `<orgSafety.isSandbox>`
- 운영 org 차단 여부: `<orgSafety.productionBlocked>`
- 상세:
  - `<orgSafety.details>`

## 승인 게이트 결과

| 게이트 | 필수 여부 | 상태 | 승인자 | 승인 시각 | 메모 |
| --- | --- | --- | --- | --- | --- |
| `<gate>` | `<required>` | `<status>` | `<approvedBy>` | `<approvedAt>` | `<notes>` |

## 단계별 결과

| 단계 | 에이전트 | 상태 | 요약 | 차단 사유 |
| --- | --- | --- | --- | --- |
| `<phase.name>` | `<phase.agent>` | `<phase.status>` | `<phase.summary>` | `<phase.blockingReasons>` |

## 시나리오 요약

- 시나리오 JSON: `<scenario.json path>`
- 시나리오 리뷰: `<scenario-review.md path>`
- 컨텍스트 요약: `<context-summary.md path>`
- 인계 메모: `<handoff-notes.md path>`
- 주요 시나리오:
  - `<scenario summary>`

## Apex 단위 테스트 결과

- 결과 JSON: `<unit-test-result.json path>`
- 리포트: `<unit-test-report.md path>`
- 테스트 실행 상태: `<unit-test-result.testRun.status>`
- 실행 테스트 수: `<unit-test-result.testRun.testsRan>`
- 통과 수: `<unit-test-result.testRun.passing>`
- 실패 수: `<unit-test-result.testRun.failing>`
- Coverage 요약:
  - `<coverage summary>`

## E2E 검증 결과

- 결과 JSON: `<e2e-validation-result.json path>`
- 리포트: `<e2e-validation-report.md path>`
- 실행 모드: `<e2e-validation-result.validationScope.executionMode>`
- 검증 상태:
  - `<scenario status summary>`
- 정리 작업 상태: `<e2e-validation-result.cleanup.status>`

## 증거 상태

- Workbook: `<e2e-validation-result.workbook.path>`
- Workbook 상태: `<e2e-validation-result.workbook.status>`
- CSV 대체 산출물 사용 여부: `<e2e-validation-result.workbook.fallback.used>`
- CSV 대체 산출물 디렉터리: `<e2e-validation-result.workbook.fallback.directory>`
- 증거:
  - `<evidence summary>`

## 통합 수정 요청 요약

| ID | 유형 | 대상 | 심각도 | 발생 단계 | 담당 | 상태 |
| --- | --- | --- | --- | --- | --- | --- |
| `<fixRequest.id>` | `<fixRequest.type>` | `<fixRequest.target>` | `<fixRequest.severity>` | `<fixRequest.sourcePhases>` | `<fixRequest.recommendedOwner>` | `<fixRequest.status>` |

## 전체 판정

- 상태: `<overallStatus>`
- 판단 근거:
  - `<decision reason>`

## 남은 리스크와 다음 단계

### 리스크

- `<risks>`

### 불확실한 점

- `<unknowns>`

### 다음 단계

- `<nextActions>`

## 산출물 목록

| 유형 | 경로 | 상태 | 생성 단계 |
| --- | --- | --- | --- |
| `<artifact.type>` | `<artifact.path>` | `<artifact.status>` | `<artifact.sourcePhase>` |
