# 250423 TIL - Tools, Function call (Wednesday)

1초 동안 생각함

“Function calling”과 “tools”의 차이는 단순히 “커스텀 함수” 기능 여부를 넘어서, 확장성·보안·오케스트레이션 측면에서 완전히 다른 프레임워크라는 점입니다. 아래 한글로 정리합니다.

## 1. 함수 호출(function calling) 개념

- Chat Completions API의 옛 파라미터 `functions`로 제공되던 기능입니다.

- LLM이 응답으로 특정 함수 이름과 JSON 인수(payload)를 내보내면, 애플리케이션이 그 함수를 호출하여 결과를 돌려줍니다.

- **제한점**

1. 한 번의 응답에서 단일 함수만 호출 가능 citeturn0search6

2. 함수 메타데이터(name, description, JSON schema) 외에는 별도 확장성·발견성 제공 없음 citeturn0search0

3. 동시 호출, 비동기 처리, 권한 관리 등의 기능이 없고 수작업으로 결합해야 함

## 2. tools 프레임워크

- 최신 파라미터 `tools`로 대체된, 더 일반화·확장된 개념입니다 citeturn0search0.

- **함수 호출**(function calling)도 tools의 한 종류(tool type)에 불과하며, tools는 다음을 지원합니다:

1. **다양한 툴**: 순수 함수뿐 아니라 HTTP API, 코드 인터프리터, MCP 서버, 데이터베이스 쿼리 등 모든 외부 기능을 “툴”로 등록 가능 citeturn0search2

2. **병렬·연쇄 호출**: 한 응답 내에서 여러 툴을 동시에 혹은 순차적으로 호출 가능 citeturn0search1

3. **메타데이터 및 탐색성**: JSON 스키마, 상세 설명, 권한 정보 등을 포함해 런타임에 동적으로 툴을 검색·선택할 수 있음 citeturn0search11

4. **보안·감사**: 툴별 사용 승인 절차, 샌드박스, 호출 로그 등 운영 환경에서 필요한 제어 기능 내장 citeturn0search11

5. **스트리밍·비동기**: SSE(서버-센트 이벤트)나 stdio 스트리밍, 비동기 호출 워크플로우 지원 citeturn0search11

## 3. 함수 호출 vs. tools 비교표

|특징|함수 호출(function calling)|tools 프레임워크|
|---|---|---|
|등록 대상|함수 시그니처(name, schema)|함수·HTTP API·코드 실행기·MCP 서버 등 모든 툴|
|동시 호출|불가|가능 citeturn0search1|
|메타데이터|이름·설명·입출력 스키마|풍부한 JSON schema·권한·사용 설명|
|발견성|수동 관리|런타임 툴 탐색·자동 완성|
|보안·감사|없음|권한 승인·로그|
|스트리밍/비동기|불가|지원|

## 4. 결론

- “커스텀 함수 기능”은 tools의 기본 사례이지만, tools는 그 위에 **병렬성**, **확장성**, **보안**, **메타데이터 기반 탐색/오케스트레이션** 등의 중요한 기능을 추가한 **상위 개념**입니다.

- 따라서 function calling은 tools의 한 부분일 뿐이며, modern agent 워크플로우에서는 반드시 tools 프레임워크를 활용하는 것이 바람직합니다.

- **Created Date**: 2025-04-23
- **Category**: TIL
- **ID**: N_5p1i79ki