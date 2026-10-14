import json, re
ans = json.load(open('../0003-argument.answer.json'))
pages = """fixed-tape-model nlogn-conjecture nlogn-multiplier array-order stream-ops controlled-shifts matrix-basics network frames subset-labels rank-saving bit-network lower-triangular matrix-shear power-saving-recurrence power-interchange chunk-interchange packed-bit-addition polynomial-ring-mod kronecker-packing cyclic-convolution int-as-convolution dft butterfly-fft phase-network fixed-point-disk-grid negacyclic-twist simultaneous-layer convolution-theorem multidim-transform synthetic-transform gaussian-resampling chirp-identity permutation-cancellation transform-layout ring-convolution crt-axis-map prime-lengths complex-convolution source-transform exact-recovery mult-algorithm parameter-balance main-theorem""".split()
known = """big-o polynomials complex-numbers tape-machines asymptotic-notation-beyond-big-o logarithms-and-exponentials floor-ceiling-and-rounding proof-by-induction-and-recursion sets-subsets-and-basic-combinatorics functions-bijections-and-permutations graphs modular-arithmetic primes-coprimality-and-gcd binary-field-f2-and-xor positional-number-representation-and-carries dyadic-rationals-and-binary-fractions exponential-function-and-gaussian-function vectors-matrices-and-linear-maps vector-norms-and-error-bounds boolean-gates-and-circuits determinism-and-exact-versus-approximate-computation""".split()
idx = {p:i for i,p in enumerate(pages)}
ids = set(); used_pages = {}; used_from = set(); errs = []
def walk(n, curpage, depth=0):
    if n['id'] in ids: errs.append('dup id '+n['id'])
    ids.add(n['id'])
    pg = n.get('page') or curpage
    if n.get('page'):
        if n['page'] in used_pages: errs.append('page twice '+n['page'])
        used_pages[n['page']] = n['id']
    for f in n.get('from', []):
        used_from.add(f)
        if f in known: continue
        if f not in idx: errs.append('bad from %s in %s' % (f, n['id'])); continue
        if idx[f] >= idx[pg]: errs.append('from %s not before page %s at %s' % (f, pg, n['id']))
    if n['intention'] == 'show':
        if not n.get('method') or not n.get('motivation'): errs.append('show lacks method/mot '+n['id'])
        if not n.get('children'): errs.append('show without children '+n['id'])
        if n['motivation']['source']=='explicit' and not n['motivation'].get('quote'): errs.append('explicit w/o quote '+n['id'])
    else:
        if n.get('children'): errs.append('infer with children '+n['id'])
        if not n.get('quote'): errs.append('infer w/o quote '+n['id'])
    # adds occurrence
    for a in n.get('adds', []):
        sym = a['symbol']
        found = False
        def claims(m):
            yield m['claim']
            for c in m.get('children', []): yield from claims(c)
        for c in n.get('children', []):
            for cl in claims(c):
                maths = re.findall(r'\$(.*?)\$', cl)
                if any(sym in mm for mm in maths): found = True
        if not found: errs.append('adds symbol %s not in descendants of %s' % (sym, n['id']))
    for c in n.get('children', []): walk(c, pg, depth+1)
walk(ans['root'], None)
if ans['root'].get('page') != 'main-theorem': errs.append('root page')
for p in pages:
    if p not in used_pages and p not in used_from: errs.append('page unused '+p)
print('nodes', len(ids), 'pages as steps', len(used_pages))
print('\n'.join(errs) if errs else 'OK')
