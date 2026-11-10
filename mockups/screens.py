from _shell import page
S={}
# 1 Setup checklist
S['01_setup_checklist']=page("Setup checklist","Get started",'''
<div style="display:flex;justify-content:space-between;align-items:flex-end">
 <div><div class="label">Setup · 2 of 4 done</div><h1 style="margin-top:10px">Protect your first device</h1>
 <p class="sub">Four steps, in this order. Each one checks itself before you move on.</p></div>
 <div style="display:flex;gap:10px"><span class="btn ghost">Try with sample data first</span></div></div>
<div style="height:6px;background:var(--soft);border-radius:99px;margin:28px 0 26px"><div style="width:50%;height:100%;background:var(--ok);border-radius:99px"></div></div>
<div style="display:flex;flex-direction:column;gap:12px">
 <div class="card" style="padding:20px 24px;display:flex;gap:18px;align-items:center"><span class="pill ok">✓ Done</span><div style="flex:1"><h2>Name your team</h2><div class="sub" style="margin:2px 0 0">acme-it · users type this when they enroll</div></div><span class="label">Checked</span></div>
 <div class="card" style="padding:20px 24px;display:flex;gap:18px;align-items:center"><span class="pill ok">✓ Done</span><div style="flex:1"><h2>Choose how people sign in</h2><div class="sub" style="margin:2px 0 0">One-time PIN to email now · connect Okta or Entra ID later</div></div><span class="label">Test login passed</span></div>
 <div class="card" style="padding:24px;box-shadow:0 0 0 2px var(--ink)">
  <div style="display:flex;gap:18px;align-items:center"><span class="pill hint">Next</span><div style="flex:1"><h2>Let devices join</h2><div class="sub" style="margin:2px 0 0">Who may enroll, then one test device</div></div><span class="btn">Set up enrollment</span></div>
  <div style="margin:18px 0 0 92px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
   <div style="border:1px solid var(--line);border-radius:10px;padding:12px 14px"><div class="label">a · Enrollment rule</div><div style="margin-top:4px">Emails ending in <b>@acme.example</b></div></div>
   <div style="border:1px solid var(--line);border-radius:10px;padding:12px 14px"><div class="label">b · Login method</div><div style="margin-top:4px">One-time PIN <span style="color:var(--ok)">✓ linked</span></div></div>
   <div style="border:1px solid var(--line);border-radius:10px;padding:12px 14px"><div class="label">c · Test device</div><div style="margin-top:4px;color:var(--muted)">Waiting for first device</div></div></div></div>
 <div class="card" style="padding:20px 24px;display:flex;gap:18px;align-items:center;opacity:.6"><span class="pill mute">Locked</span><div style="flex:1"><h2>Turn on your first policy</h2><div class="sub" style="margin:2px 0 0">Unlocks when one device is connected, so you can see it work</div></div></div>
</div>''')
# 2 Enrollment pre-flight (fix for the top friction)
S['02_enrollment_preflight']=page("Enrollment check","Devices",'''
<div class="label">Devices · before you share the team name</div><h1 style="margin-top:10px">Ready for devices?</h1>
<p class="sub">We run the same checks the client runs, so users don't hit "Enrollment request is invalid".</p>
<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:24px;margin-top:30px">
 <div class="card" style="padding:8px 0">
  <div style="padding:16px 24px;display:flex;gap:14px;align-items:center;border-bottom:1px solid var(--line)"><span class="pill ok">Pass</span><div style="flex:1">Team name <span class="mono">acme-it</span> resolves</div></div>
  <div style="padding:16px 24px;display:flex;gap:14px;align-items:center;border-bottom:1px solid var(--line)"><span class="pill ok">Pass</span><div style="flex:1">A login method is attached to enrollment</div></div>
  <div style="padding:16px 24px;display:flex;gap:14px;align-items:flex-start;background:var(--warnbg)"><span class="pill warn" style="background:#fff">Fail</span><div style="flex:1"><b>No enrollment rule yet.</b> Every device will be refused until one exists.<div style="margin-top:12px;display:flex;gap:10px"><span class="btn">Allow @acme.example</span><span class="btn ghost">Choose people</span></div></div></div>
  <div style="padding:16px 24px;display:flex;gap:14px;align-items:center"><span class="pill mute">Skipped</span><div style="flex:1;color:var(--muted)">Test email gets a PIN · runs after the rule exists</div></div>
 </div>
 <div class="card" style="padding:24px;display:flex;flex-direction:column;gap:14px">
  <div class="label">Share with your users</div>
  <div style="display:flex;gap:16px;align-items:center"><div style="width:96px;height:96px;border-radius:10px;background:repeating-conic-gradient(var(--ink) 0 25%,#fff 0 50%) 0 0/16px 16px;opacity:.85"></div>
  <div><b>Enroll link</b><div class="sub" style="margin:2px 0 0">Fills in the team name for them</div></div></div>
  <div class="mono" style="font-size:12.5px;background:var(--soft);padding:10px 12px;border-radius:8px;color:var(--muted)">Locked until all checks pass</div>
  <div style="border-top:1px solid var(--line);padding-top:14px"><div class="label">Rolling out to many devices?</div><div style="margin-top:4px">Download an MDM file with the team name already set</div></div>
 </div></div>''')
