import json, sys
SRC = open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3B/sources/paper.tex').read()

def Q(s):
    return {"source": "paper", "quote": s}

def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": Q(quote) if quote else None}

def B(symbol, name, meaning, relation="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "from": frm or []}
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

# ---------------- S1: chunk interchange ----------------
S1_1 = infer("S1.1",
  "Digit permutations, digit moves, split-map-merge scans and cyclic row distribution among $W$ streams all take $O(V)$ steps on an array of $V$ bits stored in lexicographic order.",
  "Fix a radix $q\\ge2$.  Each of the following operations on an array of",
  page="tape-stream-operations",
  frm=["multitape-turing-machine", "row-major-order-and-matrix-transposition", "positional-number-systems-and-carries"])

S1_2 = infer("S1.2",
  "Adding to a target field an offset computed from earlier control fields, or multiplying it by a rational unit, takes $O(V)$ steps when the target field follows its controls.",
  "Suppose a target field $y\\in[Q]$ follows its control fields, each control",
  page="controlled-shift",
  frm=["tape-stream-operations", "modular-arithmetic", "primes-coprimality-and-the-extended-euclidean-algorithm"])

S131_1 = infer("S1.3.1.1",
  "Three stages of forward invocations, built from gather, scatter and side wires on three-element subsets, send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every scratch wire to its arbitrary initial value.",
  "For arbitrary initial values of its auxiliary wires, a forward",
  page="exchange-network",
  frm=["finite-sets-subsets-and-counting", "arithmetic-modulo-2-and-linear-algebra-over-f-2", "circuits-and-directed-acyclic-graphs"])

S131_2 = infer("S1.3.1.2",
  "If every vertex of the network carries an invertible frame operator $D_v$ shared by all wires at a gate, pointwise linear gates commute with the frames, the intermediate frames cancel, and only the endpoint operator $D_{\\rm sink}D_{\\rm source}^{-1}$ acts on each role.",
  "At a vertex $v$, the invariant is that the stored array equals $D_v$ applied",
  page="frames",
  frm=["exchange-network", "matrices-and-linear-maps", "permutations-bijections-and-permutation-matrices"])

S131_3 = infer("S1.3.1.3",
  "Nested nondegenerate subspaces of an $m$-dimensional bilinear space can be attached to gates and terminals so that the only decreasing edges are the central-wire edges, and each edge's orthogonal residual has dimension equal to the number of smaller operations the edge needs.",
  "Every edge joins comparable nondegenerate labels.  The only decreasing",
  page="subspace-labels",
  frm=["exchange-network", "frames", "vector-spaces-subspaces-dimension-and-rank", "inner-products-bilinear-forms-and-orthogonal-complements"])

S131_4 = infer("S1.3.1.4",
  "The ranks of all edge changes sum to $s<Wm$, because the dimension lost on decreasing edges is less than half the number of source ranks that the rational interface adds.",
  "The sum of the rational ranks of all edge differences is",
  frm=["subspace-labels", "frames", "exchange-network", "matrices-and-linear-maps", "vector-spaces-subspaces-dimension-and-rank"])

S131 = show("S1.3.1",
  "There is a fixed network of $W$ wires, using only pointwise XOR gates, that exchanges two banks and restores every scratch wire, and for which the edge changes in a suitable frame assignment have total rank $s<Wm$.",
  "Build the three-stage exchange network from three-element subsets, choose frames whose intermediate changes cancel at pointwise gates, label gates and terminals by nested subspaces, and add up the residual dimensions.",
  mot("The recursion will need one smaller call per unit of edge rank, so the labelling must make the total edge rank fall below the trivial bound $Wm$.", "explicit",
      "the subspace assignments. The decisive property is that the total"),
  [S131_1, S131_2, S131_3, S131_4], page="rank-saving",
  frm=["circuits-and-directed-acyclic-graphs", "vector-spaces-subspaces-dimension-and-rank"],
  salient="The saving $Wm-s$ is strictly positive but tiny, a relative deficit of about $1.5\\times10^{-11}$, so the construction must be exact about every rank it counts.")

S132_1 = infer("S1.3.2.1",
  "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
  "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
  page="matrix-factorization",
  frm=["gaussian-elimination-and-triangular-matrices", "matrices-and-linear-maps", "vector-spaces-subspaces-dimension-and-rank", "permutations-bijections-and-permutation-matrices"])

S132_2 = infer("S1.3.2.2",
  "Transform $D$ and $H$ by the triangular factors, then replace each of the $a$ ones of $\\Pi$ by a three-update sequence containing exactly one interchange of $b$-digit fields.",
  "It uses just one interchange.  There are $a$ ones, which proves the",
  frm=["matrix-factorization", "controlled-shift"])

S132 = show("S1.3.2",
  "For a rational $m\\times m$ matrix $A$ of rank $a$, the shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ takes exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
  "Factor $A$ into lower-triangular pieces, apply them with controlled shifts, and turn each one of the remaining partial permutation into a single field interchange.",
  mot("Lower-triangular changes of coordinates update a later field from earlier ones, which is exactly the direction in which controlled shifts run in linear time.", "explicit",
      "earlier fields in linear time.  Lower triangular changes of coordinates"),
  [S132_1, S132_2], page="matrix-shear",
  frm=["controlled-shift", "modular-arithmetic", "gaussian-elimination-and-triangular-matrices"],
  adds=[B("a", "matrix rank", "the rational rank of the matrix $A$, which is the number of smaller interchanges the shear needs", "count"),
        B("b", "field width", "the number of radix-$q$ digits in each interchanged field", "count")])

S133_a = infer("S1.3.3a",
  "Distribute whole rows cyclically among the $W$ roles and apply, on each edge, the shear of the edge matrix to that role stream; the endpoint matrices then give the shear $H\\leftarrow H+D$ on every role, scratch roles included.",
  "Split whole rows cyclically into $W$ role streams within each prefix",
  frm=["rank-saving", "matrix-shear", "frames", "tape-stream-operations"])
S133_b = infer("S1.3.3b",
  "Two equal chunks are interchanged by the three updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, only the middle one using the network.",
  "To interchange the two full chunks, perform")
S133_c = infer("S1.3.3c",
  "The number of recursive calls is the sum of the edge ranks, so the time per unit volume $F_k$ obeys $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
  "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
  frm=["recurrences-and-geometric-sums"])
S133_d = infer("S1.3.3d",
  "Since $s/W<m^\\tau$, the geometric sum of the recurrence is $O(m^{k\\tau})$, so $F_k=O(e^\\tau)$.",
  "Hence $F_k=O(e^\\tau)$.",
  frm=["recurrences-and-geometric-sums"])

S13 = show("S1.3",
  "Two disjoint address chunks of $e$ radix-$q$ digits each, with $e$ a power of $m$ and enough rows, can be interchanged in $O(Ve^\\tau)$ time.",
  "Apply the fixed bit network to $W$ cyclic role streams, implementing every edge change by smaller shears and hence smaller interchanges, one per unit of edge rank, and solve the resulting recurrence.",
  mot("Dividing cost by volume, each increase of the chunk width by the factor $m$ multiplies the recursive contribution by only $s/W$, and $s/W<m$.", "explicit",
      "increases the recursive contribution by $s/W<m$. This strict inequality"),
  [S131, S132, S133_a, S133_b, S133_c, S133_d], page="power-width-interchange",
  frm=["tape-stream-operations", "controlled-shift", "recurrences-and-geometric-sums"],
  adds=[B("e", "chunk width", "the number $m^k$ of radix-$q$ digits in each of the two chunks being interchanged", "count")],
  salient="The cost is $O(Ve^\\tau)$ with $\\tau<1$, sublinear in the chunk width, although the shear on every role is itself built from interchanges of narrower chunks.")

S14 = infer("S1.4",
  "An arbitrary width is split in base $m$ into pieces, rows are padded to a multiple of $W^k$, and each pair of pieces is interchanged by the power-width procedure, for a total of $O(Vu^\\tau)$.",
  "O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau).",
  frm=["power-width-interchange", "positional-number-systems-and-carries"])
S15 = infer("S1.5",
  "Binary chunks of $u$ bits are padded to radix-$q$ chunks, interchanged, and unpadded, giving the stated bound for exact swaps of $u$-bit chunks.",
  "Since $e=O(u)$ for fixed $q$, the bound is",
  frm=["tape-stream-operations"])

S1 = show("S1",
  "Two disjoint equal-width bit chunks of $u$ bits in an address array can be swapped in $O(Vu^\\tau)$ steps for a fixed $\\tau<1$, by XOR combinations of data whose final effect is an exact permutation.",
  "Reduce arbitrary chunk widths to power-width interchanges, which are obtained from a fixed linear network with a strict rank saving.",
  mot("The recursion over the network only handles chunk widths that are powers of the label dimension with enough rows, so general widths are reduced to those.", "explicit",
      "We have proved the fast operation for power widths with enough rows."),
  [S1_1, S1_2, S13, S14, S15], page="chunk-interchange",
  frm=["bitwise-operations-and-xor", "permutations-bijections-and-permutation-matrices", "multitape-turing-machine"],
  adds=[B("u", "chunk width", "the number of bits in each of the two address chunks being swapped", "count")],
  salient="Swapping two $u$-bit chunks costs less than a full pass per bit of chunk width ($\\tau<1$), even though the procedure runs through XOR combinations of the data; the reason is that the network needs fewer than $Wm$ smaller calls.")

# ---------------- S2: simultaneous butterfly layer ----------------
S21_1 = infer("S2.1.1",
  "Each edge's frame change is a product of translation kernels $aI+bX_v$ or their inverses, one for each vector in an orthonormal basis of the edge residual.",
  "=\\prod_{j=1}^{\\rho_{\\rm edge}}(aI+bX_{v_j})^{\\epsilon_j},")
S21_2 = infer("S2.1.2",
  "Running the complex network with these column frames on a group of selected axes makes exactly $s$ calls, each on $1/m$ of the axes, and leaves $C^{\\otimes}$ on every role, scratch roles included, with no extra recursive calls from the corrections.",
  "$e=mf$ selected axes.  Summing its residual dimensions gives exactly")
S21_3 = infer("S2.1.3",
  "With $H_0=b\\,\\mathsf S C\\mathsf S$, the layer of $D$ butterflies is $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, so a $C$ layer gives the normalized layer by exact diagonal phase operations.",
  "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.")
S21 = show("S2.1",
  "In the complex network with Hadamard-diagonalized phase frames, a layer of $D$ butterflies $H_0$ reduces to $C^{\\otimes D}$ for the two-point kernel $C=aI+bX$, which the network computes with $s<Wm$ smaller calls on groups of fewer selected bits.",
  "Express each edge's frame change as translation kernels on selected directions, run the network recursively on column frames, and convert the resulting $C$ layer to the $H_0$ layer by diagonal phases.",
  mot("Phase frames express a tensor product of $C$ on a group of selected bits through smaller groups of bits, which is what a recursion needs.", "explicit",
      "frames express a $C$ tensor product using smaller groups of"),
  [S21_1, S21_2, S21_3], page="phase-frames",
  frm=["exchange-network", "frames", "subspace-labels", "rank-saving", "fft-butterfly", "matrices-and-linear-maps", "arithmetic-modulo-2-and-linear-algebra-over-f-2"])

S22_1 = infer("S2.2.1",
  "Eight conditional rotations of two integers $u,w$ flip the parity of $u$ exactly when the control $c=1$ and restore the arbitrary scratch integer $w$.",
  "If $c=0$, these operations do nothing. If $c=1$, the first four operations")
S22_2 = infer("S2.2.2",
  "Packed cyclic shifts of all $f-1$ segments agree with the ideal XORs except at addresses where a guard value fails, a fraction at most $80(f-1)2^{-K}$ of all addresses.",
  "There are exactly twenty excluded values for each guard in")
S22_3 = infer("S2.2.3",
  "The exceptional records are extracted, stably radix-sorted by destination rank and reinserted, which implements the ideal XOR at every address.",
  "This implements $T_0$ everywhere.")
S22_4 = infer("S2.2.4",
  "With the bad fraction exponentially small in $K$, the total time is $O(V(L^\\tau+1))$ for every payload.",
  "Equation~\\eqref{eq:packed-bad-fraction} proves")
S22 = show("S2.2",
  "The selected bits at $f$ positions spaced $K$ apart in one address chunk can be XORed into the corresponding bits of another chunk of $L=fK$ bits, with a third chunk as restored scratch, in $O(V(L^\\tau+1))$ steps.",
  "Perform all additions at once by a constant number of cyclic shifts and chunk swaps, which equal the ideal XORs except on a small explicit set of exceptional addresses, then repair that set by sorting.",
  mot("A cyclic shift of a whole chunk moves all packed segments in one linear pass, and it fails only at addresses where a guard value is near an end of its range, which are few and identified by address alone.", "recoverable"),
  [S22_1, S22_2, S22_3, S22_4], page="packed-selected-bit-addition",
  frm=["chunk-interchange", "controlled-shift", "tape-stream-operations", "bitwise-operations-and-xor", "arithmetic-modulo-2-and-linear-algebra-over-f-2"],
  adds=[B("f", "bit count", "the number of selected bit positions, one in each $K$-bit block, XORed at once", "count"),
        B("L", "chunk width in bits", "the number $fK$ of address bits in each of the three chunks", "count")],
  salient="The exceptional set has density only $O(d2^{-K})$, exponentially small in the block width $K$, so sorting it costs $o(V)$ although a constant number of shifts handles all other addresses.")

S23_1 = infer("S2.3.1",
  "Normalized time obeys $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ for a group of $e$ chunks, since the $s$ child calls run on streams of volume $V/W$ and the basis changes cost $O(V((eK)^\\tau+1))$.",
  "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),",
  page=None, frm=["rank-saving", "recurrences-and-geometric-sums", "phase-frames"])
S23_2 = infer("S2.3.2",
  "Stopping the recursion at $e<d^{1/2}$, splitting the chunks into base-$m$ pieces and summing, the normalized cost of a layer is $O(d^{\\lambda'})$ for a fixed $\\lambda'<1$.",
  "=O(d^{\\lambda'})",
  frm=["recurrences-and-geometric-sums"])

S24_1 = infer("S2.4.1",
  "The arithmetic dependency depth of the recursive layer is at most $8B^2d^{\\nu+1}$ for constants $B$ and $\\nu$ determined by the fixed network.",
  "A(e)\\le 8dB^{k+1}\\le8B^2d^{\\nu+1}.")
S24_2 = infer("S2.4.2",
  "A value at depth $\\ell$ lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ and has modulus at most $2^\\ell$, so $p+\\Delta$ fractional bits and $\\Delta+3$ integer bits per component hold every intermediate value exactly.",
  "lies in \\(2^{-(p+\\ell)}\\mathbb Z[i]\\) and has modulus at most")
S24_3 = infer("S2.4.3",
  "Since $\\epsilon C_1<1$ the guard width $\\Delta$ is $o(p)$, so the full coefficient width is $O(p)$ and all additions, shifts and phase changes cost $O(p)$ per coefficient.",
  "\\(\\Delta=o(p)\\), and the full coefficient width is \\(O(p)\\), as")
S24 = show("S2.4",
  "Within one butterfly layer all intermediate values are exact Gaussian dyadics held in $O(p)$ bits per component, so a single truncation to the $2^{-p}$ grid after the whole contractive layer suffices.",
  "Bound the arithmetic dependency depth of the recursive network, and let the depth bound both the denominator growth and the magnitude growth.",
  mot("Intermediate operators of the accelerated network need not be contractions, so the layer must be evaluated exactly and rounded only once at the end.", "explicit",
      "The accelerated network is evaluated exactly until an entire"),
  [S24_1, S24_2, S24_3], page="guard-bits",
  frm=["contraction-error", "fixed-point-numbers-dyadic-rationals-and-rounding", "complex-numbers"])

S25 = infer("S2.5",
  "The row construction and the recurrence give total time $O(Vd^{\\lambda'})$ on fixed tapes, and the exact $C$ layer is converted to $\\mathcal H=H_0^{\\otimes D}$.",
  "The row construction and the recurrence analysis",
  frm=["guard-bits", "packed-selected-bit-addition", "phase-frames"])
S26 = infer("S2.6",
  "Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ preserves the disk, and truncation changes each coefficient by less than $\\sqrt2\\,2^{-p}$.",
  "Finally, every row of $\\mathcal H$ has",
  frm=["contraction-error", "vector-norms-and-the-triangle-inequality"])

S2 = show("S2",
  "Applying $H_0$ to one selected bit in each of $D\\le d$ address chunks of width $K$ at once, on arrays of ring records with complex fixed-point coefficients, takes $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$ and leaves error below $\\sqrt2\\,2^{-p}$ after one truncation.",
  "Reduce a layer to the complex phase network, run it recursively with the binary basis changes done by packed bit additions, evaluate the whole layer exactly with guard bits, and truncate once.",
  mot("Separate butterfly factors would need $D$ whole-array passes, so the layer is organised as one recursion that splits the selected axes among smaller calls.", "explicit",
      "factors would require $D$ whole-array passes."),
  [S21, S22, S23_1, S23_2, S24, S25, S26], page="simultaneous-butterfly-layer",
  frm=["chunk-interchange", "complex-numbers", "bitwise-operations-and-xor"],
  adds=[B("D", "number of selected chunks", "the number of address chunks, at most $d$, in each of which one bit is selected for the butterfly", "count")],
  salient="The exponent $\\lambda'$ is below one, so the whole layer costs less than $D$ separate passes; it inherits the strict inequality $s/W<m$ of the complex network.")

# ---------------- S3: synthetic transforms and layout ----------------
S31_1 = infer("S3.1.1",
  "Roots $\\omega_t=y^{2r/t}$ satisfy character cancellation in $\\mathcal R_r$, so $F_t^+F_t^-=t^{-1}I$ even though the ring has zero divisors.",
  "The ring has zero divisors, so we verify character cancellation")
S31_2 = infer("S3.1.2",
  "The decimation-in-frequency step pairs entries, applies $H_0$, multiplies one output by $\\omega_t^{-k}$ (a signed shift) and recurses in the two halves, computing $F_t^-$.",
  "the $b=1$ output by $\\omega_t^{-k}$, and then apply the length-$t/2$")
S31 = show("S3.1",
  "The normalized Fourier transform over $\\mathcal R_r$ with root of unity $\\omega_t=y^{2r/t}$ is computed by a radix-two recursion in which every twiddle multiplication is a signed shift, so only butterflies cost arithmetic.",
  "Use radix-two decimation in frequency over the negacyclic ring, where powers of $y$ act as exact roots of unity.",
  mot("Powers of $y$ serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list.", "explicit",
      "serve as roots of unity in the remaining axes, and multiplication by"),
  [S31_1, S31_2], page="synthetic-transform",
  frm=["negacyclic-ring", "dft", "fft-butterfly", "roots-of-unity", "polynomials"],
  adds=[B("t", "transform length", "the power-of-two length of one axis of the synthetic transform", "count")])

S32_1 = infer("S3.2.1",
  "The recursion writes the output $(F_t^-z)_j$ in slot $\\mathrm{rev}(j)$, so the stored order is the bit-reversal permutation $B_t$ and no whole index is moved.",
  "directly in this order; it does not move whole frequency indices.")
S32_2 = infer("S3.2.2",
  "Traversing the recursion in reverse consumes this stored order, and the exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
  "so the reverse procedure composed with $B_tF_t^-$ is")
S32 = show("S3.2",
  "The forward transforms leave their outputs in bit-reversed record order $B_t$, and the opposite transform consumes that same order, so no reordering is executed between the forward transforms and the inverse.",
  "Run the recursion to write outputs where it produces them, and run the inverse recursion backwards so that it starts from that order.",
  mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the product can be formed in the retained order.", "explicit",
      "Pointwise multiplication commutes with applying the same record"),
  [S32_1, S32_2], page="bit-reversed-order",
  frm=["synthetic-transform", "fft-butterfly", "permutations-bijections-and-permutation-matrices"])

