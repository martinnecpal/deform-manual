"""
Convert RoboHelp .htm files in _docs/ to clean Jekyll Markdown .md files.

What it does per file:
  1. Reads existing Jekyll front matter (lang, title, etc.)
  2. Extracts <body> content, strips RoboHelp boilerplate divs
  3. Converts remaining HTML to Markdown via html2text
  4. Rewrites internal links: foo/bar.htm  ->  foo/bar/  (Jekyll collection URLs)
  5. Writes <filename>.md alongside the .htm, then deletes the .htm
"""

import os
import re
import sys
import html2text
from bs4 import BeautifulSoup, Comment

DOCS_DIR = os.path.join(os.path.dirname(__file__), '..', '_docs')

# RoboHelp wrapper div IDs / classes to strip entirely before conversion
STRIP_IDS = {'rh-topic-header', 'rh-topic-header-shadow'}
STRIP_CLASSES = {'topic-header', 'topic-header-shadow', 'WebHelpNavBar'}


def extract_front_matter(text):
    """Return (front_matter_str, rest_of_file) or ('', text) if none."""
    if not text.startswith('---'):
        return '', text
    end = text.find('\n---', 3)
    if end == -1:
        return '', text
    fm = text[:end + 4]          # includes closing ---
    rest = text[end + 4:]
    return fm, rest


def rewrite_links(md_text, file_dir, docs_root):
    """
    Turn relative .htm hrefs into Jekyll collection URLs.
    e.g.  ../foo/bar.htm  ->  /docs/en/foo/bar/
    The collection prefix (docs/en or docs/sk) is derived from file_dir.
    """
    # Determine lang prefix from path
    rel = os.path.relpath(file_dir, docs_root)          # e.g. en/about_deform/...
    parts = rel.replace('\\', '/').split('/')
    lang = parts[0] if parts else 'en'                  # 'en' or 'sk'

    def replace_href(m):
        prefix = m.group(1)   # [text]( or src="
        href   = m.group(2)
        suffix = m.group(3)   # ) or "

        # Skip external, anchor-only, or already-converted links
        if href.startswith(('http', 'mailto', '#', '/')):
            return m.group(0)

        # Resolve relative path from file_dir to an absolute path under _docs
        abs_path = os.path.normpath(os.path.join(file_dir, href))
        rel_to_docs = os.path.relpath(abs_path, docs_root).replace('\\', '/')

        # Strip .htm extension and produce Jekyll URL
        rel_to_docs = re.sub(r'\.htm$', '', rel_to_docs, flags=re.IGNORECASE)
        jekyll_url = '/docs/' + rel_to_docs + '/'
        return prefix + jekyll_url + suffix

    # Match Markdown links:  [text](some/path.htm)
    md_link = re.compile(r'(\[.*?\]\()([^)]+\.htm)(\))', re.IGNORECASE)
    # Match Markdown images: ![alt](some/path.png)  — leave alone, just strip .htm if any
    md_text = md_link.sub(replace_href, md_text)
    return md_text


def convert_file(htm_path, docs_root):
    with open(htm_path, encoding='utf-8', errors='replace') as f:
        raw = f.read()

    front_matter, rest = extract_front_matter(raw)

    # --- Parse HTML body ---
    soup = BeautifulSoup(rest, 'lxml')

    # Remove HTML comments
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()

    # Strip RoboHelp-specific wrapper divs
    for div in soup.find_all('div', id=lambda i: i in STRIP_IDS if i else False):
        div.decompose()
    for div in soup.find_all('div', class_=lambda c: bool(c and STRIP_CLASSES.intersection(c))):
        div.decompose()

    # Get body content; fall back to whole soup if no <body>
    body = soup.find('body')
    content_html = str(body) if body else str(soup)

    # --- Convert to Markdown ---
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0            # no hard line wraps
    h.protect_links = False
    h.unicode_snob = True
    h.images_to_alt = False
    h.single_line_break = False

    md_body = h.handle(content_html)

    # Clean up excessive blank lines (3+ -> 2)
    md_body = re.sub(r'\n{3,}', '\n\n', md_body).strip()

    # Rewrite internal .htm links to Jekyll URLs
    file_dir = os.path.dirname(htm_path)
    md_body = rewrite_links(md_body, file_dir, docs_root)

    # --- Write .md file ---
    md_path = re.sub(r'\.htm$', '.md', htm_path, flags=re.IGNORECASE)
    with open(md_path, 'w', encoding='utf-8') as f:
        if front_matter:
            f.write(front_matter + '\n\n')
        f.write(md_body + '\n')

    os.remove(htm_path)
    return md_path


def main():
    docs_root = os.path.abspath(DOCS_DIR)
    htm_files = []
    for dirpath, _, filenames in os.walk(docs_root):
        for fname in filenames:
            if fname.lower().endswith('.htm'):
                htm_files.append(os.path.join(dirpath, fname))

    total = len(htm_files)
    print(f"Found {total} .htm files to convert in {docs_root}")

    errors = []
    for i, path in enumerate(htm_files, 1):
        try:
            md_path = convert_file(path, docs_root)
            rel = os.path.relpath(md_path, docs_root)
            print(f"[{i}/{total}] {rel}")
        except Exception as e:
            errors.append((path, e))
            print(f"[{i}/{total}] ERROR: {path}: {e}", file=sys.stderr)

    print(f"\nDone. {total - len(errors)} converted, {len(errors)} errors.")
    if errors:
        print("\nFailed files:")
        for p, e in errors:
            print(f"  {p}: {e}")


if __name__ == '__main__':
    main()
