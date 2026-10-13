import json, sys

SRC = open('/home/user/openai-nlogn-wiki/runs/P1/sources/paper.tex').read()
OUT = '/home/user/openai-nlogn-wiki/runs/P1/exegenius/tasks/0003-argument.answer.json'


def ev(q):
    return {"source": "paper", "quote": q}


def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": ev(quote) if quote else None}


def infer(id, claim, quote, page=None, frm=(), salient=None, deferred=False):
    d = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if page:
        d["page"] = page
    if salient:
        d["salient"] = salient
    if deferred:
        d["deferred"] = True
    return d


def show(id, claim, method, motivation, children, page=None, frm=(), salient=None, adds=()):
    d = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": list(frm)}
    if page:
        d["page"] = page
    if salient:
        d["salient"] = salient
    if adds:
        d["adds"] = [{"symbol": s, "name": n, "meaning": m, "relation": r} for (s, n, m, r) in adds]
    return d


# ---------------------------------------------------------------- S1
S1 = show(
    "S1",
    "Linear-time scans on arrays stored in lexicographic order on a fixed number of tapes (permuting or moving digits, splitting and merging streams, controlled cyclic shifts of a later field) supply the elementary operations of both tape procedures.",
    "Fix the array and address conventions, then prove the few linear-time scans (digit moves, stream splits and merges, controlled shifts) that every later procedure is built from.",
    mot("Both tape procedures are compositions of such scans, and their costs only add up if each scan is shown to take time linear in the volume, counters and head returns included.", "recoverable"),
    [
        infer("S1.1",
              "An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order with the address implicit in position; its logical volume $V$ is the number of stored data bits, and a row is the complete suffix block at a fixed prefix and row index.",
              "An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in",
              page="tape-address-arrays",
              frm=["turing-machine-tapes", "binary-representation-and-schoolbook-arithmetic", "sets-functions-bijections-and-permutations"]),
        infer("S1.2",
              "Fixed digit permutations, moving one digit, splitting on a digit and merging, and splitting whole rows cyclically into $W$ streams each take $O(V)$ steps on a fixed number of tapes.",
              "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
              page="elementary-stream-operations",
              frm=["tape-address-arrays", "turing-machine-tapes", "big-o"]),
        infer("S1.3",
              "Updating a target field by an offset $a$ computed from earlier fields, $y\\mapsto y+a \\pmod{q^b}$, or multiplying it by a rational unit, takes $O(V)$ time.",
              "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
              page="controlled-shifts",
              frm=["modular-arithmetic", "elementary-stream-operations", "tape-address-arrays"]),
    ],
)

