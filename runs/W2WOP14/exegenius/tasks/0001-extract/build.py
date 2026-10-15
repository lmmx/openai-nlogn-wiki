import json, re, sys
base = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4"
src = open(base + "/sources/paper.tex").read()

C = []
def add(id, name, gloss, requires, evidence=(), known=False, aliases=(), title=None, symbols=None):
    d = dict(id=id, name=name, aliases=list(aliases), gloss=gloss, requires=list(requires), known=known,
             evidence=[{"source": "paper", "quote": q} for q in evidence])
    if title: d["title"] = title
    if symbols: d["symbols"] = symbols
    C.append(d)

# known
add("big-o", "Big-O notation", "Asymptotic upper bounds on running time such as O(n log n).", [], known=True)
add("polynomials", "Polynomials", "Expressions Σ a_k x^k with coefficients, added and multiplied by the usual rules.", [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a + bi with i² = −1, including modulus and unit-modulus numbers e^{iθ}.", [], known=True)
add("multitape-tm", "Multitape Turing machine", "A deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each head moving at most one cell per step.", [], known=True)

add("integer-multiplication-conjecture", "The n log n conjecture for integer multiplication",
    "Schönhage and Strassen's 1971 proposal that n log n is the optimal multitape-Turing-machine time for multiplying two n-bit integers; the O(n log n) algorithm of Harvey and van der Hoeven met it from above, and this paper beats it by a power of the logarithm.",
    ["multitape-tm", "big-o"],
    ["proposed $n\\log n$ as the optimal order of growth",
     "Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper",
     "In the multitape Turing model,"],
    aliases=["n log n optimality conjecture", "Schönhage–Strassen conjecture"])

add("established-multiplier", "Established n log n multiplier",
    "The known fixed-tape integer multiplier of Harvey and van der Hoeven running in O(N log N) on N-bit inputs, used here only as an ordinary subroutine on short operands (never recursively on the improved algorithm).",
    ["big-o", "multitape-tm"],
    ["Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine",
     "they do not invoke the improved theorem recursively."])

add("tape-address-model", "Arrays, addresses and volume on tapes",
    "An array on address set [a₁]×…×[a_t] is stored on a tape in lexicographic order with the address implicit in position; its logical volume V is the number of stored data bits, and an adjacent group of address bits is an address field or chunk.",
    ["multitape-tm", "big-o"],
    ["An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in",
     "The \\emph{logical volume} $V$ is the number of stored data bits."],
    aliases=["address field", "logical volume"])

add("elementary-stream-ops", "Elementary stream operations",
    "Linear-time (O(V)) tape scans that permute two radix-q digits, move a digit, split an array into aligned streams on a digit, apply a pointwise map and merge, or deal whole rows cyclically to W streams.",
    ["tape-address-model"],
    ["volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:"],
    aliases=["split and merge", "row splitting"])

add("controlled-shift", "Controlled cyclic shifts",
    "An update y ↦ y + a(controls) mod Q of a target field that follows its control fields on tape, done in O(V) by splitting each fiber at the offset and merging the two pieces in the opposite order; also multiplication by a fixed unit and negation of the target.",
    ["elementary-stream-ops"],
    ["y\\longmapsto y+a(\\text{controls})\\pmod Q",
     "The next operations are linear because their target field follows their"],
    aliases=["controlled shifts", "ordered affine streams"])

add("linear-algebra-basics", "Rank, subspaces and orthogonal complements",
    "Matrix rank, subspaces, projections, bilinear forms and the orthogonal complement of a subspace inside a larger one, including over the two-element field F₂.",
    [],
    ["A label is a nondegenerate subspace of a fixed bilinear space.",
     "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"],
    aliases=["nondegenerate subspace", "orthogonal residual"])

add("cyclic-convolution", "Cyclic convolution",
    "The convolution u*v of arrays on Z/t₁×…×Z/t_D, where output index j sums u_k v_{j−k} with indices wrapping modulo each length; it is the product in the group algebra C[x₁,…]/(x₁^{t₁}−1,…), and integer multiplication is a convolution of digit lists.",
    ["polynomials"],
    ["let $*$ denote cyclic convolution in the displayed",
     "Thus convolution modulo $x^S-1$ has no nonzero wraparound."],
    aliases=["convolution"])

add("dft", "Discrete Fourier transform",
    "The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}, with an opposite-sign inverse F⁺ satisfying F⁺F = I/q, which turns cyclic convolution into a pointwise product: F(u*v) = q·(Fu)(Fv).",
    ["complex-numbers", "cyclic-convolution"],
    ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q},",
     "Each normalized Fourier transform above is a contraction, since each"],
    aliases=["Fourier transform", "DFT"])

