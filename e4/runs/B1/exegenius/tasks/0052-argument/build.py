import json, re, sys
sys.path.insert(0,'.')
from quotes import Q, src

def ev(k): return {"source":"paper","quote":Q[k]}
def expl(text,k): return {"text":text,"source":"explicit","quote":ev(k)}
def rec(text): return {"text":text,"source":"recoverable","quote":None}
def recon(text): return {"text":text,"source":"reconstructed","quote":None}
def inf(id,claim,qk,page=None,frm=(),salient=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":ev(qk),"from":list(frm)}
    if page: n["page"]=page
    if salient: n["salient"]=salient
    return n
def show(id,claim,method,motivation,children,page=None,frm=(),salient=None,adds=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":motivation,"children":children,"from":list(frm)}
    if page: n["page"]=page
    if salient: n["salient"]=salient
    if adds: n["adds"]=adds
    return n
def b(symbol,name,meaning,rel="direct"): return {"symbol":symbol,"name":name,"meaning":meaning,"relation":rel}

T1=show("S1","Elementary scans on a fixed number of tapes (digit moves, splitting and merging streams, cyclic row splitting, controlled shifts) cost $O(V)$ time in the logical volume $V$.",
 "Collect the linear-time scan operations that every later tape procedure is built from",
 expl("The later procedures are assembled from these scans, so they must be shown to cost only linear time first.","motiv_T1"),
 [inf("S1.1","Permuting or moving a radix-$q$ digit, splitting on a digit and merging, and splitting whole rows cyclically into $W$ streams each take $O(V)$ steps.","T1.1",page="elementary-stream-operations",frm=["tape-address-arrays","turing-machine-tapes","big-o"]),
  inf("S1.2","Updating a later address field by an offset computed from earlier fields, $y\\mapsto y+a \\pmod{q^b}$, or multiplying it by a rational unit, costs $O(V)$.","T1.2",page="controlled-shifts",frm=["modular-arithmetic","elementary-stream-operations"])],
 frm=["tape-address-arrays"])

T2=show("S2","A fixed linear network of $W$ wires, with an $m\\times m$ matrix attached to each vertex, exchanges two banks of values with signs, restores every scratch wire, and has total edge rank $s<Wm$.",
 "Build a scalar gadget that exchanges the banks, put each wire's array in a frame so that only edge operators remain to implement, and label vertices with nested subspaces whose dimension changes count the edge ranks",
 expl("The tape procedures recurse once per unit of edge rank, so the whole point is that the total rank is strictly below the trivial bound.","motiv_T2"),
 [show("S2.1","A fixed network built from a three-subset gadget adds $x_S$ to $y_S$ for arbitrary scratch values and, in three stages, sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ while restoring every scratch wire.",
        "Schedule copy, gather, scatter and side injection in 8 rows so that unwanted intersection coefficients cancel, then compose three stages",
        recon("The intersection-size coefficients of the gather and scatter are wrong on some pairs of triples, and the side wires correct exactly those pairs; the eight-row schedule makes the result independent of the unknown scratch contents. Composing $y\\gets y+x$, $x\\gets x-y$, $y\\gets y+x$ gives an exchange."),
        [inf("S2.1.1","For arbitrary initial scratch values a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.","T2.1.1"),
         inf("S2.1.2","Three stages send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every auxiliary value.","T2.1.2")],
        page="triple-subset-gadget",frm=["linear-network-roles","groups-rings-and-fields","xor-and-arithmetic-over-f-2"]),
  inf("S2.2","When every wire at a gate carries the same frame $D_v$, a pointwise linear gate commutes with the frame, so only edge operators $D_vD_u^{-1}$ need implementing and the endpoint frames fix the net operator $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$.","T2.2",page="frames",frm=["linear-network-roles","entrywise-operations-on-arrays-and-vectors","special-matrices-and-matrix-algebra"]),
  show("S2.3","Nondegenerate subspace labels on gates and terminals, nested along every edge, can be chosen so that only the central-wire edges lose dimension and the total dimension change $s$ is strictly less than $Wm$.",
        "Attach tensor-product subspaces built from triple indicator vectors, and count the dimension lost on the decreasing edges",
        rec("The cost of an edge is the dimension of its orthogonal residual, so bounding the total change reduces to locating the few decreasing edges and totalling what they lose."),
        [inf("S2.3.1","Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.","T2.3.1"),
         inf("S2.3.2","The dimension lost on decreasing edges is less than half of the source dimension $N$, so the rank budget stays strictly below $Wm$.","T2.3.2")],
        page="subspace-labels-rank-deficit",frm=["frames","triple-subset-gadget","linear-algebra-basics"],
        salient="The total change is strictly below $Wm$, because the dimension lost is only $100/539$ (bit network) or $101/539$ (complex network) of $N$, below $1/2$, and all of it is lost on one kind of edge. The page should explain why only the central-wire return can decrease dimension, from the gate order and the nesting of labels."),
  show("S2.4","With rational projection matrices at the vertices, the bit network sends its input to the permutation $\\rho$ and its endpoint matrices differ by $I_m$ on every role, with total edge rank $s_{\\rm b}<W_{\\rm b}m$.",
        "Assign the projection $P_U$ to each vertex with label $U$ and the source matrix $-P_{U_a}$ to $X_a$, then read off endpoint differences and edge ranks",
        rec("Using projections turns the label dimension changes into matrix ranks, and the extra source rank is already absorbed in the spare dimension."),
        [inf("S2.4.1","For every input role $w$ the endpoint matrix difference $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}$ equals $I_m$.","T2.4.1"),
         inf("S2.4.2","The sum of the rational ranks of all edge differences is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.","T2.4.2")],
        page="address-shear",frm=["subspace-labels-rank-deficit","frames","special-matrices-and-matrix-algebra","modular-arithmetic"],
        salient="Every role, including scratch roles holding arbitrary values, receives the same shear $(H,D)\\mapsto(H+D,D)$. This uniformity should be explained from the endpoint matrix difference being the identity $I_m$ on every route."),
  inf("S2.5","Over the complex scalar network with binary labels, each edge frame change is a product of translation kernels $aI+bX_v$, one per residual basis vector, and telescoping gives $C^{\\otimes m}$ on every role including scratch roles.","T2.5",page="binary-phase-interface",frm=["subspace-labels-rank-deficit","frames","butterfly-and-phase-kernels","xor-and-arithmetic-over-f-2","complex-numbers"],
      salient="The same kernel $C^{\\otimes m}$ appears on every role, even auxiliary ones, although each route passes through different frames; this should follow from telescoping the phase frames.")],
 adds=[b("m","label dimension","the dimension of the fixed ambient label space, equal to the side of the matrices at the vertices","count"),
       b("W","wire count","the number of wires (roles) in the network","count"),
       b("s","total edge rank","the sum over all edges of the rank of the dimension or matrix change on that edge, equal to the number of smaller calls","count")])

T3=show("S3","Two disjoint equal-width address chunks of $u$ bits in a bit array of volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\\tau)$ time for a fixed rational $\\tau<1$.",
 "Realize the interchange as three shears, make the middle shear by running the bit network on row-split role streams, and implement each edge by rank-many smaller interchanges, recursively",
 expl("An edge of rank $a$ costs $a$ smaller interchanges, and the sum of these ranks is below $Wm$ times the number of wires, so the recurrence saves a power of the width.","motiv_T3"),
 [show("S3.1","A rational shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ costs exactly $\\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ work.",
        "Factor $A=E_1\\Pi E_2$ with lower triangular $E_1,E_2$, perform the triangular parts by controlled shifts, and spend one interchange per entry of $\\Pi$",
        rec("Lower triangular changes of coordinates are exactly the updates that a later field can receive from earlier fields in linear time, so only the partial permutation $\\Pi$ costs an interchange."),
        [inf("S3.1.1","Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.","T3.1.1"),
         inf("S3.1.2","The shear by $A$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.","T3.1.2")],
        page="triangular-factorization",frm=["controlled-shifts","linear-algebra-basics","modular-arithmetic","special-matrices-and-matrix-algebra"],
        salient="The partial permutation $\\Pi$ has exactly rank-many ones, so the interchange count equals the rank rather than the matrix size."),
  show("S3.2","For $e=m^k$ and enough rows, two chunks of $e$ digits can be interchanged in $O(Ve^\\tau)$ time.",
        "Split rows into $W$ role streams, run the bit network with address-shear frames on every edge so as to get the shear $H\\leftarrow H+D$ on all roles, form the interchange from three shears, and solve the resulting recurrence",
        rec("Each edge needs a smaller interchange on a stream of volume $V/W$, so the cost obeys a recurrence in the width, whose solution depends only on the ratio $s/W$ to $m$."),
        [inf("S3.2.1","Whole rows are split cyclically into $W$ role streams, each of logical volume $V/W$ with the same remaining shape.","T3.2.1",page="row-splitting",frm=["elementary-stream-operations","tape-address-arrays"]),
         inf("S3.2.2","Applying the address shear $\\Phi_{A_e}$ on every edge and the gates pointwise yields the shear $H\\leftarrow H+D$ on every original row, including rows of scratch roles.","T3.2.2"),
         inf("S3.2.3","The interchange follows from three shears, $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$, only the middle one using the circuit.","T3.2.3"),
         inf("S3.2.4","The normalized cost satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$, which for $s/W<m^\\tau$ gives $F_k=O(e^\\tau)$.","T3.2.4",page="recursive-power-saving",frm=["recurrences-and-the-recursion-tree","summation-telescoping-sums-and-geometric-series","row-splitting","triangular-factorization"],
             salient="The cost per volume grows like $e^\\tau$ with $\\tau<1$ rather than like $e$. This power saving should be explained from the strict inequality $s/W<m$ together with the factor $m$ by which the width shrinks at each level."),
         inf("S3.2.5","Recursive calls run on a fixed number of tapes by parking the inactive role streams on a stack tape, copying the active one to the child and restoring afterwards, at linear cost in the parent's volume.","T3.2.5",page="fixed-tape-recursion",frm=["recursion-call-stack-and-subroutines","turing-machine-tapes","row-splitting"])]),
  inf("S3.3","For arbitrary widths $u$ and arbitrary prefix, gap and suffix lengths, the interchange $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ costs $O(Vu^\\tau)$.","T3.3")],
 page="address-chunk-interchange",frm=["elementary-stream-operations","controlled-shifts","address-shear","tape-address-arrays","floor-ceiling-and-logarithms"],
 adds=[b("u","chunk width","the number of bits in each of the two interchanged address chunks","count"),
       b("\\tau","interchange exponent","a fixed rational exponent below $1$ in the cost $O(Vu^\\tau)$"),
       b("e","power width","the width $m^k$ of the chunks interchanged by the recursive procedure","count")],
 salient="The cost is $O(Vu^\\tau)$ with a fixed $\\tau<1$ even though the intermediate steps form XOR combinations of the data and the final effect is an exact permutation. The page should explain why a power saving appears at all, from the strict rank deficit $s<Wm$.")

T4=show("S4","A normalized butterfly layer $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied at one bit position in $D\\le d$ address chunks of every record costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$, with a single truncation at the end.",
 "Turn $H_0^{\\otimes D}$ into phases around a layer of the kernel $C$, evaluate $C^{\\otimes D}$ by the complex network with binary changes of basis done as packed address operations, recurse on row-split role streams, and keep everything exact in guarded dyadics",
 expl("Doing the layer by separate butterflies costs one whole-array pass per butterfly, which is exactly the $\\Theta(n\\log n)$ barrier; the layer must be done in one recursive pass.","motiv_T4"),
 [inf("S4.1","The butterfly equals phases around the kernel $C=aI+bX$: $H_0=b\\,\\mathsf S C\\mathsf S$ with $\\mathsf S=\\operatorname{diag}(1,i)$, so a layer of $H_0$ equals phases times a layer of $C$.","T4.1",page="butterfly-and-phase-kernels",frm=["complex-numbers","special-matrices-and-matrix-algebra"]),
  inf("S4.2","Applying the complex network with column frames to a group of $e=mf$ selected axes gives $C^{\\otimes e}$ on every role using $s_{\\rm c}$ child calls on $f$ axes each.","T4.2"),
  inf("S4.3","XORing corresponding selected bits of two address chunks across many chunks at once, with a third chunk as temporary, takes a few cyclic shifts plus a deterministic repair of a small exceptional set of addresses, in time $O(V(L^\\tau+1))$ in the stated regime.","T4.3",page="packed-selected-bit-addition",frm=["address-chunk-interchange","controlled-shifts","elementary-stream-operations","xor-and-arithmetic-over-f-2"]),
  inf("S4.4","With row splitting, the normalized cost satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which unrolls to $O(d^{\\lambda'})$.","T4.4"),
  inf("S4.5","Reserving $p+\\Delta$ fractional bits and $\\Delta+3$ integer and sign bits per component represents every intermediate coefficient of a layer exactly, with $\\Delta=o(p)$.","T4.5",page="guard-bits-dyadic",frm=["rational-numbers-and-dyadic-fractions","fixed-point-disk-grid","recurrences-and-the-recursion-tree"]),
  inf("S4.6","The procedure returns $Q_p(\\mathcal H z)$ in $O(Vd^{\\lambda'})$ time, with error below $\\sqrt2\\,2^{-p}$ and values in the unit disk.","T4.6")],
 page="simultaneous-butterfly-layer",
 frm=["binary-phase-interface","address-chunk-interchange","recursive-power-saving","row-splitting","fixed-tape-recursion","fixed-point-disk-grid","elementary-stream-operations","triangle-inequality-and-norm-bounds"],
 adds=[b("d","chunk count","the maximum number of address chunks (axes) acted on by one layer","count"),
       b("K","chunk width","the number of bits in each address chunk","count"),
       b("D","active chunk count","the number of chunks whose selected bit is acted on in a given layer","count"),
       b("\\Delta","guard width","the number of extra guard bits reserved for exact intermediate values","count")],
 salient="The layer costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$ although it touches $D\\le d$ axes; the saving over $D$ separate passes should be explained from the strict inequality $s_{\\rm c}<W_{\\rm c}m$ of the complex network.")

T5=show("S5","Normalized convolution over $\\mathbb C[y]/(y^r+1)$ on a product of cyclic axes is approximated with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O\\bigl(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)]\\bigr)$.",
 "Take two forward synthetic transforms in a retained frequency order, multiply pointwise by signed packing, and apply the opposite transform consuming that order",
 expl("The synthetic roots of unity act as exact signed permutations of coefficients, so only the butterflies cost arithmetic.","motiv_T5"),
 [inf("S5.1","With $\\omega_t=y^{2r/t}$ as roots of unity, the transforms $F_t^\\pm$ satisfy $F_t^+F_t^-=t^{-1}I$ and are computed by the butterfly recursion with twiddle monomials.","T5.1",page="synthetic-polynomial-transform",frm=["dft","multidimensional-transform","fft-butterfly","polynomial-ring-mod-y-r-plus-1","convolution"]),
  inf("S5.2","Leaving outputs in the bit-reversed order the recursion writes gives the exact procedures $B_tF_t^-$ and $F_t^+B_t^{-1}$, so no separate permutation is executed.","T5.2",page="frequency-order-retention",frm=["synthetic-polynomial-transform","fft-butterfly"]),
  inf("S5.3","A layout permutation $L$ places selected bits of all axes at a common offset in consecutive $K$-bit chunks, so each round is one simultaneous layer and the forward and opposite transforms cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.","T5.3",page="synthetic-transform-layout",frm=["simultaneous-butterfly-layer","address-chunk-interchange","frequency-order-retention","synthetic-polynomial-transform","elementary-stream-operations"]),
  inf("S5.4","Evaluating integer-coefficient polynomials at $2^{4p}$ turns the pointwise ring products into four integer products of $O(rp)$ bits, from which the coefficients are extracted by centered residues, in time $O(rp\\log(rp))$.","T5.4",page="signed-packing",frm=["nlogn-multiplier-subroutine","polynomial-ring-mod-y-r-plus-1","binary-representation-and-schoolbook-arithmetic"]),
  inf("S5.5","Both forward transforms are retained in the common $LB$ order, multiplied pointwise, and fed to the opposite procedure and scaled by $M$, giving $\\mathcal M_r(f,g)=(f*g)/T$ with the stated error.","T5.5")],
 page="synthetic-convolution",
 frm=["contractions-and-error","convolution","polynomial-ring-mod-y-r-plus-1","dft","multidimensional-transform","triangle-inequality-and-norm-bounds"],
 adds=[b("r","ring length","the number of complex coefficients in a record, a power of two","count"),
       b("M","record count","the number of records, equal to the product of the lengths of the first axes","count"),
       b("T","box size","the total number of entries $rM$ of the padded power-of-two box","count"),
       b("\\ell","ring log-length","$\\log_2 r$, the number of rounds contributing error","direct")],
 salient="The error bound $\\sqrt2\\,M(3\\ell+1)2^{-p}$ counts three transform errors plus one truncation, each contributing $\\ell$ rounds of at most $\\sqrt2\\,2^{-p}$; the page should explain the factor $3\\ell+1$ from the three transforms and the one product.")

T6=show("S6","A Fourier transform of pairwise coprime source lengths can be computed through power-of-two transforms, with the coordinate permutations kept inside the transform identity: $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, and the source permutation $R$ cancels in a convolution.",
 "Apply Gaussian resampling along each axis, write the middle transform as a chirp convolution, and show that the retained permutations cancel",
 expl("Executing the two permutations would cost two full sorts per axis, which is too expensive, so they are carried inside the identity instead.","motiv_T6"),
 [show("S6.1","The resampling identity $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ holds with contractions $A,B_0$ that are computable with error less than $p^2$, and tensoring gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$.",
        "Compose the Gaussian identity with a left inverse that keeps the permutations, then tensor over axes",
        rec("Harvey and van der Hoeven's argument composes a left inverse of the Gaussian map; here the sorting permutations are simply left in the formula, so only the normalizations need rechecking."),
        [inf("S6.1.1","The Gaussian identity $\\mathsf T P_sF_s=P_tF_t\\mathsf S$ holds with a near-identity correction $N=C\\mathsf T\\mathsf D$ satisfying $\\|N-I\\|<2^{-\\alpha^2\\theta}$.","T6.1.1",page="gaussian-resampling",frm=["dft","complex-numbers","triangle-inequality-and-norm-bounds","exponentials-and-elementary-inequalities"]),
         inf("S6.1.2","Applying the left inverse of $\\mathsf T$ and collecting normalizations gives $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.","T6.1.2"),
         inf("S6.1.3","Tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.","T6.1.3")],
        page="resampling-permutations-retained",frm=["gaussian-resampling","multidimensional-transform","dft","sets-functions-bijections-and-permutations"]),
  inf("S6.2","The middle factor with its target permutation equals a pointwise chirp phase around a cyclic convolution with the chirp kernel: $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.","T6.2",page="bluestein-chirp",frm=["dft","convolution","multidimensional-transform","complex-numbers"]),
  inf("S6.3","The retained source permutation cancels across two forward source transforms, their pointwise product and the opposite-sign transform, leaving $(u*v)/S^2$.","T6.3",page="permutation-cancellation",frm=["resampling-permutations-retained","dft","convolution","modular-arithmetic"],
      salient="The permutation $R$ appears in three transforms, yet no permutation is left in the result $(u*v)/S^2$; this should be explained from $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$ for a unit dilation and from pointwise products commuting with permutations.")],
 frm=["dft","multidimensional-transform"],
 adds=[b("s","source length","the prime length of a source axis","count"),b("t","padded length","the power-of-two length of the corresponding padded axis","count"),b("\\alpha","resampling width","an integer controlling the width of the Gaussian window and the accuracy of resampling")])

T8=show("S8","The scaled and rounded output coefficients equal the exact integer coefficients of the radix-digit product, and carry propagation yields the exact $2n$-bit product.",
 "Remove the known normalizations, bound the accumulated error below $1/2$ so that rounding is exact, then propagate radix-$2^b$ carries",
 rec("The approximate transforms only give coefficients up to a small error, and the true coefficients are integers, so exactness follows once the error is below one half."),
 [inf("S8.1","The final absolute error of each coefficient is less than $448b\\,2^{-b+\\gamma}\\le 448b\\,2^{-3b/4}<1/2$, so the nearest integer is the correct coefficient.","T8.1"),
  inf("S8.2","Radix-$2^b$ carries, defined by $d_j=(c_j+k_j)\\bmod 2^b$ and $k_{j+1}=\\lfloor (c_j+k_j)/2^b\\rfloor$, stay below $2^{2b}$ and give the exact $2n$-bit product.","T8.2")],
 page="exact-recovery",frm=["contractions-and-error","fixed-point-disk-grid","binary-representation-and-schoolbook-arithmetic","triangle-inequality-and-norm-bounds"],
 salient="The error bound $448b\\,2^{-3b/4}$ is below $1/2$ only because $p=6b$ leaves $b$ bits of room after the normalizations, and $\\gamma=o(b)$; the page should explain why these powers of two compensate.")

T7=show("S7","The six-step algorithm built on the source transforms outputs the exact $2n$-bit product of the inputs.",
 "Choose parameters and prime lengths, place the digit list on a product of prime cyclic axes, compute the convolution by the source transform pipeline, and run the six-step algorithm",
 expl("The three transforms needed by the radix-digit convolution are supplied by the source-transform procedures, so the remaining work is to arrange the inputs and outputs around them.","motiv_T7a"),
 [inf("S7.1","The sizes are $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, with $T\\in[4n/b,8n/b)$ a power of two and axis lengths $t_i\\in\\{r/2,r\\}$, giving $Tp=\\Theta(n)$.","T7.1",page="parameter-choice",frm=["floor-ceiling-and-logarithms","exponentials-and-elementary-inequalities"]),
  inf("S7.2","Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist, are found by trial division, and satisfy $T/2<S<T$ together with the separation $\\alpha^4\\theta_i>p$ needed by resampling.","T7.2",page="prime-source-lengths",frm=["parameter-choice","prime-numbers-and-trial-division","gaussian-resampling"],
      salient="The product $S=\\prod_i s_i$ of the primes fills more than half the box, $T/2<S<T$; this follows from each $s_i$ lying within a factor $1-2\\eta$ of $t_i$ with $\\eta=1/(4d)$."),
  inf("S7.3","Writing the inputs in base $2^b$ with $q=\\lceil n/b\\rceil$ digits, the product's degree is below $S$, so cyclic convolution of length $S$ has no wraparound, and every coefficient is below $2^{3b}$.","T7.3",page="integer-as-digit-convolution",frm=["convolution","binary-representation-and-schoolbook-arithmetic","parameter-choice","prime-source-lengths"]),
  inf("S7.4","The map $\\Phi:x\\mapsto\\prod_i x_i^{\\mu_i}$ is an algebra isomorphism from cyclic convolution of length $S$ to convolution on the product of cyclic axes, implemented by triangular controlled shifts.","T7.4",page="crt-address-map",frm=["convolution","modular-arithmetic","controlled-shifts","address-chunk-interchange","prime-source-lengths"]),
  inf("S7.5","Multiplying coefficient $k$ of the last cyclic axis by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $x_d^r-1$ to $y^r+1$, so complex cyclic convolution is computed by ring convolution followed by the untwist.","T7.5",page="phase-twist",frm=["convolution","polynomial-ring-mod-y-r-plus-1","complex-numbers"]),
  inf("S7.6","The approximate source transform resamples with $A$ along each axis, applies the chirp transform through ring convolution, compresses with $B_0$ and rescales by $2^\\gamma$, with exact counterpart $RF_{\\boldsymbol s}$.","T7.6",page="source-transform",frm=["resampling-permutations-retained","bluestein-chirp","phase-twist","synthetic-convolution","gaussian-resampling"]),
  inf("S7.7","The six steps are: form radix digits, apply the address map $\\Phi$, compute two source transforms, multiply pointwise, apply the opposite transform and rescale, round and carry.","T7.7"),
  T8],
 page="multiplication-algorithm",
 frm=["permutation-cancellation","synthetic-convolution"],
 adds=[b("b","digit width","the number of bits in one radix digit, so inputs are written in base $2^b$"),
       b("p","working precision","the number of fractional bits of the fixed-point values, equal to $6b$","count"),
       b("S","padded length","the product of the prime source lengths, the length of the convolution","count"),
       b("q","digit count","the number of radix-$2^b$ digits of each input","count"),
       b("\\eta","prime window","the relative window width $1/(4d)$ below $t_i$ in which each prime $s_i$ is chosen")])

T9=show("S9","Every normalized cost, divided by $Tp$, is at most $p^{1-2\\kappa}$, so the total cost is $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
 "Tabulate the normalized cost of each operation as a power of $p$, take the smallest margin below one, and absorb any fixed power of $\\log p$",
 rec("Each operation has cost $Tp$ times a power of $p$; the total is governed by the largest power, so only the margins to $1$ matter."),
 [inf("S9.1","The smallest margin below one among the seven dominant powers is $\\min_i g_i=2^{-181}=2\\kappa$.","T9.1"),
  inf("S9.2","Hence the total cost is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$, and with schoolbook multiplication below a cutoff the machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$.","T9.2")],
 page="cost-analysis",frm=["parameter-choice","synthetic-convolution","simultaneous-butterfly-layer","address-chunk-interchange","multiplication-algorithm","exponentials-and-elementary-inequalities","big-o"],
 salient="The smallest margin is $g_2=\\epsilon c(1-\\tau)=2^{-181}$, a tiny quantity coming from the chunk-exchange row; the page should explain why the exponent $\\kappa=2^{-182}$ is half of this margin and how it comes from the chosen constants $\\epsilon=2^{-75}$, $c=2^{-56}$ and $1-\\tau=2^{-50}$.")

root=show("S0","One deterministic fixed-alphabet, fixed-tape Turing machine multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time, where $\\kappa=2^{-182}$.",
 "Reduce the product to a convolution of radix digits evaluated by synthetic-transform Fourier transforms, and cut the cost of their data movement and arithmetic with two power-saving tape procedures built on finite linear networks",
 expl("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both movement and arithmetic must be sped up.","motiv_root"),
 [T1,T2,T3,T4,T5,T6,T7,T9],
 page="integer-multiplication-below-nlogn",
 frm=["nlogn-conjecture","convolution","nlogn-multiplier-subroutine","karatsuba-and-classical-multiplication-algorithms","deterministic-algorithms-and-worst-case-time","turing-machine-tapes","big-o"],
 salient="The saving is a power of the logarithm, $(\\lg n)^{-\\kappa}$, with an astronomically small but positive exponent, so $n\\log n$ is not a lower bound. The page should explain why the saving is a power rather than a smaller factor, from the strict inequality $s<Wm$ shared by both tape procedures.")

json.dump({"root":root},open('../0052-argument.answer.json','w'),indent=1)
