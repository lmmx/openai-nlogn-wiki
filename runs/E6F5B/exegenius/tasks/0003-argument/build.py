import json, re
ROOT='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5B/'
lines=open(ROOT+'sources/paper.tex').read().split('\n')
src=open(ROOT+'sources/paper.tex').read()

def Q(n, sub=None):
    t=lines[n-1].strip()
    if sub is not None:
        assert sub in lines[n-1], (n, sub)
        t=sub
    assert t in src
    return {"source":"paper","quote":t}

def mot(text, source, q=None):
    m={"text":text,"source":source}
    if q is not None: m["quote"]=q
    return m

def B(sym,name,meaning,rel="direct"):
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}

def infer(id,claim,page,frm,quote,salient=None):
    n={"id":id,"intention":"infer","claim":claim,"page":page,"from":frm,"quote":quote}
    if salient: n["salient"]=salient
    return n

def show(id,claim,page,frm,method,motivation,children,adds=None,salient=None):
    n={"id":id,"intention":"show","claim":claim,"page":page,"from":frm,"method":method,"motivation":motivation,"children":children}
    if adds: n["adds"]=adds
    if salient: n["salient"]=salient
    return n

# ---- S1 ----
S1_1=infer("S1.1","Permuting digit values, moving one digit, splitting on a digit with a pointwise map and merging, and splitting whole rows cyclically into a fixed number of streams each take $O(V)$ time on a fixed number of tapes.",
 "elementary-streams",["multitape-model","array-layout","positional-notation-in-any-radix-and-mixed-radix","stable-radix-sort-and-counting-sort"],
 Q(494))
S1_2=infer("S1.2","A later field modulo $q^b$ can be shifted cyclically by an offset computed from earlier control fields, or multiplied by a unit, in $O(V)$ time by splitting and merging blocks.",
 "controlled-shifts",["elementary-streams","modular-arithmetic","extended-euclidean-algorithm"],
 Q(566))

S1_3_1=infer("S1.3.1","For arbitrary initial values of the scratch wires, one forward invocation changes the target bank by $y_S\\mapsto y_S+x_S$ and leaves every other value unchanged, because the schedule first subtracts the scratch effect, adds the real contribution and undoes the scratch changes.",
 "scratch-restoration",["linear-algebra-basics","bitwise-operations-xor-and-hamming-weight"],Q(730))
S1_3_2=infer("S1.3.2","Three invocations at stages 1, 2 and 3 on banks indexed by triples of 3-subsets realize the signed exchange $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ and restore all auxiliary wires, the unwanted intersection-size coefficients being cancelled by scratch wires.",
 "subset-intersection-network",["scratch-restoration","counting-subsets-and-binomial-coefficients","bitwise-operations-xor-and-hamming-weight","complex-numbers"],Q(732))
S1_3_3=infer("S1.3.3","Giving every source, gate and sink an invertible frame $D_v$ makes the implemented operator $D_{\\rm out}\\mathsf S D_{\\rm in}^{-1}$, so a route sends input role $w$ to $D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$ and only changes of frame along edges cost work.",
 "gate-network-frames",["array-layout","linear-algebra-basics","permutations-and-permutation-matrices"],Q(818))
S1_3_4=infer("S1.3.4","Each gate and terminal gets a nested nondegenerate subspace of the $m$-dimensional space so that the only decreasing edges are the central wires between times 3 and 4, losing dimension $h$ each, and the summed dimension change is $Wm-2N+2L$ with $L<N/2$.",
 "subspace-labels",["nondegenerate-subspaces","gate-network-frames","subset-intersection-network","vector-norms-inner-products-and-orthogonality","linear-algebra-basics"],Q(999),
 salient="Only one family of edges ever loses dimension, and the total loss $L$ is under half of the source dimension $N$ (the ratio is $100/539$); the order in which the gates touch the wires confines every decrease to the central-wire return.")
S1_3_5=infer("S1.3.5","With projection matrices of the labels as frames, the bit network sends its input to the role exchange and every input role sees the same matrix difference $I_m$, while the total rational edge rank satisfies $s_{\\rm b}<W_{\\rm b}m$.",
 "bit-network-interface",["subspace-labels","gate-network-frames","linear-algebra-basics","bitwise-operations-xor-and-hamming-weight"],Q(1139),
 salient="The endpoint matrix difference is the identity $I_m$ on every role, including the scratch roles, so the same shear $H\\gets H+D$ is applied uniformly to all wires.")
