인간의 인지 과정을 언어적 사고 가설(LoTH)에 기반하여 모델링한 NLoTM의 핵심 구성 요소 및 원리 이해.

### 1. 언어적 사고 가설 (Language of Thought Hypothesis, LoTH)

#### 1.1 LoTH의 기본 개념

- 핵심 개념(Key Term): Mentalese

- 이론적 원리: 인간 인지가 구조화된 언어와 같은 정신적 표현 시스템에 기반

- 구조: 의미를 전달하는 문장과 같은 구조를 형성하는 단어와 같은 단위로 구성

### 2. NLoTM (Neural Language of Thought Model)

#### 2.1 NLoTM의 개요

- 핵심 개념(Key Term): 비지도 학습 기반 사고 패턴 구현 모델

- 구성 요소: SVQ-VAE, ALP

- 목표: 계층적이고 구성 가능한 의미 표현 학습 및 의미 개념 토큰 생성

#### 2.2 Semantic Vector-Quantized Variational Autoencoder (SVQ-VAE)

- 핵심 개념(Key Term): SVQ

- 역할: 시각 장면의 위계적이고 구성 가능한 요소를 학습하여 장면의 의미를 불연속적으로 분해

- 학습 내용: 객체와 그 속성에 맞춰 계층적이고 조합 가능한 이산 표현 학습

#### 2.3 Autoregressive LoT Prior (ALP)

- 핵심 개념(Key Term): ALP

- 역할: 의미적 개념 토큰의 확률적 생성을 학습하는 오토회귀 변환기

- 특징: VQ-VAE와 달리, 장면 표현을 위해 객체와 그 속성 등 의미 개념을 조합하여 사용