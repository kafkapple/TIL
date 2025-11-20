# 251015_TIL_GPU Process type

# 📄 GPU Process Type Analysis

## 1. GPU 프로세스 타입 개념

### 1.1 기본 타입 분류

- **C(Compute)**: GPU의 연산 자원(CUDA 등)만 활용.
- **G(Graphics)**: 그래픽 자원(OpenGL/DirectX 등)만 활용.
- **C+G(Compute+Graphics)**: 연산(CUDA)과 그래픽(OpenGL 등) 자원을 모두 활용.

### 1.3 실전 구분 기준

- 동일한 python 프로세스라도 연산만 할 경우 `C`,  
  그래픽까지 사용할 경우 `C+G`로 나타남.
- 복합적 GPU 작업 환경에서 리소스 충돌(예, VRAM 부족) 원인 분석에 활용.