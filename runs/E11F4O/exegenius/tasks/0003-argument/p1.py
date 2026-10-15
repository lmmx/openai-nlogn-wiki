from lib import ev, bind, infer, show


def s1():
    return infer(
        "S1",
        r"To refute the conjecture in the fixed-tape model it suffices to exhibit one machine $A$ with $\liminf_{n\to\infty}T_A(n)/(n\lg n)=0$, and a bound $T_A(n)=O(n(\lg n)^{1-\kappa})$ with $\kappa>0$ makes this ratio tend to zero through all input lengths.",
        r"The power saving proved here gives a limit of zero through all input lengths, which is a stronger conclusion.",
        frm=["big-o", "multitape-tm", "logarithms-and-iterated-logarithm-notation",
             "big-omega-theta-and-little-o-notation"],
        page="integer-multiplication-conjecture",
    )


def s21():
    return show(
        "S2.1",
        r"On a fixed number of tapes, arrays stored in lexicographic address order admit linear-time primitives: permuting or moving fixed-radix digits, splitting on a digit to apply a pointwise map and merging, dealing whole rows cyclically to $W$ streams, and cyclically shifting a target field by an offset computed from earlier fields, each in $O(V)$ steps.",
        r"Split the ordered stream on the relevant digits or at the shift offset and merge the pieces in the required order, charging counters and descriptor arithmetic to the scanned volume.",
        r"Addresses are implicit in positions, so moving one fixed-radix digit or rotating a field that follows its controls only splits and merges ordered streams a bounded number of times, unlike interchanging fields whose number of digits grows.",
        "explicit",
        [
            infer(
                "S2.1.1",
                r"For a fixed radix $q\ge2$, permuting the digit values at two positions, moving one digit, splitting on a digit to apply a fixed pointwise map and merging, and dealing whole rows of $[P]\times[R]\times[B]$ cyclically into $W$ streams of volume $V/W$ each (merging back when $W$ divides $R$) all take $O(V)$ steps, counters and cleanup included.",
                r"Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes",
                frm=["tape-address-model", "sorting-and-data-movement-on-tapes",
                     "binary-representation-and-bit-operations",
                     "permutations-and-cartesian-products"],
                page="elementary-stream-ops",
            ),
            infer(
                "S2.1.2",
                r"If a target field ranging over $[Q]$, with $Q$ a power of a fixed prime $q$, follows its control fields, the update $y\mapsto y+a(\text{controls})\bmod Q$ costs $O(V)$ by splitting each fiber at $Q-a$ and merging the two pieces in the opposite order, provided the offset takes time polynomial in $\log Q$; multiplication of the target by a fixed rational unit, and negation, also cost $O(V)$.",
                r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values.",
                frm=["elementary-stream-ops", "tape-address-model", "modular-arithmetic",
                     "primes-coprimality-and-gcd"],
                page="controlled-shift",
            ),
        ],
        mot_quote=r"We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow.",
        frm=["multitape-tm", "sorting-and-data-movement-on-tapes",
             "finite-alphabet-encodings-and-constant-factor-simulation",
             "binary-representation-and-bit-operations"],
        page="tape-address-model",
    )


