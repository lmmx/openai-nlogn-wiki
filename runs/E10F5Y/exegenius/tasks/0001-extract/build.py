import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5"
C = []
def add(id, name, gloss, requires, quotes=(), known=False, aliases=(), title=None, symbols=None):
    d = dict(id=id, name=name, aliases=list(aliases), gloss=gloss, requires=list(requires), known=known,
             evidence=[dict(source="paper", quote=q) for q in quotes])
    if title: d["title"] = title
    if symbols: d["symbols"] = symbols
    C.append(d)

# known
add("big-o", "Big-O notation", "Asymptotic upper bounds on running time such as O(n log n).", [], known=True)
add("polynomials", "Polynomials", "Finite sums of coefficients times powers of a variable, added and multiplied coefficientwise.", [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a + bi with i² = −1, with modulus, conjugation and roots of unity e^{2πi/k}.", [], known=True)
add("turing-machine-basics", "Turing machines and tapes", "A finite-state machine with read/write heads moving over tapes of symbols from a finite alphabet.", [], known=True)
add("binary-integers", "Binary integers", "Nonnegative integers written as bit strings, with addition, shifting and two's-complement signed forms.", [], known=True)
add("modular-arithmetic", "Modular arithmetic", "Arithmetic on residues modulo m, including units, inverses and the Chinese remainder theorem.", [], known=True)
add("linear-algebra-basics", "Matrices, rank and linear maps", "Matrices as linear maps, rank, invertibility, subspaces, projections and tensor (Kronecker) products.", [], known=True)

add("multitape-model", "Fixed-tape Turing machine model",
    "The cost model: one fixed finite alphabet and one fixed finite number of one-dimensional tapes, where a step touches one cell per tape and time counts steps.",
    ["turing-machine-basics", "big-o"],
    ["A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.",
     "A step reads and writes at most one cell on each tape and moves each head by at most one cell."])
add("array-layout", "Arrays, address fields and logical volume",
    "Data is stored as a stream in lexicographic address order over a product of fields; the logical volume V counts stored bits and rows are consecutive blocks over a suffix field.",
    ["multitape-model", "binary-integers"],
    ["An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order, with the first coordinate most significant.",
     "The \\emph{logical volume} $V$ is the number of stored data bits."])
add("elementary-streams", "Elementary stream operations",
    "Linear-time scans on fixed tapes that permute digit values, move one digit, split a stream on a digit, apply a pointwise map to aligned streams and merge, or split whole rows cyclically among W streams.",
    ["array-layout"],
    ["Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:"])
add("controlled-shifts", "Controlled cyclic shifts and rational scalings",
    "A later target field can be shifted cyclically by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time by splitting and merging blocks.",
    ["elementary-streams", "modular-arithmetic"],
    ["Suppose a target field $y\\in[Q]$ follows its control fields, each control used in an offset having $O(b)$ digits."])
add("cyclic-convolution", "Cyclic convolution",
    "The convolution of two length-S sequences with indices added modulo S, which is polynomial multiplication in C[x]/(x^S − 1).",
    ["polynomials", "modular-arithmetic"],
    ["Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
     "let $*$ denote cyclic convolution in the displayed axes"])
add("discrete-fourier-transform", "Normalized discrete Fourier transform",
    "The map u ↦ (1/q) Σ_j u_j e^{−2πi jk/q} on length-q vectors; it turns cyclic convolution into pointwise product, is inverted by the opposite-sign transform up to scaling, and is a contraction in the maximum norm.",
    ["complex-numbers", "cyclic-convolution"],
    ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q},",
     "Each normalized Fourier transform above is a contraction"])
add("multidimensional-transform", "Multidimensional transforms and convolution on several axes",
    "Tensor-product transforms and cyclic convolution on arrays indexed by a product of axes, applied one axis at a time, with the maximum-norm contraction property preserved.",
    ["discrete-fourier-transform"],
    ["F_{\\boldsymbol q}:=\\bigotimes_iF_{q_i}",
     "it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two"])
add("fixed-point-numerics", "Fixed-point complex arithmetic and truncation error",
    "Complex values are stored as pairs of signed integers over a 2^p grid inside the unit disk, truncated toward zero by Q_p; contractions pass errors through unchanged and errors of composed steps add.",
    ["complex-numbers", "binary-integers"],
    ["\\mathbb D_p=\\{2^{-p}(a+ib):a,b\\in\\mathbb Z,\\ a^2+b^2\\leq 2^{2p}\\}",
     "Composing such algorithms adds their errors"])