S33_1 = infer("S3.3.1",
  "The axis steps of a round group into one parallel butterfly followed by one recordwise monomial multiplication $y^E$, a signed shift of each polynomial.",
  "Consequently the individual axis steps may be grouped as a parallel")
S33_2 = infer("S3.3.2",
  "Placing the selected bits of all axes at a common offset in $K$-bit chunks uses $O(p/K)$ chunk exchanges of width $K$, normalized cost $O(pK^{\\tau-1})$.",
  "=O\\bigl(Tp\\,pK^{\\tau-1}\\bigr).",
  frm=["chunk-interchange"])
S33_3 = infer("S3.3.3",
  "The at most $\\ell$ rounds on chunked axes each apply the simultaneous layer at cost $O(Tpd^{\\lambda'})$, normalized cost $\\ell d^{\\lambda'}$.",
  "The simultaneous-layer procedure therefore applies at cost",
  frm=["simultaneous-butterfly-layer"])
S33_4 = infer("S3.3.4",
  "The at most $K$ rounds on prefix slots use individual butterflies at normalized cost $O(dK)$.",
  "most $b+1\\leq K$ rounds on prefix slots, giving cost $O(TpdK)$.")
S3 = show("S3",
  "The synthetic transform of $d-1$ axes of record length $r$ and total size $T$ can be laid out so that each round uses the simultaneous layer, at total normalized cost $dK+pK^{\\tau-1}+\\ell d^{\\lambda'}$ per unit of $Tp$.",
  "Compute the transform round by round, with a layout permutation placing the selected bits of all participating axes at a common offset in $K$-bit chunks, and add up the costs of the layout, the chunked rounds and the prefix rounds.",
  mot("To apply the simultaneous layer in a transform round, the selected bits of the participating axes must lie at a common offset in consecutive $K$-bit chunks.", "explicit",
      "we must place the selected bits of the participating axes at a common"),
  [S31, S32, S33_1, S33_2, S33_3, S33_4], page="transform-layout",
  frm=["simultaneous-butterfly-layer", "chunk-interchange", "tape-stream-operations", "negacyclic-ring"],
  salient="The three cost terms $dK$, $pK^{\\tau-1}$ and $\\ell d^{\\lambda'}$ each carry a power of $p$ below one only because $K$ is a small power of $d$ and $d$ a small power of $p$.")

