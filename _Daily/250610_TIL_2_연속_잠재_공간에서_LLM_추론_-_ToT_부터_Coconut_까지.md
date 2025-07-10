# 250610 TIL - 2_연속 잠재 공간에서 LLM 추론 - ToT 부터 Coconut 까지 (Tuesday)
**Project**: [[30_Projects/2506_Podcast AI/2506_Podcast AI|2506_Podcast AI]] (ID: P_civi38os)
2
언어모델, 진짜 뇌처럼 생각할까? 연속 잠재 공간에서 LLM 추론 - ToT 부터 Coconut 까지
이번 에피소드에서는 대규모 언어 모델(LLM)이 복잡한 문제를 해결하는 방식의 진화에 대해 이야기 나눕니다.
기존 LLM은 복잡한 추론 문제에 답하기 위해 '생각의 사슬(Chain-of-Thought, CoT)' 방식을 사용해왔습니다. 이 방식은 문제를 해결하기 위한 일련의 중간 추론 단계를 자연어 형태로 생성함으로써 LLM의 추론 능력을 크게 향상시켰습니다. 마치 사람이 문제를 풀 때 단계별로 생각하는 과정을 보여주는 것과 같습니다. 이러한 단계별 사고 과정은 특히 산술, 상식, 상징적 추론 등 다양한 문제에서 효과적임이 입증되었습니다. CoT 프롬프트는 몇 가지 시연 예시를 제공하는 간단한 방법만으로도 상당한 성능 향상을 가져왔습니다.
하지만 CoT는 기본적으로 선형적인 추론 경로를 따라가기 때문에, 문제 해결에 탐색이나 계획이 필요한 경우 한계를 보였습니다. 잘못된 초기 결정이 전체 추론 과정을 망가뜨릴 수 있고, 다양한 대안을 탐색하기 어렵다는 단점이 있었습니다.
이러한 CoT의 한계를 극복하기 위해 등장한 것이 '생각의 나무(Tree-of-Thought, ToT)' 프레임워크입니다. ToT는 인간이 문제를 해결할 때 여러 가능성을 탐색하고 시행착오를 겪는 과정에서 영감을 받았습니다. ToT는 추론 과정을 '생각(thought)'이라는 단위로 분해하고, 각 단계에서 여러 가능한 다음 '생각'들을 생성합니다. 이러한 '생각'들은 단순히 토큰의 나열이 아니라 문제 해결의 중간 단계 역할을 하는 유의미한 단위입니다. ToT는 생성된 다양한 '생각'들을 평가하여 어떤 경로가 문제 해결에 더 유망한지 판단하고, 이를 바탕으로 너비 우선 탐색(BFS)이나 깊이 우선 탐색(DFS)과 같은 탐색 알고리즘을 활용하여 가장 유망한 추론 경로를 체계적으로 탐색합니다. 필요하다면 이전 단계로 되돌아가 다른 경로를 탐색(backtracking)할 수도 있습니다. 이러한 방식으로 ToT는 CoT보다 훨씬 넓은 문제 공간을 탐색하며 복잡한 문제에 대한 해결 성공률을 높입니다. 특히 게임 플레이나 창의적 글쓰기처럼 탐색이나 계획이 필수적인 문제에서 ToT의 효과가 두드러집니다.ToT의 성능을 더욱 향상시키기 위한 연구들도 진행되고 있습니다. 예를 들어, 생성된 '생각'의 유효성을 검증하는 전담 에이전트('Thought Validator')를 도입하여 잘못된 추론 경로를 걸러내거나, 강화 학습(RL)과 퍼즐 게임을 활용하여 LLM이 ToT 전략을 자체적으로 학습하도록 훈련하기도 합니다.
더 나아가, 최근에는 자연어 형태의 '생각'을 넘어 LLM의 내부 연속적인 잠재 공간에서 직접 추론을 수행하는 'Chain of Continuous Thought(Coconut)'와 같은 새로운 패러다임도 제안되었습니다. 이는 언어 표현에 얽매이지 않고 보다 효율적이고 유연한 추론을 가능하게 할 잠재력을 보여줍니다.
결론적으로, LLM의 추론 능력은 단순한 단계별 나열(CoT)에서 여러 가능성을 탐색하고 평가하는 나무 구조(ToT)로 발전하고 있으며, 더 나아가 언어의 제약을 벗어난 잠재 공간에서의 추론까지 탐구되고 있습니다. 이러한 발전은 LLM이 더욱 복잡하고 실제적인 문제를 해결하는 데 중요한 역할을 할 것으로 기대됩니다.
참고 문헌
- Training Large Language Models to Reason in a Continuous Latent Space [⁠⁠https://arxiv.org/abs/2412.06769⁠](https://arxiv.org/abs/2412.06769)
- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.pdf
- Improving LLM Reasoning with Multi-Agent Tree-of-Thought Validator Agent.pdf
- Large Language Model Guided Tree-of-Thought.pdf
- ToTRL_ Unlock LLM Tree-of-Thoughts Reasoning Potential through Puzzles Solving.pdf
- Tree of Thoughts_ Deliberate Problem Solving with Large Language Models.pdf
## Metadata
- **Created Date**: 2025-06-10
- **Category**: TIL
- **ID**: N_00jzb48e
## Project Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File"
FROM ""
WHERE category = "TIL" AND context_id = "P_civi38os" AND file.name != "250610_TIL_2_연속_잠재_공간에서_LLM_추론_-_ToT_부터_Coconut_까지"
SORT date DESC
LIMIT 5
```
## Recent Notes
```dataview
TABLE date as "Date", category as "Category", file.name as "File" 
FROM ""
WHERE context_id = "P_civi38os" AND file.name != "250610_TIL_2_연속_잠재_공간에서_LLM_추론_-_ToT_부터_Coconut_까지"
SORT date DESC
LIMIT 5
```