add("radix-digit-convolution", "Integer multiplication as digit convolution",
    "Writing each operand in radix 2^b turns the product into a convolution of short digit polynomials whose coefficients are small integers; carries then recover the binary product.",
    ["polynomials", "binary-integers", "cyclic-convolution"],
    ["Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
     "Thus convolution modulo $x^S-1$ has no nonzero wraparound."])
add("nlogn-multiplier", "Established O(n log n) integer multiplier",
    "The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N), used here only as a black-box subroutine on short records.",
    ["big-o", "multitape-model", "binary-integers"],
    ["Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper bound",
     "Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively."])
add("nlogn-conjecture", "The n log n optimality conjecture",
    "Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multitape multiplication, which a power saving in the log factor refutes.",
    ["nlogn-multiplier"],
    ["disproves the $n\\log n$ optimality conjecture",
     "Its negation requires one machine satisfying $\\liminf_{n\\to\\infty}T_A(n)/(n\\lg n)=0$."])
add("negacyclic-ring", "Polynomial ring modulo y^r + 1",
    "The ring of complex polynomials of degree below r with y^r = −1, where multiplying by y^a only permutes coefficients and flips some signs, so powers of y act as exact roots of unity.",
    ["polynomials", "complex-numbers"],
    ["\\mathcal R_r=\\mathbb C[y]/(y^r+1),",
     "Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs"],
    title="Polynomial ring modulo $y^r + 1$",
    symbols=[dict(symbol="y", name="ring variable", meaning="The formal variable of the polynomials, which satisfies y^r = −1 in the quotient.", relation="direct"),
             dict(symbol="r", name="record length", meaning="The number of complex coefficients in a polynomial record, a power of two.", relation="count")])
add("signed-packing", "Signed packing (Kronecker substitution)",
    "A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at a large base 2^{4p}, multiplying the resulting integers with the O(N log N) multiplier, and reading centered coefficients back out, then wrapping modulo y^r + 1.",
    ["negacyclic-ring", "nlogn-multiplier", "fixed-point-numerics"],
    ["The reduction is a signed form of Kronecker substitution",
     "One can compute the exact Gaussian integer numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time $O(rp\\log(rp))$ on a fixed number of tapes."])
add("coefficient-twist", "Phase twist from cyclic to negacyclic",
    "Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps the cyclic coordinate C[x]/(x^r − 1) isomorphically onto the polynomial ring modulo y^r + 1, so cyclic convolution is computed over the ring and untwisted.",
    ["negacyclic-ring", "cyclic-convolution", "ring-convolution"],
    ["is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",
     "Untwisting therefore recovers the cyclic coefficient with the correct sign."])
add("synthetic-transform", "Synthetic polynomial transform",
    "A Fourier transform over the negacyclic ring in which the roots of unity are powers of y, ω_t = y^{2r/t}, so every twiddle multiplication is a signed shift of a coefficient list (Nussbaumer–Quandalle).",
    ["negacyclic-ring", "discrete-fourier-transform", "multidimensional-transform"],
    ["For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",
     "These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer"])
add("butterfly-recursion", "Decimation-in-frequency butterflies and bit-reversed frequency order",
    "The transform is computed by log t rounds each pairing entries z_k and z_{k+t/2}, applying the two-point butterfly and a twiddle shift, which leaves frequency j stored at its bit-reversed position; the opposite transform consumes that order.",
    ["synthetic-transform", "two-point-butterfly"],
    ["the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for $0\\leq k<t/2$.",
     "the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$."])
add("crt-prime-axes", "Chinese-remainder map to prime cyclic axes",
    "A cyclic convolution of length S = s_1⋯s_d with pairwise coprime s_i becomes a convolution on the product of cyclic axes of lengths s_i via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.",
    ["cyclic-convolution", "modular-arithmetic", "controlled-shifts", "multidimensional-transform", "array-layout"],
    ["$\\Phi$ is an isomorphism and preserves cyclic convolution.",
     "Each triangular update is a prefix-controlled cyclic shift."])
