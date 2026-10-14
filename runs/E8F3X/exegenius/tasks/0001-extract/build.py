import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3"
C = []
def add(id, name, gloss, requires, quotes=(), known=False, aliases=(), title=None, symbols=None):
    d = dict(id=id, name=name, aliases=list(aliases), gloss=gloss, requires=list(requires), known=known,
             evidence=[{"source": "paper", "quote": q} for q in quotes])
    if title:
        d["title"] = title
        d["symbols"] = symbols
    C.append(d)

# known
add("big-o-notation", "Big-O notation", "Asymptotic upper bounds on running time such as O(n log n).", [], known=True)
add("polynomials", "Polynomials", "Finite sums of terms c_k y^k, which can be added, multiplied and reduced modulo another polynomial.", [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a + bi with i² = −1, with modulus, conjugation and unit-modulus phases e^{iθ}.", [], known=True)
add("multitape-turing-machine", "Multitape Turing machine", "A machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes whose heads each move at most one cell per step.", [], known=True)

# unknown
add("schonhage-strassen-conjecture", "Schönhage–Strassen optimality conjecture",
    "The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine; the best earlier bound was the unconditional O(n log n) of Harvey and van der Hoeven.",
    ["big-o-notation", "multitape-turing-machine"],
    ["and proposed $n\\log n$ as the optimal order of growth", "disproves the $n\\log n$ optimality conjecture"])
add("hh-multiplier", "Harvey–van der Hoeven O(n log n) multiplier",
    "The established fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here as an ordinary subroutine for short integer products.",
    ["multitape-turing-machine", "big-o-notation"],
    ["Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper",
     "Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine"])
add("cyclic-convolution", "Cyclic convolution",
    "For arrays indexed by a product of cyclic groups, the product whose entry at address j is the sum of u_k v_{j−k} with all indices taken modulo the axis lengths.",
    ["polynomials", "complex-numbers"],
    ["cyclic convolution on the product of the coordinate groups"])
add("radix-digit-convolution", "Integer product as digit convolution",
    "Splitting two integers into radix-2^b digits turns their product into a convolution of the digit sequences followed by carry propagation.",
    ["cyclic-convolution"],
    ["Splitting the inputs into radix digits reduces multiplication to"])
add("dft", "Discrete Fourier transform",
    "The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} (and its opposite-sign version) that turns cyclic convolution into pointwise multiplication.",
    ["cyclic-convolution", "complex-numbers"],
    ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}",
     "The normalized convolution rule is"], aliases=["Fourier transform", "F_q"])
add("multidimensional-transform", "Multidimensional transform",
    "The tensor product of one-dimensional transforms applied along each axis of an array whose axis lengths are t_1,…,t_D; convolution on the product of cyclic groups becomes pointwise multiplication.",
    ["dft", "cyclic-convolution"],
    ["F_{\\boldsymbol t}^\\pm=\\bigotimes_{i=1}^D F_{t_i}^\\pm,"])
add("fft-butterfly", "Two-point butterfly and radix-two recursion",
    "The operation H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of entries, and the decimation-in-frequency recursion that builds a length-2^a transform from a, such layers interleaved with twiddle multiplications.",
    ["dft"],
    ["decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$",
     "address rearrangements, signed shifts, and two-point butterfly operations."],
    aliases=["H₀", "butterfly layer"])
add("contraction-error", "Contractions and error accumulation",
    "A linear map that does not increase the sup norm is a contraction; approximating contractions on a fixed-point grid of 2^{−p} spacing adds errors without amplifying them.",
    ["complex-numbers"],
    ["Composing such algorithms", "Each normalized Fourier transform above is a contraction"])
add("crt-axis-map", "Chinese-remainder map to prime axes",
    "An algebra isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to convolution on the product of cyclic axes of lengths s_i, implemented by triangular controlled shifts.",
    ["multidimensional-transform", "cyclic-convolution"],
    ["Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution",
     "x\\longmapsto\\prod_i x_i^{\\mu_i}"])
add("prime-axis-lengths", "Prime axis lengths near powers of two",
    "Choosing distinct odd primes s_i slightly below the powers of two t_i so their product fills a fixed fraction of the padded box and each ratio t_i/s_i leaves room for resampling.",
    ["crt-axis-map"],
    ["The distinct prime lengths $s_i$ must be close to the powers of two",
     "We may therefore choose distinct odd primes satisfying"])
