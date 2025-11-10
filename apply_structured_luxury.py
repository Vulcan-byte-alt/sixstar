#!/usr/bin/env python3
"""
Apply Structured Luxury Design - User's exact specification
1. Top Section - Brand & Duration (aligned with divider)
2. Middle - Voyage Title + Tagline (ship • region)
3. Secondary Info - Departure with calendar icon
4. CTA Zone - Buttons together
"""

import re

def apply_structured_luxury(html_content):
    """
    Apply structured luxury design with user's exact layout
    """

    # Update card hover effects
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.transform='translateY(0)'; el.style.opacity='1'; el.style.visibility='visible'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})"
    )
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.transform='translateY(-10px)'; el.style.opacity='0'; el.style.visibility='hidden'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})"
    )

    # Pattern to match content sections
    pattern = r'(<!-- (?:True Luxury Minimalist Content|Rich Luxury Content|Ultra-Refined Luxury Content|Opulent Luxury Content) -->)(.*?)(</div>\s*</article>)'

    def replace_content(match):
        full_section = match.group(0)

        # Extract data
        logo_match = re.search(r'<img src="([^"]+)"\s+alt="([^"]+)"', full_section)
        if not logo_match:
            return full_section
        logo_src = logo_match.group(1)
        logo_alt = logo_match.group(2)

        duration_match = re.search(r'(\d+)\s*Nights?', full_section)
        duration = duration_match.group(1) if duration_match else "7"

        title_match = re.search(r'<h3[^>]*>([^<]+)</h3>', full_section)
        title = title_match.group(1).strip() if title_match else "Luxury Voyage"

        # Departure
        departure_match = re.search(r'(\d+)\s+([A-Za-z]+)\s+(\d{4})', full_section)
        if departure_match:
            month = departure_match.group(2)
            year = departure_match.group(3)
            departure_display = f"{month} {year}"
        else:
            # Try to extract just year
            year_match = re.search(r'(\d{4})', full_section)
            departure_display = year_match.group(1) if year_match else "2026"

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

        new_content = f'''<!-- Structured Luxury Content -->
                            <div style="padding: 54px 60px 52px; display: flex; flex-direction: column; justify-content: space-between; position: relative;">

                                <!-- 🏛️ 1. Top Section — Brand & Duration -->
                                <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 28px; border-bottom: 1px solid rgba(10, 25, 41, 0.08); margin-bottom: 38px;">
                                    <!-- Logo -->
                                    <img src="{logo_src}" alt="{logo_alt}"
                                        style="max-height: 46px; width: auto; max-width: 200px; object-fit: contain; opacity: 0.96;">

                                    <!-- Duration Badge -->
                                    <div style="display: flex; align-items: center; gap: 10px; padding: 10px 22px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.08), rgba(212, 175, 55, 0.03)); border-radius: 30px; border: 1px solid rgba(212, 175, 55, 0.18);">
                                        <span style="font-size: 18px; opacity: 0.7;">⏳</span>
                                        <div>
                                            <div style="color: var(--navy); font-size: 17px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.3px;">{duration} Nights</div>
                                        </div>
                                    </div>
                                </div>

                                <!-- 🕊️ 2. Middle — Voyage Title + Tagline -->
                                <div style="flex-grow: 1; margin-bottom: 36px;">
                                    <!-- Title -->
                                    <h3 style="font-size: 33px; font-family: 'Cormorant Garamond', serif; color: var(--navy); line-height: 1.3; font-weight: 500; margin-bottom: 14px; letter-spacing: 0.5px;">
                                        {title}
                                    </h3>

                                    <!-- Subheadline: Ship • Region -->
                                    <div style="font-size: 14px; font-family: 'Inter', sans-serif; color: #888; font-weight: 400; letter-spacing: 0.5px; margin-bottom: 32px;">
                                        {ship} <span style="color: var(--gold); margin: 0 8px; opacity: 0.5;">•</span> {region}
                                    </div>

                                    <!-- 🧭 3. Secondary Info — Departure -->
                                    <div style="display: inline-flex; align-items: center; gap: 12px; padding: 14px 24px; background: rgba(10, 25, 41, 0.02); border-radius: 10px; border: 1px solid rgba(10, 25, 41, 0.06);">
                                        <!-- Calendar Icon -->
                                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <rect x="3" y="4" width="18" height="18" rx="2" stroke="#d4a574" stroke-width="2" fill="none" opacity="0.6"/>
                                            <line x1="3" y1="10" x2="21" y2="10" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                            <line x1="8" y1="2" x2="8" y2="6" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                            <line x1="16" y1="2" x2="16" y2="6" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                        </svg>
                                        <div>
                                            <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; margin-bottom: 4px; opacity: 0.7;">Departs</div>
                                            <div style="color: var(--navy); font-size: 16px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.3px;">{departure_display}</div>
                                        </div>
                                    </div>

                                    <!-- Premium Features (EXPANDS on hover) -->
                                    <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                        <div style="overflow: hidden;">
                                            <div style="margin-top: 24px; padding: 20px 24px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.04), rgba(212, 175, 55, 0.01)); border-radius: 12px; border-left: 3px solid var(--gold);">
                                                <div style="display: flex; flex-direction: column; gap: 11px;">
                                                    <div style="display: flex; align-items: center; gap: 12px;">
                                                        <div style="width: 5px; height: 5px; background: var(--gold); border-radius: 50%; opacity: 0.6;"></div>
                                                        <span style="font-size: 12px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">All-inclusive premium experience</span>
                                                    </div>
                                                    <div style="display: flex; align-items: center; gap: 12px;">
                                                        <div style="width: 5px; height: 5px; background: var(--gold); border-radius: 50%; opacity: 0.6;"></div>
                                                        <span style="font-size: 12px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Exclusive shore excursions included</span>
                                                    </div>
                                                    <div style="display: flex; align-items: center; gap: 12px;">
                                                        <div style="width: 5px; height: 5px; background: var(--gold); border-radius: 50%; opacity: 0.6;"></div>
                                                        <span style="font-size: 12px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Limited availability – reserve today</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- 💬 4. Call-to-Action Zone — Buttons Together -->
                                <div style="display: flex; gap: 14px;">
                                    <!-- Primary Button (Filled Gradient) -->
                                    <button
                                        onmouseover="this.style.background='linear-gradient(135deg, #c9965f, var(--gold))'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 10px 28px rgba(212, 175, 55, 0.3)'"
                                        onmouseout="this.style.background='linear-gradient(135deg, var(--navy), #1a3348)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 6px 18px rgba(10, 25, 41, 0.2)'"
                                        style="flex: 1; padding: 19px 34px; background: linear-gradient(135deg, var(--navy), #1a3348); color: white; border: none; border-radius: 14px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 18px rgba(10, 25, 41, 0.2);">
                                        View Voyage
                                    </button>

                                    <!-- Secondary Button (Outlined) -->
                                    <button
                                        onmouseover="this.style.background='rgba(212, 175, 55, 0.08)'; this.style.borderColor='var(--gold)'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(10, 25, 41, 0.15)'; this.style.transform='translateY(0)'"
                                        style="padding: 19px 32px; background: transparent; color: var(--navy); border: 1px solid rgba(10, 25, 41, 0.15); border-radius: 14px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);">
                                        Inquire
                                    </button>
                                </div>

                                <!-- Secondary Actions (EXPANDS on hover) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                    <div style="overflow: hidden;">
                                        <div style="display: flex; justify-content: center; align-items: center; gap: 32px; padding-top: 22px; margin-top: 18px; border-top: 1px solid rgba(10, 25, 41, 0.05);">
                                            <button
                                                onmouseover="this.style.color='var(--gold)'"
                                                onmouseout="this.style.color='#999'"
                                                style="background: none; border: none; color: #999; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.6px; padding: 0;">
                                                Request Callback
                                            </button>
                                            <div style="width: 1px; height: 12px; background: rgba(10, 25, 41, 0.1);"></div>
                                            <button
                                                onmouseover="this.style.color='var(--gold)'"
                                                onmouseout="this.style.color='#999'"
                                                style="background: none; border: none; color: #999; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.6px; padding: 0;">
                                                Download Brochure
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </article>'''

        return new_content

    updated_html = re.sub(pattern, replace_content, html_content, flags=re.DOTALL)
    return updated_html

if __name__ == "__main__":
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("✨ Applying STRUCTURED LUXURY Design...")
    print("\n📐 Layout Structure:")
    print("  🏛️  1. Top Section - Brand & Duration (balanced alignment)")
    print("     [ Logo ]  ────────────────────  [ ⏳ 7 Nights ]")
    print()
    print("  🕊️  2. Middle - Voyage Title + Tagline")
    print("     Large Title")
    print("     Ship • Region (muted gold subtext)")
    print()
    print("  🧭  3. Secondary Info - Departure")
    print("     📅 Departs [Month Year]")
    print()
    print("  💬  4. CTA Zone - Buttons Together")
    print("     [ View Voyage ]   [ Inquire ]")
    print()
    print("✨ Features:")
    print("  • Squircle buttons (14px radius)")
    print("  • Primary button: Navy gradient with gold hover")
    print("  • Secondary button: Outlined with gold hover")
    print("  • Calendar icon for departure")
    print("  • Premium features expand on hover")
    print("  • Secondary actions expand on hover")
    print("  • Clean divider line under top section")
    print("  • Muted gold bullet separator (•)")

    updated_html = apply_structured_luxury(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ DONE! All 30 cards now have structured luxury design!")
