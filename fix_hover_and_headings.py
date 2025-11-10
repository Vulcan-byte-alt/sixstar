#!/usr/bin/env python3
"""
Fix three issues:
1. Add expand-on-hover functionality to article tags
2. Handle long headings by reducing font size
3. Prepare for image downloads
"""

import re

def fix_hover_and_headings(html_content):
    """
    Fix card hover expansion and handle long headings
    """

    # 1. Fix article hover to include expand-on-hover functionality
    old_hover = r'''onmouseover="this\.style\.transform='translateY\(-4px\)'; this\.style\.boxShadow='0 16px 48px rgba\(0,0,0,0\.12\)'"
                            onmouseout="this\.style\.transform='translateY\(0\)'; this\.style\.boxShadow='0 8px 32px rgba\(0,0,0,0\.08\)'"'''

    new_hover = r'''onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 48px rgba(0,0,0,0.12)'; this.style.borderColor='rgba(212, 175, 55, 0.3)'; this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'});"
                            onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0,0,0,0.08)'; this.style.borderColor='rgba(255,255,255,0.8)'; this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})"'''

    html_content = re.sub(old_hover, new_hover, html_content)

    # 2. Handle long headings - reduce font size for titles over 60 characters
    def adjust_title_font(match):
        full_tag = match.group(0)
        title_text = match.group(1)

        # If title is very long, reduce font size
        if len(title_text) > 70:
            # Very long - use 26px
            new_tag = full_tag.replace('font-size: 34px', 'font-size: 26px')
            new_tag = new_tag.replace('line-height: 1.35', 'line-height: 1.3')
        elif len(title_text) > 50:
            # Long - use 30px
            new_tag = full_tag.replace('font-size: 34px', 'font-size: 30px')
            new_tag = new_tag.replace('line-height: 1.35', 'line-height: 1.3')
        else:
            new_tag = full_tag

        return new_tag

    # Pattern to match h3 titles
    title_pattern = r'<h3 style="font-size: 34px[^>]*>([^<]+)</h3>'
    html_content = re.sub(title_pattern, adjust_title_font, html_content)

    return html_content

if __name__ == "__main__":
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("🔧 Fixing issues...")
    print("  1. Adding expand-on-hover to article hover events")
    print("  2. Adjusting font size for long headings")

    updated_html = fix_hover_and_headings(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ Fixed hover expansion and long headings!")

    # Now extract all titles to prepare for image downloads
    print("\n📋 Extracting cruise titles for image downloads...")
    titles = re.findall(r'<h3[^>]*>([^<]+)</h3>', updated_html)

    print(f"\n Found {len(titles)} cruise titles:")
    for i, title in enumerate(titles[:10], 1):
        print(f"  {i}. {title[:60]}{'...' if len(title) > 60 else ''}")
    if len(titles) > 10:
        print(f"  ... and {len(titles) - 10} more")