S1_3_6=infer("S1.3.6","For the complex network with binary labels, the phase frame $\\mathcal C_U$ makes each edge change a product of one two-point kernel $aI+bX_v$ per residual basis vector, with total length $s_{\\rm c}<W_{\\rm c}m$, and the whole network equals $C^{\\otimes m}$ on every role.",
 "phase-interface",["two-point-butterfly","subspace-labels","nondegenerate-subspaces","bit-network-interface","bitwise-operations-xor-and-hamming-weight","complex-numbers"],Q(1217),
 salient="After the source and sink corrections the network acts as the same tensor power $C^{\\otimes m}$ on every role, including roles that only carried scratch values.")
S1_3_7=infer("S1.3.7","If the network's total edge rank satisfies $s<Wm$, a call at parameter $mf$ makes $s$ calls on streams of volume $V/W$ at parameter $f$, so the cost per volume obeys $F_k\\le(s/W)F_{k-1}+O(1)$ and grows only like $m^{k\\tau}$ for a fixed $\\tau<1$ such as $1-2^{-50}$.",
 "rank-saving-recurrence",["divide-and-conquer-recurrences","convergent-series-and-the-geometric-series","exponential-and-logarithm-functions","subspace-labels","big-o"],Q(1326),
 salient="The strict inequality $s<Wm$ is the whole source of the saving, and the exponent $\\tau=1-2^{-50}$ is only barely below one because the relative rank deficit is of order $10^{-14}$.")
S1_3=show("S1.3","Two fixed linear networks exchange two banks of values with prescribed signs while restoring every scratch value, and carry subspace labels whose total edge rank $s$ is less than $Wm$.",
 None,[],
 "Construct the scalar gate schedule and show how frames turn it into an operator on arrays, attach nested nondegenerate subspaces as labels so that dimension changes count the cost of edges, and read off the bit and phase interfaces and the resulting recurrence.",
 mot("The saving cannot be obtained from the data alone; one needs a fixed network on a constant number of wires whose edge changes are cheap, and the sources build it before choosing labels.","explicit",Q(643,"We construct two fixed linear networks that exchange two banks of values")),
 [S1_3_1,S1_3_2,S1_3_3,S1_3_4,S1_3_5,S1_3_6,S1_3_7])

S1_4_1=infer("S1.4.1","Every rational matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
 "lower-triangular-factorization",["gaussian-elimination","linear-algebra-basics","permutations-and-permutation-matrices"],Q(1366))
S1_4_2=infer("S1.4.2","The address map $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ is performed with exactly $\\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ further work.",
 "matrix-shear-cost",["lower-triangular-factorization","controlled-shifts","elementary-streams","modular-arithmetic"],Q(1406),
 salient="Exactly $\\operatorname{rank}(A)$ interchanges are needed, however large the matrix is, because three updates turn the shear $H+D$ into a single swap.")
S1_4_3=infer("S1.4.3","Two chunks of $e=m^k$ radix-$q$ digits are interchanged in $O(Ve^\\tau)$ time by splitting rows into $W$ role streams and running the bit network with each edge shear done by recursive interchanges of chunks of width $e/m$.",
 "power-width-interchange",["rank-saving-recurrence","bit-network-interface","gate-network-frames","matrix-shear-cost","elementary-streams","controlled-shifts","array-layout"],Q(1486))
S1_4_4=infer("S1.4.4","For arbitrary widths and row counts, interchange a few high digits first, pad the row count to a multiple of $W^k$, split the remaining width in base $m$ and interchange each piece, which stays within $O(Vu^\\tau)$.",
 None,[],Q(1633))
S1_4=show("S1.4","Two disjoint address chunks of $u$ bits in an array with complete Cartesian address set can be exchanged in $O(Vu^\\tau)$ time, although the intermediate steps form XOR combinations of the data.",
 "chunk-interchange",["array-layout","multitape-model"],
 "Turn the bit network into an address shear, factor each edge matrix so that an edge of rank $a$ costs $a$ smaller interchanges, recurse on chunks of $1/m$ the width, and then remove the power-of-$m$ width and row-count restrictions by padding.",
 mot("An edge matrix of rank $a$ requires only $a$ smaller interchanges, and because the ranks sum to less than the wire count times $m$, the recurrence saves a power of the chunk width.","explicit",Q(1352,"Because the sum of these ranks is less than the number of wires times")),
 [S1_4_1,S1_4_2,S1_4_3,S1_4_4],adds=[B("u","chunk width","The number of bits in each of the two address chunks being interchanged.","count")])

