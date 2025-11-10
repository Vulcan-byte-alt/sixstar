#!/usr/bin/env python3
"""
Add full voyage title to the info box for better visibility of long titles
"""

import re

with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("🔧 Adding 'Voyage' field to info boxes...")

# Pattern to match h3 with title attribute and subsequent info box
pattern = r'(<h3[^>]*title="([^"]+)"[^>]*>.*?</h3>.*?<!-- Rich Info Box -->.*?<div style="display: grid; grid-template-columns: repeat\(2, 1fr\); gap: 18px;">)'

def add_voyage_field(match):
    """Add voyage field to info box"""
    full_match = match.group(1)
    title_text = match.group(2)

    # Add voyage field after the grid opening
    new_content = full_match + f'''
                                            <div style="grid-column: 1 / -1; padding-bottom: 12px; border-bottom: 1px solid rgba(212, 175, 55, 0.15);">
                                                <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: 'Inter', sans-serif;">Voyage</div>
                                                <div style="color: #1a2332; font-size: 15px; font-weight: 400; font-family: 'Cormorant Garamond', serif; line-height: 1.4;">{title_text}</div>
                                            </div>'''

    return new_content

updated_html = re.sub(pattern, add_voyage_field, html, flags=re.DOTALL)

# Count how many were updated
count = len(re.findall(r'<div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: \'Inter\', sans-serif;">Voyage</div>', updated_html))

with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print(f"✅ Added 'Voyage' field to {count} info boxes!")
print(f"✅ Full titles now visible in info box below truncated heading")
