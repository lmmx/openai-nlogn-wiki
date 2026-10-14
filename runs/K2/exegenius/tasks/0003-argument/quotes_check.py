import sys
text = open('/home/user/openai-nlogn-wiki/runs/K2/sources/paper.tex', encoding='utf-8').read()
lines = text.split('\n')
quotes = [l.rstrip('\n') for l in open(sys.argv[1], encoding='utf-8')]
for q in quotes:
    if not q:
        continue
    cnt = text.count(q)
    locs = []
    if cnt:
        start = 0
        while True:
            i = text.find(q, start)
            if i < 0: break
            ln = text.count('\n', 0, i) + 1
            locs.append(ln)
            start = i + 1
    print(f"{cnt:2d} {locs[:6]} :: {q}")
