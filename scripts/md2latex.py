"""Turn the site's Markdown notes into a LaTeX book and compile it.

The website is the source; this script only produces the PDF.  It rewrites the
MkDocs-specific syntax (admonitions, <figure markdown>, lecture tags, ...) into
plain Pandoc Markdown with raw LaTeX, runs pandoc to get the body, wraps it in
scripts/latex/book.tex and compiles with xelatex.

    python scripts/md2latex.py --site site        # every PDF the site links to (used by CI)
    python scripts/md2latex.py <course-dir> <out.pdf> [--lang en|ko] [--only page.md]

<course-dir> is e.g. docs/differential-geometry.  Pages are the *.md files with a
running head, in file-name order (same order as the web PDFs); index.md (or
index-ko.md) becomes the front matter.
"""
import datetime
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "scripts" / "latex" / "book.tex"
TEXT_PX = 658          # width of the text block in the web PDFs (A4 - margins)

# admonition type -> LaTeX environment (defined in book.tex)
ENV = {
    "note": "defnbox", "abstract": "thmbox", "success": "proofbox",
    "example": "examplebox", "info": "remarkbox", "warning": "cautionbox",
    "quote": "convbox", "skipped": "skippedbox", "question": "remarkbox",
    "tip": "remarkbox",
}
RUN_IN = {"defnbox", "thmbox", "proofbox", "examplebox", "remarkbox", "cautionbox"}


def tex_escape_text(s):
    """Escape a title for LaTeX, leaving $...$ math untouched."""
    out = []
    for i, part in enumerate(re.split(r"(\$[^$]*\$)", s)):
        if i % 2:
            out.append(part)
            continue
        part = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", part)
        part = re.sub(r"\*(.+?)\*", r"\\emph{\1}", part)
        for a, b in [("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_")]:
            part = part.replace(a, b)
        out.append(part)
    return "".join(out)


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def raw(s):
    return f"\n```{{=latex}}\n{s}\n```\n"


class Converter:
    def __init__(self, page_dir, build):
        self.page_dir = page_dir
        self.build = build
        self.meta = {}

    # ---------- figures ----------
    def figure(self, block):
        img = re.search(r"!\[[^\]]*\]\(([^)]+)\)(\{[^}]*\})?", block)
        cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", block, re.S)
        src = self.page_dir / img.group(1)
        width = re.search(r'width="(\d+)"', img.group(2) or "")
        frac = min(1.0, int(width.group(1)) / TEXT_PX) if width else 0.6
        pdf = self.build / (src.stem + ".pdf")
        if not pdf.exists():
            subprocess.run(["rsvg-convert", "-f", "pdf", "-o", str(pdf), str(src)], check=True)
        caption = cap.group(1).strip() if cap else ""
        return raw("\\begin{figure}[htbp]\\centering\n"
                   f"\\includegraphics[width={frac:.3f}\\linewidth]{{{pdf.name}}}\n"
                   f"\\caption{{{tex_escape_text(caption)}}}\n\\end{{figure}}")

    # ---------- main pass ----------
    def convert(self, text):
        text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)       # front matter
        lines = text.split("\n")
        out = self.blocks(lines)
        return "\n".join(out)

    def blocks(self, lines):
        out, i = [], 0
        while i < len(lines):
            line = lines[i]
            s = line.strip()
            # admonition: !!! type "title"
            m = re.match(r'^!!!\s+(\w+)(?:\s+"(.*)")?\s*$', line)
            if m:
                body, i = self.take_indented(lines, i + 1)
                out += self.admonition(m.group(1), m.group(2) or "", body)
                continue
            if s.startswith('<div class="admonition skipped"'):
                j = i + 1
                body = []
                while lines[j].strip() != "</div>":
                    body.append(lines[j]); j += 1
                out += self.admonition("skipped", "", body)
                i = j + 1
                continue
            if s.startswith("<figure"):
                j = i
                while "</figure>" not in lines[j]:
                    j += 1
                out.append(self.figure("\n".join(lines[i:j + 1])))
                i = j + 1
                continue
            if s.startswith('<div class="lang-switch"') or s.startswith('<p class="pdf-links"'):
                i += 1; continue
            m = re.match(r'<div class="running-head"><span>(.*?)</span><span>(.*?)</span></div>', s)
            if m:
                self.meta.setdefault("course", strip_tags(m.group(1)))
                self.meta["head"] = strip_tags(m.group(2))
                i += 1; continue
            m = re.match(r'<p class="lecture-tag">(.*?)</p>', s)
            if m:
                out.append(raw(f"\\lecturetag{{{tex_escape_text(strip_tags(m.group(1)))}}}"))
                i += 1; continue
            m = re.match(r'<p class="source-note">(.*?)</p>', s)
            if m:
                parts = [p for p in m.group(1).split(" · ") if "<a" not in p]
                out.append(raw(f"\\sourcenote{{{tex_escape_text(strip_tags(' · '.join(parts)))}}}"))
                i += 1; continue
            if s == "---":                       # section rules: LaTeX spaces sections itself
                i += 1; continue
            out.append(line)
            i += 1
        return out

    @staticmethod
    def take_indented(lines, i):
        body = []
        while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
            body.append(lines[i][4:] if lines[i].startswith("    ") else "")
            i += 1
        while body and body[-1] == "":
            body.pop()
        # a blank line followed by unindented text ends the block
        return body, i

    def admonition(self, kind, title, body):
        env = ENV.get(kind, "remarkbox")
        body = self.blocks(body)
        t = tex_escape_text(title.rstrip("."))
        if env in RUN_IN:
            first = next((k for k, l in enumerate(body) if l.strip()), None)
            fl = body[first].lstrip() if first is not None else ""
            starts_text = (first is not None and not re.match(r"(\$\$|\d+\.\s|[-*+]\s|\||```|<)", fl))
            head = f"\\boxtitle{{{t}}}" if t else ""
            if starts_text and head:
                body[first] = f"`{head}`{{=latex}}" + body[first]
                head = ""
            return [raw(f"\\begin{{{env}}}{{{head}}}")] + body + [raw(f"\\end{{{env}}}")]
        return [raw(f"\\begin{{{env}}}{{{t}}}")] + body + [raw(f"\\end{{{env}}}")]


