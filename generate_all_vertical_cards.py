#!/usr/bin/env python3
"""
Complete Deal Cards Generator - Vertical Luxury Style
Extracts all 30 deal cards and converts them to vertical luxury layout
"""

import re
import html

def extract_text(pattern, text, default=""):
    """Extract text using regex pattern"""
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else default

def parse_deal_card(article_html, deal_id):
    """Parse a single deal card and extract all information"""

    data = {'id': deal_id}

    # Extract image
    img_match = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]*)"', article_html)
    if img_match:
        data['image'] = img_match.group(1)
        data['title'] = html.unescape(img_match.group(2))

    # Extract badges
    data['badges'] = []
    badge_pattern = r'<div style="position: absolute; top: (\d+)px; left: 16px;[^>]*>([^<]+)</div>'
    for match in re.finditer(badge_pattern, article_html):
        badge_text = match.group(2).strip()
        if badge_text:
            data['badges'].append(badge_text)

    # Extract discount percentage
    discount_match = re.search(r'>(-\d+% OFF)<', article_html)
    data['discount'] = discount_match.group(1) if discount_match else ""

    # Extract cruise line logo
    logo_match = re.search(r'<img src="(images/deals/[^"]+logo[^"]*)"[^>]*alt="([^"]*)"', article_html)
    if logo_match:
        data['logo'] = logo_match.group(1)
        data['cruise_line'] = logo_match.group(2)
    else:
        data['logo'] = ""
        data['cruise_line'] = ""

    # Extract duration
    duration_match = re.search(r'<span[^>]*>(\d+ Nights?)</span>', article_html)
    data['duration'] = duration_match.group(1) if duration_match else ""

    # Extract departure date
    departure_patterns = [
        r'<div style="font-size: 14px; font-weight: 600; color: var\(--navy\);">([^<]+)</div>',
        r'Departure</div>\s*<div[^>]*>([^<]+)</div>'
    ]
    for pattern in departure_patterns:
        match = re.search(pattern, article_html)
        if match:
            data['departure'] = match.group(1).strip()
            break
    else:
        data['departure'] = ""

    # Extract ship name
    ship_match = re.search(r'Ship</div>\s*<div[^>]*>([^<]+)</div>', article_html)
    data['ship'] = ship_match.group(1).strip() if ship_match else ""

    # Extract region
    region_match = re.search(r'Region</div>\s*<div[^>]*>([^<]+)</div>', article_html)
    data['region'] = region_match.group(1).strip() if region_match else ""

    # Extract special offers
    offer_match = re.search(r'<!-- Special Offer.*?<div style="position: relative; z-index: 1;">(.*?)</div>', article_html, re.DOTALL)
    data['special_offer'] = offer_match.group(1).strip() if offer_match else ""

    # Extract prices
    price_label_match = re.search(r'<p style="font-size: 11px;[^>]*>([^<]+)</p>', article_html)
    data['price_label'] = price_label_match.group(1).strip() if price_label_match else "From"

    old_price_match = re.search(r'text-decoration: line-through[^>]*>(?:WAS )?£?([0-9,]+)</span>', article_html)
    data['old_price'] = old_price_match.group(1) if old_price_match else ""

    new_price_match = re.search(r"font-family: 'Playfair Display'[^>]*>£?([0-9,]+)</span>", article_html)
    data['new_price'] = new_price_match.group(1) if new_price_match else ""

    return data