S1_5_1=infer("S1.5.1","Each edge's frame change is a product of kernels $aI+bX_{v_j}$ along an orthonormal residual basis, an invertible address change puts these directions in the first slots, and $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, so a layer on $D$ chunks needs only $s$ children on $1/m$ of the axes.",
 None,[],Q(1837))
S1_5_2=infer("S1.5.2","An XOR of the same bit position in $f$ chunks of one address range into another is done together by a constant number of cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small explicitly identified set of exceptional addresses, restoring a third scratch chunk.",
 "packed-selected-bit-addition",["chunk-interchange","controlled-shifts","elementary-streams","scratch-restoration","bitwise-operations-xor-and-hamming-weight"],Q(1993))
S1_5_3=infer("S1.5.3","The whole layer is evaluated exactly on Gaussian dyadic values, with intermediate numerator and denominator widths bounded by a guard width $\\lceil C_0d^{C_1}\\rceil=o(p)$, and one truncation $Q_p$ follows the completed contractive layer.",
 None,[],Q(2452))
S1_5=show("S1.5","One $H_0$ butterfly can be applied at the same bit offset in $D\\le d$ address chunks at once, computed exactly with a single final truncation, in $O(Vd^{\\lambda'})$ time.",
 "simultaneous-butterfly-layer",["two-point-butterfly","fixed-point-numerics","phase-interface","rank-saving-recurrence","chunk-interchange","controlled-shifts","elementary-streams","negacyclic-ring"],
 "Express the normalized layer $H_0^{\\otimes D}$ through the auxiliary kernel $C^{\\otimes D}$ and its phase network, implement the binary basis changes of each edge by packed selected-bit additions, recurse on $1/m$ of the axes after splitting rows among the wires, and bound the dyadic growth by a guard width.",
 mot("Applying the butterflies one axis at a time would take $D$ whole-array passes; the network lets one pass handle all $D$ axes at a cost that grows only like a power of $d$ below one.","explicit",Q(1793,"$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly")),
 [S1_5_1,S1_5_2,S1_5_3],adds=[B("D","active chunk count","The number of address chunks, at most $d$, on which the butterfly is applied simultaneously.","count")])

S1=show("S1","Two tape procedures save a power: address chunks of $u$ bits are interchanged in $O(Vu^\\tau)$ time and a common butterfly layer on $D\\le d$ chunks is applied in $O(Vd^{\\lambda'})$ time, with fixed $\\tau,\\lambda'<1$.",
 None,[],
 "Build both procedures from fixed linear networks whose total edge rank is smaller than the wire count times the label dimension, so that a recursion on smaller calls on smaller volumes saves a power of the width.",
 mot("Scanning the array at each of the logarithmically many transform levels already costs $n\\log n$, so both data movement and butterfly arithmetic must be made cheaper than a full scan per level.","explicit",Q(91,"$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$.")),
 [S1_1,S1_2,S1_3,S1_4,S1_5],
 adds=[B("\\tau","interchange exponent","The fixed exponent below one in the cost $O(Vu^\\tau)$ of an address interchange."),
       B("\\lambda'","butterfly exponent","The fixed exponent below one in the cost $O(Vd^{\\lambda'})$ of a simultaneous layer."),
       B("W","wire count","The number of wires, scratch wires included, of the fixed linear network.","count"),
       B("m","label dimension","The dimension of the fixed space whose subspaces label the network's gates and terminals.","count"),
       B("s","edge rank total","The sum over all edges of the rank or residual dimension of the frame change, with $s<Wm$.","count")])

# ---- S2 ----
S2_1=infer("S2.1","Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the roots of unity $\\omega_t=y^{2r/t}$ give a Fourier transform with $F_t^+F_t^-=t^{-1}I$ whose twiddle multiplications are signed shifts of coefficient lists, even though the ring has zero divisors.",
 "synthetic-transform",["negacyclic-ring","discrete-fourier-transform","multidimensional-transform","polynomials"],Q(2806),
 salient="Every twiddle multiplication costs only a signed shift of a coefficient list, because powers of $y$ act as exact roots of unity.")
