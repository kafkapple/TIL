# 250612 TIL - 3_The Illusion of Thinking (Thursday)

**Project**: [[30_Projects/2506_Podcast AI/2506_Podcast AI|2506_Podcast AI]] (ID: P_civi38os)

AI 의 추론 능력, 진짜일까? 아니면 환상일까? - 최신 애플 논문 '사고의 환상 The Illusion of Thinking' 파헤치기


이번 에피소드에서는 최근 화제가 된 애플의 논문 "The Illusion of Thinking (사고의 환상)"을 중심으로, 요즘 AI, 특히 '생각하는 AI'라고 불리는 Large Reasoning Model (LRM)의 추론 능력 실체에 대해 이야기 나눕니다.

애플 연구진은 기존 수학/코딩 벤치마크의 한계를 넘어, 하노이 탑 같은 다양한 퍼즐 환경을 이용해 AI의 추론 과정을 세밀하게 분석했습니다.

놀라운 결과들이 있었는데요. AI의 추론 능력은 문제의 복잡성이 높아질수록 급격히 무너지는 '붕괴' 현상을 보였습니다. 또한, 문제 난이도에 따라 AI의 성능이 세 가지 구간으로 나뉘는 것을 발견했습니다. 아주 쉬운 문제에서는 오히려 일반 LLM이 더 잘하거나 비슷했고, 중간 난이도에서는 LRM이 강점을 보였지만, 복잡한 문제 앞에서는 둘 다 속수무책으로 실패했습니다.

더욱 흥미로운 점은, 어려운 문제일수록 AI가 '생각하는 노력' (생성하는 토큰 수)을 오히려 줄이는 반직관적인 모습을 보인다는 것입니다. 충분한 토큰 예산이 주어졌는데도 말이죠. 마치 문제 풀기를 포기하는 것처럼 보입니다. 심지어 문제 해결 알고리즘을 명시적으로 알려줘도 성능 향상이 제한적이었다는 사실은 현재 AI의 논리적 단계 실행 능력에 대한 의문을 던집니다.

과연 현재 AI의 추론은 인간의 '생각'과 같은 것일까요, 아니면 정교한 패턴 매칭의 '환상'일까요?

애플 논문이 제기하는 AI 추론 능력의 현재 한계와 앞으로의 과제에 대해 함께 이야기 나눠봐요!

  

참고 문헌:

- The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity (Apple Paper) - [⁠https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf⁠](https://www.google.com/url?sa=E&q=https%3A%2F%2Fml-site.cdn-apple.com%2Fpapers%2Fthe-illusion-of-thinking.pdf)
- On Apple's Illusion of Thinking (Hugging Face Community Article)
- The Illusion of Thinking: New Research Paper from Apple (noailabs on Medium)
- The illusion of "The Illusion of Thinking" (sean goedecke Article)
- [R] Apple Research: The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity (Reddit Thread on r/MachineLearning)
- [Paper by Apple] The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity (Reddit Thread on r/apple)


## Metadata
- **Created Date**: 2025-06-12
- **Category**: TIL
- **ID**: N_0x879x4i



## Project Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File"
FROM ""
WHERE category = "TIL" AND context_id = "P_civi38os" AND file.name != "250612_TIL_3_The_Illusion_of_Thinking"
SORT date DESC
LIMIT 5
```

## Recent Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File" 
FROM ""
WHERE context_id = "P_civi38os" AND file.name != "250612_TIL_3_The_Illusion_of_Thinking"
SORT date DESC
LIMIT 5
```
