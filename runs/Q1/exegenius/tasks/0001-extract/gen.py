import json

P = "paper"
concepts = []


def c(id, name, gloss, requires, quotes, known=False, aliases=(), title=None, symbols=None):
    d = {
        "id": id,
        "name": name,
        "aliases": list(aliases),
        "gloss": gloss,
        "requires": list(requires),
        "known": known,
        "evidence": [{"source": P, "quote": q} for q in quotes],
    }
    if title:
        d["title"] = title
        d["symbols"] = [
            {"symbol": s, "name": n, "meaning": m, "relation": r} for (s, n, m, r) in symbols
        ]
    concepts.append(d)


# ---------------- known ----------------
c("big-o", "Big-O notation",
  "Asymptotic notation O(·), Ω(·), o(·) bounding a function's growth up to constant factors for large inputs.",
  [], [], known=True)
c("polynomials", "Polynomials",
  "Expressions Σ aⱼxʲ with coefficients in a ring, added and multiplied coefficientwise and by convolution of coefficient lists.",
  [], [], known=True)
c("complex-numbers", "Complex numbers",
  "Numbers a + bi with i² = −1, including roots of unity e^{2πij/k} and the modulus |z|.",
  [], [], known=True)
c("multitape-tm", "Multitape Turing machine",
  "A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step reading, writing and moving every head by at most one cell.",
  [], [r"A step reads and writes at most one cell on each tape and moves each head by at most one cell."],
  known=True, aliases=["fixed finite-tape model"])

# ---------------- background mathematics ----------------
c("modular-arithmetic", "Modular arithmetic and finite fields",
  "Arithmetic in residue rings ℤ/qᵇℤ and in the two-element field 𝔽₂, where addition is XOR, used both for address fields and for scalar values.",
  [], [r"The fields use a radix coprime to the fixed denominators, and addition is modulo their common range.",
       r"In the bit construction, scalars lie in $\mathbb F_2$"],
  aliases=["F_2", "residue ring"])
c("linear-algebra", "Linear maps, matrices and rank",
  "Vector spaces over a field, linear maps represented by matrices, invertibility, and the rank of a matrix as the dimension of its image.",
  [], [r"The sum of the rational ranks of all edge differences is",
       r"An edge matrix of rank $a$ will require $a$ smaller interchanges."],
  aliases=["rational rank"])
c("tensor-product", "Tensor products",
  "The tensor product of vector spaces or linear maps, so that an operator on a multi-index array acting as A₁ ⊗ … ⊗ A_d applies Aᵢ independently along each coordinate.",
  ["linear-algebra"],
  [r"The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor bilinear form.",
   r"every frame and edge operator is then the tensor product of its one-column version over these $k$ coordinates."],
  aliases=["tensor power"])
c("bilinear-forms", "Nondegenerate bilinear forms and orthogonal complements",
  "A symmetric bilinear form ⟨x, y⟩ on a vector space, nondegenerate when only 0 is orthogonal to everything, together with orthogonal complements U^⊥ and orthogonal direct sums U ⊥ E.",
  ["linear-algebra", "modular-arithmetic"],
  [r"A label is a nondegenerate subspace of a fixed bilinear space.",
   r"This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate."],
  aliases=["orthogonal complement", "orthonormal basis"])

# ---------------- problem and history ----------------
c("nlogn-conjecture", "The n log n conjecture",
  "Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.",
  ["big-o", "multitape-tm"],
  [r"and proposed $n\log n$ as the optimal order of growth",
   r"Sch\"onhage and Strassen conjectured $n\log n$ as the optimal order of multiplication cost"],
  aliases=["Schönhage–Strassen conjecture", "n log n optimality conjecture"])
c("hvdh-multiplier", "Harvey–van der Hoeven O(n log n) multiplier",
  "The established deterministic multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records.",
  ["nlogn-conjecture", "multitape-tm"],
  [r"Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound",
   r"Calls to the established $O(n\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively."],
  aliases=["established multiplier"])

# ---------------- Fourier and convolution ----------------
c("cyclic-convolution", "Cyclic convolution",
  "The product of polynomials modulo xˢ − 1 (or of arrays on a product of cyclic groups ℤ/tᵢℤ), where indices add with wraparound.",
  ["polynomials"],
  [r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
   r"let $*$ denote cyclic convolution in the displayed axes"])