def pandoc(md, lang):
    args = ["pandoc", "-f", "markdown+raw_attribute+tex_math_dollars-implicit_figures",
            "-t", "latex", "--top-level-division=chapter", "--wrap=preserve"]
    tex = subprocess.run(args, input=md, capture_output=True, text=True, check=True).stdout
    tex = re.sub(r"\\\[(.*?)\\\]", fit_display, tex, flags=re.S)
    # characters Latin Modern lacks, which may also sit inside math
    tex = re.sub("([\u2460-\u24ff])", r"\\text{\1}", tex)
    return tex.replace("\u27e8", r"\ensuremath{\langle}").replace("\u27e9", r"\ensuremath{\rangle}")


def fit_display(m):
    """Shrink a one-line display that is wider than the text block (\\fitmath in book.tex)."""
    body = m.group(1)
    outer = re.sub(r"\\begin\{(\w+\*?)\}.*?\\end\{\1\}", "", body, flags=re.S)
    if "\\\\" in outer:
        return m.group(0)
    return "\\[\\fitmath{" + body + "}\\]"


def front_matter(text, conv):
    """index.md -> title page + intro sections (its Contents list is replaced by \\tableofcontents)."""
    title = re.search(r"^# (.*?)(\s*\{[^}]*\})?$", text, re.M).group(1)
    subject = re.search(r'<p class="subject-line">(.*?)</p>', text)
    info = re.search(r'<p class="course-info">(.*?)</p>', text)
    rh = re.search(r'<div class="running-head"><span>(.*?)</span><span>(.*?)</span>', text)
    body = text.split("\n## ", 1)[1]
    body = "## " + re.split(r"\n## [^\n]*\{ \.contents-heading \}", body)[0]
    body_tex = pandoc("\n".join(conv.blocks(body.split("\n"))), None)
    body_tex = body_tex.replace("\\section{", "\\section*{")
    def inline(s):
        s = re.sub(r"<em>(.*?)</em>", r"\\emph{\1}", s)
        s = s.replace("<br>", r"\\")
        return tex_escape_text(html.unescape(re.sub(r"<(?!/?em)[^>]+>", "", s)))
    return {
        "course": tex_escape_text(strip_tags(rh.group(1))), "term": tex_escape_text(strip_tags(rh.group(2))),
        "title": tex_escape_text(title),
        "subject": inline(subject.group(1)) if subject else "",
        "info": inline(info.group(1)) if info else "",
        "intro": body_tex,
    }


def build_pdf(course, lang, pages, out, full):
    """Compile `pages` of one course into `out`.  full=True adds title page, intro and contents."""
    build = Path(tempfile.mkdtemp(prefix="notes-tex-"))
    conv = Converter(course, build)
    suffix = "-ko" if lang == "ko" else ""
    fm = front_matter((course / f"index{suffix}.md").read_text(), conv)
    chapters = []
    for p in pages:
        conv.meta = {}
        tex = pandoc(conv.convert(p.read_text()), lang)
        chapters.append(f"\\renewcommand\\chapterhead{{{tex_escape_text(conv.meta.get('head', ''))}}}\n" + tex)
    doc = (TEMPLATE.read_text().replace("%%LANG%%", lang)
           .replace("%%FULL%%", "true" if full else "false")
           .replace("%%COURSE%%", fm["course"]).replace("%%TERM%%", fm["term"])
           .replace("%%TITLE%%", fm["title"]).replace("%%SUBJECT%%", fm["subject"])
           .replace("%%INFO%%", fm["info"]).replace("%%INTRO%%", fm["intro"])
           .replace("%%BODY%%", "\n\\cleardoublepage\n".join(chapters)))
    (build / "book.tex").write_text(doc)
    for _ in range(2):                      # second run fills in the contents page numbers
        r = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "book.tex"],
                           cwd=build, capture_output=True, text=True)
        if r.returncode:
            print(r.stdout[-3000:]); print("build dir:", build)
            raise SystemExit(f"LaTeX failed for {out}")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(build / "book.pdf", out)
    shutil.rmtree(build, ignore_errors=True)
    m = re.search(r"Output written on book\.pdf \((\d+) pages?", r.stdout)
    pages = int(m.group(1)) if m else 0
    print("wrote", out, f"({pages} pages)")
    return pages