add("bluestein-chirp", "Bluestein chirp identity",
    "A Fourier transform (including its target frequency permutation) equals a pointwise chirp phase, a cyclic convolution with the chirp, and another pointwise chirp phase, so it reduces to cyclic convolution.",
    ["discrete-fourier-transform", "cyclic-convolution", "multidimensional-transform"],
    ["Next, Bluestein's chirp identity converts the middle transform,",
     "The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array."])
add("permutation-cancellation", "Cancellation of the retained source permutation",
    "The coordinate permutation R left inside the resampled transform cancels across two forward transforms, their pointwise product and the opposite transform, giving R F⁺[(R F u)·(R F v)] = u*v/S².",
    ["discrete-fourier-transform", "multidimensional-transform", "cyclic-convolution", "gaussian-resampling"],
    ["Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform.",
     "The second identity shows how the retained source permutation $R$ cancels when computing a convolution."])
add("gaussian-resampling", "Gaussian resampling",
    "Harvey–van der Hoeven's method expressing a Fourier transform of coprime length s through one of a nearby power-of-two length t via Gaussian-weighted contractions A and B₀, with the two coordinate permutations left inside the identity.",
    ["discrete-fourier-transform", "fixed-point-numerics", "modular-arithmetic"],
    ["Gaussian resampling connects these two shapes.",
     "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."])
add("tensor-resampling-box", "Tensor resampling on a padded box",
    "The one-dimensional resampling maps are applied line by line along each axis of a zero-padded power-of-two box, with axes exposed by chunk interchanges, giving error below d p² and cost O(d T p^{3/2+δ} α).",
    ["gaussian-resampling", "multidimensional-transform", "array-layout", "chunk-interchange"],
    ["If each $t_i\\in\\{r/2,r\\}$ with $r=2^\\ell$, the array is kept in the full padded box of $T$ entries",
     "For the tensor product, apply the one-dimensional maps to one coordinate line at a time."])
add("prime-lengths", "Choosing prime source lengths",
    "Distinct odd primes s_i in (1−2η)t_i < s_i ≤ (1−η)t_i are found by trial division, so their product S fills at least half the padded box while each ratio t_i/s_i leaves the separation resampling needs.",
    ["gaussian-resampling"],
    ["We may therefore choose distinct odd primes satisfying",
     "The distinct prime lengths $s_i$ must be close to the powers of two $t_i$"])
add("size-parameters", "Size parameters of the multiplication",
    "From n set b = ⌈log₂ n⌉, precision p = 6b, number of axes d = ⌊b^ε⌋, chunk width K = ⌊d^c⌋, box size T ≈ n/b, axis lengths t_i ∈ {r/2, r} with r = 2^ℓ, so that Tp = Θ(n) and r exceeds every fixed power of p.",
    ["prime-lengths", "radix-digit-convolution"],
    ["b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
     "Take the power of two $T$ in $[4n/b,8n/b)$"])
add("gate-network-frames", "Role networks and frames",
    "A fixed linear network of wires (roles) and pointwise gates is run on arrays; assigning each vertex an invertible frame D_v makes the implemented operator D_out S D_in⁻¹, so only changes of frame along edges cost work.",
    ["linear-algebra-basics", "array-layout"],
    ["We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$.",
     "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}."])
add("scratch-restoration", "Restoring arbitrary scratch values",
    "A linear computation that first subtracts the effect of unknown scratch contents, adds in the real contribution, and undoes it, so the target changes correctly and every scratch value is restored whatever it started as.",
    ["linear-algebra-basics"],
    ["This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation",
     "the last two restore the scratch values."])
add("subset-intersection-network", "Three-subset gather and scatter network",
    "A fixed network on banks indexed by triples of 3-subsets whose gather, scatter, copy and side-injection gates have net coefficient depending on intersection size, cancelled by scratch wires, so three stages realize the signed exchange (X, Y) ↦ (−Y, X).",
    ["scratch-restoration", "linear-algebra-basics"],
    ["The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.",
     "(X_a,Y_a)\\longmapsto(-Y_a,X_a)"])
add("nondegenerate-subspaces", "Nondegenerate subspaces and orthogonal residuals",
    "Subspaces of a bilinear space on which the form is nondegenerate, so the space splits as a subspace plus its orthogonal complement; the orthogonal residual of nested subspaces is the complement of the smaller inside the larger.",
    ["linear-algebra-basics"],
    ["A label is a nondegenerate subspace of a fixed bilinear space.",
     "the \\emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one"])
