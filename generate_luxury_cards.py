#!/usr/bin/env python3
"""
Ultra-Luxury Deal Cards Generator
Based on premium hospitality website design principles
"""

import re
import html

def extract_deal_data(article_html, deal_id):
    """Extract all deal information from HTML"""
    data = {'id': deal_id}

    # Extract image
    img_match = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]*)"', article_html)
    if img_match:
        data['image'] = img_match.group(1)
        data['title'] = html.unescape(img_match.group(2))
    else:
        data['image'] = 'images/deals/default.jpg'
        data['title'] = 'Luxury Cruise'

    # Check for TOP DEAL badge
    data['is_top_deal'] = 'TOP DEAL' in article_html

    # Extract save amount
    save_match = re.search(r'Save £([0-9,]+)', article_html)
    data['savings'] = f"Save £{save_match.group(1)}" if save_match else ""

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
    data['duration'] = duration_match.group(1) if duration_match else "7 Nights"

    # Extract departure date
    departure_match = re.search(r'Departure</div>\s*<div[^>]*>([^<]+)</div>', article_html)
    if departure_match:
        data['departure'] = departure_match.group(1).strip()
    else:
        data['departure'] = "TBA"

    # Extract ship and region
    ship_match = re.search(r'Ship</div>\s*<div[^>]*>([^<]+)</div>', article_html)
    data['ship'] = ship_match.group(1).strip() if ship_match else ""

    region_match = re.search(r'Region</div>\s*<div[^>]*>([^<]+)</div>', article_html)
    data['region'] = region_match.group(1).strip() if region_match else ""

    # Extract special offer
    offer_match = re.search(r'<i class="fa-solid fa-star"[^>]*>[^<]*</i>\s*<span[^>]*>([^<]+)</span>', article_html)
    if offer_match:
        data['special_offer'] = offer_match.group(1).strip()
    else:
        # Try alternate pattern
        offer_match2 = re.search(r'<i class="fa-solid fa-star"[^>]*>[^<]*</i>\s*([^<]+?)(?:<span|<br|</div>)', article_html)
        data['special_offer'] = offer_match2.group(1).strip() if offer_match2 else ""

    # Extract price label
    price_label_match = re.search(r'<p style="font-size: 11px;[^>]*>([^<]+)</p>', article_html)
    data['price_label'] = price_label_match.group(1).strip() if price_label_match else "From"

    # Extract prices
    old_price_match = re.search(r'text-decoration: line-through[^>]*>(?:WAS )?£?([0-9,]+)</span>', article_html)
    data['old_price'] = old_price_match.group(1) if old_price_match else ""

    new_price_match = re.search(r"font-family: 'Playfair Display'[^>]*>£?([0-9,]+)</span>", article_html)
    data['new_price'] = new_price_match.group(1) if new_price_match else "0"

    return data

