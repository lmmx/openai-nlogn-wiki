import json, sys
C = []
def c(id, name, gloss, requires, ev=(), known=False, aliases=(), title=None, symbols=None):
    d = {"id": id, "name": name, "aliases": list(aliases), "gloss": gloss, "requires": list(requires),
         "known": known, "evidence": [{"source": "paper", "quote": q} for q in ev]}
    if title:
        d["title"] = title
        d["symbols"] = [dict(symbol=s, name=n, meaning=m, relation=r) for s, n, m, r in symbols]
    C.append(d)

c("big-o", "Big-O notation", "Asymptotic upper bounds on running time up to a constant factor.", [], known=True)
c("polynomials", "Polynomials", "Finite sums of coefficients times powers of an indeterminate, with addition and multiplication.", [], known=True)
c("complex-numbers", "Complex numbers", "Numbers a + bi with real a, b, including roots of unity and the modulus.", [], known=True)
c("multitape-turing-machine", "Multitape Turing machine", "A Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, each head moving at most one cell per step.", [], known=True)

c("nlogn-conjecture", "The n log n optimality conjecture", "Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.",
  ["big-o", "multitape-turing-machine"],
  [r"The theorem refutes an eventual $\Omega(n\log n)$ lower bound for every fixed multiplication machine in this model.",
   r"Sch\"onhage and Strassen conjectured $n\log n$ as the optimal order of multiplication cost"],
  aliases=["Schönhage–Strassen conjecture"], title=r"The $n\log n$ optimality conjecture",
  symbols=[("n", "input bit length", "The number of bits in each of the two integers being multiplied.", "count")])

c("hvdh-multiplier", "Established O(n log n) multiplier", "Harvey and van der Hoeven's fixed-tape O(n log n) integer multiplication algorithm, used here only as an ordinary subroutine on short records.",
  ["big-o", "multitape-turing-machine"],
  [r"Calls to the established $O(n\log n)$ multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively."],
  aliases=["Harvey–van der Hoeven multiplier"], title=r"Established $O(n\log n)$ multiplier",
  symbols=[("n", "input bit length", "The number of bits in each input of the subroutine multiplication.", "count"),
           ("O", "big-O bound", "Asymptotic upper bound up to a constant factor.", "direct")])

c("cyclic-convolution", "Cyclic convolution", "The product of coefficient arrays in which indices add modulo the array length, i.e. polynomial multiplication modulo x^S − 1.",
  ["polynomials"],
  [r"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
   r"let $*$ denote cyclic convolution in the displayed axes"])

c("radix-digit-convolution", "Radix-digit convolution", "Writing each input as a polynomial in 2^b, so that the product becomes a convolution of small digit coefficients followed by carry propagation.",
  ["polynomials", "cyclic-convolution"],
  [r"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
   r"Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits."],
  aliases=["Kronecker splitting into digits"])

c("dft", "Normalized discrete Fourier transform", "The map sending a length-q vector to its averages against the q-th roots of unity; it is a contraction and turns cyclic convolution into pointwise multiplication.",
  ["complex-numbers", "cyclic-convolution"],
  [r"Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one."],
  aliases=["Fourier transform", "DFT"])

c("stream-array-layout", "Array streams and logical volume", "Arrays are stored on tape in lexicographic order of their address fields with implicit addresses, and the logical volume V is the number of stored data bits.",
  ["multitape-turing-machine"],
  [r"An address is implicit in an entry's position in this ordered stream; it is not stored beside every data bit.",
   r"The \emph{logical volume} $V$ is the number of stored data bits."],
  aliases=["logical volume", "address field", "row"])

c("elementary-stream-ops", "Elementary stream operations", "Linear-time tape operations that permute or move a single fixed-radix digit of the address, split and merge streams on a digit, and split rows cyclically into a fixed number of streams.",
  ["stream-array-layout", "big-o"],
  [r"moving one specified radix-$q$ digit to another position, preserving the order of the intervening positions;"])

c("controlled-shifts", "Controlled shifts", "A linear-time update adding to a later address field an offset computed from earlier control fields (or scaling it by a fixed unit), implemented by splitting and remerging blocks.",
  ["stream-array-layout"],
  [r"The next operations are linear because their target field follows their control fields."],
  aliases=["prefix-controlled cyclic shift"])

