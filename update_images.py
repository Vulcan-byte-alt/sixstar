#!/usr/bin/env python3
"""
Update all card images to use the new cruise-destinations images
"""

import re
import os

# Get list of available images
image_dir = '/mnt/d/Websites/travel/images/cruise-destinations/'
available_images = sorted([f for f in os.listdir(image_dir) if f.endswith('.jpg')])

print(f"📸 Found {len(available_images)} new images")

with open('/mnt/d/Websites/travel/deals.html') as f:
    html = f.read()

# Pattern to find deal card images (the main cruise photo on the left)
# These are the first img tags after "position: relative; overflow: hidden"
pattern = r'(<div style="position: relative; overflow: hidden;">.*?<img src=")([^"]+)(")'

counter = 0
def replace_image(match):
    global counter

    # Skip if this is not a deal image (could be logos, icons, etc.)
    if 'deals/' not in match.group(2):
        return match.group(0)

    # This is a deal card image
    if counter < len(available_images):
        new_image_path = f'images/cruise-destinations/{available_images[counter]}'
        counter += 1
        return match.group(1) + new_image_path + match.group(3)
    else:
        # Keep original if we run out of new images
        return match.group(0)

updated_html = re.sub(pattern, replace_image, html, flags=re.DOTALL)

print(f"✓ Updated {counter} card images")

with open('/mnt/d/Websites/travel/deals.html', 'w') as f:
    f.write(updated_html)

print("\n✅ All card images updated to use cruise-destinations folder!")