add("multidimensional-dft", "Multidimensional (tensor) transform",
    "The tensor product F_t = ⊗ F_{t_i} of one-dimensional transforms applied along each axis of an array with axis lengths t₁,…,t_D; moving to many axes of power-of-two length is why the algorithm can use cheap butterflies.",
    ["dft"],
    ["multidimensional transforms whose axis lengths are",
     "For $D$ axes of lengths $t_1,\\ldots,t_D$, put"],
    aliases=["tensor transform"])

add("butterfly", "Two-point butterfly",
    "The 2×2 averaging step H₀(u,v) = ((u+v)/2, (u−v)/2) from which a power-of-two transform is built by pairing entries k and k+t/2 (decimation in frequency), with the second output multiplied by a twiddle root.",
    ["dft", "complex-numbers"],
    ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)",
     "the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"],
    aliases=["H₀", "butterfly operation"])

add("polynomial-ring-mod", "Polynomial ring modulo y^r + 1",
    "The ring of complex polynomials of degree < r with y^r = −1, in which multiplying by a power of y permutes the coefficients up to sign, so that powers of y serve as exact roots of unity.",
    ["polynomials", "complex-numbers"],
    ["stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two.",
     "Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes"],
    title="Polynomial ring modulo $y^r + 1$",
    aliases=["negacyclic polynomial ring", "R_r"],
    symbols=[
      {"symbol": "y", "name": "ring variable", "meaning": "The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.", "relation": "direct"},
      {"symbol": "r", "name": "record length", "meaning": "The number of complex coefficients in a polynomial record, a power of two.", "relation": "count"}])

add("synthetic-transform", "Synthetic polynomial transform",
    "A Fourier-type transform whose entries lie in C[y]/(y^r+1) and whose root of unity ω_t = y^{2r/t} acts as a signed coefficient shift, computed by radix-two butterfly rounds with twiddle monomials, leaving outputs in bit-reversed (retained) frequency order that the opposite transform consumes.",
    ["dft", "polynomial-ring-mod", "butterfly", "multidimensional-dft"],
    ["such a root is a signed shift of the coefficient list.",
     "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",
     "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$."],
    aliases=["Nussbaumer polynomial transform", "stored frequency order"])

add("signed-packing", "Signed packing of polynomial products",
    "A signed form of Kronecker substitution: evaluate polynomial coefficients at 2^{4p} to get integers, multiply with the established multiplier, and read the product coefficients back by centered residues and carries.",
    ["polynomial-ring-mod", "established-multiplier"],
    ["The reduction is a signed form of Kronecker substitution",
     "After the lower coefficients have been removed from an evaluation,"],
    aliases=["Kronecker substitution"])

add("linear-network", "Linear exchange network with restored scratch wires",
    "A fixed network of linear gates on wires (each with a role) that, for arbitrary initial scratch values, exchanges two banks of values with prescribed signs and restores every scratch wire; run in eight rows of copy, gather, scatter and side-injection steps.",
    ["linear-algebra-basics"],
    ["Each procedure arises from its own fixed linear network that exchanges two",
     "the following schedule remove the effect of the old scratch values;",
     "(X_a,Y_a)\\longmapsto(-Y_a,X_a)"],
    aliases=["bank exchange", "finite network", "role"])

add("common-frame-principle", "Frames on wire arrays",
    "Replacing each scalar by an array and giving every vertex an invertible linear operator D_v (its frame) lets pointwise gates commute with frames, so intermediate frames cancel and only the endpoint operator D_out·D_in⁻¹ is applied to each role while each edge pays only the change of frame D_v D_u⁻¹.",
    ["linear-network", "linear-algebra-basics"],
    ["At each source, gate and sink $v$, assign an invertible $R$-linear operator",
     "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}."],
    aliases=["frame", "common-frame identity"])