c("crt-address-map", "Chinese-remainder address map", "The isomorphism x ↦ ∏ x_i^{μ_i} that turns one cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on distinct prime axes, implemented by triangular controlled shifts and axis moves.",
  ["cyclic-convolution", "controlled-shifts", "chunk-interchange"],
  [r"Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution",
   r"Each triangular update is a prefix-controlled cyclic shift."],
  aliases=["CRT map", "prime source lengths"])

c("gaussian-resampling", "Gaussian resampling", "Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t, using Gaussian-weighted contractions.",
  ["dft"],
  [r"Gaussian resampling connects these two shapes.",
   r"it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two."])

c("retained-permutations", "Resampling with retained permutations", "Keeping the coordinate permutations P_s and P_t inside the resampling identity P_sF_s = 2^{2α²}B₀P_tF_tA instead of sorting, and letting the source permutation cancel across forward transforms, pointwise product, and opposite transform.",
  ["gaussian-resampling"],
  [r"Here the source and target permutations remain in the transform identity, while the faster tape procedures perform the required axis movements.",
   r"Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform."],
  aliases=["no-sort resampling", "permutation cancellation"])

c("tensor-resampling", "Tensor resampling interface", "Applying the one-dimensional resampling maps line by line along each of d axes of a padded power-of-two box, with axis exposure done by chunk interchanges.",
  ["retained-permutations", "chunk-interchange", "elementary-stream-ops"],
  [r"For the tensor product, apply the one-dimensional maps to one coordinate line at a time."])

c("bluestein-chirp", "Bluestein's chirp identity", "Writing a Fourier transform, including its frequency permutation, as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.",
  ["dft", "cyclic-convolution", "retained-permutations"],
  [r"Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution."],
  aliases=["chirp transform"])

c("negacyclic-ring", "Polynomial ring modulo y^r + 1", "The ring of complex polynomials of degree below r with y^r = −1, where multiplication by a power of y is a signed cyclic shift of coefficients.",
  ["polynomials", "complex-numbers"],
  [r"Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs; consequently it is an isometry for this norm."],
  aliases=["negacyclic ring"], title=r"Polynomial ring modulo $y^r+1$",
  symbols=[("y", "ring indeterminate", "The polynomial variable whose powers act as synthetic roots of unity.", "direct"),
           ("r", "record length", "The number of complex coefficients in a polynomial record, a power of two.", "count")])

c("phase-twist", "Coefficient phase twist", "The map x_d ↦ ζy with ζ = e^{πi/r} that converts cyclic convolution along the last axis into negacyclic multiplication modulo y^r + 1.",
  ["negacyclic-ring", "cyclic-convolution"],
  [r"A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed."],
  aliases=["coefficient twist"])

c("butterfly", "Normalized butterfly H₀", "The two-point map (u, v) ↦ ((u+v)/2, (u−v)/2), the basic step of radix-two Fourier transforms.",
  ["complex-numbers"],
  [r"In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations."],
  aliases=["H0"], title=r"Normalized butterfly $H_0$",
  symbols=[("H_0", "normalized butterfly", "The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2).", "direct")])

c("gaussian-dyadics", "Gaussian dyadics and fixed-point truncation", "Complex numbers whose real and imaginary parts have power-of-two denominators, stored exactly in fixed-point words and truncated toward zero to the p-bit grid only at the end of a layer.",
  ["complex-numbers"],
  [r"Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators.",
   r"A single truncation follows the completed contractive layer."],
  aliases=["disk grid", "Q_p truncation", "guard bits"])

c("synthetic-fft", "Synthetic polynomial transform", "A radix-two Fourier transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so twiddles are signed shifts; its output is stored in bit-reversed frequency order.",
  ["negacyclic-ring", "dft", "butterfly"],
  [r"Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list.",
   r"These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer"],
  aliases=["Nussbaumer transform", "synthetic transform"])

c("linear-network", "Linear bank-exchange network", "A fixed finite network of linear gates on wires (roles) that exchanges two banks of values with prescribed signs while restoring every auxiliary scratch value.",
  [],
  [r"Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.",
   r"A wire's fixed place in the network is called its role."],
  aliases=["finite network", "role", "wire"])

