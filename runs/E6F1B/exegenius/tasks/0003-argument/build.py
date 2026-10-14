import json
SRC='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1B/sources/paper.tex'
src=open(SRC).read()

def ev(q):
    assert src.count(q)==1, q
    return {"source":"paper","quote":q}

def inf(id,claim,quote,page=None,frm=(),salient=None,deferred=False):
    n={"id":id,"intention":"infer","claim":claim,"quote":ev(quote),"from":list(frm)}
    if page: n["page"]=page
    if salient: n["salient"]=salient
    if deferred: n["deferred"]=True
    return n

def show(id,claim,method,mot,children,page=None,frm=(),salient=None,adds=None):
    text,kind,*q=mot
    m={"text":text,"source":kind}
    if kind=="explicit": m["quote"]=ev(q[0])
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":m,"children":children,"from":list(frm)}
    if page: n["page"]=page
    if salient: n["salient"]=salient
    if adds: n["adds"]=[{"symbol":s,"name":nm,"meaning":me,"relation":r} for s,nm,me,r in adds]
    return n

# ---------------- S1 tape toolkit
S1=show("S1","The elementary tape scans on arrays in lexicographic order (digit moves, splits, merges, row splits, controlled cyclic shifts and rational scalings) all take linear time $O(V)$.",
 "list the linear-time scan primitives on a lexicographically stored array",
 ("Every later procedure is assembled from a fixed number of such scans, so their linear cost has to be established first and independently of the recursive machinery.","reconstructed"),
 [inf("S1.1","An array is stored in lexicographic order, so an address field is a contiguous range of positions and an address is implicit in position, not stored.",
      "An address is implicit in an entry's position in this ordered stream",page="array-order",frm=["fixed-tape-model","tape-machines","sets-subsets-and-basic-combinatorics"]),
  inf("S1.2","Permuting digit values, moving a digit, splitting on a digit with a pointwise map and merging, and splitting whole rows cyclically into $W$ equal streams each take $O(V)$ steps on a fixed number of tapes.",
      "takes $O(V)$ steps on a fixed number of one-dimensional tapes:",page="stream-ops",frm=["array-order","fixed-tape-model","functions-bijections-and-permutations"]),
  inf("S1.3","Adding to a target field an offset computed from earlier control fields modulo $q^b$ (a cyclic shift of blocks), or multiplying it by a fixed rational unit, costs $O(V)$.",
      "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",page="controlled-shifts",frm=["array-order","stream-ops","modular-arithmetic"])],
 frm=["fixed-tape-model"])

