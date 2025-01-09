# 구현

## Project Emotion

- Audio (ravdess small / wav2vec)
- image (fer2013 / efficientNet)

→ data augmenation, split, class weighted sampler, focal loss 적용해 metric 성능 증가 

## Project NLP Summarization

- Model
    - bart
    - T5
    - llama

→ 기본적인 rouge metric 계열, model 별 finetuning 옵션 추가 및 학습 metric 개선 확인.

- label 로 text input 전체가 아니라, summary 정답값 사용해 개선

# 공부

## ML High-Low level 정리

- 데이터→ 수치화
    - 비정형 데이터의 경우 매우 중요, 어렵

### High-level

- blackbox 이해법: 용도에 집중
    - 무엇이 들어가고, 무엇이 나오는가?
    - 내부 동작 원리 이해는 포기.
        - 딥러닝, 내부 원리 모르는 경우 많아 합리적 방향

### Low-level

- 모델 저수준까지 이해
    - 모델 구조 바꿔 성능 향상
    - 더 효율적 구현

## Regression 선형 회귀 모델링 실습

- 종속 변수: 연속형 변수

### Sklearn

```

# 합성 데이터 생성
X, y = make_blobs()
X, y = make_circles()

# Data split
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=random_state)

# Model fit
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Prediction
score = model.score(X_test, y_test)
probs = model.predict_proba(X_test)[:, 1] # 모델 예측 확률값
```

- Linear regression (LR)
    - MSE loss function 으로 최적화

### Numpy 이용, linear equation 풀기 (analytic solution)

- LR MSE 의 경우, Analytic solution 존재
    - Ax=b

$$
\theta = \left( X^T X \right)^{-1} X^T y
$$

```
# 위의 식을 일반적인 linear equation인 Ax=b 형태로 변형
A = train_data.T @ train_data
b = train_data.T @ train_target

# @는 가독성과 코드 간결성을 위해 추천. np.matmual(train_data.T, train_data) 도 가능.

# numpy를 활용해 linear equation 풀기
coef = np.linalg.solve(A, b)

# 학습된 parameter를 이용해 예측
train_data @ coef
```

## Classification 분류 문제 모델링 실습

- 종속변수: categorical var

### Logistic Regression (LR)

- 데이터가 **범주1(True)에 속할 확률**을 0에서 1사이 값으로 예측
    - 그 확률값이 정해진 한계값(Threshold)보다 큰지 작은지에 따라 해당 샘플이 둘중 어느 범주에 속하는지 분류

```jsx
prediction = (probs > 0.5).astype(int)

# probs는 확률(probabilities)을 담고 있는 NumPy 배열이라고 가정
# probs > 0.5는 probs의 각 요소가 0.5보다 큰지 여부를 확인하는 조건문
# 결과는 Boolean 배열로 반환 예: [True, False, True, ...].
```

### Decision tree

- 원리
    - 트리의 각 노드에는 특정 기준에 따라 데이터를 이진분류
    - 입력 샘플이 여러 노드를 거쳐 최종적으로 리프 노드 (트리의 끝)에 도달하면, 최종적인 예측값이 결정
- "불순도"
    - 한 노드에 서로 다른 범주의 데이터가 얼마나 섞여 있는지를 나타내는 지표
        - 데이터를 분할하는 기준을 결정
            - 낮을수록 해당 노드의 데이터는 한 범주에 속함.
- 불순도 측정
    - 지니 불순도(Gini impurity)
    - 엔트로피(Entropy)
- 해석력(interpretability)
    - 모델의 판단기준을 사람이 해석 가능한 정도
    - 트리 구조를 직접 확인, 데이터가 어떤 기준으로 분류되었는지 직관적으로 이해 가능

### SVM

- 데이터들과 거리가 가장 먼 초평면(hyperplane)을 **결정경계**로 선택
    - 경계의 양쪽을 별개의 클래스로 분류
- support vector
    - 결정 경계에서 가장 가까운, 큰 영향 미친 가장 까다로운 데이터셋
    - 각 서포트 벡터 마다 margin 값 계산
- 주의
    - 선형의 결정경계를 사용해 주어진 데이터셋을 분류하므로, 데이터셋이 선형분리 가능(Linearly Separable)하지 않은 경우에는 사용이 불가

### **SVM: 선형분리가능성(Linear separability)과 커널트릭(Kernel Trick)**

- **커널 트릭(Kernel Trick) 사용, 비선형 결정경계 데이터 가능**
    - **커널 함수(Kernel Function)**
        - 데이터를 선형분리 가능한 고차원 공간으로 맵핑

## Dimension Reduction - PCA

- 중요
    - [ML Basic] (4-3) PCA를 이용한 차원축소와 시각화.ipynb

### : SVD (Singular Vector Decomposition)

- 행렬 M∈Rm×n를 다음과 같이 특별한 성질을 가진 3개의 행렬들의 곱으로 나타내는 과정
    - M=UΣVT.
- 3개의 행렬 U, Σ, V는 각각
    - U
        - m차원 정규 직교 행렬 (orthonormal matrix)
    - Σ(sigma)
        - singular value를 성분으로 하는 대각 행렬(diagonal matrix)
    - V
        - n차원 정규 직교 행렬 (orthonormal matrix)
- 특성
    - 정규직교행렬(orthonormal matrix)
        - 각 행을 별개의 벡터로 볼때 모두가 서로 직교하고, 길이(norm)가 1인 행렬
        - 자기자신의 transpose와 곱했을 때 단위행렬
            - transpose만 해주면 역행렬이 된다는 편리한 특성
    - 행렬 U와 V

```jsx
# 파이썬의 @ 연산자를 이용하면 np.dot 함수와 같은 행렬곱이나 내적을 편리하게 호출할 수 있습니다.
restored = U @ Sigma @ V.T # T는 전치행렬(transpose)
```

# Python

### 1. **삼중 따옴표 사용하기**

- 삼중 따옴표(`"""` 또는 `'''`)를 사용하면 여러 줄로 작성된 문자열을 손쉽게 표현

```jsx
multiline_string = """이것은 첫 번째 줄입니다.
이것은 두 번째 줄입니다.
이것은 세 번째 줄입니다."""
```

### 3. **소괄호로 여러 줄 연결하기**

- 문자열을 소괄호 `()` 안에 나열하면 Python이 자동으로 문자열 concat
    - 줄바꿈은 포함되지 않음

```jsx
multiline_string = (
    "이것은 첫 번째 줄입니다."
    " 이것은 두 번째 줄입니다."
    " 이것은 세 번째 줄입니다."
)
print(multiline_string)

```

## Numpy bin count

```jsx
- 각 타겟 별 샘플 수 계산
count_malignant, count_benign = np.bincount(cancer["target"])
```