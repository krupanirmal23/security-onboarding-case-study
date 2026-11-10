"""Per-arm sample size for a two-sided test of two proportions (normal approximation).

    n = (z_(1-alpha/2) + z_(1-beta))^2 * (p1(1-p1) + p2(1-p2)) / (p2 - p1)^2

Every input is a placeholder the team must set from its own data. Nothing has a default.
Example (made-up inputs, only to show the call):
    python scripts/sample_size.py --baseline 0.X --mde 0.0Y --alpha A --power P --weekly-orgs W
"""
import argparse, math
from statistics import NormalDist
a=argparse.ArgumentParser()
a.add_argument('--baseline',type=float,required=True,help='p1: current activation rate within [N] days')
a.add_argument('--mde',type=float,required=True,help='smallest absolute lift worth shipping (p2 = p1 + mde)')
a.add_argument('--alpha',type=float,required=True); a.add_argument('--power',type=float,required=True)
a.add_argument('--weekly-orgs',type=float,help='eligible new orgs per week, both arms together')
x=a.parse_args()
p1,p2=x.baseline,x.baseline+x.mde
z=NormalDist().inv_cdf
n=math.ceil((z(1-x.alpha/2)+z(x.power))**2*(p1*(1-p1)+p2*(1-p2))/(p2-p1)**2)
print(f'per arm: {n}  total: {2*n}')
if x.weekly_orgs:
    w=math.ceil(2*n/x.weekly_orgs); print(f'weeks to enroll: {w} (+ the [N]-day activation window before reading the result)')