c("dft", "Normalized discrete Fourier transform",
  "The map (F_q u)_k = (1/q) Σⱼ uⱼ e^{−2πijk/q} and its opposite-sign version F_q⁺, extended to several axes by tensor products, which turns cyclic convolution into pointwise products.",
  ["complex-numbers", "cyclic-convolution", "tensor-product"],
  [r"Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one.",
   r"The normalized convolution rule is"],
  aliases=["DFT", "normalized Fourier transform", "multidimensional transform"])
c("radix-reduction", "Radix-digit reduction",
  "Writing each n-bit input as a polynomial in 2ᵇ with b-bit digits, so the product is recovered from the integer convolution of the digit lists followed by carry propagation.",
  ["polynomials", "cyclic-convolution"],
  [r"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
   r"Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits.",
   r"Propagate radix-$2^b$ carries in increasing coefficient order."],
  aliases=["radix-digit polynomials", "carry propagation"])

# ---------------- tape model ----------------
c("array-layout", "Lexicographic array layout and logical volume",
  "Arrays on address sets [a₁]×…×[a_t] stored on tape in lexicographic order with implicit addresses, with cost measured relative to the logical volume V (number of stored data bits).",
  ["multitape-tm", "big-o"],
  [r"An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in lexicographic order, with the first coordinate most significant.",
   r"The \emph{logical volume} $V$ is the number of stored data bits."],
  aliases=["address field", "logical volume", "row"])
c("elementary-streams", "Elementary stream operations",
  "Linear-time O(V) tape scans that permute or move single radix-q digits of addresses, apply fixed pointwise maps to split streams, and split or merge whole rows cyclically into a fixed number of streams.",
  ["array-layout"],
  [r"Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes",
   r"moving one specified radix-$q$ digit to another position, preserving the order of the intervening positions"])
