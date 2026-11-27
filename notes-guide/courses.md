# 과목별 정보

과목마다 다른 것(강의·교재, 장 구성, 파일 이름, 번호 규칙, 그림 접두어, 옛 주소)만 모아 둔다. 일반 규칙은 [CLAUDE.md](../CLAUDE.md), 문법은 [writing.md](writing.md).

## Differential Geometry
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

## Modern Physics
- 강의: **김제훈, 조우주**. 중간·기말 범위 모두 포함.
- Part I 양자역학
  - `qm1d.md`: Ch. 5, 1차원 양자역학 (중간)
  - `quantum.md`: Ch. 6, 수소 원자·3차원 양자역학 (기말)
- Part II 특수상대론
  - `sr1.md`: 상대론 I, §1–5 (중간)
  - `sr2.md`: 상대론 II, §6–11 (기말)
- 옛 주소 `relativity/`, `relativity-ko/`는 리다이렉트 페이지다(#6 이상이면 sr2, 아니면 sr1로). 지우지 않는다.
- 새 범위가 생기면 같은 방식(중간/기말 분리)으로 파일을 나누고, `index.md`/`index-ko.md`의 About·Contents와 홈(`docs/index.md`) 표를 함께 갱신한다.

## Abstract Algebra (특강)
- 2026년 11월 25–26일 이틀짜리 현대대수 특강. 슬라이드: Min Hoon Kim (이화여대). 교재: **Serre, *A Course in Arithmetic*, Chapter I (Finite fields)**.
- 날짜별 페이지: `day1.md`(11/25), `day2.md`(11/26, Serre 이어서 + 부록 아이젠슈타인 증명), `triples.md`(11/26 두 번째 강의, 피타고라스 세 쌍. Serre가 아니라 슬라이드 자체 번호 1–5절, 보조정리 1.1, 정리 1.2 …).
- 절 번호는 Serre 1장(§1.1, 1.2, 2.1, 2.2, 3.1–3.3), 정리·보조정리 번호는 슬라이드 그대로(정리 1–6, 보조정리는 절마다 1부터).
- 사용자가 필기하지 않고 건너뛴 슬라이드(빈 증명 칸 등)는 다루지 않은 내용이다. 정리하지 않고 제목만 남겨 skipped 상자로 표시한다.
  1일차 기준: §2 전체, 정리 1 iii)의 증명(강의에서 생략). 정리 5 iii)의 증명은 2일차에 다뤄서 1일차 페이지 해당 자리에 넣었다.
  피타고라스 세 쌍 기준: §2 대수적 증명(패리티 부분만 슬라이드에 인쇄돼 있어 남김)과 보조정리 2.1의 증명, 정리 1.2 역의 증명. 필기 없이 인쇄된 설명만 있는 슬라이드(§4, §5 등)는 내용이 완결돼 있으므로 정리했다.
- 수 집합·체·군(F_q, Z, Q, Z/nZ 등)은 칠판 볼드체 `\mathbb F`로 쓴다(`\mathbf` 쓰지 않는다).
- 1일차는 §3.3 가우스 합의 보조정리 1(y² = (−1)^ε(ℓ) ℓ)에서 끝났다. 2일차는 보조정리 2부터 정리 6의 증명, 비고·예제, 부록(가우스 보조정리, sin 곱 공식, 아이젠슈타인 증명)까지.

## 그림 파일 이름 접두어

미분기하 `ch1-*`, 양자 `qm-*`, 상대론 `rel-*`, 현대대수 특강 `aa-*`.

## 옛 주소 (리다이렉트, 지우지 않는다)

`differential-geometry/lec01/`, `lec02/`, `modern-physics/relativity/`, `relativity-ko/`, `modern-algebra/` (→ `abstract-algebra/`, 2026-11-25 이름 변경).
