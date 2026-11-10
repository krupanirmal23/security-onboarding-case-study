import asyncio,os
from playwright.async_api import async_playwright
EXE='/home/box/.cache/ms-playwright/chromium_headless_shell-1254/chrome-headless-shell-linux64/chrome-headless-shell'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=EXE)
        for f in ['journey_map','metrics_tree']:
            pg=await b.new_page(viewport={'width':1600,'height':800 if f=='journey_map' else 900},device_scale_factor=2)
            await pg.goto('file://'+os.path.abspath(f+'.html')); await pg.wait_for_timeout(500)
            await pg.screenshot(path=f+'.png',full_page=True); await pg.close()
        await b.close()
asyncio.run(main())
