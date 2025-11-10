#!/usr/bin/env python3
"""
Fix merged cards by adding missing CTA buttons and pricing sections.
Also ensure proper closing tags.
"""

import re
from typing import List, Tuple

# Pricing data for cards (extracted from Save badges and deal info)
PRICING_DATA = {
    "Colorful East Coast": {"old": "9089", "new": "6219", "discount": "-32% OFF"},
    "Greek Odyssey": {"old": "5600", "new": "4760", "discount": "-15% OFF"},
    "South Africa, Namibia & Cape Verde Cruise": {"old": "7899", "new": "6199", "discount": "-22% OFF"},
    "Fort Lauderdale to Bridgetown": {"old": "5800", "new": "4649", "discount": "-20% OFF"},
    "A Grand Journey from Barcelona to Miami": {"old": "8900", "new": "8450", "discount": "-5% OFF"},
    "A Grand Journey from Andalusian Shores to Coral-La": {"old": "7200", "new": "6899", "discount": "-4% OFF"},
    "Cairns to Darwin": {"old": "5890", "new": "5249", "discount": "-11% OFF"},
    "A Journey from Cliffs to Cathedrals": {"old": "6300", "new": "5799", "discount": "-8% OFF"},
    "10-Day Mediterranean Overture": {"old": "5300", "new": "4823", "discount": "-9% OFF"},
    "Historical echoes, a voyage from Larnaca to Athens": {"old": "4900", "new": "4349", "discount": "-11% OFF"},
    "Greece, Italy & France Cruise": {"old": "6800", "new": "6249", "discount": "-8% OFF"},
    "Chilean Fjords & Scenic Shores": {"old": "8900", "new": "7999", "discount": "-10% OFF"},
    "New York City Round Trip": {"old": "6200", "new": "5649", "discount": "-9% OFF"},
    "Monte Carlo to Civitavecchia": {"old": "5900", "new": "5299", "discount": "-10% OFF"},
    "Spotlight With Ancestry": {"old": "7200", "new": "6599", "discount": "-8% OFF"},
    "Grand Continental Sojourn": {"old": "12900", "new": "11499", "discount": "-11% OFF"},
    "Athens to Athens": {"old": "5200", "new": "4799", "discount": "-8% OFF"},
    "Athens to Civitavecchia": {"old": "5400", "new": "4949", "discount": "-8% OFF"},
    "Bangkok, Bali & Beyond": {"old": "8900", "new": "7999", "discount": "-10% OFF"},
}

CTA_BUTTONS_TEMPLATE = '''
                                <!-- CTA Buttons - Full Width -->
                                <div style="display: grid; grid-template-columns: 1fr auto; gap: 12px;">
                                    <!-- Primary CTA - Golden View Cruise Button -->
                                    <button
                                        style="padding: 16px 32px; background: linear-gradient(135deg, var(--gold) 0%, #d4a574 100%); color: white; border: none; border-radius: 50px; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 4px 16px rgba(212, 175, 55, 0.3); position: relative; overflow: hidden;"
                                        onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(212, 175, 55, 0.5)'; this.style.background='linear-gradient(135deg, #e8c296 0%, var(--gold) 100%)'"
                                        onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 16px rgba(212, 175, 55, 0.3)'; this.style.background='linear-gradient(135deg, var(--gold) 0%, #d4a574 100%)'">
                                        <span
                                            style="position: relative; z-index: 1; display: flex; align-items: center; justify-content: center; gap: 8px;">
                                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2.5">
                                                <path
                                                    d="M3 21h18M4 18h16M6 18V9M18 18V9M8 18V12M16 18V12M12 9V3M12 3 8 7M12 3l4 4" />
                                            </svg>
                                            View Cruise
                                        </span>
                                    </button>

                                    <!-- Secondary CTA - Inquire Button -->
                                    <button
                                        style="padding: 16px 28px; background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); color: var(--gold); border: 2px solid var(--gold); border-radius: 50px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06), inset 0 0 0 1px rgba(212, 175, 55, 0.2);"
                                        onmouseover="this.style.background='rgba(212, 175, 55, 0.1)'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(212, 175, 55, 0.2)'"
                                        onmouseout="this.style.background='rgba(255, 255, 255, 0.7)'; this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 16px rgba(0, 0, 0, 0.06), inset 0 0 0 1px rgba(212, 175, 55, 0.2)'">
                                        <span style="display: flex; align-items: center; gap: 6px;">
                                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2.5">
                                                <path
                                                    d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                                            </svg>
                                            Inquire
                                        </span>
                                    </button>
                                </div>
                            </div>
                        </article>'''

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

def fix_card_missing_cta(content: str, card_title: str, pricing_data: dict) -> str:
    """Fix a specific card that's missing CTA buttons and pricing."""
    # Find the card by title
    title_pattern = rf'<h3[^>]*>\s*{re.escape(card_title)}\s*</h3>'
    title_match = re.search(title_pattern, content, re.IGNORECASE)

    if not title_match:
        print(f"  ⚠️ Could not find card: {card_title}")
        return content

    # Find the end of the vertical info section for this card
    # Look for the closing </div> after the vertical info layout
    search_start = title_match.end()

    # Find the pattern: </div>\n\n (whitespace) </div>
    # This indicates end of info section and end of title/details div
    end_pattern = r'(</div>\s*</div>)\s*(?=</div>|<div\s+style="padding:)'
    end_match = re.search(end_pattern, content[search_start:search_start+3000])

    if not end_match:
        # Try alternative pattern - just end of vertical info
        end_pattern = r'(</div>)\s*</div>\s*(?=</div>|<div\s+style="padding:|<!--)'
        end_match = re.search(end_pattern, content[search_start:search_start+3000])

    if end_match:
        insert_pos = search_start + end_match.end()

        # Create pricing and CTA section
        pricing_html = create_pricing_section(
            pricing_data['old'],
            pricing_data['new'],
            pricing_data['discount']
        )

        # Insert pricing + CTA buttons + closing tags
        insertion = pricing_html + CTA_BUTTONS_TEMPLATE

        content = content[:insert_pos] + '\n' + insertion + '\n' + content[insert_pos:]
        print(f"  ✓ Fixed card: {card_title}")
        return content
    else:
        print(f"  ⚠️ Could not find insertion point for: {card_title}")
        return content

def main():
    filepath = '/mnt/d/Websites/travel/deals.html'

    print("Reading deals.html...")
    content = read_file(filepath)

    print("\nFixing cards missing CTA buttons and pricing...\n")

    # Fix cards in order
    for card_title, pricing_data in PRICING_DATA.items():
        content = fix_card_missing_cta(content, card_title, pricing_data)

    print("\nWriting fixed content...")
    write_file(filepath, content)
    print("✓ Done!")

if __name__ == '__main__':
    main()
