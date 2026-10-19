# 노트 쓰는 법

노트는 전부 `docs/` 폴더 안의 `.md`(마크다운) 파일이에요.

## 수식

- 문장 속 수식: `$E = mc^2$` → $E = mc^2$
- 따로 떨어진 수식:

```
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}
$$
```

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}
$$

## 강조 상자

```
!!! note "제목"
    내용은 4칸 들여쓰기
```

`note` 대신 `tip`, `warning`, `example`, `question`도 쓸 수 있어요.

## 그림

이미지를 `docs/images/`에 넣고:

```
![설명](../images/그림.png)
```

## 새 노트 추가하기

1. `docs/과목폴더/파일이름.md` 만들기 (파일 이름은 영어 추천)
2. `mkdocs.yml`의 `nav:`에 한 줄 추가
3. 커밋하면 1~2분 뒤 사이트에 반영
