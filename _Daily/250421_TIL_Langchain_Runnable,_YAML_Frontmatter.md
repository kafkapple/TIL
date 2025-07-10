# 250421 TIL - Langchain_Runnable, YAML Frontmatter (Monday)
**요약 개요:**
- Frontmatter는 마크다운 문서 최상단에 위치해 메타데이터를 정의하는 YAML 블록이며, Obsidian·Hugo·Jekyll 등 다양한 도구에서 문서 분류·태그·날짜 등을 지정할 때 사용합니다. 작성 시 `---` 구분, 콜론 뒤 공백, 네 칸 들여쓰기 등의 규칙을 준수해야 합니다.
- LangChain에서는 기존의 `LLMChain` 클래스가 1.0 버전에서 완전히 제거되고, 더 유연한 체이닝을 지원하는 `RunnableSequence` 또는 파이프 연산자(`|`) 방식이 공식 권장 방식이 되었습니다. 이 새 체인은 스트리밍·배치·비동기 처리를 기본으로 지원하며, 커스텀 함수 삽입과 디버깅이 용이합니다.
## Frontmatter YAML
### 1. 개념 및 역할
- **정의**: 원래 책 앞면의 제목·저작권·목차 등을 의미하던 Frontmatter를, 마크다운 문서에서 메타데이터 블록으로 차용한 것.
- **주 용도**:
    - 문서 분류(category), 태그(tags), 작성 날짜(date), 상태(status) 등 주요 속성 지정
    - Obsidian, Hugo, Jekyll, Gatsby 등 정적 사이트 생성기 및 노트 앱에서 활용
### 2. 작성 규칙
1. **문서 최상단**: 반드시 파일 제일 위에 위치
2. **`---` 구분**: 시작/종료 모두 세 개의 대시로 표시
3. **키: 값 쌍**: 콜론(`:`) 뒤 반드시 공백
4. **중첩 구조**: 들여쓰기 4칸 사용
```yaml
---
title: 내 문서 제목
tags: [기록, 정리]
date: 2025-04-22
categories:
    - 기술
    - 노트정리
---
```
## LangChain Runnable 체계적 요약
### 1. `LLMChain` 폐지 배경
- **단순 래퍼**에 불과했던 `LLMChain`은 프롬프트 + LLM 연동만 지원
- 확장성(스트리밍·배치·비동기·커스텀) 부족
- LangChain 1.0에서 완전 제거 예정
### 2. 공식 권장 체이닝 방식
- **파이프 연산자(`|`)**를 이용한 직관적 체인 연결
- **`RunnableSequence`** 클래스로 세부 제어 가능
```python
from langchain import PromptTemplate, OpenAI
from langchain_core.output_parsers import StrOutputParser
prompt = PromptTemplate(template="문장: {sentence}\n\n{language}로 번역:", input_variables=["sentence", "language"])
llm = OpenAI(temperature=0)
parser = StrOutputParser()
# 파이프 방식 체인
chain = prompt | llm | parser
result = chain.invoke({
    "sentence": "탁자 위에 고양이가 있어요",
    "language": "영어"
})
```
### 3. 주요 기능 비교
| 기능 | LLMChain (폐지) | RunnableSequence / `|` 방식 | |----------------|-----------------------|-----------------------------| | 체이닝 방식 | 클래스 기반 | 파이프 연산자 기반 | | 스트리밍 지원 | 제한적 | 완전 지원 | | 배치 처리 | 제한적 | `.batch()`, `.abatch()` 사용| | 비동기 처리 | 제한적 | `.ainvoke`, `.abatch()` 지원| | 조합 유연성 | 프롬프트+LLM 한정 | 프롬프트, LLM, 파서, 커스텀 함수| | 확장성 | 낮음 | 높음 |
### 4. 마이그레이션 예시
- **기존**:
    ```python
    chain = LLMChain(prompt=prompt, llm=llm)
    result = chain.predict(sentence="...", language="영어")
    ```
- **변경 후**:
    ```python
    chain = prompt | llm | parser
    result = chain.invoke({"sentence": "...", "language": "영어"})
    ```
### 5. 고급 사용 및 추가 팁
- **입력+출력 동시 보존**: `RunnablePassthrough().assign(...)`
    ```python
    outer_chain = RunnablePassthrough().assign(translated=prompt|llm|parser)
    result = outer_chain.invoke({...})
    # { "sentence": "...", "translated": "There is a cat on the table." }
    ```
- **커스텀 함수 삽입**:
    ```python
    from langchain_core.runnables import RunnableSequence, RunnableLambda
    chain = RunnableSequence(
        first=prompt,
        middle=[llm, RunnableLambda(lambda x: x.upper())],
        last=parser,
    )
    ```
- **배치/비동기**:
    - `chain.batch([inputs])`
    - `await chain.ainvoke(input)` / `await chain.abatch([inputs])`
### 6. 다음 단계 권장 사항
1. 모든 `LLMChain` 코드를 파이프 연산자(`|`) 또는 `RunnableSequence`로 교체
2. 실행 시 `invoke()`, `batch()`, `ainvoke()`, `abatch()` 활용
3. 공식 [LangChain 마이그레이션 가이드](https://python.langchain.com/docs/versions/migrating_chains/llm_chain/) 참고
---
이 요약을 바탕으로 Frontmatter 작성과 LangChain Runnable 체인 전환 작업을 빠르게 진행하실 수 있습니다. 추가적인 예제나 심화 가이드가 필요하시면 언제든 말씀해 주세요!
## Metadata
- **Created Date**: 2025-04-21
- **Category**: TIL
- **ID**: N_ifvpj6dw
## Same Category Notes
```dataview
TABLE date as "Date", context_name as "Context", file.name as "File"
FROM ""
WHERE category = "TIL" AND file.name != "250421_TIL_Langchain_Runnable,_YAML_Frontmatter"
SORT date DESC
LIMIT 5
```
## Recent Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File"
FROM ""
WHERE file.name != "250421_TIL_Langchain_Runnable,_YAML_Frontmatter"
SORT file.cday DESC
LIMIT 5
```