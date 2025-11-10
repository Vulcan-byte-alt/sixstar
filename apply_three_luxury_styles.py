#!/usr/bin/env python3
"""
Apply THREE Different Luxury Styles to Cards
- Cards 1-10: Editorial Luxury (Vogue/Magazine style)
- Cards 11-20: Opulent Classic (Four Seasons/Ritz-Carlton style)
- Cards 21-30: Modern Minimalist Luxury (Apple/Aesop style)
"""

import re

def get_editorial_luxury_content(logo_src, logo_alt, duration, title, departure, ship, region):
    """
    STYLE 1: Editorial Luxury - Magazine/Publication Style
    - Very large, light serif titles
    - Minimal info, huge whitespace
    - Single elegant CTA
    - Thin gold separators
    """
    return f'''<!-- STYLE 1: Editorial Luxury -->
                            <div style="padding: 75px 70px 68px; display: flex; flex-direction: column; position: relative; background: linear-gradient(135deg, #fdfcfb 0%, #faf9f7 100%);">

                                <!-- Small Logo Top -->
                                <div style="margin-bottom: 50px;">
                                    <img src="{logo_src}" alt="{logo_alt}"
                                        style="max-height: 38px; width: auto; max-width: 180px; object-fit: contain; opacity: 0.85;">
                                </div>

                                <!-- Large Editorial Title -->
                                <h3 style="font-size: 40px; font-family: 'Cormorant Garamond', serif; color: #1a2332; line-height: 1.45; font-weight: 300; margin-bottom: 20px; letter-spacing: 1px; max-width: 90%; font-style: italic;">
                                    {title}
                                </h3>

                                <!-- Thin Gold Separator -->
                                <div style="width: 100px; height: 1px; background: linear-gradient(90deg, #c9a961, transparent); margin: 32px 0 36px; opacity: 0.6;"></div>

                                <!-- Minimal Essential Info -->
                                <div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 50px;">
                                    <div style="font-size: 15px; font-family: 'Inter', sans-serif; color: #6b6b6b; font-weight: 300; letter-spacing: 0.8px;">
                                        {ship} <span style="margin: 0 12px; color: #c9a961;">·</span> {region}
                                    </div>
                                    <div style="font-size: 14px; font-family: 'Inter', sans-serif; color: #999; font-weight: 300; letter-spacing: 0.5px;">
                                        Departing {departure} <span style="margin: 0 12px; color: #c9a961;">·</span> {duration} nights
                                    </div>
                                </div>

                                <!-- Premium Details (EXPANDS) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.45s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.45s;">
                                    <div style="overflow: hidden;">
                                        <div style="padding: 24px 0; border-top: 1px solid rgba(201, 169, 97, 0.15); border-bottom: 1px solid rgba(201, 169, 97, 0.15); margin-bottom: 40px;">
                                            <div style="font-size: 11px; color: #888; font-weight: 400; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 14px; font-family: 'Inter', sans-serif;">Included</div>
                                            <div style="display: flex; flex-direction: column; gap: 10px;">
                                                <span style="font-size: 13px; color: #666; font-weight: 300; letter-spacing: 0.3px;">All-inclusive luxury amenities</span>
                                                <span style="font-size: 13px; color: #666; font-weight: 300; letter-spacing: 0.3px;">Curated shore excursions</span>
                                                <span style="font-size: 13px; color: #666; font-weight: 300; letter-spacing: 0.3px;">Exclusive onboard experiences</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Single Elegant CTA -->
                                <div>
                                    <button
                                        onmouseover="this.style.background='#1a2332'; this.style.color='#fdfcfb'; this.style.transform='translateX(4px)'"
                                        onmouseout="this.style.background='transparent'; this.style.color='#1a2332'; this.style.transform='translateX(0)'"
                                        style="background: transparent; color: #1a2332; border: 1px solid rgba(26, 35, 50, 0.2); border-radius: 0; padding: 18px 48px; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 3px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-family: 'Inter', sans-serif;">
                                        Explore This Voyage
                                    </button>
                                </div>

                                <!-- Minimal Link (EXPANDS) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.45s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.45s;">
                                    <div style="overflow: hidden;">
                                        <div style="margin-top: 24px;">
                                            <button
                                                onmouseover="this.style.color='#c9a961'"
                                                onmouseout="this.style.color='#aaa'"
                                                style="background: none; border: none; color: #aaa; font-size: 11px; font-weight: 400; cursor: pointer; transition: color 0.3s; letter-spacing: 1px; padding: 0; font-family: 'Inter', sans-serif;">
                                                Request Details →
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </article>'''

