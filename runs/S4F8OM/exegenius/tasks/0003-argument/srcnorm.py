"""Replicates exegenius quote normalisation and lookup for the source."""
import re, sys

def normalise(s):
    out = []
    pending = False
    for c in s:
        if c in '‘’‛′':
            c = "'"
        elif c in '“”‟″':
            c = '"'
        elif '‐' <= c <= '―' or c == '−':
            c = '-'
        elif c == '­':
            continue
        if c.isspace():
            pending = True
            continue
        if pending and out:
            out.append(' ')
        pending = False
        out.append(c)
    return ''.join(out)

class Source:
    def __init__(self, path):
        text = open(path, encoding='utf-8').read()
        pieces = []
        lines = []  # (offset, lineno)
        offset = 0
        raw = text.split('\n')
        if raw and raw[-1] == '':
            raw = raw[:-1]
        for n, line in enumerate(raw):
            line = line[:-1] if line.endswith('\r') else line
            for p, part in enumerate(line.split('\x0c')):
                piece = normalise(part)
                if not piece:
                    continue
                lines.append((offset, n + 1))
                offset += len(piece) + 1
                pieces.append(piece)
        self.norm = ' '.join(pieces)
        self.lines = lines

    def line_at(self, off):
        import bisect
        i = bisect.bisect_right([o for o, _ in self.lines], off) - 1
        return self.lines[max(i, 0)][1]

    def find(self, q):
        nq = normalise(q)
        if not nq:
            return None
        return self.norm.find(nq) if nq in self.norm else None

    def occurrences(self, q):
        nq = normalise(q)
        res = []
        start = 0
        while True:
            i = self.norm.find(nq, start)
            if i < 0:
                break
            res.append(i)
            start = i + 1
        return res
