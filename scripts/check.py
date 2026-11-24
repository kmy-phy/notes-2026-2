#!/usr/bin/env python3
"""배포 전 자동 점검 — 빌드된 사이트(site/)를 읽어 깨진 페이지를 찾는다.

    python scripts/check.py [site]

검사 항목 (하나라도 틀리면 종료 코드 1, 배포 중단):
  1. 영어판/한국어판 짝(<page>.md ↔ <page>-ko.md)마다
     - 제목 앵커(id) 목록이 순서까지 같은지  → 언어 탭·목차 링크가 같은 곳으로 가는지
     - 수식 블록($$), 그림, 표, 상자(종류별) 개수가 같은지
  2. 모든 노트 페이지에서
     - 마크다운이 변환되지 않고 글자로 남은 곳(!!!, ???, { #, $$, $x$, **, ](…) 등)
     - 본문 안의 상대 링크·그림이 실제 파일을 가리키는지 (언어 탭, PDF 링크 포함)
경고만 하는 항목: 인라인 수식 개수 차이 (번역하면서 조금 달라질 수 있음).

CLAUDE.md §3, §6의 손 점검을 자동으로 하는 것이다. 표준 라이브러리만 쓴다.
"""
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

SITE = sys.argv[1] if len(sys.argv) > 1 else "site"
DOCS = "docs"

# 변환되지 않은 마크다운 흔적 (코드·수식 밖의 글자에서만 찾는다)
LEAKS = [
    (re.compile(r"^\s*(!!!|\?\?\?\+?)\s"), "상자 문법(!!!/???)이 그대로 보임"),
    (re.compile(r"\{\s*[#.:][^}]*\}"), "속성 문법({ #… } / { .… })이 그대로 보임"),
    (re.compile(r"\$\$"), "$$ 가 그대로 보임 (수식 블록 앞뒤 빈 줄?)"),
    (re.compile(r"(?<![\w$])\$[^\s$][^$\n]*?\$(?![\w$])"), "$…$ 수식이 변환되지 않음"),
    (re.compile(r"\*\*\S"), "** 굵게 문법이 그대로 보임"),
    (re.compile(r"\]\((?:[^)\s]+)\)"), "링크 문법 ](…) 이 그대로 보임"),
    (re.compile(r"</?(div|span|figure|figcaption|p|a)\b[^>]*>"), "HTML 태그가 글자로 보임"),
    (re.compile(r"^\s*#{1,6}\s+\S"), "제목 문법(#)이 그대로 보임"),
]
SKIP_TEXT_TAGS = {"code", "pre", "script", "style", "kbd", "samp"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "source", "track", "wbr"}