def get_opulent_classic_content(logo_src, logo_alt, duration, title, departure, ship, region):
    """
    STYLE 2: Opulent Classic - Traditional Luxury
    - Rich gold decorative elements
    - Ornate details and borders
    - Multiple visual layers
    - Warm backgrounds
    """
    return f'''<!-- STYLE 2: Opulent Classic -->
                            <div style="padding: 58px 64px 56px; display: flex; flex-direction: column; position: relative; background: linear-gradient(135deg, #faf8f5 0%, #f5f3ee 100%);">

                                <!-- Decorative Gold Frame -->
                                <div style="position: absolute; top: 24px; left: 24px; right: 24px; bottom: 24px; border: 1px solid rgba(201, 169, 97, 0.25); pointer-events: none;"></div>
                                <div style="position: absolute; top: 28px; left: 28px; right: 28px; bottom: 28px; border: 1px solid rgba(201, 169, 97, 0.15); pointer-events: none;"></div>

                                <!-- Header with Logo & Duration Badge -->
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 42px; position: relative; z-index: 1;">
                                    <div>
                                        <img src="{logo_src}" alt="{logo_alt}"
                                            style="max-height: 48px; width: auto; max-width: 200px; object-fit: contain; opacity: 0.92;">
                                        <!-- Gold Decorative Underline -->
                                        <div style="display: flex; gap: 4px; margin-top: 12px;">
                                            <div style="width: 50px; height: 2px; background: linear-gradient(90deg, #c9a961, transparent);"></div>
                                            <div style="width: 25px; height: 2px; background: linear-gradient(90deg, #c9a961, transparent); opacity: 0.5;"></div>
                                        </div>
                                    </div>

                                    <!-- Ornate Duration Badge -->
                                    <div style="position: relative; padding: 16px 28px; background: linear-gradient(135deg, rgba(201, 169, 97, 0.15), rgba(201, 169, 97, 0.05)); border: 2px solid rgba(201, 169, 97, 0.3); border-radius: 8px; box-shadow: inset 0 1px 2px rgba(255,255,255,0.5), 0 4px 12px rgba(201, 169, 97, 0.1);">
                                        <div style="text-align: center;">
                                            <div style="color: #c9a961; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 6px;">Duration</div>
                                            <div style="color: #1a2332; font-size: 22px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{duration} Nights</div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Title with Side Border -->
                                <div style="border-left: 3px solid rgba(201, 169, 97, 0.4); padding-left: 26px; margin-bottom: 38px; position: relative; z-index: 1;">
                                    <!-- Gold Accent Dot -->
                                    <div style="position: absolute; left: -7px; top: 0; width: 10px; height: 10px; background: #c9a961; border-radius: 50%; box-shadow: 0 0 12px rgba(201, 169, 97, 0.5);"></div>

                                    <h3 style="font-size: 34px; font-family: 'Cormorant Garamond', serif; color: #1a2332; line-height: 1.35; font-weight: 400; margin-bottom: 28px; letter-spacing: 0.6px;">
                                        {title}
                                    </h3>

                                    <!-- Rich Info Box -->
                                    <div style="background: linear-gradient(135deg, rgba(201, 169, 97, 0.08), rgba(201, 169, 97, 0.03)); padding: 22px 26px; border-radius: 10px; border: 1px solid rgba(201, 169, 97, 0.2);">
                                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px;">
                                            <div>
                                                <div style="color: #c9a961; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85;">Vessel</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{ship}</div>
                                            </div>
                                            <div>
                                                <div style="color: #c9a961; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85;">Region</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{region}</div>
                                            </div>
                                            <div style="grid-column: 1 / -1;">
                                                <div style="color: #c9a961; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85;">Departure</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{departure}</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Premium Features (EXPANDS) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s; position: relative; z-index: 1;">
                                    <div style="overflow: hidden;">
                                        <div style="margin-bottom: 32px; padding: 20px 24px; background: linear-gradient(135deg, rgba(26, 35, 50, 0.04), transparent); border-radius: 10px; border-left: 3px solid #c9a961;">
                                            <div style="display: flex; flex-direction: column; gap: 12px;">
                                                <div style="display: flex; align-items: center; gap: 12px;">
                                                    <div style="width: 6px; height: 6px; background: #c9a961; border-radius: 50%; box-shadow: 0 0 8px rgba(201, 169, 97, 0.6);"></div>
                                                    <span style="font-size: 13px; color: #555; font-weight: 400; letter-spacing: 0.3px;">Premium all-inclusive amenities</span>
                                                </div>
                                                <div style="display: flex; align-items: center; gap: 12px;">
                                                    <div style="width: 6px; height: 6px; background: #c9a961; border-radius: 50%; box-shadow: 0 0 8px rgba(201, 169, 97, 0.6);"></div>
                                                    <span style="font-size: 13px; color: #555; font-weight: 400; letter-spacing: 0.3px;">Curated shore experiences</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Opulent Buttons -->
                                <div style="display: flex; gap: 14px; position: relative; z-index: 1;">
                                    <button
                                        onmouseover="this.style.background='linear-gradient(135deg, #b8935a, #c9a961)'; this.style.boxShadow='0 8px 24px rgba(201, 169, 97, 0.35)'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='linear-gradient(135deg, #1a2332, #2a3442)'; this.style.boxShadow='0 4px 16px rgba(26, 35, 50, 0.25)'; this.style.transform='translateY(0)'"
                                        style="flex: 1; padding: 20px 36px; background: linear-gradient(135deg, #1a2332, #2a3442); color: white; border: none; border-radius: 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s; box-shadow: 0 4px 16px rgba(26, 35, 50, 0.25);">
                                        View Details
                                    </button>
                                    <button
                                        onmouseover="this.style.background='rgba(201, 169, 97, 0.15)'; this.style.borderColor='#c9a961'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(26, 35, 50, 0.2)'; this.style.transform='translateY(0)'"
                                        style="padding: 20px 32px; background: transparent; color: #1a2332; border: 2px solid rgba(26, 35, 50, 0.2); border-radius: 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s;">
                                        Inquire
                                    </button>
                                </div>

                                <!-- Secondary Actions (EXPANDS) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s; position: relative; z-index: 1;">
                                    <div style="overflow: hidden;">
                                        <div style="display: flex; justify-content: center; gap: 28px; padding-top: 24px; margin-top: 20px; border-top: 1px solid rgba(201, 169, 97, 0.2);">
                                            <button
                                                onmouseover="this.style.color='#c9a961'"
                                                onmouseout="this.style.color='#888'"
                                                style="background: none; border: none; color: #888; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0;">
                                                Request Callback
                                            </button>
                                            <button
                                                onmouseover="this.style.color='#c9a961'"
                                                onmouseout="this.style.color='#888'"
                                                style="background: none; border: none; color: #888; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0;">
                                                Download Brochure
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </article>'''