# ---------------- S2 networks
S2=show("S2","There are two fixed linear networks, a bit network on $\\mathbb F_2$ with address shears and a complex phase network, that exchange two banks of values, restore every scratch wire, and need a total number $s$ of smaller calls strictly below $Wm$.",
 "build a fixed exchange network on wires, give its gates frames and nested subspace labels, and count the dimension changes along its edges",
 ("The sources attach nested subspaces to the vertices so that each edge's change of representation costs one smaller call per unit of dimension change; the saving is then read off from the total.","explicit","count the smaller operations needed on an edge"),
 [inf("S2.1","A fixed schedule of copy, gather, scatter and side-injection gates changes $y_S$ to $y_S+x_S$ for arbitrary initial scratch values, and three such stages give the signed exchange $(X_a,Y_a)\\mapsto(-Y_a,X_a)$.",
      "For arbitrary initial values of its auxiliary wires, a forward",page="network",frm=["binary-field-f2-and-xor","vectors-matrices-and-linear-maps","boolean-gates-and-circuits","sets-subsets-and-basic-combinatorics"]),
  inf("S2.2","If every array on a wire is given an invertible address-space operator (frame) at each vertex, a common frame commutes with a pointwise linear gate, so the network's overall effect is the endpoint frames applied to each role and each edge only changes the frame.",
      "Thus the common frame commutes with the pointwise gate, and",page="frames",frm=["network","vectors-matrices-and-linear-maps"],
      salient="The intermediate frames cancel completely: only the first and last frame of each route matter, so they can be chosen freely to make every edge cheap."),
  inf("S2.3","Subspaces of a tensor-cube bilinear space built from indicator vectors of three-element subsets, whose pairings are intersection sizes, label the gates so that labels are nested along edges and neighboring triples are orthogonal.",
      "Thus every triple line is nondegenerate, and neighboring triple lines",page="subset-labels",frm=["matrix-basics","network","frames","sets-subsets-and-basic-combinatorics"]),
  inf("S2.4","Summing the dimension changes of all labels gives a total $s$ of smaller calls strictly below $Wm$, because only the central-wire edges from time 3 to time 4 decrease and the loss ratio $L/N$ is below $1/2$.",
      "edges are the central-wire edges from time 3 to time 4; their dimension",page="rank-saving",frm=["subset-labels","matrix-basics","frames"],
      salient="The deficit $Wm-s$ is a tiny but strictly positive fraction of $Wm$, which is the sole source of the power saving."),
  inf("S2.5","The bit network uses only XOR gates, its frames are address shears with endpoint operator $(H,D)\\mapsto(H+D,D)$ on every role, and its rank sum satisfies $s_{\\rm b}<W_{\\rm b}m$.",
      "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",page="bit-network",frm=["network","frames","subset-labels","rank-saving","matrix-basics"]),
  inf("S2.6","The complex phase network has frames $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}(i^{\\operatorname{wt}(P_Ux)\\bmod 4})H^{\\otimes m}$, each edge is a product of two-point kernels $aI+bX_v$, and the endpoint operator is $C^{\\otimes m}$ on every role with $s_{\\rm c}<W_{\\rm c}m$.",
      "After source and sink diagonal corrections, and undoing the signed",page="phase-network",frm=["network","frames","subset-labels","rank-saving","butterfly-fft","dft","complex-numbers"]),
  inf("S2.7","With $\\tau=\\sigma=1-2^{-50}$ the ratios satisfy $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$.",
      "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,",frm=["rank-saving","bit-network","logarithms-and-exponentials"],
      salient="The exponent is fixed at $1-2^{-50}$: the relative rank deficits are only about $10^{-11}$, so the usable saving is minuscule but positive.")],
 frm=["fixed-tape-model","matrix-basics"],
 adds=[("W","wire count","the number of wires (roles) in the network","count"),
       ("m","label dimension","the dimension of the bilinear label space, which is the number of fields in each address chunk","count"),
       ("s","call count","the total number of smaller operations needed over all edges of the network","count")])

# ---------------- S3 chunk interchange
P_children=[
  inf("S3.3.1","Split whole rows cyclically into $W$ role streams, each of volume $V/W$ and with the same remaining address shape.",
      "Split whole rows cyclically into $W$ role streams within each prefix",frm=["stream-ops","bit-network"]),
  inf("S3.3.2","On every edge of the bit network apply the shear $\\Phi_{A_e}$ to that role stream by recursively interchanging each pivot pair of $b$-digit fields, and run each gate pointwise.",
      "$\\Phi_{A_e}$ to that role stream; implement it by",frm=["matrix-shear","frames","bit-network"]),
  inf("S3.3.3","After merging the streams back, the effect is $H\\leftarrow H+D$ on every original row, including rows carrying arbitrary scratch values.",
      "is $H\\leftarrow H+D$ on every original row, including rows assigned",frm=["frames","bit-network"]),
  inf("S3.3.4","The three updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ interchange the two chunks, and only the middle shear uses the network.",
      "To interchange the two full chunks, perform",frm=["controlled-shifts"]),
  inf("S3.3.5","The normalized cost satisfies $F_0=O(1)$ and $F_k\\le (s/W)F_{k-1}+O(1)$, which solves to $F_k=O(e^\\tau)$ because $s/W<m^\\tau$.",
      "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",page="power-saving-recurrence",frm=["rank-saving","bit-network","proof-by-induction-and-recursion","logarithms-and-exponentials","asymptotic-notation-beyond-big-o"],
      salient="Although the recursion branches into $s$ calls on streams of volume $V/W$, the cost per unit volume grows only like $e^\\tau$ with $\\tau<1$: the branching factor $s/W$ is strictly less than $m^\\tau$, where $m$ is the factor by which the parameter shrinks."),
]
S33=show("S3.3","Two disjoint chunks of $e=m^k$ digits, with a row field divisible by $W^k$, can be interchanged in $O(Ve^\\tau)$ time.",
 "apply the bit network to the chunks' address fields, doing each edge's shear by smaller interchanges, then compose three shears into a swap",
 ("A shear of one field into another is what the network's endpoint operator provides, and a swap is three shears; the edges of the network are the smaller shears, so the same procedure recurses on a width smaller by the factor $m$.","recoverable"),
 P_children,page="power-interchange",frm=["lower-triangular","matrix-shear","bit-network","frames","stream-ops","controlled-shifts"])

