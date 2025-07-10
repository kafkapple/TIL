import os
from src.file_handler import discover_til_notes, sync_new_notes
from src.readme_generator import update_readme
from src.git_handler import git_sync

# --- 설정 ---
# 사용자의 환경에 맞게 경로를 자동으로 탐색합니다.
POSSIBLE_PATHS = [
    ("/home/joon/Documents/Obsidian", "/home/joon/dev/TIL"),
    ("/Users/joon/Documents/Obsidian", "/Users/joon/dev/TIL"),
    ("D:/Documents/Obsidian", "D:/dev/TIL"),
]

def find_paths():
    """현재 환경에 맞는 Obsidian 볼트와 TIL 저장소 경로를 찾습니다."""
    for vault_path, repo_path in POSSIBLE_PATHS:
        if os.path.isdir(vault_path) and os.path.isdir(repo_path):
            print(f"성공: 작업 경로를 찾았습니다.")
            print(f"  - Obsidian 볼트: {vault_path}")
            print(f"  - TIL 저장소: {repo_path}")
            return vault_path, repo_path
    print("오류: 현재 환경에 맞는 경로를 찾을 수 없습니다.")
    print("POSSIBLE_PATHS 변수에 올바른 경로를 추가해주세요.")
    return None, None

def main():
    """TIL 동기화 프로세스를 실행합니다."""
    print("\n======= Obsidian TIL 동기화 스크립트 시작 =======")
    
    vault_path, repo_path = find_paths()
    if not vault_path:
        return

    # 1. 새로운 TIL 노트 탐색 및 복사
    print("\n[1/3] Obsidian -> 로컬 저장소")
    til_notes = discover_til_notes(vault_path)
    sync_new_notes(til_notes, repo_path)

    # 2. README.md 업데이트 (히트맵 및 목차 생성)
    print("\n[2/3] README.md 업데이트")
    # readme_generator.py가 TIL 폴더 내에서 실행되어야 하므로, 작업 디렉토리 변경
    original_dir = os.getcwd()
    os.chdir(repo_path)
    update_readme()
    os.chdir(original_dir)

    # 3. Git 저장소 동기화 (Pull -> Add -> Commit -> Push)
    print("\n[3/3] 로컬 저장소 -> 원격 저장소")
    git_sync(repo_path)

    print("\n✨ 모든 동기화 작업이 성공적으로 완료되었습니다! ✨")
    print("===================================================")

if __name__ == "__main__":
    main()