def get_modern_minimalist_content(logo_src, logo_alt, duration, title, departure, ship, region):
    """
    STYLE 3: Modern Minimalist Luxury - Contemporary Premium
    - Asymmetric layout
    - Ultra-refined spacing
    - Cool tones, subtle details
    - Premium but understated
    """
    return f'''<!-- STYLE 3: Modern Minimalist Luxury -->
                            <div style="padding: 70px 68px 66px; display: flex; flex-direction: column; position: relative; background: linear-gradient(135deg, #fefefe 0%, #f9f9f9 100%);">

                                <!-- Top: Logo & Duration (Asymmetric) -->
                                <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 40px; align-items: start; margin-bottom: 52px; padding-bottom: 32px; border-bottom: 1px solid rgba(0, 0, 0, 0.04);">
                                    <div>
                                        <img src="{logo_src}" alt="{logo_alt}"
                                            style="max-height: 42px; width: auto; max-width: 190px; object-fit: contain; opacity: 0.88;">
                                    </div>
                                    <div style="text-align: right;">
                                        <div style="font-size: 11px; color: #999; font-weight: 400; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 6px; font-family: 'Inter', sans-serif;">Duration</div>
                                        <div style="font-size: 20px; color: #2a2a2a; font-weight: 300; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{duration} Nights</div>
                                    </div>
                                </div>

                                <!-- Large Refined Title -->
                                <div style="margin-bottom: 48px;">
                                    <h3 style="font-size: 38px; font-family: 'Cormorant Garamond', serif; color: #1a1a1a; line-height: 1.4; font-weight: 300; margin-bottom: 18px; letter-spacing: 0.8px;">
                                        {title}
                                    </h3>

                                    <!-- Subtle Info Line -->
                                    <div style="font-size: 14px; font-family: 'Inter', sans-serif; color: #888; font-weight: 300; letter-spacing: 0.6px; margin-top: 16px;">
                                        {ship} <span style="margin: 0 10px; color: #ccc;">|</span> {region}
                                    </div>
                                </div>

                                <!-- Minimal Info Card -->
                                <div style="margin-bottom: 48px;">
                                    <div style="display: inline-block; padding: 16px 26px; background: rgba(0, 0, 0, 0.02); border-radius: 16px; border: 1px solid rgba(0, 0, 0, 0.04);">
                                        <div style="font-size: 10px; color: #aaa; font-weight: 400; text-transform: uppercase; letter-spacing: 1.8px; margin-bottom: 6px; font-family: 'Inter', sans-serif;">Departure</div>
                                        <div style="font-size: 15px; color: #333; font-weight: 300; font-family: 'Inter', sans-serif; letter-spacing: 0.5px;">{departure}</div>
                                    </div>
                                </div>

                                <!-- Premium Details (EXPANDS) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.45s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.45s;">
                                    <div style="overflow: hidden;">
                                        <div style="margin-bottom: 42px; padding: 20px 0; border-top: 1px solid rgba(0, 0, 0, 0.04); border-bottom: 1px solid rgba(0, 0, 0, 0.04);">
                                            <div style="display: flex; flex-direction: column; gap: 12px;">
                                                <span style="font-size: 13px; color: #666; font-weight: 300; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">― All-inclusive premium experience</span>
                                                <span style="font-size: 13px; color: #666; font-weight: 300; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">― Exclusive shore excursions</span>
                                                <span style="font-size: 13px; color: #666; font-weight: 300; letter-spacing: 0.3px; font-family: 'Inter', sans-serif;">― Limited availability</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Minimal CTAs -->
                                <div style="display: flex; gap: 16px;">
                                    <button
                                        onmouseover="this.style.background='#1a1a1a'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 20px rgba(0, 0, 0, 0.12)'"
                                        onmouseout="this.style.background='#2a2a2a'; this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0, 0, 0, 0.08)'"
                                        style="flex: 1; padding: 19px 38px; background: #2a2a2a; color: #ffffff; border: none; border-radius: 16px; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 3px; cursor: pointer; transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08); font-family: 'Inter', sans-serif;">
                                        View Voyage
                                    </button>
                                    <button
                                        onmouseover="this.style.background='rgba(0, 0, 0, 0.04)'; this.style.borderColor='rgba(0, 0, 0, 0.15)'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(0, 0, 0, 0.08)'; this.style.transform='translateY(0)'"
                                        style="padding: 19px 34px; background: transparent; color: #2a2a2a; border: 1px solid rgba(0, 0, 0, 0.08); border-radius: 16px; font-size: 10px; font-weight: 500; text-transform: uppercase; letter-spacing: 3px; cursor: pointer; transition: all 0.35s; font-family: 'Inter', sans-serif;">
                                        Inquire
                                    </button>
                                </div>

                                <!-- Subtle Link (EXPANDS) -->
                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.45s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.45s;">
                                    <div style="overflow: hidden;">
                                        <div style="display: flex; justify-content: center; gap: 32px; padding-top: 26px; margin-top: 22px;">
                                            <button
                                                onmouseover="this.style.color='#666'"
                                                onmouseout="this.style.color='#aaa'"
                                                style="background: none; border: none; color: #aaa; font-size: 10px; font-weight: 400; cursor: pointer; transition: color 0.25s; letter-spacing: 1.5px; padding: 0; font-family: 'Inter', sans-serif;">
                                                Request Information
                                            </button>
                                            <button
                                                onmouseover="this.style.color='#666'"
                                                onmouseout="this.style.color='#aaa'"
                                                style="background: none; border: none; color: #aaa; font-size: 10px; font-weight: 400; cursor: pointer; transition: color 0.25s; letter-spacing: 1.5px; padding: 0; font-family: 'Inter', sans-serif;">
                                                Download Brochure
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </article>'''

