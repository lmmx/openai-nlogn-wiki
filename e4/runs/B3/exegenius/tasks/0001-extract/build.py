import json, re, sys
C = []
def add(id, name, gloss, requires=(), known=False, ev=(), aliases=(), title=None, symbols=None):
    d = dict(id=id, name=name, aliases=list(aliases), gloss=gloss, requires=list(requires), known=known,
             evidence=[dict(source="paper", quote=q) for q in ev])
    if title:
        d["title"] = title
        d["symbols"] = [dict(symbol=s, name=n, meaning=m, relation=r) for (s, n, m, r) in symbols]
    C.append(d)

# known
add("big-o", "Big-O notation", "Asymptotic upper bound on running time as input size grows.", known=True)
add("polynomials", "Polynomials", "Sums of coefficients times powers of a variable, with addition and multiplication.", known=True)
add("complex-numbers", "Complex numbers", "Numbers a+bi with i²=-1, including roots of unity e^{2πi/k}.", known=True)
add("multitape-tm", "Multitape Turing machine", "A finite-state machine with a fixed number of one-dimensional tapes, each head reading/writing one cell and moving at most one cell per step.", known=True)

add("history", "Integer multiplication complexity and the n log n conjecture",
    "Schönhage–Strassen gave O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n), which this paper's algorithm beats.",
    ["multitape-tm", "big-o"],
    ev=[r"Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper",
        r"Sch\"onhage and Strassen conjectured $n\log n$ as the optimal order of"])

add("linear-algebra", "Subspaces, rank, orthogonal complements and bilinear forms",
    "Basic linear algebra over Q or F₂: subspaces, rank of a matrix, a nondegenerate symmetric bilinear form, orthogonal complements and orthogonal direct sums.",
    ev=[r"A label is a nondegenerate subspace of a fixed bilinear space."])

add("stream-ops", "Arrays on tape and elementary stream operations",
    "An array with a product address set is stored in lexicographic order on tape; splitting on a digit, merging, moving a digit and splitting whole rows cyclically into streams each cost O(V) for stored volume V.",
    ["multitape-tm", "big-o"],
    ev=[r"An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in",
        r"Each of the following operations on an array of"])

add("controlled-shift", "Controlled cyclic shifts and fixed rational scalings",
    "Updating a later address field y by y+a(controls) mod q^b, or multiplying it by a fixed rational unit, costs O(V) on tape by splitting each fibre in two pieces and merging them in swapped order.",
    ["stream-ops"],
    ev=[r"Controlled shifts and fixed rational scalings",
        r"\longmapsto y+a(\text{controls})\pmod Q"])

add("dft", "Discrete Fourier transform",
    "The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πi jk/q} of a length-q vector, with the opposite-sign inverse F⁺ satisfying F⁺F = I/q.",
    ["complex-numbers", "polynomials"],
    ev=[r"(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q},"])

add("convolution", "Cyclic convolution and the convolution theorem",
    "Cyclic convolution u*v multiplies polynomials modulo x^q − 1 and equals, up to normalization, the inverse transform of the pointwise product of the transforms.",
    ["polynomials", "dft"],
    ev=[r"The normalized convolution rule is",
        r"$F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot}"])