c("scratch-restoration", "Restoration of arbitrary scratch values", "An eight-row schedule that subtracts the effect of unknown scratch contents, adds the intended computation, and uncomputes, so scratch wires may start with arbitrary values.",
  ["linear-network"],
  [r"This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation"],
  aliases=["transparent computation"])

c("triple-gadget", "Three-element-subset gather and scatter", "Gates indexed by three-element subsets of [100]: gather and scatter produce coefficients depending on intersection size, and side wires cancel the unwanted ones so the net effect is y ← y + x.",
  ["linear-network", "scratch-restoration"],
  [r"The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients."],
  aliases=["index-code decoding", "Frankl–Wilson construction"])

c("frame-invariant", "Frames and the common-frame identity", "Storing each wire's array through an invertible operator (frame) that is common at each gate, so pointwise gates commute with frames and only endpoint frames determine the net operator.",
  ["linear-network", "stream-array-layout"],
  [r"We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$.",
   r"At a pointwise linear gate $G$, the common frame commutes with the gate:"],
  aliases=["frame"])

c("subspace-labels", "Nested subspace labels", "Nondegenerate subspaces of a fixed bilinear space attached to gates and terminals, nested along each edge, whose orthogonal residual dimensions count the smaller operations an edge needs.",
  ["frame-invariant", "triple-gadget"],
  [r"A label is a nondegenerate subspace of a fixed bilinear space.",
   r"the \emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one"],
  aliases=["orthogonal residual", "labels"])

c("rank-deficit", "Rank deficit of the network", "The property that the total number s of smaller calls over all edges is strictly less than the wire count W times the label dimension m.",
  ["subspace-labels"],
  [r"The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$."],
  aliases=["s < Wm"])

c("address-shear", "Address shear", "The array permutation moving the entry at address (H, D) to (H + MD, D) for a matrix M acting on two groups of address fields.",
  ["stream-array-layout"],
  [r"For the bit procedure, that endpoint operator is an address shear:",
   r"the frame $\Phi_M$ moves the array entry at $(H,D)$ to $(H+MD,D)$"],
  aliases=["shear"])

c("bit-motif-interface", "Rational matrix interface", "The bit network with XOR gates and rational projection matrices on its vertices, whose endpoint matrices differ by the identity on every role and whose edge ranks sum to s_b < W_b·m.",
  ["rank-deficit", "address-shear"],
  [r"The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector."],
  aliases=["bit network"])

c("lower-triangular-factorization", "Lower triangular factorization", "Writing any rational matrix of rank a as E₁ΠE₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, a reversed Bruhat factorization.",
  [],
  [r"The rank reduction used for address shears is a singular-matrix Bruhat factorization"],
  aliases=["Bruhat factorization"])

c("matrix-shear-cost", "Cost of a rational matrix shear", "A shear (H, D) ↦ (H + AD, D) by a fixed rational matrix of rank a costs exactly a interchanges of smaller field pairs plus linear work.",
  ["lower-triangular-factorization", "controlled-shifts", "address-shear"],
  [r"can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work."])

c("row-splitting", "Row splitting among roles", "Distributing rows of an array cyclically among the W wire roles so that each role stream has the same address shape and volume V/W.",
  ["linear-network", "elementary-stream-ops"],
  [r"Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$."])

c("volume-recurrence", "Volume-normalized recurrence", "The recurrence F_k ≤ (s/W)F_{k−1} + O(1) for cost divided by volume, which yields a power saving because s/W < m.",
  ["rank-deficit", "row-splitting"],
  [r"After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$.",
   r"This strict inequality is the source of the power saving."],
  aliases=["recursive saving"])

c("chunk-interchange", "Fast address chunk interchange", "A fixed-tape procedure that exchanges two equal-width contiguous address chunks of u bits in O(Vu^τ) time with τ < 1, via XOR combinations of data driven by the bit network.",
  ["bit-motif-interface", "matrix-shear-cost", "volume-recurrence"],
  [r"The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product.",
   r"Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$."],
  aliases=["chunk swap", "address interchange"])

c("phase-frames", "Binary phase frames", "Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} attached to binary labels, whose edge changes factor into one two-point kernel aI + bX_v per residual basis vector.",
  ["subspace-labels", "gaussian-dyadics", "butterfly", "frame-invariant"],
  [r"Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis."],
  aliases=["kernel C", "phase kernel"])

