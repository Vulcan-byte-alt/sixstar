#!/usr/bin/env python3
"""
Clean up all remaining luxury class references and stray elements from deals.html
"""

import re
import sys

def cleanup_file(file_path):
    """Remove all luxury class divs and other remnants"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Remove luxury-card-body sections with nested content
    # Pattern: <div class="luxury-card-body"> ... </div> (multiple lines)
    content = re.sub(
        r'<div class="luxury-card-body">.*?</div>\s*</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove luxury-price-section divs
    content = re.sub(
        r'<div class="luxury-price-section">.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove any remaining luxury class tags
    content = re.sub(
        r'<div class="luxury-[^"]+">.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove multiple consecutive blank lines (keep max 2)
    content = re.sub(r'\n\n\n+', '\n\n', content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    changes = len(original_content) - len(content)
    print(f"Removed {changes} characters of old luxury class references")

    return changes > 0

if __name__ == '__main__':
    file_path = '/mnt/d/Websites/travel/deals.html'

    print("Cleaning up luxury class remnants...")
    print(f"File: {file_path}")
    print("-" * 60)

    try:
        had_changes = cleanup_file(file_path)
        if had_changes:
            print("✓ Cleanup complete!")
        else:
            print("✓ No changes needed - file was already clean")
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
