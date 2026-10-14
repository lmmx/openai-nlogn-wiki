#!/usr/bin/env python3
"""Helper: locate quotes in the source (whitespace-normalised), report line, count, offsets."""
import re, sys, json, bisect

SRC = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1SM/sources/paper.tex'

def norm_with_map(text):
    """Collapse whitespace runs to single space; return normalised text and map norm-index -> raw-index."""
    out = []
    mp = []
    i = 0
    n = len(text)
    prev_space = False
    while i < n:
        ch = text[i]
        if ch.isspace():
            if not prev_space:
                out.append(' ')
                mp.append(i)
                prev_space = True
        else:
            out.append(ch)
            mp.append(i)
            prev_space = False
        i += 1
    return ''.join(out), mp

def typo_norm(s):
    # normalise typographic quotes/dashes the way the checker presumably does
    rep = {'‘': "'", '’': "'", '“': '"', '”': '"', '–': '-', '—': '-', '−': '-'}
    return ''.join(rep.get(c, c) for c in s)

raw = open(SRC, encoding='utf-8').read()
nsrc, nmap = norm_with_map(raw)
nsrc_t = typo_norm(nsrc)
line_starts = [0]
for m in re.finditer('\n', raw):
    line_starts.append(m.end())

def line_of(raw_idx):
    return bisect.bisect_right(line_starts, raw_idx)

def find(quote):
    q, _ = norm_with_map(quote.strip())
    q = typo_norm(q)
    res = []
    start = 0
    while True:
        k = nsrc_t.find(q, start)
        if k < 0:
            break
        res.append(k)
        start = k + 1
    return q, res

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        q, res = find(arg)
        print(repr(q[:70]), '->', 'count', len(res), [ (r, line_of(nmap[r])) for r in res[:5]])
