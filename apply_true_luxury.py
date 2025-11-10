#!/usr/bin/env python3
"""
Apply True Luxury Minimalist Design to All Deal Cards
- Bigger logos (48px)
- Much less information by default
- Lighter font weights
- More breathing room
- Cleaner, simpler CTA
"""

import re

def apply_true_luxury(html_content):
    """
    Replace all card content sections with true luxury minimalist design
    """

    # Pattern to match the content section (both old styles)
    pattern = r'(<!-- (?:Ultra-Luxury Interactive Content Section|True Luxury Minimalist Content) -->)(.*?)(</div>\s*</article>)'

    def replace_content(match):
        full_section = match.group(0)

        # Extract data
        logo_match = re.search(r'<img src="([^"]+)"\s+alt="([^"]+)"', full_section)
        if not logo_match:
            return full_section
        logo_src = logo_match.group(1)
        logo_alt = logo_match.group(2)

        # Duration
        duration_match = re.search(r'(\d+)\s*Nights?', full_section)
        duration = duration_match.group(1) if duration_match else "7"

        # Title
        title_match = re.search(r'<h3[^>]*>([^<]+)</h3>', full_section)
        title = title_match.group(1).strip() if title_match else "Luxury Voyage"

        # Departure - extract just month and year
        departure_match = re.search(r'(\d+)\s+([A-Za-z]+)\s+(\d{4})', full_section)
        if departure_match:
            month = departure_match.group(2)
            year = departure_match.group(3)
            departure = f"{month} {year}"
        else:
            departure = "2026"

        # Ship
        ship_match = re.search(r'<div[^>]*>Ship</div>\s*<div[^>]*>([^<]+)</div>', full_section)
        if not ship_match:
            ship_match = re.search(r'>Ship<[^>]*>([^<]+)<', full_section)
        ship = ship_match.group(1).strip() if ship_match else "TBA"

        # Region
        region_match = re.search(r'<div[^>]*>Region</div>\s*<div[^>]*>([^<]+)</div>', full_section)
        if not region_match:
            region_match = re.search(r'>Region<[^>]*>([^<]+)<', full_section)
        region = region_match.group(1).strip() if region_match else "TBA"

        # Build new content
        new_content = f'''<!-- True Luxury Minimalist Content -->
                            <div style="padding: 60px 64px; display: flex; flex-direction: column; justify-content: space-between;">

                                <!-- Luxury Logo -->
                                <div style="margin-bottom: 50px;">
                                    <img src="{logo_src}" alt="{logo_alt}"
                                        style="max-height: 48px; width: auto; max-width: 220px; object-fit: contain; opacity: 1;">
                                </div>

                                <!-- Title Section -->
                                <div style="flex-grow: 1; margin-bottom: 48px;">
                                    <h3 style="font-size: 32px; font-family: 'Cormorant Garamond', serif; color: var(--navy); line-height: 1.3; font-weight: 400; margin-bottom: 36px; letter-spacing: 0.5px;">
                                        {title}
                                    </h3>

                                    <!-- Minimal Essential Info Only -->
                                    <div style="display: flex; gap: 48px; padding-bottom: 32px; border-bottom: 1px solid rgba(10, 25, 41, 0.08);">
                                        <div>
                                            <div style="color: #999; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">Departure</div>
                                            <div style="color: var(--navy); font-size: 16px; font-weight: 300; font-family: 'Inter', sans-serif; letter-spacing: 0.3px;">{departure}</div>
                                        </div>
                                        <div>
                                            <div style="color: #999; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">Duration</div>
                                            <div style="color: var(--navy); font-size: 16px; font-weight: 300; font-family: 'Inter', sans-serif; letter-spacing: 0.3px;">{duration} Nights</div>
                                        </div>
                                    </div>

                                    <!-- Hidden Details on Hover -->
                                    <div class="expand-on-hover" style="margin-top: 0; max-height: 0; opacity: 0; overflow: hidden; transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);">
                                        <div style="display: flex; gap: 48px; padding: 28px 0;">
                                            <div>
                                                <div style="color: #999; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">Ship</div>
                                                <div style="color: var(--navy); font-size: 16px; font-weight: 300; font-family: 'Inter', sans-serif; letter-spacing: 0.3px;">{ship}</div>
                                            </div>
                                            <div>
                                                <div style="color: #999; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px;">Region</div>
                                                <div style="color: var(--navy); font-size: 16px; font-weight: 300; font-family: 'Inter', sans-serif; letter-spacing: 0.3px;">{region}</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Refined Single CTA -->
                                <button
                                    onmouseover="this.style.background='var(--navy)'; this.style.color='white'; this.style.transform='translateY(-2px)'"
                                    onmouseout="this.style.background='transparent'; this.style.color='var(--navy)'; this.style.transform='translateY(0)'"
                                    style="width: 100%; padding: 20px; background: transparent; color: var(--navy); border: 1px solid rgba(10, 25, 41, 0.15); border-radius: 2px; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 3px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                    View Details
                                </button>

                                <!-- Minimal Secondary Actions on Hover -->
                                <div class="expand-on-hover" style="display: flex; justify-content: center; gap: 32px; margin-top: 0; max-height: 0; opacity: 0; overflow: hidden; transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); padding-top: 24px;">
                                    <button
                                        onmouseover="this.style.color='var(--gold)'"
                                        onmouseout="this.style.color='#999'"
                                        style="background: none; border: none; color: #999; font-size: 10px; font-weight: 400; cursor: pointer; transition: color 0.3s; text-transform: uppercase; letter-spacing: 2px; padding: 0;">
                                        Inquire
                                    </button>
                                    <button
                                        onmouseover="this.style.color='var(--gold)'"
                                        onmouseout="this.style.color='#999'"
                                        style="background: none; border: none; color: #999; font-size: 10px; font-weight: 400; cursor: pointer; transition: color 0.3s; text-transform: uppercase; letter-spacing: 2px; padding: 0;">
                                        Save
                                    </button>
                                </div>
                            </div>
                        </article>'''

        return new_content

    # Apply the replacement
    updated_html = re.sub(pattern, replace_content, html_content, flags=re.DOTALL)

    return updated_html

if __name__ == "__main__":
    # Read the deals.html file
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("Applying TRUE luxury minimalist design...")
    print(f"Original file size: {len(html_content)} characters")

    # Apply redesign
    updated_html = apply_true_luxury(html_content)

    print(f"Updated file size: {len(updated_html)} characters")

    # Save the updated file
    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✨ TRUE LUXURY DESIGN COMPLETE!")
    print("\n🎨 What Changed:")
    print("  ✓ Logos increased: 34px → 48px (40% larger)")
    print("  ✓ Padding increased: 48px 56px → 60px 64px")
    print("  ✓ Font weights lighter: 500 → 400 (titles), 500 → 300 (info)")
    print("  ✓ Title size: 26px → 32px (more presence)")
    print("  ✓ Letter spacing increased throughout")
    print("  ✓ Minimal info by default (Departure + Duration only)")
    print("  ✓ Ship + Region reveal on hover")
    print("  ✓ Single clean CTA button")
    print("  ✓ Secondary actions hidden until hover")
    print("  ✓ No icons/progress bars cluttering the view")
    print("  ✓ Much more breathing room")
    print("\n💎 This is TRUE luxury minimalism!")