# ---------------------------------------------------------------- S2
S2 = show(
    "S2",
    "Two fixed linear networks, one over bits and one over Gaussian dyadic values, exchange two banks of values with prescribed signs and restore every scratch wire, and carry subspace labels whose total dimension change $s$ is strictly less than $Wm$.",
    "Build a scalar network from a three-subset gadget, lift it to arrays through common frames at each gate, and choose nested subspace labels so that the frame changes on the edges have small total rank.",
    mot("The saving must come from the edges: the network is fixed and exchanges banks exactly, so the only freedom is the representation on each wire, and the cost of changing representation is measured by the dimension lost.", "explicit",
        "The saving will come from keeping the total dimension lost on decreasing"),
    [
        show(
            "S2.1",
            "Three stages of an invocation that adds a source bank $x$ into a target bank $y$ send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ and restore every scratch wire, for arbitrary scratch contents.",
            "Compose three invocations of the elementary update $y\\gets y+x$ (stage 1 from $X$ to $Y$, stage 2 its inverse from $Y$ to $X$, stage 3 from $X$ to $Y$), each with its own scratch wires.",
            mot("One update followed by its inverse in the other direction and a second update turns $(x,y)$ into $(-y,x)$, an exchange with a sign; since scratch values come from real data and cannot be assumed zero, each update must be independent of them.", "recoverable"),
            [
                infer("S2.1.1",
                      "A fixed gadget on three-element subsets of $[100]$ with copy, gather, scatter and side-injection gates, scheduled in 8 rows, changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, whatever the scratch values.",
                      "For arbitrary initial values of its auxiliary wires, a forward",
                      page="triple-subset-gadget",
                      frm=["linear-network-roles", "frames", "xor-and-arithmetic-over-f-2"]),
                infer("S2.1.2",
                      "Performing the update at stage 1 from $X$ to $Y$, the inverse update from $Y$ to $X$ at stage 2 and the update again at stage 3 gives $(x,y)\\to(x,y+x)\\to(-y,y+x)\\to(-y,x)$ and restores every auxiliary wire.",
                      "Performing a forward invocation from $X$ to $Y$ at stage 1,"),
            ],
            page="linear-network-roles",
            frm=["entrywise-operations-on-arrays-and-vectors", "sets-functions-bijections-and-permutations", "xor-and-arithmetic-over-f-2"],
        ),
        infer("S2.2",
              "Giving all wires at a gate the same invertible operator $D_v$ on their address-indexed arrays, and applying $D_vD_u^{-1}$ on each edge, makes the net operator on each routed role equal to $D_{\\rm sink}D_{\\rm source}^{-1}$, because a common frame commutes with pointwise linear gates.",
              "Thus the common frame commutes with the pointwise gate, and",
              page="frames",
              frm=["linear-network-roles", "entrywise-operations-on-arrays-and-vectors", "tape-address-arrays"]),
        infer("S2.3",
              "Nested nondegenerate subspaces of an $m$-dimensional space, built from tensor products of three-element subset lines, label the gates and terminals so that every edge joins comparable labels and the total dimension change $s$ over all edges is strictly less than $Wm$, where $W$ is the wire count.",
              "Every edge joins comparable nondegenerate labels.",
              page="subspace-labels-rank-deficit",
              frm=["linear-algebra-basics", "triple-subset-gadget", "linear-network-roles", "frames"],
              salient="The total dimension change $s$ is strictly below $Wm$: only about $100/539$ of the source rank $N$ is lost on decreasing edges (a deficit $N-2L>0$), although every wire's label could in principle change by rank $m$ on every edge."),
        infer("S2.4",
              "The bit network sends its input to the role permutation and its endpoint matrices differ by $I_m$ on every input role, so its net effect on every role array is the address shear $(H,D)\\mapsto(H+D,D)$, with edge matrix ranks summing to $s_{\\rm b}<W_{\\rm b}m$.",
              "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",
              page="address-shear",
              frm=["frames", "subspace-labels-rank-deficit", "linear-network-roles", "modular-arithmetic", "tape-address-arrays"],
              salient="The same shear $H\\gets H+D$ is applied on every role, scratch roles included, although the frames differ from vertex to vertex; they cancel along each route and leave only the endpoint difference $I_m$."),
        infer("S2.5",
              "In the complex network each edge's frame change is a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of the edge residual, with $s_{\\rm c}<W_{\\rm c}m$ kernels in total, and telescoping gives $C^{\\otimes m}$ on every role.",
              "For each edge of the complex network, write $U,V$ for its tail and",
              page="binary-phase-interface",
              frm=["frames", "linear-network-roles", "triple-subset-gadget", "subspace-labels-rank-deficit", "butterfly-and-phase-kernels", "linear-algebra-basics", "xor-and-arithmetic-over-f-2"],
              salient="After the source and sink sign corrections the net operator is the same $C^{\\otimes m}$ on every role, including the exchanged pair and the scratch roles."),
    ],
)

