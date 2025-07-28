# MLflow Tracking server, Artifact store 연동 이슈 

# MLflow 문제 요약 및 분석

## Tracking server & Artifact Store

1. **Tracking Server**:

- HTTP를 통해 접근 (예: [http://127.0.0.1:5000](http://127.0.0.1:5000/))

- 메트릭과 파라미터 기록

2. **Artifact Store**:

- 로컬 파일 시스템 사용 (file://)

- 모델 및 아티팩트 저장

## 연동

1. **연동 구조**:

- **Tracking Server**: 메트릭, 파라미터 기록

- **Artifact Store**: 모델 및 파일 저장

- 두 시스템은 독립적으로 동작하나 연동됨

2. **파일 저장 위치**:

- **config/model_registry.json**: 모델 메타데이터 저장

- **mlruns/**: MLflow 메타데이터 저장

- **mlartifacts/**: 모델과 아티팩트 저장

- 실제 모델 위치: `Project Root /mlartifacts/{run_id}/artifacts/model/data/model.pth`

## 실행

1. **MLflow UI 실행**:

- 실행 명령어: `mlflow ui --host 127.0.0.1 --port 5050`

2. **포트 확인 및 서버 종료**:

- 포트 상태 확인: `netstat -ano | findstr :5050`

- 작동 중인 서버 종료: `pkill -f "mlflow"`

# **현재 문제**

## **요약**

- **경로 관리 문제**

- MLflow가 사용하는 경로는 URI 스키마(`file://`, `http://` 등)로 지정해야 함.

- 현재 Windows 절대 경로(`E:\...`)가 사용되며, MLflow의 URI 스키마와 충돌 발생.

- Windows 백슬래시(`\`)와 Unix 슬래시(`/`) 혼용 문제.

- **Server-Client 설정 불일치**

- Server와 Client 측에서 사용하는 URI 형식이 다름.

- 상대 경로와 절대 경로 혼용으로 경로 해석 오류 발생.

- **Artifact 저장 방식 문제**

- `log_model` 함수에서 절대 경로 URI(`file:///E:/...`) 사용 시 충돌.

- MLflow는 상대 경로로 아티팩트를 관리하는 것을 기본으로 기대.

---

## **기존 시도 및 문제점**

1. **시도한 해결 방안**

- 모든 경로를 URI 형식(`file:///path`)으로 변환.

- 경로 구분자 통일(`/` 사용).

- MLflow 서버와 클라이언트 설정을 일치하려 시도.

2. **문제가 지속된 원인**

- Windows 경로의 드라이브 문자(`E:`) 처리 미흡.

- Server와 Client가 서로 다른 설정 사용.

- 상대 경로와 절대 경로가 혼용된 상태로 동작.

---

# **개선 방안**

| **문제 영역** | **원인 분석** | **개선 방안** |

| --- | --- | --- |

| **URI 스키마 불일치** | 경로 형식(`E:\...`)이 URI 스키마와 다름 | 모든 경로를 `file:///` 형식으로 변환 (예: `file:///E:/path`). |

| **경로 구분자 문제** | Windows(`\`)와 Unix(`/`) 혼용 | 경로 구분자를 포워드 슬래시(`/`)로 통일. |

| **Server-Client 설정 차이** | Server/Client URI 설정 불일치 | Server와 Client 모두 같은 URI 형식을 사용하도록 설정. |

| **Artifact 저장 문제** | 절대 경로 사용이 상대 경로 예상과 충돌 | Artifact 저장 시 상대 경로(`artifacts/model`)로 지정. |

| **드라이브 문자 처리** | 드라이브 문자(`E:`) 처리 미흡 | 드라이브 문자를 대문자와 콜론(`:`) 포함 형태로 유지 (`file:///E:/path`). |

---

## **추천 설정 및 운영 방안**

1. **경로 관리 표준화**

- 모든 경로를 URI 형식으로 관리.

```python

import pathlib

path = pathlib.Path("E:/mlartifacts")

uri = path.as_uri() # Outputs: 'file:///E:/mlartifacts'

```

2. **Server/Client 통일**

- Tracking Server와 Artifact Store 모두 URI 스키마를 명확히 지정.

```bash

mlflow server \

--backend-store-uri file:///E:/mlruns \

--default-artifact-root file:///E:/mlartifacts

```

3. **Artifact 로깅 규칙**

- `log_model` 및 `log_artifact` 사용 시 상대 경로 지정:

```python

mlflow.log_model(model, "artifacts/model")

```

4. **Windows 드라이브 문자 처리**

- MLflow 내부에서 경로 변환 로직을 개선:

```python

import re

def normalize_path(path):

if re.match(r'^[a-zA-Z]:\\', path):

return pathlib.Path(path).as_uri()

return path

```

---

### **5. 추가 학습 및 질문**

1. **MLflow 내부 동작 원리**

- 경로 관리와 관련된 MLflow API 내부 구현 분석.

- `mlflow.store.artifact` 모듈에서 URI 파싱 로직 확인.

2. **Artifact Store 및 Tracking Server 분리 운영**

- Tracking Server를 HTTP로 두고, Artifact Store를 클라우드(S3)로 이전 가능 여부.

3. **MLflow와 운영 환경 통합**

- 로컬 환경 외에 Docker 컨테이너 또는 클라우드 환경에서의 MLflow 구성.