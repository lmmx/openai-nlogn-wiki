import json, sys
body_path = '../0015-write-subset-intersection-labels.answer.md'
body = open(body_path, encoding='utf-8').read()

Q_LINK = r"The labels are attached to the gates and terminals of a [Linear exchange network with restored scratch wires](linear-network.md)."
Q_FRAME = r"They are used as frames in [Frames on wire arrays](common-frame-principle.md): vertex $v$ carries $M_v=P_{U_v}$, the orthogonal projection onto $U_v$."
Q_ALG = r"The labels are based on [Rank, subspaces and orthogonal complements](linear-algebra-basics.md)."
Q_NEST = r"For nested labels $U\subset V$, $P_V-P_U$ is the identity on the residual $V\cap U^\perp$ and zero on its complement, so an edge costs $\operatorname{rank}(P_V-P_U)=\dim V-\dim U$."
Q_BIT = r"For the bit network $F=\mathbb Q^h$ with $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$, $J$ the all-ones matrix; for the complex network $F=\mathbb F_2^h$ with the dot product."
Q_GROUND = r"Triples $S,T$ in a ground set of $h=100$ points have indicators $t_S,t_T$."
Q_LABEL = r"The label space $\mathcal F=F^{\otimes3}$ has dimension $m=h^3$."
Q_INPUT = r"An input $a=(a_1,a_2,a_3)$ of three triples has label $U_a=\langle u_a\rangle$, where $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$."
Q_ROLES = r"$X_a$ has source $U_a$ and sink $\mathcal F$, $Y_a$ has source $0$ and sink $U_a^\perp$, and scratch roles have source $0$ and sink $\mathcal F$."
Q_SUMS = r"Each $U_a$ is a line, so sources total $N$, one per input, and sinks $Wm-N$."
Q_STAGE = r"At stage $j$ let $A=F^{\otimes(j-1)}$, $R=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$ and $B=R^\perp$ in $A$."
Q_INV = r"With $\nu$ invocations of $c$ central wires each, the total loss $L$ equals $\nu ch$."
Q_GATE = r"Gate labels at times $0$ to $7$ are $B\otimes\langle t\rangle$, $B\otimes F$, $(B\otimes F)\oplus(R\otimes\langle t\rangle)$, $A\otimes F$, $B\otimes F$, $(B\otimes F)\oplus(R\otimes\langle t\rangle^\perp)$, $A\otimes F$, $A\otimes F$, with $t$ the wire's triple indicator and $\oplus$ the orthogonal sum."
Q_CPX = r"Complex network: $C=H\operatorname{diag}(1,i)H=\alpha I+\beta\sigma$, with $H$ the Hadamard matrix, $\alpha=\frac{1+i}{2}$, $\beta=\frac{1-i}{2}$ and $\sigma$ the coordinate swap."
Q_FRAMES = r"Frames over binary $x$ are $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with $q_U(x)=\operatorname{wt}(P_Ux)\bmod4$, $\operatorname{wt}$ the Hamming weight."
Q_BASIS = r"For an orthonormal basis $\mathcal K$ of a residual $E$, $q_V(x)-q_U(x)=\sum_{w\in\mathcal K}\operatorname{wt}(w)\,(w\cdot x\bmod2)\pmod4$, with each $\operatorname{wt}(w)$ odd."
Q_KERNEL = r"Each factor $i^{\pm(w\cdot x\bmod2)}$ is a kernel $\alpha I+\beta\tau_w$ or its inverse, since $H\operatorname{diag}(1,-1)H=\sigma$ turns $(-1)^{w\cdot x}$ into a translation $\tau_w$."
Q_PAIR = r"The pair $X_a\to Y_a$ has inverse kernels, which $C=iZC^{-1}Z$ with $Z=\operatorname{diag}(1,-1)$ turns into $C$, so every role carries $C^{\otimes m}$."
Q_BITX = r"Bit network: $-P_{U_a}$ replaces $M_v$ at the source of $X_a$; with $P_{U_a^\perp}+P_{U_a}=I_m$, every endpoint difference is $I_m$. Edge ranks equal dimension changes, except at the $N$ source edges, where $2P_{U_a}$ has rank one. Write $s$ for the total edge rank, so $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$."
Q_LOSS = r"Both are below one half, so $N$ extra source ranks leave a strict saving."
Q_DIM = r"Dimension drops only on central edges from time $3$ to $4$, each by $h$. "
Q_SIDE = r"The side edge has residual $R\otimes\langle t_S,t_T\rangle^\perp$ of dimension $h-2$, since neighbouring triples satisfy $t_S\perp t_T$."
Q_TRIPLE = r"Since $t_S,t_T$ have three ones, $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$, so each triple line is nondegenerate."
Q_STAGE_NEXT = r"The next stage has $A'=A\otimes F$, $R'=R\otimes\langle t_{a_j}\rangle$ and $B'=(R')^\perp$, so outgoing labels equal the next incoming labels."
Q_WEIGHT = r"Frames over binary $x$"
Q_CSTEP = r"Each factor $i^{\pm(w\cdot x\bmod2)}$ is a kernel $\alpha I+\beta\tau_w$ or its inverse, since $H\operatorname{diag}(1,-1)H=\sigma$ turns $(-1)^{w\cdot x}$ into a translation $\tau_w$. Over $\mathbb F_2$ residuals have orthonormal bases, so $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$."
Q_W = r"Here $W$ counts wires."
Q_VERT = Q_FRAME

