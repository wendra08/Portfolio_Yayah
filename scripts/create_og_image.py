from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
output_path = r"E:\Helping People\Ayah\Portfolio\public\og-image.jpg"
portrait_path = r"E:\Helping People\Ayah\Portfolio\src\assets\muhamad-yayah-formal.png"

bg = Image.new("RGB", (WIDTH, HEIGHT), (239, 243, 240))

# main premium card container
card = Image.new("RGB", (1010, 500), (255, 255, 255))
shadow = Image.new("RGBA", (1010, 500), (0, 0, 0, 24))
shadow_draw = ImageDraw.Draw(shadow)
shadow_draw.rounded_rectangle((0, 0, 1010, 500), radius=18, fill=(0, 0, 0, 24))
# add subtle shadow behind white card
bg.paste(shadow.convert("RGB"), (95, 65), shadow)

a = Image.new("RGB", (1010, 500), (255, 255, 255))
card_draw = ImageDraw.Draw(a)
card_draw.rounded_rectangle((0, 0, 1010, 500), radius=18, fill=(255, 255, 255))
card_draw.rounded_rectangle((1, 1, 1009, 499), radius=17, outline=(223, 232, 228), width=2)
bg.paste(a, (95, 65))

# navy panel for portrait
navy = Image.new("RGB", (420, 430), (18, 31, 49))
bg.paste(navy, (120, 110))

# portrait image
portrait = Image.open(portrait_path).convert("RGBA")
portrait = portrait.resize((345, 410), Image.Resampling.LANCZOS)
portrait_bg = Image.new("RGBA", (420, 430), (0, 0, 0, 0))
portrait_bg.paste(portrait, (35, 10), portrait)
bg.paste(portrait_bg.convert("RGB"), (120, 110), portrait_bg)

# clean text panel with no side line
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 40)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 28)
    font_url = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
    font_tag = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 16)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_url = ImageFont.load_default()
    font_tag = ImageFont.load_default()

text_draw = ImageDraw.Draw(bg)
text_draw.text((610, 210), "Muhamad Yayah", fill=(18, 31, 42), font=font_title)
text_draw.text((610, 272), "Assistant Manager HRD", fill=(31, 104, 82), font=font_sub)
text_draw.text((610, 334), "muhamadyayah.my.id", fill=(93, 104, 112), font=font_url)

# minimal tag pill without side accent line
pill = Image.new("RGB", (210, 42), (18, 33, 52))
bg.paste(pill, (610, 392))
text_draw.text((640, 401), "HR & HRGA", fill=(255, 255, 255), font=font_tag)

# subtle footer label
text_draw.text((120, 560), "MUHAMADYAYAH.MY.ID", fill=(94, 108, 120), font=font_url)

bg = bg.resize((1200, 630), Image.Resampling.LANCZOS)
bg.save(output_path, quality=92)
print(f"Created OG image: {output_path}")
