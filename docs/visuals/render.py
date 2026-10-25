"""Renders the README feature cards from showcase.html into docs/*.png.

    py -3.13 docs/visuals/render.py
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
CARDS = {
    "ticks-card": "ticks.png",
    "deleted-card": "deleted.png",
    "privacy-card": "privacy.png",
    "edits-card": "edits.png",
    "ghost-card": "ghost.png",
    "scheduled-card": "scheduled.png",
    "updates-card": "updates.png",
}

with sync_playwright() as p:
    # The bundled Chromium is unusable on this machine; Edge renders the same.
    browser = p.chromium.launch(channel="msedge")
    page = browser.new_page(viewport={"width": 900, "height": 900}, device_scale_factor=2)
    page.goto((HERE / "showcase.html").as_uri())
    page.evaluate("document.fonts.ready")
    for card, name in CARDS.items():
        page.locator(f"#{card}").screenshot(path=OUT / name, omit_background=True)
        print(OUT / name)
    browser.close()
