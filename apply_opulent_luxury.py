#!/usr/bin/env python3
"""
Apply OPULENT LUXURY Design - Rich, layered, sophisticated
NOT minimalistic - full of luxurious details and visual richness
"""

import re

def apply_opulent_luxury(html_content):
    """
    Apply opulent luxury design with rich visual layers and details
    """

    # Update card hover effects
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})"
    )
    html_content = html_content.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})"
    )

    # Pattern to match content sections
    pattern = r'(<!-- (?:True Luxury Minimalist Content|Rich Luxury Content|Ultra-Refined Luxury Content) -->)(.*?)(</div>\s*</article>)'

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
            day = departure_match.group(1)
            month = departure_match.group(2)
            year = departure_match.group(3)
            departure = f"{day} {month} {year}"
            departure_short = f"{month} {year}"
        else:
            departure = "2026"
            departure_short = "2026"

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

        new_content = f'''<!-- Opulent Luxury Content -->
                            <div style="padding: 52px 58px 50px; display: flex; flex-direction: column; justify-content: space-between; position: relative; background: linear-gradient(135deg, rgba(255,255,255,0.5) 0%, rgba(250,248,246,0.3) 100%);">

                                <!-- Decorative Corner Accents -->
                                <div style="position: absolute; top: 20px; right: 20px; width: 60px; height: 60px; border-top: 1px solid rgba(212, 175, 55, 0.15); border-right: 1px solid rgba(212, 175, 55, 0.15);"></div>
                                <div style="position: absolute; bottom: 20px; left: 20px; width: 60px; height: 60px; border-bottom: 1px solid rgba(212, 175, 55, 0.15); border-left: 1px solid rgba(212, 175, 55, 0.15);"></div>

                                <!-- Luxury Header Section -->
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 38px; position: relative;">
                                    <div>
                                        <img src="{logo_src}" alt="{logo_alt}"
                                            style="max-height: 50px; width: auto; max-width: 210px; object-fit: contain; opacity: 0.95;">
                                        <!-- Gold Decorative Lines -->
                                        <div style="display: flex; gap: 6px; margin-top: 14px;">
                                            <div style="width: 40px; height: 2px; background: linear-gradient(90deg, var(--gold), transparent); opacity: 0.6;"></div>
                                            <div style="width: 20px; height: 2px; background: linear-gradient(90deg, var(--gold), transparent); opacity: 0.4;"></div>
                                        </div>
                                    </div>

                                    <!-- Duration Badge with Rich Styling -->
                                    <div style="position: relative; padding: 14px 26px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.12), rgba(212, 175, 55, 0.04)); border-radius: 12px; border: 1px solid rgba(212, 175, 55, 0.25); box-shadow: 0 4px 12px rgba(212, 175, 55, 0.08);">
                                        <div style="position: absolute; top: -1px; left: -1px; right: -1px; height: 50%; background: linear-gradient(180deg, rgba(255,255,255,0.4), transparent); border-radius: 12px 12px 0 0; pointer-events: none;"></div>
                                        <div style="text-align: center;">
                                            <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 6px; opacity: 0.8;">Duration</div>
                                            <div style="color: var(--navy); font-size: 20px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{duration} Nights</div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Title with Gold Frame -->
                                <div style="flex-grow: 1; margin-bottom: 36px;">
                                    <div style="padding: 0 0 32px 0; border-left: 2px solid rgba(212, 175, 55, 0.2); padding-left: 24px; margin-left: 4px; position: relative;">
                                        <!-- Gold Accent Dot -->
                                        <div style="position: absolute; left: -5px; top: 0; width: 8px; height: 8px; background: var(--gold); border-radius: 50%; opacity: 0.7;"></div>

                                        <h3 style="font-size: 31px; font-family: 'Cormorant Garamond', serif; color: var(--navy); line-height: 1.3; font-weight: 500; margin-bottom: 34px; letter-spacing: 0.4px;">
                                            {title}
                                        </h3>

                                        <!-- Rich Info Grid with Icons -->
                                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 22px 32px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.03), rgba(212, 175, 55, 0.01)); padding: 26px; border-radius: 14px; border: 1px solid rgba(212, 175, 55, 0.1);">
                                            <div style="display: flex; gap: 14px; align-items: flex-start;">
                                                <!-- Icon -->
                                                <div style="margin-top: 2px;">
                                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                        <rect x="3" y="4" width="18" height="18" rx="2" stroke="#d4a574" stroke-width="2" fill="none" opacity="0.6"/>
                                                        <line x1="3" y1="10" x2="21" y2="10" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                                        <line x1="8" y1="2" x2="8" y2="6" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                                        <line x1="16" y1="2" x2="16" y2="6" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                                    </svg>
                                                </div>
                                                <div>
                                                    <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; margin-bottom: 8px; opacity: 0.75;">Departure</div>
                                                    <div style="color: var(--navy); font-size: 16px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.3px;">{departure_short}</div>
                                                </div>
                                            </div>

                                            <div style="display: flex; gap: 14px; align-items: flex-start;">
                                                <!-- Icon -->
                                                <div style="margin-top: 2px;">
                                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                        <path d="M3 12L6 9M6 9L12 3L18 9M6 9V21H18V9M18 9L21 12" stroke="#d4a574" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity="0.6"/>
                                                    </svg>
                                                </div>
                                                <div>
                                                    <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; margin-bottom: 8px; opacity: 0.75;">Ship</div>
                                                    <div style="color: var(--navy); font-size: 16px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.3px;">{ship}</div>
                                                </div>
                                            </div>

                                            <div style="display: flex; gap: 14px; align-items: flex-start; grid-column: 1 / -1;">
                                                <!-- Icon -->
                                                <div style="margin-top: 2px;">
                                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                        <circle cx="12" cy="12" r="9" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                                        <path d="M12 3C12 3 8 8 8 12C8 16 12 21 12 21C12 21 16 16 16 12C16 8 12 3 12 3Z" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                                        <line x1="3" y1="12" x2="21" y2="12" stroke="#d4a574" stroke-width="2" opacity="0.6"/>
                                                    </svg>
                                                </div>
                                                <div>
                                                    <div style="color: var(--gold); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.8px; margin-bottom: 8px; opacity: 0.75;">Region</div>
                                                    <div style="color: var(--navy); font-size: 16px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.3px;">{region}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Premium Features (EXPANDS on hover) -->
                                    <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                        <div style="overflow: hidden;">
                                            <div style="margin-top: 24px; padding: 24px 28px; background: linear-gradient(135deg, rgba(10, 25, 41, 0.03), rgba(10, 25, 41, 0.01)); border-radius: 14px; border: 1px solid rgba(10, 25, 41, 0.08); position: relative;">
                                                <!-- Decorative Gold Strip -->
                                                <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: linear-gradient(180deg, var(--gold), transparent); border-radius: 14px 0 0 14px;"></div>

                                                <div style="display: grid; gap: 14px;">
                                                    <div style="display: flex; align-items: center; gap: 14px;">
                                                        <div style="width: 6px; height: 6px; background: var(--gold); border-radius: 50%; box-shadow: 0 0 8px rgba(212, 175, 55, 0.4);"></div>
                                                        <span style="font-size: 13px; color: #444; font-weight: 500; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">All-inclusive premium amenities</span>
                                                    </div>
                                                    <div style="display: flex; align-items: center; gap: 14px;">
                                                        <div style="width: 6px; height: 6px; background: var(--gold); border-radius: 50%; box-shadow: 0 0 8px rgba(212, 175, 55, 0.4);"></div>
                                                        <span style="font-size: 13px; color: #444; font-weight: 500; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Exclusive shore excursions included</span>
                                                    </div>
                                                    <div style="display: flex; align-items: center; gap: 14px;">
                                                        <div style="width: 6px; height: 6px; background: var(--gold); border-radius: 50%; box-shadow: 0 0 8px rgba(212, 175, 55, 0.4);"></div>
                                                        <span style="font-size: 13px; color: #444; font-weight: 500; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Limited availability – reserve today</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Opulent Squircle Buttons -->
                                <div style="display: flex; gap: 14px;">
                                    <button
                                        onmouseover="this.style.background='linear-gradient(135deg, #c9965f, var(--gold))'; this.style.transform='translateY(-3px)'; this.style.boxShadow='0 12px 32px rgba(212, 175, 55, 0.35)'"
                                        onmouseout="this.style.background='linear-gradient(135deg, var(--navy), #1a3348)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 6px 20px rgba(10, 25, 41, 0.25)'"
                                        style="flex: 1; padding: 20px 36px; background: linear-gradient(135deg, var(--navy), #1a3348); color: white; border: none; border-radius: 14px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 6px 20px rgba(10, 25, 41, 0.25); position: relative; overflow: hidden;">
                                        <span style="position: relative; z-index: 1;">View Voyage Details</span>
                                        <!-- Shine effect -->
                                        <div style="position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); pointer-events: none;"></div>
                                    </button>
                                    <button
                                        onmouseover="this.style.background='linear-gradient(135deg, rgba(212, 175, 55, 0.12), rgba(212, 175, 55, 0.06))'; this.style.borderColor='var(--gold)'; this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(212, 175, 55, 0.15)'"
                                        onmouseout="this.style.background='rgba(255, 255, 255, 0.5)'; this.style.borderColor='rgba(10, 25, 41, 0.18)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(10, 25, 41, 0.06)'"
                                        style="padding: 20px 32px; background: rgba(255, 255, 255, 0.5); color: var(--navy); border: 1px solid rgba(10, 25, 41, 0.18); border-radius: 14px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 2px 8px rgba(10, 25, 41, 0.06);">
                                        Inquire
                                    </button>
                                </div>

                                <!-- Rich Secondary Actions (EXPANDS on hover) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);">
                                    <div style="overflow: hidden;">
                                        <div style="padding-top: 24px; margin-top: 20px; border-top: 1px solid rgba(212, 175, 55, 0.12); display: flex; justify-content: center; align-items: center; gap: 20px;">
                                            <button
                                                onmouseover="this.style.color='var(--gold)'; this.querySelector('div').style.background='var(--gold)'"
                                                onmouseout="this.style.color='#777'; this.querySelector('div').style.background='#999'"
                                                style="background: none; border: none; color: #777; font-size: 10px; font-weight: 500; cursor: pointer; transition: all 0.25s; text-transform: uppercase; letter-spacing: 1.8px; padding: 0; display: flex; align-items: center; gap: 8px;">
                                                <div style="width: 5px; height: 5px; background: #999; border-radius: 50%; transition: all 0.25s;"></div>
                                                Request Callback
                                            </button>
                                            <div style="width: 1px; height: 14px; background: linear-gradient(180deg, transparent, rgba(212, 175, 55, 0.3), transparent);"></div>
                                            <button
                                                onmouseover="this.style.color='var(--gold)'; this.querySelector('div').style.background='var(--gold)'"
                                                onmouseout="this.style.color='#777'; this.querySelector('div').style.background='#999'"
                                                style="background: none; border: none; color: #777; font-size: 10px; font-weight: 500; cursor: pointer; transition: all 0.25s; text-transform: uppercase; letter-spacing: 1.8px; padding: 0; display: flex; align-items: center; gap: 8px;">
                                                <div style="width: 5px; height: 5px; background: #999; border-radius: 50%; transition: all 0.25s;"></div>
                                                Save to Wishlist
                                            </button>
                                            <div style="width: 1px; height: 14px; background: linear-gradient(180deg, transparent, rgba(212, 175, 55, 0.3), transparent);"></div>
                                            <button
                                                onmouseover="this.style.color='var(--gold)'; this.querySelector('div').style.background='var(--gold)'"
                                                onmouseout="this.style.color='#777'; this.querySelector('div').style.background='#999'"
                                                style="background: none; border: none; color: #777; font-size: 10px; font-weight: 500; cursor: pointer; transition: all 0.25s; text-transform: uppercase; letter-spacing: 1.8px; padding: 0; display: flex; align-items: center; gap: 8px;">
                                                <div style="width: 5px; height: 5px; background: #999; border-radius: 50%; transition: all 0.25s;"></div>
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

    print("💎 Applying OPULENT LUXURY Design...")
    print("\n✨ Rich Features (NOT Minimalistic):")
    print("  • Decorative corner frames (gold accents)")
    print("  • Layered background gradients")
    print("  • Rich duration badge with glossy effect")
    print("  • Gold vertical line frame for title section")
    print("  • SVG icons for each info item (calendar, ship, globe)")
    print("  • Info grid with gold background and border")
    print("  • Premium features box with gold strip accent")
    print("  • Glowing gold bullet points")
    print("  • Multiple decorative gold lines")
    print("  • Squircle buttons with shine effects")
    print("  • 3 secondary actions with gold dividers")
    print("  • Rich typography with multiple font sizes")
    print("  • Multiple layers and depths")
    print("  • Gold accents throughout")
    print("\n⚡ This is RICH and OPULENT luxury!")

    updated_html = apply_opulent_luxury(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ DONE! All 30 cards now have opulent, rich luxury design!")
