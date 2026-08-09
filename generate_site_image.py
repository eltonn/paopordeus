from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent
output = root / 'img' / 'site_hero.png'
size = (1200, 800)
img = Image.new('RGB', size, (250, 248, 241))
d = ImageDraw.Draw(img)
try:
    font_b = ImageFont.truetype('arialbd.ttf', 64)
    font_s = ImageFont.truetype('arial.ttf', 36)
except Exception:
    font_b = ImageFont.load_default()
    font_s = ImageFont.load_default()

headline = 'ESPACO PARA EVENTOS'
subline = 'Centro Histórico de São José'
footer = 'Espaço ideal para realização de eventos sociais e corporativos.'

w, h = d.textbbox((0, 0), headline, font=font_b)[2:]
d.text(((size[0] - w) / 2, 220), headline, fill=(47, 43, 38), font=font_b)

w, h = d.textbbox((0, 0), subline, font=font_s)[2:]
d.text(((size[0] - w) / 2, 300), subline, fill=(107, 103, 92), font=font_s)

bar_y = 420
bar_h = 70
d.rectangle([120, bar_y, 1080, bar_y + bar_h], fill=(139, 87, 42), outline=None)

w, h = d.textbbox((0, 0), footer, font=font_s)[2:]
d.text(((size[0] - w) / 2, bar_y + (bar_h - h) / 2), footer, fill=(255, 255, 255), font=font_s)

img.save(output)
print(output)
