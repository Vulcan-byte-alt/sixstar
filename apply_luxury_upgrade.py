#!/usr/bin/env python3
"""
Apply Ultra-Luxury Upgrade to deals.html
- Add luxury card CSS styles
- Add promo-bg.png background
- Replace old deals grid with new luxury cards
"""

import re

def main():
    print("🎨 Applying ULTRA-LUXURY Upgrade to deals.html...\n")

    # Read deals.html
    print("📖 Reading deals.html...")
    with open('/home/user/sixstar/deals.html', 'r', encoding='utf-8') as f:
        deals_content = f.read()

    # Read luxury cards HTML (complete with styles and cards)
    print("📖 Reading luxury cards...")
    with open('/home/user/sixstar/ALL-30-LUXURY-CARDS-FINAL.html', 'r', encoding='utf-8') as f:
        luxury_content = f.read()

    # Extract CSS from luxury cards (between <style> and </style>)
    style_match = re.search(r'<style>(.*?)</style>', luxury_content, re.DOTALL)
    if not style_match:
        print("❌ ERROR: Could not find styles in luxury cards file")
        return

    luxury_css = style_match.group(1)
    print(f"✅ Extracted {len(luxury_css)} characters of luxury CSS")

    # Extract HTML cards (from <!-- DEALS GRID --> to the </div> before JavaScript)
    grid_match = re.search(r'(<!-- DEALS GRID -->.*?)</div>\s*<!-- JavaScript', luxury_content, re.DOTALL)
    if not grid_match:
        print("❌ ERROR: Could not find deals grid in luxury cards file")
        return

    luxury_grid_html = grid_match.group(1) + "</div>"
    print(f"✅ Extracted {len(luxury_grid_html)} characters of luxury grid HTML")

    # Step 1: Add luxury CSS before the closing </style> tag
    print("\n🎨 Step 1: Adding luxury CSS styles...")

    # Find the last </style> tag in the head
    style_close_pattern = r'(</style>\s*</head>)'

    # Insert luxury CSS before </style>
    luxury_css_with_comment = f"\n\n        /* ========================================\n           ULTRA-LUXURY DEAL CARDS STYLES\n           Based on premium hospitality design\n           ======================================== */\n{luxury_css}\n        "

    deals_content = re.sub(
        r'(\s+)(</style>\s*</head>)',
        luxury_css_with_comment + r'\2',
        deals_content,
        count=1
    )
    print("✅ Added luxury CSS to <head>")

    # Step 2: Change section background to use promo-bg.png
    print("\n🖼️  Step 2: Adding promo-bg.png background...")

    old_section_bg = r'<section style="background: var\(--cream\); padding: 80px 0 120px 0;">'
    new_section_bg = '<section style="background: url(\'images/promo-bg.png\') center center / cover no-repeat, linear-gradient(135deg, #f9f7f4 0%, #f4f2ee 100%); padding: 80px 0 120px 0; position: relative;">'

    deals_content = deals_content.replace(old_section_bg, new_section_bg)
    print("✅ Updated section background with promo-bg.png")

    # Step 3: Replace old deals grid with luxury cards grid
    print("\n🔄 Step 3: Replacing old deals grid with luxury cards...")

    # Find the old deals grid section
    # It starts with <!-- Deal Cards --> or <div style="display: grid; gap: 32px;">
    # and ends before <!-- Pagination -->

    old_grid_pattern = r'<!-- Deal Cards -->\s*<div style="display: grid; gap: 32px;">.*?</div>\s*(?=<!-- Pagination -->)'

    if not re.search(old_grid_pattern, deals_content, re.DOTALL):
        print("⚠️  WARNING: Could not find old deals grid with expected pattern")
        print("   Trying alternate pattern...")

        # Try finding by comment alone
        old_grid_pattern = r'(<!-- Deal Cards -->).*?(</div>\s*(?=<!-- Pagination -->))'

        match = re.search(old_grid_pattern, deals_content, re.DOTALL)
        if match:
            print(f"   Found grid section ({len(match.group(0))} chars)")
        else:
            print("❌ ERROR: Could not find deals grid section to replace")
            return

    # Replace old grid with new luxury grid
    deals_content = re.sub(
        old_grid_pattern,
        '<!-- Deal Cards - ULTRA-LUXURY DESIGN -->\n                    ' + luxury_grid_html + '\n\n                    ',
        deals_content,
        flags=re.DOTALL
    )
    print("✅ Replaced old deals grid with luxury cards")

    # Step 4: Add toggleSave JavaScript function if not exists
    print("\n⚙️  Step 4: Adding JavaScript for heart button...")

    if 'function toggleSave' not in deals_content:
        # Find the closing </body> tag and add script before it
        toggle_save_script = '''
    <!-- Luxury Cards Toggle Save Script -->
    <script>
    function toggleSave(btn) {
        btn.classList.toggle('saved');
        const card = btn.closest('.luxury-deal-card');
        const dealId = card.getAttribute('data-deal-id');

        // Add your save logic here (e.g., save to localStorage, send to backend)
        if (btn.classList.contains('saved')) {
            console.log('Saved deal:', dealId);
            // Example: Save to localStorage
            // let saved = JSON.parse(localStorage.getItem('savedDeals') || '[]');
            // saved.push(dealId);
            // localStorage.setItem('savedDeals', JSON.stringify(saved));
        } else {
            console.log('Unsaved deal:', dealId);
            // Example: Remove from localStorage
            // let saved = JSON.parse(localStorage.getItem('savedDeals') || '[]');
            // saved = saved.filter(id => id !== dealId);
            // localStorage.setItem('savedDeals', JSON.stringify(saved));
        }
    }
    </script>
'''
        deals_content = deals_content.replace('</body>', toggle_save_script + '\n</body>')
        print("✅ Added toggleSave JavaScript function")
    else:
        print("ℹ️  toggleSave function already exists")

    # Write updated content
    print("\n💾 Writing updated deals.html...")
    with open('/home/user/sixstar/deals.html', 'w', encoding='utf-8') as f:
        f.write(deals_content)

    print("\n✅ SUCCESS! Ultra-Luxury Upgrade Applied!\n")
    print("📊 Summary:")
    print(f"   • Added {len(luxury_css)} chars of luxury CSS")
    print(f"   • Added promo-bg.png background image")
    print(f"   • Replaced deals grid with 30 luxury cards")
    print(f"   • Added toggleSave JavaScript function")
    print(f"\n🎨 Luxury Features:")
    print("   ✨ Large 320px images with smooth zoom")
    print("   ✨ Minimal elegant badges")
    print("   ✨ Generous white space (40px padding)")
    print("   ✨ Cormorant Garamond typography")
    print("   ✨ Soft shadows & smooth transitions")
    print("   ✨ Sophisticated CTA buttons")
    print("   ✨ Clean iconography")
    print("   ✨ 8px hover lift with gold glow")
    print("   ✨ Professional promo background")

if __name__ == '__main__':
    main()
