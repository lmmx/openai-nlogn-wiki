import json, sys, re
sys.path.insert(0, '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E9F2Y/exegenius/tasks/0003-argument')
import build
SRC = build.SRC
root = build.ROOT

pages_order = """n-log-n-conjecture radix-digit-convolution triple-gadget bank-exchange-network fixed-tape-model nlogn-subroutine stream-arrays frames controlled-shifts bilinear-orthogonal subspace-labels triangular-factorization matrix-shear power-width-interchange chunk-swap packed-selected-bits negacyclic-ring signed-kronecker-packing fixed-point-disk-grid dft-cyclic-convolution multidim-transform crt-axis-map gaussian-resampling bluestein-chirp coefficient-twist synthetic-transform butterfly-layers phase-kernel-network simultaneous-butterfly-layer transform-layout ring-convolution resampling-no-sort chirp-permutation-cancel parameter-choice source-transform exact-recovery multiplication-algorithm cost-accounting main-theorem""".split()
pidx = {p: i for i, p in enumerate(pages_order)}
known = """big-o polynomials complex-numbers turing-machine-tapes modular-arithmetic-and-residues primes-divisibility-gcd-and-coprimality binary-representation-of-integers bitwise-xor logarithms-floors-ceilings-and-powers-of-two matrices-invertibility-and-rank vector-spaces-basis-and-dimension permutations-and-permutation-matrices lexicographic-order-and-index-tuples euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle geometric-series-and-orthogonality-of-sums-of-roots-of-unity norms-and-the-triangle-inequality rational-numbers-dyadic-rationals-and-exact-arithmetic algebraic-structures-groups-rings-and-isomorphisms discrete-math-proof-techniques schoolbook-multiplication-and-divide-and-conquer-multiplication multitape-machine-cost-model-and-linear-time-scans complex-polynomial-evaluation-and-interpolation gaussian-function convolution-as-polynomial-multiplication quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o""".split()

errs = []
ids = set()
pages_used = {}
from_used = set()
last = 0
lastq = None


def walk(n, parent_page):
    global last, lastq
    if n['id'] in ids:
        errs.append("dup id " + n['id'])
    ids.add(n['id'])
    pg = n.get('page') or parent_page
    if n.get('page'):
        if n['page'] in pages_used:
            errs.append("page reused %s by %s and %s" % (n['page'], pages_used[n['page']], n['id']))
        pages_used[n['page']] = n['id']
        if n['page'] not in pidx:
            errs.append("bad page " + n['page'])
    for f in n.get('from', []):
        from_used.add(f)
        if f in pidx:
            if pidx[f] >= pidx[pg]:
                errs.append("from %s not before page %s at %s" % (f, pg, n['id']))
        elif f not in known:
            errs.append("unknown from %s at %s" % (f, n['id']))
    if n['intention'] == 'infer':
        q = n['quote']['quote']
        c = SRC.count(q)
        if c == 0:
            errs.append("QUOTE NOT FOUND %s: %r" % (n['id'], q))
        else:
            if c > 1:
                errs.append("warn: quote not unique (%d) %s: %r" % (c, n['id'], q[:60]))
            pos = SRC.find(q)
            if not n.get('deferred'):
                # find first occurrence at/after last
                p2 = SRC.find(q, last)
                if p2 < 0:
                    errs.append("ORDER VIOLATION %s: %r (after %r) first pos %d last %d" % (n['id'], q[:50], lastq, pos, last))
                else:
                    last = p2 + len(q)
                    lastq = q[:40]
        if n.get('children'):
            errs.append("infer with children " + n['id'])
    else:
        m = n.get('motivation')
        if not m:
            errs.append("no motivation " + n['id'])
        elif m['source'] == 'explicit':
            if not m.get('quote'):
                errs.append("explicit w/o quote " + n['id'])
            else:
                if SRC.count(m['quote']['quote']) == 0:
                    errs.append("MOTIVATION QUOTE NOT FOUND %s: %r" % (n['id'], m['quote']['quote']))
        for ch in n['children']:
            walk(ch, pg)
        # adds
        for a in n.get('adds', []):
            sym = a['symbol']
            found = False

            def desc(x):
                yield x
                for c in x.get('children', []):
                    yield from desc(c)
            for d in desc(n):
                if d is n:
                    continue
                if sym in d['claim']:
                    found = True
            if not found:
                errs.append("adds symbol %s not in descendants of %s" % (sym, n['id']))


walk(root, None)
for p in pidx:
    if p not in pages_used and p not in from_used:
        errs.append("page %s neither used nor in from" % p)
for p in pages_used:
    pass
print("pages with steps:", len(pages_used))
print("pages not stepped:", [p for p in pidx if p not in pages_used])
for e in errs:
    print(e)
print("nodes:", len(ids))
