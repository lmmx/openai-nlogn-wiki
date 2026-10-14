"""Build the argument plan for task 0003-argument and check it."""
import json
import sys

sys.path.insert(0, "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1OM/exegenius/tasks/0003-argument")
from lib import ANSWER, Q, X, add, assign_ids, check, coverage, infer, mot, show  # noqa: E402

# =====================================================================================
# Part 1. The two tape procedures (Sections 2-5)
# =====================================================================================

stream_ops = infer(
    r"For a fixed radix $q$, permuting the digit values at two positions, moving one digit, "
    r"splitting on a digit, mapping aligned streams pointwise and merging, and splitting whole "
    r"rows cyclically into a fixed number $W$ of equal streams (and merging them back) each take "
    r"$O(V)$ steps on a fixed number of tapes, counters, head returns and cleanup included.",
    X("Fix a radix $q\\ge2$.", "takes $O(V)$ steps on a fixed number of one-dimensional tapes:"),
    page="stream-ops",
    frm=["array-order", "fixed-tape-model", "positional-number-representation-and-carries"],
)

controlled_shifts = show(
    r"When a target field $y\in[Q]$, $Q=q^b$, follows its control fields, the update "
    r"$y\mapsto y+a(\text{controls})\bmod Q$, a cyclic shift of whole blocks, and "
    r"multiplication of $y$ by a fixed rational unit each cost $O(V)$, provided the offset is "
    r"prepared in $b^{O(1)}$ time.",
    r"Within each fiber of $Q$ consecutive blocks, split at $Q-a$ and merge the two pieces in "
    r"the opposite order; for multiplication by $c$ split the fiber into its $c$ increasing "
    r"pieces and merge by a residue counter; for negation reverse the blocks through a stack.",
    mot(
        r"Because the target follows its controls, every fiber of the target is one contiguous "
        r"run of blocks whose offset is known when the run starts, so a shift is a single split "
        r"and merge, and the polynomial offset work is absorbed by the $Q$ blocks of the fiber.",
        "explicit",
        Q("The next operations are linear because their target field follows their control fields."),
    ),
    [
        infer(
            r"Splitting each fiber at $Q-a$ and reading the second piece before the first realizes "
            r"$y\mapsto y+a\bmod Q$, and the offset work is absorbed because $b^C=O(q^b)=O(Q)$.",
            X("In the merge read the second piece and then the first piece for each prefix.",
              "of the new target coordinate."),
        ),
        infer(
            r"Multiplication by a fixed $c$ prime to $q$ splits a fiber into the $c$ increasing "
            r"pieces $j=\lfloor cy/Q\rfloor$ and merges by the unique $j$ with "
            r"$y'+jQ\equiv0\pmod c$; reversing split and merge gives $c^{-1}$, and negation "
            r"reverses the blocks through a stack.",
            X("For positive fixed integer $c$ prime to $q$, the permutation",
              "has $c$ increasing pieces, classified by"),
        ),
    ],
    page="controlled-shifts",
    frm=["stream-ops", "modular-arithmetic", "primes-coprimality-and-gcd"],
)

# ---------------------------------------------------------------- the scalar network

network = show(
    r"For arbitrary initial scratch values, the three-stage scalar network sends "
    r"$(X_a,Y_a)\mapsto(-Y_a,X_a)$ for every index $a$ and restores every scratch wire; in the "
    r"bit construction this is the permutation exchanging $X_a$ and $Y_a$.",
    r"Run each invocation (one coordinate of the triple index at a time) by the eight-row "
    r"schedule: subtract side injection and scatter, copy, gather, scatter, side injection, "
    r"undo gather, undo copy; check that its net effect is $y_S\gets y_S+x_S$ coefficient by "
    r"coefficient, and compose a forward, an inverse and a forward stage.",
    mot(
        r"Subtracting the effect of the old scratch values before injecting the sources, and "
        r"undoing copies and gathers afterwards, makes the net change independent of the "
        r"arbitrary scratch contents and returns them unchanged.",
        "explicit",
        X("The first two rows of", "the last two restore the scratch values."),
    ),
    [
        infer(
            r"If the initial side and central vectors are $a,c$, rows 0-1 subtract "
            r"$\mathcal Ja+\mathcal Rc$ from the target, rows 2-3 change the scratch to "
            r"$a+\mathcal Vx,c+\mathcal Gx$, rows 4-5 add "
            r"$\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$ and rows 6-7 restore $c,a$, "
            r"so the net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, "
            r"independent of $a$ and $c$.",
            Q("The net target change is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independently of $a,c$."),
        ),
        infer(
            r"In the bit construction the central coefficient from $x_T$ to $y_S$ is "
            r"$|S\cap T|\bmod2$; side injection cancels exactly the pairs meeting in one point, "
            r"distinct triples meeting in zero or two points already give zero, and $S=T$ gives one.",
            X("In the bit case, the central coefficient", "and the self coefficient is one."),
        ),
        infer(
            r"In the complex construction the central coefficient is $(|S\cap T|-1)/2$; side "
            r"injection cancels it for distinct triples meeting in zero or two points, "
            r"intersection one contributes zero and $S=T$ gives one, so both nets are "
            r"$y\gets y+x$.",
            X("In the complex case, the central coefficient", "Thus both net maps are $y\\gets y+x$."),
        ),
        infer(
            r"A forward stage, an inverse stage ($X\gets X-Y$) and a forward stage take "
            r"$(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, each invocation restoring "
            r"its own scratch wires.",
            X("Starting from $(x,y)$, the three stages give", "Each invocation restores its own auxiliary wires."),
        ),
    ],
    page="network",
    frm=["sets-subsets-and-basic-combinatorics", "binary-field-f2-and-xor", "boolean-gates-and-circuits"],
    salient=r"The outcome does not depend on the arbitrary initial scratch contents, and every "
            r"scratch wire ends with its initial value.",
)

frames = show(
    r"If every source, gate and sink $v$ carries an invertible frame $D_v$, common to all "
    r"incidences of a gate, and each edge $u\to v$ applies $D_vD_u^{-1}$, then the array "
    r"network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so a route from input "
    r"role $w$ to output role $\rho(w)$ with sign $\varepsilon_w$ applies "
    r"$\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, scratch roles included.",
    r"Maintain the invariant that the stored array at each vertex is $D_v$ applied to the "
    r"logical array: define the input's logical interpretation by $D_{\rm in}^{-1}$, let each "
    r"edge change the frame, and use linearity of the pointwise gates.",
    mot(
        r"Once the scalar routing is fixed, only the endpoint frames determine each route's "
        r"operator, so the intermediate frames are free to be chosen to make each edge change cheap.",
        "explicit",
        X("Once the scalar routing is fixed, the endpoint frames", "to make each edge change inexpensive."),
    ),
    [
        infer(
            r"The physical input $f$ is given the logical interpretation $g=D_{\rm in}^{-1}f$, "
            r"which needs no tape work, so the invariant holds at the sources.",
            X("For a supplied physical input $f$, define its logical interpretation", "requires no physical preprocessing."),
        ),
        infer(
            r"An edge changes $D_u\varphi$ into $D_v\varphi$, and at a gate "
            r"$\sum_jc_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the common frame commutes with "
            r"the pointwise gate and the invariant reaches the sinks.",
            Q("Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks."),
        ),
        infer(
            r"For a signed role permutation the route from $w$ to $\rho(w)$ therefore applies "
            r"$\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, and every "
            r"role, auxiliary ones included, enters this identity.",
            Q("All roles, including the auxiliary roles, enter this identity."),
        ),
    ],
    page="frames",
    frm=["network", "vectors-matrices-and-linear-maps", "functions-bijections-and-permutations"],
)

# ---------------------------------------------------------------- the key step: rank saving

subset_labels = show(
    r"Nondegenerate subspaces of $\mathcal F=F^{\otimes3}$, of dimension $m=h^3$, can be "
    r"attached to all sources, gates and sinks so that every edge joins nested labels, the "
    r"terminal labels run $U_a\to\mathcal F$ on $X_a$, $0\to U_a^\perp$ on $Y_a$ and "
    r"$0\to\mathcal F$ on scratch wires, and the only decreasing edges are the central-wire "
    r"edges from time 3 to time 4, each losing dimension $h$.",
    r"Pair the indicator vectors $t_T$ of three-element subsets by "
    r"$\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$ (form $I-J/9$) or by the dot "
    r"product over $\mathbb F_2$, so that neighboring triple lines are orthogonal; expose one "
    r"tensor factor per stage; and assign gate labels from the split "
    r"$A\otimes F=(B\otimes F)\perp(P\otimes F)$, side wires passing through "
    r"$P\otimes\langle t_X\rangle\subset P\otimes t_Y^\perp$ and central wires returning once "
    r"from $A\otimes F$ to $B\otimes F$.",
    mot(
        r"Gather and scatter create coefficients depending on intersection size, and the side "
        r"wires cancel the unwanted ones; the orthogonality of neighboring indicator vectors is "
        r"what lets the side-wire labels grow monotonically through the gates.",
        "explicit",
        Q("Orthogonality of the corresponding indicator vectors permits the subspace assignments."),
    ),
    [
        infer(
            r"For the bit network, labels live in $F=\mathbb Q^h$ with "
            r"$\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ (eigenvalues $1$ and $-91/9$), where "
            r"$\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$; for the "
            r"complex network, in $F=\mathbb F_2^h$ with the dot product, where "
            r"$t_T\cdot t_T=1$; so every triple line is nondegenerate and neighboring triple "
            r"lines (meeting in one point, respectively distinct with even intersection) are "
            r"orthogonal.",
            X("Thus every triple line is nondegenerate, and neighboring triple lines",
              "in the label field belonging to either construction."),
        ),
        infer(
            r"The ambient space $\mathcal F=F^{\otimes3}$ with the tensor form is nondegenerate "
            r"of dimension $m$, and the data lines are $U_a=\langle t_{a_1}\otimes t_{a_2}\otimes t_{a_3}\rangle$.",
            X("The ambient label space is $\\mathcal F=F^{\\otimes3}$", "It has dimension $m$ and is nondegenerate."),
        ),
        infer(
            r"At stage $j$, with $A=F^{\otimes(j-1)}$, $P$ the line of the earlier triple "
            r"factors, $B=P^\perp$ in $A$ and $Q$ the line of the later ones, the $X$ label goes "
            r"from $A\otimes\langle t\rangle\otimes Q$ to $(A\otimes F)\otimes Q$ and the $Y$ "
            r"label from $B\otimes\langle t\rangle\otimes Q$ to "
            r"$(P\otimes\langle t\rangle)^\perp_{A\otimes F}\otimes Q$, which are exactly the next "
            r"stage's incoming labels, starting at $U_a,0$ and ending at $\mathcal F,U_a^\perp$.",
            X("Thus the prescribed outgoing labels are", "the next incoming labels."),
        ),
        infer(
            r"A side wire joining neighboring physical triples grows its common component to "
            r"$B\otimes F$ while the rest passes through "
            r"$P\otimes\langle t_X\rangle\subset P\otimes t_Y^\perp\subset P\otimes F$, which is "
            r"possible because $t_X\perp t_Y$.",
            Q("The first inclusion is possible because $t_X\\perp t_Y$."),
        ),
        infer(
            r"Central wires carry $A\otimes F$ at the physical $X$ gates and $B\otimes F$ at the "
            r"$Y$ gates and return once from the former to the latter, losing exactly "
            r"$P\otimes F$; the gate order confines all decreases to this return.",
            X("A central wire", "while the other edges realize the prescribed stage transitions."),
        ),
        infer(
            r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are "
            r"the central-wire edges from time 3 to time 4, each losing dimension $h$.",
            X("Every edge joins comparable nondegenerate labels.", "their dimension loss is $h$."),
        ),
        infer(
            r"The side edge from time 2 to time 5 is where the neighbor relation is used: "
            r"$t_X\perp t_Y$ gives $\langle t_X\rangle\subset t_Y^\perp$, with complement "
            r"$\langle t_X,t_Y\rangle^\perp$ of dimension $h-2$.",
            X("The side edge $2\\to5$ uses the neighbor relation essentially.",
              "we have $\\langle t_X\\rangle\\subset t_Y^\\perp$."),
        ),
        infer(
            r"Splitting $A=B\perp P$ and $F=\langle t\rangle\perp t^\perp$ gives every other "
            r"residual, so label dimension is nondecreasing on every edge except the central "
            r"$3\to4$ edges, which remove $P\otimes F\otimes Q$.",
            X("Label dimension is nondecreasing along every edge except", "which removes $P\\otimes F\\otimes Q$."),
        ),
    ],
    page="subset-labels",
    frm=["matrix-basics", "network", "sets-subsets-and-basic-combinatorics", "binary-field-f2-and-xor"],
    adds=[
        add(r"\mathcal F", "ambient label space",
            "The tensor cube of the triple-indicator space, with its tensor bilinear form, in which all labels lie.",
            "direct"),
        add(r"t_T", "triple indicator",
            "The indicator vector, over the rationals or over the two-element field, of a three-element subset T of the ground set.",
            "direct"),
    ],
)

dimension_sum = show(
    r"The absolute label-dimension changes over all edges sum to $Wm-2N+2L$ with $L=Ich$: the "
    r"signed changes telescope to the sink total $Wm-N$ minus the source total $N$, and the "
    r"only exceptions to monotonicity, the $Ic$ central $3\to4$ edges, each lose $h$.",
    r"Telescope the signed changes through the gates, evaluate the two terminal sums from the "
    r"prescribed labels, and add back twice the loss on the decreasing edges.",
    mot(
        r"Absolute and signed changes differ only on decreasing edges, and the signed sum "
        r"depends only on the terminal labels because each gate's label is shared by the "
        r"incoming and outgoing incidence of every wire it touches.",
        "recoverable",
    ),
    [
        infer(
            r"Each touched wire has one incoming and one outgoing incidence with the same gate "
            r"label, so at every gate the signed dimension changes cancel and the signed sum "
            r"telescopes to the terminal labels.",
            X("The signed sum of dimension changes telescopes at every gate:", "with the same gate label."),
        ),
        infer(
            r"The source labels ($U_a$ of dimension one on the $N$ wires $X_a$, zero elsewhere) "
            r"sum to $N$ and the sink labels ($U_a^\perp$ of dimension $m-1$ on the $Y_a$, "
            r"$\mathcal F$ elsewhere) sum to $Wm-N$, so the signed increase is $Wm-2N$.",
            X("The sum of source dimensions is $N$,", "The signed increase is therefore $Wm-2N$."),
        ),
        infer(
            r"There are $Ic$ decreasing edges ($I=3v^2$ invocations with $c$ central wires each), "
            r"each losing $h$, so $L=Ich$ and replacing signed by absolute changes adds $2L$.",
            Q("There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$."),
        ),
    ],
    frm=["subset-labels", "matrix-basics"],
)

