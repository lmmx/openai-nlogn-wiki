from lib import *

def s0_1():
    return infer(
        'S0.1',
        r"""Refuting the conjecture needs only one machine $A$ with $\liminf_{n\to\infty}T_A(n)/(n\lg n)=0$, the negation of an eventual bound $T_A(n)\ge c_An\lg n$, and a power saving gives this limit through all input lengths.""",
        Q(r"Its negation requires one machine satisfying", r"which is a stronger conclusion."),
        frm=['nlogn-conjecture', 'asymptotic-notation-beyond-big-o', 'big-o'])

# ---------------------------------------------------------------- tools
def stream_ops():
    return infer(
        'S1.1',
        r"""Splitting on a radix-$q$ digit, permuting digit values, moving a digit, applying a pointwise map to aligned streams, merging, and splitting whole rows cyclically into a fixed number of equal streams each take $O(V)$ steps on a fixed number of tapes.""",
        Q(r"Fix a radix $q\ge2$.", r"in any fixed order of the row classes."),
        page='stream-ops',
        frm=['array-order', 'fixed-tape-model', 'positional-number-representation-and-carries'])

def controlled_shifts():
    return infer(
        'S1.2',
        r"""A target field that follows its control fields can be updated by $y\mapsto y+a(\text{controls})\pmod{q^b}$, or multiplied by a fixed rational unit, in $O(V)$ time whatever spectator fields lie between.""",
        Q(r"Suppose a target field $y\in[Q]$ follows its control fields", r"fixed number of control values."),
        page='controlled-shifts',
        frm=['stream-ops', 'array-order', 'modular-arithmetic', 'primes-coprimality-and-gcd'])

# ---------------------------------------------------------------- network (K.1.1)
def network():
    return show(
        'K.1.1',
        r"""An eight-row invocation of copy, gather, scatter and side-injection gates adds $x_S$ to $y_S$ for arbitrary initial scratch values, and three such stages (forward, inverse, forward) exchange the banks $X_a,Y_a$ up to one sign on the $W$ wires while restoring every scratch wire.""",
        r"""Design each invocation as subtract-the-old-scratch-effect, add-the-source-effect, restore-the-scratch, so that the scratch contribution cancels exactly; then chain a forward, an inverse and a forward stage.""",
        r"""The scratch wires start with arbitrary values that must come back unchanged, so each invocation first cancels their old effect and finally restores them, and chaining three stages with the middle one inverted turns adding $x$ to $y$ into an exchange of the banks.""",
        'recoverable',
        page='network',
        frm=['matrix-basics', 'binary-field-f2-and-xor', 'sets-subsets-and-basic-combinatorics', 'vectors-matrices-and-linear-maps', 'boolean-gates-and-circuits'],
        salient=r"""The scratch wires may start with arbitrary values and end with exactly those values, and the result for the data wires does not depend on them.""",
        children=[
            infer('K.1.1.1',
                  r"""A forward invocation changes the target by $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, the side injection, copy, scatter and gather applied to the sources $x$, independently of the arbitrary initial scratch vectors $a,c$.""",
                  Q(r"If the initial side and central vectors are $a,c$", r"independently of $a,c$.")),
            infer('K.1.1.2',
                  r"""The net map is $y\gets y+x$: the central coefficient is $|S\cap T|\bmod2$ (bit) or $(|S\cap T|-1)/2$ (complex), the side wires cancel it exactly for the neighboring triples, it is already zero for the other distinct triples, and the self coefficient is one.""",
                  Q(r"In the bit case, the central coefficient from", r"Thus both net maps are $y\gets y+x$.")),
            infer('K.1.1.3',
                  r"""A forward stage, an inverse stage and a forward stage take $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, exchanging the banks with one sign change and restoring each invocation's own scratch wires.""",
                  Q(r"The inverse schedule with logical source $Y$ and target $X$ effects", r"Each invocation restores its own auxiliary wires.")),
            infer('K.1.1.4',
                  r"""A fixed triple has $z_{\rm b}=13968$ (bit) or $z_{\rm c}=147731$ (complex) neighbors, giving the fixed wire counts $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})$ and $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})$, independent of the input length.""",
                  Q(r"A fixed triple has", r"independently of any eventual input length.")),
        ])

