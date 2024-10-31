
import os

def update_readme():
    til_content = "## Today I Learned\n\n"
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                file_path = os.path.join(root, file)
                til_content += f"- [{file}]({file_path})\n"
    
    with open("README.md", "w") as f:
        f.write(til_content)

if __name__ == "__main__":
    update_readme()
    print("README.md has been updated.")  # 디버깅을 위한 출력