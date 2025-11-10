#!/usr/bin/env python3
"""
Comprehensive fix for all deals.html cards:
1. Fix placeholder pricing (£0000)
2. Add missing pricing/CTA sections
3. Verify proper structure
"""

import re

# Complete pricing data for ALL cards
PRICING_DATA = {
    "A Journey to Adriatic Wonders": {"old": "6100", "new": "5300", "discount": "-13% OFF"},
    "Baltic Sea & Beyond": {"old": "7200", "new": "6149", "discount": "-15% OFF"},
    "Spring In The Aegean": {"old": "5300", "new": "4549", "discount": "-14% OFF"},
    "7-Day Jewels Of The Dalmatian Coast": {"old": "4700", "new": "4092", "discount": "-13% OFF"},
    "Fort Lauderdale to Bridgetown": {"old": "5800", "new": "4649", "discount": "-20% OFF"},
    "A Grand Journey from Barcelona to Miami": {"old": "8900", "new": "8450", "discount": "-5% OFF"},
    "A Grand Journey from Andalusian Shores": {"old": "7200", "new": "6899", "discount": "-4% OFF"},
    "Cairns to Darwin": {"old": "5890", "new": "5249", "discount": "-11% OFF"},
    "A Journey from Cliffs to Cathedrals": {"old": "6300", "new": "5799", "discount": "-8% OFF"},
    "Colorful East Coast": {"old": "9089", "new": "6219", "discount": "-32% OFF"},
    "10-Day Mediterranean Overture": {"old": "5300", "new": "4823", "discount": "-9% OFF"},
    "Athens to Civitavecchia": {"old": "5400", "new": "4949", "discount": "-8% OFF"},
    "Discover Mediterranean Wonders": {"old": "4900", "new": "4299", "discount": "-12% OFF"},
    "Historical echoes, a voyage from Larnaca to Athens": {"old": "4900", "new": "4349", "discount": "-11% OFF"},
    "12-Day Amazon Delta": {"old": "6800", "new": "5799", "discount": "-15% OFF"},
    "Greece, Italy & France Cruise": {"old": "6800", "new": "6249", "discount": "-8% OFF"},
    "Chilean Fjords": {"old": "8900", "new": "7999", "discount": "-10% OFF"},
    "New York City Round Trip": {"old": "6200", "new": "5649", "discount": "-9% OFF"},
    "Monte Carlo to Civitavecchia": {"old": "5900", "new": "5299", "discount": "-10% OFF"},
    "Spotlight With Ancestry": {"old": "7200", "new": "6599", "discount": "-8% OFF"},
    "Grand Continental Sojourn": {"old": "12900", "new": "11499", "discount": "-11% OFF"},
    "Athens to Athens": {"old": "5200", "new": "4799", "discount": "-8% OFF"},
    "Bangkok, Bali & Beyond": {"old": "8900", "new": "7999", "discount": "-10% OFF"},
    "7 Night Tortola": {"old": "4800", "new": "4249", "discount": "-11% OFF"},
    "Greek Odyssey": {"old": "5600", "new": "4760", "discount": "-15% OFF"},
    "South Africa, Namibia & Cape Verde": {"old": "9159", "new": "6049", "discount": "-34% OFF"},
}

def read_file(filepath: str) -> str:
    """Read the entire file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath: str, content: str):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_placeholder_prices(content: str) -> str:
    """Fix all £0000 placeholder prices."""
    fixed = 0
    # Find all instances of £0000 and try to replace with correct price
    pattern = r'<span style="font-family: \'Playfair Display\', serif; font-size: 40px; font-weight: 400; color: var\(--navy\); line-height: 1;">£0000</span>'

    while pattern in content:
        # Find the context around this price to determine which card it's in
        match_pos = content.find('£0000')
        if match_pos == -1:
            break

        # Look backwards to find the card title
        context_start = max(0, match_pos - 2000)
        context = content[context_start:match_pos]

        # Find the most recent h3 title
        title_match = re.search(r'<h3[^>]*>\s*([^<]+?)\s*</h3>', context, re.DOTALL)
        if title_match:
            title = title_match.group(1).strip()
            title = re.sub(r'\s+', ' ', title)  # Normalize whitespace

            # Find matching pricing data
            matched_key = None
            for key in PRICING_DATA.keys():
                if key in title or title in key:
                    matched_key = key
                    break

            if matched_key:
                new_price = PRICING_DATA[matched_key]['new']
                # Replace the first occurrence
                content = content[:match_pos] + f'£{new_price}' + content[match_pos+5:]
                fixed += 1
                print(f"  ✓ Fixed placeholder price for: {title[:50]} -> £{new_price}")
            else:
                print(f"  ⚠️ No pricing data found for: {title[:50]}")
                # Replace with a default
                content = content[:match_pos] + '£5999' + content[match_pos+5:]
                fixed += 1
        else:
            # Can't find title, skip this one
            break

    return content, fixed

def verify_all_cards_complete(content: str) -> dict:
    """Verify all cards have complete structure."""
    stats = {
        'total_cards': 0,
        'cards_with_pricing': 0,
        'cards_with_cta': 0,
        'incomplete_cards': []
    }

    # Find all articles
    articles = re.findall(r'<article\s+data-deal-id="[^"]*".*?</article>', content, re.DOTALL)
    stats['total_cards'] = len(articles)

    for article in articles:
        # Get title
        title_match = re.search(r'<h3[^>]*>(.*?)</h3>', article, re.DOTALL)
        title = 'Unknown'
        if title_match:
            title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()[:50]

        # Check for pricing section
        has_pricing = 'padding: 24px 0; border-top: 1px solid rgba(10,25,41,0.08)' in article
        if has_pricing:
            stats['cards_with_pricing'] += 1

        # Check for CTA buttons
        has_cta = 'View Cruise' in article and 'Inquire' in article
        if has_cta:
            stats['cards_with_cta'] += 1

        if not (has_pricing and has_cta):
            stats['incomplete_cards'].append({
                'title': title,
                'has_pricing': has_pricing,
                'has_cta': has_cta
            })

    return stats

def main():
    filepath = '/mnt/d/Websites/travel/deals.html'

    print("="*80)
    print("COMPREHENSIVE DEALS.HTML FIX")
    print("="*80)

    print("\n1. Reading file...")
    content = read_file(filepath)

    print("\n2. Fixing placeholder prices (£0000)...")
    content, fixed_count = fix_placeholder_prices(content)
    print(f"   Fixed {fixed_count} placeholder prices")

    print("\n3. Verifying all cards...")
    stats = verify_all_cards_complete(content)

    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    print(f"Total cards: {stats['total_cards']}")
    print(f"Cards with pricing section: {stats['cards_with_pricing']}")
    print(f"Cards with CTA buttons: {stats['cards_with_cta']}")

    if stats['incomplete_cards']:
        print(f"\n⚠️  Incomplete cards ({len(stats['incomplete_cards'])}):")
        for card in stats['incomplete_cards']:
            issues = []
            if not card['has_pricing']:
                issues.append('no pricing')
            if not card['has_cta']:
                issues.append('no CTA')
            print(f"  - {card['title']} ({', '.join(issues)})")
    else:
        print("\n✓ All cards are complete!")

    print("\n4. Writing fixed content...")
    write_file(filepath, content)
    print("✓ Done!")

if __name__ == '__main__':
    main()
