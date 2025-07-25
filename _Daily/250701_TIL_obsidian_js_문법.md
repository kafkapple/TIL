# 250701 TIL - obsidian js 문법 (Tuesday)

- 
옵시디언의 Dataview 쿼리에서 `FROM "projects"`로 하면 해당 폴더(projects) 내 **직접 포함된 파일**이 모두 보이고,  
`FROM "projects/**"`로 하면 **projects 폴더와 그 하위 폴더 전체**의 파일을 보여주는 것이 기본 의도입니다.

하지만 실제로는 `projects/**`로 했을 때 **파일이 하나도 보이지 않는 현상**이 발생할 수 있습니다.  
이유는 다음과 같습니다.

## 1. **폴더 경로 표기 오류**

- **슬래시(/)와 백슬래시($$ 혼동:**

- Windows에서는 폴더 구분자로 `\`를 사용하지만, Dataview 쿼리에서는 반드시 `/`를 사용해야 합니다.

- 예시:

- 잘못된 표기: `FROM "projects\**"`

- 올바른 표기: `FROM "projects/**"`

- **폴더 이름 오타 또는 대소문자:**

- 폴더명이 정확히 일치해야 합니다.

- 예를 들어, 실제 폴더명이 `Projects`라면 `FROM "Projects/**"`로 해야 합니다.

## 2. **파일 구조 문제**

- **빈 파일 또는 메타데이터 없음:**

- Dataview는 **비어 있는 파일**이나 **유효한 메타데이터가 없는 파일**은 쿼리 결과에 포함하지 않을 수 있습니다[1](https://github.com/blacksmithgu/obsidian-dataview/issues/124)[2](https://github.com/blacksmithgu/obsidian-dataview/issues/2051).

- **특수문자, 공백, 인코딩 문제:**

- 파일명이나 폴더명에 특수문자, 공백, 한글이 포함되어 있으면 인식에 문제가 생길 수 있습니다.

## 3. **Dataview 버그 또는 인덱싱 문제**

- **Dataview 인덱싱 지연:**

- 새로 만든 파일이나 폴더가 인덱싱되지 않았을 수 있습니다.

- Dataview 인덱스를 강제로 재로드하거나, 옵시디언을 재시작해 보세요.

- **플러그인 충돌 또는 버그:**

- Dataview나 관련 플러그인에 버그가 있을 수 있습니다[3](https://forum.obsidian.md/t/dataview-not-showing-results/78004)[4](https://forum.obsidian.md/t/dataview-query-for-specific-tag-in-folder-tags-not-working-and-siomplified-query-only-returns-1-2-of-files-in-directory/46596).

- 최신 버전으로 업데이트하고, 필요시 재설치해 보세요.

## 4. **쿼리 문법 오류**

- **쿼리 문법 오류:**

- 쿼리 문법이 잘못되었거나, 쿼리가 포함된 파일의 위치가 잘못되었을 수 있습니다.

- 예시:

text

`TABLE file.mtime as "마지막 수정" FROM "projects/**" SORT file.mtime DESC`

- 이 쿼리는 projects 폴더와 그 하위 모든 파일을 보여줘야 합니다.

## 5. **트러블슈팅 팁**

- **쿼리 위치 확인:**

- 쿼리가 포함된 파일이 projects 폴더 내에 있지 않은지 확인하세요.

- 일부 쿼리는 자기 자신을 결과에서 제외할 수도 있습니다.

- **폴더 내 파일 수 확인:**

- 실제로 projects 폴더와 하위에 파일이 있는지 다시 확인하세요.

- **다른 쿼리 시도:**

- `FROM "projects"`와 `FROM "projects/**"`를 번갈아가며 테스트해 보세요.

- **Dataview 인덱스 재로드:**

- Dataview 설정에서 "인덱스 재로드" 기능을 사용해 보세요.

## 요약

- **폴더 경로 표기, 쿼리 문법, 파일 구조, 인덱싱 지연, 플러그인 버그** 등이 원인일 수 있습니다[1](https://github.com/blacksmithgu/obsidian-dataview/issues/124)[5](https://www.reddit.com/r/ObsidianMD/comments/1795mua/new_to_dataview_why_cant_i_pull_files_from_folders/)[2](https://github.com/blacksmithgu/obsidian-dataview/issues/2051).

- **빈 파일, 메타데이터 없는 파일, 특수문자/공백 문제**도 체크하세요.

- **Dataview 인덱스 재로드, 옵시디언 재시작, 플러그인 재설치** 등으로 해결할 수 있습니다.

이런 점들을 하나씩 체크해보면 문제를 해결할 수 있습니다.

1. [https://github.com/blacksmithgu/obsidian-dataview/issues/124](https://github.com/blacksmithgu/obsidian-dataview/issues/124)
2. [https://github.com/blacksmithgu/obsidian-dataview/issues/2051](https://github.com/blacksmithgu/obsidian-dataview/issues/2051)
3. [https://forum.obsidian.md/t/dataview-not-showing-results/78004](https://forum.obsidian.md/t/dataview-not-showing-results/78004)
4. [https://forum.obsidian.md/t/dataview-query-for-specific-tag-in-folder-tags-not-working-and-siomplified-query-only-returns-1-2-of-files-in-directory/46596](https://forum.obsidian.md/t/dataview-query-for-specific-tag-in-folder-tags-not-working-and-siomplified-query-only-returns-1-2-of-files-in-directory/46596)
5. [https://www.reddit.com/r/ObsidianMD/comments/1795mua/new_to_dataview_why_cant_i_pull_files_from_folders/](https://www.reddit.com/r/ObsidianMD/comments/1795mua/new_to_dataview_why_cant_i_pull_files_from_folders/)
6. [https://www.reddit.com/r/ObsidianMD/comments/10u0zfr/what_i_am_missing_with_dataview/](https://www.reddit.com/r/ObsidianMD/comments/10u0zfr/what_i_am_missing_with_dataview/)
7. [https://stackoverflow.com/questions/56148470/using-wildcards-in-file-path/56148765](https://stackoverflow.com/questions/56148470/using-wildcards-in-file-path/56148765)
8. [https://www.reddit.com/r/ObsidianMD/comments/tb7n1m/dataview_question_pages_that_start_with_project/](https://www.reddit.com/r/ObsidianMD/comments/tb7n1m/dataview_question_pages_that_start_with_project/)
9. [https://stackoverflow.com/questions/74072506/using-wildcard-for-folder-in-the-mid-of-the-path](https://stackoverflow.com/questions/74072506/using-wildcard-for-folder-in-the-mid-of-the-path)
10. [https://www.reddit.com/r/ObsidianMD/comments/1612hka/streamlining_obsidian_and_dataview_for_enhanced/](https://www.reddit.com/r/ObsidianMD/comments/1612hka/streamlining_obsidian_and_dataview_for_enhanced/)

- **Created Date**: 2025-07-01
- **Category**: TIL
- **ID**: N_et4esnhn