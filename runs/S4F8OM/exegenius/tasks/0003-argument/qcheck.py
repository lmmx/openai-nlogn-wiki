import sys
sys.path.insert(0, '.')
from srcnorm import Source
src = Source('../../../sources/paper.tex')
quotes = [l.rstrip('\n') for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
for q in quotes:
    occ = src.occurrences(q)
    if not occ:
        print('MISSING :', q)
    else:
        print('%4d x%d: %s' % (src.line_at(occ[0]), len(occ), q[:110]))