add("subspace-labels", "Subspace labels and the rank budget",
    "Each gate and terminal of the network gets a nested nondegenerate subspace of an m-dimensional space, so an edge costs its dimension change, and the only decreasing edges are central wires, keeping the total below the wire count times m.",
    ["subset-intersection-network", "nondegenerate-subspaces", "gate-network-frames"],
    ["The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.",
     "Every edge joins comparable nondegenerate labels."])
add("rank-saving-recurrence", "Rank saving and the power-saving recurrence",
    "If a network of W wires has total edge rank s < W m, a call at parameter m·f makes s calls on streams of volume V/W at parameter f, so per-volume cost obeys F_k ≤ (s/W) F_{k−1} + O(1) and grows only like e^τ with τ < 1.",
    ["big-o", "subspace-labels"],
    ["This strict inequality is the source of the power saving.",
     "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."])
add("lower-triangular-factorization", "Lower-triangular factorization of a matrix",
    "Every rational matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones (a Bruhat-type factorization in reversed coordinate order).",
    ["linear-algebra-basics"],
    ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
     "The required factorization is the Bruhat factorization for arbitrary matrices, with coordinate order reversed"])
add("matrix-shear-cost", "Cost of a rational matrix shear",
    "The address map (H,D) ↦ (H + A D, D) over Z/q^b is performed with exactly rank(A) interchanges of b-digit fields plus linear work, using triangular steps and the trick that three updates turn H+D into a swap.",
    ["lower-triangular-factorization", "controlled-shifts", "modular-arithmetic"],
    ["can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.",
     "D_j\\leftarrow D_j+H_i,\\qquad"])
add("bit-network-interface", "Bit network as an address shear",
    "Using projection matrices of the labels as frames, the XOR network turns the role exchange into the shear H ← H + D on every role, with total rational edge rank s_b < W_b m.",
    ["subspace-labels", "gate-network-frames"],
    ["The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",
     "In the tape application, two address chunks are written as vectors $H,D$ of $m$ fields."])
add("power-width-interchange", "Power-width address interchange",
    "Two chunks of m^k radix-q digits are interchanged by splitting rows into W role streams, running the bit network with each edge shear done by recursive interchanges of chunks of 1/m the width, in O(V e^τ) time on fixed tapes.",
    ["bit-network-interface", "matrix-shear-cost", "rank-saving-recurrence", "elementary-streams"],
    ["The chunks can be interchanged in $O(Ve^\\tau)$ time",
     "D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,"])
add("chunk-interchange", "Fast interchange of address chunks",
    "Two disjoint address chunks of u bits in an array with complete Cartesian address set can be exchanged in O(V u^τ) time for a fixed τ < 1, although the intermediate steps form XOR combinations of the data.",
    ["power-width-interchange"],
    ["The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product.",
     "Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."])
add("two-point-butterfly", "Two-point butterfly H₀ and the kernel C",
    "The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and its Gaussian dyadic relative C = H S H = aI + bX with a=(1+i)/2, b=(1−i)/2, C² = X and H₀ = b S C S, which lets H₀ layers be computed from C layers.",
    ["complex-numbers", "linear-algebra-basics"],
    ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)",
     "H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad"])
add("phase-interface", "Binary phase frames",
    "For the complex network with binary labels, the frame C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} makes each edge change a product of one two-point kernel aI + bX_v per residual basis vector, and the whole network equals C^{⊗m} on every role.",
    ["two-point-butterfly", "subspace-labels", "gate-network-frames", "subset-intersection-network"],
    ["is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual",
     "q_U(x)=\\operatorname{wt}(P_Ux)\\pmod4."])
add("packed-selected-bit-addition", "Packed selected-bit addition",
    "An XOR of the same bit position in f chunks of one address range into another is done together by a constant number of cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small explicitly identified set of exceptional addresses.",
    ["chunk-interchange", "controlled-shifts", "elementary-streams"],
    ["We implement a binary row addition on corresponding selected bits in two address chunks.",
     "The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses."])
add("simultaneous-butterfly-layer", "Simultaneous butterfly layer",
    "One H₀ butterfly applied at the same bit offset in D ≤ d address chunks at once, computed exactly via the phase network with recursive calls on 1/m of the axes and a single final truncation, in O(V d^{λ'}) time with λ' < 1.",
    ["phase-interface", "packed-selected-bit-addition", "chunk-interchange", "rank-saving-recurrence", "fixed-point-numerics", "two-point-butterfly"],
    ["The procedure returns $Q_p(\\mathcal H z)$ in the same array,",
     "The procedure evaluates the entire layer exactly before this final truncation."])
