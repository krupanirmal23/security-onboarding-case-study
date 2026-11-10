"""Documented steps per onboarding stage, counted by hand from the Dashboard tab of each public doc page (accessed 2026-11-11).
Counting rule: one numbered instruction = one step. Lettered sub-steps are not counted separately.
Optional or conditional steps are counted in their own column. API and Terraform tabs are ignored."""
import csv
B="https://developers.cloudflare.com/cloudflare-one/"
S=[ # stage, path, page, section, required, optional, url
("1 Team setup","all paths","Get started","1. Create a Cloudflare account + 2. Create a Zero Trust organization",4,0,B+"setup/"),
("2 Identity","shortest (one-time PIN)","One-time PIN login","Set up OTP",3,0,B+"integrations/identity-providers/one-time-pin/"),
("2 Identity","Okta (App Catalog)","Okta","Set up Okta as an OIDC provider (Okta App Catalog)",9,0,B+"integrations/identity-providers/okta/"),
("2 Identity","Okta (custom app)","Okta","Set up Okta as an OIDC provider (Custom App Integration)",14,3,B+"integrations/identity-providers/okta/"),
("2 Identity","Microsoft Entra ID","Microsoft Entra ID","1. Obtain settings (12) + 2. API permissions (6) + 3. Add as IdP (6, plus 1 optional)",24,1,B+"integrations/identity-providers/entra-id/"),
("3 Device enrollment","all paths","Device enrollment permissions","Set device enrollment permissions",5,0,B+"team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/"),
("3 Device enrollment","desktop GUI, client 2026.2+","Manual deployment","Enroll using the GUI",6,0,B+"team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/"),
("3 Device enrollment","desktop CLI","Manual deployment","Enroll using the CLI",6,3,B+"team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/"),
("3 Device enrollment","iOS / Android / ChromeOS","Manual deployment","Enroll manually",8,1,B+"team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/"),
("4 First policy","Gateway DNS policy","DNS filtering","2. Verify device connectivity (5) + 3. Create your first DNS policy (6)",11,0,B+"traffic-controls/get-started/dns/"),
("4 First policy","Access policy for a private web app (guided)","Private web application","Steps 1-5 (9+3+2+2+3); step 6 is a review screen",19,4,B+"setup/secure-private-apps/private-web-app/"),
]
with open('data/documented_steps.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['stage','path','doc_page','section','required_steps','optional_or_conditional_steps','url','accessed'])
    for r in S: w.writerow(list(r)+['2026-11-11'])
g=lambda p: next(r[4] for r in S if r[1]==p)
short=g('all paths')+3+5+6+11
print('stage1',4,'| shortest: OTP 3, enroll perms 5 + GUI 6, DNS policy 11 ->',short)
print('Entra path:',4+24+5+6+11, '| Okta catalog path:',4+9+5+6+11)
