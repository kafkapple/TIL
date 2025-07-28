# 📄 Neural_Rendering_Quality_Metrics

신경망 렌더링 모델의 출력 품질을 평가하는 세 가지 주요 지표: 재구성 오차, 구조 유사성, 지각 유사성.

### 1. 재구성 오차 (Reconstruction Error)

#### 1.1 PSNR (Peak Signal-to-Noise Ratio)

- 핵심 개념: 원본과 재구성 이미지 간의 신호 대 잡음비

- 이론적 원리: MSE(Mean Squared Error) 기반의 로그 스케일 변환

- 활용: 단순 계산, 정량적 baseline 평가

### 2. 구조 유사성 (Structural Similarity)

#### 2.1 SSIM (Structural Similarity Index Measure)

- 핵심 개념: 인간 시각 시스템의 구조적 정보 인지 반영

- 이론적 원리: 밝기, 대비, 구조 세 가지 요소의 조합

- 활용: 텍스처, 윤곽 등 시각적 유사성 평가

### 3. 지각 유사성 (Perceptual Similarity)

#### 3.1 LPIPS (Learned Perceptual Image Patch Similarity)

- 핵심 개념: 딥러닝 모델이 학습한 특징 공간에서의 유사성

- 이론적 원리: CNN 특징 추출 기반의 인간 지각 유사성 측정

- 활용: 실제 시각 품질, 자연스러움 비교
# 📄 4D_Rendering_Hybrid_Approach

3DGS와 HexPlane 아이디어를 결합한 4D 렌더링 하이브리드 접근법은 '명시적 기본 모델 + 암시적 움직임 모델' 구조를 통해 고품질의 빠른 렌더링과 시간적 연속성 및 압축 효율성을 동시에 달성함.

## 📍 학습 내용

### 1. 4D 렌더링 하이브리드 접근법

#### 1.1 핵심 개념

- '명시적 기본 모델 + 암시적 움직임 모델' 구조를 가짐

- 각 방식의 장점을 결합하여 최적의 결과를 얻는 하이브리드 접근법임

- 3DGS의 빠른 렌더링 속도와 HexPlane의 시간적 연속성 및 압축 효율성을 모두 잡음

### 2. 3DGS와 HexPlane 결합 방식

#### 2.1 기본 모델 (Canonical Model) - 3DGS 역할

- 기준 시간(t=0)에 매우 정교하고 사실적인 3D 가우시안 모델을 생성함

- 장면의 '기본 형태'를 명시적(explicit)으로 표현하는 역할을 함

- 고품질의 '찰흙 인형'에 비유될 수 있음

#### 2.2 움직임 모델 (Deformation/Motion Model) - HexPlane 역할

- 작고 효율적인 신경망이 시간(t)에 따른 변화를 학습함

- 특정 시간 t와 3D 좌표 (x, y, z)를 입력받아 해당 지점의 변형 정보를 출력함

- '움직임' 자체를 연속적인 함수로 표현하는 암시적(implicit) 방식의 아이디어를 차용함

### 3. 결합 및 렌더링 과정

#### 3.1 렌더링 과정

- 기준 시간의 3D 가우시안들을 가져옴

- 가우시안들의 위치, 크기, 회전 값을 움직임 모델에 통과시켜 시간 t에 맞는 상태로 변형시킴

- 변형된 가우시안들을 3DGS의 빠른 렌더러를 이용해 최종 이미지를 생성함