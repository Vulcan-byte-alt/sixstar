#!/usr/bin/env python3
"""
Make all titles single-line with ellipsis and add full title on hover
"""

import re

with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("🔧 Making titles single-line with tooltips...")

# Find all h3 titles and add single-line styling with title attribute
def add_single_line_and_tooltip(match):
    """Add single-line truncation and tooltip to h3 titles"""
    full_match = match.group(0)
    title_text = match.group(1).strip()

    # Create new h3 with single-line styling and tooltip
    new_h3 = f'''<h3 style="font-size: 32px; font-family: 'TheSeasons', serif; color: #1a2332; line-height: 1.2; font-weight: 400; margin-bottom: 24px; letter-spacing: 0.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; cursor: pointer;" title="{title_text}">
                                        {title_text}
                                    </h3>'''

    return new_h3

# Pattern to match h3 titles
pattern = r'<h3 style="font-size: 28px; font-family: \'TheSeasons\', serif; color: #1a2332; line-height: 1\.5; font-weight: 400; margin-bottom: 24px; letter-spacing: 0\.4px;">\s*(.*?)\s*</h3>'

updated_html = re.sub(pattern, add_single_line_and_tooltip, html, flags=re.DOTALL)

# Also add a new row in the info box to show full title on hover (optional - adds to expandable section)
# We'll add it to the expand-on-hover section right after title

with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

# Count
count = updated_html.count('text-overflow: ellipsis')

print(f"✅ Updated {count} titles to single-line with ellipsis")
print(f"✅ Added hover tooltips showing full title")
print(f"✅ Font size increased to 32px (since now single line)")
