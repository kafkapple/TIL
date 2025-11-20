import os
from src.file_handler import discover_til_notes, sync_new_notes
from src.readme_generator import update_readme
from src.git_handler import git_pull_rebase, git_commit_and_push

# --- 설정 ---
POSSIBLE_PATHS = [
    ("/Users/joon/Documents/Obsidian", "/Users/joon/dev/TIL"), # 2025 Macbook Pro
    ("/home/joon/Documents/Obsidian", "/home/joon/dev/TIL"),
    ("/Users/joonpark/Documents/Obsidian/Obsidian", "/Users/joonpark/Documents/dev/TIL"),
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
    return None, None

def main():
    """TIL 동기화 프로세스를 올바른 순서로 실행합니다."""
    print("\n======= Obsidian TIL 동기화 스크립트 시작 =======")
    
    vault_path, repo_path = find_paths()
    if not vault_path:
        return

    # 1. (가장 먼저) 원격 저장소의 변경사항을 가져옵니다.
    print("\n[1/4] 원격 저장소와 동기화 (Pull)")
    if not git_pull_rebase(repo_path):
        print("  - Pull 실패. 동기화를 중단합니다.")
        return

    # 2. 새로운 TIL 노트 탐색 및 복사
    print("\n[2/4] Obsidian -> 로컬 저장소")
    til_notes = discover_til_notes(vault_path)
    sync_new_notes(til_notes, repo_path)

    # 3. README.md 업데이트
    print("\n[3/4] README.md 업데이트")
    original_dir = os.getcwd()
    os.chdir(repo_path)
    update_readme()
    os.chdir(original_dir)

    # 4. (가장 마지막에) 로컬 변경사항을 원격으로 푸시
    print("\n[4/4] 로컬 저장소 -> 원격 저장소 (Push)")
    git_commit_and_push(repo_path)

    print("\n✨ 모든 동기화 작업이 성공적으로 완료되었습니다! ✨")
    print("===================================================")

if __name__ == "__main__":
    main()