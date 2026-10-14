"""Build the argument answer and check it the way `exegenius submit` does."""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from srcnorm import Source, normalise
from part4 import ANSWER

PROJECT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
src = Source(os.path.join(PROJECT, 'sources', 'paper.tex'))
graph = json.load(open(os.path.join(PROJECT, 'exegenius', 'graph.json')))
concepts = {c['id']: c for c in graph['concepts']}

# Reading order, from the task file.
task = open(os.path.join(PROJECT, 'exegenius', 'tasks', '0003-argument.md')).read()
order_block = task.split('## Pages, in reading order')[1].split('## Concepts the reader knows')[0]
order = re.findall(r'^- `([^`]+)`', order_block, re.M)
pos = {p: i for i, p in enumerate(order)}

errors, warnings = [], []

def walk(node, path=()):
    yield path, node
    for c in node.get('children', []):
        yield from walk(c, path + (node,))

def tokens(latex):
    out = []
    i = 0
    while i < len(latex):
        c = latex[i]
        if c == '\\':
            if i + 1 < len(latex) and latex[i + 1].isascii() and latex[i + 1].isalpha():
                j = i + 1
                while j < len(latex) and latex[j].isascii() and latex[j].isalpha():
                    j += 1
                tok = latex[i:j]
            elif i + 1 < len(latex):
                tok = latex[i:i + 2]
            else:
                tok = '\\'
        else:
            tok = c
        i += len(tok)
        if tok in ('\\,', '\\;', '\\:', '\\!', '\\ ', '~', '{', '}') or tok.isspace():
            continue
        out.append(tok)
    return out

def math(text):
    return re.findall(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', text)

def occurs(sym, maths):
    want = tokens(sym)
    for m in maths:
        t = tokens(m)
        for k in range(len(t) - len(want) + 1):
            if t[k:k + len(want)] == want:
                return True
    return False

root = ANSWER['root']
nodes = list(walk(root))
if root['intention'] != 'show':
    errors.append('root not show')
if root.get('page') != graph['target']:
    errors.append('root page')
ids, pages = set(), {}
for path, n in nodes:
    what = 'step `%s`' % n['id']
    if n['id'] in ids:
        errors.append(what + ' twice')
    ids.add(n['id'])
    if n['intention'] == 'show':
        if not n.get('children'):
            errors.append(what + ' show without children')
        if not n.get('method'):
            errors.append(what + ' no method')
        m = n.get('motivation')
        if not m:
            errors.append(what + ' no motivation')
        else:
            if m['source'] == 'explicit' and not m.get('quote'):
                errors.append(what + ' explicit without quote')
            if m.get('quote') and not src.occurrences(m['quote']['quote']):
                errors.append(what + ' motivation quote missing: ' + m['quote']['quote'])
            if m['source'] not in ('explicit', 'recoverable', 'reconstructed'):
                errors.append(what + ' bad provenance')
    else:
        if n.get('children'):
            errors.append(what + ' infer with children')
        q = n.get('quote')
        if not q or not src.occurrences(q['quote']):
            errors.append(what + ' quote missing: ' + (q or {}).get('quote', ''))
    p = n.get('page')
    if p:
        if p not in pos:
            errors.append(what + ' bad page ' + p)
        elif p in pages:
            errors.append('%s presents both %s and %s' % (p, pages[p], n['id']))
        else:
            pages[p] = n['id']
    step_page = next((a.get('page') for a in (n,) + tuple(reversed(path)) if a.get('page')), None)
    for f in n.get('from', []):
        c = concepts.get(f)
        if c is None:
            errors.append('%s: %s not a concept' % (what, f))
        elif c['known']:
            pass
        elif f not in pos:
            errors.append('%s: %s neither known nor page' % (what, f))
        elif step_page and pos[f] >= pos[step_page]:
            errors.append('%s: %s not before %s' % (what, f, step_page))
    below = [m for _, d in walk(n) for m in math(d['claim'])]
    for b in n.get('adds', []):
        if not occurs(b['symbol'], below):
            errors.append('%s: adds %s not in claims below' % (what, b['symbol']))
        if not (1 <= len(b['name'].split()) <= 4):
            errors.append('%s: binding name %r' % (what, b['name']))
    if p and p in pos:
        for a in path:
            ap = a.get('page')
            if ap and pos[ap] < pos[p]:
                warnings.append('%s on %s after ancestor page %s' % (n['id'], p, ap))

# Report order.
last = None
for _, n in nodes:
    if n['intention'] != 'infer' or n.get('deferred'):
        continue
    at = src.find(n['quote']['quote'])
    if at is None:
        continue
    if last and at < last[0]:
        errors.append('step %s quotes before step %s (lines %d < %d)' % (
            n['id'], last[1], src.line_at(at), src.line_at(last[0])))
    last = (at, n['id'])

used = set()
for _, n in nodes:
    if n.get('page'):
        used.add(n['page'])
    used.update(n.get('from', []))
unused = [p for p in order if p not in used]
if unused:
    errors.append('unused pages: ' + ', '.join(unused))

# Coverage: top-level sections holding quotes.
quote_lines = []
for _, n in nodes:
    for q in [n.get('quote'), (n.get('motivation') or {}).get('quote')]:
        if q:
            occ = src.occurrences(q['quote'])
            if occ:
                quote_lines.append(src.line_at(occ[0]))
sections = [(37, 431, '1'), (432, 639, '2'), (640, 1346, '3'), (1347, 1762, '4'), (1763, 2758, '5'),
            (2759, 3207, '6'), (3208, 3495, '7'), (3496, 3988, '8'), (3989, 4995, '9'), (5199, 5361, 'A')]
cov = {s: sum(1 for l in quote_lines if a <= l <= b) for a, b, s in sections}

print('steps:', len(nodes), ' infer:', sum(1 for _, n in nodes if n['intention'] == 'infer'),
      ' deferred:', sum(1 for _, n in nodes if n.get('deferred')),
      ' salient:', sum(1 for _, n in nodes if n.get('salient')))
print('section quotes:', cov)
for w in warnings:
    print('WARNING', w)
for e in errors:
    print('ERROR', e)
out = os.path.join(PROJECT, 'exegenius', 'tasks', '0003-argument.answer.json')
with open(out, 'w', encoding='utf-8') as fh:
    json.dump(ANSWER, fh, ensure_ascii=False, indent=1)
print('wrote', out, 'errors:', len(errors))