add("transform-layout", "Transform layout and cost",
    "A positional permutation moves selected bits of the d−1 axes to a common offset in K-bit chunks so each transform round is one simultaneous layer, giving a forward and opposite synthetic transform costing O(T p [dK + p K^{τ−1} + ℓ d^{λ'}]).",
    ["simultaneous-butterfly-layer", "butterfly-recursion", "chunk-interchange", "synthetic-transform", "array-layout"],
    ["The procedure constructs an explicit positional layout permutation $L$ of record addresses",
     "The forward procedure may retain its output layout for a pointwise product and the following opposite procedure."])
add("ring-convolution", "Convolution from the retained transform layout",
    "Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with explicit error bound.",
    ["transform-layout", "signed-packing", "cyclic-convolution", "negacyclic-ring"],
    ["\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}.",
     "Perform both forward transforms and retain their common $LB$ order."])
add("source-transform", "Source Fourier transform procedure",
    "The computed transform for a coprime-length source: linewise Gaussian map A, the chirp transform done by complex convolution through the phase twist, linewise map B₀, and an exact 2^γ rescale, approximating R F_s.",
    ["gaussian-resampling", "tensor-resampling-box", "bluestein-chirp", "coefficient-twist", "fixed-point-numerics"],
    ["apply the computed chirp transform $\\widetilde{\\mathscr C}$",
     "Define the opposite-sign procedure by"])
add("multiplication-algorithm", "The multiplication algorithm",
    "Split the operands into radix digits, map them by Φ to prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}, round to integers, undo Φ and propagate carries.",
    ["crt-prime-axes", "source-transform", "radix-digit-convolution", "permutation-cancellation", "size-parameters"],
    ["Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain source arrays $u,v$.",
     "Propagate radix-$2^b$ carries in increasing coefficient order."])
add("exact-recovery", "Precision and exact recovery",
    "Disk-margin and error bookkeeping shows the recovered coefficient error stays below 1/2, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.",
    ["multiplication-algorithm", "fixed-point-numerics", "permutation-cancellation"],
    ["The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.",
     "The two occurrences of $S$ in this algorithm undo different normalizations."])
add("time-accounting", "Cost table and the saving exponent κ",
    "Dividing each cost by V = Tp, seven dominant terms have powers of p at most 1 − 2κ below one; the smallest margin 2^{-181} fixes κ = 2^{-182}, and any polylog factor is absorbed.",
    ["multiplication-algorithm", "exact-recovery", "chunk-interchange", "transform-layout", "tensor-resampling-box", "ring-convolution", "size-parameters"],
    ["Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
     "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})."])
add("main-theorem", "Integer multiplication below n log n",
    "A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{-182}, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.",
    ["time-accounting", "exact-recovery", "multiplication-algorithm", "nlogn-conjecture"],
    ["There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes,",
     "T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right),"],
    title="Integer multiplication below $n\\log n$",
    symbols=[dict(symbol="n", name="input length", meaning="The number of bits in each of the two integers being multiplied.", relation="count")])

ans = dict(target="main-theorem", concepts=C)
src = open(ROOT + "/sources/paper.tex").read()
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2013", "-").replace("\u2014", "-")
    return re.sub(r"\s+", "", s)
ns = norm(src)
ids = {c["id"] for c in C}
bad = 0
for c in C:
    for r in c["requires"]:
        if r not in ids: print("missing req", c["id"], r); bad += 1
    if not c["known"] and not c["evidence"]: print("no evidence", c["id"]); bad += 1
    for e in c["evidence"]:
        if norm(e["quote"]) not in ns: print("QUOTE FAIL", c["id"], e["quote"][:80]); bad += 1
# cycle check
state = {}
def dfs(u):
    if state.get(u) == 1: print("CYCLE", u); return
    if state.get(u) == 2: return
    state[u] = 1
    for r in next(c for c in C if c["id"] == u)["requires"]: dfs(r)
    state[u] = 2
for i in ids: dfs(i)
print("bad", bad, "concepts", len(C))
json.dump(ans, open(ROOT + "/exegenius/tasks/0001-extract.answer.json", "w"), indent=1, ensure_ascii=False)
