import json, re, sys

SRC = open('/home/user/openai-nlogn-wiki/runs/P4/sources/paper.tex', encoding='utf-8').read()

C = []


def add(id, name, gloss, requires, quotes=(), known=False, aliases=(), title=None, symbols=None):
    d = {
        "id": id, "name": name, "aliases": list(aliases), "gloss": gloss,
        "requires": [] if known else list(requires), "known": known,
        "evidence": [{"source": "paper", "quote": q} for q in quotes],
    }
    if title:
        d["title"] = title
        d["symbols"] = symbols
    C.append(d)


def sym(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}


# ---- known
add("big-o", "Big-O notation", "Asymptotic upper bounds on running time such as O(n log n).", [], known=True)
add("polynomials", "Polynomials", "Sums of coefficients times powers of a variable, with addition and multiplication.", [], known=True)
add("complex-numbers", "Complex numbers", "Numbers a + bi with i² = −1, with modulus, conjugation and the unit-modulus numbers e^{iθ}.", [], known=True)
add("turing-tapes", "Turing machines and tapes", "A finite-state machine with read/write heads moving over one-dimensional tapes.", [], known=True)

# ---- model / conjecture
add("multitape-model", "Fixed-tape Turing machine model",
    "The paper's cost model: one fixed finite alphabet, a fixed finite number of one-dimensional tapes, each step reads/writes one cell per tape and moves each head by at most one cell, so moving data far costs time.",
    ["turing-tapes", "big-o"],
    ["A machine has one fixed finite alphabet and one fixed finite number of\none-dimensional tapes.",
     "A step reads and writes at most one cell on each\ntape and moves each head by at most one cell."])
add("nlogn-conjecture", "The n log n optimality conjecture",
    "Schönhage and Strassen's 1971 conjecture that Θ(n log n) is the optimal time to multiply two n-bit integers on a multitape Turing machine; Harvey and van der Hoeven reached O(n log n), and this paper refutes optimality.",
    ["big-o", "multitape-model"],
    ["disproves the $n\\log n$ optimality conjecture",
     "Sch\\\"onhage and Strassen conjectured $n\\log n$ as the optimal order of"])
add("established-multiplier", "Established near-linear integer multiplier",
    "The Harvey–van der Hoeven fixed-tape multiplier running in O(N log N) on N-bit inputs, used only as an ordinary subroutine on short records (it does not invoke the improved theorem).",
    ["multitape-model", "big-o"],
    ["$O(N\\log(2N))$ on $N$-bit inputs",
     "they do not invoke the improved theorem recursively."])

# ---- math background
add("linear-algebra-basics", "Matrices, rank, subspaces and projections",
    "Linear maps as matrices, rank, invertibility, lower-triangular matrices, subspaces, direct sums, and projection onto a subspace along a complement.",
    [],
    ["where $E_1,E_2$ are invertible lower triangular rational matrices and"])
add("tensor-products", "Tensor products of vectors, spaces and operators",
    "The tensor (Kronecker) product of vectors, spaces and operators, which acts factor by factor on coordinates of a multi-index.",
    ["linear-algebra-basics"],
    ["The ambient label space is $\\mathcal F=F^{\\otimes3}$ with its tensor"])
add("f2-vectors", "Binary vectors, XOR and Hamming weight",
    "Vectors over the two-element field with addition equal to XOR, dot product mod 2, and Hamming weight wt(x), the number of ones.",
    ["linear-algebra-basics"],
    ["denote its integer Hamming weight"])
add("bilinear-orthogonality", "Nondegenerate bilinear forms and orthogonal complements",
    "A symmetric bilinear form defines orthogonality; for a nondegenerate subspace the space splits as the subspace plus its orthogonal complement, and over F₂ a nonalternating form has an orthonormal basis.",
    ["linear-algebra-basics", "f2-vectors"],
    ["A label is a nondegenerate subspace of a fixed bilinear space."])

# ---- Fourier background
add("dft", "Discrete Fourier transform",
    "The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} on length-q vectors, together with its opposite-sign inverse-like partner F_q⁺.",
    ["complex-numbers", "polynomials"],
    ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q},"])