S2_2=infer("S2.2","A positional permutation moves selected bits of the $d-1$ axes of an array of $M$ polynomial records to a common offset in $K$-bit chunks so each transform round is one simultaneous layer, giving forward and opposite synthetic transforms costing $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ that keep the frequency order for a pointwise product.",
 "transform-layout",["butterfly-recursion","synthetic-transform","simultaneous-butterfly-layer","chunk-interchange","elementary-streams","fixed-point-numerics","negacyclic-ring"],Q(2973),
 salient="Frequency $j$ is stored at its bit-reversed position, and the opposite transform consumes exactly that order, so no permutation of the frequencies is ever executed.")
S2_3=infer("S2.3","A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at the base $2^{4p}$, multiplying the resulting integers with the $O(N\\log N)$ multiplier, and reading centered coefficients back out, then wrapping modulo $y^r+1$.",
 "signed-packing",["nlogn-multiplier","negacyclic-ring","polynomials","fixed-point-numerics","binary-integers"],Q(3223))
S2=show("S2","Normalized convolution over $\\mathbb C[y]/(y^r+1)$ is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with explicit error bound.",
 "ring-convolution",["negacyclic-ring","cyclic-convolution","multidimensional-transform","discrete-fourier-transform","fixed-point-numerics","nlogn-multiplier"],
 "Use the convolution theorem for the synthetic transform, apply the fast layered transforms in their retained layout, and multiply the polynomial records with signed packing and the established $O(n\\log n)$ multiplier.",
 mot("Pointwise multiplication commutes with the record permutation of the stored forward outputs, so the forward outputs can be multiplied in their retained order and passed straight to the opposite procedure.","explicit",Q(3202)),
 [S2_1,S2_2,S2_3],
 adds=[B("\\ell","record exponent","The base-2 logarithm of the record length $r$, equal to the number of butterfly rounds on a long axis."),
       B("M","record count","The number of polynomial records, the product of the axis lengths other than the polynomial axis.","count"),
       B("y","ring generator","The variable of $\\mathbb C[y]/(y^r+1)$ satisfying $y^r=-1$, whose powers serve as roots of unity."),
       B("\\omega_t","synthetic root","The root of unity $y^{2r/t}$ of order $t$ in the polynomial ring.")])

# ---- S3 ----
S3_1=infer("S3.1","There are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable by fixed multitape algorithms with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, which expresses a transform of coprime length $s$ through one of length $t$.",
 "gaussian-resampling",["discrete-fourier-transform","fixed-point-numerics","nlogn-multiplier","exponential-and-logarithm-functions","convergent-series-and-the-geometric-series","floor-ceiling-and-rounding"],Q(3559))
S3_2=infer("S3.2","Applying the one-dimensional maps line by line along each axis of a zero-padded power-of-two box gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with error below $dp^2$, at cost $O(dTp^{3/2+\\delta}\\alpha)$ plus the chunk interchanges that expose the axes.",
 "tensor-resampling-box",["gaussian-resampling","multidimensional-transform","chunk-interchange","fixed-point-numerics"],Q(3802))
S3_3=infer("S3.3","The target-permuted transform equals a pointwise chirp phase, a cyclic convolution with the chirp, and another pointwise chirp phase: $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
 "bluestein-chirp",["cyclic-convolution","discrete-fourier-transform","multidimensional-transform","complex-numbers"],Q(3919),
 salient="The target frequency permutation $Q$ is absorbed into the chirp identity and is never applied to the array as a separate permutation.")
S3_4=infer("S3.4","The source permutation $R$ retained inside each transform cancels across two forward transforms, their pointwise product and the opposite transform: $RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=u*v/S^2$.",
 "permutation-cancellation",["gaussian-resampling","bluestein-chirp","discrete-fourier-transform","permutations-and-permutation-matrices","modular-arithmetic","cyclic-convolution"],Q(3926),
 salient="The answer contains no trace of the permutation $R$ even though both forward transforms carry it, because dilation by a unit commutes with the opposite transform up to inversion and permutations commute with pointwise products.")
S3=show("S3","A Fourier transform of pairwise coprime lengths $s_i$ is expressed through a power-of-two tensor transform by Gaussian resampling, with the source and target permutations retained and removed by cancellation and the chirp identity.",
 None,[],
 "Apply Gaussian resampling to move from coprime lengths to power-of-two lengths, keep the two coordinate permutations inside the identity instead of sorting, convert the middle power-of-two transform to a cyclic convolution by Bluestein's chirp, and cancel the source permutation across the pointwise product.",
 mot("The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two, and Gaussian resampling connects these two shapes.","explicit",Q(3499)),
 [S3_1,S3_2,S3_3,S3_4],
 adds=[B("A","expansion map","The linear contraction from $\\mathbb C^s$ to $\\mathbb C^t$ that spreads the source onto the power-of-two grid."),
       B("B_0","compression map","The linear contraction from $\\mathbb C^t$ to $\\mathbb C^s$ that collects the transformed values at the source frequencies."),
       B("R","source permutation","The coordinate permutation left inside the source transform on the coprime-length side."),
       B("Q","target permutation","The coordinate permutation left inside the power-of-two transform, absorbed by the chirp.")])