c("complex-motif-interface", "Binary phase interface", "The complex network with binary labels: after endpoint corrections it applies the tensor power of the kernel C on every role using s_c < W_c·m smaller kernel calls.",
  ["phase-frames", "rank-deficit"],
  [r"After source and sink diagonal corrections, and undoing the signed bank exchange, telescoping these phase frames gives $C^{\otimes m}$ on every role, including auxiliary roles."],
  aliases=["complex network"])

c("packed-selected-bit", "Packed selected-bit addition", "XORing selected bits of one address chunk into another by eight packed cyclic shifts with guard bits, followed by deterministic repair of an explicitly bounded set of exceptional addresses.",
  ["chunk-interchange", "controlled-shifts", "elementary-stream-ops"],
  [r"The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses."],
  aliases=["binary change of basis", "deterministic repair"])

c("simultaneous-layer", "Simultaneous butterfly layer", "Applying H₀ on the same bit position in up to d address chunks at once in O(Vd^{λ'}) time, λ' < 1, by recursing through the complex network and evaluating the layer exactly before one truncation.",
  ["complex-motif-interface", "packed-selected-bit", "volume-recurrence", "butterfly", "gaussian-dyadics", "row-splitting"],
  [r"On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$."],
  aliases=["fast butterfly layer", "parallel butterfly"])

c("transform-layout", "Transform layout", "A positional permutation of address bits placing the bits used in each transform round at a common offset in consecutive K-bit chunks, so simultaneous layers apply and the frequency order is retained.",
  ["synthetic-fft", "simultaneous-layer", "chunk-interchange"],
  [r"we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks."])

c("signed-packing", "Signed coefficient packing", "A signed Kronecker substitution that evaluates integer polynomials at B₀ = 2^{4p}, multiplies with the established multiplier, and recovers coefficients by centered residues, giving products in the ring modulo y^r + 1.",
  ["negacyclic-ring", "hvdh-multiplier"],
  [r"Signed coefficient packing is a form of Kronecker substitution"],
  aliases=["Kronecker substitution"])

c("synthetic-convolution", "Convolution from the retained transform layout", "Normalized convolution over the polynomial ring computed by two forward synthetic transforms, pointwise packed products in the stored order, and the opposite transform consuming that order.",
  ["transform-layout", "signed-packing"],
  [r"Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands."])

c("exact-recovery", "Exact recovery by rounding and carries", "Undoing known scales, rounding each approximate coefficient whose error is below 1/2 to the exact integer, and propagating radix-2^b carries to obtain the binary product.",
  ["radix-digit-convolution", "gaussian-dyadics"],
  [r"proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product."])

c("cost-table", "Parameter choice and cost table", "Fixed rational parameters (τ = 1 − 2^{-50}, ε = 2^{-75}, κ = 2^{-182}, …) under which every term of the cost per bit is at most p^{1−2κ}.",
  ["chunk-interchange", "simultaneous-layer", "transform-layout", "tensor-resampling", "crt-address-map", "synthetic-convolution"],
  [r"A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}.",
   r"Thus $\min_i g_i=2^{-181}=2\kappa$."])

c("main-theorem", "Integer multiplication in O(n (lg n)^(1−κ)) time", "One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, refuting the n log n lower-bound conjecture in this model.",
  ["nlogn-conjecture", "radix-digit-convolution", "crt-address-map", "tensor-resampling", "bluestein-chirp", "phase-twist", "synthetic-convolution", "exact-recovery", "cost-table", "hvdh-multiplier"],
  [r"We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time",
   r"$\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes."],
  aliases=["Theorem 1"], title=r"Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time",
  symbols=[("n", "input bit length", "The number of bits in each of the two input integers.", "count"),
           (r"\lg", "ceiling binary logarithm", "The function lg n = max{⌈log₂ n⌉, 1}.", "direct"),
           (r"\kappa", "saving exponent", "The fixed constant 2^{-182} by which the logarithmic exponent drops below one.", "direct"),
           ("O", "big-O bound", "Asymptotic upper bound up to a constant factor on worst-case running time.", "direct")])

out = {"target": "main-theorem", "concepts": C}
json.dump(out, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