add("multidim-dft", "Multidimensional transform and cyclic convolution on a product of axes",
    "The tensor product of one-dimensional DFTs along several axes of a box of coordinates, acting on arrays indexed by a product of cyclic groups.",
    ["dft", "tensor-products"],
    ["F_{\\boldsymbol t}^\\pm=\\bigotimes_{i=1}^D F_{t_i}^\\pm,"])
add("cyclic-convolution", "Cyclic convolution and the convolution theorem",
    "Convolution of arrays indexed by cyclic groups; the DFT turns it into pointwise multiplication (up to normalization), so convolution can be computed by transform, pointwise product, inverse transform.",
    ["dft", "multidim-dft"],
    ["cyclic convolution on the product of the coordinate groups"])
add("fft-butterfly", "Butterfly step and decimation-in-frequency recursion",
    "The two-point step H₀(u,v) = ((u+v)/2,(u−v)/2) paired with a twiddle multiplication; applying it recursively on halves computes a length-2^a transform in a levels.",
    ["dft"],
    ["decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"])
add("multiplication-as-convolution", "Integer multiplication as convolution of radix digits",
    "Writing each integer as a polynomial in a radix 2^b with small digits, the product's digit coefficients are the (non-wrapping) convolution of the digit lists, followed by carry propagation.",
    ["cyclic-convolution", "polynomials"],
    ["Splitting the inputs into radix digits reduces multiplication to",
     "Write the two inputs as polynomials in $2^b$, each with"])
add("contraction-error-budget", "Max-modulus norm, contractions and error propagation",
    "Under the maximum-modulus norm, normalized transforms and permutations are contractions (never increase norm), so approximation errors of composed steps add up without amplification.",
    ["complex-numbers"],
    ["The vector norm is the maximum modulus of its coordinates.",
     "Composing such algorithms\nadds their errors"])
add("disk-grid-truncation", "Disk grid and truncation",
    "Fixed-point complex numbers with p fractional bits inside the unit disk, and the operator that truncates real and imaginary parts toward zero to that grid, never increasing norm and causing error below √2·2^{−p}.",
    ["contraction-error-budget"],
    ["\\mathbb D_p=\\{2^{-p}(a+ib):a,b\\in\\mathbb Z,\\ a^2+b^2\\leq 2^{2p}\\}",
     "let $Q_p$ truncate each real and\nimaginary coefficient part toward zero to this grid"],
    title="Disk grid $\\mathbb D_p$ and truncation $Q_p$",
    symbols=[sym("p", "precision bits", "the number of fractional bits kept in each real or imaginary part", "count"),
             sym("\\mathbb D_p", "p-bit disk grid", "the set of complex numbers 2^{-p}(a+ib) with integers a,b lying in the closed unit disk"),
             sym("Q_p", "truncation operator", "the map that truncates the real and imaginary parts of each coefficient toward zero to multiples of 2^{-p}")])
add("fixed-point-arithmetic", "Streaming fixed-point and Gaussian dyadic arithmetic",
    "Signed two's-complement fixed-point addition, sign change, halving and multiplication by i on tapes in linear bit time, kept exact by reserving guard bits; values are Gaussian dyadics (complex numbers with power-of-two denominators).",
    ["multitape-model"],
    ["are streaming operations of linear bit cost",
     "Intermediate values are exact Gaussian dyadics,"])

# ---- tape array basics
add("address-fields-volume", "Arrays, address fields, rows and logical volume",
    "Arrays on a product of ranges [a₁]×…×[a_t] are stored in lexicographic order with implicit addresses; V is the number of stored bits, and a row is the full block at a fixed prefix and row index.",
    ["multitape-model"],
    ["The \\emph{logical volume} $V$ is the number of stored data bits.",
     "is stored in\nlexicographic order, with the first coordinate most significant."])
add("stream-ops", "Linear-time stream operations",
    "Splitting a stream on a digit, applying a fixed pointwise map to aligned streams, merging, moving one digit, and splitting rows cyclically into W streams all cost O(V) on a fixed number of tapes.",
    ["address-fields-volume"],
    ["takes $O(V)$ steps on a fixed number of one-dimensional tapes"])
