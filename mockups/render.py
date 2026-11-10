import asyncio,glob,sys
from playwright.async_api import async_playwright
EXE='/home/box/.cache/ms-playwright/chromium_headless_shell-1254/chrome-headless-shell-linux64/chrome-headless-shell'
async def main(files):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=EXE)
        for f in files:
            w,h=(1440,900)
            pg=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=2)
            import os; await pg.goto('file://'+os.path.abspath(f)); await pg.wait_for_timeout(600)
            await pg.screenshot(path=f.replace('.html','.png')); await pg.close(); print(f)
        await b.close()
asyncio.run(main(sys.argv[1:] or sorted(glob.glob('0*.html'))))
