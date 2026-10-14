import json, sys
src = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1SX/sources/paper.tex').read()
ans = json.load(open(sys.argv[1]))
order = []
def walk(n):
    if n.get('quote'):
        order.append((n['id'], n['quote']['quote'], n.get('deferred', False)))
    m = n.get('motivation')
    if m and m.get('quote'):
        order.append((n['id']+'/mot', m['quote']['quote'], True))  # motivation quotes: only existence
    for c in n.get('children', []):
        walk(c)
walk(ans['root'])
pos = -1; bad = 0
for id_, q, dfr in order:
    cnt = src.count(q)
    if cnt == 0:
        print('MISSING', id_, repr(q[:80])); bad += 1; continue
    if cnt > 1: print('REPEATED', cnt, id_, repr(q[:60]))
    if dfr: continue
    i = src.find(q, pos + 1)
    if i < 0:
        j = src.find(q); print('OUT OF ORDER', id_, 'line', src[:j].count('\n') + 1, repr(q[:60])); bad += 1
    else:
        pos = i
print('checked', len(order), 'quotes; problems:', bad)