# ---------------- S4: ring convolution ----------------
S41_1 = infer("S4.1.1",
  "Evaluating the coefficient polynomials at $B_0=2^{4p}$ packs each into a signed integer of $4pr$ bits, and every product coefficient is below $B_0/2$ in size, so adjacent fields cannot collide.",
  "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2.")
S41_2 = infer("S4.1.2",
  "Centered extraction with a carry of at most one recovers each product coefficient exactly from the integer product, including negative values.",
  "Thus $\\widehat h_j=h_j$.")
S41_3 = infer("S4.1.3",
  "Subtracting the coefficient at $j+r$ from the one at $j$ reduces the product modulo $y^r+1$, and a shift by $p+\\ell$ bits gives the normalized truncated product.",
  "To reduce them modulo $y^r+1$, subtract the")
S41_4 = infer("S4.1.4",
  "Four integer products on $O(rp)$-bit inputs dominate, so the whole normalized ring product costs $O(rp\\log(rp))$.",
  "Four exact integer products dominate the linear")
S41 = show("S4.1",
  "Two polynomials of $\\mathcal R_r$ with $p$-bit grid coefficients can be multiplied exactly, and the normalized product $Q_p(fg/r)$ returned, in $O(rp\\log(rp))$ time with the established $O(N\\log N)$ multiplier.",
  "Use signed Kronecker substitution: pack coefficients into big signed integers by evaluation at $2^{4p}$, multiply, and unpack with centered extraction.",
  mot("The established fixed-tape integer multiplier of Harvey and van der Hoeven multiplies the polynomial records, so each product is turned into integer products.", "explicit",
      "To multiply the polynomial records, we use the fixed-tape integer"),
  [S41_1, S41_2, S41_3, S41_4], page="kronecker-packing",
  frm=["negacyclic-ring", "hh-multiplier", "polynomials", "positional-number-systems-and-carries"])

