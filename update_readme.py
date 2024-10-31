import os

def update_readme():
    til_content = "## Today I Learned\n\n"
    
    # TIL 디렉토리 내의 파일들을 순회
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                # 파일 경로와 이름을 README에 추가
                file_path = os.path.join(root, file)
                til_content += f"- [{file}]({file_path})\n"
    
    # README.md 파일 업데이트
    with open("README.md", "r+") as f:
        content = f.read()
        f.seek(0)
        f.write(til_content + "\n" + content)
        f.truncate()

if __name__ == "__main__":
    update_readme()