#!/usr/bin/env python3
"""
Final cleanup:
1. Remove duplicate pricing sections
2. Add pricing to second Athens to Civitavecchia card
"""

import re

def read_file(filepath: str) -> str:
    """Read the entire file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath: str, content: str):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def remove_duplicate_pricing_sections(content: str) -> tuple:
    """Remove duplicate pricing sections that appear consecutively."""
    removed = 0

    # Pattern to match a pricing section followed immediately by another pricing section
    duplicate_pattern = r'(<div style="padding: 24px 0; border-top: 1px solid rgba\(10,25,41,0\.08\); border-bottom: 1px solid rgba\(10,25,41,0\.08\); margin-bottom: 32px;">.*?</div>\s*</div>)\s*<!-- CTA Buttons - Full Width -->\s*(<div style="padding: 24px 0; border-top: 1px solid rgba\(10,25,41,0\.08\); border-bottom: 1px solid rgba\(10,25,41,0\.08\); margin-bottom: 32px;">.*?</div>\s*</div>)'

    matches = list(re.finditer(duplicate_pattern, content, re.DOTALL))

    if matches:
        print(f"Found {len(matches)} duplicate pricing sections")
        for match in reversed(matches):  # Process in reverse to maintain positions
            # Keep the first, remove the second
            content = content[:match.start(2)] + content[match.end(2):]
            removed += 1
            print(f"  ✓ Removed duplicate pricing section")

    return content, removed

def add_pricing_to_second_athens_civitavecchia(content: str) -> tuple:
    """Add pricing to the second Athens to Civitavecchia card (Silver Muse)."""
    # Find the second Athens to Civitavecchia (Silver Muse)
    pattern = r'(Athens to Civitavecchia</h3>.*?Silver\s+Muse.*?</div>\s*</div>)\s*(.*?<button class="luxury-heart-btn")'

    match = re.search(pattern, content, re.DOTALL)

    if match:
        # Create pricing section
        pricing_html = '''
<div style="padding: 24px 0; border-top: 1px solid rgba(10,25,41,0.08); border-bottom: 1px solid rgba(10,25,41,0.08); margin-bottom: 32px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-family: 'Montserrat', sans-serif; font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em; color: #999; margin-bottom: 8px;">From</div>
            <div style="display: flex; align-items: baseline; gap: 12px;">
                <span style="font-family: 'Montserrat', sans-serif; font-size: 16px; color: #999; text-decoration: line-through;">£5400</span>
                <span style="font-family: 'Playfair Display', serif; font-size: 40px; font-weight: 400; color: var(--navy); line-height: 1;">£4949</span>
                <span style="font-family: 'Montserrat', sans-serif; font-size: 16px; color: #666; font-weight: 500;">pp</span>
            </div>
        </div>
        <div style="background: linear-gradient(135deg, var(--gold) 0%, #d4a574 100%); color: white; padding: 8px 20px; border-radius: 50px; font-family: 'Montserrat', sans-serif; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">-8% OFF</div>
    </div>
</div>

'''

        # Insert pricing before the luxury-heart-btn
        insert_pos = match.start(2)
        content = content[:insert_pos] + pricing_html + content[insert_pos:]
        print("  ✓ Added pricing to second Athens to Civitavecchia card (Silver Muse)")
        return content, True

    return content, False

def main():
    filepath = '/mnt/d/Websites/travel/deals.html'

    print("="*80)
    print("FINAL CLEANUP")
    print("="*80)

    print("\n1. Reading file...")
    content = read_file(filepath)

    print("\n2. Removing duplicate pricing sections...")
    content, removed = remove_duplicate_pricing_sections(content)
    print(f"   Removed {removed} duplicates")

    print("\n3. Adding pricing to second Athens to Civitavecchia card...")
    content, added = add_pricing_to_second_athens_civitavecchia(content)
    if not added:
        print("   ⚠️ Could not find second Athens to Civitavecchia card")

    print("\n4. Writing file...")
    write_file(filepath, content)

    print("\n✓ Final cleanup complete!")

if __name__ == '__main__':
    main()