# ---------------------------------------------------------------- frames (K.1.2)
def frames():
    return show(
        'K.1.2',
        r"""If each scalar wire value is replaced by an array and each vertex gets an invertible frame $D_v$, with one frame for all incidences of a gate, the implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: only the endpoint frames matter and each edge merely changes the frame.""",
        r"""Carry the invariant 'stored array = frame applied to logical array' along edges and through gates, using that a pointwise linear gate commutes with a frame common to all its wires.""",
        r"""Once the scalar routing of the network is fixed, the array operator on each route is decided by its endpoint frames alone, so every intermediate frame is free and can be chosen to make each edge cheap.""",
        'explicit',
        mot_quote=Q(r"Once the scalar routing is fixed", r"make each edge change inexpensive."),
        page='frames',
        frm=['network', 'matrix-basics', 'vectors-matrices-and-linear-maps', 'functions-bijections-and-permutations'],
        salient=r"""All intermediate frames cancel: the array operator on each role depends only on its source and sink frames, auxiliary roles included.""",
        children=[
            infer('K.1.2.1',
                  r"""At every vertex the stored array equals the frame applied to the logical array, an edge changes $D_u\varphi$ to $D_v\varphi$, and a pointwise gate commutes with the common frame, so the implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$.""",
                  Q(r"At a vertex $v$, the invariant is that the stored array equals", r"\end{equation}")),
            infer('K.1.2.2',
                  r"""For a signed role permutation, the route from input role $w$ to output role $\rho(w)$ applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to its array, auxiliary roles included.""",
                  Q(r"In particular, if the scalar network is a signed role permutation", r"enter this identity.")),
        ])

# ---------------------------------------------------------------- subset labels (K.1.3)
def subset_labels():
    return show(
        'K.1.3',
        r"""Labels, nondegenerate subspaces of $\mathcal F=F^{\otimes3}$ of dimension $m=h^3$ built from indicator vectors of three-element subsets of $[h]$, can be assigned to sources, gates and sinks so that one label contains the other along every edge, which makes the cost of an edge the dimension of its orthogonal residual.""",
        r"""Choose the bilinear form so that indicator vectors of neighboring triples are orthogonal, tensor three copies, and prescribe terminal labels, stage transitions and gate labels that are nested.""",
        r"""The saving of the construction is measured by the total dimension lost on decreasing edges, so the labels are chosen to keep decreases rare and small.""",
        'explicit',
        mot_quote=Q(r"The saving will come from keeping", r"small relative to $N$."),
        page='subset-labels',
        frm=['matrix-basics', 'sets-subsets-and-basic-combinatorics', 'binary-field-f2-and-xor', 'network', 'frames'],
        children=[
            infer('K.1.3.1',
                  r"""A label is a nondegenerate subspace of a fixed bilinear space, one label contains the other along each edge, and the orthogonal residual of $U\subset V$ inside $V$ has dimension $\dim V-\dim U$, the absolute change in label dimension.""",
                  Q(r"A label is a nondegenerate subspace of a fixed bilinear space.", r"the absolute change in label dimension.")),
            infer('K.1.3.2',
                  r"""With $F=\mathbb Q^h$ and the form $x^{\mathsf T}(I-J/9)y$ (bit network) or $F=\mathbb F_2^h$ with the dot product (complex network), triple indicators pair as $\langle t_S,t_T\rangle=|S\cap T|-1$ (respectively $|S\cap T|\bmod 2$), so each triple line is nondegenerate and neighboring triple lines are orthogonal.""",
                  Q(r"For the bit network, let $F=\mathbb Q^h$", r"in the label field belonging to either construction.")),
            infer('K.1.3.3',
                  r"""The terminal labels are $U_a$ to $\mathcal F$ on $X_a$, $0$ to $U_a^\perp$ on $Y_a$ and $0$ to $\mathcal F$ on each scratch role, so the source dimensions sum to $N$ and the sink dimensions to $N m+N(m-1)+(W-2N)m=W m-N$.""",
                  Q(r"The ambient label space is $\mathcal F=F^{\otimes3}$", r"to $Wm-N$.")),
            infer('K.1.3.4',
                  r"""The outgoing labels of one stage are exactly the incoming labels of the next, since $A'=A\otimes F$, $P'=P\otimes\langle t\rangle$ and $B'=(P')^\perp_{A'}=(B\otimes F)\perp(P\otimes t^\perp)$, starting from $U_a$ and $0$ and ending at $\mathcal F$ and $U_a^\perp$.""",
                  Q(r"These transitions expose one tensor factor at each stage.", r"as prescribed at the terminals.")),
            infer('K.1.3.5',
                  r"""Central gates carry $A\otimes F$ on the $X$ bank and $B\otimes F$ on the $Y$ bank, so a central wire returns once from the former to the latter, losing exactly $P\otimes F$, and the order in which the eight gate times touch the wires confines every decrease to that return.""",
                  Q(r"For the central gates we assign", r"X\text{-center},\quad X\text{-side}.")),
        ])

