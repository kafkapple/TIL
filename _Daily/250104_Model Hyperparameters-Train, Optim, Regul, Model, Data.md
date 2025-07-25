# 모델 하이퍼파라미터 튜닝 가이드
- 모델 하이퍼파라미터 튜닝 시 **핵심 카테고리**별로 중요한 요소들을 **우선순위**에 따라 **두 개의 축**으로 정리
- 각 카테고리는 두 개의 주요 축(하이퍼파라미터와 설명)으로 구성되어 있으며, 기본적인 우선순위부터 단계별로 정렬
---
## 1. 학습 관련 파라미터 (Training Parameters)
| **하이퍼파라미터**               | **설명**                                                                                     |
|---------------------------------|----------------------------------------------------------------------------------------------|
| **에폭 (Epoch)**                | 전체 학습 데이터를 한 번 학습하는 횟수. 과소적합과 과적합을 조절하는데 중요함.                   |
| **배치 사이즈 (Batch Size)**     | 한 번의 업데이트에 사용되는 샘플의 수. 학습 속도와 일반화 성능에 영향을 미침.                    |
| **학습률 스케줄러 (LR Scheduler)** | 학습 과정에서 학습률을 조정하는 방법 (예: Step Decay, Cosine Annealing 등). 안정성과 수렴 속도 향상. |
## 2. 최적화 관련 파라미터 (Optimization Parameters)
| **하이퍼파라미터**           | **설명**                                                                                             |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| **학습률 (Learning Rate)**    | 가중치 업데이트의 크기를 결정. 너무 크면 최적점에 도달하지 못하고, 너무 작으면 학습이 느려짐.               |
| **최적화 알고리즘 (Optimizer)** | 가중치를 업데이트하는 방법 (예: SGD, Adam, RMSprop 등). 학습 속도와 안정성에 큰 영향.                        |
| **모멘텀 (Momentum)**         | 이전 업데이트의 영향을 고려하여 가중치를 업데이트. 진동을 줄이고 수렴 속도를 높임.                          |
## 3. 정규화 및 규제 관련 파라미터 (Regularization Parameters)
| **하이퍼파라미터**                  | **설명**                                                                                              |
|------------------------------------|-------------------------------------------------------------------------------------------------------|
| **드롭아웃 (Dropout)**               | 학습 과정에서 무작위로 뉴런을 비활성화하여 과적합을 방지 (일반적으로 0.2 ~ 0.5).                        |
| **L1/L2 정규화 (L1/L2 Regularization)** | 가중치의 크기를 제한하여 과적합을 방지. L1은 절대값 합, L2는 제곱합을 최소화.                           |
| **레이블 스무딩 (Label Smoothing)**    | 타겟 레이블을 부드럽게 하여 모델의 확신을 줄이고 일반화 성능을 향상시킴.                                  |
| **조기 종료 (Early Stopping)**        | 검증 성능이 향상되지 않을 때 학습을 조기에 중단하여 과적합을 방지하고 학습 시간을 절약.                     |
## 4. 모델 구조 관련 파라미터 (Model Architecture Parameters)
| **하이퍼파라미터**                 | **설명**                                                                                      |
|-----------------------------------|-----------------------------------------------------------------------------------------------|
| **네트워크 깊이 (Network Depth)**    | 신경망의 층 수. 더 깊은 네트워크는 복잡한 패턴 학습 가능하지만 과적합 및 학습 어려움 위험.                      |
| **뉴런 수 (Units per Layer)**       | 각 층의 뉴런 또는 필터 수. 모델의 표현력을 결정.                                                  |
| **활성화 함수 (Activation Function)** | 뉴런의 출력을 결정하는 함수 (예: ReLU, Sigmoid, Tanh 등).                                       |
| **배치 정규화 (Batch Normalization)** | 각 배치마다 입력을 정규화하여 학습을 안정화하고 속도를 높임.                                       |
## 5. 데이터 관련 파라미터 (Data-related Parameters)
| **하이퍼파라미터**               | **설명**                                                                                      |
|---------------------------------|-----------------------------------------------------------------------------------------------|
| **데이터 증강 (Data Augmentation)**  | 학습 데이터에 다양한 변형을 가해 데이터 다양성을 높이고 과적합을 줄임.                              |
| **데이터 전처리 (Data Preprocessing)** | 데이터의 스케일링, 정규화 등 (예: 표준화, 정규화, PCA 등).                                      |
## 6. 기타 파라미터 (Other Parameters)
| **하이퍼파라미터**                     | **설명**                                                                                             |
|---------------------------------------|------------------------------------------------------------------------------------------------------|
| **가중치 초기화 (Weight Initialization)** | 모델 학습 시작 시 가중치의 초기값 설정 방법 (예: Xavier, He 초기화). 학습의 안정성과 속도에 영향.             |
| **손실 함수 (Loss Function)**           | 모델 학습 시 최적화할 목표 함수 (예: 교차 엔트로피, MSE, Hinge Loss 등).                                 |
| **가중치 감소 (Weight Decay)**          | 가중치의 크기를 줄여 과적합을 방지하는 기법으로 L2 정규화와 유사.                                         |
| **학습률 감쇠 (Learning Rate Decay)**    | 학습이 진행됨에 따라 학습률을 점진적으로 줄여 학습의 안정성과 최적화를 도모.                                |
---
## 하이퍼파라미터 튜닝 방법론 (Hyperparameter Tuning Methodologies)
| **방법론**                           | **설명**                                                                                          |
|--------------------------------------|---------------------------------------------------------------------------------------------------|
| **그리드 서치 (Grid Search)**           | 미리 정의된 하이퍼파라미터 조합을 모두 시도. 간단하지만 계산 비용이 많이 듦.                                  |
| **랜덤 서치 (Random Search)**           | 하이퍼파라미터 공간에서 무작위로 조합을 선택하여 시도. 그리드 서치보다 효율적일 수 있음.                        |
| **베이지안 최적화 (Bayesian Optimization)** | 이전 평가 결과를 기반으로 다음 시도할 하이퍼파라미터를 선택. 효율적이고 성능이 우수함.                        |
| **하이퍼밴드 (Hyperband)**              | 랜덤 서치와 조기 종료를 결합한 방법. 자원을 효율적으로 사용하여 빠르게 최적화를 수행.                              |
---
## 하이퍼파라미터 튜닝 시 고려 사항
1. **우선순위 설정**: 기본적인 하이퍼파라미터(예: 학습률, 배치 사이즈 등)부터 조정한 후, 점차적으로 복잡한 파라미터로 이동.
2. **상호작용 고려**: 일부 하이퍼파라미터는 서로 영향을 미칠 수 있으므로, 다양한 조합을 실험할 필요가 있음.
3. **자원 제약**: 튜닝에 소요되는 시간과 계산 자원을 고려하여 효율적인 방법론 선택.
4. **평가 지표 선정**: 모델의 성능을 평가할 적절한 지표(예: 정확도, F1 스코어 등)를 선정하여 튜닝 과정에서 활용.
5. **재현성 확보**: 실험의 재현성을 위해 랜덤 시드를 고정하고, 실험 설정을 체계적으로 관리.