S3=show("S3","Two disjoint address chunks of $u$ bits can be interchanged in an array in $O(Vu^\\tau)$ tape steps for the fixed $\\tau=1-2^{-50}<1$, whatever the prefix, gap and suffix.",
 "turn the bit network into a recursive interchange, then remove the width and row restrictions by padding and a base-$m$ split",
 ("An edge matrix of rank $a$ will require $a$ smaller interchanges.","explicit","An edge matrix of rank $a$ will require $a$ smaller interchanges."),
 [inf("S3.1","Every rational matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with $a$ ones.",
      "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",page="lower-triangular",frm=["matrix-basics","vectors-matrices-and-linear-maps"]),
  inf("S3.2","The map $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ for a rank-$a$ rational matrix $A$ is performed by triangular controlled shifts and exactly $a$ interchanges of $b$-digit fields.",
      "can be performed with exactly $a$ interchanges of pairs of $b$-digit",page="matrix-shear",frm=["lower-triangular","controlled-shifts","modular-arithmetic"]),
  S33,
  inf("S3.4","The rows needed by the power-width interchange can be supplied by the high digits of the chunks themselves, which are exchanged one pair at a time at a cost below the final bound.",
      "Write each chunk as its top $\\rho$ digits followed by its remaining",frm=["stream-ops","power-interchange"]),
  inf("S3.5","Padding the row count with zero rows to a multiple of $W^k$ at most doubles the volume and does not disturb the completed interchanges.",
      "Append zero rows, separately within",frm=["power-interchange"]),
  inf("S3.6","Writing the remaining width in base $m$ splits each chunk into pieces of widths $m^j$, each interchanged by the power-width procedure, for total cost $O(Ve^\\tau)$.",
      "Write the remaining width in base $m$:",frm=["power-interchange","positional-number-representation-and-carries"]),
  inf("S3.7","Padding a binary chunk range $[2^u]$ up to $[q^e]$ changes the volume by a fixed factor, so the bound holds for arbitrary binary widths $u$.",
      "Finally, for binary chunks let $e$ be the least integer with",frm=["power-interchange"])],
 page="chunk-interchange",frm=["bit-network","array-order","stream-ops"],
 salient="The final effect is an exact permutation, even though the intermediate steps form XOR combinations of data and the scratch rows start with arbitrary values.",
 adds=[("\\tau","interchange exponent","the fixed exponent below 1 in the interchange cost $O(Vu^\\tau)$","direct")])

# ---------------- S4 simultaneous layer
S42=show("S4.2","The selected bit can be added to the same position of $f$ chunks at once, $y\\leftarrow y\\oplus x$, restoring a scratch chunk, in time $O(V(L^\\tau+1))$ away from a small exceptional set of addresses.",
 "do the packed update with a fixed number of whole-chunk cyclic shifts, then repair the explicitly identified exceptional addresses",
 ("The shifts are linear-time and need no per-bit work, but guard values fail at a few addresses; since those addresses depend only on the address, repairing them keeps the bound worst case over payloads.","explicit","The correction depends only on addresses, so the time bound is"),
 [inf("S4.2.1","Eight conditional increments of two integers induce a parity flip of $u$ and restore the scratch integer $w$.",
      "We first construct eight rotations that have the required effect away",frm=["controlled-shifts","chunk-interchange"]),
  inf("S4.2.2","The small set of addresses where the guard values fail is identified from the addresses alone and corrected deterministically.",
      "We then correct exactly that set.",frm=["stream-ops"])],
 page="packed-bit-addition",frm=["controlled-shifts","chunk-interchange","stream-ops"])

