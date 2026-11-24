# CLAUDE.md — 노트 사이트 작업 규칙

이 저장소는 사용자의 수업 필기를 교과서(LaTeX) 스타일 노트로 정리해 올리는 사이트다.
사용자가 손필기 사진·칠판 사진·PDF를 주면, Claude가 그것을 정리된 노트로 바꿔서 직접 커밋·푸시한다.

- 사이트: https://kmy-phy.github.io/notes-2026-2/
- 저장소: `kmy-phy/notes-2026-2` (MkDocs Material, GitHub Pages, GitHub Actions로 배포)

---

## 0. 사용자와 대화할 때

- **항상 한국어로 답한다.** 코드·커밋 메시지·영어판 노트 본문은 영어로 써도 되지만, 사용자에게 하는 말은 전부 한국어다.
- 개념 질문(예: 노트 내용에 대한 물리 질문)에는 노트를 고치지 말고 먼저 설명으로 답한다. 노트에 반영할지는 제안만 하고, 사용자가 원할 때 반영한다.
- 실수 없이 한다. 특히 **깨진 페이지를 배포하지 않는다** (아래 §6 검증 절차를 반드시 지킨다).

## 1. 과목 구성

### Differential Geometry
- 강의: **Claudio Arezzo**. 주교재: **do Carmo, *Differential Geometry of Curves and Surfaces***.
- 노트는 강의 번호가 아니라 **do Carmo의 장 구성**을 따른다.
  - `chapter1.md` = Chapter 1 — Curves (§1.1–1.7). Lecture 1–3이 여기에 들어간다.
  - 새 장이 시작되면 `chapter2.md`, `chapter2-ko.md` 식으로 만든다.
- 번호는 do Carmo 절 번호를 따른다: **Theorem 1.5.3** = §1.5의 세 번째 번호 붙은 항목.
- 수업에서 다루지 않은 절(현재 §1.4, §1.6)도 **목차와 본문에 제목은 넣고**, 아래 상자로 "수업에서 다루지 않아 생략"이라고 적는다. 뒤에서 필요한 사실만 한두 줄 요약해 둔다.
  ```
  <div class="admonition skipped" markdown>
  This section was not covered in the lectures and is skipped in these notes. ...
  </div>
  ```
- 판서와 교재가 다르면(예: 계수 오타) 교재·수학적으로 맞는 쪽을 따르고, 확신이 없으면 사용자에게 묻는다.
- 손필기 원본 PDF는 `docs/differential-geometry/originals/`에 두고 `source-note`에서 링크한다.

### Modern Physics
- 강의: **김제훈, 조우주**. 중간·기말 범위 모두 포함.
- Part I 양자역학
  - `qm1d.md`: Ch. 5, 1차원 양자역학 (중간)
  - `quantum.md`: Ch. 6, 수소 원자·3차원 양자역학 (기말)
- Part II 특수상대론
  - `sr1.md`: 상대론 I, §1–5 (중간)
  - `sr2.md`: 상대론 II, §6–11 (기말)
