#!/usr/bin/env python3
"""
Extract card data and generate AI image prompts for each cruise card
"""

import re
import json

with open('/mnt/d/Websites/travel/deals.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all article cards (capture the full article content)
articles = re.findall(r'<article data-deal-id="[^"]+[^>]*>(.*?)</article>', html, re.DOTALL)

print(f"📋 Found {len(articles)} cruise cards\n")
print("=" * 80)

image_prompts = []

for i, article in enumerate(articles, 1):
    # Extract data with better patterns
    title_match = re.search(r'<h3[^>]*>(.*?)</h3>', article, re.DOTALL)
    title = ' '.join(title_match.group(1).split()) if title_match else "Luxury Cruise"

    region_match = re.search(r'Region</div>\s*<div[^>]*>(.*?)</div>', article, re.DOTALL)
    region = ' '.join(region_match.group(1).split()) if region_match else "Mediterranean"

    ship_match = re.search(r'Vessel</div>\s*<div[^>]*>(.*?)</div>', article, re.DOTALL)
    ship = ' '.join(ship_match.group(1).split()) if ship_match else "Luxury Vessel"

    img_match = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]*)"[^>]*style="width: 100%; height: 100%', article)
    current_image = img_match.group(1) if img_match else "N/A"

    # Generate AI prompt based on title and region
    prompt = f"A stunning ultra-luxury cruise destination photograph. {title}. Beautiful {region} scenery with crystal clear waters, elegant coastal architecture, and golden hour lighting. Cinematic composition, professional travel photography, vibrant colors, 8K resolution, photorealistic. Focus on the natural beauty and luxury appeal of the destination."

    image_prompts.append({
        "card_number": i,
        "title": title,
        "region": region,
        "ship": ship,
        "current_image": current_image,
        "ai_prompt": prompt
    })

    print(f"\n🚢 Card {i}: {title}")
    print(f"   Region: {region}")
    print(f"   Ship: {ship}")
    print(f"   Current Image: {current_image}")
    print(f"\n   🎨 AI Image Prompt:")
    print(f"   {prompt}")
    print("-" * 80)

# Save to JSON file
with open('/mnt/d/Websites/travel/image_prompts.json', 'w', encoding='utf-8') as f:
    json.dump(image_prompts, f, indent=2, ensure_ascii=False)

print(f"\n✅ Generated {len(image_prompts)} AI image prompts")
print(f"✅ Saved to: /mnt/d/Websites/travel/image_prompts.json")
