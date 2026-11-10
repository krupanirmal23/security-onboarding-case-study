"""Screenshots of public Cloudflare pages with headless Chromium. Usage: python scripts/shoot.py scripts/pages.txt"""
import sys, asyncio
from playwright.async_api import async_playwright
pages=[l.split() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/home/box/.cache/ms-playwright/chromium_headless_shell-1254/chrome-headless-shell-linux64/chrome-headless-shell')
        ctx=await b.new_context(viewport={'width':1440,'height':900},device_scale_factor=1,
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36')
        for name,url in pages:
            pg=await ctx.new_page()
            try:
                r=await pg.goto(url,wait_until='domcontentloaded',timeout=60000)
                await pg.wait_for_timeout(8000)
                for sel in ['#onetrust-accept-btn-handler','button:has-text("Accept all")','button:has-text("Accept")']:
                    try: await pg.click(sel,timeout=700)
                    except: pass
                await pg.wait_for_timeout(800)
                await pg.screenshot(path=f'screens/{name}.png')
                await pg.screenshot(path=f'screens/full/{name}_full.png',full_page=True)
                print(name,r.status if r else None,pg.url)
            except Exception as e: print(name,'ERR',str(e)[:150])
            await pg.close()
        await b.close()
asyncio.run(main())