def note_pages(course, lang):
    return sorted(p for p in course.glob("*.md")
                  if p.stem not in ("index", "index-ko")
                  and p.stem.endswith("-ko") == (lang == "ko")
                  and 'class="running-head"' in p.read_text())


def running_head(md):
    m = re.search(r'<div class="running-head"><span>(.*?)</span><span>(.*?)</span>', md.read_text())
    return (strip_tags(m.group(1)), strip_tags(m.group(2))) if m else ("", "")


def download_name(md, default):
    """The download="..." file name of the page's PDF link (a.pdf-link or .pdf-links a)."""
    for line in md.read_text().splitlines():
        if "pdf-link" in line:
            m = re.search(r'class="pdf-link"[^>]*download="([^"]+)"', line) or                 re.search(r'download="([^"]+)"', line)
            if m:
                return m.group(1)
    return default


def last_changed(path):
    """Date of the last commit touching `path` (needs full history in CI), else today."""
    try:
        d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
    except OSError:
        d = ""
    return d or datetime.date.today().isoformat()


def thumbnail(pdf, out):
    """Page 1 of `pdf` as a small JPEG for the home page (pdftoppm, poppler-utils)."""
    try:
        subprocess.run(["pdftoppm", "-f", "1", "-l", "1", "-singlefile", "-jpeg",
                        "-jpegopt", "quality=82", "-scale-to", "520", str(pdf), str(out.with_suffix(""))],
                       check=True, capture_output=True)
        return True
    except (OSError, subprocess.CalledProcessError) as e:
        print("thumbnail skipped:", e)
        return False


def build_site(site):
    """All PDFs the site links to: <course>/all-lectures(-ko).pdf and <course>/<page>/notes.pdf.

    Also writes site/manifest.json (read by the home page and the PDF viewer): per course its
    names, page counts and last change; per PDF its language, the other edition, the download
    name and a title.  And <course>/thumb.jpg, page 1 of the Korean full PDF."""
    manifest = {"updated": datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
                .isoformat(timespec="minutes"), "courses": [], "pdfs": {}}
    for course in sorted((ROOT / "docs").iterdir()):
        if not (course / "index.md").exists():
            continue
        c = course.name
        entry = {"id": c, "en": running_head(course / "index.md")[0],
                 "ko": running_head(course / "index-ko.md")[0] if (course / "index-ko.md").exists() else "",
                 "updated": last_changed(course), "parts": 0, "pages": {}}
        for lang in ("en", "ko"):
            pages = note_pages(course, lang)
            if not pages:
                continue
            ko = lang == "ko"
            suffix, other = ("-ko", "") if ko else ("", "-ko")
            idx = course / f"index{suffix}.md"
            course_name = running_head(idx)[0]
            name = "all-lectures-ko.pdf" if ko else "all-lectures.pdf"
            n = build_pdf(course, lang, pages, site / c / name, full=True)
            entry["pages"][lang] = n
            entry["parts"] = len(pages)
            manifest["pdfs"][f"{c}/{name}"] = {
                "lang": lang, "pair": f"{c}/all-lectures{other}.pdf", "pages": n,
                "name": download_name(idx, name),
                "title": course_name + (" · 전체" if ko else " · All parts"),
                "back": f"{c}/index-ko/" if ko else f"{c}/"}
            for p in pages:
                n = build_pdf(course, lang, [p], site / c / p.stem / "notes.pdf", full=False)
                base = p.stem[:-3] if ko else p.stem
                manifest["pdfs"][f"{c}/{p.stem}/notes.pdf"] = {
                    "lang": lang, "pair": f"{c}/{base}{other}/notes.pdf", "pages": n,
                    "name": download_name(p, "notes.pdf"),
                    "title": course_name + " · " + running_head(p)[1],
                    "back": f"{c}/{p.stem}/"}
        full = site / c / "all-lectures-ko.pdf"
        if not full.exists():
            full = site / c / "all-lectures.pdf"
        if full.exists() and thumbnail(full, site / c / "thumb.jpg"):
            entry["thumb"] = f"{c}/thumb.jpg"
        manifest["courses"].append(entry)
    (site / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", site / "manifest.json")


def main():
    if sys.argv[1] == "--site":
        build_site(Path(sys.argv[2]).resolve())
        return
    course = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    lang = "ko" if "--lang" in sys.argv and sys.argv[sys.argv.index("--lang") + 1] == "ko" else "en"
    if "--only" in sys.argv:
        build_pdf(course, lang, [course / sys.argv[sys.argv.index("--only") + 1]], out, full=False)
    else:
        build_pdf(course, lang, note_pages(course, lang), out, full=True)


if __name__ == "__main__":
    main()
