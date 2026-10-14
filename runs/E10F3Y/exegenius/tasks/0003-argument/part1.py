from lib import *

# ---------------------------------------------------------------- S1.1 exchange network
s11_1 = show(
    "S1.1.1",
    r"For arbitrary initial values of its scratch wires, one forward invocation (eight rows of gates) changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
    r"Write $\mathcal V$ for copy, $\mathcal G$ for gather, $\mathcal J$ for side injection and $\mathcal R$ for scatter. With initial side and central values $a,c$, rows 0-1 subtract $\mathcal Ja+\mathcal Rc$ from $y$, rows 2-5 add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$, rows 6-7 restore $c,a$; check coefficient by coefficient that $\mathcal J\mathcal V+\mathcal R\mathcal G$ is the identity.",
    mot("The first rows of the schedule undo whatever the old scratch values would add, so the net change cannot depend on them.", "explicit",
        r"the following schedule remove the effect of the old scratch values;"),
    [
        infer("S1.1.1a",
              r"The net change of the target is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independent of the initial side and central vectors $a,c$.",
              r"Rows 6 and 7 restore $c,a$."),
        infer("S1.1.1b",
              r"Bit construction over $\mathbb F_2$ (neighbors have $|S\cap T|=1$): the central path gives $x_T$ the coefficient $|S\cap T| \bmod 2$ in $y_S$, i.e. $1$ for $|S\cap T|=1$ and for $T=S$ ($|S\cap T|=3$) and $0$ for intersection $0$ or $2$; the side injection cancels exactly the intersection-one neighbors, so the net coefficient is $1$ for $T=S$ and $0$ otherwise.",
              r"In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
        infer("S1.1.1c",
              r"Complex construction over $\mathbb Z[i,1/2]$ (neighbors are distinct triples with even intersection): the central coefficient is $(|S\cap T|-1)/2$, equal to $-1/2$ for intersection $0$, $0$ for intersection $1$, $+1/2$ for intersection $2$ and $1$ for $T=S$; the side injection cancels the values for intersection $0$ and $2$, so the net coefficient is $1$ for $T=S$ and $0$ otherwise.",
              r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$."),
    ])

s11_2 = infer(
    "S1.1.2",
    r"Running a forward invocation from $X$ to $Y$ at stage 1, the inverse schedule from $Y$ to $X$ at stage 2 and a forward invocation from $X$ to $Y$ at stage 3 sends $(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x)$, that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$, and each invocation restores its own scratch wires.",
    r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.")

s11_3 = infer(
    "S1.1.3",
    r"The fixed sizes are $h=100$, $v=\binom h3=161700$, $N=v^3=4227952113000000$, $m=h^3=10^6$ and $I=3v^2=78440670000$ invocations; a triple has $z_{\rm b}=3\binom{97}{2}=13968$ and $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbors (ordered pairs, so $vz$ side wires per invocation), with $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires, giving $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ and $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires.",
    r"With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation,")

s11 = show(
    "S1.1",
    r"A fixed network with $W$ wires, built from three-element subsets of $[h]$ and $I$ invocations of an eight-row gate schedule, sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and returns every scratch wire to its arbitrary initial value, in a bit version over $\mathbb F_2$ with $W_{\rm b}$ wires and a complex version over $\mathbb Z[i,1/2]$ with $W_{\rm c}$ wires.",
    r"Do three stages, one per coordinate of the bank index $a\in\mathcal T^3$: stage $j$ adds the bank $X$ into $Y$ along coordinate $j$ (forward invocation), then subtracts $Y$ from $X$, then adds $X$ to $Y$ again, so the composition is the signed swap; each invocation uses copy, gather, side-injection and scatter gates whose scratch effects cancel.",
    mot("Adding, subtracting and adding again swaps two banks with a sign, just as three additions swap two numbers; the scratch cancellation is what lets the exchange run when the scratch wires hold unrelated data.", "recoverable"),
    [s11_1, s11_2, s11_3],
    page="exchange-network",
    frm=["finite-sets-subsets-and-counting", "arithmetic-modulo-2-and-linear-algebra-over-f-2", "circuits-and-directed-acyclic-graphs", "matrices-and-linear-maps"],
    adds=[
        add(r"h", "ground set size", "The size $h=100$ of the ground set $[h]$ whose three-element subsets index the banks.", "count"),
        add(r"v", "number of triples", "The number $\binom h3=161700$ of three-element subsets of $[h]$, i.e. the number of values in one bank along one coordinate.", "count"),
        add(r"N", "bank size", "The number $v^3=4227952113000000$ of entries $X_a$ (and of entries $Y_a$) in a data bank.", "count"),
        add(r"I", "number of invocations", "The number $3v^2=78440670000$ of separate invocations of the eight-row schedule, each with its own scratch wires.", "count"),
        add(r"W_{\rm b}", "bit wire count", "The total number of wires of the bit network, $W_{\rm b}=177176569091445000000$.", "count"),
        add(r"W_{\rm c}", "complex wire count", "The total number of wires of the complex network, $W_{\rm c}=1873807244643542670000$.", "count"),
    ],
    salient=r"Both banks are exchanged exactly even though every scratch wire starts with an arbitrary value: the eight-row schedule is constructed so that the unknown scratch contents cancel (rows 0-1 against rows 6-7) rather than being assumed zero.")

# ---------------------------------------------------------------- S1.2 frames
s12 = show(
    "S1.2",
    r"Give every source, gate and sink $v$ an invertible frame $D_v$ on arrays indexed by a common address set $\Omega$, with edge operator $D_vD_u^{-1}$; since a pointwise linear gate commutes with the common frame, the array network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, and the route from input role $w$ to output role $\rho(w)$ applies only $\varepsilon_wD_{{\rm sink}(\rho(w))}D_{{\rm source}(w)}^{-1}$.",
    r"Replace each scalar by an array in $R^\Omega$ and apply each scalar gate at every address; maintain the invariant that the stored array equals the frame applied to the logical array, use linearity to push the common frame through each gate, and let the intermediate frames cancel along each route.",
    mot("Once the scalar routing is fixed, only the endpoint frames matter, so the intermediate frames are free to be chosen to make each edge change cheap.", "explicit",
        r"the endpoint frames determine the array operator on each route; the"),
    [
        infer("S1.2a",
              r"The invariant `stored array $=D_v\,$(logical array)' holds at the sources by the definition $g=D_{\rm in}^{-1}f$ of the logical input, which needs no physical preprocessing, and an edge from $u$ to $v$ applying $D_vD_u^{-1}$ carries it from $D_u\varphi$ to $D_v\varphi$.",
              r"At a vertex $v$, the invariant is that the stored array equals $D_v$ applied"),
        infer("S1.2b",
              r"At a gate every incident array has the same frame $D_v$ and the gate is $R$-linear, so $G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t)$: the invariant continues through the gate to the sinks.",
              r"$c_j\in R$.  Thus the common frame commutes with the pointwise gate, and"),
        infer("S1.2c",
              r"If the scalar network is a signed role permutation sending input role $w$ to output role $\rho(w)$ with sign $\varepsilon_w$, the intermediate frames cancel and that route applies $\varepsilon_wD_{{\rm sink}(\rho(w))}D_{{\rm source}(w)}^{-1}$, on auxiliary roles as well as on data roles.",
              r"In particular, if the scalar network is a signed role permutation that"),
    ],
    page="frames",
    frm=["exchange-network", "matrices-and-linear-maps", "permutations-bijections-and-permutation-matrices", "vector-spaces-subspaces-dimension-and-rank"],
    adds=[
        add(r"D_v", "frame", "The invertible linear operator on the array carried by a wire at source, gate or sink $v$: the stored array is $D_vg$ when the logical array is $g$.", "direct"),
        add(r"\rho", "role permutation", "The permutation of roles by which the scalar network moves the input value of role $w$ to output role $\rho(w)$.", "direct"),
    ],
    salient=r"The operator that finally acts is the same shear (or kernel) on every one of the $W$ roles, including the scratch roles that carry arbitrary values, although the network is irregular: only the endpoint frames survive the telescoping.")

# ---------------------------------------------------------------- S1.3 subspace labels
tab_x = infer("S1.3.5a",
              r"Data wire $X$: the residual of the edge from the previous vertex into time 2 is $B\otimes t_X^\perp$ of dimension $(a-1)(h-1)$, that of $2\to3$ is $P\otimes t_X^\perp$ of dimension $h-1$, and the edges $3\to6$ and $6\to7$ have residual $0$.",
              r"X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\")
tab_y = infer("S1.3.5b",
              r"Data wire $Y$: the edge into time 0 has residual $0$, $0\to1$ has residual $B\otimes t_Y^\perp$ of dimension $(a-1)(h-1)$, $1\to4$ has residual $0$, and $4\to5$ has residual $P\otimes t_Y^\perp$ of dimension $h-1$.",
              r"Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\")
tab_c = infer("S1.3.5c",
              r"Central wire: source$\to1$ has residual $B\otimes F$ of dimension $(a-1)h$, and each of $1\to3$, $3\to4$, $4\to6$ has residual $P\otimes F$ of dimension $h$; the edge $3\to4$ is the only one on which the label shrinks, losing exactly $P\otimes F$.",
              r"\mathrm{center}:\ 3\to4&P\otimes F&h\\")
tab_s = infer("S1.3.5d",
              r"Side wire: source$\to0$ has residual $B\otimes\langle t_Y\rangle$ of dimension $a-1$, $0\to2$ has $(B\otimes t_Y^\perp)\perp(P\otimes\langle t_X\rangle)$ of dimension $(a-1)(h-1)+1$, $2\to5$ has $P\otimes\langle t_X,t_Y\rangle^\perp$ of dimension $h-2$ (this edge needs $t_X\perp t_Y$), and $5\to7$ has $P\otimes\langle t_Y\rangle$ of dimension $1$.",
              r"\mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\")
tab_z = infer("S1.3.5e",
              r"Scratch wire: the final edge to the sink enlarges $(A\otimes F)\otimes Q$ to $\mathcal F$, with residual $(A\otimes F)\otimes Q^\perp$ of dimension $ah(f-1)$; label dimension is nondecreasing on every edge except central $3\to4$.",
              r"\mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink}")

s13_5 = show(
    "S1.3.5",
    r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each of dimension loss $h$; the orthogonal residual of every edge is listed in a table by wire type.",
    r"Split $A=B\perp P$ and $F=\langle t\rangle\perp t^\perp$ and read off the orthogonal residual of each edge in the eight-time schedule for the five wire types (data $X$, data $Y$, central, side, scratch).",
    mot("The residual is the complement of the smaller label in the larger, so its dimension is the label change; a table lists each of the finitely many edge types.", "recoverable"),
    [tab_x, tab_y, tab_c, tab_s, tab_z])

s13 = show(
    "S1.3",
    r"Attach to every gate and terminal a nondegenerate subspace of the $m$-dimensional space $\mathcal F=F^{\otimes3}$, nested along every edge, so that the dimension of an edge's orthogonal residual is the number of smaller operations it needs; the only decreasing edges lose $h$ each, their total loss is $L=Ich$ and the absolute changes sum to $Wm-2N+2L$.",
    r"Choose a bilinear form on $F$ ($\mathbb Q^h$ with $I-J/9$ for the bit network, $\mathbb F_2^h$ with the dot product for the complex one) for which indicator vectors $t_T$ of neighboring triples are orthogonal, take tensor products $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, expose one tensor factor per stage through $A=B\perp P$, and verify the label of every edge in a table of orthogonal residuals.",
    mot("Cheap changes of frame need nested labels with few dimensions lost, because the loss on decreasing edges is what eats the saving.", "explicit",
        r"The saving will come from keeping the total dimension lost on decreasing"),
    [
        infer("S1.3.1",
              r"Bit network: on $F=\mathbb Q^h$ with $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$, whose eigenvalues $1$ and $1-h/9=-91/9$ make it nondegenerate, $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$; complex network: on $\mathbb F_2^h$ with the dot product $t_T\cdot t_T=1$. In both, triple lines are nondegenerate and neighboring triple lines are orthogonal.",
              r"Thus every triple line is nondegenerate, and neighboring triple lines"),
        infer("S1.3.2",
              r"The terminal labels are $U_a$ (source) and $\mathcal F$ (sink) on $X_a$, $0$ and $U_a^\perp$ on $Y_a$, and $0$ and $\mathcal F$ on every scratch role; the source dimensions sum to $N$ and the sink dimensions to $Wm-N$, so the signed dimension changes sum to $Wm-2N$.",
              r"Write $W$ for the wire count in the construction under consideration."),
        infer("S1.3.3",
              r"At stage $j$, a data wire $X$ goes from $A\otimes\langle t\rangle\otimes Q$ to $(A\otimes F)\otimes Q$ and $Y$ from $B\otimes\langle t\rangle\otimes Q$ to $((B\otimes F)\perp(P\otimes t^\perp))\otimes Q$; with $A'=A\otimes F$, $P'=P\otimes\langle t\rangle$, $B'=(P')^\perp_{A'}$ the outgoing labels are exactly the next incoming labels, starting at $U_a,0$ and ending at $\mathcal F,U_a^\perp$.",
              r"These transitions expose one tensor factor at each stage. To see that"),
        infer("S1.3.4",
              r"In every invocation the gates touch the wires in the order $Y$-side, $Y$-center, $X$-side, $X$-center, $Y$-center, $Y$-side, $X$-center, $X$-side with common labels $B\otimes\langle t\rangle$, $B\otimes F$, $(B\otimes F)\perp(P\otimes\langle t\rangle)$, $A\otimes F$, $B\otimes F$, $(B\otimes F)\perp(P\otimes t^\perp)$, $A\otimes F$, $A\otimes F$ at times $0,\ldots,7$; a central wire returns once from $A\otimes F$ to $B\otimes F$, losing exactly $P\otimes F$.",
              r"The gate labels are organized by the decomposition"),
        s13_5,
        infer("S1.3.6",
              r"There are $Ic$ decreasing edges, each losing $h$, so $L=Ich$ and, replacing signed changes by absolute ones, the edges' absolute dimension changes sum to $Wm-2N+2L$.",
              r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
        infer("S1.3.7",
              r"Over $\mathbb F_2$ every nonzero residual is nonalternating (it contains a vector of norm one, e.g. a coordinate unit outside the supports) and nondegenerate, and every nondegenerate nonalternating binary symmetric space has an orthonormal basis.",
              r"For completeness, every nondegenerate nonalternating binary symmetric"),
        infer("S1.3.8",
              r"The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
              r"The loss ratios have the exact values"),
    ],
    page="subspace-labels",
    frm=["exchange-network", "frames", "inner-products-bilinear-forms-and-orthogonal-complements", "vector-spaces-subspaces-dimension-and-rank", "arithmetic-modulo-2-and-linear-algebra-over-f-2"],
    adds=[
        add(r"\mathcal F", "label space", "The ambient $m$-dimensional space $F^{\otimes3}$ with its tensor bilinear form, in which all labels are nondegenerate subspaces.", "direct"),
        add(r"t_T", "triple indicator", "The indicator vector in $F=\mathbb Q^h$ (or $\mathbb F_2^h$) of the three-element subset $T$.", "direct"),
        add(r"U_a", "bank line", "The line spanned by $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the label of source $X_a$.", "direct"),
        add(r"A", "exposed prefix", "The space $F^{\otimes(j-1)}$ of the factors already exposed at stage $j$, of dimension $a=h^{j-1}$.", "direct"),
        add(r"P", "prefix line", "The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.", "direct"),
        add(r"B", "prefix complement", "The orthogonal complement $P^\perp$ of $P$ inside $A$, with $A=B\perp P$.", "direct"),
        add(r"Q", "future line", "The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$ in the factors not yet exposed, of dimension at most $f=h^{3-j}$.", "direct"),
        add(r"L", "total loss", "The total dimension lost on all decreasing edges, $L=Ich$.", "count"),
        add(r"a", "prefix dimension", "The dimension $h^{j-1}$ of $A$ at stage $j$.", "count"),
        add(r"f", "future dimension", "The dimension $h^{3-j}$ of the tensor factors not yet exposed at stage $j$.", "count"),
    ],
    salient=r"Only one kind of edge in the whole network ever loses dimension, the central-wire edge from time 3 to time 4, and it always loses exactly $h$; every other edge only enlarges its label.")

# ---------------------------------------------------------------- S1.4 rank saving
s14_1 = show(
    "S1.4.1",
    r"For the bit network, assign the projection $P_U$ to every gate and sink with label $U$ and $-P_{U_a}$ to source $X_a$; then every input role has endpoint difference $M_{{\rm sink}(\rho(w))}-M_{{\rm source}(w)}=I_m$ and the total edge rank is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}=177176569088785861287000000<W_{\rm b}m$.",
    r"Compute each edge's rank as that of $P_V-P_U$, which equals the dimension change, and add the $N$ exceptional source edges whose rank exceeds their dimension change by one.",
    mot("A projection difference is the identity on the residual and zero elsewhere, so its rank equals the residual dimension; only the negated source projections break this.", "recoverable"),
    [
        infer("S1.4.1a",
              r"For nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, unchanged when the edge is reversed.",
              r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its"),
        infer("S1.4.1b",
              r"The $N$ source edges are exceptions: at stage 1, $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so the first edge matrix is $2P_{U_a}$, of rank one where the dimension change was zero. Hence $s_{\rm b}=(Wm-2N+2L_{\rm b})+N$, and the deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}$ is positive because $L_{\rm b}/N=100/539<1/2$.",
              r"At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$."),
        infer("S1.4.1c",
              r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix, which is the condition $M_{{\rm out}(\rho(w))}-M_{{\rm in}(w)}=I_m$ that makes the frame shear the same on every role.",
              r"For an input $X_a$ the endpoint difference is"),
    ])

s14_2 = show(
    "S1.4.2",
    r"For the complex network with binary labels and phase frames $\mathcal C_U$, each edge change is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of its residual, so the total number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$, and telescoping the frames gives $C^{\otimes m}$ on every role.",
    r"Use the weight function $q_U(x)=\mathrm{wt}(P_Ux)\bmod4$: weight is additive modulo four for orthogonal vectors, each basis vector $v$ has odd weight, so the phase change $i^{\pm[v\cdot x]}$ is a combination of $1$ and $(-1)^{v\cdot x}$, which the Hadamard transform turns into the translation kernel $aI+bX_v$.",
    mot("Phases $i^{\mathrm{wt}}$ turn orthogonality over $\mathbb F_2$ into additivity of weight mod 4, so an edge factorizes into one two-point kernel per residual direction.", "recoverable"),
    [
        infer("S1.4.2a",
              r"For binary $z,w$, $\mathrm{wt}(z+w)=\mathrm{wt}(z)+\mathrm{wt}(w)-2|\mathrm{supp}(z)\cap\mathrm{supp}(w)|$; if $z\cdot w=0$ the intersection is even, so weight is additive modulo four, giving $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\mathrm{wt}(v)[v\cdot x] \pmod 4$ for $V=U\perp E$ with $\mathcal B$ an orthonormal basis of $E$ (negated on decreasing edges).",
              r"If $z\cdot w=0$, the intersection cardinality is even, so weight is"),
        infer("S1.4.2b",
              r"Each $v$ has norm one, so $\mathrm{wt}(v)$ is odd and its coefficient is some $\varepsilon\in\{1,-1\}$ mod 4; $i^{\varepsilon[v\cdot x]}=\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$, and $H\,\mathrm{diag}(1,-1)H=X$ tensored over $\mathrm{supp}(v)$ sends $(-1)^{v\cdot x}$ to the translation $X_v$, so the factor becomes $aI+bX_v$ or its inverse; counting basis lengths with Lemma-level dimensions gives $s_{\rm c}$ with deficit $2N-2L_{\rm c}>0$.",
              r"The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the"),
        infer("S1.4.2c",
              r"The pair $X_a\to Y_a$ is the only route whose labels are neither zero nor full: with $u=u_a$ of binary norm one and weight $3^3=27$, orthogonal weight additivity gives $q_{U_a^\perp}-q_{U_a}=\mathrm{wt}(x)+2[u\cdot x] \pmod 4$, so the operator is $C^{-1}$ on the 27 coordinates of $\mathrm{supp}(u)$ and $C$ elsewhere.",
              r"Since $2[u\cdot x]\equiv2\sum_{j\in\operatorname{supp}(u)}x_j"),
        infer("S1.4.2d",
              r"With $Z=\mathrm{diag}(1,-1)$, $C=iZC^{-1}Z$, so applying $Z_{a,k}$ before the network at $X_a$ and $i^{27k}Z_{a,k}$ after it at $Y_a$ turns every inverse factor into $C$; negating the physical $X$ outputs and sending role $\rho(w)$ back to $w$ leaves $C^{\otimes mk}$ on every role, scratch roles included.",
              r"Only the physical $X$ outputs still carry the minus sign of the"),
    ])

s14_3 = show(
    "S1.4.3",
    r"With $\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$ the relative rank deficits, $\tau=\sigma=1-2^{-50}$ gives $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$.",
    r"Compare the deficits $\eta$ with $20\cdot2^{-50}$, and bound $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)$ from below using $m<2^{20}$ and $\log2<1$ so that $\log m<20$.",
    mot("It suffices to show the fixed rational power $m^\tau$ lies above the ratio $s/W=m(1-\\eta)$, which needs only integer comparisons.", "reconstructed"),
    [
        infer("S1.4.3a",
              r"Both exact relative deficits $\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$ are greater than $20\cdot2^{-50}$.",
              r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$."),
        infer("S1.4.3b",
              r"Since $m<2^{20}$ and $\log2<1$, $\log m<20$, hence $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)$ for either $\eta$.",
              r">m(1-20\cdot2^{-50})>m(1-\eta)"),
        infer("S1.4.3c",
              r"Consequently $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $0<\tau=\sigma<1$; $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence.",
              r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
    ])

s14 = show(
    "S1.4",
    r"The total rank $s$ of all edge changes is strictly less than $Wm$ in both networks, $s_{\rm b}<W_{\rm b}m$ and $s_{\rm c}<W_{\rm c}m$, and in fact $s/W<m^\tau$ for the rational exponents $\tau=\sigma=1-2^{-50}$.",
    r"Turn the dimension count of the labels into ranks of the matrices or kernels that implement each edge (rational projections for the bit network, orthonormal-basis kernels for the complex one), add them up, and compare the result with $Wm$ and with $m^\tau$.",
    mot("The extra $N$ source ranks of the bit network are paid for by the slack $L<N/2$.", "explicit",
        r"an additional $N$ source ranks, so this inequality will leave a strict"),
    [s14_1, s14_2, s14_3],
    page="rank-saving",
    frm=["subspace-labels", "frames", "exchange-network", "vector-spaces-subspaces-dimension-and-rank", "logarithms-exponentials-floors-and-ceilings", "inner-products-bilinear-forms-and-orthogonal-complements"],
    adds=[
        add(r"\sigma", "complex exponent", "The rational upper bound $1-2^{-50}$ for the logarithmic exponent of the complex recurrence, equal to $\\tau$.", "direct"),
        add(r"\eta", "relative rank deficit", "The relative deficit $(Wm-s)/(Wm)$ of the total edge rank, $\\eta_{\\rm b}=339/22587335000000$ for the bit network and $\\eta_{\\rm c}=73/19906842167500$ for the complex one.", "direct"),
    ],
    salient=r"The deficit is strict but tiny: $s/W$ misses the trivial value $m$ by a relative amount $\eta\approx1.5\times10^{-11}$ (bit network), so the exponent $\tau=1-2^{-50}$ is only barely below one; the whole power saving, and ultimately $\kappa=2^{-182}$, is as small as this slack allows.")