S4=show("S4","The two-point butterfly $H_0$ can be applied at one bit position in each of at most $d$ address chunks of an array at once, with one final truncation, in $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$.",
 "recurse on the complex phase network applied to the selected bits, implementing basis changes by packed bit addition and splitting rows among the wire roles",
 ("The $D$ butterfly factors would otherwise need $D$ whole-array passes; the network turns the layer into $s_{\\rm c}$ smaller layers on streams of volume $V/W_{\\rm c}$.","explicit","$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly"),
 [inf("S4.1","A group of $e=mf$ selected axes is handled by the phase network with column frames: each edge's residual basis gives one child call on $f$ axes, in total $s_{\\rm c}$ children, after binary basis changes of the selected bits.",
      "Apply the finite network with these column frames to a group of",frm=["phase-network","frames","butterfly-fft"]),
  S42,
  inf("S4.3","Selected chunks are used as a row index split cyclically among the $W_{\\rm c}$ roles, so every child call acts on a stream of exactly $1/W_{\\rm c}$ of the parent's volume.",
      "write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),",frm=["stream-ops","phase-network"]),
  inf("S4.4","The normalized cost satisfies $F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1)$ with $F(e)=O(e)$ for small $e$, which unrolls to $O(d^{\\lambda'})$.",
      "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),",frm=["power-saving-recurrence","packed-bit-addition","chunk-interchange"],
      salient="The recurrence is the same one as for the address interchange: the strict inequality $s/W<m^\\sigma$ again turns a branching recursion into a power saving."),
  inf("S4.5","Intermediate Gaussian dyadic values stay exact within a guard width of $\\lceil C_0d^{C_1}\\rceil=o(p)$ extra bits, so the whole layer is evaluated exactly before one truncation.",
      "The accelerated network is evaluated exactly until an entire",frm=["dyadic-rationals-and-binary-fractions","fixed-point-disk-grid"]),
  inf("S4.6","The identity $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$ turns the $C$-layer into the normalized butterfly layer, and the final truncation toward zero keeps the unit disk with error below $\\sqrt2\\,2^{-p}$.",
      "converts the resulting exact $C$-layer to $\\mathcal H$.",frm=["butterfly-fft","fixed-point-disk-grid","complex-numbers"])],
 page="simultaneous-layer",frm=["phase-network","packed-bit-addition","power-saving-recurrence","fixed-point-disk-grid","butterfly-fft","polynomial-ring-mod"],
 salient="The cost exponent $\\lambda'<1$ does not depend on the number $D$ of simultaneous axes: $D$ layers cost far less than $D$ passes over the array.",
 adds=[("d","axis bound","the maximum number of address chunks on which the layer acts together","count"),
       ("K","chunk width","the number of bits in each address chunk","count"),
       ("\\lambda'","layer exponent","the fixed exponent below 1 in the layer cost $O(Vd^{\\lambda'})$","direct")])

# ---------------- S5 transform layout
S5=show("S5","The normalized synthetic transform on arrays of polynomials modulo $y^r+1$ (and its opposite) runs in $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ time, leaving frequencies in bit-reversed order that the opposite transform consumes.",
 "arrange the selected bits of all participating axes at a common offset so that each radix-two round is one simultaneous layer",
 ("The simultaneous layer applies one butterfly bit position across many chunks, so the layout must line up the same bit of every axis in consecutive chunks.","explicit","we must place the selected bits of the participating axes at a common"),
 [inf("S5.1","Taking $\\omega_t=y^{2r/t}$ as root of unity in the ring, the length-$t$ transforms are contractions and $F_t^+F_t^-=t^{-1}I$, with twiddle multiplication a signed shift of coefficients.",
      "Every power of $\\omega_t$ is an isometry, and each transform entry is",page="synthetic-transform",frm=["polynomial-ring-mod","dft","butterfly-fft","complex-numbers"]),
  inf("S5.2","After all rounds the output entry $j$ sits in slot $\\operatorname{rev}_a(j)$, and the opposite procedure traverses the recursion in reverse to consume this stored order.",
      "After all $a$ rounds, the named slots from high to low therefore",frm=["butterfly-fft","synthetic-transform"]),
  inf("S5.3","One round on $D$ axes is a parallel butterfly followed by one recordwise monomial multiplication $y^E$ whose exponent depends only on the address.",
      "Consequently the individual axis steps may be grouped as a parallel",frm=["multidim-transform","synthetic-transform","simultaneous-layer"]),
  inf("S5.4","An explicit positional layout permutation, built from single-bit moves and chunk interchanges, makes each round one call of the simultaneous layer, with cost charged to the transform.",
      "The procedure constructs an explicit positional",frm=["simultaneous-layer","chunk-interchange","stream-ops"])],
 page="transform-layout",frm=["butterfly-fft","multidim-transform","polynomial-ring-mod","fixed-point-disk-grid","simultaneous-layer","chunk-interchange","synthetic-transform"],
 salient="The forward transform never reorders its output: the bit-reversed order is kept through the pointwise product and consumed by the opposite transform, so no sorting pass is executed.")

