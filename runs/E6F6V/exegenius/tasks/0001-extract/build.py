import json, re, sys
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6"
src = open(ROOT + "/sources/paper.tex", encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s)
nsrc = norm(src)

C = []
def add(id, name, gloss, requires, evidence=(), known=False, aliases=(), title=None, symbols=None):
    d = {"id": id, "name": name, "aliases": list(aliases), "gloss": gloss,
         "requires": list(requires), "known": known,
         "evidence": [{"source": "paper", "quote": q} for q in evidence]}
    if title:
        d["title"] = title
        d["symbols"] = symbols
    C.append(d)

# Known
add("big-o", "Big-O notation", "Asymptotic upper bounds on running time such as O(n log n).", [], known=True)
add("polynomials", "Polynomials", "Sums of coefficients times powers of a variable, with addition and multiplication.", [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a + bi with i² = −1, including roots of unity and modulus.", [], known=True)
add("turing-machines", "Turing machines and tapes", "Machines with a finite control reading and writing symbols on tapes, one cell at a time.", [], known=True)

add("multitape-streams", "Fixed-tape model and elementary stream scans",
    "The fixed-alphabet, fixed-number-of-tapes machine model in which arrays are streams in lexicographic order, and splitting, merging, digit moves and row splits cost O(V) for volume V.",
    ["turing-machines", "big-o"],
    ["A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.",
     "is the number of stored data bits",
     "Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes"])

add("controlled-shifts", "Controlled cyclic shifts and rational scalings",
    "Updating a target address field by an offset computed from earlier control fields (a cyclic rotation of blocks), or multiplying it by a unit modulo q^b, in O(V) time.",
    ["multitape-streams"],
    ["Suppose a target field $y\\in[Q]$ follows its control fields",
     "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values"])

add("hvdh-multiplier", "Established O(n log n) integer multiplier",
    "The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short inputs.",
    ["big-o", "turing-machines"],
    ["Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively.",
     "we use the fixed-tape integer multiplier of Harvey and van der Hoeven"])

add("convolution-multiplication", "Integer multiplication as convolution of radix digits",
    "Writing each integer as a polynomial in 2^b with small digit coefficients turns the product into a convolution of digit lists, with carries propagated afterwards.",
    ["polynomials"],
    ["Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
     "Write the two inputs as polynomials in $2^b$, each with"])

add("discrete-fourier-transform", "Normalized discrete Fourier transform and convolution theorem",
    "The transform F_q averaging inputs times roots of unity e^(−2πijk/q) (with inverse-sign version F_q⁺), which turns cyclic convolution into pointwise products up to a normalization.",
    ["complex-numbers", "convolution-multiplication"],
    ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}",
     "Each normalized Fourier transform above is a contraction"])

add("radix-two-fft", "Radix-two FFT butterflies",
    "The decimation-in-frequency recursion that pairs entries k and k+t/2, applies the two-point butterfly H₀ = ½[[1,1],[1,−1]] and a twiddle multiplication, then recurses on both halves, leaving outputs in bit-reversed order.",
    ["discrete-fourier-transform"],
    ["decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$",
     "the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$"])

add("negacyclic-ring", "Polynomial ring modulo y^r + 1",
    "Complex polynomials of degree below r with y^r = −1, so multiplying by a power of y is a signed cyclic shift of the coefficient list and powers of y serve as roots of unity.",
    ["polynomials", "complex-numbers"],
    ["is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two",
     "Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs"],
    title="Polynomial ring modulo $y^r + 1$",
    symbols=[
        {"symbol": "y", "name": "ring variable", "meaning": "The indeterminate of the polynomials, whose powers act as roots of unity because y^r = −1.", "relation": "direct"},
        {"symbol": "r", "name": "record length", "meaning": "The number of complex coefficients in a polynomial of the ring, a power of two.", "relation": "count"}])

add("synthetic-transforms", "Synthetic polynomial transforms",
    "Fourier-type transforms over the polynomial ring modulo y^r + 1 using ω_t = y^(2r/t) as root of unity, so twiddle multiplications are signed coefficient shifts; their forward and opposite versions invert each other up to 1/t.",
    ["negacyclic-ring", "radix-two-fft"],
    ["These are the synthetic polynomial transforms of Nussbaumer and Quandalle",
     "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$."])