add("gaussian-resampling", "Gaussian resampling",
    "Harvey–van der Hoeven's identity expressing a Fourier transform of prime-product length s as a transform of power-of-two length t, between two cheap Gaussian-weighted linear contractions A and B₀.",
    ["dft", "multidimensional-transform", "contraction-error"],
    ["Gaussian resampling connects these two shapes",
     "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."])
add("chirp-identity", "Bluestein chirp identity",
    "A Fourier transform of even length t can be written as pointwise multiplication by a chirp phase a, a cyclic convolution with a, and another chirp multiplication.",
    ["dft", "cyclic-convolution"],
    ["Bluestein's chirp identity converts the middle transform", "chirp identity below performs the frequency change"])
add("permutation-cancellation", "Retained permutations cancel in a convolution",
    "The coordinate permutations left inside the resampled transform cancel across two forward transforms, a pointwise product and an opposite-sign transform, so no full sort is executed.",
    ["gaussian-resampling", "chirp-identity", "multidimensional-transform"],
    ["retained source permutation $R$ cancels when computing a convolution"])
add("negacyclic-ring", "Polynomial ring modulo y^r + 1",
    "The complex polynomials of degree below r with y^r = −1; multiplying by a power of y just shifts the coefficient list and flips some signs.",
    ["polynomials", "complex-numbers"],
    ["\\mathcal R_r=\\mathbb C[y]/(y^r+1),", "permutes the coefficients and changes"],
    title="Polynomial ring modulo $y^r + 1$",
    symbols=[
      dict(symbol="y", name="ring variable", meaning="The formal polynomial variable, satisfying y^r = −1 in the ring.", relation="direct"),
      dict(symbol="r", name="ring length", meaning="The number of complex coefficients in a ring element, a power of two.", relation="count")],
    aliases=["negacyclic ring", "R_r"])
add("phase-twist", "Coefficient phase twist",
    "Substituting x_d ↦ ζy with ζ = e^{πi/r} multiplies coefficient k by ζ^k and turns cyclic convolution of length r into negacyclic polynomial multiplication, exactly undone by untwisting.",
    ["negacyclic-ring", "cyclic-convolution"],
    ["A phase twist changes the last cyclic coordinate into a polynomial",
     "x_d\\longmapsto\\zeta y"])
add("synthetic-transform", "Synthetic polynomial transform",
    "A Fourier transform over the negacyclic ring using ω_t = y^{2r/t} as root of unity, so each twiddle multiplication is a signed shift and only butterflies cost arithmetic.",
    ["negacyclic-ring", "fft-butterfly", "multidimensional-transform"],
    ["For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",
     "polynomial transforms\ndeveloped by Nussbaumer and Quandalle".replace("\n", " ")])
add("bit-reversed-order", "Stored bit-reversed frequency order",
    "The recursion writes outputs in bit-reversed order (record permutation B_t), and the opposite transform consumes that same order, so no reordering is needed between the forward transforms and the inverse.",
    ["synthetic-transform"],
    ["Let $B_t$ denote this record permutation",
     "B_tF_t^-,\\qquad F_t^+B_t^{-1},"])
add("kronecker-packing", "Signed Kronecker packing",
    "Packing the coefficients of two polynomials into big signed integers (evaluation at 2^{4p}), multiplying with the fast integer multiplier and unpacking the coefficients.",
    ["negacyclic-ring", "hh-multiplier"],
    ["Signed coefficient packing is a form of Kronecker substitution",
     "signed evaluation integer"])
add("ring-convolution", "Convolution over the polynomial ring",
    "Normalized convolution of arrays with entries in the negacyclic ring: forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform in the retained order.",
    ["synthetic-transform", "bit-reversed-order", "kronecker-packing", "contraction-error"],
    ["\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}.",
     "Perform both forward transforms and retain their common $LB$ order."])
add("tape-stream-operations", "Arrays and elementary stream operations on tape",
    "Arrays stored in lexicographic address order, with linear-time scans that split on a digit, apply a pointwise map and merge, or distribute whole rows among streams.",
    ["multitape-turing-machine", "big-o-notation"],
    ["An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order",
     "\\begin{lemma}[Elementary stream operations]"])
