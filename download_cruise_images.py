#!/usr/bin/env python3
"""
Download appropriate images for all 30 cruise deals
Using Picsum Photos as high-quality placeholders
"""

import subprocess
import re
import os
import hashlib

# Mapping of cruise titles to search keywords for images
cruise_image_mapping = {
    "A Journey to Adriatic Wonders & Whispered Ancient Secrets": ("adriatic-coast", "croatia-dubrovnik"),
    "Baltic Sea & Beyond": ("stockholm-sweden", "baltic-sea"),
    "Spring In The Aegean": ("santorini-greece", "aegean-sea"),
    "South Africa, Namibia & Cape Verde Cruise: Cape Town, Walvis Bay & Saint Helena": ("cape-town-south-africa", "table-mountain"),
    "7-Day Jewels Of The Dalmatian Coast": ("dubrovnik-croatia", "adriatic-coast"),
    "Fort Lauderdale to Bridgetown": ("caribbean-beach", "barbados"),
    "A Grand Journey from Barcelona to Miami": ("barcelona-spain", "mediterranean-coast"),
    "A Grand Journey from Andalusian Shores to Coral-Laden Lagoons": ("andalusia-spain", "caribbean-reef"),
    "Cairns to Darwin": ("great-barrier-reef", "australia-coast"),
    "A Journey from Cliffs to Cathedrals": ("amalfi-coast-italy", "mediterranean"),
    "Colorful East Coast": ("new-england-coast", "coastal-town"),
    "Greek Odyssey": ("greek-islands", "mykonos"),
    "10-Day Mediterranean Overture": ("mediterranean-sea", "cruise-ship"),
    "Athens to Civitavecchia": ("athens-acropolis", "rome-italy"),
    "Discover Mediterranean Wonders": ("mediterranean-coast", "azure-water"),
    "Historical echoes, a voyage from Larnaca to Athens": ("cyprus-coast", "greek-ruins"),
    "12-Day Amazon Delta & Coast Of Brazil": ("amazon-river", "brazil-coast"),
    "Greece, Italy & France Cruise: Athens, Amalfi Coast & Nice": ("greek-islands", "amalfi-coast"),
    "Chilean Fjords & Scenic Shores": ("patagonia-chile", "fjords"),
    "New York City Round Trip": ("new-york-skyline", "statue-liberty"),
    "13 Night Italy & Bermuda Transatlantic": ("bermuda-beach", "pink-sand"),
    "Monte Carlo to Civitavecchia": ("monaco-harbor", "mediterranean-yacht"),
    "Spotlight With Ancestry": ("european-coast", "historic-port"),
    "Grand Continental Sojourn": ("european-capitals", "scenic-coast"),
    "A Toast To West Africa": ("west-africa-coast", "african-sunset"),
    "Athens to Athens": ("athens-greece", "parthenon"),
    "King George Island to King George Island": ("antarctica", "glaciers"),
    "Athens to Civitavecchia": ("athens-greece", "rome-italy"),
    "Bangkok, Bali & Beyond": ("bali-indonesia", "thai-temple"),
    "7 Night Tortola, San Juan & Puerto Plata": ("caribbean-island", "turquoise-water")
}

# Picsum Photos (reliable placeholder images)
def get_image_url(keyword, width=1200, height=800, image_id=None):
    """Generate Picsum URL for placeholder images"""
    # Use different image IDs for variety
    if image_id is None:
        import hashlib
        # Generate consistent ID from keyword
        hash_val = int(hashlib.md5(keyword.encode()).hexdigest()[:8], 16)
        image_id = (hash_val % 900) + 100  # IDs between 100-999

    return f"https://picsum.photos/id/{image_id}/{width}/{height}"

def download_image(url, filename):
    """Download image using curl with proper redirect handling"""
    try:
        # Use wget which handles Unsplash redirects better
        result = subprocess.run(
            ['wget', '-q', '-O', filename, url, '--user-agent=Mozilla/5.0'],
            capture_output=True,
            timeout=30
        )
        # Check if file is actually an image (>10KB)
        if os.path.exists(filename) and os.path.getsize(filename) > 10000:
            return True
        else:
            # If too small, it's probably an error page
            if os.path.exists(filename):
                os.remove(filename)
            return False
    except Exception as e:
        print(f"  ✗ Error downloading: {e}")
        return False

if __name__ == "__main__":
    output_dir = "/mnt/d/Websites/travel/images/cruise-destinations"

    print("🖼️  Downloading cruise destination images...")
    print(f"📁 Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0

    for i, (title, keywords) in enumerate(cruise_image_mapping.items(), 1):
        # Create safe filename from title
        safe_name = re.sub(r'[^a-z0-9]+', '-', title.lower())
        safe_name = safe_name.strip('-')[:50]  # Limit length
        filename = f"{output_dir}/cruise-{i:02d}-{safe_name}.jpg"

        # Use first keyword for download
        keyword = keywords[0] if isinstance(keywords, tuple) else keywords
        url = get_image_url(keyword, 1200, 800)

        print(f"{i:2d}. {title[:50]}...")
        print(f"    Keyword: {keyword}")

        if download_image(url, filename):
            print(f"    ✓ Saved: cruise-{i:02d}-{safe_name}.jpg")
            successful += 1
        else:
            print(f"    ✗ Failed to download")
            failed += 1

        print()

    print(f"\n✅ Complete! {successful} images downloaded, {failed} failed")
    print(f"\n📂 Images saved to: {output_dir}/")
