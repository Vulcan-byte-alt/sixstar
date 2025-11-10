#!/usr/bin/env python3
"""
Apply Expanding Luxury Design - Cards that ACTUALLY expand on hover
Uses CSS Grid for smooth height expansion without lag
"""

import re

def apply_expanding_luxury(html_content):
    """
    Apply rich luxury design with TRUE card expansion on hover
    """

    # Update card hover effects for actual expansion
    # Change the hover handlers to add a class that triggers grid expansion
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.transform='translateY(0)'; el.style.opacity='1'; el.style.visibility='visible'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})"
    )
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.transform='translateY(-10px)'; el.style.opacity='0'; el.style.visibility='hidden'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})"
    )

    # Pattern to match content sections
    pattern = r'(<!-- (?:True Luxury Minimalist Content|Rich Luxury Content) -->)(.*?)(</div>\s*</article>)'

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

        new_content = f'''<!-- Rich Luxury Content -->
                            <div style="padding: 56px 60px; display: flex; flex-direction: column; justify-content: space-between; position: relative;">

                                <!-- Luxury Header -->
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 44px;">
                                    <img src="{logo_src}" alt="{logo_alt}"
                                        style="max-height: 48px; width: auto; max-width: 200px; object-fit: contain; opacity: 0.98;">
                                    <!-- Elegant Duration Badge -->
                                    <div style="text-align: right; padding: 12px 24px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.08), rgba(212, 175, 55, 0.03)); border-radius: 30px; border: 1px solid rgba(212, 175, 55, 0.15);">
                                        <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 4px; opacity: 0.7;">Duration</div>
                                        <div style="color: var(--navy); font-size: 18px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{duration} Nights</div>
                                    </div>
                                </div>

                                <!-- Title & Info Section -->
                                <div style="flex-grow: 1; margin-bottom: 40px;">
                                    <!-- Gold Accent Bar -->
                                    <div style="width: 60px; height: 1px; background: linear-gradient(90deg, var(--gold), transparent); margin-bottom: 24px; opacity: 0.5;"></div>

                                    <h3 style="font-size: 30px; font-family: 'Cormorant Garamond', serif; color: var(--navy); line-height: 1.35; font-weight: 500; margin-bottom: 32px; letter-spacing: 0.3px;">
                                        {title}
                                    </h3>

                                    <!-- Elegant Info Grid -->
                                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; padding: 24px 0; border-top: 1px solid rgba(10, 25, 41, 0.06); border-bottom: 1px solid rgba(10, 25, 41, 0.06);">
                                        <div>
                                            <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; opacity: 0.6;">Departure</div>
                                            <div style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif;">{departure}</div>
                                        </div>
                                        <div>
                                            <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; opacity: 0.6;">Ship</div>
                                            <div style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif;">{ship}</div>
                                        </div>
                                        <div>
                                            <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; opacity: 0.6;">Region</div>
                                            <div style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif;">{region}</div>
                                        </div>
                                    </div>

                                    <!-- Premium Details (EXPANDS on hover) -->
                                    <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1); margin-top: 20px;">
                                        <div style="overflow: hidden;">
                                            <div style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.04), transparent); padding: 20px 24px; border-radius: 12px; border-left: 2px solid var(--gold); margin-top: 4px;">
                                                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                                                    <div style="width: 4px; height: 4px; background: var(--gold); border-radius: 50%; opacity: 0.6;"></div>
                                                    <span style="font-size: 11px; color: #666; font-weight: 500; letter-spacing: 0.5px;">All-inclusive luxury experience</span>
                                                </div>
                                                <div style="display: flex; align-items: center; gap: 12px;">
                                                    <div style="width: 4px; height: 4px; background: var(--gold); border-radius: 50%; opacity: 0.6;"></div>
                                                    <span style="font-size: 11px; color: #666; font-weight: 500; letter-spacing: 0.5px;">Limited availability – book soon</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Luxury CTA Section -->
                                <div style="display: flex; gap: 12px;">
                                    <button
                                        onmouseover="this.style.background='linear-gradient(135deg, var(--gold), #c9965f)'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(212, 175, 55, 0.25)'"
                                        onmouseout="this.style.background='linear-gradient(135deg, var(--navy), #1e3a52)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 12px rgba(10, 25, 41, 0.15)'"
                                        style="flex: 1; padding: 18px 32px; background: linear-gradient(135deg, var(--navy), #1e3a52); color: white; border: none; border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; cursor: pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 4px 12px rgba(10, 25, 41, 0.15);">
                                        View Voyage
                                    </button>
                                    <button
                                        onmouseover="this.style.background='rgba(212, 175, 55, 0.08)'; this.style.borderColor='var(--gold)'"
                                        onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(10, 25, 41, 0.12)'"
                                        style="padding: 18px 28px; background: transparent; color: var(--navy); border: 1px solid rgba(10, 25, 41, 0.12); border-radius: 4px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; cursor: pointer; transition: all 0.3s;">
                                        Inquire
                                    </button>
                                </div>

                                <!-- Secondary Actions (EXPANDS on hover) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                    <div style="overflow: hidden;">
                                        <div style="display: flex; justify-content: center; gap: 32px; padding-top: 20px; margin-top: 16px; border-top: 1px solid rgba(10, 25, 41, 0.04);">
                                            <button
                                                onmouseover="this.style.color='var(--gold)'"
                                                onmouseout="this.style.color='#999'"
                                                style="background: none; border: none; color: #999; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0;">
                                                Request Callback
                                            </button>
                                            <button
                                                onmouseover="this.style.color='var(--gold)'"
                                                onmouseout="this.style.color='#999'"
                                                style="background: none; border: none; color: #999; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0;">
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

    print("🎨 Applying EXPANDING LUXURY Design...")
    print("✨ Features:")
    print("  • TRUE card height expansion (CSS Grid technique)")
    print("  • Smooth 0.4s animation using grid-template-rows")
    print("  • Gold gradient duration badge")
    print("  • Gold accent bar before title")
    print("  • 3-column info grid (always visible)")
    print("  • Premium details box EXPANDS on hover")
    print("  • Navy gradient primary button")
    print("  • Outlined inquire button")
    print("  • Secondary actions EXPAND on hover")
    print("\n⚡ The card will actually grow in height now!")

    updated_html = apply_expanding_luxury(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ DONE! Cards now EXPAND smoothly on hover with true height animation!")
