from lib import *
from tree1 import *
from tree2 import *


def butterfly_layer():
    contract = show(
        r"Applying $C^{\otimes e}$ to $e=mf$ selected axes takes exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, plus a fixed number of binary row additions.",
        "Write each edge's phase-frame difference in coordinates by an invertible binary matrix $M$ whose first columns are the residual basis, so the kernels become coordinate kernels acting on slots; reduce $M$ to row additions.",
        mot("The directional kernels must be put into coordinate positions without performing a general transpose, so the basis change is done through row additions of whole slots.",
            "explicit", (1845, r"The number of directional kernels is precisely", r"into coordinate positions without performing a general transpose.")),
        [
            infer(r"An edge from label $U_-$ to $U_+$ with orthonormal residual basis $v_1,\dots,v_{\rho_{\rm edge}}$ has frame change $\prod_j(aI+bX_{v_j})^{\epsilon_j}$ with $\epsilon_j=\pm1$.",
                  1835, r"Proposition~\ref{prop:complex-motif-interface} gives the frame change", r"\epsilon_j\in\{1,-1\}."),
            infer(r"Extending the residual basis to a basis of $\mathbb F_2^m$ as the first columns of $M$ conjugates the edge operator into $\prod_jC_{e_j}^{\epsilon_j}$ by the permutation $\mathcal P_M$, which needs only invertibility of $M$.",
                  1855, r"Extend $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ and take these vectors as",
                  r"The displayed edge identity then becomes"),
            infer(r"On a group of $e=mf$ chunks, apply $\mathcal P_M^{-1}$ to each column, then $(C^{\epsilon_h})^{\otimes f}$ to the $f$ bits of slot $h$ for each $h\le\rho_{\rm edge}$ (one child per slot), then $\mathcal P_M$.",
                  1878, r"To implement \eqref{eq:phase-edge-coordinate} on the group, first apply", r"Finally apply $\mathcal P_M$ to every column."),
            infer(r"A negative kernel still needs only one forward child because $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$, whose wrappers are signs and fourth-root phases.",
                  1884, r"A negative directional kernel still requires only one", r"forward child, because"),
            infer(r"Gaussian elimination writes any $M\in\operatorname{GL}(m,\mathbb F_2)$ as at most $m(m-1)+3m$ elementary row additions, a fixed number, each a swap being three additions.",
                  1892, r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$", r"each row swap is three row additions."),
            infer(r"Summing the residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
                  1904, r"Summing its residual dimensions gives exactly", r"of one slot."),
        ],
        frm=["frames", "phase-frame-network", "linear-algebra-prelims", "permutations"])

    identity = show(
        r"The normalized layer satisfies $H_0^{\otimes D}=\left(\tfrac{1-i}{2}\right)^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $\mathcal S_D$ the diagonal phase $i^{x_1+\dots+x_D}$, so a $C$-layer gives the $H_0$-layer by exact Gaussian dyadic operations.",
        "Conjugate by the diagonal phase operator on the selected bits, using the one-bit identity $H_0=\\beta\\mathsf SC\\mathsf S$ coordinatewise.",
        mot("The recursion is built for the kernel $C$, whose phase frames are cheap, so the butterfly $H_0$ is expressed through $C$.", "reconstructed"),
        [
            infer(r"Applying the one-bit identities on all selected coordinates gives the layer identity, with the scalar a binary shift and fourth-root phase times at most one factor $\tfrac{1-i}{2}$.",
                  1931, r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
            infer(r"All phases, inverse wrappers and scalar corrections are exact Gaussian dyadic operations, so the layer is exact up to its final truncation.",
                  1937, r"All phases, inverse wrappers, and scalar corrections above", r"are exact Gaussian dyadic operations."),
        ],
        frm=["butterfly", "complex-numbers"])

    batching = show(
        r"One internal node on $e=m^k$ chunks costs $O(V((eK)^\tau+1))$ beyond its $s$ child calls, each child acting on volume $V/W$, with the rows supplied by padding and splitting the first chunks.",
        "Charge the binary basis changes by the packed procedure, supply rows from the leading chunks, split rows into $W$ role streams, and handle the case of few chunks by individual kernels.",
        mot("The network needs $W$ equal-shape role streams, which a row index supplies; the first chunks provide it.", "recoverable"),
        [
            infer(r"Individual $C$ kernels are applied by splitting at the selected bit, scanning aligned record pairs and merging, so $e$ kernels cost $O(Ve)$.",
                  2283, r"Thus \(e\) individual kernels cost", r"\(O(Ve)\) on any stream with these complete ranges and record format."),
            infer(r"At an internal node the phase construction gives exactly $s$ calls, and the binary changes of basis, scalar gates, corrections and reassembly cost $O(V((eK)^\tau+1))$.",
                  2289, r"The phase construction supplies one recursive call on a slot for each", r"at this node."),
            infer(r"If $D\le q_0$, only individual $C$ kernels are used, at cost $O(V\log d)$.",
                  2313, r"If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\)."),
            infer(r"Otherwise the first $q_0$ chunks, treated individually, serve as the row index of range $R_{\rm row}=2^{q_0K}\ge W^{k_0}$, padded with zero rows to a multiple of $W^{k_0}$ so that at depth $j$ the row count is divisible by $W^{k_0-j}$.",
                  2318, r"regard their concatenated bits as one row index.", r"divisible by \(W^{k_0-j}\)."),
            infer(r"A row index $u=Wg+w$ sends the whole row to role $w$, so each recursive edge call acts on one role stream of exactly $1/W$ of its parent's volume.",
                  2325, r"At a node, write a row index as \(u=Wg+w\)", r"of its parent's logical volume."),
            infer(r"Padded zero rows are again zero when an invocation finishes, so the added rows can be deleted afterwards.",
                  2389, r"Each padded zero row is again zero when an invocation finishes,", r"have completed."),
        ],
        frm=["stream-operations", "packed-selected-bit-addition", "arbitrary-width-interchange"])

    recurrence = show(
        r"With $F(e)$ the time divided by stream volume, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ for $e\ge d^\beta$ and $F(e)=O(e)$ below, which sums to $O(d^{\lambda'})$ over the base-$m$ pieces for any fixed $\lambda'<1$.",
        "Unroll the recurrence: the per-node overhead is $O(e^\lambda)$ because $K\\le e^{c/\\beta}$, the internal levels form a geometric sum, the leaves stop at $e<d^\\beta$, and the base-$m$ partition adds a logarithmic factor absorbed by $\\lambda'$.",
        mot("Stopping the recursion at $e<d^\\beta$ turns the large chunk-width $K=\\lfloor d^c\\rfloor$ into a mere power of $e$, so the overhead stays polynomially below linear.", "recoverable"),
        [
            infer(r"Fix $\beta=1/2$ and exponents with $0<\tau<1$, $\max\{0,\log_m(s/W)\}\le\sigma<1$, $\max\{\tau,\sigma\}<\lambda<1$ and $\tau(1+c/\beta)<\lambda$.",
                  2394, r"Fix \(\beta=1/2\), and choose real exponents satisfying", r"\tau(1+c/\beta)<\lambda."),
            infer(r"Recursion stops when $e<d^\beta$, and then $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, $F(e)=O(e)$ for $e<d^\beta$.",
                  2403, r"Stop recursion when \(e<d^\beta\)", r"F(e)=O(e)\quad(e<d^\beta)."),
            infer(r"The $s$ child calls run on streams of volume $V/W$, costing $s(V/W)F(e/m)$, so dividing by $V$ gives the factor $s/W$.",
                  2410, r"Indeed, the \(s\) child calls are executed on streams of volume \(V/W\),", r"gives the factor \(s/W\)."),
            infer(r"At an internal node $e\ge d^\beta$ gives $K\le d^c\le e^{c/\beta}$, so the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.",
                  2413, r"At an internal node \(e\ge d^\beta\), hence", r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)."),
            infer(r"With $a=s/W\le m^\sigma<m^\lambda$ the internal costs sum to at most $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$.",
                  2416, r"Put \(a=s/W\).", r"(a/m^\lambda)^j=O(e^\lambda)."),
            infer(r"The leaves after $j$ levels, each with $u=e/m^j<d^\beta$ chunks, contribute at most $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$, using $a^j\le m^{j\sigma}=(e/u)^\sigma$.",
                  2421, r"If the leaves after \(j\) levels contain", r"\(a^j\le m^{j\sigma}=(e/u)^\sigma\)."),
            infer(r"Splitting $D-q_0=\sum_ja_jm^j$ in base $m$ into at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces gives $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
                  2432, r"Write \(D-q_0=\sum_j a_jm^j\) in base \(m\)", r"\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1."),
        ],
        frm=["recursion-and-divide-and-conquer-recurrences", "summation-geometric-series-and-products", "power-saving-recurrence"],
        salient="The leaves contribute $d^{\\sigma+\\beta(1-\\sigma)}$, which is why the exponent $\\lambda'$ must exceed $\\sigma+\\beta(1-\\sigma)$ and recursion is stopped at $e=d^\\beta$.")

    guard = show(
        r"The whole layer can be evaluated exactly with $p+\Delta$ fractional bits and $\Delta+3$ integer bits per real component, where $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$.",
        "Bound the arithmetic dependency depth $A(e)$ along any chain by the recurrence $A(e)\\le sA(e/m)+E$, then convert depth into denominator and magnitude growth.",
        mot("Each addition can double the modulus and each halving adds a denominator bit, so the number of operations on a chain bounds both growths.", "recoverable"),
        [
            infer(r"Put $E=64(W+m+1)^3$, $B=s+E$, $\nu=\min\{j\ge1:m^j\ge B\}$, $C_1=\max\{20,\nu+3\}$, $C_0=128mB^2$ and $\Delta=\lceil C_0d^{C_1}\rceil$.",
                  2459, r"E=64(W+m+1)^3,\qquad B=s+E,", r"\Delta=\lceil C_0d^{C_1}\rceil."),
            infer(r"Every physical wire occurs in at most twelve scalar gates, there are at most $12W$ gates, and evaluating all outputs of a gate takes at most $2W^2$ elementary operations.",
                  2490, r"The scalar schedule \eqref{eq:motif-schedule} touches a data wire", r"at most \(2W^2\) elementary operations."),
            infer(r"The child corrections take at most $4s$ operations and the endpoint corrections $4W+4$, and since $s<Wm$ the total $24W^3+4s+4W+4$ is less than $E$.",
                  2503, r"This gives at most \(4s\) operations for the child corrections.", r"\(E=64(W+m+1)^3\)."),
            infer(r"A paired kernel evaluation uses at most eight operations, so $A(e)\le sA(e/m)+E$ at an internal node and $A(e)\le8e$ at a leaf; depth concatenates all $s$ calls and so uses $s$, not $s/W$.",
                  2511, r"We may therefore use", r"smaller stream volumes."),
            infer(r"For $x\ge1$, $sx+E\le(s+E)x=Bx$; with at most $\lceil\log_md\rceil$ levels and $B^{k+1}\le B^2d^{\log_mB}\le B^2d^\nu$ this gives $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$.",
                  2523, r"There are at most \(k\le\lceil\log_m d\rceil\) internal levels.", r"8B^2d^{\nu+1}."),
            infer(r"Concatenating the at most $md$ base-$m$ pieces adds depth $8mB^2d^{\nu+2}$, and at most $d$ individual kernels add $8d$.",
                  2536, r"For the sufficiently large sizes under consideration, the earlier", r"contributing at most \(8d\)."),
            infer(r"The totals $8mB^2d^{\nu+2}+8d+t+9\le26mB^2d^{\nu+2}<128mB^2d^{\nu+3}\le C_0d^{C_1}$, with $C_1\ge\nu+3$, bound both denominator and magnitude growth.",
                  2554, r"8mB^2d^{\nu+2}+8d+t+9", r"&<128mB^2d^{\nu+3}\le C_0d^{C_1}."),
            infer(r"A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ and has modulus at most $2^\ell$: addition at most doubles the modulus, halving adds one denominator bit, and signs and multiplication by $i$ preserve both.",
                  2563, r"A value at depth \(\ell\)", r"preserve both bounds."),
            infer(r"Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component therefore represents every intermediate coefficient exactly.",
                  2569, r"Thus reserving \(p+\Delta\) fractional bits", r"prevents overflow."),
            infer(r"Choosing $\epsilon C_1<1$ with $d=\Theta(p^\epsilon)$ gives $\Delta=o(p)$, so the full coefficient width is $O(p)$.",
                  2582, r"Choose \(\epsilon C_1<1\).", r"required in the time analysis."),
        ],
        frm=["fixed-point-disk", "recursion-and-divide-and-conquer-recurrences", "complex-numbers"])

    uniform = infer(
        r"The extra normalized terms of the packed lemma tend to zero uniformly over the allowed $d,r$, so every packed call has cost $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ with one common constant.",
        2732, r"Both bounds tend to zero uniformly over all current allowed", r"with one common time constant.")

    final_cost = infer(
        r"The row construction and the recurrence analysis give total time $O(Vd^{\lambda'})$ on fixed tapes, including padded and auxiliary streams, and the layer identity converts the exact $C$-layer to $\mathcal H$.",
        2736, r"The row construction and the recurrence analysis", r"to $\mathcal H$.")

    truncate = infer(
        r"Every row of $\mathcal H$ has absolute row sum one, so $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation keeps the disk and errs by less than $\sqrt2\,2^{-p}$.",
        2751, r"Finally, every row of $\mathcal H$ has", r"changes each by less than $2^{-p}$.")

    return show(
        r"Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ at once to the same bit position of $D\le d$ address chunks of every polynomial record, followed by one truncation, costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.",
        "Rewrite $H_0^{\\otimes D}$ through the kernel $C$ and diagonal phases, compute $C^{\\otimes D}$ recursively with the complex network (children on streams of volume $V/W$, binary basis changes by packed bit moves), keep every value an exact Gaussian dyadic, and truncate once.",
        mot("Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis.",
            "explicit", (1797, r"Its phase frames express a $C$ tensor product using smaller groups of", r"separated by binary changes of basis.")),
        [phase_frame_network(), contract, identity, packed_bits(), batching, recurrence, guard, uniform, final_cost, truncate],
        page="simultaneous-butterfly-layer",
        frm=["phase-frame-network", "packed-selected-bit-addition", "arbitrary-width-interchange", "power-saving-recurrence",
             "butterfly", "fixed-point-disk", "negacyclic-ring"],
        adds=[bind(r"D", "selected chunks", "the number of consecutive address chunks, at most $d$, on whose common selected bit the butterfly acts", "count"),
              bind(r"C", "phase kernel", "the two-point kernel $\\tfrac{1+i}{2}I+\\tfrac{1-i}{2}X$ with $C^2=X$ and $C^4=I$", "direct")],
        salient="The saving over $D$ separate butterfly passes has the same origin as the address interchange: each level multiplies the number of children by $s$ but divides the volume per child by $W$, with $s/W<m$.")