# ---------------------------------------------------------------- S3
S3 = show(
    "S3",
    "Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\\tau)$ time, for a fixed rational $\\tau<1$, with an exact permutation as final effect for arbitrary scratch contents.",
    "Run the bit network on role streams so that its endpoint operator is the shear $H\\gets H+D$, implement each edge shear by rank-many smaller interchanges, compose three shears into an interchange, solve the resulting recurrence, and then lift the width and row restrictions.",
    mot("An edge matrix of rank $a$ needs only $a$ smaller interchanges, and the ranks sum to less than $Wm$, so the recursion on the network saves a power of the chunk width.", "explicit",
        "Because the sum of these ranks is less than the number of wires times"),
    [
        show(
            "S3.1",
            "Every rational matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ lower triangular and $\\Pi$ a partial permutation with $a$ ones, so the shear $(H,D)\\mapsto(H+AD,D)$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
            "Factor $A=E_1\\Pi E_2$ by pivoting from the top row with lower triangular elimination, then conjugate the elementary shear $H_i\\gets H_i+D_j$ for each one of $\\Pi$ by triangular controlled shifts.",
            mot("Lower triangular changes of coordinates update a later field from earlier fields, which controlled shifts do in linear time, so all the cost is concentrated in the rank-many ones of $\\Pi$.", "explicit",
                "can be performed entirely in this direction."),
            [
                infer("S3.1.1",
                      "Every rational $m\\times m$ matrix $A$ of rank $a$ is $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ having exactly $a$ ones, at most one per row and column.",
                      "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"),
                infer("S3.1.2",
                      "The shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ is performed with exactly $a$ interchanges of $b$-digit fields, each between an $H$ field and a $D$ field, and $O(V)$ further work.",
                      "can be performed with exactly $a$ interchanges of pairs of $b$-digit"),
            ],
            page="triangular-factorization",
            frm=["controlled-shifts", "linear-algebra-basics", "address-shear", "special-matrices-and-matrix-algebra", "modular-arithmetic"],
            salient="The cost of a shear is the rank $a$ of its matrix, in interchanges, not the dimension $m$: each pivot one of $\\Pi$ costs one interchange and everything else is linear.",
        ),
        infer("S3.2",
              "Splitting whole rows cyclically into $W$ role streams, after padding the row count to a multiple of the needed power of $W$, gives streams of identical shape with volume $V/W$ each.",
              "Split whole rows cyclically into $W$ role streams within each prefix",
              page="row-splitting",
              frm=["tape-address-arrays", "elementary-stream-operations"]),
        infer("S3.3",
              "Running the bit network on the $W$ role streams, with $\\Phi_{A_e}$ on each edge and the gates pointwise, yields $H\\gets H+D$ on every row, including rows that served as scratch roles.",
              "On every circuit edge apply"),
        infer("S3.4",
              "The interchange of the two chunks is the composition $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$, of which only the middle shear needs the network.",
              "To interchange the two full chunks, perform"),
        show(
            "S3.5",
            "A call of width $e=m^k$ makes $s$ calls on streams of volume $V/W$ and does $O(V)$ other work, so the normalized cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$ and is $O(e^\\tau)$ because $s/W<m^\\tau$.",
            "Count the cost of one node as $O(V)$ plus $s$ child calls on streams of volume $V/W$, divide by $V$, and sum the resulting geometric series.",
            mot("Dividing by the volume turns the $s$ calls on $V/W$-volume streams into a factor $s/W<m$ per multiplication of the width by $m$, which is a power saving instead of the factor $m$ per level that a naive recursion gives.", "explicit",
                "is the source of the power saving."),
            [
                infer("S3.5.1",
                      "The relative rank deficits allow the fixed rational exponent $\\tau=1-2^{-50}$, for which $s_{\\rm b}/W_{\\rm b}<m^\\tau$.",
                      "For both recurrences we may use the fixed rational exponent",
                      deferred=True),
                infer("S3.5.2",
                      "With $a=s/W<m^\\tau$ the sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$, so $F_k=O(e^\\tau)$.",
                      "For $a=s/W<m^\\tau$ the geometric sum"),
                infer("S3.5.3",
                      "With finitely many tapes the $s$ recursive calls are run depth first by parking the other $W-1$ role streams on a stack tape, copying the active stream to the child and restoring afterwards, at $O(V)$ cost per node.",
                      "Before a recursive call, append the $W-1$ inactive role streams to the",
                      page="fixed-tape-recursion",
                      frm=["recursion-call-stack-and-subroutines", "turing-machine-tapes", "row-splitting", "linear-network-roles"]),
            ],
            page="recursive-power-saving",
            frm=["recurrences-and-the-recursion-tree", "summation-telescoping-sums-and-geometric-series", "subspace-labels-rank-deficit", "address-shear", "row-splitting", "fixed-tape-recursion"],
            salient="The exponent $\\tau$ is strictly below one exactly because $s<Wm$: the recursive contribution grows by $s/W<m$ per $m$-fold increase of the parameter, so the normalized cost is $e^\\tau$ rather than $e$.",
        ),
        infer("S3.6",
              "For arbitrary chunk widths $u$ and arbitrary row counts, padding the row count to a multiple of $W^k$ and splitting the width in base $m$ interchanges two $u$-bit chunks in $O(Vu^\\tau)$ time.",
              "There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape"),
    ],
    page="address-chunk-interchange",
    frm=["address-shear", "subspace-labels-rank-deficit", "frames", "linear-network-roles", "triple-subset-gadget", "elementary-stream-operations", "controlled-shifts", "tape-address-arrays", "triangular-factorization", "row-splitting", "fixed-tape-recursion", "recursive-power-saving", "modular-arithmetic"],
    salient="The bound $O(Vu^\\tau)$ has an exponent strictly below one, a power saving over the $O(Vu)$ of moving digits one at a time, although intermediate steps compute XORs of data and the final effect is an exact permutation, valid for arbitrary scratch contents.",
)

