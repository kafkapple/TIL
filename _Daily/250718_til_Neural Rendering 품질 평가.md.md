# Neural Rendering 품질 평가
## **재구성 오차** 지표

- **핵심**: PSNR (Peak Signal-to-Noise Ratio)

- 원리: MSE 기반, 로그 스케일 변환

- 활용: 단순 계산, 정량적 baseline 평가

---

## **구조 유사성** 지표

- **핵심**: SSIM (Structural Similarity Index Measure)

- 특징: 밝기, 대비, 구조 세 요소 조합

- 연결: 텍스처, 윤곽 등 시각적 유사성 평가

---

## **지각 유사성** 지표

- **핵심**: LPIPS (Learned Perceptual Image Patch Similarity)

- 원리: CNN 특징 추출, 인간 지각 유사성

- 활용: 실제 시각 품질, 자연스러움 비교