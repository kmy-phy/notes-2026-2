# 노트 쓰는 법 (문법·파일 참고서)

노트를 쓰거나 고칠 때 필요한 구체적인 문법과 파일 구조. 일반 규칙은 [CLAUDE.md](../CLAUDE.md), 과목별 정보는 [courses.md](courses.md).

## 파일 구조

```
docs/
  index.md                     홈 (과목 표)
  guide.md                     노트 쓰는 법 (사용자용)
  <course>/index.md, index-ko.md   과목 소개·목차 (과목 전체에 대한 설명)
  <course>/<page>.md, <page>-ko.md  노트 본문 (영어판, 한국어판)
  <course>/images/*.svg        TikZ로 그린 그림
  stylesheets/extra.css        교과서 스타일 + 인쇄(PDF) 규칙
  javascripts/mathjax.js       MathJax 설정 (unicode 확장, \oiint 매크로)
  javascripts/lang.js          English/한국어 탭 (#해시 유지)
  javascripts/pdfview.js       PDF 링크 → viewer.html (PDF 보기 화면, 위에 내려받기 버튼)
  viewer.html                  PDF 보기 화면 (PDF.js)
figures-src/*.tex              그림의 TikZ 원본 (사이트에는 안 올라감)
scripts/check.py               배포 전 자동 점검 (영/한 짝, 마크다운 흔적, 링크)
scripts/md2latex.py            배포 때 PDF 생성 (마크다운 → pandoc → LaTeX → xelatex)
scripts/latex/book.tex         PDF용 LaTeX 템플릿 (표지, 머리글, 상자 모양)
.github/workflows/deploy.yml   빌드·PDF·배포
mkdocs.yml                     nav(왼쪽 메뉴)는 여기서 직접 관리
notes-guide/                   작업 참고서 (이 파일, 과목별 정보)
```

- 새 페이지를 만들면 `mkdocs.yml`의 `nav`에 **영어판만** 추가한다(한국어판은 탭으로 들어감).
- 과목 소개 페이지(`index.md`)는 **과목 전체**에 대한 설명이다. 특정 장에만 해당하는 규약(Conventions)은 그 장 페이지에 둔다.

## 영어판 / 한국어판 문법

- 모든 노트 페이지는 **영어판과 한국어판 두 개**가 있고 **내용이 완전히 같아야** 한다(언어만 다름). 한쪽을 고치면 반드시 다른 쪽도 고친다.
- 페이지 맨 위에 언어 탭:
  ```
  <div class="lang-switch"><a class="on">English</a><a href="../sr2-ko/">한국어</a></div>
  ```
  (한국어판은 `<a href="../sr2/">English</a><a class="on">한국어</a>`)
- **한국어판의 모든 제목에는 영어판과 같은 앵커를 직접 붙인다.** 그래야 탭을 바꿔도 같은 위치로 가고 목차 링크가 맞는다.
  ```
  ## 6 발산, 회전, 그리고 전하의 불변성 { #6-divergence-curl-and-the-invariance-of-charge }
  ```
  앵커는 영어 제목을 MkDocs가 만드는 slug(소문자, 공백→`-`, 특수문자 제거)와 똑같이 한다.
- 한국어판 PDF 파일명은 한국어로(`download="현대물리학-상대론-II.pdf"`).
- 수정 후 패리티 확인: `python3 scripts/check.py site` (CLAUDE.md의 작업 절차). 두 판의 제목 앵커 목록, `$$` 개수, 그림·상자 개수가 같아야 한다.

## 노트 작성

### 페이지 머리
```
---
title: "Part II — Special Relativity II (final range)"
---

<div class="lang-switch">...</div>

<div class="running-head"><span>Modern Physics</span><span>Part II · Relativity II</span></div>

# Part II — Special Relativity II { .part-title }

<p class="source-note">Lecture notes, final range · <a class="pdf-link" href="notes.pdf" download="Modern-Physics-Relativity-II.pdf">This part as PDF</a></p>
```
`running-head`가 있는 페이지만 PDF가 만들어진다.

### 상자(admonition) 종류 — 교과서 상자로 스타일링되어 있음
| 문법 | 의미 |
|---|---|
| `!!! note "Definition 1.2.1"` | 정의 |
| `!!! abstract "Theorem 1.3.1"` | 정리·명제·보조정리 (테두리, 이탤릭) |
| `!!! success "Proof"` | 증명 |
| `!!! example "Example 1.3.5 (Lines)"` | 예제 |
| `!!! info "Remark — ..."` | 비고 |
| `!!! warning "..."` | 주의 |
| `!!! quote "Conventions used in this chapter."` | 규약 상자 (장 맨 앞) |
| `<div class="admonition skipped" markdown>` | 수업에서 다루지 않은 절 |

한국어판 제목: 정의 / 정리 / 명제 / 보조정리 / 증명 / 예제 / 비고 / 주의 / "이 장에서 쓰는 규약."

### 수식과 글자
- 수식은 `$...$`, `$$...$$` (arithmatex generic, MathJax 3).
  - `$$` 블록 앞뒤에는 **반드시 빈 줄**. 상자 안이면 4칸 들여쓰기 유지.
  - 면적분 `\oiint`는 매크로로 정의되어 있음. 지원 안 되는 명령은 쓰지 말고, 새 명령이 필요하면 `mathjax.js`에 매크로를 추가한다.
- 목록(`li`)은 `word-break: keep-all`이 적용되어 있다.

