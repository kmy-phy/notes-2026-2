"""빌드된 사이트(site/)의 노트 페이지들을 PDF로 저장한다.

- 머리말(running-head)이 있는 페이지마다 같은 폴더에 notes.pdf 를 만든다.
  예: site/differential-geometry/lec02/index.html -> site/differential-geometry/lec02/notes.pdf
- 과목 폴더(예: site/differential-geometry/)마다 첫 페이지 + 모든 강의를
  순서대로 합친 all-lectures.pdf 를 만든다.

GitHub Actions에서 `mkdocs build` 다음에 실행된다:
    python scripts/make_pdfs.py site
"""

import functools
import http.server
import sys
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

SITE = Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
PORT = 8123

FOOTER = (
    '<div style="width:100%;text-align:center;font-size:8pt;'
    'font-family:serif;color:#444"><span class="pageNumber"></span></div>'
)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve():
    handler = functools.partial(QuietHandler, directory=str(SITE))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def note_pages():
    """머리말(running-head)이 있는 페이지 = 노트 페이지."""
    pages = []
    for html in sorted(SITE.rglob("index.html")):
        if html.parent == SITE:
            continue
        if 'class="running-head"' in html.read_text(encoding="utf-8"):
            pages.append(html.parent)
    return pages


def render(page, folder: Path):
    url = f"http://127.0.0.1:{PORT}/{folder.relative_to(SITE).as_posix()}/"
    page.goto(url, wait_until="networkidle", timeout=60_000)
    # 수식(MathJax)과 글꼴이 다 그려질 때까지 기다림
    page.wait_for_function("window.MathJax && MathJax.startup && MathJax.startup.promise", timeout=60_000)
    page.evaluate("MathJax.startup.promise")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    out = folder / "notes.pdf"
    page.pdf(
        path=str(out),
        format="A4",
        margin={"top": "18mm", "bottom": "20mm", "left": "18mm", "right": "18mm"},
        print_background=True,
        display_header_footer=True,
        header_template="<span></span>",
        footer_template=FOOTER,
    )
    return out


def main():
    httpd = serve()
    made = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for folder in note_pages():
            made[folder] = render(page, folder)
            print("PDF:", made[folder].relative_to(SITE))
        browser.close()
    httpd.shutdown()

    # 과목별 전체 묶음: 과목 첫 페이지 + 강의 페이지들(폴더 이름 순)
    for course in sorted({f for f in made if f.parent == SITE}):
        parts = [made[course]] + [made[f] for f in sorted(made) if f.parent == course]
        writer = PdfWriter()
        for part in parts:
            writer.append(str(part))
        out = course / "all-lectures.pdf"
        writer.write(str(out))
        print("PDF:", out.relative_to(SITE), f"({len(parts)} parts)")


if __name__ == "__main__":
    main()
