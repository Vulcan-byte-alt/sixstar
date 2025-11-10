#!/usr/bin/env python3
"""
Extract data from original HTML and apply Opulent Classic design with correct data
"""

import re

def extract_card_data(html_content):
    """Extract all card data from HTML"""
    cards_data = []

    # Find all article elements
    article_pattern = r'<article[^>]*data-deal-id="([^"]*)"[^>]*>(.*?)</article>'
    articles = re.findall(article_pattern, html_content, re.DOTALL)

    for deal_id, content in articles:
        data = {'deal_id': deal_id}

        # Extract logo
        logo_match = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]+)"', content)
        if logo_match:
            data['logo_src'] = logo_match.group(1)
            data['logo_alt'] = logo_match.group(2)
        else:
            data['logo_src'] = ''
            data['logo_alt'] = ''

        # Extract title from h2 or h3
        title_match = re.search(r'<h[23][^>]*>([^<]+)</h[23]>', content)
        if title_match:
            data['title'] = title_match.group(1).strip()
        else:
            data['title'] = 'Luxury Voyage'

        # Extract duration - look for "X Nights" or "X Night"
        duration_match = re.search(r'>(\d+)\s*Nights?<', content)
        if duration_match:
            data['duration'] = duration_match.group(1)
        else:
            data['duration'] = '7'

        # Extract departure - look for month and year pattern or just dates
        departure_match = re.search(r'>(\d+\s+[A-Za-z]+\s+\d{4})<', content)
        if departure_match:
            # Full date found
            full_date = departure_match.group(1)
            parts = full_date.split()
            if len(parts) >= 2:
                data['departure'] = f"{parts[1]} {parts[2] if len(parts) > 2 else parts[1]}"
            else:
                data['departure'] = full_date
        else:
            # Look for just year
            year_match = re.search(r'>(\d{4})<', content)
            data['departure'] = year_match.group(1) if year_match else '2026'

        # Extract ship - look for "Ship" label followed by value
        ship_patterns = [
            r'Ship</div>\s*<div[^>]*>([^<]+)<',
            r'>Ship<[^>]*>\s*<div[^>]*>([^<]+)<',
            r'Ship.*?font-weight: 600[^>]*>([^<]+)<'
        ]
        for pattern in ship_patterns:
            ship_match = re.search(pattern, content, re.DOTALL)
            if ship_match:
                data['ship'] = ship_match.group(1).strip()
                break
        if 'ship' not in data:
            data['ship'] = 'TBA'

        # Extract region - look for "Region" label followed by value
        region_patterns = [
            r'Region</div>\s*<div[^>]*>([^<]+)<',
            r'>Region<[^>]*>\s*<div[^>]*>([^<]+)<',
            r'Region.*?font-weight: 600[^>]*>([^<]+)<'
        ]
        for pattern in region_patterns:
            region_match = re.search(pattern, content, re.DOTALL)
            if region_match:
                data['region'] = region_match.group(1).strip()
                break
        if 'region' not in data:
            data['region'] = 'TBA'

        cards_data.append(data)

    return cards_data

def apply_opulent_classic_with_data(current_html, cards_data):
    """Apply opulent classic design with extracted data"""

    # Update card hover effects first
    current_html = current_html.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.transform='translateY(0)'; el.style.opacity='1'; el.style.visibility='visible'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})"
    )
    current_html = current_html.replace(
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.transform='translateY(-10px)'; el.style.opacity='0'; el.style.visibility='hidden'})",
        "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})"
    )

    # Pattern to match content sections
    pattern = r'(<article[^>]*data-deal-id="([^"]*)"[^>]*>.*?)(<!-- [^>]*Luxury[^>]*Content -->)(.*?)(</div>\s*</article>)'

    card_index = 0

    def replace_with_data(match):
        nonlocal card_index

        if card_index >= len(cards_data):
            return match.group(0)

        data = cards_data[card_index]
        card_index += 1

        article_opening = match.group(1)

        new_content = f'''<!-- Opulent Classic Luxury -->
                            <div style="padding: 58px 64px 56px; display: flex; flex-direction: column; position: relative; background: linear-gradient(135deg, #faf8f5 0%, #f5f3ee 100%);">

                                <!-- Decorative Gold Double Frame -->
                                <div style="position: absolute; top: 24px; left: 24px; right: 24px; bottom: 24px; border: 1px solid rgba(212, 175, 55, 0.25); pointer-events: none;"></div>
                                <div style="position: absolute; top: 28px; left: 28px; right: 28px; bottom: 28px; border: 1px solid rgba(212, 175, 55, 0.15); pointer-events: none;"></div>

                                <!-- Header with Logo & Duration Badge -->
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 42px; position: relative; z-index: 1;">
                                    <div>
                                        <img src="{data['logo_src']}" alt="{data['logo_alt']}"
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
                                            <div style="color: #1a2332; font-size: 22px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{data['duration']} Nights</div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Title with Gold Accent Border -->
                                <div style="border-left: 3px solid rgba(212, 175, 55, 0.4); padding-left: 26px; margin-bottom: 38px; position: relative; z-index: 1;">
                                    <!-- Gold Accent Dot -->
                                    <div style="position: absolute; left: -7px; top: 0; width: 10px; height: 10px; background: #d4af37; border-radius: 50%; box-shadow: 0 0 12px rgba(212, 175, 55, 0.5);"></div>

                                    <h3 style="font-size: 34px; font-family: 'TheSeasons', serif; color: #1a2332; line-height: 1.35; font-weight: 400; margin-bottom: 28px; letter-spacing: 0.6px;">
                                        {data['title']}
                                    </h3>

                                    <!-- Rich Info Box -->
                                    <div style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.08), rgba(212, 175, 55, 0.03)); padding: 22px 26px; border-radius: 10px; border: 1px solid rgba(212, 175, 55, 0.2);">
                                        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px;">
                                            <div>
                                                <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: 'Inter', sans-serif;">Vessel</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{data['ship']}</div>
                                            </div>
                                            <div>
                                                <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: 'Inter', sans-serif;">Region</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{data['region']}</div>
                                            </div>
                                            <div style="grid-column: 1 / -1;">
                                                <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; opacity: 0.85; font-family: 'Inter', sans-serif;">Departure</div>
                                                <div style="color: #1a2332; font-size: 16px; font-weight: 400; font-family: 'Cormorant Garamond', serif;">{data['departure']}</div>
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

        return article_opening + new_content

    updated_html = re.sub(pattern, replace_with_data, current_html, flags=re.DOTALL)
    return updated_html

if __name__ == "__main__":
    # Read original HTML to extract data
    print("📊 Extracting data from original HTML...")
    with open('/tmp/deals_original.html', 'r', encoding='utf-8') as f:
        original_html = f.read()

    cards_data = extract_card_data(original_html)
    print(f"✓ Extracted data for {len(cards_data)} cards")

    # Show first 3 cards data for verification
    for i, data in enumerate(cards_data[:3]):
        print(f"\nCard {i+1}:")
        print(f"  Title: {data['title']}")
        print(f"  Ship: {data['ship']}")
        print(f"  Region: {data['region']}")
        print(f"  Departure: {data['departure']}")
        print(f"  Duration: {data['duration']} nights")

    # Read current HTML
    print("\n🎨 Applying Opulent Classic design with correct data...")
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        current_html = f.read()

    # Apply design with data
    updated_html = apply_opulent_classic_with_data(current_html, cards_data)

    # Save updated HTML
    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("\n✅ DONE! All cards now have Opulent Classic design with CORRECT data!")
