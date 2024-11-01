
# Quiz 2
1. X: PCA, clustering → 비지도
2. X: Logistic regression → classification
3. 상관관계 분석 기본 가정 아닌 것은? → 비선형성
4. **O: PCA 로 M→ N dim reduc 시 선택하는 SVD comp 수는 N**
5. **O: k-means cluster centroid = average of the samples allocated**

# ML Process

5 단계
- Data collection
- Data preprocessing
  - EDA
  - 문제 처리
    - 결측치
    - 이상치
  - 변수 처리
    - 연속형
    - 범주형
- Feature engineering 파생 변수 생성
  - 함수 변환, scaling 등
  - 단순 합성 아닌, 문제 도메인 지식 연관
- 변수 선택
- Deploy

# Programming
    - Refactoring 체계 정리 중
        - [Refactoring](https://www.notion.so/Refactoring-12f596a3652f80d184fbeaff6e292cff?pvs=21)
    - python 환경 관리 pip / conda environment setup
        - pip: pip freeze > .txt / pip install -r .txt
            
            ```
            pip freeze > requirements.txt
            전체 기록
            pip list --format=freeze > requirements.txt
            패키지 이름과 버전만이 기록
            pip install -r requirements.txt
            ```
            
        - conda: conda env  export > .yml / conda env create -f .yml
            
            ```
            conda env export > environment.yml
            conda env create -f environment.yml
            ```
            
- **Git**
    - [Github Process Routine](https://www.notion.so/Github-Process-Routine-12f596a3652f80cd9b09dcecc39721d7?pvs=21) 정리 및 실습 중
    - 정리 중
        - Leader/member 역할
        - Trouble shooting