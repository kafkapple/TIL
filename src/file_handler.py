import os
import re

# --- 정규식 ---
DATE_PREFIX_REGEX = re.compile(r"^(?:\d{8}|\d{6})_.*\.md$")
TIL_TAG_REGEX = re.compile(r"category:\s*[\"']*TIL[\"']*", re.IGNORECASE)
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
    print("-> Obsidian ↔ TIL 저장소 차이 분석 및 동기화 시작...")
    
    synced_count = 0
    deleted_count = 0
    skipped_count = 0
    target_base_dir = os.path.join(repo_path, TARGET_DAILY_FOLDER)
    if not os.path.exists(target_base_dir):
        os.makedirs(target_base_dir)

    # 현재 Obsidian에 있는 파일 목록 생성 (파일명과 경로 매핑)
    obsidian_files = {}
    for path in til_notes:
        filename = os.path.basename(path)
        obsidian_files[filename] = path
    
    # TIL 저장소에 있는 기존 파일들 확인
    existing_files = set()
    if os.path.exists(target_base_dir):
        existing_files = set(f for f in os.listdir(target_base_dir) if f.endswith('.md'))
    
    print(f"📊 파일 상태 분석:")
    print(f"   Obsidian: {len(obsidian_files)}개 파일")
    print(f"   TIL 저장소: {len(existing_files)}개 파일")
    
    # 삭제 대상 파일들 (TIL에 있지만 Obsidian에 없음)
    files_to_delete = existing_files - set(obsidian_files.keys())
    # 새로 추가될 파일들 (Obsidian에 있지만 TIL에 없음)
    files_to_add = set(obsidian_files.keys()) - existing_files
    # 기존 파일들 (양쪽에 모두 있음)
    files_existing = set(obsidian_files.keys()) & existing_files
    
    print(f"🔍 변경 사항 감지:")
    print(f"   삭제 대상: {len(files_to_delete)}개")
    print(f"   신규 추가: {len(files_to_add)}개")
    print(f"   기존 파일: {len(files_existing)}개")
    
    # 1. 삭제 작업
    if files_to_delete:
        print(f"\n🗑️  삭제 작업 ({len(files_to_delete)}개):")
        for filename in sorted(files_to_delete):
            target_path = os.path.join(target_base_dir, filename)
            try:
                os.remove(target_path)
                print(f"  ❌ 삭제: {filename}")
                print(f"     경로: TIL/_Daily/{filename}")
                print(f"     이유: Obsidian에서 제거됨")
                deleted_count += 1
            except Exception as e:
                print(f"  ⚠️  삭제 실패: {filename} - {e}")
    
    # 2. 신규 추가 작업
    if files_to_add:
        print(f"\n📝 신규 추가 ({len(files_to_add)}개):")
        for filename in sorted(files_to_add):
            source_path = obsidian_files[filename]
            target_path = os.path.join(target_base_dir, filename)
            
            try:
                with open(source_path, 'r', encoding='utf-8') as f_source:
                    content = f_source.read()
                
                content_without_frontmatter = FRONTMATTER_REGEX.sub('', content, count=1)
                cleaned_content = clean_obsidian_boilerplate(content_without_frontmatter)

                with open(target_path, 'w', encoding='utf-8') as f_target:
                    f_target.write(cleaned_content)

                print(f"  ✅ 추가: {filename}")
                print(f"     원본: {source_path}")
                print(f"     대상: TIL/_Daily/{filename}")
                synced_count += 1
            except Exception as e:
                print(f"  ⚠️  추가 실패: {filename} - {e}")
    
    # 3. 기존 파일 수정 감지 및 업데이트
    if files_existing:
        print(f"\n🔄 기존 파일 업데이트 확인 ({len(files_existing)}개):")
        updated_files = []
        
        for filename in sorted(files_existing):
            source_path = obsidian_files[filename]
            target_path = os.path.join(target_base_dir, filename)
            
            # 수정 시간 비교
            if os.path.getmtime(source_path) > os.path.getmtime(target_path):
                try:
                    with open(source_path, 'r', encoding='utf-8') as f_source:
                        content = f_source.read()
                    
                    content_without_frontmatter = FRONTMATTER_REGEX.sub('', content, count=1)
                    cleaned_content = clean_obsidian_boilerplate(content_without_frontmatter)

                    with open(target_path, 'w', encoding='utf-8') as f_target:
                        f_target.write(cleaned_content)

                    print(f"  🔄 업데이트: {filename}")
                    print(f"     원본: {source_path}")
                    print(f"     대상: TIL/_Daily/{filename}")
                    print(f"     이유: Obsidian 파일이 더 최신")
                    updated_files.append(filename)
                    synced_count += 1
                except Exception as e:
                    print(f"  ⚠️  업데이트 실패: {filename} - {e}")
            else:
                skipped_count += 1
        
        if not updated_files:
            print("  ℹ️  업데이트할 파일이 없습니다 (모든 파일이 최신 상태)")

    # 최종 결과 출력
    print(f"\n📋 동기화 완료 요약:")
    print(f"   ✅ 추가/업데이트: {synced_count}개")
    print(f"   ❌ 삭제: {deleted_count}개")
    print(f"   ⏭️  건너뜀: {skipped_count}개")
    print(f"   📁 현재 TIL 파일 수: {len(obsidian_files)}개")
    
    return True
