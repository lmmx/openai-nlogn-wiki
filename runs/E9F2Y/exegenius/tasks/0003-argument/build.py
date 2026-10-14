import json, re, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E9F2Y/sources/paper.tex', encoding='utf-8').read()


def Q(t):
    return {"source": "paper", "quote": t}


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def infer(id, claim, quote, page=None, frm=(), deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "from": list(frm)}
    if page:
        n["page"] = page
    if deferred:
        n["deferred"] = True
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, mot, src, children, page=None, frm=(), salient=None, adds=None, mquote=None):
    m = {"text": mot, "source": src}
    if mquote:
        m["quote"] = Q(mquote)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": list(frm)}
    if page:
        n["page"] = page
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = adds
    return n


# ---------------------------------------------------------------- S1 chunk swap
S1_1 = show(
    "S1.1",
    "Arrays with a product address set are stored in lexicographic order with implicit addresses, and fixed digit permutations, digit moves, pointwise maps and cyclic row splits on a volume-$V$ array cost $O(V)$ steps.",
    "Split the array into streams by the specified digit values, so that each stream is a subarray with the same remaining address set in the same order, then apply the fixed map to aligned streams and merge.",
    "A split on a complete digit range leaves every stream in the same order with the same shape, so a fixed number of linear scans suffices.",
    "recoverable",
    [
        infer("S1.1.1", "An array on $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order with the first coordinate most significant, so an entry's address is implicit in its position.",
              r"An address is implicit in an entry's position in this ordered stream; it",
              frm=["lexicographic-order-and-index-tuples"]),
        infer("S1.1.2", "Fixed permutations of two digit values, digit moves, splitting on a digit with a pointwise map, and cyclic splitting of whole rows into a fixed number $W$ of streams each take $O(V)$ steps on a fixed number of tapes.",
              r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
              frm=["multitape-machine-cost-model-and-linear-time-scans"]),
        infer("S1.1.3", "Splitting into $q^2$ (or $q$) streams by the relevant digits and enumerating output addresses in order realises the permutation, since the order of the remaining digits is unchanged.",
              r"For the first operation split into $q^2$ streams according to the two"),
        infer("S1.1.4", "Writing a row number as $r=Wg+w$ and sending the whole row to stream $w$ gives $W$ streams of equal shape, each of volume $V/W$.",
              r"$0\le w<W$, and send the whole row to stream $w$.  If $W$ divides $R$,",
              salient="Each role stream has exactly $1/W$ of the parent's volume, which is the volume factor used in every later recurrence."),
    ],
    page="stream-arrays",
    frm=["fixed-tape-model", "turing-machine-tapes"],
)

S1_2 = show(
    "S1.2",
    "A target field that follows its control fields can be shifted by an offset computed from the controls modulo $Q=q^b$, or multiplied by a fixed rational unit, in $O(V)$ steps.",
    "Cut each fiber of $Q$ blocks at the offset and merge the two pieces in the opposite order (a cyclic shift); for multiplication by an integer $c$ prime to $q$, split into the $c$ increasing pieces of $y\\mapsto cy$ and merge them by residue.",
    "A cyclic shift is a swap of two consecutive pieces, which a split and a merge do in one pass, and the offset arithmetic is polynomial in $b$, hence negligible next to the $Q$ blocks of a fiber.",
    "recoverable",
    [
        infer("S1.2.1", "Splitting each fiber at $Q-a$ and merging the second piece before the first realises $y\\mapsto y+a \\pmod Q$.",
              r"For an offset $a\in[Q]$, split these blocks at $Q-a$.  Append the two",
              frm=["modular-arithmetic-and-residues"]),
        infer("S1.2.2", "The offset work of $b^{O(1)}$ steps is absorbed by the $QB\\ge Q$ bits of the fiber because $b^C=O(q^b)$.",
              r"for each fixed $C$, this work is absorbed by the $QB\ge Q$ bits of the"),
        infer("S1.2.3", "Multiplication by an integer $c$ coprime to $q$ splits $y\\mapsto cy \\pmod Q$ into $c$ increasing pieces, and the unique piece $j$ with $y'+jQ\\equiv0 \\pmod c$ supplies each output coordinate $y'$.",
              r"The required stream is the unique $j\in[c]$ for which",
              frm=["primes-divisibility-gcd-and-coprimality"]),
    ],
    page="controlled-shifts",
    frm=["stream-arrays"],
)