add("controlled-shifts", "Controlled cyclic shifts and rational scalings",
    "Updating a target field y ↦ y + a(controls) mod Q, with the controls earlier on the tape than the target, costs O(V) by splitting and re-merging blocks; multiplication by rational units mod q^b is also linear.",
    ["stream-ops"],
    ["y\\longmapsto y+a(\\text{controls})\\pmod Q"])
add("fixed-tape-dfs-schedule", "Depth-first recursion schedule on fixed tapes",
    "Recursive calls on W role streams are run on one fixed set of tapes by parking the inactive streams on a stack, copying the active stream to the child, and restoring afterwards, costing O(V) per node.",
    ["stream-ops", "multitape-model"],
    ["A fixed-tape depth-first schedule.",
     "Before a recursive call, append the $W-1$ inactive role streams to the\nparking stack in a fixed order, with separators."])

# ---- the finite networks
add("subset-pairing-formulas", "Triple-intersection pairing formulas",
    "Using indicator vectors of three-element subsets of a 100-element set, intersection sizes appear as bilinear pairings (|S∩T|−1 over the rationals, |S∩T| mod 2 over F₂), following Alon's presentation of Frankl–Wilson.",
    ["bilinear-orthogonality", "f2-vectors"],
    ["\\langle t_S,t_T\\rangle=|S\\cap T|-1,",
     "At the prime $p=2$, its subsets have size three"])
add("scalar-exchange-network", "Linear network exchanging two banks with restored scratch",
    "A fixed network of linear gates (copy, gather, scatter, side injection) on banks X and Y that sends (X,Y) to (−Y,X) in three stages while restoring every auxiliary scratch wire to its arbitrary initial value.",
    ["linear-algebra-basics", "f2-vectors", "subset-pairing-formulas"],
    ["a forward\ninvocation changes $y_S$ to $y_S+x_S$ and leaves every other value\nunchanged",
     "(X_a,Y_a)\\longmapsto(-Y_a,X_a)"])
add("network-frames", "Frames and the common-frame identity",
    "Replace each wire's scalar by an array and give each gate/terminal an invertible frame operator; since a common frame commutes with pointwise linear gates, the whole network acts as D_out S D_in⁻¹, so only endpoint frames matter and each edge can be implemented by D_v D_u⁻¹.",
    ["scalar-exchange-network", "linear-algebra-basics"],
    ["At a pointwise linear gate $G$, the common frame commutes with the gate:",
     "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}."])
add("subspace-labels-rank-saving", "Nested subspace labels and the rank deficit",
    "Gates and terminals are labeled by nested subspaces of an m-dimensional space built from tensor powers of triple indicator vectors; the total dimension change over edges is below W·m (W = number of wires), which is the strict saving that powers the recursion.",
    ["subset-pairing-formulas", "network-frames", "tensor-products", "bilinear-orthogonality"],
    ["The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$.",
     "the \\emph{orthogonal residual} is the orthogonal complement of the smaller label inside\nthe larger one"])
add("address-shear", "Address shear",
    "The invertible permutation of array entries sending address (H,D) to (H+MD,D) for a matrix M, which composes additively and, combined with two linear-cost updates, interchanges the H and D fields.",
    ["address-fields-volume", "controlled-shifts", "linear-algebra-basics"],
    ["the frame $\\Phi_M$ moves the array entry\nat $(H,D)$ to $(H+MD,D)$",
     "$\\Phi_{M'}\\Phi_M=\\Phi_{M'+M}$"])
add("bit-network-interface", "Bit network and rational shear interface",
    "The bit-valued network (XOR gates, W_b wires) with rational projection matrices on gates so that every route's endpoint difference is the identity (the shear H ← H+D) while the total rank of edge differences s_b is below W_b·m.",
    ["subspace-labels-rank-saving", "network-frames", "address-shear"],
    ["The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",
     "M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m"])
