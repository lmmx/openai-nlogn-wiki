#!/usr/bin/env python3
"""Assemble the 0003-argument answer, validate it, and write the JSON."""
import sys, json, re, importlib
sys.path.insert(0, '.')
import lib
from lib import nsrc, nmap, norm, line_of_raw
import t_s5

OUT = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1SM/exegenius/tasks/0003-argument.answer.json'

PAGES = ['fixed-tape-model','nlogn-conjecture','nlogn-multiplier','array-order','stream-ops','controlled-shifts','matrix-basics','network','frames','subset-labels','rank-saving','bit-network','lower-triangular','matrix-shear','power-saving-recurrence','power-interchange','chunk-interchange','packed-bit-addition','polynomial-ring-mod','kronecker-packing','cyclic-convolution','int-as-convolution','dft','butterfly-fft','phase-network','fixed-point-disk-grid','negacyclic-twist','simultaneous-layer','convolution-theorem','multidim-transform','synthetic-transform','gaussian-resampling','chirp-identity','permutation-cancellation','transform-layout','ring-convolution','crt-axis-map','prime-lengths','complex-convolution','source-transform','exact-recovery','mult-algorithm','parameter-balance','main-theorem']
KNOWN = ['big-o','polynomials','complex-numbers','tape-machines','asymptotic-notation-beyond-big-o','logarithms-and-exponentials','floor-ceiling-and-rounding','proof-by-induction-and-recursion','sets-subsets-and-basic-combinatorics','functions-bijections-and-permutations','graphs','modular-arithmetic','primes-coprimality-and-gcd','binary-field-f2-and-xor','positional-number-representation-and-carries','dyadic-rationals-and-binary-fractions','exponential-function-and-gaussian-function','vectors-matrices-and-linear-maps','vector-norms-and-error-bounds','boolean-gates-and-circuits','determinism-and-exact-versus-approximate-computation']
PIDX = {p: i for i, p in enumerate(PAGES)}

def tidy(n):
    """Drop empty optional keys."""
    out = dict(n)
    if out['intention'] == 'show':
        out['children'] = [tidy(c) for c in out['children']]
    if 'from' in out:
        seen = []
        for x in out['from']:
            if x not in seen: seen.append(x)
        out['from'] = seen
    return out

def renumber(n, new_id):
    n['id'] = new_id
    if n['intention'] == 'show':
        for i, c in enumerate(n['children']):
            nid = 'K' if c['id'] == 'K' else '%s.%d' % (new_id, i + 1)
            renumber(c, nid)

def walk(n, anc_page=None, depth=0, parent=None):
    page = n.get('page') or anc_page
    yield n, page, depth, parent
    if n['intention'] == 'show':
        for c in n['children']:
            yield from walk(c, page, depth + 1, n)

def math_of(claim):
    return re.findall(r'\$(.+?)\$', claim, flags=re.S)

def descendants(n):
    if n['intention'] == 'show':
        for c in n['children']:
            yield c
            yield from descendants(c)

def occurs(sym, mathtexts):
    for m in mathtexts:
        if sym[0] == '\\' or '_' in sym or '(' in sym or "'" in sym:
            i = 0
            while True:
                k = m.find(sym, i)
                if k < 0: break
                nxt = m[k+len(sym):k+len(sym)+1]
                if not (nxt.isalpha() and sym[-1].isalpha()):
                    return True
                i = k + 1
        else:
            if re.search(r'(?<![A-Za-z\\])' + re.escape(sym) + r'(?![A-Za-z])', m):
                return True
    return False