add("fixed-point-precision", "Fixed-point disk-grid arrays and truncation",
    "Complex coefficients of modulus at most 1 stored with p fractional bits per component; truncation Q_p toward zero costs error below √2·2^(−p) and never increases the norm.",
    ["complex-numbers"],
    ["A disk array has norm at most one.",
     "let $Q_p$ truncate each real and imaginary coefficient part toward zero to this grid"])

add("signed-kronecker-packing", "Signed packing of polynomial products",
    "Computing products of ring polynomials exactly by evaluating each at a large power of two (signed Kronecker substitution), multiplying the resulting integers with the established multiplier and unpacking the coefficients.",
    ["negacyclic-ring", "hvdh-multiplier", "fixed-point-precision"],
    ["The reduction is a signed form of Kronecker substitution",
     "One can compute the exact Gaussian integer numerators of $fg$"])

add("linear-algebra-spaces", "Subspaces, orthogonal complements and projections",
    "Vector subspaces of a space with a nondegenerate bilinear form, orthogonal complements, orthogonal projections P_U and tensor products of such spaces.",
    [],
    ["For a nondegenerate rational subspace $U\\subset\\mathcal F$, write $P_U$ for the projection onto $U$ along $U^\\perp$."])

add("lower-triangular-factorization", "Lower-triangular (Bruhat) factorization",
    "Every m×m rational matrix A of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation matrix with exactly a ones.",
    ["linear-algebra-spaces"],
    ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])

add("bank-exchange-network", "Linear network exchanging two banks with restored scratch wires",
    "A fixed network of linear gates on wires (roles) that, using gather, scatter, copy and side-injection steps over triples, adds one bank into the other three times to exchange X and Y up to sign while restoring all scratch wires whatever their initial values.",
    [],
    ["We construct two fixed linear networks that exchange two banks of values while restoring every auxiliary value.",
     "For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged."])

add("frames-on-arrays", "Frames and the common-frame identity",
    "Replacing scalars by arrays, each vertex of the network gets an invertible operator (frame) on its array; since pointwise linear gates commute with a common frame, the network implements D_out S D_in^(−1) and each edge only changes frame.",
    ["bank-exchange-network", "linear-algebra-spaces"],
    ["We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$.",
     "Thus the intermediate frames cancel"])

add("subspace-labels", "Nested subspace labels with a rank deficit",
    "Nondegenerate subspaces built from three-element subsets are attached to gates and terminals so adjacent labels are nested; the orthogonal residual dimensions total fewer than W·m, which bounds the number of smaller calls.",
    ["bank-exchange-network", "frames-on-arrays", "linear-algebra-spaces"],
    ["A label is a nondegenerate subspace of a fixed bilinear space.",
     "The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$."])

add("recursive-power-saving", "Recursive power saving from s < Wm",
    "A call at parameter m·f makes s calls at parameter f on streams of volume V/W, so normalized cost satisfies F_k ≤ (s/W)F_(k−1)+O(1) with s/W < m^τ, giving cost O(V e^τ) with τ < 1.",
    ["subspace-labels", "big-o"],
    ["This strict inequality is the source of the power saving.",
     "A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$."])

add("bit-shear-interface", "Rational matrix interface and address shear",
    "Using frames Φ_M that move the entry at (H,D) to (H+MD,D), the bit network turns the exchange into the shear H ← H+D on every role, with total edge rank s_b < W_b·m.",
    ["subspace-labels", "frames-on-arrays"],
    ["the frame $\\Phi_M$ moves the array entry at $(H,D)$ to $(H+MD,D)$",
     "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates"])

add("matrix-shear-cost", "Cost of a rational matrix shear",
    "The address map (H,D) → (H+AD,D) over Z/q^b with A of rank a costs exactly a interchanges of b-digit fields plus O(V) work, by factoring A and using one swap per pivot.",
    ["lower-triangular-factorization", "controlled-shifts"],
    ["can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work"])

add("power-width-interchange", "Power-width chunk interchange with rows",
    "Interchanging two chunks of e = m^k digits by splitting rows into W role streams, running the bit network with shear edges implemented by smaller interchanges, then applying D←D−H, H←H+D, D←H−D; cost O(V e^τ).",
    ["bit-shear-interface", "matrix-shear-cost", "recursive-power-saving", "multitape-streams"],
    ["Split whole rows cyclically into $W$ role streams within each prefix preceding the row field.",
     "To interchange the two full chunks, perform"])

