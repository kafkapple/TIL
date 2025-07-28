# 데이터 누출(data leakage)
- 모델이 훈련 중에 테스트 데이터의 정보를 미리 알게 되는 상황
- 다음 과정에서 Validation, Test set 정보가 Train set 에 유입되는 것 주의
    - Data preprocessing
    - Data augmentation
## 1. 데이터 분할
- train_test_split을 사용하여 데이터를 훈련 및 검증 세트로 나누는 경우,
    - stratify 매개변수를 사용하여 클래스 분포를 유지하면서 무작위로 분할
        - 이로 인해 데이터 누출의 위험 감소
- kfold 또는 stratified_kfold를 사용할 때는 각 폴드가 독립적으로 유지되도록 해야
    - 현재 설정에서는 stratified를 사용하고 있으므로, 데이터 누출의 위험 낮음
## 2. 데이터 증강:
- 증강은 훈련 데이터에만 적용되어야 하며, 검증 및 테스트 데이터에는 적용되지 않아야
    - is_train 플래그를 사용하여 훈련 데이터에만 증강을 적용
- 단, Test dataset 에 심한 증강이 이미 가해져있거나 한 상황에서는 약간의 예외.
- off-line aug는 Train, test 모두 증강 하되, on-line augmentation 시 train 에만 가하는 것도 방법