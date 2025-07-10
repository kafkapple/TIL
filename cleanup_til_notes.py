import os
import re
import sys

# --- 설정 ---
TARGET_DIR = "/home/joon/dev/TIL"

# --- 정리 함수 (sync_til.py와 동일) ---
def clean_obsidian_boilerplate(content):
    """Obsidian 관련 보일러플레이트(메타데이터, Dataview 쿼리 등)를 제거합니다."""
    # 1. Area: [[...]] (ID: ...)
    content = re.sub(r"^Area: .*\n", "", content, flags=re.MULTILINE)
    # 2. Metadata block
    content = re.sub(r"^Metadata\n(Created Date: .*\n)?(Category: .*\n)?(ID: .*\n)?", "", content, flags=re.MULTILINE)
    # 3. Area Notes & Recent Notes Dataview blocks
    content = re.sub(r"^(?:Area|Recent) Notes\nTABLE[\s\S]*?LIMIT 5\n", "", content, flags=re.MULTILINE)
    # 제거 후 남는 연속적인 빈 줄들을 하나로 줄입니다.
    content = re.sub(r'\n\s*\n', '\n', content)
    return content.strip()

def cleanup_markdown_files(directory):
    """지정된 디렉토리의 모든 마크다운 파일 내용을 정리합니다."""
    print(f"지정된 디렉토리: {directory}")
    print("마크다운 파일 정리를 시작합니다...")
    
    file_count = 0
    cleaned_count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                file_count += 1
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    cleaned_content = clean_obsidian_boilerplate(original_content)
                    
                    # 변경 사항이 있을 경우에만 파일을 다시 씁니다.
                    if original_content != cleaned_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(cleaned_content)
                        print(f"  - 정리 완료: {os.path.basename(file_path)}")
                        cleaned_count += 1

                except Exception as e:
                    print(f"  - 오류 발생 {os.path.basename(file_path)}: {e}")

    print("\n정리 작업 요약:")
    print(f"- 총 검사한 마크다운 파일: {file_count}개")
    print(f"- 내용이 변경된 파일: {cleaned_count}개")
    if cleaned_count == 0:
        print("모든 파일이 이미 깨끗한 상태입니다.")
    else:
        print(f"{cleaned_count}개의 파일에서 불필요한 내용을 제거했습니다.")


if __name__ == "__main__":
    # 사용자가 스크립트 실행 시 --force 플래그를 사용하도록 하여
    # 실수로 실행하는 것을 방지합니다.
    if "--force" not in sys.argv:
        print("주의: 이 스크립트는 TIL 폴더 내의 모든 .md 파일을 직접 수정합니다.")
        print("파일을 직접 수정하시려면 `--force` 옵션을 추가하여 실행해주세요.")
        print("예: python3 cleanup_til_notes.py --force")
        sys.exit(1)
        
    if os.path.isdir(TARGET_DIR):
        cleanup_markdown_files(TARGET_DIR)
    else:
        print(f"오류: 대상 디렉토리 '{TARGET_DIR}'를 찾을 수 없습니다.")