def apply_three_luxury_styles(html_content):
    """
    Apply three different luxury styles to different card groups
    """

    pattern = r'(<!-- (?:True Luxury Minimalist Content|Rich Luxury Content|Ultra-Refined Luxury Content|Opulent Luxury Content|Structured Luxury Content) -->)(.*?)(</div>\s*</article>)'

    card_counter = 0

    def replace_content(match):
        nonlocal card_counter
        card_counter += 1

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

        # Apply different styles based on card number
        if card_counter <= 10:
            return get_editorial_luxury_content(logo_src, logo_alt, duration, title, departure, ship, region)
        elif card_counter <= 20:
            return get_opulent_classic_content(logo_src, logo_alt, duration, title, departure, ship, region)
        else:
            return get_modern_minimalist_content(logo_src, logo_alt, duration, title, departure, ship, region)

    updated_html = re.sub(pattern, replace_content, html_content, flags=re.DOTALL)
    return updated_html

if __name__ == "__main__":
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("✨ Applying THREE LUXURY STYLES for comparison...")
    print("\n" + "="*70)
    print("📖 STYLE 1: Editorial Luxury (Cards 1-10)")
    print("="*70)
    print("  • Vogue/Condé Nast magazine style")
    print("  • Very large (40px), light-weight italic serif titles")
    print("  • Minimal info visible by default")
    print("  • Huge whitespace (75px padding)")
    print("  • Single elegant CTA with minimal border")
    print("  • Thin gold line separators")
    print("  • Cream background gradient")
    print("  • Very refined and editorial")
    print()
    print("="*70)
    print("🏛️ STYLE 2: Opulent Classic (Cards 11-20)")
    print("="*70)
    print("  • Four Seasons/Ritz-Carlton traditional luxury")
    print("  • Double gold frame borders")
    print("  • Rich gold decorative elements & glowing accents")
    print("  • Ornate duration badge with inner shadow")
    print("  • Gold vertical accent line with dot")
    print("  • Info in rich gold-background box")
    print("  • Multiple visual layers")
    print("  • Warm beige background")
    print()
    print("="*70)
    print("🎨 STYLE 3: Modern Minimalist Luxury (Cards 21-30)")
    print("="*70)
    print("  • Apple/Aesop contemporary premium")
    print("  • Asymmetric grid layout (2fr 1fr)")
    print("  • Ultra-refined spacing (70px padding)")
    print("  • Large (38px) light-weight titles")
    print("  • Cool grayscale tones")
    print("  • Subtle borders and shadows")
    print("  • Modern typography mix")
    print("  • Premium but understated")
    print()
    print("="*70)

    updated_html = apply_three_luxury_styles(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ DONE! Scroll through the page to see all three styles:")
    print("   • Cards 1-10: Editorial Luxury")
    print("   • Cards 11-20: Opulent Classic")
    print("   • Cards 21-30: Modern Minimalist Luxury")
    print("\nWhich style feels most luxurious to you? 🎯")
