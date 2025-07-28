데이터 분석 전 데이터 타입 변환 및 결측치 확인/처리는 필수적인 전처리 과정

### 1. 데이터 타입 변환 (Data Type Conversion)

#### 1.1 object 타입에서 string 타입으로 변환

- **목적**: Pandas 문자열 메서드(.str) 활용성 증대

- **코드 예시**: df.astype({col: 'string' for col in df.select_dtypes(include='object').columns})

- **장점**:

- Pandas의 일관된 문자열 메서드 활용

- 결측치 <NA>로 표준화

### 2. 결측치 확인 (Missing Value Inspection)

#### 2.1 결측치 포함 열 확인

- **목적**: 결측치가 존재하는 열 식별

- **코드 예시**: df.columns[df.isnull().any()].tolist()

- **결과**: 결측치 포함 열 이름 리스트 반환

#### 2.2 결측치 비율 확인

- **목적**: 각 열의 결측치 비중 파악

- **코드 예시**: df.isnull().sum() / len(df) * 100

- **결과**: 결측치 비율이 0보다 큰 열만 표시

### 3. 결측치 처리 (Missing Value Handling)

#### 3.1 열/행 제거 (Dropping Rows/Columns)

- **열 제거**: df.dropna(axis=1, how='any', inplace=True)

- **행 제거**: df.dropna(axis=0, how='any', inplace=True)

- **원리**: 결측치가 포함된 열 또는 행을 데이터셋에서 제거

#### 3.2 결측치 채우기 (Filling Missing Values)

- **특정 값으로 채우기**: df.fillna(0, inplace=True)

- **열별 평균값으로 채우기**: df.fillna(df.mean(), inplace=True)

- **원리**: 결측치를 특정 값, 통계량(평균, 중앙값 등)으로 대체

#### 3.3 조건 기반 및 문자열 열 처리 (Conditional & String Column Handling)

- **조건 기반 대체**: df['column_name'].apply(lambda x: 0 if pd.isnull(x) else x)

- **문자열 열 빈 문자열 대체**: df.update(df.select_dtypes(include='string').fillna(''))

- **원리**: 특정 조건에 따라 결측치를 처리하거나, 문자열 타입의 결측치를 빈 문자열로 대체