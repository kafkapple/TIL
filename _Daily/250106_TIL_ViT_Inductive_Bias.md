ViT는 약한 Inductive Bias를 가지며, 대규모 데이터셋 사전 학습을 통해 일반화 성능을 확보한 Vision Transformer 모델

### 1. ViT의 특징 및 동작 원리

#### 1.1 Inductive Bias의 약점 극복

- **데이터 기반 학습**: 매우 큰 데이터셋에서의 사전 학습을 통해 약한 Inductive Bias로 인한 일반화 성능 저하 문제 극복

- **통합적 모델 구조**: CNN의 Locality, RNN의 Sequentiality와 같은 강한 Inductive Bias 없이 보다 통합적이고 일반적인 모델 구조 지향

- **공간 관계 학습**: Position Embedding 초기화 시 위치 정보가 전달되지 않아, 공간(Spatial) 관계를 처음부터 학습 필요

#### 1.2 Self-Attention 메커니즘

- **글로벌 관계 처리**: Self-Attention 메커니즘을 통해 이미지 전체의 글로벌한 영역 처리 가능

- **2차원 구조 활용**: 이미지 Patch를 잘라 Input으로 사용하며, Fine-tune 시 다른 해상도 이미지에 대한 위치 임베딩 조정 필요

- **MLP Layer의 역할**: MLP Layer에서만 Local 및 Translation Equivariance 특성 유지

### 2. Inductive Bias 관점 모델 비교

#### 2.1 CNN (Convolutional Neural Networks)

- **강한 Inductive Bias**: 지역성(Locality) 및 번역 불변성(Translation Invariance)

- **장점**: 효율적인 공간 정보 처리, 파라미터 효율성, 다양한 비전 응용 분야

- **단점**: 글로벌 관계 학습 및 복잡한 구조 관계 표현의 한계

#### 2.2 RNN/LSTM (Recurrent Neural Networks)

- **강한 Inductive Bias**: 순차성(Sequentiality)

- **장점**: 시퀀스 데이터 처리, 시간적 의존성 학습

- **단점**: 병렬화의 어려움, 장기 의존성 문제, 복잡한 구조 학습의 제한

#### 2.3 Transformer

- **약한 Inductive Bias**: Self-Attention 메커니즘을 통한 모든 위치 간 관계 학습

- **장점**: 병렬 처리, 긴 거리 의존성 학습, 유연한 구조, 스케일링 용이

- **단점**: 대규모 데이터 필요, 높은 계산 비용, 위치 정보 명시적 인코딩 필요

#### 2.4 ViT (Vision Transformer)

- **공간적 Inductive Bias 없음**: CNN과 달리 지역성이나 번역 불변성 가정 없음

- **장점**: 글로벌 관계 학습, 대규모 데이터셋에서 높은 성능, 유연한 구조

- **단점**: 대규모 데이터 필요, 높은 계산 비용, 위치 임베딩 조정 필요

#### 2.5 MLP-Mixer

- **거의 없는 Inductive Bias**: 전적으로 MLP 기반 설계

- **장점**: 단순한 구조, 글로벌 관계 학습 가능

- **단점**: Inductive Bias 부족으로 대규모 데이터 필요, 상대적으로 낮은 성능, 계산 비용 증가

### 3. 핵심 개념 요약

#### 3.1 Inductive Bias

- **정의**: 모델이 학습하지 않은 입력에 대해 특정 가정을 하도록 유도하는 경향

- **모델별 특성**: CNN(Locality, Translation Invariance), RNN(Sequentiality), Transformer/ViT(약함)

- **영향**: 강한 Inductive Bias는 적은 데이터로도 학습 가능하나, 유연성 제한; 약한 Inductive Bias는 대규모 데이터 필요하나, 높은 일반화 성능 잠재력

#### 3.2 Self-Attention

- **정의**: 입력 시퀀스의 각 요소가 다른 모든 요소와의 관계를 학습하여 가중치를 부여하는 메커니즘

- **특징**: 글로벌한 의존성 학습, 병렬 처리 가능

- **ViT 적용**: 이미지 패치 간의 관계 학습에 활용되어 이미지 전체의 맥락 이해

#### 3.3 Positional Encoding/Embedding

- **정의**: 시퀀스 내 요소들의 상대적 또는 절대적 위치 정보를 모델에 주입하는 방법

- **필요성**: Transformer 계열 모델은 순서 정보를 자체적으로 학습하지 못하므로 필수

- **ViT 적용**: 이미지 패치의 공간적 위치 정보를 제공하여 모델이 공간 관계를 학습하도록 지원