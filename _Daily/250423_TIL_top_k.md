# 250423 TIL - top k (Wednesday)

## GPT Playground에서 Top-p란?

**Top-p**(또는 _nucleus sampling_)는 GPT Playground에서 텍스트 생성 시 다양성과 예측 가능성을 조절하는 중요한 하이퍼파라미터입니다. 이 값은 모델이 다음 단어를 선택할 때, 확률 분포에서 누적 확률이 특정 임계값(p)에 도달할 때까지 상위 후보 단어만을 고려하는 방식을 의미합니다[1](https://wktj.tistory.com/164)[2](https://velog.io/@funda__mental_/GPT-Playground%EB%A1%9C-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%95%B4%EB%B3%B4%EA%B8%B0-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC)[6](https://www.jiniai.biz/2023/07/23/openai-chatgpt-playground-%EC%99%84%EC%A0%84-%EC%B4%88%EB%B3%B4%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%82%AC%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C/)[8](https://testmanager.tistory.com/425).

**동작 원리**

- 모델이 다음 단어를 예측할 때, 가능한 모든 후보 단어의 확률을 계산합니다.

- 확률이 높은 순서대로 누적 확률을 더해가면서, 누적 합이 Top-p 값(예: 0.9)에 도달할 때까지 후보군을 만듭니다.

- 이 후보군 내에서 무작위로 단어를 선택해 텍스트를 생성합니다[2](https://velog.io/@funda__mental_/GPT-Playground%EB%A1%9C-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%95%B4%EB%B3%B4%EA%B8%B0-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC)[6](https://www.jiniai.biz/2023/07/23/openai-chatgpt-playground-%EC%99%84%EC%A0%84-%EC%B4%88%EB%B3%B4%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%82%AC%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C/)[8](https://testmanager.tistory.com/425).

**Top-p 값에 따른 차이**

- **Top-p 값이 낮을 때(예: 0.3):**

- 상위 확률 단어만 선택됩니다.

- 텍스트가 더 예측 가능하고 일관성이 높지만, 다양성은 줄어듭니다.

- **Top-p 값이 높을 때(예: 0.9):**

- 더 많은 후보 단어가 선택지에 포함됩니다.

- 텍스트가 더 다양하고 창의적으로 생성되지만, 예측 가능성은 낮아집니다[1](https://wktj.tistory.com/164)[2](https://velog.io/@funda__mental_/GPT-Playground%EB%A1%9C-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%95%B4%EB%B3%B4%EA%B8%B0-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC)[3](https://wikidocs.net/195818)[6](https://www.jiniai.biz/2023/07/23/openai-chatgpt-playground-%EC%99%84%EC%A0%84-%EC%B4%88%EB%B3%B4%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%82%AC%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C/)[8](https://testmanager.tistory.com/425)[10](https://dusanbaek.tistory.com/101).

**비유와 예시**

- Top-p는 "상위 몇 %의 후보만 선택하겠다"는 확률 필터와 같습니다.

- 예를 들어, Top-p=0.9로 설정하면, 모델이 예측한 모든 단어 중 누적 확률이 90%에 포함되는 단어들만 후보로 삼아 그중에서 무작위로 선택합니다[2](https://velog.io/@funda__mental_/GPT-Playground%EB%A1%9C-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%ED%95%B4%EB%B3%B4%EA%B8%B0-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC)[8](https://testmanager.tistory.com/425).

**GPT Playground에서의 활용**

- Top-p는 Temperature(온도)와 함께 모델의 응답 다양성과 품질을 세밀하게 조절할 수 있는 도구입니다.

- 실험적으로 Top-p와 Temperature를 조정하며 원하는 스타일의 텍스트를 얻을 수 있습니다[1](https://wktj.tistory.com/164)[6](https://www.jiniai.biz/2023/07/23/openai-chatgpt-playground-%EC%99%84%EC%A0%84-%EC%B4%88%EB%B3%B4%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EC%82%AC%EC%9A%A9-%EA%B0%80%EC%9D%B4%EB%93%9C/)[7](https://knou4silver.tistory.com/211).

| Top-p 값 | 특징            | 예시 텍스트 스타일                                     |
| ------- | ------------- | ---------------------------------------------- |
| 0.3     | 예측 가능, 일관성 높음 | "식비 절약을 잘 하셨네요. 교통비도 계획적으로 관리해보세요."            |
| 0.9     | 다양성, 창의성 높음   | "이번 달 예산을 잘 지키셨네요! 특히 식비와 카페 비용에서 멋지게 절약하셨어요." |

- **Created Date**: 2025-04-23
- **Category**: TIL
- **ID**: N_6xbkl8io