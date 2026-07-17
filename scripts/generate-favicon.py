"""Generate ultra-simple high-contrast favicons (readable at 16px)."""
from PIL import Image, ImageDraw
import os

out_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(out_dir, exist_ok=True)

BLUE = (65, 79, 162, 255)
WHITE = (255, 255, 255, 255)


def draw_mark(size: int) -> Image.Image:
    """Blue rounded tile + white filled triangle — crisp in address bar."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    pad = max(0, size // 64)
    radius = max(3, int(size * 0.22))
    draw.rounded_rectangle(
        (pad, pad, size - 1 - pad, size - 1 - pad),
        radius=radius,
        fill=BLUE,
    )

    # Inset triangle (pointing up), generous margins
    m = size * 0.22
    top = m
    bottom = size - m * 0.95
    left = m * 1.05
    right = size - m * 1.05
    cx = size / 2
    triangle = [
        (cx, top),
        (right, bottom),
        (left, bottom),
    ]
    draw.polygon(triangle, fill=WHITE)
    return img


def save_all():
    fav32 = draw_mark(32)
    fav32.save(os.path.join(out_dir, "favicon.png"), "PNG", optimize=True)

    fav64 = draw_mark(64)
    fav64.save(os.path.join(out_dir, "favicon-64.png"), "PNG", optimize=True)

    fav128 = draw_mark(128)
    fav128.save(os.path.join(out_dir, "favicon-128.png"), "PNG", optimize=True)

    fav128.save(
        os.path.join(out_dir, "favicon.ico"),
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
    )

    draw_mark(180).save(os.path.join(out_dir, "apple-touch-icon.png"), "PNG", optimize=True)
    draw_mark(192).save(os.path.join(out_dir, "icon-192.png"), "PNG", optimize=True)

    for junk in ("_icon-crop-debug.png", "_left100.png", "_preview-16.png", "_preview-32.png"):
        p = os.path.join(out_dir, junk)
        if os.path.exists(p):
            os.remove(p)

    # 16px preview for QA
    draw_mark(128).resize((16, 16), Image.Resampling.LANCZOS).save(
        os.path.join(out_dir, "_preview-16.png")
    )
    print("OK simple triangle favicons")


if __name__ == "__main__":
    save_all()
