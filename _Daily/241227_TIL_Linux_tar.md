# Linux_tar

# 241227 linux tar 압축
-c # 압축
-x # 해제
## 압축
tar -czvf 파일명.tar.gz 폴더명
• `-c`: 새로운 아카이브 생성
• `-z`: gzip으로 압축
• `-v`: 진행 상황 표시
• `-f`: 파일 이름 지정
## 해제
tar -xzvf 파일명.tar.gz
tar -xzvf 파일명.tar.gz -C 경로명