S42_1 = infer("S4.2.1",
  "Perform both forward transforms, retaining their common order, multiply corresponding records by the packing procedure, apply the opposite transform to that order, and scale exactly by $M=T/r$.",
  "Perform both forward transforms and retain their common $LB$ order.",
  frm=["transform-layout", "bit-reversed-order", "kronecker-packing"])
S42_2 = infer("S4.2.2",
  "The three transform errors and the product truncation total less than $M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$, and the result lies in the disk when one operand has norm at most $\\rho<1$ and the error is below $1-\\rho$.",
  "$M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$, as claimed.",
  frm=["contraction-error"])
S4 = show("S4",
  "On arrays over $\\mathcal R_r$ indexed by a product of cyclic groups, the normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ is computed with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "Take two forward synthetic transforms, multiply pointwise in the retained order by Kronecker packing, apply the opposite transform, and rescale by the known factor $M=T/r$.",
  mot("A convolution is a pointwise product of transforms, and because the product commutes with a common permutation of the records the forward outputs can stay in the retained order.", "recoverable"),
  [S41, S42_1, S42_2], page="ring-convolution",
  frm=["cyclic-convolution", "convolution-of-sequences", "transform-layout", "synthetic-transform", "bit-reversed-order", "contraction-error"])

# ---------------- S5: resampling ----------------
S51_1 = infer("S5.1.1",
  "There are linear contractions $A$ from length $s_i$ to length $t_i$ and $B_0$ from $t_i$ to $s_i$, and a coordinate-permutation identity $P_{s_i}F_{s_i}=2^{2\\alpha^2}B_0P_{t_i}F_{t_i}A$.",
  "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and")
