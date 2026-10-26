import os
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",headless=True)
    for w,h,t in [(1440,900,"1440"),(390,844,"390")]:
        pg=b.new_context(viewport={"width":w,"height":h}).new_page(); pg.goto("file://"+ROOT+"/index.html"); pg.wait_for_timeout(1800)
        pg.screenshot(path=f"shots/clip-hero-{t}.png")
        for sel,n in [("#value","value"),("#assets","orbit"),("#practice","flow")]:
            el=pg.locator(sel).first; el.scroll_into_view_if_needed(); pg.wait_for_timeout(1500); el.screenshot(path=f"shots/clip-{n}-{t}.png")
    b.close()
