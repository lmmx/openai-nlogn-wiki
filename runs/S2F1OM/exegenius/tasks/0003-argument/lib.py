"""Helpers for building and checking the argument tree (mirrors exegenius' checks)."""
import json
import re

PROJECT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1OM"
SRC_PATH = PROJECT + "/sources/paper.tex"
ANSWER = PROJECT + "/exegenius/tasks/0003-argument.answer.json"
GRAPH = PROJECT + "/exegenius/graph.json"


def normalise(s):
    out = []
    pending = False
    for c in s:
        if c in "‘’‛′":
            c = "'"
        elif c in "“”‟″":
            c = '"'
        elif "‐" <= c <= "―" or c == "−":
            c = "-"
        elif c == "­":
            continue
        if c.isspace():
            pending = True
            continue
        if pending and out:
            out.append(" ")
        pending = False
        out.append(c)
    return "".join(out)


TEXT = open(SRC_PATH, encoding="utf-8").read()
PIECES = []
LINES = []  # (offset, line)
_off = 0
for _n, _line in enumerate(TEXT.split("\n")):
    _p = normalise(_line)
    if not _p:
        continue
    LINES.append((_off, _n + 1))
    PIECES.append(_p)
    _off += len(_p) + 1
NORM = " ".join(PIECES)


def line_at(offset):
    lo, hi = 0, len(LINES)
    while lo < hi:
        mid = (lo + hi) // 2
        if LINES[mid][0] <= offset:
            lo = mid + 1
        else:
            hi = mid
    return LINES[lo - 1][1] if lo else 1


def position(quote):
    return NORM.find(normalise(quote))


class QuoteError(Exception):
    pass


def Q(text):
    """A verbatim quote; fails if not found."""
    if position(text) < 0:
        raise QuoteError("quote not found: " + text)
    return {"source": "paper", "quote": text}


def X(start, end):
    """The normalised source text from the first occurrence of `start` to the end of the
    first occurrence of `end` after it."""
    s, e = normalise(start), normalise(end)
    a = NORM.find(s)
    if a < 0:
        raise QuoteError("start not found: " + start)
    b = NORM.find(e, a)
    if b < 0:
        raise QuoteError("end not found after start: " + end)
    return {"source": "paper", "quote": NORM[a : b + len(e)]}


def mot(text, source, quote=None):
    m = {"text": text, "source": source}
    if quote is not None:
        m["quote"] = quote
    return m


