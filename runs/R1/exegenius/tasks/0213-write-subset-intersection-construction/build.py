import json
D = "/home/user/lmmx/openai-nlogn-wiki/runs/R1/exegenius/tasks/"
body = open(D + "0213-write-subset-intersection-construction.answer.md", encoding="utf-8").read()

Q_F = r"Let $\mathcal F=(\mathbb Q^h)^{\otimes 3}$, a space built from the [Tensor product of vector spaces](tensor-product-of-vector-spaces.md) of three copies of $\mathbb Q^h$, and let $m=h^3$ be its dimension (the letter $m$ changes meaning here)."
Q_T = r"For a three-element subset $T$ of $[h]$, called a triple, $t_T$ is its indicator vector, and $\mathcal T$ is the set of all triples."
Q_U = r"A *label* $U$ is a nondegenerate subspace of $\mathcal F$, so $\mathcal F=U\oplus U^\perp$ and the projection $P_U$ onto $U$ along $U^\perp$ is defined."
Q_S = r"Let $s=\sum_e\operatorname{rank}A_e$ be the total rank over all edges $e$, where $A_e$ is the difference of the matrices at the two ends of $e$ (the letter $s$ changes meaning here)."

def sym(symbol, name, meaning, relation, quote):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation, "quote": quote}

symbols = [
    sym("h", "ground set size", "The number of elements of the ground set $[h]$, which is $100$.", "count",
        r"Let $[h]=\{1,\dots,h\}$ be the ground set, where $h=100$ is its number of elements."),
    sym("T", "triple", "A three-element subset of $[h]$, called a triple.", "direct", Q_T),
    sym(r"\mathcal T", "set of triples", "The set of all triples.", "direct", Q_T),
    sym("g_T", "triple value", "The value carried by the triple $T$.", "direct",
        r"Each triple $T$ carries a value $g_T$."),
    sym("C_i", "central wire", "The central wire that gathers the values of the triples containing element $i$.", "direct",
        r"Over $\mathbb F_2$, gather adds the sum of $g_T$ over the triples $T\ni i$ to a central wire $C_i$, for each $i\in[h]$."),
    sym("A_{ST}", "copy wire", "The auxiliary wire carrying a copy of $g_T$ into $S$, for a neighbor pair $S,T$.", "direct",
        r"For each neighbor pair, an auxiliary wire $A_{ST}$ carries a copy of $g_T$ into $S$, which adds $1$ exactly when $|S\cap T|=1$."),
    sym("J", "all-ones matrix", "The matrix with every entry equal to 1.", "direct",
        r"Over $\mathbb Q$, let $J$ be the all-ones matrix (the letter $J$ changes meaning here), and the bilinear form with matrix $I-J/9$ gives $\langle t_T,t_S\rangle=|T\cap S|-1$, so neighbors are orthogonal."),
    sym("m", "space dimension", "The dimension of $\\mathcal F$, which is $h^3$.", "count", Q_F),
    sym(r"\mathcal F", "label space", "The tensor cube $(\\mathbb Q^h)^{\\otimes 3}$, in which labels live.", "direct", Q_F),
    sym("U", "label", "A nondegenerate subspace of $\\mathcal F$.", "direct", Q_U),
    sym("P_U", "label projection", "The projection onto the label $U$ along $U^\\perp$.", "direct", Q_U),
    sym(r"\iota", "index", "A triple of triples $(T_1,T_2,T_3)$ indexing a source.", "direct",
        r"For an index $\iota=(T_1,T_2,T_3)\in\mathcal T^3$, the label $U_\iota$ is the line spanned by $t_{T_1}\otimes t_{T_2}\otimes t_{T_3}$."),
    sym("V", "second label", "A second label, containing or contained in $U$ in the comparison.", "direct",
        r"If $U\subseteq V$ for labels $U,V$, then $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on $U\oplus V^\perp$, so an edge between nested labels has rank equal to its absolute change of label dimension."),
    sym("s", "total rank", "The total rank over all edges, which is the number of smaller calls.", "direct", Q_S),
    sym("A_e", "edge matrix", "The matrix of the edge $e$, the difference of the matrices at its two ends.", "direct", Q_S),
    sym("L", "lost dimension", "The total dimension lost on decreasing edges.", "direct",
        r"Summing gives $2L$, where $L$ is the total dimension lost on decreasing edges (the letter $L$ changes meaning here)."),
    sym("v", "triple count", "The number of triples, $\\binom h3$.", "count",
        r"Let $v=\binom h3$ be the number of triples."),
    sym("N", "index count", "The number of indices $\\iota$, which is $v^3$.", "count",
        r"Let $N=v^3$ be the number of indices $\iota$ (the letter $N$ changes meaning here), so there are $N$ sources."),
]

relations = [
    {"prerequisite": "linear-network-roles", "predicate": "is built inside",
     "quote": r"It is built inside a [Finite linear network with roles and frames](linear-network-roles.md)."},
    {"prerequisite": "tensor-product-of-vector-spaces", "predicate": "is built from",
     "quote": Q_F},
]

missing = [q[:70] for q in [s["quote"] for s in symbols] + [r["quote"] for r in relations] if q not in body]
assert not missing, missing
out = {"symbols": symbols, "relations": relations}
with open(D + "0213-write-subset-intersection-construction.answer.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("ok")
