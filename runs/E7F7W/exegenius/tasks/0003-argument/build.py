import json, sys, re

SRC = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7W/sources/paper.tex"
OUT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7W/exegenius/tasks/0003-argument.answer.json"
LINES = open(SRC, encoding="utf-8").read().split("\n")

errors = []
trace = []  # (lineno, id, deferred)


def find(snippet, after=0, nth=0):
    hits = [i + 1 for i, l in enumerate(LINES) if snippet in l and i + 1 > after]
    if not hits:
        errors.append("NOT FOUND: %r" % snippet)
        return None
    if len(hits) > 1 and nth == 0 and after == 0:
        pass
    return hits[nth]


def E(snippet, after=0, nth=0):
    ln = find(snippet, after, nth)
    return {"source": "paper", "quote": snippet, "_ln": ln}


def mot(text, source, quote=None, **kw):
    m = {"text": text, "source": source}
    if quote:
        m["quote"] = E(quote, **kw)
    else:
        m["quote"] = None
    return m


def infer(id, claim, quote, page=None, frm=None, salient=None, deferred=False, **kw):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": E(quote, **kw)}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if deferred:
        n["deferred"] = True
    return n


def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


def bind(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---------------------------------------------------------------- Part A: tools
A1 = infer(
    "A1",
    "For a fixed radix $q\\ge2$, permuting the digit pair at two positions, moving a digit, splitting on a digit with a pointwise map, and cyclically splitting rows into $W$ streams (and merging them back) each take $O(V)$ steps on an array of volume $V$ on a fixed number of tapes.",
    "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="stream-operations",
    frm=["fixed-tape-model", "tapes-scanning-and-sorting-as-basic-machine-procedures",
         "binary-representation-and-bitwise-operations"],
)
A2 = infer(
    "A2",
    "A target field $y\\in[Q]$, $Q=q^b$, that follows its control fields is shifted $y\\mapsto y+a(\\text{controls})\\pmod Q$, or multiplied by a fixed rational unit, in $O(V)$ time when the offset is prepared in $b^{O(1)}$ time.",
    "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
    page="controlled-shifts",
    frm=["stream-operations", "modular-arithmetic", "primes-coprimality-and-gcd",
         "rational-numbers-and-rounding"],
)
A = show(
    "A",
    "Rearranging an array by one digit, splitting it into streams, and shifting a field by an offset computed from earlier fields all cost $O(V)$ on fixed tapes.",
    "Express each operation as splitting the array into streams on a digit or a row index, applying a fixed pointwise map to aligned streams, and merging the streams back in the required order.",
    mot("Every later recursive procedure is assembled from these linear scans, so its cost is charged to them; the sources do not say this in one sentence but the section states that it 'supplies the elementary scans' used later.",
        "recoverable"),
    [A1, A2],
)

# ---------------------------------------------------------------- Part B: finite networks
B1 = show(
    "B1",
    "A fixed network of pointwise linear gates on data banks $X,Y$, scratch wires and central wires sends $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ in three stages and returns every scratch wire to its arbitrary initial value.",
    "Use an eight-row schedule whose first two rows cancel the old scratch contributions and whose last two restore the scratch wires, so the net change of the target does not depend on the scratch values; then compose a forward pass, the inverse pass in the other direction, and a second forward pass.",
    mot("The old scratch values must be removed before the source values are introduced and put back afterwards, so that arbitrary scratch contents are restored.",
        "explicit",
        "the following schedule remove the effect of the old scratch values;"),
    [
        infer("B1.1",
              "For arbitrary initial scratch values the schedule changes the target $y$ by the net map $\\mathcal J\\mathcal V+\\mathcal R\\mathcal G$ applied to the source $x$, independently of the initial side and central values.",
              "Rows 6 and 7 restore $c,a$.  The net target change is"),
        infer("B1.2",
              "The net coefficient from $x_T$ to $y_S$ is one for $T=S$ and zero otherwise, because the side injection cancels the intersection-count coefficient for neighbouring triples, so one forward invocation is $y\\gets y+x$.",
              "Thus both net maps are $y\\gets y+x$."),
        infer("B1.3",
              "A forward pass $X\\to Y$, the inverse schedule $Y\\to X$ and a forward pass $X\\to Y$ send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
              "Starting from $(x,y)$, the three stages give"),
    ],
    page="xor-linear-network",
    frm=["matrices-and-linear-maps", "linear-algebra-prelims", "modular-arithmetic"],
    salient="Although every gate is a pointwise XOR-type combination, the final effect is an exact exchange of the two banks, and it holds for arbitrary initial values of every scratch wire.",
)

B2 = show(
    "B2",
    "If every source, gate and sink $v$ carries an invertible operator $D_v$ (its frame) and each edge applies $D_vD_u^{-1}$, the network implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so the endpoint frames alone fix the operator applied on every role.",
    "Maintain the invariant that the stored array equals the frame applied to the logical array, and use that a common frame commutes with a pointwise linear gate.",
    mot("Once the scalar routing is fixed, the endpoint frames determine the operator, so the intermediate frames are free to be chosen to make each edge change cheap.",
        "explicit",
        "intermediate frames can then be chosen to make each edge change inexpensive."),
    [
        infer("B2.1",
              "At a vertex $v$ the stored array equals $D_v$ applied to the logical array, which holds at the sources by definition and is preserved along each edge by the edge operator $D_vD_u^{-1}$.",
              "At a vertex $v$, the invariant is that the stored array equals $D_v$ applied"),
        infer("B2.2",
              "At a gate all incidences share one frame $D_v$, and $R$-linearity gives $\\sum_j c_jD_v\\varphi_j=D_v(\\sum_j c_j\\varphi_j)$, so the common frame commutes with the pointwise gate.",
              "Thus the common frame commutes with the pointwise gate, and"),
        infer("B2.3",
              "The operator implemented by the whole network is $D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}$, since the intermediate frames cancel along each route.",
              "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}."),
        infer("B2.4",
              "A route from input role $w$ to output role $\\rho(w)$ applies the sign-weighted operator $D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$, including on roles that carry only auxiliary scratch values.",
              "the endpoint frames determine the array operator on each route; the"),
    ],
    page="frames",
    frm=["xor-linear-network", "matrices-and-linear-maps", "permutations"],
    salient="All intermediate frames cancel: whatever representation changes happen inside the network, the operator on every role (scratch roles included) depends only on its two endpoint frames.",
)

B3 = show(
    "B3",
    "Attach to each gate and terminal a nondegenerate subspace of $F^{\\otimes3}$, built from tensor cubes of indicator vectors of three-element subsets of $[100]$, so that labels on adjacent vertices are nested and the only decreasing edges are the central-wire edges from time $3$ to time $4$.",
    "Use inner products $\\langle t_S,t_T\\rangle=|S\\cap T|-1$ (rational form) or the dot product (binary form) so neighbouring triple lines are orthogonal, prescribe an incoming and outgoing label at every stage, and tabulate the orthogonal residual of every edge.",
    mot("Orthogonality of the indicator vectors of neighbouring triples is what lets the subspace assignments nest.",
        "explicit",
        "Orthogonality of the corresponding indicator vectors permits"),
    [
        infer("B3.1",
              "For a triple $T$ with indicator vector $t_T$ one has $\\langle t_S,t_T\\rangle=|S\\cap T|-1$ and $\\langle t_T,t_T\\rangle=2$, so every triple line is nondegenerate and neighbouring triple lines are orthogonal.",
              "\\langle t_S,t_T\\rangle=|S\\cap T|-1,"),
        infer("B3.2",
              "The terminal labels are $U_a$ at the source and $\\mathcal F$ at the sink of $X_a$, $0$ and $U_a^\\perp$ for $Y_a$, and $0$ and $\\mathcal F$ for each scratch role.",
              "X_a&U_a&\\mathcal F\\\\"),
        infer("B3.3",
              "At stage $j$ a data wire $X$ moves from label $A\\otimes\\langle t\\rangle\\otimes Q$ to $(A\\otimes F)\\otimes Q$, exposing one tensor factor, so the outgoing labels of one stage are exactly the incoming labels of the next.",
              "X&A\\otimes\\langle t\\rangle\\otimes Q&(A\\otimes F)\\otimes Q\\\\"),
        infer("B3.4",
              "The gate order confines every decrease to the return of a central wire from label $A\\otimes F$ to $B\\otimes F$, which loses exactly $P\\otimes F$, of dimension $h$.",
              "The gate order below confines all decreases to this"),
        infer("B3.5",
              "Every edge joins comparable nondegenerate labels, the only decreasing edges are the $Ic$ central-wire edges from time $3$ to $4$ with loss $h$ each, hence $L=Ich$ and the absolute dimension changes sum to $Wm-2N+2L$.",
              "Every edge joins comparable nondegenerate labels.  The only decreasing"),
    ],
    page="subset-labels",
    frm=["linear-algebra-prelims", "xor-linear-network"],
)

B4 = show(
    "B4",
    "The sum $s$ of the rational ranks of all edge differences of the bit network equals $Wm-N+2L$ and is strictly less than $Wm$, because the dimension $L$ lost on decreasing edges is below $N/2$.",
    "Count the dimension changes along the labelled network by telescoping at the gates, correct the signed count by twice the loss on decreasing edges, show that edge rank equals dimension change except at the $N$ negative source projections, and compare with $Wm$.",
    mot("The power saving comes from the total dimension lost on decreasing edges being small relative to $N$, so the argument must bound this loss against the number of source ranks.",
        "explicit",
        "The saving will come from keeping the total dimension lost on decreasing"),
    [
        infer("B4.1",
              "The signed dimension changes telescope at each gate, because every touched wire has one incoming and one outgoing incidence with the same gate label; source dimensions sum to $N$ and sink dimensions to $Wm-N$, so the signed total is $Wm-2N$.",
              "The signed increase is therefore $Wm-2N$."),
        infer("B4.2",
              "Only the $Ic$ central-wire edges decrease, each by $h$, so $L=Ich$, and replacing signed changes by absolute changes adds $2L$, giving absolute total $Wm-2N+2L$.",
              "There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
        infer("B4.3",
              "The loss ratio is exactly $L/N=100/539$ for the bit network, which is below $1/2$, so $N-2L>0$.",
              "\\frac{L_{\\rm b}}{N}=\\frac{100}{539},\\qquad"),
        show(
            "B4.4",
            "The rational rank of an edge difference equals the dimension change of its nested labels, except at the $N$ negative source projections $-P_{U_a}$, each of which adds one extra rank.",
            "Compute the rank of the projection difference $P_V-P_U$ on nested nondegenerate labels, then treat the source edges, where the matrix is $2P_{U_a}$ although the dimension change is zero, as the only exception.",
            mot("Edge ranks, not label dimensions, are what count the smaller calls, so the dimension count must be converted to a rank count and its exceptions identified.",
                "recoverable"),
            [
                infer("B4.4.1",
                      "For nondegenerate $U\\subset V$ the matrix $P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its orthogonal complement, so its rank is $\\dim V-\\dim U$, and reversing the edge only negates it.",
                      "$P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its"),
                infer("B4.4.2",
                      "The only exceptions to rank equal to dimension change are the $N$ negative source projections.",
                      "The only exceptions are the $N$ negative source projections."),
                infer("B4.4.3",
                      "At stage $1$ one has $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so the first edge matrix is $2P_{U_a}$, of rank one where the dimension change was zero.",
                      "Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,"),
            ],
        ),
        infer("B4.5",
              "Hence $s=Wm-N+2L$ and its deficit from $Wm$ is $N-2L>0$.",
              "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
    ],
    page="rank-deficit",
    frm=["subset-labels", "frames", "xor-linear-network", "linear-algebra-prelims", "matrices-and-linear-maps"],
    salient="The deficit is strictly positive but tiny: the decreasing edges lose only $L=\\tfrac{100}{539}N<N/2$, which exactly offsets the extra $N$ source ranks, leaving a relative deficit of about $1.5\\cdot10^{-11}$ for the bit network.",
)

B5 = infer(
    "B5",
    "With the frame $\\Phi_M$ that moves the entry at $(H,D)$ to $(H+MD,D)$, the endpoint matrices of the bit network differ by the identity on every role, $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$, so the network implements the shear $H\\gets H+D$ on every role with total edge rank $s<Wm$.",
    "P_{U_a^\\perp}-(-P_{U_a})=I_m",
    page="bit-shear-interface",
    frm=["frames", "rank-deficit", "subset-labels", "xor-linear-network", "controlled-shifts"],
    salient="The same shear $H\\gets H+D$ is applied on every role, scratch roles included; this works only because the negative source projection $-P_{U_a}$ makes the $X_a\\to Y_a$ endpoint difference equal to $I_m$.",
)

B6 = show(
    "B6",
    "On Gaussian dyadic values with binary labels and phase frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{\\operatorname{wt}(P_Ux)})H^{\\otimes m}$, every edge change is a product of two-point kernels $C=aI+bX$, there are $s_{\\rm c}<W_{\\rm c}m$ such factors in all, and telescoping gives $C^{\\otimes m}$ on every role.",
    "Show that Hamming weight is additive modulo $4$ over orthogonal binary vectors, turn the phase change along each orthonormal residual vector into a translation kernel, count the kernels with the label dimensions, and correct the one exceptional pair $X_a\\to Y_a$ with the identity $C=iZC^{-1}Z$.",
    mot("The butterfly layer needs the same recursive saving as the bit network, with phases instead of address shifts, so the same labelled network is rerun over Gaussian dyadic values.",
        "reconstructed"),
    [
        infer("B6.1",
              "For orthogonal binary vectors the intersection of supports is even, so Hamming weight is additive modulo four and the phase change along an orthonormal residual basis is a sum of weight terms.",
              "If $z\\cdot w=0$, the intersection cardinality is even, so weight is"),
        infer("B6.2",
              "Each basis vector has odd weight, so its phase is $i^{\\varepsilon[v\\cdot x]}=\\frac{1+i^\\varepsilon}{2}+\\frac{1-i^\\varepsilon}{2}(-1)^{v\\cdot x}$ with $\\varepsilon=\\pm1$, which $H\\operatorname{diag}(1,-1)H=X$ turns into the translation kernel $aI+bX_v$ or its inverse.",
              "becomes $aI+bX_v$ or its inverse."),
        infer("B6.3",
              "The total number of kernels is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}$, with deficit $2N-2L_{\\rm c}>0$ and no extra source ranks.",
              "The deficit is $2N-2L_{\\rm c}>0$."),
        infer("B6.4",
              "The one exceptional pair $X_a\\to Y_a$ has operator $C^{-1}$ on the $27$ coordinates of $\\operatorname{supp}(u_a)$ and $C$ elsewhere, and the identity $C=iZC^{-1}Z$ with sign corrections at source and sink turns every inverse factor into $C$.",
              "C=iZC^{-1}Z,\\qquad C^{-1}=-iZCZ."),
        infer("B6.5",
              "After negating the physical $X$ outputs and undoing the role exchange, every role, scratch roles included, carries $C^{\\otimes m}$, and the same holds on any number of columns by tensor products.",
              "Every role, including every scratch role, now has"),
    ],
    page="phase-frame-network",
    frm=["butterfly", "frames", "subset-labels", "rank-deficit", "bit-shear-interface", "xor-linear-network",
         "complex-numbers"],
    salient="Every role, including the scratch roles, ends with the same operator $C^{\\otimes m}$, even though the pair $X_a\\to Y_a$ passes through a different chain of phase changes.",
)

B7 = show(
    "B7",
    "Because $s/W<m$ strictly, a fixed rational exponent $\\tau=1-2^{-50}<1$ satisfies $s/W<m^{\\tau}$, so a recursion $F_k\\le(s/W)F_{k-1}+O(1)$ on a call of parameter $m^k$ costs $O((m^k)^{\\tau})$ per unit volume.",
    "Show that the relative rank deficits exceed $20\\cdot2^{-50}$ and that $m^{1-2^{-50}}>m(1-20\\cdot2^{-50})$, so the contraction factor per level lies below $m^{\\tau}$, and then sum the geometric series of the recursion.",
    mot("A strict inequality only gives some exponent below one if it is converted into an explicit rational $\\tau$ with $s/W<m^\\tau$; the explicit value is needed for the cost table at the end.",
        "recoverable"),
    [
        infer("B7.1",
              "Both relative deficits $\\eta_{\\rm b}$ and $\\eta_{\\rm c}$ exceed $20\\cdot2^{-50}$.",
              "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$."),
        infer("B7.2",
              "Since $m<2^{20}$, $m^{1-2^{-50}}=m\\exp(-2^{-50}\\log m)>m(1-20\\cdot2^{-50})>m(1-\\eta)$.",
              ">m(1-20\\cdot2^{-50})>m(1-\\eta)"),
        infer("B7.3",
              "Consequently $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ with $\\tau=\\sigma=1-2^{-50}$.",
              "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,"),
        infer("B7.4",
              "If $a=s/W<m^\\tau$, the geometric sum $\\sum_{j\\le k}a^j$ is $O(m^{k\\tau})$, whether $a\\le1$ (at most $k+1$) or $a>1$ (order $a^k$).",
              "For $a=s/W<m^\\tau$ the geometric sum",
              deferred=True),
    ],
    page="power-saving-recurrence",
    frm=["rank-deficit",
         "recursion-and-divide-and-conquer-recurrences", "summation-geometric-series-and-products",
         "logarithms-exponentials-floor-and-ceiling"],
    salient="The exponent is extremely close to one, $\\tau=1-2^{-50}$, because the relative rank deficit is only about $10^{-11}$; this is why the final saving $\\kappa=2^{-182}$ is so small.",
)

B = show(
    "B",
    "Fixed linear networks with $W$ wires exchange two banks of values, restore every scratch wire, and attach nested subspaces of an $m$-dimensional space to their gates so that the total rank $s$ of the edge changes satisfies $s<Wm$ and yields a power saving.",
    "Build the scalar exchange network, lift it to arrays through common frames, label the gates with nested nondegenerate subspaces from three-element subsets, count dimension changes edge by edge, and read off the address-shear and phase interfaces.",
    mot("A network that exchanges two banks while restoring its scratch values can be run on arrays, and with cheap edge changes it realizes the address interchange and butterfly layer.",
        "explicit",
        "We construct two fixed linear networks that exchange two banks of values"),
    [B1, B2, B3, B4, B5, B6, B7],
    adds=[
        bind("W", "wire count", "the number of wires of the network, scratch wires included", "count"),
        bind("m", "label dimension", "the dimension $h^3=10^6$ of the label space of subspaces attached to gates"),
        bind("N", "source dimension total", "the sum of the dimensions of the source labels, equal to the number of data banks"),
        bind("s", "smaller calls", "the number of smaller calls, equal to the sum of the ranks of all edge differences", "count"),
        bind("L", "dimension loss", "the total dimension lost on decreasing edges"),
    ],
)

# ---------------------------------------------------------------- Part C: address interchange
C1 = infer(
    "C1",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones; for $A=0$ take $E_1=E_2=I$ and $\\Pi=0$.",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
    page="lower-triangular-factorization",
    frm=["matrices-and-linear-maps", "rational-numbers-and-rounding"],
)
C2 = show(
    "C2",
    "For a rational matrix $A$ of rank $a$, the shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ is done with exactly $a$ interchanges of $b$-digit fields and $O(V)$ other work.",
    "Write $A=E_1\\Pi E_2$, apply the lower triangular factors as controlled shifts, and realize each one in $\\Pi$ by a shear on a single pair of fields costing one interchange.",
    mot("Lower triangular updates target a later field from earlier fields, which is exactly the direction of controlled shifts, so only the $a$ pivots of $\\Pi$ need genuine interchanges.",
        "recoverable"),
    [
        infer("C2.1",
              "A lower triangular transformation of $H$ or of $D$ costs $O(V)$ by updating coordinates in descending physical order with controlled shifts.",
              "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
        infer("C2.2",
              "For $A=E_1\\Pi E_2$, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
              "For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
        infer("C2.3",
              "Each one of $\\Pi$ at $(i,j)$, meaning $H_i\\leftarrow H_i+D_j$, is done by $D_j\\leftarrow D_j+H_i$, the swap $(H_i,D_j)\\leftarrow(D_j,H_i)$ and $D_j\\leftarrow H_i-D_j$, with one interchange.",
              "On an initial pair $(h,d)$ this sequence yields $(h+d,d)$."),
    ],
    page="matrix-shear-cost",
    frm=["lower-triangular-factorization", "controlled-shifts", "stream-operations", "modular-arithmetic"],
)
C3 = show(
    "C3",
    "Two disjoint address chunks of $e=m^k$ radix-$q$ digits each, preceded by a row field of length divisible by $W^k$, are interchanged in $O(Ve^{\\tau})$ time.",
    "Split rows into $W$ role streams, run the bit network with each edge applying a shear $\\Phi_{A_e}$ done by smaller interchanges, obtain the shear $H\\leftarrow H+D$ on every row, finish with $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, and solve the recurrence for the normalized cost.",
    mot("An edge matrix of rank $a$ costs $a$ smaller interchanges, and because the ranks sum to less than $Wm$ the recurrence saves a power of the chunk width.",
        "explicit",
        "Because the sum of these ranks is less than the number of wires times"),
    [
        infer("C3.1",
              "For $k=0$ the interchange is the single-digit operation of the elementary stream lemma, costing $O(V)$.",
              "For $k=0$ apply the single-digit operation of"),
        infer("C3.2",
              "Rows are split cyclically into $W$ role streams of volume $V/W$ each with the same remaining shape, giving the common address set required by the frame identity.",
              "Split whole rows cyclically into $W$ role streams within each prefix"),
        infer("C3.3",
              "On every circuit edge the shear $\\Phi_{A_e}$ is applied to that role stream, implemented by recursively interchanging the pivot pairs of $b$-digit fields with $b=e/m$, and each gate acts pointwise on matching addresses.",
              "On every circuit edge apply"),
        infer("C3.4",
              "By the frame identity and $M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$ the result is $H\\leftarrow H+D$ on every original row, including rows assigned to scratch roles with arbitrary initial values.",
              "is $H\\leftarrow H+D$ on every original row, including rows assigned"),
        infer("C3.5",
              "The interchange of the two full chunks is $D\\leftarrow D-H$, then $H\\leftarrow H+D$, then $D\\leftarrow H-D$; only the middle shear uses the circuit and the others are linear-cost updates of the later group.",
              "D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,"),
        infer("C3.6",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a stream of volume $V/W$.",
              "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("C3.7",
              "The normalized cost $F_k$ satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
              "F_k\\le(s/W)F_{k-1}+O(1)."),
        infer("C3.8",
              "For $s/W<m^\\tau$ the geometric sum gives $F_k=O(e^\\tau)$.",
              "Hence $F_k=O(e^\\tau)$."),
        infer("C3.9",
              "A fixed-tape depth-first schedule parks the inactive role streams on a stack, so pushing, popping, copying and erasing cost $O(V)$ at each node and the recursion fits the stated recurrence.",
              "Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
    ],
    page="power-width-interchange",
    frm=["bit-shear-interface", "power-saving-recurrence", "matrix-shear-cost", "frames", "stream-operations",
         "controlled-shifts"],
    adds=[
        bind("e", "chunk width", "the number $m^k$ of radix-$q$ digits in each interchanged address chunk"),
        bind("k", "recursion depth", "the exponent with $e=m^k$, equal to the number of recursion levels", "count"),
    ],
)
C4 = show(
    "C4",
    "Two disjoint contiguous address fields of $u$ bits, with any gaps and even a one-bit payload, are interchanged in $O(Vu^{\\tau})$ time for the fixed $\\tau=1-2^{-50}<1$.",
    "Peel off $O(\\log e)$ high digits of each chunk to serve as a row field, pad the rows to a multiple of $W^k$, split the remaining width in base $m$ into power-width pieces, interchange each piece with the power-width procedure, and undo the padding.",
    mot("Rows for a general array can be supplied by a few of its own high digits, and moving them costs less than the final bound.",
        "explicit",
        "Rows for a general array can be supplied by a few of its own high digits."),
    [
        infer("C4.1",
              "Widths below a fixed bound are handled by individual digit interchanges, whose cost is absorbed in the constant of $O(Ve^\\tau)$.",
              "Handle the bounded remaining set of widths by $e$ individual digit"),
        infer("C4.2",
              "Swapping the top $\\rho=O(\\log e)$ digits pair by pair and joining them leaves a row field of range $R=q^{2\\rho}\\ge W^k$ before both remaining chunks.",
              "R=q^{2\\rho}\\ge W^k"),
        infer("C4.3",
              "Appending zero rows within each prefix until the row count is $R'=W^k\\lceil R/W^k\\rceil<2R$ at most doubles the volume, and the padded rows stay zero.",
              "R'=W^k\\left\\lceil R/W^k\\right\\rceil<2R."),
        infer("C4.4",
              "Writing the remaining width as $e-\\rho=\\sum_{j}a_jm^j$ with $0\\le a_j<m$ partitions each chunk into $a_j$ pieces of width $m^j$.",
              "e-\\rho=\\sum_{j=0}^{k} a_jm^j,\\qquad 0\\le a_j<m."),
        infer("C4.5",
              "Applying the power-width procedure to each corresponding pair costs $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$, a geometric sum because $a_j<m$ and $m^k<me$.",
              "O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)."),
        infer("C4.6",
              "Binary chunks of $u$ bits are padded numerically to $[q^e]$ with $e=O(u)$, an increase in volume by less than a factor $q^2$, and the padded entries are scanned away afterwards, giving $O(Vu^\\tau)$.",
              "Pad each of the two chunk ranges numerically from $[2^u]$"),
    ],
    page="arbitrary-width-interchange",
    frm=["power-width-interchange", "stream-operations", "binary-representation-and-bitwise-operations"],
)
C = show(
    "C",
    "Two address chunks of $u$ bits are interchanged in $O(Vu^{\\tau})$ time on a fixed number of tapes, with $\\tau=1-2^{-50}<1$.",
    "Turn the bit network into a recursion in which a shear on chunks of $m^k$ digits calls $s$ shears on $m^{k-1}$ digits over streams of volume $V/W$, make each rank unit cost one interchange by a triangular factorization, and then remove the power-width and row restrictions.",
    mot("An edge matrix of rank $a$ will require $a$ smaller interchanges, and the ranks sum to less than the number of wires times $m$, so the recursion saves a power of the chunk width.",
        "explicit",
        "An edge matrix of rank $a$ will require $a$ smaller interchanges."),
    [C1, C2, C3, C4],
)

# ---------------------------------------------------------------- Part D: butterfly layers
P_pack = show(
    "D5",
    "A binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ at the selected positions $j_i=\\rho+iK$, $0\\le i<f$, of two address chunks, using a third chunk $z$ of arbitrary contents that is restored, costs $O(V(L^\\tau+1))$ with $L=fK$.",
    "Apply a constant number of whole-chunk cyclic shifts that realize the XORs correctly except on a small address set, then repair that explicitly bounded set deterministically by extracting, key-sorting and reinserting its records.",
    mot("A cyclic shift of a whole chunk adds the same offset to all selected segments at once, but it can carry between segments, so it is correct only away from a rare set of guard values that must be repaired separately.",
        "reconstructed"),
    [
        infer("D5.1",
              "In the stated regime ($A_{\\rm rect}=O(p)$, $R$ above every fixed polynomial in $p$, $f\\le d\\le p$, $K/\\log p\\to\\infty$) the whole operation costs $O(V(L^\\tau+1))$.",
              "$O(V(L^\\tau+1))$, uniformly over the permitted lengths and payloads"),
        infer("D5.2",
              "Eight conditional shifts of $\\pm1$ with parity tests flip the parity of $u$ exactly when the control $c=1$ and restore the auxiliary integer $w$, so each coordinate moves by at most four.",
              "Here $u\\bmod2\\in\\{0,1\\}$, also for negative $u$. Thus the parity of $u$"),
        infer("D5.3",
              "Away from addresses where some guard value falls in an excluded interval (twenty excluded values per guard) no segment carries into the next, so the packed shifts agree with the ideal XOR permutation; the bad set has size at most $\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.",
              "There are exactly twenty excluded values for each guard in"),
        infer("D5.4",
              "The correction scans the stream, extracts the records at the exceptional addresses and computes each destination rank directly from the chunk values.",
              "To implement the correction, scan the stream with a record-rank counter."),
        infer("D5.5",
              "Stable radix sorting of the extracted records by destination key and one reinsertion scan implement the ideal map on the bad set, since $T_0S_0^{-1}$ permutes it.",
              "Hold the full stream untouched"),
    ],
    page="packed-selected-bit-addition",
    frm=["arbitrary-width-interchange", "controlled-shifts", "stream-operations", "xor-linear-network"],
    salient="A third chunk of arbitrary contents is used as temporary storage and comes back unchanged, and the only inexact addresses are a fraction $O(f2^{-K})$ of all addresses, which is why sorting them is affordable.",
)

D = show(
    "D",
    "The two-point butterfly $H_0$ applied at once to the same bit of $D\\le d$ address chunks of every polynomial record is computed exactly and then truncated once by $Q_p$ in $O(Vd^{\\lambda'})$ time, with error below $\\sqrt2\\,2^{-p}$, for a fixed $\\lambda'<1$.",
    "Rewrite $H_0^{\\otimes D}$ through the phase tensor power $C^{\\otimes D}$, evaluate $C^{\\otimes e}$ with the complex phase network whose edges are $s_{\\rm c}$ smaller layers on $e/m$ axes, implement the binary changes of basis by packed selected-bit additions, and unroll the recurrence.",
    mot("Applying one butterfly factor per selected bit would need $D$ whole-array passes, whereas the recursive network needs only a power $d^{\\lambda'}$ of them.",
        "explicit",
        "$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly"),
    [
        infer("D1",
              "An arbitrary residual basis is moved onto coordinate directions by conjugating with an address permutation $\\mathcal P_M$, since $\\mathcal P_MX_v\\mathcal P_M^{-1}=X_{Mv}$, and $\\mathcal P_M$ factors into a fixed number of row additions.",
              "\\mathcal P_MX_v\\mathcal P_M^{-1}=X_{Mv}."),
        infer("D2",
              "A negative directional kernel needs only a forward child because $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$.",
              "=(-i)^f Z^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}."),
        infer("D3",
              "Applying the phase network with column frames to $e=mf$ selected axes gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
              "$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
        infer("D4",
              "The normalized butterfly layer is $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, where $\\mathcal S_D$ multiplies by $i^{x_1+\\cdots+x_D}$ and $b^D$ is a binary shift with a fourth-root phase and at most one factor $b$.",
              "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."),
        P_pack,
        infer("D6",
              "Splitting the row index among the $W$ roles gives each recursive edge call a stream of exactly $1/W$ of its parent's volume, with padded rows kept zero.",
              "one role stream with volume exactly \\(1/W\\) of its parent"),
        infer("D7",
              "With $F(e)$ the time divided by volume, $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ and $F(e)=O(e)$ for $e<d^\\beta$.",
              "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
        infer("D8",
              "Unrolling with $s/W<m^\\sigma$ and a base-$m$ partition of the $D$ chunks gives total cost $O(d^{\\lambda'})$ per unit volume for any fixed $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
              "=O(d^{\\lambda'})"),
        infer("D9",
              "The procedure returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time, uniformly in $p,d,r,D,P,S,\\rho,w$ and $z$.",
              "The procedure returns $Q_p(\\mathcal H z)$ in the same array,"),
        infer("D10",
              "The phase-frame construction reduces a group of $e$ selected bits to $s_{\\rm c}$ children on $e/m$ bits and the row split gives each child $1/W_{\\rm c}$ of the volume.",
              "The phase-frame construction reduces a group of $e$ selected bits to"),
        infer("D11",
              "Denominator and magnitude growth are bounded by $\\lceil C_0d^{C_1}\\rceil=o(p)$, so every intermediate coefficient is represented exactly in $O(p)$ bits and only the final truncation rounds.",
              "every intermediate coefficient is represented exactly with"),
    ],
    page="simultaneous-butterfly-layer",
    frm=["phase-frame-network", "packed-selected-bit-addition", "power-saving-recurrence", "arbitrary-width-interchange",
         "fixed-point-disk", "negacyclic-ring", "butterfly", "rank-deficit"],
)

T = show(
    "T",
    "There are fixed-tape procedures that interchange two address chunks of $u$ bits in $O(Vu^{\\tau})$ time and apply a butterfly layer to $D\\le d$ address chunks in $O(Vd^{\\lambda'})$ time, for fixed $\\tau,\\lambda'<1$ and data of volume $V$.",
    "Obtain each procedure from a fixed linear network that exchanges two banks of values and restores its scratch wires, whose changes of representation along its edges are smaller calls of the same procedure, strictly fewer than $Wm$ in total.",
    mot("A strict inequality on the number $s$ of smaller calls makes the recursive contribution grow by a factor below $m$ per level, and this strict inequality is the source of the power saving.",
        "explicit",
        "is the source of the power saving."),
    [A, B, C, D],
)

# ---------------------------------------------------------------- Part X: synthetic transforms and products
E1 = show(
    "E1",
    "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$, the transforms $F_t^{\\pm}$ with roots $\\omega_t=y^{2r/t}$ are contractions satisfying $F_t^+F_t^-=t^{-1}I$ despite zero divisors, and $F_t^-$ is computed by decimation-in-frequency rounds of butterflies and monomial twiddles.",
    "Use that every power of $\\omega_t$ is an isometry for the contraction bound, prove character cancellation directly by pairing summands (the ring has zero divisors, so one cannot divide by $\\omega_t^j-1$), and split the transform into a butterfly and a monomial twiddle.",
    mot("Multiplication by a power of $y$ is a signed shift of the coefficient list, so roots of unity cost only a shift.",
        "explicit",
        "such a root is a signed shift of the coefficient list. These are the"),
    [
        infer("E1.1",
              "Every power of $\\omega_t$ is an isometry and each transform entry averages $t$ such images, so both transforms are contractions.",
              "Thus both transforms are contractions."),
        infer("E1.2",
              "With $j=2^vj_0$, $j_0$ odd, shifting $k$ by $t/2^{v+1}$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$, so the sum is zero when $t\\nmid j$ because the additive group has no two-torsion, giving $\\sum_k\\omega_t^{jk}=t$ if $t\\mid j$ and $F_t^+F_t^-=t^{-1}I$.",
              "Hence the sum is zero, since the additive group of"),
        infer("E1.3",
              "The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by the monomial $\\omega_t^{-k}$ and recurses on both halves of length $t/2$.",
              "decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"),
    ],
    page="synthetic-transform",
    frm=["negacyclic-ring", "dft", "butterfly", "roots-of-unity", "error-accounting"],
)
E2 = show(
    "E2",
    "The recursion writes frequencies in bit-reversed slots, entry $j$ in slot $\\operatorname{rev}_a(j)$; the forward transform keeps this order through the pointwise product and the opposite transform consumes it, so no sort is executed.",
    "Track which address-bit slot holds which frequency bit through the rounds, then show that the reversed recursion composed with the forward one gives $I/t$ so it is the correct opposite of the stored order.",
    mot("A sort of the frequency entries would cost a full movement pass, which the power saving cannot afford, so the order is kept and consumed as it is.",
        "reconstructed"),
    [
        infer("E2.1",
              "After all $a=\\log_2t$ rounds the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$, i.e. the output is $B_tF_t^-z$ with $B_t$ the bit-reversal record permutation.",
              "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$."),
        infer("E2.2",
              "The recursion writes its outputs directly in this order and does not move whole frequency indices.",
              "it does not move whole frequency indices."),
        infer("E2.3",
              "The reverse procedure processes the smaller branches first, then the inverse monomial, then $H_0$, and since $H_0^2=I/2$ it composed with $B_tF_t^-$ gives $2^{-a}I=I/t$.",
              "so the reverse procedure composed with $B_tF_t^-$ is"),
        infer("E2.4",
              "The two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
              "B_tF_t^-,\\qquad F_t^+B_t^{-1},"),
    ],
    page="retained-frequency-order",
    frm=["synthetic-transform", "permutations"],
    salient="No permutation is ever applied: the bit-reversal produced by the recursion is simply retained through the pointwise product and undone by the opposite transform's own reversed arithmetic.",
)
E3 = show(
    "E3",
    "With a layout permutation $L$ placing the selected bits of all axes at a common offset in consecutive $K$-bit chunks, the forward and opposite synthetic transforms on $M$ records of $r$ coefficients cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
    "Group one butterfly per participating axis into a parallel butterfly followed by a monomial twiddle, build $L$ from prefix moves and chunk exchanges so each round is one simultaneous layer, and add the three costs and the per-round errors.",
    mot("A round is a simultaneous layer only if the selected bits of all axes sit at the same offset in consecutive chunks, so the data must first be rearranged.",
        "explicit",
        "we must place the selected bits of the participating axes at a common"),
    [
        infer("E3.1",
              "The individual axis steps of a round group into one parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$, because the twiddle of an axis depends only on that axis's address bits and commutes with the other axes' butterflies.",
              "butterfly $\\mathcal H$, followed by one recordwise monomial operation"),
        infer("E3.2",
              "Each $\\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction.",
              "$J_E$ is an isometry, so every completed round is a contraction."),
        infer("E3.3",
              "The simultaneous layer supplies one truncated contraction per round, at most $\\ell$ rounds in all.",
              "The layer then supplies one truncated contraction per round,"),
        infer("E3.4",
              "Moving at most $D(b+1)=O(dK)$ listed bit slots into a prefix costs $O(TpdK)$.",
              "listed slots, so the moves cost $O(TpdK)$."),
        infer("E3.5",
              "At most $Dq-1$ exchanges of width-$K$ chunks, each costing $O(TpK^\\tau)$, cost $O(Tp\\,pK^{\\tau-1})$ in total.",
              "=O\\bigl(Tp\\,pK^{\\tau-1}\\bigr)."),
        infer("E3.6",
              "Starting from zero error, at most $\\ell$ rounds each adding a truncation of size below $\\sqrt2\\,2^{-p}$ give error below $\\sqrt2\\,\\ell\\,2^{-p}$, and the layout permutations are isometries.",
              "zero error, at most $\\ell$ rounds therefore"),
    ],
    page="transform-layout",
    frm=["simultaneous-butterfly-layer", "arbitrary-width-interchange", "retained-frequency-order",
         "synthetic-transform", "stream-operations"],
)
F1 = show(
    "F1",
    "For disk grid polynomials $f,g\\in\\mathcal R_r$, the exact Gaussian integer numerators of $fg$ and then $Q_p(fg/r)$ are computed in $O(rp\\log(rp))$ time by evaluating at $2^{4p}$ and multiplying integers with the established multiplier.",
    "Use a signed form of Kronecker substitution: evaluate each coefficient polynomial at $B_0=2^{4p}$, multiply four pairs of integers, read the product coefficients back by centered residues, and wrap negacyclically.",
    mot("The established $O(N\\log N)$ multiplier handles integers, so polynomial records have to be turned into integers, with signs handled by centered residues.",
        "explicit",
        "This is an independent subroutine."),
    [
        infer("F1.1",
              "The product of two disk grid polynomials of $r<2^p$ coefficients is returned as $Q_p(fg/r)$, with error below $\\sqrt2\\,2^{-p}$, in time $O(rp\\log(rp))$.",
              "$O(rp\\log(rp))$ on a fixed number of tapes."),
        infer("F1.2",
              "Evaluating the integer coefficient polynomials at $B_0=2^{4p}$ gives signed integers whose magnitudes fit in $4pr$ bits.",
              "Set $B_0=2^{4p}$"),
        infer("F1.3",
              "Every ordinary product coefficient satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so each coefficient is identified as the centered residue modulo $B_0$ after the lower ones are removed.",
              "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2."),
        infer("F1.4",
              "Hence the carry recurrence recovers every $h_j$ exactly: $\\widehat h_j=h_j$.",
              "Thus $\\widehat h_j=h_j$."),
        infer("F1.5",
              "Four exact integer products dominate the linear packing, extraction, combination, wrapping and truncation costs, giving $O(rp\\log(rp))$.",
              "Four exact integer products dominate the linear"),
    ],
    page="signed-packing-product",
    frm=["negacyclic-ring", "fixed-point-disk", "established-multiplier"],
)
F2 = show(
    "F2",
    "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ on disk grid operands is approximated with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "Do both forward synthetic transforms in the retained layout order, multiply the records pointwise by the ring product divided by $r$, apply the opposite transform and scale exactly by $M$, using $F^-(f*g)=M(F^-f)(F^-g)$.",
    mot("The convolution theorem turns convolution into a pointwise product, and keeping one layout order across the three stages avoids any extra permutation.",
        "recoverable"),
    [
        infer("F2.1",
              "Perform both forward transforms and keep their common $LB$ order; pass the records to the packed ring product and then to the opposite procedure.",
              "Perform both forward transforms and retain their common $LB$ order."),
        infer("F2.2",
              "Expansion of the finite sums gives $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$, so with $F^+F^-=I/M$ the scaled chain equals $(f*g)/(rM)$.",
              "=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)."),
        infer("F2.3",
              "Since $LB$ permutes records and leaves polynomial suffixes intact, the pointwise product commutes with it, so the stored forward outputs can be multiplied directly.",
              "Since $LB$ permutes records and leaves their polynomial suffixes"),
        infer("F2.4",
              "The two forward errors $\\delta$ propagate through the bilinear product to $2\\delta$, the truncation adds $\\eta$ and the opposite transform is a contraction, so the error is below $M(3\\delta+\\eta)=\\sqrt2M(3\\ell+1)2^{-p}$ after scaling by $M$.",
              "The final exact multiplication by $M$ therefore gives error less than"),
    ],
    page="synthetic-convolution",
    frm=["cyclic-convolution", "multidimensional-dft", "transform-layout", "signed-packing-product",
         "retained-frequency-order", "error-accounting"],
)
X = show(
    "X",
    "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with $r=2^\\ell$ the normalized cyclic convolution of two disk grid arrays on $d-1$ power-of-two axes is computed with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$, where $T=rM$.",
    "Compute convolution as two forward synthetic transforms, a pointwise ring product and an opposite transform, with roots of unity realized as signed shifts, the rounds done by simultaneous butterfly layers on a chunked layout, and the frequency order retained in between.",
    mot("Roots of unity that are powers of $y$ act as exact signed permutations of coefficient lists, so the transform needs no arithmetic with general roots of unity.",
        "explicit",
        "where the required roots of unity act by exact signed permutations"),
    [E1, E2, E3, F1, F2],
    adds=[
        bind("r", "record length", "the number of complex coefficients in a polynomial record", "count"),
        bind("M", "record count", "the number of ring-valued records, the product of the first $d-1$ axis lengths", "count"),
        bind("\\ell", "log record length", "the exponent with $r=2^{\\ell}$"),
    ],
)

# ---------------------------------------------------------------- Part Y: resampling
G1 = show(
    "G1",
    "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computed on the disk grid with errors below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
    "Write the Fourier transform of length $s$ through Gaussian-weighted maps $\\mathsf S,\\mathsf T$ and a diagonal correction, invert $N=C\\mathsf T\\mathsf D$ by a Neumann series, and normalize so both maps become contractions.",
    mot("Gaussian weights make the map between length $s$ and length $t$ transforms nearly diagonal, so the leftover $N-I$ is small enough to invert by a series.",
        "recoverable"),
    [
        infer("G1.1",
              "Linear contractions $A$ and $B_0$ exist with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, where the permutations $P_s,P_t$ remain inside the identity instead of being executed.",
              "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."),
        infer("G1.2",
              "The Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the estimate $\\|N-I\\|<2^{-\\alpha^2\\theta}$ hold with $N=C\\mathsf T\\mathsf D$.",
              "\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}."),
        infer("G1.3",
              "Since $\\alpha^2\\theta>1$, $\\|N-I\\|<1/2$ and $N$ is invertible by the Neumann series.",
              "Thus $\\|N-I\\|<1/2$, so $N$ is invertible"),
        infer("G1.4",
              "The normalizations $2^{-(2\\alpha^2-2)}$, $1/2$ and $1/2$ multiply to $2^{-2\\alpha^2}$, so $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
              "$2^{-(2\\alpha^2-2)}2^{-1}2^{-1}=2^{-2\\alpha^2}$."),
    ],
    page="gaussian-resampling",
    frm=["dft", "fixed-point-disk", "error-accounting", "established-multiplier", "newton-s-method",
         "triangle-inequality-and-norms"],
)
G2 = show(
    "G2",
    "In $d$ dimensions, applying the one-dimensional maps line by line on the zero-padded box of $T=\\prod_it_i$ entries gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ at cost $O(dTp^{3/2+\\delta}\\alpha)$ plus $O(Tp\\,d^2(1+\\ell^\\tau))$ for axis movement.",
    "Tensor the one-dimensional identity, expand or compress one axis at a time on valid lines of the padded box, and expose each axis with address-chunk interchanges.",
    mot("The tape procedures work on contiguous address fields, so each axis must be brought innermost by chunk interchanges before its line maps run.",
        "reconstructed"),
    [
        infer("G2.1",
              "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
              "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,"),
        infer("G2.2",
              "The linewise implementations of $\\mathcal A$ and $\\mathcal B_0$ each have error below $dp^2$.",
              "Both $\\mathcal A$ and $\\mathcal B_0$ are contractions."),
        infer("G2.3",
              "At most $T/t_i$ lines are processed on axis $i$, so the line maps cost $\\sum_i(T/t_i)O(t_ip^{3/2+\\delta}\\alpha)=O(dTp^{3/2+\\delta}\\alpha)$.",
              "The total time spent in the"),
        infer("G2.4",
              "Exposing and restoring all lines costs $O(Tp\\,d^2(1+\\ell^\\tau))$ by the equal-width chunk-swap bound, because each adjacent interchange costs $O(Tp(1+\\ell^\\tau))$ and $O(d^2)$ are needed.",
              "O\\bigl(Tp\\,d^2(1+\\ell^\\tau)\\bigr)", nth=0),
    ],
    page="padded-box-tensor-resampling",
    frm=["gaussian-resampling", "multidimensional-dft", "arbitrary-width-interchange", "stream-operations"],
)
G3 = show(
    "G3",
    "The source permutation $R$ left in the resampling identity cancels across two forward transforms, the pointwise product and the opposite-sign transform, giving $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$, while the middle transform $QF_{\\boldsymbol t}$ becomes a convolution with a chirp.",
    "Write $QF_{\\boldsymbol t}$ by Bluestein's chirp identity, and show that conjugating the opposite transform by $R$ removes it using that each $t_i$ is a unit modulo $s_i$.",
    mot("Sorting the coordinates twice per axis would cost full movement passes, so the permutations are kept inside the transform formula, where the dilation structure lets them cancel.",
        "explicit",
        "We retain both permutations in the transform formula and"),
    [
        infer("G3.1",
              "For the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_is_ij_i^2/t_i)$, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
              "\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}."),
        infer("G3.2",
              "The coefficient of $u_{\\boldsymbol k}$ on the right is $\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$, which is precisely the coefficient of $QF_{\\boldsymbol t}$ because $Q$ reads frequency $-s_ij_i$.",
              "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because"),
        infer("G3.3",
              "Each $t_i$ is a unit modulo $s_i$, so for the dilation $(R_cz)_j=z_{cj}$ one has $F_q^+R_c=R_c^{-1}F_q^+$, hence $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$.",
              "Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives"),
        infer("G3.4",
              "With $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)\\cdot(F_{\\boldsymbol s}v)$ and $F_{\\boldsymbol s}^+F_{\\boldsymbol s}=I/S$ the two normalizations give $F_{\\boldsymbol s}^+(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)=(u*v)/S^2$.",
              "proving \\eqref{eq:source-permutation-cancel}."),
    ],
    page="permutation-cancellation",
    frm=["gaussian-resampling", "bluestein-chirp", "cyclic-convolution", "multidimensional-dft", "permutations",
         "modular-arithmetic"],
    salient="The permutation $R$ that Gaussian resampling forces on the source transform vanishes entirely from the product $(u*v)/S^2$, so neither $R$ nor its inverse is ever executed on tape.",
)
Y = show(
    "Y",
    "The Fourier transforms of pairwise coprime lengths $s_i$ needed for the convolution are expressed through power-of-two tensor transforms with their permutations retained, which cancel in the product, and the middle transform becomes a chirp convolution.",
    "Apply Gaussian resampling line by line on a padded box, keep the source and target coordinate permutations in the transform identity, convert the middle transform to a convolution by Bluestein's chirp, and show the retained source permutation cancels.",
    mot("The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two, so Gaussian resampling connects these two shapes.",
        "explicit",
        "whereas the synthetic transforms use powers of two. Gaussian resampling"),
    [G1, G2, G3],
)

# ---------------------------------------------------------------- Part Z: assembly
H1 = show(
    "H1",
    "With $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, $K=\\lfloor d^{c}\\rfloor$, $\\epsilon=2^{-75}$, $c=2^{-56}$, the box has axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod_it_i=T$ and distinct primes $s_i$ just below $t_i$ with $T/2<S<T$, and all resampling hypotheses hold.",
    "Fix rational exponents satisfying every layer condition with room to spare, derive the sizes from $n$, pick the primes by the prime-interval estimate and deterministic trial division, and check that radix digits cannot wrap around.",
    mot("The distinct prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box while each ratio $t_i/s_i$ leaves enough separation for resampling.",
        "explicit",
        "The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        infer("H1.1",
              "The fixed rational parameters are $\\tau=\\sigma=1-2^{-50}$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$.",
              "C_1=20,\\qquad \\epsilon=2^{-75},\\qquad \\kappa=2^{-182}."),
        infer("H1.2",
              "For large $n$ set $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$.",
              "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
        infer("H1.3",
              "With $T\\in[4n/b,8n/b)$ a power of two and $r=2^{\\lceil(\\log_2T)/d\\rceil}$, the axis lengths satisfy $t_i\\in\\{r/2,r\\}$, $\\prod_it_i=T$ and $t_d=r$.",
              "t_i\\in\\{r/2,r\\},\\qquad \\prod_i t_i=T,\\qquad t_d=r."),
        infer("H1.4",
              "The prime-interval estimate gives enough primes to choose distinct odd $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, where $\\eta=1/(4d)$.",
              "(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i."),
        infer("H1.5",
              "Multiplying the lower bounds and applying Bernoulli's inequality gives $S/T>(1-\\tfrac1{2d})^d>\\tfrac12$, hence $T/2<S<T$.",
              "Together with $s_i<t_i$, this gives $T/2<S<T$."),
        infer("H1.6",
              "Then $\\alpha^4\\theta_i>3db\\ge p$, so the separation hypothesis of the resampling lemma holds for all large $n$.",
              "\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\geq6b=p."),
        infer("H1.7",
              "The primes are found deterministically by scanning the two intervals and trial division, in time $n^{o(1)}=o(n)$.",
              "The machine finds these primes by scanning the two intervals"),
        infer("H1.8",
              "The product of two radix-$2^b$ digit polynomials has degree at most $2q-2<2n/b\\le T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
              "Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
    ],
    page="prime-axis-parameters",
    frm=["radix-digit-convolution", "primes-coprimality-and-gcd", "logarithms-exponentials-floor-and-ceiling"],
    salient="The primes $s_i$ lie just below the powers of two $t_i$, yet their product $S$ still exceeds half of the box size $T$ even though there are $d$ of them.",
)
H2 = show(
    "H2",
    "For pairwise coprime $s_i$ with product $S$, the map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism turning one cyclic convolution of length $S$ into a multidimensional cyclic convolution on the prime axes, and on tape it is a sequence of prefix-controlled cyclic shifts costing $O(Tp\\,d^2(1+\\ell^\\tau))$.",
    "Use the Chinese remainder theorem with coordinate exponents $\\mu_i=P_i^{-1}\\pmod{s_i}$ so that each axis coordinate depends only on lower-index digits, which makes every update a shift controlled by earlier fields.",
    mot("A shift controlled by earlier fields is linear in time, so choosing the exponents to make the map triangular keeps the change of order cheap.",
        "explicit",
        "with coordinate powers that make the change of order a"),
    [
        infer("H2.1",
              "The image of $x$ has order $S$ because each $\\mu_i$ is a unit and the $s_i$ are pairwise coprime, so the map is an isomorphism and preserves cyclic convolution.",
              "$\\Phi$ is an isomorphism and preserves cyclic convolution."),
        infer("H2.2",
              "In mixed radix $k=\\sum_ja_jP_j$ the axis-$i$ coordinate is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i\\equiv1$.",
              "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}."),
        infer("H2.3",
              "Each step rotates the valid interval $[0,s_i)$ and fixes $[s_i,t_i)$, a bijection of the padded box that preserves the valid set, so zero padding remains zero after every step.",
              "zero padding remains zero after every step."),
        infer("H2.4",
              "Each triangular update is a prefix-controlled cyclic shift: split the valid target interval in two pieces and merge them in the opposite order.",
              "Each triangular update is a prefix-controlled cyclic shift."),
        infer("H2.5",
              "With axis widths $\\ell$ or $\\ell-1$, reordering the axes uses $O(d^2)$ chunk swaps, so $\\Phi$, its inverse and the padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              "O\\bigl(Tp\\,d^2(1+\\ell^\\tau)\\bigr).", after=4195),
    ],
    page="crt-map",
    frm=["cyclic-convolution", "multidimensional-dft", "controlled-shifts", "arbitrary-width-interchange",
         "radix-digit-convolution", "modular-arithmetic", "primes-coprimality-and-gcd"],
)
H3 = show(
    "H3",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathcal R_r$, turning the last cyclic axis into a polynomial ring so that its negative wrap becomes the cyclic wrap after untwisting, at cost $O(Tp^{1+\\delta})$.",
    "Define the twist $x_d\\mapsto\\zeta y$, check it respects the relation and is diagonal on the monomial bases, and verify directly that the sign of the wrap is cancelled by $\\zeta^r=-1$.",
    mot("The synthetic transforms only handle the ring $\\mathbb C[y]/(y^r+1)$, while the chirp identity needs a cyclic convolution, so a diagonal change of basis connects them.",
        "recoverable"),
    [
        infer("H3.1",
              "The map $x_d\\mapsto\\zeta y$ is well defined since $(\\zeta y)^r=(-1)(-1)=1$, diagonal with entries $\\zeta^k$, hence an isomorphism preserving the sup norm.",
              "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."),
        infer("H3.2",
              "For the wrap, write $k+l=j+hr$ with $h\\in\\{0,1\\}$; the factor is $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$, so the exceptional wrapped terms with $h=1$ carry no extra sign.",
              "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j."),
        infer("H3.3",
              "Untwisting therefore recovers the cyclic coefficient with the correct sign.",
              "Untwisting therefore recovers the cyclic coefficient with the correct"),
        infer("H3.4",
              "Generating every twist factor anew with exact dyadic products and truncations costs $O(Tp^{1+\\delta})$ in total.",
              "twist cost $O(Tp^{1+\\delta})$."),
    ],
    page="phase-twist",
    frm=["negacyclic-ring", "synthetic-convolution", "cyclic-convolution", "roots-of-unity"],
)
H4 = show(
    "H4",
    "The source Fourier transform $RF_{\\boldsymbol s}$ is computed as $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$: Gaussian expansion on each line, the chirp transform (a twisted synthetic convolution) and Gaussian compression, then a power-of-two scaling, with tracked disk margins and errors.",
    "Compose the linewise expansion map, the chirp transform built from the twisted synthetic convolution with two endpoint phase multiplications, and the linewise compression map, then scale exactly by a power of two.",
    mot("Each stage is a contraction that was already analysed, so the composite is analysed by inserting exact maps at computed inputs and adding the errors.",
        "recoverable"),
    [
        infer("H4.1",
              "Computing the chirp numerators modulo $2r$ and the exponentials costs $O(Tdp^{1+\\delta})$ in total.",
              "construction costs $O(Td p^{1+\\delta})$ in total."),
        infer("H4.2",
              "The computed chirp transform multiplies by the conjugate chirp, convolves with the chirp kernel by the twisted complex convolution, and multiplies by the conjugate chirp again.",
              "y_0&=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0),"),
        infer("H4.3",
              "The exact counterpart of the source transform is $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$ by the tensor resampling identity.",
              "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A"),
        infer("H4.4",
              "The opposite-sign procedure is obtained by conjugating input and output, with exact counterpart $RF_{\\boldsymbol s}^+$.",
              "its exact counterpart is $RF_{\\boldsymbol s}^{+}$ by"),
    ],
    page="source-transform",
    frm=["padded-box-tensor-resampling", "permutation-cancellation", "bluestein-chirp", "phase-twist",
         "synthetic-convolution", "gaussian-resampling", "error-accounting"],
)
H5 = show(
    "H5",
    "The algorithm extracts radix digits, maps them to prime axes, takes two source transforms, a truncated pointwise product and one opposite-sign transform, rescales by $S$ and $2^{2b+4}$, rounds, inverts the address map and propagates carries to produce the $2n$-bit product.",
    "Run the radix-digit convolution through the source transforms: two forward transforms, a pointwise product, an opposite-sign transform, then two exact rescalings that undo the normalizations before rounding.",
    mot("The two forward transforms and the opposite-sign one reproduce the convolution $(u*v)/S^2$ by the cancellation identity, so only known scalings remain to be removed.",
        "recoverable"),
    [
        infer("H5.0",
              "The inputs are read backward in groups of $b$ bits to give radix-$2^b$ digits, stored as grid numerators $a_j2^{p-b-2}$, and padded with zero records to length $S$.",
              "Read each stored operand backward from"),
        infer("H5.1",
              "Step 1 applies the coefficient-address map $\\Phi$ with its padded layout to obtain source arrays $u,v$ of norm below $1/4$.",
              "\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"),
        infer("H5.2",
              "Step 2 computes the source transforms $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
              "\\item Compute $\\widetilde{\\mathscr F}(u)$ and"),
        infer("H5.3",
              "Step 3 multiplies corresponding coefficients exactly and truncates to $p$ fractional bits, giving $z$.",
              "\\item Multiply corresponding complex coefficients exactly and truncate"),
        infer("H5.4",
              "Step 4 computes the opposite-sign transform $\\widetilde{\\mathscr F}^{+}(z)$ and multiplies the numerators exactly by $S$, giving $\\widetilde w$.",
              "\\item Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
        infer("H5.5",
              "Step 5 multiplies by $2^{2b+4}S$, rounds each real value to the nearest integer, writes it in a $(3b+1)$-bit word and applies $\\Phi^{-1}$ with the padding removed.",
              "\\item Multiply the grid numerators of $\\widetilde w$ exactly by"),
        infer("H5.6",
              "Step 6 propagates radix-$2^b$ carries in increasing coefficient order and outputs exactly $2n$ bits.",
              "\\item Propagate radix-$2^b$ carries in increasing coefficient order."),
        infer("H5.7",
              "The two occurrences of $S$ undo different normalizations: after three transforms the exact result is $(u*v)/S^2$, the first scale gives $(u*v)/S$ and the second, with $2^{2b+4}$, gives the integer convolution.",
              "The two occurrences of $S$ in this algorithm undo different"),
    ],
    page="multiplication-algorithm",
    frm=["source-transform", "crt-map", "radix-digit-convolution", "permutation-cancellation", "exact-recovery"],
)
H6 = show(
    "H6",
    "The final error of each recovered convolution coefficient is below $448b\\,2^{-b+\\gamma}<1/2$, so rounding gives the true integer coefficient, which is below $2^{3b}$, and carries give the exact product.",
    "Track disk margins and error bounds through the composition, using that bilinear contractions add the two operand errors and linear contractions do not increase errors, then multiply the error by the two scale factors $S$ and $2^{2b+4}$.",
    mot("Errors of composed approximate steps add, and the final answer is rounded to integers, so it suffices to bound the accumulated error by $1/2$.",
        "recoverable"),
    [
        infer("H6.1",
              "Two normalized synthetic forwards, the pointwise product and the opposite transform give a ring convolution with error below $E_{\\rm ring}=M(3L+2)<5TL$ in units of $2^{-p}$, and one operand of norm at most $.7$ keeps the output a disk array.",
              "E_{\\rm ring}:=M(3L+2)<5TL."),
        infer("H6.2",
              "The source transform has error below $E_s=9\\cdot2^\\gamma TL$ in units of $2^{-p}$ and stays in the disk.",
              "E_s=9\\,2^\\gamma TL,"),
        infer("H6.3",
              "After the pointwise product, the opposite-sign transform and the scale by $S$, $\\widetilde w$ approximates $w=(u*v)/S$ with error below $E_w=S(3E_s+2)<28\\cdot2^\\gamma T^2L$.",
              "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L."),
        infer("H6.4",
              "Since $S\\le T<2^b$ and $L<b$, multiplying the error by $2^{2b+4}S$ and the grid size $2^{-6b}$ gives a final error below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$.",
              "<448b\\,2^{-b+\\gamma}"),
        infer("H6.5",
              "The true coefficients are integers and the error is strictly below $1/2$, so the nearest integer to each computed value is the unique correct coefficient, below $2^{3b}$ by the capacity bound.",
              "The strict error below $1/2$ makes the nearest integer to"),
        infer("H6.6",
              "Carries in the recurrence $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$, so $b$-bit digits with $O(b)$-bit carries yield the exact product.",
              "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$."),
    ],
    page="exact-recovery",
    frm=["error-accounting", "source-transform", "radix-digit-convolution", "permutation-cancellation",
         "phase-twist", "synthetic-convolution", "rational-numbers-and-rounding"],
)
H7 = show(
    "H7",
    "Divided by the volume $V=Tp$, the seven dominant costs are each at most $p^{1-2\\kappa}$, the smallest margin below one being $2^{-181}=2\\kappa$, which absorbs log factors and gives total time $O(n(\\log n)^{1-\\kappa})$.",
    "List every cost per unit volume as a power of $p$, compute its margin below $1$ for the fixed exponents, take the minimum, and absorb setup, exceptional streams and fixed powers of $\\log p$ into the slack.",
    mot("The explicit slack in the smallest margin covers any remaining fixed power of $\\log p$, so only the margins of the dominant terms need computing.",
        "explicit",
        "This explicit slack will cover"),
    [
        infer("H7.1",
              "Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $p^{\\epsilon(1+c)}$.",
              "Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$\\\\"),
        infer("H7.2",
              "Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, a power $p^{1-\\epsilon c(1-\\tau)}$.",
              "Chunk exchanges for transform layout & $pK^{\\tau-1}$ & $1-\\epsilon c(1-\\tau)$\\\\"),
        infer("H7.3",
              "Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, a power $p^{1-\\epsilon(1-\\lambda')}$.",
              "Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$\\\\"),
        infer("H7.4",
              "CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, a power $p^{\\tau+\\epsilon(2-\\tau)}$.",
              "CRT and axis layouts & $d^2(1+\\ell^\\tau)$ & $\\tau+\\epsilon(2-\\tau)$\\\\"),
        infer("H7.5",
              "Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, a power $p^{3/4+\\delta+3\\epsilon/2}$.",
              "Gaussian line maps & $dp^{1/2+\\delta}\\alpha$ & $3/4+\\delta+3\\epsilon/2$\\\\"),
        infer("H7.6",
              "Chirps, twists and scalar products cost $dp^\\delta$, a power $p^{\\epsilon+\\delta}$.",
              "Chirps, twists and scalar products & $dp^\\delta$ & $\\epsilon+\\delta$\\\\"),
        infer("H7.7",
              "Packed polynomial products cost $\\log(rp)$, a power $p^{1-\\epsilon}$, using the established multiplier only on records of $O(rp)=o(n)$ bits.",
              "Packed polynomial products & $\\log(rp)$ & $1-\\epsilon$\\\\"),
        infer("H7.8",
              "The margins below one are $g_1>1/2$, $g_2=\\epsilon c(1-\\tau)=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$.",
              "g_1>\\frac12,\\quad g_2=2^{-181},\\quad g_3=2^{-129},\\quad"),
        infer("H7.9",
              "Hence $\\min_ig_i=2^{-181}=2\\kappa$, attained by the chunk exchanges, because $\\epsilon c(1-\\tau)=2^{-75}2^{-56}2^{-50}$.",
              "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
        infer("H7.10",
              "Setup at recursion nodes, per-record and per-line descriptors, and the compact exceptional streams cost $o(Tp)$ in total because $r$ exceeds every fixed power of $p$ and $K\\to\\infty$.",
              "costs at most $p^{A+C}=o(Tp)$."),
        infer("H7.11",
              "Each of the seven powers is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
              "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})."),
    ],
    page="cost-accounting",
    frm=["transform-layout", "arbitrary-width-interchange", "simultaneous-butterfly-layer", "crt-map",
         "padded-box-tensor-resampling", "phase-twist", "signed-packing-product", "prime-axis-parameters",
         "logarithms-exponentials-floor-and-ceiling", "established-multiplier"],
    salient="The smallest margin below one is $2^{-181}$ and comes from the chunk exchanges, where the saving $1-\\tau=2^{-50}$ is multiplied by $\\epsilon c=2^{-131}$; this is why $\\kappa=2^{-182}$ is half of it.",
)
Z = show(
    "Z",
    "From $n$ one fixes compatible parameters, places the radix-digit polynomial on prime axes, computes the convolution with two source transforms, a pointwise product and an opposite-sign transform, recovers exact integer coefficients and carries, and totals the cost.",
    "Choose parameters, apply the Chinese-remainder address map, run the resampled transform pipeline, show that the final error is below $1/2$ to round, and add up all costs against the power margins.",
    mot("The tape procedures and transforms have been proved separately, so what remains is to choose compatible parameters, recover the integer coefficients from the approximations and account for the remaining tape operations.",
        "explicit",
        "We choose compatible parameters for these procedures, recover"),
    [H1, H2, H3, H4, H5, H6, H7],
    adds=[
        bind("b", "digit length", "the radix exponent $\\lceil\\log_2n\\rceil$, so digits are in base $2^b$"),
        bind("p", "working precision", "the number $6b$ of fractional bits of every fixed-point coefficient"),
        bind("d", "axis count", "the number $\\lfloor b^{\\epsilon}\\rfloor$ of tensor axes", "count"),
        bind("T", "box size", "the number of complex entries of the padded power-of-two box, a power of two near $n/b$", "count"),
    ],
)

ROOT = show(
    "R",
    "One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Reduce the product to a convolution evaluated by Gaussian-resampling, Bluestein-chirp and synthetic-transform steps, speed up the address movement and the butterfly layers of those transforms with two recursive tape procedures that each save a power of the logarithm, and then fix parameters, recover the integers and add up the cost.",
    mot("Scanning the whole array at each of the $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both movement and arithmetic need savings.",
        "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [T, X, Y, Z],
    page="main-theorem",
    frm=["nlogn-history", "fixed-tape-model", "established-multiplier", "big-o", "turing-machine",
         "worst-case-running-time-and-subroutines", "schoolbook-integer-arithmetic"],
)

# ------------------------------------------------------------------ checks
def walk(n, out):
    out.append(n)
    for c in n.get("children", []) or []:
        walk(c, out)


allnodes = []
walk(ROOT, allnodes)
last = 0
for n in allnodes:
    if n["intention"] == "infer" and not n.get("deferred"):
        ln = n["quote"]["_ln"]
        if ln is None:
            continue
        if ln < last:
            errors.append("ORDER: %s at line %d after %d" % (n["id"], ln, last))
        last = max(last, ln)


def clean(n):
    if isinstance(n, dict):
        return {k: clean(v) for k, v in n.items() if not k.startswith("_")}
    if isinstance(n, list):
        return [clean(x) for x in n]
    return n


ids = [n["id"] for n in allnodes]
if len(ids) != len(set(ids)):
    errors.append("duplicate ids")
pages = [n.get("page") for n in allnodes if n.get("page")]
if len(pages) != len(set(pages)):
    errors.append("duplicate page")

if errors:
    print("\n".join(errors))
    sys.exit(1)

# positions
for n in allnodes:
    if n["intention"] == "infer":
        print(n["id"], n["quote"]["_ln"], "(deferred)" if n.get("deferred") else "")

json.dump({"root": clean(ROOT)}, open(OUT, "w"), indent=1, ensure_ascii=False)
print("ok", len(allnodes), "nodes; pages", len(pages))