def find(q):
    assert body.count(q) == 1, ("not found exactly once", q[:70], body.count(q))
    return q

relations = [
    {"prerequisite": "linear-network", "predicate": "are attached to the gates and terminals of", "quote": find(Q_LINK)},
    {"prerequisite": "common-frame-principle", "predicate": "are used as frames in", "quote": find(Q_FRAME)},
    {"prerequisite": "linear-algebra-basics", "predicate": "are based on", "quote": find(Q_ALG)},
]

def sym(symbol, name, meaning, relation, quote):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation, "quote": find(quote)}

symbols = [
    sym("W", "wire count", "The number of wires of the network, written $W_{\\rm b}$ and $W_{\\rm c}$ for the two constructions.", "count", Q_W),
    sym("m", "label dimension", "The dimension of the label space, which counts the basis vectors of $F^{\\otimes3}$.", "count", Q_LABEL),
    sym("v", "vertex", "A vertex of the network, which carries a frame matrix.", "direct", Q_FRAME),
    sym("M_v", "vertex frame matrix", "The frame matrix at vertex $v$, equal to the projection onto the vertex label.", "direct", Q_FRAME),
    sym("U_v", "vertex label", "The label of vertex $v$.", "direct", Q_FRAME),
    sym("P_U", "label projection", "The orthogonal projection onto a label $U$.", "direct", Q_FRAME),
    sym("U", "smaller label", "A label, the smaller of a nested pair $U\\subset V$.", "direct", Q_NEST),
    sym("V", "larger label", "A label, the larger of a nested pair $U\\subset V$.", "direct", Q_NEST),
    sym("F", "bilinear space", "The bilinear space $\\mathbb Q^h$ of the bit network or $\\mathbb F_2^h$ of the complex network.", "direct", Q_BIT),
    sym("J", "all-ones matrix", "The matrix with every entry equal to one.", "direct", Q_BIT),
    sym("h", "ground-set size", "The number of points in the ground set, here 100, which is also the length of each triple indicator.", "count", Q_GROUND),
    sym("S", "triple", "A triple, a 3-element subset of the ground set.", "direct", Q_GROUND),
    sym("T", "triple", "A triple, a 3-element subset of the ground set.", "direct", Q_GROUND),
    sym("t_S", "triple indicator", "The indicator vector of the triple $S$.", "direct", Q_GROUND),
    sym("t_T", "triple indicator", "The indicator vector of the triple $T$.", "direct", Q_GROUND),
    sym("\\mathcal F", "label space", "The label space $F^{\\otimes3}$.", "direct", Q_LABEL),
    sym("a", "input", "An input, named by a triple of triple indices $(a_1,a_2,a_3)$.", "direct", Q_INPUT),
    sym("u_a", "input tensor", "The pure tensor $t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$ of input $a$.", "direct", Q_INPUT),
    sym("U_a", "input label", "The label of input $a$, the line spanned by $u_a$.", "direct", Q_INPUT),
    sym("X_a", "input role", "The input role of $a$, whose source is the label $U_a$.", "direct", Q_ROLES),
    sym("Y_a", "paired role", "The role paired with $X_a$, whose sink is $U_a^\\perp$.", "direct", Q_ROLES),
    sym("N", "input count", "The number of inputs $a$, each contributing one source dimension.", "count", Q_SUMS),
    sym("j", "stage index", "The index of the current stage, which exposes the $j$th tensor factor.", "direct", Q_STAGE),
    sym("A", "stage space", "The tensor space $F^{\\otimes(j-1)}$ at stage $j$.", "direct", Q_STAGE),
    sym("R", "stage line", "The line spanned by the first $j-1$ triple tensors.", "direct", Q_STAGE),
    sym("B", "stage complement", "The complement $R^\\perp$ of $R$ inside $A$.", "direct", Q_STAGE),
    sym("\\nu", "invocation count", "The number of invocations of the repeated block.", "count", Q_INV),
    sym("c", "central wires", "The number of central wires in one invocation.", "count", Q_INV),
    sym("L", "total loss", "The total dimension lost on decreasing edges.", "count", Q_INV),
    sym("t", "wire triple", "The indicator of the triple on the wire under consideration.", "direct", Q_GATE),
    sym("\\oplus", "orthogonal sum", "The orthogonal direct sum of two subspaces.", "direct", Q_GATE),
    sym("s", "total edge rank", "The total rank of all edge changes in the network.", "count", Q_BITX),
    sym("C", "two-point kernel", "The matrix $H\\operatorname{diag}(1,i)H=\\alpha I+\\beta\\sigma$.", "direct", Q_CPX),
    sym("H", "Hadamard matrix", "The normalized Hadamard matrix.", "direct", Q_CPX),
    sym("\\alpha", "kernel coefficient", "The coefficient $\\frac{1+i}{2}$ of the identity in $C$.", "direct", Q_CPX),
    sym("\\beta", "kernel coefficient", "The coefficient $\\frac{1-i}{2}$ of $\\sigma$ in $C$.", "direct", Q_CPX),
    sym("\\sigma", "coordinate swap", "The matrix that interchanges the two coordinates.", "direct", Q_CPX),
    sym("\\mathcal C_U", "phase frame", "The phase frame of label $U$, a matrix on functions of binary vectors.", "direct", Q_FRAMES),
    sym("q_U", "phase exponent", "The phase exponent of label $U$ at a binary vector $x$, taken mod 4.", "direct", Q_FRAMES),
    sym("x", "binary vector", "A binary vector in $\\mathbb F_2^m$.", "direct", Q_FRAMES),
    sym("\\operatorname{wt}", "Hamming weight", "The number of ones in a binary vector.", "direct", Q_FRAMES),
    sym("\\mathcal K", "orthonormal basis", "An orthonormal basis of the residual $E$.", "direct", Q_BASIS),
    sym("E", "residual", "The orthogonal residual of an edge.", "direct", Q_BASIS),
    sym("w", "basis vector", "A vector of the orthonormal basis $\\mathcal K$.", "direct", Q_BASIS),
    sym("\\tau_w", "translation", "The translation $f(x)\\mapsto f(x+w)$ by a binary vector $w$.", "direct", Q_KERNEL),
    sym("Z", "sign matrix", "The diagonal sign matrix $\\operatorname{diag}(1,-1)$.", "direct", Q_PAIR),
]

derivations = [
    {"step": "S4.3.1", "quote": find(Q_TRIPLE)},
    {"step": "S4.3.2", "quote": find(Q_ROLES + " " + Q_SUMS)},
    {"step": "S4.3.3", "quote": find(Q_STAGE_NEXT)},
    {"step": "S4.3.4", "quote": find(Q_DIM + Q_INV)},
    {"step": "S4.3.5", "quote": find(Q_LOSS)},
    {"step": "S4.3.6", "quote": find(Q_BITX)},
    {"step": "S4.3.7", "quote": find(Q_CSTEP)},
]

out = {"symbols": symbols, "relations": relations, "derivations": derivations}
open('../0015-write-subset-intersection-labels.answer.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print("ok", len(symbols), "symbols")
