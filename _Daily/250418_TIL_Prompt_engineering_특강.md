# 250418 TIL - Prompt engineering  (Friday)

**Area**: [[_Index_of_2a_Prompt-Engineering|2a_Prompt-Engineering]] (ID: A_y5jkryoi)



# Seminar
- Prompt engineering

- 
- solar prompt cook book
![[Pasted image 20250416191150.png]]![[Pasted image 20250416191223.png]]![[Pasted image 20250416191230.png]]![[Pasted image 20250416191249.png]]강수진 박사


![[Pasted image 20250416191304.png]]


![[Pasted image 20250416191314.png]]


![[Pasted image 20250416191359.png]]![[Pasted image 20250416191420.png]]


![[Pasted image 20250416191435.png]]


- tuning
- zero
- few
- cot

3. function call, RAG
LangGraph - prompt optimization


![[Pasted image 20250416191457.png]]


![[Pasted image 20250416191525.png]]
]]![[Pasted image 20250416191726.png]]


- structured output
- hierarchical 
- turn construction unit
- consistency 조절
	- fact check
- 효율화
	- semantic condensation
		- 두 줄을 한 줄로 대체


![[Pasted image 20250416192205.png]]![[Pasted image 20250416192402.png]]![[Pasted image 20250416192647.png]]![[Pasted image 20250416192940.png]]![[Pasted image 20250416193030.png]]

- n-gram viewer
	- 사용 빈도 더 높은 단어 -> 내용 더 디테일
	- 
- 프롬프트 다 제작한 뒤, 
	- 토큰 줄여가며 고도화 할 경우 이 것 적용
	- 

- 메타 프롬프트
	- 프롬프트 마저 LLM 이 생성하게 유도
		- 단, 도메인 특화의 경우, 커스텀 추천

# 1. Hallucination 
## Clarity & Consistency


![[Pasted image 20250416193356.png]]

![[Pasted image 20250416193633.png]]

- model, size, task 마다 천차만별인 prompt 통일하려면?
	- sentence type 에 집중
		- 청유문 등
		- 
보통, closed ended form 평서문으로 씀 (restricted)

- open-ended form 이 더 outperform

- chain of functional prompts

![[Pasted image 20250416193819.png]]![[Pasted image 20250416194014.png]]![[Pasted image 20250416194104.png]]

![[Pasted image 20250416194209.png]]


hallucination 극복 방법
- 사실, 의견 구분
- 생각, 결론 구분


![[Pasted image 20250416194403.png]]

- verification plan 하고 자기 검증하게

# 2. LLM 성능 극대화 prompt engineering

![[Pasted image 20250416194613.png]]


- 모델을 생각하게
	- 인문학적 사고 필요
![[Pasted image 20250416194633.png]]

![[Pasted image 20250416194716.png]]

![[Pasted image 20250416194752.png]]![[Pasted image 20250416194851.png]]![[Pasted image 20250416194900.png]]![[Pasted image 20250416194936.png]]
# 3. Trends: MCP, Lazy Prompt


- 비추론 모델, prompt heavy 할 수밖에 없으나,
	- 추론 모델에서는 lazy prompt 간단하게 쓰는게 좋을 수도
	- 그러나 advanced tech?
![[Pasted image 20250416195111.png]]![[Pasted image 20250416195234.png]]


- MCP
	- orchestrate 하는 prompt

![[Pasted image 20250416195802.png]]


![[Pasted image 20250416195822.png]]

## Q&A

prompt 요소의 배치 순서 (role, persona, instruction, context /few-shot, output format 등) 도 결과에 영향을 미치는것 같았는데, rule of thumb 이 있을까요? (중요한 정보를 처음/끝에 놓는다든지)

- model size 커질수록
	- 지시문, 맥락 순
- 소형일 수록
	- 맥락 먼저, 지시문 끝에 나오는게

  

- 구분자 delimiter 중요

  

구조화된 프롬프트 설정시, XML, markdown, 또는 []같은 기호로 감싸는 방식 등 구분자 사용은 적당히 일관성 있게만 사용하면 될까요?

또는 사용 예에 따른 요령이 있을까요?

(few-shot context 는 <>, Instruction 등은 markdown )

  
  

- 타겟 /출력 텍스트 언어가 한국어인 경우에도, 모든 프롬프트를 영어로 구성하는게 좋을까요? 예전에 비해 요즘 모델 (gemma3 같은) 은 한국어도 잘 이해하는것 같긴 한데, 그럼에도 영어 기반으로 모든 걸 처리하고 번역하게 하는 방식이 안전할까요? 
- No: 한국어 써야하는 모델도 있음
- 한국어 잘 이해한다 해도, 토큰 절약을 위해 영어로
- 코드 스위칭

- 언어 번갈아가면서
- 안나오는 용어는 한국어 사용
- 번역해서 사용: 생각보다 비추

번역, LLM 에 맡기지는 않음 (도움은 받고)



solar prompt cook book

## Metadata
- **Created Date**: 2025-04-18
- **Category**: TIL
- **ID**: N_y5k6113n



## Area Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File"
FROM ""
WHERE category = "TIL" AND context_id = "A_y5jkryoi" AND file.name != "250418_TIL_Prompt_engineering_"
SORT date DESC
LIMIT 5
```

## Recent Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File"
FROM ""
WHERE context_id = "A_y5jkryoi" AND file.name != "250418_TIL_Prompt_engineering_"
SORT date DESC
LIMIT 5
```
