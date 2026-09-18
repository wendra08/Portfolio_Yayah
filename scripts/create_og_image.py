from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
output_path = r"E:\Helping People\Ayah\Portfolio\public\og-image.jpg"
portrait_path = r"E:\Helping People\Ayah\Portfolio\src\assets\muhamad-yayah-formal.png"

bg = Image.new("RGB", (WIDTH, HEIGHT), (239, 243, 240))

# Main card
card = Image.new("RGB", (1050, 500), (255, 255, 255))
bg.paste(card, (75, 65))

# Left navy panel
navy = Image.new("RGB", (430, 430), (18, 33, 52))
bg.paste(navy, (110, 110))

# Portrait image
portrait = Image.open(portrait_path).convert("RGBA")
portrait = portrait.resize((360, 420), Image.Resampling.LANCZOS)
portrait_bg = Image.new("RGBA", (430, 430), (0, 0, 0, 0))
portrait_bg.paste(portrait, (30, 5), portrait)
# white border around portrait area
border = Image.new("RGBA", (430, 430), (255, 255, 255, 255))
# soft shadow effect using a slightly offset dark overlay
shadow = Image.new("RGBA", (430, 430), (15, 20, 26, 70))
shadow_mask = Image.new("L", (430, 430), 0)
# keep simple and stable
bg.paste(portrait_bg.convert("RGB"), (110, 110), portrait_bg)

# Accent panel line
accent = Image.new("RGB", (6, 110), (29, 108, 92))
bg.paste(accent, (610, 200))

# Title and subtitle text
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 38)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 26)
    font_url = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_url = ImageFont.load_default()

# Title text block
text_color = (18, 31, 42)
sub_color = (31, 104, 82)
draw = ImageDraw.Draw(bg)
draw.text((610, 210), "Muhamad Yayah", fill=text_color, font=font_title)
draw.text((610, 265), "Assistant Manager HRD", fill=sub_color, font=font_sub)
draw.text((610, 320), "muhamadyayah.my.id", fill=(82, 96, 108), font=font_url)

# Bottom subtle bar
bar = Image.new("RGB", (340, 6), (34, 96, 78))
bg.paste(bar, (610, 370))

# Small badge text
badge = Image.new("RGB", (250, 46), (22, 33, 52))
bg.paste(badge, (610, 405))
draw.text((628, 416), "HR & HRGA", fill=(255, 255, 255), font=font_url)

# Save image
bg = bg.resize((1200, 630), Image.Resampling.LANCZOS)
bg.save(output_path, quality=92)
print(f"Created OG image: {output_path}")