class Page(HTMLParser):
    """md-content__inner(본문) 안만 본다."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # 열린 태그 (본문 안)
        self.depth = 0           # 본문 진입 후 깊이, 0이면 본문 밖
        self.skip = 0            # 코드/수식 안 깊이
        self.ids, self.links = [], []
        self.counts = {}
        self.inline_math = 0
        self.text = []           # (줄 번호, 글자)

    def _count(self, k):
        self.counts[k] = self.counts.get(k, 0) + 1

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if not self.depth:
            if tag == "article" and "md-content__inner" in cls:
                self.depth = 1
            return
        if tag not in VOID:
            self.depth += 1
            closes_skip = tag in SKIP_TEXT_TAGS or "arithmatex" in cls
            self.stack.append((tag, closes_skip))
            if closes_skip:
                self.skip += 1
        if re.fullmatch(r"h[1-6]", tag) and a.get("id"):
            self.ids.append(a["id"])
        if "arithmatex" in cls:
            if tag == "div":
                self._count("수식 블록")
            else:
                self.inline_math += 1
        if tag == "figure":
            self._count("그림")
        if tag == "table":
            self._count("표")
        if tag in ("div", "details") and ("admonition" in cls or tag == "details"):
            kind = next((c for c in cls if c not in ("admonition",)), "plain")
            self._count("상자:" + kind)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.links.append(a["src"])

    def handle_endtag(self, tag):
        if not self.depth or tag in VOID:
            return
        # 짝이 안 맞는 닫는 태그에도 견디도록 스택에서 찾아 닫는다
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for _, sk in self.stack[i:]:
                    if sk:
                        self.skip -= 1
                    self.depth -= 1
                del self.stack[i:]
                break
        else:
            if tag == "article" and not self.stack:
                self.depth = 0

    def handle_data(self, data):
        if self.depth and not self.skip and data.strip():
            self.text.append((self.getpos()[0], data))


def parse(path):
    p = Page()
    with open(path, encoding="utf-8") as f:
        p.feed(f.read())
    return p


def site_html(md_rel):
    """docs 기준 md 경로 → site의 html 경로 (use_directory_urls)."""
    stem = md_rel[:-3]
    if os.path.basename(stem) == "index":
        return os.path.join(SITE, os.path.dirname(stem), "index.html")
    return os.path.join(SITE, stem, "index.html")


def main():
    if not os.path.isdir(SITE):
        sys.exit(f"{SITE}/ 가 없음. 먼저 mkdocs build")
    errors, warnings = [], []
    # PDF는 md2latex.py가 만든다. 그 전에 돌렸으면 PDF 링크는 건너뛴다.
    have_pdfs = any("notes.pdf" in fs for _, _, fs in os.walk(SITE))

    md_files = sorted(os.path.relpath(os.path.join(d, f), DOCS).replace(os.sep, "/")
                      for d, _, fs in os.walk(DOCS) for f in fs if f.endswith(".md"))
    pages = {}
    for md in md_files:
        html = site_html(md)
        if not os.path.exists(html):
            errors.append(f"{md}: 빌드 결과 {html} 가 없음")
            continue
        pages[md] = parse(html)

    # 1. 영어판/한국어판 짝
    pairs = 0
    for md in md_files:
        if md.endswith("-ko.md"):
            if md[:-6] + ".md" not in pages:
                errors.append(f"{md}: 짝인 영어판 {md[:-6]}.md 가 없음")
            continue
        ko = md[:-3] + "-ko.md"
        if ko not in pages or md not in pages:
            continue
        pairs += 1
        en_p, ko_p = pages[md], pages[ko]
        if en_p.ids != ko_p.ids:
            missing = [i for i in en_p.ids if i not in ko_p.ids]
            extra = [i for i in ko_p.ids if i not in en_p.ids]
            msg = f"{md} ↔ {ko}: 제목 앵커가 다름"
            if missing:
                msg += f"\n      한국어판에 없음: {', '.join(missing[:8])}"
            if extra:
                msg += f"\n      한국어판에만 있음: {', '.join(extra[:8])}"
            if not missing and not extra:
                first = next(k for k, (x, y) in enumerate(zip(en_p.ids, ko_p.ids)) if x != y)
                msg += f"\n      순서가 다름 ({first + 1}번째 제목: {en_p.ids[first]} vs {ko_p.ids[first]})"
            errors.append(msg)
        for k in sorted(set(en_p.counts) | set(ko_p.counts)):
            a, b = en_p.counts.get(k, 0), ko_p.counts.get(k, 0)
            if a != b:
                errors.append(f"{md} ↔ {ko}: {k} 개수 다름 (영어 {a}, 한국어 {b})")
        if en_p.inline_math != ko_p.inline_math:
            warnings.append(f"{md} ↔ {ko}: 인라인 수식 개수 다름 (영어 {en_p.inline_math}, "
                            f"한국어 {ko_p.inline_math})")

    # 2. 페이지마다: 마크다운 흔적, 깨진 링크
    for md, p in pages.items():
        html = site_html(md)
        for line, text in p.text:
            for rx, why in LEAKS:
                m = rx.search(text)
                if m:
                    snippet = text.strip().replace("\n", " ")[:70]
                    errors.append(f"{md} (html {line}행): {why}: “{snippet}”")
        base = os.path.dirname(html)
        for href in p.links:
            u = urlsplit(href)
            if u.scheme or u.netloc or href.startswith(("#", "mailto:", "data:")):
                continue
            path = unquote(u.path)
            if not path:
                continue
            target = os.path.normpath(os.path.join(SITE if path.startswith("/") else base,
                                                   path.lstrip("/")))
            if path.endswith("/") or os.path.isdir(target):
                target = os.path.join(target, "index.html")
            if target.endswith(".pdf") and not have_pdfs:
                continue        # PDF 생성 전에 돌린 경우
            if not os.path.exists(target):
                errors.append(f"{md}: 깨진 링크 {href}")

    for w in warnings:
        print("경고:", w)
    for e in errors:
        print("오류:", e)
    print(f"\n페이지 {len(pages)}개, 영/한 짝 {pairs}개 점검"
          + ("" if have_pdfs else " (PDF 없음: PDF 링크는 건너뜀)")
          + f" — 오류 {len(errors)}, 경고 {len(warnings)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