S51_2 = infer("S5.1.2",
  "Harvey and van der Hoeven's Gaussian identity $\\mathsf T P_sF_s=P_tF_t\\mathsf S$ with $\\|N-I\\|<2^{-\\alpha^2\\theta}$ makes $N$ invertible by the Neumann series and gives the identity.",
  "\\mathsf T P_sF_s=P_tF_t\\mathsf S,")
S51_3 = infer("S5.1.3",
  "Ordered numerical routines for $A$ and $B_0$ built from the Gaussian maps and a subsequence selection have error below $p^2$ and time $O(t_ip^{3/2+\\delta}\\alpha)$ on a line of length $t_i$.",
  "Contraction of the exact maps yields errors less than $16p<p^2$ and")
S51 = show("S5.1",
  "A Fourier transform of length $s_i$ equals, up to the scale $2^{2\\alpha^2}$ and two coordinate permutations kept inside the identity, a transform of length $t_i>s_i$ between two cheap Gaussian-weighted contractions $A$ and $B_0$.",
  "Use the Gaussian resampling identity, invert its near-identity correction by a Neumann series, and implement the maps with ordered Gaussian arithmetic.",
  mot("The coprime source lengths needed for the product differ from the power-of-two lengths the synthetic transforms handle, and resampling connects the two.", "explicit",
      "connects these two shapes. Its usual implementation sorts twice on each"),
  [S51_1, S51_2, S51_3], page="gaussian-resampling",
  frm=["dft", "roots-of-unity", "contraction-error", "fixed-point-numbers-dyadic-rationals-and-rounding", "vector-norms-and-the-triangle-inequality", "hh-multiplier", "complex-numbers"],
  adds=[B("\\alpha", "window parameter", "the integer width parameter $2\\le\\alpha<\\sqrt p$ of the Gaussian weights, with $\\alpha^4$ at least $p$ over the relative gap $t_i/s_i-1$", "direct")])

S52_1 = infer("S5.2.1",
  "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with the maps applied line by line along each axis of the padded box.",
  "Tensoring \\eqref{eq:no-sort-one-dimensional} proves")
S52_2 = infer("S5.2.2",
  "Exposing and restoring the lines of all $d$ axes costs $O(Tp\\,d^2(1+\\ell^\\tau))$ by chunk swaps, and the line maps cost $O(dTp^{3/2+\\delta}\\alpha)$.",
  "costs $O(Tp(1+\\ell^\\tau))$. Exposing and restoring one axis needs",
  frm=["chunk-interchange"])
S52 = show("S5.2",
  "The tensor product of the one-dimensional transforms along each axis of the padded array, of axis lengths $t_1,\\dots,t_d$, has error below $dp^2$ and cost $O(dTp^{3/2+\\delta}\\alpha)$ plus $O(Tp\\,d^2(1+\\ell^\\tau))$ for axis movement.",
  "Apply the one-dimensional maps to one coordinate line at a time, bringing each axis in turn to the innermost position by chunk swaps.",
  mot("For the tensor product, the one-dimensional maps are applied to one coordinate line at a time.", "explicit",
      "For the tensor product, apply the one-dimensional maps to one coordinate"),
  [S52_1, S52_2], page="multidimensional-transform",
  frm=["dft", "cyclic-convolution", "convolution-of-sequences", "matrices-and-linear-maps", "chunk-interchange"])

S53 = infer("S5.3",
  "For even $t_i$ the chirp array $a$ satisfies $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, so the middle transform is a cyclic convolution between two chirp multiplications.",
  "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because",
  page="chirp-identity",
  frm=["dft", "cyclic-convolution", "roots-of-unity", "complex-numbers"])
S54 = infer("S5.4",
  "Since $F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and a coordinate permutation commutes with pointwise products, the retained permutation $R$ cancels, giving $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
  "$F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence",
  frm=["multidimensional-transform", "chirp-identity", "permutations-bijections-and-permutation-matrices", "modular-arithmetic"])
S5 = show("S5",
  "The transforms of lengths $s_i$ needed for the product are computed through power-of-two lengths $t_i$ by resampling and one chirp convolution, with the coordinate permutations left inside the formulas so that they cancel across a convolution and no full sort is executed.",
  "Apply the one-dimensional Gaussian identity along every axis, turn the middle transform into a convolution by Bluestein's chirp, and show that the retained source permutation cancels between the forward and opposite transforms.",
  mot("The usual implementation of Gaussian resampling sorts twice on each coordinate; retaining both permutations in the transform formula avoids those sorts.", "explicit",
      "coordinate. We retain both permutations in the transform formula and"),
  [S51, S52, S53, S54], page="permutation-cancellation",
  frm=["dft", "cyclic-convolution", "roots-of-unity", "permutations-bijections-and-permutation-matrices"],
  salient="No sort is ever executed: the permutation $R$ and its inverse sit on both sides of the pointwise product, so only the cancellation $(u*v)/S^2$ remains.")

# ---------------- S6: algorithm ----------------
S61_1 = infer("S6.1.1",
  "Fixed rational exponents $\\tau=\\sigma=1-2^{-50}$, $\\lambda'=1-2^{-54}$, $c=2^{-56}$, $\\epsilon=2^{-75}$, $\\delta=1/16$, $\\kappa=2^{-182}$ satisfy all the layer conditions with room to spare.",
  "Take the following fixed rational numbers:")
S61_2 = infer("S6.1.2",
  "Sizes are set by $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$.",
  "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,")
S61_3 = infer("S6.1.3",
  "The power of two $T\\in[4n/b,8n/b)$ and $r=2^\\ell$ give axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod_i t_i=T$ and $t_d=r$.",
  "t_i\\in\\{r/2,r\\},\\qquad \\prod_i t_i=T,\\qquad t_d=r.")
S61_4 = infer("S6.1.4",
  "These give $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$, so $r$ exceeds every fixed power of $p$.",
  "Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),\\quad")
S61 = show("S6.1",
  "Fixed rational exponents $(\\tau,\\sigma,\\lambda',c,\\epsilon,\\delta,\\kappa)$ and sizes $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, $T\\approx n/b$, $r=2^\\ell$ with prime axis lengths $s_i<t_i$ make $Tp=\\Theta(n)$ and satisfy every condition of the layer and transform interfaces.",
  "State the fixed exponents, check the layer inequalities, and derive all sizes from $n$.",
  mot("The interfaces of the earlier procedures impose inequalities among the exponents, and one rational choice must satisfy all of them at once so that every size is computable.", "recoverable"),
  [S61_1, S61_2, S61_3, S61_4], page="parameter-choice",
  frm=["prime-axis-lengths", "crt-axis-map", "simultaneous-butterfly-layer", "transform-layout", "chunk-interchange", "logarithms-exponentials-floors-and-ceilings"])

