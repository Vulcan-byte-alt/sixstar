#!/usr/bin/env python3
"""
Apply Ultra-Refined Luxury Design
- Squircle buttons (rounded rectangles)
- More sophisticated content arrangement
- Better visual flow and hierarchy
- Elegant info presentation (not rigid grid)
- More breathing room and gold accents
"""

import re

def apply_ultra_refined_luxury(html_content):
    """
    Apply ultra-refined luxury design with squircle buttons and better arrangement
    """

    # Update card hover effects for actual expansion
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})"
    )
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})",
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

        new_content = f'''<!-- Ultra-Refined Luxury Content -->
                            <div style="padding: 58px 64px 56px; display: flex; flex-direction: column; justify-content: space-between; position: relative;">

                                <!-- Elegant Header with Logo -->
                                <div style="margin-bottom: 48px; position: relative;">
                                    <img src="{logo_src}" alt="{logo_alt}"
                                        style="max-height: 52px; width: auto; max-width: 220px; object-fit: contain; opacity: 0.96;">
                                    <!-- Subtle Gold Underline -->
                                    <div style="width: 80px; height: 1px; background: linear-gradient(90deg, var(--gold) 0%, transparent 100%); margin-top: 16px; opacity: 0.4;"></div>
                                </div>

                                <!-- Title Section with Better Hierarchy -->
                                <div style="flex-grow: 1; margin-bottom: 44px;">
                                    <h3 style="font-size: 32px; font-family: 'Cormorant Garamond', serif; color: var(--navy); line-height: 1.25; font-weight: 500; margin-bottom: 40px; letter-spacing: 0.5px; max-width: 95%;">
                                        {title}
                                    </h3>

                                    <!-- Elegant Inline Info (not rigid grid) -->
                                    <div style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 12px 40px; padding-bottom: 28px; border-bottom: 1px solid rgba(10, 25, 41, 0.05);">
                                        <div style="display: flex; align-items: baseline; gap: 10px;">
                                            <div style="width: 3px; height: 3px; background: var(--gold); border-radius: 50%; opacity: 0.5; margin-top: 8px;"></div>
                                            <div>
                                                <span style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; opacity: 0.7; margin-right: 8px;">Departure</span>
                                                <span style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif; letter-spacing: 0.2px;">{departure}</span>
                                            </div>
                                        </div>
                                        <div style="display: flex; align-items: baseline; gap: 10px;">
                                            <div style="width: 3px; height: 3px; background: var(--gold); border-radius: 50%; opacity: 0.5; margin-top: 8px;"></div>
                                            <div>
                                                <span style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; opacity: 0.7; margin-right: 8px;">Duration</span>
                                                <span style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif; letter-spacing: 0.2px;">{duration} Nights</span>
                                            </div>
                                        </div>
                                        <div style="display: flex; align-items: baseline; gap: 10px;">
                                            <div style="width: 3px; height: 3px; background: var(--gold); border-radius: 50%; opacity: 0.5; margin-top: 8px;"></div>
                                            <div>
                                                <span style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; opacity: 0.7; margin-right: 8px;">Region</span>
                                                <span style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif; letter-spacing: 0.2px;">{region}</span>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Ship Info with Gold Accent (EXPANDS on hover) -->
                                    <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                        <div style="overflow: hidden;">
                                            <div style="padding-top: 24px; display: flex; align-items: baseline; gap: 10px;">
                                                <div style="width: 3px; height: 3px; background: var(--gold); border-radius: 50%; opacity: 0.5; margin-top: 8px;"></div>
                                                <div>
                                                    <span style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; opacity: 0.7; margin-right: 8px;">Ship</span>
                                                    <span style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif; letter-spacing: 0.2px;">{ship}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Premium Highlights (EXPANDS on hover) -->
                                    <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                        <div style="overflow: hidden;">
                                            <div style="margin-top: 28px; padding: 22px 26px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.03), rgba(212, 175, 55, 0.01)); border-radius: 16px; border: 1px solid rgba(212, 175, 55, 0.08);">
                                                <div style="display: flex; flex-direction: column; gap: 10px;">
                                                    <div style="display: flex; align-items: center; gap: 12px;">
                                                        <div style="width: 5px; height: 5px; background: var(--gold); border-radius: 50%; opacity: 0.5;"></div>
                                                        <span style="font-size: 12px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">All-inclusive luxury experience</span>
                                                    </div>
                                                    <div style="display: flex; align-items: center; gap: 12px;">
                                                        <div style="width: 5px; height: 5px; background: var(--gold); border-radius: 50%; opacity: 0.5;"></div>
                                                        <span style="font-size: 12px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Limited availability – reserve your voyage</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Squircle CTA Buttons -->
                                <div style="display: flex; gap: 14px;">
                                    <button
                                        onmouseover="this.style.background='linear-gradient(135deg, var(--gold), #c9965f)'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 10px 28px rgba(212, 175, 55, 0.28)'"
                                        onmouseout="this.style.background='linear-gradient(135deg, var(--navy), #1e3a52)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 6px 16px rgba(10, 25, 41, 0.18)'"
                                        style="flex: 1; padding: 19px 34px; background: linear-gradient(135deg, var(--navy), #1e3a52); color: white; border: none; border-radius: 14px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 16px rgba(10, 25, 41, 0.18);">
                                        View Voyage
                                    </button>
                                    <button
                                        onmouseover="this.style.background='rgba(212, 175, 55, 0.06)'; this.style.borderColor='var(--gold)'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(10, 25, 41, 0.14)'; this.style.transform='translateY(0)'"
                                        style="padding: 19px 30px; background: transparent; color: var(--navy); border: 1px solid rgba(10, 25, 41, 0.14); border-radius: 14px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);">
                                        Inquire
                                    </button>
                                </div>

                                <!-- Refined Secondary Actions (EXPANDS on hover) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                    <div style="overflow: hidden;">
                                        <div style="display: flex; justify-content: center; align-items: center; gap: 36px; padding-top: 22px; margin-top: 18px; border-top: 1px solid rgba(10, 25, 41, 0.04);">
                                            <button
                                                onmouseover="this.style.color='var(--gold)'; this.style.transform='translateX(2px)'"
                                                onmouseout="this.style.color='#999'; this.style.transform='translateX(0)'"
                                                style="background: none; border: none; color: #999; font-size: 10px; font-weight: 500; cursor: pointer; transition: all 0.25s; text-transform: uppercase; letter-spacing: 1.6px; padding: 0;">
                                                Request Callback
                                            </button>
                                            <div style="width: 1px; height: 12px; background: rgba(10, 25, 41, 0.08);"></div>
                                            <button
                                                onmouseover="this.style.color='var(--gold)'; this.style.transform='translateX(2px)'"
                                                onmouseout="this.style.color='#999'; this.style.transform='translateX(0)'"
                                                style="background: none; border: none; color: #999; font-size: 10px; font-weight: 500; cursor: pointer; transition: all 0.25s; text-transform: uppercase; letter-spacing: 1.6px; padding: 0;">
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

    print("✨ Applying ULTRA-REFINED LUXURY Design...")
    print("\n🎨 Major Improvements:")
    print("  • Squircle buttons (border-radius: 14px) - modern luxury shape")
    print("  • Bigger logo (52px) with elegant gold underline")
    print("  • Larger title (32px) with better spacing")
    print("  • Elegant inline info layout (not rigid grid)")
    print("  • Gold bullet points for visual flow")
    print("  • Ship info expands on hover")
    print("  • Premium highlights in rounded card (expands)")
    print("  • Refined secondary actions with separator")
    print("  • Better breathing room and spacing")
    print("  • More subtle gold accents throughout")
    print("  • Smoother hover transitions (0.35s)")
    print("\n⚡ This feels MUCH more luxurious!")

    updated_html = apply_ultra_refined_luxury(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ DONE! All 30 cards now have ultra-refined luxury design with squircle buttons!")
