from PIL import Image
import os

src = r"C:\Users\Anwender\Meine Ablage\Ablage Andy\GmbH Unterlagen\Logo FVM GmbH\GmbH unten2.jpg.png"
out_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "fvm-logo.png")
favicon = os.path.join(out_dir, "favicon.png")

img = Image.open(src).convert("RGBA")
w, h = img.size
pixels = img.load()


def row_is_black(y, threshold=40):
    black = sum(
        1
        for x in range(w)
        if pixels[x, y][0] < threshold
        and pixels[x, y][1] < threshold
        and pixels[x, y][2] < threshold
    )
    return black > w * 0.85


crop_bottom = h
for y in range(h - 1, -1, -1):
    if row_is_black(y):
        crop_bottom = y
    else:
        break

if crop_bottom < h:
    img = img.crop((0, 0, w, crop_bottom))

w, h = img.size
pixels = img.load()

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if r > 235 and g > 235 and b > 235:
            pixels[x, y] = (r, g, b, 0)
        elif r < 30 and g < 30 and b < 30:
            pixels[x, y] = (r, g, b, 0)

bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

max_h = 96
if img.height > max_h:
    ratio = max_h / img.height
    img = img.resize((int(img.width * ratio), max_h), Image.Resampling.LANCZOS)

img.save(out, "PNG", optimize=True)

fav = img.copy()
fav.thumbnail((64, 64), Image.Resampling.LANCZOS)
fav.save(favicon, "PNG", optimize=True)

print(f"Saved: {out} ({img.size})")