# ---------------------------------------------------------------- rank saving (K.1.4)
def rank_saving():
    return show(
        'K.1.4',
        r"""The edge dimension changes of the labeled network sum to $W m-2N+2L$, where $L=I c h$ is the total dimension lost on the central $3\to4$ edges and $L<N/2$, so the total is strictly below $W m$.""",
        r"""Count by telescoping along each wire: the sources contribute $N$ and the sinks $W m-N$, so the signed changes sum to $W m-2N$; every decrease is counted twice more by taking absolute values; then bound the loss against $N$.""",
        r"""The sum of changes is fixed by the terminal labels because gate contributions cancel along each wire; only the decreasing edges add to it, so the whole saving rests on how little is lost there.""",
        'explicit',
        mot_quote=Q(r"Thus the signed dimension changes will sum to", r"We will obtain $L<N/2$."),
        page='rank-saving',
        frm=['subset-labels', 'frames', 'network', 'matrix-basics'],
        salient=r"""The total falls below the trivial count $W m$ (every wire climbing from dimension $0$ to $m$) by exactly $2N-2L$: the $2N$ data wires each climb one dimension less than $m$, while the unavoidable decreases take back only $2L$ with $L/N=100/539$ (bit) or $101/539$ (complex).""",
        children=[
            infer('K.1.4.1',
                  r"""Every edge joins comparable nondegenerate labels and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$ dimensions, so $L=I c h$ and the absolute changes sum to $W m-2N+2L$; for binary labels every nonzero residual has an orthonormal basis.""",
                  Q(r"Every edge joins comparable nondegenerate labels.", r"has an orthonormal basis.")),
            infer('K.1.4.2',
                  r"""The side edge from time 2 to time 5 uses the neighbor relation essentially, since $t_X\perp t_Y$ gives $\langle t_X\rangle\subset t_Y^\perp$ and hence nested labels, and the remaining residuals follow by splitting $A=B\perp P$ and $F=\langle t\rangle\perp t^\perp$.""",
                  Q(r"The side edge $2\to5$ uses the neighbor relation", r"$F=\langle t\rangle\mathbin{\perp}t^\perp$.")),
            infer('K.1.4.3',
                  r"""Label dimension is nondecreasing along every edge except the central edge from time 3 to time 4, which removes $P\otimes F\otimes Q$ of dimension $h$; the interstage edges are included in the table and the initial and final data labels match the terminals, so there is no other change.""",
                  Q(r"Label dimension is nondecreasing along every edge except center", r"so no other dimension changes occur.")),
            infer('K.1.4.4',
                  r"""The signed changes telescope along each wire because a touched wire has one incoming and one outgoing incidence with the same gate label, so they sum to the sink dimensions $W m-N$ minus the source dimensions $N$, that is $W m-2N$.""",
                  Q(r"The signed sum of dimension changes telescopes at every gate", r"The signed increase is therefore $Wm-2N$.")),
            infer('K.1.4.5',
                  r"""There are $I c$ decreasing edges, each of loss $h$, and replacing signed by absolute changes adds twice the loss, so the absolute changes sum to $W m-2N+2L$.""",
                  Q(r"There are $Ic$ decreasing edges, each of loss $h$", r"adds $2L$.")),
            infer('K.1.4.6',
                  r"""Since $L=3v^2c h$ and $N=v^3$ with $v=\binom h3=161700$, the loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both below $1/2$, so $W m-2N+2L<W m$.""",
                  Q(r"The loss ratios have the exact values", r"both are smaller than $1/2$.")),
        ])