add("phase-kernel", "Phase kernel C = aI + bX",
    "The two-point Gaussian dyadic kernel C = H S H = aI + bX with a=(1+i)/2, b=(1−i)/2, satisfying C²=X, C⁴=I, C⁻¹ = −iZCZ and H₀ = b S C S, which relates a normalized butterfly to C.",
    ["complex-numbers", "linear-algebra-basics", "fft-butterfly"],
    ["C=H\\mathsf SH=aI+bX",
     "H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad"],
    title="Phase kernel $C = aI + bX$",
    symbols=[sym("C", "phase kernel", "the two-by-two matrix H S H acting on one selected bit"),
             sym("a", "kernel coefficient a", "the complex number (1+i)/2 multiplying the identity"),
             sym("b", "kernel coefficient b", "the complex number (1−i)/2 multiplying the bit flip"),
             sym("I", "identity matrix", "the two-by-two identity matrix"),
             sym("X", "bit-flip matrix", "the two-by-two matrix interchanging the two coordinates")])
add("complex-network-interface", "Complex phase network interface",
    "The Gaussian-dyadic version of the network with binary-vector labels and phase frames i^{wt(P_U x) mod 4}; each edge's frame change is a product of translation kernels aI+bX_v over an orthonormal basis of the residual, and telescoping gives C^{⊗m} on every role with total length s_c below W_c·m.",
    ["subspace-labels-rank-saving", "network-frames", "phase-kernel", "f2-vectors", "bilinear-orthogonality"],
    ["is a product of one translation\nkernel $aI+bX_v$",
     "telescoping these phase frames gives $C^{\\otimes m}$\non every role"])