# ---------------------------------------------------------------- S4
S4 = show(
    "S4",
    "A simultaneous layer applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ at bit position $\\rho$ of each of $D\\le d$ consecutive $K$-bit address chunks of every record runs in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$, evaluating exactly and truncating once with error below $\\sqrt2\\,2^{-p}$.",
    "Write $H_0^{\\otimes D}$ as phases around a layer of the kernel $C$, evaluate $C^{\\otimes e}$ by the complex network recursion on $s$ slots of $e/m$ chunks with binary basis changes done by packed XORs, split rows among roles, solve the recurrence, and bound the guard bits needed for exactness.",
    mot("Applying the butterflies one axis at a time would need $D$ whole-array passes, so the layer is done in one recursion whose cost per level obeys the same rank saving $s<Wm$.", "explicit",
        "$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly"),
    [
        infer("S4.1",
              "With $C=aI+bX$, $a=(1+i)/2$, $b=(1-i)/2$ and $\\mathsf S=\\operatorname{diag}(1,i)$, the two-point butterfly satisfies $H_0=b\\,\\mathsf SC\\mathsf S$, and $C^2=X$, $C^4=I$.",
              "H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad",
              page="butterfly-and-phase-kernels",
              frm=["complex-numbers", "special-matrices-and-matrix-algebra", "xor-and-arithmetic-over-f-2"]),
        infer("S4.2",
              "The complex network with column frames evaluates $C^{\\otimes e}$ on $e=mf$ chunks with exactly $s_{\\rm c}$ child calls on $f$ chunks each, plus a fixed number of binary row additions as basis changes.",
              "Summing its residual dimensions gives exactly"),
        infer("S4.3",
              "On all selected coordinates $H_0^{\\otimes D}=b^D\\,\\mathcal S_D\\,C^{\\otimes D}\\,\\mathcal S_D$, where $\\mathcal S_D$ multiplies by $i^{x_1+\\cdots+x_D}$, so a normalized layer is exact Gaussian dyadic phases around a $C$ layer.",
              "\\eqref{eq:phase-basic-identities} on all selected coordinates gives"),
        infer("S4.4",
              "XORing the selected bits $x_{j_i}$ into $y_{j_i}$ at the $f$ positions $j_i=\\rho+iK$ across whole chunks, restoring a third chunk, costs $O(V(L^\\tau+1))$ by eight cyclic shifts and a deterministic repair of an exceptional address set of density at most $80(f-1)2^{-K}$.",
              "At the selected positions $j_i=\\rho+iK$, numbered from the least",
              page="packed-selected-bit-addition",
              frm=["address-chunk-interchange", "controlled-shifts", "elementary-stream-operations", "xor-and-arithmetic-over-f-2"]),
        infer("S4.5",
              "Splitting padded rows cyclically among the $W$ roles gives each child call a stream of volume $V/W$ on a fixed number of tapes, with the scratch roles supplied by existing rows.",
              "At a node, write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),"),
        infer("S4.6",
              "The normalized cost satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ and unrolls, with $a=s/W<m^\\lambda$, to $O(d^{\\lambda'})$ for a fixed $\\lambda'<1$.",
              "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
        infer("S4.7",
              "A bound $\\Delta=\\lceil C_0d^{C_1}\\rceil$ on the arithmetic depth of the layer controls both denominator and magnitude growth, so $p+\\Delta$ fractional and $\\Delta+3$ integer bits represent every intermediate value exactly, and $\\Delta=o(p)$.",
              "The accelerated network is evaluated exactly until an entire",
              page="guard-bits-dyadic",
              frm=["fixed-point-disk-grid", "rational-numbers-and-dyadic-fractions", "complex-numbers", "exponentials-and-elementary-inequalities"]),
        infer("S4.8",
              "Since every row of $\\mathcal H$ has absolute row sum one, $\\mathcal H$ maps disk arrays to disk arrays, and the single final truncation $Q_p$ changes the result by less than $\\sqrt2\\,2^{-p}$ in the maximum norm.",
              "Finally, every row of $\\mathcal H$ has"),
    ],
    page="simultaneous-butterfly-layer",
    frm=["address-chunk-interchange", "binary-phase-interface", "butterfly-and-phase-kernels", "packed-selected-bit-addition", "guard-bits-dyadic", "fixed-point-disk-grid", "row-splitting", "recursive-power-saving", "fixed-tape-recursion", "complex-numbers"],
    salient="One layer of up to $d$ butterflies costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, less than the $d$ separate passes of cost $\\Theta(V)$ each, and the whole layer is evaluated exactly and truncated only once.",
    adds=[("D", "selected chunks", "the number of consecutive address chunks in which the same bit position is butterflied", "count"),
          ("K", "chunk width", "the number of bits in one address chunk", "count")],
)

T1 = show(
    "T1",
    "Two tape procedures exist: interchanging two $u$-bit address chunks of an array of volume $V$ in $O(Vu^\\tau)$ time with $\\tau<1$, and applying $H_0$ at one bit position in each of $D\\le d$ address chunks in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$.",
    "Build one fixed linear network per procedure that exchanges two banks of values with signs while restoring all scratch wires, label it with nested subspaces so that the sum $s$ of edge ranks is below $Wm$, and recurse on the edges.",
    mot("A transform level costs a scan of all $\\Theta(n)$ bits for movement and again for arithmetic, so a saving over $\\Theta(n\\log n)$ needs both the address rearrangement and the butterflies to be cheaper than one scan per level.", "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [S1, S2, S3, S4],
    adds=[("W", "wire count", "the number of wires (roles) of the fixed linear network", "count"),
          ("m", "label dimension", "the number of dimensions of the fixed space in which the gate and terminal subspace labels lie", "count"),
          ("s", "call count", "the total number of smaller recursive calls, the sum of the edge ranks of the network", "count")],
)

# ---------------------------------------------------------------- T2
T2 = show(
    "T2",
    "Normalized cyclic convolution over $\\mathbb C[y]/(y^r+1)$ on power-of-two axes is computed from two forward synthetic transforms, pointwise ring products by signed packing and the opposite transform, with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
    "Transform over the ring $\\mathbb C[y]/(y^r+1)$, whose roots of unity are powers of $y$, with simultaneous butterfly layers on a suitable tape layout; keep the frequency order through the pointwise product; multiply the ring elements by signed packing and the established multiplier; then apply the opposite transform.",
    mot("In the ring $\\mathbb C[y]/(y^r+1)$ a multiplication by a root of unity is a signed shift, so the only arithmetic in a transform is the two-point butterflies that the fast layer procedure accelerates.", "explicit",
        "serve as roots of unity in the remaining axes, and multiplication by"),
    [
        show(
            "T2.1",
            "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the length-$t$ transforms $F_t^\\pm$ with roots $\\omega_t=y^{2r/t}$ are contractions, are inverse to each other up to the factor $1/t$, and are computed by a butterfly recursion whose twiddle multiplications are signed shifts.",
            "Define the transforms with roots that are powers of $y$, prove inversion by character cancellation done directly, and evaluate by decimation in frequency.",
            mot("The ring has zero divisors, so the usual division by $\\omega^j-1$ in the geometric-sum argument is unavailable and cancellation must be proved by pairing summands.", "explicit",
                "The ring has zero divisors, so we verify character cancellation"),
            [
                infer("T2.1.1",
                      "Every power of $\\omega_t$ is an isometry of $\\mathcal R_r$, so each transform entry, an average of $t$ such images, is bounded by the maximum input, and both $F_t^\\pm$ are contractions.",
                      "Every power of $\\omega_t$ is an isometry, and each transform entry is"),
                infer("T2.1.2",
                      "Character cancellation $\\sum_{k=0}^{t-1}\\omega_t^{jk}=0$ for $t\\nmid j$ gives $F_t^+F_t^-=t^{-1}I$.",
                      "F_t^+F_t^-=t^{-1}I"),
                infer("T2.1.3",
                      "The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\\omega_t^{-k}$ and recurses on both halves, computing $F_t^-$.",
                      "decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"),
            ],
            page="synthetic-polynomial-transform",
            frm=["polynomial-ring-mod-y-r-plus-1", "dft", "multidimensional-transform", "fft-butterfly", "groups-rings-and-fields", "complex-numbers"],
        ),
        infer("T2.2",
              "The recursion writes $(F_t^-z)_j$ at slot $\\operatorname{rev}_a(j)$, so the procedures $B_tF_t^-$ and $F_t^+B_t^{-1}$, with the bit reversal $B_t$ never executed, are inverse up to $1/t$ and a pointwise product can be taken between them in the stored order.",
              "After all $a$ rounds, the named slots from high to low therefore",
              page="frequency-order-retention",
              frm=["synthetic-polynomial-transform", "fft-butterfly", "butterfly-and-phase-kernels"],
              salient="No bit-reversal permutation is ever executed: the outputs stay in the order the recursion writes them, and the opposite transform, the same recursion run backwards, consumes exactly that order."),
        infer("T2.3",
              "A layout permutation $L$ built from single-bit moves and $O(p/K)$ exchanges of $K$-bit chunks places the selected bits of the axes at a common offset in consecutive chunks, so each transform round is one simultaneous butterfly layer and a transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
              "To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round,",
              page="synthetic-transform-layout",
              frm=["tape-address-arrays", "elementary-stream-operations", "address-chunk-interchange", "simultaneous-butterfly-layer", "frequency-order-retention", "synthetic-polynomial-transform", "fixed-point-disk-grid"]),
        infer("T2.4",
              "Two disk-grid polynomials in $\\mathcal R_r$ can be multiplied exactly, by evaluating their integer coefficient polynomials at $2^{4p}$, multiplying with the established $O(N\\log N)$ multiplier and extracting centered coefficients, and the normalized product is returned in $O(rp\\log(rp))$ time.",
              "One can compute the exact Gaussian integer",
              page="signed-packing",
              frm=["polynomial-ring-mod-y-r-plus-1", "nlogn-multiplier-subroutine", "convolution", "binary-representation-and-schoolbook-arithmetic"]),
        infer("T2.5",
              "Two forward synthetic transforms in the retained $LB$ order, pointwise ring products divided by $r$, the opposite transform and an exact scaling by $M$ compute $\\mathcal M_r(f,g)=(f*g)/T$ with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
              "Perform both forward transforms and retain their common $LB$ order.",
              page="synthetic-convolution",
              frm=["convolution", "synthetic-transform-layout", "frequency-order-retention", "signed-packing", "contractions-and-error", "synthetic-polynomial-transform", "nlogn-multiplier-subroutine"],
              salient="The error bound $\\sqrt2\\,M(3\\ell+1)2^{-p}$ counts three transforms of error $\\sqrt2\\,\\ell\\,2^{-p}$ each plus one truncation, and no permutation of the frequency order contributes."),
    ],
)

# ---------------------------------------------------------------- T3
T3 = show(
    "T3",
    "A Fourier transform on pairwise coprime lengths $s_i$ is expressed through transforms on power-of-two lengths $t_i$ in which the coordinate permutations are retained, the middle transform becomes a cyclic convolution by a chirp, and the retained source permutation cancels in a convolution.",
    "Replace the prime-length transform by Gaussian resampling to power-of-two lengths with the permutations left in the identity, turn the middle transform into a convolution by Bluestein's chirp, and cancel the retained source permutation.",
    mot("The transform lengths that suit the integer product are pairwise coprime, whereas the synthetic transforms only handle powers of two, so some resampling between the two shapes is needed.", "explicit",
        "whereas the synthetic transforms use powers of two. Gaussian resampling"),
    [
        show(
            "T3.1",
            "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, and tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with no sorting.",
            "Use the Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, invert the near-identity $N$ by a Neumann series to extract contractions $A$ and $B_0$, keep the coordinate permutations $P_s$, $P_t$ inside the identity, and apply the maps axis by axis in a padded box.",
            mot("The usual implementation sorts twice on each coordinate; leaving the permutations in the transform formula removes both sorts and leaves only the axis movements that the fast interchange already makes cheap.", "explicit",
                "coordinate. We retain both permutations in the transform formula and"),
            [
                infer("T3.1.1",
                      "The Gaussian-weighted maps $\\mathsf S,\\mathsf T$ satisfy $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, and the sampled map $N=C\\mathsf T\\mathsf D$ is a near-identity with $\\|N-I\\|<2^{-\\alpha^2\\theta}$.",
                      "The Gaussian resampling argument uses two maps",
                      page="gaussian-resampling",
                      frm=["dft", "multidimensional-transform", "complex-numbers", "triangle-inequality-and-norm-bounds", "exponentials-and-elementary-inequalities"]),
                infer("T3.1.2",
                      "Inverting $N$ by a Neumann series and rescaling gives contractions $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$ with $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
                      "Now set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$."),
                infer("T3.1.3",
                      "Ordered disk-grid algorithms approximate $A$ and $B_0$ with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$ on a line of length $t$.",
                      "Lemmas~4.8, 4.9 and 4.12 of"),
                infer("T3.1.4",
                      "Applied axis by axis in the full padded box of $T$ entries, the maps give the tensor identity with error below $dp^2$, time $O(dTp^{3/2+\\delta}\\alpha)$ and axis movement $O(Tp\\,d^2(1+\\ell^\\tau))$.",
                      "Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
            ],
            page="resampling-permutations-retained",
            frm=["gaussian-resampling", "dft", "multidimensional-transform", "address-chunk-interchange", "fixed-point-disk-grid", "contractions-and-error", "tape-address-arrays", "elementary-stream-operations", "nlogn-multiplier-subroutine", "modular-arithmetic"],
            salient="No sort is performed: the two coordinate permutations of the usual implementation, each costing $O(tp\\log t)$ per line, stay inside the formula $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ and only fast axis interchanges remain.",
        ),
        infer("T3.2",
              "For even $t_i$ and the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, $QF_{\\boldsymbol t}u=\\overline a\\cdot\\frac{a*(\\overline a\\cdot u)}{T}$, so the target permutation $Q$ is absorbed into a cyclic convolution.",
              "The factor $QF_{\\boldsymbol t}$ in \\eqref{eq:no-sort-tensor} can be",
              page="bluestein-chirp",
              frm=["dft", "multidimensional-transform", "convolution", "resampling-permutations-retained", "complex-numbers"],
              salient="The chirp convolution also performs the frequency change $Q$ on the target side, so the target permutation never has to be applied as a separate sort."),
        infer("T3.3",
              "The retained source permutation cancels across two forward source transforms, their pointwise product and the opposite-sign transform: $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
              "For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.",
              page="permutation-cancellation",
              frm=["dft", "multidimensional-transform", "convolution", "resampling-permutations-retained", "modular-arithmetic", "sets-functions-bijections-and-permutations"],
              salient="The permutation $R$ appears in all three transforms and disappears from the result: the answer is the plain convolution $(u*v)/S^2$ although $R$ is never executed."),
    ],
)

# ---------------------------------------------------------------- T4
T4 = show(
    "T4",
    "Choosing the parameters $b,p,d,T,S$ compatibly, the radix-digit convolution is mapped onto prime-length axes, evaluated by source transforms, multiplied pointwise and inverted, and the exact $2n$-bit product is recovered by scaling, rounding and carries within time $O(n(\\lg n)^{1-\\kappa})$.",
    "Fix one compatible set of rational exponents and sizes, reduce the integer product to a convolution on prime axes, evaluate the three transforms with the source transform, then verify the error bound for rounding and total the cost.",
    mot("Each procedure comes with its own preconditions (precision, number of axes, separation of lengths), so the integer algorithm exists only after all of them are met simultaneously, and its exactness and cost follow by adding up their errors and times.", "recoverable"),
    [
        infer("T4.1",
              "Put $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, $K=\\lfloor d^{c}\\rfloor$, take a power of two $T\\in[4n/b,8n/b)$, $r=2^{\\lceil(\\log_2T)/d\\rceil}$ and axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod_it_i=T$, so that $Tp=\\Theta(n)$ and $d=\\Theta(p^\\epsilon)$.",
              "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
              page="parameter-choice",
              frm=["floor-ceiling-and-logarithms", "exponentials-and-elementary-inequalities", "big-o", "simultaneous-butterfly-layer", "synthetic-transform-layout", "gaussian-resampling", "resampling-permutations-retained"]),
        infer("T4.2",
              "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, $\\eta=1/(4d)$, exist and are found by deterministic trial division in time $n^{o(1)}$; they give $T/2<S<T$ for $S=\\prod_is_i$ and $t_i/s_i-1>\\eta$ as resampling needs.",
              "We may therefore choose distinct odd primes satisfying",
              page="prime-source-lengths",
              frm=["parameter-choice", "prime-numbers-and-trial-division", "resampling-permutations-retained", "modular-arithmetic", "deterministic-algorithms-and-worst-case-time"]),
        infer("T4.3",
              "Writing both inputs in base $2^b$ with $q=\\lceil n/b\\rceil$ digits, the integer product is the convolution of the digit lists; because $2q-2<S$ padding to length $S$ causes no wraparound, and every coefficient is below $2^{3b}$.",
              "Write the two inputs as polynomials in $2^b$, each with",
              page="integer-as-digit-convolution",
              frm=["convolution", "polynomials", "binary-representation-and-schoolbook-arithmetic", "parameter-choice", "prime-source-lengths"]),
        infer("T4.4",
              "The map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism from $\\mathbb C[x]/(x^S-1)$ to $\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$ preserving convolution, implemented by $d$ triangular controlled shifts and axis reorders in $O(Tp\\,d^2(1+\\ell^\\tau))$ time.",
              "Let $s_1,\\ldots,s_d$ be the pairwise coprime",
              page="crt-address-map",
              frm=["modular-arithmetic", "controlled-shifts", "convolution", "address-chunk-interchange", "tape-address-arrays", "integer-as-digit-convolution", "parameter-choice", "prime-source-lengths"]),
        infer("T4.5",
              "Multiplying coefficient $k$ of the last cyclic axis by $\\zeta^k$, $\\zeta=e^{\\pi i/r}$, is an isomorphism $\\mathbb C[x_d]/(x_d^r-1)\\to\\mathbb C[y]/(y^r+1)$, so complex cyclic convolution of length $T$ is computed by ring convolution followed by the untwist.",
              "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",
              page="phase-twist",
              frm=["convolution", "polynomial-ring-mod-y-r-plus-1", "complex-numbers", "polynomials"]),
        infer("T4.6",
              "The source transform applies the resampling map $A$ on each axis, the chirp transform by ring convolution, the compression $B_0$ and the scale $2^\\gamma$, and approximates $RF_{\\boldsymbol s}$ with error below $9\\,2^{\\gamma}TL\\,2^{-p}$ on inputs of norm at most $.5$.",
              "For a source disk-grid tensor of norm at most $.5$, write",
              page="source-transform",
              frm=["resampling-permutations-retained", "bluestein-chirp", "phase-twist", "synthetic-convolution", "fixed-point-disk-grid", "parameter-choice", "prime-source-lengths", "contractions-and-error"]),
        infer("T4.7",
              "The algorithm forms the radix digits, applies the address map $\\Phi$, computes two source transforms, multiplies pointwise, applies the opposite transform, rescales by $S$ and by $2^{2b+4}S$, rounds and propagates carries.",
              "The source-transform procedures now supply the three transforms needed",
              page="multiplication-algorithm",
              frm=["integer-as-digit-convolution", "crt-address-map", "source-transform", "permutation-cancellation", "parameter-choice", "fixed-point-disk-grid"]),
        infer("T4.8",
              "Rescaling by $S$ and $2^{2b+4}$ undoes the normalizations, the coefficient error is below $448\\,b\\,2^{-3b/4}<1/2$, so rounding gives the exact integer coefficients $c_j<2^{3b}$ and radix-$2^b$ carries give the $2n$-bit product.",
              "In tensor order, the unscaled integer coefficient array is",
              page="exact-recovery",
              frm=["parameter-choice", "integer-as-digit-convolution", "permutation-cancellation", "contractions-and-error", "fixed-point-disk-grid", "synthetic-convolution", "bluestein-chirp", "resampling-permutations-retained", "triangle-inequality-and-norm-bounds", "binary-representation-and-schoolbook-arithmetic"]),
        infer("T4.9",
              "Each of the seven normalized cost terms, relative to $Tp$, is at most $p^{1-2\\kappa}$, with smallest margin $2^{-181}=2\\kappa$, so the total is $O(n(\\lg n)^{1-\\kappa})$ for $\\kappa=2^{-182}$.",
              "Each of the seven displayed powers is at most $1-2\\kappa$ by",
              page="cost-analysis",
              frm=["parameter-choice", "address-chunk-interchange", "simultaneous-butterfly-layer", "synthetic-transform-layout", "synthetic-convolution", "resampling-permutations-retained", "source-transform", "crt-address-map", "bluestein-chirp", "signed-packing", "multiplication-algorithm", "exact-recovery", "deterministic-algorithms-and-worst-case-time", "big-o"],
              salient="The smallest margin below one is $2^{-181}=2\\kappa$, from the chunk-exchange term $pK^{\\tau-1}$ with exponent $1-\\epsilon c(1-\\tau)$, where $\\epsilon=2^{-75}$, $c=2^{-56}$ and $1-\\tau=2^{-50}$; every other term has a far larger margin."),
    ],
    adds=[("b", "digit width", "the number of bits in one radix digit, $\\lceil\\log_2 n\\rceil$", "count"),
          ("p", "working precision", "the number of fractional bits of every stored fixed-point component", "count"),
          ("d", "axis count", "the number of axes of the padded box, also the bound on chunks in one butterfly layer", "count"),
          ("T", "box size", "the number of entries of the padded power-of-two box, the product of the axis lengths", "count"),
          ("S", "convolution length", "the number of coefficients, the product of the prime source lengths", "count")],
)

ROOT = show(
    "R",
    "One deterministic fixed-alphabet, fixed-tape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time, with $\\kappa=2^{-182}$.",
    "Split the integers into radix digits, compute the digit convolution with synthetic transforms whose data movement and butterfly arithmetic are accelerated by two new tape procedures, and recover the exact product by rounding and carries.",
    mot("Multiplication reduces to convolution of short digit lists, which Fourier-type transforms compute, but their $\\Theta(\\log n)$ levels each scanning $\\Theta(n)$ bits already cost $\\Theta(n\\log n)$, so the transforms themselves must be made cheaper.", "explicit",
        "Splitting the inputs into radix digits reduces multiplication to"),
    [T1, T2, T3, T4],
    page="integer-multiplication-below-nlogn",
    frm=["nlogn-conjecture", "deterministic-algorithms-and-worst-case-time", "turing-machine-tapes"],
    salient="The logarithmic factor is beaten by a strict power, $(\\lg n)^{-\\kappa}$, although the exponent $\\kappa=2^{-182}$ is astronomically small.",
    adds=[("n", "input length", "the number of bits of each of the two integers", "count"),
          ("\\kappa", "saving exponent", "the fixed constant $2^{-182}$ by which the power of $\\lg n$ falls below one", "direct")],
)

# ---------------------------------------------------------------- checks
last = -1
ok = True


def walk(node):
    global last, ok
    if node["intention"] == "infer":
        q = node["quote"]["quote"]
        c = SRC.count(q)
        pos = SRC.find(q)
        if c == 0:
            print("MISSING", node["id"], q); ok = False
            return
        if c > 1:
            print("MULTI", c, node["id"], q)
        if not node.get("deferred"):
            if pos < last:
                print("ORDER", node["id"], pos, last, q); ok = False
            last = pos
        print(node["id"], SRC.count("\n", 0, pos) + 1, "deferred" if node.get("deferred") else "")
    else:
        m = node["motivation"]
        if m["source"] == "explicit":
            q = m["quote"]["quote"]
            if SRC.count(q) == 0:
                print("MISSING MOT", node["id"], q); ok = False
        for ch in node["children"]:
            walk(ch)


walk(ROOT)
print("OK" if ok else "BAD")
json.dump({"root": ROOT}, open(OUT, 'w'), indent=1)