def generate_luxury_card(data):
    """Generate ultra-luxury card HTML"""

    # Badge type
    badge_class = "top-deal" if data.get('is_top_deal') else ""
    badge_text = "Exclusive Offer" if data.get('is_top_deal') else "Special Offer"

    # Logo HTML
    if data.get('logo'):
        logo_html = f'<img src="{data["logo"]}" alt="{html.escape(data.get("cruise_line", ""))}">'
    else:
        logo_html = f'<span style="font-size: 11px; font-weight: 700; color: var(--navy); letter-spacing: 1px;">{html.escape(data.get("cruise_line", "LUXURY CRUISE"))}</span>'

    # Build destination display
    destination = data.get('region', '')
    ship = data.get('ship', '')
    if destination and ship:
        destination_display = f"{destination} • {ship}"
    elif destination:
        destination_display = destination
    elif ship:
        destination_display = ship
    else:
        destination_display = "Worldwide"

    # Special offer HTML
    special_offer_html = ""
    if data.get('special_offer'):
        offer_text = data['special_offer']
        # Clean up the offer text
        offer_text = offer_text.replace('*', '').strip()
        special_offer_html = f'''
            <div class="luxury-offer">
                <span class="luxury-offer-icon">★</span>
                {html.escape(offer_text)}
            </div>'''

    # Old price HTML
    old_price_html = f'<span class="luxury-price-old">£{data["old_price"]}</span>' if data.get('old_price') else ''

    # Savings badge HTML
    savings_html = f'<div class="luxury-savings">{data["savings"]}</div>' if data.get('savings') else ''

    card_html = f'''    <!-- Luxury Deal Card {data['id']} -->
    <article class="luxury-deal-card" data-deal-id="{data['id']}">
        <div class="luxury-image-container">
            <img src="{data.get('image', 'images/deals/default.jpg')}" alt="{html.escape(data.get('title', ''))}">

            <div class="luxury-badge {badge_class}">{badge_text}</div>

            <button class="luxury-heart-btn" onclick="toggleSave(this)" aria-label="Save cruise">
                <svg viewBox="0 0 24 24">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                </svg>
            </button>

            {savings_html}
        </div>

        <div class="luxury-card-body">
            <div class="luxury-header">
                <div class="luxury-logo">
                    {logo_html}
                </div>
                <div class="luxury-duration">{data.get('duration', '7 Nights')}</div>
            </div>

            <h3 class="luxury-title">{html.escape(data.get('title', 'Luxury Cruise Experience'))}</h3>

            <div class="luxury-meta">
                <div class="luxury-meta-item">
                    <svg class="luxury-meta-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <rect x="3" y="4" width="18" height="18" rx="2"/>
                        <line x1="16" y1="2" x2="16" y2="6"/>
                        <line x1="8" y1="2" x2="8" y2="6"/>
                        <line x1="3" y1="10" x2="21" y2="10"/>
                    </svg>
                    <span>Departs {data.get('departure', 'TBA')}</span>
                </div>
                <div class="luxury-meta-item">
                    <svg class="luxury-meta-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                        <circle cx="12" cy="10" r="3"/>
                    </svg>
                    <span>{destination_display}</span>
                </div>
            </div>
            {special_offer_html}

            <div style="flex: 1;"></div>

            <div class="luxury-price-section">
                <div class="luxury-price-label">{data.get('price_label', 'From')}</div>
                <div class="luxury-price-display">
                    {old_price_html}
                    <span class="luxury-price-current">£{data.get('new_price', '0')}</span>
                    <span class="luxury-price-suffix">pp</span>
                </div>

                <button class="luxury-cta">View Details</button>
            </div>
        </div>
    </article>

'''
    return card_html

def main():
    """Generate all luxury cards"""
    print("🏆 Generating ULTRA-LUXURY Deal Cards...")

    with open('/home/user/sixstar/deals.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all deal cards
    deal_pattern = r'<article data-deal-id="(-?\d+)"[^>]*>.*?</article>'
    matches = list(re.finditer(deal_pattern, content, re.DOTALL))

    print(f"📊 Found {len(matches)} deal cards\n")

    # Read the luxury card styles
    with open('/home/user/sixstar/LUXURY-CARDS-ULTRA-PREMIUM.html', 'r', encoding='utf-8') as f:
        luxury_template = f.read()

    # Extract styles
    style_match = re.search(r'<style>(.*?)</style>', luxury_template, re.DOTALL)
    styles = style_match.group(1) if style_match else ""

    # Start building output
    output_html = f'''<!-- ULTRA-LUXURY DEAL CARDS -->
<!-- Based on premium hospitality website design principles -->

<style>
{styles}
</style>

<!-- DEALS GRID -->
<div class="luxury-deals-grid">

'''

    for i, match in enumerate(matches, 1):
        deal_id = match.group(1)
        article_html = match.group(0)

        print(f"✨ Processing card {i}/30 (ID: {deal_id})...")

        try:
            data = extract_deal_data(article_html, deal_id)
            card_html = generate_luxury_card(data)
            output_html += card_html
        except Exception as e:
            print(f"  ⚠️  ERROR processing card {deal_id}: {e}")
            continue

    output_html += '''</div>

<!-- JavaScript for Heart Button -->
<script>
function toggleSave(btn) {
    btn.classList.toggle('saved');
    const card = btn.closest('.luxury-deal-card');
    const dealId = card.getAttribute('data-deal-id');
    // Add your save logic here
    console.log('Toggled save for deal:', dealId);
}
</script>
'''

    # Write output
    output_file = '/home/user/sixstar/ALL-30-LUXURY-CARDS-FINAL.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_html)

    print(f"\n✅ SUCCESS! Generated {len(matches)} ultra-luxury cards")
    print(f"📁 Output: {output_file}")
    print(f"📊 Size: {len(output_html):,} characters")
    print(f"\n🎨 Design features:")
    print(f"   • Large 320px images with smooth zoom")
    print(f"   • Minimal elegant badges")
    print(f"   • Generous white space (40px padding)")
    print(f"   • Refined typography with Cormorant Garamond")
    print(f"   • Soft shadows & smooth transitions")
    print(f"   • Single sophisticated CTA")
    print(f"   • Clean iconography")
    print(f"   • Elegant hover states (8px lift + gold glow)")

if __name__ == '__main__':
    main()
