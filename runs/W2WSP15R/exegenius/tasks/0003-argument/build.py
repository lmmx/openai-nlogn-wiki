import json, sys

SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E9F4Y/sources/paper.tex').read()

PAGES = """integer-multiplication-conjecture polynomial-ring-mod fixed-point-truncation established-multiplier tape-address-model elementary-stream-ops controlled-shift linear-algebra-basics linear-network address-shear common-frame-principle subset-intersection-labels rank-saving-recurrence address-chunk-interchange packed-selected-bit-addition signed-packing cyclic-convolution radix-digit-convolution phase-twist exact-recovery dft multidimensional-dft butterfly synthetic-transform bluestein-chirp phase-frame-kernel fast-butterfly-layer ring-convolution gaussian-resampling permutation-cancellation crt-address-map parameter-choice multiplication-algorithm time-accounting main-theorem""".split()
KNOWN = """big-o polynomials complex-numbers multitape-tm logarithms-and-iterated-logarithm-notation big-omega-theta-and-little-o-notation binary-representation-and-bit-operations modular-arithmetic primes-coprimality-and-gcd chinese-remainder-theorem roots-of-unity vectors-matrices-and-invertibility finite-field-f2-arithmetic permutations-and-cartesian-products floor-ceiling-and-summation-notation recurrences-and-induction norms-absolute-values-and-error-bounds fast-fourier-transform-and-divide-and-conquer sorting-and-data-movement-on-tapes finite-alphabet-encodings-and-constant-factor-simulation ring-and-group-notions-for-polynomials""".split()


def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


def ev(q):
    return {"source": "paper", "quote": q}


def I(id, claim, q, page=None, frm=None, salient=None, deferred=False, adds=None):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": ev(q)}
    if page: d["page"] = page
    if frm: d["from"] = frm
    if salient: d["salient"] = salient
    if deferred: d["deferred"] = True
    if adds: d["adds"] = adds
    return d


def S(id, claim, method, mot, children, page=None, frm=None, salient=None, adds=None):
    text, src, q = mot
    m = {"text": text, "source": src}
    if q: m["quote"] = ev(q)
    d = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m, "children": children}
    if page: d["page"] = page
    if frm: d["from"] = frm
    if salient: d["salient"] = salient
    if adds: d["adds"] = adds
    return d


