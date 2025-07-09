import os
import shutil
import subprocess
import datetime
import re

# --- 설정 ---
# (Obsidian 볼트 경로, GitHub TIL 저장소 경로)
POSSIBLE_PATHS = [
    ("/home/joon/Documents/Obsidian", "/home/joon/dev/TIL"),
    ("/Users/joon/Documents/Obsidian", "/Users/joon/dev/TIL"),
    ("D:/Documents/Obsidian", "D:/dev/TIL"),
]
# 동기화할 노트가 있는 Obsidian 내의 상위 폴더
SOURCE_FOLDERS = ["10_Daily", "30_Projects", "40_Areas"]
# GitHub 저장소에서 Daily 노트가 저장될 폴더
TARGET_DAILY_FOLDER = "_Daily"

# --- 정규식 ---
DATE_PREFIX_REGEX = re.compile(r"^(?:\d{8}|\d{6})_.*\.md$")
TIL_TAG_REGEX = re.compile(r"tags:.*til", re.IGNORECASE)

# --- 스크립트 본체 ---

def find_paths():
    for vault_path, repo_path in POSSIBLE_PATHS:
        if os.path.isdir(vault_path) and os.path.isdir(repo_path):
            print(f"경로 발견:\n  - Obsidian 볼트: {vault_path}\n  - GitHub 저장소: {repo_path}")
            return vault_path, repo_path
    print("오류: 현재 환경에 맞는 경로를 찾을 수 없습니다.")
    return None, None

def discover_til_notes(vault_path):
    """볼트 내에��� 유효한 TIL 노트를 탐색하고 목록을 반환합니다."""
    print("\n[1/5] Obsidian 볼트에서 TIL 노트 탐색 중...")
    valid_notes = []
    search_paths = [os.path.join(vault_path, d) for d in SOURCE_FOLDERS]

    for path in search_paths:
        if not os.path.isdir(path):
            continue
        for root, _, files in os.walk(path):
            for file in files:
                # 1. 파일명이 날짜 접두사 규칙에 맞는지 확인
                if not DATE_PREFIX_REGEX.match(file):
                    continue
                
                file_path = os.path.join(root, file)
                try:
                    # 2. 파일 내용에 'til' 태그가 있는지 확인
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read(500)
                        if TIL_TAG_REGEX.search(content):
                            valid_notes.append(file_path)
                except Exception as e:
                    print(f"  - 파일 읽기 오류 {file_path}: {e}")
    
    print(f"총 {len(valid_notes)}개의 유효한 TIL 노트를 발견했습니다.")
    return valid_notes

def sync_new_notes(til_notes, repo_path):
    """새롭거나 변경된 TIL 노트만 GitHub 저장소의 _Daily 폴더로 복사합니다."""
    print("\n[2/5] 새로운 노트 동기화 중...")
    synced_count = 0
    target_base_dir = os.path.join(repo_path, TARGET_DAILY_FOLDER)
    if not os.path.exists(target_base_dir):
        os.makedirs(target_base_dir)

    for source_path in til_notes:
        filename = os.path.basename(source_path)
        target_path = os.path.join(target_base_dir, filename)

        # 복사 조건: 타겟 파일이 없거나, 소스 파일이 더 최신일 경우
        if not os.path.exists(target_path) or \
           os.path.getmtime(source_path) > os.path.getmtime(target_path):
            
            print(f"  - 복사: {filename}")
            shutil.copy2(source_path, target_path)
            synced_count += 1
            
    if synced_count == 0:
        print("새롭게 변경된 노트가 없습니다.")
    else:
        print(f"총 {synced_count}개의 파일을 동기화했습니다.")
    return True

def run_command(command, working_dir):
    """지정된 디렉토리에서 명령어를 실행합니다."""
    print(f"  > 실행: {' '.join(command)}")
    try:
        # check=False로 변경하여 오류를 직접 처리
        result = subprocess.run(
            command, cwd=working_dir, text=True, capture_output=True
        )
        if result.returncode != 0:
            # 커밋할 내용이 없는 것은 정상이므로 오류에서 제외
            if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
                print("  - 커밋할 내용이 없습니다.")
                return True # 성공으로 간주
            
            print(f"  - 오류 발생 (종료 코드: {result.returncode}):")
            if result.stdout: print(result.stdout)
            if result.stderr: print(result.stderr)
            return False
        
        if result.stdout: print(result.stdout.strip())
        return True
    except FileNotFoundError:
        print(f"  - 오류: '{command[0]}' 명령을 찾을 수 없습니다.")
        return False

def get_current_branch(working_dir):
    """현재 Git 브랜치 이름을 가져옵니다."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=working_dir, check=True, text=True, capture_output=True
        )
        return result.stdout.strip()
    except Exception:
        return None

def main():
    vault_path, repo_path = find_paths()
    if not vault_path: return

    til_notes = discover_til_notes(vault_path)
    
    if not sync_new_notes(til_notes, repo_path): return

    print("\n[3/5] README 업데이트...")
    if not run_command(["python3", "update_readme.py"], repo_path): return

    print("\n[4/5] Git 변경사항 스테이징...")
    if not run_command(["git", "add", "."], repo_path): return

    print("\n[5/5] Git 커밋 및 푸시...")
    commit_message = f"TIL Sync: {datetime.datetime.now().strftime('%Y-%m-%d')}"
    if not run_command(["git", "commit", "-m", commit_message], repo_path): return
    
    current_branch = get_current_branch(repo_path)
    if not current_branch:
        print("  - 오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return
        
    if not run_command(["git", "push", "origin", current_branch], repo_path): return
    
    print("\n✨ 모든 동기화 작업이 성공적으로 완료되었습니다!")

if __name__ == "__main__":
    main()