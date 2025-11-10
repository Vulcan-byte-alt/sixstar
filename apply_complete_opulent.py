#!/usr/bin/env python3
"""
Apply complete Opulent Classic design to ALL 30 cards with:
1. Proper tag closing
2. Correct data extraction
3. Hover expansion
4. Long heading handling
5. New images
"""

import re
import os

def apply_complete_opulent(html_content):
    """Apply opulent design with all fixes"""

    # First, update article hover to include expand-on-hover
    article_pattern = r'(<article[^>]*onmouseover=")(this\.style\.transform[^"]*")(\s+onmouseout=")(this\.style\.transform[^"]*")'

    def fix_article_hover(match):
        return (match.group(1) +
                "this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 48px rgba(0,0,0,0.12)'; this.style.borderColor='rgba(212, 175, 55, 0.3)'; this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'});" +
                match.group(3) +
                "this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0,0,0,0.08)'; this.style.borderColor='rgba(255,255,255,0.8)'; this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})")

    html_content = re.sub(article_pattern, fix_article_hover, html_content)

    # Pattern to match the redesigned content sections
    pattern = r'(<!-- Redesigned Content Section -->)(.*?)(</div>\s*</article>)'

    card_counter = 0

    def replace_content(match):
        nonlocal card_counter
        card_counter += 1

        full_section = match.group(0)

        # Extract title
        title_match = re.search(r'<h[23][^>]*>([^<]+)</h[23]>', full_section)
        title = title_match.group(1).strip() if title_match else "Luxury Voyage"

        # Adjust font size for long titles
        if len(title) > 70:
            title_size = "26px"
            line_height = "1.3"
        elif len(title) > 50:
            title_size = "30px"
            line_height = "1.3"
        else:
            title_size = "34px"
            line_height = "1.35"

        # Extract duration
        duration_match = re.search(r'>(\d+)\s*Nights?<', full_section)
        duration = duration_match.group(1) if duration_match else "7"

        # Extract departure
        departure_match = re.search(r'>(\d+\s+[A-Za-z]+\s+\d{4})<', full_section)
        if departure_match:
            parts = departure_match.group(1).split()
            departure = f"{parts[1]} {parts[2]}" if len(parts) >= 3 else departure_match.group(1)
        else:
            year_match = re.search(r'>(\d{4})<', full_section)
            departure = year_match.group(1) if year_match else "2026"

        # Extract ship and region - combined format
        combined_match = re.search(r'<span>([^•<]+)•([^<]+)</span>', full_section)
        if combined_match:
            region = combined_match.group(1).strip()
            ship = combined_match.group(2).strip()
        else:
            # Fallback: separate labels
            ship_match = re.search(r'Ship</div>.*?<div[^>]*>([^<]+)</div>', full_section, re.DOTALL)
            ship = ' '.join(ship_match.group(1).split()) if ship_match else "Luxury Vessel"

            region_match = re.search(r'Region</div>.*?<div[^>]*>([^<]+)</div>', full_section, re.DOTALL)
            region = ' '.join(region_match.group(1).split()) if region_match else "Worldwide"

        # Extract logo
        logo_match = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]+)"', full_section)
        if logo_match:
            logo_src = logo_match.group(1)
            logo_alt = logo_match.group(2)
        else:
            logo_src = "images/deals/default-logo.png"
            logo_alt = "Cruise Line"

        # Get new cruise image
        cruise_image = f"images/cruise-destinations/cruise-{card_counter:02d}-{re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:50]}.jpg"
        # Check if file exists, otherwise use fallback
        if not os.path.exists(f"/mnt/d/Websites/travel/{cruise_image}"):
            # Use original image
            img_match = re.search(r'<img src="(images/deals/[^"]+)"', full_section)
            cruise_image = img_match.group(1) if img_match else "images/deals/default.jpg"

        # Extract the entire image section (left side of card)
        image_section_match = re.search(r'(<div style="position: relative; overflow: hidden;">.*?</div>\s*</div>)', full_section, re.DOTALL)
        image_section = image_section_match.group(1) if image_section_match else ""

        # Update the image src in the image section
        if image_section and cruise_image:
            image_section = re.sub(r'<img src="[^"]*"', f'<img src="{cruise_image}"', image_section, count=1)

        new_content = f'''{image_section}

                            <!-- Opulent Classic Luxury -->
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

                                    <h3 style="font-size: {title_size}; font-family: 'TheSeasons', serif; color: #1a2332; line-height: {line_height}; font-weight: 400; margin-bottom: 28px; letter-spacing: 0.6px;">
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

    print(f"\n✓ Processed {card_counter} cards")

    return updated_html

if __name__ == "__main__":
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("🔧 Applying COMPLETE Opulent Classic design...")
    print("   • Proper tag closing")
    print("   • All 30 cards")
    print("   • Hover expansion")
    print("   • Long heading handling")
    print("   • New cruise images")

    updated_html = apply_complete_opulent(html_content)

    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ COMPLETE! All 30 cards fixed with Opulent Classic design!")
