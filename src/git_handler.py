import subprocess
import datetime

def run_command(command, working_dir):
    """지정된 디렉토리에서 셸 명령을 실행하고 결과를 출력합니다."""
    print(f"  > git {' '.join(command[1:])}")
    try:
        result = subprocess.run(
            command, cwd=working_dir, text=True, capture_output=True, check=True
        )
        if result.stdout.strip():
            print(f"     {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stdout or "nothing to commit" in e.stderr:
            print("     커밋할 내용이 없습니다.")
            return True
        if "Already up to date" in e.stdout or "Already up-to-date" in e.stdout:
            print("     이미 최신 상태입니다.")
            return True
        print(f"  - 오류 (종료 코드: {e.returncode}):\n{e.stderr or e.stdout}")
        return False
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

def git_pull_rebase(repo_path):
    """원격 저장소의 변경사항을 안전하게 가져옵니다.
    로컬 변경사항을 stash하고 pull 후 다시 적용합니다.
    """
    current_branch = get_current_branch(repo_path)
    if not current_branch:
        print("  - 오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return False
    
    # 원격 저장소 정보 가져오기
    if not run_command(["git", "fetch", "origin"], repo_path):
        print("  - 경고: 원격 저장소 정보를 가져오지 못했습니다. 계속 진행합니다.")
    
    # 로컬 변경사항 확인
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"], 
            cwd=repo_path, text=True, capture_output=True, check=True
        )
        has_changes = bool(result.stdout.strip())
    except:
        has_changes = False
    
    # 변경사항이 있으면 stash
    stashed = False
    if has_changes:
        print("   로컬 변경사항을 임시 저장합니다 (stash).")
        if run_command(["git", "stash", "push", "-m", "Auto-stash before sync"], repo_path):
            stashed = True
        else:
            print("  - 경고: stash에 실패했습니다. 계속 진행합니다.")
    
    # Pull 시도
    pull_success = run_command(["git", "pull", "origin", current_branch], repo_path)
    
    # Stash한 변경사항 복원
    if stashed:
        print("   임시 저장된 변경사항을 복원합니다 (stash pop).")
        if not run_command(["git", "stash", "pop"], repo_path):
            print("  - 경고: stash pop에 실패했습니다. 수동으로 'git stash pop'을 실행하세요.")
    
    return pull_success

def git_commit_and_push(repo_path):
    """변경된 내용을 add, commit, push 합니다."""
    print("-> 변경사항을 원격 저장소에 푸시합니다...")
    
    # 1. Add
    print(" 1. 변경된 파일들을 스테이징합니다 (add).")
    if not run_command(["git", "add", "."], repo_path):
        return False

    # 2. Commit
    print(" 2. 변경사항을 커밋합니다 (commit).")
    commit_message = f"docs: TIL Sync {datetime.datetime.now().strftime('%Y-%m-%d')}"
    if not run_command(["git", "commit", "-m", commit_message], repo_path):
        return False # 커밋할 내용이 없는 경우도 여기서 True가 반환되어 계속 진행됨

    # 3. Push
    print(" 3. 원격 저장소로 푸시합니다 (push).")
    current_branch = get_current_branch(repo_path)
    if not current_branch:
        print("  - 오류: 현재 Git 브랜치 이름을 가져올 수 없습니다.")
        return False
    if not run_command(["git", "push", "origin", current_branch], repo_path):
        return False
        
    print("   Git 동기화가 성공적으로 완료되었습니다.")
    return True
