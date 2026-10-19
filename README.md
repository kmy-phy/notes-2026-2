# 노트 사이트 올리는 법 (터미널 없이, 웹에서만)

## 1. 저장소 만들기
1. github.com 로그인 → 오른쪽 위 **+** → **New repository**
2. 이름 예: `notes-2026-2`, **Public** 선택 → **Create repository**

## 2. 파일 올리기
1. 새 저장소 화면에서 **uploading an existing file** 클릭
2. 압축 푼 폴더 안의 `docs` 폴더, `mkdocs.yml`, `requirements.txt`, `README.md`를 끌어다 놓기
3. 아래 **Commit changes** 클릭

## 3. 배포 설정 파일 만들기
`.github` 폴더는 숨김 폴더라 끌어다 놓기로 안 올라가는 경우가 많아서 직접 만듭니다.
1. **Add file → Create new file**
2. 파일 이름 칸에 `.github/workflows/deploy.yml` 입력 (`/`를 치면 폴더가 자동으로 생김)
3. 압축 파일 안의 `.github/workflows/deploy.yml` 내용을 그대로 복사해서 붙여넣기
4. **Commit changes**

## 4. GitHub Pages 켜기
1. 저장소 **Settings → Pages**
2. **Source**를 **GitHub Actions**로 변경
3. **Actions** 탭에서 실행 중인 작업 확인 (실패했으면 오른쪽 위 **Re-run all jobs**)
4. 초록 체크가 뜨면 `https://내아이디.github.io/notes-2026-2/` 접속

## 이후
노트 `.md` 파일을 추가하거나 수정해서 커밋할 때마다 자동으로 사이트가 다시 만들어집니다.
작성법은 사이트의 "노트 쓰는 법" 페이지 참고.

## (선택) 내 컴퓨터에서 미리보기
```
pip install -r requirements.txt
mkdocs serve
```
→ http://127.0.0.1:8000
