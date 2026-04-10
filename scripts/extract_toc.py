"""
Extract RoboHelp TOC from whxdata/toc*.new.js files and write _data/nav_en.yml
and _data/nav_sk.yml.

Usage:
    python scripts/extract_toc.py

Reads from:  whxdata/toc*.new.js  (English TOC)
Writes to:   _data/nav_en.yml
             _data/nav_sk.yml
"""

import re
import json
import os
import sys

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

TOC_DIR = os.path.join(os.path.dirname(__file__), '..', 'whxdata')
OUT_DIR = os.path.join(os.path.dirname(__file__), '..', '_data')


def load_toc_file(key: str) -> list:
    """Parse a single toc<key>.new.js file and return the JSON array."""
    filename = f"toc{key}.new.js" if key else "toc.new.js"
    path = os.path.join(TOC_DIR, filename)
    if not os.path.exists(path):
        print(f"  [warn] missing {filename}", file=sys.stderr)
        return []
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    # Extract the array from:  var toc = [...];
    m = re.search(r'var toc\s*=\s*(\[.*?\]);', raw, re.DOTALL)
    if not m:
        print(f"  [warn] could not parse {filename}", file=sys.stderr)
        return []
    return json.loads(m.group(1))


def rewrite_url(url: str, lang: str = 'en') -> str:
    """
    Convert RoboHelp relative URL to Jekyll collection URL.
    e.g. 'documentation_content/about_deform/about_deform.htm'
      -> '/docs/en/about_deform/about_deform/'
    """
    if not url:
        return '#'
    # Strip leading 'documentation_content/'
    url = re.sub(r'^documentation_content/', '', url)
    # Drop extension
    url = re.sub(r'\.(htm|html)$', '', url, flags=re.IGNORECASE)
    return f"/docs/{lang}/{url}/"


def build_tree(nodes: list, lang: str = 'en') -> list:
    """Recursively expand book nodes into children lists."""
    result = []
    for node in nodes:
        entry = {
            'name': node['name'],
            'url': rewrite_url(node.get('url', ''), lang),
        }
        if node.get('type') == 'book' and node.get('key'):
            # key is like "toc1" -> strip "toc" prefix to get the file number
            key_str = node['key'].replace('toc', '')
            children_raw = load_toc_file(key_str)
            if children_raw:
                entry['children'] = build_tree(children_raw, lang)
        result.append(entry)
    return result


# ---------------------------------------------------------------------------
# YAML serialiser (minimal, no PyYAML dependency)
# ---------------------------------------------------------------------------

def to_yaml(nodes: list, indent: int = 0) -> str:
    lines = []
    pad = '  ' * indent
    for node in nodes:
        lines.append(f"{pad}- name: {yaml_str(node['name'])}")
        lines.append(f"{pad}  url: {node['url']}")
        if 'children' in node and node['children']:
            lines.append(f"{pad}  children:")
            lines.append(to_yaml(node['children'], indent + 2))
    return '\n'.join(lines)


def yaml_str(s: str) -> str:
    """Quote a string if it contains special YAML characters."""
    if any(c in s for c in (':', '#', '[', ']', '{', '}', '&', '*', '!', '|', '>', "'", '"', '%', '@', '`')):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("Reading English TOC...")
    root_nodes = load_toc_file('')          # toc.new.js
    en_tree = build_tree(root_nodes, 'en')

    out_en = os.path.join(OUT_DIR, 'nav_en.yml')
    with open(out_en, 'w', encoding='utf-8') as f:
        f.write(to_yaml(en_tree))
        f.write('\n')
    print(f"Written: {out_en}")

    # Slovak TOC — same structure, just different URL prefix.
    # If sk/ has its own whxdata use that; otherwise rewrite en tree with 'sk'.
    sk_whxdata = os.path.join(os.path.dirname(__file__), '..', 'sk', 'whxdata')
    if os.path.isdir(sk_whxdata):
        global TOC_DIR
        TOC_DIR = sk_whxdata
        print("Reading Slovak TOC from sk/whxdata/...")
        root_nodes_sk = load_toc_file('')
        sk_tree = build_tree(root_nodes_sk, 'sk')
    else:
        print("No sk/whxdata found — rewriting EN URLs for SK...")
        sk_tree = rewrite_tree_lang(en_tree, 'sk')

    out_sk = os.path.join(OUT_DIR, 'nav_sk.yml')
    with open(out_sk, 'w', encoding='utf-8') as f:
        f.write(to_yaml(sk_tree))
        f.write('\n')
    print(f"Written: {out_sk}")
    print("Done.")


def rewrite_tree_lang(nodes: list, lang: str) -> list:
    """Deep-copy a tree, replacing /docs/en/ with /docs/<lang>/."""
    result = []
    for node in nodes:
        entry = {
            'name': node['name'],
            'url': node['url'].replace('/docs/en/', f'/docs/{lang}/'),
        }
        if 'children' in node:
            entry['children'] = rewrite_tree_lang(node['children'], lang)
        result.append(entry)
    return result


if __name__ == '__main__':
    main()
