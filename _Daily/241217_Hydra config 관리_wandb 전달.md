### 1. 필요한 라이브러리 임포트
```python
import hydra
from omegaconf import OmegaConf, DictConfig
import wandb
```
### 2. Hydra 데코레이터 사용
Hydra 데코레이터를 사용하여 메인 함수를 정의
```python
@hydra.main(version_base="1.2", config_path="configs", config_name="config")
def main(cfg: DictConfig):
    # 여기서 cfg는 전체 Hydra 설정을 포함
    # 필요한 섹션만 추출
    selected_config = OmegaConf.select(cfg, 'defaults,train')
    # WandB 초기화 시 config 전달
    wandb.init(project="your_project_name", config=OmegaConf.to_container(selected_config, resolve=True))
    # 예시: WandB에서 config 설정 업데이트 및 확인
    wandb.config.update(selected_config)
    wandb.finish()
```
또는 `OmegaConf`의 `create` 및 `merge` 기능을 활용
```python
selected_config = OmegaConf.create({
    'defaults': cfg.defaults,
    'train': cfg.train
})
```
### 3. 여러 yaml 관리
```jsx
project/
├── configs/
│   ├── config.yaml          # 기본 설정
│   ├── model/
│   │   ├── wav2vec.yaml        
│   │   ├── transformer.yaml   
│   ├── dataset/
│       ├── ravdessyaml         
│       ├── fer2013.yaml         
└── main.py
```
- config.yaml 파일에서 각 yaml 파일 load
```jsx
defaults:
  - dataset: ravdess #
  - model: wav2vec
  - _self_
```
### 4. timestamp, 프로젝트 루트 위치, 기타 변수 활용
```jsx
project:
  name: "joon_test_multimodal_emotion"
  timestamp: ${now:%Y%m%d_%H%M%S}
  hydra_cwd: ${hydra:runtime.cwd}
project_name: ${project.name}
```
- **현재 시간**: `${now}`를 사용하거나 Python `datetime` 모듈로 직접 설정 가능.
- **프로젝트 루트 폴더**: `hydra.utils.get_original_cwd()`를 사용.