rank_saving = show(
    r"Summed over all edges of either network, the absolute changes of label dimension equal "
    r"$Wm-2N+2L$, where the loss $L=Ich$ on decreasing edges satisfies $L/N=100/539$ (bit) or "
    r"$101/539$ (complex), below $1/2$; so the total stays below $Wm-N$, leaving a strict "
    r"deficit $s<Wm$ even after the bit interface adds $N$ source ranks.",
    r"Attach nested nondegenerate subspace labels to every vertex, telescope the signed "
    r"dimension changes from the terminal labels, confine all decreases to the central-wire "
    r"returns, and compute the resulting loss exactly.",
    mot(
        r"The terminal labels fix the signed sum of dimension changes at $Wm-2N$, so the "
        r"absolute sum, which counts the smaller calls, exceeds it only by twice the dimension "
        r"lost on decreasing edges; keeping that loss small relative to $N$ leaves the saving.",
        "explicit",
        X("The saving will come from keeping the total dimension lost on decreasing", "small relative to $N$."),
    ),
    [
        subset_labels,
        dimension_sum,
        infer(
            r"Over $\mathbb F_2$ every residual is nondegenerate and every nonzero one contains a "
            r"norm-one vector (coordinate units outside small supports), hence is nonalternating "
            r"and has an orthonormal basis, so in the complex construction a residual of "
            r"dimension $k$ is realized by exactly $k$ two-point kernels, one per basis vector.",
            X("Each residual is nondegenerate by the decompositions above.",
              "nonalternating binary symmetric space has an orthonormal basis."),
        ),
        infer(
            r"With $N=v^3$, $I=3v^2$, $v=\binom{100}3=161700$, $h=100$ and $c=h$ (bit) or $h+1$ "
            r"(complex, the extra wire $C_\ast$), the identity $L/N=3ch/v$ gives exactly "
            r"$100/539$ and $101/539$, both below $1/2$.",
            X("The loss ratios have the exact values", "In particular, both are smaller than $1/2$."),
        ),
    ],
    page="rank-saving",
    frm=["network", "frames", "matrix-basics"],
    salient=r"The deficit is strict but minute: the relative deficits are "
            r"$\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$, about "
            r"$10^{-11}$, yet any strict deficit $s<Wm$ already makes the recursion exponent "
            r"smaller than one.",
    adds=[
        add("L", "decreasing-edge loss", "The total label dimension lost on edges whose label shrinks.", "count"),
        add("I", "invocation count", "The number of separate eight-row invocations over the three stages.", "count"),
        add("c", "central wires", "The number of central wires per invocation: h in the bit network and h+1 in the complex one.", "count"),
        add("v", "triple count", "The number of three-element subsets of the ground set of size h.", "count"),
    ],
)