# ---- S4 ----
S4_1=infer("S4.1","From $n$ set $b=\\lceil\\log_2n\\rceil$, precision $p=6b$, axes $d=\\lfloor b^\\epsilon\\rfloor$, chunk width $K=\\lfloor d^c\\rfloor$, box size $T\\approx n/b$ and axis lengths $t_i\\in\\{r/2,r\\}$ with $r=2^\\ell$, so that $Tp=\\Theta(n)$ and $r$ exceeds every fixed power of $p$.",
 "size-parameters",["simultaneous-butterfly-layer","transform-layout","tensor-resampling-box","gaussian-resampling","floor-ceiling-and-rounding","exponential-and-logarithm-functions"],Q(4055),
 salient="The record length $r=2^{\\Theta(p^{1-\\epsilon})}$ is superpolynomial in $p$ although the number of axes $d$ grows only like $p^\\epsilon$, which makes all per-record setup negligible.")
S4_2=infer("S4.2","Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ are found by trial division, so their product $S$ satisfies $T/2<S<T$ while each ratio $t_i/s_i$ leaves the separation that resampling needs.",
 "prime-lengths",["prime-numbers-coprimality-and-trial-division","gaussian-resampling","exponential-and-logarithm-functions","big-o"],Q(4135),
 salient="The product of the $d$ primes fills more than half of the padded box, uniformly in $d$, because each is within a factor $1-1/(2d)$ of its power of two.")
S4_3=infer("S4.3","A cyclic convolution of length $S=s_1\\cdots s_d$ with pairwise coprime $s_i$ becomes a convolution on the product of cyclic axes of lengths $s_i$ via $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$, implemented by triangular controlled shifts and axis moves.",
 "crt-prime-axes",["cyclic-convolution","controlled-shifts","chunk-interchange","modular-arithmetic","extended-euclidean-algorithm","positional-notation-in-any-radix-and-mixed-radix","prime-lengths"],Q(4220),
 salient="Each new axis coordinate depends only on lower-index digits, so the map is triangular and every update is one controlled cyclic shift.")
S4_4=infer("S4.4","Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathbb C[y]/(y^r+1)$, so the last cyclic axis is convolved over the ring and then untwisted.",
 "coefficient-twist",["negacyclic-ring","ring-convolution","cyclic-convolution","complex-numbers","fixed-point-numerics"],Q(4319))
S4_5=infer("S4.5","The computed source transform applies the linewise Gaussian map $A$, the chirp transform done by complex convolution through the twist, the linewise map $B_0$, and an exact $2^\\gamma$ rescale, approximating $RF_{\\boldsymbol s}$.",
 "source-transform",["tensor-resampling-box","bluestein-chirp","coefficient-twist","ring-convolution","fixed-point-numerics"],Q(4456))
S4_6=infer("S4.6","Split the operands into radix-$2^b$ digits, map them by $\\Phi$ to prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by $S$ and $2^{2b+4}$, round to integers, undo $\\Phi$ and propagate carries.",
 "multiplication-algorithm",["radix-digit-convolution","crt-prime-axes","source-transform","permutation-cancellation","fixed-point-numerics","floor-ceiling-and-rounding","binary-integers"],Q(4488),
 salient="The scale $S$ is applied twice for different reasons: once to undo the $1/S^2$ left by the three normalized transforms and once for the normalization of the convolution itself.")
S4_7=infer("S4.7","Disk-margin and error bookkeeping show that the recovered coefficient error stays below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.",
 "exact-recovery",["fixed-point-numerics","multiplication-algorithm","ring-convolution","source-transform","permutation-cancellation","coefficient-twist","floor-ceiling-and-rounding"],Q(4730,"The strict error below $1/2$ makes the nearest integer to"),
 salient="Working precision $p=6b$ is enough: the final error bound $448b\\,2^{-3b/4}$ is far below $1/2$ even after the large rescalings.")