add("chunk-interchange", "Fast interchange of address chunks",
    "Interchanging two disjoint address fields of u bits in an array in O(V u^τ) time for a fixed τ < 1, although the intermediate steps XOR data together; arbitrary widths are handled by padding and a base-m decomposition.",
    ["power-width-interchange"],
    ["The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product.",
     "Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."])

add("phase-frames", "Phase frames and the two-point kernel C",
    "With C = H S H = aI+bX (a=(1+i)/2, b=(1−i)/2) one has H₀^(⊗D) = b^D S_D C^(⊗D) S_D, and phase frames of binary labels make each network edge a product of translation kernels, one per residual basis vector.",
    ["subspace-labels", "frames-on-arrays", "complex-numbers"],
    ["Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis.",
     "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D"])

add("packed-selected-bit-addition", "Packed changes of selected address bits",
    "Adding (XOR) selected bits of one address chunk into another using a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small explicitly identified set of exceptional addresses.",
    ["chunk-interchange", "controlled-shifts"],
    ["We implement a binary row addition on corresponding selected bits in two address chunks.",
     "then corrects an explicitly bounded set of addresses"])

add("guard-bits", "Exact Gaussian dyadics and guard width",
    "Intermediate values in a butterfly layer are exact Gaussian dyadics whose denominators and magnitudes grow by at most a bounded number of guard bits, so one truncation follows the completed layer.",
    ["fixed-point-precision", "phase-frames"],
    ["Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators.",
     "The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete."])

add("simultaneous-butterfly-layer", "Simultaneous butterfly layer",
    "Applying H₀(u,v) = ((u+v)/2,(u−v)/2) to the same bit position in d address chunks at once, on polynomial records, in O(V d^λ') time with λ' < 1 instead of d whole-array passes.",
    ["phase-frames", "packed-selected-bit-addition", "recursive-power-saving", "guard-bits", "radix-two-fft", "fixed-point-precision", "chunk-interchange"],
    ["Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise.",
     "whereas separate butterfly factors would require $D$ whole-array passes"])

add("synthetic-transform-layout", "Synthetic transform layout on tape",
    "A positional address permutation placing the selected bits of all participating axes at a common offset in consecutive K-bit chunks so that each FFT round is one simultaneous layer; total cost O(Tp[dK + pK^(τ−1) + ℓ d^λ']).",
    ["synthetic-transforms", "simultaneous-butterfly-layer", "chunk-interchange"],
    ["we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks"])

add("synthetic-convolution", "Convolution over the polynomial ring from retained frequency order",
    "Convolving arrays over the ring by transforming both operands, multiplying pointwise in the retained stored frequency order, and applying the opposite transform, with error below √2·M(3ℓ+1)·2^(−p).",
    ["synthetic-transform-layout", "signed-kronecker-packing"],
    ["Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands.",
     "We may therefore multiply the forward outputs in their retained order and pass that order directly to the opposite procedure."])

add("coefficient-twist", "Cyclic-to-negacyclic coefficient twist",
    "Multiplying coefficient k of the last cyclic coordinate by ζ^k with ζ = e^(πi/r) maps cyclic convolution of length r to the ring modulo y^r + 1, so the ring convolution computes complex cyclic convolution.",
    ["negacyclic-ring", "synthetic-convolution", "convolution-multiplication"],
    ["A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$",
     "Untwisting therefore recovers the cyclic coefficient with the correct sign."])

add("crt-cyclic-convolution", "Chinese-remainder map to distinct prime cyclic axes",
    "An algebra isomorphism sending x to the product of x_i^(μ_i) turns one cyclic convolution of length S = s₁…s_d into a d-dimensional cyclic convolution over pairwise coprime axes, implemented by triangular controlled shifts.",
    ["convolution-multiplication", "controlled-shifts", "chunk-interchange"],
    ["Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution",
     "Each triangular update is a prefix-controlled cyclic shift."])

add("gaussian-resampling", "Gaussian resampling without sorting",
    "Rewrites the prime-length transform P_s F_s as 2^(2α²) B₀ P_t F_t A with contractions A, B₀ and power-of-two length t, keeping the two coordinate permutations inside the transform identity instead of sorting.",
    ["discrete-fourier-transform", "fixed-point-precision"],
    ["Its usual implementation sorts twice on each coordinate.",
     "We retain both permutations in the transform formula and compute that formula directly."])

