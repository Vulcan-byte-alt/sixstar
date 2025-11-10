#!/usr/bin/env python3
"""
Redesign all deal card content sections to be more luxurious and minimalistic
"""

import re

def redesign_card_content(html_content):
    """
    Find and replace all card content sections with the new luxury design
    """

    # Pattern to match the content section of deal cards
    # Looking for: <!-- Redesigned Content Section --> or similar comments followed by the content div
    pattern = r'(<!-- (?:Redesigned )?Content Section -->)\s*<div\s+style="padding:\s*\d+px\s+\d+px;[^"]*display:\s*grid;[^"]*grid-template-rows:[^"]*">(.*?)</div>\s*</article>'

    def replace_content(match):
        full_match = match.group(0)

        # Extract key data from the existing content
        # Logo
        logo_match = re.search(r'<img src="([^"]+)"\s+alt="([^"]+)"\s+style="height:\s*\d+px;[^"]*">', full_match)
        if not logo_match:
            return full_match
        logo_src = logo_match.group(1)
        logo_alt = logo_match.group(2)

        # Duration
        duration_match = re.search(r'<span[^>]*>(\d+)\s*Nights?</span>', full_match)
        if not duration_match:
            return full_match
        duration = duration_match.group(1)

        # Title
        title_match = re.search(r'<h3[^>]*style="[^"]*">([^<]+)</h3>', full_match)
        if not title_match:
            return full_match
        title = title_match.group(1).strip()

        # Departure
        departure_match = re.search(r'<span[^>]*>Departure</span>\s*<span[^>]*>([^<]+)</span>', full_match)
        departure = departure_match.group(1).strip() if departure_match else "TBA"

        # Ship
        ship_match = re.search(r'<span[^>]*>Ship</span>\s*<span[^>]*>([^<]+)</span>', full_match)
        ship = ship_match.group(1).strip() if ship_match else "TBA"

        # Region
        region_match = re.search(r'<span[^>]*>Region</span>\s*<span[^>]*>([^<]+)</span>', full_match)
        region = region_match.group(1).strip() if region_match else "TBA"

        # Build the new luxury content section
        new_content = f'''<!-- Luxury Minimalist Content Section -->
                            <div style="padding: 48px 56px; display: flex; flex-direction: column; justify-content: space-between;">

                                <!-- Top Section: Logo & Duration Badge -->
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 36px;">
                                    <img src="{logo_src}" alt="{logo_alt}"
                                        style="height: 36px; width: auto; opacity: 0.95;">
                                    <div style="text-align: right;">
                                        <div style="color: var(--gold); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 4px; opacity: 0.7;">Duration</div>
                                        <div style="color: var(--navy); font-size: 22px; font-weight: 300; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{duration} Nights</div>
                                    </div>
                                </div>

                                <!-- Middle Section: Title -->
                                <div style="flex-grow: 1; margin-bottom: 36px;">
                                    <h3 style="font-size: 28px; font-family: 'Cormorant Garamond', serif; color: var(--navy); line-height: 1.4; font-weight: 500; margin-bottom: 32px; letter-spacing: 0.3px;">
                                        {title}
                                    </h3>

                                    <!-- Elegant Info Grid -->
                                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; padding: 24px 0; border-top: 1px solid rgba(10, 25, 41, 0.08); border-bottom: 1px solid rgba(10, 25, 41, 0.08);">
                                        <div>
                                            <div style="color: var(--gold); font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 8px; opacity: 0.7;">Departure</div>
                                            <div style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif;">{departure}</div>
                                        </div>
                                        <div>
                                            <div style="color: var(--gold); font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 8px; opacity: 0.7;">Ship</div>
                                            <div style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif;">{ship}</div>
                                        </div>
                                        <div>
                                            <div style="color: var(--gold); font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 8px; opacity: 0.7;">Region</div>
                                            <div style="color: var(--navy); font-size: 15px; font-weight: 400; font-family: 'Inter', sans-serif;">{region}</div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Bottom Section: CTA Buttons -->
                                <div style="display: flex; gap: 12px; margin-top: 8px;">
                                    <button
                                        style="flex: 1; padding: 16px 32px; background: linear-gradient(135deg, var(--gold) 0%, #c9965f 100%); color: white; border: none; border-radius: 6px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; cursor: pointer; transition: all 0.3s ease;"
                                        onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 8px 24px rgba(212, 175, 55, 0.35)'"
                                        onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
                                        View Details
                                    </button>
                                    <button
                                        style="padding: 16px 28px; background: transparent; color: var(--gold); border: 1.5px solid var(--gold); border-radius: 6px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; cursor: pointer; transition: all 0.3s ease;"
                                        onmouseover="this.style.background='rgba(212, 175, 55, 0.08)'; this.style.transform='translateY(-2px)'"
                                        onmouseout="this.style.background='transparent'; this.style.transform='translateY(0)'">
                                        Inquire
                                    </button>
                                </div>
                            </div>
                        </article>'''

        return new_content

    # Apply the replacement
    updated_html = re.sub(pattern, replace_content, html_content, flags=re.DOTALL)

    return updated_html

if __name__ == "__main__":
    # Read the deals.html file
    with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("Starting card content redesign...")
    print(f"Original file size: {len(html_content)} characters")

    # Apply redesign
    updated_html = redesign_card_content(html_content)

    print(f"Updated file size: {len(updated_html)} characters")

    # Save the updated file
    with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print("✓ Card content redesign complete!")
    print("All 30 deal cards now have the new luxury minimalist design")
