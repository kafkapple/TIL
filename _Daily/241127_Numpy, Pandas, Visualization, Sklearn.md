# Python library
## **0. 주요 활용법 요약**
### **2.1. Numpy**
| **기능** | **코드 예시** |
| --- | --- |
| 난수 생성 및 데이터 샘플링 | `np.random.choice(len(data.columns))` |
| SVD 수행 | `U, singular_values, V = np.linalg.svd(matrix)` |
| 행렬 랭크 계산 | `rank = np.linalg.matrix_rank(matrix)` |
| 거리 계산 및 군집화 | `distances = np.linalg.norm(X - centroid, axis=-1)` |
---
### **2.2. Pandas**
| **기능** | **코드 예시** |
| --- | --- |
| 결측치 처리 | `.fillna(0, inplace=True)`, `.dropna(axis=0, inplace=True)` |
| 피벗 테이블 생성 | `rating_data.pivot_table('rating', index='userId', columns='movieId')` |
| 날짜 데이터 변환 | `data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')` |
---
### **2.3. Matplotlib**
| **기능** | **코드 예시** |
| --- | --- |
| 단일 히스토그램 시각화 | `plt.hist(data_malignant[:, feature_idx], bins=20, alpha=0.3)` |
| 다변량 히스토그램 시각화 | `for feature_idx in range(30): plt.hist(data[:, feature_idx])` |
---
### **2.4. Seaborn**
| **기능** | **코드 예시** |
| --- | --- |
| 박스플롯 시각화 | `sns.boxplot(data=data, y=target_feature)` |
| 상관행렬 히트맵 | `sns.heatmap(data=corr, annot=True, fmt='.2f', mask=mask, cmap='RdYlBu_r')` |
| 데이터 변환 전후 분포 비교 | `sns.histplot(data=data, x=target_feature, kde=True)` |
---
### **2.5. Plotly**
| **기능** | **코드 예시** |
| --- | --- |
| 애니메이션 산점도 시각화 | `px.scatter(df, x="X", y="Y", animation_frame="iter", color="cluster_idx")` |
---
### **2.6. Scikit-learn**
| **기능** | **코드 예시** |
| --- | --- |
| 데이터 스케일링 | `StandardScaler().fit_transform(data[[target_feature]])`, `MinMaxScaler().fit_transform(data[[target_feature]])` |
| PCA | `PCA(n_components=2).fit(data)` |
| K-Means 군집화 | `KMeans(n_clusters=3, random_state=0).fit(X)` |
---
## **1. Numpy (np)**
### **1.1. 난수 생성 및 데이터 샘플링**
- np.random.choice
```python
import numpy as np
# 데이터 컬럼 중 랜덤으로 하나 선택
selected_column = np.random.choice(len(data.columns))
print("Selected Column Index:", selected_column)
```
### **1.2. 상관행렬 마스크 생성**
```python
# 상관행렬 마스크 생성 (상삼각행렬만 마스킹)
mask = np.ones_like(corr, dtype=bool)  # 전체 True로 초기화
mask = np.triu(mask)  # 상삼각형 부분만 유지
```
### **1.3. 선형 간격 배열 생성**
```python
# x_min에서 x_max까지 10개의 균일한 값 생성
x = np.linspace(x_min, x_max, 10)
print("Generated Points:", x)
```
### **1.4. Singular Value Decomposition (SVD)**
```python
# 행렬 분해
U, singular_values, V = np.linalg.svd(matrix)
print("U:\n", U)
print("Singular Values:\n", singular_values)
print("V:\n", V)
# 행렬의 랭크 계산
rank = np.linalg.matrix_rank(matrix)
print("Matrix Rank:", rank)
# sklearn library
U, sigma, Vt = svds(centered_user_movie_rating.to_numpy(), k=12)
```
### **1.5. 거리 계산 및 군집화**
```python
# 각 데이터 포인트와 군집 중심 간 거리 계산
diff = X.reshape(-1, 1, 2) - centroid  # 데이터와 중심 간 차이
distances = np.linalg.norm(diff, axis=-1)  # 유클리드 거리 계산
clusters = np.argmin(distances, axis=-1)  # 가장 가까운 중심으로 할당
print("Cluster Assignments:", clusters)
```
---
## **2. Pandas**
.value_counts() # sample per col
(df[’col’]<0).any() # 음수값 하나라도 있는지
print("데이터 타입: ", data['str_date'].dtype)
### **2.1. 데이터프레임 구조 및 요약 통계**
```python
import pandas as pd
print("Dataframe Shape:", data.shape)
# 요약 통계
print(data.describe())
data.info() #컬럼에 대한 기본 정보
```
### **2.2. 결측치 처리**
```python
indices_with_nan = df.isnull().sum(axis=1) > 0 #nan 행에 하나라도 있는 인덱스
print("Rows with NaN:", indices_with_nan)
# 결측치 채우기
df.fillna(0, inplace=True)
# 결측치 포함 행 제거
df.dropna(axis=0, inplace=True)
display(OHLCV_data[OHLCV_data["Change"].isna() == True])
# 모든 컬럼은 Non-Null의 개수가 같으나, 다른 경우가 있다면 결측치가 있다는 것을 의미
```
### **2.3. 데이터 필터링 및 분석**
```python
# 특정 열의 음수 값 확인
has_negative_values = (df['col'] < 0).any()
print("Has Negative Values:", has_negative_values)
# 분위수 계산 (0.75 분위)
q75 = df['col'].quantile(0.75)
print("75th Percentile:", q75)
```
### **2.4. 피벗 테이블 생성**
- pivot_table
    - 데이터 column 중에서
        - 행, 열로 사용할 두 개를 골라 각각을 축으로 데이터를 펼쳐두는 기능
