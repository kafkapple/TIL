import os
import re
import sys

# --- 설정 ---
TARGET_DIR = "/home/joon/dev/TIL"

# --- 최종 정리 함수 ---
def clean_obsidian_boilerplate(content):
    """Obsidian 관련 보일러플레이트(마크다운, 메타데이터, Dataview 쿼리 등)를 모두 제거합니다."""
    
    # 1. Area 라인 제거 (마크다운 강조, 공백 등 변형 고려)
    content = re.sub(r"^\*\*?Area\*\*?:.*\(ID: .*\)\s*\n?", "", content, flags=re.MULTILINE)

    # 2. Metadata, Area Notes, Recent Notes 블록 전체를 한 번에 제거
    #    - `## Metadata`로 시작해서 dataview 코드 블록의 끝(` ``` `)까지를 하나의 패턴으로 인식
    content = re.sub(r"\n## Metadata[\s\S]*?```\s*", "", content, flags=re.DOTALL)

    # 정리 후 상단과 하단의 불필요한 공백을 모두 제거합니다.
    return content.strip()

def cleanup_markdown_files(directory):
    """지정된 디렉토리의 모든 마크다운 파일 내용을 정리합니다."""
    print(f"지정된 디렉토리: {directory}")
    print("마크다운 파일 정리를 시작합니다 (최종 로직 적용)...")
    
    file_count = 0
    cleaned_count = 0

    for root, _, files in os.walk(directory):
        if ".git" in root.split(os.sep):
            continue
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                file_count += 1
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        original_content = f.read()
                    
                    cleaned_content = clean_obsidian_boilerplate(original_content)
                    
                    if original_content != cleaned_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(cleaned_content)
                        print(f"  - 정리 완료: {os.path.relpath(file_path, directory)}")
                        cleaned_count += 1

                except Exception as e:
                    print(f"  - 오류 발생 {os.path.basename(file_path)}: {e}")

    print("\n정리 작업 요약:")
    print(f"- 총 검사한 마크다운 파일: {file_count}개")
    print(f"- 내용이 변경된 파일: {cleaned_count}개")
    if cleaned_count == 0:
        print("모든 파일이 이미 깨끗한 상태이거나, 추가로 정리할 파일이 없습니다.")
    else:
        print(f"{cleaned_count}개의 파일에서 불필요한 내용을 최종적으로 제거했습니다.")


if __name__ == "__main__":
    if "--force" not in sys.argv:
        print("주의: 이 스크립트는 TIL 폴더 내의 모든 .md 파일을 직접 수정합니다.")
        print("파일을 직접 수정하시려면 `--force` 옵션을 추가하여 실행해주세요.")
        print("예: python3 cleanup_til_notes.py --force")
        sys.exit(1)
        
    if os.path.isdir(TARGET_DIR):
        cleanup_markdown_files(TARGET_DIR)
    else:
        print(f"오류: 대상 디렉토리 '{TARGET_DIR}'를 찾을 수 없습니다.")