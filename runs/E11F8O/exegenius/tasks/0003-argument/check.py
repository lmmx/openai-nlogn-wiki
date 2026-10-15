import json, re

BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E11F8O"
src = open(BASE + "/sources/paper.tex").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
nsrc = norm(src)
ans = json.load(open(BASE + "/exegenius/tasks/0003-argument.answer.json"))
task = open(BASE + "/exegenius/tasks/0003-argument.md").read()

pages = re.findall(r"^- `([a-z0-9-]+)`:", task.split("## Pages, in reading order")[1].split("## Concepts the reader knows")[0], re.M)
known = re.findall(r"^- `([a-z0-9-]+)`:", task.split("## Concepts the reader knows")[1].split("## Sources")[0], re.M)
order = {p: i for i, p in enumerate(pages)}

problems = []
seen_pages = {}
used_from = set()
last = -1
ids = set()


def mathsegs(s):
    return re.findall(r"\$([^$]*)\$", s)


def walk(node, page, anc_adds):
    global last
    nid = node["id"]
    if nid in ids:
        problems.append(f"dup id {nid}")
    ids.add(nid)
    pg = node.get("page") or page
    if node.get("page"):
        if node["page"] in seen_pages:
            problems.append(f"page {node['page']} used twice: {seen_pages[node['page']]} and {nid}")
        seen_pages[node["page"]] = nid
        if node["page"] not in order:
            problems.append(f"unknown page {node['page']}")
    for f in node.get("from", []):
        used_from.add(f)
        if f in known:
            continue
        if f not in order:
            problems.append(f"{nid}: unknown from {f}")
        elif order[f] >= order[pg]:
            problems.append(f"{nid}: from {f} (#{order[f]}) not before page {pg} (#{order[pg]})")
    if node["intention"] == "infer":
        q = node["quote"]["quote"]
        nq = norm(q)
        cnt = nsrc.count(nq)
        if cnt == 0:
            problems.append(f"{nid}: quote not found: {q[:80]}")
        else:
            if cnt > 1:
                problems.append(f"{nid}: quote occurs {cnt} times: {q[:60]}")
            pos = nsrc.find(nq)
            if not node.get("deferred"):
                if pos <= last:
                    problems.append(f"{nid}: quote out of order (pos {pos} <= {last}): {q[:60]}")
                last = max(last, pos)
        if node.get("children"):
            problems.append(f"{nid}: infer with children")
    else:
        m = node.get("motivation")
        if not m:
            problems.append(f"{nid}: show without motivation")
        elif m["source"] == "explicit":
            q = m["quote"]["quote"]
            if norm(q) not in nsrc:
                problems.append(f"{nid}: motivation quote not found: {q[:80]}")
        if not node.get("method"):
            problems.append(f"{nid}: no method")
        if not node.get("children"):
            problems.append(f"{nid}: show without children")
        # adds check
        desc_math = []

        def collect(n):
            for ch in n.get("children", []):
                desc_math.extend(mathsegs(ch["claim"]))
                collect(ch)
        collect(node)
        dm = " ".join(desc_math)
        for b in node.get("adds", []):
            sym = b["symbol"]
            # token-ish match
            pat = re.escape(sym)
            if re.match(r"^[A-Za-z]$", sym):
                pat = r"(?<![A-Za-z\\])" + pat + r"(?![A-Za-z])"
            if not re.search(pat, dm):
                problems.append(f"{nid}: added symbol {sym} not in descendant math")
        for ch in node.get("children", []):
            walk(ch, pg, anc_adds)


walk(ans["root"], ans["root"]["page"], [])
for p in pages:
    if p not in seen_pages and p not in used_from:
        problems.append(f"page {p} has no step and is in no from")
print("pages with steps:", len(seen_pages), "of", len(pages))
print("\n".join(problems) if problems else "OK")