```python
# 사용자와 영화별 평점 피벗 테이블 생성
user_movie_rating = rating_data.pivot_table('rating', index='userId', columns='movieId')
print(user_movie_rating.head())
```
### **2.5. 그룹화 및 집계**
- groubby(’묶을 대상”)[’관심 컬럼’].agg([계산할 통계량])
```python
# 영화별 평점 개수와 평균
rating_stats = rating_data.groupby('movieId')['rating'].agg(['count', 'mean'])
print(rating_stats)
```
### **2.6. 날짜 데이터 변환 및 추출**
```python
# 날짜 데이터 변환
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
# 날짜에서 "일" 정보 추출
days = data['date'].dt.day
print("Days:", days.head())
# 날짜에서 "요일" 정보 추출
weekdays = data['date'].dt.dayofweek
print("Weekdays:", weekdays.head()
```
## **3. 시각화 (Visualization)**
### **3.1. Matplotlib**
**악성/양성 샘플 히스토그램**
```python
import matplotlib.pyplot as plt
plt.hist(data_malignant[:, feature_idx], bins=20, alpha=0.3, label="Malignant")
```
**모든 변수에 대해 히스토그램 시각화**
```python
plt.figure(figsize=[20, 15])
for feature_idx in range(30):  # 변수 30개
    plt.subplot(6, 5, feature_idx + 1)
    plt.hist(data_malignant[:, feature_idx], bins=20, alpha=0.3, label="Malignant")
    plt.hist(data_benign[:, feature_idx], bins=20, alpha=0.3, label="Benign")
    plt.title(cancer["feature_names"][feature_idx])
    if feature_idx == 0:
        plt.legend(cancer["target_names"])
    plt.xticks([])
plt.show(
```
---
### **3.2. Seaborn**
**박스플롯**
```python
import seaborn as sns
sns.boxplot(data=data, y=target_feature)
plt.title("Boxplot of Target Feature")
plt.show()
```
**히스토그램 (로그 스케일 적용)**
```python
sns.histplot(data=data, x=target_feature, log_scale=(False, True))
plt.title("Histogram with Log Scale")
plt.show()
```
**막대그래프 (카테고리별 평균)**
```python
barplot = sns.barplot(data=data, x=category_feature, y=target_feature, color='C0', errorbar=None)
plt.xticks(rotation=90)  # 카테고리 라벨 회전
plt.title("Category-wise Average")
plt.show()
```
**상관행렬 히트맵**
```python
sns.heatmap(data=corr, annot=True, fmt=".2f", mask=mask, linewidths=0.5, cmap="RdYlBu_r")
plt.title("Correlation Matrix")
plt.show()
```
**로그 변환 전후 분포 비교**
```python
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
sns.histplot(data=data, x=target_feature, kde=True, ax=ax[0])
ax[0].set_title('Before Log Transformation')
sns.histplot(data=data, x=f'log_{target_feature}', kde=True, ax=ax[1])
ax[1].set_title('After Log Transformation')
plt.show()
```
---
### **3.3. Plotly**
**애니메이션을 활용한 산점도**
```python
import plotly.express as px
fig = px.scatter(
    df,
    x="X", y="Y",
    animation_frame="iter",
    color="cluster_idx",
    size="label_size",
    symbol="label",
    width=1000, height=800,
    symbol_sequence=['circle', 'star']
)
fig.update_coloraxes(showscale=False)
fig.show(
```
---
## **4. Scikit-learn**
### **4.1. 데이터 스케일링**
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# 표준화 (평균=0, 분산=1)
standard_scaler = StandardScaler()
data['standardized_feature'] = standard_scaler.fit_transform(data[[target_feature]])
# 정규화 (0~1 범위)
normalized_scaler = MinMaxScaler()
data['normalized_feature'] = normalized_scaler.fit_transform(data[[target_feature]])
```
---
### **4.2. PCA (주성분 분석)**
```python
from sklearn.decomposition import PCA
# PCA로 차원 축소
pca_estimator = PCA(n_components=2, svd_solver="full", whiten=True)
pca_estimator.fit(faces_centered)
# 주요 특성
print("Singular Values:", pca_estimator.singular_values_
```
---
### **4.3. t-SNE**
```python
from sklearn.manifold import TSNE
# t-SNE로 데이터 시각화용 2차원 축소
transformer = TSNE(n_components=2, random_state=0)
transformed_data = transformer.fit_transform(data)
```
---
### **4.4. K-Means 군집화**
```python
from sklearn.cluster import KMeans
# 데이터에 대해 K-Means 군집화
kmeans_clustering = KMeans(n_clusters=3, n_init="auto")
kmeans_clustering.fit(X)
# 군집 라벨 및 중심
clusters = kmeans_clustering.labels_
centroid = kmeans_clustering.cluster_centers_
print("Cluster Labels:", clusters)
print("Centroid Locations:\n", centroid)
```
---
### **정리**
- **Matplotlib**: 기본적인 히스토그램, 다변량 시각화 등.
- **Seaborn**: 박스플롯, 상관행렬, 로그 변환 전후 분포 비교 등 고급 시각화.
- **Plotly**: 애니메이션 및 상호작용을 포함한 시각화.
- **Scikit-learn**: 데이터 스케일링, PCA, t-SNE, K-Means 등 ML 분석 및 전처리.