# Autolog
```python
# 다른 프레임워크의 autolog
mlflow.tensorflow.autolog()    # TensorFlow
mlflow.pytorch.autolog()       # PyTorch
mlflow.xgboost.autolog()       # XGBoost
mlflow.lightgbm.autolog()      # LightGBM
mlflow.keras.autolog()         # Keras
```
## autolog 세부 설정
mlflow.sklearn.autolog(
log_input_examples=True,    # 입력 데이터 예시 기록
log_model_signatures=True,  # 모델 시그니처 기록
log_models=True,           # 모델 아티팩트 기록
log_datasets=True,         # 데이터셋 정보 기록
disable=False,             # autolog 비활성화 여부
exclusive=False,           # 다른 프레임워크의 autolog 비활성화 여부
disable_for_unsupported_versions=False,  # 지원되지 않는 버전에서 비활성화
silent=False              # 로깅 메시지 출력 여부
)
# MLflow DB 구조
- **MLflow 구조**:
    1. **`backend-store-uri`**: SQLite, PostgreSQL, MySQL 등의 데이터베이스를 통해 **실험 메타데이터**(실험 이름, 실행 정보, 매개변수, 메트릭 등)를 저장.
    2. **`default-artifact-root`**: 로컬 파일 시스템 또는 클라우드 스토리지(S3, GCS 등)에 **모델 파일, 로그, 출력물**(아티팩트)을 저장.
- SQLite를 설정해도 **실험의 메타데이터는 SQLite DB에 저장되지만**, **아티팩트(모델 파일, 로그 등)**는 여전히 디스크 상의 폴더(예: `artifacts`, `mlruns`)에 저장
### **2. SQLite와 로컬 파일 저장 방식 비교**
SQLite를 설정하지 않은 경우, MLflow는 **모든 데이터를 로컬 파일 시스템에 JSON 및 디렉토리 구조로 저장**합니다. SQLite를 사용하는 경우에는 다음과 같은 차이가 있습니다:
| 항목 | 로컬 파일 시스템 | SQLite DB |
| --- | --- | --- |
| **메타데이터 저장** | JSON 파일 (`mlruns` 폴더) | SQLite DB 파일 (`mlruns.db`) |
| **아티팩트 저장** | 로컬 디렉토리 (예: `artifacts`, `mlruns`) | 로컬 디렉토리 (예: `artifacts`, `mlruns`) |
| **데이터 검색** | 파일 기반으로 직접 검색 | SQL 쿼리로 검색 가능 |
| **다중 사용자 환경** | 동시 읽기/쓰기 문제 발생 가능 | SQLite 트랜잭션 관리로 더 안정적 |
| **확장성** | 작은 규모에 적합 | 중간 규모에 적합 (대규모는 PostgreSQL 권장) |
### **3. SQLite의 실제 데이터 저장 위치**
SQLite DB 파일은 `backend-store-uri`로 설정한 파일 경로에 저장
```bash
--backend-store-uri sqlite:///D:/dev/Upstage/mlruns.db
```
- **SQLite DB 파일**:
    - `D:/dev/Upstage/mlruns.db`에 저장.
- **아티팩트 디렉토리**:
    - 기본적으로 **`default-artifact-root`*에서 지정된 경로에 저장됩니다.
    - 명시하지 않은 경우, **현재 작업 디렉토리**에 `artifacts` 폴더가 생성
- **SQLite CLI**: `sqlite3 mlruns.db` 명령으로 데이터베이스에 직접 접속.
- **Python**: `sqlite3` 라이브러리를 사용하여 데이터 쿼리 가능.
- **MLflow Tracking Server**: `mlflow server`를 통해 브라우저 기반 GUI로 확인.
`mlflow ui` 명령어는 기본적으로 **현재 디렉토리의 `./mlruns` 폴더**를 데이터 저장소로 사용합니다. 이 방식은 SQLite DB 파일이 아닌 로컬 디렉토리를 사용하므로, 원하는 `backend-store-uri`를 설정하려면 Tracking Server 명령어를 길게 적어야 
### **단축 명령어 사용 방법**
1. **Bash Alias를 설정**하여 Tracking Server 명령어를 간단히 단축
    ```bash
    alias mlflow-ui="mlflow server --backend-store-uri sqlite:///mlruns.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5000"
    ```
    이후, 다음처럼 간단히 실행
    ```bash
    mlflow-ui
    ```
2. **`mlflow ui` 기본값을 SQLite DB로 변경**:
`mlruns.db`를 기본 `backend-store-uri`로 사용하는 스크립트를 작성
    ```bash
    mlflow server --backend-store-uri sqlite:///mlruns.db --default-artifact-root ./artifa
    ```
## **5. 데이터베이스 구조**
SQLite에 저장된 MLflow 데이터베이스는 다음과 같은 주요 테이블을 포함
### 주요 테이블
| 테이블 이름 | 설명 |
| --- | --- |
| `experiments` | 실험 ID, 이름, 상태 등의 정보. |
| `runs` | 실행(run) ID, 상태, 시작/종료 시간. |
| `metrics` | 실행(run)에 기록된 메트릭. |
| `params` | 실행(run)에 기록된 하이퍼파라미터. |
| `tags` | 실행(run)에 추가된 태그. |
### 예제: 실험 목록 확인
```sql
SELECT * FROM experiments;
```
### 예제: 실행(run) 정보 확인
```sql
SELECT * FROM runs;
```
## **1. SQLite vs PostgreSQL: 주요 차이**
| 특성 | **SQLite** | **PostgreSQL** |
| --- | --- | --- |
| **구조** | 파일 기반 (로컬 파일 `.db`로 저장) | 클라이언트-서버 기반 (DB 서버가 별도로 필요) |
| **설치 및 설정** | 매우 간단, 의존성 없이 동작 | 서버 설정 및 관리 필요 |
| **성능** | 소규모 트랜잭션 및 읽기/쓰기 작업에서 빠름 | 대규모 데이터와 복잡한 쿼리에서 뛰어난 성능 |
| **동시성** | 기본적으로 단일 쓰기 프로세스와 다중 읽기 프로세스 지원. 동시 쓰기에는 제약이 있음 | 다중 클라이언트 동시 읽기/쓰기 지원 |
| **데이터 무결성** | 제한적. 간단한 무결성 규칙 적용 가능 | 강력한 데이터 무결성 및 ACID 준수 |
| **확장성** | 제한적. 단일 파일로 데이터 관리 | 매우 확장 가능. 수백 GB~TB 규모의 데이터 처리 가능 |
| **지원 기능** | 기본적인 SQL 지원, 트리거, 인덱스 등 | 복잡한 쿼리, 함수, JSON 지원, CTE(Common Table Expression), 파티셔닝 등 고급 기능 제공 |
| **보안** | 내장 보안 기능 없음. 파일 권한에 의존 | 사용자 인증, 권한 제어, 데이터 암호화 등 보안 기능 제공 |
| **호환성** | 임베디드 애플리케이션과 가볍게 연동 | 엔터프라이즈 환경, 다중 사용자 및 복잡한 비즈니스 로직 구현 |