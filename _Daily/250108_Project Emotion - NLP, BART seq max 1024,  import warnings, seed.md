# 회고
- 이번 주 월요일에는 성공했었으나,
  - 아침 일찍 운동
  - 하루 계획 
  - 적당한 타임 블럭
- 화요일부터 다시 조금 밸런스 무너짐
  - 운동 못함
  - 프로젝트 코딩 위주로 다시... 오늘 특히
  - 강의는 거의 못들, 정리 위주. 최근 개념들 재정리 필요. 
  - 그래도 TIL 꾸준히 보충 및 채우기.
# Project
## Multi-modal emotion
- image, audio 각각에 대해서는 dataset, model 및 학습 로깅 확인. 
  - 로깅 관련 사소한 오류 (로컬 폴더 저장 등)
- emotion-llama 테스트중, hugging face model 은 text input 만 가능하다는 것 확인 (약간은 불확실)
  - text dataset, model (bert) 추가 구현중 오류. 다시 롤백. 
  - 
## NLP dialogue summarization
- 기본 data, model, train 후 metric 기록 개선까지는 체크
- 다음 기능 개선 중 오류. 다시 차근차근 필요.
  - model 추가
  - quantize 등 기법 적용
  - unfreeze layer 등 학습 기법 조절
  - logging 조절
  - refactoring
# Transformer BART input sequence max 1024
- BART 모델의 max_position_embeddings는 1024
- 입력 시퀀스의 길이가 너무 길거나, 토큰화된 입력이 모델의 최대 길이를 초과할 때 오류 발생 가능
- text generation (summarization ) 시, 다음과 같은 설정 추천.
- max_length=512, # BART의 max_position_embeddings 고려
- max_length=128, # 요약문은 더 짧게 제한
# Warning 무시
- Python
```jsx
import warnings
warnings.filterwarnings(action='ignore')
```
- torchvision
```python
# 모든 torchvision 관련 경고 비활성화
warnings.filterwarnings(action = "ignore", category=UserWarning, module="torchvision")
# Beta transforms 경고 비활성화
torchvision.disable_beta_transforms_warning()
```
# SEED 고정
```
# 재현성을 위한 시드 고정
SEED = 0
random.seed(SEED)
np.random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)
```
## Torch lightning - seed_everything
```jsx
import pytorch_lightning as pl
# 시드 값 설정 (여기서는 예시로 42 사용)
pl.seed_everything(42, workers=True)
# 이후 Trainer 설정
trainer = pl.Trainer(
    # ...
    deterministic=True  # 연산 결과 재현성 보장을 위해 deterministic 모드 활성화
)
```
- **`pl.seed_everything(seed, workers=True)`**
    - `seed`: 원하는 시드 값(정수).
    - `workers=True`로 설정하면 PyTorch DataLoader의 num_workers가 0보다 큰 경우에도 워커(worker)마다 시드를 고정
    - 내부적으로 Python의 `random`, NumPy, PyTorch, CUDA 시드를 설정
- **재현성 보장을 위한 추가 설정**
    - `trainer = pl.Trainer(deterministic=True)`로 설정 시, CuDNN 연산 등에 있어 항상 동일한 결과를 보장하도록 시도
    - 정확한 재현성을 위해서는 사용 중인 라이브러리, GPU 환경 등에 따라 약간의 주의가 필요
- **환경 변수나 CUDA 설정**
    - 시드를 고정해도 GPU 연산 특성(특히 병렬 연산)으로 인해 완벽히 동일한 결과가 재현되지 않을 수