add("subset-intersection-labels", "Subspace labels from three-element subsets",
    "Attaching nested nondegenerate subspaces of F^{⊗3} (spanned by indicator vectors of 3-element subsets, with ⟨t_S,t_T⟩ = |S∩T|−1) to gates and terminals so that gather/scatter coefficients depend on intersection size and unwanted ones are cancelled by side wires; the total rank change of all edges is less than Wm.",
    ["linear-network", "common-frame-principle", "linear-algebra-basics"],
    ["three-element subsets: gather and scatter create coefficients depending",
     "A label is a nondegenerate subspace of a fixed bilinear space.",
     "\\langle t_S,t_T\\rangle=|S\\cap T|-1,"],
    aliases=["rank saving construction", "orthogonal residual labels"])

add("address-shear", "Address shear and lower-triangular factorization",
    "The address permutation (H,D) ↦ (H+AD, D) on two vectors of fields; a rank-a matrix factors as E₁ΠE₂ with lower-triangular E₁,E₂ so that it costs a single-pair swaps plus linear-time updates, and three shears D←D−H, H←H+D, D←H−D interchange H and D.",
    ["linear-algebra-basics", "controlled-shift", "elementary-stream-ops"],
    ["updated by $(H,D)\\mapsto(H+D,D)$.",
     "A=E_1\\Pi E_2,",
     "D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,"],
    aliases=["Bruhat factorization", "matrix shear"])

add("rank-saving-recurrence", "Recursive rank saving",
    "Running the linear network with edge changes implemented by smaller calls on role streams of volume V/W gives a cost-per-volume recurrence F_k ≤ (s/W)F_{k−1}+O(1); because the number s of smaller calls satisfies s < Wm, this yields F_k = O(e^τ) with τ<1, a power saving in the parameter.",
    ["subset-intersection-labels", "common-frame-principle", "elementary-stream-ops", "big-o"],
    ["number $s$ of smaller calls satisfies $s<Wm$.",
     "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
     "increases the recursive contribution by $s/W<m$. This strict inequality"],
    aliases=["power saving recurrence"])

add("address-chunk-interchange", "Fast address-chunk interchange",
    "The first tape procedure: swapping two disjoint contiguous address fields of u bits, (p,h,g,d,z) ↦ (p,d,g,h,z), in O(V u^τ) for a fixed τ<1 by building the swap from address shears executed through the bit network, with XOR combinations of intermediate data.",
    ["address-shear", "rank-saving-recurrence", "common-frame-principle", "tape-address-model"],
    ["The first procedure interchanges two disjoint contiguous address",
     "Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$.",
     "(p,h,g,d,z)\\longmapsto(p,d,g,h,z)"],
    aliases=["chunk swap", "tape interchange"])

add("phase-frame-kernel", "Phase frames and the two-point kernel C",
    "The complex version of the network uses frames built from Hamming-weight phases i^{wt(x) mod 4}; each edge change factors into two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), so a simultaneous C-layer on e=mf axes needs s smaller layers on f axes, and H₀^{⊗D} = b^D S_D C^{⊗D} S_D.",
    ["common-frame-principle", "subset-intersection-labels", "butterfly", "linear-algebra-basics"],
    ["C=H\\mathsf SH=aI+bX",
     "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
     "Its phase-frame difference"],
    aliases=["binary phase interface", "C kernel"])

add("packed-selected-bit-addition", "Packed selected-bit addition",
    "A binary row addition y_j ← y_j ⊕ x_j on the same bit position in f address chunks at once, done with eight chunk-wide cyclic shifts whose segments cannot carry into each other except at a small explicit set of exceptional addresses, which are then repaired deterministically; it restores the third chunk's arbitrary contents.",
    ["controlled-shift", "address-chunk-interchange"],
    ["We implement a binary row addition on corresponding selected bits in two",
     "Let $\\mathcal B$ consist of the addresses for which"],
    aliases=["packed XOR", "exceptional address repair"])

add("fixed-point-truncation", "Fixed-point disk-grid arithmetic",
    "Complex values stored as 2^{−p}(a+ib) with signed two's-complement words in the unit disk, exact Gaussian-dyadic intermediate results with guard bits, and one truncation Q_p toward zero that costs error less than √2·2^{−p} per coefficient while never increasing the norm.",
    ["complex-numbers"],
    ["Intermediate values are exact Gaussian dyadics,",
     "\\|Q_p z-z\\|_\\infty<\\sqrt2\\,2^{-p},\\qquad"],
    aliases=["disk grid", "Gaussian dyadics", "truncation Q_p"])

