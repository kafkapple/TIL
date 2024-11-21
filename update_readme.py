import os
def update_readme():
    # README 파일의 시작 부분 텍스트 설정
    til_content = "# Today I Learned\n\n"
    # os.walk를 사용해 현재 디렉토리(".")부터 모든 하위 폴더를 순회
    for root, dirs, files in os.walk("."):
        # 현재 폴더에 있는 파일 중 .md 파일만 필터링
        md_files = [file for file in files if file.endswith(".md") and file != "README.md"]
        
        # 폴더의 깊이를 계층 구조에 반영
        depth = root.count(os.sep)
        # 현재 폴더 이름 추출
        folder_name = os.path.basename(root)
        
        # MD_Daily 폴더에만 년도, 월 그룹화 적용
        if folder_name == "MD_Daily":
            # 계층에 따라 헤딩 레벨 설정 (최상위: #, 하위: ##, 하위 하위: ### ...)
            heading = "#" * (depth + 1)
            # 폴더명에 맞는 헤딩 추가
            til_content += f"{heading} {folder_name}\n\n"
            
            # 날짜와 제목 기준으로 내림차순 정렬 (날짜 우선)
            sorted_md_files = sorted(md_files, key=lambda x: x.split('_')[0], reverse=True)
            
            # 년도와 월을 추적할 변수
            current_year = None
            current_month = None
            
            # 현재 폴더의 각 .md 파일을 처리
            for file in sorted_md_files:
                # 파일명에서 날짜와 제목 분리
                date_part = file.split('_')[0]
                title_part = file.split('_')[1].split('.')[0] if '_' in file else ''
                
                # 날짜에서 년도와 월 추출
                year = '20' + date_part[:2]
                month = date_part[2:4]
                
                # 년도가 바뀌면 년도 헤더 추가
                if year != current_year:
                    til_content += f"### {year}년\n"
                    current_year = year
                    current_month = None
                
                # 월이 바뀌면 월 헤더 추가
                if month != current_month:
                    til_content += f"#### {month}월\n"
                    current_month = month
                
                # 상대 경로로 링크를 생성해 파일명과 제목과 함께 추가
                relative_path = os.path.relpath(os.path.join(root, file), ".")
                til_content += f"- [{date_part} {title_part}]({relative_path})\n"
            
            # 폴더 간 구분을 위한 개행 추가
            til_content += "\n"
        
        # 다른 폴더들 (ML 폴더 등)은 기존 방식으로 처리
        elif md_files:
            # 계층에 따라 헤딩 레벨 설정 (최상위: #, 하위: ##, 하위 하위: ### ...)
            heading = "#" * (depth + 1)
            # 폴더명에 맞는 헤딩 추가
            til_content += f"{heading} {folder_name}\n\n"
            
            # 현재 폴더의 각 .md 파일을 처리
            for file in md_files:
                # 확장자를 제외한 파일명만 추출
                file_name = os.path.splitext(file)[0]
                # 상대 경로로 링크를 생성해 파일명과 함께 추가
                relative_path = os.path.relpath(os.path.join(root, file), ".")
                til_content += f"- [{file_name}]({relative_path})\n"
            
            # 폴더 간 구분을 위한 개행 추가
            til_content += "\n"
    
    # 작성한 내용을 README.md 파일에 저장
    with open("./README.md", "w", encoding='utf-8') as f:
        f.write(til_content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")