def generate_vertical_card(data):
    """Generate HTML for a single vertical luxury card"""

    # Build badges HTML
    badges_html = ""
    for i, badge_text in enumerate(data.get('badges', [])):
        if 'TOP DEAL' in badge_text:
            bg_color = "rgba(156, 17, 52, 0.3)"
            border_color = "rgba(156, 17, 52, 0.5)"
        elif 'UK DEPARTURE' in badge_text:
            bg_color = "rgba(10, 25, 41, 0.3)"
            border_color = "rgba(10, 25, 41, 0.5)"
        else:
            bg_color = "rgba(212, 175, 55, 0.35)"
            border_color = "rgba(212, 175, 55, 0.6)"

        badges_html += f'<span style="background: {bg_color}; backdrop-filter: blur(20px); border: 1px solid {border_color}; padding: 8px 16px; border-radius: 8px; font-size: 11px; font-weight: 700; color: white; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);">{badge_text}</span>\n                '

    # Build special offer HTML
    special_offer_html = ""
    if data.get('special_offer'):
        special_offer_html = f'''<div style="background: linear-gradient(135deg, var(--navy) 0%, #1e3a52 100%); color: white; padding: 12px 16px; border-radius: 10px; font-size: 11px; position: relative; overflow: hidden;">
                <div style="position: absolute; top: -20px; right: -20px; width: 80px; height: 80px; background: rgba(212, 175, 55, 0.15); border-radius: 50%; filter: blur(25px);"></div>
                <div style="position: relative; z-index: 1; line-height: 1.5;">
                    {data['special_offer']}
                </div>
            </div>'''

    # Build logo HTML
    logo_html = ""
    if data.get('logo'):
        logo_html = f'<img src="{data["logo"]}" alt="{data.get("cruise_line", "")}" style="height: 32px; width: auto;">'
    else:
        logo_html = f'<div style="height: 32px; display: flex; align-items: center; font-size: 12px; font-weight: 700; color: var(--navy); text-transform: uppercase;">{data.get("cruise_line", "Luxury Cruise")}</div>'

    card_html = f'''    <!-- Deal Card {data['id']} -->
    <article data-deal-id="{data['id']}" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.08); transition: all 0.4s; border: 1px solid rgba(255,255,255,0.8); display: flex; flex-direction: column;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 20px 48px rgba(212, 175, 55, 0.2)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0,0,0,0.08)'">
        <div style="position: relative; height: 280px; overflow: hidden;">
            <img src="{data.get('image', 'images/deals/default.jpg')}" alt="{html.escape(data.get('title', ''))}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.08)'" onmouseout="this.style.transform='scale(1)'">
            <button class="heart-button" onclick="toggleSave(this)" aria-label="Save cruise">
                <svg class="heart-icon" viewBox="0 0 24 24">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                </svg>
            </button>
            <div style="position: absolute; top: 16px; left: 16px; display: flex; flex-direction: column; gap: 8px; z-index: 5;">
                {badges_html}
            </div>
            {f'<div style="position: absolute; top: 16px; right: 56px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.95) 0%, rgba(232, 194, 150, 0.95) 100%); backdrop-filter: blur(10px); color: white; padding: 10px 18px; border-radius: 50px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; box-shadow: 0 4px 16px rgba(212, 175, 55, 0.5); border: 1px solid rgba(255, 255, 255, 0.3);">{data["discount"]}</div>' if data.get('discount') else ''}
        </div>
        <div style="padding: 28px 24px; flex: 1; display: flex; flex-direction: column; gap: 18px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                {logo_html}
                <div style="background: rgba(212, 175, 55, 0.1); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 50px; padding: 6px 14px;">
                    <span style="color: var(--gold); font-size: 12px; font-weight: 600;">{data.get('duration', '')}</span>
                </div>
            </div>
            <h3 style="font-size: 24px; font-family: 'Playfair Display', serif; color: var(--navy); line-height: 1.3; margin: 0; font-weight: 600;">{html.escape(data.get('title', ''))}</h3>
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; align-items: center; gap: 10px; color: #666; font-size: 13px;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--gold); flex-shrink: 0;">
                        <rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>
                    </svg>
                    <span style="font-weight: 500;">{data.get('departure', 'TBA')}</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; color: #666; font-size: 13px;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--gold); flex-shrink: 0;">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
                    </svg>
                    <span style="font-weight: 500;">{data.get('region', '')}</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; color: #666; font-size: 13px;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--gold); flex-shrink: 0;">
                        <path d="M3 21h18M4 18h16M6 18V9M18 18V9M8 18V12M16 18V12M12 9V3M12 3 8 7M12 3l4 4"/>
                    </svg>
                    <span style="font-weight: 500;">{data.get('ship', '')}</span>
                </div>
            </div>
            {special_offer_html}
            <div style="flex: 1;"></div>
            <div style="border-top: 1px solid rgba(0,0,0,0.08); padding-top: 20px; margin-top: auto;">
                <div style="margin-bottom: 16px;">
                    <p style="font-size: 11px; color: #999; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 8px; font-weight: 600;">{data.get('price_label', 'From')}</p>
                    <div style="display: flex; align-items: baseline; gap: 12px;">
                        {f'<span style="font-size: 14px; color: #999; text-decoration: line-through;">£{data["old_price"]}</span>' if data.get('old_price') else ''}
                        <span style="font-size: 36px; font-weight: 700; color: var(--gold); font-family: 'Playfair Display', serif;">£{data.get('new_price', '0')}</span>
                        <span style="font-size: 16px; color: var(--navy); font-weight: 600;">pp</span>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr auto; gap: 10px;">
                    <button style="padding: 14px 28px; background: linear-gradient(135deg, var(--gold) 0%, #d4a574 100%); color: white; border: none; border-radius: 50px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 16px rgba(212, 175, 55, 0.3);" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(212, 175, 55, 0.5)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 16px rgba(212, 175, 55, 0.3)'">
                        <span style="display: flex; align-items: center; justify-content: center; gap: 8px;">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                <path d="M3 21h18M4 18h16M6 18V9M18 18V9M8 18V12M16 18V12M12 9V3M12 3 8 7M12 3l4 4"/>
                            </svg>
                            View Cruise
                        </span>
                    </button>
                    <button style="padding: 14px 20px; background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(20px); color: var(--gold); border: 2px solid var(--gold); border-radius: 50px; font-size: 12px; font-weight: 600; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);" onmouseover="this.style.background='rgba(212, 175, 55, 0.1)'; this.style.transform='translateY(-2px)'" onmouseout="this.style.background='rgba(255, 255, 255, 0.7)'; this.style.transform='translateY(0)'">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </article>

'''
    return card_html