add("integer-as-convolution", "Integer product as convolution of radix digits",
    "Writing both inputs as polynomials in 2^b with b-bit digits, the product is a convolution of digit lists; padding so the degree is below the cyclic length S avoids wraparound, and coefficients stay below 2^{3b}.",
    ["convolution", "history"],
    ev=[r"Write the two inputs as polynomials in $2^b$, each with",
        r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."])

add("butterfly-fft", "Butterfly (decimation-in-frequency) transform",
    "A length-t transform is computed in log₂t levels, each pairing z_k with z_{k+t/2}, applying the two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2), a twiddle multiplication, and recursing on both halves.",
    ["dft", "big-o"],
    ev=[r"decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"])

add("multidim-transform", "Multidimensional transforms (tensor products)",
    "A transform on an array indexed by several axes is the tensor product of one-dimensional transforms, computed one axis at a time; convolution on the product group corresponds to pointwise product.",
    ["dft", "convolution"],
    ev=[r"multidimensional transforms whose axis lengths are",
        r"F_{\boldsymbol q}:=\bigotimes_iF_{q_i}"])

add("crt-map", "Chinese-remainder map to distinct prime axes",
    "With pairwise coprime axis lengths s_i and product S, the map x ↦ ∏ x_i^{μ_i} is an isomorphism from C[x]/(x^S−1) to the multi-axis cyclic ring, converting one long cyclic convolution into a multidimensional one; on tape it is a sequence of triangular controlled shifts.",
    ["multidim-transform", "convolution", "controlled-shift"],
    ev=[r"First, the radix-digit coefficient list is placed on a product of",
        r"respects $x^S=1$, so it defines an algebra map."])

add("fixed-point", "Fixed-point complex grid and truncation",
    "Complex numbers are stored as pairs of signed two's-complement integers scaled by 2^{-p}; the truncation Q_p rounds each part toward zero to this grid with error below √2·2^{-p}.",
    ["complex-numbers"],
    ev=[r"$p$-bit grid array has real and imaginary coefficient parts in",
        r"\|Q_p z-z\|_\infty<\sqrt2\,2^{-p}"])

add("contraction-error", "Contractions and error accumulation",
    "A linear map that does not increase the maximum coefficient norm is a contraction; errors of composed approximations add, and for a bilinear contraction the error is bounded by ‖Δf‖‖g′‖+‖f‖‖Δg‖.",
    ["fixed-point", "complex-numbers"],
    ev=[r"Each normalized Fourier transform above is a contraction, since each",
        r"Composing such algorithms"])

add("gaussian-resampling", "Gaussian resampling",
    "Harvey–van der Hoeven's identity expressing a Fourier transform of coprime length s as a transform of larger power-of-two length t, sandwiched between two Gaussian-weighted contractions A and B₀ and two coordinate permutations.",
    ["dft", "multidim-transform", "contraction-error"],
    ev=[r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."],
    aliases=["Gaussian gridding"])

add("bluestein", "Bluestein chirp identity",
    "A transform with quadratic-phase (chirp) factors equals pointwise chirp multiplication, a cyclic convolution with the chirp array, and a second chirp multiplication.",
    ["dft", "convolution", "multidim-transform"],
    ev=[r"Next, Bluestein's chirp identity converts the middle transform,"],
    aliases=["chirp identity"])

add("retained-permutations", "Resampling with the permutations left in the transform",
    "Instead of sorting twice per coordinate, the coordinate permutations of resampling are kept in the transform formula; the chirp absorbs the target permutation and the source permutation cancels across the two forward transforms, the pointwise product and the opposite transform.",
    ["gaussian-resampling", "bluestein"],
    ev=[r"Resampling with the permutations left in the transform",
        r"Section~\ref{sec:resampling} retains the"])

add("ring-mod-yr", "Polynomial ring modulo yʳ + 1",
    "The ring C[y]/(y^r+1) of polynomials of degree below a power of two r; multiplying by y^a permutes the coefficient list with sign changes, and the coefficient maximum norm is preserved.",
    ["polynomials", "complex-numbers"],
    title=r"Polynomial ring $\mathbb C[y]/(y^r+1)$",
    symbols=[("y", "ring variable", "The formal polynomial variable, which satisfies y^r = -1 and serves as a root of unity.", "direct"),
             ("r", "record length", "The number of complex coefficients in a ring element, a power of two.", "count"),
             (r"\mathbb C", "complex numbers", "The field of complex numbers from which the coefficients are drawn.", "direct")],
    ev=[r"\mathcal R_r=\mathbb C[y]/(y^r+1),"])

add("synthetic-transform", "Synthetic polynomial transform",
    "A butterfly transform over the ring C[y]/(y^r+1) whose roots of unity ω_t=y^{2r/t} act as exact signed shifts of the coefficient list, so twiddle multiplications are cheap (Nussbaumer–Quandalle).",
    ["ring-mod-yr", "butterfly-fft", "multidim-transform"],
    ev=[r"For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$.",
        r"such a root is a signed shift of the coefficient list."],
    aliases=["polynomial transform"])

add("phase-twist", "Phase twist from cyclic to negacyclic wrap",
    "Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps C[x]/(x^r−1) isomorphically onto C[y]/(y^r+1), so the negative wrap of the ring gives exactly the cyclic wrap after the twist is removed.",
    ["ring-mod-yr", "convolution"],
    ev=[r"A phase twist changes the last cyclic coordinate into a polynomial",
        r"x_d\longmapsto\zeta y"])

add("signed-packing", "Signed packing (Kronecker substitution) of ring products",
    "Polynomials with small signed coefficients are evaluated at a large power of two to give integers, multiplied by the established O(N log N) integer multiplier as a subroutine, and the product coefficients are recovered by centered residues, giving normalized ring products in O(rp log(rp)).",
    ["ring-mod-yr", "history", "fixed-point"],
    ev=[r"The reduction is a signed form of Kronecker substitution; compare",
        r"To multiply the polynomial records, we use the fixed-tape integer"])

add("exact-recovery", "Exact recovery by rounding and carry propagation",
    "After removing the known scales, each recovered digit-convolution coefficient has error below 1/2, so rounding gives the exact integer coefficients and radix-2^b carries give the 2n-bit product.",
    ["integer-as-convolution", "contraction-error", "fixed-point"],
    ev=[r"Propagate radix-$2^b$ carries in increasing coefficient order.",
        r"coefficient error is strictly below $1/2$"])

add("linear-network", "Linear exchange network with restored scratch wires",
    "A fixed network of linear gates on W scalar wires that exchanges two banks of values with signs while returning every auxiliary (scratch) wire to its arbitrary initial value; each wire's fixed place is its role.",
    ["linear-algebra"],
    ev=[r"Each procedure arises from its own fixed linear network that exchanges two",
        r"A wire's fixed place in the network is called its role."],
    aliases=["finite network"])

add("subset-gadget", "Three-element-subset gather/scatter gadget",
    "Using triples of a ground set, gather and scatter create coefficients depending on intersection size, and side wires cancel the unwanted ones so that three stages realize (X,Y)↦(−Y,X) with arbitrary scratch values restored.",
    ["linear-network"],
    ev=[r"three-element subsets: gather and scatter create coefficients depending",
        r"For arbitrary initial values of its auxiliary wires, a forward"])

add("frames", "Frames: changing the representation along network edges",
    "Each array on a wire is stored as D_v g for a vertex-dependent invertible operator D_v; since all wires at a gate share the frame and gates are pointwise linear, the whole network implements D_out S D_in^{-1}, with edge cost D_v D_u^{-1}.",
    ["linear-network", "linear-algebra"],
    ev=[r"At a source, gate, or sink $v$, choose an invertible linear operator",
        r"Thus the common frame commutes with the pointwise gate, and"])

add("rank-saving", "Subspace labels and the rank saving s < Wm",
    "Attaching nested nondegenerate subspaces of an m-dimensional space to gates so that the sum s of edge-difference ranks stays strictly below W·m; this strict deficit is the source of the power saving.",
    ["subset-gadget", "frames", "linear-algebra"],
    title=r"Rank saving $s<Wm$",
    symbols=[("s", "total rank", "The sum over all network edges of the rank of the frame difference, equal to the number of smaller calls needed.", "count"),
             ("W", "wire count", "The number of wires, including scratch wires, in the fixed network.", "count"),
             ("m", "label dimension", "The dimension of the fixed space whose subspaces label the gates.", "count")],
    ev=[r"The decisive property is that the total",
        r"\emph{orthogonal residual} is the orthogonal complement of the smaller label inside"])

add("bit-network-shear", "Bit network and the address shear",
    "The XOR-only bit network with rational matrices M_v whose endpoint difference is the identity, so frames Φ_M (moving entry (H,D) to (H+MD,D)) make every role undergo the shear (H,D)↦(H+D,D).",
    ["rank-saving", "frames", "controlled-shift"],
    ev=[r"uses only pointwise XOR gates,",
        r"the frame $\Phi_M$ moves the array entry"])

add("triangular-factorization", "Lower-triangular (Bruhat) factorization",
    "Every rational m×m matrix of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones, matching the tape order of controlled shifts.",
    ["linear-algebra", "controlled-shift"],
    ev=[r"Lower triangular factorization",
        r"A=E_1\Pi E_2,"],
    aliases=["Bruhat factorization"])

add("matrix-shear", "Cost of a rational matrix shear",
    "The shear (H,D)↦(H+AD,D) for a rank-a rational matrix A is done with exactly a interchanges of b-digit fields plus O(V) work, using triangular factors and three controlled updates per pivot.",
    ["triangular-factorization", "controlled-shift"],
    ev=[r"can be performed with exactly $a$ interchanges of pairs of $b$-digit"])

add("power-width-interchange", "Power-width chunk interchange and the recursive saving",
    "For chunks of e=m^k digits, running the bit network on W row-split role streams, with each edge done by smaller interchanges, gives F_k ≤ (s/W)F_{k−1}+O(1); because s/W<m^τ this yields cost O(V e^τ).",
    ["bit-network-shear", "matrix-shear", "stream-ops"],
    ev=[r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).",
        r"The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every"])

add("chunk-interchange", "Chunk interchange in O(V uᵗ) time",
    "Interchanging two disjoint u-bit address fields of an array in which all address combinations occur costs O(V u^τ) for a fixed τ<1, via XOR-style intermediate steps whose final effect is an exact permutation.",
    ["power-width-interchange"],
    title=r"Chunk interchange in $O(Vu^\tau)$ time",
    symbols=[("V", "stored bit volume", "The number of stored data bits in the array being rearranged.", "count"),
             ("u", "chunk width", "The number of bits in each of the two address chunks being interchanged.", "count"),
             (r"\tau", "interchange exponent", "A fixed constant below 1, here 1-2^{-50}, controlling the saving.", "direct")],
    ev=[r"Arbitrary-width interchange",
        r"in $O(Vu^\tau)$ steps"])

add("complex-phase-network", "Complex phase network and the C kernel",
    "The complex version of the network with binary labels and phase frames C_U=H^{⊗m}diag(i^{wt(P_U x) mod 4})H^{⊗m}; each edge difference is a product of two-point kernels aI+bX_v, and telescoping gives C^{⊗m} on every role.",
    ["rank-saving", "frames", "complex-numbers"],
    ev=[r"C=H\mathsf SH=aI+bX",
        r"Its phase-frame difference"])

add("phase-frame-reduction", "Phase frames reduce a butterfly layer to C kernels",
    "Since H₀=b·S·C·S with a diagonal phase S, a simultaneous layer H₀^{⊗D} equals b^D S_D C^{⊗D} S_D; the network turns C^{⊗e} on e axes into s calls on e/m axes plus binary basis changes of selected bits.",
    ["complex-phase-network", "butterfly-fft"],
    ev=[r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."])

add("packed-bit-addition", "Packed addition of selected address bits",
    "A binary row addition on corresponding selected bits of two address chunks, using a third chunk as restored scratch, is done by eight packed cyclic shifts plus deterministic repair of an exponentially small set of exceptional addresses.",
    ["chunk-interchange", "controlled-shift"],
    ev=[r"Packed selected-bit addition on one rectangle",
        r"y_{j_i}\longleftarrow y_{j_i}\mathbin\oplus x_{j_i}"])

add("simultaneous-layer", "Simultaneous butterfly layer in O(V d^λ′) time",
    "Applying H₀ to the same bit position in d address chunks of polynomial records at once, exactly in Gaussian dyadics with guard bits and one final truncation, costs O(V d^{λ′}) with λ′<1 instead of d passes.",
    ["phase-frame-reduction", "packed-bit-addition", "power-width-interchange", "fixed-point"],
    title=r"Simultaneous butterfly layer in $O(Vd^{\lambda'})$ time",
    symbols=[("V", "stored bit volume", "The number of stored data bits in the array of polynomial records.", "count"),
             ("d", "axis count", "The number of address chunks (axes) on which the butterfly acts simultaneously.", "count"),
             (r"\lambda'", "layer exponent", "A fixed constant below 1, here 1-2^{-54}, bounding the cost growth in d.", "direct")],
    ev=[r"The procedure returns $Q_p(\mathcal H z)$ in the same array,",
        r"coefficient order, and component format in $O(Vd^{\lambda'})$ time,"])

add("transform-layout", "Synthetic transform layout and retained frequency order",
    "Selected bits of the participating axes are brought to a common offset in K-bit chunks by chunk interchanges; the forward transform leaves frequencies in bit-reversed order B_t and layout L, which the opposite transform consumes, at cost O(Tp[dK+pK^{τ−1}+ℓd^{λ′}]).",
    ["synthetic-transform", "simultaneous-layer", "chunk-interchange"],
    ev=[r"The procedure constructs an explicit positional",
        r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."])

add("ring-convolution", "Normalized convolution over the ring from the retained layout",
    "Forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform in the same stored order compute f*g/(rM) on the remaining axes over C[y]/(y^r+1) with error below √2·M(3ℓ+1)2^{-p}.",
    ["transform-layout", "signed-packing", "convolution"],
    ev=[r"Convolution from the retained transform layout",
        r"Perform both forward transforms and retain their common $LB$ order."])

add("complex-convolution-twist", "Complex cyclic convolution via the coefficient twist",
    "Normalized cyclic convolution on all d power-of-two axes is obtained by twisting the last coordinate into the ring, applying the ring convolution on the other axes, and untwisting.",
    ["ring-convolution", "phase-twist"],
    ev=[r"Complex convolution by a coefficient twist",
        r"normalized complex cyclic"])

add("source-transform", "Computed source transform",
    "The procedure evaluating R F_s: Gaussian map A on each line, the chirp-based transform via complex convolution, Gaussian map B₀, then scaling by 2^γ, with the opposite sign obtained by complex conjugation.",
    ["retained-permutations", "complex-convolution-twist", "chunk-interchange"],
    ev=[r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"])

add("parameters", "Parameter choices, padded box and prime source lengths",
    "From n pick b=⌈log₂n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, a power of two T≈n/b split into d axes of length r/2 or r, and distinct primes s_i just below each t_i (found by deterministic search), with fixed rational exponents leaving positive margins.",
    ["integer-as-convolution", "gaussian-resampling", "synthetic-transform"],
    ev=[r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,",
        r"contains at least $\eta x/(2\log x)$ primes"])

add("multiplication-algorithm", "The multiplication algorithm",
    "Form radix-2^b digits, apply the CRT map Φ, compute two forward source transforms, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}S, round, invert Φ, and propagate carries to output the 2n-bit product.",
    ["parameters", "crt-map", "source-transform", "exact-recovery", "integer-as-convolution"],
    ev=[r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"])

add("cost-accounting", "Cost table and the κ margin",
    "Dividing costs by Tp=Θ(n), seven dominant terms have powers of p at most 1−2κ (smallest margin 2^{-181}), so every polylogarithmic loss is absorbed and the total is O(n (log n)^{1−κ}).",
    ["multiplication-algorithm", "chunk-interchange", "simultaneous-layer", "transform-layout", "ring-convolution"],
    ev=[r"Thus $\min_i g_i=2^{-181}=2\kappa$.",
        r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."])

add("main-theorem", "Integer multiplication in O(n (lg n)^(1−κ)) time",
    "A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it works by fast address interchanges and fast simultaneous butterfly layers inside a Gaussian-resampling/Bluestein/synthetic-transform reduction.",
    ["multiplication-algorithm", "cost-accounting", "history"],
    title=r"Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time",
    symbols=[("n", "operand length", "The number of bits in each of the two integers being multiplied.", "count"),
             (r"\kappa", "saving exponent", "The fixed positive constant 2^{-182} giving the power saving in the logarithmic factor.", "direct")],
    ev=[r"computes this exact product for every $n\ge1$ and every pair of $n$-bit",
        r"T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right),"])

src = open("/home/user/openai-nlogn-wiki/runs/P3/sources/paper.tex").read()
norm = lambda s: re.sub(r"\s+", "", s)
ns = norm(src)
ids = {c["id"] for c in C}
for c in C:
    for q in c["evidence"]:
        if norm(q["quote"]) not in ns: print("BAD QUOTE", c["id"], q["quote"])
    for r in c["requires"]:
        if r not in ids: print("BAD REQ", c["id"], r)
json.dump(dict(target="main-theorem", concepts=C), open("/home/user/openai-nlogn-wiki/runs/P3/exegenius/tasks/0001-extract.answer.json", "w"), indent=1, ensure_ascii=False)
