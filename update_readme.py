import os

def update_readme():
    til_content = "# Today I Learned\n\n"

    for root, dirs, files in os.walk("."):
        # 루트 경로를 현재 디렉토리명으로 나누어 계층을 파악
        depth = root.count(os.sep)
        if depth > 0:  # 최상위 루트 제외
            folder_name = os.path.basename(root)
            heading = "#" * (depth + 1)  # 계층에 맞게 헤딩 레벨 설정
            til_content += f"{heading} {folder_name}\n\n"
        
        for file in files:
            if file.endswith(".md") and file != "README.md":
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, ".")  # 상대 경로로 저장
                til_content += f"- [{file}]({relative_path})\n"
        
        til_content += "\n"  # 폴더 간 구분을 위한 개행

    with open("./README.md", "w", encoding='utf-8') as f:
        f.write(til_content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")
