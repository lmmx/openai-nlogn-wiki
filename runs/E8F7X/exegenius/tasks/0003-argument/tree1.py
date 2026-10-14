from lib import *


def stream_ops():
    return infer(
        r"Moving or swapping radix-$q$ digits, applying a fixed pointwise map to split streams, and cyclically splitting rows into $W$ streams each take $O(V)$ steps on a fixed number of tapes.",
        494, r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
        page="stream-operations",
        frm=["fixed-tape-model", "tapes-scanning-and-sorting-as-basic-machine-procedures",
             "binary-representation-and-bitwise-operations"])


def controlled_shifts():
    return show(
        r"Updating a target field $y\mapsto y+a(\text{controls}) \pmod{q^b}$ whose controls precede it, or multiplying it by a fixed rational unit, costs $O(V)$.",
        "Realise the update as a cyclic shift: split each fibre of $Q=q^b$ blocks at $Q-a$ and merge the two pieces in the opposite order; build unit multiplications from a split into increasing pieces.",
        mot("The sources say the operations are linear because the target field comes after its controls, so one pass with the offset known suffices.",
            "explicit", (552, r"The next operations are linear because their target field follows their", r"control fields.")),
        [
            infer(r"A cyclic shift of a fibre by the offset $a$ is a split of its $Q$ blocks at $Q-a$ onto two tapes followed by a merge that reads the second piece first.",
                  577, r"For an offset $a\in[Q]$, split these blocks at $Q-a$.",
                  r"In the merge read the second piece and then the first piece for each prefix."),
            infer(r"The $b^{O(1)}$ work of preparing an offset is absorbed by the $QB\ge Q$ bits of a fibre, because $b^C=O(q^b)=O(Q)$.",
                  585, r"for each fixed $C$, this work is absorbed by the $QB\ge Q$ bits of the", r"fiber."),
            infer(r"Multiplying $y$ by a fixed unit $c$ modulo $Q$ splits into $c$ increasing pieces, and the output coordinate selects its piece uniquely because $\gcd(Q,c)=1$.",
                  592, r"For positive fixed integer $c$ prime to $q$, the permutation",
                  r"$y\mapsto cy\pmod Q$ has $c$ increasing pieces, classified by"),
            infer(r"Negation fixes the block at zero and reverses the other $Q-1$ blocks, which two stack passes achieve while restoring each block's inner order.",
                  606, r"Negation leaves the block at zero fixed and reverses the order of the other $Q-1$ blocks."),
        ],
        page="controlled-shifts",
        frm=["stream-operations", "modular-arithmetic", "primes-coprimality-and-gcd", "fixed-tape-model"])