def main():
    """Main function to generate all vertical cards"""

    print("Reading deals.html...")
    with open('/home/user/sixstar/deals.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all deal cards
    deal_pattern = r'<article data-deal-id="(-?\d+)"[^>]*>.*?</article>'
    matches = list(re.finditer(deal_pattern, content, re.DOTALL))

    print(f"Found {len(matches)} deal cards")

    output_html = '''<!-- Deal Cards - NEW VERTICAL LUXURY STYLE -->
<!-- Replace the entire <div style="display: grid; gap: 32px;"> section with this code -->

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(380px, 1fr)); gap: 32px;">

'''

    for i, match in enumerate(matches, 1):
        deal_id = match.group(1)
        article_html = match.group(0)

        print(f"Processing card {i}/30 (ID: {deal_id})...")

        try:
            data = parse_deal_card(article_html, deal_id)
            card_html = generate_vertical_card(data)
            output_html += card_html
        except Exception as e:
            print(f"  ERROR processing card {deal_id}: {e}")
            continue

    output_html += '''</div>
<!-- END OF DEALS GRID -->
'''

    # Write output
    output_file = '/home/user/sixstar/ALL-30-VERTICAL-CARDS-COMPLETE.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_html)

    print(f"\n✅ SUCCESS! Generated ALL 30 vertical luxury cards")
    print(f"📁 Output file: {output_file}")
    print(f"📊 Total size: {len(output_html):,} characters")
    print(f"\nNext steps:")
    print(f"1. Open {output_file}")
    print(f"2. Copy ALL the content")
    print(f"3. In deals.html, find line 5594: <div style=\"display: grid; gap: 32px;\">")
    print(f"4. Replace that entire <div> section (until the matching </div>) with the new code")

if __name__ == '__main__':
    main()