# 3 Guided first policy
S['03_guided_first_policy']=page("First policy","Policies",'''
<div class="label">Policies · guided</div><h1 style="margin-top:10px">Your first policy</h1>
<p class="sub">Start from a template. See what it will do before it touches real traffic.</p>
<div style="display:grid;grid-template-columns:360px 1fr;gap:24px;margin-top:28px">
 <div style="display:flex;flex-direction:column;gap:10px">
  <div class="card" style="padding:18px 20px;box-shadow:0 0 0 2px var(--ink)"><span class="pill hint">Recommended start</span><h2 style="margin-top:10px">Block security threats</h2><div class="sub" style="margin:4px 0 0">DNS · all security risk categories</div></div>
  <div class="card" style="padding:18px 20px"><h2>Block a list of sites</h2><div class="sub" style="margin:4px 0 0">DNS · paste or upload domains</div></div>
  <div class="card" style="padding:18px 20px"><h2>Protect one internal app</h2><div class="sub" style="margin:4px 0 0">Access · only your team can open it</div></div>
 </div>
 <div class="card" style="padding:26px 28px">
  <div class="label">In plain words</div>
  <p style="font-family:'Instrument Serif',serif;font-size:30px;line-height:1.2;margin-top:8px">When anyone at <u>acme-it</u> looks up a site in a <u>security risk</u> category, <u>block it</u> and show the block page.</p>
  <div style="display:flex;gap:10px;margin-top:22px;flex-wrap:wrap"><span class="pill mute">Selector · Security categories</span><span class="pill mute">Operator · in</span><span class="pill mute">Value · All security risks</span><span class="pill mute">Action · Block</span></div>
  <div style="margin-top:26px;border-top:1px solid var(--line);padding-top:20px;display:grid;grid-template-columns:1fr 1fr;gap:16px">
   <div><div class="label">Step 1 · Dry run</div><div style="margin-top:6px">Log what would be blocked. Nothing is blocked yet.</div></div>
   <div><div class="label">Step 2 · Prove it</div><div style="margin-top:6px">Open a test domain from your enrolled device and watch it appear here.</div></div></div>
  <div style="display:flex;gap:10px;margin-top:24px"><span class="btn">Start dry run</span><span class="btn ghost">Edit conditions</span></div>
 </div></div>''')
