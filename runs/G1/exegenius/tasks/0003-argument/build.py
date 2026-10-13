import json

def ev(q): return {"source": "paper", "quote": q}
def expl(text, q): return {"text": text, "source": "explicit", "quote": ev(q)}
def reco(text): return {"text": text, "source": "recoverable", "quote": None}
def recon(text): return {"text": text, "source": "reconstructed", "quote": None}
def infer(id, claim, q, page=None, frm=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(q), "from": frm or []}
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n
def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n
def b(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

s1_1 = infer("S1.1", "Elementary scans on an array of volume $V$ (digit-pair permutations, digit moves, split-map-merge, row splitting into streams) each take $O(V)$ steps on a fixed number of tapes.",
    "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="stream-operations", frm=["turing-machine-tapes", "tape-scans-and-constant-factor-simulation-on-turing-machines", "binary-and-radix-integer-representation"])
s1_2 = infer("S1.2", "A target address field can be cyclically shifted by an offset computed from earlier control fields in $O(V)$ time, which also multiplies a field by fixed units modulo $q^b$.",
    "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
    page="controlled-shifts", frm=["stream-operations", "modular-arithmetic-and-congruences", "primes-gcd-and-coprimality"])

s13_1 = infer("S1.3.1", "Three-element subset gates (copy, gather, scatter, side injection) are fixed linear maps whose net coefficient from $x_T$ to $y_S$ depends only on the intersection size $|S\\cap T|$, and auxiliary side and center wires cancel the unwanted coefficients.",
    "The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair.",
    page="subset-intersection-gates", frm=["counting-and-binomial-coefficients", "xor-and-mod-2-arithmetic", "vectors-matrices-and-linear-maps"])
s13_2 = infer("S1.3.2", "Three staged invocations of the gate schedule exchange the two banks, sending $(X_a,Y_a)$ to $(-Y_a,X_a)$, and restore every auxiliary scratch value whatever its initial content.",
    "(X_a,Y_a)\\longmapsto(-Y_a,X_a)",
    page="bank-exchange-network", frm=["subset-intersection-gates"],
    salient="The exchange restores every scratch wire for arbitrary initial scratch values; the net effect depends on none of them.")
s13_3 = infer("S1.3.3", "Replacing scalars by arrays with an invertible frame $D_v$ at each vertex lets pointwise linear gates commute with the common frame, so the whole network acts as $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$.",
    "At a vertex $v$, the invariant is that the stored array equals $D_v$ applied",
    page="frames-network", frm=["bank-exchange-network", "vectors-matrices-and-linear-maps", "sets-functions-bijections-and-permutations"])
s13_4 = show("S1.3.4", "Nested subspace labels on the gates and terminals make each edge cost its rank in smaller operations, and the total rank $s$ over all edges is strictly less than $Wm$, where $W$ is the number of wires and $m$ the dimension of the label space.",
    "attach nested nondegenerate subspaces of a fixed bilinear space to every gate and terminal, then count the dimension lost edge by edge",
    expl("The cost of an edge is the dimension change of its label, so a small total loss of dimension gives the deficit.", "The saving will come from keeping the total dimension lost on decreasing"),
    [infer("S1.3.4a", "Every edge of the network joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges, each losing dimension $h$.",
           "Every edge joins comparable nondegenerate labels."),
     infer("S1.3.4b", "The sum $s$ of the rational ranks of the edge differences is $W m-N+2L$ and is therefore less than $Wm$.",
           "The sum of the rational ranks of all edge differences is")],
    page="subspace-rank-saving",
    frm=["rank-bases-and-subspaces", "dot-product-and-orthogonality", "frames-network", "bank-exchange-network", "special-matrices-triangular-diagonal-and-permutation-matrices"],
    salient="The total rank $s$ falls strictly short of $Wm$, although the deficit is a tiny relative fraction; the page should explain why the decreasing edges are confined to the central wires so that the saving exists at all.")
s13_5 = infer("S1.3.5", "A call at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, so the cost per volume obeys $F_k\\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\\tau$ for the explicit exponent $\\tau=1-2^{-50}<1$.",
    "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.")
s1_3 = show("S1.3", "A fixed linear network that exchanges two banks of values, restores its scratch wires and has total edge rank $s<Wm$ yields a recursion whose cost per volume grows only like a fixed power $m^\\tau$ with $\\tau<1$ per multiplication of the parameter by $m$.",
    "build the network from subset gates, carry arrays along it by frames, label its vertices by subspaces, and read off the recursion",
    expl("The source states that the strict inequality is the origin of the saving.", "is the source of the power saving."),
    [s13_1, s13_2, s13_3, s13_4, s13_5],
    page="recursive-power-saving",
    frm=["geometric-series-and-recurrences", "logarithms-and-exponents", "frames-network", "subspace-rank-saving", "big-o-notation"],
    salient="The saving comes from the strict inequality $s/W<m$: the number of smaller calls per unit of volume is below the growth $m$ of the parameter, so each recursion level pays less than the naive factor.",
    adds=[b("W", "wire count", "The number of wires in the fixed linear network, which is also the number of role streams.", "count"),
          b("m", "label dimension", "The dimension of the fixed space whose subspaces label the gates.", "count"),
          b("s", "total edge rank", "The total of the edge ranks, which is the number of smaller operations a call uses.", "count")])

s1_4 = show("S1.4", "Two disjoint address chunks of $u$ bits in a complete array of volume $V$ can be interchanged in time $O(Vu^\\tau)$ for a fixed $\\tau<1$, although intermediate steps form XOR combinations of data.",
    "factor each edge matrix as lower triangular, partial permutation, lower triangular so that an edge of rank $a$ costs $a$ smaller interchanges, then run the bit network recursion and remove the width and row restrictions",
    expl("The source says the rank sum being below the wire count times $m$ gives a power saving in the chunk width.", "$m$, the resulting recurrence saves a power of the chunk width."),
    [infer("S1.4.1", "Every rational matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with $a$ ones.",
           "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
           page="lower-triangular-factorization", frm=["special-matrices-triangular-diagonal-and-permutation-matrices", "rank-bases-and-subspaces", "rational-numbers-and-the-number-systems-q-r-c"]),
     infer("S1.4.2", "The address map $(H,D)\\mapsto(H+AD,D)$ of rank $a$ is performed with exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
           "can be performed with exactly $a$ interchanges of pairs of $b$-digit",
           page="matrix-shear-cost", frm=["lower-triangular-factorization", "controlled-shifts", "modular-arithmetic-and-congruences"]),
     infer("S1.4.3", "For power widths $e=m^k$ with enough rows, the bit network with its shears gives an interchange of two chunks in $O(Ve^\\tau)$ time.",
           "The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every"),
     infer("S1.4.4", "For arbitrary width $u$ and arbitrary shape, the interchange $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ costs $O(Vu^\\tau)$ steps.",
           "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.")],
    page="address-interchange",
    frm=["recursive-power-saving", "stream-operations", "controlled-shifts", "xor-and-mod-2-arithmetic", "frames-network"],
    salient="The procedure computes XOR combinations of intermediate data yet ends as an exact permutation, exact for arbitrary initial auxiliary values; the page should explain why the common frame cancels so that only the shear remains.",
    adds=[b("u", "chunk width", "The number of bits in each of the two address chunks being interchanged.", "count"),
          b("V", "stored volume", "The number of bits stored in the array on which the procedure operates.", "count")])

s1_5 = show("S1.5", "The layer $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied to one selected bit in each of up to $d$ address chunks of polynomial records takes $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$.",
    "express a tensor product of the kernel $C$ through phase frames of the complex network, realize its binary basis changes by packed selected-bit additions on whole chunks, bound the exact dyadic values and convert to the normalized layer",
    expl("The source contrasts the single simultaneous layer with the $D$ separate whole-array passes that individual butterfly factors would need.", "factors would require $D$ whole-array passes."),
    [infer("S1.5.0", "Over Gaussian dyadic values the phase frame changes along the complex network are products of two-point kernels $aI+bX_v$ and telescope to $C^{\\otimes m}$ on every role.",
           "bank exchange, telescoping these phase frames gives $C^{\\otimes m}$",
           page="binary-phase-interface", frm=["subspace-rank-saving", "frames-network", "bank-exchange-network", "fixed-point-arithmetic", "complex-numbers"], deferred=True,
           salient="Every role, including the auxiliary ones, ends with the same kernel power $C^{\\otimes m}$, since the intermediate phase frames telescope."),
     infer("S1.5.1", "Adding the same bit position of $f$ address chunks of one field into another costs a few cyclic shifts of whole chunks plus a correction of an explicitly bounded set of exceptional addresses, restoring a third chunk.",
           "Let $R\\ge1$, $K\\ge6$, $f\\ge1$, $L=fK$, and $0\\le\\rho<K$.",
           page="packed-selected-bit-addition", frm=["address-interchange", "controlled-shifts", "stream-operations", "xor-and-mod-2-arithmetic"]),
     infer("S1.5.2", "The simultaneous normalized butterfly layer returns $Q_p(\\mathcal H z)$ in $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$, evaluating the whole layer exactly before one truncation.",
           "The procedure returns $Q_p(\\mathcal H z)$ in the same array,")],
    page="simultaneous-butterfly-layer",
    frm=["recursive-power-saving", "binary-phase-interface", "packed-selected-bit-addition", "fixed-point-arithmetic", "address-interchange", "fft-butterfly", "negacyclic-ring"],
    salient="One layer on up to $d$ axes costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, less than the $d$ separate whole-array passes; the page should explain why the same rank saving applies to the numerical network.")

S1 = show("S1", "Two recursive tape procedures, an address-chunk interchange and a simultaneous butterfly layer, run faster than the naive costs of address rearrangement and Fourier layers by a power of the width.",
    "build the elementary tape tools, derive a general recursive power saving from a fixed linear network, and instantiate it twice, once for bits and once for complex values",
    expl("Scanning at each of the logarithmically many transform levels already costs $n\\log n$, so both movement and arithmetic need savings.", "$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$."),
    [s1_1, s1_2, s1_3, s1_4, s1_5], frm=["turing-machine-tapes"])

S2 = show("S2", "Convolution of two arrays over $\\mathbb C[y]/(y^r+1)$ is approximated with small error by two forward synthetic transforms, polynomial products and the opposite transform in cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "lay the selected bits of the axes out so that simultaneous layers and chunk interchanges evaluate the synthetic transforms, multiply each record by signed packing, and apply the opposite transform to the same stored frequency order",
    expl("The source says the remaining work is to apply the layers on a suitable layout and keep the frequency order through the convolution.", "layout and retain the resulting frequency order through convolution."),
    [infer("S2.1", "The synthetic transforms on a layout that places the selected bits at a common offset in consecutive $K$-bit chunks cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ and keep a fixed frequency order.",
           "layout permutation $L$ of record addresses, preserving their polynomial",
           page="synthetic-transform-layout",
           frm=["synthetic-transform", "synthetic-roots", "fft-butterfly", "simultaneous-butterfly-layer", "address-interchange", "stream-operations", "negacyclic-ring", "multidimensional-transform", "fixed-point-arithmetic"]),
     infer("S2.2", "Two polynomials of $\\mathbb C[y]/(y^r+1)$ with disk-grid coefficients are multiplied exactly by signed Kronecker packing into four integer products, then divided by $r$ and truncated.",
           "One can compute the exact Gaussian integer",
           page="kronecker-packing", frm=["hvdh-multiplier", "negacyclic-ring", "polynomial-evaluation-and-interpolation", "binary-and-radix-integer-representation"]),
     infer("S2.3", "The normalized ring convolution $\\mathcal M_r(f,g)=(f*g)/T$ has an approximation with error below $\\sqrt2M(3\\ell+1)2^{-p}$ built from the retained transform layout.",
           "$\\mathcal M_r$ on disk grid operands has an approximation with error")],
    page="synthetic-convolution",
    frm=["synthetic-transform-layout", "kronecker-packing", "convolution-theorem", "cyclic-convolution", "negacyclic-ring", "hvdh-multiplier", "synthetic-transform", "synthetic-roots", "fft-butterfly", "fixed-point-arithmetic"],
    salient="The same frequency order is consumed by the opposite transform after a pointwise product, so no sorting back to natural order is ever executed.")

pc = show("S3.9", "With fixed rational exponents and sizes ($p=6\\lceil\\log n\\rceil$, $d\\approx p^\\epsilon$, $T\\approx n/\\log n$), every row of the cost table is a power of $p$ at most $1-2\\kappa$, so the total is $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
    "fix all exponents and sizes at once, tabulate every operation's cost divided by volume as a power of $p$, and check the margin below one for each row",
    reco("The cost of each procedure is a power of the width, so choosing the parameters as powers of $p$ lets every row be compared with $p^1$ and the smallest margin gives $\\kappa$."),
    [infer("S3.9a", "The parameters are the fixed rational numbers $\\tau,\\sigma,\\beta,\\delta,\\lambda,c,\\lambda',C_1,\\epsilon,\\kappa$, chosen conservatively without optimization.",
           "These constants are deliberately conservative; no optimization is claimed.", deferred=True,
           salient="The exponents are astronomically small, such as $\\kappa=2^{-182}$, yet every layer condition holds with room to spare."),
     infer("S3.9b", "The seven dominant margins $g_1,\\dots,g_7$ below one have minimum $2^{-181}=2\\kappa$.",
           "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
     infer("S3.9c", "The complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$, extended to all $n$ by schoolbook multiplication below a cutoff.",
           "The complete large-input bound is consequently")],
    page="parameter-choice",
    frm=["logarithms-and-exponents", "floor-and-ceiling-functions", "geometric-series-and-recurrences", "big-o-notation", "address-interchange", "simultaneous-butterfly-layer", "crt-axis-map", "gaussian-resampling", "synthetic-convolution", "prime-axis-lengths"],
    salient="The final exponent gap $\\kappa=2^{-182}$ is tiny but strictly positive: it is half the smallest of the seven margins below one.")

S3 = show("S3", "The product of two $n$-bit integers is computed exactly by placing radix digits on distinct prime axes, transforming them by resampled, chirped synthetic transforms, multiplying pointwise, transforming back, rescaling, rounding and carrying, within the stated time bound.",
    "reduce the digit convolution to cyclic convolution on prime axes, then to power-of-two axes by Gaussian resampling and chirps, then to the ring convolution by a phase twist, and finish with rounding, carries and a cost table",
    expl("The source says the source transforms are now available as the three transforms needed for the digit convolution.", "The source-transform procedures now supply the three transforms needed"),
    [show("S3.1", "A prime-length Fourier transform is expressed through a power-of-two tensor transform by Gaussian resampling, with the two coordinate permutations left inside the identity rather than sorted.",
          "state Harvey and van der Hoeven's resampling identity for one axis with the permutations retained, then take its tensor product over the axes",
          expl("Executing the permutations would cost two sorts on each coordinate, so the identity retains them and computes the formula directly.", "We retain both permutations in the transform formula and"),
          [infer("S3.1.1", "For coprime $s<t$ with $t/s-1>p/\\alpha^4$, there are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
                 "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and"),
           infer("S3.1.2", "Tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with line-by-line cost $O(dTp^{3/2+\\delta}\\alpha)$ plus axis exposure cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
                 "Suppose every pair $(s_i,t_i)$, $1\\leq i\\leq d$, satisfies")],
          page="gaussian-resampling",
          frm=["dft", "multidimensional-transform", "contraction-error", "hvdh-multiplier", "fixed-point-arithmetic", "address-interchange", "roots-of-unity"],
          salient="The two coordinate permutations of the resampling identity are never executed as sorts; they stay inside the transform formula."),
     infer("S3.2", "The retained source permutation cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving $(u*v)/S^2$, while the middle transform with its permutation becomes a Bluestein chirp convolution.",
           "retained source permutation $R$ cancels when computing a convolution.",
           page="permutation-cancellation", frm=["bluestein-chirp", "convolution-theorem", "cyclic-convolution", "multidimensional-transform", "dft", "modular-arithmetic-and-congruences"],
           salient="After the three transforms the result is exactly $(u*v)/S^2$, the same as if no permutation had been applied."),
     infer("S3.3", "Choosing distinct primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ below the power-of-two axis lengths $t_i$ gives $T/2<S<T$ and leaves each ratio $t_i/s_i$ room for resampling.",
           "We may therefore choose distinct odd primes satisfying",
           page="prime-axis-lengths", frm=["primes-gcd-and-coprimality", "logarithms-and-exponents", "floor-and-ceiling-functions"],
           salient="The product $S$ of the primes fills more than half of the padded box of size $T$."),
     infer("S3.4", "The Chinese-remainder map $\\Phi$ sends cyclic convolution of length $S$ to convolution on $d$ prime-length axes, and is implemented by triangular controlled shifts.",
           "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
           page="crt-axis-map", frm=["integer-mult-as-convolution", "cyclic-convolution", "controlled-shifts", "address-interchange", "primes-gcd-and-coprimality", "modular-arithmetic-and-congruences"]),
     infer("S3.5", "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ turns cyclic convolution of length $r$ on the last axis into convolution modulo $y^r+1$, and untwisting restores the cyclic wrap.",
           "Untwisting therefore recovers the cyclic coefficient with the correct",
           frm=["phase-twist", "synthetic-convolution", "roots-of-unity"]),
     infer("S3.6", "The source transform applies the linewise Gaussian approximations around the chirp transform, which is built from the complex convolution, and scales by $2^\\gamma$; conjugation gives the opposite-sign procedure.",
           "computed chirp transform $\\widetilde{\\mathscr C}$, apply the linewise",
           frm=["gaussian-resampling", "permutation-cancellation", "bluestein-chirp", "synthetic-convolution"]),
     infer("S3.7", "The algorithm places the radix-$2^b$ digits on the prime axes by $\\Phi$, transforms both operands, multiplies pointwise, applies the opposite transform, rescales twice by $S$, rounds, undoes $\\Phi$ and propagates carries.",
           "With these streams prepared, perform the following operations.",
           frm=["crt-axis-map", "integer-mult-as-convolution", "cyclic-convolution", "binary-and-radix-integer-representation"]),
     infer("S3.8", "With the known normalizations removed the total coefficient error is below $1/2$, so rounding to integers and propagating radix carries yields the exact $2n$-bit product.",
           "The strict error below $1/2$ makes the nearest integer to",
           page="exact-recovery", frm=["contraction-error", "integer-mult-as-convolution", "floor-and-ceiling-functions", "binary-and-radix-integer-representation", "triangle-inequality-and-absolute-value"],
           salient="The error bound is strictly below one half uniformly in $n$, so the rounded value is the unique integer coefficient."),
     pc],
    page="multiplication-algorithm",
    frm=["phase-twist", "bluestein-chirp", "integer-mult-as-convolution", "synthetic-convolution", "crt-axis-map", "gaussian-resampling", "permutation-cancellation", "exact-recovery"],
    adds=[b("p", "working precision", "The number of fractional bits kept in each coordinate of a stored complex value.", "count"),
          b("d", "axis count", "The number of axes of the padded array on which the transforms act.", "count"),
          b("T", "padded box size", "The number of entries of the padded power-of-two array.", "count"),
          b("S", "source size", "The product of the distinct prime axis lengths, which is the number of valid coefficient addresses.", "count")])

root = show("S0", "A deterministic fixed-tape Turing machine multiplies $n$-bit integers in $T_A(n)=O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "reduce the product to a digit convolution computed by synthetic transforms, replace the address rearrangement and butterfly layers inside those transforms by two faster recursive tape procedures, then assemble, round and bound the cost",
    expl("The source starts from the reduction of multiplication to convolution and says that both movement and arithmetic need savings.", "We therefore need savings in both movement and arithmetic."),
    [S1, S2, S3], page="sub-nlogn-multiplication",
    frm=["nlogn-conjecture", "integer-mult-as-convolution", "turing-machine-tapes", "big-o-notation"],
    salient="The exponent $1-\\kappa$ with $\\kappa=2^{-182}$ is astronomically close to one, yet strictly below it, which is what refutes the $n\\log n$ conjecture.")

json.dump({"root": root}, open("/home/user/openai-nlogn-wiki/runs/G1/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
