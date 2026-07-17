"""Generate square F-mark favicon assets for browser tabs."""
from PIL import Image, ImageDraw, ImageFont
import os

out_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(out_dir, exist_ok=True)

NAVY = (10, 26, 47, 255)  # #0a1a2f
BLUE = (65, 79, 162, 255)  # logo blue #414fa2
WHITE = (255, 255, 255, 255)


def make_mark(size: int, radius_ratio: float = 0.22) -> Image.Image:
    radius = int(size * radius_ratio)
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=NAVY)

    inset = max(1, int(size * 0.08))
    plate = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    pd = ImageDraw.Draw(plate)
    pd.rounded_rectangle(
        (inset, inset, size - 1 - inset, size - 1 - inset),
        radius=max(2, radius - inset // 2),
        fill=BLUE,
    )
    img = Image.alpha_composite(img, plate)
    draw = ImageDraw.Draw(img)

    font_paths = [
        r"C:\Windows\Fonts\arialbd.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf",
        r"C:\Windows\Fonts\calibrib.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    font = None
    for fp in font_paths:
        if os.path.exists(fp):
            font = ImageFont.truetype(fp, int(size * 0.58))
            break
    if font is None:
        font = ImageFont.load_default()

    text = "F"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0] + size * 0.02
    y = (size - th) / 2 - bbox[1] - size * 0.03
    draw.text((x, y), text, font=font, fill=WHITE)
    return img


fav32 = make_mark(32)
fav32.save(os.path.join(out_dir, "favicon.png"), "PNG", optimize=True)

fav64 = make_mark(64)
fav64.save(os.path.join(out_dir, "favicon-64.png"), "PNG", optimize=True)

# ICO with multiple sizes (Pillow embeds from the largest)
fav64.save(
    os.path.join(out_dir, "favicon.ico"),
    format="ICO",
    sizes=[(16, 16), (32, 32), (48, 48)],
)

apple = make_mark(180, radius_ratio=0.2)
apple.save(os.path.join(out_dir, "apple-touch-icon.png"), "PNG", optimize=True)

pwa = make_mark(192, radius_ratio=0.2)
pwa.save(os.path.join(out_dir, "icon-192.png"), "PNG", optimize=True)

print("OK: favicon.png, favicon.ico, apple-touch-icon.png, icon-192.png, favicon-64.png")
for name in [
    "favicon.png",
    "favicon.ico",
    "apple-touch-icon.png",
    "icon-192.png",
    "favicon-64.png",
]:
    p = os.path.join(out_dir, name)
    print(f"  {name}: {os.path.getsize(p)} bytes")