# ---------------------------------------------------------------- bit interface (K.1.5)
def bit_interface():
    return show(
        'K.1.5',
        r"""Taking the projection $P_U$ as the matrix at a gate or sink of label $U$ and $-P_{U_a}$ at the source of $X_a$, the endpoint difference is $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role $w$, and the edge ranks sum to $s=W m-N+2L<W m$.""",
        r"""Read each label as a rational projection matrix; an edge's matrix difference has rank equal to its dimension change except on the $N$ source edges of the $X_a$ wires, where the negative source projection adds one rank each.""",
        r"""With frames $\Phi_{M_v}$ the endpoint matrix difference on a route is exactly the shear applied to that role, so matrices whose endpoint difference is the identity make it the same shear $H\leftarrow H+D$ on every role.""",
        'explicit',
        mot_quote=Q(r"Using $D_v=\Phi_{M_v}$", r"on every role;"),
        frm=['subset-labels', 'rank-saving', 'frames', 'matrix-basics', 'modular-arithmetic'],
        children=[
            infer('K.1.5.1',
                  r"""A nondegenerate rational label $U$ is assigned the projection $P_U$ onto $U$ along $U^\perp$ at each gate or sink, the source of $X_a$ the matrix $-P_{U_a}$, and every other source zero.""",
                  Q(r"For a nondegenerate rational subspace $U\subset\mathcal F$, write", r"zero to every other source.")),
            infer('K.1.5.2',
                  r"""The frame of a vertex with matrix $M$ is the shear $\Phi_M:(H,D)\mapsto(H+MD,D)$ on two chunks of $m$ fields, an invertible permutation with $\Phi_{M'}\Phi_M=\Phi_{M'+M}$, so an edge changes the frame by $\Phi$ of the matrix difference.""",
                  Q(r"In the tape application, two address chunks are written as vectors", r"$\Phi_{M'}\Phi_M=\Phi_{M'+M}$.")),
            infer('K.1.5.3',
                  r"""The bit network has $W_{\rm b}$ wires and only XOR gates, obeys $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ and has edge-rank sum $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}=177176569088785861287000000<W_{\rm b}m$.""",
                  Q(r"The bit network has $W_{\rm b}$ wires", r"<W_{\rm b}m.")),
            infer('K.1.5.4',
                  r"""For nested nondegenerate $U\subset V$ the matrix $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and reversing the edge negates the matrix without changing its rank.""",
                  Q(r"Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including", r"without changing its rank.")),
            infer('K.1.5.5',
                  r"""The only exceptions are the $N$ negative source projections: at stage 1 the first gate on $X_a$ has label exactly $U_a$, so the first edge matrix is $2P_{U_a}$ of rank one although the dimension change is zero, and the rank sum exceeds the dimension count by $N$, leaving the deficit $N-2L_{\rm b}>0$.""",
                  Q(r"The only exceptions are the $N$ negative source projections.", r"is $N-2L_{\rm b}>0$.")),
            infer('K.1.5.6',
                  r"""For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix, which proves the interface.""",
                  Q(r"For an input $X_a$ the endpoint difference is", r"This proves the interface.")),
        ])

def bit_network():
    return show(
        'K.1',
        r"""A fixed bit network on $W$ wires with only XOR gates exchanges two banks while restoring its scratch wires and, with rational matrix labels, has the endpoint operator $(H,D)\mapsto(H+D,D)$ on every role, while the ranks of its edge differences sum to $s<W m$.""",
        r"""Build the scalar exchange network, lift it to arrays through frames, attach nested subspace labels, count the dimension changes along all edges, and read the labels as address-shear frames.""",
        r"""The scalar network already has the required signed exchange; what remains is to choose intermediate labels so that every change of frame is cheap, and that choice is where the saving is made.""",
        'explicit',
        mot_quote=Q(r"The scalar network already has the required signed exchange.", r"make the changes of frame inexpensive."),
        page='bit-network',
        frm=['network', 'frames', 'subset-labels', 'rank-saving', 'matrix-basics', 'binary-field-f2-and-xor', 'vectors-matrices-and-linear-maps'],
        adds=adds_(
            (r'N', 'bank size', r'The number of $X$ wires, equal to the number of $Y$ wires: $N=v^3$ with $v=\binom h3=161700$.', 'count'),
            (r'L', 'total dimension loss', r'The total dimension lost on the decreasing edges, $L=I c h$.', 'count'),
            (r'h', 'ground-set size', r'The size of the ground set $[h]$, $h=100$, whose three-element subsets index the banks.', 'count'),
            (r'I', 'invocation count', r'The number of separate three-stage invocations of the scalar schedule, $I=3v^2$.', 'count'),
            (r'c', 'central wire count', r'The number of central wires in one invocation.', 'count'),
        ),
        salient=r"""The endpoint operator is the same shear $H\leftarrow H+D$ on every one of the $W$ roles, including the scratch roles that start with arbitrary values.""",
        children=[network(), frames(), subset_labels(), rank_saving(), bit_interface()])