def add(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def show(claim, method, motivation, children, page=None, frm=(), salient=None, adds=()):
    n = {"intention": "show", "claim": claim, "method": method, "motivation": motivation,
         "children": list(children)}
    if page:
        n["page"] = page
    if frm:
        n["from"] = list(frm)
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = list(adds)
    return n


def infer(claim, quote, page=None, frm=(), deferred=False, salient=None):
    n = {"intention": "infer", "claim": claim, "quote": quote}
    if page:
        n["page"] = page
    if frm:
        n["from"] = list(frm)
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


KEY_ORDER = ["id", "intention", "claim", "page", "from", "method", "motivation", "salient",
             "adds", "quote", "deferred", "children"]


def assign_ids(node, ident="S0"):
    node["id"] = ident
    for i, child in enumerate(node.get("children", []), 1):
        assign_ids(child, (ident + "." if ident != "S0" else "S") + str(i))
    ordered = {k: node[k] for k in KEY_ORDER if k in node}
    node.clear()
    node.update(ordered)
    return node


# ---------------------------------------------------------------- checks


def math_of(text):
    """Approximate inline math extraction: $...$ spans (no $$ used)."""
    return re.findall(r"\$([^$]+)\$", text)


def tokens(latex):
    out = []
    i = 0
    while i < len(latex):
        c = latex[i]
        if c == "\\":
            if i + 1 < len(latex) and latex[i + 1].isascii() and latex[i + 1].isalpha():
                j = i + 1
                while j < len(latex) and latex[j].isascii() and latex[j].isalpha():
                    j += 1
                tok = latex[i:j]
            elif i + 1 < len(latex):
                tok = latex[i : i + 2]
            else:
                tok = "\\"
        else:
            tok = c
        i += len(tok)
        if c.isspace() or tok in ("\\,", "\\;", "\\:", "\\!", "\\ ", "~", "{", "}"):
            continue
        out.append(tok)
    return out


def occurs(symbol, maths):
    w = tokens(symbol)
    if not w:
        return False
    for m in maths:
        t = tokens(m)
        for k in range(len(t) - len(w) + 1):
            if t[k : k + len(w)] == w:
                return True
    return False


def walk(node, path=()):
    yield path, node
    for c in node.get("children", []):
        yield from walk(c, path + (node,))


def check(root, verbose=True):
    graph = json.load(open(GRAPH))
    concepts = {c["id"]: c for c in graph["concepts"]}
    # reading order from the task file
    md = open(PROJECT + "/exegenius/tasks/0003-argument.md").read()
    sec = md.split("## Pages, in reading order")[1].split("## Concepts the reader knows")[0]
    order = re.findall(r"^- `([^`]+)`", sec, re.M)
    pos = {p: i for i, p in enumerate(order)}
    errors, warnings = [], []
    if root["intention"] != "show":
        errors.append("root not show")
    if root.get("page") != graph["target"]:
        errors.append("root page")
    ids = set()
    pages = {}
    nodes = list(walk(root))
    for path, n in nodes:
        what = "step " + n["id"]
        if n["id"] in ids:
            errors.append(what + " twice")
        ids.add(n["id"])
        if n["intention"] == "show":
            if not n.get("children"):
                errors.append(what + " show without children")
            if not n.get("method"):
                errors.append(what + " no method")
            m = n.get("motivation")
            if not m:
                errors.append(what + " no motivation")
            else:
                if m["source"] == "explicit" and not m.get("quote"):
                    errors.append(what + " explicit without quote")
                if m.get("quote") and position(m["quote"]["quote"]) < 0:
                    errors.append(what + " motivation quote not found")
                if m["source"] not in ("explicit", "recoverable", "reconstructed"):
                    errors.append(what + " bad provenance")
        else:
            if n.get("children"):
                errors.append(what + " infer with children")
            if not n.get("quote"):
                errors.append(what + " infer without quote")
            elif position(n["quote"]["quote"]) < 0:
                errors.append(what + " quote not found")
        if n.get("page"):
            p = n["page"]
            if p not in pos:
                errors.append(what + " page not in wiki " + p)
            elif p in pages:
                errors.append(f"{p} presents {pages[p]} and {n['id']}")
            else:
                pages[p] = n["id"]
        page = None
        for a in (n,) + tuple(reversed(path)):
            if a.get("page"):
                page = a["page"]
                break
        for f in n.get("from", []):
            c = concepts.get(f)
            if c is None:
                errors.append(f"{what}: {f} not a concept")
            elif c.get("known"):
                pass
            elif f not in pos:
                errors.append(f"{what}: {f} neither known nor page")
            elif page is not None and pos[f] >= pos[page]:
                errors.append(f"{what}: {f} not before {page}")
        below = [m for _, d in walk(n) for m in math_of(d["claim"])]
        for b in n.get("adds", []):
            if not occurs(b["symbol"], below):
                errors.append(f"{what}: adds {b['symbol']} occurs nowhere below")
            if not 1 <= len(b["name"].split()) <= 4:
                errors.append(f"{what}: adds name {b['name']} length")
        if n.get("page") and n["page"] in pos:
            for a in path:
                if a.get("page") in pos and pos[a["page"]] < pos[n["page"]]:
                    warnings.append(f"{n['id']} on {n['page']} after ancestor page {a['page']}")
    last = None
    for _, n in nodes:
        if n["intention"] != "infer" or n.get("deferred"):
            continue
        at = position(n["quote"]["quote"])
        if at < 0:
            continue
        if last and at < last[0]:
            errors.append(f"order: {n['id']} (line {line_at(at)}) before {last[1]} (line {line_at(last[0])})")
        last = (at, n["id"])
    used = set()
    for _, n in nodes:
        if n.get("page"):
            used.add(n["page"])
        used.update(n.get("from", []))
    unused = [p for p in order if p not in used]
    if unused:
        errors.append("unused pages: " + ", ".join(unused))
    if verbose:
        for path, n in nodes:
            q = n.get("quote")
            ln = line_at(position(q["quote"])) if q else ""
            depth = len(path)
            occ = NORM.count(normalise(q["quote"])) if q else 0
            print(f"{'  ' * depth}{n['id']:<14} {n['intention']:<5} {n.get('page') or '':<26} "
                  f"{ln}{' DEFERRED' if n.get('deferred') else ''}{' x' + str(occ) if occ > 1 else ''}")
    return errors, warnings


def coverage(root):
    """Top-level sections holding a quote (infer and motivation quotes)."""
    heads = []
    for n, line in enumerate(TEXT.split("\n")):
        m = re.match(r"\s*\\(section|appendix)\b", line)
        if m:
            heads.append((n + 1, line.strip()))
    qs = []
    for _, n in walk(root):
        if n.get("quote"):
            qs.append(n["quote"]["quote"])
        m = n.get("motivation")
        if m and m.get("quote"):
            qs.append(m["quote"]["quote"])
    lines = sorted(line_at(position(q)) for q in qs)
    return heads, lines
