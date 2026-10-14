import json, re, sys
SRC = open('/home/user/openai-nlogn-wiki/runs/O1/sources/paper.tex').read()
def Q(q):
    if q not in SRC:
        print("MISSING:", repr(q)); sys.exit(1)
    return {"source": "paper", "quote": q}
def B(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}
def infer(id, claim, quote, page=None, frm=(), salient=None, deferred=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": Q(quote), "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n
def show(id, claim, method, mot, children, page=None, frm=(), salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot,
         "children": children, "from": list(frm)}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n
def M(text, src, quote=None):
    m = {"text": text, "source": src}
    if quote: m["quote"] = Q(quote)
    return m

tape_prims = show("S1.1",
  "Fixed digit permutations and moves, digit splits and merges, cyclic row splits, and controlled shifts $y\\mapsto y+a(\\text{controls}) \\pmod Q$ of a later field each cost $O(V)$ on fixed tapes.",
  "establish each primitive by a constant number of split-and-merge scans with counters",
  M("Every later tape procedure is assembled from these scans, so each must be linear in the logical volume regardless of how many address fields surround it.", "recoverable"),
  [
    infer("S1.1.1", "Permuting or moving fixed radix digits, splitting on a digit and merging, and splitting rows cyclically into $W$ streams each take $O(V)$ steps.",
          "Each of the following operations on an array of", page="elementary-stream-ops",
          frm=["array-layout","binary-counters-and-amortized-analysis","binary-and-radix-representation","lexicographic-order"]),
    infer("S1.1.2", "Adding to a target field an offset computed from earlier control fields, or multiplying it by a fixed rational unit, costs $O(V)$.",
          "The next operations are linear because their target field follows their", page="controlled-shifts",
          frm=["array-layout","elementary-stream-ops","modular-arithmetic","greatest-common-divisor-and-coprimality"]),
  ])

networks = show("S1.2",
  "There are two fixed linear networks with $W$ wires that exchange two banks while restoring all scratch wires, whose edge changes need in total $s<Wm$ smaller calls, so that $s/W<m^\\tau$ with $\\tau=1-2^{-50}$.",
  "build a three-stage bank exchange from triple-subset invocations, attach nested nondegenerate subspace labels to its vertices, and count the dimensions of the edge residuals",
  M("When a network's values are replaced by arrays, a common frame at each gate commutes with the pointwise gate, so only the frame changes on edges cost anything; labels whose residual dimensions sum to less than $Wm$ make that cost smaller than doing $m$ full-size operations per wire.",
    "explicit", "The saving will come from keeping the total dimension lost on decreasing"),
  [
    show("S1.2.1", "Three stages of invocations send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ and restore every scratch wire, whatever its initial value.",
         "compose a forward invocation $y\\gets y+x$, an inverse invocation $x\\gets x-y$, and a forward invocation, each with its own restored scratch wires",
         M("Three additive updates realize an exchange up to sign, and each update can be built from gather, scatter and side wires whose old values are subtracted first.", "recoverable"),
         [
           infer("S1.2.1.1", "Gather and scatter through the $h$ central wires give coefficient $|S\\cap T|$ modulo two (or $(|S\\cap T|-1)/2$), the side wires cancel the unwanted neighbor coefficients, and the net effect of one invocation is $y_S\\gets y_S+x_S$.",
                 "Thus both net maps are $y\\gets y+x$.", page="triple-intersection",
                 frm=["scratch-restoration","subsets-and-binomial-coefficients","linear-algebra","bitwise-xor"]),
           infer("S1.2.1.2", "The three stages take $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
                 "$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."),
         ],
         page="bank-exchange-network", frm=["triple-intersection","scratch-restoration","directed-graphs-and-acyclic-networks"],
         salient="The exchange is exact for arbitrary initial scratch values, so scratch wires can later be fed arbitrary existing data."),
    infer("S1.2.2", "With an invertible frame $D_v$ at every vertex, common to all incidences of a gate, the network on arrays implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so each route applies the endpoint frame ratio.",
          "Thus the common frame commutes with the pointwise gate, and", page="frames",
          frm=["bank-exchange-network","linear-algebra","matrix-inverse-transpose-and-identity"]),
    infer("S1.2.3", "Nested nondegenerate labels in $F^{\\otimes 3}$ can be attached so that the only decreasing edges are central-wire returns losing dimension $h$, and the absolute dimension changes sum to $Wm-2N+2L$ with $L<N/2$.",
          "Every edge joins comparable nondegenerate labels.", page="subspace-labels",
          frm=["bilinear-form","tensor-product","linear-algebra","indicator-vector","subsets-and-binomial-coefficients","bank-exchange-network","frames"]),
    infer("S1.2.4", "With projection matrices as frames, the bit network has endpoint matrix difference $I_m$ on every role and total edge rank $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
          "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
          frm=["subspace-labels","frames","lower-bounds-for-computational-problems"] [0:2]),
    infer("S1.2.5", "With binary labels, the complex network's residual basis lengths sum to $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$.",
          "The deficit is $2N-2L_{\\rm c}>0$.", frm=["subspace-labels","bilinear-form"]),
    infer("S1.2.6", "Both relative deficits exceed $20\\cdot 2^{-50}$, hence $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\tau$ with $\\tau=1-2^{-50}$.",
          "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.",
          frm=["logarithms-and-exponentials"]),
  ],
  page="rank-deficit",
  frm=["subspace-labels","frames","bank-exchange-network","recurrences-and-divide-and-conquer-analysis","geometric-series"],
  salient="The relative deficit is only about $1.5\\times10^{-11}$, yet any strict inequality $s<Wm$ already yields a power saving $e^\\tau$ with $\\tau<1$.")

interchange = show("S1.3",
  "Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$.",
  "run the bit network on role streams with address-shear frames, implementing each edge by as many smaller interchanges as its rational rank, recurse on power widths, then remove width and row restrictions by padding",
  M("Interchanging growing fields costs a full scan per digit; the network turns one interchange of width $mf$ into $s<Wm$ interchanges of width $f$ on streams of volume $V/W$, which gives a power saving.",
    "explicit", "Because the sum of these ranks is less than the number of wires times"),
  [
    infer("S1.3.1", "Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with invertible lower triangular $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones.",
          "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization", page="lower-triangular-factorization",
          frm=["linear-algebra","special-matrices","matrix-inverse-transpose-and-identity"]),
    infer("S1.3.2", "The shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ needs exactly $a=\\operatorname{rank}A$ interchanges of $b$-digit fields plus $O(V)$ work.",
          "can be performed with exactly $a$ interchanges of pairs of $b$-digit", page="address-shear",
          frm=["lower-triangular-factorization","controlled-shifts","modular-arithmetic","prime-numbers"]),
    show("S1.3.3", "For widths $e=m^k$ with enough rows, the interchange costs $O(Ve^\\tau)$.",
         "split rows into role streams, apply the bit network with frames $\\Phi_{M_v}$ so that every role undergoes $H\\gets H+D$, complete the interchange with two linear updates, and solve the resulting recurrence",
         M("The frame identity makes the endpoint shear identical on every role, while each edge costs only its rank in smaller calls on a stream of volume $V/W$.", "recoverable"),
         [
           infer("S1.3.3.1", "Rows are distributed cyclically among the $W$ roles, so each role stream has the same shape and volume $V/W$.",
                 "Split whole rows cyclically into $W$ role streams within each prefix", page="role-streams",
                 frm=["elementary-stream-ops","array-layout","stack"]),
           infer("S1.3.3.2", "Running the network with shear frames yields $H\\gets H+D$ on every original row, including rows used as scratch.",
                 "is $H\\leftarrow H+D$ on every original row, including rows assigned",
                 frm=["frames","rank-deficit","address-shear"]),
           infer("S1.3.3.3", "The updates $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ send $(H,D)$ to $(D,H)$.",
                 "sends $(H,D)$ to $(D,H)$.", frm=["controlled-shifts"]),
           infer("S1.3.3.4", "The normalized cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$, hence $F_k=O(e^\\tau)$.",
                 "Hence $F_k=O(e^\\tau)$.", frm=["rank-deficit","recurrences-and-divide-and-conquer-analysis","geometric-series"]),
         ]),
    infer("S1.3.4", "Using high digits as rows, padding, a base-$m$ split of the width and padding binary chunks to radix $q$ gives $O(Vu^\\tau)$ for every width $u$.",
          "Since $e=O(u)$ for fixed $q$, the bound is", frm=["elementary-stream-ops"]),
  ],
  page="chunk-interchange",
  frm=["rank-deficit","role-streams","frames","address-shear","elementary-stream-ops","controlled-shifts"],
  salient="The final effect is an exact data-independent permutation, yet it is computed by forming XOR combinations of the data.")

layer = show("S1.4",
  "Applying $H_0$ on one selected bit in each of $D\\le d$ address chunks of a polynomial-record array costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, with error below $\\sqrt2\\,2^{-p}$.",
  "express $H_0^{\\otimes D}$ through $C^{\\otimes D}$, compute $C^{\\otimes e}$ by running the complex network with phase frames on role streams, implement binary basis changes by packed selected-bit additions, and bound the guard width",
  M("Separate butterfly factors would need $D$ whole-array passes; the network replaces a group of $e$ selected axes by $s<Wm$ children on $e/m$ axes at volume $V/W$.",
    "explicit", "We will obtain cost $O(Vd^{\\lambda'})$, with"),
  [
    infer("S1.4.1", "Each edge's phase-frame change is a product of one kernel $aI+bX_v$ per orthonormal residual basis vector, and the network yields $C^{\\otimes e}$ on every role from $s$ child calls on $e/m$ axes.",
          "Proposition~\\ref{prop:complex-motif-interface} gives the frame change", page="phase-frames",
          frm=["butterfly","bank-exchange-network","subspace-labels","frames","bilinear-form","tensor-product","complex-numbers"]),
    infer("S1.4.2", "$H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, so the $C$ layer gives the normalized butterfly layer after diagonal phases and a dyadic scale.",
          "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D", frm=["phase-frames","butterfly"]),
    infer("S1.4.3", "XORing corresponding selected bits of two chunks of width $L$ costs $O(V(L^\\tau+1))$ by eight cyclic shifts with guard values and a deterministic sort-based repair of the exceptional addresses.",
          "$O(V(L^\\tau+1))$, uniformly over the permitted lengths and payloads", page="packed-selected-bit",
          frm=["chunk-interchange","controlled-shifts","elementary-stream-ops","sorting-and-stable-radix-sort","bitwise-xor"]),
    infer("S1.4.4", "The normalized cost satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which unrolls to $O(d^{\\lambda'})$.",
          "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1)", frm=["role-streams","rank-deficit","recurrences-and-divide-and-conquer-analysis"]),
    infer("S1.4.5", "Intermediate dyadic values need $\\Delta=\\lceil C_0d^{C_1}\\rceil=o(p)$ extra bits, so all coefficients stay exact at width $O(p)$ until one final truncation.",
          "\\(\\Delta=o(p)\\), and the full coefficient width is \\(O(p)\\), as", frm=["disk-grid","fixed-point-binary-fractions"]),
  ],
  page="simultaneous-layer",
  frm=["phase-frames","packed-selected-bit","role-streams","disk-grid","butterfly","rank-deficit"])

procedures = show("S1",
  "Two tape procedures save a power of their parameter: chunk interchange in $O(Vu^\\tau)$ and a simultaneous butterfly layer in $O(Vd^{\\lambda'})$, with $\\tau,\\lambda'<1$.",
  "derive both from fixed linear networks with a rank deficit, transferred to arrays by frames on role streams and applied recursively",
  M("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both data movement and butterfly arithmetic must be cheaper than one scan per level.",
    "explicit", "We therefore need savings in both movement and arithmetic."),
  [tape_prims, networks, interchange, layer])

ringconv = show("S2",
  "Normalized cyclic convolution $\\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes has error below $\\sqrt2M(3\\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "compute two forward synthetic transforms, multiply records pointwise in their retained stored order with signed packing, and apply the opposite transform to that order",
  M("Pointwise multiplication commutes with the common record permutation of both forward outputs, so the bit-reversed and layout order never has to be undone before the opposite transform.",
    "explicit", "Pointwise multiplication commutes with applying the same record"),
  [
    infer("S2.1", "Radix-two butterflies and monomial twiddles compute $B_tF_t^-$, storing frequency $j$ at the bit-reversed slot, and the reversed procedure computes $F_t^+B_t^{-1}$.",
          "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.", page="synthetic-transform",
          frm=["polynomial-ring","dft","butterfly","fast-fourier-transform","permutations"]),
    infer("S2.2", "With a layout placing selected bits at common offsets in consecutive $K$-bit chunks, each multidimensional synthetic transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\ell 2^{-p}$.",
          "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right)", page="synthetic-layout",
          frm=["synthetic-transform","multidim-dft","simultaneous-layer","chunk-interchange","elementary-stream-ops","contraction-error"]),
    infer("S2.3", "Each normalized ring product $Q_p(fg/r)$ is computed exactly by signed Kronecker packing and four calls to the $O(N\\log N)$ multiplier in $O(rp\\log(rp))$ time.",
          "$O(rp\\log(rp))$ on a fixed number of tapes.", page="signed-packing",
          frm=["hvdh-multiplier","polynomial-ring","disk-grid","two-s-complement-and-signed-integer-representation"]),
    infer("S2.4", "Errors add through the contractions, giving total error below $M(3\\delta+\\eta)=\\sqrt2M(3\\ell+1)2^{-p}$.",
          "$M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$, as claimed.", frm=["contraction-error"]),
  ],
  page="ring-convolution",
  frm=["synthetic-layout","signed-packing","synthetic-transform","cyclic-convolution","contraction-error"])

resamp = show("S3",
  "With $R=\\bigotimes_iP_{s_i}$ and $Q=\\bigotimes_iP_{t_i}$, $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ for contractions $\\mathcal A,\\mathcal B_0$ computable linewise with error below $dp^2$, the permutations never being executed as sorts.",
  "keep the source and target permutations inside Harvey and van der Hoeven's one-dimensional Gaussian identity, then tensor it over the axes using chunk interchanges to expose each axis",
  M("Gaussian resampling's usual implementation sorts twice on each coordinate; retaining the permutations in the formula avoids those full sorts.",
    "explicit", "Its usual implementation sorts twice on each"),
  [
    infer("S3.1", "For coprime $s<t$ with enough separation, $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with linear contractions $A,B_0$ approximable in $O(tp^{3/2+\\delta}\\alpha)$ time.",
          "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.", frm=["gaussian-resampling","dft","permutations"]),
    infer("S3.2", "Tensoring gives the multidimensional identity; applying the maps one exposed axis at a time costs $O(dTp^{3/2+\\delta}\\alpha)$ plus $O(Tp\\,d^2(1+\\ell^\\tau))$ for axis movement.",
          "Tensoring \\eqref{eq:no-sort-one-dimensional} proves", frm=["tensor-product","multidim-dft","chunk-interchange"]),
  ],
  page="resampling-retained-permutations",
  frm=["gaussian-resampling","multidim-dft","chunk-interchange","contraction-error"])

root_children = [
  procedures, ringconv, resamp,
  infer("S4", "With chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, $QF_{\\boldsymbol t}u=\\overline a\\cdot\\frac{a*(\\overline a\\cdot u)}{T}$, so the middle transform with its target permutation is a normalized cyclic convolution.",
        "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because", page="chirp-identity",
        frm=["cyclic-convolution","multidim-dft","complex-numbers"]),
  infer("S5", "The retained source permutation cancels: $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
        "Each $t_i$ is a unit modulo $s_i$, so tensoring this identity gives", page="permutation-cancellation",
        frm=["multidim-dft","cyclic-convolution","permutations","modular-arithmetic"]),
  infer("S6", "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist, give $T/2<S<T$, and satisfy the resampling separation $\\alpha^4\\theta_i>p$.",
        "We may therefore choose distinct odd primes satisfying", page="prime-lengths",
        frm=["prime-numbers","resampling-retained-permutations","gaussian-resampling"]),
  infer("S7", "Splitting the inputs into $q=\\lceil n/b\\rceil$ digits base $2^b$ gives a product of degree below $S$, so convolution modulo $x^S-1$ has no wraparound and coefficients are below $2^{3b}$.",
        "Thus convolution modulo $x^S-1$ has no nonzero wraparound.", page="radix-digit-reduction",
        frm=["binary-and-radix-representation","cyclic-convolution","schoolbook-addition-and-multiplication-with-carries"]),
  infer("S8", "The map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism onto convolution on axes of lengths $s_i$, implemented by triangular controlled shifts and axis moves in $O(Tp\\,d^2(1+\\ell^\\tau))$ time.",
        "Hence\n$\\Phi$ is an isomorphism and preserves cyclic convolution.", page="crt-address-map",
        frm=["chinese-remainder-theorem","controlled-shifts","chunk-interchange","cyclic-convolution","greatest-common-divisor-and-coprimality"]),
  infer("S9", "Multiplying coefficient $k$ by $\\zeta^k$, $\\zeta=e^{\\pi i/r}$, turns cyclic convolution in the last axis into multiplication modulo $y^r+1$, so $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
        "Untwisting therefore recovers the cyclic coefficient with the correct", page="coefficient-twist",
        frm=["polynomial-ring","cyclic-convolution","complex-numbers"]),
  infer("S10", "Through the source transforms, pointwise product and opposite transform, the final coefficient error is below $448b\\,2^{-3b/4}<1/2$, so rounding and radix carry propagation give the exact product.",
        "The strict error below $1/2$ makes the nearest integer to", page="exact-recovery",
        frm=["contraction-error","radix-digit-reduction","schoolbook-addition-and-multiplication-with-carries","sup-norm-and-the-triangle-inequality"]),
  infer("S11", "With $\\tau=1-2^{-50}$, $\\lambda'=1-2^{-54}$, $c=2^{-56}$, $\\epsilon=2^{-75}$, every row of the normalized cost table is at most $p^{1-2\\kappa}$, since the smallest margin is $2^{-181}=2\\kappa$.",
        "Thus $\\min_i g_i=2^{-181}=2\\kappa$.", page="parameter-choice",
        frm=["chunk-interchange","simultaneous-layer","synthetic-layout","resampling-retained-permutations","rank-deficit","asymptotic-notation-beyond-big-o"]),
]

root = show("S0",
  "One deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
  "reduce the product to a cyclic convolution of radix digits, move it by a Chinese-remainder map and Gaussian resampling to power-of-two axes, compute that convolution with synthetic polynomial transforms accelerated by two network-based tape procedures, recover the exact coefficients by rounding, and bound every cost term",
  M("The Harvey and van der Hoeven route already reaches $O(n\\log n)$; its remaining cost is a full scan per transform level for both address rearrangement and butterflies, so a power saving in those two tape operations lowers the whole bound.",
    "explicit", "The algorithm\nuses linear combinations of intermediate data to reduce the cost of\nboth address rearrangement and Fourier-transform layers."),
  root_children,
  page="main-theorem",
  frm=["nlogn-conjecture","hvdh-multiplier","multitape-turing-machine","deterministic-algorithm","worst-case-running-time","big-o-notation","logarithms-and-exponentials"],
  salient="The saving is a strict power of the logarithm, $(\\lg n)^{-\\kappa}$, but with a minute exponent $\\kappa=2^{-182}$, enough to refute the $n\\log n$ conjecture in this model.",
  adds=[
    B("n","input length","The number of bits in each of the two input integers.","count"),
    B("V","logical volume","The number of stored data bits of the array a tape procedure acts on.","count"),
    B("W","wire count","The number of wires (roles) in a fixed finite network.","count"),
    B("m","label dimension","The dimension of the fixed tensor label space, and the factor by which the recursion parameter grows per level.","count"),
    B("s","smaller calls","The number of smaller recursive calls one network invocation needs, the sum of its edge ranks or residual dimensions.","count"),
    B("p","working precision","The number of fractional bits of the fixed-point grid used for complex coefficients.","count"),
    B("d","axis count","The number of axes of the multidimensional transforms, of order $p^\\epsilon$.","count"),
    B("r","record length","The number of complex coefficients in each polynomial record modulo $y^r+1$.","count"),
    B("T","padded box size","The number of entries of the padded power-of-two box, the product of the axis lengths $t_i$.","count"),
    B("\\tau","interchange exponent","The fixed exponent $1-2^{-50}$ below one in the chunk-interchange bound.","direct"),
  ])

json.dump({"root": root}, open('/home/user/openai-nlogn-wiki/runs/O1/exegenius/tasks/0003-argument.answer.json','w'), indent=1, ensure_ascii=False)
# order check
pos=[]
def walk(n):
    if n["intention"]=="infer": pos.append((n["id"], SRC.find(n["quote"]["quote"])))
    for c in n.get("children",[]): walk(c)
walk(root)
prev=-1
for i,p in pos:
    flag = "" if p>prev else "  <-- OUT OF ORDER"
    print(i,p,flag); prev=max(prev,p)