# ---------------- S6 ring convolution
S6=show("S6","Normalized convolution of arrays of ring polynomials is computed by two forward synthetic transforms, pointwise ring products, and the opposite transform, in the stored order, within the stated error and cost.",
 "transform, multiply pointwise, and transform back using the convolution theorem",
 ("A transform turns convolution into pointwise product, and the pointwise product of short polynomial records is cheap by Kronecker substitution with the known multiplier.","recoverable"),
 [inf("S6.1","Both forward transforms are performed and their common layout order is retained.",
      "Perform both forward transforms and retain their common $LB$ order.",frm=["transform-layout","convolution-theorem"]),
  inf("S6.2","Two ring polynomials are multiplied by evaluating at $B_0=2^{4p}$ as signed integers, multiplying with the $O(N\\log N)$ multiplier, extracting centered coefficients and wrapping negacyclically, in $O(rp\\log(rp))$ time.",
      "One can compute the exact Gaussian integer",page="kronecker-packing",frm=["nlogn-multiplier","polynomial-ring-mod","positional-number-representation-and-carries"],deferred=True),
  inf("S6.3","The opposite transform is applied to the retained order and the result is scaled exactly by $M$, giving the normalized convolution.",
      "Apply the opposite procedure",frm=["transform-layout","convolution-theorem"])],
 page="ring-convolution",frm=["transform-layout","kronecker-packing","convolution-theorem","synthetic-transform","cyclic-convolution","polynomial-ring-mod"])

# ---------------- S7 resampling & chirp
S7=show("S7","A Fourier transform of pairwise coprime lengths, with its coordinate permutations kept in the formula, is expressed through a power-of-two transform and cheap maps, and the middle transform is a cyclic convolution whose permutation cancels in the product.",
 "keep both coordinate permutations in the identity instead of sorting, then rewrite the middle transform by the chirp identity",
 ("The usual implementation of Gaussian resampling sorts twice on each coordinate; keeping the permutations inside the formula avoids those sorts.","explicit","Its usual implementation sorts twice on each"),
 [inf("S7.1","There are contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable line by line with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
      "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and",page="gaussian-resampling",frm=["dft","fixed-point-disk-grid","exponential-function-and-gaussian-function","primes-coprimality-and-gcd","functions-bijections-and-permutations"]),
  inf("S7.2","Tensoring the one-dimensional identity over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, the lines being processed one axis at a time using chunk interchanges.",
      "Tensoring \\eqref{eq:no-sort-one-dimensional} proves",frm=["gaussian-resampling","multidim-transform","chunk-interchange"]),
  inf("S7.3","The factor $QF_{\\boldsymbol t}$ equals pointwise multiplication by a quadratic chirp phase, a cyclic convolution with the chirp array, and another pointwise phase multiplication.",
      "The coefficient of $u_{\\boldsymbol k}$ in the right side of",page="chirp-identity",frm=["dft","multidim-transform","cyclic-convolution","complex-numbers"]),
  inf("S7.4","The source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving $(u*v)/S^2$.",
      "For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.",page="permutation-cancellation",frm=["gaussian-resampling","chirp-identity","convolution-theorem","functions-bijections-and-permutations"],
      salient="No permutation is ever executed: the same permutation $R$ appears before and after the pointwise product and drops out.")],
 frm=["dft","multidim-transform","chunk-interchange","fixed-point-disk-grid","cyclic-convolution"])

