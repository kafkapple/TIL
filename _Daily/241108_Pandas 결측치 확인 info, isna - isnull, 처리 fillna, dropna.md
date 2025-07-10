### 1. **`isna` vs `isnull`**
- **차이**:
    - `isna`와 `isnull`은 사실상 **동일**
    - 둘 다 결측치를 확인하기 위한 메서드이며, Pandas에서는 `isnull`이 내부적으로 `isna`를 호출하는 방식으로 구현
- **선택 기준**:
    - `isna`는 Pandas에서 더 직관적으로 이해할 수 있는 이름으로 추가된 함수
    - `isnull`은 오래된 코드나, `scikit-learn`과 같은 라이브러리에서의 사용과 호환성을 위해 여전히 널리 사용
---
### 2. **결측치 처리 방법**
### (1) **결측치 확인**
```python
# 데이터프레임의 모든 결측치를 True/False로 반환
df.isna()  # 또는 df.isnull()
# 결측치의 개수 확인
df.isna().sum()  # 각 열에서 결측치 개수
df.isna().sum(axis=1)  # 각 행에서 결측치 개수
```
### (2) **결측치 포함 행/열 찾기**
```python
# 결측치가 하나라도 있는 행/열 확인
indices_with_nan = df.isnull().sum(axis=1) > 0
print("Rows with NaN:", indices_with_nan)
```
### (3) **결측치 채우기**
- **`fillna(value)`**
    - 결측치를 특정 값으로 채움.
    ```python
    df.fillna(0, inplace=True)  # 모든 결측치를 0으로 대체
    ```
- **`ffill` / `bfill`**
    - 결측치를 앞 또는 뒤 값으로 채움.
    ```python
    df.fillna(method='ffill', inplace=True)  # 이전 값으로 채움
    df.fillna(method='bfill', inplace=True)  # 다음 값으로 채움
    ```
### (4) **결측치 포함 행/열 제거**
- **`dropna`**
    ```python
    df.dropna(axis=0, inplace=True)  # 결측치 포함 행 제거
    df.dropna(axis=1, inplace=True)  # 결측치 포함 열 제거
    ```
### (5) **특정 조건 확인**
- 특정 열에서 결측치가 있는 행 필터링:
    ```python
    OHLCV_data[OHLCV_data["Change"].isna() == True]
    ```
---
### 3. **결측치 처리를 위한 팁**
- 모든 열의 **Non-Null 개수**가 같지 않다면, 특정 열에 결측치가 포함되어 있을 가능성
    ```python
    df.info()  # Non-Null 개수 확인
    ```
---
### 4. **장단점 비교**
| 메서드 | 장점 | 단점 |
| --- | --- | --- |
| `isna`, `isnull` | 직관적이고 Pandas에서 기본적으로 지원. | 대규모 데이터에서는 계산 비용이 증가할 수 있음. |
| `fillna` | 결측치를 다른 값으로 쉽게 대체 가능 (`0`, 평균, 중위값 등). | 적절하지 않은 값으로 채우면 통계적 왜곡 발생 가능. |
| `dropna` | 결측치 있는 데이터를 깔끔하게 제거. | 데이터가 많이 손실될 수 있음. |
| `ffill`, `bfill` | 시계열 데이터에서 결측치를 시간 흐름에 따라 쉽게 채움. | 앞뒤 값으로 채워야 하는 데이터가 아닌 경우, 의미 없는 값으로 대체될 수 있음. |
| `indices_with_nan` | 결측치가 있는 행/열의 인덱스를 명확히 알 수 있음. | 결과를 조작하거나 다른 메서드로 결합하는 과정이 필요할 수 있음. |
---
### 5. **결측치 처리 전략**
- 결측치가 많지 않다면 `dropna` 사용.
- 시계열 데이터는 `ffill`/`bfill` 사용.
- 통계적 분석 시 평균/중위값으로 채우기 (`fillna`).
- 머신러닝 모델 적용 전에는 결측치 처리 후 이상치 확인 권장.