#!/usr/bin/env python3
"""
Generate a comprehensive summary of all cards in deals.html
"""

import re

def read_file(filepath: str) -> str:
    """Read the entire file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def analyze_cards(content: str) -> dict:
    """Analyze all cards and generate summary."""
    articles = re.findall(r'<article\s+data-deal-id="[^"]*".*?</article>', content, re.DOTALL)

    cards = []
    for i, article in enumerate(articles, 1):
        card_info = {'number': i}

        # Get title
        title_match = re.search(r'<h3[^>]*>(.*?)</h3>', article, re.DOTALL)
        if title_match:
            card_info['title'] = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        else:
            card_info['title'] = 'Unknown'

        # Check for pricing section
        has_pricing = 'padding: 24px 0; border-top: 1px solid rgba(10,25,41,0.08)' in article
        card_info['has_pricing'] = has_pricing

        # Extract pricing if available
        if has_pricing:
            price_match = re.search(r'<span[^>]*>£(\d+)</span>\s*<span[^>]*>£(\d+)</span>', article)
            if price_match:
                card_info['old_price'] = price_match.group(1)
                card_info['new_price'] = price_match.group(2)

            discount_match = re.search(r'(-\d+%\s*OFF)', article)
            if discount_match:
                card_info['discount'] = discount_match.group(1)

        # Check for CTA buttons
        has_view_cruise = 'View Cruise' in article
        has_inquire = 'Inquire' in article
        card_info['has_cta'] = has_view_cruise and has_inquire

        # Check for glassmorphic overlay (should be none)
        has_glassmorphic = 'backdrop-filter: blur(40px)' in article and 'position: absolute; bottom:' in article
        card_info['has_glassmorphic'] = has_glassmorphic

        cards.append(card_info)

    return cards

def print_summary(cards: list):
    """Print a formatted summary."""
    print("="*80)
    print("DEALS.HTML COMPREHENSIVE SUMMARY")
    print("="*80)

    print(f"\nTotal Cards: {len(cards)}")
    print(f"Cards with Pricing: {sum(1 for c in cards if c.get('has_pricing'))}")
    print(f"Cards with CTA Buttons: {sum(1 for c in cards if c.get('has_cta'))}")
    print(f"Cards with Glassmorphic Overlays: {sum(1 for c in cards if c.get('has_glassmorphic'))}")

    print("\n" + "="*80)
    print("DETAILED CARD LISTING")
    print("="*80)

    for card in cards:
        print(f"\n{card['number']}. {card['title']}")
        print(f"   Pricing: {'✓' if card.get('has_pricing') else '✗'}", end="")
        if card.get('old_price') and card.get('new_price'):
            print(f" (£{card['old_price']} -> £{card['new_price']}, {card.get('discount', 'N/A')})")
        else:
            print()
        print(f"   CTA Buttons: {'✓' if card.get('has_cta') else '✗'}")
        print(f"   Glassmorphic Overlay: {'✗ (removed)' if not card.get('has_glassmorphic') else '✓ (ERROR: still present)'}")

    print("\n" + "="*80)
    print("VERIFICATION CHECKLIST")
    print("="*80)

    all_have_pricing = all(c.get('has_pricing') for c in cards)
    all_have_cta = all(c.get('has_cta') for c in cards)
    none_have_glassmorphic = not any(c.get('has_glassmorphic') for c in cards)

    print(f"✓ All cards have pricing sections: {all_have_pricing}")
    print(f"✓ All cards have CTA buttons: {all_have_cta}")
    print(f"✓ All glassmorphic overlays removed: {none_have_glassmorphic}")
    print(f"✓ Pricing moved from image to content: {all_have_pricing and none_have_glassmorphic}")

    if all_have_pricing and all_have_cta and none_have_glassmorphic:
        print("\n🎉 SUCCESS: All cards are properly structured!")
    else:
        print("\n⚠️  WARNING: Some issues remain")

def main():
    filepath = '/mnt/d/Websites/travel/deals.html'
    content = read_file(filepath)
    cards = analyze_cards(content)
    print_summary(cards)

if __name__ == '__main__':
    main()
