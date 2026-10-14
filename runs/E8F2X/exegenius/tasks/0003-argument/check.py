import json,re,sys
root=json.load(open('../0003-argument.answer.json'))['root']
src=open('../../../sources/paper.tex').read()
order=["n-log-n-conjecture","radix-digit-convolution","triple-gadget","bank-exchange-network","fixed-tape-model","nlogn-subroutine","stream-arrays","frames","controlled-shifts","bilinear-orthogonal","subspace-labels","triangular-factorization","matrix-shear","power-width-interchange","chunk-swap","packed-selected-bits","negacyclic-ring","signed-kronecker-packing","fixed-point-disk-grid","dft-cyclic-convolution","multidim-transform","crt-axis-map","gaussian-resampling","bluestein-chirp","coefficient-twist","synthetic-transform","butterfly-layers","phase-kernel-network","simultaneous-butterfly-layer","transform-layout","ring-convolution","resampling-no-sort","chirp-permutation-cancel","parameter-choice","source-transform","exact-recovery","multiplication-algorithm","cost-accounting","main-theorem"]
idx={p:i for i,p in enumerate(order)}
ids=set(); pos=0; errs=[]; used_pages=[]; frompages=set()
def walk(n,page,anc):
    global pos
    if n['id'] in ids: errs.append('dup id '+n['id'])
    ids.add(n['id'])
    pg=n.get('page') or page
    if n.get('page'):
        used_pages.append(n['page'])
    for f in n.get('from',[]):
        if f in idx:
            frompages.add(f)
            if idx[f]>=idx[pg]: errs.append(f"{n['id']}: from {f} not before page {pg}")
    if n['intention']=='show':
        if not n.get('children'): errs.append('show without children '+n['id'])
        m=n.get('motivation')
        if m and m['source']=='explicit':
            q=m['quote']['quote']
            if src.count(q)<1: errs.append(f"{n['id']} motivation quote missing: {q}")
        for c in n['children']: walk(c,pg,anc+[n])
        for b in n.get('adds',[]):
            sym=b['symbol']
            found=False
            def dd(x):
                for c in x.get('children',[]) or []:
                    yield c; yield from dd(c)
            for c in dd(n):
                for mm in re.findall(r'\$(.*?)\$',c['claim']):
                    if sym in mm: found=True
            if not found: errs.append(f"{n['id']}: adds {sym} not in descendants math")
    else:
        q=n['quote']['quote']
        c=src.count(q)
        if c==0: errs.append(f"{n['id']} quote missing: {q}")
        else:
            if c>1: errs.append(f"{n['id']} quote not unique ({c}): {q}")
            if not n.get('deferred'):
                p=src.find(q,pos)
                if p<0:
                    errs.append(f"{n['id']} OUT OF ORDER: {q}")
                    # show where
                    print('  at',src.find(q))
                else:
                    pos=p+len(q)
walk(root,None,[])
print('pages with steps',len(used_pages), len(set(used_pages)))
dup=[p for p in used_pages if used_pages.count(p)>1]
print('dup pages',set(dup))
missing=[p for p in order if p not in used_pages and p not in frompages]
print('missing',missing)
for e in errs: print(e)
