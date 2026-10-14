import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2"
src = open(ROOT + "/sources/paper.tex", encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", "", s)
srcn = norm(src)

C = []
def add(id, name, gloss, requires, quotes, known=False, aliases=None, title=None, symbols=None):
    d = dict(id=id, name=name, aliases=aliases or [], gloss=gloss, requires=requires,
             known=known, evidence=[dict(source="paper", quote=q) for q in quotes])
    if title:
        d["title"] = title
        d["symbols"] = [dict(symbol=s, name=n, meaning=m, relation=r) for (s, n, m, r) in symbols]
    C.append(d)

# ---- known
add("big-o", "Big-O notation", "Asymptotic upper bounds on running time such as O(n log n).", [], [], known=True)
add("polynomials", "Polynomials", "Sums of coefficients times powers of a variable, with addition, multiplication and evaluation.", [], [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a + bi with i² = −1, including roots of unity e^{2πi/q} and absolute value.", [], [], known=True)
add("turing-machine-tapes", "Turing machines and tapes", "A finite-state machine with read/write heads moving one cell at a time on tapes; running time counts steps.", [], [], known=True)

# ---- context
add("n-log-n-conjecture", "The n log n optimality conjecture",
    "Schönhage and Strassen's conjecture that n log n is the optimal order of growth for the time to multiply two n-bit integers on a multitape Turing machine.",
    ["big-o", "turing-machine-tapes"],
    [r"proposed $n\log n$ as the optimal order of growth",
     r"disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model"])

add("fixed-tape-model", "Fixed finite-tape Turing machine model",
    "One machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads and writes one cell per tape and moves each head by at most one cell, and cost is the number of steps.",
    ["turing-machine-tapes", "big-o"],
    [r"A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.",
     r"A step reads and writes at most one cell on each tape and moves each head by at most one cell."])

add("stream-arrays", "Arrays, address fields and elementary scans",
    "Arrays with a product address set are stored in lexicographic order on tape, with addresses implicit in position; fixed permutations of digits, digit moves, pointwise maps and cyclic row splits cost O(V) for V stored bits.",
    ["fixed-tape-model"],
    [r"An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in lexicographic order, with the first coordinate most significant.",
     r"takes $O(V)$ steps on a fixed number of one-dimensional tapes",
     r"The \emph{logical volume} $V$ is the number of stored data bits."])

add("controlled-shifts", "Controlled cyclic shifts and rational scalings",
    "A linear-time tape operation that adds an offset computed from earlier control fields to a later target field modulo q^b, or multiplies it by a fixed unit, by splitting and re-merging blocks.",
    ["stream-arrays"],
    [r"Suppose a target field $y\in[Q]$ follows its control fields, each control used in an offset having $O(b)$ digits.",
     r"The next operations are linear because their target field follows their control fields."])

# ---- multiplication side
add("radix-digit-convolution", "Integer multiplication as digit convolution",
    "Writing each integer as a polynomial in a power of two 2^b, the product's digit-coefficient list is the convolution of the two digit lists, followed by carry propagation.",
    ["polynomials", "big-o"],
    [r"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
     r"Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits."])

add("dft-cyclic-convolution", "Normalized DFT and cyclic convolution",
    "The length-q discrete Fourier transform with 1/q normalization turns cyclic convolution into pointwise multiplication; its inverse uses the opposite sign of the exponent.",
    ["complex-numbers", "polynomials"],
    [r"(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}",
     r"The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot}"])

add("multidim-transform", "Multidimensional (tensor) Fourier transform",
    "The tensor product of one-dimensional transforms along several axes; a transform on an array with axis lengths t_1,…,t_d is applied axis by axis.",
    ["dft-cyclic-convolution"],
    [r"it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two",
     r"F_{\boldsymbol q}:=\bigotimes_iF_{q_i}"])

add("crt-axis-map", "Chinese-remainder map to prime cyclic axes",
    "An algebra isomorphism sending one cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to a convolution on a product of d cyclic axes, implemented by triangular controlled cyclic shifts.",
    ["dft-cyclic-convolution", "multidim-transform", "controlled-shifts"],
    [r"the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution",
     r"Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution"])

add("gaussian-resampling", "Gaussian resampling",
    "Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through a Fourier transform of a larger power-of-two length t, using Gaussian-weighted interpolation maps A and B₀.",
    ["multidim-transform"],
    [r"Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform.",
     r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA"])

add("fixed-point-disk-grid", "Fixed-point disk-grid arithmetic and contractions",
    "Complex numbers stored as signed two's-complement integers scaled by 2^{-p} inside the unit disk; truncation Q_p toward zero costs error below √2·2^{-p}, and contractions never increase the sup norm so errors add up predictably.",
    ["complex-numbers"],
    [r"\mathbb D_p=\{2^{-p}(a+ib):a,b\in\mathbb Z,\ a^2+b^2\leq 2^{2p}\}",
     r"\|Q_p z-z\|_\infty<\sqrt2\,2^{-p}",
     r"Each normalized Fourier transform above is a contraction"])

add("negacyclic-ring", "Polynomial ring modulo y^r + 1",
    "The ring of complex polynomials of degree below r with y^r = −1, where multiplication by a power of y is a signed shift of the coefficient list.",
    ["polynomials", "complex-numbers"],
    [r"\mathcal R_r=\mathbb C[y]/(y^r+1)",
     r"Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs; consequently it is an isometry for this norm."],
    title=r"Polynomial ring modulo $y^r + 1$",
    symbols=[("y", "ring variable", "the formal variable of the polynomials, subject to y^r = -1.", "direct"),
             ("r", "record length", "the number of complex coefficients in a polynomial record, a power of two.", "count")])

add("synthetic-transform", "Synthetic Fourier transform modulo y^r + 1",
    "A Fourier transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so twiddle multiplications are signed coefficient shifts; it satisfies a character-cancellation identity despite zero divisors.",
    ["negacyclic-ring", "dft-cyclic-convolution", "multidim-transform"],
    [r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$.",
     r"The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$."],
    title=r"Synthetic Fourier transform modulo $y^r + 1$",
    symbols=[("y", "ring variable", "the formal variable of the polynomial ring, subject to y^r = -1.", "direct"),
             ("r", "record length", "the number of complex coefficients in a polynomial record, a power of two.", "count")])

add("butterfly-layers", "Radix-2 butterfly layers and stored frequency order",
    "Decimation in frequency: each level combines entries k and k+t/2 by the two-point butterfly H₀ and a twiddle monomial, leaving frequencies stored in bit-reversed order, which the opposite transform consumes directly.",
    ["synthetic-transform"],
    [r"the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for",
     r"the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$"])

add("coefficient-twist", "Twist from cyclic to negacyclic convolution",
    "Multiplying coefficient k by ζ^k with ζ = e^{πi/r} is a ring isomorphism from the cyclic ring (x^r = 1) to the ring modulo y^r + 1, so its negative wrap yields the cyclic wrap after untwisting.",
    ["negacyclic-ring", "dft-cyclic-convolution"],
    [r"A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$",
     r"Untwisting therefore recovers the cyclic coefficient with the correct sign."])

add("nlogn-subroutine", "Established n log n multiplier as a subroutine",
    "The Harvey–van der Hoeven O(N log N) integer multiplier is used as an ordinary subroutine on short inputs and does not invoke the improved theorem recursively.",
    ["big-o", "fixed-tape-model"],
    [r"Calls to the established $O(n\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively.",
     r"Harvey and van der Hoeven proved the unconditional $O(n\log n)$ bound"])

add("signed-kronecker-packing", "Signed Kronecker packing of polynomial products",
    "Multiplying two polynomial records exactly by evaluating their integer-coefficient parts at a large power of two, multiplying the resulting integers with the established multiplier, and recovering signed coefficients by centered carries.",
    ["negacyclic-ring", "polynomials", "nlogn-subroutine"],
    [r"Signed coefficient packing is a form of Kronecker substitution",
     r"Multiply the four pairs of absolute values using the established multiplier and restore each product's sign."])

add("bluestein-chirp", "Bluestein's chirp identity",
    "Rewrites a Fourier transform as a pointwise phase multiplication, a cyclic convolution with a chirp array, and another pointwise phase multiplication.",
    ["dft-cyclic-convolution", "multidim-transform"],
    [r"Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution",
     r"a_{\boldsymbol j} =\exp\left(-\pi i\sum_{i=1}^d\frac{s_i j_i^2}{t_i}\right)"])

add("resampling-no-sort", "Resampling with the permutations left in the transform",
    "The tensor form of Gaussian resampling in which the source and target coordinate permutations R and Q stay inside the transform identity, so they need not be executed as separate sorts.",
    ["gaussian-resampling", "fixed-point-disk-grid", "multidim-transform"],
    [r"There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying",
     r"RF_{\boldsymbol s} =2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A",
     r"We retain both permutations in the transform formula and compute that formula directly."])

add("chirp-permutation-cancel", "Chirp identity and source-permutation cancellation",
    "A chirp-convolution formula for Q·F_t that leaves the target permutation unexecuted, together with the fact that the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform.",
    ["bluestein-chirp", "resampling-no-sort"],
    [r"The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.",
     r"The second identity shows how the retained source permutation $R$ cancels when computing a convolution."])

# ---- tape side
add("triple-gadget", "Three-element subset intersection gadget",
    "Gather, scatter and side-injection updates indexed by three-element subsets of a 100-element set, whose coefficients depend on intersection size; side wires cancel the unwanted intersection-one (or intersection-zero/two) contributions.",
    [],
    [r"The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.",
     r"In the bit construction, scalars lie in $\mathbb F_2$, and $S,T$ are neighbors when $|S\cap T|=1$."])

add("bank-exchange-network", "Linear network that exchanges two banks and restores scratch values",
    "A fixed network of linear gates with three stages whose net effect is (X, Y) ↦ (−Y, X) on two banks, restoring every auxiliary scratch value whatever its initial contents.",
    ["triple-gadget"],
    [r"Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.",
     r"For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged."])

add("frames", "Frames and the common-frame identity",
    "An invertible operator D_v on each wire's address-indexed array at every network vertex; since gates are pointwise and linear they commute with a shared frame, so the whole network implements D_out S D_in⁻¹ and only edge changes D_v D_u⁻¹ cost anything.",
    ["bank-exchange-network", "stream-arrays"],
    [r"We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$.",
     r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}"])

add("bilinear-orthogonal", "Orthogonal complements and projections in a bilinear space",
    "In a vector space with a nondegenerate symmetric bilinear form, a subspace U has an orthogonal complement U⊥ and a projection P_U along it; the residual of nested subspaces has dimension equal to the difference of their dimensions.",
    [],
    [r"For a nondegenerate rational subspace $U\subset\mathcal F$, write $P_U$ for the projection onto $U$ along $U^\perp$.",
     r"the \emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one"])

add("subspace-labels", "Nested subspace labels and the rank saving",
    "Subspaces of an m-dimensional space attached to gates and terminals so adjacent labels are nested; edge dimension changes count the smaller operations needed, and their total s is strictly below W·m.",
    ["frames", "triple-gadget", "bilinear-orthogonal"],
    [r"The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.",
     r"A label is a nondegenerate subspace of a fixed bilinear space.",
     r"Orthogonality of the corresponding indicator vectors permits the subspace assignments."])

add("triangular-factorization", "Lower-triangular rank factorization",
    "Every rational square matrix of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation matrix with exactly a ones (a Bruhat factorization with coordinate order reversed).",
    [],
    [r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
     r"The required factorization is the Bruhat factorization for arbitrary matrices, with coordinate order reversed"])

add("matrix-shear", "Cost of a rational matrix shear",
    "The address update (H, D) ↦ (H + AD, D) over Z/q^b is performed with exactly rank(A) interchanges of pairs of b-digit fields plus linear extra work, using triangular factors and controlled shifts.",
    ["triangular-factorization", "controlled-shifts"],
    [r"can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.",
     r"D_j\leftarrow D_j+H_i,\qquad (H_i,D_j)\leftarrow(D_j,H_i),\qquad D_j\leftarrow H_i-D_j."])

add("power-width-interchange", "Power-width chunk interchange in O(Ve^τ) time",
    "Recursively interchanges two chunks of e = m^k digits by running the bank-exchange network on W role streams of volume V/W, each edge costing rank-many smaller interchanges; since s/W < m^τ the cost per volume is O(e^τ).",
    ["matrix-shear", "subspace-labels", "bank-exchange-network", "frames", "stream-arrays"],
    [r"The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes.",
     r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).",
     r"This strict inequality is the source of the power saving."],
    title=r"Power-width chunk interchange in $O(Ve^\tau)$ time",
    symbols=[("V", "stored bit volume", "the number of data bits stored in the array.", "count"),
             ("e", "chunk width", "the number of radix digits in each of the two interchanged chunks, a power of a fixed integer m.", "count"),
             ("\\tau", "interchange exponent", "a fixed rational constant strictly between 0 and 1.", "direct")])

add("chunk-swap", "Chunk interchange in O(Vu^τ) time",
    "Interchanges two disjoint address chunks of u bits in any bit array in O(V u^τ) steps for a fixed τ < 1, by padding rows and splitting the width in base m into power-width pieces; intermediate steps are XOR combinations but the final effect is an exact permutation.",
    ["power-width-interchange"],
    [r"in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$",
     r"Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.",
     r"Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data."],
    title=r"Chunk interchange in $O(Vu^\tau)$ time",
    symbols=[("V", "stored bit volume", "the number of data bits stored in the array.", "count"),
             ("u", "chunk width", "the number of bits in each of the two interchanged address chunks.", "count"),
             ("\\tau", "interchange exponent", "a fixed rational constant strictly below 1, namely 1 - 2^{-50}.", "direct")])

add("phase-kernel-network", "Two-point kernel C and the complex phase network",
    "The Gaussian-dyadic two-point kernel C = H S H = aI + bX (a = (1+i)/2, b = (1−i)/2) satisfies H₀ = b S C S; the complex bank-exchange network with binary labels makes C^{⊗m} on every role from products of translation kernels, one per residual basis vector.",
    ["frames", "subspace-labels", "butterfly-layers"],
    [r"C=H\mathsf SH=aI+bX",
     r"Its phase-frame difference $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual.",
     r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D"])

add("packed-selected-bits", "Packed XOR of selected bits across address chunks",
    "A binary row addition y ← y ⊕ x on the selected bit of each of f chunks at once, done by a constant number of cyclic shifts of whole chunk ranges followed by deterministic repair of a small explicit set of bad addresses, using a third chunk as restored temporary space.",
    ["chunk-swap", "controlled-shifts"],
    [r"We implement a binary row addition on corresponding selected bits in two address chunks.",
     r"The correction depends only on addresses, so the time bound is worst-case over all payloads."])

add("simultaneous-butterfly-layer", "Simultaneous butterfly layer in O(Vd^λ') time",
    "Applies the normalized butterfly H₀ to one bit position in each of d address chunks of polynomial records in one pass, exactly in Gaussian dyadics followed by a single truncation, in O(V d^λ') for a fixed λ' < 1 instead of d whole-array passes.",
    ["phase-kernel-network", "packed-selected-bits", "fixed-point-disk-grid", "butterfly-layers", "power-width-interchange"],
    [r"coefficient order, and component format in $O(Vd^{\lambda'})$ time",
     r"whereas separate butterfly factors would require $D$ whole-array passes",
     r"The procedure evaluates the entire layer exactly before this final truncation."],
    title=r"Simultaneous butterfly layer in $O(Vd^{\lambda'})$ time",
    symbols=[("V", "stored bit volume", "the number of data bits stored in the array of records.", "count"),
             ("d", "axis count", "the number of equal-width address chunks (transform axes) whose selected bit is butterflied simultaneously.", "count"),
             ("\\lambda'", "layer exponent", "a fixed rational constant strictly below 1, namely 1 - 2^{-54}.", "direct")])

add("transform-layout", "Layout and cost of the synthetic transform",
    "A positional layout permutation puts the selected bits of all axes at a common offset in K-bit chunks so each transform round is one simultaneous layer; the forward transform keeps its output order for the pointwise product and the opposite transform.",
    ["synthetic-transform", "butterfly-layers", "simultaneous-butterfly-layer", "chunk-swap"],
    [r"The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes",
     r"The forward procedure may retain its output layout for a pointwise product and the following opposite procedure."])

add("ring-convolution", "Convolution over the polynomial ring from the retained layout",
    "Normalized convolution of arrays over the ring modulo y^r + 1: two forward synthetic transforms, pointwise ring products by signed packing, then the opposite transform consuming the same frequency order, with error O(M ℓ 2^{-p}).",
    ["transform-layout", "signed-kronecker-packing"],
    [r"Perform both forward transforms and retain their common $LB$ order.",
     r"\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}"])

add("source-transform", "Source transform via resampling, chirp and ring convolution",
    "The computed procedure for a source Fourier transform of prime lengths: Gaussian maps A, then a chirp transform evaluated by a twisted ring convolution, then B₀ and an exact power-of-two scale, with exact counterpart R F_s.",
    ["resampling-no-sort", "chirp-permutation-cancel", "ring-convolution", "coefficient-twist"],
    [r"write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform",
     r"\mathcal M_{\mathbb C}(f,g) :=D_-\iota^{-1} \mathcal M_r(\iota D_+f,\iota D_+g)"])

add("parameter-choice", "Choice of sizes, precision and prime axis lengths",
    "Fixing b = ⌈log₂ n⌉, precision p = 6b, axis count d = ⌊b^ε⌋, padded size T ≈ n/b, record length r, power-of-two axis lengths t_i, and distinct odd prime lengths s_i just below t_i, so that Tp = Θ(n) and all hypotheses of the interfaces hold.",
    ["crt-axis-map", "gaussian-resampling", "fixed-point-disk-grid"],
    [r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor",
     r"We may therefore choose distinct odd primes satisfying",
     r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16}"])

add("exact-recovery", "Exact recovery: scaling, rounding and carries",
    "Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2 so rounding gives exact convolution coefficients, then propagating radix-2^b carries to the 2n-bit product.",
    ["fixed-point-disk-grid", "radix-digit-convolution", "source-transform"],
    [r"proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product",
     r"Propagate radix-$2^b$ carries in increasing coefficient order."])

add("multiplication-algorithm", "The multiplication algorithm",
    "Split into radix digits, map by Φ to prime axes, take two source transforms, multiply pointwise, apply the opposite-sign transform with the two scalings by S, round, undo Φ, and propagate carries to output the 2n-bit product.",
    ["crt-axis-map", "source-transform", "exact-recovery", "parameter-choice", "radix-digit-convolution"],
    [r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$.",
     r"The two occurrences of $S$ in this algorithm undo different normalizations."])

add("cost-accounting", "Cost accounting and the saving exponent κ",
    "A table of costs divided by Tp, each at most p^{1−2κ} thanks to the slack in the chosen exponents (seven dominant margins, the smallest 2^{-181} = 2κ), giving O(n (log n)^{1−κ}) overall.",
    ["multiplication-algorithm", "chunk-swap", "simultaneous-butterfly-layer", "transform-layout", "resampling-no-sort"],
    [r"Each of the seven displayed powers is at most $1-2\kappa$ by",
     r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
     r"This strict inequality is the source of the power saving."],
    title=r"Cost accounting and the saving exponent $\kappa$",
    symbols=[("\\kappa", "saving exponent", "the fixed constant 2^{-182} by which the power of the logarithm is reduced below 1.", "direct")])

add("main-theorem", "Multiplying n-bit integers in O(n (lg n)^(1−κ)) time",
    "A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, using fast address-chunk interchange and simultaneous butterfly layers to speed synthetic transforms inside a Gaussian-resampling multiplication.",
    ["multiplication-algorithm", "cost-accounting", "n-log-n-conjecture", "fixed-tape-model"],
    [r"We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time",
     r"T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)"],
    title=r"Multiplying $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time",
    symbols=[("n", "input length", "the number of bits in each of the two integers being multiplied.", "count"),
             ("\\kappa", "saving exponent", "the fixed constant 2^{-182} by which the power of the logarithm is reduced below 1.", "direct")])

ans = dict(target="main-theorem", concepts=C)

# validate
ids = {c["id"] for c in C}
assert len(ids) == len(C)
bad = 0
for c in C:
    for r in c["requires"]:
        assert r in ids, (c["id"], r)
    if c["known"]:
        assert c["requires"] == []
    elif not c["evidence"]:
        print("no evidence", c["id"]); bad += 1
    for e in c["evidence"]:
        if norm(e["quote"]) not in srcn:
            print("MISSING QUOTE", c["id"], e["quote"]); bad += 1
# cycle check
state = {}
def dfs(u):
    if state.get(u) == 1: raise Exception("cycle " + u)
    if state.get(u) == 2: return
    state[u] = 1
    for v in next(c for c in C if c["id"] == u)["requires"]: dfs(v)
    state[u] = 2
for i in ids: dfs(i)
if bad: sys.exit(1)
json.dump(ans, open(ROOT + "/exegenius/tasks/0001-extract.answer.json", "w"), indent=1, ensure_ascii=False)
print("ok", len(C))