# ---------------- D multiplication algorithm
D=show("D","Two $n$-bit integers are multiplied exactly by splitting them into radix-$2^b$ digits, mapping the digit convolution onto prime axes, computing source transforms of both, multiplying pointwise, applying the opposite-sign transform with scalings, then rounding and propagating carries.",
 "reduce integer product to digit convolution, evaluate the convolution through the source transforms, and recover exact integers from approximations",
 ("Exactness comes from rounding approximate coefficients that are known to be integers, so every approximation error must be shown to be below $1/2$.","recoverable"),
 [inf("D.1","Each input is written as a polynomial in $2^b$ with digit coefficients, and with enough zero padding the cyclic convolution modulo $x^S-1$ equals the ordinary product, whose coefficients are below $2^{3b}$.",
      "Thus convolution modulo $x^S-1$ has no nonzero wraparound.",page="int-as-convolution",frm=["cyclic-convolution","polynomials","positional-number-representation-and-carries"],deferred=True),
  inf("D.2","Distinct odd primes $s_i$ just below the powers of two $t_i$ are found by deterministic search so that $T/2<S<T$ and every hypothesis of the resampling lemma holds.",
      "We may therefore choose distinct odd primes satisfying",page="prime-lengths",frm=["primes-coprimality-and-gcd","gaussian-resampling","floor-ceiling-and-rounding"]),
  inf("D.3","The Chinese-remainder map $x\\mapsto\\prod_i x_i^{\\mu_i}$ is an isomorphism preserving cyclic convolution, and on tape it is a triangular sequence of prefix-controlled cyclic shifts plus axis exchanges.",
      "$\\Phi$ is an isomorphism and preserves cyclic convolution.",page="crt-axis-map",frm=["primes-coprimality-and-gcd","modular-arithmetic","controlled-shifts","chunk-interchange","cyclic-convolution"]),
  show("D.4","Normalized cyclic convolution $f*g/T$ of complex arrays on power-of-two axes is obtained by twisting the last axis into the polynomial ring and using the ring convolution.",
       "twist the last axis into the negacyclic ring and use the ring convolution",
       ("The ring convolution is negacyclic while the chirp identity needs cyclic wrap; the coefficient twist by $\\zeta^k$ exactly cancels the sign of the wrap.","recoverable"),
       [inf("D.4.1","Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps cyclic convolution on the last axis to convolution modulo $y^r+1$, whose negative wrap cancels the twist.",
            "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",page="negacyclic-twist",frm=["polynomial-ring-mod","cyclic-convolution","complex-numbers"]),
        inf("D.4.2","Twisting both operands, convolving the first $d-1$ axes over the ring, and untwisting gives the normalized complex convolution as a bilinear contraction.",
            "Here $\\mathcal M_r$ convolves the first $d-1$ axes over $\\mathcal R$,",frm=["ring-convolution","negacyclic-twist"])],
       page="complex-convolution",frm=["ring-convolution","negacyclic-twist","cyclic-convolution","fixed-point-disk-grid"]),
  inf("D.5","The middle factor $QF_{\\boldsymbol t}$ is evaluated by the chirp identity as phase multiplication, complex convolution with the chirp array, and phase multiplication.",
      "We next use the complex convolution to evaluate the middle factor",frm=["chirp-identity","complex-convolution","fixed-point-disk-grid"]),
  inf("D.6","The source transform applies the Gaussian map $\\mathcal A$ line by line, the chirp transform, the map $\\mathcal B_0$, and an exact scale by $2^\\gamma$, and has exact counterpart $RF_{\\boldsymbol s}$.",
      "$\\widetilde{\\mathscr F}$ for the following procedure: apply the linewise",page="source-transform",frm=["gaussian-resampling","chirp-identity","complex-convolution","fixed-point-disk-grid","crt-axis-map"]),
  inf("D.7","The source transforms of both digit arrays are computed.",
      "\\item Compute $\\widetilde{\\mathscr F}(u)$ and",frm=["source-transform"]),
  inf("D.8","The two transforms are multiplied pointwise exactly and truncated to $p$ fractional bits.",
      "\\item Multiply corresponding complex coefficients exactly and truncate",frm=["source-transform"]),
  inf("D.9","The opposite-sign transform is applied and the result is scaled exactly by $S$ and then by $2^{2b+4}S$, so that by permutation cancellation the exact counterpart is the integer coefficient convolution.",
      "\\item Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid",frm=["source-transform","permutation-cancellation"]),
  show("D.10","The recovered coefficient error is below $1/2$, so rounding gives the integer convolution coefficients, and radix-$2^b$ carries yield exactly $2n$ product bits.",
       "bound the accumulated approximation error, round, then propagate carries",
       ("Since the true coefficients are integers, an error below $1/2$ identifies each uniquely, and carrying converts coefficients to binary digits.","recoverable"),
       [inf("D.10.1","The final absolute error after the exact scalings is less than $448b\\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.",
            "the final absolute error is less than",frm=["fixed-point-disk-grid","vector-norms-and-error-bounds"]),
        inf("D.10.2","Carries in increasing coefficient order produce the product digits, and the stream is reversed to output exactly $2n$ bits.",
            "To propagate carries, let $Q_0=2^b$.",frm=["positional-number-representation-and-carries"])],
       page="exact-recovery",frm=["fixed-point-disk-grid","source-transform","permutation-cancellation","positional-number-representation-and-carries","vector-norms-and-error-bounds","floor-ceiling-and-rounding"])],
 page="mult-algorithm",frm=["int-as-convolution","crt-axis-map","complex-convolution","source-transform","exact-recovery","prime-lengths","determinism-and-exact-versus-approximate-computation"])