# ---------------------------------------------------------------- key step: networks
K1 = S("S4.1",
       "A fixed linear network on $W$ wires, built from three stages of an eight-row schedule per invocation, sends $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ (a pure exchange of the two data banks over $\\mathbb F_2$) and restores every scratch wire, whatever its initial value.",
       "Give each invocation copy, gather, scatter and side-injection gates whose net effect on a target is $y_S\\gets y_S+x_S$ independent of the scratch values (subtract the old scratch effect, add the new one, undo it), then chain three such updates $y\\gets y+x$, $x\\gets x-y$, $y\\gets y+x$ to exchange the banks.",
       ("The sources say the schedule first cancels the arbitrary old scratch values, then adds the source values' effect, then restores the scratch values.", "explicit",
        r"the following schedule remove the effect of the old scratch values;"),
       [
           I("S4.1.1",
             "Fixed constants of the construction: ground set size $h=100$, number of 3-subsets $v=\\binom h3=161700$, number of index triples $N=v^3=4227952113000000$, label-space dimension $m=h^3=1000000$.",
             r"h=100,\qquad v=\binom h3=161700,\qquad"),
           I("S4.1.2",
             "The three stages (one per coordinate $j$ of $a\\in\\mathcal T^3$) comprise $I=3v^2=78440670000$ invocations, each with its own scratch wires, so that each invocation updates $v$ values of a bank at a time.",
             r"I=3v^2=78440670000"),
           I("S4.1.3",
             "Bit construction over $\\mathbb F_2$: triples $S,T$ are neighbors when $|S\\cap T|=1$; copy adds $x_T$ to the scratch wire $A_{ST}$, side injection adds $\\sum_{T:|S\\cap T|=1}A_{ST}$ to $y_S$, gather adds $\\sum_{T\\ni i}x_T$ to a central wire $C_i$ and scatter adds $\\sum_{i\\in S}C_i$ to $y_S$.",
             r"The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair."),
           I("S4.1.4",
             "Complex construction over $\\mathbb Z[i,1/2]$: neighbors are distinct triples with even intersection, the side injection has coefficient $-(|S\\cap T|-1)/2$, and an extra central wire $C_\\ast$ makes the scatter add $(\\sum_{i\\in S}C_i-C_\\ast)/2$.",
             r"-\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST}"),
           I("S4.1.5",
             "The eight-row forward schedule is: subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy; the first two rows remove the effect of the old scratch values and the last two restore them.",
             r"0&\text{subtract side injection}&\text{one gate per target}\\"),
           I("S4.1.6",
             "The net change of the target is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$ (side injection times copy plus scatter times gather), independent of the initial scratch values $a,c$, because rows 0-1 subtract exactly the old contribution.",
             r"$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$"),
           I("S4.1.7",
             "Bit case: the central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod2$; the side injection cancels the intersection-one cases, intersection zero or two already give zero, and the self coefficient is one, so the net map is $y\\gets y+x$.",
             r"In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
           I("S4.1.8",
             "Complex case: the central coefficient is $(|S\\cap T|-1)/2$; the side wires cancel it for distinct triples with intersection zero or two, intersection one contributes zero, and the self coefficient is one, so again the net map is $y\\gets y+x$.",
             r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$."),
           I("S4.1.9",
             "Three stages starting from $(x,y)$ give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$: the signed exchange $(X_a,Y_a)\\mapsto(-Y_a,X_a)$, with every invocation restoring its own scratch wires.",
             r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
           I("S4.1.10",
             "Wire counts: a triple has $z_{\\rm b}=3\\binom{97}{2}=13968$ bit-neighbors and $z_{\\rm c}=\\binom{97}{3}+3\\cdot97=147731$ complex neighbors, with $c_{\\rm b}=100$, $c_{\\rm c}=101$ central wires per invocation, giving $W_{\\rm b}=2N+I(vz_{\\rm b}+c_{\\rm b})=177176569091445000000$ and $W_{\\rm c}=2N+I(vz_{\\rm c}+c_{\\rm c})=1873807244643542670000$.",
             r"W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})"),
       ],
       page="linear-network",
       frm=["finite-field-f2-arithmetic", "vectors-matrices-and-invertibility", "permutations-and-cartesian-products", "tape-address-model"],
       adds=[B("h", "ground-set size", "The size 100 of the ground set from which three-element subsets are drawn."),
             B("v", "subset count", "The number $\\binom h3=161700$ of three-element subsets of $[h]$.", "count"),
             B("N", "triple count", "The number $v^3$ of index triples $a$, i.e. of entries of each data bank.", "count"),
             B("I", "invocation count", "The number $3v^2$ of separate invocations of the eight-row schedule over the three stages.", "count")])

K2 = S("S4.2",
       "Replacing each scalar of the network by an array and giving every vertex $v$ an invertible linear frame $D_v$ makes the implemented operator $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so only the endpoint frames matter and each edge pays only the change of frame $D_vD_u^{-1}$.",
       "Show by induction along the wires that the stored array is $D_v$ applied to the logical array, using that a pointwise linear gate commutes with a frame common to all its incidences; then read off the operator on each route of the signed role permutation.",
       ("The sources say that once routing is fixed the endpoint frames determine the operator on each route and the intermediate frames can be chosen freely to make edges cheap.", "explicit",
        r"the endpoint frames determine the array operator on each route; the"),
       [
           I("S4.2.1",
             "Invariant: at every vertex $v$ the stored array equals $D_v$ applied to the logical array; it holds at sources by definition of the logical input $g=D_{\\rm in}^{-1}f$, passes along an edge by applying $D_vD_u^{-1}$, and passes through a gate because $G(D_vg_1,\\dots,D_vg_t)=D_vG(g_1,\\dots,g_t)$; hence the network implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$.",
             r"The implemented operator is therefore"),
           I("S4.2.2",
             "For a signed role permutation sending input role $w$ to output role $\\rho(w)$ with sign $\\varepsilon_w$, the route applies $\\varepsilon_wD_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$ to its array, auxiliary roles included, so the intermediate frames can be chosen purely for cheap edges.",
             r"$\varepsilon_wD_{\mathrm{sink}(\rho(w))}"),
       ],
       page="common-frame-principle",
       frm=["linear-network", "vectors-matrices-and-invertibility", "permutations-and-cartesian-products"],
       salient="Every intermediate frame cancels: whatever frames are placed on the interior vertices, each role receives the same endpoint operator, so the interior frames can be chosen only to make each edge cheap.",
       adds=[B("D_v", "frame", "An invertible linear operator on arrays indexed by the common address set, attached to a source, gate or sink $v$; the stored array is $D_v$ applied to the logical array.")])

K3_4 = S("S4.3.4",
         "Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to time 4 (each losing exactly $h$ dimensions), so $L=Ich$ and the sum of absolute dimension changes is $Wm-2N+2L$.",
         "Tabulate the orthogonal residual of every edge from the stage transitions and the gate-label table, observe where dimension drops, and telescope the signed changes through the gates.",
         ("A reader can verify the table row by row; the sources do not say why they tabulate it, but the total is needed to bound the number of smaller calls.", "recoverable", None),
         [
             I("S4.3.4.1",
               "Gate labels by time in an invocation (suppressing the factor $Q$): time 0 $B\\otimes\\langle t\\rangle$ on $Y$ side wires, time 1 $B\\otimes F$ on $Y$ and central wires, time 2 $(B\\otimes F)\\perp(P\\otimes\\langle t\\rangle)$ on $X$ side wires, time 3 $A\\otimes F$ on $X$ and central wires, time 4 $B\\otimes F$, time 5 $(B\\otimes F)\\perp(P\\otimes t^\\perp)$, time 6 $A\\otimes F$, time 7 $A\\otimes F$.",
               r"0&Y,\ \text{its side wires}&B\otimes\langle t\rangle\\"),
             I("S4.3.4.2",
               "The side edge from time 2 to time 5 uses the neighbor relation essentially: neighbors have orthogonal indicators $t_X\\perp t_Y$, hence $\\langle t_X\\rangle\\subset t_Y^\\perp$ and the labels are nested, with residual $P\\otimes\\langle t_X,t_Y\\rangle^\\perp$ of dimension $h-2$.",
               r"The side edge $2\to5$ uses the neighbor relation"),
             I("S4.3.4.3",
               "Label dimension is nondecreasing along every edge except the central edge $3\\to4$, which removes $P\\otimes F\\otimes Q$, of dimension $h$; there are $Ic$ such edges ($c$ central wires per invocation), so $L=Ich$.",
               r"Label dimension is nondecreasing along every edge except center $3\to4$, which removes"),
             I("S4.3.4.4",
               "The signed sum of dimension changes telescopes at every gate (each touched wire has one incoming and one outgoing incidence with the same gate label); sources total $N$ and sinks $Wm-N$, so the signed increase is $Wm-2N$, and using absolute values adds $2L$.",
               r"The signed sum of dimension changes telescopes at every gate: each"),
             I("S4.3.4.5",
               "Over $\\mathbb F_2$ every nonzero residual is nondegenerate and nonalternating (it contains a coordinate unit vector of norm one), hence has an orthonormal basis, which the complex phase interface needs.",
               r"is nonalternating precisely when it contains a vector of norm one."),
         ],
         salient="All dimension is lost on a single edge per central wire (the return from time 3 to time 4, losing exactly $h$), so the total loss is only a small fraction of $N$.")

K3_6 = S("S4.3.6",
         "Bit network, rational interface: assign to each vertex the projection matrix $P_U$ onto its label (and $-P_{U_a}$ at the source of $X_a$); then $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ for every input role and the sum of rational ranks of edge differences is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
         "Use the frame $\\Phi_M:(H,D)\\mapsto(H+MD,D)$ with $M_v=P_{U_v}$: the rank of $P_V-P_U$ equals the dimension change, except for the $N$ negative source projections, each costing one extra rank.",
         ("Taking projections as matrices makes each edge difference have rank equal to the label dimension change, which is what the dimension count of the labels bounds.", "recoverable", None),
         [
             I("S4.3.6.1",
               "Endpoint identity required by the tape application: $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ for every input role $w$, so every role receives the same shear $H\\gets H+D$.",
               r"M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m"),
             I("S4.3.6.2",
               "The total rank is $s_{\\rm b}=\\sum_e\\operatorname{rank}_{\\mathbb Q}(M_{\\mathrm{head}(e)}-M_{\\mathrm{tail}(e)})=W_{\\rm b}m-N+2L_{\\rm b}=177176569088785861287000000<W_{\\rm b}m$.",
               r"&=W_{\rm b}m-N+2L_{\rm b}"),
             I("S4.3.6.3",
               "For nondegenerate $U\\subset V$, $P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its orthogonal complement, so its rank is $\\dim V-\\dim U$, and reversing an edge only negates it.",
               r"$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its"),
             I("S4.3.6.4",
               "The only exceptions are the $N$ source edges: at stage 1, $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so its first edge matrix $2P_{U_a}$ has rank one although the dimension change is zero; this adds $N$ to the dimension count.",
               r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,"),
             I("S4.3.6.5",
               "Endpoint check: for $X_a$ the difference is $P_{U_a^\\perp}-(-P_{U_a})=I_m$, and every other role has source matrix zero and sink matrix identity.",
               r"For an input $X_a$ the endpoint difference is"),
         ])

K3_7 = S("S4.3.7",
         "Complex network, binary phase interface: with frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}_x(i^{q_U(x)})H^{\\otimes m}$ ($q_U(x)=\\operatorname{wt}(P_Ux)\\bmod4$), each edge change factors into one two-point kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of its residual, the total count is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$, and after source/sink corrections every role receives $C^{\\otimes m}$.",
         "Use Hamming-weight additivity modulo 4 for orthogonal vectors to turn the phase difference of an edge into a sum over residual basis vectors, each of which is a kernel $C=aI+bX$; fix up the one pair $X_a\\to Y_a$ with $C=iZC^{-1}Z$.",
         ("Weight is additive modulo four on orthogonal binary vectors, so label nesting translates into products of kernels, one per residual dimension.", "recoverable", None),
         [
             I("S4.3.7.1",
               "Definition of the phase frame: $q_U(x)=\\operatorname{wt}(P_Ux)\\pmod4$ (projection over $\\mathbb F_2$), with $C=H\\operatorname{diag}(1,i)H=aI+bX$, $a=(1+i)/2$, $b=(1-i)/2$, and $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}_x(i^{q_U(x)})H^{\\otimes m}$ with Gaussian-dyadic entries.",
               r"q_U(x)=\operatorname{wt}(P_Ux)\pmod4."),
             I("S4.3.7.2",
               "The sum of residual-basis lengths over all edges is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}=1873807244636671267308000000<W_{\\rm c}m$ (deficit $2N-2L_{\\rm c}>0$).",
               r"s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}"),
             I("S4.3.7.3",
               "For binary $z,w$, $\\operatorname{wt}(z+w)=\\operatorname{wt}(z)+\\operatorname{wt}(w)-2|\\operatorname{supp}(z)\\cap\\operatorname{supp}(w)|$, and for $z\\cdot w=0$ the intersection is even, so weight is additive modulo four.",
               r"=\operatorname{wt}(z)+\operatorname{wt}(w)"),
             I("S4.3.7.4",
               "For $V=U\\perp E$ with orthonormal basis $\\mathcal B$ of $E$: $q_V(x)-q_U(x)=\\sum_{v\\in\\mathcal B}\\operatorname{wt}(v)[v\\cdot x]\\pmod4$ (negated on a decreasing edge), and each $\\operatorname{wt}(v)$ is odd since $v$ has norm one.",
               r"q_V(x)-q_U(x)=\sum_{v\in\mathcal B}"),
             I("S4.3.7.5",
               "Each factor $i^{\\varepsilon[v\\cdot x]}$ equals $\\frac{1+i^\\varepsilon}{2}+\\frac{1-i^\\varepsilon}{2}(-1)^{v\\cdot x}$, and $H\\operatorname{diag}(1,-1)H=X$ turns the character $(-1)^{v\\cdot x}$ into the translation $X_v$, giving the kernel $aI+bX_v$ or its inverse.",
               r"\frac{1+i^\varepsilon}{2}"),
             I("S4.3.7.6",
               "The pair $X_a\\to Y_a$ gets $C^{-1}$ on the 27 coordinates of $\\operatorname{supp}(u_a)$ and $C$ elsewhere; the identity $C=iZC^{-1}Z$ (with $Z=\\operatorname{diag}(1,-1)$) converts each inverse factor to $C$ using signs $Z_{a,k}$ before the network and $i^{27k}Z_{a,k}$ after it.",
               r"C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ."),
             I("S4.3.7.7",
               "After negating the physical $X$ outputs and sending output role $\\rho(w)$ back to $w$, every role, scratch roles included, carries the forward tensor product $C^{\\otimes m}$ (and $C^{\\otimes mk}$ on $k$ columns).",
               r"Negate those outputs and send output role $\rho(w)$"),
         ])

K3 = S("S4.3",
       "Nested nondegenerate subspace labels, spanned by indicator vectors of 3-element subsets and attached to gates and terminals, give the networks total edge rank $s_{\\rm b}<W_{\\rm b}m$ and $s_{\\rm c}<W_{\\rm c}m$ because the total dimension $L$ lost on decreasing edges is $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, below $N/2$.",
       "Label every vertex with a subspace of $F^{\\otimes3}$ built from the indicators $t_T$ of triples, so that neighboring triples are orthogonal and labels nest along every edge; then the orthogonal residual of an edge has dimension equal to the label change, and the edge cost (its rank) equals that dimension.",
       ("The sources say the saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.", "explicit",
        r"The saving will come from keeping the total dimension lost on decreasing"),
       [
           I("S4.3.1",
             "Bilinear spaces: $F=\\mathbb Q^h$ with $\\langle x,y\\rangle=x^{\\mathsf T}(I-J/9)y$ (bit network) or $F=\\mathbb F_2^h$ with the dot product (complex network); triple indicators satisfy $\\langle t_S,t_T\\rangle=|S\\cap T|-1$ over $\\mathbb Q$, so every triple line is nondegenerate and neighboring triple lines are orthogonal; labels live in $\\mathcal F=F^{\\otimes3}$ of dimension $m$ with $u_a=t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$.",
             r"\langle t_S,t_T\rangle=|S\cap T|-1,"),
           I("S4.3.2",
             "Terminal labels: source $U_a$ and sink $\\mathcal F$ for $X_a$, source $0$ and sink $U_a^\\perp$ for $Y_a$, source $0$ and sink $\\mathcal F$ for each scratch role; source dimensions sum to $N$ and sink dimensions to $Wm-N$.",
             r"The source dimensions sum to $N$ and the sink dimensions to $Wm-N$."),
           I("S4.3.3",
             "Stage transitions expose one tensor factor at a time: with $A=F^{\\otimes(j-1)}$, $P=\\langle t_{a_1}\\otimes\\cdots\\otimes t_{a_{j-1}}\\rangle$, $B=P^\\perp\\subset A$, the next stage has $A'=A\\otimes F$, $P'=P\\otimes\\langle t\\rangle$, $B'=(P')^\\perp_{A'}$, so outgoing labels equal the next incoming labels.",
             r"A'=A\otimes F,\qquad"),
           K3_4,
           I("S4.3.5",
             "Loss ratios: $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$ (with $L=Ich$), both smaller than $1/2$; the rational interface adds only $N$ more source ranks, so a strict saving remains in both constructions.",
             r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad"),
           K3_6,
           K3_7,
       ],
       page="subset-intersection-labels",
       frm=["linear-algebra-basics", "linear-network", "common-frame-principle", "finite-field-f2-arithmetic", "vectors-matrices-and-invertibility"],
       salient="The dimension lost on decreasing edges is only a fraction $100/539$ (bit) or $101/539$ (complex) of $N$, below $1/2$, so total rank falls strictly below $Wm$ even after the $N$ extra source ranks.",
       adds=[B("L", "decreasing loss", "The total dimension lost on decreasing edges of the label assignment.", "count"),
             B("t_T", "triple indicator", "The indicator vector in $F^h$ of a three-element subset $T$ of $[h]$.")])

K4 = S("S4.4",
       "With $\\tau=\\sigma=1-2^{-50}$ one has $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$, because both relative rank deficits $\\eta_{\\rm b}=339/22587335000000$ and $\\eta_{\\rm c}=73/19906842167500$ exceed $20\\cdot2^{-50}$.",
       "Bound $m^{1-2^{-50}}=m\\exp(-2^{-50}\\log m)>m(1-20\\cdot2^{-50})$ from below using $\\log m<20$, and compare with $m(1-\\eta)$.",
       ("Since the strict inequality is exact rational arithmetic, a fixed exponent below 1 can be read off by comparing the deficit with the first-order loss in $m^{-2^{-50}}$.", "recoverable", None),
       [
           I("S4.4.1", "The relative rank deficits are $\\eta=(Wm-s)/(Wm)$, equal to $339/22587335000000$ for the bit network and $73/19906842167500$ for the complex network, both greater than $20\\cdot2^{-50}$.",
             r"\eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m}"),
           I("S4.4.2", "Since $m<2^{20}$ and $\\log 2<1$, we have $\\log m<20$.",
             r"Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence"),
           I("S4.4.3", "Hence $m^{1-2^{-50}}=m\\exp(-2^{-50}\\log m)>m(1-20\\cdot2^{-50})>m(1-\\eta)$ for either deficit $\\eta$.",
             r"=m\exp(-2^{-50}\log m)"),
           I("S4.4.4", "Consequently $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ with $0<\\tau=\\sigma=1-2^{-50}<1$.",
             r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,"),
       ],
       salient="The relative deficits are only of order $10^{-11}$, yet a fixed exponent $1-2^{-50}$ below one suffices because $m^{-2^{-50}}$ loses about $20\\cdot2^{-50}$ of $m$.")

# ---- bit variant: address chunk interchange
K5_1 = S("S4.5.1",
         "A rational shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ by a rank-$a$ matrix $A$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
         "Factor $A=E_1\\Pi E_2$ with lower-triangular invertible $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones; the triangular parts are controlled shifts in tape order, and each one in $\\Pi$ is one field interchange.",
         ("Lower triangular changes of coordinates update a later field from earlier ones, which is the direction in which a tape can do it in linear time.", "explicit",
          r"can be performed entirely in this direction."),
         [
             I("S4.5.1.1", "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ having exactly $a$ ones, at most one per row and column (Bruhat factorization with reversed coordinate order).",
               r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"),
             I("S4.5.1.2", "Elimination picks the topmost nonzero row and its rightmost nonzero entry, clears its column to the left by right multiplication and below by left multiplication with lower triangular elementary matrices, scales the pivot to one, deletes that row and column, and repeats; the number of pivots is the rank.",
               r"nonzero row and its rightmost nonzero entry."),
             I("S4.5.1.3", "A fixed odd prime $q$ avoiding all denominators and diagonal numerators in a finite table of factors lets all rational identities specialize to $\\mathbb Z/q^b\\mathbb Z$ with the triangular factors invertible.",
               r"Choose an odd prime avoiding every denominator"),
             I("S4.5.1.4", "A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, each by a diagonal unit and a fixed combination of earlier coordinates (controlled shifts).",
               r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
             I("S4.5.1.5", "Each one at position $(i,j)$ of $\\Pi$ calls for $H_i\\gets H_i+D_j$, done by $D_j\\gets D_j+H_i$, then interchanging $(H_i,D_j)$, then $D_j\\gets H_i-D_j$; from $(h,d)$ this gives $(h+d,d)$ using just one interchange, so $a$ ones cost $a$ interchanges.",
               r"D_j\leftarrow D_j+H_i,\qquad"),
             I("S4.5.1.6", "Three shears $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ interchange $H$ and $D$; only the middle shear needs the network, the other two target the later group and have linear cost.",
               r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,", deferred=True),
         ],
         page="address-shear",
         frm=["controlled-shift", "linear-algebra-basics", "modular-arithmetic"],
         salient="The number of expensive operations is the rank $a$ of the matrix, not its size $m$: a rank-$a$ shear needs only $a$ field swaps.")

K5_2g = S("S4.5.2.7",
          "The recurrence $F_0=O(1)$, $F_k\\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\\tau$ solves to $F_k=O(e^\\tau)$.",
          "Unroll it into the geometric sum $\\sum_{j=0}^k a^j$ with $a=s/W$ and bound it separately for $a\\le1$ and $a>1$.",
          ("A linear recurrence with ratio $a$ unrolls to a geometric sum, dominated by its last term when $a>1$.", "recoverable", None),
          [
              I("S4.5.2.7.1", "Each of the $s$ recursive calls acts on one role stream of volume $V/W$, so dividing by $V$ gives $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
                r" F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
              I("S4.5.2.7.2", "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$: at most $k+1=O(m^{k\\tau})$ if $a\\le1$, and $O(a^k)$ if $a>1$.",
                r"For $a=s/W<m^\tau$ the geometric sum"),
              I("S4.5.2.7.3", "Hence $F_k=O(e^\\tau)$ for $e=m^k$, i.e. time $O(Ve^\\tau)$.",
                r"Hence $F_k=O(e^\tau)$."),
          ],
          salient="Since $a<m^\\tau$ with $\\tau<1$, multiplying the width by $m$ multiplies the per-volume cost by less than $m$, which is exactly what makes the cost a power $e^\\tau$ below linear.")

K5_2h = S("S4.5.2.8",
          "Scheduling the recursive calls on a fixed number of tapes costs only $O(V)$ at each node, so the additive term of the recurrence is valid and temporary storage is not charged to volume.",
          "Keep role streams on a parking stack and descriptors on a separate stack, so each call moves only its own volume; bound descriptor work by a power of $\\log V_j$.",
          ("The recurrence's additive $O(V)$ assumes each call touches only its own streams, which a stack discipline guarantees.", "recoverable", None),
          [
              I("S4.5.2.8.1", "Reserve $W$ role tapes, work tapes, a parking stack and a descriptor stack; before a recursive call park the $W-1$ inactive streams, copy the active stream to the child I/O area, and restore afterwards, never sweeping parked ancestors.",
                r"Reserve $W$ role tapes, a fixed set of"),
              I("S4.5.2.8.2", "Each push, pop, copy, positioning or erasure moves $O(V)$ symbols at a parent node and there are only the fixed number $s$ of child calls, giving precisely the extra $O(V)$ term.",
                r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
              I("S4.5.2.8.3", "Descriptor processing fits too: with $V_j=V_0/W^j$ and $j\\le\\log_m e_0$ we have $V_j\\ge q^{2e_0}$ and $j\\log W=O(e_0)=O(\\log V_j)$, so $\\log V_0=O(\\log(2V_j))$ and descriptor work $(\\log(2V_0))^{O(1)}=O(V_j)$.",
                r"V_j\ge q^{2e_0},\qquad"),
          ])

K5_2 = S("S4.5.2",
         "Power-width interchange: for $e=m^k$ and a row field divisible by $W^k$, two chunks of $e$ radix-$q$ digits are interchanged in $O(Ve^\\tau)$ time.",
         "Induct on $k$: split rows cyclically into $W$ role streams of volume $V/W$, run the bit network with the frame $\\Phi_{M_v}$ so that each edge $e$ applies the shear $\\Phi_{A_e}$ via Lemma on matrix shears (smaller interchanges), and obtain the full interchange from three shears.",
         ("The sources reduce width $e$ to widths $e/m$ on streams of volume $V/W$, which is a recursion with $s$ calls, not a stated motivation; the reason is worked out from the counts.", "recoverable", None),
         [
             I("S4.5.2.1", "Split whole rows cyclically into $W$ role streams within each prefix, writing the row number as $r=Wg+(w-1)$; all streams have the same shape and volume $V/W$, and row counts divisible by $W^{k-1}$.",
               r"Split whole rows cyclically into $W$ role streams within each prefix"),
             I("S4.5.2.2", "Apply $\\Phi_{A_e}$ to each edge's role stream (implemented by the shear lemma with recursive interchanges of pivot pairs of $b=e/m$ digit fields) and run every circuit gate pointwise at matching addresses.",
               r"$\Phi_{A_e}$ to that role stream; implement it by"),
             I("S4.5.2.3", "By the frame identity with $M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$, the physical output is $f'_{\\rho(w)}=\\Phi_{I_m}f_w$, i.e. $H\\gets H+D$ on every row, including rows serving as scratch roles with arbitrary contents; merging returns each row to its original place.",
               r"=\Phi_{I_m}f_w,"),
             I("S4.5.2.4", "The interchange is $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ componentwise, and only the middle shear uses the circuit; the other two updates target the later group and cost $O(V)$.",
               r"updates target the later group and have linear cost."),
             I("S4.5.2.5", "The number of recursive calls equals the sum of the edge ranks, exactly $s$, each on one role stream of volume $V/W$.",
               r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
             K5_2g,
             K5_2h,
         ],
         adds=[B("e", "chunk length in digits", "The number $m^k$ of radix-$q$ digits in each of the two interchanged chunks.", "count"),
               B("k", "recursion depth", "The exponent with $e=m^k$, i.e. the number of recursion levels.", "count"),
               B("F_k", "cost per volume", "A uniform upper bound for time divided by logical volume for width $e=m^k$.")])

K5_3 = S("S4.5.3",
         "Any equal-width interchange $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ of two $u$-bit chunks costs $O(Vu^\\tau)$, $\\tau=1-2^{-50}$, for arbitrary $P,G,B$ and $u\\ge1$ (including $B=1$).",
         "Take the top $\\rho$ digits of both chunks as an ad-hoc row field, pad rows to a multiple of $W^k$, split the remaining width into base-$m$ pieces handled by the power-width interchange, and pad binary ranges up to $q^e$.",
         ("The sources say general arrays can be given enough rows from their own high digits, whose movement is cheap.", "explicit",
          r"Rows for a general array can be supplied by a few of its own high digits."),
         [
             I("S4.5.3.1", "Set $k=\\lceil\\log_m e\\rceil$ and $\\rho=\\lceil k\\log W/(2\\log q)\\rceil$, so $1\\le\\rho<e$ and $\\rho=O(\\log(2e))$ for all large $e$; the bounded remaining widths use $e$ single-digit interchanges.",
               r"k=\lceil\log_m e\rceil,\qquad"),
             I("S4.5.3.2", "Exchange the top $\\rho$ digits of the two chunks and join them: field orders $(h^+,h^-,g,d^+,d^-)\\to(d^+,h^+,h^-,g,d^-)\\to(d^+,h^+,d^-,g,h^-)\\to(d^+,d^-,g,h^+,h^-)$, costing $O(V\\rho)$.",
               r"\text{after exchanging and joining the high parts}"),
             I("S4.5.3.3", "In the two middle orders the first two fields form a row field of range $R=q^{2\\rho}\\ge W^k$ before both remaining chunks.",
               r"R=q^{2\rho}\ge W^k"),
             I("S4.5.3.4", "Pad zero rows within each prefix to $R'=W^k\\lceil R/W^k\\rceil<2R$, so the row count is divisible by $W^k$ and padded volume is less than $2V$.",
               r"R'=W^k\left\lceil R/W^k\right\rceil<2R."),
             I("S4.5.3.5", "Write the remaining width in base $m$: $e-\\rho=\\sum_{j=0}^k a_jm^j$ with $0\\le a_j<m$, and split each chunk into $a_j$ consecutive pieces of width $m^j$.",
               r"e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m."),
             I("S4.5.3.6", "Applying the power-width interchange to each piece pair costs $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^\\tau)$, a geometric sum since $a_j<m$ and $m^k<me$.",
               r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
             I("S4.5.3.7", "For binary chunks, pad each range $[2^u]$ up to $[q^e]$ with $q^e\\ge2^u$ minimal (volume grows by less than $q^2$, a fixed factor), interchange, and scan the invalid entries away; since $e=O(u)$ the cost is $O(Vu^\\tau)$.",
               r"Finally, for binary chunks let $e$ be the least integer with"),
             I("S4.5.3.8", "Chunks differing by one bit in width are handled by one single-bit move ($O(V)$) before or after an equal-width interchange.",
               r"For widths differing by one bit, choose the leading bit of the longer"),
         ])

K5 = S("S4.5",
       "Fast address-chunk interchange: swapping two disjoint contiguous address fields of $u$ bits, $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$, takes $O(Vu^\\tau)$ time with $\\tau=1-2^{-50}$.",
       "Run the bit network with address-shear frames, so that an edge matrix of rank $a$ costs $a$ smaller interchanges on role streams of volume $V/W$; solve the resulting recurrence, then remove the power-width and row restrictions.",
       ("The sources say an edge matrix of rank $a$ requires $a$ smaller interchanges, and the rank sum is below $Wm$, which saves a power of the chunk width.", "explicit",
        r"An edge matrix of rank $a$ will require $a$ smaller interchanges."),
       [K5_1, K5_2, K5_3],
       page="address-chunk-interchange",
       frm=["address-shear", "controlled-shift", "elementary-stream-ops", "linear-network", "common-frame-principle", "rank-saving-recurrence"],
       adds=[B("u", "chunk width", "The number of address bits in each of the two interchanged chunks.", "count")])

# ---- complex variant: fast butterfly layer
K6_1 = S("S4.6.1",
         "Phase frames in butterfly form: $C=H\\mathsf SH=aI+bX$ satisfies $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$, $C^4=I$, $C^{-1}=-iZCZ$; an edge change is $\\mathcal P_M(\\prod_jC_{e_j}^{\\epsilon_j})\\mathcal P_M^{-1}$ with $M\\in\\operatorname{GL}(m,\\mathbb F_2)$; on a group of $e=mf$ axes this needs $s_{\\rm c}$ child layers on $f$ axes, and $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$.",
         "Express each edge's residual operator as a product of kernels along residual basis vectors, rotate the basis into coordinate position by an invertible $\\mathbb F_2$ matrix (a product of row additions of whole slots), and convert the final $C$ layer to the normalized $H_0$ layer by diagonal phases.",
         ("The sources say the phase identities express an edge's residual operator as a product of two-point kernels on selected directions.", "explicit",
          r"identities below express an edge's residual operator as a product of"),
         [
             I("S4.6.1.1", "Definitions: $H_0=\\frac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$, $H=\\sqrt2H_0$, $\\mathsf S=\\operatorname{diag}(1,i)$, $C=H\\mathsf SH=aI+bX$ with $a=\\frac{1+i}2$, $b=\\frac{1-i}2$.",
               r"C=H\mathsf SH=aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}."),
             I("S4.6.1.2", "Direct multiplication gives $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=bI+aX=-iZCZ$, using only Gaussian dyadic coefficients.",
               r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
             I("S4.6.1.3", "For $M\\in\\operatorname{GL}(m,\\mathbb F_2)$ and the address permutation $\\mathcal P_M$ moving $x$ to $Mx$, $\\mathcal P_MX_v\\mathcal P_M^{-1}=X_{Mv}$; extending the residual basis to the columns of $M$ gives the coordinate form of the edge change, and $M$ need not preserve the dot product.",
               r"\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}."),
             I("S4.6.1.4", "Take a group of $e=mf$ consecutive axis chunks as $m$ slots of $f$ chunks; apply $\\mathcal P_M^{-1}$ to each column $(x_{1,j},\\dots,x_{m,j})$, then one child layer $(C^{\\epsilon_h})^{\\otimes f}$ on the $f$ bits of slot $h$ for each residual basis vector, then $\\mathcal P_M$.",
               r"take a group of $e=mf$ consecutive"),
             I("S4.6.1.5", "A negative kernel needs only one forward child: $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$, where the wrappers are address signs and fourth-root phases adding no recursive calls.",
               r"=(-i)^f Z^{\otimes f}C^{\otimes f}Z^{\otimes f}."),
             I("S4.6.1.6", "Gaussian elimination writes $M$ as at most $m(m-1)+3m$ elementary row additions (a row swap is three), a constant since $m$ is fixed; one row addition changes corresponding selected positions in two whole slots.",
               r"as a product of at most $m(m-1)+3m$ elementary row additions"),
             I("S4.6.1.7", "Summing residual dimensions of the finite complex network gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and with the endpoint signs every role receives $C^{\\otimes e}$, scratch roles with arbitrary initial values included.",
               r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
             I("S4.6.1.8", "Applying the identities on all selected coordinates gives $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ with $(\\mathcal S_Dz)(x)=i^{x_1+\\cdots+x_D}z(x)$ and $b^D=(-i/2)^{\\lfloor D/2\\rfloor}b^{D\\bmod2}$, a binary shift and fourth-root phase.",
               r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
         ],
         page="phase-frame-kernel",
         frm=["subset-intersection-labels", "common-frame-principle", "linear-network", "butterfly", "linear-algebra-basics", "finite-field-f2-arithmetic"],
         adds=[B("a", "kernel coefficient", "The coefficient $(1+i)/2$ of the identity in the kernel $C=aI+bX$."),
               B("b", "kernel coefficient", "The coefficient $(1-i)/2$ of the flip $X$ in the kernel $C=aI+bX$.")])

K6_2 = S("S4.6.2",
         "Packed selected-bit addition: for $L=fK$, a binary row addition $y_{j_i}\\gets y_{j_i}\\oplus x_{j_i}$ ($j_i=\\rho+iK$, $0\\le i<f$) on chunks $x,y$ with an arbitrary third chunk $z$ restored costs $O(V(L^\\tau+1))$.",
         "Realize the XORs as eight whole-chunk cyclic shifts (in which $K$-bit segments cannot carry into each other except at a small set $\\mathcal B$ of addresses), compute the exact correction on $\\mathcal B$ by extraction, radix sorting and reinsertion, and bound $|\\mathcal B|$ by a union bound.",
         ("The sources say they use a constant number of cyclic shifts of whole chunk ranges and then correct an explicitly bounded set of addresses.", "explicit",
          r"cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of"),
         [
             I("S4.6.2.1", "For a Boolean control $c$ and integers $u,w$, eight conditional $\\pm c$ updates (tested on parities of the other integer) act, for $c=1$, as the cycle $(00\\ 01\\ 10)$ on parity pairs $(u,w)$ in every $2\\times2$ square for the first four, and $(01\\ 10\\ 11)$ for the last four.",
               r"induce the cycle $(00\ 01\ 10)$ in every square"),
             I("S4.6.2.2", "Applying the first cycle and then the second gives $(00\\ 10)(01\\ 11)$.",
               r"Applying the first cycle and then the second gives"),
             I("S4.6.2.3", "Hence the output is $(u',w')=(u+c(1-2(u\\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are preserved, and the auxiliary integer $w$ is restored; each coordinate moves by at most eight.",
               r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr)."),
             I("S4.6.2.4", "Write segment values as $u_i=2g_i+a_i$, $w_i=2h_i+b_i$ with guard values $g_i,h_i\\in\\{0,\\dots,2^{K-1}-1\\}$ for the $f-1$ disjoint $K$-bit segments below the top selected position, with control $c_i=x_{j_i}$.",
               r"u_i=2g_i+a_i,\qquad w_i=2h_i+b_i,"),
             I("S4.6.2.5", "Each of the eight lines for all segments at once is one cyclic shift of the target chunk $y\\gets y+\\varepsilon\\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=b]\\pmod{2^L}$, whose offset does not depend on the target, so each line is a bijection.",
               r"\varepsilon\sum_{i=0}^{f-2}2^{j_i}"),
             I("S4.6.2.6", "Let $\\mathcal B$ be the addresses where some used guard fails $10\\le g\\le2^{K-1}-11$; outside $\\mathcal B$ every segment lies in $[20,2^K-21]$ and even displacement eight stays within $[0,2^K-1]$, so no segment carries into the next and the shifts $S_0$ agree with the ideal XOR permutation $T_0$.",
               r"10\le g\le 2^{K-1}-11."),
             I("S4.6.2.7", "Each guard has exactly twenty excluded values among $2^{K-1}$, so the union bound over $2(f-1)$ guards gives $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$, independently of record values.",
               r"There are exactly twenty excluded values for each guard in",
               salient="Only twenty of the $2^{K-1}$ values of each guard are bad, so the exceptional fraction is at most $80(f-1)2^{-K}$, tiny because $K/\\log p\\to\\infty$."),
             I("S4.6.2.8", "Since $T_0$ and $S_0$ are bijections agreeing off $\\mathcal B$, $T_0S_0^{-1}$ fixes $\\mathcal B^c$ and permutes $\\mathcal B$, so the correction is a permutation of the exceptional records.",
               r"Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."),
             I("S4.6.2.9", "Each rotation moves its target to the rightmost chunk position by one chunk swap of width $L$ (cost $O(VL^\\tau)$ by the arbitrary-width interchange), then uses the controlled-shift lemma in $O(V)$ and undoes the swap; $S_0$ uses at most sixteen swaps and eight rotations.",
               r"There are at most sixteen swaps and eight rotations in $S_0$."),
             I("S4.6.2.10", "Extract the records of $\\mathcal B$ with destination ranks as keys, stably radix-sort only those records, and reinsert them in one forward scan, which implements $T_0$ everywhere deterministically (the keys are distinct and equal the marked holes).",
               r"while stable binary radix sorting scans only the extracted records and"),
             I("S4.6.2.11", "Total movement is $O(V(L^\\tau+1))$, scans of the full stream $O(MA_{\\rm rect}^3+V)$ and the radix passes $O(|\\mathcal B|A_{\\rm rect}(R+A_{\\rm rect}))$.",
               r"The movement costs $O(V(L^\tau+1))$."),
             I("S4.6.2.12", "After dividing by $V=MR$ the extra terms are bounded by $A_{\\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\\rm rect}(1+A_{\\rm rect}/R)$; with $A_{\\rm rect}=O(p)$, $R$ above every fixed polynomial in $p$, $f\\le d\\le p$ and $K/\\log p\\to\\infty$ they are $o(1)$, so the cost is $O(V(L^\\tau+1))$.",
               r"After division by $V=MR$, its additional terms are bounded by"),
             I("S4.6.2.13", "A fixed invertible binary change of basis on $e=mf$ axes (and its inverse) therefore costs $O(V((eK)^\\tau+1))$, since slot width is $L=(e/m)K$.",
               r"$O(V((eK)^\tau+1))$ on a stream of volume $V$."),
         ],
         page="packed-selected-bit-addition",
         frm=["address-chunk-interchange", "controlled-shift", "elementary-stream-ops", "sorting-and-data-movement-on-tapes", "binary-representation-and-bit-operations", "finite-field-f2-arithmetic"],
         salient="Eight additions of at most one on integers whose parity tests are mutually dependent compose to a pure parity flip of $u$ that leaves the other integer $w$ unchanged for every initial value.",
         adds=[B("f", "number of chunks", "The number of $K$-bit chunks whose selected bit is updated at once, with $0\\le i<f$.", "count"),
               B("L", "slot width", "The address-bit width $fK$ of one slot of $f$ chunks.", "count"),
               B("\\mathcal B", "exceptional set", "The set of addresses at which some used guard value falls outside the safe interval and packed additions may carry."),
               B("\\delta_{\\rm bad}", "bad fraction", "The bound $\\min\\{1,80(f-1)2^{-K}\\}$ on the fraction of addresses in the exceptional set.")])

K6_3 = S("S4.6.3",
         "Batching a common $C$-layer on $D\\le d$ chunks gives per-volume cost $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ with $F(e)=O(e)$ for $e<d^\\beta$, which solves to $O(d^{\\lambda'})$.",
         "Take the first $q_0$ chunks as the row index (supplying a row count divisible by $W^{k_0}$), recurse with the complex network on slots of $e/m$ chunks, and sum the internal-node overhead and the leaves of the recursion, then handle general $D$ by a base-$m$ partition.",
         ("The row count needed for the cyclic role split must come from the layer's own chunks, which is why a small number of chunks is spent on individual kernels.", "recoverable", None),
         [
             I("S4.6.3.1", "Applying $C$ individually on $e$ selected bits (split on the bit, combine paired records by $C(u,v)=((u+v+i(u-v))/2,(u+v-i(u-v))/2)$, merge) costs $O(Ve)$.",
               r"Thus \(e\) individual kernels cost"),
             I("S4.6.3.2", "At a node with $e=m^k$ chunks, the $s$ children plus binary basis changes, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\\tau+1))$ at that node.",
               r"O\bigl(V((eK)^\tau+1)\bigr)"),
             I("S4.6.3.3", "Put $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ and $k_0=\\lceil\\log_md\\rceil$; apply $C$ individually on the first $q_0$ chunks ($O(V\\log d)$) and use their bits as a row index.",
               r"q_0=\lceil\log_2 W\rceil\,"),
             I("S4.6.3.4", "The row range $R_{\\rm row}=2^{q_0K}\\ge W^{k_0}$; padding zero rows to a multiple of $W^{k_0}$ at most doubles the volume, and at recursive depth $j\\le k_0$ the row count is divisible by $W^{k_0-j}$.",
               r"length \(R_{\rm row}=2^{q_0K}\ge W^{k_0}\), since"),
             I("S4.6.3.5", "A row index $u=Wg+w$ goes entirely to wire role $w$, so every role stream has the same address shape and each recursive call acts on a stream of volume exactly $1/W$ of its parent's.",
               r"one role stream with volume exactly \(1/W\) of its parent's logical"),
             I("S4.6.3.6", "Fix $\\beta=1/2$ and choose rational exponents $0<\\tau<1$, $\\max\\{0,\\log_m(s/W)\\}\\le\\sigma<1$, $\\max\\{\\tau,\\sigma\\}<\\lambda<1$ and $\\tau(1+c/\\beta)<\\lambda$.",
               r"Fix \(\beta=1/2\), and choose real exponents satisfying"),
             I("S4.6.3.7", "Stopping the recursion at $e<d^\\beta$ and applying $e$ kernels individually, the cost per volume satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, $F(e)=O(e)$ for $e<d^\\beta$, because the $s$ calls on volume $V/W$ cost $s(V/W)F(e/m)$.",
               r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
             I("S4.6.3.8", "At an internal node $e\\ge d^\\beta$, so $K\\le d^c\\le e^{c/\\beta}$ and the overhead is $O(e^{\\tau(1+c/\\beta)}+1)=O(e^\\lambda)$.",
               r"At an internal node \(e\ge d^\beta\), hence"),
             I("S4.6.3.9", "With $a=s/W\\le m^\\sigma<m^\\lambda$ the internal costs sum to at most $Ce^\\lambda\\sum_{j\\ge0}(a/m^\\lambda)^j=O(e^\\lambda)$.",
               r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)."),
             I("S4.6.3.10", "Leaves after $j$ levels hold $u=e/m^j<d^\\beta$ chunks and contribute $O(a^ju)\\le O(e^\\sigma u^{1-\\sigma})\\le O(e^\\sigma d^{\\beta(1-\\sigma)})$, using $a^j\\le m^{j\\sigma}=(e/u)^\\sigma$.",
               r"O(a^ju)\le O(e^\sigma u^{1-\sigma})"),
             I("S4.6.3.11", "Writing $D-q_0=\\sum_ja_jm^j$ in base $m$ and handling the at most $(m-1)(1+\\lfloor\\log_md\\rfloor)$ pieces gives total $O(\\log(2d)[d^\\lambda+d^{\\sigma+\\beta(1-\\sigma)}+1])=O(d^{\\lambda'})$ for any fixed $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
               r"=O(d^{\lambda'})"),
         ],
         salient="The exponent $\\lambda'$ is only slightly below one, but strictly, because the recursive branching $s/W$ is below $m^\\sigma$ and the overhead is polynomial in $e$ with exponent $\\lambda<1$.",
         adds=[B("\\beta", "recursion cutoff exponent", "The exponent $1/2$ at which recursion stops: for $e<d^\\beta$ chunks the kernels are applied individually."),
               B("q_0", "row chunk count", "The number $\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ of leading chunks whose bits serve as the row index.", "count")])

K6_4 = S("S4.6.4",
         "The accelerated network can be evaluated exactly until a whole layer is complete: every intermediate coefficient needs at most $\\Delta=\\lceil C_0d^{C_1}\\rceil$ extra fractional bits and $\\Delta+3$ integer and sign bits, with $C_1=20$ and $C_0=128mB^2$, and $\\Delta=o(p)$.",
         "Bound the arithmetic dependency depth $A(e)$ of a recursive layer by the recurrence $A(e)\\le sA(e/m)+E$ and convert depth to magnitude and denominator growth, since each operation at most doubles the modulus or adds one denominator bit.",
         ("The sources say they give explicit constants bounding denominator and magnitude growth within one layer, since intermediate operators need not be contractions.", "explicit",
          r"denominator and magnitude growth within one layer."),
         [
             I("S4.6.4.1", "Constants: $E=64(W+m+1)^3$, $B=s+E$ and $\\nu=\\min\\{j\\ge1:m^j\\ge B\\}$.",
               r"E=64(W+m+1)^3,\qquad B=s+E,"),
             I("S4.6.4.2", "$C_1=\\max\\{20,\\nu+3\\}$, $C_0=128mB^2$ and $\\Delta=\\lceil C_0d^{C_1}\\rceil$; for the complex network $m^{10}<B<m^{11}$, hence $\\nu=11$ and $C_1=20$.",
               r"These values give \(m^{10}<B<m^{11}\), hence \(\nu=11\) and"),
             I("S4.6.4.3", "Every physical wire occurs in at most twelve scalar gates (four per stage), so there are at most $12W$ gates; a gate has at most $W$ inputs, coefficients in $\\{0,\\pm1,\\pm1/2\\}$, and evaluating all its outputs from saved inputs takes at most $2W^2$ operations.",
               r"physical wire occurs in at most twelve scalar gates, and there are"),
             I("S4.6.4.4", "Inverse-child corrections need at most $4s$ operations, source, sink and bank corrections at most $4W+4$, so the per-invocation total $24W^3+4s+4W+4$ is less than $E$ because $s<Wm$.",
               r"\(24W^3+4s+4W+4\) is less than"),
             I("S4.6.4.5", "The arithmetic depth satisfies $A(e)\\le sA(e/m)+E$ at an internal node and $A(e)\\le8e$ at a leaf (the depth estimate concatenates the $s$ calls, so it uses $s$, not $s/W$).",
               r"A(e)\le sA(e/m)+E"),
             I("S4.6.4.6", "With at most $\\lceil\\log_md\\rceil$ levels, $sx+E\\le Bx$ and $B^{k+1}\\le B^2d^\\nu$, so $A(e)\\le8dB^{k+1}\\le8B^2d^{\\nu+1}$.",
               r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}."),
             I("S4.6.4.7", "Adding the base-$m$ pieces ($\\le md$ of them), at most $d$ individual kernels and the diagonal phases, the total is $<128mB^2d^{\\nu+3}\\le C_0d^{C_1}$.",
               r"&<128mB^2d^{\nu+3}\le C_0d^{C_1}."),
             I("S4.6.4.8", "A value at depth $\\ell$ lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^\\ell$ (addition at most doubles the modulus, halving adds one denominator bit), so $p+\\Delta$ fractional and $\\Delta+3$ integer bits represent every intermediate coefficient exactly.",
               r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most"),
             I("S4.6.4.9", "Since $\\epsilon C_1<1$ and $d=\\Theta(p^\\epsilon)$, $\\Delta=o(p)$, so the full coefficient width remains $O(p)$.",
               r"\(\Delta=o(p)\), and the full coefficient width is \(O(p)\), as"),
         ],
         salient="The guard width $\\Delta\\approx C_0d^{20}$ is a polynomial in $d$ with huge constant but, since $d=\\Theta(p^{\\epsilon})$ with $\\epsilon=2^{-75}$, it is $o(p)$.",
         adds=[B("\\Delta", "guard width", "The number $\\lceil C_0d^{C_1}\\rceil$ of extra fractional bits reserved for exact intermediate values."),
               B("A(e)", "arithmetic depth", "A bound on the number of arithmetic operations along any chain through the recursive $C$-layer on $e$ axes.", "count")])

K6_5 = S("S4.6.5",
         "Proposition (simultaneous normalized layer): for $z$ in the unit disk on the grid $2^{-p}\\mathbb Z[i]$ the procedure returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time, evaluating the whole layer exactly before one truncation, with error $<\\sqrt2\\,2^{-p}$.",
         "Verify that the width bands make every packed child cost $O(M_{\\rm child}R_{\\rm g}(L^\\tau+1))$ uniformly, then use that $\\mathcal H$ is a contraction (rows have absolute sum one) so a single truncation adds less than $\\sqrt2\\,2^{-p}$.",
         ("The proof checks that the descriptor and exceptional-set terms of the packed lemma vanish under the parameter bands, then bounds the truncation.", "recoverable", None),
         [
             I("S4.6.5.1", "Fix $\\tau=\\sigma=1-2^{-50}$, $\\beta=\\frac12$, $C_1=20$ and rational $c,\\epsilon,\\lambda,\\lambda'$ with $\\max\\{\\tau,\\sigma\\}<\\lambda<1$, $\\tau(1+c/\\beta)<\\lambda$, $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$ and $\\epsilon C_1<1$ (concretely $\\epsilon=2^{-75}$, $c=2^{-56}$, $\\lambda=1-2^{-52}$, $\\lambda'=1-2^{-54}$).",
               r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20."),
             I("S4.6.5.2", "Since $d\\le b_dp^\\epsilon$ and $\\epsilon C_1<1$, $\\Delta\\le p$, so the guarded record width is $R_{\\rm g}=2r(p+2\\Delta+3)\\le12rp$ and also $R_{\\rm g}\\ge2rp$.",
               r"R_{\rm g}=2r(p+2\Delta+3)\le12rp"),
             I("S4.6.5.3", "A packed child's width parameter satisfies $A_*\\le\\lceil\\log_2(4MR_{\\rm g})\\rceil\\le C_Ap$ with $C_A=C_M+b_r+7$.",
               r"\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap,"),
             I("S4.6.5.4", "The two additional normalized terms are $A_*^3/R_{\\rm g}\\le C_A^3p^2/(2r)$ and $80(f-1)2^{-K}A_*(1+A_*/R_{\\rm g})\\le80C_Ap^22^{-K}(1+C_A/(2r))$.",
               r"\frac{A_*^3}{R_{\rm g}}"),
             I("S4.6.5.5", "Both bounds tend to zero uniformly, since $K\\ge\\frac12a_d^cp^{\\epsilon c}$ gives $K/\\log p\\to\\infty$ and $r\\ge2^{(a_r/b_d)p^{1-\\epsilon}}$ dominates every polynomial in $p$; thus every packed call has cost $O(M_{\\rm child}R_{\\rm g}(L^\\tau+1))$ with one constant.",
               r"Both bounds tend to zero uniformly over all current allowed $d,r$."),
             I("S4.6.5.6", "Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ maps disk arrays to disk arrays; truncation toward zero cannot increase either component and changes each by less than $2^{-p}$, so the error is less than $\\sqrt2\\,2^{-p}$.",
               r"absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk"),
         ])

K6 = S("S4.6",
       "Fast simultaneous butterfly layer: $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied coefficientwise at the same bit offset in $D\\le d$ address chunks of a polynomial-record array costs $O(Vd^{\\lambda'})$ with $\\lambda'=1-2^{-54}$, evaluating the whole layer exactly before a single truncation.",
       "Express the layer through the complex phase network (kernels $C$ on smaller groups of selected bits separated by binary changes of basis), implement the basis changes by whole-chunk moves and packed selected-bit additions, split complete rows among the $W$ roles for volume $V/W$ per recursive call, and bound the intermediate dyadic values.",
       ("The sources contrast the layer with separate butterfly factors, which would need $D$ whole-array passes, whereas the recursion costs $O(Vd^{\\lambda'})$.", "explicit",
        r"factors would require $D$ whole-array passes."),
       [K6_1, K6_2, K6_3, K6_4, K6_5],
       page="fast-butterfly-layer",
       frm=["address-chunk-interchange", "packed-selected-bit-addition", "phase-frame-kernel", "rank-saving-recurrence", "subset-intersection-labels", "fixed-point-truncation", "polynomial-ring-mod", "butterfly"],
       salient="The layer is evaluated with exact Gaussian dyadic arithmetic on non-contractive intermediate operators and truncated only once at the end, so rounding error does not accumulate over the $D$ simultaneous butterflies.",
       adds=[B("p", "precision", "The number of fractional bits: coefficients are multiples of $2^{-p}$, with $p=6b$ in the multiplication algorithm.", "count"),
             B("d", "number of axes", "The number of address axes (and bound on selected chunks), $d=\\lfloor b^\\epsilon\\rfloor=\\Theta(p^\\epsilon)$.", "count"),
             B("K", "chunk width", "The number $\\lfloor d^c\\rfloor$ of address bits per chunk, where one common bit offset is selected.", "count"),
             B("r", "record length", "The number $2^{\\Theta(p/d)}$ of complex coefficients in a polynomial record, growing faster than every power of $p$.", "count"),
             B("\\epsilon", "axis exponent", "The exponent $2^{-75}$ with $d=\\Theta(p^\\epsilon)$."),
             B("c", "chunk exponent", "The exponent $2^{-56}$ with $K=\\lfloor d^c\\rfloor$."),
             B("\\lambda'", "layer exponent", "The exponent $1-2^{-54}$ in the layer cost $O(Vd^{\\lambda'})$.")])

KEY = S("S4",
        "Both tape procedures cost a power of their parameter below one, because each runs a fixed linear exchange network on $W$ wires whose edge changes are smaller calls on role streams of volume $V/W$, with total number of calls $s<Wm$, so that each level of recursion multiplies the cost per volume by $s/W<m^\\tau$ while the parameter shrinks by $m$.",
        "Build a finite linear exchange network that restores its scratch wires, give its vertices frames so that only endpoint operators matter, attach nested subspace labels so that the total rank $s$ of all edge changes is below $Wm$, and unroll the resulting recursion once with bit gates (address-chunk interchange) and once with Gaussian-dyadic phase gates (simultaneous butterfly layer).",
        ("The sources state that the strict inequality $s/W<m$ per level is the source of the power saving.", "explicit",
         r"is the source of the power saving."),
        [K1, K2, K3, K4, K5, K6],
        page="rank-saving-recurrence",
        frm=["linear-network", "common-frame-principle", "subset-intersection-labels", "recurrences-and-induction", "big-o"],
        salient="The saving comes from a strict inequality between two huge numbers: $s_{\\rm b}$ and $s_{\\rm c}$ fall short of $W_{\\rm b}m$ and $W_{\\rm c}m$ by a relative amount of only about $10^{-11}$, yet that is enough to make the cost per volume grow as $e^\\tau$ with $\\tau<1$ instead of linearly in the width.",
        adds=[B("m", "label dimension", "The dimension $h^3=10^6$ of the label space, equal to the factor by which the recursive parameter shrinks at each level.", "count"),
              B("W", "wire count", "The number of wires in the linear network (including scratch wires), equal to the number of role streams into which the volume is split.", "count"),
              B("s", "call count", "The sum over all edges of the rank of the edge change, i.e. the number of smaller calls made by one invocation of the network.", "count"),
              B("V", "logical volume", "The number of stored data bits in the array being processed.", "count"),
              B("\\tau", "exponent", "A fixed rational exponent $1-2^{-50}$ with $s/W<m^\\tau$ (also called $\\sigma$ for the complex network).")])

# ---------------------------------------------------------------- first children
C1 = I("S1",
       "Setting: Schönhage and Strassen proposed $n\\log n$ as the optimal order of multitape-Turing-machine time for multiplying two $n$-bit integers, Harvey and van der Hoeven reached $O(n\\log n)$ from above, and a strict power saving in the logarithm is obtained in the same fixed finite-tape model.",
       r"machine, and proposed $n\log n$ as the optimal order of growth",
       page="integer-multiplication-conjecture", frm=["multitape-tm", "big-o", "logarithms-and-iterated-logarithm-notation"])

C2 = I("S2",
       "Elementary scans: on a fixed number of tapes, in $O(V)$ steps one can permute the values of two radix-$q$ digits, move a digit, split on a digit and merge after a pointwise map, and deal whole rows cyclically into $W$ streams of equal shape.",
       r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
       page="elementary-stream-ops", frm=["tape-address-model", "multitape-tm", "sorting-and-data-movement-on-tapes", "big-o"])

C3 = I("S3",
       "Controlled cyclic shift: an update $y\\mapsto y+a(\\text{controls})\\pmod Q$ of a target field following its control fields costs $O(V)$, by splitting each fiber at the offset and merging the two pieces in opposite order; multiplication by a fixed unit and negation also cost $O(V)$.",
       r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
       page="controlled-shift", frm=["elementary-stream-ops", "tape-address-model", "modular-arithmetic"])

# ---------------------------------------------------------------- synthetic transforms and ring convolution
R1 = S("S5.1",
       "Synthetic transform: over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$, with $\\omega_t=y^{2r/t}$ a signed coefficient shift, $F_t^\\pm$ satisfy $F_t^+F_t^-=I/t$, are contractions, and are computed by radix-two decimation-in-frequency rounds with twiddle monomials that leave the outputs in bit-reversed order, which the opposite transform consumes.",
       "Define the transform entrywise with $\\omega_t=y^{2r/t}$, prove inversion by direct character cancellation (the ring has zero divisors), obtain the butterfly recursion from the even/odd split, track the bit-reversed storage order, and group the rounds across axes.",
       ("The sources choose polynomial rings in which the needed roots of unity act by exact signed permutations of coefficient lists.", "explicit",
        r"where the required roots of unity act by exact signed permutations"),
       [
           I("S5.1.1", "Definition: for $r\\ge2$ a power of two, $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with coefficient sup norm; multiplication by $y^a$ permutes coefficients up to sign and is an isometry.",
             r"\mathcal R_r=\mathbb C[y]/(y^r+1),\qquad"),
           I("S5.1.2", "Truncation $Q_p$ toward zero satisfies $\\|Q_pz-z\\|_\\infty<\\sqrt2\\,2^{-p}$ and $\\|Q_pz\\|_\\infty\\le\\|z\\|_\\infty$.",
             r"\|Q_p z-z\|_\infty<\sqrt2\,2^{-p},\qquad"),
           I("S5.1.3", "For a power of two $t$ dividing $2r$ put $\\omega_t=y^{2r/t}$ and $(F_t^\\mp z)_j=\\frac1t\\sum_k\\omega_t^{\\mp jk}z_k$; every power of $\\omega_t$ is an isometry, so both transforms are contractions.",
             r"The ring has zero divisors, so we verify character cancellation"),
           I("S5.1.4", "Character cancellation: $\\sum_{k=0}^{t-1}\\omega_t^{jk}$ equals $t$ if $t\\mid j$ and $0$ otherwise (shifting $k$ by $t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$, and $\\mathcal R_r$ has no two-torsion), hence $F_t^+F_t^-=t^{-1}I$.",
             r"F_t^+F_t^-=t^{-1}I."),
           I("S5.1.5", "Decimation in frequency: pair $z_k$ with $z_{k+t/2}$, apply $H_0$, multiply the $b=1$ output by $\\omega_t^{-k}$ and recurse in the two branches, because $(F_t^-z)_{2h+b}=\\frac1{t/2}\\sum_{k<t/2}(\\omega_t^2)^{-hk}\\omega_t^{-bk}\\frac{z_k+(-1)^bz_{k+t/2}}2$.",
             r"(F_t^-z)_{2h+b}"),
           I("S5.1.6", "After all $a=\\log_2t$ rounds, entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$; with $B_t$ the record permutation $j\\mapsto\\operatorname{rev}_a(j)$ the recursion writes outputs directly in this order.",
             r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
           I("S5.1.7", "The reverse traversal (smaller branches first, then the inverse monomial, then $H_0$) composed with $B_tF_t^-$ is $2^{-a}I=I/t$, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
             r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
           I("S5.1.8", "On $D$ axes, one round applies a parallel butterfly $\\mathcal H$ then a recordwise monomial $J_E$ multiplying by $y^E$ with $E=-\\sum_i\\frac{2r}{u_i}b_ik_i\\pmod{2r}$, since each axis's twiddle depends only on its own address bits and commutes with the other butterflies.",
             r"\frac{2r}{u_i}\,b_i k_i\pmod{2r}."),
           I("S5.1.9", "Each $\\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction; in the opposite direction the round is $\\mathcal HJ_E^{-1}$.",
             r"Each $\mathcal H$ is a contraction and each"),
       ],
       page="synthetic-transform",
       frm=["polynomial-ring-mod", "dft", "multidimensional-dft", "butterfly", "roots-of-unity", "fixed-point-truncation"])

R2 = S("S5.2",
       "Transform layout and cost: on $d-1$ axes of lengths $t_i\\in\\{2^{\\ell-1},2^\\ell\\}$ ($M=\\prod t_i$, $T=rM$), a layout permutation $L$ places the participating bits at a common offset in consecutive $K$-bit chunks, so that $LBF^-_{\\boldsymbol t}$ and $F^+_{\\boldsymbol t}B^{-1}L^{-1}$ each cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error less than $\\sqrt2\\ell\\,2^{-p}$.",
       "Move the top slots to a prefix, exchange $K$-bit chunks so equal-offset bits of all axes are adjacent, run the first $b+1\\le K$ rounds on prefix slots bit by bit, run the remaining $qK$ rounds with the fast simultaneous layer, and add up one truncation per round.",
       ("The sources say the selected bits of the participating axes must be placed at a common offset in consecutive $K$-bit chunks for the layer to apply.", "explicit",
        r"we must place the selected bits of the participating axes at a common"),
       [
           I("S5.2.1", "Put $b=(\\ell-1)\\bmod K$ and $q=\\lfloor(\\ell-1)/K\\rfloor$; the prefix list is the top slot of every long axis followed by slots $h=b-1,\\dots,0$ of all axes, and the rest of each axis consists of $q$ consecutive $K$-bit chunks.",
             r"b=(\ell-1)\bmod K,"),
           I("S5.2.2", "There are at most $D(b+1)=O(dK)$ listed slots, so moving them to a prefix costs $O(TpdK)$.",
             r"$D(b+1)=O(dK)$"),
           I("S5.2.3", "Reordering chunks from axis-major to chunk-index-major uses at most $Dq-1$ exchanges of width-$K$ chunks, each $O(TpK^\\tau)$, in total $O(Tp\\,DqK^\\tau)=O(Tp\\,pK^{\\tau-1})$ because $Dq=O(p/K)$.",
             r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
           I("S5.2.5", "Each remaining round has the complete address set $[P]\\times[2^K]^D\\times[S]$ and costs $O(Tpd^{\\lambda'})$ by the simultaneous-layer proposition, so the $\\ell$ rounds cost $O(Tp\\ell d^{\\lambda'})$ in total.",
             r"$O(Tp\ell d^{\lambda'})$ in total."),
           I("S5.2.4", "Rounds on prefix slots process the participating bits one at a time with $O(rp)$ work per pair and no truncation between axes (after $s\\le D$ factors the values are exact dyadics in the disk), costing $O(TpdK)$ for at most $b+1\\le K$ rounds.",
             r"$p+D+O(1)=O(p)$ bits per component suffice, since $D\leq d$ and"),
           I("S5.2.6", "A monomial $y^E$ with $E=er+s$ is applied by splitting the coefficient list before position $r-s$, swapping the two pieces, negating the moved tail and applying the sign $(-1)^e$, at cost $O(rp)$ per record.",
             r"To implement the monomial, write $E=er+s$ with $0\leq s<r$."),
           I("S5.2.7", "Truncation is odd and $J_E$ is a signed coefficient permutation, so $J_EQ_p(\\mathcal Hz)=Q_p(J_E\\mathcal Hz)$: each round is exactly one truncation after an exact contraction.",
             r"J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z)."),
           I("S5.2.8", "Each round does not increase the error of its input (it is a contraction) and adds less than $\\sqrt2\\,2^{-p}$ by one truncation, so starting from zero error at most $\\ell$ rounds give error less than $\\sqrt2\\ell\\,2^{-p}$ and disk output; layout permutations add no error.",
             r"zero error, at most $\ell$ rounds therefore"),
           I("S5.2.9", "Executing the named-slot procedures after $L$ conjugates them, so the full exact operators are $(L\\mathcal D_-L^{-1})L=LBF^-_{\\boldsymbol t}$ and $L^{-1}(L\\mathcal D_+L^{-1})=F^+_{\\boldsymbol t}B^{-1}L^{-1}$.",
             r"(L\mathcal D_-L^{-1})L=LB F_{\boldsymbol t}^-,"),
       ],
       salient="The three cost terms are the whole price of the transform: $dK$ for slots handled one at a time, $pK^{\\tau-1}$ for chunk exchanges (a saving because $\\tau<1$), and $\\ell d^{\\lambda'}$ for the fast layer rounds.")

R3 = S("S5.3",
       "Signed packing: for disk-grid polynomials $f,g\\in\\mathcal R_r$ one computes the exact Gaussian-integer numerators of $fg$ and returns $Q_p(fg/r)$ in $O(rp\\log(rp))$ time with four products of $4pr$-bit integers by the established multiplier.",
       "Evaluate the integer coefficient polynomials at $B_0=2^{4p}$ (signed Kronecker substitution), multiply, and read the coefficients back by centered residues, since each product coefficient is below $B_0/2$.",
       ("The sources describe the reduction as a signed form of Kronecker substitution.", "explicit",
        r"reduction is a signed form of Kronecker substitution; compare"),
       [
           I("S5.3.1", "Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer polynomials of coefficients at most $2^p$; set $B_0=2^{4p}$ and $A_u=u(B_0)$, so $|A_u|<B_0^r/2$ fits in $4pr$ bits.",
             r"Set $B_0=2^{4p}$"),
           I("S5.3.2", "Every coefficient of an ordinary product satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so each coefficient is identified by its centered residue modulo $B_0$ once lower ones are removed.",
             r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
           I("S5.3.3", "Forming $A_u$ from signed coefficients: with carry $\\gamma_j\\in\\{-1,0\\}$ ($d_j\\equiv u_j+\\gamma_j\\pmod{B_0}$), the blocks form a two's-complement encoding of $A_u$ computed by a constant number of linear scans.",
             r"Since $-B_0<u_j+\gamma_j<B_0$ whenever"),
           I("S5.3.4", "Extraction: at block $j$ let $\\widehat h_j\\in[-B_0/2,B_0/2)$ be congruent to $q_j+\\rho_j$ and $\\rho_{j+1}=(q_j+\\rho_j-\\widehat h_j)/B_0\\in\\{0,1\\}$; the residual identity $\\sum_{k\\ge j}h_kB_0^{k-j}=\\sum_{k\\ge j}q_kB_0^{k-j}+\\rho_j+\\varepsilon B_0^{J-j}$ shows $\\widehat h_j=h_j$ by induction.",
             r"At block $j$, let $\widehat h_j$ be the unique"),
           I("S5.3.5", "Reduction modulo $y^r+1$ (subtracting coefficient $j+r$ from $j$) gives each coefficient $H_j$ as a sum of exactly $r$ signed products, so $|H_j|\\le r2^{2p}$ and the normalized product $fg/r$ lies in the disk.",
             r"|H_j|\leq r2^{2p}."),
           I("S5.3.6", "The output numerator is $\\operatorname{trunc}_0(\\Re H_j/2^{p+\\ell})+i\\operatorname{trunc}_0(\\Im H_j/2^{p+\\ell})$, implemented by a right shift of $p+\\ell$ bits, with error less than $\\sqrt2\\,2^{-p}$ from $fg/r$.",
             r"Finally the $p$-bit grid numerator of the normalized product is"),
           I("S5.3.7", "Four exact integer products of $O(rp)$ bits each, at cost $O(rp\\log(rp))$, dominate the linear packing, extraction, combination, wrapping and truncation costs.",
             r"Four exact integer products dominate the linear"),
       ],
       page="signed-packing",
       frm=["established-multiplier", "polynomial-ring-mod", "fixed-point-truncation", "binary-representation-and-bit-operations"])

R4 = S("S5.4",
       "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathcal R_r$ on $d-1$ axes is approximated with error less than $\\sqrt2\\,M(3\\ell+1)2^{-p}$ by two forward transforms retaining the same order, pointwise products, and one opposite transform.",
       "Because a common record permutation commutes with pointwise products, multiply the forward outputs in their stored order, apply the opposite transform and the exact scale $M$; then propagate errors through the bilinear contraction.",
       ("Pointwise product commutes with a common record permutation, so no re-sorting is needed between transforms.", "recoverable", None),
       [
           I("S5.4.1", "Define $\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}$; each output coefficient averages $rM$ signed scalar products, so $\\mathcal M_r$ is a bilinear contraction.",
             r"\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}."),
           I("S5.4.2", "Convolution theorem and inversion: $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$ and $F^+_{\\boldsymbol t}F^-_{\\boldsymbol t}=I/M$, so $MF^+_{\\boldsymbol t}((F^-f)(F^-g)/r)=(f*g)/(rM)$.",
             r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)."),
           I("S5.4.3", "Error chain: put $\\delta=\\sqrt2\\ell\\,2^{-p}$ and $\\eta=\\sqrt2\\,2^{-p}$; each forward error is below $\\delta$.",
             r"$\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$."),
           I("S5.4.4", "The pointwise step: bilinearity of $P(x,y)=xy/r$ gives $\\|P(\\widetilde u,\\widetilde v)-P(u,v)\\|<2\\delta$ and, with one truncation, $\\|\\widetilde z-z_*\\|_\\infty<2\\delta+\\eta$.",
             r"$\|\widetilde z-z_*\|_\infty<2\delta+\eta$."),
           I("S5.4.5", "Through the contractive opposite transform $\\mathcal T_+$, $\\|\\widetilde h-\\mathcal T_+z_*\\|_\\infty<3\\delta+\\eta$ (its own approximation error plus the propagated $2\\delta+\\eta$).",
             r"<3\delta+\eta."),
           I("S5.4.6", "Exact multiplication by $M$ gives error less than $M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$, with the returned width $w_M=w+\\log_2M$ (the scale is a power of two).",
             r"$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."),
           I("S5.4.7", "There are $M=T/r$ pointwise polynomial products, costing $O(Tp\\log(rp))$ in total, which with the three transform costs gives $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
             r"There are $M=T/r$ pointwise polynomial products."),
       ])

C5 = S("S5",
       "Convolution over $\\mathbb C[y]/(y^r+1)$: the normalized convolution of arrays on $d-1$ power-of-two axes with ring entries is computed in $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$ time with error less than $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
       "Apply two synthetic forward transforms keeping the same frequency order, multiply pointwise by signed packing divided by $r$, and apply the opposite transform, using the fast layers and chunk swaps for the transforms.",
       ("The sources observe that pointwise multiplication commutes with a common record permutation, so the forward outputs can be multiplied in their retained order and passed directly to the opposite transform.", "explicit",
        r"forward outputs in their retained order and pass that order directly"),
       [R1, R2, R3, R4],
       page="ring-convolution",
       frm=["fast-butterfly-layer", "address-chunk-interchange", "synthetic-transform", "signed-packing", "cyclic-convolution", "established-multiplier", "fixed-point-truncation", "polynomial-ring-mod"],
       adds=[B("T", "padded size", "The total number of complex scalar entries $T=rM$ of the array, a power of two with $T\\in[4n/b,8n/b)$.", "count"),
             B("M", "record count", "The number $T/r=\\prod_{i<d}t_i$ of ring records.", "count"),
             B("\\ell", "log of record length", "The exponent $\\log_2r$, of order $p^{1-\\epsilon}$.")])

# ---------------------------------------------------------------- resampling
G1 = S("S6.1",
       "One-dimensional resampling: for coprime $2\\le s<t<2^p$ and $\\alpha<\\sqrt p$ with $\\theta=t/s-1>p/\\alpha^4$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, approximated with error less than $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, the permutations $P_s,P_t$ staying in the identity.",
       "Use the Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ with a nearly-identity contraction $N=C\\mathsf T\\mathsf D$ inverted by a Neumann series, normalize so all factors are contractions, and quote the numerical maps of Harvey and van der Hoeven.",
       ("Normalizing by powers of two makes each Gaussian factor a contraction so the approximation errors can be tracked by contraction bounds.", "recoverable", None),
       [
           I("S6.1.1", "The permutations are $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$.",
             r"(P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}."),
           I("S6.1.2", "Claim: $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ for contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$.",
             r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."),
           I("S6.1.3", "Two Gaussian maps $\\mathsf S,\\mathsf T:\\mathbb C^s\\to\\mathbb C^t$: $(\\mathsf Su)_k=\\frac1\\alpha\\sum_je^{-\\pi\\alpha^{-2}(j-sk/t)^2}u_j$ and $(\\mathsf Tu)_k=\\sum_je^{-\\pi\\alpha^2(tj/s-k)^2}u_j$.",
             r"(\mathsf S u)_k=\frac1\alpha\sum_{j\in\mathbb Z}"),
           I("S6.1.4", "Gaussian identity: $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, and $N=C\\mathsf T\\mathsf D$ (selecting the nearest coordinate $q_j=\\lfloor tj/s+1/2\\rfloor$ with weights $e^{\\pi\\alpha^2\\beta_j^2}$) satisfies $\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}$.",
             r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
           I("S6.1.5", "Since $\\alpha^2\\theta>p/\\alpha^2>1$, $\\|N-I\\|<1/2$ and $N$ is invertible by a Neumann series.",
             r"Thus $\|N-I\|<1/2$, so $N$ is invertible"),
           I("S6.1.6", "With $\\mathsf S'=\\mathsf S/2$, $\\mathsf J'=N^{-1}/2$, $\\mathsf D'=2^{-(2\\alpha^2-2)}\\mathsf D$ one has $\\|\\mathsf S'\\|<3/4$, $\\|\\mathsf J'\\|<7/8$, $\\|\\mathsf D'\\|<1$.",
             r"\|\mathsf S'\|<\frac34,\qquad"),
           I("S6.1.7", "Set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$, both contractions since $\\|C\\|=1$; the left inverse $\\mathsf DN^{-1}C$ of $\\mathsf T$ turns the Gaussian identity into $\\mathsf DN^{-1}CP_tF_t\\mathsf S=P_sF_s$.",
             r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$."),
           I("S6.1.8", "The normalizations multiply to $2^{-(2\\alpha^2-2)}\\cdot2^{-1}\\cdot2^{-1}=2^{-2\\alpha^2}$, so $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
             r"$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$.",
             salient="The three halvings that make $\\mathsf S'$, $\\mathsf J'$ and $\\mathsf D'$ contractions multiply to exactly $2^{-2\\alpha^2}$, which is the scale factor $2^{2\\alpha^2}$ that must be restored afterwards."),
           I("S6.1.9", "Numerical maps (Lemmas 4.8, 4.9, 4.12 of Harvey–van der Hoeven): $\\widetilde{\\mathsf S}'$ has error $16p$ and time $O(tp^{3/2+\\delta}\\alpha)$, $\\widetilde{\\mathsf J}'$ error $3p^2/4$ and the same time, $\\widetilde{\\mathsf D}'$ error $4$ and time $O(tp^{1+\\delta})$.",
             r"\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\"),
           I("S6.1.10", "$C$ selects an ordered subsequence ($q_0=0$, $q_{s-1}<t$, $q_{j+1}>q_j$), generated in order with $O(p)$ work per index using counters $e_j,f_j$ with $tj=sf_j+e_j$, so $C$ costs $O(tp)$ with zero error.",
             r"The selected indices can themselves be generated in order using only"),
           I("S6.1.11", "Taking $\\widetilde A=\\widetilde{\\mathsf S}'$ and $\\widetilde B_0=\\widetilde{\\mathsf D}'\\widetilde{\\mathsf J}'C$ gives errors $16p<p^2$ and $4+3p^2/4<p^2$ and the claimed time; the original construction's two label-and-sort steps (each $O(tp\\log t)$) are avoided because the permutations stay in the identity.",
             r"Contraction of the exact maps yields errors less than $16p<p^2$ and"),
       ],
       adds=[B("s", "source length", "The prime length of one source Fourier transform axis."),
             B("t", "transform length", "The power-of-two length of the transform axis with $s<t$ and $\\gcd(s,t)=1$."),
             B("\\alpha", "Gaussian width", "The integer $2\\le\\alpha<\\sqrt p$ controlling the Gaussian window, $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$."),
             B("\\theta", "oversampling margin", "The ratio $t/s-1$, required to exceed $p/\\alpha^4$.")])

G2 = S("S6.2",
       "Tensor interface: if every pair $(s_i,t_i)$ satisfies the one-dimensional hypotheses, then $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, the linewise maps have error less than $dp^2$ and cost $O(dTp^{3/2+\\delta}\\alpha)$, and exposing and restoring the lines costs $O(Tpd^2(1+\\ell^\\tau))$.",
       "Tensor the one-dimensional identity, apply the maps to one axis at a time on the zero-padded box, and use chunk swaps to expose each axis as the innermost field.",
       ("Moving each axis to the innermost position by chunk interchanges makes the linewise maps independent of the number of axes.", "recoverable", None),
       [
           I("S6.2.1", "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $R=\\bigotimes P_{s_i}$, $Q=\\bigotimes P_{t_i}$, $\\mathcal A=\\bigotimes A_i$, $\\mathcal B_0=\\bigotimes B_{0,i}$ and $\\gamma=2d\\alpha^2$.",
             r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
           I("S6.2.2", "Axis by axis, expand valid lines from $s_i$ to $t_i$ entries (zero lines elsewhere) and compress back; each axis map is a contraction with error less than $p^2$, so $d$ axes give error less than $dp^2$.",
             r"Composing the $d$ axis maps gives error less than $dp^2$."),
           I("S6.2.3", "At most $T/t_i$ lines invoke the one-dimensional algorithm on axis $i$, so the cost is $\\sum_i\\frac T{t_i}O(t_ip^{3/2+\\delta}\\alpha)=O(dTp^{3/2+\\delta}\\alpha)$.",
             r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
           I("S6.2.4", "Exposing an axis needs $O(d)$ adjacent interchanges of $\\ell$- or $(\\ell-1)$-bit fields, each $O(Tp(1+\\ell^\\tau))$ (an unequal pair peels off a leading bit), so all axes cost $O(d^2)$ interchanges, i.e. $O(Tpd^2(1+\\ell^\\tau))$.",
             r"$O(d)$ adjacent interchanges, hence all axes need $O(d^2)$."),
           I("S6.2.5", "Since $t_i\\ge r/2$ at most $2dT/r$ lines occur, so $O(p^c)$ setup per line is $o(Tp)$ because $r$ exceeds every polynomial in $p$.",
             r"$\sum_iT/t_i\leq2dT/r$ lines."),
       ])

C6 = S("S6",
       "Gaussian resampling with the permutations left in the transform: the Fourier transform of prime lengths $s_i$ is expressed as $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ through a power-of-two transform, with ordered numerical maps, error less than $dp^2$ and cost $O(dTp^{3/2+\\delta}\\alpha)$.",
       "Use the Harvey–van der Hoeven Gaussian identity but keep the source and target coordinate permutations inside the formula, so that no sort is executed, then tensor over the $d$ axes.",
       ("The sources retain both permutations in the transform formula because the usual implementation sorts twice on each coordinate.", "explicit",
        r"coordinate. We retain both permutations in the transform formula and"),
       [G1, G2],
       page="gaussian-resampling",
       frm=["dft", "multidimensional-dft", "address-chunk-interchange", "fixed-point-truncation", "established-multiplier", "norms-absolute-values-and-error-bounds"],
       adds=[B("\\gamma", "resampling exponent", "The exponent $2d\\alpha^2$ of the power of two accumulated by the tensor of $d$ one-dimensional scales."),
             B("R", "source permutation", "The tensor $\\bigotimes P_{s_i}$ of coordinate permutations $j\\mapsto tj$ on the source axes."),
             B("Q", "target permutation", "The tensor $\\bigotimes P_{t_i}$ of coordinate permutations $k\\mapsto-sk$ on the power-of-two axes.")])

# ---------------------------------------------------------------- chirp / permutation cancellation
B1 = S("S7.1",
       "Bluestein chirp identity: with $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_is_ij_i^2/t_i)$ (periodic of period $t_i$), the permuted transform is $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, a chirp-weighted normalized convolution.",
       "Compare coefficients of $u_{\\boldsymbol k}$ on both sides, using $-s_i(j_i-k_i)^2/t_i+s_ij_i^2/t_i+s_ik_i^2/t_i$ to see that only the cross term $2s_ij_ik_i/t_i$ survives.",
       ("Expanding the square in the chirp leaves exactly the Fourier kernel, so a transform is a convolution between two chirp multiplications.", "recoverable", None),
       [
           I("S7.1.1", "Define $a_{\\boldsymbol j}=\\exp\\left(-\\pi i\\sum_{i=1}^d s_ij_i^2/t_i\\right)$ for even $t_i$.",
             r"=\exp\left(-\pi i\sum_{i=1}^d\frac{s_i j_i^2}{t_i}\right)."),
           I("S7.1.2", "Claim: $QF_{\\boldsymbol t}u=\\overline a\\cdot\\frac{a*(\\overline a\\cdot u)}{T}$.",
             r"\frac{a*(\overline a\mathbin{\cdot}u)}{T}."),
           I("S7.1.3", "$a$ has period $t_i$ in coordinate $i$ because replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\\pi is_i(2j_i+t_i)$, an integral multiple of $2\\pi i$.",
             r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
           I("S7.1.4", "The coefficient of $u_{\\boldsymbol k}$ on the right is $\\frac1T\\overline a_{\\boldsymbol j}a_{\\boldsymbol j-\\boldsymbol k}\\overline a_{\\boldsymbol k}=\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$.",
             r"=\frac1T\exp\left(2\pi i\sum_i"),
           I("S7.1.5", "This is the coefficient in $QF_{\\boldsymbol t}$, because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.",
             r"from the negative-sign transform."),
       ],
       page="bluestein-chirp",
       frm=["dft", "multidimensional-dft", "cyclic-convolution", "roots-of-unity"])

C7 = S("S7",
       "Permutation cancellation: the middle factor $QF_{\\boldsymbol t}$ is computed by a chirp convolution without executing $Q$, and the source permutation $R$ cancels across the two source transforms, the pointwise product and the opposite transform: $RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
       "Convert the target permutation into the chirp convolution and show that $R$ commutes with pointwise products and satisfies $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$, so the result is the ordinary convolution.",
       ("The sources say the chirp identity performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.", "explicit",
        r"in $Q$ without applying $Q$ as a separate permutation of the array."),
       [
           B1,
           I("S7.2",
             "For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ gives $F_q^+R_c=R_c^{-1}F_q^+$; each $t_i$ is a unit modulo $s_i$, so $F^+_{\\boldsymbol s}R=R^{-1}F^+_{\\boldsymbol s}$ and $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$.",
             r"Substituting $h=ck$"),
           I("S7.3",
             "Since $R$ commutes with pointwise products, $RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=F^+_{\\boldsymbol s}(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)$, and by $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)(F_{\\boldsymbol s}v)$ and $F^+_{\\boldsymbol s}F_{\\boldsymbol s}=I/S$ this equals $\\frac1SF^+_{\\boldsymbol s}F_{\\boldsymbol s}(u*v)=\\frac{u*v}{S^2}$.",
             r"=\frac{u*v}{S^2},",
             salient="The permutation $R$ appears in all three transforms but never has to be executed: because it conjugates $F^+_{\\boldsymbol s}$ to itself, it cancels completely and the result is the plain convolution divided by $S^2$."),
       ],
       page="permutation-cancellation",
       frm=["gaussian-resampling", "bluestein-chirp", "dft", "multidimensional-dft", "cyclic-convolution"])

# ---------------------------------------------------------------- assembly
P1 = S("S8.1",
       "Parameter choices: $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$, $r=2^{\\lceil(\\log_2T)/d\\rceil}$, axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod t_i=T$, $t_d=r$, and distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, $\\eta=1/(4d)$, so that $T/2<S<T$ and every Gaussian-resampling hypothesis holds.",
       "Fix conservative rational exponents, then verify by direct estimates that the prime intervals contain enough primes, that the product of the primes occupies more than half the box, and that $\\alpha^4\\theta_i>p$.",
       ("The sources say the primes must be close to the powers of two so that their product fills a fixed fraction of the padded box while each ratio leaves enough separation for resampling.", "explicit",
        r"$t_i$: their product must occupy a fixed fraction of the padded box,"),
       [
           I("S8.1.1", "Fixed rational exponents: $\\tau=\\sigma=1-2^{-50}$, $\\beta=\\frac12$, $\\delta=\\frac1{16}$.",
             r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\"),
           I("S8.1.2", "$\\lambda=1-2^{-52}$ and $c=2^{-56}$.",
             r"\lambda=1-2^{-52},\qquad c=2^{-56},\qquad"),
           I("S8.1.3", "$C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$ (and $\\lambda'=1-2^{-54}$), chosen deliberately conservative with no optimization claimed.",
             r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
           I("S8.1.4", "Sizes: $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$.",
             r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
           I("S8.1.5", "Take the power of two $T\\in[4n/b,8n/b)$ and $r=2^{\\lceil(\\log_2T)/d\\rceil}$, $\\ell=\\log_2r$.",
             r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
           I("S8.1.6", "Choose $d\\ell-\\log_2T$ axis lengths equal to $r/2$ and the rest equal to $r$, so $t_i\\in\\{r/2,r\\}$, $\\prod t_i=T$ and the last axis has $t_d=r$.",
             r"t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r."),
           I("S8.1.7", "Set $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, $\\gamma=2d\\alpha^2$ and $\\eta=1/(4d)$.",
             r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
           I("S8.1.8", "Then $\\gamma<28d^2\\sqrt b\\le28b^{1/2+2\\epsilon}\\le28b^{2/3}$, so $2\\le\\alpha<\\sqrt p$ and $\\gamma=o(b)$ (for $b\\ge2^{24}$, $\\gamma\\le b/4$).",
             r"\gamma<28d^2\sqrt b\le28b^{1/2+2\epsilon}\le28b^{2/3}."),
           I("S8.1.9", "Primes in $((1-2\\eta)x,(1-\\eta)x]$: for $0<\\eta<1/4$ and $x>e^{2/\\eta}$ there are at least $\\eta x/(2\\log x)$ primes (Rosser–Schoenfeld), which exceeds $d$ for $x\\in\\{r/2,r\\}$.",
             r"contains at least $\eta x/(2\log x)$ primes."),
           I("S8.1.10", "Choose distinct odd primes with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$; $\\gcd(s_i,t_i)=1$ since $t_i$ is a power of two.",
             r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
           I("S8.1.11", "Multiplying the lower bounds with strict Bernoulli gives $S/T>(1-\\frac1{2d})^d>\\frac12$, so $T/2<S<T$ with $S=\\prod s_i$.",
             r"\left(1-\frac1{2d}\right)^d>\frac12"),
           I("S8.1.12", "With $\\theta_i=t_i/s_i-1>\\eta$: $\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\ge6b=p$, so the resampling hypothesis $\\theta>p/\\alpha^4$ holds, and $t_i\\le T<2^p$.",
             r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
           I("S8.1.13", "The primes are found by deterministic trial division in time $O(dr^{3/2}\\operatorname{poly}(p))=n^{o(1)}=o(n)$.",
             r"$O(dr^{3/2}\operatorname{poly}(p))$"),
       ],
       page="parameter-choice",
       frm=["primes-coprimality-and-gcd", "logarithms-and-iterated-logarithm-notation", "floor-ceiling-and-summation-notation", "ring-convolution", "gaussian-resampling", "fast-butterfly-layer"],
       salient="Every exponent is a power of two with an enormous negative exponent ($\\epsilon=2^{-75}$, $c=2^{-56}$, $1-\\tau=2^{-50}$), chosen to make all hypotheses hold with room to spare rather than to optimize $\\kappa$.",
       adds=[B("b", "digit width", "The number $\\lceil\\log_2n\\rceil$ of bits per radix digit, so that the input has $\\lceil n/b\\rceil$ digits."),
             B("S", "prime-axis size", "The product $\\prod_is_i$ of the distinct prime source lengths, with $T/2<S<T$."),
             B("s_i", "prime length", "The distinct odd prime length of source axis $i$, just below $t_i$."),
             B("t_i", "power-of-two length", "The power-of-two length $r/2$ or $r$ of transform axis $i$.")])

P2 = S("S8.2",
       "Integer product as digit convolution: writing each input as $q=\\lceil n/b\\rceil$ digits in base $2^b$, the product polynomial has degree at most $2q-2<2n/b\\le T/2<S$ and coefficients $c_j\\le q(2^b-1)^2<2^{3b}$, so cyclic convolution modulo $x^S-1$ has no wraparound.",
       "Count degrees and bound a sum of at most $q\\le n\\le2^b$ products of digits below $2^b$.",
       ("Because the zero-padded length exceeds the product degree, cyclic and ordinary convolution agree.", "recoverable", None),
       [
           I("S8.2.1", "Write the two inputs as polynomials in $2^b$, each with $q=\\lceil n/b\\rceil$ nonnegative digits.",
             r"Write the two inputs as polynomials in $2^b$, each with"),
           I("S8.2.2", "The product has degree at most $2q-2<2n/b\\le T/2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
             r"2q-2<2n/b\le T/2<S."),
           I("S8.2.3", "Every product coefficient obeys $0\\le c_j\\le q(2^b-1)^2<2^{3b}$ since $q\\le n\\le2^b$.",
             r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
       ],
       page="radix-digit-convolution",
       frm=["cyclic-convolution", "polynomials", "binary-representation-and-bit-operations"])

P3 = S("S8.3",
       "Chinese-remainder address map: $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$, $x\\mapsto\\prod_ix_i^{\\mu_i}$ with $P_i=\\prod_{j<i}s_j$ and $\\mu_i=P_i^{-1}\\bmod s_i$, is an isomorphism preserving cyclic convolution, with $k=\\sum_ja_jP_j$ mapped to axis coordinates $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, computed by triangular controlled shifts in $O(Tpd^2(1+\\ell^\\tau))$ time.",
       "Show $\\Phi$ is an algebra isomorphism because the image of $x$ has order $S$ and runs through all monomials, then implement the coordinate formula as shifts of a later axis controlled by earlier axes, processing $i=d,d-1,\\dots,1$.",
       ("The sources use the Agarwal–Cooley split with coordinate powers making the change of order a sequence of controlled cyclic shifts.", "explicit",
        r"algebraic split, with coordinate powers that make the change of order a"),
       [
           I("S8.3.1", "Define $P_i=\\prod_{j<i}s_j$ and $\\mu_i=P_i^{-1}\\pmod{s_i}$ for pairwise coprime $s_i$.",
             r"P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}."),
           I("S8.3.2", "$\\Phi$ sends $x\\mapsto\\prod_ix_i^{\\mu_i}$, respects $x^S=1$, and so defines an algebra map.",
             r"x\longmapsto\prod_i x_i^{\mu_i}"),
           I("S8.3.3", "The image of $x$ has order $S$ because each $\\mu_i$ is a unit and the $s_i$ are coprime, so its powers run through all target monomials once: $\\Phi$ is an isomorphism and preserves cyclic convolution.",
             r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
           I("S8.3.4", "With the mixed-radix form $k=\\sum_ja_jP_j$, the coordinate of $\\Phi(x^k)$ on axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, since terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i\\equiv1$.",
             r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
           I("S8.3.5", "Insert zero padding in one nested scan of the box $\\prod_i[0,t_i)$, reorder axes to $(a_1,\\dots,a_d)$ and update targets in the order $i=d,d-1,\\dots,1$, so lower-index controls still hold original digits.",
             r"order $i=d,d-1,\ldots,1$ using"),
           I("S8.3.6", "On a fixed control prefix rotate the valid target interval $[0,s_i)$ by the offset and fix $[s_i,t_i)$; each step is a bijection preserving the valid set, so zero padding remains zero.",
             r"zero padding remains zero after every step."),
           I("S8.3.7", "Axes have widths $\\ell$ or $\\ell-1$ and reversing all axes uses $O(d^2)$ interchanges of unequal-width neighbors, so $\\Phi$, its inverse and their padding cost $O(Tpd^2(1+\\ell^\\tau))$.",
             r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
       ],
       page="crt-address-map",
       frm=["cyclic-convolution", "chinese-remainder-theorem", "controlled-shift", "address-chunk-interchange", "permutations-and-cartesian-products", "modular-arithmetic"])

P4 = S("S8.4",
       "Coefficient twist: $\\Theta:\\mathbb C[x_d]/(x_d^r-1)\\to\\mathcal R_r$, $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$, multiplies coefficient $k$ by $\\zeta^k$, and the negative wrap of $\\mathcal R_r$ becomes the original cyclic wrap after untwisting; hence $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
       "Check that $(\\zeta y)^r=1$ so $\\Theta$ is well defined, that it is diagonal and invertible, and that a wrapped term acquires the factor $\\zeta^j$.",
       ("The sources obtain the power-of-two complex convolution of the chirp identity from the synthetic convolution by a coefficient twist.", "explicit",
        r"obtained from the synthetic convolution by a coefficient twist."),
       [
           I("S8.4.1", "$\\Theta$ is the algebra map sending $x_d\\mapsto\\zeta y$.",
             r"x_d\longmapsto\zeta y"),
           I("S8.4.2", "It is well defined since $(\\zeta y)^r=(-1)(-1)=1$, diagonal on bases $(x_d^k)$ and $(y^k)$ with entries $\\zeta^k\\ne0$, hence an isomorphism with inverse multiplying coefficient $k$ by $\\zeta^{-k}$; both maps preserve the sup norm.",
             r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
           I("S8.4.3", "Wrap check: writing $k+l=j+hr$ with $h\\in\\{0,1\\}$, a product term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
             r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
           I("S8.4.4", "With $(D_\\pm f)_{\\boldsymbol j,k}=\\zeta^{\\pm k}f_{\\boldsymbol j,k}$ and $\\iota$ identifying the tensor with $M$ ring records, normalized complex convolution is $\\mathcal M_{\\mathbb C}(f,g):=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$, a bilinear contraction.",
             r":=D_-\iota^{-1}"),
           I("S8.4.5", "Computed version: $f'=Q_p(\\widetilde\\theta^+\\cdot f)$, $g'=Q_p(\\widetilde\\theta^+\\cdot g)$, $h'=\\widetilde{\\mathcal M}_r(\\iota f',\\iota g')$, output $Q_p(\\widetilde\\theta^-\\cdot\\iota^{-1}h')$, with twist factors $\\zeta^{\\pm k}$ computed to error below $2\\cdot2^{-p}$ in $O(p^{1+\\delta})$ per factor.",
             r"f'&=Q_p(\widetilde\theta^+\mathbin{\cdot}f),\\"),
       ],
       page="phase-twist",
       frm=["cyclic-convolution", "polynomial-ring-mod", "roots-of-unity", "complex-numbers"])

P5 = S("S8.5",
       "Chirp and source-transform procedures: the computed chirp transform $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,Q_p(\\overline{\\widetilde a}\\cdot x)))$ approximates $QF_{\\boldsymbol t}x$, and the source transform $\\widetilde{\\mathscr F}$ (resampling map $\\mathcal A$, chirp transform, resampling map $\\mathcal B_0$, scale $2^\\gamma$) approximates $RF_{\\boldsymbol s}$, with opposite-sign version by conjugation.",
       "Compose the chirp convolution with the Gaussian maps on the zero-padded box, computing chirp phases modulo $2r$ with the established multiplier, and obtain the opposite transform by conjugating input and output.",
       ("Composing the three maps of the resampling identity implements the source transform without executing either permutation.", "recoverable", None),
       [
           I("S8.5.1", "The chirp phase numerator at tensor address $j$ is computed modulo $2r$ as $-\\sum_is_ij_i^2(r/t_i)$ using the established multiplier, costing $O(Tdp^{1+\\delta})$.",
             r"-\sum_i s_i j_i^2(r/t_i)\pmod{2r}."),
           I("S8.5.2", "Chirp transform: $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$, $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot y_0)$, with $\\widetilde a$ the kernel and $x_0$ the data operand.",
             r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\"),
           I("S8.5.3", "The source transform applies $\\mathcal A$, then $\\widetilde{\\mathscr C}$, then $\\mathcal B_0$, then multiplies numerators by $2^\\gamma$; its exact counterpart is $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
             r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
           I("S8.5.4", "The opposite-sign procedure is $\\widetilde{\\mathscr F}^+(z)=\\overline{\\widetilde{\\mathscr F}(\\overline z)}$, with exact counterpart $RF^+_{\\boldsymbol s}$.",
             r"=\overline{\widetilde{\mathscr F}(\overline z)};"),
       ])

P6 = S("S8.6",
       "The algorithm: form radix digits, apply $\\Phi$, run two source transforms, multiply pointwise, run the opposite transform scaled by $S$, rescale by $2^{2b+4}S$, round to integers, undo $\\Phi$ and propagate carries to the $2n$-bit product.",
       "Prepare scaled digits $a_j2^{-b-2}$ as exact grid values below $1/4$, apply the six listed steps, and use the two scales $S$ and $2^{2b+4}$ to undo the normalizations $(u*v)/S^2$ and the input scalings.",
       ("The scalings are chosen so that the exact counterpart after the three transforms is $(u*v)/S^2$, which the two multiplications by $S$ and the input scale undo.", "recoverable", None),
       [
           I("S8.6.0", "Read each operand backward in groups of $b$ bits to get digits $a_0,\\dots,a_{q-1}$, write the exact grid numerator $a_j2^{p-b-2}$ (value $a_j2^{-b-2}$) as a real word with zero imaginary word, and append $S-q$ zero records.",
             r"Read each stored operand backward from"),
           I("S8.6.1", "Step 1: apply $\\Phi$ with padded layout to obtain source arrays $u,v$ of exact $p$-bit grid values of norm less than $1/4$.",
             r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
           I("S8.6.2", "Step 2: compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
             r"Compute $\widetilde{\mathscr F}(u)$ and"),
           I("S8.6.3", "Step 3: multiply the corresponding coefficients exactly and truncate each part to $p$ fractional bits, giving $z$.",
             r"Multiply corresponding complex coefficients exactly and truncate"),
           I("S8.6.4", "Step 4: compute $\\widetilde{\\mathscr F}^+(z)$ and multiply its numerators exactly by $S$, giving $\\widetilde w$.",
             r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
           I("S8.6.5", "Step 5: multiply by $2^{2b+4}S$, round the real values to nearest integers (a signed $(3b+1)$-bit word per valid address) and apply $\\Phi^{-1}$ with padding removal.",
             r"Multiply the grid numerators of $\widetilde w$ exactly by"),
           I("S8.6.6", "Step 6: propagate radix-$2^b$ carries in increasing order and output exactly $2n$ bits most significant first.",
             r"Propagate radix-$2^b$ carries in increasing coefficient order."),
           I("S8.6.7", "The two occurrences of $S$ undo different normalizations: the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$.",
             r"The two occurrences of $S$ in this algorithm undo different"),
       ])

P7p = S("S8.7",
        "Error propagation: each computed procedure is within a few multiples of $TL\\,2^{-p}$ of its exact map ($L=\\log_2T$): the ring convolution has error $<5TL$, the complex convolution $<6TL$, the chirp transform $<8TL$, and the source transform $<E_s=9\\cdot2^\\gamma TL$ units of $2^{-p}$, with all intermediate arrays staying inside the unit disk.",
        "Insert the exact bilinear or linear contraction at each computed input and add its error to the propagated input error (bilinear contraction bound $\\|f'\\|\\|g'-g\\|+\\|g\\|\\|f'-f\\|$), checking norms $.5\\to.51\\to.701\\to.501$ to stay in the disk.",
        ("Each step of the chain adds its own truncation error to the contraction-propagated error of its input.", "recoverable", None),
        [
            I("S8.7.1", "Ring convolution: three transform errors and the polynomial-product truncation total less than $3L+2$ before the scale $M$, so $E_{\\rm ring}:=M(3L+2)<5TL$ (units of $h_p=2^{-p}$), and the output has norm below $.7+5TLh_p<.701$.",
              r"E_{\rm ring}:=M(3L+2)<5TL."),
            I("S8.7.2", "Complex convolution with twists: inserting the exact $\\mathcal M_r$ propagates two input twist errors (each below 4), the approximation contributes $E_{\\rm ring}$ and the output untwist below 4, giving error below $6TLh_p$.",
              r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
            I("S8.7.3", "Chirp transform: kernel error 2, first phase 4, convolution $6TL$, last phase 4, so $\\|\\widetilde{\\mathscr C}(x)-QF_{\\boldsymbol t}x\\|<8TLh_p$.",
              r"<(6TL+2+4+4)h_p<8TLh_p."),
            I("S8.7.4", "Source transform: expansion error $dp^2$, chirp $8TL$ and compression $dp^2$ give $2dp^2+8TL$ before the scale, so after the scale by $2^\\gamma$ the error is below $E_sh_p$ with $E_s=9\\cdot2^\\gamma TL$ (using $2dp^2<TL$).",
              r"E_s=9\,2^\gamma TL,"),
        ],
        adds=[B("E_s", "source error", "The bound $9\\cdot2^\\gamma TL$ (in units of $2^{-p}$) on the error of the computed source transform."),
              B("L", "log of padded size", "The integer $\\log_2T$.")])

P7 = S("S8.8",
       "Exact recovery: rescaling the computed product by the known factors $S$ and $2^{2b+4}$ leaves coefficient error below $448b\\,2^{-3b/4}<1/2$, so rounding yields the exact integer coefficients $c_j<2^{3b}$, and radix-$2^b$ carries produce the $2n$-bit product.",
       "Propagate the source error $E_s$ through the pointwise product and the opposite transform, multiply by the scale factors, compare the final error with $1/2$ using $p=6b$, and then run the carry recurrence.",
       ("The sources say a strict error below one half makes the nearest integer the unique correct coefficient.", "explicit",
        r"that value the unique correct coefficient."),
       [
           I("S8.8.1", "Pointwise step: $\\widetilde U\\cdot\\widetilde V_1-U\\cdot V_1=(\\widetilde U-U)\\cdot\\widetilde V_1+U\\cdot(\\widetilde V_1-V_1)$ with norms below $.26$ and one truncation, giving $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.",
             r"Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$."),
           I("S8.8.2", "Opposite transform: since $G=RF^+_{\\boldsymbol s}$ is a contraction with $G(U\\cdot V_1)=(u*v)/S^2$, the error is below $(3E_s+2)h_p$.",
             r"&<(3E_s+2)h_p."),
           I("S8.8.3", "After the first scale by $S<2^b$, $\\widetilde w$ approximates $w=(u*v)/S$ with error below $E_wh_p$, $E_w:=S(3E_s+2)<28\\cdot2^\\gamma T^2L$, and $\\|\\widetilde w\\|<1/16+10^{-3}<1$ since $\\|w\\|<1/16$.",
             r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
           I("S8.8.4", "The integer coefficient array is $2^{2b+4}Sw$: the second $S$ reverses the normalization in $w$ and $2^{2b+4}$ the two input scales $2^{-b-2}$ each.",
             r"2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}"),
           I("S8.8.5", "Final absolute error $<2^{2b+4}S\\cdot28\\cdot2^\\gamma T^2L\\cdot2^{-6b}<448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<\\frac12$, using $S\\le T<2^b$, $L<b$, $p=6b$ and $\\gamma\\le b/4$.",
             r"\le448b\,2^{-3b/4}<\frac12.",
             salient="The precision $p=6b$ is chosen so that the factor $2^{-6b}$ beats the scale $2^{2b+4}$ and the two factors $T\\cdot S$ both below $2^b$, leaving the tiny error $2^{-3b/4+O(\\log b)}$."),
           I("S8.8.6", "The true coefficients are integers, so rounding the represented value $H_j/2^p$ to the nearest integer gives the unique correct $c_j\\in[0,2^{3b})$ (fitting a signed $(3b+1)$-bit word).",
             r"The strict error below $1/2$ makes the nearest integer to"),
           I("S8.8.7", "Carry recurrence: $k_0=0$, $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$.",
             r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,"),
           I("S8.8.8", "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$, since $c_j+k_j\\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$.",
             r"The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$."),
           I("S8.8.9", "The invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ shows the digits $d_j$ are the radix digits of the product.",
             r"\sum_{h<j}c_hQ_0^h"),
           I("S8.8.10", "The product is less than $2^{2n}$, so all bits above position $2n-1$ are zero; drop only them to output exactly $2n$ bits (zero inputs behave the same).",
             r"than $2^{2n}$; all bits above position $2n-1$ are therefore zero."),
       ],
       page="exact-recovery",
       frm=["fixed-point-truncation", "radix-digit-convolution", "norms-absolute-values-and-error-bounds", "recurrences-and-induction", "binary-representation-and-bit-operations"])

C8 = S("S8",
       "The multiplication algorithm: form base-$2^b$ digits, place them on distinct prime cyclic axes by the Chinese-remainder map $\\Phi$, run two source transforms (Gaussian resampling plus chirp convolution through a twisted ring convolution), multiply pointwise, run the opposite transform, rescale, round and propagate carries, obtaining the exact $2n$-bit product in $O(Tp)$ steps beyond the layer costs.",
       "Choose compatible parameters, reduce the product to a cyclic convolution of digit coefficients, evaluate the convolution through Gaussian-resampled transforms with all permutations left in the formulas, and recover exact integer coefficients from the approximations by an error bound below one half.",
       ("A reader can follow how each reduction converts the problem into the shape the next tool handles: integer product, prime-axis convolution, power-of-two convolution, polynomial-ring convolution.", "recoverable", None),
       [P1, P2, P3, P4, P5, P6, P7p, P7],
       page="multiplication-algorithm",
       frm=["parameter-choice", "radix-digit-convolution", "crt-address-map", "phase-twist", "gaussian-resampling", "permutation-cancellation", "bluestein-chirp", "ring-convolution", "exact-recovery", "established-multiplier"],
       salient="A single reduction chain converts an integer product into a convolution on a product of prime-length axes, then into power-of-two axes with permutations never executed, then into a polynomial-ring convolution where the roots of unity are signed shifts.")

# ---------------------------------------------------------------- time accounting
T1 = S("S9.1",
       "Dividing every cost by $V=Tp=\\Theta(n)$ gives seven dominant powers of $p$, namely $\\epsilon(1+c)$, $1-\\epsilon c(1-\\tau)$, $1-\\epsilon(1-\\lambda')$, $\\tau+\\epsilon(2-\\tau)$, $3/4+\\delta+3\\epsilon/2$, $\\epsilon+\\delta$ and $1-\\epsilon$.",
       "Tabulate the normalized cost of each operation from the lemmas, using $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$.",
       ("Each table row is the cost of one stage from its own lemma expressed in powers of $p$.", "recoverable", None),
       [
           I("S9.1.0", "Put $V=Tp=\\Theta(n)$: fixed-width coefficient formats use $\\Theta(p)$ bits so the padded array has $\\Theta(V)$ stored bits, and costs are listed after division by $V$.",
             r"For the cost calculation put $V=Tp=\Theta(n)$."),
           I("S9.1.1", "Prefix-slot moves and individual butterfly rounds cost $dK$, power of $p$ equal to $\\epsilon(1+c)$.",
             r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\"),
           I("S9.1.2", "Chunk exchanges for transform layout cost $pK^{\\tau-1}$, power $1-\\epsilon c(1-\\tau)$.",
             r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\"),
           I("S9.1.3", "Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, power $1-\\epsilon(1-\\lambda')$.",
             r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\"),
           I("S9.1.4", "CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, power $\\tau+\\epsilon(2-\\tau)$.",
             r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\"),
           I("S9.1.5", "Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, power $3/4+\\delta+3\\epsilon/2$.",
             r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\"),
           I("S9.1.6", "Chirps, twists and scalar products cost $dp^\\delta$, power $\\epsilon+\\delta$.",
             r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\"),
           I("S9.1.7", "Packed polynomial products cost $\\log(rp)$, power $1-\\epsilon$; final scaling, input, padding, carries and output are absorbed by these rows.",
             r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\"),
       ],
       adds=[B("\\delta", "exponent slack", "The fixed exponent $1/16$ used in the Gaussian and multiplier costs $p^{1+\\delta}$.")])

T2 = S("S9.2",
       "Each of the seven dominant powers is at most $1-2\\kappa$: the margins $g_1,\\dots,g_7$ below one are $g_1=1-\\epsilon(1+c)>\\frac12$, $g_2=\\epsilon c(1-\\tau)=2^{-181}$, $g_3=\\epsilon(1-\\lambda')=2^{-129}$, $g_4=1-\\tau-\\epsilon(2-\\tau)>2^{-51}$, $g_5=\\frac14-\\delta-\\frac32\\epsilon>\\frac18$, $g_6=1-\\delta-\\epsilon>\\frac12$, $g_7=\\epsilon=2^{-75}$, with minimum $2^{-181}=2\\kappa$.",
       "Substitute the fixed values $\\epsilon=2^{-75}$, $c=2^{-56}$, $1-\\tau=2^{-50}$, $1-\\lambda'=2^{-54}$, $\\delta=1/16$ into each margin and take the minimum.",
       ("The sources say the explicit slack will cover any remaining fixed power of $\\log p$.", "explicit",
        r"any remaining fixed power of $\log p$."),
       [
           I("S9.2.1", "The margins below one are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4=1-\\tau-\\epsilon(2-\\tau)$, $g_5=1/4-\\delta-3\\epsilon/2$, $g_6=1-\\delta-\\epsilon$, $g_7=\\epsilon$.",
             r"g_1&=1-\epsilon(1+c),\qquad"),
           I("S9.2.2", "Direct substitution gives $g_1>\\frac12$, $g_2=2^{-181}$ (from $2^{-75}\\cdot2^{-56}\\cdot2^{-50}$), $g_3=2^{-129}$ (from $2^{-75}\\cdot2^{-54}$), $g_4>2^{-51}$, $g_5>\\frac18$, $g_6>\\frac12$ and $g_7=2^{-75}$.",
             r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
           I("S9.2.3", "Thus $\\min_ig_i=2^{-181}=2\\kappa$, so each power is at most $1-2\\kappa$ and $\\kappa=2^{-182}$.",
             r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
             salient="The saving $\\kappa=2^{-182}$ is exactly half of the smallest margin $g_2=\\epsilon c(1-\\tau)=2^{-75-56-50}$, which comes from the chunk-exchange row $pK^{\\tau-1}$: its saving is the product of the three tiny exponents $\\epsilon$ (axes), $c$ (chunk width) and $1-\\tau$ (swap saving)."),
       ])

T3 = S("S9.3",
       "Each table row is justified from its lemma: row costs come from the transform layout lemma, the simultaneous layer, axis exposure, Gaussian lines, chirps and packed products, while setup and exceptional streams cost $o(Tp)$ in total.",
       "Sum the stated costs per row and show that every setup term has the form $O(Tp^C/r)$ or $2^{-K}p^{A'}V$, both negligible because $r$ exceeds every fixed power of $p$ and $K$ grows polynomially in $p^{\\epsilon c}$.",
       ("Because $r$ is superpolynomial in $p$, any polynomial setup per record is negligible against the $\\Theta(rp)$ record bits.", "recoverable", None),
       [
           I("S9.3.1", "Chunk exchanges: $O(p/K)$ exchanges of width-$K$ chunks, each $O(VK^\\tau)$, normalized $O(p/K)K^\\tau=O(pK^{\\tau-1})$.",
             r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
           I("S9.3.2", "Axis exposure and restoration need $O(d^2)$ adjacent axis moves each costing $O(V(1+\\ell^\\tau))$; the $d$ CRT rotations cost $O(dV)$.",
             r"Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths"),
           I("S9.3.3", "Gaussian lines: $\\sum_{i=1}^d\\frac T{t_i}O(t_ip^{3/2+\\delta}\\alpha)=O(dTp^{3/2+\\delta}\\alpha)$, and dividing by $V=Tp$ gives the fifth row since $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$.",
             r"Dividing by $V=Tp$ gives the fifth row."),
           I("S9.3.4", "Chirp numerators cost $O(dp^{1+\\delta})$ per entry with the established multiplier, and twists and scalar products fit the same row.",
             r"costs $O(dp^{1+\delta})$ per entry."),
           I("S9.3.5", "Four integer products on $O(rp)$ bits per record, for $T/r$ records, cost $O(Tp\\log(rp))$ in total, using the established multiplier on records of length $O(rp)=o(n)$ without calling the improved algorithm.",
             r"$O(Tp\log(rp))$ in total."),
           I("S9.3.6", "Recursion nodes and rounds are at most $p^A$ in number with setup at most $p^C$ each, so their total setup is $p^{A+C}=o(Tp)$.",
             r"$p^{A+C}=o(Tp)$."),
           I("S9.3.7", "The compact exceptional stream of each packed call has length $O(V_{\\rm call}d2^{-K})$ and its radix passes cost $O(V_{\\rm call}dp2^{-K})$, so over all calls they total $O(Vp^{A'}2^{-K})=o(V)$, a deterministic worst-case bound.",
             r"=O(Vp^{A'}2^{-K})=o(V)"),
       ])

T4 = S("S9.4",
       "Total: any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the cost is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$; with schoolbook multiplication below a fixed cutoff, one fixed machine runs in $O(n(\\lg n)^{1-\\kappa})$ for every $n\\ge1$.",
       "Combine the seven rows with the margin $2\\kappa$ and absorb finitely many small lengths in the constant.",
       ("Taking the margin $2\\kappa$ per row leaves room for a $p^{\\kappa}$ factor, so the bound is $p^{1-\\kappa}$.", "recoverable", None),
       [
           I("S9.4.1", "Each of the seven powers is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
             r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
           I("S9.4.2", "The complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
             r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
           I("S9.4.3", "Below a fixed cutoff use schoolbook multiplication; the finitely many smaller lengths are absorbed by enlarging the implicit constant, giving one fixed-alphabet, fixed-tape deterministic machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
             r"many smaller lengths are included by enlarging the implicit constant."),
       ])

C9 = S("S9",
       "Cost accounting: dividing every cost by $V=Tp=\\Theta(n)$, the algorithm's seven dominant costs are at most $p^{1-2\\kappa}$ per unit volume, giving total time $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
       "Tabulate the normalized cost of every stage, compute each stage's margin below one, and take the smallest margin.",
       ("The dominant exponents are read off a table and compared with one.", "recoverable", None),
       [T1, T2, T3, T4],
       page="time-accounting",
       frm=["parameter-choice", "address-chunk-interchange", "fast-butterfly-layer", "ring-convolution", "gaussian-resampling", "crt-address-map", "multiplication-algorithm", "established-multiplier"],
       salient="The final exponent $1-\\kappa$ is limited by the smallest of seven margins, $2^{-181}$, which belongs to the chunk-exchange row; every other row has a much larger margin.")

ROOT = S("S0",
         "A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
         "Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs.",
         ("The sources note that scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both movement and arithmetic need savings.", "explicit",
          r"We therefore need savings in both movement and arithmetic."),
         [C1, C2, C3, KEY, C5, C6, C7, C8, C9],
         page="main-theorem",
         frm=["multitape-tm", "big-o", "logarithms-and-iterated-logarithm-notation", "integer-multiplication-conjecture"],
         salient="The logarithmic factor drops to a power strictly below one although a transform with $\\Theta(\\log n)$ levels, each scanning $\\Theta(n)$ bits, naively costs $\\Theta(n\\log n)$.",
         adds=[B("n", "operand length", "The number of bits of each of the two input integers.", "count"),
               B("\\kappa", "saving exponent", "The fixed constant $2^{-182}$ such that the running time is $O(n(\\lg n)^{1-\\kappa})$.")])

answer = {"root": ROOT}

# ------------------------------------------------------------ validation
def walk(n, parent_page, out):
    pg = n.get("page") or parent_page
    out.append((n, pg))
    for c in n.get("children", []):
        walk(c, pg, out)

nodes = []
walk(ROOT, None, nodes)
ids = [n["id"] for n, _ in nodes]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
pidx = {p: i for i, p in enumerate(PAGES)}
errs = []
used_pages = {}
for n, pg in nodes:
    if n.get("page"):
        if n["page"] in used_pages:
            errs.append("page used twice: %s %s %s" % (n["page"], used_pages[n["page"]], n["id"]))
        used_pages[n["page"]] = n["id"]
        if n["page"] not in pidx:
            errs.append("bad page " + n["page"])
    for f in n.get("from", []):
        if f in KNOWN:
            continue
        if f not in pidx:
            errs.append("bad from %s in %s" % (f, n["id"]))
        elif pg is None or pidx[f] >= pidx[pg]:
            errs.append("from %s not before page %s in %s" % (f, pg, n["id"]))
all_from = set()
for n, pg in nodes:
    all_from.update(n.get("from", []))
for p in PAGES:
    if p not in used_pages and p not in all_from:
        errs.append("page without step and not in from: " + p)
# quotes in DFS order
pos = 0
infers = [n for n, _ in nodes if n["intention"] == "infer"]
last = -1
for n in infers:
    q = n["quote"]["quote"]
    c = SRC.count(q)
    if c == 0:
        errs.append("MISSING quote %s: %r" % (n["id"], q)); continue
    if c > 1:
        errs.append("NONUNIQUE quote %s (%d): %r" % (n["id"], c, q))
    if n.get("deferred"):
        continue
    p = SRC.find(q, last + 1) if c > 0 else -1
    p0 = SRC.find(q)
    if p0 <= last:
        # try later occurrence
        errs.append("ORDER quote %s at %d <= %d: %r" % (n["id"], p0, last, q))
    last = max(last, p0)
for n, _ in nodes:
    if n["intention"] == "show":
        mq = n["motivation"].get("quote")
        if mq and SRC.count(mq["quote"]) == 0:
            errs.append("MISSING motivation quote %s: %r" % (n["id"], mq["quote"]))
        if n["motivation"]["source"] == "explicit" and not mq:
            errs.append("explicit w/o quote " + n["id"])
# adds symbols occur below
def descendants_claims(n):
    out = []
    for c in n.get("children", []):
        out.append(c["claim"])
        out.extend(descendants_claims(c))
    return out
for n, _ in nodes:
    for b in n.get("adds", []):
        sym = b["symbol"]
        if not any(sym in cl for cl in descendants_claims(n)):
            errs.append("adds symbol %s of %s not in descendants" % (sym, n["id"]))
print("nodes", len(nodes), "infers", len(infers))
if errs:
    print("\n".join(errs))
    sys.exit(1)
OUT = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E9F4Y/exegenius/tasks/0003-argument.answer.json'
json.dump(answer, open(OUT, 'w'), indent=1, ensure_ascii=False)
print("written")
