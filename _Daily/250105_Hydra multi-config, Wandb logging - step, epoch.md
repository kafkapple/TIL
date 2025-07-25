# Project
## Project template
### Step / Epoch Learning curves
### Debug
- PyTorch DataLoader가 멀티프로세싱을 사용시 오류
  - Lambda 함수는 pickle이 불가능하기 때문에 프로세스 간 전달시 문제
  - 대안
  - 1) num workers =0 
  - 2) psutils 설치 후, 구동 환경에 맞는 값 설정
# Study
## Hydra multi-config → wandb logging
- OmegaConf.to_container(cfg, resolve=True)
- model_config = config_dict["model"]
- "train": train_config
```jsx
    config_dict = OmegaConf.to_container(cfg, resolve=True)
    # 두 개 카테고리 값 그대로 가져오기
    train_config = config_dict["train"]
    model_config = config_dict["model"]
    # 2. 커스텀 값 추가
    custom_values = {
        "learning_rate_squared": train_config["lr"] ** 2,  # 계산 예시
        "experiment_name": "baseline_experiment",          # 고정 값 예시
        "custom_batch_times_lr": train_config["batch_size"] * train_config["lr"]
    }
    # 3. wandb.init
    wandb.init(
        project="my_project",
        config={
            "train": train_config,
            "model": model_config,
            **custom_values  # 커스텀 값 추가
        }
    )
    # 4. wandb.log (추가 로깅 예시)
    wandb.log({
        "epoch": 1,
        "accuracy": 0.85,
        **custom_values
    })
```
## Wandb logging 단위: Step, Epoch
- step 단위 로깅의 장단점
    - 장점: 더 세밀한 학습 과정 모니터링 가능
    - 단점: 로깅 데이터양 증가, 계산 비용 증가
- Step 단위 로깅 (추천)
    - Loss: step 단위로 로깅 (학습 진행 상황을 자세히 모니터링)
    - Accuracy: step 또는 epoch 단위 (계산 비용 고려)
- Epoch 단위 로깅 (추천)
    - 기타 메트릭(F1, Precision 등): epoch 단위 (계산 비용이 높음)
    - 시각화(Confusion Matrix, PR Curve 등): epoch 단위