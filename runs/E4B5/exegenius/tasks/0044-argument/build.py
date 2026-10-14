import json, re, sys
PROJ = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/B5"
src = open(PROJ + "/sources/paper.tex", encoding="utf-8").read()
norm = lambda s: " ".join(s.split())
nsrc = norm(src)

def Q(text):
    return {"source": "paper", "quote": text}

def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": Q(quote) if quote else None}

def Bd(symbol, name, meaning, rel):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

def infer(id, claim, quote, page=None, frm=(), salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, motivation, children, page=None, frm=(), salient=None, adds=()):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = list(adds)
    return n

# ---------------------------------------------------------------- A: address interchange
S1_1 = infer("S1.1",
    "Splitting, merging and fixed permutations of digits of an array stored in lexicographic address order cost $O(V)$ by linear scans on a fixed number of tapes.",
    "Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="streams", frm=["fixed-tape-model", "lexicographic-order-and-mixed-radix-indices", "tape-basics"])
S1_2 = infer("S1.2",
    "Adding to a later address field an offset computed from earlier fields, or multiplying it by a fixed unit modulo $q^b$, costs $O(V)$.",
    "Suppose a target field $y\\in[Q]$ follows its control fields, each control used in an offset having $O(b)$ digits.",
    page="controlled-shifts", frm=["streams", "modular-arithmetic", "division-with-remainder"])
S1_3 = infer("S1.3",
    "A fixed linear network of copy, gather, scatter and side-injection gates on banks $X,Y$ and scratch wires sends $(X,Y)$ to $(-Y,X)$ in three stages and restores arbitrary initial scratch values.",
    "For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
    page="scalar-exchange-network", frm=["three-subset-pairing", "linear-algebra", "xor-and-arithmetic-over-f₂"],
    salient="The exchange works whatever the scratch wires held at the start, and leaves them exactly as they were: a first pair of rows cancels the old scratch contents, later rows add the wanted contribution, and the last rows undo the scratch changes.")
S1_4 = infer("S1.4",
    "If each vertex $v$ of the network carries an invertible operator $D_v$ so that stored arrays are $D_v$ applied to logical arrays, pointwise gates commute with the common frame and the network implements $D_{\\rm out}\\,\\mathsf S\\,D_{\\rm in}^{-1}$, leaving only the edge changes $D_vD_u^{-1}$ to pay for.",
    "Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks.",
    page="frames", frm=["scalar-exchange-network", "linear-algebra", "matrices-and-linear-maps"])
S1_5 = infer("S1.5",
    "Nested nondegenerate subspaces of an $m$-dimensional space attached to the gates and terminals make the only dimension losses the central-wire returns, so the total rank of the edge changes satisfies $s<Wm$.",
    "Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$.",
    page="subspace-labels", frm=["three-subset-pairing", "linear-algebra", "frames"],
    salient="The total rank is strictly below the number of wires times $m$: only the central wires ever lose dimension, so the loss is less than half the source dimension, and this strict gap is the whole source of the power saving.")
S1_6 = infer("S1.6",
    "The $\\mathbb F_2$ network with $W_{\\rm b}$ wires and rational labels has endpoint matrices differing by the identity on every input role, which gives the address shear $H\\leftarrow H+D$ on every role at total edge rank $s_{\\rm b}<W_{\\rm b}m$.",
    "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\\rho$ of that vector.",
    page="bit-network", frm=["scalar-exchange-network", "frames", "subspace-labels", "power-saving-recursion", "linear-algebra"],
    salient="The endpoint matrices differ by the same identity matrix on every input role, scratch roles included, so one and the same shear $H\\leftarrow H+D$ is applied to all $W_{\\rm b}$ role arrays.")
S1_7 = infer("S1.7",
    "Every rational matrix $A$ of rank $a$ equals $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
    "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
    page="lower-triangular-factorization", frm=["linear-algebra", "matrices-and-linear-maps"])
S1_8 = infer("S1.8",
    "The permutation $(H,D)\\mapsto(H+AD,D)$ of address fields modulo $q^b$ is done with exactly $\\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ work, using triangular factors and controlled shifts.",
    "can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.",
    page="address-shear", frm=["controlled-shifts", "lower-triangular-factorization", "bit-network", "streams", "modular-arithmetic"])
S1_9 = infer("S1.9",
    "The network makes $s<Wm$ calls on streams of volume $V/W$, so the per-volume cost obeys $F_k\\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\\tau$, giving $F_k=O(e^\\tau)$ at width $e=m^k$, scheduled depth first on fixed tapes.",
    "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$.",
    page="power-saving-recursion", frm=["recurrences-and-divide-and-conquer", "asymptotic-notation-beyond-big-o", "streams", "frames", "subspace-labels"],
    salient="Each recursion level multiplies the cost per volume by $s/W$, which may exceed one, yet the total grows only like $e^\\tau$ with $\\tau<1$ because $s/W$ is strictly smaller than $m$, the factor by which the width grows.")
S1_10 = infer("S1.10",
    "Arbitrary widths and row counts reduce to power widths with enough rows, supplied by a few of the array's own high digits at cost below the final bound, so the interchange costs $O(Vu^\\tau)$ for every $u$.",
    "Rows for a general array can be supplied by a few of its own high digits.")
S1 = show("S1",
    "Interchanging two disjoint contiguous $u$-bit address fields of an array of volume $V$ takes $O(Vu^\\tau)$ time for a fixed $\\tau<1$, by recursing through a network of $W$ wires and $m$-dimensional labels that makes only $s<Wm$ smaller interchanges.",
    "Build a fixed linear network whose edge changes cost rank-many smaller interchanges, and solve the resulting rank-deficit recursion",
    mot("An edge change of rank $a$ costs $a$ smaller interchanges, and because the total rank is below the number of wires times $m$, the recursion on chunk width grows only by a power less than one.",
        "explicit",
        "Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width."),
    [S1_1, S1_2, S1_3, S1_4, S1_5, S1_6, S1_7, S1_8, S1_9, S1_10],
    page="chunk-interchange", frm=["fixed-tape-model", "recurrences-and-divide-and-conquer", "xor-and-arithmetic-over-f₂"],
    salient="Although the final effect is an exact permutation, the intermediate steps are XOR combinations of data, and the cost per bit grows only as $u^\\tau$ with $\\tau<1$, not as $\\log V$.",
    adds=[Bd("u", "field width", "The number of bits in each of the two address fields being interchanged.", "count"),
          Bd("V", "array volume", "The number of data bits stored in the array.", "count"),
          Bd("W", "wire count", "The number of wires of the fixed linear network.", "count"),
          Bd("m", "label dimension", "The dimension of the fixed space whose subspaces label the network.", "count"),
          Bd("s", "smaller calls", "The total rank of all edge changes, which is the number of smaller interchanges one use of the network makes.", "count")])

# ---------------------------------------------------------------- B: simultaneous layer
B1 = infer("B1",
    "A complex network with binary labels and Hadamard-conjugated phase frames $i^{\\operatorname{wt}(P_Ux)}$ makes every edge a product of translation kernels $aI+bX_v$ and produces $C^{\\otimes e}$ on every role, where $C=H\\operatorname{diag}(1,i)H$, and $H_0=b\\,\\mathsf S C\\mathsf S$.",
    "Proposition~\\ref{prop:complex-motif-interface} therefore gives $C^{\\otimes e}$ on every role, including roles whose initial scratch values were arbitrary.",
    page="phase-frames", frm=["scalar-exchange-network", "frames", "subspace-labels", "linear-algebra", "complex-numbers", "xor-and-arithmetic-over-f₂"],
    salient="The same kernel $C$ appears on every role, scratch roles included, and the butterfly $H_0$ is just $C$ conjugated by the diagonal phases $\\mathsf S=\\operatorname{diag}(1,i)$ up to a scalar.")
B2 = infer("B2",
    "A binary row addition on corresponding selected bits of address chunks, which implements the binary basis changes, takes a constant number of whole-chunk cyclic shifts followed by repair of an explicitly bounded exceptional set of addresses.",
    "The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses.",
    page="packed-selected-bits", frm=["chunk-interchange", "controlled-shifts", "streams", "xor-and-arithmetic-over-f₂"])
B3 = infer("B3",
    "A node of $e=m^k$ selected axes makes $s_{\\rm c}<W_{\\rm c}m$ recursive calls on slots of $e/m$ axes, each on a $1/W_{\\rm c}$ share of the volume, so the same rank-deficit recursion gives cost $O(d^{\\lambda'})$ per unit volume.",
    "The phase construction supplies one recursive call on a slot for each vector in an edge residual basis, hence exactly \\(s\\) calls in one invocation of the network.",
    frm=["power-saving-recursion", "phase-frames", "packed-selected-bits"])
B4 = infer("B4",
    "Intermediate values of a butterfly layer are Gaussian integers over powers of two, computed exactly with a guard width of $O(d^{20})=o(p)$ extra bits, with a single truncation at the end.",
    "The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete.",
    page="dyadic-exact", frm=["fixed-point", "two-s-complement-and-truncation", "complex-numbers", "binary-representation-and-integer-arithmetic"])
B5 = infer("B5",
    "Every row of the layer matrix has absolute sum one, so the layer maps disk arrays to disk arrays and the single final truncation toward zero adds error below $\\sqrt2\\,2^{-p}$.",
    "Thus $\\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk",
    frm=["fixed-point", "dyadic-exact", "inequalities-for-error-bounds"])
B = show("B",
    "Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ at one common bit position of $D\\le d$ address chunks of an array of $r$-coefficient polynomial records, then truncating once to the $2^{-p}$ grid, takes $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$, rather than $D$ whole-array passes.",
    "Write the layer as a tensor product of the two-point kernel $C$ through phase frames of the complex network, recurse on $e=mf$ axes with rank-deficit calls, make the basis changes by packed bit additions, and evaluate exactly in Gaussian dyadics before one truncation",
    mot("The rank-deficit recursion that speeds up address interchange also applies to a network of two-point kernels; the layer must be evaluated exactly in dyadics because the intermediate operators are not contractions.",
        "recoverable"),
    [B1, B2, B3, B4, B5],
    page="simultaneous-layer", frm=["fixed-point", "dyadic-exact", "chunk-interchange", "power-saving-recursion"],
    salient="One layer on $D$ chunks costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, which is less than the $D$ separate whole-array passes it replaces.")

# ---------------------------------------------------------------- C: transform layout
C1_ring = infer("C1.1",
    "In $\\mathbb C[y]/(y^r+1)$ with $y^r=-1$, multiplication by any power of $y$ permutes the coefficients and changes some signs, so it is a signed shift and an isometry for the maximum coefficient norm.",
    "Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs; consequently it is an isometry for this norm.",
    page="ring-mod-yr-plus-1", frm=["polynomials", "complex-numbers", "modular-arithmetic"])
C1_char = infer("C1.2",
    "Character sums of $\\omega_t=y^{2r/t}$ vanish unless $t\\mid j$, shown directly because the ring has zero divisors, so $F_t^+F_t^-=t^{-1}I$.",
    "The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\\omega_t^j-1$.",
    frm=["ring-mod-yr-plus-1", "dft"])
C1_bf = infer("C1.3",
    "The map $H_0$, followed by multiplying one output by a power of $\\omega_t$, splits a length-$t$ transform into two half-length transforms (decimation in frequency), and $\\log_2 t$ rounds give the transform.",
    "For $t\\geq2$, the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for $0\\leq k<t/2$.",
    page="butterfly", frm=["dft", "fast-fourier-transform-as-an-algorithm", "recurrences-and-divide-and-conquer"])
C1 = show("C1",
    "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the normalized transforms $F_t^{-}$ and $F_t^{+}$ with roots of unity $\\omega_t=y^{2r/t}$ are evaluated by radix-two butterfly rounds whose twiddle multiplications are signed shifts.",
    "Run the radix-two decimation-in-frequency recursion with powers of $y$ as the roots of unity",
    mot("Powers of $y$ serve as roots of unity and multiplication by such a root is a signed shift of the coefficient list.",
        "explicit",
        "Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list."),
    [C1_ring, C1_char, C1_bf],
    page="synthetic-transform", frm=["dft", "ring-mod-yr-plus-1", "butterfly"])
C2 = infer("C2",
    "The forward synthetic transform writes its outputs in bit-reversed slots, and the pointwise product and the opposite-sign transform consume that same order, so no reordering is executed.",
    "The recursion writes its outputs directly in this order; it does not move whole frequency indices.",
    page="stored-order", frm=["synthetic-transform", "butterfly", "sets-functions-and-permutations"],
    salient="The bit-reversal permutation costs nothing, because the forward transform leaves frequencies in that order and the opposite transform is built to read them in that order.")
C3 = infer("C3",
    "With the layout permutation $L$ and its restoration charged, each forward or opposite procedure on $T$ entries has error below $\\sqrt2\\,\\ell\\,2^{-p}$ and costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "Each procedure has error less than $\\sqrt2\\ell\\,2^{-p}$, returns disk grid coefficients in the same component format, and costs",
    frm=["chunk-interchange", "simultaneous-layer", "fixed-point"])
C = show("C",
    "Placing the selected bits of the participating axes at a common offset in $K$-bit chunks lets every synthetic transform round use the simultaneous layer, so a transform of $T$ entries costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "Build the simultaneous layer, define the synthetic transform and its stored order, then lay out the axes so each round is one layer call",
    mot("Each radix-two round must act on the same bit position of many axes at once for the layer to apply, so the axes' bits have to be brought to a common offset in consecutive chunks.",
        "explicit",
        "we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks."),
    [B, C1, C2, C3],
    page="transform-layout", frm=["fixed-point", "chunk-interchange"],
    salient="Each of the three cost terms $dK$, $pK^{\\tau-1}$ and $\\ell d^{\\lambda'}$ is a power of $p$ below one after dividing by the volume, which is what makes the transform cheaper than $\\Theta(Tp\\ell)$.")

# ---------------------------------------------------------------- D: synthetic convolution
D1 = infer("D1",
    "Evaluating polynomials at $2^{4p}$ (a signed Kronecker substitution) turns one product in the ring into four integer products by the established multiplier, and centered coefficients are read back, in $O(rp\\log(rp))$ time.",
    "One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\\log(rp))$ on a fixed number of tapes.",
    page="signed-packing", frm=["ring-mod-yr-plus-1", "hvdh-multiplier", "fixed-point", "two-s-complement-and-truncation"])
D2 = infer("D2",
    "Both forward transforms keep the layout order, the records are multiplied pointwise in that order, and the opposite transform followed by exact scaling by $M$ returns $\\mathcal M_r(f,g)=(f*g)/T$.",
    "Perform both forward transforms and retain their common $LB$ order.",
    frm=["stored-order", "signed-packing", "convolution", "dft"])
D = show("D",
    "Two forward synthetic transforms, a pointwise ring product by signed packing and the opposite transform give the normalized convolution $(f*g)/T$ over $\\mathbb C[y]/(y^r+1)$, with $T=rM$, error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "Apply the convolution theorem over the ring: transform both operands, multiply pointwise, transform back",
    mot("Convolution becomes pointwise multiplication under a Fourier transform; over this ring the transform needs only signed shifts and the pointwise products are polynomial products done by the established multiplier.",
        "recoverable"),
    [C, D1, D2],
    page="synthetic-convolution", frm=["convolution", "dft", "fixed-point"])

# ---------------------------------------------------------------- M: multiplication algorithm
M_gauss = infer("M1",
    "Gaussian resampling expresses the Fourier transform of length $s_i$ through a power-of-two length $t_i>s_i$ transform by contractions $A$ and $B_0$, with $P_{s_i}F_{s_i}=2^{2\\alpha^2}B_0P_{t_i}F_{t_i}A$ and a small error $N-I$.",
    "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ satisfying",
    page="gaussian-resampling", frm=["dft", "fixed-point", "complex-numbers", "inequalities-for-error-bounds", "convolution"],
    salient="The two coordinate permutations $P_{s_i}$ and $P_{t_i}$ stay inside the identity instead of being executed as sorts.")
M_tensor = infer("M2",
    "The one-dimensional maps are applied one coordinate line at a time to a $d$-fold tensor, giving $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ at line cost $O(dTp^{3/2+\\delta}\\alpha)$, with axis movement by the fast interchange.",
    "For the tensor product, apply the one-dimensional maps to one coordinate line at a time.",
    frm=["gaussian-resampling", "chunk-interchange"])
M_chirp = infer("M3",
    "A Fourier transform is a pointwise phase multiplication, a cyclic convolution with a chirp array $a$, and another phase multiplication: $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
    "The factor $QF_{\\boldsymbol t}$ in \\eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications.",
    page="bluestein-chirp", frm=["dft", "convolution", "gaussian-resampling", "complex-numbers"])
M_perm = infer("M4",
    "The chirp absorbs the target permutation $Q$, and the source permutation $R$ cancels across two forward transforms, a pointwise product and the opposite transform: $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "The second identity shows how the retained source permutation $R$ cancels when computing a convolution.",
    page="retained-permutations", frm=["bluestein-chirp", "gaussian-resampling", "dft", "convolution", "sets-functions-and-permutations"],
    salient="Neither coordinate permutation of resampling is ever executed: the target one is absorbed by the chirp and the source one cancels between the forward and opposite transforms.")
M_size = infer("M5",
    "Taking $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d\\approx b^\\epsilon$, $K\\approx d^c$, $T\\approx n/b$ a power of two, axis lengths $t_i\\in\\{r/2,r\\}$ and distinct odd primes $s_i$ just below $t_i$ with $T/2<S<T$ gives $Tp=\\Theta(n)$ and $r$ larger than every power of $p$.",
    "Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\\lceil(\\log_2T)/d\\rceil}$ and $\\ell=\\log_2r$.",
    page="size-parameters", frm=["primes-divisibility-and-coprimality", "logarithms-floors-and-ceilings", "fixed-point", "asymptotic-notation-beyond-big-o"])
M_digit = infer("M6",
    "Writing both inputs in radix $2^b$ with $q=\\lceil n/b\\rceil$ digits, the product coefficients are a cyclic convolution of length $S>2q-2$ with no wraparound and each coefficient is below $2^{3b}$.",
    "Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
    page="digit-convolution", frm=["convolution", "polynomials", "schoolbook-and-karatsuba-multiplication", "binary-representation-and-integer-arithmetic"])
M_crt = infer("M7",
    "For pairwise coprime lengths $s_i$ the map $x\\mapsto\\prod_i x_i^{\\mu_i}$ turns a length-$S$ cyclic convolution into convolution on a product of prime cyclic axes, realized by triangular controlled shifts.",
    "Hence $\\Phi$ is an isomorphism and preserves cyclic convolution.",
    page="crt-cyclic-axes", frm=["convolution", "digit-convolution", "primes-divisibility-and-coprimality", "modular-arithmetic", "controlled-shifts", "chunk-interchange"],
    salient="Each new axis coordinate depends only on lower-index digits, so the whole change of order is a sequence of controlled cyclic shifts rather than a general sort.")
M_twist = infer("M8",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathbb C[y]/(y^r+1)$, so negative wrap becomes cyclic wrap.",
    "On the bases $(x_d^k)_{0\\le k<r}$ and $(y^k)_{0\\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\\zeta^k$.",
    page="phase-twist", frm=["ring-mod-yr-plus-1", "convolution", "complex-numbers"],
    salient="A term that wraps past degree $r$ picks up $\\zeta^r=-1$, which exactly cancels the sign $-1$ of the negacyclic wrap.")
M_run = infer("M9",
    "The digits are placed on the prime axes by $\\Phi$, two source transforms and one opposite transform with a pointwise product give the digit convolution, and two exact rescalings by $S$ and $2^{2b+4}$ follow.",
    "Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain source arrays $u,v$.",
    frm=["crt-cyclic-axes", "synthetic-convolution", "retained-permutations", "phase-twist"])
M_exact = infer("M10",
    "Undoing the known scales $S$ and $2^{2b+4}$ leaves coefficient error below $1/2$, so rounding gives the exact integer coefficients and carry propagation in radix $2^b$ gives the exact $2n$-bit product.",
    "The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.",
    page="exact-recovery", frm=["fixed-point", "digit-convolution", "crt-cyclic-axes", "inequalities-for-error-bounds", "two-s-complement-and-truncation", "division-with-remainder"])
M = show("M",
    "Digits in radix $2^b$ are placed on distinct prime cyclic axes, two source transforms (Gaussian resampling with chirp convolution over the ring via a twist) and one opposite transform give their convolution, and rescaling, rounding and carrying yield the exact $2n$-bit product.",
    "Reduce the product to a radix-digit convolution, compute it with Fourier transforms made of Gaussian resampling, chirps and synthetic ring convolution, then recover exact integers",
    mot("Multiplication is a convolution of the digit sequences, and a Fourier transform turns convolution into pointwise multiplication.",
        "explicit",
        "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients."),
    [D, M_gauss, M_tensor, M_chirp, M_perm, M_size, M_digit, M_crt, M_twist, M_run, M_exact],
    page="multiplication-algorithm", frm=["convolution", "dft", "hvdh-multiplier"],
    adds=[Bd("b", "digit width", "The number of bits in each radix-$2^b$ digit, about $\\log_2 n$.", "count"),
          Bd("p", "precision", "The number of fractional bits of the fixed-point grid.", "count"),
          Bd("d", "axis count", "The number of axes (also the number of chunks a layer treats at once), a small power of $p$.", "count"),
          Bd("K", "chunk width", "The number of bits in one address chunk of a layer.", "count"),
          Bd("\\ell", "log record length", "The base-two logarithm of the number of coefficients of a ring element.", "direct"),
          Bd("r", "record length", "The number of complex coefficients of a polynomial modulo $y^r+1$.", "count"),
          Bd("T", "padded size", "The number of complex entries in the padded box of power-of-two axes.", "count"),
          Bd("\\lambda'", "layer exponent", "A fixed exponent below one for the cost of a simultaneous butterfly layer.", "direct"),
          Bd("S", "source product", "The product of the distinct odd prime lengths of the source axes.", "direct"),
          Bd("s_i", "prime length", "The i-th prime source axis length, just below t_i.", "direct"),
          Bd("t_i", "axis length", "The i-th power-of-two transform axis length, r/2 or r.", "direct")])

# ---------------------------------------------------------------- cost
S3 = infer("S3",
    "Dividing each cost term by $Tp$ leaves powers of $p$ with margins $g_i$ below one; the smallest margin is $2\\kappa=2^{-181}$, which absorbs any polylogarithmic factor and gives total time $O(n(\\lg n)^{1-\\kappa})$.",
    "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
    page="cost-accounting", frm=["big-o", "asymptotic-notation-beyond-big-o", "size-parameters", "synthetic-convolution", "chunk-interchange", "multiplication-algorithm"],
    salient="The smallest of the seven margins is $g_2=\\epsilon c(1-\\tau)=2^{-181}$, a product of tiny fixed parameters, which is why the final exponent $\\kappa=2^{-182}$ is so small.")

ROOT = show("S0",
    "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Replace the logarithmic number of full scans of Fourier-transform multiplication by two power-saving tape procedures, build an exact convolution-based multiplier around them, and add up the costs",
    mot("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both the data movement and the butterfly arithmetic must be made cheaper than one scan per level.",
        "explicit",
        "We therefore need savings in both movement and arithmetic."),
    [S1, M, S3],
    page="main-theorem", frm=["fixed-tape-model", "nlogn-conjecture", "hvdh-multiplier"],
    salient="The saving is a strict power of the logarithm, $(\\lg n)^{-\\kappa}$, although the exponent $\\kappa=2^{-182}$ is astronomically small; the bound holds through all input lengths.",
    adds=[Bd("n", "input length", "The number of bits of each of the two integers to be multiplied.", "count"),
          Bd("\\kappa", "saving exponent", "The fixed constant $2^{-182}$ by which the power of the logarithm is lowered.", "direct"),
          Bd("\\tau", "interchange exponent", "A fixed exponent below one: the cost per bit of interchanging two address fields of width u is u to this power.", "direct")])

ans = {"root": ROOT}

# ------------- checks
def walk(n):
    yield n
    for c in n.get("children", []):
        yield from walk(c)
last = -1
ok = True
for n in walk(ROOT):
    qs = []
    if n["intention"] == "infer":
        qs.append((n["quote"]["quote"], True))
    elif n.get("motivation") and n["motivation"].get("quote"):
        qs.append((n["motivation"]["quote"]["quote"], False))
    for q, ordered in qs:
        i = nsrc.find(norm(q))
        if i < 0:
            print("NOT FOUND", n["id"], q); ok = False; continue
        if ordered:
            if i < last:
                print("OUT OF ORDER", n["id"], i, last); ok = False
            last = i
            print(n["id"], i)
print("ok" if ok else "PROBLEMS")
out = PROJ + "/exegenius/tasks/0044-argument.answer.json"
json.dump(ans, open(out, "w"), ensure_ascii=False, indent=1)
