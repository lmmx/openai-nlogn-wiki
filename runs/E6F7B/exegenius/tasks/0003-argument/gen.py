import json, sys

def inf(id, claim, quote, page=None, frm=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim,
         "quote": {"source": "paper", "quote": quote}, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": mot, "children": children, "from": frm or []}
    if page: n["page"] = page
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def expl(text, quote):
    return {"text": text, "source": "explicit", "quote": {"source": "paper", "quote": quote}}
def recov(text):
    return {"text": text, "source": "recoverable", "quote": None}
def recon(text):
    return {"text": text, "source": "reconstructed", "quote": None}

def add(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

# ---- S1.3 networks
s13 = show("S1.3",
  "Fixed linear networks that exchange two banks of values and restore all scratch values, with a change of representation (frame) along each edge, have total edge rank $s<Wm$ and therefore give a recursion with exponent $\\tau<1$.",
  "Build a three-stage bank-exchange network, run it on arrays by choosing a frame at every vertex, label the vertices by nested subspaces of an $m$-dimensional space so that edge changes are small residuals, count the total edge rank, and feed the count into the recurrence.",
  expl("The whole construction is aimed at one inequality: the number of smaller calls must be below the number of wire-dimension slots, because that strict gap is what yields a power saving.",
       "number $s$ of smaller calls satisfies $s<Wm$."),
  [
   inf("S1.3.1", "A fixed network of pointwise linear gates exchanges two banks, sending $(X,Y)$ to $(-Y,X)$, and returns every scratch wire to its arbitrary initial value.",
       "For arbitrary initial values of its auxiliary wires, a forward",
       page="xor-linear-network", frm=["modular-arithmetic", "sets-functions-cartesian-products-and-bijections"],
       salient="The scratch wires start with arbitrary contents yet are restored exactly: the first two schedule rows subtract the old scratch effect, as in transparent computation, so no clean workspace is needed."),
   inf("S1.3.2", "If a common invertible frame is assigned at every source, gate and sink and every edge applies the change of frame, the network implements $D_{\\mathrm{out}}\\mathsf S D_{\\mathrm{in}}^{-1}$ on arrays, so the endpoint frames alone fix the operator on every role.",
       "Thus the common frame commutes with the pointwise gate",
       page="frames", frm=["matrices-and-linear-maps", "permutations", "xor-linear-network"]),
   inf("S1.3.3", "Nested nondegenerate subspace labels built from three-element subsets of $[100]$ make every edge change a small orthogonal residual, with total dimension loss $L$ on decreasing edges.",
       "Every edge joins comparable nondegenerate labels.",
       page="subset-labels", frm=["linear-algebra-prelims", "xor-linear-network"]),
   inf("S1.3.4", "The total edge rank satisfies $s<Wm$ because the loss $L$ on decreasing edges is below $N/2$.",
       "In particular, both are smaller than $1/2$.",
       page="rank-deficit", frm=["subset-labels", "frames", "linear-algebra-prelims"],
       salient="The deficit $Wm-s$ is a minuscule fraction of $Wm$ yet strictly positive, and that strictness alone is what the later power saving rests on; it comes from the loss $L$ being under half of $N$."),
   inf("S1.3.5", "The bit network sends its input to a permutation of itself, has matrix differences $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ on every role, and has total edge rank $s_{\\rm b}<W_{\\rm b}m$.",
       "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",
       page="bit-shear-interface", frm=["frames", "subset-labels", "rank-deficit", "xor-linear-network", "linear-algebra-prelims"],
       salient="The same shear $H\\leftarrow H+D$ is obtained on every role, including the scratch roles whose initial values were arbitrary."),
   inf("S1.3.6", "The complex phase network over Gaussian dyadic values gives the tensor power $C^{\\otimes m}$ of the two-point kernel $C=aI+bX$ on every role, each edge being a product of two-point kernels, with total count $s_{\\rm c}<W_{\\rm c}m$.",
       "For each edge of the complex network, write $U,V$ for its tail and",
       page="phase-frame-network", frm=["frames", "subset-labels", "rank-deficit", "xor-linear-network", "linear-algebra-prelims", "butterfly", "complex-numbers"],
       salient="Every role, scratch roles included, receives the same operator $C^{\\otimes m}$, although each edge only applies a few kernel factors."),
   inf("S1.3.7", "Because $s/W<m^\\tau$ for a rational $\\tau<1$, the recurrence $F_k\\le (s/W)F_{k-1}+O(1)$ for the volume-normalized cost gives $F_k=O(e^\\tau)$ at parameter $e=m^k$.",
       "For both recurrences we may use the fixed rational exponent",
       page="power-saving-recurrence", frm=["rank-deficit", "recursion-and-divide-and-conquer-recurrences", "summation-geometric-series-and-products", "logarithms-exponentials-floor-and-ceiling"],
       salient="Each call spawns $s$ calls, yet the exponent is strictly below one: each child sees only $1/W$ of the volume, so the growth factor per level is $s/W<m$ rather than $m$."),
  ],
  adds=[
    add("W", "wire count", "The number of wires in the fixed network, scratch wires included.", "count"),
    add("m", "label dimension", "The dimension of the fixed space whose subspaces label the vertices; a call at parameter $mf$ makes calls at parameter $f$.", "count"),
    add("s", "child calls", "The sum of the ranks of all edge differences, which is the number of smaller calls one network use makes.", "count"),
  ])

# ---- S1.4 address interchange
s141 = show("S1.4.1",
  "For a rational matrix $A$ of rank $a$, the shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ takes exactly $a$ interchanges of $b$-digit fields and $O(V)$ other work.",
  "Factor $A=E_1\\Pi E_2$ with lower-triangular $E_1,E_2$ and a partial permutation $\\Pi$, perform the triangular parts as controlled shifts, and turn each one of $\\Pi$ into one interchange.",
  expl("Controlled shifts only update a later field from earlier ones, so the changes of coordinates must be triangular in tape order; the factorization isolates the rank in $\\Pi$.",
       "can be performed entirely in this direction."),
  [
   inf("S1.4.1.1", "Every rational matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
       "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
       page="lower-triangular-factorization", frm=["matrices-and-linear-maps", "permutations", "rational-numbers-and-rounding"]),
   inf("S1.4.1.2", "A lower-triangular change of the fields $H$ or $D$ costs $O(V)$, being a sequence of controlled shifts and unit multiplications.",
       "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:",
       frm=["controlled-shifts", "modular-arithmetic"]),
   inf("S1.4.1.3", "Each one of $\\Pi$ at position $(i,j)$ gives $H_i\\leftarrow H_i+D_j$ by two controlled shifts around one interchange of $H_i$ and $D_j$.",
       "The first and last updates target a later field controlled by an earlier",
       frm=["controlled-shifts", "stream-operations"]),
  ], page="matrix-shear-cost",
  frm=["controlled-shifts", "stream-operations", "lower-triangular-factorization", "modular-arithmetic", "primes-coprimality-and-gcd", "matrices-and-linear-maps"])

s142 = show("S1.4.2",
  "For $e=m^k$, two disjoint address chunks of $e$ digits, with enough preceding rows, are interchanged in time $O(Ve^\\tau)$.",
  "Write each chunk as $m$ fields, run the bit network on the role streams so that every edge is a shear done by smaller interchanges (Lemma on matrix shears), complete the swap with two cheap shears, and solve the recurrence.",
  expl("Because the sum of the edge ranks is below the number of wires times $m$, the resulting recurrence saves a power of the chunk width.",
       "An edge matrix of rank $a$ will require $a$ smaller interchanges."),
  [
   inf("S1.4.2.1", "Rows are split cyclically into $W$ role streams of volume $V/W$ each, the network gates act pointwise on matching addresses, and every edge applies the shear permutation $\\Phi_{A_e}$ done by smaller interchanges.",
       "Split whole rows cyclically into $W$ role streams within each prefix",
       frm=["stream-operations", "bit-shear-interface", "frames", "matrix-shear-cost"]),
   inf("S1.4.2.2", "By the frame identity and the endpoint condition $M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$, the network applies $H\\leftarrow H+D$ on every original row.",
       "is $H\\leftarrow H+D$ on every original row, including rows assigned",
       frm=["frames", "bit-shear-interface"]),
   inf("S1.4.2.3", "The three updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ interchange $H$ and $D$, and only the middle shear uses the network.",
       "To interchange the two full chunks, perform",
       frm=["controlled-shifts"]),
   inf("S1.4.2.4", "The number of recursive calls is exactly $s$, each on volume $V/W$, so the normalized cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$ and $F_k=O(e^\\tau)$.",
       "Hence $F_k=O(e^\\tau)$.",
       frm=["power-saving-recurrence", "recursion-and-divide-and-conquer-recurrences"]),
   inf("S1.4.2.5", "A depth-first schedule on a fixed number of tapes, parking inactive role streams on a stack, realizes the recursion with only $O(V)$ extra work at each node.",
       "Reserve $W$ role tapes, a fixed set of",
       frm=["fixed-tape-model", "tapes-scanning-and-sorting-as-basic-machine-procedures"]),
  ], page="power-width-interchange",
  frm=["matrix-shear-cost", "bit-shear-interface", "power-saving-recurrence", "frames", "stream-operations", "controlled-shifts", "fixed-tape-model"],
  adds=[add("e", "chunk width", "The number of radix digits in each of the two interchanged address chunks, a power $m^k$ of $m$.", "count")])

s14 = show("S1.4",
  "Two disjoint contiguous address fields of $u$ bits, of any width and with any gaps, are interchanged in $O(Vu^\\tau)$ steps for a fixed $\\tau=1-2^{-50}<1$.",
  "Handle widths that are powers of $m$ with enough rows by the recursive network, then reach arbitrary widths by peeling off high digits to supply rows, padding the row count, splitting the width in base $m$ and padding the field ranges to a radix.",
  expl("The recursion needs a row count divisible by a power of $W$ and a width that is a power of $m$; both can be arranged cheaply.",
       "Rows for a general array can be supplied by a few of its own high digits."),
  [
   s141, s142,
   inf("S1.4.3", "Peeling off the top $\\rho$ digits of each chunk, interchanging them and joining them in front gives a row field of range at least $W^k$ before both remaining chunks.",
       "Write each chunk as its top $\\rho$ digits followed by its remaining",
       frm=["stream-operations"]),
   inf("S1.4.4", "Padding the row count to a multiple of $W^k$ with zero rows and splitting the remaining width in base $m$ into pieces of width $m^j$ gives total cost $O(Ve^\\tau)$ by a geometric sum.",
       "Append zero rows, separately within",
       frm=["power-width-interchange", "summation-geometric-series-and-products", "binary-representation-and-bitwise-operations"]),
   inf("S1.4.5", "Padding binary ranges $[2^u]$ to radix-$q$ ranges $[q^e]$ costs only a fixed factor and, since $e=O(u)$, gives the bound $O(Vu^\\tau)$.",
       "Finally, for binary chunks let $e$ be the least integer with",
       frm=["binary-representation-and-bitwise-operations", "logarithms-exponentials-floor-and-ceiling"]),
  ], page="arbitrary-width-interchange",
  frm=["power-width-interchange", "matrix-shear-cost", "stream-operations", "controlled-shifts", "permutations"],
  salient="The final effect is an exact permutation of the data, although the intermediate steps form XOR combinations of data streams; this is why the cost can fall below a general sort of addresses.")

# ---- S1.5 butterfly
s15 = show("S1.5",
  "The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied at once to the same bit position of $D\\le d$ address chunks of every polynomial record, with one final truncation, in $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$.",
  "Write $H_0^{\\otimes D}$ as phase factors around the tensor power $C^{\\otimes D}$ of the two-point kernel, evaluate $C^{\\otimes D}$ by the complex phase network with smaller layers as children, implement the binary changes of basis by packed selected-bit additions, bound the intermediate dyadic widths, and solve the recurrence.",
  expl("Applying the $D$ butterfly factors separately would cost $D$ passes over the whole array, so the factors must be done together.",
       "factors would require $D$ whole-array passes."),
  [
   inf("S1.5.1", "The recursive network on $e=mf$ selected axes makes exactly $s$ child calls on streams of volume $V/W$ and yields $C^{\\otimes e}$ on every role.",
       "Apply the finite network with these column frames to a group of",
       frm=["phase-frame-network", "power-saving-recurrence"]),
   inf("S1.5.2", "The normalized butterfly layer is $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$ with $\\mathcal S_D$ a diagonal phase operator, so a $C$ layer gives an $H_0$ layer by exact Gaussian dyadic operations.",
       "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D",
       frm=["butterfly", "phase-frame-network", "complex-numbers"]),
   inf("S1.5.3", "A binary row addition on selected bits of two address chunks is done by a constant number of whole-chunk cyclic shifts, using a third chunk of arbitrary contents as temporary storage, plus a repair of an explicitly bounded set of exceptional addresses.",
       "At the selected positions $j_i=\\rho+iK$",
       page="packed-selected-bit-addition", frm=["stream-operations", "controlled-shifts", "arbitrary-width-interchange", "binary-representation-and-bitwise-operations"]),
   inf("S1.5.4", "Splitting the cost into overhead $O((eK)^\\tau+1)$ per node and the factor $s/W$ gives $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which unrolls to $O(d^{\\lambda'})$ after base-$m$ partition of the $D$ chunks.",
       "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),",
       frm=["power-saving-recurrence", "arbitrary-width-interchange", "packed-selected-bit-addition", "summation-geometric-series-and-products"]),
   inf("S1.5.5", "The accelerated network is evaluated exactly until the whole layer is complete, and explicit guard widths bound denominator and magnitude growth of all intermediate Gaussian dyadics by $o(p)$ bits.",
       "The accelerated network is evaluated exactly until an entire",
       frm=["fixed-point-disk", "complex-numbers"]),
   inf("S1.5.6", "The row construction and recurrence give total time $O(Vd^{\\lambda'})$ on fixed tapes, and one final truncation yields a disk array with error below $\\sqrt2\\,2^{-p}$.",
       "The row construction and the recurrence analysis",
       frm=["fixed-point-disk", "packed-selected-bit-addition"]),
  ], page="simultaneous-butterfly-layer",
  frm=["phase-frame-network", "packed-selected-bit-addition", "power-saving-recurrence", "arbitrary-width-interchange", "butterfly", "fixed-point-disk", "negacyclic-ring", "complex-numbers"],
  adds=[add("D", "layer width", "The number of address chunks, at most $d$, whose selected bits are butterflied together.", "count")],
  salient="The cost is a fixed power $d^{\\lambda'}$ with $\\lambda'<1$ of the number of chunks, rather than the factor $D$ of separate passes, and the exponent mirrors the strict gap $s<Wm$ of the complex network.")

s1 = show("S1",
  "Two tape procedures cost $O(Vu^\\tau)$ for interchanging two address fields of $u$ bits and $O(Vd^{\\lambda'})$ for a butterfly layer on at most $d$ chunks, where $V$ is the stored bit volume, $\\tau<1$ and $\\lambda'<1$.",
  "Derive both procedures from the same device: a fixed linear network whose edge changes are cheaper smaller calls of the same procedure, on top of elementary linear-time stream operations.",
  recov("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $n\\log n$, so address movement and butterfly arithmetic must each be done at less than a full scan per level."),
  [
   inf("S1.1", "Digit moves, digit swaps, pointwise maps on split streams and cyclic splitting of rows into $W$ streams take $O(V)$ steps on a fixed number of tapes.",
       "Each of the following operations on an array of",
       page="stream-operations", frm=["fixed-tape-model", "turing-machine", "tapes-scanning-and-sorting-as-basic-machine-procedures", "binary-representation-and-bitwise-operations"]),
   inf("S1.2", "Cyclically shifting a target field by an offset computed from control fields that precede it, or multiplying it by a fixed unit, costs $O(V)$.",
       "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
       page="controlled-shifts", frm=["stream-operations", "modular-arithmetic", "primes-coprimality-and-gcd"]),
   s13, s14, s15,
  ],
  adds=[
    add("V", "stored volume", "The number of stored data bits of the array a procedure acts on.", "count"),
    add("\\tau", "interchange exponent", "A fixed exponent below one such that interchanging two $u$-bit address fields costs $O(Vu^{\\tau})$."),
    add("\\lambda'", "layer exponent", "A fixed exponent below one such that a butterfly layer on at most $d$ chunks costs $O(Vd^{\\lambda'})$."),
    add("u", "field width", "The number of bits in each of the two interchanged address fields.", "count"),
  ])

# ---- S2 synthetic convolution
s2 = show("S2",
  "On arrays over $\\mathbb C[y]/(y^r+1)$ with $M$ records, the normalized convolution $(f*g)/T$ is computed with error below $\\sqrt2 M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "Compute two forward synthetic transforms on a layout where every round is one simultaneous butterfly layer, multiply pointwise in the retained frequency order with signed-packed ring products, apply the opposite transform that consumes that order, and rescale by $M$.",
  expl("The opposite transform needs the frequencies in the same order the forward transforms leave them, so the order is kept rather than sorted.",
       "is stored, because the opposite transform consumes that same order"),
  [
   inf("S2.1", "The transform $F_t^\\pm$ over $\\mathbb C[y]/(y^r+1)$ with roots $\\omega_t=y^{2r/t}$ is a contraction and satisfies character cancellation $F_t^+F_t^-=t^{-1}I$ despite zero divisors.",
       "The ring has zero divisors, so we verify character cancellation",
       page="synthetic-transform", frm=["negacyclic-ring", "dft", "roots-of-unity", "triangle-inequality-and-norms", "fixed-point-disk"],
       salient="The ring has zero divisors, yet the sum of powers of the root is $0$ whenever $t\\nmid j$: shifting the summation index multiplies the sum by $y^{rj_0}=-1$, and the ring has no two-torsion."),
   inf("S2.2", "Decimation-in-frequency rounds leave the frequency $j$ in slot $\\mathrm{rev}(j)$, and the reverse procedure consumes this bit-reversed order, so no sort is executed.",
       "Let $B_t$ denote this record permutation",
       page="retained-frequency-order", frm=["synthetic-transform", "butterfly", "permutations"],
       salient="The bit-reversal permutation $B_t$ is never carried out: the forward recursion writes its outputs directly in that order and the opposite procedure reads it."),
   inf("S2.3", "A positional layout permutation $L$ places the selected bits of all axes at a common offset in consecutive $K$-bit chunks, so each round is one simultaneous layer, and the transforms cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\ell 2^{-p}$.",
       "The procedure constructs an explicit positional",
       page="transform-layout", frm=["synthetic-transform", "retained-frequency-order", "arbitrary-width-interchange", "simultaneous-butterfly-layer", "stream-operations", "fixed-point-disk"]),
   inf("S2.4", "A signed Kronecker substitution evaluates polynomial records at $2^{4p}$, multiplies with the established multiplier, and returns $Q_p(fg/r)$ in time $O(rp\\log(rp))$.",
       "One can compute the exact Gaussian integer",
       page="signed-packing-product", frm=["established-multiplier", "negacyclic-ring", "fixed-point-disk", "schoolbook-integer-arithmetic", "polynomials"]),
   inf("S2.5", "Both forward transforms are performed in the common order $LB$, the ring products are formed pointwise, the opposite procedure consumes that order, and the result is multiplied exactly by $M=T/r$.",
       "Perform both forward transforms and retain their common",
       frm=["error-accounting", "cyclic-convolution", "multidimensional-dft", "synthetic-transform", "transform-layout"]),
  ], page="synthetic-convolution",
  frm=["error-accounting", "cyclic-convolution", "multidimensional-dft", "synthetic-transform", "retained-frequency-order", "transform-layout", "signed-packing-product", "negacyclic-ring"],
  adds=[
    add("T", "box size", "The total number of complex coefficients in the padded box, the product of the axis lengths times the record length.", "count"),
    add("M", "record count", "The number of polynomial records, the product of the axis lengths other than the polynomial axis.", "count"),
    add("\\ell", "record exponent", "The binary logarithm of the record length $r$, so $r=2^\\ell$.", "direct"),
    add("K", "chunk width", "The number of address bits in each chunk on which simultaneous layers act.", "count"),
  ])

# ---- S3 resampling
s3 = show("S3",
  "A Fourier transform of coprime lengths is expressed through power-of-two transforms of the same box by Gaussian resampling, in $d$ dimensions, with the source and target permutations kept inside the identity, and the source permutation cancels across a convolution.",
  "Apply the Harvey--van der Hoeven resampling identity line by line on a zero-padded box, keep both coordinate permutations in the formula instead of sorting, and show that the retained source permutation drops out of the product of two forward transforms and one opposite transform.",
  expl("Gaussian resampling normally sorts twice on each coordinate, which would cost full passes; keeping the permutations in the identity avoids executing them.",
       "We retain both permutations in the transform formula and"),
  [
   inf("S3.1", "For coprime $s<t$ there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computed on a line of length $t$ in time $O(tp^{3/2+\\delta}\\alpha)$ without executing the permutations.",
       "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and",
       page="gaussian-resampling", frm=["dft", "primes-coprimality-and-gcd", "permutations", "newton-s-method", "fixed-point-disk", "error-accounting", "established-multiplier"]),
   inf("S3.2", "In $d$ dimensions the identity $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ holds, with line maps costing $O(dTp^{3/2+\\delta}\\alpha)$ in total and axis exposure $O(Tpd^2(1+\\ell^\\tau))$ using the chunk interchange.",
       "If each $t_i\\in\\{r/2,r\\}$ with $r=2^\\ell$, the array is kept in the",
       page="padded-box-tensor-resampling", frm=["gaussian-resampling", "arbitrary-width-interchange", "multidimensional-dft"]),
   inf("S3.3", "The source permutation $R$ cancels, giving $R F_{\\boldsymbol s}^+[(R F_{\\boldsymbol s}u)\\cdot(R F_{\\boldsymbol s}v)]=(u*v)/S^2$.",
       "because a coordinate permutation commutes with pointwise products.",
       page="permutation-cancellation", frm=["gaussian-resampling", "padded-box-tensor-resampling", "bluestein-chirp", "cyclic-convolution", "multidimensional-dft"],
       salient="The permutation $R$ appears twice, on both forward transforms and the opposite transform, and disappears from the result: $RF^+R=F^+$, so a coordinate permutation commutes with the pointwise product and nothing needs sorting."),
  ])

# ---- S4 multiplication algorithm
s44 = show("S4.4",
  "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ turns the last cyclic axis into a negacyclic polynomial ring, so the synthetic convolution computes the normalized complex convolution $(f*g)/T$.",
  "Twist each last-axis line by $\\zeta^k$, use the ring convolution on the remaining axes, and untwist.",
  expl("The power-of-two cyclic convolution needed by the chirp identity is not a ring convolution as it stands; the twist converts it to one.",
       "obtained from the synthetic convolution by a coefficient twist."),
  [
   inf("S4.4.1", "The map $x_d\\mapsto\\zeta y$ is an isomorphism from $\\mathbb C[x_d]/(x_d^r-1)$ onto the negacyclic ring, and the negative wrap becomes the cyclic wrap after untwisting.",
       "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",
       frm=["negacyclic-ring", "roots-of-unity", "complex-numbers"]),
   inf("S4.4.2", "The computed complex convolution twists both operands, calls the synthetic convolution, untwists, and truncates, each step with tracked disk and error bounds.",
       "the computed complex convolution is the",
       frm=["synthetic-convolution", "fixed-point-disk", "error-accounting"]),
  ], page="phase-twist",
  frm=["negacyclic-ring", "synthetic-convolution", "cyclic-convolution", "roots-of-unity", "complex-numbers"])

s46 = show("S4.6",
  "The source transform $RF_{\\boldsymbol s}$ is computed as $2^\\gamma\\mathcal B_0 Q F_{\\boldsymbol t}\\mathcal A$ from Gaussian expansion, a chirp transform and Gaussian compression, with tracked errors.",
  "Replace the middle factor $QF_{\\boldsymbol t}$ by the Bluestein chirp identity, evaluated with the twisted complex convolution, and wrap it in the line maps $\\mathcal A$ and $\\mathcal B_0$ and a power-of-two scaling.",
  expl("The middle transform is a Fourier transform of power-of-two length, which Bluestein's chirp identity reduces to convolution, and convolution is what the twist and the synthetic transforms compute.",
       "We next use the complex convolution to evaluate the middle factor"),
  [
   inf("S4.6.1", "The chirp transform $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,Q_p(\\overline{\\widetilde a}\\cdot x)))$ approximates $QF_{\\boldsymbol t}x$, with the permutation $Q$ absorbed.",
       "Thus $\\widetilde a$ is the convolution kernel and $x_0$ is the data",
       frm=["bluestein-chirp", "phase-twist", "padded-box-tensor-resampling"]),
   inf("S4.6.2", "Applying $\\mathcal A$ linewise, then the chirp transform, then $\\mathcal B_0$, then exact multiplication by $2^\\gamma$ computes $RF_{\\boldsymbol s}$ on a disk grid source tensor.",
       "For a source disk-grid tensor of norm at most $.5$, write",
       frm=["gaussian-resampling", "padded-box-tensor-resampling", "fixed-point-disk"]),
  ], page="source-transform",
  frm=["gaussian-resampling", "padded-box-tensor-resampling", "bluestein-chirp", "phase-twist", "synthetic-convolution", "permutation-cancellation", "error-accounting", "fixed-point-disk"])

s48 = show("S4.8",
  "Each recovered convolution coefficient lies within $1/2$ of its true integer value, which is below $2^{3b}$, so rounding and carry propagation give the exact product.",
  "Track scales and disk margins through every call, bound the accumulated error by $448b\\,2^{-b+\\gamma}<1/2$, round to the nearest integers, and propagate radix carries.",
  recov("Every step was an approximation with a known error bound that adds under composition, so only a final error below one half is needed for rounding to be correct."),
  [
   inf("S4.8.1", "The final absolute error is below $448b\\,2^{-b+\\gamma}\\le 448b\\,2^{-3b/4}<1/2$.",
       "<448b\\,2^{-b+\\gamma}",
       frm=["error-accounting", "source-transform", "permutation-cancellation"]),
   inf("S4.8.2", "The strict error below $1/2$ makes the nearest integer the unique correct coefficient, and it lies in $[0,2^{3b})$.",
       "The strict error below $1/2$ makes the nearest integer to",
       frm=["rational-numbers-and-rounding", "radix-digit-convolution"]),
   inf("S4.8.3", "Left-to-right carry propagation with $d_j=(c_j+k_j)\\bmod 2^b$ yields the $2n$ output bits exactly.",
       "To propagate carries, let $Q_0=2^b$.",
       frm=["schoolbook-integer-arithmetic", "radix-digit-convolution"]),
  ], page="exact-recovery",
  frm=["error-accounting", "source-transform", "permutation-cancellation", "radix-digit-convolution", "rational-numbers-and-rounding", "schoolbook-integer-arithmetic"],
  salient="The error budget is a power-of-two tolerance, not a lucky bound: with working precision $p=6b$ the error is $2^{-b/4}$-small against the required $1/2$.")

s4 = show("S4",
  "The algorithm of digit extraction, address map to prime axes, two source transforms, truncated pointwise product, opposite-sign transform, rescaling by $S$ and $2^{2b+4}$, rounding, inverse address map and carries produces the exact $2n$-bit product.",
  "Turn the product into a radix-digit convolution, place it on prime cyclic axes by a Chinese-remainder map, compute the convolution through the three source transforms, and prove that rounding recovers the integer coefficients.",
  recov("Integer multiplication is a convolution of digit lists, and the source transforms of the preceding sections compute convolutions on prime-length axes, so the digit list must be placed on such axes and the approximate result rounded."),
  [
   inf("S4.1", "Fixed parameters $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, $T\\approx n/b$, $r=2^{\\lceil(\\log_2T)/d\\rceil}$, with axes of length $r/2$ or $r$ and distinct primes $s_i$ just below $t_i$ found by deterministic search.",
       "b=\\lceil\\log_2n\\rceil,\\quad p=6b",
       page="prime-axis-parameters", frm=["logarithms-exponentials-floor-and-ceiling", "primes-coprimality-and-gcd", "gaussian-resampling", "padded-box-tensor-resampling", "transform-layout"],
       salient="Every exponent is a fixed rational ($\\epsilon=2^{-75}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $\\kappa=2^{-182}$), chosen so that all layer, resampling and recovery conditions hold at once with room to spare."),
   inf("S4.2", "Splitting each input into radix-$2^b$ digits gives a digit polynomial product of degree below $S$, so convolution modulo $x^S-1$ has no wraparound and every coefficient is below $2^{3b}$.",
       "Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
       page="radix-digit-convolution", frm=["schoolbook-integer-arithmetic", "polynomials", "binary-representation-and-bitwise-operations", "cyclic-convolution"]),
   inf("S4.3", "The map $x\\mapsto\\prod_i x_i^{\\mu_i}$ is an algebra isomorphism from $\\mathbb C[x]/(x^S-1)$ onto the prime-axis cyclic ring and is realized on tape by prefix-controlled cyclic shifts.",
       "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
       page="crt-map", frm=["controlled-shifts", "arbitrary-width-interchange", "primes-coprimality-and-gcd", "modular-arithmetic", "cyclic-convolution", "multidimensional-dft"],
       salient="Because $\\mu_iP_i\\equiv 1$ modulo $s_i$, axis $i$ depends only on lower-index digits, so the map is triangular in tape order and each axis is a single controlled shift."),
   s44,
   s46,
   inf("S4.7", "The algorithm computes $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$, multiplies pointwise and truncates, applies the opposite-sign transform, and scales by $S$ and $2^{2b+4}S$, where the retained source permutation cancels and the two scales $S$ undo different normalizations.",
       "The source-transform procedures now supply the three transforms needed",
       frm=["source-transform", "permutation-cancellation", "crt-map", "radix-digit-convolution"]),
   inf("S4.7b", "The exact counterpart after the three transforms is $(u*v)/S^2$, so the first scale gives $(u*v)/S$ and the second gives $2^{2b+4}(u*v)$, the integer convolution.",
       "The two occurrences of $S$ in this algorithm undo different",
       frm=["permutation-cancellation"]),
   s48,
  ], page="multiplication-algorithm",
  frm=["radix-digit-convolution", "crt-map", "phase-twist", "source-transform", "permutation-cancellation", "prime-axis-parameters", "cyclic-convolution"],
  adds=[
    add("b", "digit size", "The number of bits in each radix digit, $b=\\lceil\\log_2 n\\rceil$.", "count"),
    add("S", "cyclic length", "The product of the distinct prime axis lengths $s_i$, the length of the cyclic convolution.", "count"),
  ])

s5 = show("S5",
  "Dividing costs by $V=Tp$ leaves seven dominant terms, each at most $p^{1-2\\kappa}$, so the total time is $O(n(\\lg n)^{1-\\kappa})$ for $\\kappa=2^{-182}$.",
  "List the normalized cost of each operation as a power of $p$, bound every power by its margin below one, and let the smallest margin absorb all logarithmic factors.",
  expl("The parameters were chosen so that the cost table fits the theorem; the remaining check is arithmetic on the exponents.",
       "parameters makes all terms in its cost table fit"),
  [
   inf("S5.1", "The seven margins $g_1,\\ldots,g_7$ below one satisfy $\\min_i g_i=2^{-181}=2\\kappa$.",
       "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
       frm=["logarithms-exponentials-floor-and-ceiling", "asymptotic-notation-beyond-big-o"],
       salient="The smallest margin, from the chunk-exchange term $pK^{\\tau-1}$, is exactly $2\\kappa=2^{-181}$; the theorem's $\\kappa$ is half of it so that every fixed power of $\\log p$ is absorbed."),
   inf("S5.2", "Each of the seven displayed powers of $p$ is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
       "Each of the seven displayed powers is at most $1-2\\kappa$ by",
       frm=["worst-case-running-time-and-subroutines"]),
   inf("S5.3", "Below a fixed cutoff, schoolbook multiplication is used, so one fixed-tape machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
       "Fix one cutoff beyond all the size, precision, margin and layout",
       frm=["schoolbook-integer-arithmetic", "big-o"]),
  ], page="cost-accounting",
  frm=["multiplication-algorithm", "synthetic-convolution", "transform-layout", "simultaneous-butterfly-layer", "arbitrary-width-interchange", "padded-box-tensor-resampling", "crt-map", "prime-axis-parameters", "established-multiplier", "big-o", "asymptotic-notation-beyond-big-o"],
  salient="All seven cost terms have a power of $p$ below one by a margin of at least $2\\kappa$, with the tightest margin shared by one term only, so the same $\\kappa$ works for the whole algorithm.")

root = show("S0",
  "One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in time $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
  "Keep the transform-based multiplication of Harvey and van der Hoeven (Gaussian resampling, Bluestein chirp, synthetic polynomial transforms) but replace its two costly tape operations, address rearrangement and butterfly layers, by faster procedures obtained from rank-saving linear networks, then check exactness and total cost.",
  expl("Scanning an array at every transform level costs $n\\log n$ by itself, so a power saving needs both the data movement and the arithmetic of a level to be cheaper than a scan.",
       "We therefore need savings in both movement and arithmetic."),
  [s1, s2, s3, s4, s5],
  page="main-theorem",
  frm=["nlogn-history", "fixed-tape-model", "established-multiplier", "turing-machine", "big-o"],
  adds=[
    add("n", "input length", "The number of bits in each of the two integers being multiplied.", "count"),
    add("\\kappa", "saving exponent", "The constant $2^{-182}$ by which the power of $\\lg n$ falls below one."),
    add("p", "working precision", "The number of fractional bits of every fixed-point complex coefficient, $p=6b$.", "count"),
    add("r", "record length", "The number of complex coefficients in a polynomial record, a power of two.", "count"),
    add("d", "axis count", "The number of axes of the padded box, which is also the bound on the chunks of one butterfly layer.", "count"),
  ],
  salient="The saving is a genuine power $(\\lg n)^{-\\kappa}$ of the logarithm, although $\\kappa=2^{-182}$ is astronomically small; the theorem trades constants and thresholds, not asymptotic order, for beating $n\\log n$.")

json.dump({"root": root}, open(sys.argv[1], "w"), indent=1)