add("tensor-resampling", "Tensor resampling on the padded box",
    "Applying the one-dimensional resampling maps line by line along each of d axes of the zero-padded power-of-two box, exposing each axis with chunk interchanges, for error below d·p² and total line cost O(dTp^(3/2+δ)α).",
    ["gaussian-resampling", "chunk-interchange"],
    ["For the tensor product, apply the one-dimensional maps to one coordinate line at a time."])

add("bluestein-chirp", "Bluestein chirp identity",
    "Writes the permuted transform Q F_t as chirp multiplication, a cyclic convolution with the chirp array a, and chirp multiplication again, so the frequency permutation is never executed.",
    ["discrete-fourier-transform", "convolution-multiplication", "gaussian-resampling"],
    ["The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.",
     "Bluestein's chirp identity converts the middle transform"])

add("permutation-cancellation", "Cancellation of the retained source permutation",
    "Because a coordinate permutation R commutes with pointwise products, applying R F_s to both operands and R F_s⁺ to their pointwise product yields (u*v)/S², so the source permutation never has to be undone.",
    ["gaussian-resampling", "discrete-fourier-transform"],
    ["Finally, the source permutation retained during resampling cancels across the two forward source transforms"])

add("parameter-choice", "Size parameters and prime axis lengths",
    "For input length n choose b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, a power-of-two T near 4n/b split into d axis lengths r/2 or r, and distinct odd primes s_i just below the t_i with T/2 < S < T.",
    ["crt-cyclic-convolution", "gaussian-resampling", "synthetic-transform-layout"],
    ["The distinct prime lengths $s_i$ must be close to the powers of two $t_i$",
     "p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor"])

add("multiplication-algorithm", "The multiplication algorithm",
    "Split into radix digits, map by the CRT address map, apply the source transform (resampling, chirp convolution via ring convolution) to both operands, multiply pointwise, apply the opposite transform, undo scales, round and propagate carries.",
    ["parameter-choice", "crt-cyclic-convolution", "tensor-resampling", "bluestein-chirp", "permutation-cancellation", "coefficient-twist"],
    ["Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain source arrays $u,v$.",
     "Compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$."])

add("exact-recovery", "Precision, rounding and carry recovery",
    "Disk margins keep every intermediate array in the unit disk, accumulated approximation errors stay below 1/2 per coefficient so rounding returns exact integer product coefficients, and carry propagation gives the 2n-bit product.",
    ["multiplication-algorithm", "fixed-point-precision"],
    ["proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product"])

add("time-bound-accounting", "Cost table and exponent margins",
    "Dividing each phase's cost by Tp = Θ(n) gives seven dominant powers of p, each at most 1−2κ for the fixed rational exponents, so the total is O(n (log n)^(1−κ)).",
    ["multiplication-algorithm", "chunk-interchange", "simultaneous-butterfly-layer", "tensor-resampling", "signed-kronecker-packing"],
    ["Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
     "Each of the seven displayed powers is at most $1-2\\kappa$ by"])

add("multiplication-below-nlogn", "Integer multiplication below n log n",
    "A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture, by combining fast address interchange and simultaneous butterfly layers inside the Gaussian-resampling and synthetic-transform reduction.",
    ["multiplication-algorithm", "exact-recovery", "time-bound-accounting", "hvdh-multiplier"],
    ["We give a deterministic algorithm that multiplies two $n$-bit integers",
     "disproves the $n\\log n$ optimality conjecture"])

ans = {"target": "multiplication-below-nlogn", "concepts": C}
ids = {c["id"] for c in C}
assert len(ids) == len(C)
bad = 0
for c in C:
    for r in c["requires"]:
        assert r in ids, (c["id"], r)
    if c["known"]:
        assert not c["requires"]
    elif not c["evidence"]:
        print("no evidence", c["id"]); bad += 1
    for e in c["evidence"]:
        if norm(e["quote"]) not in nsrc:
            print("MISSING QUOTE", c["id"], e["quote"]); bad += 1
# cycle check
state = {}
def dfs(n):
    if state.get(n) == 1: raise SystemExit("cycle at " + n)
    if state.get(n) == 2: return
    state[n] = 1
    for r in next(c for c in C if c["id"] == n)["requires"]: dfs(r)
    state[n] = 2
for c in C: dfs(c["id"])
print("concepts", len(C), "bad", bad)
json.dump(ans, open(ROOT + "/exegenius/tasks/0001-extract.answer.json", "w"), indent=1, ensure_ascii=False)
