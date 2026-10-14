import json, re, sys

ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1OX"
src = open(ROOT + "/sources/paper.tex").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
S = norm(src)
graph = json.load(open(ROOT + "/exegenius/graph.json"))
CONCEPTS = {c["id"]: c for c in graph["concepts"]}

ORDER = """fixed-tape-model nlogn-conjecture nlogn-multiplier array-order stream-ops controlled-shifts
matrix-basics network frames subset-labels rank-saving bit-network lower-triangular matrix-shear
power-saving-recurrence power-interchange chunk-interchange packed-bit-addition polynomial-ring-mod
kronecker-packing cyclic-convolution int-as-convolution dft butterfly-fft phase-network
fixed-point-disk-grid negacyclic-twist simultaneous-layer convolution-theorem multidim-transform
synthetic-transform gaussian-resampling chirp-identity permutation-cancellation transform-layout
ring-convolution crt-axis-map prime-lengths complex-convolution source-transform exact-recovery
mult-algorithm parameter-balance main-theorem""".split()
POS = {p: i for i, p in enumerate(ORDER)}


def ev(q):
    return {"source": "paper", "quote": q}


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def infer(id, claim, quote, frm=(), page=None, deferred=False, salient=None, adds=()):
    n = {"id": id, "intention": "infer", "claim": claim, "from": list(frm), "quote": ev(quote)}
    if page:
        n["page"] = page
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = list(adds)
    return n


def show(id, claim, method, mot, children, frm=(), page=None, salient=None, adds=()):
    text, source, quote = mot
    m = {"text": text, "source": source}
    if quote:
        m["quote"] = ev(quote)
    n = {"id": id, "intention": "show", "claim": claim, "from": list(frm), "method": method,
         "motivation": m, "children": children}
    if page:
        n["page"] = page
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = list(adds)
    return n


exec(open(ROOT + "/exegenius/tasks/0003-argument/tree.py").read())

# ---------------------------------------------------------------- checks
errors = []


def walk(n, path=()):
    yield path, n
    for c in n.get("children", []):
        yield from walk(c, path + (n,))


def math(text):
    return re.findall(r"\$([^$]+)\$", text)


def tokens(latex):
    out = []
    i = 0
    while i < len(latex):
        c = latex[i]
        if c == "\\":
            j = i + 1
            if j < len(latex) and latex[j].isalpha():
                while j < len(latex) and latex[j].isalpha():
                    j += 1
                tok = latex[i:j]
            else:
                tok = latex[i:j + 1]
                j = j + 1
        else:
            tok = c
            j = i + 1
        if not (c.isspace() or tok in ("\\,", "\\;", "\\:", "\\!", "\\ ", "~", "{", "}")):
            out.append(tok)
        i = j
    return out


def occurs(sym, maths):
    w = tokens(sym)
    for m in maths:
        t = tokens(m)
        for k in range(len(t) - len(w) + 1):
            if t[k:k + len(w)] == w:
                return True
    return False


ids = set()
pages = {}
used = set()
last = None
for path, n in walk(root):
    what = n["id"]
    if what in ids:
        errors.append(f"dup id {what}")
    ids.add(what)
    for q in ([n["quote"]] if "quote" in n else []) + (
            [n["motivation"]["quote"]] if n.get("motivation", {}).get("quote") else []):
        if norm(q["quote"]) not in S:
            errors.append(f"{what}: quote not found: {q['quote']}")
    if n["intention"] == "infer" and not n.get("deferred"):
        at = S.find(norm(n["quote"]["quote"]))
        cnt = S.count(norm(n["quote"]["quote"]))
        if cnt > 1:
            print(f"note: {what} quote occurs {cnt} times")
        if last and at < last[0]:
            errors.append(f"order: {what} ({at}) before {last[1]} ({last[0]})")
        last = (at, what)
    if n.get("page"):
        p = n["page"]
        if p not in POS:
            errors.append(f"{what}: bad page {p}")
        if p in pages:
            errors.append(f"page {p} twice: {pages[p]} {what}")
        pages[p] = what
        used.add(p)
        for a in path:
            if a.get("page") and POS[a["page"]] < POS[p]:
                errors.append(f"warning: {what} page {p} after ancestor page {a['page']}")
    page = next((a.get("page") for a in (n,) + tuple(reversed(path)) if a.get("page")), None)
    for f in n.get("from", []):
        c = CONCEPTS.get(f)
        if c is None:
            errors.append(f"{what}: unknown from {f}")
            continue
        used.add(f)
        if c["known"]:
            continue
        if POS[f] >= POS[page]:
            errors.append(f"{what}: from {f} not before {page}")
    below = [m for _, d in walk(n) for m in math(d["claim"])]
    for b in n.get("adds", []):
        if not occurs(b["symbol"], below):
            errors.append(f"{what}: adds {b['symbol']} not below")
        if not 1 <= len(b["name"].split()) <= 4:
            errors.append(f"{what}: name too long {b['name']}")
    if n["intention"] == "show":
        if not n.get("children"):
            errors.append(f"{what}: show without children")
    # dollar sanity
    if n["claim"].count("$") % 2:
        errors.append(f"{what}: odd dollars in claim")

unused = [p for p in ORDER if p not in used]
if unused:
    errors.append(f"unused pages: {unused}")
for e in errors:
    print("ERR", e)
print("nodes", len(ids), "pages with steps", len(pages))
json.dump({"root": root}, open(ROOT + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1,
          ensure_ascii=False)
