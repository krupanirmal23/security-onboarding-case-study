"""Builds data/signals.csv. Every row was read and tagged by hand from a public page.
Usernames are left out. Team names, domains and account IDs inside excerpts are replaced with [team] / [id].
Stages: S1 account & team setup, S2 identity / login method, S3 device enrollment, S4 first policy, S0 cross-stage.
Clusters (friction rows only):
  ENROLL_PREREQ  device enrollment fails with an opaque error; the stated or suggested fix is a missing enrollment policy or login method
  POLICY_VERIFY  first policy appears not to work, or the admin cannot confirm traffic is protected
  CONSOLE_NAV    lost in the console or docs: navigation, docs vs UI mismatch, too many concepts, learning curve
  SIGNUP_PLAN    blocked while creating the team or checking out the Free plan
  IDP_LOGIN      identity provider or login errors not explained by an enrollment policy
  POLICY_BUILD   cannot work out how to build the policy they want, or the first policy blocks the wrong thing
  MDM_DEPLOY     scripted / MDM rollout of the client
  CERT_TLS       certificate or TLS inspection breaks traffic
  ROAMING        client connectivity on hotel / airline / public Wi-Fi
Positive rows have cluster POSITIVE and are kept to show the other side of the sample."""
import csv, collections
ACC = "2026-11-11"
X = "https://x.com/i/status/"
CC = "https://community.cloudflare.com/t/"
R = []
def add(src, date, prec, url, stage, cluster, fit, excerpt): R.append([src, date, prec, url, stage, cluster, fit, excerpt])
# ---- X (search_posts_all via the x tools; raw JSON in raw/, not published)
add("X","2026-11-06","day",X+"2118542997625462832","S0","CONSOLE_NAV","unclear","Cloudflare Zero Trust config is a big challenge for normal user. Confusing")
add("X","2022-10-11","day",X+"1579972286500982784","S4","POLICY_BUILD","personal","Got @Cloudflare zero trust tunnel setup for my homelab. Not too straightforward but also not hard. ... cant figure out how to require auth for connecting to tunnel though.")
add("X","2022-07-15","day",X+"1547933833294557187","S1","SIGNUP_PLAN","unclear","whilst trying the onboarding process for CF Zero Trust, I am experiencing an error when choosing the team name.")
add("X","2024-11-19","day",X+"1858905119339016490","S4","POLICY_BUILD","personal","Protected the ai using cloudflare zero trust. Now even I cant access it, trying to find the documentation.")
add("X","2023-05-05","day",X+"1654351244360839169","S0","CONSOLE_NAV","industry","Zero Trust is hard to sell without channel support. Needs hand-holding.")
add("X","2025-06-13","day",X+"1933643142772781338","S3","POSITIVE","org","With the nightmare that Cisco secure client is to install and configure using Intune ... I have @cloudflare zero trust a go. Lovely breath of fresh air - easy install, great documentation and crazy powerful.")
add("X","2023-09-10","day",X+"1700714362242265446","S0","POSITIVE","unclear","I appreciate @Cloudflare zero trust documentation..")
# ---- Reddit (read through web search results; direct Reddit fetches returned 403)
RD="https://www.reddit.com/r/"
add("Reddit r/CloudFlare","2026-09","month (page shows '2mo ago'; first reply 2026-09-07)",RD+"CloudFlare/comments/1w9hogl/cloudflare_ztna_warpcloudflared_initial_setup/","S0","CONSOLE_NAV","org","Followed the Cloudflare \"wizard\" config/setup experience... Started getting slightly lost amongst various IDP, Tunnel, User, Device, Policy, etc options... Nothing seems to match the actual user interface. Not YT vids. Not Cloudflare's own documentation.")
add("Reddit r/CloudFlare (comment)","2026-09-07","day",RD+"CloudFlare/comments/1w9hogl/cloudflare_ztna_warpcloudflared_initial_setup/","S0","CONSOLE_NAV","org","When I first start I also get overhelm of too much stuff and options and features.")
add("Reddit r/CloudFlare (comment)","2026-09-07","day",RD+"CloudFlare/comments/1w9hogl/cloudflare_ztna_warpcloudflared_initial_setup/","S0","CONSOLE_NAV","org","the documentation is not really beginner friendly - like do step 1 to 10 in order basis. The KB does works if you are already familiar with the steps.")
add("Reddit r/CloudFlare","2026-05","month (page shows '6mo ago')",RD+"CloudFlare/comments/1te9qk1/navigating_the_maze/","S0","CONSOLE_NAV","unclear","I am completely lost with this UI... I only find the right settings by pure accident.")
add("Reddit r/sysadmin","2024-11-18","day (first reply)",RD+"sysadmin/comments/1gtodxj/cloudflare_warp_zero_trust_happy_eyeballs_on/","S3","ROAMING","org","We are testing (hoping to deploy) Cloudflare Warp Zero Trust, generally works great. biggest issue is I keep running into Happy Eyeballs connection failures.")
add("Reddit r/sysadmin (comment)","2024-11-18","day",RD+"sysadmin/comments/1gtodxj/cloudflare_warp_zero_trust_happy_eyeballs_on/","S3","ROAMING","org","We have switched to MASQUE, have a longer auto connect, and our users have constant issues with captive portals.")
add("Reddit r/CloudFlare","2022-06-10","day (first reply)",RD+"CloudFlare/comments/v92pie/cloudflare_zero_trust_warp_setup/","S3","ENROLL_PREREQ","org","When I'm traying to connect devices in Cloudflare Zero Trust... Page getting stuck... Says that is added but the rule is not showing the table... Always getting this error")
add("Reddit r/CloudFlare (comment)","2022-06-10","day",RD+"CloudFlare/comments/v92pie/cloudflare_zero_trust_warp_setup/","S3","ENROLL_PREREQ","unclear","I kinda had similar error... What you ought to input is tesla only and not Tesla.cloudflareaccess.com")
add("Reddit r/CloudFlare","2024-07-14","day",RD+"CloudFlare/comments/1e34t8z/issue_with_device_enrollment_in_cloudflare_zero/","S3","ENROLL_PREREQ","personal","I encounter the \"Enrollment request is invalid\" error immediately after clicking the \"Login via Browser\" button. The problem occurs before reaching any authentication step")
add("Reddit r/CloudFlare (comment)","2025-10-08","day",RD+"CloudFlare/comments/1e34t8z/issue_with_device_enrollment_in_cloudflare_zero/","S2","IDP_LOGIN","unclear","[translated from Chinese] I have already defined the team name and edited device enrollment permissions... I filled in three different emails (from different providers) and cannot receive the one-time PIN.")
add("Reddit r/CloudFlare","2025-03","month (first reply 2025-03-08)",RD+"CloudFlare/comments/1j6clfh/how_to_enroll_a_device_in_a_zerotrust_team/","S3","ENROLL_PREREQ","personal","goes to Preference > Account > Login with Cloudflare Zero Trust, it immediately showed a screen said \"Forbidden, you dont have permission to view this\".")
add("Reddit r/CloudFlare","2025-04","month (first reply 2025-04-17)",RD+"CloudFlare/comments/1k19twq/zero_trust_access_policies_azure_groups_not/","S2","IDP_LOGIN","org","when I create an Access Policy, select the Azure group, then test the policy, the results show BLOCKED for us both. What have I missed?")
add("Reddit r/CloudFlare","2024-03","month (first reply 2024-03-21)",RD+"CloudFlare/comments/1bjvrcy/enabling_warp_gateway_selectors/","S4","POLICY_VERIFY","personal","My phone connects to my warp connection but does shows both warp and gateway off")
add("Reddit r/CloudFlare","2022-10","month (first reply 2022-10-16)",RD+"CloudFlare/comments/y5gpos/cloudflare_access_and_warpgatewayteams_policy/","S4","POLICY_VERIFY","personal","I see the enrolled device and the completed posture check for android version. But nothing from warp or gateway, even if the phone is connected.")
add("Reddit r/CloudFlare","2023-08","month (first reply 2023-08-16)",RD+"CloudFlare/comments/15siybn/should_i_install_cloudflare_root_certificate_on/","S3","CERT_TLS","personal","Should I install Cloudflare root certificate on iPhone?")
# ---- Cloudflare Community (public forum, read via its search JSON and topic pages)
add("Cloudflare Community","2023-03-08","day",CC+"481516","S3","ENROLL_PREREQ","unclear","when I configure the WARP client and enter team_name, it stated team name is invalid")
add("Cloudflare Community","2022-05-29","day",CC+"387171","S3","ENROLL_PREREQ","org","type my team name, click OK and get a message saying that team name is invalid or there is no device policy. But I believe that the team name is valid")
add("Cloudflare Community","2026-07-27","day",CC+"943310","S3","ENROLL_PREREQ","unclear","I cannot enroll my Apple Silicon Mac in a newly created C[loudflare Zero Trust org]... Enrollment request is invalid")
add("Cloudflare Community","2022-11-26","day",CC+"438431","S3","ENROLL_PREREQ","personal","whenever I try to login through WARP it gives me the error \"Invalid team name\", even though it's the correct name that I set up before.")
add("Cloudflare Community","2026-08-04","day",CC+"945601","S3","ENROLL_PREREQ","org","Enrolling any device via Cloudflare One Client fails with \"Enrollment request is invalid\" on Windows. New Zero Trust org... The error appears immediately after entering the team name.")
add("Cloudflare Community","2023-02-19","day",CC+"475196","S3","ENROLL_PREREQ","personal","having a few issues with that, specifically with \"Invalid Team Name\" when I try to connect from the device at the warp client")
add("Cloudflare Community","2023-05-26","day",CC+"514427","S3","ENROLL_PREREQ","personal","I stuck on the step on the app \"Login to Cloudflare Zero Trust\". I get \"Invalid Organization Name\".")
add("Cloudflare Community","2026-05-22","day",CC+"929227","S3","ENROLL_PREREQ","unclear","keep getting Enrollment rquest invalid error Added device enrollment, add login method but still get the error")
add("Cloudflare Community","2024-05-03","day",CC+"651456","S3","ENROLL_PREREQ","unclear","whenever I enter the team name into WARP, it takes me to a browser page that says \"Enrollment Request is Invalid\"")
add("Cloudflare Community","2026-07-08","day",CC+"938510","S3","ENROLL_PREREQ","org","fails with \"Enrollment request is invalid\" on both iOS (Cloudflare One Agent app) and Windows desktop client. New Zero Trust org")
add("Cloudflare Community","2026-09-14","day",CC+"958864","S3","ENROLL_PREREQ","unclear","The enrollment page shows \"Enrollment request is invalid\" immediately after entering the team name, before any login/authentication screen is ever shown.")
add("Cloudflare Community","2024-02-28","day",CC+"621728","S3","ENROLL_PREREQ","personal","I am blocked by a popup asking for an \"organization name\" which I assumed was my team name. But entering that in says an invalid name.")
add("Cloudflare Community","2026-09-08","day",CC+"956865","S3","ENROLL_PREREQ","org","New Zero Trust Free tenant ([id]). Enrolling any device fails immediately with \"Enrollment request is invalid\" - this happens before any login/authentication prompt appears")
add("Cloudflare Community","2026-05-22","day",CC+"929073","S3","ENROLL_PREREQ","personal","I try Cloudflare One and when I write Team name (don't understand how it's work)")
add("Cloudflare Community","2024-07-18","day",CC+"687191","S3","ENROLL_PREREQ","unclear","unabel to activate Zero Trust using [team].cloudflareaccess.com error Enrollment request is invalid")
add("Cloudflare Community","2025-05-31","day",CC+"803354","S2","ENROLL_PREREQ","unclear","When I try to login via the WARP client, I don't receive an email with my one-time PIN... The only email that this works for is the super user on my account. [Reply: the email address does not match the device enrollment policy.]")
add("Cloudflare Community","2026-11-09","day",CC+"978731","S4","POLICY_VERIFY","unclear","Gateway DNS block policy shows blocks in the logs, but the macOS Cloudflare One Client still returns the real IP, so blocked test sites load.")
add("Cloudflare Community","2026-09-08","day",CC+"956722","S4","POLICY_VERIFY","unclear","Gateway DNS location queries resolve but don't appear in logs — block policy not wo[rking]")
add("Cloudflare Community","2024-08-26","day",CC+"703578","S4","POLICY_VERIFY","unclear","have set up a block rule under Firewall policies for both DNS and HTTP traffic. However, it's not blocking any websites.")
add("Cloudflare Community","2022-11-16","day",CC+"435587","S4","POLICY_VERIFY","unclear","many of the domains I'm blocking with Policies utilizing Lists are still loading for me.")
add("Cloudflare Community","2022-10-07","day",CC+"425146","S4","POLICY_VERIFY","org","we are in the testing phase for Cloudflare Zero Trust. Specifically, we are using a free account and starting with basic DNS filtering [topic: Gateway No Traffic (DNS)]")
add("Cloudflare Community","2023-10-30","day",CC+"574584","S4","POLICY_VERIFY","org","we have a dns policy rule that dont allow adult content but... the gateway dns policy allowed a user to access a adult site. it shows up in the logs as allowed")
add("Cloudflare Community","2023-06-11","day",CC+"520301","S4","POLICY_VERIFY","unclear","placed many blocking policies under gateway. However i am still able to browse the blocked sites.")
add("Cloudflare Community (reply)","2026-01-26","day",CC+"520301","S4","POLICY_VERIFY","unclear","I set up a simple BLOCK policy for a domain to test, but I can still browse the site.")
add("Cloudflare Community","2026-03-25","day",CC+"910719","S4","POLICY_VERIFY","personal","I am a new user on the Free Plan attempting to set up Cloudflare Zero Trust for my family [topic: Cannot get the DNS blocking to work]")
add("Cloudflare Community","2023-03-18","day",CC+"486077","S4","POLICY_BUILD","org","I need to block approximate 3000 domains... I have created the policy but I can't find how I can block all the domains at once")
add("Cloudflare Community","2023-11-04","day",CC+"577045","S4","POLICY_BUILD","unclear","theverge.com being blocked by the \"Security Category\" > \"All security risks\" firewall policy")
add("Cloudflare Community","2025-10-12","day",CC+"846167","S4","POLICY_BUILD","personal","I cannot for the life of me figure out how to set up OTP access to my private services externally, i did it once ad cant figure ou[t]")
add("Cloudflare Community","2026-07-06","day",CC+"938020","S1","SIGNUP_PLAN","unclear","Unable to complete Cloudflare Zero Trust onboarding – \"Get Started\" button disabled")
add("Cloudflare Community (reply)","2026-07-06","day",CC+"938020","S1","SIGNUP_PLAN","unclear","all attempts to enable zero trust have failed at the payment screen after selecting the free account.")
add("Cloudflare Community","2022-07-17","day",CC+"399916","S1","SIGNUP_PLAN","unclear","onboarding stage seemingly hanging at the \"Create Team\" stage... [later: the UI does not have a clear way of showing when there is a name collision]")
add("Cloudflare Community","2026-11-06","day",CC+"977833","S1","SIGNUP_PLAN","unclear","Zero Trust Free onboarding completes but dashbord remains stuck on Welcome screen")
add("Cloudflare Community","2026-10-12","day",CC+"967927","S1","SIGNUP_PLAN","unclear","The Free checkout requires consent to recurring charges for usage exceeding free limits.")
add("Cloudflare Community","2026-11-04","day",CC+"976954","S1","SIGNUP_PLAN","unclear","The Zero Trust Free checkout shows $0/month and up[...] [topic: checkout overage consent and a strict $0 spending cap]")
add("Cloudflare Community","2021-02-08","day",CC+"242706","S1","SIGNUP_PLAN","unclear","I've seen several other posts about the same issue: Unable to \"Enable Access\".")
add("Cloudflare Community","2022-07-05","day",CC+"396648","S0","CONSOLE_NAV","org","I'm currently evaluating Cloudflare Zero Trust and having a concern about the separation of \"Tunnels\" and \"Applications\" concepts. [topic: too easy to make a costly mistake?]")
add("Cloudflare Community","2022-01-09","day",CC+"343697","S3","MDM_DEPLOY","org","after 20 hours of banging my head on the desk! Has anyone had experience deploying Warp Configuration files with MDM products on Mac OS?")
add("Cloudflare Community","2025-01-05","day",CC+"754684","S3","MDM_DEPLOY","org","zero touch configuration for iOS does not work... the VPN won't actually connect until the user opens the Cloudflare One app for the first time.")
add("Cloudflare Community","2025-04-08","day",CC+"787236","S2","IDP_LOGIN","unclear","Authentication Error. Failed to fetch user/group information from the identity provider. ... Verifying Cloudflare Warp account with Azure login")
add("Cloudflare Community","2025-10-13","day",CC+"846605","S2","IDP_LOGIN","unclear","[team].cloudflareaccess.com redirected you too many times. ... I want to activate the Cloudflare Zero Trust feature.")
add("Cloudflare Community","2025-01-16","day",CC+"758739","S2","IDP_LOGIN","org","Open WARP > Account > Login with cloudflare Zero Trust > enter team name > Get taken to logon page > Sign in with AzureAD > \"That account does not have access.\"")
add("Cloudflare Community","2021-11-11","day",CC+"325197","S4","CERT_TLS","unclear","Cloudflare Teams Access HTTPS Inspection Causing Stream Failures Across Wide Range of Sites")
# ---- G2 (public review page)
G2="https://www.g2.com/products/cloudflare-one-sase/reviews"
add("G2","not shown","none",G2,"S0","CONSOLE_NAV","org","Some settings are confusing at first, and figuring out why someone can't access a particular tool can take a little time. I'd like the setup process to be simpler, especially for people who don't work with security tools every day.")
add("G2","2026-10-26","day",G2,"S0","CONSOLE_NAV","org","Some settings can be confusing when you're first getting onboarded. Troubleshooting access issues can also take time when a rule blocks something unexpectedly.")
add("G2","2025-11-24","day",G2,"S0","CONSOLE_NAV","org","the dashboard can be confusing when you're first learning it. Policy setup sometimes takes more steps than expected")
add("G2","2025-10-14","day",G2,"S0","CONSOLE_NAV","org","its initial complexity, particularly when configuring advanced policies or integrating with other systems... the documentation and support sometimes fall behind.")
add("G2","2025-10-21","day (updated; submitted 2025-10-16)",G2,"S0","CONSOLE_NAV","org","While documentation is comprehensive, onboarding new users may still have a slight learning curve.")
add("G2","2025-10-13","day",G2,"S0","CONSOLE_NAV","org","the initial setup can feel a bit technical for teams that are new to SASE concepts.")
add("G2","2025-07-04","day",G2,"S0","CONSOLE_NAV","org","The learning curve can be steep when transitioning from traditional network security to Zero Trust architecture.")
add("G2","2025-06-22","day",G2,"S0","CONSOLE_NAV","org","steep learning curve, especially when combining multiple products like Zero Trust policies, Gateway rules, and Access applications. The documentation, can sometimes be fragmented across different products")
add("G2","2025-10-13","day",G2,"S4","POSITIVE","org","The dashboard is intuitive, and policies can be deployed within minutes.")
# ---- Gartner Peer Insights (public snippets only; full reviews need a login)
GP="https://www.gartner.com/reviews/product/cloudflare-one?marketSeoName=security-service-edge"
add("Gartner Peer Insights","2024-02-13","day",GP,"S0","CONSOLE_NAV","org","[review title, rated 3.0] Missing the Mark on Ease of Use and Management")
add("Gartner Peer Insights","not shown","none",GP,"S0","CONSOLE_NAV","org","High in cost, complex to use and implement, need experts for a integration and management.")
add("Gartner Peer Insights","2026-06-04","day",GP,"S0","POSITIVE","org","Easy to use platform, making it possible for us to work remotely and from different devices in a secure way.")
def keep(r): return r[6]!='personal' and not (r[1][:2]=='20' and r[1]<'2022')
EXC=[r for r in R if not keep(r)]; R=[r for r in R if keep(r)]
with open('data/excluded.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['source','date','date_precision','url','stage','cluster','persona_fit','excerpt','why_excluded','accessed'])
    for r in EXC: w.writerow(r+['personal / home use' if r[6]=='personal' else 'before 2022',ACC])
print('excluded',len(EXC))
with open('data/signals.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['n','source','date','date_precision','url','stage','cluster','persona_fit','excerpt','accessed'])
    for i,r in enumerate(R,1): w.writerow([i]+r+[ACC])
fr=[r for r in R if r[5]!='POSITIVE']
print('total',len(R),'friction',len(fr),'positive',len(R)-len(fr))
print('by source',collections.Counter(r[0].split(' (')[0].split(' r/')[0] for r in R))
print('clusters',collections.Counter(r[5] for r in fr).most_common())
print('stages (friction)',collections.Counter(r[4] for r in fr).most_common())
print('fit',collections.Counter(r[6] for r in R))
for c in ['ENROLL_PREREQ','POLICY_VERIFY','CONSOLE_NAV','SIGNUP_PLAN','IDP_LOGIN']:
    sub=[r for r in fr if r[5]==c]; print(c,'org',sum(r[6]=='org' for r in sub),'sources',collections.Counter(r[0].split(' (')[0] for r in sub))
d=[r[1] for r in R if r[1][:2]=='20']; print('dates',min(d),max(d))
