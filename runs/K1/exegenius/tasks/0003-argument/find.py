import sys
src = open('/home/user/openai-nlogn-wiki/runs/K1/sources/paper.tex', encoding='utf-8').read().split('\n')
quotes = [l.rstrip('\n') for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
for q in quotes:
    hits = [i+1 for i, line in enumerate(src) if q in line]
    print(('OK  ' if hits else 'MISS'), hits[:4], q)
