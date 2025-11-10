import os
import re
from google import genai

# =====================================================
#  CONFIGURATION
# =====================================================

# Option A: Use environment variable (recommended)
client = genai.Client()

# Option B: Directly pass your API key (uncomment if needed)
# client = genai.Client(api_key="YOUR_API_KEY_HERE")

output_folder = "gemini_generated_images"
os.makedirs(output_folder, exist_ok=True)

# =====================================================
#  PROMPTS
# =====================================================

prompts = [
    "Cinematic shot of the Italian Adriatic coastline near Brindisi at golden hour, ancient stone fortifications overlooking deep azure waters, luxurious Explora Journeys cruise ship anchored offshore, warm sunlight, ultra-detailed 8k, photorealistic",
    "Aerial view of Stockholm archipelago in summer, colorful Gamla Stan buildings reflecting in calm Baltic waters, Oceania Cruises ship navigating narrow channels, soft northern daylight, hyper-realistic, 8k resolution",
    "Majestic view of Istanbul Bosphorus strait at sunset, silhouette of Hagia Sophia and Blue Mosque minarets against opulent orange sky, Regent Seven Seas ship sailing through, cinematic lighting, highly detailed",
    "Breathtaking view of Table Mountain looming over Cape Town harbour, bright sunny day with clear blue sky, Azamara luxury cruise ship docked in foreground, vibrant colors, 8k photorealistic",
    "Ancient stone walls of Dubrovnik Old Town meeting crystal clear Adriatic Sea, sunny midday light, Seabourn luxury yacht anchored off the Dalmatian coast, ultra-sharp details, 8k resolution",
    "Vibrant colonial architecture of Old San Juan Puerto Rico, colorful streets leading down to the sea, Crystal Cruises ship docked in harbour, tropical bright lighting, photorealistic travel photography style",
    "Sleek Explora Journeys luxury ship sailing the vast open Atlantic ocean at sunrise, calm waves reflecting orange and pink sky, transition from European coast to Caribbean horizon, cinematic wide shot, 8k",
    "Lush green cliffs of Madeira island plunging into the deep blue Atlantic ocean, exotic flowers in foreground, Explora Journeys ship approaching Funchal harbour, dramatic natural lighting, ultra-realistic",
    "Aerial drone shot of the Great Barrier Reef near Cairns, vibrant turquoise coral reefs visible through crystal clear water, Silversea luxury ship navigating the channel, bright tropical sun, 8k highly detailed",
    "Glamorous French Riviera coastline near Nice, azure sea meeting pebble beaches and Belle Epoque buildings, Explora Journeys ship sailing parallel to coast, soft afternoon Mediterranean light, photorealistic",
    "Montreal Old Port in peak autumn, vibrant red and orange foliage on trees surrounding historic stone buildings, Oceania cruise ship docked on St. Lawrence River, crisp fall atmosphere, 8k resolution",
    "Pink sand beaches of Bermuda with jagged rock formations, turquoise clear water, Celebrity Beyond cruise ship anchored in the distance, sunny tropical vibe, hyper-realistic travel photo",
    "Glitzy Monte Carlo harbour at twilight, hills lined with illuminated luxury villas and casinos, Seabourn cruise ship docked among superyachts, reflections on water, cinematic 8k shot",
    "Stunning Amalfi Coast cliffside village with colorful houses stacked vertically, Silversea ship anchored in the deep blue Tyrrhenian sea below, warm golden hour sunshine, highly detailed landscape",
    "Iconic white and blue domed churches of Santorini Greece overlooking the volcanic caldera, Emerald Azzurra luxury yacht anchored in the deep blue bay below, brilliant bright daylight, photorealistic 8k",
    "Majestic view of the Acropolis in Athens at dusk, ancient Parthenon ruins illuminated against twilight sky, Emerald Azzurra yacht visible in distant Piraeus harbour, dramatic and historical atmosphere",
    "Meeting of waters in the Amazon delta Brazil, lush dense rainforest shoreline, exotic wildlife, Seabourn expedition ship navigating the wide brown river, humid tropical atmosphere, hyper-realistic",
    "Vibrant mosaic architecture of Park Güell overlooking Barcelona city and Mediterranean sea, Azamara cruise ship visible in the distant commercial port, sunny Spanish day, ultra-detailed 8k",
    "Dramatic Chilean fjords with snow-capped mountains and massive blue glaciers meeting icy water, Viking ocean ship sailing through narrow misty passage, atmospheric cold lighting, cinematic shot",
    "New York City Manhattan skyline with Statue of Liberty in foreground, Crystal Cruises ship sailing out of New York harbour at sunset, city lights beginning to turn on, cinematic cityscape 8k",
    "Panoramic view of the Bay of Naples with Mount Vesuvius looming in background, Silversea cruise ship sailing across deep blue Italian waters, clear sunny day, photorealistic travel photography",
    "Breathtaking Bay of Kotor Montenegro, dramatic steep rugged mountains surrounding medieval fortified town, calm fjord-like water reflecting scenery, Regent Seven Seas ship anchored, early morning mist, 8k",
    "Neoclassical colorful mansions of Syros Greece cascading down hill to the sea, vibrant bougainvillea flowers, Silversea ship in the azure harbour, bright Mediterranean sun, highly detailed",
    "Exotic Southeast Asian seascape features limestone karsts rising from emerald water, traditional junk boat sailing past a Viking ocean ship, warm humid sunset light, atmospheric and realistic",
    "Miami South Beach art deco skyline and white sandy beach, turquoise Atlantic ocean, Celebrity Beyond cruise ship sailing out to sea, vibrant sunny tropical day, 8k ultra-realistic"
]

# =====================================================
#  HELPER FUNCTION
# =====================================================

def safe_filename(text):
    """Create a filesystem-safe filename from a prompt."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", text[:60]).strip("_")

# =====================================================
#  IMAGE GENERATION LOOP
# =====================================================

for i, prompt in enumerate(prompts, start=1):
    print(f"\n🌅 Generating image {i}/{len(prompts)}")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[prompt],
        )

        got_image = False
        for part in response.parts:
            if getattr(part, "inline_data", None):
                image = part.as_image()  # Convert inline data to PIL image
                filename = f"{safe_filename(prompt)}.png"
                filepath = os.path.join(output_folder, filename)
                image.save(filepath)
                print(f"✅ Saved: {filepath}")
                got_image = True

        if not got_image:
            text_reply = "".join(
                getattr(p, "text", "") or "" for p in response.parts
            )
            print(f"⚠️ No image returned (text response): {text_reply[:200]}")

    except Exception as e:
        print(f"❌ Error generating image {i}: {e}")

print("\n🎉 All cruise images generated successfully (or attempted).")
