import re, json, sys
sys.path.insert(0,'.')
import build4
from lib import *
PAGES = """convolution-multiplication negacyclic-ring hvdh-multiplier multitape-streams controlled-shifts bank-exchange-network linear-algebra-spaces frames-on-arrays subspace-labels recursive-power-saving bit-shear-interface lower-triangular-factorization matrix-shear-cost power-width-interchange chunk-interchange phase-frames packed-selected-bit-addition fixed-point-precision guard-bits signed-kronecker-packing discrete-fourier-transform radix-two-fft synthetic-transforms simultaneous-butterfly-layer synthetic-transform-layout synthetic-convolution coefficient-twist gaussian-resampling bluestein-chirp permutation-cancellation tensor-resampling crt-cyclic-convolution parameter-choice multiplication-algorithm exact-recovery time-bound-accounting multiplication-below-nlogn""".split()
KNOWN = """big-o polynomials complex-numbers turing-machines modular-arithmetic-and-congruences primes-coprimality-and-gcd euclidean-algorithm-and-modular-inverses trial-division-and-primality-search binary-representation-bit-strings-and-xor radix-representation-and-carry-propagation logarithms-floor-and-ceiling recurrences-and-induction divide-and-conquer-multiplication permutations-and-bijections matrices-invertibility-and-rank gaussian-elimination vector-spaces-bases-and-dimension cartesian-products-and-lexicographic-order rational-numbers-and-dyadic-fractions norms-absolute-value-and-triangle-inequality euler-s-formula-and-roots-of-unity rounding-and-square-roots polynomial-time-and-computational-cost-on-tapes fast-fourier-transform-as-a-known-algorithm""".split()
PIDX = {p:i for i,p in enumerate(PAGES)}
root = build4.ROOT
ids=set(); pages_used={}; fromset=set(); last=0; errs=[]
def descend(n, eff, anc_claims):
    if n['id'] in ids: errs.append("dup id "+n['id'])
    ids.add(n['id'])
    pg = n.get('page') or eff
    if n.get('page'):
        if n['page'] in pages_used: errs.append("page reused "+n['page'])
        pages_used[n['page']]=n['id']
    for f in n.get('from',[]):
        fromset.add(f)
        if f in PIDX:
            if PIDX[f] >= PIDX[pg]: errs.append(f"from {f} not before page {pg} at {n['id']}")
        elif f not in KNOWN: errs.append("unknown from "+f)
    global last
    if n['intention']=='infer':
        q=n['quote']
        if not n.get('deferred'):
            if q['_line'] < last: errs.append(f"order {n['id']} line {q['_line']} < {last}")
            last = max(last,q['_line'])
        if n.get('children'): errs.append("infer with children "+n['id'])
    else:
        if not n.get('children'): errs.append("show without children "+n['id'])
        # adds check
        allclaims = " ".join(collect(n))
        maths = " ".join(re.findall(r'\$(.+?)\$', allclaims))
        for a in n.get('adds',[]):
            sym=a['symbol']
            if sym not in maths: errs.append(f"adds {sym} at {n['id']} not in claims below")
        for c in n['children']: descend(c, pg, anc_claims)
def collect(n):
    out=[]
    for c in n.get('children',[]):
        out.append(c['claim']); out+=collect(c)
    return out
descend(root,'multiplication-below-nlogn',[])
for p in PAGES:
    if p not in pages_used and p not in fromset: errs.append("page without step and not in from: "+p)
if pages_used.get('multiplication-below-nlogn')!='S0': errs.append("target page")
print("\n".join(errs) or "OK")
print(len(ids),"nodes; pages with steps",len(pages_used))
# control chars
txt=json.dumps(build4.strip(root))
for ch in ['\r','\t','\x08','\x0c']:
    if ch in json.dumps(build4.strip(root), ensure_ascii=False): print("CTRL",repr(ch))
def walk(o):
    if isinstance(o,dict):
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
    elif isinstance(o,str): yield o
bad=[s for s in walk(build4.strip(root)) if any(ord(c)<32 for c in s)]
print("ctrl-char strings:",bad[:3])
