import json, re, sys
BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4B"
text = open(BASE + "/sources/paper.tex").read()

def ev(q):
    return {"source": "paper", "quote": q}

def infer(id, claim, q, page=None, frm=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(q), "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot, children, page=None, frm=None, salient=None, adds=None):
    src, mtext, mq = mot
    m = {"text": mtext, "source": src}
    if mq: m["quote"] = ev(mq)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def b(symbol, name, meaning, rel="direct"):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

# ---------------- S1 ----------------
s1 = show("S1",
 "A tape procedure interchanges two disjoint address chunks of $u$ bits, $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$, in time $O(Vu^{\\tau})$ for a fixed $\\tau<1$.",
 "build the interchange from three address shears, executing the middle shear through a fixed linear exchange network whose edge changes are smaller interchanges on role streams",
 ("explicit", "A rank-$a$ edge needs only $a$ smaller interchanges, and the total over the network is below the number of wires times $m$, so the recursion saves a power of the chunk width.",
  "Because the sum of these ranks is less than the number of wires times"),
 [
  infer("S1.1", "A fixed network of $W$ wires of linear gates exchanges two banks of values with a sign and restores every scratch wire, for arbitrary initial scratch values.",
        "For arbitrary initial values of its auxiliary wires, a forward",
        page="linear-network",
        frm=["linear-algebra-basics", "finite-field-f2-arithmetic", "vectors-matrices-and-invertibility"]),
  infer("S1.2", "If each wire carries an array and each vertex has an invertible frame, pointwise gates commute with frames, so only the endpoint operator and the change of frame on each edge need to be paid for.",
        "Thus the common frame commutes with the pointwise gate, and",
        page="common-frame-principle",
        frm=["linear-network", "vectors-matrices-and-invertibility", "permutations-and-cartesian-products"]),
  show("S1.3",
   "Labels from three-element subsets give nested nondegenerate subspaces of an $m$-dimensional space on the gates and terminals, so that the sum $s$ of the edge ranks is below $Wm$ and every route has endpoint difference the identity.",
   "attach subspaces built from indicator vectors of 3-element subsets, using their intersection pairings to cancel unwanted gather and scatter coefficients, and count the dimension changes along edges",
   ("explicit", "The scalar network already routes the exchange, so only the intermediate labels are free; they are chosen so that edge changes of frame are cheap.",
    "choose its intermediate labels to make the changes of frame inexpensive."),
   [
    infer("S1.3a", "Every edge of the labelled network joins comparable nondegenerate labels, and only the central-wire edges lose dimension, by $h$ each.",
          "Every edge joins comparable nondegenerate labels."),
    infer("S1.3b", "The total rank $s$ of all edge differences of the bit network is less than $Wm$, while each input role has endpoint matrix difference $I_m$.",
          "The sum of the rational ranks of all edge differences is"),
   ],
   page="subset-intersection-labels",
   frm=["linear-algebra-basics", "linear-network", "common-frame-principle", "finite-field-f2-arithmetic"],
   salient="The total rank change $s$ is strictly below $Wm$, although only by a minuscule relative margin, and this strictness is what later yields a power saving; it holds because only the central wires lose dimension and the loss ratio $L/N$ is below $1/2$."),
  show("S1.4",
   "The address map $(H,D)\\mapsto(H+AD,D)$ of rank $a$ costs only $a$ single-pair interchanges plus linear-time updates, and three shears interchange $H$ and $D$.",
   "factor the matrix as $E_1\\Pi E_2$ with lower-triangular $E_1,E_2$, so every triangular part is a linear-time controlled shift and only the $a$ pivots need an interchange",
   ("explicit", "Controlled shifts update a later field from earlier fields in linear time, and lower-triangular changes of coordinates only ever work in that direction.",
    "can be performed entirely in this direction."),
   [
    infer("S1.4a", "Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with $a$ ones.",
          "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"),
    infer("S1.4b", "For a fixed finite set of matrices there is an odd prime $q$ such that the shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ costs exactly $a$ field interchanges plus $O(V)$ work.",
          "Let $\\mathcal A$ be a fixed finite collection of rational $m\\times m$"),
    infer("S1.4c", "The three shears $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ interchange the chunks $H$ and $D$, and only the middle one uses the network.",
          "To interchange the two full chunks, perform"),
   ],
   page="address-shear",
   frm=["controlled-shift", "elementary-stream-ops", "linear-algebra-basics", "linear-network", "modular-arithmetic", "tape-address-model"]),
  show("S1.5",
   "Running the network with edge changes done by smaller calls on role streams of volume $V/W$ gives cost per volume $F_k\\le(s/W)F_{k-1}+O(1)$, hence $F_k=O(e^{\\tau})$ with $\\tau<1$ since $s/W<m^{\\tau}$.",
   "split the rows cyclically into $W$ role streams, spend $s$ recursive calls on streams one $W$-th as large, and sum the resulting geometric series",
   ("explicit", "Multiplying the parameter by $m$ raises the recursive contribution by $s/W$, which is strictly below $m$; this strict inequality is what turns the recursion into a power saving.",
    "is the source of the power saving."),
   [
    infer("S1.5a", "The number of smaller interchange calls equals the sum $s$ of the edge ranks, each acting on one role stream of volume $V/W$.",
          "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
    infer("S1.5b", "The cost per unit volume satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
          "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."),
    infer("S1.5c", "For $s/W<m^{\\tau}$ the geometric sum is $O(m^{k\\tau})$, so $F_k=O(e^{\\tau})$ when $e=m^k$.",
          "For $a=s/W<m^\\tau$ the geometric sum"),
   ],
   page="rank-saving-recurrence",
   frm=["linear-network", "common-frame-principle", "subset-intersection-labels", "address-shear", "recurrences-and-induction"],
   salient="Each level multiplies the work per volume by $s/W$, which sits strictly (but only slightly) below $m$; because the width grows by the factor $m$ per level while the cost grows by less, the total is a power $e^{\\tau}$ of the width with $\\tau<1$ instead of $e$."),
  infer("S1.6", "For arbitrary widths $u$ and arbitrary prefix, gap and suffix lengths, the interchange of two $u$-bit chunks costs $O(Vu^{\\tau})$ after padding rows and splitting the width in base $m$.",
        "There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape"),
 ],
 page="address-chunk-interchange",
 frm=["tape-address-model", "elementary-stream-ops", "controlled-shift", "permutations-and-cartesian-products", "sorting-and-data-movement-on-tapes", "finite-alphabet-encodings-and-constant-factor-simulation"],
 adds=[b("m", "label dimension", "number of fields in each of the two address-chunk vectors, equal to the dimension of the label space", "count"),
       b("W", "wire count", "number of wires, that is roles, of the exchange network", "count"),
       b("s", "total edge rank", "sum of the ranks of all edge changes, that is the number of smaller interchange calls", "count"),
       b("\\tau", "interchange exponent", "fixed exponent below one with $s/W<m^{\\tau}$")])

# ---------------- S2 ----------------
s2 = show("S2",
 "A tape procedure applies $H_0$ simultaneously at the same bit offset in $D\\le d$ address chunks of $K$ bits of a polynomial-record array, exactly and then with one truncation, in time $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
 "evaluate the layer exactly through the phase-frame network, implementing its binary changes of basis by packed chunk moves, and bound the cost by a recurrence in the number of axes",
 ("recoverable", "Separate butterflies would need $D$ whole-array passes; the network turns a layer on $e=mf$ axes into $s$ layers on $f$ axes, and the same rank deficit gives a power saving in the number of axes.", None),
 [
  show("S2.1",
   "A layer of the kernel $C$ on $e=mf$ axes needs $s$ layers on $f$ axes, and $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$.",
   "express each edge change of the complex network as a product of two-point kernels $C=aI+bX$ on directions of the residual, and convert $C$-layers back to normalized butterflies by diagonal phases",
   ("explicit", "Phase frames reduce a tensor product of $C$ on many selected bits to tensor products on fewer selected bits.",
    "frames express a $C$ tensor product using smaller groups of"),
   [
    infer("S2.1a", "An edge from label $U_-$ to $U_+$ changes the phase frame by a product of kernels $(aI+bX_{v_j})^{\\epsilon_j}$, one for each vector of an orthonormal basis of the residual.",
          "=\\prod_{j=1}^{\\rho_{\\rm edge}}(aI+bX_{v_j})^{\\epsilon_j},"),
    infer("S2.1b", "Applying the network to a group of $e=mf$ axes gives exactly $s$ child calls, each on $f=e/m$ axes, and $C^{\\otimes e}$ on every role.",
          "Summing its residual dimensions gives exactly"),
    infer("S2.1c", "The normalized layer is recovered from the $C$-layer by $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$.",
          "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."),
   ],
   page="phase-frame-kernel",
   frm=["linear-network", "common-frame-principle", "subset-intersection-labels", "butterfly", "complex-numbers", "finite-field-f2-arithmetic"]),
  show("S2.2",
   "Adding the selected bit of $f$ address chunks of one slot to those of another, $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ for $0\\le i<f$, costs $O(V(L^{\\tau}+1))$ and restores the third chunk's arbitrary contents.",
   "perform eight chunk-wide cyclic shifts that act correctly except at a small explicit set of exceptional addresses, then repair those addresses by sorting",
   ("recoverable", "A single shift of a whole chunk range acts on all $f$ selected positions at once, but carries could cross between neighbouring segments; the guard bits make that happen only on few addresses, which can be corrected cheaply.", None),
   [
    infer("S2.2a", "Eight shifts flip the parity of $u$ exactly when the control is one, restoring the auxiliary integer $w$; they agree with the ideal XORs outside an exceptional set.",
          "We first construct eight rotations that have the required effect away"),
    infer("S2.2b", "The exceptional set has at most $\\delta_{\\rm bad}M$ addresses, a fraction at most $80(f-1)2^{-K}$, independent of the payload.",
          "There are exactly twenty excluded values for each guard in"),
    infer("S2.2c", "The exceptional records are extracted, stably radix-sorted by destination rank and reinserted, which gives the ideal map everywhere.",
          "while stable binary radix sorting scans only the extracted records and"),
   ],
   page="packed-selected-bit-addition",
   frm=["address-chunk-interchange", "controlled-shift", "elementary-stream-ops", "finite-field-f2-arithmetic", "binary-representation-and-bit-operations", "sorting-and-data-movement-on-tapes"],
   salient="The third chunk may hold arbitrary data yet is returned unchanged: the eight shifts compose to a map that flips only the parity of one coordinate and leaves the other fixed."),
  infer("S2.3", "Rows are split cyclically among the $W$ roles, so every child call acts on a stream with exactly $1/W$ of the parent's volume, padded rows being zero again after each call.",
        "At a node, write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),"),
  infer("S2.4", "The time per volume on $e$ axes obeys $F(e)\\le(s/W)F(e/m)+O((eK)^{\\tau}+1)$, which unrolls to $O(d^{\\lambda'})$ for $d$ axes.",
        "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
  infer("S2.5", "Reserving $p+\\Delta$ fractional bits with $\\Delta=O(d^{C_1})=o(p)$ represents every intermediate dyadic coefficient of the layer exactly.",
        "Thus reserving \\(p+\\Delta\\)"),
  infer("S2.6", "The procedure returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time, with every coefficient in the unit disk and error less than $\\sqrt2\\,2^{-p}$.",
        "The procedure returns $Q_p(\\mathcal H z)$ in the same array,"),
 ],
 page="fast-butterfly-layer",
 frm=["fixed-point-truncation", "polynomial-ring-mod", "butterfly", "linear-network", "common-frame-principle", "subset-intersection-labels",
      "rank-saving-recurrence", "address-chunk-interchange", "packed-selected-bit-addition", "phase-frame-kernel", "controlled-shift"],
 adds=[b("d", "number of axes", "maximum number of address chunks, that is axes, on which a layer acts", "count"),
       b("K", "chunk width", "number of bits in each address chunk"),
       b("\\lambda'", "layer exponent", "fixed exponent below one in the layer cost $O(Vd^{\\lambda'})$")])

# ---------------- S3 ----------------
s3 = show("S3",
 "The normalized convolution of arrays over $\\mathbb C[y]/(y^r+1)$ on the axes of lengths $t_i$ is computed from two forward synthetic transforms, pointwise products, and the opposite transform, with error less than $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
 "transform with synthetic Fourier transforms whose roots of unity are signed shifts, keep the common stored frequency order through the pointwise product, and multiply polynomials by signed packing",
 ("explicit", "In $\\mathbb C[y]/(y^r+1)$ powers of $y$ are roots of unity and multiplying by one is just a signed shift of coefficients, so the transforms need only butterflies and shifts.",
  "serve as roots of unity in the remaining axes, and multiplication by"),
 [
  show("S3.1",
   "The synthetic transform $F_t^{\\pm}$ with $\\omega_t=y^{2r/t}$ is computed by radix-two butterfly rounds with twiddle monomials and leaves outputs in bit-reversed order.",
   "use decimation in frequency with twiddles that are monomials $y^E$ and track the stored frequency order",
   ("explicit", "The required roots of unity act as exact signed permutations of coefficient lists, which is why the transform is computable with exact shifts and butterflies.",
    "where the required roots of unity act by exact signed permutations"),
   [
    infer("S3.1a", "For a power of two $t$ dividing $2r$, the element $\\omega_t=y^{2r/t}$ serves as a primitive root of unity in $\\mathbb C[y]/(y^r+1)$.",
          "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$."),
    infer("S3.1b", "The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\\omega_t^{-k}$ and recurses.",
          "The length-one procedure is the identity."),
    infer("S3.1c", "After all rounds the entry $(F_t^-z)_j$ is stored at the bit-reversed slot, and the reverse procedure consumes that order and computes the opposite transform.",
          "Let $B_t$ denote this record permutation: it moves the entry at $j$"),
   ],
   page="synthetic-transform",
   frm=["polynomial-ring-mod", "dft", "multidimensional-dft", "butterfly", "roots-of-unity", "fast-fourier-transform-and-divide-and-conquer"]),
  infer("S3.2", "On a layout that places the selected bits of all participating axes at a common offset in consecutive $K$-bit chunks, a multidimensional synthetic transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error less than $\\sqrt2\\ell2^{-p}$.",
        "The procedure constructs an explicit positional"),
  show("S3.3",
   "Two polynomials of $\\mathbb C[y]/(y^r+1)$ on the $p$-bit disk grid are multiplied exactly, and $Q_p(fg/r)$ is returned, in time $O(rp\\log(rp))$.",
   "evaluate the coefficients at $2^{4p}$ to turn the polynomial product into integer products, multiply with the established multiplier, and read the coefficients back by centered residues and carries",
   ("recoverable", "A product of polynomials with small coefficients is an integer product in disguise once each coefficient has a wide enough field, and an established $O(N\\log N)$ multiplier then handles it.", None),
   [
    infer("S3.3a", "Setting $B_0=2^{4p}$ and evaluating each integer polynomial at $B_0$ gives signed integers that fit in $4pr$ bits.",
          "Set $B_0=2^{4p}$"),
    infer("S3.3b", "The four evaluation products are formed by the established multiplier on absolute values with signs restored.",
          "pairs of absolute values using the established multiplier and restore"),
    infer("S3.3c", "Each product coefficient is the centered residue of its block modulo $B_0$ plus a carry in $\\{0,1\\}$, because every coefficient is below $B_0/2$.",
          "At block $j$, let $\\widehat h_j$ be the unique"),
   ],
   page="signed-packing",
   frm=["established-multiplier", "polynomial-ring-mod", "fixed-point-truncation", "binary-representation-and-bit-operations"]),
  infer("S3.4a", "Both forward transforms are performed keeping the common retained order, multiplied pointwise by the packed product, and the opposite transform consumes that order.",
        "Perform both forward transforms and retain their common $LB$ order."),
  infer("S3.4b", "The errors of the three transforms and the product add to less than $\\sqrt2\\,M(3\\ell+1)2^{-p}$ after the exact scaling by $M$.",
        "For the error estimate, put"),
 ],
 page="ring-convolution",
 frm=["polynomial-ring-mod", "synthetic-transform", "signed-packing", "fast-butterfly-layer", "address-chunk-interchange",
      "cyclic-convolution", "multidimensional-dft", "dft", "fixed-point-truncation", "established-multiplier"],
 adds=[b("r", "ring size", "power of two giving the number of coefficients of each polynomial record", "count"),
       b("M", "record count", "number of polynomial records, the product of the axis lengths other than the ring axis", "count")])

# ---------------- S4 ----------------
s4 = show("S4",
 "A Fourier transform on distinct prime lengths $s_i$ is expressed through power-of-two transforms of lengths $t_i>s_i$ by $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with the permutations $R,Q$ left inside the identity.",
 "apply Gaussian resampling line by line along each axis, and keep the source and target coordinate permutations in the formula instead of sorting",
 ("explicit", "The prime lengths required for the integer product do not match the power-of-two lengths of the synthetic transforms, and resampling connects the two shapes.",
  "whereas the synthetic transforms use powers of two. Gaussian resampling"),
 [
  infer("S4a", "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
        "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and"),
  infer("S4b", "Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, and the axes are exposed by chunk interchanges.",
        "Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
 ],
 page="gaussian-resampling",
 frm=["dft", "multidimensional-dft", "fixed-point-truncation", "established-multiplier", "norms-absolute-values-and-error-bounds", "primes-coprimality-and-gcd", "address-chunk-interchange"],
 adds=[b("\\alpha", "resampling width", "integer parameter controlling the width of the Gaussian window and the separation condition $t/s-1>p/\\alpha^4$")])

# ---------------- S5, S6 ----------------
s5 = infer("S5", "The middle factor $QF_{\\boldsymbol t}$, with its target permutation, equals a chirp-weighted normalized cyclic convolution $\\overline a\\cdot\\bigl(a*(\\overline a\\cdot u)\\bigr)/T$.",
  "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because",
  page="bluestein-chirp",
  frm=["dft", "cyclic-convolution", "multidimensional-dft", "roots-of-unity"])
s6 = infer("S6", "The source permutation $R$ cancels across the two forward transforms, the pointwise product and the opposite transform: $RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
  "$RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$",
  page="permutation-cancellation",
  frm=["dft", "multidimensional-dft", "cyclic-convolution", "gaussian-resampling", "permutations-and-cartesian-products"],
  salient="Neither coordinate permutation is ever executed: the unit dilation $R$ commutes through the opposite transform ($RF^+R=F^+$) and pointwise products, so the retained permutations disappear exactly and only the normalization $1/S^2$ remains.")

# ---------------- S7 ----------------
s7 = show("S7",
 "The pipeline forms radix digits, places them on prime axes by the Chinese-remainder map $\\Phi$, applies two source transforms, multiplies pointwise, applies the opposite transform, rescales, rounds and propagates carries, giving the exact $2n$-bit product.",
 "reduce integer multiplication to a cyclic convolution of digit lists, evaluate that convolution with Fourier transforms through resampling, chirps and the ring convolution, and recover the exact integer coefficients",
 ("recoverable", "Integer multiplication is a convolution of digits; a convolution is a pointwise product of transforms, and the transforms are made fast and exact by the earlier steps.", None),
 [
  show("S7.1",
   "The parameters are $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, $K=\\lfloor d^{c}\\rfloor$, a power of two $T\\in[4n/b,8n/b)$, axis lengths $t_i\\in\\{r/2,r\\}$ and distinct odd primes $s_i$ with $T/2<S<T$, so that all hypotheses of the lemmas hold.",
   "fix explicit rational exponents and size parameters, then choose primes just below the powers of two and verify the hypotheses of each lemma",
   ("explicit", "The primes must be close to the powers of two so that their product fills a fixed fraction of the box while each ratio leaves enough room for resampling.",
    "The distinct prime lengths $s_i$ must be close to the powers of two"),
   [
    infer("S7.1a", "The exponents are fixed rationals, with $\\epsilon=2^{-75}$, $C_1=20$ and $\\kappa=2^{-182}$.",
          "C_1=20,\\qquad \\epsilon=2^{-75},\\qquad \\kappa=2^{-182}."),
    infer("S7.1b", "The sizes are $b=\\lceil\\log_2n\\rceil$, $p=6b$ and $d=\\lfloor b^{\\epsilon}\\rfloor$, giving $Tp=\\Theta(n)$.",
          "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
    infer("S7.1c", "Distinct odd primes $s_i$ lie in $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$.",
          "(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i."),
    infer("S7.1d", "The product $S=\\prod_i s_i$ satisfies $T/2<S<T$.",
          "Together with $s_i<t_i$, this gives $T/2<S<T$."),
   ],
   page="parameter-choice",
   frm=["primes-coprimality-and-gcd", "floor-ceiling-and-summation-notation", "logarithms-and-iterated-logarithm-notation", "gaussian-resampling", "fast-butterfly-layer", "ring-convolution"],
   salient="Every prime $s_i$ is strictly below its power of two $t_i$, yet the product $S$ stays within a factor two of the full box size $T$, uniformly in the number of axes."),
  infer("S7.2", "Writing the inputs as polynomials in $2^b$, their product has coefficients below $2^{3b}$ and, with padding to $S>2q-2$, the cyclic convolution has no wraparound.",
        "Write the two inputs as polynomials in $2^b$, each with",
        page="radix-digit-convolution",
        frm=["cyclic-convolution", "polynomials", "binary-representation-and-bit-operations"]),
  infer("S7.3", "The Agarwal-Cooley map $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$ is an isomorphism preserving cyclic convolution, implemented by triangular controlled shifts and axis moves.",
        "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
        page="crt-address-map",
        frm=["cyclic-convolution", "chinese-remainder-theorem", "controlled-shift", "address-chunk-interchange", "ring-and-group-notions-for-polynomials"]),
  show("S7.4",
   "The last cyclic coordinate is turned into $\\mathbb C[y]/(y^r+1)$ by the twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$, and untwisting recovers the cyclic wrap.",
   "multiply coefficient $k$ by $\\zeta^k$, which is a diagonal isomorphism, and check that the negative wrap becomes the cyclic wrap",
   ("explicit", "The complex cyclic convolution needed for the chirp is obtained from the synthetic ring convolution by this twist.",
    "The power-of-two complex convolution used in the chirp identity is"),
   [
    infer("S7.4a", "The map $x_d\\mapsto\\zeta y$ is well defined, and is a diagonal isomorphism multiplying coefficient $k$ by $\\zeta^k$.",
          "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."),
    infer("S7.4b", "A product term that wraps once picks up $\\zeta^{k+l}(-1)^h=\\zeta^j$, so untwisting yields the cyclic coefficient with the correct sign.",
          "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j."),
   ],
   page="phase-twist",
   frm=["polynomial-ring-mod", "cyclic-convolution", "roots-of-unity", "complex-numbers"]),
  infer("S7.5", "The chirp transform is computed as $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0))$ with $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$.",
        "Thus $\\widetilde a$ is the convolution kernel and $x_0$ is the data"),
  infer("S7.6", "The source transform applies the linewise resampling map $\\mathcal A$, the chirp transform, the linewise map $\\mathcal B_0$ and the exact scale $2^{\\gamma}$, and approximates $RF_{\\boldsymbol s}$.",
        "For a source disk-grid tensor of norm at most $.5$, write"),
  infer("S7.7", "The algorithm applies $\\Phi$, two source transforms, an exact pointwise product, the opposite transform, the exact scales $S$ and $2^{2b+4}S$, rounding, $\\Phi^{-1}$ and carry propagation.",
        "With these streams prepared, perform the following operations."),
  show("S7.8",
   "The accumulated coefficient error is below $1/2$, so rounding recovers the exact integer coefficients, and radix-$2^b$ carries give the $2n$-bit product.",
   "bound every approximation error and disk margin, show that the final scaled error is below one half, then propagate carries",
   ("recoverable", "The true coefficients are integers, so any approximation within one half determines them; the large scale factors are known exactly and the precision $p=6b$ is chosen to absorb them.", None),
   [
    infer("S7.8a", "All intermediate arrays stay in the disk with explicit sup-norm error bounds, and the margins are enforced by one fixed cutoff.",
          "Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this"),
    infer("S7.8b", "The final absolute error after rescaling by $2^{2b+4}S$ is less than $448b\\,2^{-3b/4}<1/2$.",
          "2^{2b+4}S\\cdot28\\,2^\\gamma T^2L\\cdot2^{-6b}"),
    infer("S7.8c", "Radix-$2^b$ carries propagate with carries below $Q_0^2$, which fixes the digits of the full product.",
          "To propagate carries, let $Q_0=2^b$."),
   ],
   page="exact-recovery",
   frm=["fixed-point-truncation", "norms-absolute-values-and-error-bounds", "radix-digit-convolution", "recurrences-and-induction"]),
 ],
 page="multiplication-algorithm",
 frm=["bluestein-chirp", "gaussian-resampling", "permutation-cancellation", "ring-convolution", "crt-address-map", "phase-twist",
      "radix-digit-convolution", "parameter-choice", "exact-recovery", "address-chunk-interchange", "fast-butterfly-layer"],
 adds=[b("b", "digit width", "number of bits per radix digit, $\\lceil\\log_2 n\\rceil$"),
       b("p", "precision", "number of fractional bits of the fixed-point grid, equal to $6b$"),
       b("T", "padded box size", "power of two with $T=\\Theta(n/b)$, the product of the power-of-two axis lengths", "count"),
       b("S", "prime product", "product of the distinct prime source lengths, with $T/2<S<T$")])

# ---------------- S8 ----------------
s8 = show("S8",
 "Dividing every cost by $V=Tp=\\Theta(n)$ gives seven dominant powers of $p$, each at most $1-2\\kappa$, so the total is $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
 "tabulate the normalized cost of every operation, bound each power of $p$ by explicit margins below one, and absorb setup and exceptional streams",
 ("explicit", "The smallest margin below one is explicit, and it is large enough to absorb any leftover fixed power of the logarithm.",
  "This explicit slack will cover"),
 [
  infer("S8a", "The cost table divides each operation's cost by $V=Tp=\\Theta(n)$, which is the volume of a full padded array.",
        "For the cost calculation put $V=Tp=\\Theta(n)$."),
  infer("S8b", "The seven margins below one are at least $2^{-181}=2\\kappa$, the smallest being the chunk-exchange term.",
        "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
  infer("S8c", "The simultaneous butterfly rounds cost $O(Vd^{\\lambda'})$ each, at most $\\ell$ rounds, normalized $\\ell d^{\\lambda'}$.",
        "For the at most $\\ell$ simultaneous rounds,"),
  infer("S8d", "Gaussian line maps cost $O(dTp^{3/2+\\delta}\\alpha)$ in total over the at most $T/t_i$ lines per axis.",
        "For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines."),
  infer("S8e", "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^{\\kappa}$ eventually.",
        "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
  infer("S8f", "The resulting fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
        "$O(n(\\lg n)^{1-\\kappa})$ for every input length and produces precisely"),
 ],
 page="time-accounting",
 frm=["parameter-choice", "address-chunk-interchange", "fast-butterfly-layer", "ring-convolution", "gaussian-resampling", "crt-address-map", "multiplication-algorithm", "big-omega-theta-and-little-o-notation"],
 salient="Seven structurally different costs (layout moves, chunk exchanges, butterfly rounds, CRT layout, Gaussian maps, chirps, packed products) all land at or below the same exponent $1-2\\kappa$, and the smallest margin, $2^{-181}$, from the chunk exchanges is what fixes $\\kappa=2^{-182}$.",
 adds=[b("V", "stored volume", "number of stored data bits of a full padded array, $Tp=\\Theta(n)$", "count")])

root = show("S0",
 "A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "build two faster tape procedures, address-chunk interchange and simultaneous butterfly layers, put them inside a reduction of integer multiplication to cyclic convolution through resampling and synthetic ring transforms, and account the cost",
 ("explicit", "Scanning the array at each of the $\\Theta(\\log n)$ transform levels already costs $n\\log n$, so both the data movement and the arithmetic must be sped up.",
  "We therefore need savings in both movement and arithmetic."),
 [s1, s2, s3, s4, s5, s6, s7, s8],
 page="main-theorem",
 frm=["integer-multiplication-conjecture", "multitape-tm", "big-o", "logarithms-and-iterated-logarithm-notation"],
 salient="The saving is a power $(\\lg n)^{-\\kappa}$ with the astronomically small $\\kappa=2^{-182}$, yet it is strict: it exists only because every recursion in the two tape procedures loses a tiny fraction of its rank, $s<Wm$.")

answer = {"root": root}

# ---------- checks ----------
pages_order = """integer-multiplication-conjecture polynomial-ring-mod fixed-point-truncation established-multiplier tape-address-model elementary-stream-ops controlled-shift linear-algebra-basics linear-network address-shear common-frame-principle subset-intersection-labels rank-saving-recurrence address-chunk-interchange packed-selected-bit-addition signed-packing cyclic-convolution radix-digit-convolution phase-twist exact-recovery dft multidimensional-dft butterfly synthetic-transform bluestein-chirp phase-frame-kernel fast-butterfly-layer ring-convolution gaussian-resampling permutation-cancellation crt-address-map parameter-choice multiplication-algorithm time-accounting main-theorem""".split()
pos = {p: i for i, p in enumerate(pages_order)}
known = """big-o polynomials complex-numbers multitape-tm logarithms-and-iterated-logarithm-notation big-omega-theta-and-little-o-notation binary-representation-and-bit-operations modular-arithmetic primes-coprimality-and-gcd chinese-remainder-theorem roots-of-unity vectors-matrices-and-invertibility finite-field-f2-arithmetic permutations-and-cartesian-products floor-ceiling-and-summation-notation recurrences-and-induction norms-absolute-values-and-error-bounds fast-fourier-transform-and-divide-and-conquer sorting-and-data-movement-on-tapes finite-alphabet-encodings-and-constant-factor-simulation ring-and-group-notions-for-polynomials""".split()
errors = []
used_pages = []
used_from = set()
ids = set()
last = [-1]
def walk(n, curpage, ancestors_adds):
    if n["id"] in ids: errors.append("dup id " + n["id"])
    ids.add(n["id"])
    pg = n.get("page") or curpage
    if n.get("page"):
        used_pages.append(n["page"])
    for f in n.get("from", []):
        used_from.add(f)
        if f in pos:
            if pos[f] >= pos[pg]: errors.append(f"{n['id']}: from {f} not before page {pg}")
        elif f not in known:
            errors.append(f"{n['id']}: unknown from {f}")
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        i = text.find(q)
        if i < 0:
            errors.append(f"{n['id']}: quote not found: {q}")
        else:
            if text.count(q) > 1:
                # use first occurrence at/after last
                j = text.find(q, last[0] + 1)
                i = j if j >= 0 else i
            if i < last[0]:
                errors.append(f"{n['id']}: out of order ({i} < {last[0]}) {q}")
            last[0] = max(last[0], i)
    else:
        mq = n["motivation"].get("quote")
        if n["motivation"]["source"] == "explicit":
            if not mq or mq["quote"] not in text:
                errors.append(f"{n['id']}: motivation quote missing/not found")
        for c in n["children"]:
            walk(c, pg, None)
    # adds check
def descendants_claims(n):
    out = []
    for c in n.get("children", []):
        out.append(c["claim"]); out += descendants_claims(c)
    return out
def check_adds(n):
    for a in n.get("adds", []):
        found = False
        for cl in descendants_claims(n):
            for mth in re.findall(r"\$(.+?)\$", cl):
                if a["symbol"] in mth: found = True
        if not found: errors.append(f"{n['id']}: add {a['symbol']} not used")
    for c in n.get("children", []): check_adds(c)
walk(root, None, None)
check_adds(root)
dups = [p for p in set(used_pages) if used_pages.count(p) > 1]
if dups: errors.append(f"dup pages {dups}")
step_pages = set(used_pages)
for p in pages_order:
    if p not in step_pages and p not in used_from:
        errors.append(f"page {p} neither step nor in any from")
if errors:
    print("\n".join(errors)); sys.exit(1)
json.dump(answer, open(BASE + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
print("ok; wrote answer")
