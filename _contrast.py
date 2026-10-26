import os, sys
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.abspath(__file__))
import glob; pages=sorted(os.path.basename(f)[:-5] for f in glob.glob(ROOT+"/*.html") if not os.path.basename(f).startswith("_"))
JS="""()=>{
function parse(c){const m=c.match(/rgba?\\(([^)]+)\\)/);if(!m)return null;const p=m[1].split(',').map(x=>parseFloat(x));return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1}}
function lum(c){const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(c.r)+.7152*f(c.g)+.0722*f(c.b)}
function blend(fg,bg){const a=fg.a;return {r:fg.r*a+bg.r*(1-a),g:fg.g*a+bg.g*(1-a),b:fg.b*a+bg.b*(1-a),a:1}}
function bgOf(e){let layers=[];let n=e;while(n&&n.nodeType===1){const cs=getComputedStyle(n);const c=parse(cs.backgroundColor);if(cs.backgroundImage!=='none'&&!/gradient/.test(cs.backgroundImage)){return null}
 if(c&&c.a>0){layers.push(c);if(c.a>=1)break}n=n.parentElement}
 let base={r:252,g:255,b:254,a:1};for(let i=layers.length-1;i>=0;i--)base=blend(layers[i],base);return base}
const out=[];const seen=new Set();
document.querySelectorAll('body *').forEach(e=>{
 if(!e.childNodes.length)return;let t='';e.childNodes.forEach(n=>{if(n.nodeType===3)t+=n.textContent});t=t.trim();if(!t)return;
 const r=e.getBoundingClientRect();if(r.width===0||r.height===0)return;const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.display==='none')return;
 let op=1,n=e;while(n&&n.nodeType===1){op*=parseFloat(getComputedStyle(n).opacity);n=n.parentElement}
 if(e.closest('.scene:not(.is-active)'))return;
 const fg=parse(cs.color);const bg=bgOf(e);if(!bg||!fg)return;const f=blend({...fg,a:fg.a*op},bg);
 const L1=lum(f),L2=lum(bg);const cr=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
 const size=parseFloat(cs.fontSize),bold=parseInt(cs.fontWeight)>=700;const large=size>=24||(size>=18.66&&bold);
 const need=large?3:4.5;if(cr<need){const k=e.tagName+'.'+e.className+'|'+t.slice(0,30);if(!seen.has(k)){seen.add(k);out.push([cr.toFixed(2),need,k,cs.color,'on',`rgb(${Math.round(bg.r)},${Math.round(bg.g)},${Math.round(bg.b)})`])}}
});return out}"""
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",headless=True)
    pg=b.new_context(viewport={"width":1440,"height":900},reduced_motion="reduce").new_page()
    for n in pages:
        pg.goto("file://"+ROOT+"/"+n+".html"); pg.wait_for_timeout(500)
        for lane in ["mfd","ria"]:
            if n in("index","spring-sense"):
                pg.locator(f"[data-sense-lane={lane}]").first.click()
            for i in range(5 if n in ("index","spring-sense") else 1):
                if n in("index","spring-sense"): pg.locator(".agent-btn").nth(i).click(); pg.wait_for_timeout(150)
                for r in pg.evaluate(JS): print(n,lane,i,r)
            if n not in("index","spring-sense"): break
    b.close()
print("done")