bit_network = show(
    r"With matrices $M_v=P_U$ (projection onto the label $U$ along $U^\perp$) at gates and "
    r"sinks, $-P_{U_a}$ at the source of $X_a$ and $0$ at other sources, the XOR-only bit "
    r"network routes each input role $w$ to $\rho(w)$ with "
    r"$M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$, and its edge differences have "
    r"total rational rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.",
    r"Use address shears $\Phi_M:(H,D)\mapsto(H+MD,D)$ as frames, so frames compose by adding "
    r"matrices; read each edge's rank off its label change, treat the $N$ source edges "
    r"separately, and telescope the terminal matrices.",
    mot(
        r"Shear frames compose additively, $\Phi_{M'}\Phi_M=\Phi_{M'+M}$, so with "
        r"$D_v=\Phi_{M_v}$ the endpoint matrix difference on each route is exactly the shear "
        r"applied to that role, and each edge is a shear by a matrix of small rank.",
        "explicit",
        X("Using $D_v=\\Phi_{M_v}$ in", "is exactly the shear applied to that role."),
    ),
    [
        infer(
            r"Each gate or sink with label $U$ gets $P_U$, the source of $X_a$ gets $-P_{U_a}$ "
            r"and every other source gets $0$.",
            X("Assign $P_U$ to", "zero to every other source."),
        ),
        infer(
            r"Over a radix coprime to the fixed denominators, $\Phi_M$ is an invertible "
            r"$\mathbb F_2$-linear permutation of array entries with $\Phi_{M'}\Phi_M=\Phi_{M'+M}$.",
            X("Hence $\\Phi_M$ is an invertible", "$\\Phi_{M'}\\Phi_M=\\Phi_{M'+M}$."),
        ),
        infer(
            r"For nested nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ "
            r"and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and "
            r"reversing an edge only negates it.",
            X("For $U\\subset V$ nondegenerate,", "negates the matrix without changing its rank."),
        ),
        infer(
            r"The one exception is the $N$ edges leaving the $X_a$ sources: the first gate on "
            r"$X_a$ has label $U_a$, so the edge matrix $P_{U_a}-(-P_{U_a})=2P_{U_a}$ has rank one "
            r"where the label dimension did not change, adding $N$ to the label count.",
            X("The only exceptions are the $N$ negative source projections.", "where the corresponding dimension change was zero."),
        ),
        infer(
            r"Hence $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-N+2L_{\rm b}$, whose "
            r"deficit $N-2L_{\rm b}$ from $W_{\rm b}m$ is positive because $L_{\rm b}<N/2$.",
            Q("Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
        ),
        infer(
            r"For $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other "
            r"role has zero source and identity sink matrix, so every routed role receives the "
            r"same shear $H\gets H+D$.",
            X("For an input $X_a$ the endpoint difference is", "zero source matrix and identity sink matrix."),
        ),
    ],
    page="bit-network",
    frm=["frames", "subset-labels", "rank-saving", "matrix-basics", "binary-field-f2-and-xor"],
)

phase_network = show(
    r"In the complex network with binary labels and phase frames "
    r"$\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, "
    r"$q_U(x)=\operatorname{wt}(P_Ux)\bmod4$, each edge's frame change $\mathcal C_V\mathcal C_U^{-1}$ "
    r"is a product of one two-point kernel $aI+bX_v$ (or its inverse) per vector of an "
    r"orthonormal residual basis, these kernels number $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, "
    r"and after diagonal source and sink corrections the endpoint operator is $C^{\otimes m}$ "
    r"on every role, on any number of columns.",
    r"Use additivity of Hamming weight modulo four on orthogonal binary vectors to write each "
    r"frame change as one diagonal phase per residual basis vector, conjugate each phase by "
    r"Hadamard matrices into a translation kernel, and telescope the frames along each route, "
    r"repairing the one route $X_a\to Y_a$ with $Z$ signs.",
    mot(
        r"The frames are chosen so that the endpoint operator becomes the butterfly layer after "
        r"diagonal phases and a dyadic scale, while each edge is a few smaller calls of the same "
        r"procedure on fewer selected bits.",
        "explicit",
        X("For the numerical procedure, the endpoint operator becomes", "smaller calls to the same procedure."),
    ),
    [
        infer(
            r"Since $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$, "
            r"weight is additive modulo four when $z\cdot w=0$, so on an increasing edge "
            r"$q_V-q_U\equiv\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod4$ for an "
            r"orthonormal basis $\mathcal B$ of the residual, with the sign reversed on a "
            r"decreasing edge.",
            Q("If $z\\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four."),
        ),
        infer(
            r"Each basis vector has odd weight, so its phase is "
            r"$i^{\varepsilon[v\cdot x]}=\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$, "
            r"and $H\operatorname{diag}(1,-1)H=X$ turns the character into the translation $X_v$, "
            r"giving $aI+bX_v$ or its inverse.",
            Q("The displayed phase therefore becomes $aI+bX_v$ or its inverse."),
        ),
        infer(
            r"Nonzero residuals have orthonormal bases and zero residuals take the empty basis, "
            r"so the kernels number $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$, with deficit "
            r"$2N-2L_{\rm c}>0$ and no source exception.",
            X("The nonzero residuals have such bases by", "The deficit is $2N-2L_{\\rm c}>0$."),
        ),
        infer(
            r"On $k$ columns every frame is a $k$th tensor power, so each residual vector "
            r"contributes one factor acting on all $k$ columns at once.",
            X("Thus each residual vector contributes one factor acting on all $k$", "such factors over the network."),
        ),
        infer(
            r"The zero label has frame $I$ and the full label frame $C^{\otimes m}$ since "
            r"$q_{\mathcal F}(x)=\operatorname{wt}(x)$, so every route except $X_a\to Y_a$ "
            r"already receives $C^{\otimes m}$.",
            X("The zero label has frame $I$,", "Every pair except $X_a\\to Y_a$ has these zero and full labels."),
        ),
        infer(
            r"On the exceptional route $X_a\to Y_a$ the operator is $C^{-1}$ on the 27 "
            r"coordinates of $\operatorname{supp}(u_a)$ and $C$ elsewhere; applying $Z_{a,k}$ "
            r"before and $i^{27k}Z_{a,k}$ after turns all $27k$ inverse factors into $C$ by "
            r"$C=iZC^{-1}Z$.",
            X("There are $27k$ inverse factors, so the identity", "turns each of them into $C$."),
        ),
        infer(
            r"Negating the physical $X$ outputs and returning output role $\rho(w)$ to role $w$ "
            r"leaves the forward tensor product on every role, scratch roles included.",
            Q("Every role, including every scratch role, now has the required forward tensor product."),
        ),
    ],
    page="phase-network",
    frm=["frames", "subset-labels", "rank-saving", "butterfly-fft", "complex-numbers", "binary-field-f2-and-xor"],
)

explicit_exponents = infer(
    r"The relative deficits $\eta_{\rm b}=339/22587335000000$ and "
    r"$\eta_{\rm c}=73/19906842167500$ both exceed $20\cdot2^{-50}$, and $\log m<20$ gives "
    r"$m^{1-2^{-50}}>m(1-20\cdot2^{-50})>m(1-\eta)$, so $s_{\rm b}/W_{\rm b}<m^\tau$ and "
    r"$s_{\rm c}/W_{\rm c}<m^\sigma$ with $\tau=\sigma=1-2^{-50}$.",
    X("Both exact deficits displayed above are greater than", "0<\\tau=\\sigma<1."),
    frm=["logarithms-and-exponentials"],
)

networks = show(
    r"Two fixed linear networks, a bit network over $\mathbb F_2$ with $W_{\rm b}$ wires and "
    r"a complex network over $\mathbb Z[i,1/2]$ with $W_{\rm c}$ wires, each exchange two "
    r"banks of $N$ values with prescribed signs and restore every scratch wire, and admit "
    r"frames whose edge changes need $s<Wm$ smaller calls in total, with $m=h^3=10^6$; "
    r"quantitatively $s/W<m^{1-2^{-50}}$ for both.",
    r"Build the scalar exchange network, show that a frame common to all wires at a gate "
    r"commutes with the pointwise gate, attach nested subspace labels built from "
    r"three-element subsets and count their dimension changes, then turn labels into frames: "
    r"projection-matrix address shears for the bit network and phase operators for the "
    r"complex network.",
    mot(
        r"A gate acts pointwise, so a representation common to all its wires does not disturb "
        r"it; the representation may then change along each wire, and subspace labels choose "
        r"those changes so that each costs few smaller calls.",
        "explicit",
        X("When the values are replaced by arrays, a common representation", "that make changes of representation cheap."),
    ),
    [network, frames, rank_saving, bit_network, phase_network, explicit_exponents],
    frm=["matrix-basics", "boolean-gates-and-circuits", "vectors-matrices-and-linear-maps"],
    adds=[
        add("h", "ground-set size", "The size, 100, of the ground set whose three-element subsets index the data.", "count"),
        add("N", "bank size", "The number of values in each of the two data banks, one for each triple of three-element subsets.", "count"),
    ],
)

# ---------------------------------------------------------------- Section 4: interchange

lower_triangular = show(
    r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with "
    r"$E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly "
    r"$a$ ones (a Bruhat factorization with coordinate order reversed).",
    r"Eliminate from the topmost nonzero row at its rightmost nonzero entry, clearing the row "
    r"to the left by lower-triangular column operations and the column below by "
    r"lower-triangular row operations, and repeat on the remaining indices.",
    mot(
        r"Choosing the topmost row and its rightmost entry means all clearing goes leftward and "
        r"downward, so every elementary operation is lower triangular in the original order.",
        "recoverable",
    ),
    [
        infer(
            r"At the topmost nonzero row's rightmost nonzero entry, the entries to its left are "
            r"cleared by right multiplication and those below by left multiplication with lower "
            r"triangular elementary matrices, since rows above are zero in the active columns.",
            X("Otherwise choose the topmost", "were zero in the still active columns."),
        ),
        infer(
            r"Each pivot isolates a rank-one block, so the resulting $LAR=\Pi$ has exactly $a$ "
            r"ones, and $E_1=L^{-1}$, $E_2=R^{-1}$ are invertible lower triangular.",
            X("Each step isolates a rank-one block", "have the required form."),
        ),
    ],
    page="lower-triangular",
    frm=["matrix-basics", "vectors-matrices-and-linear-maps"],
)

matrix_shear = show(
    r"For a fixed finite set of rational $m\times m$ matrices there is a fixed odd prime $q$ "
    r"such that, for fields over $[q^b]$ with every $H_i$ before every $D_j$, the permutation "
    r"$(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ with $\operatorname{rank}_{\mathbb Q}A=a$ "
    r"takes exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
    r"Factor $A=E_1\Pi E_2$ once and for all, pick $q$ avoiding all denominators and diagonal "
    r"numerators, perform the triangular parts as controlled updates of later fields by "
    r"earlier ones, and realize each one of $\Pi$ by two such updates around one interchange.",
    mot(
        r"Controlled shifts update a later field from earlier ones in linear time, and "
        r"lower-triangular coordinate changes only ever update in that direction, so all of a "
        r"shear except its rank-many pivots is linear-time work.",
        "explicit",
        X("Lemma~\\ref{lem:ordered-affine-streams} updates a later field using earlier fields", "can be performed entirely in this direction."),
    ),
    [
        lower_triangular,
        infer(
            r"A lower-triangular transformation of $H$ or $D$ costs $O(V)$: update coordinates in "
            r"descending physical order, multiplying by the diagonal unit and adding a fixed "
            r"combination of earlier coordinates, which still hold their original values.",
            X("A lower triangular transformation of $H$, or of $D$, costs $O(V)$:", "in descending physical order."),
        ),
        infer(
            r"Each one of $\Pi$ at $(i,j)$, i.e. $H_i\gets H_i+D_j$, is done as "
            r"$D_j\gets D_j+H_i$, $(H_i,D_j)\gets(D_j,H_i)$, $D_j\gets H_i-D_j$, taking $(h,d)$ "
            r"to $(h+d,d)$ with one interchange, so the shear uses exactly $a$ interchanges.",
            X("On an initial pair $(h,d)$ this sequence yields $(h+d,d)$.", "which proves the claim."),
        ),
    ],
    page="matrix-shear",
    frm=["controlled-shifts", "modular-arithmetic", "primes-coprimality-and-gcd"],
)

recurrence = show(
    r"The procedure makes exactly $s$ recursive calls, each on a role stream of volume $V/W$ "
    r"with chunks $m$ times narrower, plus $O(V)$ other work, so the normalized cost obeys "
    r"$F_0=O(1)$, $F_k\le(s/W)F_{k-1}+O(1)$, and $s/W<m^\tau$ gives $F_k=O(e^\tau)$ for $e=m^k$.",
    r"Count the recursive calls as the sum of edge ranks, divide time by logical volume, and "
    r"sum the resulting geometric series.",
    mot(
        r"Dividing cost by volume turns $s$ children of volume $V/W$ into the factor $s/W$, "
        r"which is below $m^\tau$; a geometric series with that ratio is dominated by "
        r"$m^{k\tau}=e^\tau$ (or by $k+1$ when the ratio is at most one).",
        "explicit",
        X("A recursive call at parameter $mf$ therefore uses $s$ calls at parameter", "each on a stream of volume $V/W$."),
    ),
    [
        infer(
            r"The number of recursive calls is the sum $s$ of the edge ranks, and each acts on one "
            r"role stream of volume $V/W$ with all other fields as spectators.",
            X("The number of recursive calls is the sum of the edge ranks, exactly $s$.", "retaining all other fields as spectators."),
        ),
        infer(
            r"With ratio $s/W<m^\tau$, $\sum_{j\le k}(s/W)^j$ is $k+1=O(m^{k\tau})$ when "
            r"$s/W\le1$ and $O((s/W)^k)$ otherwise, so $F_k=O(m^{k\tau})=O(e^\tau)$.",
            X("For $a=s/W<m^\\tau$ the geometric sum", "Hence $F_k=O(e^\\tau)$."),
        ),
    ],
    page="power-saving-recurrence",
    frm=["rank-saving", "bit-network", "big-o", "proof-by-induction-and-recursion", "logarithms-and-exponentials"],
    salient=r"Each level multiplies the chunk width by $m$ but the normalized cost only by "
            r"$s/W<m^\tau$, so the cost grows like $e^\tau$ with $\tau<1$ rather than linearly "
            r"in the width.",
    adds=[add("F_k", "normalized cost", "A uniform bound on running time divided by logical volume for chunks of m^k digits.", "direct")],
)

power_interchange = show(
    r"For a fixed circuit with $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$ and $s<Wm$ "
    r"and a rational $\tau$ with $s/W<m^\tau$, two disjoint chunks of $e=m^k$ radix-$q$ digits "
    r"can be interchanged in $O(Ve^\tau)$ time whenever a row field before both chunks has "
    r"length divisible by $W^k$.",
    r"Write each chunk as $m$ fields of $e/m$ digits ($H$ and $D$), split rows cyclically "
    r"into $W$ role streams, run the bit network with frames $\Phi_{M_v}$ so that each edge is "
    r"a matrix shear done by recursive interchanges of smaller fields, merge to get "
    r"$H\gets H+D$ on every row, compose three shears into the interchange, and solve the "
    r"volume-normalized recurrence.",
    mot(
        r"Each edge matrix of rank $a$ costs $a$ smaller interchanges, and the ranks sum to "
        r"less than $W$ times $m$, so the recurrence saves a power of the chunk width.",
        "explicit",
        X("Because the sum of these ranks is less than the number of wires times", "saves a power of the chunk width."),
    ),
    [
        matrix_shear,
        infer(
            r"The bit network supplies the required finite data: $W=W_{\rm b}$ wires, terminal "
            r"and gate matrices with $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$, and "
            r"edge-rank sum $s=s_{\rm b}<Wm$ with the negative source projections counted.",
            X("Proposition~\\ref{prop:bit-motif-interface} supplies these conditions", "has already been included in the rank sum."),
        ),
        infer(
            r"Splitting whole rows cyclically within each prefix, row $Wg+(w-1)$ going to role "
            r"stream $w$ as row $g$, gives $W$ streams of identical shape, each of volume $V/W$ "
            r"with row count divisible by $W^{k-1}$.",
            X("These streams have exactly the same remaining shape,", "its row count is divisible by $W^{k-1}$."),
        ),
        infer(
            r"Each circuit edge applies $\Phi_{A_e}$, $A_e=M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)}$, "
            r"to its role stream by the matrix-shear lemma with recursive interchanges of the "
            r"pivot pairs of $(e/m)$-digit fields, and each gate acts pointwise at matching addresses.",
            X("On every circuit edge apply $\\Phi_{A_e}$ to that role stream;", "of $b$-digit fields."),
        ),
        infer(
            r"A common address permutation commutes with pointwise bit gates, so the frame "
            r"identity gives $f'_{\rho(w)}=\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$ "
            r"on every role.",
            X("The same invariant proof applies", "commutes with every pointwise bit gate."),
        ),
        infer(
            r"Merging row $g$ of output role $\rho(w)$ back to row $Wg+(w-1)$ undoes $\rho$ and "
            r"yields $H\gets H+D$ on every original row, including rows that served as scratch "
            r"with arbitrary values.",
            X("The result is $H\\leftarrow H+D$ on every original row,", "whose initial values were arbitrary."),
        ),
        infer(
            r"The componentwise updates $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ send $(H,D)$ to "
            r"$(D,H)$; only the middle shear uses the circuit, the other two update the later "
            r"group in linear time.",
            X("Only the middle shear uses the circuit.", "The transformation sends $(H,D)$ to $(D,H)$."),
        ),
        recurrence,
        infer(
            r"On fixed tapes, parking the $W-1$ inactive streams on a stack, copying the active "
            r"one to the child and restoring afterwards moves $O(V)$ symbols per child, and there "
            r"are only $s$ children, so scheduling adds $O(V)$ per node and no factor to $s/W$.",
            X("Each push, pop, copy, positioning operation, or erasure moves $O(V)$", "the fixed number $s$ of child calls."),
        ),
    ],
    page="power-interchange",
    frm=["bit-network", "frames", "stream-ops", "controlled-shifts"],
)

chunk_interchange = show(
    r"One fixed-tape procedure transforms any bit array on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ "
    r"by exchanging its two $u$-bit address coordinates while fixing the prefix, gap and "
    r"suffix coordinates, in $O(Vu^\tau)$ steps with $\tau=1-2^{-50}$, for arbitrary prefix, "
    r"gap and suffix lengths, padding and cleanup included.",
    r"Pad the chunks numerically to radix-$q$ ranges $[q^e]$, supply a row field from the top "
    r"$O(\log e)$ digits of both chunks and pad its count to a multiple of $W^k$, write the "
    r"remaining width in base $m$ and interchange corresponding pieces by the power-width "
    r"procedure, then undo the joins and the padding.",
    mot(
        r"The power-width procedure needs widths that are powers of $m$ and a row field "
        r"divisible by $W^k$; a few high digits of the chunks supply the rows cheaply, and a "
        r"base-$m$ split of the width makes the piece costs a geometric sum.",
        "explicit",
        X("Rows for a general array can be supplied by a few of its own high digits.", "Their movement will cost less than the final bound."),
    ),
    [
        power_interchange,
        infer(
            r"For chunks of $e$ radix-$q$ digits, interchanging the top "
            r"$\lceil k\log W/(2\log q)\rceil=O(\log e)$ digits pairwise and joining them gives a "
            r"row field of range at least $W^k$ before both remaining chunks, at cost "
            r"$O(V\log e)$; zero rows pad its count to a multiple of $W^k$, less than doubling the volume.",
            X("The joining moves preserve the order of the remaining digits", "costs $O(V\\rho)$ by Lemma~\\ref{lem:elementary-streams}."),
        ),
        infer(
            r"Writing the remaining width as $\sum_{j\le k}a_jm^j$ with $0\le a_j<m$ and "
            r"interchanging the $a_j$ pairs of width-$m^j$ pieces on the common padded row field "
            r"costs $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, a geometric sum since $a_j<m$ and "
            r"$m^k<me$, and each call preserves row addresses so padded rows stay zero.",
            X("The fixed bound $a_j<m$ and the inequality $m^k<me$", "geometric sum of the stated order."),
        ),
        infer(
            r"Binary chunks of $u$ bits are padded numerically to $[q^e]$ with $q^e\ge2^u$ (a "
            r"fixed factor below $q^2$ in volume), which keeps entry order because radix-$q$ "
            r"lexicographic order is numerical order; invalid entries are scanned away after the "
            r"interchange, and $e=O(u)$ gives $O(Vu^\tau)$.",
            X("Lexicographic radix-$q$ order of $[q^e]$ is its numerical order,", "the bound is $O(Vu^\\tau)$."),
        ),
    ],
    page="chunk-interchange",
    frm=["stream-ops", "controlled-shifts", "array-order", "fixed-tape-model"],
    adds=[
        add("e", "chunk digit width", "The number of radix-q digits in each of the two chunks being interchanged.", "count"),
        add("k", "recursion depth", "The number of recursion levels, the exponent with e equal to m to the power k.", "count"),
    ],
    salient=r"The final effect is an exact permutation, valid for arbitrary initial auxiliary "
            r"values, although intermediate steps form XOR combinations of data, and it costs "
            r"$O(Vu^\tau)$ rather than the $\Theta(Vu)$ of moving one digit at a time.",
)

# ---------------------------------------------------------------- Section 5: layers

phase_frames = show(
    r"On a group of $e=mf$ selected chunks arranged as $m$ slots of $f$ chunks, the complex "
    r"network with column frames $\mathcal C_U^{\otimes f}$ yields $C^{\otimes e}$ on every "
    r"role using exactly $s_{\rm c}$ child calls $C^{\otimes f}$ on single slots, a fixed "
    r"number of binary row additions and coefficientwise scalar operations, and "
    r"$H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with exact Gaussian dyadic phases.",
    r"Conjugate each edge's directional kernels into coordinate directions by an address "
    r"permutation $\mathcal P_M$ whose matrix extends the residual basis, run one child per "
    r"direction on one slot, realize inverse kernels and endpoint corrections by signs and "
    r"fourth-root phases, and convert $C$ to $H_0$ by diagonal phases.",
    mot(
        r"A child call acts on whole slots of coordinate bits, so each residual direction must "
        r"first be moved into a coordinate position; an invertible binary change of basis does "
        r"this without a general transpose.",
        "explicit",
        Q("The next step puts those directions into coordinate positions without performing a general transpose."),
    ),
    [
        infer(
            r"Taking a basis extending the residual basis as the columns of $M$ gives "
            r"$\mathcal C_{U_+}\mathcal C_{U_-}^{-1}=\mathcal P_M(\prod_jC_{e_j}^{\epsilon_j})\mathcal P_M^{-1}$, "
            r"which uses only $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$ and the invertibility of $M$.",
            X("The matrix $M$ need not preserve the dot product:", "only uses its invertibility."),
        ),
        infer(
            r"An inverse kernel needs one forward child, since "
            r"$(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ with address "
            r"signs and fourth-root phases as wrappers.",
            X("A negative directional kernel still requires only one forward child", "so they add no recursive calls."),
        ),
        infer(
            r"Each $\mathcal P_M$ is at most $m(m-1)+3m$ row additions, each XORing the selected "
            r"bits of one whole slot into the corresponding bits of another.",
            X("Gaussian elimination expresses any", "positions in two whole slots."),
        ),
        infer(
            r"Summing residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f$ "
            r"chunks of one slot, and the phase interface gives $C^{\otimes e}$ on every role.",
            X("Summing its residual dimensions gives exactly $s_{\\rm c}$ child calls,", "of one slot."),
        ),
        infer(
            r"Since $H_0=b\mathsf SC\mathsf S$ with $\mathsf S=\operatorname{diag}(1,i)$, "
            r"$H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, and "
            r"$b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ is a binary shift and a fourth-root "
            r"phase with at most one further factor $b$.",
            X("The scalar is \\[ b^D=", "with at most one further factor $b$."),
        ),
    ],
    frm=["phase-network", "binary-field-f2-and-xor", "butterfly-fft", "complex-numbers"],
)

packed_bit_addition = show(
    r"For $R$-bit records on $[N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2}\times[N_2]\times[2^L]_{\chi_3}\times[N_3]$ "
    r"with $L=fK$, one fixed procedure performs $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ at the "
    r"selected positions $j_i=\rho+iK$, $0\le i<f$, restoring the scratch chunk $z$ for every "
    r"initial value, in $O(V(L^\tau+1))$ time when $R$ exceeds every fixed polynomial in $p$ "
    r"and $K/\log p\to\infty$.",
    r"Apply eight cyclic shifts of whole chunk ranges, each adding to all $K$-bit segments at "
    r"once, which flip the parity of each $y$ segment exactly when its control bit is one and "
    r"restore $z$; they agree with the ideal XOR map off an explicit set $\mathcal B$ of "
    r"addresses with extreme guard values, which is then repaired by extracting, sorting and "
    r"reinserting those records.",
    mot(
        r"A shift of a whole chunk range adds to every segment of the chunk at once, so packed "
        r"integer additions handle all selected bits together; carries between segments occur "
        r"only at addresses with extreme guard values, few enough when $K/\log p\to\infty$ to "
        r"repair by sorting.",
        "explicit",
        X("Also $K/\\log p\\to\\infty$, which will make the exceptional set", "small enough to repair by sorting."),
    ),
    [
        infer(
            r"For a control $c$ and integers $u,w$, the eight conditional $\pm1$ updates induce "
            r"$(00\ 01\ 10)$ and then $(01\ 10\ 11)$ on parity squares, composing to "
            r"$(00\ 10)(01\ 11)$, i.e. $(u',w')=(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips "
            r"exactly when $c=1$, both quotients by two are kept and $w$ is restored.",
            Q("Applying the first cycle and then the second gives $(00\\ 10)(01\\ 11)$."),
        ),
        infer(
            r"Applied to the $K$-bit segments starting at $j_0,\dots,j_{f-2}$, each line is one "
            r"cyclic shift $y\gets y+\varepsilon\sum_i2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^L}$ "
            r"whose offset does not depend on its target, hence a bijection of the rectangle.",
            X("Physically, a line updating $y$ by sign $\\varepsilon$", "so each line is a bijection of the rectangle."),
        ),
        infer(
            r"Off the set $\mathcal B$ of addresses where some used guard value fails "
            r"$10\le g\le2^{K-1}-11$, each segment starts in $[20,2^K-21]$ and moves by at most "
            r"eight, so no segment carries into the next and the composition $S_0$ agrees with "
            r"the ideal XOR map $T_0$.",
            X("Inductively, each packed addition therefore agrees", "borrows from the next segment."),
        ),
        infer(
            r"Each guard excludes exactly twenty of its $2^{K-1}$ values, so a union bound over "
            r"the $2(f-1)$ guards gives $|\mathcal B|\le\min\{1,80(f-1)2^{-K}\}M$, whatever the "
            r"record payloads.",
            X("There are exactly twenty excluded values for each guard", "|\\mathcal B|\\le\\delta_{\\rm bad}M."),
        ),
        infer(
            r"Since $T_0$ preserves guard values, $S_0$ and $T_0$ are bijections agreeing off "
            r"$\mathcal B$, so $T_0S_0^{-1}$ fixes the complement of $\mathcal B$ and permutes "
            r"$\mathcal B$; the exceptional records are extracted with their destination ranks, "
            r"radix sorted and reinserted.",
            X("Thus $T_0S_0^{-1}$ fixes $\\mathcal B^c$ and permutes $\\mathcal B$.", "on tapes."),
        ),
        infer(
            r"The omitted top position $j_{f-1}$ is one two-bit XOR in $O(V)$, and for $f=1$ "
            r"this is the whole algorithm.",
            X("Finally apply the two-bit XOR to $x_{j_{f-1}},y_{j_{f-1}}$", "step is the entire algorithm."),
        ),
        infer(
            r"The shifts cost $O(V(L^\tau+1))$ through at most sixteen interchanges and eight "
            r"rotations, and with $A=\lceil\log_2(2V)\rceil=O(p)$ the repair terms per unit "
            r"volume, $A^3/R$ and $80(f-1)2^{-K}A(1+A/R)$, tend to zero under the family bounds.",
            X("Under the stated family bounds the first tends to zero,", "This proves the final assertion."),
        ),
    ],
    page="packed-bit-addition",
    frm=["chunk-interchange", "controlled-shifts", "stream-ops", "binary-field-f2-and-xor", "modular-arithmetic"],
    salient=r"Eight cyclic shifts, each a bijection, net to flipping the parity of $u$ exactly "
            r"when $c=1$ while restoring the arbitrary scratch integer $w$, and the repair "
            r"depends only on addresses, so the bound is worst case over all payloads.",
)

basis_change = infer(
    r"A row addition of a binary change of basis is one packed selected-bit addition with slot "
    r"$h'$ as $x$, slot $h$ as $y$ and a third slot as $z$, so a whole change of basis and its "
    r"inverse on a stream of volume $V$ cost $O(V((eK)^\tau+1))$.",
    X("To add row $h'$ to row $h$, use slot $h'$ as $x$,", "whatever its initial address value."),
)

batching = show(
    r"With rows supplied by the first chunks and split among the $W$ roles, the normalized "
    r"cost $F(e)$ of $C^{\otimes e}$ obeys $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ for $e\ge d^{1/2}$ "
    r"and $F(e)=O(e)$ below, which over the base-$m$ pieces of the active chunks gives "
    r"$O(d^{\lambda'})$ for any fixed $\lambda'$ with "
    r"$\max\{\lambda,\sigma+(1-\sigma)/2\}<\lambda'<1$.",
    r"Charge each internal node its basis changes, gates and corrections, give each of its $s$ "
    r"children $1/W$ of the volume, stop with individual kernels when fewer than $d^{1/2}$ "
    r"chunks remain, and sum internal and leaf contributions.",
    mot(
        r"Splitting complete rows among the wire roles divides each recursive call's volume by "
        r"$W$, which turns the $s$ children into the factor $s/W\le m^\sigma$ per level.",
        "explicit",
        X("Splitting complete rows among", "reduces the volume of each recursive call."),
    ),
    [
        infer(
            r"One kernel $C(u,v)=((u+v+i(u-v))/2,(u+v-i(u-v))/2)$ at a selected bit is a split, "
            r"an exact paired coefficient scan and a merge, $O(V)$, so $e$ individual kernels "
            r"cost $O(Ve)$.",
            X("Thus \\(e\\) individual kernels cost", "with these complete ranges and record format."),
        ),
        infer(
            r"An internal node with $e=m^k$ chunks makes exactly $s$ calls on slots, one per "
            r"residual basis vector, and its other work costs $O(V((eK)^\tau+1))$.",
            X("The phase construction supplies one recursive call on a slot", "in one invocation of the network."),
        ),
        infer(
            r"After individual kernels on the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ "
            r"chunks, their bits form a row index of range $2^{q_0K}\ge W^{\lceil\log_md\rceil}$, "
            r"padded with zero rows to a multiple of that power at most doubling the volume.",
            X("Its range has length", "\\(q_0K\\ge k_0\\log_2W\\)."),
        ),
        infer(
            r"Sending row $Wg+w$ to role $w$ gives role streams of identical shape, so pointwise "
            r"gates align, existing rows supply the scratch roles, and each child has exactly "
            r"$1/W$ of its parent's volume.",
            X("Each recursive edge call acts on", "of its parent's logical volume."),
        ),
        infer(
            r"The $s$ children on volume $V/W$ cost $s(V/W)F(e/m)$, giving the factor $s/W$, and "
            r"at internal nodes $K\le e^{2c}$ makes the overhead $O(e^\lambda)$.",
            X("Indeed, the \\(s\\) child calls are executed on streams of volume", "\\(s(V/W)F(e/m)\\)."),
        ),
        infer(
            r"Since $s/W\le m^\sigma<m^\lambda$, the internal costs sum to $O(e^\lambda)$ as a "
            r"geometric series, and leaves after $j$ levels with $u<d^{1/2}$ chunks contribute "
            r"$O((s/W)^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{(1-\sigma)/2})$.",
            X("Put \\(a=s/W\\).", "=O(e^\\lambda)."),
        ),
        infer(
            r"Splitting the $D-q_0$ remaining chunks into base-$m$ pieces of $m^j$ chunks, at most "
            r"$(m-1)(1+\lfloor\log_md\rfloor)$ of them, and adding the row preprocessing gives "
            r"$O(\log(2d)[d^\lambda+d^{\sigma+(1-\sigma)/2}+1])=O(d^{\lambda'})$.",
            X("Write \\(D-q_0=\\sum_j a_jm^j\\) in base \\(m\\)", "pieces."),
        ),
    ],
    frm=["power-saving-recurrence", "stream-ops", "proof-by-induction-and-recursion"],
)

guard_width = show(
    r"Every intermediate coefficient of one layer is an exact Gaussian dyadic whose "
    r"denominator and magnitude growth are bounded by $\Delta=\lceil C_0d^{C_1}\rceil$ with "
    r"$C_0=128m(s+64(W+m+1)^3)^2$ and $C_1=20$, so $p+\Delta$ fractional and $\Delta+3$ "
    r"integer bits represent the whole layer "
    r"exactly, and $\epsilon C_1<1$ makes $\Delta=o(p)$ and the width $O(p)$.",
    r"Bound the arithmetic dependency depth by $A(e)\le sA(e/m)+E$ at internal nodes and "
    r"$A(e)\le8e$ at leaves, add the outer phases and the final shift, and note that each "
    r"operation at most doubles the modulus and adds one denominator bit.",
    mot(
        r"The intermediate network operators are not contractions, so instead of truncating "
        r"along the way the whole layer is evaluated exactly, which requires a bound on the "
        r"growth of denominators and magnitudes.",
        "explicit",
        X("The accelerated network is evaluated exactly until an entire", "need not be contractions."),
    ),
    [
        infer(
            r"One invocation adds fewer than $E=64(W+m+1)^3$ operations to any dependency chain "
            r"(at most $12W$ gates of at most $2W^2$ operations, plus child and endpoint "
            r"corrections), so $A(e)\le sA(e/m)+E$ and, through $\lceil\log_md\rceil$ levels, "
            r"$A(e)\le8B^2d^{\nu+1}$ with $B=s+E$ and $\nu$ the least $j$ with $m^j\ge B$.",
            X("Since \\(s<Wm\\), the total", "\\(E=64(W+m+1)^3\\)."),
        ),
        infer(
            r"A value at depth $t$ lies in $2^{-(p+t)}\mathbb Z[i]$ with modulus at most $2^t$, "
            r"since addition at most doubles the modulus, halving adds one denominator bit, and "
            r"signs and multiplication by $i$ change neither.",
            X("This follows by induction: addition or subtraction", "preserve both bounds."),
        ),
        infer(
            r"With $\epsilon C_1<1$ and $d=\Theta(p^\epsilon)$, $\Delta=o(p)$, so the full "
            r"coefficient width is $O(p)$ as the time analysis assumes.",
            X("Choose \\(\\epsilon C_1<1\\).", "as required in the time analysis."),
        ),
    ],
    frm=["fixed-point-disk-grid", "dyadic-rationals-and-binary-fractions", "complex-numbers"],
)

simultaneous_layer = show(
    r"For large $p$, $d=\Theta(p^\epsilon)$, $K=\lfloor d^c\rfloor$ and $r=2^{\Theta(p/d)}$, one "
    r"fixed-tape procedure applies the tensor product $\mathcal H$ of "
    r"$H_0(u,v)=((u+v)/2,(u-v)/2)$ at bit $\rho$ of each of $D\le d$ consecutive $K$-bit "
    r"address chunks to arrays of $r$-coefficient disk-grid polynomial records, returning "
    r"$Q_p(\mathcal Hz)$, within $\sqrt2\,2^{-p}$ of $\mathcal Hz$, in $O(Vd^{\lambda'})$ time, "
    r"exact before one final truncation.",
    r"Express $C^{\otimes e}$ through the complex network's phase frames on $m$ slots with each "
    r"edge a binary basis change around smaller calls, implement basis changes by packed "
    r"selected-bit additions, supply rows from the first chunks and split them among the $W$ "
    r"roles, solve the recurrence, bound the exact dyadic growth, and convert "
    r"$C^{\otimes D}$ to $H_0^{\otimes D}$ by diagonal phases and a scale.",
    mot(
        r"Applying the $D$ butterfly factors separately would cost $D$ whole-array passes; the "
        r"network processes all selected bits together with a power saving.",
        "explicit",
        X("We will obtain cost $O(Vd^{\\lambda'})$, with", "would require $D$ whole-array passes."),
    ),
    [
        phase_frames,
        packed_bit_addition,
        basis_change,
        batching,
        guard_width,
        infer(
            r"With $d,r$ in fixed bands, $K\ge6$, $K/\log p\to\infty$ and $r$ exceeds every fixed "
            r"power of $p$, so every packed call meets its family bounds with one common time constant.",
            X("Thus Lemma~\\ref{lem:packed-selected-bit-rectangle} has the required", "with one common time constant."),
        ),
        infer(
            r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk "
            r"arrays to disk arrays, and the single final truncation toward zero keeps the disk "
            r"and adds error below $\sqrt2\,2^{-p}$.",
            X("Thus $\\mathcal H$ maps disk arrays to disk", "changes each by less than $2^{-p}$."),
        ),
    ],
    page="simultaneous-layer",
    frm=["phase-network", "packed-bit-addition", "power-saving-recurrence", "butterfly-fft",
         "fixed-point-disk-grid", "chunk-interchange", "polynomial-ring-mod"],
    adds=[
        add("e", "group chunk count", "The number of selected chunks handled by one recursive call of the layer construction.", "count"),
        add("D", "active chunk count", "The number of consecutive chunks whose selected bits one layer transforms, at most d.", "count"),
        add("f", "slot width", "The number of chunks in one slot, equal to the number of selected bits one child call or one packed addition handles.", "count"),
        add("C", "two-point phase kernel", "The two-by-two matrix aI+bX with a=(1+i)/2 and b=(1-i)/2 given by the complex network's phase interface.", "direct"),
        add(r"\mathcal H", "butterfly layer", "The tensor product of the normalized butterfly over the selected bits, acting coefficientwise on the records.", "direct"),
    ],
)

procedures = show(
    r"Two fixed-tape procedures run with a power saving: interchanging two disjoint $u$-bit "
    r"address chunks of an array of volume $V$ costs $O(Vu^\tau)$, and applying the normalized "
    r"butterfly at one selected bit of each of at most $d$ address chunks of polynomial "
    r"records costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$.",
    r"Derive each procedure from its own fixed linear network that exchanges two banks of "
    r"values and restores every scratch value: split array rows cyclically among the $W$ wire "
    r"roles, give each vertex a frame so that the endpoint effect is the wanted operator and "
    r"each edge is a few smaller calls of the same procedure, and solve the resulting "
    r"volume-normalized recurrence.",
    mot(
        r"With rows split among $W$ roles, a call at parameter $mf$ makes $s$ calls at "
        r"parameter $f$ on streams of volume $V/W$, so per unit volume the cost grows by "
        r"$s/W$ when the parameter grows by $m$; a network with $s<Wm$ gives an exponent below one.",
        "explicit",
        X("After dividing cost by volume, multiplying the parameter by $m$", "is the source of the power saving."),
    ),
    [stream_ops, controlled_shifts, networks, chunk_interchange, simultaneous_layer],
    frm=["fixed-tape-model", "array-order", "big-o"],
    salient=r"Both costs have exponents strictly below one in the parameter, $u^\tau$ and "
            r"$d^{\lambda'}$, where moving $u$ digits one at a time or applying $D$ butterfly "
            r"factors separately would cost a full pass per digit or factor.",
    adds=[
        add("u", "chunk width", "The number of bits in each of the two address chunks being interchanged.", "count"),
        add(r"\sigma", "layer recursion exponent", "The fixed exponent 1-2^{-50}, at least the base-m logarithm of s/W for the complex network.", "direct"),
        add("W", "wire count", "The total number of wires of the network in use, data and scratch together.", "count"),
        add("m", "label dimension", "The dimension of the label space, and the factor by which a recursive call's parameter shrinks.", "count"),
        add("s", "smaller-call count", "The total number of smaller calls of the same procedure needed by all edge frame changes of a network.", "count"),
        add("q", "digit radix", "The fixed radix of the address digits being moved, an odd prime for interchanges.", "direct"),
    ],
)

# =====================================================================================
# Part 2. The multiplication reduction (Sections 6-9)
# =====================================================================================

synthetic_transform = show(
    r"With $\omega_t=y^{2r/t}$ in $\mathcal R_r=\mathbb C[y]/(y^r+1)$, the normalized "
    r"transforms $F_t^\pm$ are contractions with $F_t^+F_t^-=t^{-1}I$, the "
    r"decimation-in-frequency recursion computes $B_tF_t^-$ with outputs in bit-reversed "
    r"slots, the reversed recursion computes $F_t^+B_t^{-1}$, and on several axes each round "
    r"is a parallel butterfly followed by one address-determined monomial $y^E$.",
    r"Verify character cancellation directly in a ring with zero divisors, follow the "
    r"address-bit slots through the decimation-in-frequency recursion (butterfly $H_0$, then "
    r"twiddle $\omega_t^{-k}$ on one branch), and invert the levels using $H_0^2=I/2$.",
    mot(
        r"In $\mathcal R_r$ the roots of unity are powers of $y$, which act by exact signed "
        r"permutations of coefficient lists, so twiddles cost no arithmetic and only the "
        r"butterflies do.",
        "explicit",
        X("Their entries will be short polynomials in a quotient", "act by exact signed permutations of coefficient lists."),
    ),
    [
        infer(
            r"Every power of $\omega_t$ is an isometry of the coefficient sup norm and each "
            r"transform entry averages $t$ such images, so $F_t^-$ and $F_t^+$ are contractions.",
            X("Every power of $\\omega_t$ is an isometry,", "Thus both transforms are contractions."),
        ),
        infer(
            r"$\sum_k\omega_t^{jk}$ is $t$ if $t\mid j$ and $0$ otherwise, because shifting $k$ "
            r"by $t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$ and the additive group has no "
            r"two-torsion; hence $F_t^+F_t^-=t^{-1}I$.",
            X("Replacing $k$ by $k+t/2^{v+1}$ modulo $t$", "has no two-torsion."),
        ),
        infer(
            r"After all $\log_2t$ levels the entry $(F_t^-z)_j$ sits in slot "
            r"$\operatorname{rev}(j)$, so the recursion computes $B_tF_t^-$ without moving whole "
            r"frequency indices.",
            X("If $\\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$,", "occupies slot $\\operatorname{rev}_a(j)$."),
        ),
        infer(
            r"The reversed level is half the inverse of the forward level, so the reverse "
            r"procedure composed with $B_tF_t^-$ is $I/t$, as is $F_t^+B_t^{-1}$, and the reverse "
            r"procedure computes $F_t^+B_t^{-1}$.",
            X("As $H_0^2=I/2$, the reversed level is half the inverse", "of the corresponding forward level."),
        ),
        infer(
            r"On several axes a twiddle depends only on its own axis's address bits, so a round "
            r"is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $J_E$, "
            r"multiplication by $y^E$, and every completed round is a contraction.",
            X("Consequently the individual axis steps may be grouped", "one recordwise monomial operation $J_E$."),
        ),
    ],
    page="synthetic-transform",
    frm=["polynomial-ring-mod", "butterfly-fft", "dft", "multidim-transform", "vector-norms-and-error-bounds"],
    salient=r"All roots of unity are exact: multiplying by a power of $\omega_t$ is a signed "
            r"cyclic shift of the coefficient list, so the butterflies are the only arithmetic, "
            r"and outputs land in bit-reversed order without moving any frequency index.",
)

transform_layout = show(
    r"For $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ with records in $\mathcal R_r$, "
    r"a fixed-tape forward procedure with exact counterpart $LBF_{\boldsymbol t}^-$ and an "
    r"opposite procedure consuming that order with exact counterpart "
    r"$F_{\boldsymbol t}^+B^{-1}L^{-1}$ ($B$ the bit-reversal order, $L$ a layout "
    r"permutation) each have error below $\sqrt2\ell\,2^{-p}$ and cost "
    r"$O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
    r"Move the leading slot of each long axis and the lowest $(\ell-1)\bmod K$ slots of every "
    r"axis to a prefix, interchange the remaining $K$-bit chunks into chunk-index-major order, "
    r"run each round on the remaining chunks as one simultaneous layer followed by an exact "
    r"monomial twiddle, process prefix rounds individually, and truncate once per round.",
    mot(
        r"A simultaneous layer needs the selected bits of all participating axes at a common "
        r"offset in consecutive $K$-bit chunks, which the layout provides once for all rounds.",
        "explicit",
        X("To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round,", "in consecutive $K$-bit chunks."),
    ),
    [
        synthetic_transform,
        infer(
            r"Moving each long axis's leading slot and the lowest $(\ell-1)\bmod K$ slots of every "
            r"axis to a prefix costs $O(TpdK)$ and leaves each axis as consecutive $K$-bit chunks.",
            X("There are at most $D(b+1)=O(dK)$ listed slots,", "so the moves cost $O(TpdK)$."),
        ),
        infer(
            r"Reordering the remaining chunks from axis-major to chunk-index-major takes "
            r"$O(p/K)$ interchanges of $K$-bit chunks, since $d\ell=O(p)$, at $O(TpK^\tau)$ each, "
            r"$O(Tp\cdot pK^{\tau-1})$ in all, and these moves define $L$.",
            X("This uses at most $Dq-1$ exchanges of width-$K$ address chunks,", "even when the chunks are nonadjacent."),
        ),
        infer(
            r"In a round on the remaining chunks the selected bit has one common offset in each "
            r"of the $D$ consecutive chunks of one chunk index over the complete address set, so "
            r"the round is one simultaneous layer costing $O(Tpd^{\lambda'})$, "
            r"$O(Tp\ell d^{\lambda'})$ over all rounds.",
            X("The simultaneous-layer procedure therefore applies at cost", "$O(Tp\\ell d^{\\lambda'})$ in total."),
        ),
        infer(
            r"Rounds on prefix slots apply $H_0$ to each participating bit individually, exactly "
            r"on a slightly finer grid and truncated once per round, at $O(Tp)$ per participating "
            r"bit and $O(TpdK)$ over at most $K$ such rounds.",
            X("There are at most $b+1\\leq K$ rounds on prefix slots,", "giving cost $O(TpdK)$."),
        ),
        infer(
            r"Multiplication by $y^E$, $E=er+s$, splits the coefficient list before $r-s$, puts "
            r"the negated tail first and applies the sign $(-1)^e$, in $O(rp)$ per record with no "
            r"coefficient sort.",
            X("To implement the monomial, write $E=er+s$", "This is multiplication by $y^E$ modulo $y^r+1$."),
        ),
        infer(
            r"Truncation toward zero is odd and componentwise and $J_E$ is a signed coefficient "
            r"permutation, so $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: each round is one "
            r"truncation after an exact contraction, and $\ell$ rounds give error below "
            r"$\sqrt2\ell\,2^{-p}$.",
            X("Thus the actual forward call sequence returns exactly the result", "after the exact contraction round."),
        ),
        infer(
            r"Operating on named slots after $L$ conjugates each operation by $L$, so the forward "
            r"entry with frequency address $j$ is stored at $L(Bj)$ and the opposite arithmetic "
            r"consumes that order before $L^{-1}$ restores axis-major order.",
            X("In particular, the forward entry with frequency address $j$ is", "stored at $L(Bj)$."),
        ),
    ],
    page="transform-layout",
    frm=["simultaneous-layer", "chunk-interchange", "stream-ops", "butterfly-fft", "multidim-transform",
         "fixed-point-disk-grid", "polynomial-ring-mod"],
)

kronecker = show(
    r"For disk-grid $f,g\in\mathcal R_r$ with $r=2^\ell<2^p$, the exact Gaussian integer "
    r"numerators of $fg$ and then $Q_p(fg/r)$, a disk-grid polynomial within $\sqrt2\,2^{-p}$ "
    r"of $fg/r$, are computed in $O(rp\log(rp))$ time on fixed tapes from four products of the "
    r"established multiplier.",
    r"Write $f=2^{-p}(a+ib)$ and $g=2^{-p}(c+ie)$, evaluate $a,b,c,e$ at $B_0=2^{4p}$ as signed "
    r"integers, form the four products with the $O(N\log N)$ multiplier, extract centered "
    r"coefficients block by block, reduce modulo $y^r+1$, and truncate.",
    mot(
        r"Evaluating at a power of two far larger than every product coefficient turns a "
        r"polynomial product into one integer product whose $4p$-bit blocks determine the "
        r"coefficients, so the established fast integer multiplier does all the arithmetic.",
        "recoverable",
    ),
    [
        infer(
            r"Each evaluation $A_u=u(B_0)$ has $|A_u|<B_0^r/2$ and is formed from the coefficient "
            r"stream with a carry in $\{-1,0\}$, and the four products "
            r"$A_aA_c,A_bA_e,A_aA_e,A_bA_c$ come from the established multiplier.",
            X("Multiply the four pairs of absolute values using the established multiplier", "restore each product's sign."),
        ),
        infer(
            r"Every coefficient of the ordinary products obeys $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so "
            r"once the lower coefficients are removed the next one is the centered residue modulo $B_0$.",
            X("After the lower coefficients have been removed from an evaluation,", "by its centered residue modulo $B_0$."),
        ),
        infer(
            r"Centered extraction with a carry in $\{0,1\}$ maintains the residual identity, so "
            r"every extracted block equals the true coefficient and the final carry cancels the "
            r"sign extension.",
            X("By \\eqref{eq:packing-separation}, including the padded value", "Thus $\\widehat h_j=h_j$."),
        ),
        infer(
            r"Reducing $ac-be$ and $ae+bc$ modulo $y^r+1$ subtracts the coefficient at $j+r$ from "
            r"that at $j$, so each $H_j$ is a sum of exactly $r$ signed products, "
            r"$|H_j|\le r2^{2p}$, and $\|fg/r\|_\infty\le\|f\|_\infty\|g\|_\infty$.",
            X("Thus each resulting Gaussian integer coefficient $H_j$ is a sum of exactly", "of modulus at most $2^p$."),
        ),
        infer(
            r"Shifting by $p+\ell$ bits gives $Q_p(fg/r)$, and the four exact integer products "
            r"dominate the linear packing, extraction, wrapping and truncation costs.",
            X("Four exact integer products dominate the linear", "wrapping, and truncation costs."),
        ),
    ],
    page="kronecker-packing",
    frm=["polynomial-ring-mod", "nlogn-multiplier", "positional-number-representation-and-carries",
         "dyadic-rationals-and-binary-fractions", "complex-numbers"],
)

ring_convolution = show(
    r"Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays of $M=T/r$ "
    r"records in $\mathcal R_r$ is computed with error below $\sqrt2M(3\ell+1)2^{-p}$ in time "
    r"$O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$, by two forward synthetic transforms, "
    r"pointwise normalized ring products, and the opposite transform consuming the same stored "
    r"order, followed by an exact scale $M$.",
    r"Perform both forward transforms and keep their common stored order $LB$, multiply "
    r"corresponding records by signed packing, apply the opposite procedure to that order, "
    r"scale exactly by $M$, and compare with the exact identity through contraction bounds.",
    mot(
        r"Pointwise multiplication commutes with applying the same record permutation to both "
        r"operands, so the forward outputs can be multiplied in their stored order and passed "
        r"straight to the opposite transform, with no reordering.",
        "explicit",
        X("Pointwise multiplication commutes with applying the same record", "pass that order directly to the opposite procedure."),
    ),
    [
        transform_layout,
        kronecker,
        infer(
            r"Since $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and "
            r"$F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, two forward transforms, the pointwise "
            r"product $P(u,v)=uv/r$, the opposite transform and the scale $M$ give exactly "
            r"$(f*g)/(rM)$, and the stored order does not interfere because $LB$ permutes whole "
            r"records, so $P(LBu,LBv)=LBP(u,v)$.",
            X("Since $LB$ permutes records and leaves their polynomial suffixes", "$P(LBu,LBv)=LBP(u,v)$."),
        ),
        infer(
            r"Two forward errors below $\sqrt2\ell\,2^{-p}$, the bilinear contraction "
            r"$\|P(x,y)\|\le\|x\|\|y\|$, one product truncation and the opposite error add to "
            r"less than $\sqrt2(3\ell+1)2^{-p}$ before the exact scale by $M$.",
            X("The final exact multiplication by $M$ therefore gives error less than", "as claimed."),
        ),
        infer(
            r"The $M=T/r$ pointwise products cost $O(Tp\log(rp))$ in total, on top of the three "
            r"transform costs and a linear final scaling.",
            X("There are $M=T/r$ pointwise polynomial products.", "the last exact scaling is linear in $Tp$."),
        ),
    ],
    page="ring-convolution",
    frm=["convolution-theorem", "cyclic-convolution", "polynomial-ring-mod", "fixed-point-disk-grid",
         "vector-norms-and-error-bounds", "multidim-transform"],
)

resampling = show(
    r"For coprime $s<t$ with $t/s-1>p/\alpha^4$ and the permutations $(P_su)_j=u_{tj}$, "
    r"$(P_tv)_k=v_{-sk}$, there are contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, "
    r"computed on disk grids with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$; "
    r"tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, "
    r"$\gamma=2d\alpha^2$, with error below $dp^2$, line costs $O(dTp^{3/2+\delta}\alpha)$ and "
    r"axis movement $O(Tpd^2(1+\ell^\tau))$ in the padded box.",
    r"Use Harvey and van der Hoeven's Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ and "
    r"the near-identity $N=C\mathsf T\mathsf D$, invert $N$ by a Neumann series to get a left "
    r"inverse of $\mathsf T$, normalize the maps into contractions, keep $P_s$ and $P_t$ inside "
    r"the identity instead of sorting, and apply the one-dimensional maps line by line, "
    r"exposing axes with the chunk interchange.",
    mot(
        r"The usual implementation sorts twice on each coordinate; keeping both permutations in "
        r"the transform formula avoids executing them, since the chirp absorbs one and the "
        r"other cancels in the convolution.",
        "explicit",
        X("Its usual implementation sorts twice on each coordinate.", "compute that formula directly."),
    ),
    [
        infer(
            r"With $N=C\mathsf T\mathsf D$ selecting the coordinates nearest $tj/s$, "
            r"$\|N-I\|<2^{-\alpha^2\theta}<1/2$ because $\alpha^2\theta>p/\alpha^2>1$, so $N$ is "
            r"invertible by the Neumann series.",
            X("Thus $\\|N-I\\|<1/2$, so $N$ is invertible", "by the Neumann series."),
        ),
        infer(
            r"$\mathsf DN^{-1}C$ is a left inverse of $\mathsf T$, so "
            r"$\mathsf DN^{-1}CP_tF_t\mathsf S=P_sF_s$, and normalizing to $A=\mathsf S/2$ and "
            r"$B_0=2^{-(2\alpha^2-2)}\mathsf D\,N^{-1}C/2$ gives $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ "
            r"with contractions.",
            X("Applying this left inverse to the first identity in", "$\\mathsf D N^{-1}CP_tF_t\\mathsf S=P_sF_s$."),
        ),
        infer(
            r"The quoted arithmetic maps and the ordered selection $C$ give approximations of $A$ "
            r"and $B_0$ with errors below $16p<p^2$ and $4+3p^2/4<p^2$.",
            X("Contraction of the exact maps yields errors less than", "respectively."),
        ),
        infer(
            r"The original algorithm executes $P_t$ and $P_s^{-1}$ by two label-and-sort passes "
            r"costing $O(tp\log t)$ each; here both permutations remain in the identity.",
            X("Its two label-and-sort operations", "these permutations remain in the transform identity."),
        ),
        infer(
            r"Tensoring over all pairs $(s_i,t_i)$ gives "
            r"$RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with "
            r"$R=\bigotimes_iP_{s_i}$ and $Q=\bigotimes_iP_{t_i}$.",
            X("Tensoring \\eqref{eq:no-sort-one-dimensional} proves", "\\eqref{eq:no-sort-tensor}."),
        ),
        infer(
            r"Applying the line maps to each valid line of the padded box and zero elsewhere "
            r"keeps each axis map a contraction with error below $p^2$, so the tensor maps have "
            r"error below $dp^2$ and line cost $\sum_i(T/t_i)O(t_ip^{3/2+\delta}\alpha)$.",
            Q("Composing the $d$ axis maps gives error less than $dp^2$."),
        ),
        infer(
            r"Exposing each axis takes $O(d)$ adjacent interchanges of $\ell$- or $(\ell-1)$-bit "
            r"fields by the chunk interchange, peeling one bit for unequal widths, at "
            r"$O(Tp(1+\ell^\tau))$ each.",
            X("Each adjacent interchange therefore", "costs $O(Tp(1+\\ell^\\tau))$."),
        ),
    ],
    page="gaussian-resampling",
    frm=["dft", "multidim-transform", "fixed-point-disk-grid", "nlogn-multiplier", "chunk-interchange",
         "exponential-function-and-gaussian-function", "vector-norms-and-error-bounds", "primes-coprimality-and-gcd"],
)

chirp = show(
    r"For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, which "
    r"has period $t_i$ in coordinate $i$, the permuted middle transform is "
    r"$QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$: two pointwise phase "
    r"multiplications around one normalized cyclic convolution.",
    r"Check the periodicity of $a$ and compare the coefficient of $u_{\boldsymbol k}$ on both "
    r"sides, using $\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\exp(2\pi i\sum_is_ij_ik_i/t_i)$.",
    mot(
        r"Bluestein's identity turns the transform into a convolution, and the coefficient "
        r"$s_i$ in the chirp performs the frequency permutation $Q$, so $Q$ is never applied "
        r"as a separate permutation of the array.",
        "explicit",
        X("The chirp identity below performs the frequency change", "as a separate permutation of the array."),
    ),
    [
        infer(
            r"Since $t_i$ is even, replacing $j_i$ by $j_i+t_i$ changes the exponent by "
            r"$-\pi is_i(2j_i+t_i)\in2\pi i\mathbb Z$, so $a$ is periodic and the convolution cyclic.",
            X("Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$", "an integral multiple of $2\\pi i$."),
        ),
        infer(
            r"The coefficient of $u_{\boldsymbol k}$ on the right is "
            r"$T^{-1}\exp(2\pi i\sum_is_ij_ik_i/t_i)$, exactly that of $QF_{\boldsymbol t}$, "
            r"since $Q$ reads frequency $(-s_ij_i)_i$ of the negative-sign transform.",
            X("This is precisely the coefficient in $QF_{\\boldsymbol t}$,", "from the negative-sign transform."),
        ),
    ],
    page="chirp-identity",
    frm=["dft", "cyclic-convolution", "multidim-transform", "gaussian-resampling", "complex-numbers",
         "exponential-function-and-gaussian-function"],
    salient=r"The frequency permutation $Q$, multiplication of frequencies by $-s_i$, costs "
            r"nothing: it is absorbed into the chirp's coefficients, so no sort is executed.",
)

cancellation = show(
    r"With $S=\prod_is_i$, $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, "
    r"so the retained source permutation $R$ cancels between the two forward transforms, their "
    r"pointwise product and the opposite-sign transform, and conjugating input and output of "
    r"an algorithm for $RF_{\boldsymbol s}$ gives one for $RF_{\boldsymbol s}^+$.",
    r"Show $F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ by substituting $h=ck$ for units "
    r"$c$, commute $R$ with pointwise products, and apply the normalized convolution rule with "
    r"$F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$.",
    mot(
        r"A convolution needs the forward transforms only through their pointwise product and "
        r"the opposite transform, and a dilation by units passes through the opposite transform "
        r"as its inverse, so the retained permutation can cancel instead of being executed.",
        "explicit",
        X("The second identity shows how the", "cancels when computing a convolution."),
    ),
    [
        infer(
            r"For a unit $c$ modulo $q$, $F_q^+R_c=R_c^{-1}F_q^+$, and each $t_i$ is a unit "
            r"modulo $s_i$, so $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
            X("Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives", "$RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$."),
        ),
        infer(
            r"$(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$ "
            r"because a coordinate permutation commutes with pointwise products.",
            X("Also $(RF_{\\boldsymbol s}u)", "because a coordinate permutation commutes with pointwise products."),
        ),
        infer(
            r"With $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and "
            r"$F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$, the two normalizations give $(u*v)/S^2$.",
            X("The normalized convolution rule is", "$F_{\\boldsymbol s}^+F_{\\boldsymbol s}=I/S$."),
        ),
        infer(
            r"Complex conjugation turns the negative sign into the positive one, commutes with "
            r"the real permutation $R$, and preserves grid, norm and error bound.",
            X("Finally, conjugation changes the negative Fourier sign to the positive one", "commutes with the real permutation $R$."),
        ),
    ],
    page="permutation-cancellation",
    frm=["convolution-theorem", "multidim-transform", "dft", "gaussian-resampling",
         "primes-coprimality-and-gcd", "modular-arithmetic", "functions-bijections-and-permutations"],
    salient=r"The permutation $R$ is never executed: a dilation by units on the source side "
            r"passes through the opposite transform as its inverse and cancels exactly.",
)

# ---------------------------------------------------------------- Section 9: assembly

prime_lengths = show(
    r"For all large $n$ there are distinct odd primes $s_i$ with "
    r"$(1-2\eta)t_i<s_i\le(1-\eta)t_i$, $\eta=1/(4d)$, found deterministically in $n^{o(1)}$ "
    r"time, so that $T/2<S<T$, each $t_i/s_i-1>\eta$ gives $\alpha^4(t_i/s_i-1)>p$, and every "
    r"hypothesis of the resampling lemma holds.",
    r"Apply the prime-interval bound of Harvey and van der Hoeven (from Rosser and "
    r"Schoenfeld) to the intervals below $r/2$ and $r$, each holding more than $d$ primes, "
    r"multiply the lower bounds using Bernoulli's inequality, and search the intervals by trial division.",
    mot(
        r"The product of the source lengths must fill a fixed fraction of the padded box, while "
        r"each ratio $t_i/s_i$ must stay separated from one for resampling, so the primes must "
        r"lie just below the powers of two but not too close.",
        "explicit",
        X("The distinct prime lengths $s_i$ must be close to the powers of two", "must leave enough separation for resampling."),
    ),
    [
        infer(
            r"Since $\log(r/2)/d\to\infty$, both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$, so "
            r"each interval $((1-2\eta)x,(1-\eta)x]$ holds at least $x/(8d\log x)>d$ primes, and "
            r"the two intervals are disjoint.",
            X("Thus both $x=r/2$ and $x=r$ satisfy", "$\\log x>8d=2/\\eta$."),
        ),
        infer(
            r"Multiplying the lower bounds and using Bernoulli's inequality gives "
            r"$S/T>(1-1/(2d))^d>1/2$, so $T/2<S<T$.",
            Q("Together with $s_i<t_i$, this gives $T/2<S<T$."),
        ),
        infer(
            r"Each $t_i/s_i-1\ge\eta/(1-\eta)>\eta$ gives "
            r"$\alpha^4(t_i/s_i-1)>12d^2b/(4d)=3db\ge p$, and with $2\le\alpha<\sqrt p$ and "
            r"$t_i<2^p$ every hypothesis of the resampling lemma holds.",
            X("Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds", "for all sufficiently large input lengths."),
        ),
        infer(
            r"Trial-division search costs $O(dr^{3/2}\operatorname{poly}(p))$, whose logarithm "
            r"is $o(p)$, hence $n^{o(1)}$ time, and the primes are computed by the machine rather "
            r"than supplied as advice.",
            X("Since $p=6\\lceil\\log_2 n\\rceil=\\Theta(\\log n)$, the search takes", "$n^{o(1)}=o(n)$ time."),
        ),
    ],
    page="prime-lengths",
    frm=["crt-axis-map", "gaussian-resampling", "primes-coprimality-and-gcd", "logarithms-and-exponentials"],
)

int_as_convolution = show(
    r"Writing each input as $\lceil n/b\rceil$ radix-$2^b$ digits, the product polynomial of "
    r"the digit lists has degree below $2n/b\le T/2<S$, so it equals their cyclic convolution "
    r"modulo $x^S-1$, and its coefficients satisfy $0\le c_j<2^{3b}$.",
    r"Compare the degree of the digit product with the convolution length, and bound each "
    r"coefficient by the number of digit products it sums.",
    mot(
        r"Cyclic convolution of length $S$ agrees with ordinary polynomial multiplication when "
        r"the product's degree is below $S$, and the coefficient bound fixes the word width "
        r"needed to round and carry exactly.",
        "recoverable",
    ),
    [
        infer(
            r"The product has degree at most $2\lceil n/b\rceil-2<2n/b\le T/2<S$, so convolution "
            r"modulo $x^S-1$ has no nonzero wraparound.",
            Q("Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
        ),
        infer(
            r"Each coefficient sums at most $\lceil n/b\rceil$ digit products, so "
            r"$0\le c_j\le\lceil n/b\rceil(2^b-1)^2<2^{3b}$ since $n\le2^b$.",
            X("Every product coefficient obeys", "since $q\\le n\\le2^b$."),
        ),
    ],
    page="int-as-convolution",
    frm=["cyclic-convolution", "polynomials", "positional-number-representation-and-carries"],
)

crt_axis_map = show(
    r"For pairwise coprime $s_1,\dots,s_d$ with prefix products $P_i=\prod_{j<i}s_j$ and "
    r"$\mu_i=P_i^{-1}\bmod s_i$, the map $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ is a ring isomorphism "
    r"from $\mathbb C[x]/(x^S-1)$ to $d$-dimensional cyclic convolution sending index "
    r"$\sum_ja_jP_j$ to coordinates $a_i+\mu_i\sum_{j<i}a_jP_j\bmod s_i$, and on tape $\Phi$, "
    r"its inverse and the padding cost $O(Tpd^2(1+\ell^\tau))$.",
    r"Check that $\Phi$ respects $x^S=1$ and maps $x$ to an element of order $S$, express the "
    r"coordinates as a triangular function of the mixed-radix digits, insert padding in one "
    r"nested scan, reverse the axes, and apply the triangular updates as prefix-controlled "
    r"cyclic shifts from the last axis to the first.",
    mot(
        r"The Agarwal-Cooley split converts one cyclic convolution into a multidimensional one, "
        r"and choosing the coordinate powers $\mu_i$ makes the change of order triangular, "
        r"hence a sequence of controlled cyclic shifts.",
        "explicit",
        X("The following map uses that algebraic split,", "a sequence of controlled cyclic shifts."),
    ),
    [
        infer(
            r"$\Phi$ respects $x^S=1$, and since each $\mu_i$ is a unit and the $s_i$ are "
            r"pairwise coprime the image of $x$ has order $S$, so its powers run once through "
            r"all target monomials and $\Phi$ is an isomorphism preserving cyclic convolution.",
            Q("Hence $\\Phi$ is an isomorphism and preserves cyclic convolution."),
        ),
        infer(
            r"Index $\sum_ja_jP_j$ goes to $a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$ because terms "
            r"with $j>i$ vanish modulo $s_i$ and $\mu_iP_i\equiv1$.",
            X("Indeed terms with $j>i$ are divisible by $s_i$,", "$\\mu_iP_i=1$ modulo $s_i$."),
        ),
        infer(
            r"After reversing the axes, updating targets $i=d,\dots,1$ uses only original "
            r"lower-index digits as controls, each update a prefix-controlled rotation of the "
            r"valid interval $[0,s_i)$.",
            X("When target $i$ is updated, none of its lower-index controls has yet changed,", "required by the formula."),
        ),
        infer(
            r"Each step is a bijection of the padded box preserving the valid set, so zero "
            r"padding stays zero, and the inverse subtracts the same offsets for $i=1,\dots,d$.",
            Q("Consequently zero padding remains zero after every step."),
        ),
        infer(
            r"Reversing the axes takes $O(d^2)$ adjacent interchanges of $\ell$- or "
            r"$(\ell-1)$-bit fields, so $\Phi$, its inverse and the padding cost "
            r"$O(Tpd^2(1+\ell^\tau))$, with offset preparation $o(Tp)$.",
            X("Reversing all axes", "O\\bigl(Tp\\,d^2(1+\\ell^\\tau)\\bigr)."),
        ),
    ],
    page="crt-axis-map",
    frm=["cyclic-convolution", "primes-coprimality-and-gcd", "modular-arithmetic", "controlled-shifts",
         "chunk-interchange", "multidim-transform", "array-order"],
)

negacyclic_twist = show(
    r"The twist $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$ with "
    r"$\zeta=e^{\pi i/r}$, is a norm-preserving ring isomorphism multiplying coefficient $k$ "
    r"by $\zeta^k$, and a product term with $k+l=j+hr$ picks up $\zeta^{k+l}(-1)^h=\zeta^j$.",
    r"Check $(\zeta y)^r=1$, diagonality on the monomial bases, and the sign of each wrapped "
    r"product term.",
    mot(
        r"Scaling coefficient $k$ by $\zeta^k$ with $\zeta^r=-1$ converts the cyclic relation "
        r"$x^r=1$ into the negacyclic $y^r=-1$, so the ring in which twiddles are signed shifts "
        r"can carry the cyclic convolution.",
        "recoverable",
    ),
    [
        infer(
            r"$\Theta$ is well defined since $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal with "
            r"nonzero entries $\zeta^k$, hence an isomorphism.",
            X("The map \\[ \\Theta", "with inverse multiplying that coefficient by $\\zeta^{-k}$."),
        ),
        infer(
            r"For $k+l=j+hr$ with $h\in\{0,1\}$ the negacyclic sign $(-1)^h$ and $\zeta^{hr}$ "
            r"cancel, so untwisting recovers the cyclic coefficient with the correct sign.",
            Q("Untwisting therefore recovers the cyclic coefficient with the correct sign."),
        ),
    ],
    page="negacyclic-twist",
    frm=["polynomial-ring-mod", "cyclic-convolution", "complex-numbers"],
    salient=r"The negative wrap from $y^r=-1$ and the factor $\zeta^r=-1$ from the twist cancel "
            r"exactly, so the twisted negacyclic product is the cyclic one.",
)

complex_convolution = show(
    r"Normalized complex cyclic convolution on the power-of-two box with $t_d=r$ is "
    r"$\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, "
    r"where $D_\pm$ multiplies coefficient $k$ of the last axis by $\zeta^{\pm k}$ and $\iota$ "
    r"reads the last axis as a record of $\mathcal R_r$; its computed version, for disk-grid "
    r"inputs one of norm at most $.7$, twists with approximate phases, applies the ring "
    r"convolution and untwists, with twist cost $O(Tp^{1+\delta})$.",
    r"Identify the last cyclic axis with the negacyclic ring through the twist, note that "
    r"$\iota$ only changes the shape descriptor, and compute the twists with approximate "
    r"phases followed by truncation.",
    mot(
        r"A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$ whose "
        r"negative wrap gives exactly the cyclic wrap once the twist is removed, so the ring "
        r"convolution computes the complex one.",
        "explicit",
        X("A phase twist changes the last cyclic coordinate into a polynomial", "after the twist is removed."),
    ),
    [
        negacyclic_twist,
        infer(
            r"Linewise $\Theta$ is $\iota D_+$ with inverse $D_-\iota^{-1}$, all isometries, so "
            r"$\mathcal M_{\mathbb C}(f,g)=(f*g)/T$ is a bilinear contraction.",
            X("The maps $D_\\pm$ and", "is also a bilinear contraction."),
        ),
        infer(
            r"With component width $p+2$ both formats concatenate the same words in the same "
            r"order, so $\iota$ and $\iota^{-1}$ change only the shape descriptor.",
            X("Hence $\\iota$ and $\\iota^{-1}$ change only the shape descriptor", "when these component formats agree."),
        ),
        infer(
            r"The computed version truncates the twisted inputs, applies the ring convolution, "
            r"removes sign-extension bits and truncates the untwisted output, with phases within "
            r"$2\cdot2^{-p}$ and total twist cost $O(Tp^{1+\delta})$.",
            X("Generating every factor anew therefore still gives total", "twist cost $O(Tp^{1+\\delta})$."),
        ),
    ],
    page="complex-convolution",
    frm=["ring-convolution", "cyclic-convolution", "fixed-point-disk-grid", "polynomial-ring-mod", "complex-numbers"],
)

source_transform = show(
    r"For a disk-grid source tensor of norm at most $.5$ in the padded box, the computed "
    r"source transform $\widetilde{\mathscr F}$ (linewise $\mathcal A$, the computed chirp "
    r"transform, linewise $\mathcal B_0$, exact scale $2^\gamma$) has exact counterpart "
    r"$2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, and "
    r"$\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$ has exact "
    r"counterpart $RF_{\boldsymbol s}^+$.",
    r"Compute the chirp phases modulo $2r$ from the axis descriptors, evaluate the middle "
    r"factor by the chirp identity through the complex convolution, compose with the Gaussian "
    r"line maps and the exact power-of-two scale, and obtain the opposite sign by conjugation.",
    mot(
        r"The resampling identity reduces the prime-length transform to the middle factor "
        r"$QF_{\boldsymbol t}$, which the chirp identity turns into one complex convolution; "
        r"composing with the Gaussian maps then gives $RF_{\boldsymbol s}$ itself.",
        "recoverable",
    ),
    [
        infer(
            r"The chirp numerator $-\sum_is_ij_i^2(r/t_i)\bmod2r$ at each address takes "
            r"$O(dp^{1+\delta})$ with the established multiplier, so the chirp array costs "
            r"$O(Tdp^{1+\delta})$.",
            Q("Thus chirp construction costs $O(Td p^{1+\\delta})$ in total."),
        ),
        infer(
            r"With exact phases and exact convolution, $x\mapsto\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)$ "
            r"is $QF_{\boldsymbol t}$ by the chirp identity.",
            X("Replacing the approximations by exact phases and exact convolution gives", "by \\eqref{eq:permuted-chirp}."),
        ),
        infer(
            r"The source transform applies linewise $\mathcal A$, the computed chirp transform, "
            r"linewise $\mathcal B_0$ and the exact scale $2^\gamma$, so its exact counterpart is "
            r"$2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
            X("For a source disk-grid tensor of norm at most $.5$, write", "=RF_{\\boldsymbol s}."),
        ),
        infer(
            r"Conjugating input and output gives the opposite-sign procedure with exact "
            r"counterpart $RF_{\boldsymbol s}^+$.",
            X("Define the opposite-sign procedure by", "by Lemma~\\ref{lem:chirp-permutation}."),
        ),
    ],
    page="source-transform",
    frm=["gaussian-resampling", "chirp-identity", "complex-convolution", "permutation-cancellation",
         "fixed-point-disk-grid", "nlogn-multiplier"],
)

mult_algorithm = show(
    r"The algorithm writes digit $a_j$ as the exact grid value $a_j2^{-b-2}$, applies $\Phi$ to "
    r"get source arrays $u,v$ of norm below $1/4$, computes $\widetilde{\mathscr F}(u)$ and "
    r"$\widetilde{\mathscr F}(v)$, multiplies pointwise with one truncation, applies "
    r"$\widetilde{\mathscr F}^+$, scales by $S$ and then by $2^{2b+4}S$, rounds, applies "
    r"$\Phi^{-1}$ and propagates radix-$2^b$ carries, and its exact counterpart is "
    r"$2^{2b+4}(u*v)$, whose preimage under $\Phi$ is the integer convolution of the digits.",
    r"Follow the exact counterparts: the cancellation identity gives $(u*v)/S^2$ after the "
    r"three transforms, the first scale by $S$ gives $w=(u*v)/S$, and the second scale "
    r"$2^{2b+4}S$ undoes the remaining normalization and the two input scales.",
    mot(
        r"Every transform is normalized and the digits were scaled into the disk, so the exact "
        r"counterpart of the pipeline is a known rescaling of the digit convolution; the two "
        r"factors $S$ undo different normalizations.",
        "explicit",
        Q("The two occurrences of $S$ in this algorithm undo different normalizations."),
    ),
    [
        infer(
            r"Each digit $a_j$ becomes the exact grid numerator $a_j2^{p-b-2}$, i.e. the value "
            r"$a_j2^{-b-2}<1/4$, with zero records appended up to length $S$, in $O(Tp)$.",
            X("This exponent is nonnegative", "the represented value is exactly $a_j2^{-b-2}$."),
        ),
        infer(
            r"The steps are: $\Phi$ with padding, the two computed source transforms, an exact "
            r"pointwise product truncated to the grid, the computed opposite transform scaled "
            r"exactly by $S$, a second exact scale by $2^{2b+4}S$ with rounding, $\Phi^{-1}$, and "
            r"carry propagation.",
            X("Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain", "source arrays $u,v$."),
        ),
        infer(
            r"By the cancellation identity the exact counterpart after the three transforms is "
            r"$(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$.",
            X("By \\eqref{eq:source-permutation-cancel}, the exact", "after the first scale it is $w=(u*v)/S$."),
        ),
        infer(
            r"The second scale gives $2^{2b+4}(u*v)$, whose preimage under $\Phi$ is the original "
            r"integer coefficient convolution.",
            X("The second scale gives $2^{2b+4}(u*v)$,", "the original integer coefficient convolution."),
        ),
    ],
    page="mult-algorithm",
    frm=["int-as-convolution", "crt-axis-map", "source-transform", "permutation-cancellation",
         "fixed-point-disk-grid", "positional-number-representation-and-carries"],
)

exact_recovery = show(
    r"Every computed map stays in the unit disk with margin, the computed $\widetilde w$ "
    r"approximates $w=(u*v)/S$ within $28\cdot2^\gamma T^2\log_2T\cdot2^{-p}$, so after the "
    r"exact scale $2^{2b+4}S$ the error is below $448b\,2^{-3b/4}<1/2$; rounding then gives the "
    r"exact integer coefficients and carry propagation outputs exactly the $2n$ product bits.",
    r"Propagate errors through contractions and bilinear contractions, whose errors add when "
    r"operands lie in the disk, checking a disk margin at each call (ring convolution, "
    r"twisted complex convolution, chirp, source transform, pointwise product, opposite "
    r"transform), compare the scaled error with $1/2$ using $\gamma\le b/4$ and $S\le T<2^b$, "
    r"and verify the carry invariant.",
    mot(
        r"The true coefficients are integers, so any approximation within less than $1/2$ "
        r"rounds to the exact value; contraction bounds make the errors of successive stages add.",
        "explicit",
        X("The true coefficients are real integers.", "the unique correct coefficient."),
    ),
    [
        infer(
            r"The ring convolution has error below $M(3\log_2T+2)<5T\log_2T$ grid units, and "
            r"with one operand of norm at most $.7$ its output norm is below $.701$, a disk margin "
            r"after the scale $M$.",
            X("This proves the disk margin after the scale $M$,", "without clipping the output."),
        ),
        infer(
            r"The two input twists and the output untwist add less than $4$ units each, so the "
            r"computed complex convolution has error below $6T\log_2T$ units and stays in the disk.",
            X("All these comparisons are at the normalized $\\mathcal M_r$", "after its factor $M$."),
        ),
        infer(
            r"For $\|x\|\le.6$ the chirp operands keep norm at most $.6$, the chirp output has "
            r"norm below $.701$, and its error is below $8T\log_2T$ units.",
            X("In particular, the chirp output", "is a legal disk-grid input to the compression maps."),
        ),
        infer(
            r"The source transform has error below $2^\gamma(2dp^2+8T\log_2T)<E_s=9\cdot2^\gamma T\log_2T$ "
            r"units, since $2dp^2<T\log_2T$, and output norm below $.501$, and conjugation gives the "
            r"same for the opposite transform.",
            X("Multiplication by $2^\\gamma$ therefore gives error less than", "because $2dp^2<TL$ eventually."),
        ),
        infer(
            r"Since $\|u\|,\|v\|<1/4$, the computed transforms have norm below $.26$, the "
            r"truncated product $z$ has norm below $.5$ and error below $2E_s+2$, and the "
            r"opposite transform adds $E_s$, so the error against $(u*v)/S^2$ is below $3E_s+2$.",
            Q("Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$."),
        ),
        infer(
            r"The exact scale by $S$ gives $\widetilde w$ within $S(3E_s+2)<28\cdot2^\gamma T^2\log_2T$ "
            r"units of $w$, and $\|w\|<1/16$ keeps $\widetilde w$ in the disk.",
            Q("This proves the disk bound for the computed first scaled result."),
        ),
        infer(
            r"The second exact scale with $S\le T<2^b$, $\log_2T<b$ and $\gamma\le b/4$ gives final "
            r"error below $2^{2b+4}S\cdot28\cdot2^\gamma T^2\log_2T\cdot2^{-6b}<448b\,2^{-3b/4}<1/2$.",
            X("Since $S\\le T<2^b$ and $L<b$ eventually, the final absolute error is less than", "<\\frac12."),
        ),
        infer(
            r"Carries $k_{j+1}=\lfloor(c_j+k_j)/2^b\rfloor$ stay below $2^{2b}$, and the invariant "
            r"$\sum_{h<j}c_h2^{bh}=\sum_{h<j}d_h2^{bh}+k_j2^{bj}$ fixes the radix digits of the product.",
            Q("The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$."),
        ),
        infer(
            r"The product is below $2^{2n}$, so removing only higher zero bits outputs exactly "
            r"$2n$ bits, most significant first.",
            X("The exact product is", "are therefore zero."),
        ),
    ],
    page="exact-recovery",
    frm=["fixed-point-disk-grid", "vector-norms-and-error-bounds", "ring-convolution", "complex-convolution",
         "source-transform", "permutation-cancellation", "int-as-convolution",
         "positional-number-representation-and-carries", "floor-ceiling-and-rounding"],
    salient=r"Despite many approximate stages and a final scale near $2^{5b}$, the total error "
            r"stays strictly below $1/2$, because the precision $p=6b$ leaves room above the "
            r"scale $2^{2b+4}S\cdot2^\gamma T^2\log_2T$ with $\gamma=o(b)$.",
)

parameter_balance = show(
    r"With fixed rationals $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$, "
    r"$\delta=1/16$ and sizes $p=6\lceil\log_2n\rceil$, $d=\lfloor b^\epsilon\rfloor$, "
    r"$K=\lfloor d^c\rfloor$, $T\in[4n/b,8n/b)$, $r=2^{\lceil\log_2T/d\rceil}$, every row of "
    r"the cost table normalized by $Tp=\Theta(n)$ is at most $p^{1-2\kappa}$ up to fixed powers "
    r"of $\log p$, so the time is $O(Tp\cdot p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ with "
    r"$\kappa=2^{-182}$.",
    r"Fix exponents and sizes satisfying every layer, transform and resampling hypothesis, list "
    r"the normalized cost of each operation as a power of $p$, compute the seven margins below "
    r"one, and absorb setup, descriptor work and exceptional sorting as $o(Tp)$.",
    mot(
        r"Each procedure's cost is a power of $p$ through $d$, $K$ and $\ell$, so the exponents "
        r"must be balanced together: enough axes for the layer saving, chunks wide enough for "
        r"cheap layouts and repair, yet axis moves and Gaussian maps still below one pass per level.",
        "explicit",
        X("A compatible choice of rational", "fit Theorem~\\ref{thm:main}."),
    ),
    [
        infer(
            r"Fix $\tau=\sigma=1-2^{-50}$, $\beta=1/2$, $\delta=1/16$, $\lambda=1-2^{-52}$, "
            r"$c=2^{-56}$, $\lambda'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$ and "
            r"$\kappa=2^{-182}$, which satisfy all layer conditions and "
            r"$\epsilon(2-\tau)<1-\tau$, $3/4+\delta+3\epsilon/2<1$.",
            X("Take the following fixed rational numbers:", "\\kappa=2^{-182}."),
            deferred=True,
        ),
        infer(
            r"Put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, "
            r"$K=\lfloor d^c\rfloor$, $T$ the power of two in $[4n/b,8n/b)$ and "
            r"$r=2^{\lceil\log_2T/d\rceil}$ with axis lengths in $\{r/2,r\}$, so that "
            r"$Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$ and "
            r"$\log_2r=\Theta(p^{1-\epsilon})$.",
            X("Take the power of two $T$ in $[4n/b,8n/b)$, and let", "and $\\ell=\\log_2r$."),
            deferred=True,
        ),
        infer(
            r"Normalized by $V=Tp$, the costs are $dK$ (prefix moves and individual rounds), "
            r"$pK^{\tau-1}$ (layout chunk exchanges), $\ell d^{\lambda'}$ (simultaneous rounds), "
            r"$d^2(1+\ell^\tau)$ (CRT and axis layouts), $dp^{1/2+\delta}\alpha$ (Gaussian line "
            r"maps), $dp^\delta$ (chirps, twists, scalar products) and $\log(rp)$ (packed "
            r"polynomial products).",
            X("Table~\\ref{tab:costs} lists costs after division", "is included in its constants."),
        ),
        infer(
            r"The seven margins below one are $1-\epsilon(1+c)>1/2$, $\epsilon c(1-\tau)=2^{-181}$, "
            r"$\epsilon(1-\lambda')=2^{-129}$, $1-\tau-\epsilon(2-\tau)>2^{-51}$, "
            r"$1/4-\delta-3\epsilon/2>1/8$, $1-\delta-\epsilon>1/2$ and $\epsilon=2^{-75}$, so the "
            r"least is $2^{-181}=2\kappa$, from the layout chunk exchanges.",
            Q("Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
        ),
        infer(
            r"Setup at the $p^{O(1)}$ recursion visits and polynomial descriptor work per record or "
            r"per Gaussian line cost $o(Tp)$, because $r$ exceeds every fixed power of $p$.",
            Q("This setup then costs at most $p^{A+C}=o(Tp)$."),
        ),
        infer(
            r"The exceptional sorting of all packed basis changes costs $O(Vp^{A'}2^{-K})=o(V)$ "
            r"since $K=\Theta(p^{\epsilon c})$, a deterministic worst-case bound.",
            Q("This is a deterministic worst-case bound."),
        ),
        infer(
            r"Each power is at most $1-2\kappa$ and any fixed power of $\log p$ is eventually at "
            r"most $p^\kappa$, so the time is $O(Tp\cdot p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
            X("Each of the seven displayed powers is at most", "=O(n(\\log n)^{1-\\kappa})."),
        ),
        infer(
            r"Schoolbook multiplication below one fixed cutoff covers the finitely many small "
            r"lengths, so a single machine achieves $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.",
            X("Fix one cutoff beyond all the size, precision, margin and layout", "use schoolbook multiplication below it."),
        ),
    ],
    page="parameter-balance",
    frm=["simultaneous-layer", "chunk-interchange", "transform-layout", "ring-convolution", "kronecker-packing",
         "gaussian-resampling", "crt-axis-map", "prime-lengths", "source-transform", "packed-bit-addition",
         "nlogn-multiplier", "big-o", "logarithms-and-exponentials"],
    salient=r"Every row is a power of $p$ strictly below one, and the smallest margin, "
            r"$\epsilon c(1-\tau)=2^{-181}=2\kappa$, comes from the chunk exchanges of the "
            r"transform layout, which fixes the saving exponent $\kappa=2^{-182}$.",
    adds=[
        add("c", "chunk exponent", "The fixed exponent 2^{-56} with K the floor of d^c.", "direct"),
    ],
)

assembly = show(
    r"With a fixed rational choice of exponents and sizes, the machine converts the inputs to "
    r"radix-$2^b$ digits, maps them to prime cyclic axes, applies two computed source "
    r"transforms, multiplies pointwise, applies the opposite transform, rescales, rounds and "
    r"propagates carries, producing the exact $2n$-bit product within $O(n(\lg n)^{1-\kappa})$ steps.",
    r"Instantiate the procedures with compatible parameters, prove each reduction exact at the "
    r"level of exact counterparts, track errors and disk margins through every computed map "
    r"to bring the final error below $1/2$, and sum a cost table normalized by $Tp=\Theta(n)$.",
    mot(
        r"The building blocks come with error and cost bounds under parameter hypotheses, so "
        r"assembling them needs one parameter choice meeting all hypotheses, an error budget "
        r"below one half for exact rounding, and a cost table whose rows are powers of $p$ below one.",
        "recoverable",
    ),
    [prime_lengths, int_as_convolution, crt_axis_map, complex_convolution, source_transform,
     mult_algorithm, exact_recovery, parameter_balance],
    adds=[
        add("b", "digit bit width", "The radix exponent: each input digit has b bits, b being the ceiling of log2 n.", "count"),
        add("S", "source convolution length", "The product of the distinct odd prime axis lengths, the length of the digit convolution.", "count"),
    ],
)

reduction = show(
    r"Placed inside the reduction of multiplication to synthetic polynomial transforms, with "
    r"every change of representation, precision loss and tape movement accounted for, the two "
    r"procedures yield the exact $2n$-bit product in $O(n(\lg n)^{1-\kappa})$ time.",
    r"Compute normalized convolution over $\mathbb C[y]/(y^r+1)$ by synthetic transforms in a "
    r"retained layout, express the prime-length source transforms through power-of-two "
    r"transforms by Gaussian resampling and the chirp identity while keeping both coordinate "
    r"permutations in the formulas, and assemble the algorithm: digits, Chinese-remainder "
    r"address map, coefficient twist, source transforms, pointwise product, opposite "
    r"transform, rounding and carries.",
    mot(
        r"Once one coordinate is a polynomial modulo $y^r+1$, roots of unity are signed shifts, "
        r"so the transforms consist only of address rearrangements, signed shifts and two-point "
        r"butterflies, which is exactly what the two tape procedures accelerate.",
        "explicit",
        X("In this representation, the transform calculation consists of address", "two-point butterfly operations."),
    ),
    [ring_convolution, resampling, chirp, cancellation, assembly],
    frm=["int-as-convolution", "cyclic-convolution", "dft", "convolution-theorem", "multidim-transform"],
    adds=[
        add("T", "padded box size", "The number of entries of the padded power-of-two transform box, the product of the axis lengths.", "count"),
        add(r"\ell", "ring log-length", "The base-two logarithm of r, so every axis has length 2^ell or 2^{ell-1}.", "count"),
        add("M", "record count", "The number T/r of polynomial records in a ring array, the product of all axis lengths but the last.", "count"),
        add(r"\alpha", "Gaussian width", "The integer parameter, between 2 and the square root of p, that sets the width of the Gaussian kernels.", "direct"),
        add(r"\gamma", "resampling scale exponent", "The exponent 2d alpha^2 of the power of two that rescales the normalized resampled transform.", "direct"),
        add("s_i", "prime source length", "The odd prime length of source axis i, coprime to the power of two t_i.", "count"),
    ],
)

refutation = infer(
    r"Refuting an eventual lower bound $T_A(n)\ge c_An\lg n$ for every machine needs one machine "
    r"with $\liminf_{n\to\infty}T_A(n)/(n\lg n)=0$, and a power saving in the logarithm gives "
    r"limit zero through all input lengths.",
    X("Its negation requires one machine satisfying", "which is a stronger conclusion."),
    frm=["nlogn-conjecture", "asymptotic-notation-beyond-big-o"],
)

root = show(
    r"There is one deterministic Turing machine with a fixed finite alphabet and a fixed finite "
    r"number of one-dimensional tapes that returns the exact $2n$-bit product of any two "
    r"$n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, "
    r"disproving the $n\log n$ optimality conjecture of Schönhage and Strassen in this model.",
    r"Observe that one machine with a power saving refutes the conjecture; build two tape "
    r"procedures, a fast interchange of address chunks and a simultaneous butterfly layer, "
    r"whose recursive costs carry a power saving from linear networks with a rank deficit; "
    r"then place them inside Harvey and van der Hoeven's reduction of multiplication to "
    r"synthetic polynomial transforms, accounting for every change of representation, "
    r"precision and cost.",
    mot(
        r"The transform route already spends $\Theta(n\log n)$ just scanning $\Theta(n)$ stored "
        r"bits at each of $\Theta(\log n)$ levels, so beating $n\log n$ needs savings in both "
        r"data movement and arithmetic, which the two tape procedures supply.",
        "explicit",
        X("Scanning an array of $\\Theta(n)$ stored bits at each of", "Two tape procedures supply them;"),
    ),
    [refutation, procedures, reduction],
    page="main-theorem",
    frm=["fixed-tape-model", "nlogn-conjecture", "nlogn-multiplier", "big-o", "logarithms-and-exponentials",
         "determinism-and-exact-versus-approximate-computation"],
    salient=r"The saving is a strict power of the logarithm, $(\lg n)^{-\kappa}$, holding through "
            r"all input lengths, so the running time divided by $n\lg n$ tends to zero; the "
            r"exponent $\kappa=2^{-182}$ is tiny but fixed.",
    adds=[
        add("n", "input length", "The number of bits of each of the two input integers.", "count"),
        add(r"\kappa", "saving exponent", "The fixed exponent 2^{-182} by which the running time beats n lg n, as the factor (lg n)^{-kappa}.", "direct"),
        add("V", "logical bit volume", "The number of stored data bits of the array a procedure acts on, excluding work tapes and duplicate streams.", "count"),
        add("p", "working precision", "The number of fractional bits of the fixed-point grid on which complex values are stored.", "count"),
        add("d", "number of axes", "The number of transform axes, which also bounds how many address chunks one butterfly layer handles.", "count"),
        add("r", "record length", "The number of complex coefficients in one polynomial record modulo y^r+1, a power of two.", "count"),
        add("K", "chunk bit width", "The width in bits of the address chunks used by butterfly layers and transform layouts.", "count"),
        add(r"\tau", "interchange exponent", "The fixed exponent 1-2^{-50} below one in the chunk-interchange cost.", "direct"),
        add(r"\lambda'", "layer exponent", "The fixed exponent 1-2^{-54} below one in the butterfly-layer cost.", "direct"),
        add(r"\epsilon", "axis-count exponent", "The fixed exponent 2^{-75} with d of order p^epsilon.", "direct"),
    ],
)

assign_ids(root)
errors, warnings = check(root, verbose="-q" not in sys.argv)
print("errors:", *errors, sep="\n  ")
print("warnings:", *warnings, sep="\n  ")
heads, lines = coverage(root)
for i, (ln, h) in enumerate(heads):
    nxt = heads[i + 1][0] if i + 1 < len(heads) else 10**9
    print(f"  {h[:60]:<60} quotes: {sum(1 for l in lines if ln <= l < nxt)}")
count = sum(1 for _ in __import__('lib').walk(root))
print("nodes:", count)
if not errors and "--write" in sys.argv:
    json.dump({"root": root}, open(ANSWER, "w"), ensure_ascii=False, indent=1)
    print("written", ANSWER)
