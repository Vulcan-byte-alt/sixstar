#!/usr/bin/env python3
"""
Restore pricing sections to the 5 cards that lost them.
"""

import re

PRICING_DATA = {
    "Baltic Sea & Beyond": {"old": "7200", "new": "6149", "discount": "-15% OFF"},
    "7-Day Jewels Of The Dalmatian Coast": {"old": "4700", "new": "4092", "discount": "-13% OFF"},
    "Discover Mediterranean Wonders": {"old": "4900", "new": "4299", "discount": "-12% OFF"},
    "12-Day Amazon Delta & Coast Of Brazil": {"old": "6800", "new": "5799", "discount": "-15% OFF"},
    "7 Night Tortola, San Juan & Puerto Plata": {"old": "4800", "new": "4249", "discount": "-11% OFF"},
}

def create_pricing_section(old_price: str, new_price: str, discount: str) -> str:
    """Create the pricing section HTML."""
    return f'''<div style="padding: 24px 0; border-top: 1px solid rgba(10,25,41,0.08); border-bottom: 1px solid rgba(10,25,41,0.08); margin-bottom: 32px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-family: 'Montserrat', sans-serif; font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em; color: #999; margin-bottom: 8px;">From</div>
            <div style="display: flex; align-items: baseline; gap: 12px;">
                <span style="font-family: 'Montserrat', sans-serif; font-size: 16px; color: #999; text-decoration: line-through;">£{old_price}</span>
                <span style="font-family: 'Playfair Display', serif; font-size: 40px; font-weight: 400; color: var(--navy); line-height: 1;">£{new_price}</span>
                <span style="font-family: 'Montserrat', sans-serif; font-size: 16px; color: #666; font-weight: 500;">pp</span>
            </div>
        </div>
        <div style="background: linear-gradient(135deg, var(--gold) 0%, #d4a574 100%); color: white; padding: 8px 20px; border-radius: 50px; font-family: 'Montserrat', sans-serif; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">{discount}</div>
    </div>
</div>

'''

def read_file(filepath: str) -> str:
    """Read the entire file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath: str, content: str):
    """Write content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def clean_broken_pricing_fragments(content: str) -> str:
    """Remove broken pricing fragments."""
    # Remove orphaned discount badges and closing divs
    patterns = [
        r'\s*<div style="background: linear-gradient\(135deg, var\(--gold\) 0%, #d4a574 100%\); color: white; padding: 8px 20px; border-radius: 50px; font-family: \'Montserrat\', sans-serif; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0\.05em;">-\d+% OFF</div>\s*</div>\s*</div>\s*(?=\n<div style="display: grid; grid-template-columns:)',
    ]

    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)

    return content

def add_pricing_before_cta(content: str, card_title: str, pricing_data: dict) -> tuple:
    """Add pricing section before CTA buttons for a specific card."""
    # Find the card by its title
    title_pattern = rf'<h3[^>]*>\s*{re.escape(card_title)}'
    title_match = re.search(title_pattern, content, re.IGNORECASE)

    if not title_match:
        return content, False

    # Find the CTA buttons section after this title
    search_start = title_match.end()
    cta_pattern = r'<div style="display: grid; grid-template-columns: 1fr auto; gap: \d+px;">\s*<!-- Primary CTA'
    cta_match = re.search(cta_pattern, content[search_start:search_start+5000])

    if cta_match:
        insert_pos = search_start + cta_match.start()

        # Create pricing section
        pricing_html = create_pricing_section(
            pricing_data['old'],
            pricing_data['new'],
            pricing_data['discount']
        )

        # Insert pricing before CTA
        content = content[:insert_pos] + pricing_html + content[insert_pos:]
        return content, True

    return content, False

def main():
    filepath = '/mnt/d/Websites/travel/deals.html'

    print("Restoring pricing sections...\n")
    content = read_file(filepath)

    print("1. Cleaning broken pricing fragments...")
    content = clean_broken_pricing_fragments(content)

    print("\n2. Adding pricing sections to cards...")
    added_count = 0
    failed_cards = []

    for card_title, pricing_data in PRICING_DATA.items():
        content, success = add_pricing_before_cta(content, card_title, pricing_data)
        if success:
            added_count += 1
            print(f"  ✓ Added pricing to: {card_title}")
        else:
            failed_cards.append(card_title)
            print(f"  ⚠️  Failed to add pricing to: {card_title}")

    print(f"\n✓ Successfully restored pricing to {added_count} cards")
    if failed_cards:
        print(f"⚠️  Failed cards: {len(failed_cards)}")
        for card in failed_cards:
            print(f"   - {card}")

    print("\n3. Writing file...")
    write_file(filepath, content)
    print("✓ Done!")

if __name__ == '__main__':
    main()
