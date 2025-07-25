# **Precision 직접 개선**
- **FP(거짓 양성, False Positive)** 을 줄이는 데 중점.
- Precision은 "모델이 긍정이라고 예측한 샘플 중 실제로 긍정인 비율"로 정의되기 때문에,
    - **오분류를 방지**하고 **모델의 예측 신뢰도를 향상**시키는 전략
---
## **1. 주요 전략 요약**
| **방법** | **적용 대상/핵심** | **효과** |
| --- | --- | --- |
| **Threshold 조정** | 모델의 확률 예측 임계값 조정 | FP 감소 → Precision 직접 개선 |
| **Class Weight 조정** | 손실 함수에 클래스 가중치 적용 | 주요 클래스 Precision 개선 |
| **Balanced Sampling** | 데이터에서 균형 잡힌 샘플링 | 클래스 간 FP 분포 조정 |
| **Hard Negative Mining** | 잘못 예측된 음성 샘플에 집중 | FP 감소 및 Precision 직접 개선 |
| **Regularization 강화** | 모델 복잡도를 제어 (e.g., L1/L2 정규화) | 과적합 방지 및 오분류 감소 |
| **Noise 제거** | 학습 데이터에서 레이블 오류 정리 | FP 감소 및 Precision 간접 개선 |
| **Feature Selection/Engineering** | 중요한 피처를 선택하거나 새로운 피처 생성 | 데이터 품질 개선 → FP 감소 |
---
### **1. Threshold 조정**
- **설명**: 모델이 긍정(1)이라고 예측하는 확률 임계값을 기본값(0.5)에서 상향 조정.
- **효과**: FP(잘못된 긍정 예측)가 줄어들어 Precision 상승.
- **구현 예시** (Python):
    ```python
    from sklearn.metrics import precision_score
    # 예측 확률
    probs = model.predict_proba(X_test)[:, 1]
    # 임계값 조정
    threshold = 0.7
    preds = (probs >= threshold).astype(int)
    # Precision 계산
    precision = precision_score(y_test, preds)
    print("Precision:", precision)
    ```
- **주의점**: FP가 줄어드는 대신 FN(거짓 음성)이 증가할 수 있어 **Recall 감소** 가능성.
---
### **2. Class Weight 조정**
- **설명**: 손실 함수에서 긍정 클래스에 더 높은 가중치를 부여.
- **효과**: 모델이 특정 클래스에서 오분류(FP)를 줄이는 방향으로 학습.
- **구현 예시** (Sklearn):
    ```python
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(class_weight={0: 1, 1: 2})
    model.fit(X_train, y_train)
    ```
- **적용 데이터**: 클래스 불균형이 심한 경우 효과적.
---
### **3. Balanced Sampling**
- **설명**: 학습 데이터에서 클래스 비율을 균형 있게 샘플링하여 데이터 불균형 완화.
- **효과**: 모델이 클래스 간 구분을 더 명확히 학습하여 FP 감소.
- **구현 예시**:
    ```python
    from imblearn.under_sampling import RandomUnderSampler
    sampler = RandomUnderSampler()
    X_resampled, y_resampled = sampler.fit_resample(X_train, y_train)
    ```
---
### **4. Hard Negative Mining**
- **설명**: 모델이 자주 오분류하는 **음성 샘플**(Hard Negatives)에 집중 학습.
- **효과**: FP를 직접 줄여 Precision 개선.
- **구현 예시**:
    - 손실 값이 높은 음성 샘플을 추출하여 추가 학습 데이터로 사용.
    - 예: 객체 탐지에서는 잘못 탐지된 영역을 하드 네거티브로 분류.
---
### **5. Regularization 강화**
- **설명**: 모델의 복잡도를 제어하여 오분류 감소.
- **효과**: 불필요한 피처 의존도 감소 → FP 줄이기.
- **구현 예시** (L1/L2 정규화):
    ```python
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(penalty='l1', solver='liblinear', C=0.1)
    model.fit(X_train, y_train)
    ```
---
### **6. Noise 제거**
- **설명**: 학습 데이터의 레이블 오류를 제거.
- **효과**: 잘못된 샘플로 인한 FP 감소.
- **방법**: 수작업 데이터 클리닝 또는 레이블 검증 알고리즘 활용.
---
### **7. Feature Selection/Engineering**
- **설명**: 불필요한 피처를 제거하거나, 중요한 피처를 추가 생성.
- **효과**: 모델이 적절한 신호만 학습 → FP 감소.
- **구현 예시**:
    ```python
    from sklearn.feature_selection import SelectKBest, chi2
    selector = SelectKBest(chi2, k=10)
    X_selected = selector.fit_transform(X_train, y_train)
    ```
---
### **3. Precision 개선 전략의 우선순위**
| **상황** | **1순위** | **2순위** | **3순위** |
| --- | --- | --- | --- |
| 클래스 불균형 문제 | Threshold 조정 | Class Weight 조정 | Balanced Sampling |
| 레이블 오류 또는 데이터 품질 문제 | Noise 제거 | Feature Engineering | Regularization |
| 음성 클래스에서 오분류(FP)가 많은 경우 | Hard Negative Mining | Feature Selection | Threshold 조정 |
---
### **결론**
- **Precision 직접 개선**은 **FP를 줄이는 데 초점**을 맞춰야 하며, 모델 학습 및 데이터 정제의 다양한 기법을 병행
- 상황에 따라 **Threshold 조정**, **Hard Negative Mining**, **Class Weight 조정**을 우선적으로 고려
- Precision과 Recall 사이의 **Trade-off**를 고려하여 전략을 설정하는 것이 중요