import json, re, sys

SRC = "/home/user/openai-nlogn-wiki/runs/K2/sources/paper.tex"
OUT = "/home/user/openai-nlogn-wiki/runs/K2/exegenius/tasks/0001-extract.answer.json"

def C(id_, name, gloss, requires, evidence=(), aliases=(), known=False, title=None, symbols=None):
    d = {"id": id_, "name": name, "aliases": list(aliases), "gloss": gloss,
         "requires": list(requires), "known": known,
         "evidence": [{"source": "paper", "quote": q} for q in evidence]}
    if title is not None:
        d["title"] = title
        d["symbols"] = symbols or []
    return d

def B(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

concepts = [
# ---------- known to the reader ----------
C("big-o-notation", "Big-O notation",
  "Asymptotic upper bounds: f = O(g) means f is at most a constant times g for all sufficiently large inputs.",
  [], known=True, aliases=["O-notation"]),
C("polynomials", "Polynomials",
  "Finite sums of powers of a formal variable with coefficients, with their addition and multiplication.",
  [], known=True),
C("complex-numbers", "Complex numbers",
  "Numbers a + bi with real a and b and i squared equal to -1, with modulus and complex conjugation.",
  [], known=True),
C("turing-machines", "Basic Turing machines and tapes",
  "A Turing machine reads and writes symbols on tape cells under a finite control, and a multitape machine gives each tape its own head.",
  [], known=True),

# ---------- machine model and streams ----------
C("fixed-tape-machine", "Fixed-tape Turing machine model",
  "A machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, in which each step moves each head by at most one cell and running time counts these steps.",
  ["turing-machines", "big-o-notation"],
  evidence=["A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."],
  aliases=["fixed finite-tape model"]),
C("schonhage-strassen-conjecture", "Schönhage–Strassen optimality conjecture",
  "The 1971 proposal that n log n is the optimal order of growth for multiplying integers on a multitape Turing machine; the main result refutes it in the fixed-tape model.",
  ["big-o-notation", "fixed-tape-machine"],
  evidence=["proposed $n\\log n$ as the optimal order of growth"],
  aliases=["n log n conjecture"]),
C("hvdh-multiplier", "Established fixed-tape integer multiplier",
  "Harvey and van der Hoeven's deterministic fixed-tape multiplication of N-bit integers in O(N log N) time, which the new algorithm calls as an ordinary subroutine on shorter records.",
  ["fixed-tape-machine", "big-o-notation"],
  evidence=["We use the established $O(N\\log N)$ integer multiplier of"],
  aliases=["Harvey–van der Hoeven multiplier"]),
C("elementary-stream-operations", "Elementary stream operations",
  "Linear-time scans on a fixed number of tapes that permute or move digits at chosen positions, apply fixed pointwise maps to aligned streams, and split whole rows cyclically into W streams of equal volume.",
  ["fixed-tape-machine", "big-o-notation"],
  evidence=["takes $O(V)$ steps on a fixed number of one-dimensional tapes"]),
C("logical-volume", "Logical volume",
  "The number V of stored data bits in an array, not counting work tapes or duplicate streams; every tape cost is measured against V.",
  ["fixed-tape-machine"],
  evidence=["is the number of stored data bits"]),
C("address-fields", "Address fields and rows",
  "An array is indexed by a complete lexicographic product of address fields and stored in that order, and a row is the complete block of entries at one fixed prefix and row index.",
  ["logical-volume"],
  evidence=["When one address field is designated as a row field"]),
C("row-splitting", "Row splitting into role streams",
  "Distributing the rows of an array cyclically among W role streams, so that each stream has the same shape and volume V/W and gates act pointwise on matching addresses.",
  ["address-fields", "elementary-stream-operations"],
  evidence=["Distribute rows cyclically among the $W$ roles"]),
C("controlled-shifts", "Controlled cyclic shifts",
  "A cyclic shift of a target field by an offset computed from the preceding control fields, together with multiplication by fixed rational units, all done in linear time on tapes.",
  ["elementary-stream-operations", "address-fields"],
  evidence=["their target field follows their control fields"]),
C("linear-algebra", "Linear algebra over a field",
  "Vector spaces, linear maps and matrices, with subspaces, bilinear forms, orthogonal complements and tensor products, as used by the finite networks and their labels.",
  ["complex-numbers"],
  evidence=["choose an invertible linear operator"]),

# ---------- finite linear networks ----------
C("scratch-restoration", "Restoration of arbitrary scratch values",
  "A linear computation whose auxiliary wires may start with arbitrary values and end with the same values, so that an exchange of two banks can be performed without knowing the scratch contents (the transparent-computation idea of Buhrman et al.).",
  ["linear-algebra"],
  evidence=["This cancellation of arbitrary initial scratch values is a linear"]),
C("triple-subset-exchange-network", "Triple-subset exchange network",
  "A fixed linear network whose banks are indexed by triples of three-element subsets of a 100-element set, which exchanges two banks with a sign while restoring all scratch wires, using eight rows of copy, gather, scatter and side-injection operations.",
  ["scratch-restoration", "linear-algebra"],
  evidence=["The construction uses three-element subsets"]),
C("frames", "Frames on network vertices",
  "An invertible linear operator attached to each gate, source and sink of a network, which changes the stored representation of a wire's array so that every gate acts pointwise and the endpoint operators are the only net effect.",
  ["linear-algebra", "triple-subset-exchange-network"],
  evidence=["We call $D_v$ its frame"]),
C("subspace-labels", "Subspace labels and orthogonal residuals",
  "A nondegenerate subspace attached to each network vertex, with one label containing the other along every edge, so that the dimension of the orthogonal residual on an edge measures the cost of its frame change.",
  ["linear-algebra", "frames", "triple-subset-exchange-network"],
  evidence=["A label is a nondegenerate subspace of a fixed bilinear space."]),
C("rank-saving", "Rank saving s < Wm",
  "The inequality that the number s of smaller calls is less than W times m, where W is the number of wires and m the label dimension, which is the source of the power saving.",
  ["subspace-labels", "triple-subset-exchange-network"],
  evidence=["number $s$ of smaller calls satisfies $s<Wm$"],
  aliases=["rank deficit"],
  title="Rank saving $s < Wm$",
  symbols=[B("s", "smaller-call count", "The number of smaller calls made by one network invocation, the sum of the rational ranks of all edge matrix differences.", "count"),
           B("W", "wire count", "The number of wires in the network, including its scratch wires.", "count"),
           B("m", "label dimension", "The dimension of the ambient label space, which is h cubed for the set size h = 100.", "direct")]),
C("volume-normalized-recursion", "Volume-normalized recursion",
  "A recursion in which cost per unit volume is multiplied by s/W at each level, with s/W below m to the power tau, so that the total cost is O(e^tau) per unit volume for chunks of e = m^k digits.",
  ["rank-saving", "logical-volume", "row-splitting"],
  evidence=["is the source of the power saving"]),

# ---------- address interchange ----------
C("lower-triangular-factorization", "Lower-triangular factorization",
  "Every rational matrix of rank a factors as an invertible lower-triangular matrix times a partial permutation matrix with exactly a ones, times another invertible lower-triangular matrix.",
  ["linear-algebra"],
  evidence=["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"]),
C("matrix-shear-interchange", "Matrix shear of address fields",
  "The map (H, D) to (H + AD, D) on two groups of address fields for a fixed rational matrix A of rank a, performed with exactly a interchanges of field pairs and linear extra work.",
  ["lower-triangular-factorization", "controlled-shifts", "address-fields"],
  evidence=["can be performed with exactly $a$ interchanges of pairs of $b$-digit"]),
C("circuit-to-address-permutation", "Finite circuit as address permutation",
  "The transfer of a finite bit circuit with rational vertex matrices whose rank sum is below Wm into a permutation of address fields that applies the same shear to every wire role.",
  ["triple-subset-exchange-network", "subspace-labels", "frames", "matrix-shear-interchange"],
  evidence=["Assign a rational $m\\times m$ matrix to each terminal and to each gate"]),
C("power-width-chunk-interchange", "Power-width chunk interchange",
  "The interchange of two disjoint equal chunks of e = m^k digits in O(V e^tau) time, by splitting rows into W role streams, applying one shear per unit of rank on the streams, and recursing with the same fixed tapes.",
  ["matrix-shear-interchange", "circuit-to-address-permutation", "row-splitting", "volume-normalized-recursion"],
  evidence=["The chunks can be interchanged in $O(Ve^\\tau)$ time"]),
C("arbitrary-width-chunk-interchange", "Arbitrary-width chunk interchange",
  "The interchange of two equal bit chunks of arbitrary width u in O(V u^tau) time, by padding to a power of the radix, moving high digits into a row field, and handling the remaining width as a sum of power-width pieces in base m.",
  ["power-width-chunk-interchange", "elementary-stream-operations", "logical-volume"],
  evidence=["Write the remaining width in base $m$"]),

# ---------- numerical layer ----------
C("gaussian-dyadic", "Gaussian dyadic",
  "A complex number whose real and imaginary parts are dyadic rationals, that is, have power-of-two denominators.",
  ["complex-numbers"],
  evidence=["Intermediate values are exact Gaussian dyadics"]),
C("guard-bits", "Guard bits",
  "Extra fractional and integer bits reserved in each coefficient so that every intermediate value of an exact butterfly layer is represented exactly, with a width bound that grows only as a fixed power of the number of selected axes.",
  ["gaussian-dyadic"],
  evidence=["Thus reserving \\(p+\\Delta\\)"]),
C("two-point-butterfly", "Normalized two-point butterfly",
  "The map (u, v) to ((u + v)/2, (u − v)/2) applied to a pair of coefficients, the basic step of the synthetic transforms.",
  ["complex-numbers"],
  evidence=["two-point butterfly operations"]),
C("two-point-phase-kernel", "Two-point phase kernel",
  "The 2 by 2 matrix C = aI + bX with a = (1 + i)/2 and b = (1 − i)/2, the Hadamard conjugate of the phase diag(1, i), which satisfies C² = X and C⁴ = I and is the one-bit kernel from which phase frames are built.",
  ["complex-numbers", "linear-algebra"],
  evidence=["C=H\\mathsf SH=aI+bX"]),
C("binary-phase-frames", "Binary phase frames",
  "Frames indexed by binary subspace labels, built from the Hadamard transform and phases i raised to the Hamming weight of each label's projection, so that each edge change is a product of two-point phase kernels, one per residual basis vector.",
  ["two-point-phase-kernel", "subspace-labels", "linear-algebra"],
  evidence=["Use the complex scalar network and binary labels."]),
C("packed-selected-bit-xor", "Packed selected-bit XOR",
  "A linear-time operation that XORs the selected bits of one address chunk slot into the corresponding selected bits of another for all selected positions at once, using eight packed rotations of guarded segments followed by deterministic repair of the few addresses whose guards fail.",
  ["controlled-shifts", "arbitrary-width-chunk-interchange", "elementary-stream-operations", "address-fields"],
  evidence=["We implement a binary row addition on corresponding selected bits in two"]),
C("disk-grid-arrays", "Disk-grid arrays",
  "Arrays of coefficients lying in the complex unit disk and on the grid 2^(−p) times the Gaussian integers, which hold every approximate value in the algorithm.",
  ["polynomials", "complex-numbers", "gaussian-dyadic"],
  evidence=["A disk array has norm at most one."]),
C("grid-truncation", "Truncation to the precision grid",
  "Rounding each real and imaginary part of a coefficient toward zero onto the grid of spacing 2^(−p), which keeps arrays in the disk and moves each entry by less than sqrt(2) times 2^(−p).",
  ["disk-grid-arrays"],
  evidence=["A single truncation follows the completed contractive layer."]),
C("approximate-roots-of-unity", "Approximate roots of unity",
  "Disk-grid approximations of the roots of unity e^(2πi j/k) with error below 2^(−p), computable in time O(max(p, log k)^(1+δ)) and used for the phase twists.",
  ["disk-grid-arrays", "complex-numbers"],
  evidence=["one can compute $\\widetilde\\zeta\\in\\mathbb D_p$ with"]),
C("simultaneous-butterfly-layer", "Simultaneous butterfly layer",
  "The application of the normalized two-point butterfly to the same selected bit position in each of D address chunks at once, computed exactly through binary phase frames and truncated once, at cost O(V d^(λ')) with λ' below one instead of D separate passes.",
  ["two-point-butterfly", "binary-phase-frames", "packed-selected-bit-xor", "guard-bits", "grid-truncation", "row-splitting", "volume-normalized-recursion", "disk-grid-arrays"],
  evidence=["one selects the same bit position in each of at most $d$"]),

# ---------- polynomial transforms ----------
C("polynomial-ring", "Polynomial ring modulo y^r + 1",
  "The ring of polynomials with complex coefficients of degree less than r, where r is a power of two and y^r is identified with −1, so that multiplication by a power of y is a signed cyclic shift of the coefficient list.",
  ["polynomials", "complex-numbers"],
  evidence=["the coefficient list of a polynomial modulo $y^r+1$"],
  aliases=["negacyclic polynomial ring"],
  title="Polynomial ring modulo $y^r + 1$",
  symbols=[B("y", "polynomial variable", "The formal variable of the ring, whose powers serve as roots of unity in the transforms.", "direct"),
           B("r", "record length", "The number of complex coefficients in a record, which is a power of two.", "count")]),
C("polynomial-roots-of-unity", "Polynomial roots of unity",
  "The observation that powers of y in the polynomial ring are roots of unity whose multiplication is a signed shift, so a transform over the ring can use them as twiddle factors.",
  ["polynomial-ring"],
  evidence=["serve as roots of unity in the remaining axes"]),
C("cyclic-convolution", "Cyclic convolution",
  "The convolution of two arrays indexed by a product of cyclic groups, in which each output entry sums products of input entries whose indices are added modulo the axis lengths.",
  ["complex-numbers"],
  evidence=["let $*$ denote cyclic convolution in the displayed"]),
C("discrete-fourier-transform", "Normalized discrete Fourier transform",
  "The map (F_q u)_k = (1/q) times the sum over j of u_j e^(−2πi jk/q) on vectors of length q, together with its opposite-sign partner F_q^+, which turns cyclic convolution into pointwise products up to a known factor.",
  ["complex-numbers", "cyclic-convolution"],
  evidence=["Each normalized Fourier transform above is a contraction"]),
C("contraction", "Contraction",
  "A linear map that does not increase the maximum-modulus norm, so that an error in its input is not amplified when it is applied to an approximation.",
  ["linear-algebra"],
  evidence=["Both $\\mathcal A$ and $\\mathcal B_0$ are contractions."]),
C("synthetic-transform", "Synthetic polynomial transform",
  "A normalized radix-two transform over the polynomial ring whose twiddle factors are powers of y, so each round is a parallel butterfly followed by a signed shift and the whole transform is a contraction.",
  ["polynomial-roots-of-unity", "two-point-butterfly", "discrete-fourier-transform"],
  evidence=["synthetic polynomial transforms of Nussbaumer and Quandalle"],
  aliases=["Nussbaumer polynomial transform"]),
C("transform-layout", "Positional layout of transform axes",
  "A positional permutation of record addresses that places the selected bits of all participating axes at a common offset in consecutive K-bit chunks, realized by single-bit moves and chunk interchanges so that the simultaneous layer applies.",
  ["elementary-stream-operations", "arbitrary-width-chunk-interchange", "address-fields"],
  evidence=["we must place the selected bits of the participating axes at a common"]),
C("synthetic-transform-on-tapes", "Synthetic transform on fixed tapes",
  "The forward and opposite synthetic transforms implemented on fixed tapes as a sequence of simultaneous butterfly rounds on the transform layout, with error below sqrt(2) times l times 2^(−p) and time proportional to the logical volume times a power of p.",
  ["synthetic-transform", "simultaneous-butterfly-layer", "transform-layout", "fixed-tape-machine"],
  evidence=["The procedure constructs an explicit positional"]),
C("frequency-order-retention", "Retained frequency order",
  "The stored record order produced by the forward synthetic transforms, which is preserved through a pointwise product so that the opposite transform consumes it without extra data movement.",
  ["synthetic-transform-on-tapes"],
  evidence=["retain the same frequency order through their pointwise product"]),
C("negacyclic-twist", "Phase twist of the last coordinate",
  "The isomorphism from the cyclic group algebra of length r to the polynomial ring that sends x to ζy with ζ = e^(πi/r), implemented by multiplying coefficient k by ζ^k and undone by multiplying by ζ^(−k).",
  ["polynomial-ring", "cyclic-convolution"],
  evidence=["A phase twist changes the last cyclic coordinate into a polynomial"]),
C("signed-coefficient-packing", "Signed coefficient packing",
  "Evaluating two integer polynomials at a large base 2^(4p) so that one exact integer product yields all coefficient products, with signed carries recovered by centered residues; it is a signed form of Kronecker substitution.",
  ["hvdh-multiplier", "polynomial-ring"],
  evidence=["Signed coefficient packing is a form of Kronecker substitution"]),
C("ring-product", "Normalized polynomial-ring product",
  "The normalized product f g / r of two disk-grid polynomials in the polynomial ring, computed exactly by signed packing into four integer products and returned truncated to the grid.",
  ["signed-coefficient-packing", "polynomial-ring", "grid-truncation", "disk-grid-arrays"],
  evidence=["The output is a disk grid polynomial with error less than"]),
C("normalized-ring-convolution", "Normalized ring convolution",
  "The bilinear contraction M_r(f, g) = (f ∗ g)/(rM) = (f ∗ g)/T on arrays over the polynomial ring, computed as two forward synthetic transforms, a pointwise ring product and an opposite transform.",
  ["ring-product", "synthetic-transform-on-tapes", "frequency-order-retention", "cyclic-convolution"],
  evidence=["Thus that coefficient averages"]),
C("complex-convolution-by-twist", "Complex cyclic convolution by twist",
  "The normalized complex cyclic convolution obtained from the normalized ring convolution by applying the phase twist to each operand and its inverse to the result, which is the convolution the chirp identity needs.",
  ["negacyclic-twist", "normalized-ring-convolution", "approximate-roots-of-unity"],
  evidence=["obtained from the synthetic convolution by a coefficient twist"]),

# ---------- Gaussian resampling and chirps ----------
C("gaussian-resampling", "Gaussian resampling",
  "The identity P_s F_s = 2^(2α²) B_0 P_t F_t A, with contractions A and B_0 built from Gaussian weights, which expresses a length-s Fourier transform through a length-t transform when t/s is close to one, keeping the coordinate permutations inside the identity.",
  ["discrete-fourier-transform", "contraction"],
  evidence=["Gaussian resampling then expresses each source Fourier transform through a"]),
C("permutation-free-resampling", "Resampling with permutations left in the transform",
  "Fixed-tape approximations to the Gaussian resampling maps A and B_0 for one length, with error below p^2 and time O(t p^(3/2+δ) α), in which both coordinate permutations stay in the transform identity instead of being executed as sorts.",
  ["gaussian-resampling", "prime-source-lengths", "approximate-roots-of-unity", "disk-grid-arrays", "contraction"],
  evidence=["We retain both permutations in the transform formula"]),
C("prime-source-lengths", "Prime source lengths",
  "The choice, for each axis, of a distinct odd prime s_i just below a power of two t_i with (1 − 2η) t_i < s_i ≤ (1 − η) t_i, so that the product S exceeds T/2 and each ratio t_i/s_i is large enough for the resampling lemma.",
  ["gaussian-resampling"],
  evidence=["We may therefore choose distinct odd primes satisfying"]),
C("tensor-resampling", "Multidimensional Gaussian resampling",
  "The tensor product of the one-dimensional resampling identities over all d axes, R F_s = 2^γ B_0 Q F_t A with γ = 2dα², applied one coordinate line at a time on the padded power-of-two box.",
  ["permutation-free-resampling", "prime-source-lengths"],
  evidence=["For the tensor product, apply the one-dimensional maps to one coordinate"]),
C("source-permutation-cancellation", "Cancellation of the source permutation",
  "The identity (R F_s^+)[(R F_s u)·(R F_s v)] = (u ∗ v)/S², which shows that the retained source permutation cancels across the two forward source transforms, their pointwise product and the opposite transform, leaving an ordinary convolution.",
  ["tensor-resampling", "cyclic-convolution", "discrete-fourier-transform"],
  evidence=["the source permutation retained during resampling cancels"]),
C("bluestein-chirp", "Bluestein chirp identity",
  "Bluestein's identity QF_t u = conj(a) · (a ∗ (conj(a) · u))/T, with chirp a_j = exp(−πi Σ s_i j_i²/t_i), which writes the middle transform, including its target permutation, as one cyclic convolution with pointwise phases.",
  ["discrete-fourier-transform", "cyclic-convolution"],
  evidence=["Bluestein's chirp identity converts the middle transform"]),
C("chirp-transform-procedure", "Computed chirp transform",
  "The chirp identity evaluated with approximate phases, a computed complex convolution and final truncations, mapping a disk-grid array of norm at most 0.6 to an approximation of QF_t x with error below 8TL·2^(−p).",
  ["bluestein-chirp", "complex-convolution-by-twist", "grid-truncation", "approximate-roots-of-unity"],
  evidence=["the computed chirp transform forms the arrays"]),
C("source-transform", "Source transform",
  "The approximate forward transform of a source array, obtained by applying the linewise map A, then the computed chirp transform, then the linewise map B_0, and multiplying by 2^γ, which approximates R F_s.",
  ["tensor-resampling", "chirp-transform-procedure"],
  evidence=["apply the linewise approximation to $\\mathcal A$"]),

# ---------- multiplication ----------
C("crt-coefficient-map", "Chinese-remainder coefficient map",
  "The algebra isomorphism x ↦ product of x_i^(μ_i) from C[x]/(x^S − 1) to a tensor product of cyclic rings for pairwise coprime lengths s_i, which preserves cyclic convolution and turns the ordinary coefficient order into a mixed-radix order reached by controlled cyclic shifts.",
  ["cyclic-convolution", "polynomials"],
  evidence=["placed on a product of distinct prime cyclic axes by a Chinese-remainder map"]),
C("radix-digit-convolution", "Radix-digit convolution",
  "The reduction of multiplying two n-bit integers to a cyclic convolution of their radix-2^b digit sequences, each with q = ceil(n/b) digits, whose coefficients are at most q(2^b − 1)^2, which is below 2^(3b).",
  ["cyclic-convolution", "polynomials"],
  evidence=["reduces multiplication to convolution of short integer coefficients"]),
C("carry-propagation", "Carry propagation",
  "The sweep that turns the recovered integer coefficients c_j into the binary digits of the product, using carries k_(j+1) = floor((c_j + k_j)/2^b) that stay below 2^(2b), processed from least to most significant.",
  ["radix-digit-convolution"],
  evidence=["Propagate radix-$2^b$ carries in increasing coefficient order"]),
C("fixed-exponent-choices", "Fixed rational exponent choices",
  "The fixed rational exponents τ = σ = 1 − 2^(−50), λ = 1 − 2^(−52), λ' = 1 − 2^(−54), c = 2^(−56), ε = 2^(−75) and κ = 2^(−182), chosen so that every cost term fits the target bound.",
  ["power-width-chunk-interchange", "simultaneous-butterfly-layer", "synthetic-transform-on-tapes"],
  evidence=["Take the following fixed rational numbers:"]),
C("size-parameters", "Size parameters for the input length",
  "The parameters derived from the input length n: b = ceil(log2 n), p = 6b, d = floor(b^ε), K = floor(d^c), a power of two T in [4n/b, 8n/b), and r = 2^(ceil(log2 T / d)), chosen so that T = r M and every axis length is r/2 or r.",
  ["fixed-exponent-choices", "radix-digit-convolution"],
  evidence=["Take the power of two $T$ in $[4n/b,8n/b)$"]),
C("digit-convolution-algorithm", "Multiplication algorithm by transforms",
  "The integer multiplication procedure: split both inputs into radix digits, apply the coordinate map, compute both source transforms, multiply pointwise, apply the opposite transform, scale and round the coefficients, and propagate carries.",
  ["source-transform", "source-permutation-cancellation", "crt-coefficient-map", "radix-digit-convolution", "size-parameters"],
  evidence=["The source-transform procedures now supply the three transforms needed"]),
C("precision-and-exact-recovery", "Precision and exact recovery",
  "The error analysis showing that every intermediate array stays in the disk and that the recovered coefficients have total error below one half, so rounding each coefficient gives the exact product.",
  ["digit-convolution-algorithm", "guard-bits", "carry-propagation", "grid-truncation"],
  evidence=["coefficient error is strictly below $1/2$"]),
C("cost-exponent-accounting", "Cost accounting for the dominant terms",
  "The accounting that writes every cost term as T p times a power of p, shows that each of the seven dominant exponents is at least 2κ below one, and so totals O(n (log n)^(1−κ)).",
  ["fixed-exponent-choices", "digit-convolution-algorithm", "precision-and-exact-recovery", "simultaneous-butterfly-layer", "power-width-chunk-interchange", "synthetic-transform-on-tapes", "source-transform", "ring-product"],
  evidence=["Each of the seven displayed powers is at most"]),

# ---------- target ----------
C("main-theorem", "Deterministic integer multiplication in O(n (lg n)^(1−κ)) time",
  "A single deterministic multitape machine with a fixed finite alphabet and a fixed finite number of tapes that multiplies two n-bit integers exactly in worst-case time O(n (lg n)^(1−κ)) with κ = 2^(−182), which refutes the n log n optimality conjecture in that model.",
  ["schonhage-strassen-conjecture", "fixed-tape-machine", "digit-convolution-algorithm", "precision-and-exact-recovery", "cost-exponent-accounting"],
  evidence=["There is one deterministic Turing machine $A$, with a fixed finite"],
  aliases=["main theorem", "Theorem 1"],
  title="Deterministic integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
  symbols=[B("O", "big-O bound", "The class of functions bounded above by a constant multiple of the given function for all sufficiently large inputs.", "direct"),
           B("n", "input length", "The number of bits in each of the two input integers.", "count"),
           B("\\lg", "binary logarithm", "The binary logarithm of n rounded up to an integer and at least one, lg n = max{ceil(log2 n), 1}.", "direct"),
           B("\\kappa", "saving exponent", "The fixed positive constant 2^(−182) by which the logarithmic exponent falls short of one.", "direct")]),
]

answer = {"target": "main-theorem", "concepts": concepts}

# ---------------- local checks ----------------
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", "", s)

src = norm(open(SRC, encoding="utf-8").read())
ids = [c["id"] for c in concepts]
problems = []
if len(ids) != len(set(ids)):
    problems.append("duplicate ids")
idset = set(ids)
for c in concepts:
    for r in c["requires"]:
        if r not in idset:
            problems.append(f"{c['id']} requires unknown {r}")
    if c["known"] and c["requires"]:
        problems.append(f"known concept {c['id']} has requires")
    if not c["known"] and not c["evidence"]:
        problems.append(f"unknown concept {c['id']} has no evidence")
    for e in c["evidence"]:
        if norm(e["quote"]) not in src:
            problems.append(f"quote not found for {c['id']}: {e['quote'][:60]}")
    if "$" in c["name"] or "\\" in c["name"]:
        problems.append(f"LaTeX in name of {c['id']}")
    if c.get("title") is None and re.search(r"\b(lg|log|O\(|\^|<|κ|Wm|y\^r)", c["name"]):
        problems.append(f"name of {c['id']} looks mathematical without title")
    if "title" in c:
        for sym in re.findall(r"\\?[A-Za-z]+|[A-Za-z]", c["title"].split("$")[1] if "$" in c["title"] else ""):
            pass
        bound = {b["symbol"] for b in c["symbols"]}
        math = c["title"][c["title"].index("$")+1:c["title"].rindex("$")]
        tokens = set(re.findall(r"\\[A-Za-z]+|(?<![\\A-Za-z])[A-Za-z](?![A-Za-z])", math))
        for t in tokens:
            if t not in bound and t not in ("lg",):
                problems.append(f"symbol {t} in title of {c['id']} not bound")
# cycle check
state = {}
def dfs(u, stack):
    state[u] = 1
    for v in next(x for x in concepts if x["id"] == u)["requires"]:
        if state.get(v) == 1:
            problems.append(f"cycle via {u} -> {v}")
        elif state.get(v) is None:
            dfs(v, stack)
    state[u] = 2
for c in concepts:
    if state.get(c["id"]) is None:
        dfs(c["id"], [])
if answer["target"] not in idset:
    problems.append("target not in ids")

print("concepts:", len(concepts), "known:", sum(c["known"] for c in concepts))
print("problems:", problems if problems else "none")
if not problems:
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(answer, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", OUT)
