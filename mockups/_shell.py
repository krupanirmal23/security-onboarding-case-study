def page(title, active, body, extra_css=""):
    nav=[("Setup","Get started"),("Setup","Sample data"),("Protect","Policies"),("Protect","Devices"),("Protect","People & login"),("See","Activity"),("See","Settings")]
    side=""; last=None
    for g,n in nav:
        if g!=last: side+=f'<div class="grp">{g}</div>'; last=g
        side+=f'<a class="{"on" if n==active else ""}">{n}</a>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>{extra_css}</style><title>{title}</title></head>
<body><div class="top"><div class="mark"></div><div class="brand">Zero Trust console</div><div class="org">acme-it · Free plan</div><div class="concept">Concept mockup · synthetic data · not a Cloudflare screen</div></div>
<div class="wrap"><nav class="side">{side}</nav><main>{body}</main></div></body></html>'''
