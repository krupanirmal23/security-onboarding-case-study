import asyncio,os
from playwright.async_api import async_playwright
R=os.path.abspath(os.path.dirname(__file__)+'/..')
EXE='/home/box/.cache/ms-playwright/chromium_headless_shell-1254/chrome-headless-shell-linux64/chrome-headless-shell'
css='''
@page{size:1080px 1350px;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Geist,Inter,sans-serif;color:#14161A;background:#F4F2EC}
.s{width:1080px;height:1350px;padding:96px 88px;position:relative;page-break-after:always;overflow:hidden;display:flex;flex-direction:column}
.k{font-family:"Geist Mono",monospace;font-size:22px;letter-spacing:.12em;text-transform:uppercase;color:#6B6F76}
h1{font-family:"Instrument Serif",serif;font-weight:400;font-size:128px;line-height:1.02;margin:28px 0 0}
h2{font-family:"Instrument Serif",serif;font-weight:400;font-size:72px;line-height:1.05;margin:24px 0 0}
p{font-size:30px;line-height:1.4;color:#3a3d42;margin-top:28px}
.foot{position:absolute;left:88px;right:88px;bottom:64px;display:flex;justify-content:space-between;font-family:"Geist Mono",monospace;font-size:20px;color:#6B6F76;border-top:1px solid #E2DED4;padding-top:20px}
.big{font-family:"Instrument Serif",serif;font-size:260px;line-height:1;color:#9A3B3B}
.row{display:flex;align-items:center;gap:24px;margin-top:26px;font-size:28px}
.row .l{width:420px}.row .bar{height:26px;background:#9A3B3B;border-radius:3px}.row .n{font-family:"Geist Mono",monospace;font-size:26px}
.steps{display:flex;gap:16px;margin-top:56px}
.steps div{flex:1;background:#fff;border:1px solid #E2DED4;border-radius:14px;padding:36px 28px;min-height:360px;display:flex;flex-direction:column;justify-content:space-between}
.steps b{display:block;font-family:"Instrument Serif",serif;font-weight:400;font-size:150px;line-height:1}
.steps span{font-size:24px;color:#6B6F76}
img{width:100%;border-radius:12px;border:1px solid #E2DED4;margin-top:48px;box-shadow:0 10px 40px rgba(20,22,26,.08)}
.card{background:#fff;border:1px solid #E2DED4;border-radius:14px;padding:30px 34px;margin-top:22px}
.card .t{font-family:"Geist Mono",monospace;font-size:20px;letter-spacing:.1em;color:#6B6F76;text-transform:uppercase}
.card .v{font-size:32px;margin-top:10px;line-height:1.3}
.ns{background:#14161A;color:#F4F2EC;border:none}.ns .t{color:#9aa0a8}
.ok .t{color:#1F6F5C}.warn .t{color:#9A3B3B}
.q{font-family:"Instrument Serif",serif;font-size:44px;line-height:1.2;margin-top:48px;border-left:4px solid #9A3B3B;padding-left:28px}
.src{font-size:22px;color:#6B6F76;margin-top:14px;padding-left:32px}
ul{margin-top:36px;list-style:none}li{font-size:30px;line-height:1.4;margin-top:18px;padding-left:34px;position:relative}li:before{content:"";position:absolute;left:0;top:18px;width:14px;height:2px;background:#14161A}
'''
def foot(i): return f'<div class="foot"><span>Krupa Nirmal · Zero Trust onboarding case study</span><span>{i}/8</span></div>'
clusters=[('Lost in the console or docs',17),('Device refused at enrollment',13),('First policy “isn’t working”',8),('Free-plan checkout, team creation',7),('Sign-in method errors',5)]
bars=''.join(f'<div class="row"><div class="l">{a}</div><div class="bar" style="width:{n*24}px"></div><div class="n">{n}</div></div>' for a,n in clusters)
def im(f): return f'<img src="file://{R}/mockups/{f}.png">'
S=[
f'<div class="k">Case study · Cloudflare Zero Trust</div><h1>Why new IT admins stall before their first policy</h1><p style="margin-top:48px">I walked the public setup docs step by step and coded 60 public posts and reviews from admins who tried.</p><p style="margin-top:auto;margin-bottom:80px;font-size:24px;color:#6B6F76">Independent concept. Public information only. Not affiliated with Cloudflare.</p>',
f'<div class="k">The path today</div><h2>29 documented steps to protect one laptop</h2><div class="steps"><div><b>4</b><span>Team setup</span></div><div><b>3</b><span>Sign-in (PIN)</span></div><div><b>11</b><span>Enroll device</span></div><div><b>11</b><span>First DNS policy</span></div></div><p>Shortest path, across 5 doc pages. With Entra ID as the identity provider it is 50.</p><p style="font-size:22px;color:#6B6F76">Counted from developers.cloudflare.com, 11 Nov 2026. One numbered instruction = one step.</p>',
f'<div class="k">Where it breaks</div><h2>56 friction signals, 5 themes</h2>{bars}<p style="font-size:22px;color:#6B6F76;margin-top:48px">Cloudflare Community 33 · Reddit 10 · G2 9 · X 5 · Gartner 3. Posts come from people who got stuck, so these rank themes; they are not failure rates.</p>',
f'<div class="k">The most specific failure</div><h2>The quick start skips one rule</h2><p>Device enrollment permissions live on a separate page. Without a rule, the client is refused before any sign-in screen.</p><div class="q">“Enrolling any device fails immediately with ‘Enrollment request is invalid’”</div><div class="src">Cloudflare Community, Sep 2026</div>{im("02_enrollment_preflight")}',
f'<div class="k">Then: does it work?</div><h2>Prove the first policy on the test device</h2><p>8 posts say a new block policy “isn’t working”. A guided first policy adds a template, a dry run, and a live check on the enrolled device.</p>{im("03_guided_first_policy")}',
f'<div class="k">Less blank slate</div><h2>A checklist that checks itself, and sample data</h2><p>Each step is marked done only when the console sees the real config. A read-only sample org shows what a working setup looks like.</p>{im("01_setup_checklist")}',
f'<div class="k">How to measure it</div><h2>One North Star, two guardrails</h2><div class="card ns"><div class="t">North Star</div><div class="v">Activated accounts: ≥1 enrolled device and ≥1 enforced policy within [N] days of signup</div></div><div class="card"><div class="t">Inputs</div><div class="v">Time to first policy · Checklist completion · Setup tickets per 100 new orgs</div></div><div class="card warn"><div class="t">Guardrails</div><div class="v">Misconfiguration rate · Security incidents</div></div><p style="font-size:24px;color:#6B6F76">Baselines and targets: [Team to decide] from first-party data.</p>',
f'<div class="k">What I’d test</div><h2>Two A/B tests</h2><div class="card ok"><div class="t">Test 1</div><div class="v">Guided checklist vs current console. Primary: activation within [N] days.</div></div><div class="card ok"><div class="t">Test 2</div><div class="v">Sample-data mode vs empty state. Primary: activation within [N] days.</div></div><p>Sized with a two-proportion formula once the team sets baseline, MDE, α and power. Ship only if no guardrail gets worse.</p><p style="font-size:24px;color:#6B6F76">Full case study, PRD and data: github.com/krupanirmal23/security-onboarding-case-study</p>',
]
html='<html><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+''.join(f'<section class="s">{s}{foot(i+1)}</section>' for i,s in enumerate(S))+'</body></html>'
open(R+'/carousel/carousel.html','w').write(html)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=EXE,args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.goto('file://'+R+'/carousel/carousel.html'); await pg.wait_for_timeout(800)
        await pg.pdf(path=R+'/LinkedIn_Carousel.pdf',width='1080px',height='1350px',print_background=True,prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
