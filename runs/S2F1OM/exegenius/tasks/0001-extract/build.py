import json, re, sys
root = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1"
src = open(root + "/sources/paper.tex").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
S = norm(src)

C = []
def add(id, name, gloss, requires, evid=(), known=False, title=None, symbols=None, aliases=()):
    d = {"id": id, "name": name, "aliases": list(aliases), "gloss": gloss, "requires": list(requires),
         "known": known, "evidence": [{"source": "paper", "quote": q} for q in evid]}
    if title:
        d["title"] = title
        d["symbols"] = [{"symbol": a, "name": b, "meaning": c, "relation": e} for a, b, c, e in symbols]
    C.append(d)

# known
add("big-o", "Big-O notation", "Asymptotic upper bound on growth of a function, ignoring constant factors.", [], known=True)
add("polynomials", "Polynomials", "Finite sums of coefficients times powers of a variable, added and multiplied coefficientwise.", [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a+bi with i²=−1, including unit-modulus roots of unity e^{2πi/k}.", [], known=True)
add("tape-machines", "Turing machines and tapes", "A finite-state machine reading and writing symbols on tapes with moving heads.", [], known=True)

add("fixed-tape-model", "Fixed finite-tape machine model",
    "The computation model: one fixed finite alphabet and a fixed number of one-dimensional tapes, each step touching one cell per tape, so extra tracks or work tapes change time only by a constant factor.",
    ["tape-machines", "big-o"],
    [r"A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."])
add("nlogn-conjecture", "The n log n optimality conjecture",
    "Schönhage and Strassen's proposal that n log n is the optimal order of growth for multiplying n-bit integers on multitape Turing machines.",
    ["big-o", "fixed-tape-model"],
    [r"proposed $n\log n$ as the optimal order of growth"])
add("nlogn-multiplier", "Established O(n log n) multiplier (Harvey–van der Hoeven)",
    "The known fixed-tape integer multiplier running in O(N log N) time on N-bit inputs, used here only as an ordinary subroutine on short records.",
    ["fixed-tape-model", "big-o"],
    [r"the fixed-tape integer multiplier of Harvey and van der Hoeven",
     r"Calls to the established $O(n\log n)$ multiplier are ordinary subroutine"])
add("array-order", "Arrays in lexicographic tape order with address fields",
    "A multidimensional array is stored on a tape in lexicographic order of its address (first coordinate most significant), so address fields are contiguous ranges of positions and an address is implicit in position.",
    ["fixed-tape-model"],
    [r"lexicographic order, with the first coordinate most significant"])
add("stream-ops", "Elementary stream operations",
    "Linear-time tape scans that permute digit values, move a digit, split an array by a digit, apply a pointwise map and merge, or split whole rows cyclically into a fixed number of equal streams.",
    ["array-order"],
    [r"takes $O(V)$ steps on a fixed number of one-dimensional tapes"])
add("controlled-shifts", "Controlled cyclic shifts and rational scalings",
    "In linear time, update a target address field by adding an offset computed from earlier control fields modulo q^b (a cyclic shift of blocks), or multiply it by a fixed rational unit.",
    ["stream-ops"],
    [r"Controlled shifts and fixed rational scalings"])
add("matrix-basics", "Matrix rank, subspaces and orthogonal complements",
    "Rank of a matrix, subspaces of a vector space with a bilinear form, and the orthogonal complement of one subspace inside a larger one, whose dimension equals the change in dimension.",
    [],
    [r"the orthogonal complement of the smaller label inside the larger one",
     r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"])
add("dft", "Discrete Fourier transform",
    "The normalized map sending a length-q vector u to (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}; its inverse-direction version uses the opposite sign, and both are contractions.",
    ["complex-numbers", "polynomials"],
    [r"(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}"])
add("cyclic-convolution", "Cyclic convolution",
    "Multiplication of polynomials (or arrays) modulo x^S − 1, where indices wrap around modulo the length on every axis.",
    ["polynomials"],
    [r"let $*$ denote cyclic convolution in the displayed axes"])
add("convolution-theorem", "Convolution theorem for normalized transforms",
    "The transform of a cyclic convolution equals the pointwise product of transforms (with a normalizing factor), so convolution can be computed by transform, pointwise product and inverse transform.",
    ["dft", "cyclic-convolution"],
    [r"The normalized convolution rule is"])
add("multidim-transform", "Multidimensional (tensor) transforms",
    "A transform on a product of axes of lengths t_1,…,t_D, equal to the tensor product of the one-dimensional transforms applied along each axis in turn.",
    ["dft", "cyclic-convolution", "convolution-theorem"],
    [r"F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm"])
add("int-as-convolution", "Integer multiplication as digit convolution",
    "Writing each input in radix 2^b digits makes the product's digit sequence a convolution of the two coefficient lists; with enough zero padding, cyclic convolution equals ordinary polynomial multiplication, and carrying recovers the integer.",
    ["polynomials", "cyclic-convolution"],
    [r"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
     r"Write the two inputs as polynomials in $2^b$, each with"])
add("fixed-point-disk-grid", "Fixed-point disk grid and error propagation",
    "Complex values stored as pairs of signed fixed-point integers with p fractional bits in the unit disk; algorithms approximate linear contractions, truncation toward zero adds bounded error, and errors add under composition.",
    ["complex-numbers", "fixed-tape-model", "big-o"],
    [r"\mathbb D_p=\{2^{-p}(a+ib):a,b\in\mathbb Z,\ a^2+b^2\leq 2^{2p}\}"])
add("polynomial-ring-mod", "Polynomial ring modulo y^r + 1",
    "Complex polynomials of degree below r with y^r = −1, so multiplication by a power of y is a signed cyclic shift of the coefficient list (negacyclic wraparound).",
    ["polynomials", "complex-numbers"],
    [r"\mathcal R_r=\mathbb C[y]/(y^r+1)"],
    title=r"Polynomial ring modulo $y^r+1$",
    symbols=[("y", "ring variable", "The polynomial variable, which satisfies y^r = −1 and serves as a root of unity.", "direct"),
             ("r", "coefficient count", "The number of complex coefficients in a polynomial record, a power of two.", "count")])
add("butterfly-fft", "Two-point butterfly and radix-2 FFT order",
    "The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) applied recursively by decimation in frequency, with twiddle multiplications, computes a transform of power-of-two length and leaves outputs in bit-reversed slot order.",
    ["dft"],
    [r"the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$"])
add("synthetic-transform", "Synthetic polynomial transform",
    "A Fourier-type transform of arrays of ring polynomials in which the roots of unity are powers y^{2r/t}, so twiddle multiplications are exact signed shifts of coefficient lists and only butterflies cost arithmetic.",
    ["polynomial-ring-mod", "butterfly-fft", "multidim-transform"],
    [r"synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer",
     r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$."])
add("crt-axis-map", "Chinese-remainder address map",
    "A ring isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to d-dimensional cyclic convolution on prime axes, implemented on tape by triangular prefix-controlled cyclic shifts.",
    ["cyclic-convolution", "multidim-transform", "controlled-shifts", "chunk-interchange"],
    [r"Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution"])
add("gaussian-resampling", "Gaussian resampling with retained permutations",
    "Harvey–van der Hoeven's identity expressing a Fourier transform of coprime length s through one of power-of-two length t via Gaussian-weighted maps A and B₀, here keeping the two coordinate permutations inside the formula instead of sorting.",
    ["dft", "multidim-transform", "fixed-point-disk-grid", "nlogn-multiplier"],
    [r"Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform.",
     r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA"])
add("chirp-identity", "Bluestein chirp identity",
    "Rewrites a Fourier transform (with its frequency permutation) as pointwise multiplication by a quadratic phase, a cyclic convolution with the chirp array, and another pointwise phase multiplication.",
    ["dft", "cyclic-convolution", "multidim-transform"],
    [r"Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution"])
add("permutation-cancellation", "Source-permutation cancellation",
    "The coordinate permutation retained by resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S² so no sort is executed.",
    ["gaussian-resampling", "convolution-theorem"],
    [r"Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform."])
add("negacyclic-twist", "Coefficient twist to negacyclic ring",
    "Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution on the last axis to convolution in the ring of polynomials modulo y^r+1, whose negative wrap exactly cancels the twist.",
    ["polynomial-ring-mod", "cyclic-convolution", "fixed-point-disk-grid"],
    [r"A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed."])

# core novelty
add("network", "Linear exchange network with restored scratch wires",
    "A fixed network of linear gates on wires (roles) that swaps two banks of values with prescribed signs and returns every auxiliary scratch wire to its arbitrary initial value, using a copy/gather/scatter/side-injection schedule.",
    ["matrix-basics"],
    [r"We construct two fixed linear networks that exchange two banks of values while restoring every auxiliary value."])
add("frames", "Frames and the common-frame identity",
    "Giving each array on a wire an invertible address-space operator (a frame) at every vertex; because a common frame commutes with a pointwise linear gate, the network's overall effect is the endpoint frames applied to each role, and each edge only changes the frame.",
    ["network", "matrix-basics"],
    [r"the common frame commutes with the pointwise gate",
     r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}"])
add("subset-labels", "Three-element-subset subspace labels",
    "Subspaces of a tensor-cube bilinear space attached to gates, built from indicator vectors of three-element subsets with intersection-size pairings (Frankl–Wilson, Alon), so labels are nested along edges and neighbors are orthogonal.",
    ["network", "frames", "matrix-basics"],
    [r"Let $\mathcal T$ be the set of three-element subsets of $[h]$."])
add("rank-saving", "Rank deficit s < Wm",
    "Summing the dimension changes (edge ranks) of all labels gives a total s of smaller calls strictly below W·m, where W is the number of wires and m the dimension, which is the source of the power saving.",
    ["subset-labels", "frames"],
    [r"The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$."])
add("bit-network", "Bit exchange network with shear interface",
    "The F₂ network with rational labels whose frames are address shears: its endpoint operator is (H,D)→(H+D,D) on every role, using only XOR gates, with rank sum s_b < W_b m.",
    ["subset-labels", "frames", "rank-saving"],
    [r"The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates,"])
add("phase-network", "Complex phase network",
    "The Z[i,1/2] network with binary labels whose frames are phase operators C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge is a product of two-point kernels aI+bX_v and the endpoint operator is C^{⊗m} on every role, with s_c < W_c m.",
    ["subset-labels", "frames", "rank-saving", "butterfly-fft"],
    [r"For each edge of the complex network, write $U,V$ for its tail and"])
add("lower-triangular", "Lower-triangular factorization of matrices",
    "Every rational matrix A of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with a ones (a reversed-order Bruhat factorization).",
    ["matrix-basics"],
    [r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"])
add("matrix-shear", "Rational matrix shear as field interchanges",
    "The map (H,D)→(H+AD,D) over Z/q^b for a rank-a rational matrix A is performed by triangular controlled shifts and exactly a interchanges of b-digit fields.",
    ["lower-triangular", "controlled-shifts"],
    [r"The cost of a rational matrix shear"])
add("power-saving-recurrence", "Power-saving recurrence",
    "Calling s smaller operations of parameter f/m on streams of volume V/W gives normalized cost F_k ≤ (s/W)F_{k−1}+O(1); since s/W < m^τ this solves to O(e^τ), a strict power saving.",
    ["rank-saving", "big-o"],
    [r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."])
add("power-interchange", "Power-width address interchange with rows",
    "Interchanges two chunks of m^k digits using the bit network: split rows among the W roles, apply a matrix shear on each edge via recursive smaller interchanges, merge, then compose three shears into a swap.",
    ["bit-network", "matrix-shear", "stream-ops", "power-saving-recurrence"],
    [r"Power-width interchange with rows"])
add("chunk-interchange", "Fast interchange of address chunks",
    "Exchanges two disjoint address chunks of u bits in an array (any prefix, gap and suffix) in O(V u^τ) tape steps for a fixed τ < 1, by padding rows and splitting the width in base m; the final effect is an exact permutation although intermediate steps form XOR combinations.",
    ["power-interchange"],
    [r"Arbitrary-width interchange",
     r"The first procedure interchanges two disjoint contiguous address fields of $u$ bits"],
    title=r"Fast interchange of $u$-bit address chunks in $O(Vu^\tau)$",
    symbols=[("u", "chunk width", "The number of bits in each of the two address chunks being interchanged.", "count"),
             ("V", "stored bit volume", "The number of data bits stored in the array.", "count"),
             ("\\tau", "interchange exponent", "A fixed constant with 0 < τ < 1 (here 1 − 2^{-50}) in the exponent of the cost.", "direct")])
add("packed-bit-addition", "Packed selected-bit addition with deterministic repair",
    "Performs y←y⊕x on the same bit position of f chunks at once using eight cyclic shifts of whole chunk ranges (a three-chunk rotation trick that restores a scratch chunk), then corrects the small explicitly identified set of addresses where guard values fail.",
    ["chunk-interchange", "controlled-shifts"],
    [r"Packed selected-bit addition on one rectangle"])
add("simultaneous-layer", "Simultaneous butterfly layer",
    "Applies the two-point butterfly H₀ at one bit position in each of D address chunks at once in O(V d^{λ'}) time, by recursing on the complex phase network with packed basis changes, exact Gaussian-dyadic arithmetic and one final truncation.",
    ["phase-network", "packed-bit-addition", "power-saving-recurrence", "butterfly-fft", "fixed-point-disk-grid"],
    [r"Simultaneous normalized butterfly layer"],
    title=r"Simultaneous butterfly layer $H_0^{\otimes D}$",
    symbols=[("H_0", "two-point butterfly", "The matrix ((1,1),(1,−1))/2 sending (u,v) to ((u+v)/2,(u−v)/2).", "direct"),
             ("D", "axis count", "The number of address chunks, one selected bit in each, on which the butterfly acts simultaneously.", "count")])
add("transform-layout", "Synthetic transform layout and stored frequency order",
    "Places selected bits of all participating axes at a common offset in consecutive chunks so each radix-two round is one simultaneous layer, and keeps the bit-reversed frequency order through the pointwise product to the opposite transform.",
    ["synthetic-transform", "chunk-interchange", "simultaneous-layer"],
    [r"Transform layout and cost"])
add("kronecker-packing", "Signed packing (Kronecker substitution)",
    "Multiplies two ring polynomials by evaluating them at B₀=2^{4p} as signed integers, multiplying with the O(N log N) integer multiplier, extracting centered coefficients and wrapping negacyclically.",
    ["polynomial-ring-mod", "nlogn-multiplier"],
    [r"The reduction is a signed form of Kronecker substitution"])
add("ring-convolution", "Convolution over the polynomial ring from the retained layout",
    "Computes normalized convolution of arrays of ring polynomials by two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same stored order.",
    ["transform-layout", "kronecker-packing", "convolution-theorem"],
    [r"Convolution from the retained transform layout"])
add("complex-convolution", "Complex cyclic convolution by coefficient twist",
    "Normalized cyclic convolution f*g/T of complex arrays on power-of-two axes, obtained by twisting the last axis into the polynomial ring and using the ring convolution.",
    ["ring-convolution", "negacyclic-twist"],
    [r"The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist."])
add("source-transform", "Source transform procedure",
    "Computes the transform of coprime length by applying the Gaussian map A line by line, the chirp transform through complex convolution, the map B₀, and an exact power-of-two scale, with the retained permutation R.",
    ["gaussian-resampling", "chirp-identity", "complex-convolution"],
    [r"For a source disk-grid tensor of norm at most $.5$, write"])
add("prime-lengths", "Choice of prime source lengths",
    "Chooses distinct odd primes s_i just below the powers of two t_i (with t_i/s_i separated from 1) via a prime-interval lower bound, found by deterministic search, so S is a constant fraction of the padded box T.",
    ["crt-axis-map", "gaussian-resampling"],
    [r"The distinct prime lengths $s_i$ must be close to the powers of two"])
add("parameter-balance", "Parameter choice and cost balance",
    "Fixes p = Θ(log n), d = ⌊b^ε⌋ axes, chunk size K, ring dimension r = 2^{Θ(p/d)} and the tiny exponents so that every row of the cost table has normalized power of p at most 1 − 2κ, giving total O(n (log n)^{1−κ}).",
    ["simultaneous-layer", "chunk-interchange", "prime-lengths", "source-transform", "ring-convolution"],
    [r"lists costs after division by $V$",
     r"Thus $\min_i g_i=2^{-181}=2\kappa$."])
add("exact-recovery", "Rounding and carry propagation to the exact product",
    "Shows the recovered coefficient error is below 1/2, rounds to the integer convolution coefficients, and propagates radix-2^b carries to output exactly 2n product bits.",
    ["int-as-convolution", "fixed-point-disk-grid"],
    [r"Propagate radix-$2^b$ carries in increasing coefficient order."])
add("mult-algorithm", "The multiplication algorithm",
    "Splits both inputs into digits, applies the coefficient-address map, computes the source transform of each, multiplies pointwise, applies the opposite-sign transform with scalings, rounds and propagates carries.",
    ["int-as-convolution", "crt-axis-map", "source-transform", "permutation-cancellation", "exact-recovery"],
    [r"The source-transform procedures now supply the three transforms needed for the radix-digit convolution."])
add("main-theorem", "Integer multiplication in O(n (lg n)^(1−κ)) time",
    "There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.",
    ["mult-algorithm", "parameter-balance", "nlogn-conjecture", "nlogn-multiplier"],
    [r"There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes",
     r"T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)"],
    title=r"Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time",
    symbols=[("n", "operand length", "The number of bits in each of the two integers being multiplied.", "count"),
             ("\\kappa", "saving exponent", "The fixed constant 2^{-182} by which the logarithmic factor is reduced.", "direct")])

ids = {c["id"] for c in C}
bad = 0
for c in C:
    for r in c["requires"]:
        if r not in ids: print("missing req", c["id"], r); bad += 1
    for e in c["evidence"]:
        if norm(e["quote"]) not in S: print("BAD QUOTE", c["id"], e["quote"][:70]); bad += 1
    if c["known"] and c["requires"]: print("known with reqs", c["id"]); bad += 1
    if not c["known"] and not c["evidence"]: print("no evidence", c["id"]); bad += 1
# cycle check
state = {}
def dfs(n):
    if state.get(n) == 1: print("CYCLE", n); return
    if state.get(n) == 2: return
    state[n] = 1
    for r in next(c for c in C if c["id"] == n)["requires"]: dfs(r)
    state[n] = 2
for i in ids: dfs(i)
print("concepts", len(C), "problems", bad)
json.dump({"target": "main-theorem", "concepts": C}, open(root + "/exegenius/tasks/0001-extract.answer.json", "w"), indent=1, ensure_ascii=False)