# ---- bank exchange network with the triple gadget
S1_3_gadget = show(
    "S1.3.1",
    "For arbitrary initial scratch values, a forward invocation of the eight-row schedule changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, because gather, scatter and side injection give coefficients depending on $|S\\cap T|$ and the side wires cancel the unwanted ones.",
    "Compute the net target change as $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independent of the scratch values, then check its coefficient from $x_T$ to $y_S$ case by case in the intersection size $|S\\cap T|$.",
    "The schedule first subtracts what the old scratch values contribute and finally restores them, so only a scratch-free linear map remains, whose entries depend only on $|S\\cap T|$ and can be tabulated.",
    "explicit",
    [
        infer("S1.3.1.1", "The scratch-cancelling schedule leaves the net target change $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$ for side injection $\\mathcal J$, copy $\\mathcal V$, scatter $\\mathcal R$ and gather $\\mathcal G$, independent of the initial scratch contents.",
              r"$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of"),
        infer("S1.3.1.2", "Over $\\mathbb F_2$ the central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod2$, which is nonzero only for the self pair (intersection three) and for intersection one; the side injection over neighbours with $|S\\cap T|=1$ cancels exactly the intersection-one cases, while intersection zero or two already give zero.",
              r"In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
        infer("S1.3.1.3", "Over $\\mathbb Z[i,1/2]$ the central coefficient is $(|S\\cap T|-1)/2$, equal to $-1/2$ at intersection zero, $0$ at intersection one, $+1/2$ at intersection two and $1$ for the self pair; the side injection $-\\sum (|S\\cap T|-1)/2\\,A_{ST}$ over neighbours (distinct triples with even intersection) cancels the intersection-zero and two cases.",
              r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$."),
    ],
    page="triple-gadget",
    mquote=r"the following schedule remove the effect of the old scratch values;",
    salient="The coefficients produced by gather and scatter vary with the intersection size, yet the net map is exactly the identity-plus-shear $y\\gets y+x$: every unwanted coefficient lies on a neighbour pair and is removed by a side wire.",
)

S1_3 = show(
    "S1.3",
    "A fixed network of linear gates with three stages sends $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ on two banks indexed by $a\\in\\mathcal T^3$ and restores every scratch wire whatever its initial contents, using $W_{\\rm b}$ and $W_{\\rm c}$ wires in the bit and complex constructions.",
    "Compose three invocations of the forward gadget that adds $x_S$ to $y_S$ (forward $X\\to Y$, inverse $Y\\to X$, forward $X\\to Y$), since the shears $(x,y)\\to(x,y+x)\\to(-y,y+x)\\to(-y,x)$ compose to a signed swap.",
    "A swap with one sign change is a product of three elementary shears, and the gadget supplies exactly one shear that tolerates arbitrary scratch values.",
    "recoverable",
    [
        infer("S1.3.0", "Fix $h=100$, $v=\\binom h3=161700$, $N=v^3$ bank entries and $m=h^3=10^6$, with banks $X_a,Y_a$ indexed by $a\\in\\mathcal T^3$ for $\\mathcal T$ the three-element subsets of $[h]$.",
              r"N=v^3=4227952113000000,\qquad m=h^3=1000000."),
        S1_3_gadget,
        infer("S1.3.2", "A forward invocation at stage 1, the inverse schedule from $Y$ to $X$ at stage 2 and a forward invocation at stage 3 send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, restoring each invocation's own scratch wires.",
              r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
              salient="Scratch wires with arbitrary contents are restored by the gadget's own subtract-then-add schedule, so the exchange needs no initialised workspace."),
        infer("S1.3.3", "There are $I=3v^2=78440670000$ invocations and the networks have $W_{\\rm b}=177176569091445000000$ and $W_{\\rm c}=1873807244643542670000$ wires, all fixed independently of the input length.",
              r"W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})"),
    ],
    page="bank-exchange-network",
    frm=["triple-gadget", "bitwise-xor"],
    adds=[
        B("h", "ground-set size", "The size $100$ of the set whose three-element subsets index the banks.", "count"),
        B("v", "triple count", "The number $\\binom h3=161700$ of three-element subsets of $[h]$.", "count"),
        B("N", "bank size", "The number $v^3$ of entries in each of the two banks.", "count"),
        B("I", "invocation count", "The number $3v^2$ of gadget invocations in the three stages.", "count"),
    ],
)

S1_4 = show(
    "S1.4",
    "Giving each wire at each network vertex an invertible operator $D_v$ (a frame) on its address-indexed array makes every pointwise linear gate commute with the common frame, so the whole network implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$ and only edge changes $D_vD_u^{-1}$ cost anything.",
    "Maintain the invariant that the stored array equals $D_v$ applied to the logical array, check it on edges and at gates by linearity, and read off the endpoint operator on each route.",
    "The sources state that once the routing of the scalar network is fixed, the endpoint frames fix the array operator on each route, so the freedom left is to choose cheap intermediate frames.",
    "explicit",
    [
        infer("S1.4.1", "At a gate with common frame $D_v$, $R$-linearity gives $\\sum_j c_jD_v\\varphi_j=D_v(\\sum_jc_j\\varphi_j)$, so the common frame commutes with the pointwise gate and the invariant continues.",
              r"$c_j\in R$.  Thus the common frame commutes with the pointwise gate, and"),
        infer("S1.4.2", "The implemented operator on the vector of wire arrays is $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so intermediate frames cancel.",
              r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}."),
        infer("S1.4.3", "For a signed role permutation sending input role $w$ to output role $\\rho(w)$ with sign $\\varepsilon_w$, the route applies $\\varepsilon_wD_{{\\rm sink}(\\rho(w))}D_{{\\rm source}(w)}^{-1}$ to its array, for auxiliary roles as well.",
              r"In particular, if the scalar network is a signed role permutation that"),
    ],
    page="frames",
    frm=["bank-exchange-network", "stream-arrays", "matrices-invertibility-and-rank"],
    mquote=r"intermediate frames can then be chosen to make each edge change inexpensive.",
    salient="Frames at interior vertices cancel completely: the array operator on a route depends only on the frames at its source and sink.",
)

# ---- subspace labels : the rank saving
rows = [
    ("S1.5.5.1", "Data wire $X$, edge in$\\to2$: residual $B\\otimes t_X^\\perp$ of dimension $(a-1)(h-1)$ with $a=h^{j-1}$.",
     r"X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)"),
    ("S1.5.5.2", "Data wire $X$, edge $2\\to3$: residual $P\\otimes t_X^\\perp$ of dimension $h-1$.",
     r"X:\ 2\to3&P\otimes t_X^\perp&h-1"),
    ("S1.5.5.3", "Data wire $X$, edges $3\\to6$ and $6\\to7$: residual $0$, dimension $0$.",
     r"X:\ 3\to6,\ 6\to7&0&0"),
    ("S1.5.5.4", "Data wire $Y$, edge in$\\to0$: residual $0$, dimension $0$.",
     r"Y:\ \mathrm{in}\to0&0&0"),
    ("S1.5.5.5", "Data wire $Y$, edge $0\\to1$: residual $B\\otimes t_Y^\\perp$ of dimension $(a-1)(h-1)$.",
     r"Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)"),
    ("S1.5.5.6", "Data wire $Y$, edge $1\\to4$: residual $0$, dimension $0$.",
     r"Y:\ 1\to4&0&0"),
    ("S1.5.5.7", "Data wire $Y$, edge $4\\to5$: residual $P\\otimes t_Y^\\perp$ of dimension $h-1$.",
     r"Y:\ 4\to5&P\otimes t_Y^\perp&h-1"),
    ("S1.5.5.8", "Central wire, source$\\to1$: residual $B\\otimes F$ of dimension $(a-1)h$.",
     r"\mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h"),
    ("S1.5.5.9", "Central wire, edge $1\\to3$: residual $P\\otimes F$ of dimension $h$.",
     r"\mathrm{center}:\ 1\to3&P\otimes F&h"),
    ("S1.5.5.10", "Central wire, edge $3\\to4$: residual $P\\otimes F$ of dimension $h$, the only edge on which the label dimension decreases.",
     r"\mathrm{center}:\ 3\to4&P\otimes F&h"),
    ("S1.5.5.11", "Central wire, edge $4\\to6$: residual $P\\otimes F$ of dimension $h$.",
     r"\mathrm{center}:\ 4\to6&P\otimes F&h"),
    ("S1.5.5.12", "Side wire, source$\\to0$: residual $B\\otimes\\langle t_Y\\rangle$ of dimension $a-1$.",
     r"\mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1"),
    ("S1.5.5.13", "Side wire, edge $0\\to2$: residual $(B\\otimes t_Y^\\perp)\\perp(P\\otimes\\langle t_X\\rangle)$ of dimension $(a-1)(h-1)+1$.",
     r"\mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle)"),
    ("S1.5.5.14", "Side wire, edge $2\\to5$: residual $P\\otimes\\langle t_X,t_Y\\rangle^\\perp$ of dimension $h-2$, possible because $t_X\\perp t_Y$ for neighbouring triples.",
     r"\mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2"),
    ("S1.5.5.15", "Side wire, edge $5\\to7$: residual $P\\otimes\\langle t_Y\\rangle$ of dimension $1$.",
     r"\mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1"),
    ("S1.5.5.16", "Scratch wire, last gate$\\to$sink: residual $(A\\otimes F)\\otimes Q^\\perp$ of dimension $ah(f-1)$ with $f=h^{3-j}$.",
     r"\mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink}"),
]

S1_5_5 = show(
    "S1.5.5",
    "Every edge joins comparable nondegenerate labels, the orthogonal residual of each edge type is as tabulated, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, so $L=Ich$.",
    "Tabulate the orthogonal residual and its dimension for every edge type by splitting $A=B\\perp P$ and $F=\\langle t\\rangle\\perp t^\\perp$, then read off which dimensions drop.",
    "The decomposition of each label into a common summand and a small remaining summand makes every inclusion explicit, so the residual and its dimension are computed edge by edge.",
    "recoverable",
    [
        infer("S1.5.5.19", "Over $\\mathbb F_2$ every nonzero orthogonal residual is nondegenerate and nonalternating, so it has an orthonormal basis.",
              r"For the binary label space, every nonzero orthogonal residual of an"),
    ] + [infer(i, c, q) for (i, c, q) in rows] + [
        infer("S1.5.5.17", "Label dimension is nondecreasing along every edge except the central $3\\to4$ edge, which removes $P\\otimes F\\otimes Q$; the edges at the stage boundaries and the terminals match the prescribed labels.",
              r"Label dimension is nondecreasing along every edge except center $3\to4$, which removes"),
        infer("S1.5.5.18", "The signed dimension changes telescope at every gate to $Wm-2N$, and the $Ic$ decreasing edges of loss $h$ make the absolute changes sum to $Wm-2N+2L$ with $L=Ich$.",
              r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
    ],
)

S1_5 = show(
    "S1.5",
    "Attaching to each gate and terminal a nondegenerate subspace of the $m$-dimensional space $\\mathcal F=F^{\\otimes3}$, nested along every edge, makes an edge cost its dimension change in smaller operations, and the total number of smaller operations satisfies $s<Wm$ in both constructions ($s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$, $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}$, with $L<N/2$).",
    "Choose labels so that all dimension loss is confined to one return edge per central wire, then count by telescoping: the signed changes sum to $Wm-2N$, decreasing edges add $2L$ with $L=Ich$, and the bit interface adds $N$ more ranks from the negative source projections.",
    "A change of frame costs one smaller call per unit of rank, so the total cost is the sum of edge ranks, which stays below $Wm$ exactly when little dimension is lost on decreasing edges.",
    "explicit",
    [
        infer("S1.5.1", "Over $F=\\mathbb Q^h$ with form $x^{\\mathsf T}(I-J/9)y$ the indicator vectors satisfy $\\langle t_S,t_T\\rangle=|S\\cap T|-1$ and $\\langle t_T,t_T\\rangle=2$, so neighbouring triple lines are orthogonal and every triple line is nondegenerate (over $\\mathbb F_2$ with the dot product $t_T\\cdot t_T=1$).",
              r"Thus every triple line is nondegenerate, and neighboring triple lines",
              frm=["bilinear-orthogonal", "vector-spaces-basis-and-dimension"]),
        infer("S1.5.2", "The prescribed terminal labels are $U_a$ at the source and $\\mathcal F$ at the sink of $X_a$, $0$ and $U_a^\\perp$ for $Y_a$, and $0$ and $\\mathcal F$ for each scratch role, so the source dimensions sum to $N$ and the sink dimensions to $Wm-N$.",
              r"The source dimensions sum to $N$ and the sink dimensions to $Wm-N$."),
        infer("S1.5.3", "Signed dimension changes sum to $Wm-2N$ because contributions cancel at gates, and if decreasing edges lose $L$ in total the absolute changes sum to $Wm-2N+2L$.",
              r"Thus the signed dimension changes will sum to $Wm-2N$, because the"),
        infer("S1.5.4", "At stage $j$ the labels are $A\\otimes\\langle t\\rangle\\otimes Q$ and $B\\otimes\\langle t\\rangle\\otimes Q$ on entry, with $A=F^{\\otimes(j-1)}$, $P$ the span of the earlier tensor vector and $B=P^\\perp$, expanding to $(A\\otimes F)\\otimes Q$ and $(P\\otimes\\langle t\\rangle)^\\perp\\otimes Q$ on exit, which are exactly the next stage's entry labels.",
              r"These transitions expose one tensor factor at each stage. To see that"),
        S1_5_5,
        infer("S1.5.6", "The loss ratios are exactly $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both below $1/2$.",
              r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad"),
        infer("S1.5.7", "The bit network therefore has $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$, a deficit of $N-2L_{\\rm b}>0$.",
              r"=W_{\rm b}m-N+2L_{\rm b}"),
        infer("S1.5.8", "In the bit network the projections $P_V-P_U$ have rank $\\dim V-\\dim U$, the $N$ negative source projections $-P_{U_a}$ add one extra rank each (the first edge matrix is $2P_{U_a}$), and the endpoint difference is $P_{U_a^\\perp}+P_{U_a}=I_m$ on every role.",
              r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,",
              frm=["matrices-invertibility-and-rank", "permutations-and-permutation-matrices"]),
        infer("S1.5.9", "In the complex network each edge is a product of one translation kernel per vector of an orthonormal residual basis, giving $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$, a deficit of $2N-2L_{\\rm c}>0$.",
              r"s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}"),
        show(
            "S1.5.10",
            "The relative deficits $\\eta_{\\rm b}=339/22587335000000$ and $\\eta_{\\rm c}=73/19906842167500$ exceed $20\\cdot2^{-50}$, so with $\\tau=\\sigma=1-2^{-50}$ one has $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$.",
            "Bound $m^{1-2^{-50}}=m\\exp(-2^{-50}\\log m)$ from below using $m<2^{20}$, then compare with $1-\\eta$.",
            "The recurrences need a rational exponent strictly between $\\log_m(s/W)$ and $1$, and the tiny relative deficit forces the exponent to be extremely close to $1$.",
            "reconstructed",
            [
                infer("S1.5.10.1", "Both exact deficits exceed $20\\cdot2^{-50}$.",
                      r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$."),
                infer("S1.5.10.2", "Since $m<2^{20}$ and $\\log2<1$ we have $\\log m<20$, hence $m^{1-2^{-50}}=m\\exp(-2^{-50}\\log m)>m(1-20\\cdot2^{-50})>m(1-\\eta)$.",
                      r">m(1-20\cdot2^{-50})>m(1-\eta)"),
                infer("S1.5.10.3", "Consequently $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ with $0<\\tau=\\sigma<1$.",
                      r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
            ],
            salient="The exponent $\\tau=1-2^{-50}$ is astronomically close to $1$, because the rank saving per level is only a relative $\\eta\\approx10^{-11}$ of $Wm$, yet it is strictly below $1$.",
        ),
    ],
    page="subspace-labels",
    frm=["bilinear-orthogonal", "frames", "bank-exchange-network", "triple-gadget"],
    mquote=r"The saving will come from keeping the total dimension lost on decreasing",
    salient="The total number of smaller calls is strictly below $Wm$, though only by a tiny relative amount: the signed dimension changes telescope to $Wm-2N$ at the gates, and the decreasing edges (the central $3\\to4$ returns) lose a total $L<N/2$.",
    adds=[
        B("L", "dimension loss", "The total dimension lost on all edges whose label dimension decreases."),
        B("F", "label field", "The field $\\mathbb Q$ or $\\mathbb F_2$ whose $h$-fold power carries the triple indicator vectors."),
        B("\\mathcal F", "label space", "The $m$-dimensional tensor-cube space $F^{\\otimes3}$ whose subspaces label the vertices."),
    ],
)

S1_6 = show(
    "S1.6",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
    "Eliminate pivot by pivot: take the topmost nonzero row and its rightmost nonzero entry, clear to its left by lower-triangular column operations and below it by lower-triangular row operations, then repeat on the remaining active indices.",
    "Tape updates can only use earlier fields to change later ones, so the changes of coordinates must be lower triangular, which a Bruhat-type factorization with reversed coordinate order delivers.",
    "explicit",
    [
        infer("S1.6.1", "Choose the topmost nonzero row and its rightmost nonzero entry as the pivot; right multiplication by lower-triangular elementary matrices clears entries to its left, and left multiplication clears entries below it.",
              r"If $A=0$, take $E_1=E_2=I$ and $\Pi=0$.  Otherwise choose the topmost"),
        infer("S1.6.2", "Deleting the pivot row and column and repeating keeps all operations lower triangular in the original order and leaves earlier pivots untouched.",
              r"Delete the pivot row and column from the active index sets, retaining"),
        infer("S1.6.3", "Each step isolates a rank-one block, so the final partial permutation matrix has exactly $a$ ones, and $E_1=L^{-1}$, $E_2=R^{-1}$ for $LAR=\\Pi$.",
              r"permutation matrix has exactly $a$ ones.  If $LAR=\Pi$ is the resulting"),
    ],
    page="triangular-factorization",
    frm=["matrices-invertibility-and-rank", "rational-numbers-dyadic-rationals-and-exact-arithmetic"],
    mquote=r"can be performed entirely in this direction. The required factorization",
)

S1_7 = show(
    "S1.7",
    "For a fixed finite set of rational matrices there is a fixed odd prime $q$ such that the address update $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ is performed with exactly $\\operatorname{rank}(A)$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
    "Factor $A=E_1\\Pi E_2$, apply the triangular factors by controlled shifts, and implement each of the $a$ ones of $\\Pi$ by a single interchange sandwiched between two controlled shifts.",
    "After conjugating by the triangular factors only the partial permutation remains, and each one of it is an elementary addition $H_i\\leftarrow H_i+D_j$ that needs one interchange, so the number of recursive calls equals the rank.",
    "recoverable",
    [
        infer("S1.7.1", "A fixed odd prime $q$ avoiding all denominators and diagonal numerators in the finite factor table keeps the factors invertible modulo $q^b$.",
              r"Include their factors and inverses in",
              frm=["primes-divisibility-gcd-and-coprimality"]),
        infer("S1.7.2", "A lower triangular transformation of $H$ or $D$ costs $O(V)$, by updating coordinates in descending physical order with controlled shifts.",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
        infer("S1.7.3", "To apply $A=E_1\\Pi E_2$: transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
              r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
        infer("S1.7.4", "Each one at position $(i,j)$ of $\\Pi$ is done by $D_j\\leftarrow D_j+H_i$, then interchanging $H_i,D_j$, then $D_j\\leftarrow H_i-D_j$, which sends $(h,d)$ to $(h+d,d)$ using exactly one interchange; there are $a$ ones.",
              r"It uses just one interchange.  There are $a$ ones, which proves the",
              salient="The number of recursive calls is exactly the rational rank $a$, not the matrix size $m$."),
    ],
    page="matrix-shear",
    frm=["triangular-factorization", "controlled-shifts"],
)

S1_8_rec = show(
    "S1.8.5",
    "If $F_k$ bounds time divided by logical volume for width $e=m^k$, then $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
    "Count the child calls and their volumes: each of the $s$ calls acts on one role stream of volume $V/W$, while splitting, merging, gates and triangular operations are fixed in number and cost $O(V)$ at the node.",
    "Dividing the cost $s\\cdot(V/W)F_{k-1}$ of the children by the current volume $V$ turns the call count into the factor $s/W$ on the previous level.",
    "recoverable",
    [
        infer("S1.8.5.1", "The number of recursive calls is the sum of the edge ranks, exactly $s$, each on a role stream of volume $V/W$.",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S1.8.5.2", "Splitting, merging, gates and triangular operations are fixed in number and cost $O(V)$ at the node.",
              r"merging, gates, and triangular operations have total cost $O(V)$ because"),
        infer("S1.8.5.4", "The recurrence is $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
              r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
    ],
)

S1_8_sol = show(
    "S1.8.6",
    "Since $s/W<m^\\tau$, the recurrence solves to $F_k=O(e^\\tau)$, that is, $O(Ve^\\tau)$ time.",
    "Unroll to $F_k\\le C\\sum_{j=0}^{k}a^j$ with $a=s/W$ and bound the geometric sum separately for $a\\le1$ and $a>1$.",
    "Each level multiplies the width by $m$ but the cost per volume only by $a<m^\\tau$, so the unrolled sum grows like a power $m^{k\\tau}=e^\\tau$ of the width.",
    "reconstructed",
    [
        infer("S1.8.6.1", "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^ka^j$ is $O(m^{k\\tau})$.",
              r"For $a=s/W<m^\tau$ the geometric sum"),
        infer("S1.8.6.2", "If $a\\le1$ the sum is at most $k+1=O(m^{k\\tau})$; if $a>1$ it is $O(a^k)=O(m^{k\\tau})$.",
              r"most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$."),
        infer("S1.8.6.3", "Hence $F_k=O(e^\\tau)$ since $m^{k\\tau}=e^\\tau$.",
              r"Hence $F_k=O(e^\tau)$."),
    ],
)

S1_8_sched = show(
    "S1.8.7",
    "Scheduling the $s$ recursive calls on a fixed number of tapes costs only $O(V)$ extra at each node, so the factor $s/W$ is not inflated by temporary storage.",
    "Use a depth-first schedule with $W$ role tapes, one parking stack and one descriptor stack: park the inactive streams, copy the active stream to the child, and restore on return, with all cleanup limited to the region visited by the current call.",
    "A recurrence in logical volume is only valid if moving data between tapes is charged to the parent's own volume and never rescans parked ancestors.",
    "reconstructed",
    [
        infer("S1.8.7.1", "Each push, pop, copy, positioning operation or erasure moves $O(V)$ symbols at a parent node, and there are only the fixed number $s$ of child calls, so temporary storage is not substituted for logical volume in the factor $s/W$.",
              r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
        infer("S1.8.7.2", "Descriptor processing is polynomial in $\\log V_0$, hence $O(V_j)$ at depth $j$, because both original chunk ranges remain present in every child and $V_j\\ge q^{2e_0}$.",
              r"V_j\ge q^{2e_0},\qquad"),
    ],
)

S1_8 = show(
    "S1.8",
    "For $e=m^k$ and a row field of length divisible by $W^k$, two disjoint chunks of $e$ radix-$q$ digits can be interchanged in $O(Ve^\\tau)$ time for any rational $\\tau\\in(0,1)$ with $s/W<m^\\tau$.",
    "Realise the interchange as the middle shear $H\\leftarrow H+D$ of $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$; run the bit bank-exchange network on $W$ role streams of volume $V/W$ with address-shear frames, each edge being rank-many interchanges of chunks of $e/m$ digits; then solve the recurrence.",
    "The frame identity turns each edge change into a shear whose cost is its rank, so one call at width $e$ is $s$ calls at width $e/m$ on streams $W$ times smaller, which the sum $s<Wm$ makes cheaper than the naive $m$ calls.",
    "explicit",
    [
        infer("S1.8.1", "Splitting whole rows cyclically into $W$ role streams gives $W$ streams of the same remaining shape, each of volume $V/W$ with row count divisible by $W^{k-1}$.",
              r"Split whole rows cyclically into $W$ role streams within each prefix"),
        infer("S1.8.2", "With frame $\\Phi_M$ moving the entry at $(H,D)$ to $(H+MD,D)$ at each vertex of matrix $M$, each edge changes the frame by $\\Phi_{A_e}$, implemented by $\\operatorname{rank}A_e$ recursive interchanges, and each circuit gate runs pointwise on matching addresses.",
              r"For a rational matrix $M$, let $\Phi_M$ act on an array by moving its"),
        infer("S1.8.3", "By the common-frame identity and the condition $M_{{\\rm out}(\\rho(w))}-M_{{\\rm in}(w)}=I_m$, every role array, including scratch roles, receives $\\Phi_{I_m}$, i.e. the shear $H\\leftarrow H+D$, after merging rows back.",
              r"=\Phi_{I_m}f_w,"),
        infer("S1.8.4", "The two chunks are interchanged by $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, where only the middle shear uses the circuit and the others have linear cost.",
              r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
        S1_8_rec,
        S1_8_sol,
        S1_8_sched,
        infer("S1.8.8", "The exponent $\\tau=1-2^{-50}$ established for the bit network is used, verified by fixed integer comparisons and the displayed exponential inequality.",
              r"We use the rational value $\tau=1-2^{-50}$ established in"),
    ],
    page="power-width-interchange",
    frm=["matrix-shear", "subspace-labels", "bank-exchange-network", "frames", "stream-arrays",
         "geometric-series-and-orthogonality-of-sums-of-roots-of-unity"],
    mquote=r"Because the sum of these ranks is less than the number of wires times",
    salient="The cost per volume grows as $e^\\tau$ with $\\tau=1-2^{-50}<1$ although the recursion branches into $s\\approx Wm$ calls, because each of the $s$ calls works on a stream $W$ times smaller and the ratio $s/W$ stays just below $m$.",
    adds=[
        B("e", "chunk width", "The number $m^k$ of radix-$q$ digits in each of the two chunks being interchanged.", "count"),
        B("k", "recursion depth", "The number of levels of recursion, with $e=m^k$.", "count"),
        B("F_k", "normalised cost", "A uniform bound on running time divided by logical volume for chunks of width $m^k$."),
    ],
)

S1_9 = show(
    "S1.9",
    "Two address chunks of arbitrary width $u$ in an arbitrary bit array, with the shape given as input, can be interchanged in $O(Vu^\\tau)$ steps by reducing to power widths with enough rows.",
    "Interchange $\\rho=O(\\log u)$ high digit pairs one by one so they form a row field, pad the rows to a multiple of $W^k$, split the remaining width in base $m$ into power-width pieces, and pad binary chunks up to radix-$q$ ranges.",
    "The power-width procedure needs a row field divisible by $W^k$ and a width $m^k$, and a few of the array's own high digits can supply the rows at a cost far below the final bound.",
    "explicit",
    [
        infer("S1.9.1", "Write each chunk as its top $\\rho$ digits followed by its remaining digits, interchange the high digits one pair at a time, and move them next to each other so they form a row field of range $R=q^{2\\rho}\\ge W^k$ with $\\rho=\\lceil k\\log W/(2\\log q)\\rceil=O(\\log e)$.",
              r"Write each chunk as its top $\rho$ digits followed by its remaining"),
        infer("S1.9.2", "Appending zero rows within each prefix to reach $R'=W^k\\lceil R/W^k\\rceil<2R$ rows at most doubles the volume.",
              r"R'=W^k\left\lceil R/W^k\right\rceil<2R."),
        infer("S1.9.3", "Writing the remaining width as $e-\\rho=\\sum_ja_jm^j$ with $0\\le a_j<m$ and applying the power-width interchange to $a_j$ pieces of width $m^j$ costs $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^\\tau)$.",
              r"e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m."),
        infer("S1.9.4", "Padding rows are untouched by completed calls, then scanned away and the high-part moves reversed, at extra cost $O(V\\log(2e))=O(Ve^\\tau)$.",
              r"remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$."),
        infer("S1.9.5", "For binary chunks pad each range from $[2^u]$ to $[q^e]$ with $e$ least such that $q^e\\ge2^u$, which increases volume by less than the fixed factor $q^2$, giving $O(Vu^\\tau)$.",
              r"Finally, for binary chunks let $e$ be the least integer with"),
        infer("S1.9.6", "Chunks whose widths differ by one bit use one extra single-bit move in addition to an equal-width interchange.",
              r"For widths differing by one bit, choose the leading bit of the longer"),
    ],
    frm=["power-width-interchange", "stream-arrays", "logarithms-floors-ceilings-and-powers-of-two"],
    mquote=r"Rows for a general array can be supplied by a few of its own high digits.",
)

S1 = show(
    "S1",
    "Two disjoint contiguous address chunks of $u$ bits in any bit array of $V$ stored bits can be interchanged in $O(Vu^\\tau)$ steps for the fixed $\\tau=1-2^{-50}<1$, although the intermediate steps form XOR combinations of data.",
    "Obtain the interchange as the net effect of a fixed linear bank-exchange network over $\\mathbb F_2$ whose edges are smaller interchanges: label the gates by nested subspaces so that the total edge rank $s$ is below $Wm$, express each edge as rank-many shears, and solve the resulting recurrence on streams of volume $V/W$.",
    "The sources say that multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$, and this strict inequality is the source of the power saving.",
    "explicit",
    [S1_1, S1_2, S1_3, S1_4, S1_5, S1_6, S1_7, S1_8, S1_9],
    page="chunk-swap",
    frm=["fixed-tape-model", "bank-exchange-network", "frames", "subspace-labels", "matrix-shear", "power-width-interchange"],
    mquote=r"increases the recursive contribution by $s/W<m$. This strict inequality",
    salient="The cost is $O(Vu^{\\tau})$ with $\\tau<1$, a power saving over the width $u$, even though the final effect is an exact permutation and the procedure is built from XORs.",
    adds=[
        B("u", "chunk width", "The number of bits in each of the two address chunks being interchanged.", "count"),
    ],
)

# ---------------------------------------------------------------- S2 simultaneous butterfly layer
S2_1 = show(
    "S2.1",
    "The two-point kernel $C=H\\mathsf SH=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$ satisfies $H_0=b\\mathsf SC\\mathsf S$, and the complex bank-exchange network with binary labels makes $C^{\\otimes m}$ on every role, each edge being a product of translation kernels $aI+bX_v$ (or inverses), one per vector of an orthonormal basis of its residual.",
    "Diagonalise all phase frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{q_U(x)})H^{\\otimes m}$ by one Hadamard matrix, express $q_V-q_U$ as a sum over an orthonormal residual basis by additivity of Hamming weight on orthogonal vectors, and change the residual basis by an invertible binary matrix.",
    "The phase identities express an edge's residual operator as a product of two-point kernels on selected directions, so one recursive call per residual basis vector suffices.",
    "explicit",
    [
        infer("S2.1.1", "For binary $z,w$ with $z\\cdot w=0$ the intersection of supports is even, so Hamming weight is additive modulo four, hence $q_V-q_U=\\sum_{v}\\operatorname{wt}(v)[v\\cdot x]\\pmod 4$ over an orthonormal basis of the residual.",
              r"For binary vectors $z,w$,",
              deferred=True, frm=["bitwise-xor", "vector-spaces-basis-and-dimension"]),
        infer("S2.1.2", "Each basis vector has odd weight, so its phase factor $i^{\\varepsilon[v\\cdot x]}=\\frac{1+i^\\varepsilon}2+\\frac{1-i^\\varepsilon}2(-1)^{v\\cdot x}$ with $\\varepsilon=\\pm1$ becomes the translation kernel $aI+bX_v$ or its inverse after conjugating by Hadamard matrices.",
              r"\frac{1+i^\varepsilon}{2}",
              deferred=True),
        infer("S2.1.3", "After source and sink corrections ($C=iZC^{-1}Z$ on the $27$ coordinates of $\\operatorname{supp}(u_a)$) and undoing the signed exchange, telescoping the phase frames gives $C^{\\otimes mk}$ on every role on $k$ columns.",
              r"The zero label has frame $I$, while the full label has frame",
              deferred=True),
        infer("S2.1.4", "Direct multiplication gives $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=bI+aX=-iZCZ$, all with Gaussian dyadic coefficients.",
              r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
        infer("S2.1.5", "For an invertible binary matrix $M$ with residual basis as first columns, $\\mathcal C_{U_+}\\mathcal C_{U_-}^{-1}=\\mathcal P_M(\\prod_jC_{e_j}^{\\epsilon_j})\\mathcal P_M^{-1}$, because $\\mathcal P_MX_v\\mathcal P_M^{-1}=X_{Mv}$.",
              r"\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}."),
        infer("S2.1.6", "A negative directional kernel needs only one forward child since $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$, so one edge makes one child call on $f$ axes per residual basis vector.",
              r"(C^{-1})^{\otimes f}"),
        infer("S2.1.7", "Over a group of $e=mf$ axes the network gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
              r"$e=mf$ selected axes.  Summing its residual dimensions gives exactly"),
        infer("S2.1.8", "Applying $\\mathsf S=\\operatorname{diag}(1,i)$ on all selected bits gives $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ with $b^D=(-i/2)^{\\lfloor D/2\\rfloor}b^{D\\bmod2}$, a binary shift and fourth-root phase.",
              r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
    ],
    page="phase-kernel-network",
    frm=["frames", "subspace-labels", "butterfly-layers", "complex-numbers", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"],
    mquote=r"identities below express an edge's residual operator as a product of",
    salient="A single two-point kernel $C=aI+bX$ with Gaussian dyadic coefficients generates all the phase frames, and its square is the bit flip $X$ while its fourth power is the identity.",
)

S2_2 = show(
    "S2.2",
    "A binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ on the selected bit $j_i=\\rho+iK$ of each of $f$ chunks at once, with a third chunk $z$ restored, costs $O(V(L^\\tau+1))$ for $L=fK$ under the family bounds, deterministically for every payload.",
    "Perform eight cyclic shifts of whole chunk ranges that act as the XORs away from a small explicit set $\\mathcal B$ of addresses, then repair $\\mathcal B$ by extracting those records, radix-sorting them by destination rank and reinserting them.",
    "The sources first use a constant number of cyclic shifts of whole chunk ranges and then correct an explicitly bounded set of addresses, so that the correction depends only on addresses and the bound holds in the worst case over payloads.",
    "explicit",
    [
        infer("S2.2.8", "The cost is $O(V(L^\\tau+1)+MA_{\\rm rect}^3+\\delta_{\\rm bad}MA_{\\rm rect}(R+A_{\\rm rect}))$, which is $O(V(L^\\tau+1))$ when $A_{\\rm rect}=O(p)$, $R$ exceeds every fixed polynomial in $p$, $f\\le d\\le p$ and $K/\\log p\\to\\infty$.",
              r"When $A_{\rm rect}=O(p)$, $R$ exceeds every fixed polynomial in $p$,"),
        infer("S2.2.1", "The eight operations $u\\leftarrow u\\mp c[w\\equiv0],\\ w\\leftarrow w\\mp c[u\\equiv0],\\dots$ induce, for $c=1$, the cycle $(00\\ 01\\ 10)$ from the first four and $(01\\ 10\\ 11)$ from the last four on every square of parities of $(u,w)$.",
              r"u&\leftarrow&u-c[\,w\equiv0\pmod2\,],&(1)\\"),
        infer("S2.2.2", "Composing the two cycles gives $(00\\ 10)(01\\ 11)$, so the output is $(u',w')=(u+c(1-2(u\\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, the quotients by two are preserved and the auxiliary integer $w$ is restored.",
              r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr)."),
        infer("S2.2.3", "Segments of $K$ bits with guard values $g,h$ (the quotient by two) in $[10,2^{K-1}-11]$ cannot carry or borrow into neighbours even under displacement eight, so the eight packed rotations $S_0$ agree with the ideal XOR map $T_0$ off the bad set $\\mathcal B$.",
              r"Let $\mathcal B$ consist of the addresses for which"),
        infer("S2.2.4", "Each guard has exactly twenty excluded values among $2^{K-1}$, and a union bound over the $2(f-1)$ guards gives $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$, independent of the record values.",
              r"There are exactly twenty excluded values for each guard in",
              salient="The bad fraction is $O(f2^{-K})$ and, because $K/\\log p\\to\\infty$, it is small enough to repair by sorting."),
        infer("S2.2.5", "Both $T_0$ and $S_0$ are bijections that agree off $\\mathcal B$, so $T_0S_0^{-1}$ fixes $\\mathcal B^c$ and permutes $\\mathcal B$.",
              r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
        infer("S2.2.6", "Each rotation is a chunk interchange moving the target after its two controls, a controlled shift in $O(V)$, and the undoing interchange; there are at most sixteen interchanges and eight rotations in $S_0$.",
              r"There are at most sixteen swaps and eight rotations in $S_0$."),
        infer("S2.2.7", "The correction extracts the records at $\\mathcal B$ with destination-rank keys, radix-sorts them, and reinserts them in one scan, implementing $T_0$ everywhere.",
              r"Hold the full stream untouched"),
        infer("S2.2.9", "A fixed number of full record scans costs $O(MA_{\\rm rect}^3+V)$ and the at most $A_{\\rm rect}$ radix passes cost $O(|\\mathcal B|A_{\\rm rect}(R+A_{\\rm rect}))$, with the movement costing $O(V(L^\\tau+1))$.",
              r"The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans"),
        infer("S2.2.10", "A fixed binary change of basis is a fixed number of row additions, each applied to all slots' selected bits together, so the whole change of basis and its inverse cost $O(V((eK)^\\tau+1))$.",
              r"$O(V((eK)^\tau+1))$ on a stream of volume $V$.  Here $e$ counts"),
    ],
    page="packed-selected-bits",
    frm=["chunk-swap", "controlled-shifts", "bitwise-xor"],
    mquote=r"of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of",
)

S2_3 = show(
    "S2.3",
    "With $\\beta=1/2$, rational exponents $\\max\\{\\tau,\\sigma\\}<\\lambda<1$ and $\\tau(1+c/\\beta)<\\lambda$, the normalised layer cost satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ with $F(e)=O(e)$ for $e<d^\\beta$, which solves to $O(d^{\\lambda'})$ for any fixed $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
    "Split $e=m^k$ chunks into $m$ slots of $e/m$ chunks, run the complex network on $W$ role streams of volume $V/W$ (rows coming from the first $q_0$ chunks), stop at $e<d^\\beta$ with individual kernels, and sum internal nodes and leaves of the recursion tree separately, using a base-$m$ partition of the $D-q_0$ remaining chunks.",
    "As for the interchange, one call on $e$ axes is $s$ calls on $e/m$ axes of volume $V/W$, so the ratio $s/W\\le m^\\sigma<m^\\lambda$ makes the node costs a convergent geometric sum, while stopping early bounds the leaves.",
    "recoverable",
    [
        infer("S2.3.1", "One individual $C$ kernel splits at the selected bit, applies $C(u,v)$ with exact fixed-point additions to aligned records and merges, so $e$ individual kernels cost $O(Ve)$.",
              r"Thus \(e\) individual kernels cost"),
        infer("S2.3.2", "At an internal node of $e=m^k$ chunks the binary changes of basis, inverses, scalar gates and reassembly cost $O(V((eK)^\\tau+1))$.",
              r"endpoint corrections and reassembly of the physical banks cost"),
        infer("S2.3.3", "The first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks are handled by individual kernels and serve as the row index of range $R_{\\rm row}=2^{q_0K}\\ge W^{k_0}$ with $k_0=\\lceil\\log_md\\rceil$, after padding zero rows to a multiple of $W^{k_0}$ (volume at most doubles).",
              r"R_{\rm row}=2^{q_0K}\ge W^{k_0}"),
        infer("S2.3.4", "The recurrence is $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, since the $s$ child calls act on streams of volume $V/W$.",
              r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
        infer("S2.3.5", "At an internal node $e\\ge d^\\beta$, so $K\\le d^c\\le e^{c/\\beta}$ and the overhead is $O(e^{\\tau(1+c/\\beta)}+1)=O(e^\\lambda)$.",
              r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)."),
        infer("S2.3.6", "With $a=s/W\\le m^\\sigma<m^\\lambda$ the internal costs sum to at most $Ce^\\lambda\\sum_{j\\ge0}(a/m^\\lambda)^j=O(e^\\lambda)$.",
              r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)."),
        infer("S2.3.7", "The leaves, with $u=e/m^j<d^\\beta$ chunks each after $j$ levels, contribute at most $O(a^ju)\\le O(e^\\sigma u^{1-\\sigma})\\le O(e^\\sigma d^{\\beta(1-\\sigma)})$, using $a^j\\le m^{j\\sigma}=(e/u)^\\sigma$.",
              r"O(a^ju)\le O(e^\sigma u^{1-\sigma})"),
        infer("S2.3.8", "Writing $D-q_0=\\sum_ja_jm^j$ in base $m$ gives at most $(m-1)(1+\\lfloor\\log_md\\rfloor)$ pieces, and summing them with the row preprocessing yields $O(\\log(2d)[d^\\lambda+d^{\\sigma+\\beta(1-\\sigma)}+1])=O(d^{\\lambda'})$.",
              r"Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\).",
              salient="The factor $\\log(2d)$ from the number of base-$m$ pieces is absorbed by taking $\\lambda'$ strictly above $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}$."),
    ],
    frm=["power-width-interchange", "phase-kernel-network", "packed-selected-bits", "geometric-series-and-orthogonality-of-sums-of-roots-of-unity"],
    adds=[
        B("e", "slot-group size", "The number $m^k$ of consecutive active chunks in one recursive call of the layer.", "count"),
        B("\\beta", "stopping exponent", "The fixed exponent $1/2$ such that recursion stops once $e<d^\\beta$."),
        B("\\sigma", "complex recurrence exponent", "A rational upper bound $1-2^{-50}$ for $\\log_m(s_{\\rm c}/W_{\\rm c})$."),
        B("\\lambda", "node exponent", "A fixed exponent in $(\\max\\{\\tau,\\sigma\\},1)$ bounding the per-node cost $O(e^\\lambda)$."),
    ],
)

S2_4 = show(
    "S2.4",
    "All intermediate Gaussian dyadic values of one layer are represented exactly with $p+\\Delta$ fractional bits and $\\Delta+3$ integer and sign bits, where $\\Delta=\\lceil C_0d^{C_1}\\rceil$ with $C_1=20$ and $\\epsilon C_1<1$, so $\\Delta=o(p)$ and the width is $O(p)$.",
    "Bound the arithmetic dependency depth $A(e)$ by a recurrence $A(e)\\le sA(e/m)+E$ with leaf $A(e)\\le8e$, unroll it over at most $\\lceil\\log_md\\rceil$ levels, and note that a value at depth $\\ell$ has denominator $2^{p+\\ell}$ and modulus at most $2^\\ell$.",
    "Every addition at most doubles the modulus and every halving adds one fractional bit, so the number of operations along any chain controls both denominator and magnitude growth.",
    "recoverable",
    [
        infer("S2.4.1", "Put $E=64(W+m+1)^3$, $B=s+E$ and $\\nu=\\min\\{j\\ge1:m^j\\ge B\\}$; for the stated network $\\nu=11$ and $C_1=\\max\\{20,\\nu+3\\}=20$, $C_0=128mB^2$.",
              r"E=64(W+m+1)^3,\qquad B=s+E,"),
        infer("S2.4.2", "The scalar gates and the child, source, sink and bank corrections add fewer than $E$ operations to a chain, since $24W^3+4s+4W+4<E$.",
              r"\(24W^3+4s+4W+4\) is less than"),
        infer("S2.4.3", "The depth satisfies $A(e)\\le sA(e/m)+E$ at an internal node and $A(e)\\le8e$ at a leaf.",
              r"A(e)\le sA(e/m)+E"),
        infer("S2.4.4", "For $x\\ge1$, $sx+E\\le(s+E)x=Bx$, so over $k\\le\\lceil\\log_md\\rceil$ levels $A(e)\\le8dB^{k+1}\\le8B^2d^{\\nu+1}$ using $B^{\\log_md}=d^{\\log_mB}\\le d^\\nu$.",
              r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}."),
        infer("S2.4.5", "Adding the base-$m$ pieces, the individual kernels and the outer phase and shift costs gives a total below $128mB^2d^{\\nu+3}\\le C_0d^{C_1}$.",
              r"<128mB^2d^{\nu+3}\le C_0d^{C_1}."),
        infer("S2.4.6", "A value at depth $\\ell$ lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ and has modulus at most $2^\\ell$, so reserving $p+\\Delta$ fractional bits and $\\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly.",
              r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most"),
        infer("S2.4.7", "Choosing $\\epsilon C_1<1$ with $d=\\Theta(p^\\epsilon)$ gives $\\Delta=o(p)$, so the full coefficient width stays $O(p)$.",
              r"Choose \(\epsilon C_1<1\).  Since \(d=\Theta(p^\epsilon)\),"),
    ],
    frm=["rational-numbers-dyadic-rationals-and-exact-arithmetic", "complex-numbers"],
    adds=[
        B("\\Delta", "guard width", "The number $\\lceil C_0d^{C_1}\\rceil$ of extra fractional and integer bits reserved for exact intermediate values."),
        B("\\epsilon", "axis-count exponent", "The fixed exponent $2^{-75}$ with $d=\\Theta(p^\\epsilon)$."),
    ],
)

S2 = show(
    "S2",
    "A normalised butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied simultaneously to the selected bit $\\rho$ of each of $D\\le d$ address chunks of $K$ bits, on records of $r$ complex coefficients in the unit disk on the grid $2^{-p}\\mathbb Z[i]$, costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$, exactly in Gaussian dyadics followed by one truncation $Q_p$ with error below $\\sqrt2\\,2^{-p}$.",
    "Write $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, compute $C^{\\otimes e}$ by the complex bank-exchange network whose binary basis changes are packed selected-bit additions and whose children act on streams of volume $V/W$, and solve the recurrence for the layer cost.",
    "Separate butterfly factors would require $D$ whole-array passes, whereas the network replaces $e$ axes by $s<Wm$ calls on $e/m$ axes, which gives the power saving $d^{\\lambda'}$ with $\\lambda'<1$.",
    "explicit",
    [S2_1, S2_2, S2_3, S2_4,
     infer("S2.5", "The procedure returns $Q_p(\\mathcal Hz)$ in the same array and format in $O(Vd^{\\lambda'})$ time, with every returned coefficient in the disk and $\\|Q_p(\\mathcal Hz)-\\mathcal Hz\\|_\\infty<\\sqrt2\\,2^{-p}$, because every row of $\\mathcal H$ has absolute row sum one and truncation changes each component by less than $2^{-p}$.",
           r"The procedure returns $Q_p(\mathcal H z)$ in the same array,")],
    page="simultaneous-butterfly-layer",
    frm=["phase-kernel-network", "packed-selected-bits", "fixed-point-disk-grid", "butterfly-layers", "power-width-interchange", "negacyclic-ring"],
    mquote=r"$\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly",
    salient="One layer on $d$ axes costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, not $d$ whole-array passes, and nothing is rounded until the whole layer has been computed exactly.",
)

# ---------------------------------------------------------------- S3 ring convolution
S3_1 = show(
    "S3.1",
    "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with roots $\\omega_t=y^{2r/t}$, the transforms satisfy character cancellation $\\sum_{k=0}^{t-1}\\omega_t^{jk}=t$ if $t\\mid j$ and $0$ otherwise, hence $F_t^+F_t^-=t^{-1}I$, even though the ring has zero divisors.",
    "Pair the summands: write $j=2^vj_0$ with $j_0$ odd and shift $k$ by $t/2^{v+1}$, which permutes the terms and multiplies the sum by $y^{rj_0}=-1$.",
    "The ring has zero divisors, so one cannot divide by $\\omega_t^j-1$; the pairing argument proves cancellation directly.",
    "explicit",
    [
        infer("S3.1.1", "For a power of two $t$ dividing $2r$, $\\omega_t=y^{2r/t}$ and every power of $\\omega_t$ is an isometry, so both normalised transforms are contractions.",
              r"Every power of $\omega_t$ is an isometry, and each transform entry is"),
        infer("S3.1.2", "If $t\\nmid j$, writing $j=2^vj_0$ and replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$.",
              r"Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes"),
        infer("S3.1.3", "Hence the sum is zero since the additive group of $\\mathcal R_r$ has no two-torsion, and expanding the composite transforms gives $F_t^+F_t^-=t^{-1}I$.",
              r"$\mathcal R_r$ has no two-torsion.  Expanding the composite transforms"),
    ],
    page="synthetic-transform",
    frm=["negacyclic-ring", "dft-cyclic-convolution", "multidim-transform", "geometric-series-and-orthogonality-of-sums-of-roots-of-unity"],
    mquote=r"The ring has zero divisors, so we verify character cancellation",
    salient="The orthogonality of characters holds in a ring with zero divisors because shifting the index by a half period multiplies the sum by $-1$, so the sum equals its own negative.",
)

S3_2 = show(
    "S3.2",
    "Decimation in frequency computes $F_t^-$ by applying $H_0$ to pairs $(k,k+t/2)$ and a twiddle monomial $\\omega_t^{-k}$ to the second output and recursing on the halves, leaving frequencies in bit-reversed order, so the procedures $B_tF_t^-$ and $F_t^+B_t^{-1}$ consume each other's order directly.",
    "Split the transform sum by the parity of the frequency, obtaining the two-point butterfly and twiddle, track the branch bits written at each level, and run the recursion in reverse for the opposite transform.",
    "Writing the output where it falls, instead of sorting frequencies back, avoids a full permutation, and the opposite transform is exactly the reversed procedure.",
    "recoverable",
    [
        infer("S3.2.1", "Separating even and odd frequencies gives $(F_t^-z)_{2h+b}=\\frac1{t/2}\\sum_k(\\omega_t^2)^{-hk}\\omega_t^{-bk}\\frac{z_k+(-1)^bz_{k+t/2}}2$.",
              r"(F_t^-z)_{2h+b}"),
        infer("S3.2.2", "After all $a=\\log_2t$ rounds the named slots from high to low contain the frequency bits from low to high, so entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.",
              r"After all $a$ rounds, the named slots from high to low therefore"),
        infer("S3.2.3", "The reversed level is half the inverse of the forward level because $H_0^2=I/2$, so over $a$ levels the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$.",
              r"As $H_0^2=I/2$, the reversed level is half the inverse"),
        infer("S3.2.4", "The two exact procedures therefore implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
              r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
        infer("S3.2.5", "For $D$ axes a round groups the axis butterflies into a parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$ with $E=-\\sum_i\\frac{2r}{u_i}b_ik_i\\pmod{2r}$, since the twiddle of one axis commutes with the butterflies of the others.",
              r"E=-\sum_{i\ \mathrm{participating}}",
              salient="The frequencies are left in bit-reversed order and never sorted: the opposite transform is the reversed recursion and reads that order directly."),
    ],
    page="butterfly-layers",
    frm=["synthetic-transform", "dft-cyclic-convolution", "binary-representation-of-integers"],
)

S3_3 = show(
    "S3.3",
    "A positional layout permutation $L$ puts the selected bits of all axes at a common offset in consecutive $K$-bit chunks, so that each transform round is one simultaneous layer; the forward procedure has exact counterpart $LBF^-_{\\boldsymbol t}$, the opposite $F^+_{\\boldsymbol t}B^{-1}L^{-1}$, each with error below $\\sqrt2\\,\\ell2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "Move the top slots into a prefix (about $dK$ slot moves), interleave the remaining $K$-bit chunks of the axes by at most $Dq-1$ chunk interchanges, run the $qK$ rounds as simultaneous layers and the prefix rounds individually, and truncate once per round.",
    "The simultaneous layer applies only to the same bit offset in equal consecutive chunks, so the data must first be arranged this way, using the fast chunk interchange rather than a full transpose.",
    "explicit",
    [
        infer("S3.3.1", "At most $D(b+1)=O(dK)$ listed slots are moved to a prefix, costing $O(TpdK)$, and the at most $K$ rounds on prefix slots are done individually also at $O(TpdK)$.",
              r"listed slots, so the moves cost $O(TpdK)$."),
        infer("S3.3.2", "Interleaving the $q$ chunks of each of the $D$ axes takes at most $Dq-1$ exchanges of width-$K$ chunks costing $O(Tp\\,DqK^\\tau)=O(Tp\\,pK^{\\tau-1})$, since $Dq=O(p/K)$.",
              r"O\bigl(Tp\,DqK^\tau\bigr)"),
        infer("S3.3.3", "The simultaneous-layer procedure costs $O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ over the at most $\\ell$ rounds.",
              r"$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."),
        infer("S3.3.4", "Truncation toward zero is odd and commutes with the signed coefficient permutation $J_E$, so $J_EQ_p(\\mathcal Hz)=Q_p(J_E\\mathcal Hz)$ and each round truncates once after an exact contraction.",
              r"J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z)."),
        infer("S3.3.5", "A contraction does not increase the error and each truncation adds less than $\\sqrt2\\,2^{-p}$, so at most $\\ell$ rounds give error below $\\sqrt2\\,\\ell2^{-p}$ and keep the disk bound, the layout permutations adding no error.",
              r"give the claimed error and disk bounds.  The layout permutations"),
        infer("S3.3.6", "The full exact operators are $(L\\mathcal D_-L^{-1})L=LBF^-_{\\boldsymbol t}$ and $L^{-1}(L\\mathcal D_+L^{-1})=F^+_{\\boldsymbol t}B^{-1}L^{-1}$, so the forward entry with frequency address $j$ is stored at $L(Bj)$.",
              r"(L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-,"),
    ],
    page="transform-layout",
    frm=["synthetic-transform", "butterfly-layers", "simultaneous-butterfly-layer", "chunk-swap", "permutations-and-permutation-matrices"],
    mquote=r"we must place the selected bits of the participating axes at a common",
)

S3_4 = show(
    "S3.4",
    "Two disk-grid polynomials in $\\mathcal R_r$ can be multiplied exactly (Gaussian-integer numerators of $fg$) and $Q_p(fg/r)$ returned in $O(rp\\log(rp))$ time with four integer products by the established multiplier.",
    "Evaluate the integer-coefficient parts at $B_0=2^{4p}$, multiply the resulting signed integers, and recover the signed coefficients of the product by centred carries, then reduce modulo $y^r+1$.",
    "This is a signed form of Kronecker substitution: because every product coefficient is much smaller than $B_0/2$, its centred residue modulo $B_0$ identifies it uniquely.",
    "explicit",
    [
        infer("S3.4.1", "Setting $B_0=2^{4p}$ and $A_u=u(B_0)=\\sum_ju_jB_0^j$ for $u\\in\\{a,b,c,e\\}$ makes each magnitude fit in $4pr$ bits, and the four products $A_aA_c,A_bA_e,A_aA_e,A_bA_c$ are computed by the established multiplier.",
              r"A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j."),
        infer("S3.4.2", "Every coefficient of an ordinary product satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$.",
              r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
        infer("S3.4.3", "Packing with carries $\\gamma_j\\in\\{-1,0\\}$ gives a fixed-width two's-complement encoding of $A_u$ in $r$ blocks of $4p$ bits.",
              r"Since $-B_0<u_j+\gamma_j<B_0$ whenever"),
        infer("S3.4.4", "Extraction takes at block $j$ the centred residue $\\widehat h_j\\in[-B_0/2,B_0/2)$ of $q_j+\\rho_j$ modulo $B_0$ with carry $\\rho_{j+1}\\in\\{0,1\\}$, and the separation bound gives $\\widehat h_j=h_j$.",
              r"Thus $\widehat h_j=h_j$."),
        infer("S3.4.5", "Reducing the real and imaginary streams $ac-be$ and $ae+bc$ modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$, and each result satisfies $|H_j|\\le r2^{2p}$.",
              r"|H_j|\leq r2^{2p}."),
        infer("S3.4.6", "The grid numerators of $Q_p(fg/r)$ are obtained by shifting magnitudes right by $p+\\ell$ bits, and the four exact integer products dominate the linear packing, extraction and truncation costs.",
              r"Four exact integer products dominate the linear"),
    ],
    page="signed-kronecker-packing",
    frm=["negacyclic-ring", "nlogn-subroutine", "polynomials", "convolution-as-polynomial-multiplication"],
    mquote=r"reduction is a signed form of Kronecker substitution; compare",
)

S3_5 = show(
    "S3.5",
    "The normalised convolution $\\mathcal M_r(f,g)=(f*g)/(rM)=(f*g)/T$ over $\\mathcal R_r$ on the $d-1$ axes is approximated from the retained transform layout with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "Do two forward transforms, multiply the records pointwise in the retained $LB$ order by signed packing, apply the opposite transform to that order, and scale exactly by $M$; control the error by the bilinear contraction property.",
    "Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands, so the permutation never has to be undone before the opposite transform.",
    "explicit",
    [
        infer("S3.5.1", "$\\mathcal M_r$ averages $rM$ signed scalar products per output coefficient, hence is a bilinear contraction: $\\|\\mathcal M_r(f,g)\\|_\\infty\\le\\|f\\|_\\infty\\|g\\|_\\infty$.",
              r"\leq\|f\|_\infty\|g\|_\infty.",
              frm=["norms-and-the-triangle-inequality"]),
        infer("S3.5.2", "Since $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$ and $F^+_{\\boldsymbol t}F^-_{\\boldsymbol t}=I/M$, one has $MF^+_{\\boldsymbol t}((F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)/r)=(f*g)/(rM)$.",
              r"=\frac{f*g}{rM}."),
        infer("S3.5.3", "With $\\delta=\\sqrt2\\ell2^{-p}$ and $\\eta=\\sqrt2\\,2^{-p}$, the bilinear contraction $P(u,v)=uv/r$ gives $\\|P(\\widetilde u,\\widetilde v)-P(u,v)\\|_\\infty<2\\delta$ for forward errors below $\\delta$ on disk arrays.",
              r"\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty"),
        infer("S3.5.4", "Truncating the product adds $\\eta$, and the opposite transform, a contraction with error below $\\delta$, gives total error below $3\\delta+\\eta$ before the final scale.",
              r"<3\delta+\eta."),
        infer("S3.5.5", "The exact scaling by $M$ gives error below $M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
              r"$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."),
        infer("S3.5.6", "There are $M=T/r$ pointwise polynomial products costing $O(Tp\\log(rp))$ in total, in addition to the three transform costs and a linear scaling.",
              r"There are $M=T/r$ pointwise polynomial products.  Their total cost"),
    ],
    page="ring-convolution",
    mquote=r"Pointwise multiplication commutes with applying the same record",
    frm=["transform-layout", "signed-kronecker-packing", "norms-and-the-triangle-inequality"],
    salient="No reordering is ever executed: the forward outputs are multiplied in their retained order and handed directly to the opposite procedure.",
)

S3 = show(
    "S3",
    "Normalised convolution over the polynomial ring $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ on axes of lengths $t_i\\in\\{2^{\\ell-1},2^\\ell\\}$ can be computed with synthetic transforms whose roots of unity are powers of $y$, using the accelerated layers for the butterfly rounds and the established multiplier for the pointwise products.",
    "Define the synthetic transform over $\\mathcal R_r$ and its butterfly recursion, lay out the data so every round is a simultaneous layer, multiply polynomial records exactly by signed packing, and combine them in a convolution that keeps the frequency order.",
    "In the ring $y^r=-1$ twiddle multiplication is a signed shift of the coefficient list, so all arithmetic except the pointwise products is addresses, signs and two-point butterflies, which the two accelerated primitives handle.",
    "recoverable",
    [S3_1, S3_2, S3_3, S3_4, S3_5],
    page=None,
    frm=["negacyclic-ring", "multidim-transform"],
    adds=[
        B("M", "record count", "The number $\\prod_{i<d}t_i=T/r$ of polynomial records of the array over $\\mathcal R_r$.", "count"),
    ],
)

# ---------------------------------------------------------------- S4 resampling
S4_1 = show(
    "S4.1",
    "For coprime $s<t$ with $\\theta=t/s-1>p/\\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ for the permutations $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$, and tensoring gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with line-wise approximations of error below $dp^2$ and cost $O(dTp^{3/2+\\delta}\\alpha)$.",
    "Take the Gaussian resampling identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, invert $N=C\\mathsf T\\mathsf D$ by a Neumann series, renormalise into contractions $A=\\mathsf S/2$ and $B_0=\\mathsf D'\\mathsf J'C$ without executing $P_s,P_t$, and apply them one coordinate line at a time on the padded box.",
    "The usual implementation sorts twice on each coordinate; retaining both permutations in the transform formula removes those sorts at no cost to the identity.",
    "explicit",
    [
        infer("S4.1.1", "The maps $\\mathsf S$ and $\\mathsf T$ are Gaussian-weighted sums, and the selection $C$ with diagonal $\\mathsf D$ gives $N=C\\mathsf T\\mathsf D$ whose $j$th summand at index $j$ is exactly $u_j$.",
              r"Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$",
              frm=["gaussian-function"]),
        infer("S4.1.2", "The Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the estimate $\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}$ are quoted from Harvey and van der Hoeven.",
              r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
        infer("S4.1.3", "Since $\\alpha^2\\theta>p/\\alpha^2>1$, $\\|N-I\\|<1/2$, so $N$ is invertible by the Neumann series.",
              r"Thus $\|N-I\|<1/2$, so $N$ is invertible"),
        infer("S4.1.4", "Setting $A=\\mathsf S'=\\mathsf S/2$ and $B_0=\\mathsf D'\\mathsf J'C$ with $\\mathsf J'=N^{-1}/2$ and $\\mathsf D'=2^{-(2\\alpha^2-2)}\\mathsf D$ gives contractions, using $\\|\\mathsf S'\\|<3/4$, $\\|\\mathsf J'\\|<7/8$, $\\|\\mathsf D'\\|<1$.",
              r"\|\mathsf S'\|<\frac34,\qquad"),
        infer("S4.1.5", "Because $(\\mathsf DN^{-1}C)\\mathsf T=I$ and the normalisations multiply to $2^{-(2\\alpha^2-2)}\\cdot2^{-1}\\cdot2^{-1}=2^{-2\\alpha^2}$, $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
              r"$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$."),
        infer("S4.1.6", "The ordered numerical maps have errors $16p$, $3p^2/4$ and $4$ and times $O(tp^{3/2+\\delta}\\alpha)$, $O(tp^{3/2+\\delta}\\alpha)$ and $O(tp^{1+\\delta})$, and the selection $C$ is an ordered subsequence copy in $O(tp)$ with no error, so $\\widetilde A$ and $\\widetilde B_0$ have error below $p^2$.",
              r"\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\"),
        infer("S4.1.7", "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
              r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
        infer("S4.1.8", "Axis $i$ has at most $T/t_i$ lines, so the line machines cost $\\sum_iO(T/t_i\\cdot t_ip^{3/2+\\delta}\\alpha)=O(dTp^{3/2+\\delta}\\alpha)$ and the errors add to less than $dp^2$.",
              r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
        infer("S4.1.9", "Exposing and restoring each axis in the padded box takes $O(d)$ adjacent interchanges of $\\ell$- or $(\\ell-1)$-bit fields, each costing $O(Tp(1+\\ell^\\tau))$, for $O(Tp\\,d^2(1+\\ell^\\tau))$ in total.",
              r"costs $O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs"),
    ],
    page="resampling-no-sort",
    frm=["gaussian-resampling", "fixed-point-disk-grid", "multidim-transform", "gaussian-function"],
    mquote=r"coordinate. We retain both permutations in the transform formula and",
    salient="The identity holds with the permutations $P_s$ and $P_t$ left inside the transform, so the two sorts per coordinate of the usual implementation disappear.",
)

S4_2 = show(
    "S4.2",
    "With the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_is_ij_i^2/t_i)$ one has $QF_{\\boldsymbol t}u=\\bar a\\cdot\\frac{a*(\\bar a\\cdot u)}T$ without executing $Q$, and $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$ for $S=\\prod_is_i$, so the source permutation $R$ cancels.",
    "For the first identity, expand $-s(j-k)^2$ so that the cross term $2s\\,jk$ reproduces the permuted Fourier exponent; for the second, show $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$ by substituting $h=ck$, then use the convolution rule and $F^+F=I/S$.",
    "A chirp turns the frequency change by $Q$ into a convolution (Bluestein), and an operator that is its own conjugate under a unit dilation $R$ lets the two forward $R$'s cancel the one opposite $R$.",
    "reconstructed",
    [
        infer("S4.2.1", "The chirp $a$ has period $t_i$ in coordinate $i$, because replacing $j_i$ by $j_i+t_i$ changes the exponent by an integral multiple of $2\\pi i$ (here each $t_i$ is even).",
              r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by",
              frm=["bluestein-chirp", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"]),
        infer("S4.2.2", "The coefficient of $u_{\\boldsymbol k}$ on the right of the chirp formula is $\\frac1T\\overline a_{\\boldsymbol j}a_{\\boldsymbol j-\\boldsymbol k}\\overline a_{\\boldsymbol k}=\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$, the coefficient of $QF_{\\boldsymbol t}$ since $Q$ reads frequency $-s_ij_i$ from the negative-sign transform.",
              r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because"),
        infer("S4.2.3", "For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ gives $F_q^+R_c=R_c^{-1}F_q^+$.",
              r"=(R_c^{-1}F_q^+z)_j."),
        infer("S4.2.4", "Each $t_i$ is a unit modulo $s_i$, so tensoring gives $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$, and pointwise products commute with the coordinate permutation $R$.",
              r"$RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
              salient="The source permutation $R$ appears twice from the forward transforms and once from the opposite transform, and cancels because $R$ is conjugated into $R^{-1}$ by $F^+$."),
        infer("S4.2.5", "The normalised convolution rule $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)(F_{\\boldsymbol s}v)$ and $F^+_{\\boldsymbol s}F_{\\boldsymbol s}=I/S$ give $F^+_{\\boldsymbol s}(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)=(u*v)/S^2$.",
              r"=\frac{u*v}{S^2},"),
        infer("S4.2.6", "Complex conjugation of the input and output of an algorithm for $RF_{\\boldsymbol s}$ gives one for $RF^+_{\\boldsymbol s}$, preserving the grid, norm and error bound.",
              r"Finally, conjugation"),
    ],
    page="chirp-permutation-cancel",
    frm=["bluestein-chirp", "resampling-no-sort", "dft-cyclic-convolution", "modular-arithmetic-and-residues"],
)

S4 = show(
    "S4",
    "The Fourier transforms $RF_{\\boldsymbol s}$ of coprime lengths $s_i$ can be expressed through power-of-two transforms $F_{\\boldsymbol t}$ by Gaussian resampling, with the source and target coordinate permutations $R$ and $Q$ left inside the transform identity rather than executed as sorts, and the middle transform turned into a cyclic convolution.",
    "Prove the tensor form of the one-dimensional resampling identity with permutations retained, then prove a chirp formula for $QF_{\\boldsymbol t}$ and the cancellation of $R$ across the two forward transforms, the pointwise product and the opposite transform.",
    "Executing the two permutations per coordinate would cost two sorts per axis, which would defeat the saving, so they are carried inside the identities and cancelled algebraically.",
    "explicit",
    [S4_1, S4_2],
    frm=["gaussian-resampling", "bluestein-chirp"],
    mquote=r"coordinate. We retain both permutations in the transform formula and",
    adds=[
        B("\\alpha", "resampling width", "A parameter of order $p^{1/4+\\epsilon/2}$ controlling the Gaussian window and the separation $\\theta>p/\\alpha^4$."),
        B("\\gamma", "source scale exponent", "The exponent $2d\\alpha^2$ of the exact power-of-two scale $2^\\gamma$ in the source transform."),
    ],
)

# ---------------------------------------------------------------- S5 multiplication algorithm
S5_1 = show(
    "S5.1",
    "For large $n$ fix $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$, $r=2^{\\lceil(\\log_2T)/d\\rceil}$, axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod_it_i=T$ and $t_d=r$, and distinct odd primes $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ with $\\eta=1/(4d)$, so that $Tp=\\Theta(n)$, $T/2<S<T$ and all hypotheses of the interfaces hold.",
    "Fix rational exponents first, then size parameters from $n$, then verify the interface hypotheses by explicit inequalities, finding the primes by scanning with trial division.",
    "The prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box, while each ratio $t_i/s_i$ must leave enough separation for resampling.",
    "explicit",
    [
        infer("S5.1.1", "The exponents are $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$ and $\\delta=1/16$.",
              r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\"),
        infer("S5.1.2", "The layer exponents are $\\lambda=1-2^{-52}$, $c=2^{-56}$ and $\\lambda'=1-2^{-54}$.",
              r"\lambda=1-2^{-52},\qquad c=2^{-56},\qquad"),
        infer("S5.1.3", "Further $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$, deliberately conservative.",
              r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
        infer("S5.1.4", "The layer conditions hold with room to spare: $\\tau(1+c/\\beta)<1-31\\cdot2^{-55}<\\lambda$ and $\\sigma+\\beta(1-\\sigma)=1-2^{-51}<\\lambda<\\lambda'<1$.",
              r"\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda'<1."),
        infer("S5.1.5", "With $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$, the power of two $T\\in[4n/b,8n/b)$ and $r=2^{\\lceil(\\log_2T)/d\\rceil}$ give $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
              r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,",
              frm=["logarithms-floors-ceilings-and-powers-of-two"]),
        infer("S5.1.6", "For large $b$ the comparison constants are $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$ and $C_\\ell=1$, since $\\frac1{12}p^\\epsilon\\le d\\le p^\\epsilon$ and $\\frac p{12d}\\le\\ell\\le\\frac p{3d}$.",
              r"a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$"),
        infer("S5.1.7", "Setting $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, $\\gamma=2d\\alpha^2$ and $\\eta=1/(4d)$ gives $\\gamma<28d^2\\sqrt b\\le28b^{2/3}=o(b)$ and $2\\le\\alpha<\\sqrt p$.",
              r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
        infer("S5.1.8", "Primes in $((1-2\\eta)x,(1-\\eta)x]$ number at least $\\eta x/(2\\log x)$ for $x>e^{2/\\eta}$, which exceeds $d$ for $x=r/2$ and $x=r$, so distinct odd primes $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist, with $\\gcd(s_i,t_i)=1$.",
              r"contains at least $\eta x/(2\log x)$ primes."),
        infer("S5.1.9", "Multiplying the lower bounds and applying strict Bernoulli gives $S/T>(1-1/(2d))^d>1/2$, so $T/2<S<T$.",
              r"gives $T/2<S<T$."),
        infer("S5.1.10", "From $\\theta_i\\ge\\eta/(1-\\eta)>\\eta$ one gets $\\alpha^4\\theta_i>12d^2b/(4d)=3db\\ge6b=p$, and $t_i<2^p$, so every hypothesis of the one-dimensional resampling lemma holds.",
              r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
        infer("S5.1.11", "The deterministic prime search by trial division costs $O(dr^{3/2}\\operatorname{poly}(p))=n^{o(1)}=o(n)$ and the other scalar setup is polynomial in $p$.",
              r"$n^{o(1)}=o(n)$ time."),
        infer("S5.1.12", "The radix-$2^b$ digit polynomials have $q=\\lceil n/b\\rceil$ digits, product degree $2q-2<2n/b\\le T/2<S$, so cyclic convolution modulo $x^S-1$ has no wraparound.",
              r"2q-2<2n/b\le T/2<S."),
        infer("S5.1.13", "Every product coefficient obeys $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
              r"0\le c_j\le q(2^b-1)^2<2^{3b},",
              frm=["radix-digit-convolution"]),
    ],
    page="parameter-choice",
    frm=["crt-axis-map", "gaussian-resampling", "fixed-point-disk-grid", "primes-divisibility-gcd-and-coprimality", "radix-digit-convolution"],
    mquote=r"The distinct prime lengths $s_i$ must be close to the powers of two",
    salient="The exponents are fixed rationals with astronomically small gaps ($\\epsilon=2^{-75}$, $c=2^{-56}$, $1-\\lambda'=2^{-54}$), chosen so that every margin in the final cost table stays positive.",
)

S5_2 = show(
    "S5.2",
    "The map $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$, $x\\mapsto\\prod_ix_i^{\\mu_i}$ with $\\mu_i=P_i^{-1}\\bmod s_i$ and $P_i=\\prod_{j<i}s_j$, is an algebra isomorphism preserving cyclic convolution, and it and its inverse cost $O(Tp\\,d^2(1+\\ell^\\tau))$ on the padded box.",
    "Show $\\Phi$ is a bijection on monomials by the Chinese remainder theorem, obtain the triangular formula $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j \\pmod{s_i}$ in mixed radix, and apply the updates as controlled cyclic shifts in order $i=d,\\dots,1$ on a zero-padded box.",
    "The triangular form makes each coordinate depend only on earlier coordinates, which is exactly the shape of controlled shifts, so the change of order becomes a sequence of linear-time tape operations plus axis moves.",
    "explicit",
    [
        infer("S5.2.1", "The assignment respects $x^S=1$, and the image of $x$ has order $S$ since each $\\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target monomials once and $\\Phi$ is an isomorphism preserving cyclic convolution.",
              r"$\Phi$ is an isomorphism and preserves cyclic convolution.",
              frm=["algebraic-structures-groups-rings-and-isomorphisms", "primes-divisibility-gcd-and-coprimality"]),
        infer("S5.2.2", "In mixed radix $k=\\sum_ja_jP_j$ the coordinate of $\\Phi(x^k)$ in axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j \\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i\\equiv1$.",
              r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
        infer("S5.2.3", "Zero padding to the full box $\\prod_i[0,t_i)$ is inserted by one nested scan in lexicographic order, copying the next coefficient at valid addresses and writing zeros elsewhere, in $O(Tp)$.",
              r"Insert the padding in one nested scan of the full"),
        infer("S5.2.4", "Updating targets in order $i=d,d-1,\\dots,1$ means each target's lower-index controls still hold the original digits $a_j$.",
              r"order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}."),
        infer("S5.2.5", "Each update rotates the valid target interval $[0,s_i)$ by the offset and fixes $[s_i,t_i)$, a bijection preserving the valid set and its complement, so zero padding remains zero.",
              r"zero padding remains zero after every step."),
        infer("S5.2.6", "Reversing all axes uses $O(d^2)$ interchanges, so $\\Phi$, its inverse and their padding operations cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
              r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
    ],
    page="crt-axis-map",
    frm=["dft-cyclic-convolution", "multidim-transform", "controlled-shifts", "chunk-swap"],
    mquote=r"algebraic split, with coordinate powers that make the change of order a",
)

S5_3_twist = show(
    "S5.3.1",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ is a ring isomorphism $\\Theta:\\mathbb C[x_d]/(x_d^r-1)\\to\\mathcal R_r$, $x_d\\mapsto\\zeta y$, whose negative wrap yields the cyclic wrap after untwisting, so $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
    "Check $\\Theta$ on the monomial bases, where it is diagonal, and verify the wrap term by term: a term with $k+l=j+hr$ acquires $\\zeta^{k+l}(-1)^h=\\zeta^j$.",
    "A cyclic convolution has no signs on wrap-around while the negacyclic ring has one; twisting by a $2r$th root of unity compensates the sign.",
    "reconstructed",
    [
        infer("S5.3.1.1", "The map is well defined because $(\\zeta y)^r=(-1)(-1)=1$, diagonal on the bases with coefficient $k$ multiplied by $\\zeta^k\\ne0$, hence an isomorphism with inverse multiplying by $\\zeta^{-k}$.",
              r"multiplying coefficient $k$ by the nonzero number $\zeta^k$.  It is therefore an",
              frm=["negacyclic-ring", "euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"]),
        infer("S5.3.1.2", "For $k+l=j+hr$ with $h\\in\\{0,1\\}$ a twisted negacyclic product term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
              r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
        infer("S5.3.1.3", "Hence normalised complex cyclic convolution equals $D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$, a bilinear contraction.",
              r"Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$,"),
    ],
    page="coefficient-twist",
    frm=["negacyclic-ring", "dft-cyclic-convolution"],
    salient="The sign $(-1)^h$ of the negative wrap is cancelled exactly by $\\zeta^{rh}=(-1)^h$, so the twisted negacyclic product has the plain cyclic wrap after untwisting.",
)

S5_3 = show(
    "S5.3",
    "The computed source transform $\\widetilde{\\mathscr F}$ applies the Gaussian map $\\widetilde{\\mathcal A}$, then a chirp transform $\\widetilde{\\mathscr C}$ evaluated by a twisted ring convolution, then $\\widetilde{\\mathcal B}_0$ and an exact power-of-two scale $2^\\gamma$, and has exact counterpart $RF_{\\boldsymbol s}$.",
    "Chain the resampling maps with the chirp identity so that the middle factor $QF_{\\boldsymbol t}$ is $\\bar a\\cdot\\mathcal M_{\\mathbb C}(a,\\bar a\\cdot x)$, and compute the complex convolution on the power-of-two axes through the coefficient twist and the ring convolution.",
    "The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist.",
    "explicit",
    [
        S5_3_twist,
        infer("S5.3.2", "The computed complex convolution twists both operands by disk-grid approximations $\\widetilde\\theta^+$ of $\\zeta^k$, applies $\\widetilde{\\mathcal M}_r$ to $\\iota f',\\iota g'$, and untwists the output by $\\widetilde\\theta^-$, each phase product being exact before one truncation $Q_p$, for twist cost $O(Tp^{1+\\delta})$.",
              r"f'&=Q_p(\widetilde\theta^+\mathbin{\cdot}f),\\"),
        infer("S5.3.3", "The chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$ and $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot y_0)$, with chirp construction costing $O(Tdp^{1+\\delta})$.",
              r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\"),
        infer("S5.3.4", "The source transform has exact counterpart $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$, and the opposite-sign procedure $\\widetilde{\\mathscr F}^+(z)=\\overline{\\widetilde{\\mathscr F}(\\overline z)}$ has counterpart $RF^+_{\\boldsymbol s}$.",
              r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
    ],
    page="source-transform",
    frm=["resampling-no-sort", "chirp-permutation-cancel", "ring-convolution", "coefficient-twist"],
    mquote=r"The power-of-two complex convolution used in the chirp identity is",
)

er_chain = show(
    "S5.9.1",
    "Tracking errors through the exact contractions gives a coefficient error below $28\\cdot2^\\gamma T^2L\\,2^{-p}$, where $L=\\log_2T$, for $w=(u*v)/S$, while every computed array stays in the unit disk.",
    "Propagate errors through the pipeline using that a linear contraction does not increase an input error and a bilinear contraction adds the two operand errors, inserting each exact map at the computed input.",
    "Each stage is a contraction or an exact scaling, so the error bounds of the stages can simply be added and multiplied by the known scales.",
    "recoverable",
    [
        infer("S5.9.1.1", "A linear contraction propagates an input error without increasing it, and a bilinear contraction adds the two operand errors when all four operands are in the disk.",
              r"A linear contraction propagates an input error without increasing it."),
        infer("S5.9.1.2", "A computed phase product with a disk-grid phase within $2h_p$ of a unit phase has error below $4h_p$ and does not increase the norm.",
              r"(2\|x\|+\sqrt2)h_p<4h_p,"),
        infer("S5.9.1.3", "The ring convolution has error $E_{\\rm ring}:=M(3L+2)<5TL$ in units of $h_p=2^{-p}$, and norm below $.701$ if one operand has norm at most $.7$.",
              r"E_{\rm ring}:=M(3L+2)<5TL."),
        infer("S5.9.1.4", "The computed complex convolution has error below $6TL\\,h_p$.",
              r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
        infer("S5.9.1.5", "The chirp transform has error below $8TL\\,h_p$.",
              r"<(6TL+2+4+4)h_p<8TLh_p."),
        infer("S5.9.1.6", "The source transform has error below $E_sh_p$ with $E_s=9\\cdot2^\\gamma TL$, because the Gaussian maps contribute $2dp^2<TL$ and the scale $2^\\gamma$ multiplies the error.",
              r"E_s=9\,2^\gamma TL,"),
        infer("S5.9.1.7", "The product $z=Q_p(\\widetilde U\\cdot\\widetilde V_1)$ of two arrays of norm below $.26$ has norm below $.5$ and error below $(2E_s+2)h_p$ from $U\\cdot V_1$.",
              r"$\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
        infer("S5.9.1.8", "By the cancellation $G(U\\cdot V_1)=(u*v)/S^2$ for $G=RF^+_{\\boldsymbol s}$, the opposite transform of $z$ has error below $(3E_s+2)h_p$.",
              r"G(U\cdot V_1)=(u*v)/S^2."),
        infer("S5.9.1.9", "Multiplying by $S$ gives $\\widetilde w\\approx w=(u*v)/S$ with error below $E_wh_p$, $E_w:=S(3E_s+2)<28\\cdot2^\\gamma T^2L$, and $\\|\\widetilde w\\|<1$.",
              r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
    ],
)

er_final = show(
    "S5.9.2",
    "After the second scale $2^{2b+4}S$ the real coefficient error is below $448\\,b\\,2^{-3b/4}<1/2$, so rounding gives the exact convolution coefficients $c_j\\in[0,2^{3b})$.",
    "Multiply the error bound by the known scale $2^{2b+4}S$ and use $p=6b$, $S\\le T<2^b$, $L<b$ and $\\gamma=o(b)$ to compare with $1/2$.",
    "The precision $p=6b$ is large enough to absorb scales $2^{2b+4}$ from the digit normalisation, $S<2^b$, $T^2<2^{2b}$ and $2^\\gamma$ with room to spare, leaving an exponentially small error.",
    "reconstructed",
    [
        infer("S5.9.2.1", "In tensor order the unscaled integer coefficient array is $2^{2b+4}Sw$: the factor $S$ reverses the normalisation in $w$ and $2^{2b+4}$ reverses the two input scales.",
              r"In tensor order, the unscaled integer coefficient array is"),
        infer("S5.9.2.2", "The final absolute error is below $2^{2b+4}S\\cdot28\\cdot2^\\gamma T^2L\\cdot2^{-6b}<448\\,b\\,2^{-b+\\gamma}\\le448\\,b\\,2^{-3b/4}<\\frac12$, using $S\\le T<2^b$, $L<b$ and $\\gamma\\le b/4$.",
              r"\le448b\,2^{-3b/4}<\frac12."),
        infer("S5.9.2.3", "Since the true coefficients are integers and the error is strictly below $1/2$, the nearest integer is the unique correct coefficient, and by the capacity bound it lies in $[0,2^{3b})$ and fits one signed $(3b+1)$-bit word.",
              r"that value the unique correct coefficient."),
    ],
    salient="The error is exponentially small, about $2^{-3b/4}$ times a factor linear in $b$, although the normalisations multiply the $2^{-p}$ truncation error by scales of order $2^{5b}$.",
)

er_carry = show(
    "S5.9.3",
    "Propagating radix-$2^b$ carries over the recovered coefficients $c_j$ yields the digits of the product, which has exactly $2n$ bits.",
    "Run the carry recurrence $d_j=(c_j+k_j)\\bmod2^b$, $k_{j+1}=\\lfloor(c_j+k_j)/2^b\\rfloor$ from the least significant coefficient.",
    "The product equals $\\sum_jc_j(2^b)^j$, so ordinary carry propagation converts the coefficient list to base-$2^b$ digits.",
    "recoverable",
    [
        infer("S5.9.3.1", "The recurrence is $k_0=0$, $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$.",
              r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad"),
        infer("S5.9.3.2", "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$ by induction, since $c_j+k_j\\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$.",
              r"c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1),"),
        infer("S5.9.3.3", "The invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ fixes the first $j$ radix digits of the product.",
              r"\sum_{h<j}c_hQ_0^h"),
        infer("S5.9.3.4", "The product is below $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output; zero inputs obey the same rule.",
              r"to produce exactly $2n$ bits.  Zero inputs obey the same invariant and"),
    ],
)

S5_9 = show(
    "S5.9",
    "After removing the known normalisations $S$ and $2^{2b+4}$, the recovered coefficient error is below $1/2$, so rounding gives the exact convolution coefficients, and radix-$2^b$ carry propagation yields the $2n$-bit product.",
    "Track the numerical error of each stage against explicit disk margins, show that the final error is below one half, round, then propagate carries.",
    "The convolution of the integer digit lists is computed only approximately by the floating-point-like pipeline, so exactness has to come from an error bound smaller than one half followed by rounding.",
    "recoverable",
    [er_chain, er_final, er_carry],
    page="exact-recovery",
    frm=["fixed-point-disk-grid", "radix-digit-convolution", "source-transform", "norms-and-the-triangle-inequality"],
)

S5 = show(
    "S5",
    "The algorithm splits the inputs into radix-$2^b$ digits, maps them by $\\Phi$ to the prime axes, takes two source transforms, multiplies pointwise, applies the opposite-sign transform, scales by $S$ and by $2^{2b+4}S$, rounds, undoes $\\Phi$ and propagates carries to output the exact $2n$-bit product.",
    "Obtain the digit convolution $u*v$ from $S^2\\,RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]$ using approximate source transforms, and recover the exact integer coefficients by rounding.",
    "The integer product is the carry-propagated convolution of the digit lists, and the convolution theorem turns it into pointwise multiplication of transforms; the permutation $R$ retained in the transforms cancels.",
    "recoverable",
    [
        S5_1, S5_2, S5_3,
        infer("S5.4", "The inputs are read backward in groups of $b$ bits into digits $a_0,\\dots,a_{q-1}$, each written as the exact grid numerator $a_j2^{p-b-2}$ in a signed $(p+2)$-bit real word with zero imaginary word, followed by $S-q$ zero records, costing $O(n+Sp)=O(Tp)$.",
              r"$a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero"),
        infer("S5.5", "Compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$ for the mapped digit arrays $u,v$.",
              r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
        infer("S5.6", "Multiply corresponding coefficients exactly and truncate each part toward zero to $p$ fractional bits to obtain $z$.",
              r"\item Multiply corresponding complex coefficients exactly and truncate"),
        infer("S5.7", "Compute $\\widetilde{\\mathscr F}^+(z)$ and multiply its grid numerators exactly by $S$ to obtain $\\widetilde w$.",
              r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
        infer("S5.8", "Multiply the numerators of $\\widetilde w$ exactly by $2^{2b+4}S$, round to nearest integers, write signed $(3b+1)$-bit words, apply $\\Phi^{-1}$ with padding removal, and propagate carries to output $2n$ bits.",
              r"\item Multiply the grid numerators of $\widetilde w$ exactly by",
              salient="The two occurrences of $S$ undo different normalisations: the first converts $(u*v)/S^2$ into $w=(u*v)/S$, and the second, together with $2^{2b+4}$, converts $w$ into the integer coefficient array $2^{2b+4}Sw$ that undoes the digit scaling."),
        S5_9,
    ],
    page="multiplication-algorithm",
    frm=["crt-axis-map", "source-transform", "exact-recovery", "parameter-choice", "radix-digit-convolution",
         "schoolbook-multiplication-and-divide-and-conquer-multiplication", "convolution-as-polynomial-multiplication"],
    adds=[
        B("b", "digit width", "The number $\\lceil\\log_2n\\rceil$ of bits in each radix digit, so inputs are polynomials in $2^b$.", "count"),
        B("S", "prime length product", "The product $\\prod_is_i$ of the pairwise coprime source lengths, with $T/2<S<T$.", "count"),
    ],
)

# ---------------------------------------------------------------- S6 cost accounting
rowsC = [
    ("S6.1", "Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $p^{\\epsilon(1+c)}$ of $p$.",
     r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$"),
    ("S6.2", "Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, a power $p^{1-\\epsilon c(1-\\tau)}$.",
     r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$"),
    ("S6.3", "Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, a power $p^{1-\\epsilon(1-\\lambda')}$.",
     r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$"),
    ("S6.4", "CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, a power $p^{\\tau+\\epsilon(2-\\tau)}$.",
     r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$"),
    ("S6.5", "Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, a power $p^{3/4+\\delta+3\\epsilon/2}$, because $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$.",
     r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$"),
    ("S6.6", "Chirps, twists and scalar products cost $dp^\\delta$, a power $p^{\\epsilon+\\delta}$.",
     r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$"),
    ("S6.7", "Packed polynomial products cost $\\log(rp)=O(p^{1-\\epsilon})$, a power $p^{1-\\epsilon}$.",
     r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$"),
    ("S6.8", "Final scaling and rounding cost $p^\\delta$, absorbed above.",
     r"Final scaling and rounding & $p^\delta$ & absorbed above"),
    ("S6.9", "Input, padding, carries and output cost $1$ per unit volume, absorbed above.",
     r"Input, padding, carries and output & $1$ & absorbed above"),
]

S6_table = show(
    "S6.T",
    "Divided by $V=Tp=\\Theta(n)$, the costs of the operations are the nine rows of the cost table, with seven dominant powers of $p$.",
    "List each operation's cost per unit volume and its power of $p$ by substituting the size relations $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$.",
    "With every parameter a fixed power of $p$, each cost per volume is a power of $p$ whose exponent is a simple function of the fixed rationals, so the margin below one can be read off.",
    "recoverable",
    [infer(i, c, q) for (i, c, q) in rowsC],
)

S6_margins = show(
    "S6.M",
    "The margins $g_i$ of the seven dominant powers below one are $g_1=1-\\epsilon(1+c)>1/2$, $g_2=\\epsilon c(1-\\tau)=2^{-181}$, $g_3=\\epsilon(1-\\lambda')=2^{-129}$, $g_4=1-\\tau-\\epsilon(2-\\tau)>2^{-51}$, $g_5=1/4-\\delta-3\\epsilon/2>1/8$, $g_6=1-\\delta-\\epsilon>1/2$ and $g_7=\\epsilon=2^{-75}$, so $\\min_ig_i=2^{-181}=2\\kappa$.",
    "Substitute the fixed rationals $\\tau=1-2^{-50}$, $c=2^{-56}$, $\\epsilon=2^{-75}$, $\\lambda'=1-2^{-54}$, $\\delta=1/16$ into each of the seven margins.",
    "The saving in the final bound can be no larger than the smallest margin, so the minimum over the rows decides the exponent $\\kappa$.",
    "reconstructed",
    [
        infer("S6.M.1", "The seven margins are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4=1-\\tau-\\epsilon(2-\\tau)$, $g_5=1/4-\\delta-3\\epsilon/2$, $g_6=1-\\delta-\\epsilon$ and $g_7=\\epsilon$.",
              r"g_1&=1-\epsilon(1+c),\qquad"),
        infer("S6.M.2", "Direct substitution gives $g_1>1/2$, $g_2=2^{-181}$ (as $2^{-75}\\cdot2^{-56}\\cdot2^{-50}$), $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.",
              r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
        infer("S6.M.3", "Thus $\\min_ig_i=2^{-181}=2\\kappa$, an explicit slack covering any remaining fixed power of $\\log p$.",
              r"Thus $\min_i g_i=2^{-181}=2\kappa$.  This explicit slack will cover",
              salient="The smallest margin, $g_2=\\epsilon c(1-\\tau)$, is a product of three tiny gaps ($2^{-75}\\cdot2^{-56}\\cdot2^{-50}$) and is exactly $2\\kappa$, which is why $\\kappa=2^{-182}$."),
    ],
)

S6_derive = show(
    "S6.D",
    "Each normalised cost is justified: the layout costs follow from Lemma-level bounds, the Gaussian line maps sum over lines, the chirp, twist and product costs are pointwise, and all setup, exceptional-stream and repair costs are $o(Tp)$.",
    "Derive each row from the corresponding earlier cost lemma and show the remaining setup costs vanish relative to $Tp$ because $r$ exceeds every fixed power of $p$.",
    "Rows of the table are the cost statements of the earlier pages, and what remains is to charge descriptors, setup and rare exceptional records to the volume.",
    "recoverable",
    [
        infer("S6.D.1", "The first three rows are the terms of the synthetic-transform cost: $O(dK)$ linear scans, $O(p/K)$ chunk exchanges each costing $K^\\tau$ per volume, hence $O(pK^{\\tau-1})$, and at most $\\ell$ simultaneous rounds at $d^{\\lambda'}$.",
              r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
        infer("S6.D.2", "Axis exposure and restoration need $O(d^2)$ adjacent axis moves each costing $O(V(1+\\ell^\\tau))$, and the $d$ CRT rotations cost $O(dV)$.",
              r"Axis exposure and restoration require $O(d^2)$ adjacent axis moves."),
        infer("S6.D.3", "For Gaussian resampling axis $i$ has at most $T/t_i$ lines, so the line machines sum to $O(dTp^{3/2+\\delta}\\alpha)$, and $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$ explains the power of $p$.",
              r"Dividing by $V=Tp$ gives the fifth row.  The factor"),
        infer("S6.D.4", "Chirp numerators computed with the established multiplier and the exponentials cost $O(dp^{1+\\delta})$ per entry.",
              r"then generating the exponentials, costs $O(dp^{1+\delta})$ per entry."),
        infer("S6.D.5", "Four integer products on $O(rp)$ bits per record over $T/r$ records cost $O(Tp\\log(rp))$ in total, using the established multiplier on records of length $O(rp)=o(n)$ without calling the improved algorithm.",
              r"they do not call the improved algorithm being constructed."),
        infer("S6.D.6", "Layer and layout recursions have constant branching and depth $O(\\log p)$, so at most $p^A$ visits with $p^C$ setup each cost $p^{A+C}=o(Tp)$, and per-record or per-line descriptor work is $O(Tp^{A+C}/r)=o(Tp)$.",
              r"costs at most $p^{A+C}=o(Tp)$."),
        infer("S6.D.7", "The compact exceptional stream of a packed call has length $O(V_{\\rm call}d2^{-K})$, and its stable sorting costs sum to $O(Vp^{A'}2^{-K})=o(V)$ deterministically.",
              r"=O(Vp^{A'}2^{-K})=o(V)"),
    ],
)

S6 = show(
    "S6",
    "The total running time is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$ with $\\kappa=2^{-182}$, because every row of the cost table is at most $p^{1-2\\kappa}$ per unit volume and any fixed power of $\\log p$ is at most $p^\\kappa$.",
    "Tabulate the cost per unit volume of every operation as a power of $p$, verify that each of the seven dominant exponents is at most $1-2\\kappa$ using explicit margins, absorb polylogarithmic factors into the slack, and add setup and exceptional-stream costs showing they are $o(V)$.",
    "The explicit slack in the margins will cover any remaining fixed power of $\\log p$.",
    "explicit",
    [S6_table, S6_margins, S6_derive,
     infer("S6.F", "Each of the seven displayed powers is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$, so the large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
           r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
     infer("S6.G", "Using schoolbook multiplication below a fixed cutoff gives one fixed-alphabet, fixed-tape deterministic machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length, producing exactly the $2n$-bit product.",
           r"$O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely")],
    page="cost-accounting",
    frm=["multiplication-algorithm", "chunk-swap", "simultaneous-butterfly-layer", "transform-layout", "resampling-no-sort",
         "nlogn-subroutine", "big-o", "quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o"],
    mquote=r"any remaining fixed power of $\log p$.",
    salient="The saving exponent $\\kappa=2^{-182}$ is half the smallest of seven margins below one, which is itself a product of tiny exponent gaps; the proof is built so that every cost row loses at least a power $p^{2\\kappa}$.",
)

ROOT = show(
    "S0",
    "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture in this model.",
    "Build two accelerated tape primitives (fast address-chunk interchange and simultaneous butterfly layers) from fixed linear networks with a rank saving, use them to speed up synthetic transforms over $\\mathbb C[y]/(y^r+1)$, place these in a Gaussian-resampling reduction of the digit convolution, recover the exact product by rounding and carries, and add up the cost against an explicit slack.",
    "Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both data movement and arithmetic.",
    "explicit",
    [S1, S2, S3, S4, S5, S6],
    page="main-theorem",
    frm=["n-log-n-conjecture", "fixed-tape-model", "big-o"],
    mquote=r"We therefore need savings in both movement and arithmetic.",
    salient="A strict power saving $(\\lg n)^{-\\kappa}$ below $n\\log n$ is obtained although every step is exact and deterministic, and the saving comes from a single inequality $s<Wm$ for the rank of two small linear networks.",
    adds=[
        B("m", "label dimension", "The dimension $h^3=10^6$ of the label space of a fixed network, and the factor by which one recursive call multiplies the chunk parameter.", "count"),
        B("W", "wire count", "The number of wires (roles) of a fixed network, equal to the number of role streams a call is split into.", "count"),
        B("s", "total edge rank", "The sum over the edges of a fixed network of the rank of the edge change, i.e. the number of smaller calls in one invocation.", "count"),
        B("\\kappa", "saving exponent", "The fixed exponent $2^{-182}$ by which the logarithmic factor is reduced."),
        B("V", "stored volume", "The number of stored data bits of the array being processed.", "count"),
        B("p", "precision", "The number of fractional bits of the fixed-point grid, $p=6\\lceil\\log_2n\\rceil$.", "count"),
        B("d", "axis count", "The number of power-of-two axes (address chunks), of order $p^{\\epsilon}$.", "count"),
        B("K", "chunk bits", "The number of bits in each address chunk, $K=\\lfloor d^c\\rfloor$.", "count"),
        B("r", "record length", "The number of complex coefficients $r=2^\\ell$ in a polynomial record modulo $y^r+1$.", "count"),
        B("T", "box size", "The number $\\prod_it_i$ of entries in the padded power-of-two box, with $Tp=\\Theta(n)$.", "count"),
        B("\\ell", "log record length", "The binary logarithm $\\log_2r$."),
        B("t_i", "power-of-two length", "The length $r/2$ or $r$ of axis $i$ in the padded box."),
        B("s_i", "prime length", "The distinct odd prime length of axis $i$, just below $t_i$."),
        B("\\tau", "interchange exponent", "The fixed exponent $1-2^{-50}$ in the interchange cost $O(Vu^\\tau)$."),
        B("\\lambda'", "layer exponent", "The fixed exponent $1-2^{-54}$ in the butterfly layer cost $O(Vd^{\\lambda'})$."),
    ],
)

result = {"root": ROOT}

if __name__ == "__main__":
    out = sys.argv[1]
    json.dump(result, open(out, 'w'), indent=1, ensure_ascii=False)
    print("written", out)
