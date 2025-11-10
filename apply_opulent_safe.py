#!/usr/bin/env python3
"""
SAFE Opulent Classic Application
- Preserves article tags and structure
- Only replaces content sections
- Keeps image sections intact
- Maintains proper closing tags
"""

import re

def create_opulent_content(logo_src, logo_alt, duration, title, ship, region, departure):
    """Generate Opulent Classic content section"""
    return f'''<!-- Opulent Classic Luxury -->
                            <div style="padding: 58px 64px 56px; display: flex; flex-direction: column; position: relative; background: linear-gradient(135deg, #faf8f5 0%, #f5f3ee 100%);">

                                <!-- Decorative Gold Double Frame -->
                                <div style="position: absolute; top: 24px; left: 24px; right: 24px; bottom: 24px; border: 1px solid rgba(212, 175, 55, 0.25); pointer-events: none;"></div>
                                <div style="position: absolute; top: 28px; left: 28px; right: 28px; bottom: 28px; border: 1px solid rgba(212, 175, 55, 0.15); pointer-events: none;"></div>

                                <!-- Header with Logo & Duration Badge -->
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 42px; position: relative; z-index: 1;">
                                    <div>
                                        <img src="{logo_src}" alt="{logo_alt}"
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
                                            <div style="color: #1a2332; font-size: 22px; font-weight: 500; font-family: 'Cormorant Garamond', serif; letter-spacing: 0.5px;">{duration} Nights</div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Title with Gold Accent Border -->
                                <div style="border-left: 3px solid rgba(212, 175, 55, 0.4); padding-left: 26px; margin-bottom: 38px; position: relative; z-index: 1;">
                                    <!-- Gold Accent Dot -->
                                    <div style="position: absolute; left: -7px; top: 0; width: 10px; height: 10px; background: #d4af37; border-radius: 50%; box-shadow: 0 0 12px rgba(212, 175, 55, 0.5);"></div>

                                    <h3 style="font-size: 34px; font-family: 'TheSeasons', serif; color: #1a2332; line-height: 1.35; font-weight: 400; margin-bottom: 28px; letter-spacing: 0.6px;">
                                        {title}
                                    </h3>

                                    <!-- Rich Info Box -->
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
                            </div>'''


with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("🔧 Applying Opulent Classic design safely...")

# Pattern to match ONLY the content section (after image div, before closing article)
# This matches from the content comment to the closing div and article
pattern = r'(<!-- (?:Ultra-Luxury Interactive Content Section|True Luxury Minimalist|Opulent Classic Luxury|Rich Luxury|STYLE \d+|Editorial|Structured|Ultra-Refined|Opulent|Redesigned Content Section)[^>]*-->.*?</div>\s*)(</article>)'

def replace_content_section(match):
    """Replace content section while preserving structure"""
    before_content = match.string[:match.start()]
    closing_article = match.group(2)

    # Extract data from the matched section or nearby context
    section = match.group(0)

    # Extract logo
    logo_match = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]+)"', section)
    if logo_match:
        logo_src = logo_match.group(1)
        logo_alt = logo_match.group(2)
    else:
        logo_src = "images/deals/default-logo.png"
        logo_alt = "Cruise Line"

    # Extract title
    title_match = re.search(r'<h3[^>]*>([^<]+)</h3>', section)
    title = title_match.group(1).strip() if title_match else "Luxury Voyage"

    # Extract duration
    duration_match = re.search(r'(\d+)\s*Nights?', section)
    duration = duration_match.group(1) if duration_match else "7"

    # Extract ship
    ship_match = re.search(r'Ship</div>\s*<div[^>]*>([^<]+)</div>', section, re.DOTALL)
    if ship_match:
        ship = ' '.join(ship_match.group(1).split())
    else:
        ship = "Luxury Vessel"

    # Extract region
    region_match = re.search(r'Region</div>\s*<div[^>]*>([^<]+)</div>', section, re.DOTALL)
    if region_match:
        region = ' '.join(region_match.group(1).split())
    else:
        region = "Mediterranean"

    # Extract departure
    departure_match = re.search(r'Departure</div>\s*<div[^>]*>([^<]+)</div>', section, re.DOTALL)
    if departure_match:
        departure = ' '.join(departure_match.group(1).split())
    else:
        # Try to find month and year pattern
        date_match = re.search(r'([A-Z][a-z]+)\s+(\d{4})', section)
        departure = f"{date_match.group(1)} {date_match.group(2)}" if date_match else "2026"

    # Create new content
    new_content = create_opulent_content(logo_src, logo_alt, duration, title, ship, region, departure)

    return new_content + "\n                        " + closing_article


# Apply replacement
updated_html = re.sub(pattern, replace_content_section, html, flags=re.DOTALL)

# Also update the hover effects to use grid animation
updated_html = updated_html.replace(
    "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.maxHeight=el.scrollHeight+'px'; el.style.opacity='1'; el.style.marginTop='24px'})",
    "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='1fr'; el.style.opacity='1'})"
)
updated_html = updated_html.replace(
    "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.maxHeight='0'; el.style.opacity='0'; el.style.marginTop='0'})",
    "this.querySelectorAll('.expand-on-hover').forEach(el => {el.style.gridTemplateRows='0fr'; el.style.opacity='0'})"
)

with open('/mnt/d/Websites/travel/deals.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

# Count results
opulent_count = updated_html.count('<!-- Opulent Classic Luxury -->')
article_count = updated_html.count('<article data-deal-id=')

print(f"✅ Applied Opulent Classic to {opulent_count} cards")
print(f"✅ Total article tags: {article_count}")
print(f"✅ All cards preserved: {'YES' if opulent_count == article_count else 'NO - CHECK FILE'}")