# ---- fast interchange
add("lower-factorization", "Lower-triangular factorization of a matrix",
    "Every rational matrix A of rank a factors as E₁ Π E₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones (a Bruhat-type factorization in reversed coordinate order).",
    ["linear-algebra-basics"],
    ["\\begin{lemma}[Lower triangular factorization]",
     "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])
add("matrix-shear-cost", "Cost of a rational matrix shear",
    "The shear (H,D)↦(H+AD,D) of rank a is performed with exactly a interchanges of b-digit fields plus O(V) further work, using triangular factors as linear-time controlled shifts and one interchange per pivot.",
    ["lower-factorization", "address-shear", "controlled-shifts"],
    ["can be performed with exactly $a$ interchanges of pairs of $b$-digit\nfields and $O(V)$ further work"])
add("rank-deficit-recurrence", "Strict rank deficit gives a power saving",
    "If a call at parameter m·f makes s calls at parameter f, each on a stream of volume V/W, then normalized cost obeys F_k ≤ (s/W)F_{k−1}+O(1); since s/W < m^τ with τ<1 the solution is O(e^τ), a power-of-the-width saving.",
    ["big-o", "subspace-labels-rank-saving"],
    ["F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
     "This strict inequality\nis the source of the power saving."])
add("row-splitting-roles", "Rows distributed cyclically among wire roles",
    "To run the network on an array, whole rows are dealt cyclically into W role streams (padding the row count to a multiple of W per prefix), each of volume V/W with identical remaining shape, and gates act pointwise on matching addresses.",
    ["stream-ops", "scalar-exchange-network", "network-frames"],
    ["Distribute rows cyclically among the $W$ roles, padding the row count\nfor each prefix to a multiple of $W$."])
add("power-width-interchange", "Power-width interchange with rows",
    "Using the bit network on W role streams with address shears applied recursively on every edge, two chunks of e = m^k digits are interchanged in O(V e^τ) time, via the XOR combinations of intermediate data whose net effect is an exact permutation.",
    ["bit-network-interface", "matrix-shear-cost", "row-splitting-roles", "rank-deficit-recurrence", "fixed-tape-dfs-schedule"],
    ["The chunks can be interchanged in $O(Ve^\\tau)$ time",
     "Although its final effect is an exact permutation, its intermediate\nsteps form pointwise XOR combinations of data."])
add("chunk-swap", "Fast address-chunk interchange",
    "Arbitrary-width interchange of two disjoint address chunks of u bits in O(V u^τ) with fixed τ<1: peel off top digits to supply rows, pad rows, decompose the rest in base m and apply the power-width interchange to each piece.",
    ["power-width-interchange", "stream-ops", "address-fields-volume"],
    ["in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.",
     "The first procedure interchanges two disjoint contiguous address fields\nof $u$ bits in an array whose addresses form a complete Cartesian\nproduct."])

# ---- fast butterfly layers
add("packed-rotations", "Carry-free packed controlled rotations",
    "Eight cyclic shifts of whole chunk ranges, conditioned on parities and a control bit, flip the parity of u when the control is 1 and restore the auxiliary w, so that XORs on f selected bit positions can be done at once as long as the K-bit segments have unused guard room.",
    ["controlled-shifts", "chunk-swap"],
    ["the first four operations\ninduce the cycle $(00\\ 01\\ 10)$ in every square",
     "y\\longleftarrow y+\n \\varepsilon\\sum_{i=0}^{f-2}2^{j_i}"])
add("exceptional-address-repair", "Deterministic repair of exceptional addresses",
    "The packed rotations fail only on a set of addresses whose guard values are near the segment boundary, a fraction at most 80(f−1)2^{−K} of all addresses; these records are extracted, sorted by destination rank with stable radix sort, and reinserted, keeping the bound worst-case.",
    ["packed-rotations", "stream-ops"],
    ["stable binary radix sorting scans only the extracted records and\nkeys",
     "$|\\mathcal B|\\le\\delta_{\\rm bad}M.$"][:1] + ["10\\le g\\le 2^{K-1}-11."])
add("packed-selected-bit-addition", "Packed selected-bit addition on one rectangle",
    "One fixed multitape procedure XORs the selected bit (offset ρ of each of f chunks of K bits) of chunk x into chunk y while restoring chunk z, in time O(V(L^τ+1)) plus negligible repair terms; this performs a binary row addition used for change of basis.",
    ["packed-rotations", "exceptional-address-repair", "chunk-swap"],
    ["Packed selected-bit addition on one rectangle",
     "y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}"])
add("guard-width", "Guard width for exact intermediate values",
    "The whole recursive C-layer is evaluated exactly with p + Δ fractional bits and Δ + 3 integer bits, where Δ = ⌈C₀ d^{C₁}⌉ bounds the arithmetic depth via A(e) ≤ sA(e/m)+E; since ε·C₁<1, Δ = o(p) and widths stay O(p).",
    ["fixed-point-arithmetic", "complex-network-interface", "disk-grid-truncation", "rank-deficit-recurrence"],
    ["represents every intermediate coefficient exactly",
     "A(e)\\le sA(e/m)+E"])
add("phase-frame-layer", "Recursive phase-frame layer on slots",
    "To apply C^{⊗e} on e = m·f selected bits, group the bits into m slots of f chunks, change binary basis by packed row additions, apply the f-fold inverse or forward child on each residual-basis slot (s_c children in total), and change back; inverses cost no extra child since C⁻¹ = −iZCZ.",
    ["complex-network-interface", "phase-kernel", "packed-selected-bit-addition", "f2-vectors"],
    ["Summing its residual dimensions gives exactly\n$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
     "(C^{-1})^{\\otimes f}\n =(-i)^f Z^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}."])
add("simultaneous-layer", "Simultaneous normalized butterfly layer",
    "H₀ is applied at once to the same bit offset of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) time with λ'<1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase-frame layer on rows split among wire roles, exact evaluation and one final truncation.",
    ["phase-frame-layer", "row-splitting-roles", "guard-width", "rank-deficit-recurrence", "fixed-tape-dfs-schedule", "disk-grid-truncation", "polynomial-ring-negacyclic", "fft-butterfly"],
    ["Simultaneous normalized butterfly layer",
     "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."])

# ---- synthetic transforms
add("polynomial-ring-negacyclic", "Polynomial ring modulo y^r + 1",
    "Polynomials with complex coefficients of degree below r, with y^r = −1; multiplying by a power y^a is an exact signed cyclic shift of the coefficient list (an isometry), and the wrap-around carries a minus sign (negacyclic).",
    ["polynomials", "complex-numbers"],
    ["\\mathcal R_r=\\mathbb C[y]/(y^r+1)",
     "permutes the coefficients and changes\nsome signs"],
    title="Polynomial ring modulo $y^r + 1$",
    symbols=[sym("y", "ring variable", "the indeterminate of the polynomial ring, satisfying y^r = −1"),
             sym("r", "polynomial length", "the number of complex coefficients in a record, a power of two", "count")])
add("synthetic-roots", "Synthetic root of unity ω_t = y^{2r/t}",
    "Powers of y serve as roots of unity of order t dividing 2r in the ring modulo y^r+1, so multiplying by ω_t^j costs only a signed shift of the coefficient list.",
    ["polynomial-ring-negacyclic", "dft"],
    ["define $\\omega_t=y^{2r/t}$"],
    title="Synthetic root of unity $\\omega_t = y^{2r/t}$",
    symbols=[sym("\\omega_t", "synthetic root", "the element y^{2r/t} acting as a primitive t-th root of unity in the ring"),
             sym("t", "transform length", "the length of the axis, a power of two dividing 2r", "count"),
             sym("y", "ring variable", "the indeterminate of the polynomial ring, satisfying y^r = −1"),
             sym("r", "polynomial length", "the number of complex coefficients in a record, a power of two", "count")])
add("synthetic-transform", "Synthetic polynomial transform",
    "The normalized transforms F_t^± over the polynomial ring using synthetic roots, computed by radix-two butterflies plus monomial twiddles (Nussbaumer–Quandalle); character cancellation gives F⁺F⁻ = I/t even though the ring has zero divisors.",
    ["synthetic-roots", "fft-butterfly", "multidim-dft"],
    ["synthetic polynomial transforms of Nussbaumer and Quandalle",
     "Synthetic character cancellation"])
add("frequency-order", "Retained stored frequency order",
    "The decimation-in-frequency recursion writes frequency j in slot rev(j) (bit-reversed); the forward transform B·F⁻ keeps this order and the opposite procedure consumes it directly, so no sort is needed between the pointwise product and the inverse.",
    ["synthetic-transform"],
    ["the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$."])
add("transform-layout", "Transform layout and cost",
    "A positional permutation L moves chosen bit slots to a prefix and groups the remaining bits into K-bit chunks so each transform round is a simultaneous butterfly layer; cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2·ℓ·2^{−p}.",
    ["simultaneous-layer", "chunk-swap", "synthetic-transform", "frequency-order", "disk-grid-truncation"],
    ["layout permutation $L$ of record addresses",
     "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right)."][:1] + ["Transform layout and cost"])
add("signed-packing", "Signed Kronecker packing for ring products",
    "Two disk-grid polynomials in the ring mod y^r+1 are multiplied exactly by evaluating coefficients at B₀=2^{4p} as signed integers, multiplying with the established multiplier, extracting centered coefficients, wrapping negacyclically and truncating, in O(rp log(rp)).",
    ["established-multiplier", "polynomial-ring-negacyclic", "disk-grid-truncation"],
    ["The reduction is a signed form of Kronecker substitution",
     "Signed packing and normalized ring multiplication"][:1] + ["time\n$O(rp\\log(rp))$ on a fixed number of tapes."])
add("synthetic-convolution", "Convolution from the retained transform layout",
    "Normalized convolution over the polynomial ring: two forward synthetic transforms keep their layout, records are multiplied pointwise by signed packing, and the opposite transform consumes the same order; error below √2·M(3ℓ+1)2^{−p}.",
    ["transform-layout", "signed-packing", "cyclic-convolution", "frequency-order", "contraction-error-budget"],
    ["Convolution from the retained transform layout",
     "Perform both forward transforms and retain their common $LB$ order."])
add("coefficient-twist", "Coefficient twist from cyclic to negacyclic",
    "The isomorphism x_d ↦ ζy with ζ = e^{πi/r} sends cyclic convolution of length r to the ring modulo y^r+1, multiplying coefficient k by ζ^k; the negative wrap exactly cancels the factor ζ^r, so untwisting recovers the cyclic result.",
    ["polynomial-ring-negacyclic", "cyclic-convolution", "complex-numbers"],
    ["is well defined, since $(\\zeta y)^r=(-1)(-1)=1$",
     "Untwisting therefore recovers the cyclic coefficient with the correct\nsign."])

# ---- resampling
add("gaussian-resampling", "Gaussian resampling with retained permutations",
    "Harvey–van der Hoeven resampling replaces a Fourier transform of coprime length s by one of length t (a power of two) using Gaussian-weighted maps A and B₀; here the two coordinate permutations stay in the identity P_s F_s = 2^{2α²} B₀ P_t F_t A instead of being executed as sorts.",
    ["dft", "contraction-error-budget", "disk-grid-truncation"],
    ["Gaussian resampling\nconnects these two shapes.",
     "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."])
add("tensor-resampling", "Tensor interface for resampling",
    "The resampling identity is applied along each of d axes (lines) of a padded power-of-two box, with axes exposed and restored by chunk interchanges; total cost O(dTp^{3/2+δ}α) for the line maps plus O(Tp d²(1+ℓ^τ)) for data movement.",
    ["gaussian-resampling", "multidim-dft", "chunk-swap", "address-fields-volume"],
    ["RF_{\\boldsymbol s}\n   =2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,",
     "Suppose every pair $(s_i,t_i)$, $1\\leq i\\leq d$, satisfies"][:1])
add("bluestein-chirp", "Bluestein chirp identity",
    "A DFT (here with a frequency permutation) equals pre-multiplication by a chirp phase, a cyclic convolution with the chirp, and post-multiplication by the conjugate chirp, so the middle transform becomes a normalized cyclic convolution.",
    ["cyclic-convolution", "multidim-dft"],
    ["Bluestein's chirp identity converts the middle transform,"])
add("source-permutation-cancel", "Cancellation of the source permutation",
    "The permutation R retained from resampling cancels across the two forward source transforms, their pointwise product and the opposite-sign transform: (R F⁺)[(R F u)·(R F v)] = (u*v)/S².",
    ["gaussian-resampling", "cyclic-convolution", "multidim-dft"],
    ["the source permutation retained during resampling cancels"])
add("crt-address-map", "Chinese-remainder map to prime cyclic axes",
    "With pairwise coprime lengths s_i, the map x ↦ ∏ x_i^{μ_i} is an isomorphism from cyclic convolution of length ∏s_i to multidimensional cyclic convolution on the prime axes, implemented by triangular controlled shifts on padded axes.",
    ["cyclic-convolution", "multidim-dft", "controlled-shifts", "chunk-swap"],
    ["Agarwal and Cooley used the Chinese remainder\ntheorem to convert one cyclic convolution into multidimensional cyclic\nconvolution",
     "x\\longmapsto\\prod_i x_i^{\\mu_i}"])
add("chirp-transform", "Middle transform computed by chirp and complex convolution",
    "The padded power-of-two transform Q F_t is computed by chirp phase products, a complex cyclic convolution obtained through the coefficient twist and synthetic convolution, and a final chirp product, with error below 8TL·2^{−p}.",
    ["bluestein-chirp", "coefficient-twist", "synthetic-convolution", "disk-grid-truncation"],
    ["normalized complex cyclic\nconvolution is",
     "Thus $\\widetilde a$ is the convolution kernel"])
add("source-transform", "Source transform procedure",
    "The computed transform of a prime-axes source array: expand axes by A, apply the chirp transform on power-of-two axes, compress with B₀, and scale by 2^γ; its exact counterpart is R F_s, and the opposite-sign version is obtained by conjugation.",
    ["tensor-resampling", "chirp-transform", "source-permutation-cancel"],
    ["its exact counterpart is\n\\[\n \\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A"][:0] + ["apply the linewise\napproximation to $\\mathcal A$, apply the\ncomputed chirp transform $\\widetilde{\\mathscr C}$"])

# ---- parameters and assembly
add("parameter-choice", "Size parameters of the algorithm",
    "From the input length n: b = ⌈log₂ n⌉, working precision p = 6b, number of axes d = ⌊b^ε⌋, chunk width K = ⌊d^c⌋, padded box size T ≈ n/b, axis lengths r or r/2, resampling parameter α, with fixed tiny rationals ε, c, τ, λ', δ.",
    ["multiplication-as-convolution", "polynomial-ring-negacyclic", "gaussian-resampling", "simultaneous-layer"],
    ["b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
     "\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16},"])
add("prime-lengths", "Distinct prime source lengths near powers of two",
    "Pairwise-distinct odd primes s_i with (1−2η)t_i < s_i ≤ (1−η)t_i are found by trial division; they give gcd(s_i,t_i)=1, T/2 < S < T and the separation t_i/s_i − 1 needed by Gaussian resampling.",
    ["parameter-choice", "gaussian-resampling", "crt-address-map"],
    ["contains at least $\\eta x/(2\\log x)$ primes"])
add("exact-recovery", "Exact recovery by rounding and carry propagation",
    "The scaled computed convolution has error below 1/2, so rounding each real part to the nearest integer yields the true integer coefficients, and radix carries propagated least significant first produce the exact 2n-bit product.",
    ["disk-grid-truncation", "contraction-error-budget", "multiplication-as-convolution", "source-permutation-cancel"],
    ["The strict error\nbound makes the result the correct nonnegative coefficient",
     "To propagate carries, let $Q_0=2^b$."])
add("multiplication-algorithm", "The complete multiplication algorithm",
    "Convert the inputs to radix digits, apply the CRT map to prime axes, compute the two source transforms, multiply pointwise, compute the opposite transform, rescale by S and 2^{2b+4}, round, undo the CRT map and propagate carries to output the exact product.",
    ["crt-address-map", "source-transform", "parameter-choice", "prime-lengths", "exact-recovery", "multiplication-as-convolution", "disk-grid-truncation"],
    ["Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain",
     "Propagate radix-$2^b$ carries in increasing coefficient order."])
add("cost-analysis", "Cost analysis and the exponent κ",
    "Dividing all costs by Tp = Θ(n) gives a table of seven dominant terms whose powers of p are all at most 1 − 2κ for κ = 2^{−182}, so the total is O(n (lg n)^{1−κ}) with schoolbook multiplication for small inputs.",
    ["chunk-swap", "simultaneous-layer", "transform-layout", "tensor-resampling", "chirp-transform", "signed-packing", "crt-address-map", "parameter-choice"],
    ["Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
     "Each of the seven displayed powers is at most $1-2\\kappa$ by"])

# ---- target
add("main-theorem", "Integer multiplication in O(n (lg n)^(1−κ)) time",
    "A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, by reducing to convolution over the polynomial ring with fast chunk interchanges and simultaneous butterfly layers, disproving the n log n optimality conjecture.",
    ["multiplication-algorithm", "cost-analysis", "nlogn-conjecture", "multitape-model"],
    ["We give a deterministic algorithm that multiplies two $n$-bit integers\nin $O(n(\\lg n)^{1-\\kappa})$ worst-case time, with\n$\\kappa=2^{-182}$",
     "T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right),"],
    title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
    symbols=[sym("n", "input length", "the number of bits in each of the two integers being multiplied", "count"),
             sym("\\kappa", "saving exponent", "the fixed constant 2^{-182} giving the power saving in the logarithmic factor")])

# ----- validate
ids = {c["id"] for c in C}
assert len(ids) == len(C), "dup ids"
for c in C:
    for r in c["requires"]:
        assert r in ids, (c["id"], r)


def norm(s):
    return re.sub(r'\s+', '', s)


NS = norm(SRC)
bad = 0
for c in C:
    if not c["known"] and not c["evidence"]:
        print("no evidence", c["id"]); bad += 1
    for e in c["evidence"]:
        if norm(e["quote"]) not in NS:
            print("MISSING", c["id"], repr(e["quote"])); bad += 1
# cycles
state = {}
byid = {c["id"]: c for c in C}
def dfs(u, path):
    if state.get(u) == 1:
        print("CYCLE", path + [u]); return
    if state.get(u) == 2: return
    state[u] = 1
    for v in byid[u]["requires"]: dfs(v, path + [u])
    state[u] = 2
for u in ids: dfs(u, [])
print("concepts", len(C), "bad", bad)
json.dump({"target": "main-theorem", "concepts": C}, open('/home/user/openai-nlogn-wiki/runs/P4/exegenius/tasks/0001-extract.answer.json', 'w'), indent=1, ensure_ascii=False)
