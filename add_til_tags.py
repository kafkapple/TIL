import os
import re

# --- 설정 ---
OBSIDIAN_VAULT_PATH = "/Users/joon/Documents/Obsidian"
SOURCE_FOLDERS = ["10_Daily", "30_Projects", "40_Areas"]

# --- 정규식 ---
# 파일명에 'TIL'이 포함되고 날짜 접두사가 있는 경우
QUASI_TIL_REGEX = re.compile(r"^(?:\d{8}|\d{6})_.*TIL.*\.md$", re.IGNORECASE)
# Frontmatter 영역을 찾는 정규식
FRONTMATTER_REGEX = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# 'tags:' 라인을 찾는 정규식
TAGS_LINE_REGEX = re.compile(r"^(tags:.*)$", re.MULTILINE | re.IGNORECASE)
# 'til' 태그가 이미 있는지 확인하는 정규식
TIL_TAG_EXISTS_REGEX = re.compile(r"tags:.*til", re.IGNORECASE)

def find_quasi_til_notes():
    """'til' 태그는 없지만, 파일명 규칙 상 TIL로 의심되는 노트를 찾습니다."""
    potential_notes = []
    search_paths = [os.path.join(OBSIDIAN_VAULT_PATH, d) for d in SOURCE_FOLDERS]

    for path in search_paths:
        if not os.path.isdir(path):
            continue
        for root, _, files in os.walk(path):
            for file in files:
                if not QUASI_TIL_REGEX.match(file):
                    continue
                
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if not TIL_TAG_EXISTS_REGEX.search(content):
                            potential_notes.append(file_path)
                except Exception as e:
                    print(f"  - 파일 읽기 오류 {file_path}: {e}")
    return potential_notes

def add_til_tag_to_file(file_path):
    """파일에 'til' 태그를 추가합니다."""
    try:
        with open(file_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0) # 파일 포인터를 다시 맨 앞으로 이동

            # Case 1: Frontmatter와 tags 라인이 모두 있는 경우
            if TAGS_LINE_REGEX.search(content):
                new_content = TAGS_LINE_REGEX.sub(r"\1 til", content, count=1)
            # Case 2: Frontmatter는 있지만 tags 라인이 없는 경우
            elif FRONTMATTER_REGEX.search(content):
                new_content = FRONTMATTER_REGEX.sub(r"---\n\1\ntags: til\n---\n", content, count=1)
            # Case 3: Frontmatter가 없는 경우
            else:
                new_content = f"---\ntags: til\n---\n\n{content}"
            
            f.write(new_content)
        return True
    except Exception as e:
        print(f"  - 태그 추가 오류 {file_path}: {e}")
        return False

def main():
    print("파일명은 TIL이지만 'til' 태그가 없는 노트를 탐색합니다...")
    notes_to_update = find_quasi_til_notes()

    if not notes_to_update:
        print("\n✅ 모든 TIL 의심 노트에 이미 'til' 태그가 있습니다. 추가 작업이 필요 없습니다.")
        return

    print("\n다음 노트들에 'til' 태그를 추가할 수 있습니다:")
    for note in notes_to_update:
        print(f"  - {note}")

    user_input = input("\n위 노트들에 'til' 태그를 추가하시겠습니까? (y/n): ").lower()

    if user_input == 'y':
        print("\n태그 추가 작업을 시작합니다...")
        success_count = 0
        for note in notes_to_update:
            if add_til_tag_to_file(note):
                success_count += 1
        print(f"\n총 {success_count}개의 노트에 'til' 태그를 성공적으로 추가했습니다.")
    else:
        print("\n작업을 취소했습니다.")

if __name__ == "__main__":
    main()
