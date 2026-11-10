# Getting a new IT admin to their first working policy

A product case study and PRD for onboarding in Cloudflare Zero Trust, written from public information only.

**Author:** Krupa Nirmal · November 2026

> **Before publishing:** Krupa, please check your NDA and any employer policies on public portfolio work before you make this repo or the carousel public.

Independent concept. Not affiliated with or endorsed by Cloudflare. The mockups use synthetic data and no Cloudflare logos or branding.

## The short version

- **Persona:** an IT admin at a 200–2,000 person company trying Zero Trust on the self-serve path.
- **First value:** one enrolled device whose traffic is checked by a policy the admin wrote.
- **Path today:** the shortest documented path takes 29 steps across 5 doc pages. With Entra ID as the identity provider it takes 50.
- **Biggest specific gap:** device enrollment permissions sit on a separate page that the Get started and DNS quick-start pages don't mention. "Enrollment refused" is the most specific public complaint (13 of 56 friction signals).
- **Proposal:**
  - A self-checking setup checklist.
  - An enrollment check before the first install.
  - A guided first policy you can prove on the test device.
  - Sample-data mode.
  - A read-only AI setup helper.
- **Measurement:**
  - North Star: activated accounts.
  - Guardrails: misconfiguration rate and security incidents.
  - Two A/B tests, sized with a formula. The team sets the inputs.

## Numbers in this repo

| What | Count | Where |
|---|---|---|
| Public signals kept | 60 (56 friction, 4 positive) | `data/signals.csv` |
| Signals excluded (14 personal or home use, 2 before 2022) | 16 | `data/excluded.csv` |
| By source | Cloudflare Community 33, Reddit 10, G2 9, X 5, Gartner Peer Insights 3 | |
| Friction clusters | 8 (the top 5 cover 50 of 56) | |
| Steps, shortest path (team 4 + one-time PIN 3 + enrollment 5 + desktop client 6 + DNS policy 11) | 29 | `data/documented_steps.csv` |
| Steps with Okta (App Catalog) / Entra ID | 35 / 50 | |
| Concept screens | 5 | `mockups/` |
| A/B tests | 2 | Case study, section 8 |

**Top clusters:**

| Cluster | Signals |
|---|---|
| Lost in the console or docs | 17 |
| Device refused at enrollment | 13 |
| First policy "isn't working" | 8 |
| Free-plan checkout and team creation | 7 |
| Sign-in method errors | 5 |

Everything was accessed on 11 Nov 2026. Each signal row has its source URL and date.

## Files

```
Case_Study_and_PRD.docx / .pdf   case study, PRD, metrics, experiments, sources
LinkedIn_Carousel.pdf            8 slides, 1080×1350
data/signals.csv                 60 coded public signals (no usernames)
data/excluded.csv                16 excluded signals and why
data/documented_steps.csv        step counts per stage and doc page
screens/                         screenshots of the public docs and plans page
mockups/                         5 concept screens (PNG + HTML source)
diagrams/                        journey map and metrics tree (PNG + source)
scripts/                         screenshot, signal-building, step-count and sample-size scripts
carousel/  build/                carousel and document build scripts
```

## Method

1. I read each docs page on the path from signup to first policy, using the Dashboard tab. I counted one numbered instruction as one step.
2. I searched Cloudflare Community, Reddit, G2, Gartner Peer Insights and X for setup problems. I kept posts from 2022 onward and dropped personal or home use.
3. I coded each signal by stage and cluster, on my own.

## Caveats

- **Sample bias:**
  - Forum posts come from people who got stuck.
  - One source is 33 of 60 signals.
  - For 28 of 60 I couldn't tell whether the poster was at a company.
  - The counts rank themes. They are not failure rates.
- **Not click-tested:** I didn't sign in to the product, so the journey comes from the docs.
- **Limited access:**
  - Full Gartner reviews are behind a login.
  - Reddit and Community posts were read through search and the public pages.
  - Some dates are month-level only.
- **Placeholders:** baselines, targets, the activation window [N], and the sample-size inputs are marked [Team to decide]. All outcomes are hypotheses.

Sample size per arm, for a two-proportion test:

```
python scripts/sample_size.py --baseline <p1> --mde <lift> --alpha <a> --power <1-b> --weekly-orgs <w>
```
