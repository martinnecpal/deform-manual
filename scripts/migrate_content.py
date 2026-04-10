"""
Copy documentation_content/ → _docs/en/
Copy sk/documentation_content/ → _docs/sk/
Add Jekyll front matter to each .htm file.

Usage:
    python scripts/migrate_content.py

Safe to re-run — skips files that already have front matter.
"""

import os
import re
import shutil

BASE = os.path.join(os.path.dirname(__file__), '..')


def title_from_html(html: str) -> str:
    """Extract <title> or first <h1>/<h2> text from HTML."""
    m = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'<h[12][^>]*>([^<]+)</h[12]>', html, re.IGNORECASE)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return ''


def safe_title(t: str) -> str:
    """Escape quotes for YAML front matter."""
    return t.replace('"', '\\"')


def add_front_matter(path: str, lang: str):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    if content.startswith('---'):
        return  # already done

    title = safe_title(title_from_html(content))
    fm_lines = ['---', f'lang: {lang}']
    if title:
        fm_lines.append(f'title: "{title}"')
    fm_lines.append('---')
    fm = '\n'.join(fm_lines) + '\n'

    with open(path, 'w', encoding='utf-8') as f:
        f.write(fm + content)


def copy_tree(src: str, dst: str, lang: str):
    copied = 0
    skipped = 0
    for root, dirs, files in os.walk(src):
        # Compute destination directory
        rel = os.path.relpath(root, src)
        dest_dir = os.path.join(dst, rel)
        os.makedirs(dest_dir, exist_ok=True)

        for fname in files:
            src_file = os.path.join(root, fname)
            dst_file = os.path.join(dest_dir, fname)

            # Copy if destination doesn't exist or source is newer
            if not os.path.exists(dst_file) or \
               os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                shutil.copy2(src_file, dst_file)
                if fname.lower().endswith('.htm'):
                    add_front_matter(dst_file, lang)
                copied += 1
            else:
                skipped += 1

    print(f"  {lang}: {copied} copied, {skipped} skipped")


def main():
    # English
    en_src = os.path.join(BASE, 'documentation_content')
    en_dst = os.path.join(BASE, '_docs', 'en')
    print(f"Copying EN: {en_src} -> {en_dst}")
    copy_tree(en_src, en_dst, 'en')

    # Slovak
    sk_src = os.path.join(BASE, 'sk', 'documentation_content')
    sk_dst = os.path.join(BASE, '_docs', 'sk')
    print(f"Copying SK: {sk_src} -> {sk_dst}")
    copy_tree(sk_src, sk_dst, 'sk')

    print("Done.")


if __name__ == '__main__':
    main()