S4_8=infer("S4.8","Dividing each cost by $V=Tp$, seven dominant terms have powers of $p$ at most $1-2\\kappa$, and the smallest margin $2^{-181}$ fixes $\\kappa=2^{-182}$, with any polylogarithmic factor absorbed.",
 "time-accounting",["transform-layout","simultaneous-butterfly-layer","chunk-interchange","crt-prime-axes","tensor-resampling-box","signed-packing","size-parameters","nlogn-multiplier"],Q(4983),
 salient="The saving exponent $\\kappa=2^{-182}$ is astronomically small but positive: it is half of the smallest of seven margins, which is the product of the tiny exponents $\\epsilon$, $c$ and $1-\\tau$.")
S4=show("S4","With explicit parameters, prime axes, a coefficient twist and the computed source transform, the radix-digit convolution is recovered exactly and every cost term fits within $O(n(\\lg n)^{1-\\kappa})$.",
 None,[],
 "Choose compatible rational parameters for all procedures, lay out the digit convolution on prime axes and a negacyclic last axis, run the computed source transforms, bound all errors below $1/2$, and add up every cost against the volume.",
 mot("The procedures have different parameter requirements, so one must choose compatible parameters, recover the integer coefficients from the approximations, and account for the remaining tape operations.","explicit",Q(4000,"We choose compatible parameters for these procedures, recover")),
 [S4_1,S4_2,S4_3,S4_4,S4_5,S4_6,S4_7,S4_8],
 adds=[B("b","digit width","The radix exponent $\\lceil\\log_2 n\\rceil$: each digit of the operands has $b$ bits.","count"),
       B("\\Phi","address map","The Chinese-remainder isomorphism from the cyclic coefficient index to the product of prime cyclic axes."),
       B("\\zeta","twist root","The root of unity $e^{\\pi i/r}$ whose powers twist cyclic coefficients into negacyclic ones."),
       B("\\eta","prime window","The relative width of the interval below $t_i$ from which the prime $s_i$ is chosen.")])

root=show("S0","Two $n$-bit integers are multiplied exactly by one deterministic fixed-tape Turing machine in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "main-theorem",["multitape-model","nlogn-conjecture","nlogn-multiplier","radix-digit-convolution","discrete-fourier-transform","cyclic-convolution","multidimensional-transform","two-point-butterfly","fixed-point-numerics","negacyclic-ring","butterfly-recursion"],
 "Reduce the product to a convolution of short radix-digit polynomials, evaluate it through Gaussian resampling, Bluestein chirps and synthetic polynomial transforms, and speed up the data movement and butterfly arithmetic of those transforms with two procedures built from linear networks with a rank saving, then verify exactness and the total cost.",
 mot("A scan of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $n\\log n$, so savings are needed in both movement and arithmetic.","explicit",Q(92,"We therefore need savings in both movement and arithmetic.")),
 [S1,S2,S3,S4],
 salient="The saving exponent $\\kappa=2^{-182}$ is astronomically small yet strictly positive, so the bound is a true power saving over $n\\log n$ although it is invisible at any practical size.",
 adds=[B("V","stored volume","The number of stored data bits of the array being processed.","count"),
       B("d","axis count","The number of axes (equal-width address chunks) handled together, growing like a small power of $p$.","count"),
       B("p","working precision","The number of fractional bits of the fixed-point grid, proportional to $\\log n$.","count"),
       B("r","record length","The number of complex coefficients of a polynomial record, a power of two.","count"),
       B("T","box size","The number of entries of the padded power-of-two box, with $Tp=\\Theta(n)$.","count"),
       B("S","source size","The product of the pairwise coprime prime source lengths, the number of source entries.","count"),
       B("K","chunk width","The number of bits in one address chunk of the transform layout.","count"),
       B("t_i","padded axis length","The power-of-two length of axis $i$ of the padded box.","count"),
       B("s_i","prime axis length","The prime source length of axis $i$, slightly below $t_i$.","count")])

json.dump({"root":root},open(ROOT+'exegenius/tasks/0003-argument.answer.json','w'),indent=1)

# check order
pos=[]
def walk(n):
    if n['intention']=='infer':
        q=n['quote']['quote']
        assert src.count(q)>=1
        pos.append((src.index(q),n['id'],src.count(q)))
    for c in n.get('children',[]): walk(c)
walk(root)
print(pos)
assert [p[0] for p in pos]==sorted(p[0] for p in pos)
pages=[]
def wp(n):
    if n.get('page'): pages.append(n['page'])
    for c in n.get('children',[]): wp(c)
wp(root)
print(len(pages), len(set(pages)))
