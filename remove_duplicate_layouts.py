#!/usr/bin/env python3
"""
Remove duplicate vertical info layouts from cards that have more than one
"""

import re
import sys

def remove_duplicate_layouts(file_path):
    """Remove duplicate vertical info layouts within each card"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Split content by article tags
    # For each article, keep only the first vertical info layout

    def process_article(match):
        article_tag = match.group(1)
        article_content = match.group(2)

        # Count vertical info layouts in this article
        layouts = list(re.finditer(
            r'<!-- Vertical Info Layout -->.*?</div>\s*\n',
            article_content,
            re.DOTALL
        ))

        if len(layouts) > 1:
            # Remove all but the first layout
            for layout in reversed(layouts[1:]):
                article_content = (
                    article_content[:layout.start()] +
                    article_content[layout.end():]
                )

        return article_tag + article_content

    # Process each article
    content = re.sub(
        r'(<article[^>]*>)(.*?)(?=<article|</section>)',
        process_article,
        content,
        flags=re.DOTALL
    )

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    changes = len(original_content) - len(content)

    # Count how many layouts remain
    final_count = len(re.findall(r'<!-- Vertical Info Layout -->', content))

    print(f"Removed {changes} characters of duplicate layouts")
    print(f"Vertical info layouts remaining: {final_count}")

    return changes > 0

if __name__ == '__main__':
    file_path = '/mnt/d/Websites/travel/deals.html'

    print("Removing duplicate vertical info layouts...")
    print(f"File: {file_path}")
    print("-" * 60)

    try:
        had_changes = remove_duplicate_layouts(file_path)
        if had_changes:
            print("✓ Duplicates removed!")
        else:
            print("✓ No duplicates found")
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
