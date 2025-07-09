import os
import shutil
import subprocess
import datetime
import re

# --- 설정 ---
POSSIBLE_PATHS = [
    ("/home/joon/Documents/Obsidian", "/home/joon/dev/TIL"),
    ("/Users/joon/Documents/Obsidian", "/Users/joon/dev/TIL"),
    ("D:/Documents/Obsidian", "D:/dev/TIL"),
]
SOURCE_FOLDERS = ["10_Daily", "30_Projects", "40_Areas"]
TARGET_DAILY_FOLDER = "_Daily"

# --- 정규식 ---
DATE_PREFIX_REGEX = re.compile(r"^(?:\d{8}|\d{6})_.*\.md$")
TIL_TAG_REGEX = re.compile(r"tags:.*til", re.IGNORECASE)
FRONTMATTER_REGEX = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)

# --- 스크립트 본체 ---

def find_paths():
    for vault_path, repo_path in POSSIBLE_PATHS:
        if os.path.isdir(vault_path) and os.path.isdir(repo_path):
            print(f"경로 발견:\n  - Obsidian 볼트: {vault_path}\n  - GitHub 저장소: {repo_path}")
            return vault_path, repo_path
    print("오류: 현재 환경에 맞는 경로를 찾을 수 없습니다.")
    return None, None

def discover_til_notes(vault_path):
    print("\n[1/5] Obsidian 볼트에서 TIL 노트 탐색 중...")
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
                        if TIL_TAG_REGEX.search(f.read(500)):
                            valid_notes.append(file_path)
                except Exception as e:
                    print(f"  - 파일 읽기 오류 {file_path}: {e}")
    print(f"총 {len(valid_notes)}개의 유효한 TIL 노트를 발견했습니다.")
    return valid_notes

def sync_new_notes(til_notes, repo_path):
    print("\n[2/5] 새로운 노트 동기화 중 (Frontmatter 제거 포함)...")
    synced_count = 0
    target_base_dir = os.path.join(repo_path, TARGET_DAILY_FOLDER)
    if not os.path.exists(target_base_dir):
        os.makedirs(target_base_dir)

    for source_path in til_notes:
        filename = os.path.basename(source_path)
        target_path = os.path.join(target_base_dir, filename)

        if not os.path.exists(target_path) or \
           os.path.getmtime(source_path) > os.path.getmtime(target_path):
            
            try:
                with open(source_path, 'r', encoding='utf-8') as f_source:
                    content = f_source.read()
                
                content_without_frontmatter = FRONTMATTER_REGEX.sub('', content, count=1)

                with open(target_path, 'w', encoding='utf-8') as f_target:
                    f_target.write(content_without_frontmatter)

                print(f"  - 복사 (Frontmatter 제거): {filename}")
                synced_count += 1
            except Exception as e:
                print(f"  - 동기화 오류 {filename}: {e}")

    if synced_count == 0:
        print("새롭게 변경된 노트가 없습니다.")
    else:
        print(f"총 {synced_count}개의 파일을 동기화했습니다.")
    return True

def run_command(command, working_dir):
    print(f"  > 실행: {' '.join(command)}")
    try:
        result = subprocess.run(
            command, cwd=working_dir, text=True, capture_output=True
        )
        if result.returncode != 0:
            if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
                print("  - 커밋할 내용이 없습니다.")
                return True
            print(f"  - 오류 (종료 코드: {result.returncode}):\n{result.stderr or result.stdout}")
            return False
        if result.stdout.strip(): print(result.stdout.strip())
        return True
    except FileNotFoundError:
        print(f"  - 오류: '{command[0]}' 명령을 찾을 수 없습니다.")
        return False

def get_current_branch(working_dir):
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

    print("\n[5/5] Git 동기화 및 푸시...")
    commit_message = f"TIL Sync: {datetime.datetime.now().strftime('%Y-%m-%d')}"
    if not run_command(["git", "commit", "-m", commit_message], repo_path): return
    
    current_branch = get_current_branch(repo_path)
    if not current_branch:
        print("  - 오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return
    
    print("  > 원격 저장소와 동기화 (git pull)...")
    if not run_command(["git", "pull", "--rebase", "origin", current_branch], repo_path): return

    print("  > 원격 저장소로 푸시 (git push)...")
    if not run_command(["git", "push", "origin", current_branch], repo_path): return
    
    print("\n✨ 모든 동기화 작업이 성공적으로 완료되었습니다!")

if __name__ == "__main__":
    main()