# 4 Sample data
S['04_sample_data_mode']=page("Sample data","Sample data",'''
<div style="background:var(--hintbg);color:var(--hint);border-radius:12px;padding:12px 18px;display:flex;align-items:center;gap:12px;margin-bottom:26px"><b>Sample data</b><span>Nothing here is your traffic. Policies you build stay as drafts until you go live.</span><span class="btn" style="margin-left:auto;background:var(--hint);border-color:var(--hint)">Switch to my data</span></div>
<div class="label">Activity · sample org "northwind"</div><h1 style="margin-top:10px">What a working setup looks like</h1>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px">
 <div class="card" style="padding:20px"><div class="label">Devices</div><div style="font-family:'Instrument Serif',serif;font-size:40px">12</div><div class="sub" style="margin:0">sample devices</div></div>
 <div class="card" style="padding:20px"><div class="label">Policies on</div><div style="font-family:'Instrument Serif',serif;font-size:40px">3</div><div class="sub" style="margin:0">sample policies</div></div>
 <div class="card" style="padding:20px"><div class="label">Blocked today</div><div style="font-family:'Instrument Serif',serif;font-size:40px">27</div><div class="sub" style="margin:0">sample lookups</div></div></div>
<div class="card" style="margin-top:16px;padding:6px 0">
 <div class="label" style="padding:12px 22px;display:grid;grid-template-columns:120px 1fr 220px 110px 140px">Time<span>Domain</span><span>Policy</span><span>Result</span><span></span></div>
 <div style="padding:12px 22px;border-top:1px solid var(--line);display:grid;grid-template-columns:120px 1fr 220px 110px 140px;align-items:center"><span class="mono">09:41</span><span class="mono">login-verify.example</span><span>Block security threats</span><span class="pill warn">Blocked</span><span style="color:var(--hint)">Why? →</span></div>
 <div style="padding:12px 22px;border-top:1px solid var(--line);display:grid;grid-template-columns:120px 1fr 220px 110px 140px;align-items:center"><span class="mono">09:40</span><span class="mono">docs.example</span><span style="color:var(--muted)">No match</span><span class="pill ok">Allowed</span><span></span></div>
 <div style="padding:12px 22px;border-top:1px solid var(--line);display:grid;grid-template-columns:120px 1fr 220px 110px 140px;align-items:center"><span class="mono">09:38</span><span class="mono">free-prize.example</span><span>Block security threats</span><span class="pill warn">Blocked</span><span style="color:var(--hint)">Why? →</span></div>
 <div style="padding:12px 22px;border-top:1px solid var(--line);display:grid;grid-template-columns:120px 1fr 220px 110px 140px;align-items:center"><span class="mono">09:35</span><span class="mono">intranet.northwind.example</span><span>Staff only (Access)</span><span class="pill ok">Allowed</span><span></span></div>
</div>
<div style="margin-top:18px;display:flex;gap:10px"><span class="btn ghost">Copy "Block security threats" to my org as a draft</span></div>''')
# 5 AI helper
S['05_ai_setup_helper']=page("Setup helper","Devices",'''
<div style="display:grid;grid-template-columns:1fr 470px;gap:28px;height:100%">
 <div><div class="label">Devices</div><h1 style="margin-top:10px">Devices</h1><p class="sub">No devices yet.</p>
  <div class="card" style="margin-top:26px;padding:40px;text-align:center;color:var(--muted)">Your first device will show here once it enrolls.<div style="margin-top:16px"><span class="btn ghost">Run enrollment check</span></div></div></div>
 <aside class="card" style="padding:0;display:flex;flex-direction:column;overflow:hidden">
  <div style="padding:16px 20px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:10px"><b>Setup helper</b><span class="pill mute">Reads your settings · changes nothing without you</span></div>
  <div style="padding:20px;display:flex;flex-direction:column;gap:14px;flex:1">
   <div style="align-self:flex-end;background:var(--ink);color:#fff;border-radius:14px 14px 4px 14px;padding:10px 14px;max-width:85%">My laptop says "Enrollment request is invalid". Why?</div>
   <div style="background:var(--soft);border-radius:14px 14px 14px 4px;padding:14px 16px;max-width:95%">Your org has no device enrollment rule yet, so every device is refused before sign-in.<div style="margin-top:10px">Team name and login method look fine.</div>
    <div style="margin-top:12px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px"><div class="label">Proposed change</div><div style="margin-top:4px">Allow devices for emails ending in <b>@acme.example</b></div><div style="display:flex;gap:8px;margin-top:10px"><span class="btn" style="padding:7px 12px">Review and apply</span><span class="btn ghost" style="padding:7px 12px">Not now</span></div></div>
    <div style="margin-top:10px;font-size:13px;color:var(--muted)">Source: Device enrollment permissions (docs) · Checked: your enrollment settings</div></div>
  </div>
  <div style="padding:14px 20px;border-top:1px solid var(--line);color:var(--muted)">Ask about your setup…</div>
 </aside></div>''')
for k,v in S.items(): open(k+'.html','w').write(v)
print(list(S))
