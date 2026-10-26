import os
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",headless=True)
    for w,h,tag in [(1440,900,"1440"),(390,844,"390")]:
        pg=b.new_context(viewport={"width":w,"height":h}).new_page(); errs=[]
        pg.on("pageerror",lambda e: errs.append(str(e))); pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
        pg.goto("file://"+ROOT+"/spring-sense.html"); pg.wait_for_timeout(500)
        el=pg.locator("[data-sense]").first; el.scroll_into_view_if_needed()
        for lane in ["mfd","ria"]:
            pg.locator(f"[data-sense-lane={lane}]").first.click()
            for i in range(5):
                pg.locator(".agent-btn").nth(i).click(); pg.wait_for_timeout(6500)
                if lane=="mfd" or i==1: pg.locator(".sense-window").first.screenshot(path=f"shots/sense-{lane}-agent{i+1}-{tag}.png")
        print(tag,errs)
    b.close()
