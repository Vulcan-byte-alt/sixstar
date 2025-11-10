#!/usr/bin/env python3
"""
Apply hover expansion effects and fix logo aspect ratios for all deal cards
"""

import re

def apply_hover_expansion(html_content):
    """
    1. Fix logo aspect ratios
    2. Add expand-on-hover class to booking progress and secondary actions
    3. Update card hover events for smooth expansion
    """

    # Fix 1: Update all card article tags to have expansion hover effects
    card_pattern = r'(<article data-deal-id="[^"]*"\s+style="[^"]*)(transition: all 0\.4s;)([^"]*"[^>]*)(onmouseover="[^"]*"[^>]*)(onmouseout="[^"]*")'

    def update_card_hover(match):
        style_part1 = match.group(1)
        style_part2 = match.group(3)
        rest = match.group(4) + match.group(5)

        # Replace transition and add new hover events
        new_style = style_part1 + "transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);" + style_part2
        new_hover = '''onmouseover="this.style.transform='translateY(-8px) scale(1.01)'; this.style.boxShadow='0 24px 64px rgba(0,0,0,0.15)'; this.style.borderColor='rgba(212, 175, 55, 0.3)'; this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.maxHeight=el.scrollHeight+'px'; el.style.opacity='1'; el.style.marginTop='24px'});"
                       onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 8px 32px rgba(0,0,0,0.08)'; this.style.borderColor='rgba(255,255,255,0.8)'; this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.maxHeight='0'; el.style.opacity='0'; el.style.marginTop='0'})"'''

        return new_style + new_hover

    html_content = re.sub(card_pattern, update_card_hover, html_content)

    # Fix 2: Fix all logo styling to prevent squashing
    logo_pattern = r'(<img src="[^"]*"\s+alt="[^"]*"\s+style=")height: 34px; width: auto; opacity: 0\.95;'
    html_content = re.sub(logo_pattern, r'\1max-height: 34px; width: auto; max-width: 180px; object-fit: contain; opacity: 0.95;', html_content)

    # Fix 3: Add expand-on-hover class to booking progress sections
    booking_progress_pattern = r'(<!-- Booking Progress Indicator -->\s*<div style="margin-top: 24px;)'
    html_content = re.sub(booking_progress_pattern, r'<!-- Booking Progress Indicator -->\n                                    <div class="expand-on-hover" style="margin-top: 0; max-height: 0; opacity: 0; overflow: hidden; transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);', html_content)

    # Fix 4: Add expand-on-hover class to secondary actions
    secondary_actions_pattern = r'(<!-- Secondary Actions Row -->\s*<div style="display: flex;)'
    html_content = re.sub(secondary_actions_pattern, r'<!-- Secondary Actions Row -->\n                                <div class="expand-on-hover" style="display: flex; margin-top: 0; max-height: 0; opacity: 0; overflow: hidden; transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);', html_content)

    return html_content

if __name__ == "__main__":
    # Read the deals.html file
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("Applying hover expansion effects and logo fixes...")
    print(f"Original file size: {len(html_content)} characters")

    # Apply changes
    updated_html = apply_hover_expansion(html_content)

    print(f"Updated file size: {len(updated_html)} characters")

    # Save the updated file
    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("✨ Hover expansion effects applied!")
    print("✓ Logos fixed (no more squashing)")
    print("✓ Booking progress bars hidden by default, reveal on hover")
    print("✓ Secondary actions hidden by default, reveal on hover")
    print("✓ Cards smoothly expand and lift on hover")
    print("✓ Gold border accent on hover")