S62_1 = infer("S6.2.1",
  "For $0<\\eta<1/4$ and large $x$ the interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains more than $d$ primes, for both $x=r/2$ and $x=r$.",
  "contains at least $\\eta x/(2\\log x)$ primes. Here $\\log$ is the natural")
S62_2 = infer("S6.2.2",
  "Choosing distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ gives $\\gcd(s_i,t_i)=1$ and $T/2<S<T$.",
  "Together with $s_i<t_i$, this gives $T/2<S<T$.")
S62_3 = infer("S6.2.3",
  "With $\\theta_i=t_i/s_i-1>\\eta$ one has $\\alpha^4\\theta_i>p$, so every hypothesis of the resampling lemma holds.",
  "\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\geq6b=p.",
  frm=["gaussian-resampling"])
S62 = show("S6.2",
  "Distinct odd primes $s_i$ slightly below the powers of two $t_i$, with $S=\\prod_i s_i$ filling more than half the padded box ($T/2<S<T$) and each ratio $t_i/s_i-1\\ge\\eta$, exist and can be found in time $n^{o(1)}$.",
  "Count primes in the interval $((1-2\\eta)t_i,(1-\\eta)t_i]$ with explicit prime-number estimates, then multiply the lower bounds.",
  mot("The product of the source lengths must occupy a fixed fraction of the padded box while each ratio $t_i/s_i$ leaves enough separation for resampling.", "explicit",
      "The distinct prime lengths $s_i$ must be close to the powers of two"),
  [S62_1, S62_2, S62_3], page="prime-axis-lengths",
  frm=["logarithms-exponentials-floors-and-ceilings", "primes-coprimality-and-the-extended-euclidean-algorithm", "gaussian-resampling"],
  adds=[B("\\eta", "relative gap", "the quantity $1/(4d)$ so that each prime $s_i$ lies between $(1-2\\eta)t_i$ and $(1-\\eta)t_i$", "direct")])

S63 = infer("S6.3",
  "Splitting both operands into $q=\\lceil n/b\\rceil$ digits of $b$ bits makes their product a digit convolution of degree below $S$, so cyclic convolution modulo $x^S-1$ has no wraparound, followed by carries.",
  "Thus convolution modulo $x^S-1$ has no nonzero wraparound.  Every product",
  page="radix-digit-convolution",
  frm=["convolution-of-sequences", "cyclic-convolution", "positional-number-systems-and-carries", "schoolbook-and-karatsuba-multiplication"])

S64_1 = infer("S6.4.1",
  "The map $x\\mapsto\\prod_i x_i^{\\mu_i}$ with $\\mu_i=P_i^{-1}\\bmod s_i$ is an algebra isomorphism that preserves cyclic convolution.",
  "$\\Phi$ is an isomorphism and preserves cyclic convolution.")
S64_2 = infer("S6.4.2",
  "In mixed-radix coordinates the coordinate of axis $i$ is $a_i+\\mu_i\\sum_{j<i}a_jP_j$, so each update is a prefix-controlled cyclic shift, performed in the order $i=d,\\dots,1$.",
  "Each triangular update is a prefix-controlled cyclic shift.  The",
  frm=["controlled-shift"])
S64_3 = infer("S6.4.3",
  "Reordering the padded axes by chunk swaps and doing the $d$ shifts costs $O(Tp\\,d^2(1+\\ell^\\tau))$.",
  "uses $O(d^2)$ such moves.  Therefore the map $\\Phi$, its inverse, and",
  frm=["chunk-interchange"])
S64 = show("S6.4",
  "The Chinese-remainder map $\\Phi$ is an algebra isomorphism from cyclic convolution of length $S=s_1\\cdots s_d$ to convolution on the product of cyclic axes of lengths $s_i$, and it and its inverse cost $O(Tp\\,d^2(1+\\ell^\\tau))$ by triangular controlled shifts.",
  "Use the Chinese remainder theorem with coordinate powers chosen so that the change of order is a sequence of controlled cyclic shifts.",
  mot("Coordinate powers are chosen so that the change of order becomes a sequence of controlled cyclic shifts, which run in linear time.", "explicit",
      "To use the source tensor, we first place the ordinary coefficient stream"),
  [S64_1, S64_2, S64_3], page="crt-axis-map",
  frm=["radix-digit-convolution", "cyclic-convolution", "controlled-shift", "chunk-interchange", "primes-coprimality-and-the-extended-euclidean-algorithm", "modular-arithmetic"])

S65_1 = infer("S6.5.1",
  "The map $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ is well defined and multiplies coefficient $k$ by $\\zeta^k$.",
  "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.")
S65_2 = infer("S6.5.2",
  "A product term with $k+l=j+hr$ gets the factor $\\zeta^{k+l}(-1)^h=\\zeta^j$, so negacyclic wrap after the twist is exactly the cyclic wrap, undone by untwisting.",
  "Untwisting therefore recovers the cyclic coefficient with the correct")
S65_3 = infer("S6.5.3",
  "Normalized complex cyclic convolution of length $r$ on the last axis is therefore $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)$, a bilinear contraction.",
  "by $T$ is already part of $\\mathcal M_r$.  The maps $D_\\pm$ and")
S65 = show("S6.5",
  "Substituting $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ multiplies coefficient $k$ by $\\zeta^k$ and turns cyclic convolution of length $r$ into negacyclic polynomial multiplication, exactly undone by untwisting.",
  "Twist the last cyclic coordinate by $\\zeta^k$, convolve over the ring $\\mathbb C[y]/(y^r+1)$, and untwist.",
  mot("The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist.", "explicit",
      "The power-of-two complex convolution used in the chirp identity is"),
  [S65_1, S65_2, S65_3], page="phase-twist",
  frm=["negacyclic-ring", "cyclic-convolution", "roots-of-unity", "complex-numbers"])

S66_1 = infer("S6.6.1",
  "The computed chirp transform multiplies by the conjugate chirp, convolves with the chirp via the twisted ring convolution, and multiplies again, evaluating $QF_{\\boldsymbol t}$.",
  "$x$ of norm at most $.6$, the computed chirp transform forms the arrays",
  frm=["chirp-identity", "ring-convolution", "phase-twist"])