def xor_network():
    return show(
        r"A fixed network of pointwise linear gates on $W$ wires maps the data banks $(X_a,Y_a)$ to $(-Y_a,X_a)$ in three stages and returns every scratch wire to its arbitrary initial value.",
        "Order the gates so that the first rows subtract the effect of the old scratch values, the middle rows add the source's effect, and the last rows restore the scratch values; then compose three stages.",
        mot("The sources describe the schedule by its three jobs: remove the old scratch effect, introduce the source values and add their effect to the target, restore the scratch values.",
            "explicit", (706, r"The first two rows of", r"the last two restore the scratch values.")),
        [
            infer(r"A forward invocation changes the target by $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of the arbitrary initial scratch vectors $a,c$.",
                  744, r"If the initial side and central vectors are $a,c$,", r"independently of $a,c$."),
            infer(r"In the bit case the central coefficient $|S\cap T|\bmod 2$ plus the side contribution gives exactly $y_S\gets y_S+x_S$, the distinct triples of intersection zero or two already having coefficient zero.",
                  752, r"In the bit case, the central coefficient from $x_T$ to $y_S$ is", r"the self coefficient is one."),
            infer(r"In the complex case the central coefficient is $(|S\cap T|-1)/2$, the side wires cancel it for intersections zero and two, and intersection one contributes zero, so again $y_S\gets y_S+x_S$.",
                  756, r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$.", r"Thus both net maps are $y\gets y+x$."),
            infer(r"Three stages (forward from $X$ to $Y$, inverse forward from $Y$ to $X$, forward from $X$ to $Y$) send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
                  761, r"The inverse schedule with logical source $Y$ and target $X$ effects", r"then $(-y,x)$."),
        ],
        page="xor-linear-network",
        frm=["matrices-and-linear-maps", "permutations", "modular-arithmetic"],
        salient="The scratch wires may start with arbitrary contents and are returned to exactly those contents, so the network needs no clean workspace.")


def frames():
    return show(
        r"Choosing an invertible frame $D_v$ at every source, gate and sink, and applying $D_vD_u^{-1}$ on each edge, makes the network implement $D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}$, so only the endpoint frames matter.",
        "Maintain the invariant that the stored array is the frame applied to the logical array, and check that a common frame commutes with a pointwise linear gate.",
        mot("Once the routing is fixed the endpoint frames determine the operator on each route, so the intermediate frames are free to be chosen cheaply.",
            "explicit", (823, r"Once the scalar routing is fixed, the endpoint frames determine the array operator on each route;",
                         r"the intermediate frames can then be chosen to make each edge change inexpensive.")),
        [
            infer(r"At every vertex $v$ the stored array equals $D_v$ applied to the logical array; at the sources this holds by definition.",
                  806, r"At a vertex $v$, the invariant is that the stored array equals $D_v$ applied",
                  r"It holds at the sources by definition."),
            infer(r"At a gate, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$, so the common frame commutes with the pointwise gate and the invariant continues to the sinks.",
                  810, r"$R$-linearity gives", r"the invariant continues to the sinks."),
            infer(r"A signed role permutation sending input role $w$ to output role $\rho(w)$ with sign $\varepsilon_w$ therefore applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ on that route, auxiliary roles included.",
                  818, r"In particular, if the scalar network is a signed role permutation that",
                  r"to its input array."),
        ],
        page="frames",
        frm=["matrices-and-linear-maps", "permutations", "xor-linear-network"],
        adds=[bind(r"D_v", "frame", "the invertible linear operator on the array space chosen at a source, gate or sink $v$, in which that vertex stores its array", "direct")],
        salient="The intermediate frames cancel: the operator on each route depends only on its endpoint frames, which is why any cheap intermediate frames may be chosen.")


def subset_labels():
    return show(
        r"Every wire segment can be labelled by a nondegenerate subspace of the $m$-dimensional space $\mathcal F=F^{\otimes 3}$, built from indicator lines of three-element subsets of $[100]$, so that adjacent labels are nested and each edge change is an orthogonal residual.",
        "Use the Frankl-Wilson style form $\\langle t_S,t_T\\rangle=|S\\cap T|-1$ on indicator vectors, tensor three copies, and let stage transitions expose one tensor factor at a time.",
        mot("Orthogonality of neighbouring triples' indicator vectors is what allows the subspace assignments.",
            "explicit", (164, r"three-element subsets: gather and scatter create coefficients depending", r"the subspace assignments.")),
        [
            infer(r"The indicator vectors $t_T$ of triples satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$ under the form $x^{\mathsf T}(I-J/9)y$.",
                  862, r"\langle t_S,t_T\rangle=|S\cap T|-1,", r"\langle t_T,t_T\rangle=2."),
            infer(r"Every triple line is nondegenerate and neighbouring triple lines are orthogonal, in the label field of either construction.",
                  869, r"Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal,",
                  r"to either construction."),
            infer(r"The ambient label space $\mathcal F=F^{\otimes3}$ with its tensor form is nondegenerate of dimension $m$.",
                  876, r"The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor", r"is nondegenerate."),
            infer(r"The stage transitions chain: the outgoing labels of one stage are exactly the incoming labels of the next, starting at $U_a$ on $X_a$ and zero on $Y_a$ and ending at $\mathcal F$ and $U_a^\perp$.",
                  933, r"Thus the prescribed outgoing labels are", r"as prescribed at the terminals."),
            infer(r"On a side wire joining neighbouring triples the label passes from $P\otimes\langle t_X\rangle$ to $P\otimes t_Y^\perp$, which is possible because $t_X\perp t_Y$.",
                  953, r"The first inclusion is possible because $t_X\perp t_Y$."),
            infer(r"The order of gates confines every decrease of label dimension to the single return of a central wire from $A\otimes F$ to $B\otimes F$, losing exactly $P\otimes F$.",
                  956, r"returns once from the former label to the latter, losing exactly",
                  r"while the other edges realize the prescribed stage transitions."),
        ],
        page="subset-labels",
        frm=["linear-algebra-prelims", "xor-linear-network", "sets-functions-cartesian-products-and-bijections"],
        salient="Neighbouring triples have orthogonal indicator lines, which is exactly the nesting condition needed on the side wires, while the construction uses only the fixed ground set of size 100.")


def rank_deficit():
    return show(
        r"The absolute label-dimension changes over all edges sum to $Wm-2N+2L$ with total loss $L<N/2$, so they stay below $Wm-N$; this is the deficit that the edge-rank sum $s$ inherits.",
        "Count dimension changes edge by edge: signed changes telescope at the gates to $Wm-2N$, only one edge per central wire decreases, and each decrease loses exactly $h$.",
        mot("The saving comes from keeping the total dimension lost on decreasing edges small relative to $N$.",
            "explicit", (852, r"The saving will come from keeping the total dimension lost on decreasing", r"edges small relative to $N$.")),
        [
            infer(r"Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
                  998, r"Every edge joins comparable nondegenerate labels.  The only decreasing", r"loss is $h$."),
            infer(r"Label dimension is nondecreasing along every edge except central wires' $3\to4$, which removes $P\otimes F\otimes Q$.",
                  1061, r"Label dimension is nondecreasing along every edge except center $3\to4$, which removes",
                  r"$P\otimes F\otimes Q$."),
            infer(r"The signed dimension changes telescope at every gate, because each touched wire has one incoming and one outgoing incidence with the same label, so they sum to $Wm-2N$ (sources total $N$, sinks $Wm-N$).",
                  1066, r"The signed sum of dimension changes telescopes at every gate:", r"The signed increase is therefore $Wm-2N$."),
            infer(r"There are $Ic$ decreasing edges, each of loss $h$, so $L=Ich$ and replacing signed by absolute changes adds $2L$, giving $Wm-2N+2L$.",
                  1070, r"There are $Ic$ decreasing edges, each of loss $h$;", r"adds $2L$."),
            infer(r"The loss ratios are $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
                  1107, r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad", r"In particular, both are smaller than $1/2$."),
        ],
        page="rank-deficit",
        frm=["subset-labels", "frames", "xor-linear-network", "linear-algebra-prelims"],
        salient="Only one edge per central wire ever loses dimension, and the total loss is $L=100N/539<N/2$, so a strict but tiny saving survives.")


def bit_shear():
    return show(
        r"With matrices $M_v$ at the vertices (the projection $P_U$ at a vertex labelled $U$ and $-P_{U_a}$ at the source of $X_a$) and the permutation frames $\Phi_{M}$, the bit network implements the shear $H\leftarrow H+D$ on every role, with total edge rank $s_{\rm b}<W_{\rm b}m$.",
        "Use the address permutations $\\Phi_M$ as frames, so edge changes are shears by the rational matrix differences, and check the endpoint matrices differ by the identity.",
        mot("The frame $\\Phi_M$ is an invertible permutation of array entries with $\\Phi_{M'}\\Phi_M=\\Phi_{M'+M}$, so the frame identity applies with matrix differences as edge operators.",
            "recoverable"),
        [
            infer(r"The frame $\Phi_M$ moves the array entry at $(H,D)$ to $(H+MD,D)$, is an invertible $\mathbb F_2$-linear permutation of entries, and satisfies $\Phi_{M'}\Phi_M=\Phi_{M'+M}$.",
                  1125, r"For a matrix $M$, the frame $\Phi_M$ moves the array entry", r"$\Phi_{M'}\Phi_M=\Phi_{M'+M}$."),
            infer(r"For nested nondegenerate $U\subset V$ the difference $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its complement, so its rank is $\dim V-\dim U$, unchanged by reversing the edge.",
                  1158, r"For $U\subset V$ nondegenerate,", r"without changing its rank."),
            infer(r"The only exceptions are the $N$ negative source projections: the first edge matrix at a source $X_a$ is $2P_{U_a}$, of rational rank one where the dimension change was zero.",
                  1162, r"The only exceptions are the $N$ negative source projections.",
                  r"where the corresponding dimension change was zero."),
            infer(r"Hence $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, with deficit $N-2L_{\rm b}>0$ from $W_{\rm b}m$.",
                  1166, r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
            infer(r"At an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix, so each role receives the shear.",
                  1169, r"For an input $X_a$ the endpoint difference is", r"This proves the interface."),
            show(
                r"The deficit is large enough that $s_{\rm b}/W_{\rm b}<m^\tau$ for the fixed rational exponent $\tau=1-2^{-50}$.",
                "Compare $m^{1-2^{-50}}$ with $m(1-\\eta)$ through $\\log m<20$.",
                mot("A fixed rational exponent keeps the comparison to integer arithmetic and one exponential inequality.", "recoverable"),
                [
                    infer(r"The relative rank deficits are $\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$.",
                          1321, r"\eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m}", r"\frac{73}{19906842167500}."),
                    infer(r"Both exact deficits are greater than $20\cdot2^{-50}$.",
                          1331, r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$."),
                    infer(r"Since $m<2^{20}$ we have $\log m<20$, so $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)$.",
                          1332, r"Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence", r"$\eta=\eta_{\rm c}$."),
                    infer(r"Consequently $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $0<\tau=\sigma<1$.",
                          1339, r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,", r"\qquad 0<\tau=\sigma<1."),
                ],
                frm=["rational-numbers-and-rounding", "logarithms-exponentials-floor-and-ceiling"]),
        ],
        page="bit-shear-interface",
        frm=["frames", "rank-deficit", "power-saving-recurrence", "subset-labels", "linear-algebra-prelims", "modular-arithmetic"],
        salient="The same shear $H\\leftarrow H+D$ appears on every role, auxiliary roles included, because every endpoint difference is the identity matrix.")


def lower_tri():
    return show(
        r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
        "Run Gaussian elimination with the pivot chosen as the rightmost entry of the topmost nonzero row, so that every elementary operation is lower triangular.",
        mot("Lower triangular changes of coordinates can be performed entirely in the tape direction in which a later field is updated from earlier fields.",
            "explicit", (1358, r"Lower triangular changes of coordinates", r"can be performed entirely in this direction.")),
        [
            infer(r"If $A=0$ take $E_1=E_2=I$ and $\Pi=0$.",
                  1376, r"If $A=0$, take $E_1=E_2=I$ and $\Pi=0$."),
            infer(r"Otherwise take the topmost nonzero row and its rightmost nonzero entry, clear its row by right multiplication and its column below by left multiplication, both by lower triangular elementary matrices, and scale the pivot to one.",
                  1376, r"Otherwise choose the topmost", r"and scale the pivot to one."),
            infer(r"Deleting the pivot row and column and repeating isolates a rank-one block each time, so the final partial permutation has exactly $a$ ones, with $E_1=L^{-1}$, $E_2=R^{-1}$ for $LAR=\Pi$.",
                  1384, r"Delete the pivot row and column from the active index sets,", r"have the required form."),
        ],
        page="lower-triangular-factorization",
        frm=["matrices-and-linear-maps", "linear-algebra-prelims"])


def matrix_shear():
    return show(
        r"For a rational matrix $A$ of rank $a$, the shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ needs exactly $a$ interchanges of $b$-digit fields and $O(V)$ other work.",
        "Factor $A=E_1\\Pi E_2$, conjugate the shear by the triangular factors (controlled shifts), and implement each one of $\\Pi$ as three updates containing a single interchange.",
        mot("An edge matrix of rank $a$ will require $a$ smaller interchanges.", "explicit",
            (1351, r"An edge matrix of rank $a$ will require $a$ smaller interchanges.")),
        [
            infer(r"A fixed odd prime $q$ is chosen avoiding every denominator in the finite table of factors and every numerator of a diagonal entry, so the rational identities specialise to $\mathbb Z/q^b\mathbb Z$.",
                  1417, r"Choose an odd prime avoiding every denominator", r"of an invertible factor."),
            infer(r"A lower triangular transformation of $H$ or $D$ costs $O(V)$, updating coordinates in descending physical order so earlier coordinates still hold their original values.",
                  1425, r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:", r"still have their original"),
            infer(r"For $A=E_1\Pi E_2$: transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
                  1432, r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,", r"$D$ by $E_2^{-1}$."),
            infer(r"Each one of $\Pi$ at $(i,j)$ gives $H_i\leftarrow H_i+D_j$ by $D_j\leftarrow D_j+H_i$, then interchange $(H_i,D_j)$, then $D_j\leftarrow H_i-D_j$, taking $(h,d)$ to $(h+d,d)$ with one interchange.",
                  1434, r"Each one in position $(i,j)$ of $\Pi$ calls for", r"It uses just one interchange."),
            infer(r"There are $a$ ones, so the number of recursive calls is the rational rank $a$; temporary tapes for the other operations do not multiply that count.",
                  1443, r"There are $a$ ones, which proves the claim.", r"do not multiply"),
        ],
        page="matrix-shear-cost",
        frm=["lower-triangular-factorization", "controlled-shifts", "bit-shear-interface", "stream-operations", "modular-arithmetic"],
        adds=[bind(r"a", "rank", "the number of ones in the partial permutation $\\Pi$, which equals the rational rank of $A$", "count")],
        salient="The cost depends only on the rank $a$ of the shear matrix, not on its size: exactly $a$ interchanges, one per pivot.")
