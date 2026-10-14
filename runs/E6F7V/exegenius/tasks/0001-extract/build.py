import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7"
src = open(ROOT + "/sources/paper.tex").read()
norm = re.sub(r"\s+", " ", src)

C = []
def add(id, name, gloss, requires, quotes=(), known=False, aliases=(), title=None, symbols=None):
    d = dict(id=id, name=name, aliases=list(aliases), gloss=gloss, requires=list(requires),
             known=known, evidence=[dict(source="paper", quote=q) for q in quotes])
    if title:
        d["title"] = title
        d["symbols"] = symbols
    C.append(d)

def sym(symbol, name, meaning, relation):
    return dict(symbol=symbol, name=name, meaning=meaning, relation=relation)

# known
add("big-o", "Big-O notation", "Asymptotic upper bounds such as O(f(n)) on running time.", [], known=True)
add("polynomials", "Polynomials", "Sums of coefficients times powers of a variable, with addition and multiplication.", [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a + bi with i² = −1, with modulus, conjugation and the unit-modulus numbers e^{iθ}.", [], known=True)
add("turing-machine", "Multitape Turing machine", "A finite-state machine with several tapes, each with a head that reads and writes one cell and moves one cell per step; running time counts steps.", [], known=True)

# background
add("nlogn-history", "Multiplication complexity and the n log n conjecture",
    "Schönhage and Strassen multiplied n-bit integers in O(n log n log log n) on multitape machines and conjectured that n log n is optimal; later work (Fürer, then Harvey–van der Hoeven) reached O(n log n), and the paper's theorem breaks the conjectured optimum.",
    ["big-o", "turing-machine"],
    [r"proposed $n\log n$ as the optimal order of growth",
     r"Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper",
     r"Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can"])
add("fixed-tape-model", "Fixed finite-alphabet multitape model",
    "The cost model of the paper: one machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where a step touches one cell per tape; extra tracks or work tapes change time only by a constant factor.",
    ["turing-machine"],
    [r"A machine has one fixed finite alphabet and one fixed finite number of",
     r"Fixed tracks and finitely"])
add("established-multiplier", "Established O(n log n) multiplier (subroutine)",
    "The Harvey–van der Hoeven O(N log N) integer multiplier, used as a black-box subroutine on short operands (never recursively on the improved algorithm).",
    ["nlogn-history", "fixed-tape-model"],
    [r"To multiply the polynomial records, we use the fixed-tape integer",
     r"Calls to the established $O(n\log n)$ multiplier are ordinary subroutine"])
add("stream-operations", "Array order and elementary stream operations",
    "Arrays are stored in lexicographic address order on a tape; digit moves, digit swaps, pointwise maps on split streams and cyclic splitting of rows into W streams all take O(V) steps for volume V on fixed tapes.",
    ["fixed-tape-model"],
    [r"Each of the following operations on an array of",
     r"An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in"])
add("controlled-shifts", "Controlled shifts",
    "A target address field is cyclically shifted (or multiplied by a fixed unit modulo q^b) by an offset computed from control fields that precede it, in O(V) time by splitting each fibre in two pieces and merging them in reverse order.",
    ["stream-operations"],
    [r"Suppose a target field $y\in[Q]$ follows its control fields, each control",
     r"y\longmapsto y+a(\text{controls})\pmod Q"])

# Fourier background
add("dft", "Discrete Fourier transform",
    "The map u ↦ (1/q)Σ_j u_j e^{−2πi jk/q} that evaluates a length-q sequence at the q-th roots of unity; it is a contraction in the max-modulus norm and has an inverse of the same shape with the opposite sign.",
    ["complex-numbers", "polynomials"],
    [r"(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}",
     r"Each normalized Fourier transform above is a contraction, since each"])
add("cyclic-convolution", "Cyclic convolution and the convolution theorem",
    "The product of two polynomials modulo x^q − 1 (indices added mod q); the Fourier transform turns it into a pointwise product, so convolution = transform, multiply pointwise, inverse transform.",
    ["dft", "polynomials"],
    [r"The normalized convolution rule is",
     r"cyclic convolution on the product of the coordinate groups and a dot"])
add("multidimensional-dft", "Multidimensional transforms and convolutions",
    "A tensor product of one-dimensional transforms (or convolutions) along several axes of a box of size t₁×…×t_D, applied one axis at a time.",
    ["cyclic-convolution"],
    [r"F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm,",
     r"it replaces the Fourier transforms needed for"])
add("radix-digit-convolution", "Integer multiplication as radix-digit convolution",
    "Splitting each n-bit input into radix-2^b digits turns the product into a convolution of short digit polynomials, padded so that no cyclic wraparound occurs, followed by a left-to-right carry propagation that yields the 2n-bit product.",
    ["cyclic-convolution", "polynomials"],
    [r"Write the two inputs as polynomials in $2^b$, each with",
     r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
     r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,"])
add("crt-map", "Chinese-remainder map to prime cyclic axes",
    "For pairwise coprime lengths s_i with product S, the algebra isomorphism x ↦ Π x_i^{μ_i} turns one cyclic convolution of length S into a multidimensional cyclic convolution on prime axes; on tape it is a sequence of prefix-controlled cyclic shifts.",
    ["multidimensional-dft", "controlled-shifts", "radix-digit-convolution"],
    [r"Agarwal and Cooley used the Chinese remainder",
     r"x\longmapsto\prod_i x_i^{\mu_i}"])
add("bluestein-chirp", "Bluestein chirp identity",
    "A Fourier transform can be written as a pointwise phase (chirp) multiplication, a cyclic convolution with a chirp array, and another chirp multiplication; here it also absorbs the frequency permutation Q.",
    ["cyclic-convolution", "multidimensional-dft"],
    [r"The chirp identity below performs the frequency change",
     r"Bluestein's chirp identity converts the middle transform,"])

# numerics
add("fixed-point-disk", "Fixed-point complex coefficients and truncation",
    "Complex numbers stored as 2^{−p}(a+ib) with integer a, b inside the unit disk, written as signed two's-complement words; Q_p truncates real and imaginary parts toward zero to this grid, with error below √2·2^{−p} and no increase of norm.",
    ["complex-numbers"],
    [r"\mathbb D_p=\{2^{-p}(a+ib):a,b\in\mathbb Z,\ a^2+b^2\leq 2^{2p}\}",
     r"\|Q_p z-z\|_\infty<\sqrt2\,2^{-p},"])
add("error-accounting", "Contractions and error accounting",
    "Normalized transforms and averaged convolutions are contractions in the max-modulus norm, so errors of composed approximate steps add (bilinear steps add the two operand errors) and a final error below 1/2 permits rounding to integers.",
    ["fixed-point-disk"],
    [r"adds their errors: at each step, insert the exact map at the computed",
     r"\|\mathcal M_r(f,g)\|_\infty",
     r"For a bilinear contraction $\mathcal M$, replacing its operands gives"])
add("gaussian-resampling", "Gaussian resampling",
    "Harvey–van der Hoeven technique that expresses a Fourier transform of coprime length s through a transform of the larger length t (a power of two) using Gaussian-weighted contractions A and B₀ and a Neumann-series inverse; the sorting permutations stay inside the transform identity.",
    ["multidimensional-dft", "error-accounting", "big-o"],
    [r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA.",
     r"Its usual implementation sorts twice on each"])
add("permutation-cancellation", "Retained permutations and their cancellation",
    "The source permutation R left in the resampling identity cancels across two forward transforms, the pointwise product and the opposite-sign transform, giving R F_s⁺[(R F_s u)·(R F_s v)] = (u*v)/S².",
    ["gaussian-resampling", "bluestein-chirp"],
    [r"retained source permutation $R$ cancels when computing a convolution.",
     r"(RF_{\boldsymbol s}^+)"])
add("padded-box-tensor-resampling", "Tensor resampling on the padded box",
    "Resampling in d dimensions applies the one-dimensional maps line by line on a zero-padded box of T = Πt_i entries, exposing each axis with address-chunk interchanges, at total cost O(d T p^{3/2+δ} α) plus O(Tp d²(1+ℓ^τ)) for movement.",
    ["gaussian-resampling", "arbitrary-width-interchange"],
    [r"If each $t_i\in\{r/2,r\}$ with $r=2^\ell$, the array is kept in the",
     r"RF_{\boldsymbol s}"])

# ring and synthetic transforms
add("negacyclic-ring", "Polynomial ring modulo y^r + 1",
    "Complex polynomials of degree below r with multiplication reduced by y^r = −1; multiplying by a power of y just rotates the coefficient list with sign changes, so powers of y act as roots of unity.",
    ["polynomials", "complex-numbers"],
    [r"\mathcal R_r=\mathbb C[y]/(y^r+1),",
     r"Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes"],
    aliases=["negacyclic ring"],
    title=r"Polynomial ring modulo $y^r + 1$",
    symbols=[sym("y", "ring variable", "The formal variable of the polynomials, satisfying y^r = −1.", "direct"),
             sym("r", "coefficient count", "The number of complex coefficients of each polynomial, a power of two.", "count")])
add("butterfly", "Two-point butterfly",
    "The map H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of values, the basic step of a radix-2 fast Fourier transform; applied to a coordinate bit it is a halving contraction.",
    ["dft"],
    [r"H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr)"])
add("synthetic-transform", "Synthetic polynomial transform",
    "A Fourier transform over the negacyclic ring using roots ω_t = y^{2r/t} (signed shifts), computed by decimation-in-frequency rounds of butterflies and monomial twiddles y^E; it is a contraction and satisfies character cancellation despite zero divisors.",
    ["negacyclic-ring", "butterfly", "multidimensional-dft"],
    [r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$.",
     r"The ring has zero divisors, so we verify character cancellation",
     r"Consequently the individual axis steps may be grouped as a parallel"])
add("retained-frequency-order", "Retained (bit-reversed) frequency order",
    "The recursion writes frequencies in bit-reversed slots; both forward transforms keep this order through the pointwise product and the opposite transform consumes it, so no sort is executed.",
    ["synthetic-transform"],
    [r"the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$.",
     r"retain the same frequency order through their pointwise product"])
add("phase-twist", "Coefficient twist from cyclic to negacyclic",
    "Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps ℂ[x]/(x^r − 1) isomorphically onto the negacyclic ring, turning the last cyclic axis into a polynomial ring; its negative wrap gives the cyclic wrap after untwisting.",
    ["negacyclic-ring", "cyclic-convolution"],
    [r"\Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R,",
     r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."])
add("signed-packing-product", "Signed packing of ring products",
    "A signed form of Kronecker substitution evaluates polynomial records at 2^{4p}, multiplies the resulting integers with the established multiplier, extracts coefficients, wraps negacyclically and truncates, giving a ring product in O(rp log(rp)).",
    ["negacyclic-ring", "established-multiplier", "fixed-point-disk"],
    [r"The reduction is a signed form of Kronecker substitution; compare",
     r"One can compute the exact Gaussian integer"])

# linear networks
add("linear-algebra-prelims", "Subspaces, orthogonality and rank",
    "Vector subspaces over the rationals or over the two-element field, bilinear forms, orthogonal complements, nondegeneracy, projections, matrix rank and tensor products.",
    [],
    [r"A label is a nondegenerate subspace of a fixed bilinear space."])
add("xor-linear-network", "Linear network exchanging two banks with restored scratch values",
    "A fixed network of pointwise linear gates on wires (data banks X, Y, scratch and central wires) that in three stages maps (X,Y) to (−Y,X) and returns every scratch wire to its arbitrary initial value, as in transparent computation.",
    ["linear-algebra-prelims"],
    [r"Each procedure arises from its own fixed linear network that exchanges two",
     r"(X_a,Y_a)\longmapsto(-Y_a,X_a)",
     r"This cancellation of arbitrary initial scratch values is a linear"])
add("frames", "Frames: changing the representation along a network",
    "An invertible operator D_v on an array chosen at each source, gate and sink; every edge applies D_vD_u^{-1}, a common frame commutes with the pointwise linear gate, so the network implements D_out S D_in^{-1} and the endpoint frames fix the operator on every role.",
    ["xor-linear-network"],
    [r"At each source, gate and sink $v$, assign an invertible $R$-linear operator",
     r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}."])
add("subset-labels", "Subspace labels from three-element subsets",
    "Frankl–Wilson style construction: indicator vectors of three-element subsets of [100] give intersection-size inner products; tensor cubes of these lines label gates by nested nondegenerate subspaces so that edge changes are small orthogonal residuals.",
    ["linear-algebra-prelims", "xor-linear-network"],
    [r"three-element subsets: gather and scatter create coefficients depending",
     r"\langle t_S,t_T\rangle=|S\cap T|-1,"])
add("rank-deficit", "Rank deficit s < W m",
    "The sum s of ranks of all edge differences (the number of smaller calls) is strictly less than W·m, where W is the number of wires and m the label-space dimension; the deficit comes from the loss L on decreasing edges being below N/2.",
    ["subset-labels", "frames"],
    [r"number $s$ of smaller calls satisfies $s<Wm$.",
     r"\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad"])
add("power-saving-recurrence", "Recursive power saving from the rank deficit",
    "A call at parameter m·f makes s calls at parameter f on streams of volume V/W, giving F_k ≤ (s/W)F_{k−1}+O(1) with s/W < m, so the normalized cost is O(parameter^τ) for some τ < 1.",
    ["rank-deficit"],
    [r"is the source of the power saving.",
     r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."])
add("lower-triangular-factorization", "Lower-triangular (Bruhat) factorization",
    "Every rational matrix of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.",
    ["linear-algebra-prelims"],
    [r"A=E_1\Pi E_2,",
     r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"])
add("bit-shear-interface", "Address shear from the bit network",
    "Using the permutation frame Φ_M that moves the entry at (H,D) to (H+MD,D), the bit network's endpoint matrices differ by the identity, so it implements the shear H ← H+D on every role, with total edge rank s_b < W_b·m.",
    ["frames", "rank-deficit"],
    [r"M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m",
     r"at $(H,D)$ to $(H+MD,D)$, leaving the other address fields unchanged."])
add("matrix-shear-cost", "Cost of a rational matrix shear",
    "For a rational matrix A of rank a, the shear (H,D) ↦ (H+AD,D) over ℤ/q^bℤ is done with exactly a interchanges of b-digit fields and O(V) other work, using triangular updates as controlled shifts.",
    ["lower-triangular-factorization", "controlled-shifts", "bit-shear-interface"],
    [r"(H,D)\longmapsto(H+AD,D)",
     r"can be performed with exactly $a$ interchanges of pairs of $b$-digit"])
add("power-width-interchange", "Recursive power-width address interchange",
    "Two address chunks of m^k digits are interchanged in O(V e^τ) by splitting rows into W role streams, running the bit network whose edges are shears (smaller interchanges), and finishing with D←D−H, H←H+D, D←H−D; a depth-first schedule on fixed tapes realizes the recursion.",
    ["matrix-shear-cost", "power-saving-recurrence", "stream-operations"],
    [r"The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every",
     r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"])
add("arbitrary-width-interchange", "Address-chunk interchange in time O(V u^τ)",
    "Exchanging two disjoint contiguous address fields of u bits (any width, any gaps, even one-bit payload) in O(V u^τ) for a fixed τ = 1 − 2^{−50} < 1, by peeling off high digits to make rows, padding, and splitting the width in base m; the intermediate steps are XOR combinations though the result is an exact permutation.",
    ["power-width-interchange"],
    [r"(p,h,g,d,z)\longmapsto(p,d,g,h,z)",
     r"The first procedure interchanges two disjoint contiguous address fields"],
    title=r"Address-chunk interchange in time $O(Vu^\tau)$",
    symbols=[sym("V", "stored bit volume", "The number of data bits stored in the array being rearranged.", "count"),
             sym("u", "chunk width", "The number of bits in each of the two interchanged address chunks.", "count"),
             sym("\\tau", "interchange exponent", "A fixed constant strictly below one (1 − 2^{−50}) bounding the growth of the cost with the chunk width.", "direct")])

# numerical network and butterfly layers
add("phase-frame-network", "Complex phase network and two-point kernels",
    "The same network over Gaussian dyadic values with binary labels and phase frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge change is a product of two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), and telescoping gives C^{⊗m} on every role with s_c < W_c·m kernel factors.",
    ["xor-linear-network", "frames", "subset-labels", "butterfly", "rank-deficit"],
    [r"\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}.",
     r"telescoping these phase frames gives $C^{\otimes m}$"])
add("packed-selected-bit-addition", "Packed selected-bit addition",
    "A binary row addition (XOR) of selected bits across many address chunks at once, done by a constant number of whole-chunk cyclic shifts using a third chunk of arbitrary contents as temporary storage, followed by a deterministic repair of an explicitly bounded set of exceptional addresses.",
    ["arbitrary-width-interchange", "controlled-shifts"],
    [r"We implement a binary row addition on corresponding selected bits in two",
     r"y_{j_i}\longleftarrow y_{j_i}\mathbin\oplus x_{j_i}"])
add("simultaneous-butterfly-layer", "Simultaneous butterfly layer in time O(V d^λ′)",
    "Applying H₀ at once to the same bit position of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) for fixed λ' < 1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase network, packed bit moves, exact Gaussian dyadic arithmetic and one final truncation.",
    ["phase-frame-network", "packed-selected-bit-addition", "arbitrary-width-interchange", "fixed-point-disk", "power-saving-recurrence", "butterfly"],
    [r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.",
     r"The procedure returns $Q_p(\mathcal H z)$ in the same array,",
     r"The second procedure applies"],
    title=r"Simultaneous butterfly layer in time $O(Vd^{\lambda'})$",
    symbols=[sym("V", "stored bit volume", "The number of data bits stored in the array of polynomial records.", "count"),
             sym("d", "axis count", "The upper bound on the number of address chunks (transform axes) whose selected bits are butterflied together.", "count"),
             sym("\\lambda'", "layer exponent", "A fixed constant strictly below one (1 − 2^{−54}) bounding the growth of the cost with the number of axes.", "direct")])
add("transform-layout", "Transform layout and cost",
    "A positional layout permutation L places the selected bits of all axes at a common offset in consecutive K-bit chunks (prefix moves plus chunk exchanges), so each round is one simultaneous layer; the forward and opposite transforms cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2 ℓ 2^{−p}.",
    ["simultaneous-butterfly-layer", "arbitrary-width-interchange", "synthetic-transform", "retained-frequency-order"],
    [r"The procedure constructs an explicit positional",
     r"exchanges of width-$K$ address chunks, even when the chunks are"])
add("synthetic-convolution", "Convolution from the retained transform layout",
    "Two forward synthetic transforms in layout order, a pointwise ring product divided by r, the opposite transform and an exact scaling by M compute the normalized convolution (f*g)/T over the negacyclic ring with error below √2 M(3ℓ+1)2^{−p}.",
    ["transform-layout", "signed-packing-product", "multidimensional-dft", "error-accounting"],
    [r"\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}.",
     r"Perform both forward transforms and retain their common $LB$ order."])
add("source-transform", "Computed source transform",
    "The source Fourier transform R F_s is computed as 2^γ B₀ Q F_t A: Gaussian expansion on each line, the chirp transform (a twisted synthetic convolution) and Gaussian compression, then a power-of-two scaling, all with tracked disk margins and errors.",
    ["padded-box-tensor-resampling", "bluestein-chirp", "phase-twist", "synthetic-convolution"],
    [r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A",
     r"Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and"])
add("prime-axis-parameters", "Parameter choices and prime axis lengths",
    "Fixed parameters b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^{⌈(log₂T)/d⌉}, axes of length r/2 or r, and distinct primes s_i just below t_i found by deterministic search, with ε = 2^{−75}, c = 2^{−56}, λ' = 1−2^{−54}, κ = 2^{−182}.",
    ["crt-map", "gaussian-resampling", "synthetic-transform"],
    [r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,",
     r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}.",
     r"contains at least $\eta x/(2\log x)$ primes."])
add("exact-recovery", "Precision budget and exact recovery",
    "Scale bookkeeping (the two factors S) and the error bound 448 b 2^{−b+γ} < 1/2 show that each recovered convolution coefficient rounds to the true integer, which is below 2^{3b}, so carries give the exact product.",
    ["source-transform", "permutation-cancellation", "radix-digit-convolution", "error-accounting"],
    [r"The true coefficients are real integers.",
     r"<448b\,2^{-b+\gamma}"])
add("multiplication-algorithm", "The multiplication algorithm",
    "Digit extraction, the address map Φ to prime axes, two source transforms, a truncated pointwise product, the opposite-sign transform, rescaling by S and 2^{2b+4}, rounding, inverse address map and carry propagation, producing the 2n-bit product.",
    ["crt-map", "source-transform", "permutation-cancellation", "exact-recovery", "radix-digit-convolution", "prime-axis-parameters"],
    [r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain",
     r"The two occurrences of $S$ in this algorithm undo different"])
add("cost-accounting", "Complete time bound and power margins",
    "Dividing costs by V = Tp gives seven dominant terms (butterfly rounds, chunk exchanges, simultaneous layers, CRT layouts, Gaussian lines, chirps, packed products) each at most p^{1−2κ}; the smallest margin is 2^{−181} = 2κ, which absorbs log factors and gives O(n(log n)^{1−κ}).",
    ["multiplication-algorithm", "simultaneous-butterfly-layer", "transform-layout", "arbitrary-width-interchange", "padded-box-tensor-resampling", "signed-packing-product"],
    [r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
     r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})"])
add("main-theorem", "Integer multiplication in O(n (lg n)^(1−κ)) time",
    "One deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model; the saving comes from faster address interchange and butterfly layers inside a Gaussian-resampling, Bluestein, synthetic-transform reduction.",
    ["multiplication-algorithm", "cost-accounting", "nlogn-history"],
    [r"We give a deterministic algorithm that multiplies two $n$-bit integers",
     r"T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right),"],
    title=r"Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time",
    symbols=[sym("n", "input length", "The number of bits in each of the two integers being multiplied.", "count"),
             sym("\\kappa", "saving exponent", "The fixed constant 2^{-182} by which the power of lg n is lowered below one.", "direct")])

ids = {c["id"] for c in C}
assert len(ids) == len(C)
bad = 0
for c in C:
    for r in c["requires"]:
        if r not in ids: print("missing req", c["id"], r); bad += 1
    if not c["known"] and not c["evidence"]: print("no evidence", c["id"]); bad += 1
    for e in c["evidence"]:
        q = re.sub(r"\s+", " ", e["quote"]).strip()
        if q not in norm: print("QUOTE NOT FOUND", c["id"], repr(e["quote"])); bad += 1
# cycle check
state = {}
def dfs(x):
    if state.get(x) == 1: raise SystemExit("cycle at " + x)
    if state.get(x) == 2: return
    state[x] = 1
    for r in next(c for c in C if c["id"] == x)["requires"]: dfs(r)
    state[x] = 2
for i in ids: dfs(i)
out = ROOT + "/exegenius/tasks/0001-extract.answer.json"
json.dump(dict(target="main-theorem", concepts=C), open(out, "w"), indent=1)
print("bad", bad, "concepts", len(C))
