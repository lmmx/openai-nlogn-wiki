import sys
src=open('sources/paper.tex').read()
qs=[l.rstrip('\n') for l in open(sys.argv[1])]
for q in qs:
    if not q.strip(): continue
    print(src.count(q), src.find(q), repr(q[:70]))
