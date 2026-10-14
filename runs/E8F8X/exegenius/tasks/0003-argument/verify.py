import json,re,sys
R='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F8X'
tree=json.load(open(R+'/exegenius/tasks/0003-argument.answer.json'))['root']
md=open(R+'/exegenius/tasks/0003-argument.md').read()
sec=md.split('## Pages, in reading order')[1].split('## Concepts the reader knows')[0]
pages=re.findall(r'^- `([a-z0-9-]+)`:',sec,re.M)
conc=re.findall(r'^- `([a-z0-9-]+)`:',md.split('## Concepts the reader knows')[1].split('## Sources')[0],re.M)
order={p:i for i,p in enumerate(pages)}
ids=set();pagesused={};fromused=set();errs=[]
def ctrl(s,where):
    if re.search(r'[\x00-\x08\x0b-\x1f]',s) or '\t' in s or '\n' in s and where!='quote':
        errs.append(('control char',where,s[:60]))
def math_of(n):
    out=[]
    out+=re.findall(r'\$(.*?)\$',n['claim'],re.S)
    for c in n.get('children',[]): out+=math_of(c)
    return out
def walk(n,eff,depth=0):
    if n['id'] in ids: errs.append(('dup id',n['id']))
    ids.add(n['id'])
    for k in ('claim','method'):
        if n.get(k): ctrl(n[k],n['id']+k)
    if n.get('motivation'): ctrl(n['motivation']['text'],n['id']+'mot')
    if n.get('salient'): ctrl(n['salient'],n['id']+'sal')
    pg=n.get('page')
    if pg:
        if pg in pagesused: errs.append(('page dup',pg,n['id'],pagesused[pg]))
        pagesused[pg]=n['id']
        if pg not in order: errs.append(('bad page',pg))
        eff=pg
    for f in n.get('from',[]):
        fromused.add(f)
        if f in order:
            if order[f]>=order[eff]: errs.append(('from not earlier',n['id'],f,eff))
        elif f not in conc: errs.append(('bad from',n['id'],f))
    if n['intention']=='show':
        if not n.get('method') or not n.get('motivation') or not n.get('children'): errs.append(('show incomplete',n['id']))
        m=n['motivation']
        if m['source']=='explicit' and not m.get('quote'): errs.append(('explicit w/o quote',n['id']))
    else:
        if n.get('children'): errs.append(('infer with children',n['id']))
        if not n.get('quote') or n['quote']['quote']=='MISSING': errs.append(('missing quote',n['id']))
    for b in n.get('adds',[]):
        sym=b['symbol']
        ms=[]
        for c in n.get('children',[]): ms+=math_of(c)
        if not any(sym in m for m in ms): errs.append(('adds symbol not in math below',n['id'],sym))
    for c in n.get('children',[]): walk(c,eff,depth+1)
walk(tree,tree.get('page'))
for p in pages:
    if p not in pagesused and p not in fromused: errs.append(('page unused',p))
if tree.get('page')!='main-theorem': errs.append('root page')
print('pages with step',len(pagesused),'concept-only',[p for p in pages if p not in pagesused])
print('nodes',len(ids))
for e in errs: print(e)
