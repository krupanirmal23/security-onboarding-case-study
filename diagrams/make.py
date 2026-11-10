CSS='''body{width:1600px;height:800px;display:block;padding:56px 64px;overflow:visible}
.grid{display:grid;grid-template-columns:170px repeat(4,1fr);gap:0;border-top:1px solid var(--ink)}
.cell{padding:18px 18px;border-bottom:1px solid var(--line);border-left:1px solid var(--line);font-size:14.5px}
.rowh{padding:18px 0;border-bottom:1px solid var(--line);font-family:'Geist Mono',monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.big{font-family:'Instrument Serif',serif;font-size:42px;line-height:1}
.q{font-family:'Instrument Serif',serif;font-size:19px;line-height:1.25}
.bar{height:8px;border-radius:99px;background:var(--warn);margin-top:8px}
'''
stages=[("1","Team setup"),("2","Sign-in method"),("3","Device enrollment"),("4","First policy")]
steps=[("4","Get started page"),("3 – 24","One-time PIN 3 · Okta 9–14 · Entra ID 24"),("11","Enrollment rule 5 + desktop client 6"),("11 – 19","DNS policy 11 · Access app 19")]
fric=[(7,"Free-plan checkout and team creation"),(6,"Sign-in errors: 5 IdP, 1 PIN never sent (no enrollment rule)"),(16,"12 enrollment refusals · 2 MDM · 2 roaming"),(10,"8 “policy isn’t working” · 2 policy-building")]
quotes=["“all attempts to enable zero trust have failed at the payment screen after selecting the free account”","“Sign in with AzureAD > ‘That account does not have access.’”","“fails immediately … before any login/authentication prompt appears”","“shows blocks in the logs, but … blocked test sites load”"]
prop=[("Checklist","Checks itself; next step unlocks"),("Test login","Run before anyone enrolls"),("Enrollment check","Catches the missing rule; enroll link fills team name"),("Guided policy","Template, dry run, prove it on the test device")]
h='<div class="label">Journey map · IT admin, 200–2,000 employees · Cloudflare Zero Trust</div><h1 style="margin:10px 0 6px">Current vs proposed onboarding</h1><p class="sub" style="margin-bottom:28px">Steps counted from public docs. Friction = public signals tagged to a stage (39 of 56; the other 17 are cross-stage). Accessed 11 Nov 2026.</p>'
h+='<div class="grid"><div class="rowh"></div>'+''.join(f'<div class="cell" style="border-bottom:1px solid var(--ink)"><div class="label">Stage {a}</div><h2 style="margin-top:4px">{b}</h2></div>' for a,b in stages)
h+='<div class="rowh">Documented steps</div>'+''.join(f'<div class="cell"><div class="big">{a}</div><div class="sub" style="margin-top:6px">{b}</div></div>' for a,b in steps)
mx=16
h+='<div class="rowh">Friction signals</div>'+''.join(f'<div class="cell"><div class="big" style="color:var(--warn)">{a}</div><div class="bar" style="width:{a/mx*100:.0f}%"></div><div class="sub" style="margin-top:8px">{b}</div></div>' for a,b in fric)
h+='<div class="rowh">In their words</div>'+''.join(f'<div class="cell q">{q}</div>' for q in quotes)
h+='<div class="rowh" style="color:var(--ok)">Proposed</div>'+''.join(f'<div class="cell" style="background:var(--okbg)"><h2 style="color:var(--ok)">{a}</h2><div style="margin-top:4px">{b}</div></div>' for a,b in prop)
h+='</div><div style="display:flex;gap:28px;margin-top:22px;color:var(--muted);font-size:13.5px"><span>Across all stages: 17 signals about getting lost in the console or docs → <b style="color:var(--ink)">sample-data mode + setup helper</b></span><span style="margin-left:auto">Shortest documented path: 29 steps across 5 doc pages</span></div>'
open('journey_map.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>{CSS}</style></head><body>{h}</body></html>')

CSS2='''body{width:1600px;height:900px;display:block;padding:56px 64px}
.node{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px}
.k{font-family:'Geist Mono',monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase}
.d{color:var(--muted);font-size:13.5px;margin-top:6px;line-height:1.4}
svg{position:absolute;left:0;top:0;pointer-events:none}'''
b='''<div class="label">Metrics tree</div><h1 style="margin:10px 0 34px">What “activated” means, and what feeds it</h1>
<div style="position:relative;height:640px">
<svg width="1472" height="640"><g stroke="#14161A" stroke-width="1.2" fill="none">
<path d="M736 118 V160 H245 V200"/><path d="M736 160 H736 V200"/><path d="M736 160 H1227 V200"/>
<path d="M245 330 V372 H480 V410" stroke="#9A3B3B" stroke-dasharray="4 4"/><path d="M1227 330 V372 H992 V410" stroke="#9A3B3B" stroke-dasharray="4 4"/>
</g></svg>
<div class="node" style="position:absolute;left:486px;top:0;width:500px;background:var(--ink);color:#fff;border-color:var(--ink)"><div class="k" style="color:#B9BDC4">North Star</div><div style="font-family:'Instrument Serif',serif;font-size:34px;line-height:1.1;margin-top:4px">Activated accounts</div><div class="d" style="color:#C9CCD1">New orgs with ≥1 enrolled device and ≥1 policy enforced on its traffic within [N] days of signup. N: [Team to decide]</div></div>
<div class="node" style="position:absolute;left:20px;top:200px;width:450px"><div class="k" style="color:var(--ok)">Input</div><h2 style="margin-top:4px">Time to first policy</h2><div class="d">Signup → first policy enforced on an enrolled device. Median per weekly cohort.</div></div>
<div class="node" style="position:absolute;left:511px;top:200px;width:450px"><div class="k" style="color:var(--ok)">Input</div><h2 style="margin-top:4px">Checklist completion</h2><div class="d">Share of new orgs finishing each checklist step. Shows where they stop.</div></div>
<div class="node" style="position:absolute;left:1002px;top:200px;width:450px"><div class="k" style="color:var(--ok)">Input</div><h2 style="margin-top:4px">Setup support tickets</h2><div class="d">Tickets and forum posts tagged setup, per 100 new orgs. Lower is better.</div></div>
<div class="node" style="position:absolute;left:255px;top:410px;width:450px;border-color:#E3C9C6"><div class="k" style="color:var(--warn)">Guardrail</div><h2 style="margin-top:4px">Misconfiguration rate</h2><div class="d">Share of activated orgs with a policy that blocks its own admin, blocks nothing it matched, or is rolled back within [N] days. Definition: [Team to confirm]</div></div>
<div class="node" style="position:absolute;left:767px;top:410px;width:450px;border-color:#E3C9C6"><div class="k" style="color:var(--warn)">Guardrail</div><h2 style="margin-top:4px">Security incidents</h2><div class="d">Incidents traced to a template, a sample-data draft, or a helper-suggested change. Any rise vs control stops the rollout.</div></div>
<div style="position:absolute;left:20px;top:590px;color:var(--muted);font-size:13.5px">Targets and baselines: [Team to decide] from first-party product data. Outcomes are framed as hypotheses.</div>
</div>'''
open('metrics_tree.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>{CSS2}</style></head><body>{b}</body></html>')