# ---------------- E parameter balance
E=show("E","With $p=\\Theta(\\log n)$, $d=\\lfloor b^\\epsilon\\rfloor$ axes and ring dimension $r=2^{\\Theta(p/d)}$, every row of the cost table has normalized power of $p$ at most $1-2\\kappa$, so the total time is $O(n(\\log n)^{1-\\kappa})$.",
 "fix all parameters and tiny exponents, then tabulate the normalized cost of each operation as a power of $p$ and compare with $1-2\\kappa$",
 ("The explicit minimum margin $2^{-181}=2\\kappa$ leaves enough slack to absorb any remaining fixed power of $\\log p$.","explicit","This explicit slack will cover"),
 [inf("E.1","The fixed rational exponents $\\tau,\\sigma,\\lambda,\\lambda',c,\\epsilon,\\delta$ and $\\kappa=2^{-182}$ are chosen so that all layer, resampling and dimension conditions hold with room to spare.",
      "These constants are deliberately conservative; no optimization is claimed.",frm=["power-saving-recurrence","simultaneous-layer","chunk-interchange"],deferred=True),
  inf("E.2","The seven dominant margins below one satisfy $\\min_i g_i=2^{-181}=2\\kappa$.",
      "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",frm=["logarithms-and-exponentials"],
      salient="The smallest margin, $2^{-181}$, belongs to the chunk-exchange row of the transform layout and equals exactly twice $\\kappa$, so $\\kappa=2^{-182}$ is half the weakest margin."),
  inf("E.3","Line-by-line Gaussian maps, CRT and axis layouts, chirps and twists, and packed polynomial products each cost a power of $p$ below the margin, with $p$ and $d$ as given.",
      "For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines.",frm=["gaussian-resampling","crt-axis-map","complex-convolution","kronecker-packing","transform-layout"]),
  inf("E.4","Descriptor setup, prime search, exceptional-address sorting and tape management across all recursive calls cost $o(Tp)$.",
      "We next separate setup at recursion nodes from work repeated for every",frm=["prime-lengths","packed-bit-addition","chunk-interchange"]),
  inf("E.5","Each of the seven displayed powers is at most $1-2\\kappa$, so the complete large-input bound is $O(n(\\log n)^{1-\\kappa})$.",
      "Each of the seven displayed powers is at most $1-2\\kappa$ by",frm=["big-o","logarithms-and-exponentials"])],
 page="parameter-balance",frm=["simultaneous-layer","transform-layout","chunk-interchange","gaussian-resampling","prime-lengths","crt-axis-map","complex-convolution","ring-convolution","mult-algorithm","asymptotic-notation-beyond-big-o","logarithms-and-exponentials"],
 adds=[("p","working precision","the number of fractional bits of each stored real or imaginary part, proportional to $\\log n$","count"),
       ("d","axis count","the number of axes of the padded box","count"),
       ("r","ring dimension","the number of complex coefficients in a ring polynomial record","count")])

# ---------------- root
root=show("R","There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture in this model.",
 "build two fast tape procedures from linear networks with a rank saving, insert them into a Gaussian-resampling and chirp reduction of the digit convolution to a ring convolution, and balance all parameters",
 ("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so the movement and the arithmetic of the transforms must both be made cheaper.","explicit","We therefore need savings in both movement and arithmetic."),
 [S1,S2,S3,S4,S5,S6,S7,D,E],
 page="main-theorem",frm=["fixed-tape-model","nlogn-conjecture","nlogn-multiplier","big-o","tape-machines","determinism-and-exact-versus-approximate-computation","matrix-basics","cyclic-convolution","dft","multidim-transform","butterfly-fft","polynomial-ring-mod","fixed-point-disk-grid","convolution-theorem"],
 salient="The saving $\\kappa=2^{-182}$ is astronomically small yet strictly positive, and it comes entirely from the strict inequality $s/W<m^\\tau$ for the network rather than from large constants.",
 adds=[("\\kappa","saving exponent","the fixed exponent $2^{-182}$ by which the logarithmic factor is reduced","direct")])

json.dump({"root":root},open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1B/exegenius/tasks/0003-argument.answer.json','w'),indent=1)
print("ok")