### 그림
- 절차: `figures-src/<name>.tex` 작성(standalone, `tikz`, `arrows.meta` 등) → `pdflatex` → `pdftocairo -svg` → `docs/<course>/images/<name>.svg`.
- 삽입:
  ```
  <figure markdown>
    ![Bell's spaceship paradox](images/rel-bell.svg){ .tex-fig width="380" }
    <figcaption markdown="span">Figure 9.1. ...</figcaption>
  </figure>
  ```
  `.tex-fig`는 다크 모드에서 색이 반전된다. 그림은 검정 선 위주로 그린다.
- 파일 이름 접두어는 과목마다 정한다 ([courses.md](courses.md)).

## PDF

- PDF는 **진짜 LaTeX로 컴파일**한다. 원본은 웹과 같은 마크다운 한 벌뿐이고, 배포 때 `scripts/md2latex.py --site site`가
  마크다운의 MkDocs 문법(상자, `<figure>`, lecture-tag 등)을 pandoc용으로 바꿔 LaTeX로 변환하고 `scripts/latex/book.tex`에 넣어 xelatex로 두 번 컴파일한다.
  - 과목별 `all-lectures.pdf`(영어)·`all-lectures-ko.pdf`(한국어): 표지 + 과목 소개(index.md) + 쪽수 있는 목차 + 본문, 쪽 번호가 이어짐.
  - 페이지별 `notes.pdf`: 그 장·부만.
  - 묶음 순서는 파일 이름 순(qm1d < quantum < sr1 < sr2).
- 상자 대응: note→정의, abstract→정리(테두리, 페이지에서 안 쪼개짐), success→증명, example, info→비고, warning→왼쪽 굵은 선, quote→규약 상자, skipped→회색 상자.
- 한 줄 수식이 본문 폭보다 넓으면 `\fitmath`가 자동으로 줄인다. 그림은 SVG를 rsvg-convert로 PDF로 바꿔 쓰고, 캡션은 사이트의 "Figure 7.1." 문구를 그대로 쓴다.
- 한글·①② 등은 Noto Serif CJK KR로 자동 전환된다(XeTeX interchar). Latin Modern에 없는 기호가 나오면 `pandoc()` 후처리나 `book.tex`의 범위에 추가한다.
- **새 문법을 노트에 쓰면 PDF 변환도 확인한다**: `python3 scripts/md2latex.py --site site`가 에러 없이 끝나는지, 결과 PDF 몇 쪽을 이미지로 열어 본다.
- PDF 링크(`a.pdf-link`, `.pdf-links a`)를 누르면 `javascripts/pdfview.js`가 가로채서 `viewer.html?file=...&name=...&lang=...`(사이트 안 PDF 보기 화면, PDF.js 3.2 내장 `javascripts/pdfjs/`)로 연다. 보기 화면 위쪽 버튼으로 내려받는다. 링크 문구는 "…PDF로 보기" / "… as PDF". `download` 속성의 파일명이 내려받기 파일명이 된다.
- 사이트 화면 보기는 PDF와 별개다.

## 마크다운 함정

- `$$` 뒤에 빈 줄이 없으면 그 뒤 상자·문단이 깨진다.
- 한국어 제목에 앵커를 빼먹으면 언어 탭·목차 링크가 어긋난다.
- 목록 안에 들여쓴 문단을 잘못 두면 다음 글머리 기호가 문단에 흡수된다. 목록 구조를 렌더링으로 확인한다.
- 문자열 치환으로 큰 블록을 고칠 때는, 위치(인덱스)를 계산하기 **전에** 텍스트를 바꾸지 않는다. 한 번에 하나씩 바꾸고 결과를 확인한다.

## 커밋·배포 명령

```
git -c user.name="Claude" -c user.email="noreply@anthropic.com" commit -m "..."
git -c push.negotiate=true push origin HEAD:main
R=$(gh api "repos/kmy-phy/notes-2026-2/actions/workflows/deploy.yml/runs?per_page=1" -q '.workflow_runs[0].id')
gh run watch $R -R kmy-phy/notes-2026-2 --exit-status
```

- 버전 고정 이유: Material for MkDocs는 2027-05 지원 종료, MkDocs 2.0과 호환 안 됨. CI는 `ubuntu-24.04`.
- CI의 LaTeX 설치는 .deb 캐시 + 미러 전환 재시도로 되어 있다(미러가 느리게 데이터를 흘리면 apt 타임아웃이 안 걸려서). `deploy.yml` 주석 참고.

## 홈과 PDF 보기 화면

- 홈은 `overrides/home.html`(어두운 과목 목록, course-notes-skills의 허브 디자인을 따름). 과목을 추가하면 `mkdocs.yml`의 `extra.courses`에 `{ id, ko, en }` 한 줄. 소개 문장·학기는 `extra.home`.
- 과목 줄의 "N편 · 국문 Np · 영문 Np · 날짜"와 마우스를 올리면 뜨는 첫 장 미리보기는 배포 때 `md2latex.py --site`가 만드는 `site/manifest.json`, `site/<course>/thumb.jpg`에서 온다(날짜는 그 과목 폴더의 마지막 커밋).
- `viewer.html`은 manifest의 `pdfs`에서 제목·내려받기 이름·다른 언어판을 읽는다. 목차는 PDF 책갈피, 언어를 바꾸면 같은 절(책갈피 순서가 두 판에서 같아야 함 — check.py가 제목을 맞춰 둠). 읽던 자리는 브라우저에 저장.
- `navigation.instant`는 껐다(홈이 Material 화면이 아니라서).
- 노트 페이지는 기본이 흰 배경(라이트), 오른쪽 위 버튼으로 다크 모드. 시스템 다크 모드를 따라가지 않는다. 색은 `extra.css` 맨 위의 `[data-md-color-scheme="default"]`(흰 종이, `#1a1a1a` 글씨)와 `"slate"`(`#0a0a0b` 거의 검정, 따뜻한 흰 글씨).