add("controlled-shift", "Controlled shifts and rational scalings",
    "Adding to a later address field an offset computed from earlier control fields, or multiplying it by a rational unit, in linear time by splitting and re-merging blocks.",
    ["tape-stream-operations"],
    ["Suppose a target field $y\\in[Q]$ follows its control fields"])
add("exchange-network", "Bank-exchange network with restored scratch wires",
    "A fixed network of linear gates on wires, built from three-element subsets, that swaps two banks X and Y with a sign and returns every auxiliary scratch wire to its arbitrary initial value.",
    [],
    ["For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
     "We construct two fixed linear networks that exchange two banks of values"])
add("frames", "Frames on network wires",
    "Choosing an invertible operator D_v on the array carried by a wire at each gate, so a pointwise linear gate commutes with it and the intermediate frames cancel, leaving only the endpoint operator on every role.",
    ["exchange-network"],
    ["We call $D_v$ its frame",
     "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}."])
add("subspace-labels", "Nested subspace labels and orthogonal residuals",
    "Subspaces of a fixed m-dimensional bilinear space attached to gates and terminals, nested along edges; an edge's orthogonal residual has dimension equal to the number of smaller operations the edge needs.",
    ["exchange-network", "frames"],
    ["A label is a nondegenerate subspace of a fixed bilinear space.",
     "the \\emph{orthogonal residual} is the orthogonal complement"])
add("rank-saving", "Strict rank saving",
    "The total rank s of all edge changes in the fixed network is strictly less than W·m (wires times label dimension), which makes each recursive level cost a factor s/W < m.",
    ["subspace-labels", "frames"],
    ["The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.",
     "This strict inequality is the source of the power saving."])
add("matrix-factorization", "Lower-triangular factorization of a matrix",
    "Every rational m×m matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.",
    [],
    ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])
add("matrix-shear", "Cost of a matrix shear on address fields",
    "The map (H,D) ↦ (H+AD,D) over Z/q^b for a rational matrix A of rank a is done with exactly a interchanges of b-digit fields plus linear extra work.",
    ["matrix-factorization", "controlled-shift", "tape-stream-operations"],
    ["(H,D)\\longmapsto(H+AD,D)", "can be performed with exactly $a$ interchanges of pairs of $b$-digit"])
add("power-width-interchange", "Power-width chunk interchange",
    "Interchanging two address chunks of m^k digits by running the bit network on W cyclic role streams, with one smaller interchange per unit of edge rank, giving the recurrence F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ).",
    ["rank-saving", "frames", "matrix-shear", "tape-stream-operations"],
    ["The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",
     "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."])
add("chunk-interchange", "Address chunk interchange",
    "Swapping two disjoint equal-width bit chunks of an address array in O(V u^τ) steps for a fixed τ < 1, by XOR combinations whose final effect is an exact permutation.",
    ["power-width-interchange"],
    ["(p,h,g,d,z)\\longmapsto(p,d,g,h,z)",
     "The first procedure interchanges two disjoint contiguous address"],
    title="Address chunk interchange in $O(Vu^\\tau)$",
    symbols=[
      dict(symbol="V", name="stored bit volume", meaning="The number of data bits stored in the array being permuted.", relation="count"),
      dict(symbol="u", name="chunk width", meaning="The number of bits in each of the two interchanged address chunks.", relation="count"),
      dict(symbol="\\tau", name="interchange exponent", meaning="A fixed constant below one, 1 − 2^{−50}, bounding the power of the width in the cost.", relation="direct")])
add("phase-frames", "Phase frames and the two-point kernel C",
    "The complex network uses frames diagonalized by Hadamard matrices with phases i^{wt}; an edge change becomes a product of kernels C = H S H = aI + bX, which are translations of the array, and H₀ = b S C S.",
    ["frames", "subspace-labels", "fft-butterfly"],
    ["C=H\\mathsf SH=aI+bX", "H_0=b\\mathsf SC\\mathsf S"])
add("packed-selected-bit-addition", "Packed selected-bit addition",
    "XORing corresponding selected bits of two address chunks by constantly many cyclic shifts of whole chunk ranges plus a deterministic repair of an explicitly small set of exceptional addresses, using a third chunk as restored scratch.",
    ["chunk-interchange", "controlled-shift"],
    ["y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}",
     "\\begin{lemma}[Packed selected-bit addition on one rectangle]"])
