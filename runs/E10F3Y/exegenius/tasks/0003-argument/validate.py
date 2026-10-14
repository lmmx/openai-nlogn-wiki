import json, re, sys
sys.path.insert(0,'/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F3Y/exegenius/tasks/0003-argument')
from build import PAGES, CONCEPTS, PIDX, SRC
ans=json.load(open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F3Y/exegenius/tasks/0003-argument.answer.json'))
root=ans['root']
errs=[]
ids=set()
pages_used={}
from_used=set()
last=-1
def math_of(text):
    return ' '.join(re.findall(r'\$(.+?)\$', text, re.S))
def walk(n, effpage, anc_adds, path):
    global last
    if n['id'] in ids: errs.append('dup id '+n['id'])
    ids.add(n['id'])
    pg=n.get('page') or effpage
    if n.get('page'):
        if n['page'] in pages_used: errs.append('page reused '+n['page'])
        pages_used[n['page']]=n['id']
    for f in n.get('from',[]):
        if f in CONCEPTS: continue
        if f not in PIDX: errs.append(f"{n['id']}: bad from {f}"); continue
        from_used.add(f)
        if PIDX[f] >= PIDX[pg]: errs.append(f"{n['id']}: from {f} not before page {pg}")
    if n['intention']=='infer':
        q=n['quote']['quote']
        c=SRC.count(q)
        if c==0: errs.append(f"{n['id']}: quote not found: {q[:70]}")
        else:
            if c>1: errs.append(f"{n['id']}: quote not unique ({c}): {q[:70]}")
            pos=SRC.find(q)
            if not n.get('deferred'):
                if pos<last: errs.append(f"{n['id']}: out of order pos {pos} < {last}: {q[:60]}")
                last=max(last,pos)
        if n.get('children'): errs.append(n['id']+' infer with children')
    else:
        if not n.get('children'): errs.append(n['id']+' show without children')
        m=n['motivation']
        if m['source']=='explicit':
            if not m.get('quote'): errs.append(n['id']+' explicit no quote')
            else:
                q=m['quote']['quote']
                if SRC.count(q)==0: errs.append(f"{n['id']}: mot quote not found: {q[:70]}")
        for c in n['children']:
            walk(c,pg,anc_adds,path+[n['id']])
        # adds check
        desc=[]
        def collect(x):
            for c in x.get('children',[]):
                desc.append(c['claim']); collect(c)
        collect(n)
        mm=math_of(' '.join(desc))
        for a in n.get('adds',[]):
            if a['symbol'] not in mm: errs.append(f"{n['id']}: add {a['symbol']} not in descendants' math")
walk(root,'main-theorem',[],[])
for p in PAGES:
    if p not in pages_used and p not in from_used: errs.append('page uncovered '+p)
print(len(ids),'nodes'); print('\n'.join(errs) if errs else 'OK')
