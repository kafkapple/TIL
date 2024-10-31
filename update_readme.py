import os

def update_readme():
    til_content = "# Today I Learned\n\n"

    for root, dirs, files in os.walk("."):
        md_files = [file for file in files if file.endswith(".md") and file != "README.md"]
        
        if md_files:  # .md 파일이 있는 폴더만 처리
            depth = root.count(os.sep)
            folder_name = os.path.basename(root)
            heading = "#" * (depth + 1)  # 계층에 맞게 헤딩 레벨 설정
            til_content += f"{heading} {folder_name}\n\n"

            for file in md_files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, ".")  # 상대 경로로 저장
                til_content += f"- [{file}]({relative_path})\n"
            
            til_content += "\n"  # 폴더 간 구분을 위한 개행

    with open("./README.md", "w", encoding='utf-8') as f:
        f.write(til_content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")