- 옛 주소 `relativity/`, `relativity-ko/`는 리다이렉트 페이지다(#6 이상이면 sr2, 아니면 sr1로). 지우지 않는다.
- 새 범위가 생기면 같은 방식(중간/기말 분리)으로 파일을 나누고, `index.md`/`index-ko.md`의 About·Contents와 홈(`docs/index.md`) 표를 함께 갱신한다.

## 2. 파일 구조

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
```

- 새 페이지를 만들면 `mkdocs.yml`의 `nav`에 **영어판만** 추가한다(한국어판은 탭으로 들어감).
- 과목 소개 페이지(`index.md`)는 **과목 전체**에 대한 설명이다. 특정 장에만 해당하는 규약(Conventions)은 그 장 페이지에 둔다.

## 3. 영어판 / 한국어판

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
- 수정 후 패리티 확인: `python3 scripts/check.py site` (§6). 두 판의 제목 앵커 목록, `$$` 개수, 그림·상자 개수가 같아야 한다.

## 4. 노트 작성 스타일

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

### 내용 원칙
- 필기 내용을 **빠짐없이**, 교과서처럼 정돈된 문장으로 옮긴다. 필기에서 생략된 논리 단계는 채워 넣어도 된다.
- 새로 보충한 내용에 **"(added)", "(추가)" 같은 표시를 붙이지 않는다.** 그냥 본문으로 자연스럽게 넣는다.
- 수식은 `$...$`, `$$...$$` (arithmatex generic, MathJax 3).
  - `$$` 블록 앞뒤에는 **반드시 빈 줄**. 상자 안이면 4칸 들여쓰기 유지.
  - 면적분 `\oiint`는 매크로로 정의되어 있음. 지원 안 되는 명령은 쓰지 말고, 새 명령이 필요하면 `mathjax.js`에 매크로를 추가한다.
- 목록(`li`)은 `word-break: keep-all`이 적용되어 있다.

### 그림
- **사용자의 손그림 사진을 그대로 쓰지 않는다.** 모든 그림은 TikZ로 새로 그린다.
- 절차: `figures-src/<name>.tex` 작성(standalone, `tikz`, `arrows.meta` 등) → `pdflatex` → `pdftocairo -svg` → `docs/<course>/images/<name>.svg`.
- 삽입:
  ```
  <figure markdown>
    ![Bell's spaceship paradox](images/rel-bell.svg){ .tex-fig width="380" }
    <figcaption markdown="span">Figure 9.1. ...</figcaption>
  </figure>
  ```
  `.tex-fig`는 다크 모드에서 색이 반전된다. 그림은 검정 선 위주로 그린다.
- 파일 이름 접두어: 미분기하 `ch1-*`, 양자 `qm-*`, 상대론 `rel-*`.

## 5. PDF

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

## 6. 작업 절차 (매번)

1. 수정한다 (영어판과 한국어판 둘 다).
2. `mkdocs build --strict` 통과 확인. PDF에 영향이 있는 수정이면 `python3 scripts/md2latex.py --site site`도 돌려 본다.
3. **렌더링 확인 — 생략 금지.** `python3 -m http.server`로 `site/`를 띄우고 Playwright로 바뀐 페이지를 열어, 날 마크다운(`!!!`, `$$`, `**`, `{ #` 등)이 화면에 그대로 보이지 않는지, 목록·상자·표가 제대로인지 확인한다. 샌드박스에서는 MathJax CDN이 막혀 수식은 렌더 안 되므로 구조만 확인하고, 수식 문법은 눈으로 검토한다.
4. 영어/한국어 패리티 확인 (§3): `python3 scripts/check.py site`가 오류 0으로 끝나야 한다. 제목 앵커 목록·순서, 수식 블록·그림·표·상자 개수, 변환 안 된 마크다운(`!!!`, `$$`, `{ #`, `**` 등), 깨진 링크(언어 탭·PDF 포함)를 검사한다. CI도 배포 직전에 같은 검사를 돌려서, 실패하면 배포하지 않는다. 인라인 수식 개수 차이는 경고만 한다.
5. 문자열 치환으로 큰 블록을 고칠 때는, 위치(인덱스)를 계산하기 **전에** 텍스트를 바꾸지 않는다. 한 번에 하나씩 바꾸고 결과를 확인한다.
6. 커밋·푸시:
   ```
   git -c user.name="Claude" -c user.email="noreply@anthropic.com" commit -m "..."
   git -c push.negotiate=true push origin HEAD:main
   ```
7. 배포 성공 확인:
   ```
   R=$(gh api "repos/kmy-phy/notes-2026-2/actions/workflows/deploy.yml/runs?per_page=1" -q '.workflow_runs[0].id')
   gh run watch $R -R kmy-phy/notes-2026-2 --exit-status
   ```
8. 사용자에게 한국어로 짧게 결과를 알린다 (무엇이 바뀌었는지 + 사이트 주소).

## 7. 알려진 함정

- CI는 `ubuntu-24.04`로 고정. MkDocs/Material 버전도 `requirements.txt`에 고정되어 있다(Material for MkDocs는 2027-05 지원 종료, MkDocs 2.0과 호환 안 됨). 함부로 올리지 않는다.
- `$$` 뒤에 빈 줄이 없으면 그 뒤 상자·문단이 깨진다.
- 한국어 제목에 앵커를 빼먹으면 언어 탭·목차 링크가 어긋난다.
- 목록 안에 들여쓴 문단을 잘못 두면 다음 글머리 기호가 문단에 흡수된다. 목록 구조를 렌더링으로 확인한다.
- 옛 URL(`differential-geometry/lec01/`, `lec02/`, `modern-physics/relativity/`)은 리다이렉트로 유지한다.