c("controlled-shifts", "Controlled shifts and rational scalings",
  "O(V) tape procedures that add to an address field y an offset computed from earlier control fields modulo Q = qᵇ, or multiply y by a fixed rational unit, by splitting each fiber into pieces and merging them in a new order.",
  ["elementary-streams", "modular-arithmetic"],
  [r"The next operations are linear because their target field follows their control fields.",
   r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values."],
  aliases=["prefix-controlled cyclic shift", "triangular update"])

# ---------------- numerics ----------------
c("fixed-point", "Gaussian dyadic fixed-point arithmetic",
  "Complex numbers whose real and imaginary parts have power-of-two denominators, stored as fixed-width two's-complement numerators on the p-bit disk grid, with truncation Q_p toward zero to 2^{−p}ℤ.",
  ["complex-numbers"],
  [r"Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators.",
   r"A disk array has norm at most one."],
  aliases=["disk grid", "Q_p truncation", "Gaussian dyadics"])
c("contraction-errors", "Contractions and error accounting",
  "Linear maps of operator norm at most one do not amplify errors, so errors of approximate algorithms for contractions (and bilinear contractions) simply add when composed.",
  ["fixed-point", "linear-algebra"],
  [r"Composing such algorithms adds their errors: at each step, insert the exact map at the computed input and use its contraction bound on the accumulated input error.",
   r"A linear contraction propagates an input error without increasing it."])

# ---------------- algebraic objects for transforms ----------------
c("negacyclic-ring", "Polynomial ring modulo yʳ + 1",
  "The ring ℂ[y]/(yʳ + 1) with r a power of two, in which y is a primitive 2r-th root of unity and multiplication by a power of y is a signed cyclic shift of the coefficient list.",
  ["polynomials", "complex-numbers"],
  [r"one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two.",
   r"Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list."],
  aliases=["negacyclic ring", "R_r"],
  title=r"Polynomial ring modulo $y^r + 1$",
  symbols=[("y", "polynomial variable", "The indeterminate of the ring, whose powers act as roots of unity of order 2r.", "direct"),
           ("r", "record length", "The number of complex coefficients in a polynomial record, a power of two.", "count")])
c("normalized-butterfly", "Normalized butterfly H₀",
  "The two-point map H₀(u, v) = ((u + v)/2, (u − v)/2), the radix-two butterfly of the transforms, which is a contraction with H₀² = I/2.",
  ["complex-numbers"],
  [r"of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits",
   r"In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations."],
  aliases=["butterfly", "Hadamard butterfly"],
  title=r"Normalized butterfly $H_0$",
  symbols=[("H_0", "normalized butterfly", "The 2×2 matrix ½[[1, 1], [1, −1]] sending a pair (u, v) to ((u + v)/2, (u − v)/2).", "direct")])
c("kernel-c", "Two-point kernel C",
  "The Gaussian-dyadic 2×2 kernel C = H·diag(1, i)·H = aI + bX with a = (1 + i)/2, b = (1 − i)/2, satisfying C⁴ = I and H₀ = b·S·C·S, so a layer of H₀ equals a layer of C up to diagonal phases and a scale.",
  ["normalized-butterfly", "tensor-product"],
  [r"auxiliary two-point kernel $C$",
   r"In particular, $C=iZC^{-1}Z$."],
  aliases=["translation kernel", "aI+bX"],
  title=r"Two-point kernel $C$",
  symbols=[("C", "two-point kernel", "The 2×2 complex matrix aI + bX with a = (1 + i)/2, b = (1 − i)/2 and X the coordinate swap.", "direct")])

# ---------------- finite networks ----------------
c("linear-network", "Linear network with wire roles",
  "A fixed finite circuit of wires each carrying one scalar, with gates that apply fixed linear maps to the wires they touch; a wire's fixed place in the network is its role.",
  ["linear-algebra"],
  [r"Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.",
   r"A wire's fixed place in the network is called its role."],
  aliases=["role", "wire", "gate", "scalar network"])
c("scratch-restoration", "Restoring scratch values",
  "A gate schedule that first subtracts the effect of the arbitrary initial scratch values, then injects the data, then undoes its own auxiliary updates, so every scratch wire ends with its arbitrary initial value.",
  ["linear-network"],
  [r"This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation",
   r"Our scratch schedule is the linear-readout version of that construction."],
  aliases=["transparent computation", "scratch wires"])
c("triple-construction", "Three-element subset construction",
  "Indicator vectors of 3-element subsets of a 100-element set, whose pairings |S ∩ T| mod 2 and |S ∩ T| − 1 make intersecting (or neighbouring) triples orthogonal, following Alon's account of Frankl–Wilson.",
  ["bilinear-forms"],
  [r"The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.",
   r"Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction."],
  aliases=["Frankl–Wilson construction", "triple indicators"])
c("bank-exchange", "Three-stage bank exchange",
  "The scalar network that, using copy, gather, scatter and side-injection gates per coordinate stage, maps two banks (X, Y) to (−Y, X) (a pure swap over 𝔽₂) while restoring all scratch wires.",
  ["linear-network", "scratch-restoration", "triple-construction"],
  [r"For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
   r"have the form of linear index-code decoding"],
  aliases=["gather", "scatter", "side injection", "forward invocation"])
c("frames", "Frames and the common-frame identity",
  "Assigning an invertible linear operator D_v (a frame) to each gate and terminal so that stored arrays are D_v applied to logical arrays; since a common frame commutes with pointwise gates, the network implements D_out·S·D_in⁻¹ and each route gets its endpoint operator.",
  ["linear-network", "linear-algebra", "array-layout"],
  [r"We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$.",
   r"Thus the common frame commutes with the pointwise gate"],
  aliases=["frame", "endpoint operator"])
c("subspace-labels", "Nested subspace labels and orthogonal residuals",
  "Attaching to every gate and terminal of the network a nondegenerate subspace of the m-dimensional space F^{⊗3}, nested along each edge, whose orthogonal residual dimension counts the smaller operations that edge needs.",
  ["bilinear-forms", "tensor-product", "triple-construction", "bank-exchange", "frames"],
  [r"The subspaces at adjacent vertices are nested.",
   r"Every edge joins comparable nondegenerate labels.",
   r"the \emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one"],
  aliases=["label", "orthogonal residual", "dimension loss"])
c("rank-deficit", "Rank deficit s < Wm",
  "The key property of both finite networks: the total number s of smaller calls needed over all edges is strictly less than W·m, so s/W < m.",
  ["subspace-labels"],
  [r"The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.",
   r"This strict inequality is the source of the power saving."],
  aliases=["rank saving", "relative rank deficit"],
  title=r"Rank deficit $s < Wm$",
  symbols=[("s", "number of smaller calls", "The total number of smaller recursive calls the network's edges require, summed over all edges.", "count"),
           ("W", "wire count", "The number of wires (roles) in the finite network, including scratch wires.", "count"),
           ("m", "label dimension", "The dimension of the label space, which is the factor by which each smaller call shrinks the recursion parameter.", "count")])
c("bit-interface", "Rational matrix interface of the bit network",
  "Using projections P_U onto the labels as rational matrices on the XOR network so that each edge's matrix difference has rank equal to its residual and every route's endpoint difference is the identity Iₘ, giving the address shear on every role.",
  ["rank-deficit", "frames", "address-shear"],
  [r"The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector.",
   r"For a nondegenerate rational subspace $U\subset\mathcal F$, write $P_U$ for the projection onto $U$ along $U^\perp$."])
c("phase-interface", "Binary phase interface of the complex network",
  "Using phase frames 𝒞_U = H^{⊗m}·diag(i^{q_U(x)})·H^{⊗m} on the complex network so that each edge's frame change is a product of one translation kernel aI + bX_v per orthonormal residual vector and the whole network yields C^{⊗m} on every role.",
  ["rank-deficit", "frames", "kernel-c"],
  [r"is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual.",
   r"telescoping these phase frames gives $C^{\otimes m}$ on every role, including auxiliary roles."],
  aliases=["phase frame", "complex network"])

# ---------------- address interchange ----------------
c("address-shear", "Address shear",
  "The address permutation (H, D) ↦ (H + D, D) on two groups of address fields over ℤ/qᵇℤ; together with two linear-cost updates it yields the interchange (H, D) ↦ (D, H).",
  ["array-layout", "modular-arithmetic"],
  [r"For the bit procedure, that endpoint operator is an address shear",
   r"Two further linear-cost address updates complete their interchange."])
c("bruhat", "Lower triangular (Bruhat) factorization",
  "Every rational matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.",
  ["linear-algebra"],
  [r"The rank reduction used for address shears is a singular-matrix Bruhat factorization",
   r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"])
c("matrix-shear", "Matrix shear by rank-many interchanges",
  "A shear (H, D) ↦ (H + AD, D) by a fixed rational matrix A of rank a is performed with exactly a smaller field interchanges plus O(V) triangular controlled shifts.",
  ["bruhat", "controlled-shifts", "address-shear"],
  [r"can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work."])
c("row-splitting", "Row splitting among wire roles",
  "Distributing the rows of an array cyclically among the W roles of a network (padding to a multiple of W) so that every role stream has the same address shape and volume V/W and gates act pointwise.",
  ["elementary-streams", "linear-network"],
  [r"Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$.",
   r"Each recursive edge call acts on one role stream with volume exactly \(1/W\) of its parent's logical volume."])
c("power-saving-recursion", "Volume-normalized recursion and the power saving",
  "The recurrence F(mf) ≤ (s/W)·F(f) + overhead for cost divided by volume, which, because s/W < m, gives cost O(V·e^τ) with τ < 1 instead of O(V·e) for a parameter e.",
  ["rank-deficit", "row-splitting", "big-o"],
  [r"A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$.",
   r"After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$."],
  aliases=["recursive saving"])
c("fixed-tape-schedule", "Fixed-tape depth-first schedule",
  "Running the recursion on a fixed set of tapes by parking the inactive role streams on a stack tape before each child call and restoring them afterward, at O(V) cost per node.",
  ["multitape-tm", "row-splitting"],
  [r"A fixed-tape depth-first schedule.",
   r"Before a recursive call, append the $W-1$ inactive role streams to the parking stack in a fixed order, with separators."],
  aliases=["parking stack"])
c("power-width-interchange", "Power-width interchange",
  "Interchanging two address chunks of e = mᵏ radix-q digits in O(V·e^τ) time by running the bit network on row-split role streams with shear frames and recursive smaller interchanges.",
  ["bit-interface", "matrix-shear", "power-saving-recursion", "fixed-tape-schedule"],
  [r"The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes."])
c("chunk-swap", "Fast address-chunk interchange",
  "The tape procedure that interchanges two disjoint u-bit address fields of any array in O(V·u^τ) time with fixed τ = 1 − 2^{−50}, computing XOR combinations of data along the way.",
  ["power-width-interchange", "elementary-streams"],
  [r"The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product.",
   r"Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data."],
  aliases=["chunk swap", "address interchange", "arbitrary-width interchange"])

# ---------------- simultaneous butterfly layer ----------------
c("packed-addition", "Packed selected-bit addition",
  "XORing the selected bits of one address chunk into the corresponding bits of another using eight packed cyclic shifts guarded by a third chunk, then deterministically repairing the small set of addresses where guards overflow.",
  ["chunk-swap", "controlled-shifts", "elementary-streams"],
  [r"We implement a binary row addition on corresponding selected bits in two address chunks.",
   r"The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses."],
  aliases=["binary change of basis", "deterministic repair", "guard values"])
c("recursive-c-layer", "Recursive C-layer via phase frames",
  "Computing C^{⊗e} on e selected address bits by running the complex network on row-split streams, implementing each edge's frame change by a binary change of basis and one recursive C^{⊗e/m} call per residual vector.",
  ["phase-interface", "packed-addition", "power-saving-recursion", "fixed-tape-schedule"],
  [r"Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis.",
   r"Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."])
c("simultaneous-layer", "Simultaneous butterfly layer",
  "The procedure applying H₀ on the same bit position in up to d address chunks of an array of polynomial records at once in O(V·d^{λ′}) time, λ′ < 1, evaluating exactly with guard bits and truncating once.",
  ["recursive-c-layer", "normalized-butterfly", "kernel-c", "fixed-point"],
  [r"On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.",
   r"The entire layer is evaluated exactly before one final truncation."],
  aliases=["parallel butterfly layer", "normalized butterfly layer"])

# ---------------- synthetic transforms and convolution ----------------
c("synthetic-transform", "Synthetic polynomial transform",
  "The Nussbaumer–Quandalle Fourier transform over ℂ[y]/(yʳ + 1) using powers of y as roots of unity, computed by decimation-in-frequency butterflies and monomial twiddles and leaving outputs in bit-reversed order.",
  ["negacyclic-ring", "dft", "normalized-butterfly"],
  [r"These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer",
   r"the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."],
  aliases=["Nussbaumer transform", "decimation in frequency", "bit-reversed order"])
c("transform-layout", "Transform layout and cost",
  "Rearranging the address bits of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in consecutive K-bit chunks, letting every round use the simultaneous butterfly layer.",
  ["synthetic-transform", "simultaneous-layer", "chunk-swap", "contraction-errors"],
  [r"we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks.",
   r"The forward procedure may retain its output layout for a pointwise product and the following opposite procedure."])
c("signed-packing", "Signed Kronecker packing",
  "Multiplying two polynomials with signed Gaussian-integer coefficients by evaluating them at B₀ = 2^{4p} into single integers, multiplying with the established multiplier, and extracting centered coefficients before reducing modulo yʳ + 1.",
  ["negacyclic-ring", "hvdh-multiplier", "fixed-point"],
  [r"Signed coefficient packing is a form of Kronecker substitution",
   r"The reduction is a signed form of Kronecker substitution"],
  aliases=["Kronecker substitution"])
c("synthetic-convolution", "Ring convolution from the retained layout",
  "Computing normalized cyclic convolution of arrays over ℂ[y]/(yʳ + 1) by two forward synthetic transforms, pointwise products in their retained stored order, and one opposite transform.",
  ["transform-layout", "signed-packing", "cyclic-convolution"],
  [r"The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order.",
   r"Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands."],
  aliases=["normalized convolution", "synthetic convolution"])
c("coefficient-twist", "Coefficient twist",
  "The map x ↦ ζy with ζ = e^{πi/r}, which turns cyclic convolution in the last coordinate into negacyclic multiplication modulo yʳ + 1 and back.",
  ["negacyclic-ring", "cyclic-convolution", "synthetic-convolution"],
  [r"A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed.",
   r"The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist."],
  aliases=["phase twist"])

# ---------------- resampling and chirps ----------------
c("gaussian-resampling", "Gaussian resampling",
  "Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t by convolving with Gaussian kernels, with well-conditioned resampling maps.",
  ["dft", "tensor-product"],
  [r"it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two.",
   r"Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform."])
c("resampling-retained", "Resampling with retained permutations",
  "The identity P_s F_s = 2^{2α²} B₀ P_t F_t A, in which the two coordinate permutations of Gaussian resampling are kept inside the transform identity instead of being executed as sorts.",
  ["gaussian-resampling", "contraction-errors", "fixed-point"],
  [r"retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.",
   r"Its usual implementation sorts twice on each coordinate."])
c("tensor-resampling", "Tensor resampling interface",
  "Applying the one-dimensional resampling maps line by line on every axis of a padded power-of-two box, moving axes into position with the fast chunk interchange.",
  ["resampling-retained", "chunk-swap"],
  [r"For the tensor product, apply the one-dimensional maps to one coordinate line at a time.",
   r"The chunk-swap algorithm supplies the movement of the physical axis fields, including its cost when the number of axes grows."])
c("bluestein", "Bluestein's chirp identity",
  "The identity QF_t u = ā · (a ∗ (ā · u))/T with chirp a_j = exp(−πi Σ sᵢjᵢ²/tᵢ), which converts the permuted middle Fourier transform into a cyclic convolution.",
  ["dft", "cyclic-convolution"],
  [r"Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution.",
   r"The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array."],
  aliases=["chirp transform", "chirp"])
c("source-perm-cancel", "Source permutation cancellation",
  "The identity RF⁺[(RFu)·(RFv)] = (u ∗ v)/S², showing that the source permutation R kept from resampling cancels between the two forward transforms and the opposite transform.",
  ["resampling-retained", "dft", "cyclic-convolution"],
  [r"Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform.",
   r"The second identity shows how the retained source permutation $R$ cancels when computing a convolution."])
c("source-transform", "Computed source transform",
  "The procedure approximating RF_s on the prime-axis array by composing the Gaussian expansion A, the chirp transform (via twisted ring convolution), the compression B₀, and an exact scale 2^γ.",
  ["tensor-resampling", "bluestein", "coefficient-twist"],
  [r"We next use the complex convolution to evaluate the middle factor $QF_{\boldsymbol t}$",
   r"Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations."])

# ---------------- CRT map ----------------
c("crt-map", "Chinese-remainder convolution map",
  "The Agarwal–Cooley isomorphism ℂ[x]/(x^S − 1) → ⊗ᵢ ℂ[xᵢ]/(xᵢ^{sᵢ} − 1) for pairwise coprime sᵢ, placing the digit list on a product of prime cyclic axes and implemented on tape by triangular controlled shifts and axis moves.",
  ["cyclic-convolution", "modular-arithmetic", "controlled-shifts", "chunk-swap"],
  [r"the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution",
   r"Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution"],
  aliases=["Agarwal–Cooley map", "CRT map"])

# ---------------- assembly ----------------
c("parameters", "Size parameters and prime source lengths",
  "The choices b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b split into d axes of length r or r/2, distinct odd primes sᵢ just below each tᵢ, and the fixed rational exponents ending in κ = 2^{−182}.",
  ["big-o", "modular-arithmetic", "resampling-retained"],
  [r"Take the power of two $T$ in $[4n/b,8n/b)$",
   r"We may therefore choose distinct odd primes satisfying",
   r"These constants are deliberately conservative; no optimization is claimed."],
  aliases=["fixed rational choice", "prime source lengths"])
c("precision-recovery", "Precision analysis and exact recovery",
  "The error bookkeeping showing that after undoing the normalizations S and the digit scales, every recovered convolution coefficient is within 1/2 of the true integer, so rounding and carry propagation give the exact product.",
  ["contraction-errors", "source-transform", "source-perm-cancel", "radix-reduction", "parameters"],
  [r"The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.",
   r"proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product."])
c("cost-accounting", "Cost table and the exponent κ",
  "The accounting that bounds every stage's cost divided by Tp = Θ(n) by a power of p at most 1 − 2κ, so the whole algorithm runs in O(n·(log n)^{1−κ}).",
  ["parameters", "simultaneous-layer", "transform-layout", "chunk-swap", "tensor-resampling",
   "signed-packing", "crt-map"],
  [r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
   r"Any fixed power of $\log p$ is at most $p^\kappa$ eventually."],
  aliases=["complete time bound"])

c("main-theorem", "Integer multiplication in O(n (lg n)^{1−κ}) time",
  "One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n·(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n conjecture in that model.",
  ["nlogn-conjecture", "hvdh-multiplier", "multitape-tm", "radix-reduction", "crt-map",
   "source-transform", "source-perm-cancel", "precision-recovery", "cost-accounting"],
  [r"There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs.",
   r"The theorem refutes an eventual $\Omega(n\log n)$ lower bound for every fixed multiplication machine in this model."],
  aliases=["Integer multiplication below n log n", "Theorem 1"],
  title=r"Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time",
  symbols=[("n", "input length", "The number of bits in each of the two input integers.", "count"),
           ("\\kappa", "saving exponent", "The fixed exponent 2^{−182} by which the logarithmic factor is reduced.", "direct"),
           ("\\lg", "binary logarithm", "The function lg n = max{⌈log₂ n⌉, 1}.", "direct"),
           ("O", "big-O", "Asymptotic upper bound up to a constant factor.", "direct")])

ans = {"target": "main-theorem", "concepts": concepts}
with open("/home/user/openai-nlogn-wiki/runs/Q1/exegenius/tasks/0001-extract.answer.json", "w") as f:
    json.dump(ans, f, ensure_ascii=False, indent=1)
print(len(concepts))
