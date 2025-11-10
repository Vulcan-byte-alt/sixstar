#!/usr/bin/env python3
"""
Redesign all 30 deal cards in deals.html to match the luxury card style from index.html
"""

import re
import sys

def extract_card_info(card_html):
    """Extract departure date, ship name, and region from the Info Grid"""
    info = {
        'departure': '',
        'ship': '',
        'region': ''
    }

    # Extract departure date
    departure_match = re.search(r'Departure</div>\s*<div[^>]*>([^<]+)</div>', card_html)
    if departure_match:
        info['departure'] = departure_match.group(1).strip()

    # Extract ship name
    ship_match = re.search(r'Ship</div>\s*<div[^>]*>([^<]+)</div>', card_html)
    if ship_match:
        info['ship'] = ship_match.group(1).strip()

    # Extract region
    region_match = re.search(r'Region</div>\s*<div[^>]*>([^<]+)</div>', card_html)
    if region_match:
        info['region'] = region_match.group(1).strip()

    return info

def create_vertical_info_section(departure, ship, region):
    """Create the new vertical info layout"""
    return f'''<!-- Vertical Info Layout -->
                                    <div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 32px; color: #666; font-size: 14px; font-family: 'Montserrat', sans-serif; letter-spacing: 0.02em;">
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="color: #999; min-width: 90px;">Departure</span>
                                            <span style="font-weight: 500; color: var(--navy);">{departure}</span>
                                        </div>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="color: #999; min-width: 90px;">Ship</span>
                                            <span style="font-weight: 500; color: var(--navy);">{ship}</span>
                                        </div>
                                        <div style="display: flex; align-items: center; gap: 12px;">
                                            <span style="color: #999; min-width: 90px;">Region</span>
                                            <span style="font-weight: 500; color: var(--navy);">{region}</span>
                                        </div>
                                    </div>'''

def redesign_card(card_html, card_num):
    """Redesign a single card to match luxury style"""

    # Extract info from existing grid
    info = extract_card_info(card_html)

    if not info['departure'] or not info['ship'] or not info['region']:
        print(f"Warning: Card {card_num} - Missing info (Departure: '{info['departure']}', Ship: '{info['ship']}', Region: '{info['region']}')")

    # Remove the Innovative Info Grid (3-column grid)
    # This pattern matches the entire grid structure
    card_html = re.sub(
        r'<!-- Innovative Info Grid -->.*?</div>\s*</div>\s*</div>\s*\n',
        '',
        card_html,
        flags=re.DOTALL
    )

    # Remove Special Offer - Diagonal Accent sections
    card_html = re.sub(
        r'<!-- Special Offer - Diagonal Accent -->.*?</div>\s*</div>\s*\n',
        '',
        card_html,
        flags=re.DOTALL
    )

    # Now find where to insert the new vertical info section
    # It should go right after the </h3> tag and before the CTA buttons

    # Find the title closing tag and insert the vertical info section after it
    title_pattern = r'(</h3>)\s*\n'
    replacement = r'\1\n\n' + create_vertical_info_section(info['departure'], info['ship'], info['region']) + '\n\n'

    card_html = re.sub(title_pattern, replacement, card_html, count=1)

    # Update margin-bottom in title if it exists
    card_html = re.sub(
        r'(<h3[^>]*margin-bottom:\s*)\d+px',
        r'\g<1>28px',
        card_html
    )

    # Ensure Montserrat font is used in info sections (not Playfair Display)
    # The new vertical info already has Montserrat, but let's ensure consistency

    return card_html

def process_deals_file(input_file, output_file):
    """Process the entire deals.html file"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all deal cards
    # Pattern: from <!-- Deal Card N to the next <!-- Deal Card or end of section
    card_pattern = r'(<!-- Deal Card (\d+)[^>]*>)(.*?)(?=<!-- Deal Card|\s*</section>)'

    cards_processed = []

    def replace_card(match):
        card_marker = match.group(1)
        card_num = match.group(2)
        card_content = match.group(3)

        print(f"Processing Card {card_num}...")

        # Redesign the card
        redesigned = redesign_card(card_content, card_num)

        cards_processed.append(card_num)

        return card_marker + redesigned

    # Replace all cards
    new_content = re.sub(card_pattern, replace_card, content, flags=re.DOTALL)

    # Write the output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"\n✓ Successfully redesigned {len(cards_processed)} cards")
    print(f"✓ Cards processed: {', '.join(cards_processed)}")
    print(f"✓ Output written to: {output_file}")

    return len(cards_processed)

if __name__ == '__main__':
    input_file = '/mnt/d/Websites/travel/deals.html'
    output_file = '/mnt/d/Websites/travel/deals.html'

    print("Starting deal cards redesign...")
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print("-" * 60)

    try:
        count = process_deals_file(input_file, output_file)
        print("-" * 60)
        print(f"✓ Complete! Redesigned {count} deal cards.")
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
