# 1. 머신러닝의 주요 요소
- **데이터 (Data)**
- **모델 (Model)**
- **학습 (Learning)**
## 함수와 모델 학습
- **함수의 개념**:
    - **입력 (Input)** → **일련의 과정 (Process)** → **출력 (Output)**
- **모델 학습의 의미**:
    - 머신러닝에서는 이러한 함수를 데이터로부터 학습하는 과정.
    - **문제 정의의 중요성**:
        - 해결하려는 문제를 함수로 명확하고 구체적으로 정의해야 효과적인 모델 학습이 가능.
---
# 2. 모델 선택과 이해
- **실전에서 한 가지 모델을 선택해야 한다면**:
    - **LightGBM**
    - **Transformer**
- **그러나 전체적인 모델의 이해가 필요**하며, 다음 알고리즘들의 기반 원리를 파악해야 함:
    - **LightGBM**
    - **CatBoost**
    - **XGBoost**
---
# 3. 데이터 이해 및 전처리
### **데이터 구조 파악**
- **데이터 크기 확인**: `.shape` 메소드를 사용하여 **샘플 수**와 **피처 수**를 파악.
### **결측치 및 노이즈 처리**
- **데이터 노이즈 및 라벨 노이즈 종류**:
    - **결측치 (Missing Values)**
    - **이상치 (Outliers)**
    - **잘못된 라벨 (Wrong Labels)**
    - **중복 샘플 (Duplicate Samples)**
    - **도메인 외의 샘플 (Out-of-Domain Samples, OOD)**
- **대처 방안**:
    - **노이즈 확인**: 데이터 분석을 통해 이상치를 식별.
    - **데이터 정제 및 수집**: 노이즈 데이터를 정리하고 필요한 경우 추가 데이터 수집.
    - **명확하고 구체적인 라벨링 가이드라인을 설정**하여 데이터셋 전체에 **일관성 있게 적용**.
### **Silent Failure 문제**
- **개념**:
    - 머신러닝은 데이터를 통해 함수를 정의하지만, 데이터에 노이즈가 있으면 함수 정의가 모호해지거나 불연속 함수가 되어 성능 저하를 초래할 수 있음.
- **해결 방안**:
    - 데이터 품질 향상 및 노이즈 감소를 통한 함수 정의의 명확성 확보.
### **데이터 분포 파악**
- **히스토그램** 등을 사용하여 데이터의 분포를 시각화하고 이해.
### **데이터 스케일링**
- **표준화 (Standardization)**:
    - 데이터의 평균을 0, 분산을 1로 변환.
- **정규화 (Normalization)**:
    - **Min-Max 스케일링**을 통해 데이터 값을 0에서 1 사이로 변환.
---
# 4. 회귀 모델 (Regression Model)
- **정의**: 연속형 변수를 예측하는 머신러닝 모델.
### **변수 타입**
- **입력 변수**:
    - **단순 회귀 (Simple Regression)**: 하나의 독립 변수 사용.
    - **다중 회귀 (Multiple Regression)**: 여러 독립 변수 사용.
- **출력 변수**:
    - **단변량 회귀 (Univariate Regression)**: 하나의 종속 변수 예측.
    - **다변량 회귀 (Multivariate Regression)**: 여러 종속 변수 예측.
- **선형 vs. 비선형 모델**:
    - **선형 모델**: 입력 변수와 출력 변수 간의 관계가 선형인 모델.
    - **비선형 모델**: 비선형 관계를 모델링하는 경우.
### **최적화 방법**
- **해석적 해법 (Analytical Solution)**:
    - 수학적 공식을 통해 정확한 해를 구함.
- **수치적 해법 (Numerical Solution)**:
    - 반복적 알고리즘을 통해 근사 해를 점진적으로 탐색.
### **단순 선형 회귀 모델과 상관 분석**
- **상관 분석**:
    - 한 변수가 변할 때 다른 변수가 어떻게 변하는지 경향성을 분석.
- **용도**:
    - 변수 간의 관계 파악 및 예측 모델 구축에 활용.
---
# 5. 비지도 학습 (Unsupervised Learning)
- **목적**:
    - 레이블 없이 데이터의 본질적인 구조와 패턴을 이해.
- **활용 분야**:
    - 클러스터링, 차원 축소, 이상치 탐지 등.
### **매니폴드 가설 (Manifold Hypothesis)**
- **개념**:
    - 고차원 데이터는 모든 공간에 고르게 분포하지 않고, 낮은 차원의 매니폴드(다양체)를 형성함.
- **의의**:
    - 데이터의 내재된 구조를 이해하고, 효율적인 데이터 표현 및 차원 축소에 활용.
---
# 6. 라벨 노이즈와 모호성
- **라벨 노이즈 (Label Noise)**:
    - **원인**:
        - 실수로 동일한 입력에 서로 다른 라벨이 부여된 경우.
    - **영향**:
        - 모델의 학습 혼란 및 성능 저하.
- **모호성 (Ambiguity)**:
    - **상황**:
        - 문제 자체가 명확하지 않아 정답이 불분명한 경우.
        - 사람조차도 판단하기 어려운 데이터.
    - **해결 방안**:
        - 데이터 수집 단계에서 애매한 사례를 제거하거나 별도로 처리.
        - 라벨링 시 다수의 의견 수렴 또는 추가 정보 활용.
- **대처 전략**:
    - **라벨링 가이드라인 강화**: 명확한 기준을 세워 일관성 있는 라벨링.
    - **데이터 검증**: 라벨의 정확성을 검토하고 정제.
---
# 7. 추가 참고 사항
- **모델의 성능 향상**을 위해서는 **데이터 품질**이 매우 중요함.
- **데이터 전처리**와 **노이즈 제거**는 모델 학습 이전에 반드시 수행되어야 할 단계.
- **다양한 모델과 알고리즘의 이해**를 통해 문제에 적합한 방법을 선택할 수 있음.