add("fast-butterfly-layer", "Fast simultaneous butterfly layer",
    "The second tape procedure: applying H₀ at the same bit offset in d address chunks of a polynomial-record array in cost O(V d^λ') with λ'<1, by evaluating the layer exactly through the phase-frame network with packed chunk moves before a single truncation.",
    ["phase-frame-kernel", "packed-selected-bit-addition", "rank-saving-recurrence", "fixed-point-truncation", "polynomial-ring-mod", "address-chunk-interchange"],
    ["and the cost is $O(Vd^{\\lambda'})$ for a",
     "The procedure returns $Q_p(\\mathcal H z)$ in the same array,"],
    aliases=["simultaneous normalized butterfly layer"])

add("ring-convolution", "Convolution over the polynomial ring",
    "Normalized convolution on d−1 axes of arrays with entries in C[y]/(y^r+1): two forward synthetic transforms keeping the same frequency order, pointwise polynomial products (by signed packing) divided by r, and the opposite transform, all using the fast layers and chunk swaps.",
    ["synthetic-transform", "signed-packing", "fast-butterfly-layer", "address-chunk-interchange", "cyclic-convolution"],
    ["Perform both forward transforms and retain their common $LB$ order.",
     "The two forward synthetic transforms"],
    aliases=["synthetic convolution"])

add("phase-twist", "Coefficient (phase) twist",
    "The map x_d ↦ ζy with ζ = e^{πi/r} that sends the cyclic last coordinate C[x_d]/(x_d^r−1) isomorphically to C[y]/(y^r+1) by multiplying coefficient k by ζ^k, so the negative wrap of the ring becomes the original cyclic wrap after untwisting.",
    ["polynomial-ring-mod", "cyclic-convolution", "complex-numbers"],
    ["is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",
     "A phase twist changes the last cyclic coordinate into a polynomial"],
    aliases=["twist"])

add("bluestein-chirp", "Bluestein chirp identity",
    "Writing a (permuted) transform as a chirp-weighted cyclic convolution QF_t u = ā · (a * (ā · u))/T with a_j = exp(−πi Σ s_i j_i²/t_i), so a Fourier transform with its target permutation becomes a normalized convolution.",
    ["dft", "cyclic-convolution", "multidimensional-dft"],
    ["Next, Bluestein's chirp identity converts the middle transform,",
     "computed from a cyclic convolution and two pointwise phase"],
    aliases=["chirp identity", "chirp transform"])

add("gaussian-resampling", "Gaussian resampling",
    "The Harvey–van der Hoeven reduction that expresses a Fourier transform of length s (here a prime) through a power-of-two transform of length t>s via Gaussian-weighted contractions: P_s F_s = 2^{2α²} B₀ P_t F_t A, with the two coordinate permutations P_s,P_t left inside the identity.",
    ["dft", "multidimensional-dft", "complex-numbers", "fixed-point-truncation"],
    ["Its usual implementation sorts twice on each",
     "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."],
    aliases=["Gaussian gridding", "resampling"])

add("permutation-cancellation", "Retained permutations and their cancellation",
    "Instead of executing the source and target coordinate permutations of Gaussian resampling as sorts, they stay in the transform formula; the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform: RF⁺[(RFu)(RFv)] = (u*v)/S².",
    ["gaussian-resampling", "bluestein-chirp", "dft", "cyclic-convolution"],
    ["We retain both permutations in the transform formula and",
     "retained source permutation $R$ cancels when computing a convolution."],
    aliases=["no-sort resampling"])

add("crt-address-map", "Chinese-remainder address map",
    "The Agarwal–Cooley isomorphism Φ: C[x]/(x^S−1) → C[x₁..x_d]/(x_i^{s_i}−1), x ↦ ∏ x_i^{μ_i}, for pairwise coprime (prime) s_i with S = ∏ s_i, which turns one long cyclic convolution into one on distinct prime axes and is implemented by triangular controlled shifts.",
    ["cyclic-convolution", "polynomials", "controlled-shift"],
    ["Agarwal and Cooley used the Chinese remainder",
     "x\\longmapsto\\prod_i x_i^{\\mu_i}",
     "Each triangular update is a prefix-controlled cyclic shift."],
    aliases=["CRT map", "Agarwal–Cooley map"])

add("radix-digit-convolution", "Integer product as digit convolution",
    "Writing each n-bit input as a polynomial in 2^b with ⌈n/b⌉ digits, the integer product is the polynomial product, whose coefficients are below 2^{3b}; with enough zero padding the cyclic convolution has no wraparound, and carries recover the bits.",
    ["polynomials", "cyclic-convolution"],
    ["Splitting the inputs into radix digits reduces multiplication to",
     "Write the two inputs as polynomials in $2^b$, each with"],
    aliases=["radix-2^b digits"])

