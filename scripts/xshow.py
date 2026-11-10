import json,sys
for f in sys.argv[1:]:
    s=open(f).read(); d=json.loads(s[s.find('{'):s.rfind('}')+1])
    print('#####',f,len(d.get('data',[])))
    for p in d.get('data',[]): print(p['id'],p.get('created_at','')[:10],p['text'][:260].replace('\n',' '),'\n')