def validate(root, verbose=True):
    errs, warns = [], []
    ids = {}
    pages_used = {}
    from_used = set()
    # structure
    for n, page, depth, parent in walk(root):
        i = n['id']
        if i in ids: errs.append('duplicate id %s' % i)
        ids[i] = n
        if n['intention'] not in ('show', 'infer'): errs.append('%s bad intention' % i)
        if not n.get('claim'): errs.append('%s no claim' % i)
        if n['intention'] == 'show':
            if not n.get('method'): errs.append('%s show without method' % i)
            m = n.get('motivation')
            if not m or not m.get('text') or m.get('source') not in ('explicit','recoverable','reconstructed'):
                errs.append('%s bad motivation' % i)
            elif m['source'] == 'explicit' and not m.get('quote'):
                errs.append('%s explicit motivation without quote' % i)
            elif m['source'] != 'explicit' and m.get('quote'):
                errs.append('%s non-explicit motivation with quote' % i)
            if not n.get('children'): errs.append('%s show without children' % i)
            if n.get('quote'): errs.append('%s show with quote' % i)
        else:
            if not n.get('quote'): errs.append('%s infer without quote' % i)
            if n.get('children'): errs.append('%s infer with children' % i)
            if n.get('method') or n.get('motivation'): errs.append('%s infer with method/motivation' % i)
        if n.get('deferred') and n['intention'] != 'infer': errs.append('%s deferred on show' % i)
        if n.get('page'):
            p = n['page']
            if p not in PIDX: errs.append('%s unknown page %s' % (i, p))
            if p in pages_used: errs.append('page %s used twice (%s, %s)' % (p, pages_used[p], i))
            pages_used[p] = i
        for f in n.get('from', []):
            if f in KNOWN: continue
            if f not in PIDX:
                errs.append('%s from unknown id %s' % (i, f)); continue
            from_used.add(f)
            if page is None:
                errs.append('%s has from page but no effective page' % i)
            elif PIDX[f] >= PIDX[page]:
                errs.append('%s (page %s) from %s which is not before it' % (i, page, f))
        if not math_of(n.get('claim', '')): warns.append('%s claim has no math' % i)
    if root.get('page') != 'main-theorem': errs.append('root page must be main-theorem')
    for p in PAGES:
        if p not in pages_used and p not in from_used:
            errs.append('page %s neither presents a step nor is in any from' % p)
    # quotes
    last = -1
    lastid = None
    quotes = []
    for n, page, depth, parent in walk(root):
        qs = []
        if n['intention'] == 'infer':
            qs.append(('quote', n['quote']['quote'], n.get('deferred')))
        else:
            mq = n['motivation'].get('quote')
            if mq: qs.append(('mot', mq['quote'], True))
        for kind, q, deferred in qs:
            nq = norm(q)
            cnt = nsrc.count(nq)
            if cnt == 0:
                errs.append('%s %s quote not found' % (n['id'], kind)); continue
            if cnt > 1: warns.append('%s %s quote occurs %d times' % (n['id'], kind, cnt))
            idx = nsrc.find(nq)
            if kind == 'quote' and not deferred:
                quotes.append((n['id'], idx, idx + len(nq)))
    prev = None
    for qid, s, e in quotes:
        if prev is not None:
            if s < prev[2]:
                errs.append('order/overlap: %s [%d,%d) after %s [%d,%d)' % (qid, s, e, prev[0], prev[1], prev[2]))
        prev = (qid, s, e)
    # adds
    for n, page, depth, parent in walk(root):
        if n.get('adds'):
            maths = []
            for d in descendants(n):
                maths += math_of(d['claim'])
            for b in n['adds']:
                if not occurs(b['symbol'], maths):
                    errs.append('%s adds symbol %s not found in descendant claim math' % (n['id'], b['symbol']))
                for k in ('symbol','name','meaning','relation'):
                    if not b.get(k): errs.append('%s adds %s missing %s' % (n['id'], b.get('symbol'), k))
                if len(b['name'].split()) > 4: errs.append('%s adds %s name too long' % (n['id'], b['symbol']))
                if b['relation'] not in ('direct','count'): errs.append('%s adds relation' % n['id'])
    return errs, warns, ids, pages_used, from_used

if __name__ == '__main__':
    root = tidy(t_s5.root())
    renumber(root, 'S0')
    errs, warns, ids, pages_used, from_used = validate(root)
    print('nodes:', len(ids), ' pages as steps:', len(pages_used), ' from-only pages:', sorted(set(PAGES) - set(pages_used)))
    for w in warns: print('WARN', w)
    for e in errs: print('ERR ', e)
    if '--write' in sys.argv:
        json.dump({'root': root}, open(OUT, 'w'), indent=1, ensure_ascii=False)
        print('written', OUT)
