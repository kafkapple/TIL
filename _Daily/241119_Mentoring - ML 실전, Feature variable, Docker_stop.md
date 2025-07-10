## ML Practical
### 1. Data 전처리시 Feature 들, split  요령
- 컬럼 최대한 유지하는 편→ 마지막에 제거
- data 적은 경우 k-fold
### **2. 숫자형 변수와 범주형 변수 관련 질문**
- **질문**: 숫자형 변수를 범주형으로 인코딩한 경우, 두 변수를 모두 모델에 포함하면 중복 학습 가능성 있음. 어떤 변수를 선택해야 할지?
- **답변**:
    - 문제 유형에 따라 선택:
        1. **일반 예측 문제**: 다중공선성 확인 및 Feature Importance 확인 후 선택.
        2. **시계열 분석 문제**: 변수의 시계열적 특성 고려.
    - 최종 피처 선정:
        - 다중공선성 확인.
        - 모델의 Feature Importance 기반으로 변수 결정.
## Docker
---
### **1. Dockerfile을 이용한 Airflow 관리자 계정 생성**
- **질문**: Dockerfile에 Airflow 관리자 계정 생성 명령어 포함 시 매번 새로 빌드할 때 계정을 자동 생성할 수 있는지?
- **답변**:
    - **가능**:
        - `docker-compose`에서 실행 명령어에 포함 가능.
        - 서버 실행 시마다 자동으로 관리자 계정 생성.
    - **예시**:
        ```yaml
        command: >
          bash -c "
          airflow db init &&
          airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin &&
          airflow webserver"
        ```
---
### **2. Docker 컨테이너 관리 방식**
- **질문**: 컴퓨터 종료 시 컨테이너를 `stop` 후 `start`하거나, 변경된 컨테이너를 새 이미지를 저장 후 사용하는 방식 중 어떤 방식을 사용하는지?
- **답변**:
    - **개발 환경**: `stop` → `start` 방식이 더 자주 사용됨.
    - **프로덕션 환경**:
        - 상태가 없는 컨테이너(Stateless Container)를 기반으로 새 이미지를 만들어 동일한 환경 배포.
    - **Stateless Container 참고 자료**: [Docker Container Types](https://www.shiksha.com/online-courses/articles/different-types-of-docker-containers/)
---
### **요약**
- **핵심**:
    - 데이터 모델링: 변수 선택 시 문제 유형과 모델 특성을 기반으로 판단.
    - Docker 환경: 개발 환경과 프로덕션 환경의 목적에 따라 관리 방식 달라짐.