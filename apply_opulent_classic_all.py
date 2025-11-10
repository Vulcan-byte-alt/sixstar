#!/usr/bin/env python3
"""
Apply Opulent Classic Luxury to ALL 30 Cards
With CORRECT font usage:
- TheSeasons: Main titles
- Cormorant Garamond: Numbers, secondary serif text
- Inter: Labels, small text, body
"""

import re

def apply_opulent_classic(html_content):
    """
    Apply opulent classic luxury design to all cards
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

    # Pattern to match content sections - catch everything
    pattern = r'(<!-- (?:Redesigned Content Section|Opulent Classic Luxury|STYLE 1|STYLE 2|STYLE 3|True Luxury|Rich Luxury|Ultra-Refined|Opulent|Structured|Editorial)[^>]*-->)(.*?)(</div>\s*</article>)'

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
            year_match = re.search(r'(\d{4})', full_section)
            departure = year_match.group(1) if year_match else "2026"

        # Ship and Region - they're combined in the format "Region • Ship"
        combined_match = re.search(r'<span>([^•<]+)•([^<]+)</span>', full_section)
        if combined_match:
            region = combined_match.group(1).strip()
            ship = combined_match.group(2).strip()
        else:
            # Try old format - Ship label
            ship_match = re.search(r'Ship</div>.*?<div[^>]*>([^<]+)</div>', full_section, re.DOTALL)
            if ship_match:
                ship = ' '.join(ship_match.group(1).split())  # Clean whitespace
            else:
                ship = "Luxury Vessel"

            # Region label
            region_match = re.search(r'Region</div>.*?<div[^>]*>([^<]+)</div>', full_section, re.DOTALL)
            if region_match:
                region = ' '.join(region_match.group(1).split())  # Clean whitespace
            else:
                region = "Worldwide"

        new_content = f'''<!-- Opulent Classic Luxury -->
                            <div style="padding: 58px 64px 56px; display: flex; flex-direction: column; position: relative; background: linear-gradient(135deg, #faf8f5 0%, #f5f3ee 100%);">

                                <!-- Decorative Gold Double Frame -->
                                <div style="position: absolute; top: 24px; left: 24px; right: 24px; bottom: 24px; border: 1px solid rgba(212, 175, 55, 0.25); pointer-events: none;"></div>
                                <div style="position: absolute; top: 28px; left: 28px; right: 28px; bottom: 28px; border: 1px solid rgba(212, 175, 55, 0.15); pointer-events: none;"></div>

                                <!-- Header with Logo & Duration Badge -->
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 42px; position: relative; z-index: 1;">
                                    <div>
                                        <img src="{logo_src}" alt="{logo_alt}"
                                            style="max-height: 48px; width: auto; max-width: 200px; object-fit: contain; opacity: 0.92;">
                                        <!-- Gold Decorative Underline -->
                                        <div style="display: flex; gap: 4px; margin-top: 12px;">
                                            <div style="width: 50px; height: 2px; background: linear-gradient(90deg, #d4af37, transparent);"></div>
                                            <div style="width: 25px; height: 2px; background: linear-gradient(90deg, #d4af37, transparent); opacity: 0.5;"></div>
                                        </div>
                                    </div>

                                    <!-- Ornate Duration Badge -->
                                    <div style="position: relative; padding: 16px 28px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.15), rgba(212, 175, 55, 0.05)); border: 2px solid rgba(212, 175, 55, 0.3); border-radius: 8px; box-shadow: inset 0 1px 2px rgba(255,255,255,0.5), 0 4px 12px rgba(212, 175, 55, 0.1);">
                                        <div style="text-align: center;">
                                            <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 6px; font-family: 'Inter', sans-serif;">Duration</div>
                                            <div style="color: #1a2332; font-size: 22px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{duration} Nights</div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Title with Gold Accent Border -->
                                <div style="border-left: 3px solid rgba(212, 175, 55, 0.4); padding-left: 26px; margin-bottom: 38px; position: relative; z-index: 1;">
                                    <!-- Gold Accent Dot -->
                                    <div style="position: absolute; left: -7px; top: 0; width: 10px; height: 10px; background: #d4af37; border-radius: 50%; box-shadow: 0 0 12px rgba(212, 175, 55, 0.5);"></div>

                                    <h3 style="font-size: 34px; font-family: 'TheSeasons', serif; color: #1a2332; line-height: 1.35; font-weight: 400; margin-bottom: 28px; letter-spacing: 0.6px;">
                                        {title}
                                    </h3>

                                    <!-- Rich Info Box -->
                                    <div style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.08), rgba(212, 175, 55, 0.03)); padding: 22px 26px; border-radius: 10px; border: 1px solid rgba(212, 175, 55, 0.2);">
                                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px;">
                                            <div>
                                                <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: 'Inter', sans-serif;">Vessel</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{ship}</div>
                                            </div>
                                            <div>
                                                <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: 'Inter', sans-serif;">Region</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{region}</div>
                                            </div>
                                            <div style="grid-column: 1 / -1;">
                                                <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: 'Inter', sans-serif;">Departure</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{departure}</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Premium Features (EXPANDS on hover) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s; position: relative; z-index: 1;">
                                    <div style="overflow: hidden;">
                                        <div style="margin-bottom: 32px; padding: 20px 24px; background: linear-gradient(135deg, rgba(26, 35, 50, 0.04), transparent); border-radius: 10px; border-left: 3px solid #d4af37;">
                                            <div style="display: flex; flex-direction: column; gap: 12px;">
                                                <div style="display: flex; align-items: center; gap: 12px;">
                                                    <div style="width: 6px; height: 6px; background: #d4af37; border-radius: 50%; box-shadow: 0 0 8px rgba(212, 175, 55, 0.6);"></div>
                                                    <span style="font-size: 13px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Premium all-inclusive amenities</span>
                                                </div>
                                                <div style="display: flex; align-items: center; gap: 12px;">
                                                    <div style="width: 6px; height: 6px; background: #d4af37; border-radius: 50%; box-shadow: 0 0 8px rgba(212, 175, 55, 0.6);"></div>
                                                    <span style="font-size: 13px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Curated shore experiences</span>
                                                </div>
                                                <div style="display: flex; align-items: center; gap: 12px;">
                                                    <div style="width: 6px; height: 6px; background: #d4af37; border-radius: 50%; box-shadow: 0 0 8px rgba(212, 175, 55, 0.6);"></div>
                                                    <span style="font-size: 13px; color: #555; font-weight: 400; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">Limited availability</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Opulent Squircle Buttons -->
                                <div style="display: flex; gap: 14px; position: relative; z-index: 1;">
                                    <button
                                        onmouseover="this.style.background='linear-gradient(135deg, #c9a961, #d4af37)'; this.style.boxShadow='0 8px 24px rgba(212, 175, 55, 0.35)'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='linear-gradient(135deg, #1a2332, #2a3442)'; this.style.boxShadow='0 4px 16px rgba(26, 35, 50, 0.25)'; this.style.transform='translateY(0)'"
                                        style="flex: 1; padding: 20px 36px; background: linear-gradient(135deg, #1a2332, #2a3442); color: white; border: none; border-radius: 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s; box-shadow: 0 4px 16px rgba(26, 35, 50, 0.25); font-family: 'Inter', sans-serif;">
                                        View Details
                                    </button>
                                    <button
                                        onmouseover="this.style.background='rgba(212, 175, 55, 0.15)'; this.style.borderColor='#d4af37'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(26, 35, 50, 0.2)'; this.style.transform='translateY(0)'"
                                        style="padding: 20px 32px; background: transparent; color: #1a2332; border: 2px solid rgba(26, 35, 50, 0.2); border-radius: 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s; font-family: 'Inter', sans-serif;">
                                        Inquire
                                    </button>
                                </div>

                                <!-- Secondary Actions (EXPANDS on hover) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s; position: relative; z-index: 1;">
                                    <div style="overflow: hidden;">
                                        <div style="display: flex; justify-content: center; gap: 28px; padding-top: 24px; margin-top: 20px; border-top: 1px solid rgba(212, 175, 55, 0.2);">
                                            <button
                                                onmouseover="this.style.color='#d4af37'"
                                                onmouseout="this.style.color='#888'"
                                                style="background: none; border: none; color: #888; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0; font-family: 'Inter', sans-serif;">
                                                Request Callback
                                            </button>
                                            <button
                                                onmouseover="this.style.color='#d4af37'"
                                                onmouseout="this.style.color='#888'"
                                                style="background: none; border: none; color: #888; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0; font-family: 'Inter', sans-serif;">
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

    print("🏛️ Applying OPULENT CLASSIC to ALL 30 cards...")
    print("\n✨ Correct Font Usage:")
    print("  • TheSeasons: Main voyage titles (34px)")
    print("  • Cormorant Garamond: Numbers, ship/region info (16px, 22px)")
    print("  • Inter: All labels and body text (9px, 10px, 11px, 13px)")
    print()
    print("🎨 Design Features:")
    print("  • Double gold frame borders")
    print("  • Gold decorative underlines")
    print("  • Ornate duration badge with glossy effect")
    print("  • Gold vertical accent line with glowing dot")
    print("  • Rich info box with gold background")
    print("  • Premium features expand on hover (3 items)")
    print("  • Squircle buttons (12px radius)")
    print("  • Navy gradient primary → Gold on hover")
    print("  • Secondary actions expand on hover")
    print("  • Warm beige gradient background")

    updated_html = apply_opulent_classic(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ DONE! All 30 cards now have Opulent Classic design with correct fonts!")
