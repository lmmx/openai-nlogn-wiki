"""Library for building the 0003-argument answer: exact quote extraction + node constructors."""
import re, bisect, json

SRC = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1SM/sources/paper.tex'
raw = open(SRC, encoding='utf-8').read()

def _norm_with_map(text):
    out, mp = [], []
    prev_space = False
    for i, ch in enumerate(text):
        if ch.isspace():
            if not prev_space:
                out.append(' '); mp.append(i); prev_space = True
        else:
            out.append(ch); mp.append(i); prev_space = False
    return ''.join(out), mp

nsrc, nmap = _norm_with_map(raw)
line_starts = [0]
for m in re.finditer('\n', raw):
    line_starts.append(m.end())

def line_of_raw(i):
    return bisect.bisect_right(line_starts, i)

def norm(s):
    return _norm_with_map(s.strip())[0]

def norm_idx_of_line(line):
    """first normalised index at or after the start of the 1-based raw line"""
    rawpos = line_starts[line - 1]
    k = bisect.bisect_left(nmap, rawpos)
    return k

QUOTES = []   # registry of (label, text, start_idx)

def Q(start, end=None, line=None, label=None):
    """Exact (whitespace-normalised) substring of the source from `start` through `end` (inclusive)."""
    s = norm(start)
    base = norm_idx_of_line(line) if line else 0
    i = nsrc.find(s, base)
    if i < 0:
        raise ValueError('start not found: %r (line>=%s)' % (s[:80], line))
    if end is None:
        j = i + len(s)
    else:
        e = norm(end)
        k = nsrc.find(e, i)
        if k < 0:
            raise ValueError('end not found: %r after %r' % (e[:80], s[:60]))
        j = k + len(e)
    text = nsrc[i:j]
    return text

def info(text):
    i = nsrc.find(text)
    cnt = nsrc.count(text)
    l1 = line_of_raw(nmap[i])
    l2 = line_of_raw(nmap[i + len(text) - 1])
    return i, cnt, l1, l2

# ---- node constructors ----
def ev(text):
    return {'source': 'paper', 'quote': text}

def adds_(*items):
    out = []
    for sym, name, meaning, rel in items:
        out.append({'symbol': sym, 'name': name, 'meaning': meaning, 'relation': rel})
    return out

def show(id, claim, method, mot_text, mot_source, mot_quote=None, children=None, page=None,
         frm=None, adds=None, salient=None):
    n = {'id': id, 'intention': 'show', 'claim': claim, 'method': method,
         'motivation': {'text': mot_text, 'source': mot_source,
                        'quote': ev(mot_quote) if mot_quote else None},
         'children': children or []}
    if page: n['page'] = page
    if frm is not None: n['from'] = frm
    if adds: n['adds'] = adds
    if salient: n['salient'] = salient
    return n

def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    n = {'id': id, 'intention': 'infer', 'claim': claim, 'quote': ev(quote)}
    if page: n['page'] = page
    if frm is not None: n['from'] = frm
    if deferred: n['deferred'] = True
    if salient: n['salient'] = salient
    return n
