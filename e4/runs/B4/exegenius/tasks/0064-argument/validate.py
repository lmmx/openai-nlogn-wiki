import json,re,sys
src=open('sources/paper.tex').read()
ans=json.load(open('exegenius/tasks/0064-argument.answer.json'))
order="""multitape-model nlogn-conjecture fixed-point-arithmetic established-multiplier address-fields-volume stream-ops controlled-shifts linear-algebra-basics tensor-products address-shear f2-vectors bilinear-orthogonality subset-pairing-formulas scalar-exchange-network network-frames row-splitting-roles subspace-labels-rank-saving rank-deficit-recurrence bit-network-interface lower-factorization matrix-shear-cost fixed-tape-dfs-schedule power-width-interchange chunk-swap packed-rotations exceptional-address-repair packed-selected-bit-addition polynomial-ring-negacyclic dft synthetic-roots fft-butterfly phase-kernel complex-network-interface phase-frame-layer multidim-dft synthetic-transform frequency-order contraction-error-budget disk-grid-truncation guard-width simultaneous-layer transform-layout signed-packing gaussian-resampling tensor-resampling cyclic-convolution multiplication-as-convolution bluestein-chirp source-permutation-cancel synthetic-convolution parameter-choice crt-address-map prime-lengths coefficient-twist chirp-transform source-transform exact-recovery multiplication-algorithm cost-analysis main-theorem""".split()
idx={p:i for i,p in enumerate(order)}
known="""big-o polynomials complex-numbers turing-tapes asymptotic-notation-beyond-big-o logarithms-exponentials-floors-and-ceilings binary-and-radix-b-representation-of-integers schoolbook-multiplication-and-karatsuba divisibility-primes-and-gcd modular-arithmetic-and-residue-classes roots-of-unity recurrences-and-geometric-series induction-and-elementary-proof-technique elementary-counting-and-the-union-bound sorting-and-radix-sort permutations-and-bijections sets-products-of-ranges-and-lexicographic-order matrix-transposition-and-row-major-storage triangle-inequality-and-error-bounds boolean-and-arithmetic-circuits-as-networks graphs-paths-and-neighbors stacks-and-recursion fast-fourier-transform-and-karatsuba-as-survey-knowledge real-and-imaginary-parts-rounding-and-truncation dot-product-vectors-over-the-rationals-and-orthonormal-bases""".split()
errs=[]
pages={}; ids=set(); fromsused=set(); last=-1
def walk(n,anc_page,par):
    global last
    if n['id'] in ids: errs.append('dup id '+n['id'])
    ids.add(n['id'])
    pg=n.get('page') or anc_page
    if n.get('page'):
        if n['page'] in pages: errs.append('page reused '+n['page'])
        pages[n['page']]=n['id']
        if par and idx[n['page']]>=idx[anc_page]: errs.append(f"page order: {n['page']} under {anc_page}")
    for f in n.get('from',[]):
        fromsused.add(f)
        if f in known: continue
        if f not in idx: errs.append('unknown from '+f); continue
        if idx[f]>=idx[pg]: errs.append(f"from {f} not before page {pg} at {n['id']}")
    for c in [n.get('claim','')]:
        if c.count('$')%2: errs.append('odd $ in claim '+n['id'])
    for k in ['\t','\n','\x0c','\r','\x08']:
        if k in json.dumps(n.get('claim',''))+n.get('method','') if False else False: pass
    s=json.dumps(n)
    if re.search(r'\\u000[0-9a-f]',s): errs.append('control char in '+n['id'])
    if n['intention']=='infer':
        q=n['quote']['quote']
        c=src.count(q)
        if c!=1: errs.append(f"quote count {c} at {n['id']}: {q[:50]}")
        pos=src.find(q)
        if not n.get('deferred'):
            if pos<last: errs.append(f"order violation at {n['id']} pos {pos} < {last}")
            last=max(last,pos)
        if n.get('children'): errs.append('infer w children')
    else:
        m=n['motivation']
        if m['source']=='explicit':
            if not m.get('quote'): errs.append('explicit w/o quote '+n['id'])
            else:
                q=m['quote']['quote']
                if src.count(q)<1: errs.append(f"mot quote missing {n['id']}: {q[:50]}")
        elif m.get('quote'): errs.append('quote on non explicit '+n['id'])
        if not n.get('children'): errs.append('show w/o children '+n['id'])
        # adds
        desc=[]
        def collect(x):
            for c in x.get('children',[]):
                desc.append(c); collect(c)
        collect(n)
        math=' '.join(' '.join(re.findall(r'\$(.*?)\$',d['claim'])) for d in desc)
        for a in n.get('adds',[]):
            if a['symbol'] not in math: errs.append(f"add {a['symbol']} not in descendants of {n['id']}")
    for c in n.get('children',[]): walk(c,pg,n)
r=ans['root']
if r.get('page')!='main-theorem': errs.append('root page')
walk(r,'main-theorem',None)
covered=set(pages)|fromsused
for p in order:
    if p not in covered: errs.append('page not covered: '+p)
print('pages with steps',len(pages)); print('\n'.join(errs) or 'OK')