def s221():
    P = "linear-network"
    F = ["linear-algebra-basics", "finite-field-f2-arithmetic", "complex-numbers",
         "permutations-and-cartesian-products"]
    return show(
        "S2.2.1",
        r"For arbitrary initial scratch values a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, so a forward stage 1, an inverse stage 2 and a forward stage 3 send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restore every scratch wire; in the bit network this is the permutation exchanging $X_a$ and $Y_a$.",
        r"Run in each invocation an eight-row schedule of copy, gather, scatter and side-injection gates that first subtracts the effect of the old scratch values, then adds the source's effect, then restores the scratch, and check through intersection sizes that gather-scatter plus side injection has identity coefficients.",
        r"Rows dealt to scratch roles carry arbitrary data, so the exchange must hold and restore for every initial scratch value; subtracting the old scratch effect first makes the net change independent of it, and routing through $h$ central wires keeps the gather and scatter low-rank.",
        "recoverable",
        [
            infer("S2.2.1.1",
                  r"At stage $j\in\{1,2,3\}$ the network fixes the other two coordinates of $a\in\mathcal T^3$ and runs one invocation on the $v$ values of each bank that vary coordinate $j$, so there are $v^2$ invocations per stage and $I=3v^2=78440670000$ in all, each with its own scratch wires: side wires $A_{ST}$ for neighbouring ordered pairs of triples and central wires $C_i$, $i\in[h]$, plus $C_\ast$ in the complex network.",
                  r"Thus there are $v^2$ separate invocations at each stage.", frm=F),
            infer("S2.2.1.2",
                  r"In the bit network (scalars in $\mathbb F_2$) triples $S,T$ are neighbours when $|S\cap T|=1$, copy adds $x_T$ to $A_{ST}$, side injection adds $\sum_{T:|S\cap T|=1}A_{ST}$ to $y_S$, gather adds $\sum_{T\ni i}x_T$ to $C_i$ and scatter adds $\sum_{i\in S}C_i$ to $y_S$; in the complex network (scalars in $\mathbb Z[i,1/2]$) neighbours are distinct triples with even intersection, side injection adds $-\sum_T\frac{|S\cap T|-1}{2}A_{ST}$, gather also adds $\sum_Tx_T$ to $C_\ast$, and scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$.",
                  r"In the bit construction, scalars lie in $\mathbb F_2$, and $S,T$ are neighbors when $|S\cap T|=1$.", frm=F),
            infer("S2.2.1.3",
                  r"A forward invocation runs eight rows, 0 subtract side injection, 1 subtract scatter, 2 copy, 3 gather, 4 scatter, 5 side injection, 6 undo gather, 7 undo copy: rows 0-1 remove the effect of the old scratch values, rows 2-5 introduce the source values and add their effect to the target, and rows 6-7 restore the scratch values.",
                  r"the next four introduce the source values and add their effect to the target; the last two restore the scratch values.", frm=F),
            infer("S2.2.1.4",
                  r"With initial side and central vectors $a,c$, rows 0-1 subtract $\mathcal Ja+\mathcal Rc$ from $y$, rows 2-3 change the scratch to $a+\mathcal Vx$ and $c+\mathcal Gx$, rows 4-5 add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$, and rows 6-7 restore $a,c$, so the net target change $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ does not depend on the scratch values.",
                  r"The net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$.", frm=F),
            infer("S2.2.1.5",
                  r"The net coefficient from $x_T$ to $y_S$ is the identity: in the bit network the central coefficient is $|S\cap T|\bmod2$ and the side wires cancel exactly the intersection-one cases, while intersections zero and two already give zero and the self coefficient is one; in the complex network the central coefficient is $(|S\cap T|-1)/2$, the side wires cancel intersections zero and two, intersection one already gives zero, and the self coefficient is one.",
                  r"Thus both net maps are $y\gets y+x$.", frm=F),
            infer("S2.2.1.6",
                  r"Since the inverse schedule with logical source $Y$ and target $X$ effects $X\gets X-Y$, the three stages send $(x,y)$ to $(x,y+x)$, then to $(-y,y+x)$, then to $(-y,x)$, each invocation restoring its own scratch wires.",
                  r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.", frm=F),
            infer("S2.2.1.7",
                  r"A triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit network and $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ in the complex one, each invocation has $vz$ ordered side wires and $c_{\rm b}=100$ or $c_{\rm c}=101$ central wires, so the wire counts are $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ and $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$, fixed independently of the input length.",
                  r"W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})", frm=F),
        ],
        frm=F,
        page=P,
        adds=[bind("I", "invocation count",
                   r"The number $I=3v^2=78440670000$ of invocations over the three stages, each with its own scratch wires.",
                   "count")],
        salient=r"The exchange is exact for arbitrary, unknown initial scratch values and returns each of them unchanged.",
    )


def s223():
    F = ["linear-algebra-basics", "linear-network", "finite-field-f2-arithmetic",
         "vectors-matrices-and-invertibility"]
    return show(
        "S2.2.3",
        r"Nondegenerate subspaces of $\mathcal F$ (dimension $m$) can label all sources, gates and sinks so that every edge joins nested labels and the absolute dimension changes sum to $Wm-2N+2L$ with $L=Ich$, where $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ are both below $1/2$.",
        r"Pair triple indicator vectors by a form that makes neighbours orthogonal, prescribe the terminal labels, expose one tensor factor per stage, order the gates so that only the central wires' return loses dimension, and tabulate every edge's orthogonal residual.",
        r"Because neighbouring triple lines are orthogonal, side-wire labels can grow through nested subspaces, confining every loss of dimension to the central wires.",
        "explicit",
        [
            infer("S2.2.3.1",
                  r"For the bit network $F=\mathbb Q^h$ with $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ (eigenvalues $1$ and $-91/9$) gives $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$, and for the complex network $F=\mathbb F_2^h$ with the dot product gives $t_T\cdot t_T=1$, so in both every triple line is nondegenerate and neighbouring triple lines are orthogonal.",
                  r"Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction.", frm=F),
            infer("S2.2.3.2",
                  r"The terminal labels are $U_a\to\mathcal F$ on $X_a$, $0\to U_a^\perp$ on $Y_a$ and $0\to\mathcal F$ on every scratch role, so source dimensions sum to $N$, sink dimensions to $Wm-N$, gate contributions cancel, the signed changes sum to $Wm-2N$, and a total loss $L$ on decreasing edges makes the absolute sum $Wm-2N+2L$.",
                  r"Thus the signed dimension changes will sum to $Wm-2N$, because the contributions at gates cancel.", frm=F),
            infer("S2.2.3.3",
                  r"At stage $j$, with $A=F^{\otimes(j-1)}$, $P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$, $B=P^\perp\subset A$ and $Q=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$, a data wire with triple indicator $t$ passes from $A\otimes\langle t\rangle\otimes Q$ to $(A\otimes F)\otimes Q$ on $X$ and from $B\otimes\langle t\rangle\otimes Q$ to $((B\otimes F)\perp(P\otimes t^\perp))\otimes Q$ on $Y$, and with $A'=A\otimes F$ and $P'=P\otimes\langle t\rangle$ these are the next stage's incoming labels, starting at $U_a$ and $0$ and ending at $\mathcal F$ and $U_a^\perp$.",
                  r"These transitions expose one tensor factor at each stage.", frm=F),
            infer("S2.2.3.4",
                  r"With gates touching the wires in the order $Y$-side, $Y$-center, $X$-side, $X$-center, $Y$-center, $Y$-side, $X$-center, $X$-side, the common gate labels (tensored by $Q$) at times $0,\dots,7$ are $B\otimes\langle t\rangle$, $B\otimes F$, $(B\otimes F)\perp(P\otimes\langle t\rangle)$, $A\otimes F$, $B\otimes F$, $(B\otimes F)\perp(P\otimes t^\perp)$, $A\otimes F$ and $A\otimes F$, so a central wire returns once from $A\otimes F$ to $B\otimes F$, losing $P\otimes F$.",
                  r"The gate order below confines all decreases to this return, while the other edges realize the prescribed stage transitions.", frm=F),
            infer("S2.2.3.5",
                  r"Every edge joins comparable nondegenerate labels and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$, so $L=Ich$; the residuals are $B\otimes t_X^\perp$ and $P\otimes t_X^\perp$ on $X$, $B\otimes t_Y^\perp$ and $P\otimes t_Y^\perp$ on $Y$, $B\otimes F$ and then $P\otimes F$ three times on a central wire, $B\otimes\langle t_Y\rangle$, $(B\otimes t_Y^\perp)\perp(P\otimes\langle t_X\rangle)$, $P\otimes\langle t_X,t_Y\rangle^\perp$ (of dimension $h-2$, using $t_X\perp t_Y$) and $P\otimes\langle t_Y\rangle$ on a side wire, $(A\otimes F)\otimes Q^\perp$ on each scratch sink edge, and zero elsewhere.",
                  r"The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$.", frm=F),
            infer("S2.2.3.6",
                  r"Over $\mathbb F_2$ every nonzero edge residual is nondegenerate and contains a vector of norm one, so it has an orthonormal basis, alternating planes being absorbed into a unit line through the vectors $w+a$, $w+b$, $w+a+b$.",
                  r"For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis.", frm=F),
            infer("S2.2.3.7",
                  r"With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation the loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
                  r"In particular, both are smaller than $1/2$.", frm=F),
        ],
        mot_quote=r"Orthogonality of the corresponding indicator vectors permits the subspace assignments.",
        frm=F,
        adds=[
            bind(r"\mathcal F", "label space",
                 r"The ambient label space $F^{\otimes3}$ of dimension $m=h^3$, with $F=\mathbb Q^h$ for the bit network and $F=\mathbb F_2^h$ for the complex network."),
            bind(r"t_T", "triple indicator",
                 r"The indicator vector in $F$ of a three-element subset $T$ of $[h]$."),
            bind(r"U_a", "source line",
                 r"The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of the data role $X_a$."),
        ],
    )


def s224():
    F = ["linear-algebra-basics", "common-frame-principle", "address-shear",
         "vectors-matrices-and-invertibility"]
    return show(
        "S2.2.4",
        r"Giving each gate or sink with label $U$ the projection $P_U$ onto $U$ along $U^\perp$, the source of $X_a$ the matrix $-P_{U_a}$ and every other source zero yields rational matrices with $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ on every role and total edge rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}=177176569088785861287000000<W_{\rm b}m$.",
        r"Read the rank of each edge difference $P_V-P_U$ off the label dimensions and add the exceptional source edges.",
        r"With frames given by address shears $(H,D)\mapsto(H+MD,D)$, an endpoint difference $I_m$ makes every routed role undergo the same shear $H\gets H+D$, while an edge of rank $a$ can be paid for with $a$ smaller interchanges.",
        "explicit",
        [
            infer("S2.2.4.1",
                  r"For nested nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its complement, so its rank is $\dim V-\dim U$, and reversing the edge only negates the matrix.",
                  r"Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank.", frm=F),
            infer("S2.2.4.2",
                  r"The only exceptions are the $N$ negative source projections: at stage 1 the first gate on $X_a$ has label exactly $U_a$, so that edge's matrix is $2P_{U_a}$, of rank one although its dimension change is zero, adding $N$ to the rank sum.",
                  r"Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero.", frm=F),
            infer("S2.2.4.3",
                  r"Hence $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N$, whose deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$ because $L_{\rm b}<N/2$.",
                  r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.", frm=F),
            infer("S2.2.4.4",
                  r"For an input $X_a$ (routed to $Y_a$) the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix, so every endpoint difference is $I_m$.",
                  r"For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$.", frm=F),
        ],
        mot_quote=r"The following identity makes it the same shear $H\gets H+D$ on every role;",
        frm=F,
    )


def s225():
    F = ["linear-algebra-basics", "finite-field-f2-arithmetic", "complex-numbers",
         "common-frame-principle"]
    return show(
        "S2.2.5",
        r"With phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, where $q_U(x)=\operatorname{wt}(P_Ux)\bmod4$, each edge's frame change is a product of one translation kernel $\frac{1+i}{2}I+\frac{1-i}{2}X_v$ or its inverse per vector of an orthonormal residual basis, these number $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$, and after diagonal corrections every role receives $C^{\otimes m}$.",
        r"Use additivity of Hamming weight modulo four on orthogonal binary vectors to split each phase change into one factor per residual basis vector, conjugate each factor by Hadamard matrices into a translation kernel, and repair the one non-standard endpoint with signs and a phase.",
        r"Orthogonal decompositions of labels make Hamming-weight phases additive, so each residual basis vector contributes one independent two-point kernel and the residual count of the labels becomes the number of smaller calls.",
        "recoverable",
        [
            infer("S2.2.5.1",
                  r"Since $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}z\cap\operatorname{supp}w|$, weight is additive modulo four when $z\cdot w=0$, so for $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$ one has $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod4$, negated on a decreasing edge.",
                  r"If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four.", frm=F),
            infer("S2.2.5.2",
                  r"Each basis vector has odd weight, so its phase is $i^{\varepsilon[v\cdot x]}=\frac{1+i^\varepsilon}{2}+\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}$ with $\varepsilon=\pm1$, and $H\operatorname{diag}(1,-1)H=X$ turns the character $(-1)^{v\cdot x}$ into the translation $X_v$, giving the kernel $\frac{1+i}{2}I+\frac{1-i}{2}X_v$ or its inverse.",
                  r"The displayed phase therefore becomes $aI+bX_v$ or its inverse.", frm=F),
            infer("S2.2.5.3",
                  r"By the label count the basis lengths sum to $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$, whose deficit from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$.",
                  r"The deficit is $2N-2L_{\rm c}>0$.", frm=F),
            infer("S2.2.5.4",
                  r"On $k$ columns every frame and edge operator is the $k$-th tensor power of its one-column version, so each residual vector contributes one factor acting on all $k$ columns and there are still $s_{\rm c}$ factors.",
                  r"Thus each residual vector contributes one factor acting on all $k$ columns, and there are $s_{\rm c}$ such factors over the network.", frm=F),
            infer("S2.2.5.5",
                  r"The zero label has frame $I$ and the full label has frame $C^{\otimes m}$; on the route $X_a\to Y_a$ the operator is $C^{-1}$ on the $27$ coordinates of the support of $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$ and $C$ elsewhere, which $C=iZC^{-1}Z$ corrects by applying $Z_{a,k}$ before and $i^{27k}Z_{a,k}$ after, and negating the physical $X$ outputs and undoing the exchange leaves $C^{\otimes mk}$ on every role.",
                  r"There are $27k$ inverse factors, so the identity $C=iZC^{-1}Z$ turns each of them into $C$.", frm=F),
        ],
        frm=F,
        adds=[bind("C", "two-point kernel",
                   r"The $2\times2$ matrix $C=H\operatorname{diag}(1,i)H=\frac{1+i}{2}I+\frac{1-i}{2}X$, with $H$ the normalized Hadamard matrix and $X$ the coordinate swap.")],
    )


def s22():
    F = ["linear-network", "common-frame-principle", "linear-algebra-basics",
         "finite-field-f2-arithmetic", "vectors-matrices-and-invertibility"]
    return show(
        "S2.2",
        r"Two fixed finite linear networks, a bit network over $\mathbb F_2$ and a complex network over $\mathbb Z[i,1/2]$, each exchange two banks of $N$ values with prescribed signs while restoring every scratch value, and carry nested subspace labels whose edge changes cost $s_{\rm b}<W_{\rm b}m$ and $s_{\rm c}<W_{\rm c}m$ smaller calls, so that $s/W<m^\tau$ with $\tau=\sigma=1-2^{-50}$.",
        r"Build the scalar exchange from three stages of eight-row invocations on three-element subsets of $[100]$, let frames on arrays commute with pointwise gates, attach tensor-product labels spanned by triple indicator vectors and count each edge's orthogonal residual, then realize the labels as rational projections (bit variant) or Hamming-weight phase frames (complex variant).",
        r"If labels only grow except on a few edges, the residual dimensions, which count the smaller calls, sum to $Wm$ minus a positive multiple of $N$, so the number of smaller calls falls strictly below $Wm$.",
        "explicit",
        [
            s221(),
            infer("S2.2.2",
                  r"If each scalar becomes an array on a common address set $\Omega$, each vertex $v$ gets an invertible frame $D_v$ shared by all incidences of a gate, and each edge $u\to v$ applies $D_vD_u^{-1}$, then linearity gives $\sum_jc_jD_v\varphi_j=D_v(\sum_jc_j\varphi_j)$, so the network implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$ and a signed route $w\to\rho(w)$ applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ on every role, auxiliary roles included.",
                  r"Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks.",
                  frm=["linear-network", "linear-algebra-basics",
                       "vectors-matrices-and-invertibility"],
                  page="common-frame-principle",
                  salient=r"Only the two endpoint frames of a route matter: all intermediate frames cancel, so they can be chosen freely to make every edge cheap."),
            s223(),
            s224(),
            s225(),
            infer("S2.2.6",
                  r"The relative deficits $\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$ both exceed $20\cdot2^{-50}$, and since $\log m<20$, $m^{1-2^{-50}}>m(1-20\cdot2^{-50})>m(1-\eta)$, so $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $\tau=\sigma=1-2^{-50}$.",
                  r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$.",
                  frm=["logarithms-and-iterated-logarithm-notation", "big-o"]),
        ],
        mot_quote=r"The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.",
        frm=F,
        page="subset-intersection-labels",
        adds=[
            bind("h", "ground-set size",
                 r"The size $h=100$ of the ground set $[h]$ whose three-element subsets index the data.", "count"),
            bind("v", "number of triples",
                 r"The number $v=\binom{100}{3}=161700$ of three-element subsets of $[h]$.", "count"),
            bind("N", "bank size",
                 r"The number $N=v^3=4227952113000000$ of values in each of the two data banks $X_a$, $Y_a$, indexed by triples of triples $a$.", "count"),
            bind("L", "dimension loss",
                 r"The total label dimension lost on decreasing edges, $L=Ich$ with $c$ central wires per invocation.", "count"),
        ],
        salient=r"The relative deficit is minute ($\eta_{\rm b}=339/22587335000000$), yet any strict inequality $s<Wm$, however thin, yields a power saving.",
    )