S66_2 = infer("S6.6.2",
  "The source transform applies the Gaussian map $\\mathcal A$, the chirp transform, the map $\\mathcal B_0$ and the exact scale $2^\\gamma$, with exact counterpart $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
  "For a source disk-grid tensor of norm at most $.5$, write",
  frm=["gaussian-resampling", "multidimensional-transform", "chirp-identity"])

S67_1 = infer("S6.7.1", "Apply the coefficient-address map $\\Phi$ with its padded layout to the digit arrays, obtaining the source arrays $u,v$ of norm below $1/4$.",
  "Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain")
S67_2 = infer("S6.7.2", "Compute the source transforms $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
  "Compute $\\widetilde{\\mathscr F}(u)$ and")
S67_3 = infer("S6.7.3", "Multiply corresponding complex coefficients exactly and truncate to $p$ fractional bits, obtaining the source array $z$.",
  "Multiply corresponding complex coefficients exactly and truncate")
S67_4 = infer("S6.7.4", "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its numerators exactly by $S$, giving $\\widetilde w$ approximating $(u*v)/S$.",
  "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid")
S67_5 = infer("S6.7.5", "Multiply by $2^{2b+4}S$, round to integers, write them in $(3b+1)$-bit words, and apply $\\Phi^{-1}$ including removal of padding.",
  "Multiply the grid numerators of $\\widetilde w$ exactly by")
S67_6 = infer("S6.7.6", "Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits most significant first.",
  "Propagate radix-$2^b$ carries in increasing coefficient order.")
S67 = show("S6.7",
  "Running the digit placement, two source transforms, pointwise product, opposite-sign transform, rescaling, rounding, inverse address map and carry propagation yields a $2n$-bit output.",
  "Execute the six stages of the multiplication algorithm in order, using the procedures established above as subroutines.",
  mot("Each stage is one of the established procedures, so the algorithm is their composition in the order the convolution theorem prescribes.", "recoverable"),
  [S67_1, S67_2, S67_3, S67_4, S67_5, S67_6],
  frm=["crt-axis-map", "permutation-cancellation"])

S68_1 = infer("S6.8.1",
  "A linear contraction propagates an input error without increasing it, and a bilinear contraction adds the errors of its operands, so errors compose by adding through every call.",
  "A linear contraction propagates an input error without increasing it.",
  frm=["contraction-error"])
S68_2 = infer("S6.8.2",
  "The source transform has error below $E_s h_p$ with $E_s=9\\cdot2^\\gamma TL$ for $L=\\log_2T$, and its output stays in the disk.",
  "E_s=9\\,2^\\gamma TL,")
S68_3 = infer("S6.8.3",
  "The pointwise product $z$ has norm below $.5$ and error below $(2E_s+2)h_p$.",
  "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.")
S68_4 = infer("S6.8.4",
  "After the opposite transform and the first scale $S$, $\\widetilde w$ approximates $w=(u*v)/S$ with error below $E_wh_p$, $E_w<28\\cdot2^\\gamma T^2L$.",
  "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L.")
S68_5 = infer("S6.8.5",
  "After the second scale $2^{2b+4}S$ the absolute error is below $448b\\,2^{-3b/4}<1/2$, since $p=6b$.",
  "<448b\\,2^{-b+\\gamma}")
S68_6 = infer("S6.8.6",
  "Because the true coefficients are integers and the error is strictly below $1/2$, the nearest integer to the represented value is the unique correct coefficient.",
  "The strict error below $1/2$ makes the nearest integer to")
S68_7 = infer("S6.8.7",
  "The carry recurrence $d_j=(c_j+k_j)\\bmod 2^b$, $k_{j+1}=\\lfloor(c_j+k_j)/2^b\\rfloor$ keeps $0\\le k_j<2^{2b}$ and yields the radix digits of the exact product.",
  "k_0=0,\\qquad d_j=(c_j+k_j)\\bmod Q_0,\\qquad")
S68_8 = infer("S6.8.8",
  "The product is less than $2^{2n}$, so removing zero padding bits leaves exactly $2n$ output bits.",
  "reversal is a charged linear tape pass.  The exact product is less")
S68 = show("S6.8",
  "Removing the known normalizations $S$ and $2^{2b+4}$, the recovered coefficient error is strictly below $1/2$, so rounding gives the exact integer coefficients and carry propagation outputs the exact $2n$-bit product.",
  "Track disk membership and an absolute error bound through every computed call, scale the final error by the known normalizations, and compare with $1/2$.",
  mot("The true coefficients are integers, so an error strictly below $1/2$ identifies each one uniquely by rounding.", "explicit",
      "The strict error below $1/2$ makes the nearest integer to"),
  [S68_1, S68_2, S68_3, S68_4, S68_5, S68_6, S68_7, S68_8], page="exact-recovery",
  frm=["contraction-error", "guard-bits", "radix-digit-convolution", "phase-twist", "fixed-point-numbers-dyadic-rationals-and-rounding", "positional-number-systems-and-carries", "vector-norms-and-the-triangle-inequality"],
  salient="The final error is below $448b\\,2^{-3b/4}$, exponentially small in $b$, although the computed values are rescaled by about $2^{2b+4}S$; the precision $p=6b$ is what absorbs these scale factors.")

S6 = show("S6",
  "Placing radix-$2^b$ digits on prime axes by the CRT map, transforming both operands by resampling plus chirp convolution over the polynomial ring, multiplying pointwise, transforming with opposite sign, rescaling, rounding and carrying outputs the exact $2n$-bit product.",
  "Choose compatible parameters, reduce the product to a cyclic convolution of digits on prime axes, evaluate its three transforms by the established procedures, and verify that the recovered coefficients are exact.",
  mot("The remaining proof places the tape procedures inside the multiplication reduction and accounts for every change of representation.", "explicit",
      "The remaining proof places these procedures inside the multiplication"),
  [S61, S62, S63, S64, S65, S66_1, S66_2, S67, S68], page="multiplication-algorithm",
  frm=["ring-convolution", "permutation-cancellation", "positional-number-systems-and-carries", "cyclic-convolution"],
  adds=[B("b", "digit width", "the number $\\lceil\\log_2 n\\rceil$ of bits in each radix digit of the operands", "count"),
        B("S", "convolution length", "the product $s_1\\cdots s_d$ of the pairwise coprime source axis lengths, the length of the cyclic digit convolution", "direct")])

# ---------------- S7: time bound ----------------
S7_1 = infer("S7.1",
  "Direct substitution of the fixed exponents gives margins $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.",
  "g_1>\\frac12,\\quad g_2=2^{-181},\\quad g_3=2^{-129},\\quad")
S7_2 = infer("S7.2",
  "Thus the smallest margin is $\\min_i g_i=2^{-181}=2\\kappa$.",
  "Thus $\\min_i g_i=2^{-181}=2\\kappa$.")
