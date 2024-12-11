## 요약: 하이퍼파라미터 최적화에서 메트릭 선택

하이퍼파라미터 최적화에서 어떤 메트릭을 사용할지는 태스크의 특성과 목적에 따라 

---

### 1. **Loss 최소화 (`Minimize Loss`)**

- **사용 상황**:
    - 태스크 전반에 일반적으로 적용 가능.
    - 학습 과정의 최적화를 직접적으로 반영.
    - 오버피팅 감지 용이.
- **Optuna 코드 예시**:
    
    ```python
    python
    코드 복사
    def objective(trial):
        # training code
        return metrics['loss']  # validation loss
    
    study = optuna.create_study(direction="minimize")
    
    ```
    
- **장점**:
    - 모든 태스크에 적용 가능.
    - 모델 학습 상태를 직관적으로 평가.

---

### 2. **F1 Score 최대화 (`Maximize F1 Score`)**

- **사용 상황**:
    - 불균형 데이터셋에서 적합.
    - Precision과 Recall의 조화를 고려.
    - 실제 비즈니스 메트릭과 연관성 높음.
- **Optuna 코드 예시**:
    
    ```python
    python
    코드 복사
    def objective(trial):
        # training code
        return metrics['f1']  # f1 score
    
    study = optuna.create_study(direction="maximize")
    
    ```
    
- **장점**:
    - 클래스 불균형 데이터에서 더 적합.
    - 실제 성능 평가와 연관성이 큼.

---

### 3. **현재 상황: 감성 분석**

- **문제 특징**:
    - 이진 분류 문제.
    - 클래스 불균형 가능성 있음.
    - 성능 평가에 F1 Score를 많이 사용.
- **추천**:
    - **F1 Score로 최적화** 진행이 적절.