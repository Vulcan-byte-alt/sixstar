#!/usr/bin/env python3
"""
Force apply Opulent Classic to ALL cards by processing each article individually
"""

import re

with open('/mnt/d/Websites/travel/deals.html') as f:
    html_content = f.read()

print("🔧 Force applying Opulent Classic to ALL cards...")

# Find all articles with data-deal-id
articles = list(re.finditer(r'(<article[^>]*data-deal-id="[^"]*"[^>]*>)(.*?)(</article>)', html_content, re.DOTALL))

print(f"Found {len(articles)} deal cards")

replacements = []

for i, match in enumerate(articles, 1):
    article_tag = match.group(1)
    content = match.group(2)
    closing_tag = match.group(3)

    # Check if already has Opulent
    if '<!-- Opulent Classic Luxury -->' in content:
        print(f"  Card {i}: Already has Opulent Classic ✓")
        continue

    print(f"  Card {i}: Applying Opulent Classic...")

    # Extract all needed data
    title_match = re.search(r'<h[23][^>]*>([^<]+)</h[23]>', content)
    title = title_match.group(1).strip() if title_match else "Luxury Cruise"

    duration_match = re.search(r'>(\d+)\s*Nights?<', content)
    duration = duration_match.group(1) if duration_match else "7"

    # Departure
    departure_match = re.search(r'>(\d+\s+[A-Za-z]+\s+\d{4})<', content)
    if departure_match:
        parts = departure_match.group(1).split()
        departure = f"{parts[1]} {parts[2]}" if len(parts) >= 3 else departure_match.group(1)
    else:
        year_match = re.search(r'>(\d{4})<', content)
        departure = year_match.group(1) if year_match else "2026"

    # Ship and Region
    combined_match = re.search(r'<span>([^•<]+)•([^<]+)</span>', content)
    if combined_match:
        region = combined_match.group(1).strip()
        ship = combined_match.group(2).strip()
    else:
        ship_match = re.search(r'Ship</div>.*?<div[^>]*>([^<]+)</div>', content, re.DOTALL)
        ship = ' '.join(ship_match.group(1).split()) if ship_match else "Luxury Vessel"

        region_match = re.search(r'Region</div>.*?<div[^>]*>([^<]+)</div>', content, re.DOTALL)
        region = ' '.join(region_match.group(1).split()) if region_match else "Worldwide"

    # Logo
    logo_match = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]+)"', content)
    if logo_match:
        logo_src = logo_match.group(1)
        logo_alt = logo_match.group(2)
    else:
        logo_src = "images/deals/default-logo.png"
        logo_alt = "Cruise Line"

    # Extract image section (left side)
    image_section_match = re.search(r'(<div style="position: relative; overflow: hidden;">.*?</div>\s*</div>)', content, re.DOTALL)
    image_section = image_section_match.group(1) if image_section_match else ""

    # Build the new Opulent Classic content
    new_content_section = f'''{image_section}

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
                                        <div style="display: flex; gap: 4px; margin-top: 12px;">
                                            <div style="width: 50px; height: 2px; background: linear-gradient(90deg, #d4af37, transparent);"></div>
                                            <div style="width: 25px; height: 2px; background: linear-gradient(90deg, #d4af37, transparent); opacity: 0.5;"></div>
                                        </div>
                                    </div>
                                    <div style="position: relative; padding: 16px 28px; background: linear-gradient(135deg, rgba(212, 175, 55, 0.15), rgba(212, 175, 55, 0.05)); border: 2px solid rgba(212, 175, 55, 0.3); border-radius: 8px; box-shadow: inset 0 1px 2px rgba(255,255,255,0.5), 0 4px 12px rgba(212, 175, 55, 0.1);">
                                        <div style="text-align: center;">
                                            <div style="color: #d4af37; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.5px; margin-bottom: 6px; font-family: 'Inter', sans-serif;">Duration</div>
                                            <div style="color: #1a2332; font-size: 22px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{duration} Nights</div>
                                        </div>
                                    </div>
                                </div>

                                <div style="border-left: 3px solid rgba(212, 175, 55, 0.4); padding-left: 26px; margin-bottom: 38px; position: relative; z-index: 1;">
                                    <div style="position: absolute; left: -7px; top: 0; width: 10px; height: 10px; background: #d4af37; border-radius: 50%; box-shadow: 0 0 12px rgba(212, 175, 55, 0.5);"></div>
                                    <h3 style="font-size: 34px; font-family: 'TheSeasons', serif; color: #1a2332; line-height: 1.35; font-weight: 400; margin-bottom: 28px; letter-spacing: 0.6px;">{title}</h3>

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

                                <div style="display: flex; gap: 14px; position: relative; z-index: 1;">
                                    <button onmouseover="this.style.background='linear-gradient(135deg, #c9a961, #d4af37)'; this.style.boxShadow='0 8px 24px rgba(212, 175, 55, 0.35)'; this.style.transform='translateY(-2px)'" onmouseout="this.style.background='linear-gradient(135deg, #1a2332, #2a3442)'; this.style.boxShadow='0 4px 16px rgba(26, 35, 50, 0.25)'; this.style.transform='translateY(0)'" style="flex: 1; padding: 20px 36px; background: linear-gradient(135deg, #1a2332, #2a3442); color: white; border: none; border-radius: 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s; box-shadow: 0 4px 16px rgba(26, 35, 50, 0.25); font-family: 'Inter', sans-serif;">View Details</button>
                                    <button onmouseover="this.style.background='rgba(212, 175, 55, 0.15)'; this.style.borderColor='#d4af37'; this.style.transform='translateY(-2px)'" onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(26, 35, 50, 0.2)'; this.style.transform='translateY(0)'" style="padding: 20px 32px; background: transparent; color: #1a2332; border: 2px solid rgba(26, 35, 50, 0.2); border-radius: 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2.8px; cursor: pointer; transition: all 0.35s; font-family: 'Inter', sans-serif;">Inquire</button>
                                </div>

                                <div class="expand-on-hover" style="display: grid; grid-template-rows: 0fr; opacity: 0; transition: grid-template-rows 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s; position: relative; z-index: 1;">
                                    <div style="overflow: hidden;">
                                        <div style="display: flex; justify-content: center; gap: 28px; padding-top: 24px; margin-top: 20px; border-top: 1px solid rgba(212, 175, 55, 0.2);">
                                            <button onmouseover="this.style.color='#d4af37'" onmouseout="this.style.color='#888'" style="background: none; border: none; color: #888; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0; font-family: 'Inter', sans-serif;">Request Callback</button>
                                            <button onmouseover="this.style.color='#d4af37'" onmouseout="this.style.color='#888'" style="background: none; border: none; color: #888; font-size: 10px; font-weight: 500; cursor: pointer; transition: color 0.25s; text-transform: uppercase; letter-spacing: 1.5px; padding: 0; font-family: 'Inter', sans-serif;">Download Brochure</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        {closing_tag}'''

    # Store the replacement
    replacements.append((match.group(0), new_content_section))

# Apply all replacements
for old, new in replacements:
    html_content = html_content.replace(old, new, 1)

# Save
with open('/mnt/d/Websites/travel/deals.html', 'w') as f:
    f.write(html_content)

print(f"\n✅ Applied Opulent Classic to {len(replacements)} cards!")
print(f"✅ Total cards with Opulent Classic: {html_content.count('<!-- Opulent Classic Luxury -->')}")
