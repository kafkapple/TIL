# Projct

## test_llm (emotion + a)

- chat task 추가 구현
    - 유저 인풋 1회 만으로 혼자 주거니 받거니 생성하는 문제
        - 해결하려다 emotion task json parsing 깨지는 문제.
- emotion task
    - json parsing 오류
    - chat

## nlp_task_sum

- 기존 nlp task test baseline 모듈 코드에
    - solar 추가
    - llama bllossom 추가 등
- 오류 수정

# Study

## LLM Token param

- `generation.top_p`: 누적 확률 기반 상위 토큰 선택 (0.9는 90% 확률의 토큰을 사용).
- `generation.top_k`: 상위 K개 토큰만 선택 (10으로 제한).

## Categorical val →  one-hot encoding

**중요 정보 중 unique 값이 적고 순서 정보가 없는 경우**, 일반적으로 **one-hot encoding**이 적합

---

### 1. **Unique 값이 적음**

- Unique 값(카테고리)이 적다면, one-hot encoding의 결과로 생성되는 벡터의 차원 수가 적어져 메모리 사용량이 상대적으로 효율적입니다.
- 예: `['A', 'B', 'C']`라는 3개의 카테고리가 있다면, 각 값은 `[1, 0, 0]`, `[0, 1, 0]`, `[0, 0, 1]`로 표현됩니다.

---

### 2. **순서 정보가 없음**

- 순서가 없는 카테고리 데이터를 숫자로 직접 매핑하면 모델이 **잘못된 순서 관계**를 학습할 수 있습니다. 예를 들어, `{'A': 0, 'B': 1, 'C': 2}`로 매핑하면 모델은 B가 A보다 크고 C는 B보다 더 크다고 해석할 수 있습니다.
- One-hot encoding은 각 카테고리를 독립적으로 표현하기 때문에 순서 정보를 전달하지 않습니다.

---

### 3. **대체 옵션: Target encoding / Ordinal encoding**

- 만약 카테고리 개수가 많거나 데이터셋이 매우 클 경우, one-hot encoding이 메모리와 연산 효율성을 저하시킬 수 있습니다. 이 경우 다른 방법도 고려할 수 있습니다:
    - **Target encoding**: 각 카테고리를 종속 변수(target) 값의 평균으로 매핑합니다. (e.g., 범주가 100개 이상인 경우 추천)
    - **Ordinal encoding**: 카테고리를 고유한 숫자로 매핑하되, **순서가 없는 데이터에 적합하지 않습니다**.