add("exact-recovery", "Rounding and carry propagation",
    "The final steps that rescale by known factors (S, 2^{2b+4}), prove the accumulated coefficient error is below 1/2 so rounding gives the exact integer coefficients, and propagate radix-2^b carries to produce the 2n-bit product.",
    ["radix-digit-convolution", "fixed-point-truncation"],
    ["The strict error below $1/2$ makes the nearest integer to",
     "coefficient error is strictly below $1/2$, and propagates carries to"],
    aliases=["exact recovery", "carry propagation"])

add("parameter-choice", "Parameter choices and prime source lengths",
    "The size parameters b=⌈log₂n⌉, precision p=6b, number of axes d=⌊b^ε⌋, chunk width K=⌊d^c⌋, padded size T≈n/b, power-of-two axis lengths t_i∈{r/2,r}, and distinct primes s_i just below t_i with T/2 < ∏s_i < T, chosen so resampling hypotheses and all tape lemmas apply.",
    ["crt-address-map", "gaussian-resampling", "polynomial-ring-mod", "radix-digit-convolution"],
    ["b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
     "The distinct prime lengths $s_i$ must be close to the powers of two"],
    aliases=["fixed rational choice"])

add("multiplication-algorithm", "The multiplication algorithm",
    "The pipeline: form radix digits, apply the CRT address map Φ, run two source transforms (resampling plus chirp convolution plus resampling), multiply pointwise, run the opposite transform, rescale, round and propagate carries; inside the chirp convolution the last coordinate is twisted into C[y]/(y^r+1) and convolved with synthetic transforms.",
    ["radix-digit-convolution", "crt-address-map", "gaussian-resampling", "permutation-cancellation",
     "bluestein-chirp", "phase-twist", "ring-convolution", "exact-recovery", "parameter-choice"],
    ["With these streams prepared, perform the following operations.",
     "The two occurrences of $S$ in this algorithm undo different"],
    aliases=["reduction chain"])

add("time-accounting", "Cost accounting and the saving κ",
    "Dividing every cost by V = Tp = Θ(n) gives a table of seven dominant powers of p (layout moves, chunk exchanges, simultaneous butterfly rounds, CRT layout, Gaussian line maps, chirps, packed products), each at most 1−2κ with κ = 2^{−182}, giving total O(n (lg n)^{1−κ}).",
    ["multiplication-algorithm", "parameter-choice", "address-chunk-interchange", "fast-butterfly-layer", "established-multiplier", "big-o"],
    ["Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
     "Each of the seven displayed powers is at most $1-2\\kappa$ by"],
    aliases=["complete time bound"])

add("main-theorem", "Integer multiplication below n log n",
    "A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture; it works by reducing to convolution, using fast address interchange and fast simultaneous butterfly layers to save a power of the logarithm.",
    ["integer-multiplication-conjecture", "multiplication-algorithm", "time-accounting"],
    ["We give a deterministic algorithm that multiplies two $n$-bit integers",
     "There is one deterministic Turing machine $A$, with a fixed finite",
     "T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right),"],
    aliases=["Theorem 1", "main result"])

ans = {"target": "main-theorem", "concepts": C}

def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", "", s)
ns = norm(src)
bad = 0
for c in C:
    for e in c["evidence"]:
        if norm(e["quote"]) not in ns:
            print("MISSING", c["id"], e["quote"]); bad += 1
    if not c["known"] and not c["evidence"]:
        print("NOEVID", c["id"]); bad += 1
ids = {c["id"] for c in C}
for c in C:
    for r in c["requires"]:
        if r not in ids: print("BADREQ", c["id"], r); bad += 1
    if c["known"] and c["requires"]: print("KNOWNREQ", c["id"]); bad += 1
# cycle check
state = {}
def dfs(u):
    state[u] = 1
    for r in next(c for c in C if c["id"] == u)["requires"]:
        if state.get(r) == 1: print("CYCLE", u, r); return True
        if r not in state and dfs(r): return True
    state[u] = 2
    return False
for c in C:
    if c["id"] not in state: dfs(c["id"])
print("bad", bad)
json.dump(ans, open(base + "/exegenius/tasks/0001-extract.answer.json", "w"), indent=1, ensure_ascii=False)