S7_3 = infer("S7.3",
  "The first three rows are the terms of the synthetic transform cost, from $O(dK)$ scans, $O(p/K)$ chunk exchanges and at most $\\ell$ simultaneous rounds.",
  "The first three rows are the terms in")
S7_4 = infer("S7.4",
  "Axis exposure and restoration take $O(d^2)$ adjacent axis moves, each $O(V(1+\\ell^\\tau))$, giving the CRT and axis-layout row.",
  "Axis exposure and restoration require $O(d^2)$ adjacent axis moves.")
S7_5 = infer("S7.5",
  "The Gaussian line maps cost $O(dTp^{3/2+\\delta}\\alpha)$, which is $dp^{1/2+\\delta}\\alpha$ after dividing by $Tp$.",
  "For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines.")
S7_6 = infer("S7.6",
  "Chirps, twists and scalar products cost $O(dp^{1+\\delta})$ per entry, and the packed polynomial products cost $O(Tp\\log(rp))$.",
  "Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as")
S7_7 = infer("S7.7",
  "Setup at recursion nodes, per-record and per-line descriptor work, and the compact exceptional streams cost $o(Tp)$, since $r$ exceeds every fixed power of $p$ and the bad fraction is $2^{-K}$.",
  "costs at most $p^{A+C}=o(Tp)$.")
S7_8 = infer("S7.8",
  "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
  "Each of the seven displayed powers is at most $1-2\\kappa$ by")
S7_9 = infer("S7.9",
  "The complete large-input bound is therefore $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$, and schoolbook multiplication below a fixed cutoff covers the finitely many smaller lengths.",
  "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).")

S7 = show("S7",
  "Dividing costs by the volume $Tp$, seven dominant terms with powers of $p$ below one, with margins $g_1,\\dots,g_7$ all at least $2\\kappa$, give total time $O(n(\\lg n)^{1-\\kappa})$.",
  "Tabulate the normalized cost of every phase, bound each by a power of $p$ below one, and read off the exponent from the smallest margin.",
  mot("Costs are listed divided by the stored volume so that each phase can be compared with $p^{1}$.", "explicit",
      "$\\Theta(V)$ stored bits. Table~\\ref{tab:costs} lists costs after division"),
  [S7_1, S7_2, S7_3, S7_4, S7_5, S7_6, S7_7, S7_8, S7_9], page="time-bound",
  frm=["parameter-choice", "chunk-interchange", "simultaneous-butterfly-layer", "transform-layout", "ring-convolution", "gaussian-resampling", "crt-axis-map", "multiplication-algorithm", "exact-recovery", "logarithms-exponentials-floors-and-ceilings", "asymptotic-notation-beyond-big-o"],
  salient="The smallest margin is $2^{-181}=2\\kappa$, so $\\kappa=2^{-182}$ is exactly half of it; it equals $\\epsilon c(1-\\tau)$, the product of the dimension exponent, the chunk-width exponent and the interchange saving.")

S8 = infer("S8",
  "The power saving gives $T_A(n)/(n\\lg n)\\to0$ through all input lengths, so no constant $c_A$ gives an eventual lower bound $T_A(n)\\ge c_An\\lg n$, refuting the conjecture.",
  "The power saving proved here gives a limit of zero through all input lengths,",
  deferred=True,
  frm=["limits-and-limit-inferior", "schonhage-strassen-conjecture"])

ROOT = show("S0",
  "A single deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, refuting the $n\\log n$ optimality conjecture in this model.",
  "Build two fast tape procedures, a bit-chunk interchange and a simultaneous butterfly layer, use them to evaluate the transforms of a digit convolution on an array of ring records, assemble the exact multiplier, and total its cost.",
  mot("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so a power saving needs savings in both movement and arithmetic.", "explicit",
      "We therefore need savings in both movement and arithmetic. Two tape"),
  [S1, S2, S3, S4, S5, S6, S7, S8], page="main-theorem",
  frm=["schonhage-strassen-conjecture", "hh-multiplier", "multitape-turing-machine", "big-o-notation", "asymptotic-notation-beyond-big-o"],
  adds=[B("V", "bit volume", "the number of data bits stored in the array a tape procedure acts on", "count"),
        B("p", "working precision", "the number of fractional bits kept in each real or imaginary component of a complex coefficient", "count"),
        B("d", "number of axes", "the number of address chunks, or transform axes, of the array", "count"),
        B("r", "record length", "the number of complex coefficients in a polynomial record of $\\mathbb C[y]/(y^r+1)$", "count"),
        B("K", "chunk width", "the number of address bits in each chunk on which a simultaneous layer acts", "count"),
        B("T", "record count", "the number of records of the padded transform array, with $Tp$ of order $n$", "count"),
        B("\\ell", "log record length", "the base-2 logarithm of $r$", "direct"),
        B("\\tau", "interchange exponent", "the fixed exponent below 1 in the cost $O(Vu^\\tau)$ of swapping two $u$-bit chunks", "direct"),
        B("\\lambda'", "layer exponent", "the fixed exponent below 1 in the cost $O(Vd^{\\lambda'})$ of a simultaneous butterfly layer", "direct"),
        B("W", "wire count", "the number of wires, or roles, of the fixed linear network under consideration", "count"),
        B("m", "label dimension", "the dimension of the bilinear space whose subspaces label the network", "count"),
        B("s", "total edge rank", "the sum of the ranks of all edge changes of the network, equal to the number of smaller calls per run", "count")],
  salient="The saving is a power of the logarithm so small ($\\kappa=2^{-182}$) that it only matters that it is positive; it comes entirely from the strict inequality $s<Wm$ for the fixed networks.")

ans = {"root": ROOT}
json.dump(ans, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3B/exegenius/tasks/0003-argument.answer.json','w'), indent=1, ensure_ascii=False)

# verification of quotes
last = -1
def walk(n, path=()):
    global last
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        c = SRC.count(q)
        pos = SRC.find(q)
        ok = c >= 1
        if not ok: print("MISSING", n["id"], repr(q))
        elif c > 1: print("MULTI", n["id"], c, repr(q))
        if not n.get("deferred"):
            if pos < last: print("ORDER", n["id"], pos, last)
            last = max(last, pos)
    else:
        m = n["motivation"]
        if m.get("quote"):
            q = m["quote"]["quote"]
            if SRC.count(q) < 1: print("MOTMISSING", n["id"], repr(q))
        for ch in n["children"]: walk(ch)
walk(ROOT)
print("done")
