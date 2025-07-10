import os
import re

# --- 정규식 ---
DATE_PREFIX_REGEX = re.compile(r"^(?:\d{8}|\d{6})_.*\.md$")
TIL_TAG_REGEX = re.compile(r"tags:.*til", re.IGNORECASE)
FRONTMATTER_REGEX = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)

# --- 설정 ---
SOURCE_FOLDERS = ["10_Daily", "30_Projects", "40_Areas"]
TARGET_DAILY_FOLDER = "_Daily"

def clean_obsidian_boilerplate(content):
    """Obsidian 관련 보일러플레이트(마크다운, 메타데이터, Dataview 쿼리 등)를 모두 제거합니다."""
    # 1. ```dataview ... ``` 코드 블록 제거 (가장 먼저 처리)
    content = re.sub(r"```dataview[\s\S]*?```", "", content, flags=re.DOTALL)

    # 2. 코드 블록 없는 dataview 쿼리 제거 (e.g. "제품dataview TABLE...")
    # 'dataview' 앞에 다른 문자가 붙어있을 수 있는 경우까지 고려
    content = re.sub(r"\S*dataview\s+TABLE[\s\S]*?LIMIT\s+\d+", "", content, flags=re.IGNORECASE | re.DOTALL)

    # 3. Area 라인 제거 (e.g. **Area**: ... (ID: ...))
    content = re.sub(r"^\*\*?Area\*\*?:.*\(ID: .*\)\s*\n?", "", content, flags=re.MULTILINE)

    # 4. Dataview 제거 후 남은 헤딩 제거 (## Metadata, ## Recent Notes 등)
    content = re.sub(r"^\s*## (Metadata|Area Notes|Recent Notes)\s*$", "", content, flags=re.MULTILINE)

    # 5. 모든 제거 작업 후, 여러 개의 빈 줄을 하나의 빈 줄로 줄이고 양 끝 공백 제거
    content = re.sub(r'(\n\s*){2,}', '\n\n', content).strip()
    
    return content

def discover_til_notes(vault_path):
    print("-> TIL 노트 탐색 중...")
    valid_notes = []
    search_paths = [os.path.join(vault_path, d) for d in SOURCE_FOLDERS]
    for path in search_paths:
        if not os.path.isdir(path): continue
        for root, _, files in os.walk(path):
            for file in files:
                if not DATE_PREFIX_REGEX.match(file): continue
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 파일의 앞부분만 읽어 태그를 빠르게 확인
                        if TIL_TAG_REGEX.search(f.read(500)):
                            valid_notes.append(file_path)
                except Exception as e:
                    print(f"  - 파일 읽기 오류 {file_path}: {e}")
    print(f"   총 {len(valid_notes)}개의 유효한 TIL 노트를 발견했습니다.")
    return valid_notes

def sync_new_notes(til_notes, repo_path):
    print("-> 새로운 노트 동기화 중...")
    synced_count = 0
    target_base_dir = os.path.join(repo_path, TARGET_DAILY_FOLDER)
    if not os.path.exists(target_base_dir):
        os.makedirs(target_base_dir)

    for source_path in til_notes:
        filename = os.path.basename(source_path)
        target_path = os.path.join(target_base_dir, filename)

        # 원본 파일이 타겟 파일보다 최신일 경우에만 동기화
        if not os.path.exists(target_path) or \
           os.path.getmtime(source_path) > os.path.getmtime(target_path):
            
            try:
                with open(source_path, 'r', encoding='utf-8') as f_source:
                    content = f_source.read()
                
                content_without_frontmatter = FRONTMATTER_REGEX.sub('', content, count=1)
                cleaned_content = clean_obsidian_boilerplate(content_without_frontmatter)

                with open(target_path, 'w', encoding='utf-8') as f_target:
                    f_target.write(cleaned_content)

                print(f"  - 복사 및 정리 완료: {filename}")
                synced_count += 1
            except Exception as e:
                print(f"  - 동기화 오류 {filename}: {e}")

    if synced_count == 0:
        print("   새롭게 변경된 노트가 없습니다.")
    else:
        print(f"   총 {synced_count}개의 파일을 동기화했습니다.")
    return True
