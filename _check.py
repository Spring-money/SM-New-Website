import sys, json, os, asyncio
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.abspath(__file__))
import glob; pages=sorted(os.path.basename(f)[:-5] for f in glob.glob(ROOT+"/*.html") if not os.path.basename(f).startswith("_"))
sel=sys.argv[1:] or pages
out=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",headless=True)
    for w,h,tag in [(1440,900,"1440"),(390,844,"390")]:
        ctx=b.new_context(viewport={"width":w,"height":h},device_scale_factor=1)
        for n in sel:
            pg=ctx.new_page(); errs=[]
            pg.on("console",lambda m,e=errs: e.append(m.text) if m.type=="error" else None)
            pg.on("pageerror",lambda e,l=errs: l.append(str(e)))
            pg.on("requestfailed",lambda r,l=errs: l.append("FAILED "+r.url))
            pg.goto("file://"+ROOT+"/"+n+".html"); pg.wait_for_timeout(600)
            H=pg.evaluate("document.documentElement.scrollHeight")
            for y in range(0,H,500): pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(60)
            pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(1500)
            sw=pg.evaluate("document.documentElement.scrollWidth"); 
            over=pg.evaluate("""()=>{const W=document.documentElement.clientWidth;return [...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>W+1&&getComputedStyle(e).position!=='fixed'&&!e.closest('.sw-rail,.nav-links,.house,.sense-bg,.orbit')}).slice(0,4).map(e=>e.tagName+'.'+e.className)}""")
            pg.screenshot(path=f"shots/{n}-{tag}.png",full_page=True)
            out.append((tag,n,H,sw,over,errs[:3]))
            pg.close()
        ctx.close()
    b.close()
for o in out: print(o)
