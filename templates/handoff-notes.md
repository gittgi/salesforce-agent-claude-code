# 인계 메모

## 입력 파일

- 시나리오 JSON: `test-results/<session-id>/scenario.json`
- 시나리오 리뷰: `test-results/<session-id>/scenario-review.md`
- 컨텍스트 요약: `test-results/<session-id>/context-summary.md`

## Apex 단위 테스트 에이전트에게

- `scenario.json`의 `scenarios[*].unitTestNotes`를 우선 사용한다.
- 각 시나리오의 공통 `given`, `when`, `then`, `expectedResult`를 Apex test method 구조로 변환한다.
- `requiredTestData`를 기반으로 테스트 데이터를 만든다.
- `requiresStartStopTest`가 true이면 `Test.startTest()` / `Test.stopTest()`를 포함한다.
- `requiresBulkCoverage`가 true이면 251건 이상 대량 처리 path를 고려한다.
- 이 인계 단계에서는 사용자 승인이 없는 한 Apex test class를 작성하거나 수정하지 않는다.

## E2E 검증 에이전트에게

- `scenario.json`의 `scenarios[*].e2eValidationNotes`를 우선 사용한다.
- `requiresOrgDataMutation`이 true인 시나리오는 실행 전 사용자 승인을 요구한다.
- 테스트 데이터는 `TEST_AGENT_` prefix를 사용한다.
- 생성한 record는 반드시 정리 대상 목록에 기록한다.
- 검증 후 실제 결과, 관찰값, 정리 작업 결과를 별도 검증 산출물에 기록한다.

## 공통 주의사항

- `assumptions`와 `unknowns`를 사실처럼 취급하지 않는다.
- 불확실한 기대 결과는 실행 전 사용자 확인을 받는다.
- Production org에서는 실행하지 않는다.
- Salesforce 작업은 Salesforce DX MCP를 우선 사용하고, 필요한 경우 read-only `sf` CLI 대체 경로를 사용한다.