add("guard-bits", "Exact dyadic intermediates with one truncation",
    "Intermediate values in a butterfly layer are exact Gaussian dyadics held with enough guard bits, and a single truncation to the 2^{−p} grid follows the whole contractive layer.",
    ["contraction-error"],
    ["Intermediate values are exact Gaussian dyadics,",
     "truncation follows the completed contractive layer."])
add("simultaneous-butterfly-layer", "Simultaneous butterfly layer",
    "Applying H₀ to one selected bit in each of D address chunks at once, on arrays of ring records, in O(V d^{λ′}) with λ′ < 1 instead of D whole-array passes, via the recursive complex network on packed bit changes.",
    ["phase-frames", "packed-selected-bit-addition", "chunk-interchange", "guard-bits", "rank-saving"],
    ["Simultaneous normalized butterfly layer",
     "We will obtain cost $O(Vd^{\\lambda'})$, with"])
add("transform-layout", "Transform layout and cost",
    "Placing the selected bits of all participating axes at a common offset in K-bit chunks, so each round of the synthetic transform uses the simultaneous layer, at total normalized cost dK + pK^{τ−1} + ℓd^{λ′}.",
    ["synthetic-transform", "bit-reversed-order", "simultaneous-butterfly-layer", "chunk-interchange"],
    ["we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks",
     "\\begin{lemma}[Transform layout and cost]"])
add("parameter-choice", "Parameter choice for the multiplier",
    "Fixed rational exponents (τ, σ, λ′, c, ε, δ, κ) and sizes b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^ℓ, with prime axis lengths s_i < t_i.",
    ["prime-axis-lengths", "transform-layout", "gaussian-resampling"],
    ["b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
     "\\lambda=1-2^{-52},\\qquad c=2^{-56},\\qquad"])
add("exact-recovery", "Exact recovery by rounding and carries",
    "Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2, rounding to integers, and propagating radix carries to output the exact 2n-bit product.",
    ["radix-digit-convolution", "contraction-error"],
    ["proves that the recovered coefficient error is strictly below $1/2$",
     "Propagate radix-$2^b$ carries in increasing coefficient order."])
add("multiplication-algorithm", "The multiplication algorithm",
    "Digits are placed on prime axes by the CRT map, transformed by resampling plus chirp convolution over the polynomial ring for both operands, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried.",
    ["radix-digit-convolution", "crt-axis-map", "gaussian-resampling", "chirp-identity", "permutation-cancellation",
     "phase-twist", "ring-convolution", "parameter-choice", "exact-recovery"],
    ["The source-transform procedures now supply the three transforms needed for the radix-digit convolution.",
     "Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"])
add("time-bound", "Complete time bound",
    "Dividing costs by the volume Tp, seven dominant terms with powers of p below one (margins g₁,…,g₇) show total time O(n (lg n)^{1−κ}); the smallest margin is 2κ.",
    ["multiplication-algorithm", "transform-layout", "simultaneous-butterfly-layer", "chunk-interchange"],
    ["The seven dominant powers in Table~\\ref{tab:costs} have the following",
     "Thus $\\min_i g_i=2^{-181}=2\\kappa$."])
add("main-theorem", "Sub-n-log-n integer multiplication",
    "A single deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.",
    ["time-bound", "multiplication-algorithm", "schonhage-strassen-conjecture"],
    ["We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time, with $\\kappa=2^{-182}$",
     "The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers."],
    title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
    symbols=[
      dict(symbol="n", name="input length", meaning="The number of bits in each of the two integers being multiplied.", relation="count"),
      dict(symbol="\\kappa", name="saving exponent", meaning="The fixed constant 2^{−182} giving the power of lg n saved.", relation="direct")])

ans = {"target": "main-theorem", "concepts": C}
out = ROOT + "/exegenius/tasks/0001-extract.answer.json"
json.dump(ans, open(out, "w"), indent=1, ensure_ascii=False)

# verify
src = open(ROOT + "/sources/paper.tex").read()
norm = lambda s: re.sub(r"\s+", "", s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"'))
ns = norm(src)
bad = 0
for c in C:
    for e in c["evidence"]:
        if norm(e["quote"]) not in ns:
            print("MISSING", c["id"], e["quote"]); bad += 1
ids = {c["id"] for c in C}
for c in C:
    for r in c["requires"]:
        if r not in ids: print("BAD REQ", c["id"], r)
    if not c["known"] and not c["evidence"]: print("NO EVIDENCE", c["id"])
print("bad", bad)
