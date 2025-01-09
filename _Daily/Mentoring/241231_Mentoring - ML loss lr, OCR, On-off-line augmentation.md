# 핵심

- Toy dataset
- epoch 별 loss, learning rate 모니터링 (scheduler)
- 초기 파라미터는 문헌 참고

**멘토소개**

- **포스트매스(PostMASS)**:
    
    **수학 LLM 문제 풀이**: 대형 언어 모델을 활용한 수학 문제 해결 방법
    

# **OCR (광학 문자 인식)**

- **이미지 처리 2-Stage 접근법**

1.	**텍스트 검출(Text Detection)**

- 이미지 내 텍스트 영역을 블록으로 검출하여 바이너리 맵 생성
- ResNet 기반의 피라미드 구조 활용
- U-Net 및 Autoencoder 구조 개선:
- 중간에 feature 연결 부분 강화

2.	**텍스트 디코딩(Text Decoder)**

- Latent space에 충분한 정보가 담겨 있을 경우:
    - Fully Connected (FC) layer + Softmax를 추가하여 분류기(Classifier) 구성 가능
- **데이터 전처리**
    - **Crop 및 Warping**: 텍스트 영역을 잘라내고 변형 적용

# **데이터 증강(Augmentation)**

## **Online 온라인 증강**

- 랜덤 시드 사용
- 장점:
    - 에폭 수가 늘어날수록 더 많은 학습 가능
- 단점:
    - augraphy 같이 cpu 로드 큰 경우, 시간 증가

## **Offline 오프라인 증강**

- 단점:
    - 에폭 수가 늘어나도 다양성 증가가 제한적

## 대안

- **전략**: 오프라인에서 증강을 사전 처리하고, 트레이닝 시에만 온라인 증강을 추가
- **테스트 시간 증강(TTA)**
    - 간단한 Flip 등을 적용하여 앙상블 효과 도출

# **Toyset 실험 및 모델 검증**

- **Toyset 실험**
    - 전체 데이터의 10%를 Toy set으로 분리
    - 작은 데이터셋으로 목표 모델 또는 경량화된 구조 먼저 실험
- **가정**:
    - 모델이 너무 복잡하고 데이터가 작을 경우, Loss가 급격히 하락 (Underfitting/Overfitting 가능성)
- **조치**:
    - Step size 별로 Loss 세부 로깅
    - 모델 크기 조정 및 Hard augmentation 적용
    - Loss가 완만하게 떨어지는지 확인하여 모델 문제인지 데이터 문제인지 판단

# **모델 개선 기법**

- **라벨 스무딩(Label Smoothing)**
    - 분류 후 라벨 스무딩 효과 확인
- **데이터 분할 비율**
    - 실무: Train:Validation:Test = 7:1.5:1.5
    - 데이터가 많을 경우 Train 비율을 늘림
    - **주의**: Test, Train 보다 현실 분포 잘 대변해야 함
- **모델 일반화 성능 평가**
    - 대회 지표 외에도 다양한 지표 활용

## 다양한 Loss 시도:

- Custom Loss Function: Focal Loss + Weighted BCE (가중치 부여)
- Combine Multiple Loss:
- DBNet: BCE Loss + Dice Loss

## **학습 스케줄링**

- Cosine Annealing: 학습 초반부터 큰 Learning Rate 적용
- Step LR: 단계적으로 Learning Rate 조정
    - **주의**: Learning Rate가 너무 크면 발산 위험
    - Learning Rate와 Loss를 함께 플롯하여 모니터링

# **대회 초반 전략**

- **Valid Set 분리**
    - Test 셋을 대변할 수 있는 Valid set을 Train 셋에서 분리
    - 육안으로 검토하거나 Toy set으로 모델 학습
- **Valid Set과 Test Set 간 경향성 확인**
    - Valid Set의 경향성과 Test Set의 Leaderboard 경향성 비교
  - 경진대회, 일반화 모델과 동시에 주어진 데이터셋 오버피팅 시키는걸 찾는 셈이기도
- **Tuning 할 요소 우선순위**
  - eda
  - val set 정의
  - scheudler

# **Q&A 주요 주제**

- 초기 파라미터 설정?
    - 현업은, 문헌 그대로 시작
- **Data Leakage 이슈**
    - **Train과 Validation에서의 Augmentation 적용?**
    - 이론 적으로는 train 에만 적용해야 하나, 현재 대회 같은 경우 augmentation test 에 강한 상황이기에, 분리 보다 증강 자체가 더 중요할 수도
- **Validation Set 기준 설정**
    - 실제 Test submission 시 결과와 성능 개선 트렌드 연관성 있어야
    - valid set 결과 saturation 시, 난이도 향상 필요
- **Class Imbalance 및 모델 성능 차이**
- **클래스별 결과 차이 분석**
    - **Image Data Embedding 및 Clustering**

**문제 해결 팁**

- **Papers with Code 활용**: 관련 논문과 코드를 참고하여 문제 해결
- **확장적 탐색**: 관련성이 없어 보이는 질문까지 확장하여 정보 탐색

**기술 및 모델**

- **SimCLR**
    - ResNet 기반의 Self-Supervised Learning
    - Knowledge Transfer 기법 활용

# **실무 전략**

## **모니터링 및 시각화**:

- **Step Size 별 Loss, learning rate 로깅**
  - 학습 과정 중 각 스텝마다 손실 값을 기록하여 패턴을 분석.
    - scheduler 사용시, learning rate 값도 동시 모니터링.
    - 파라미터 잘못 준 경우, 특히 초기에 완만하게 떨어지지 않고 loss 발산 현상

## **유효성 검증(Validation)**:

- **Valid Set 설정**: Test 셋을 대변할 수 있는 Valid set을 분리하여, 학습 과정에서 모델의 일반화 성능을 지속적으로 평가
- **Toy Set 실험**: 전체 데이터의 일부분(Toy set)을 활용하여 작은 규모에서 먼저 모델을 실험하고, 파라미터 설정을 조정한 후 전체 데이터에 적용

## **모델 및 데이터 문제 구분**:

- **Hard Augmentation 적용**: 데이터 다양성을 높이기 위해 강력한 증강 기법을 적용하여 모델의 일반화 성능을 향상