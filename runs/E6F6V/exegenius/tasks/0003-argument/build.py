import json, sys
P='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6V/'
SRC=open(P+'sources/paper.tex').read()

def inf(id, claim, quote, page=None, frm=None, salient=None, deferred=False):
    n={"id":id,"intention":"infer","claim":claim,"quote":{"source":"paper","quote":quote}}
    if page: n["page"]=page
    if frm: n["from"]=frm
    if salient: n["salient"]=salient
    if deferred: n["deferred"]=True
    return n

def show(id, claim, method, mot, children, page=None, frm=None, salient=None, adds=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":mot,"children":children}
    if page: n["page"]=page
    if frm: n["from"]=frm
    if salient: n["salient"]=salient
    if adds: n["adds"]=adds
    return n

def expl(text, quote): return {"text":text,"source":"explicit","quote":{"source":"paper","quote":quote}}
def reco(text): return {"text":text,"source":"recoverable"}
def reconst(text): return {"text":text,"source":"reconstructed"}
def b(sym,name,meaning,rel="direct"): return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}

# ---------- A: tape procedures ----------
A1=inf("A1","Streams, digit moves, splits and merges, and row splits of an array of volume $V$ each cost $O(V)$ on a fixed number of tapes.",
 "takes $O(V)$ steps on a fixed number of one-dimensional tapes:", page="multitape-streams",
 frm=["turing-machines","big-o","binary-representation-bit-strings-and-xor","cartesian-products-and-lexicographic-order"])
A2=inf("A2","Updating a target address field by an offset computed from earlier control fields, or multiplying it by a fixed rational unit modulo $q^b$, costs $O(V)$.",
 "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the", page="controlled-shifts",
 frm=["multitape-streams","modular-arithmetic-and-congruences","euclidean-algorithm-and-modular-inverses","primes-coprimality-and-gcd"])

A31=inf("A3.1","A fixed linear network of gates on wires, run with its scratch wires holding arbitrary values, exchanges the banks $X,Y$ up to sign and restores every scratch wire.",
 "Thus both net maps are $y\\gets y+x$.", page="bank-exchange-network",
 frm=["binary-representation-bit-strings-and-xor"],
 salient="The exchange works for arbitrary initial scratch values: the first two schedule rows subtract the effect of the old scratch values, so the net map does not depend on them.")
A32=inf("A3.2","If every vertex of the network gets an invertible frame on its array and gates act pointwise, the network implements $D_{\\mathrm{out}}\\mathsf S D_{\\mathrm{in}}^{-1}$, and each edge only changes frame.",
 " D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}.", page="frames-on-arrays",
 frm=["bank-exchange-network","linear-algebra-spaces","matrices-invertibility-and-rank","permutations-and-bijections"])
A33=show("A3.3","Nested nondegenerate subspace labels on gates and terminals make adjacent labels comparable, so the dimension lost on decreasing edges is less than $N/2$.",
 "attach labels built from three-element subsets and bound the orthogonal residual of every edge",
 reco("Each edge's cost will be the dimension of the orthogonal residual between its two labels, so one must choose labels whose residuals are small in total; three-element subsets give orthogonal neighbours and cancellations."),
 [inf("A3.3a","Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
      "Every edge joins comparable nondegenerate labels.  The only decreasing"),
  inf("A3.3b","The relative loss on decreasing edges is below one half of the bank volume, which leaves a strict saving.",
      "In particular, both are smaller than $1/2$.")],
 page="subspace-labels", frm=["bank-exchange-network","frames-on-arrays","linear-algebra-spaces","vector-spaces-bases-and-dimension"])
A34=show("A3.4","With frames $\\Phi_M$ moving the entry at $(H,D)$ to $(H+MD,D)$, the bit network turns the exchange into the shear $H\\gets H+D$ on every role at total edge rank $s_{\\rm b}<W_{\\rm b}m$.",
 "choose the rational matrix of each vertex as a projection onto its label and sum the ranks of the edge differences",
 reco("Frames that are address permutations commute with pointwise XOR gates, and a projection difference has rank equal to the dimension change, so the rank sum is controlled by the label dimensions."),
 [inf("A3.4a","The matrices at the endpoints of every route differ by the identity, so each role receives the same shear.",
      "Its rational matrices are common to all incidences of a gate and obey"),
  inf("A3.4b","The sum of the ranks of all edge differences is $s_{\\rm b}$, strictly less than $W_{\\rm b}m$.",
      "=177176569088785861287000000<W_{\\rm b}m."),
  inf("A3.4c","Hence $s_{\\rm b}/W_{\\rm b}<m^{\\tau}$ for the fixed rational exponent $\\tau=1-2^{-50}$.",
      "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,")],
 page="bit-shear-interface", frm=["subspace-labels","frames-on-arrays","modular-arithmetic-and-congruences","rational-numbers-and-dyadic-fractions"],
 salient="The same shear $H\\gets H+D$ appears on every role, including the scratch roles with arbitrary contents, even though the labels along the routes differ.")
A35=inf("A3.5","Every $m\\times m$ rational matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
 "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization", page="lower-triangular-factorization",
 frm=["linear-algebra-spaces","gaussian-elimination","matrices-invertibility-and-rank"])
A36=inf("A3.6","The address map $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ with $A$ of rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
 "can be performed with exactly $a$ interchanges of pairs of $b$-digit", page="matrix-shear-cost",
 frm=["lower-triangular-factorization","controlled-shifts","modular-arithmetic-and-congruences","trial-division-and-primality-search"])

K=show("A3.7.3","Each call at width $e=mf$ makes $s$ calls at width $f$ on streams of volume $V/W$, so the normalized cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$ and with $s/W<m^\\tau$ it is $O(e^\\tau)$.",
 "set up the recurrence for time divided by volume and sum its geometric series",
 expl("The strict inequality s/W < m (more precisely s/W < m^tau) is what turns a linear-in-width cost into a power saving.","is the source of the power saving."),
 [inf("A3.7.3a","One call at the node uses exactly $s$ smaller interchanges, one per unit of edge rank.",
      "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  inf("A3.7.3b","Each smaller call acts on one role stream, so its volume is $V/W$.",
      "Each acts on one role stream of volume $V/W$, retaining all other"),
  inf("A3.7.3c","Normalized by volume, the cost obeys $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
      " F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."),
  show("A3.7.3d","Because $s/W<m^\\tau$, the unrolled sum is $O(m^{k\\tau})$ and so $F_k=O(e^\\tau)$.",
       "unroll the recurrence into a geometric sum and bound it by its largest term",
       reco("The recurrence has the form F_k <= a F_{k-1} + O(1), so F_k is bounded by a sum of powers of a = s/W, and the sum is dominated by its largest term."),
       [inf("A3.7.3d1","The sum is at most $k+1$ when $a\\le1$ and $O(a^k)$ when $a>1$, and in both cases $O(m^{k\\tau})$.",
            "most $k+1=O(m^{k\\tau})$; if $a>1$, it is $O(a^k)$."),
        inf("A3.7.3d2","Since $m^k=e$, the normalized cost is $F_k=O(e^\\tau)$ with $\\tau<1$.",
            "Hence $F_k=O(e^\\tau)$.")])],
 page="recursive-power-saving", frm=["subspace-labels","recurrences-and-induction","big-o","logarithms-floor-and-ceiling"],
 salient="The growth factor per level, $s/W$, is strictly smaller than the factor $m$ by which the width grows, so the cost per bit grows like $e^\\tau$ with $\\tau<1$ instead of linearly in $e$; this holds because the total edge rank $s$ is below $Wm$.")
A37=show("A3.7","Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\\tau)$ time by running the bit network on $W$ role streams with each shear edge done by smaller interchanges.",
 "split rows into role streams, use the network to shear, recurse on edges, then finish with two linear updates",
 reco("The shear H<-H+D is available from the network, and an interchange is three shears; the recursion is hidden in the edges, so the cost is governed by the edge rank sum."),
 [inf("A3.7.1","Running the frames $\\Phi_M$ through the network on the $W$ role streams yields $H\\gets H+D$ on every original row.",
      "is $H\\leftarrow H+D$ on every original row, including rows assigned"),
  inf("A3.7.2","Two updates of the later group that cost linear time complete the interchange of $H$ and $D$.",
      " D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,"),
  K],
 page="power-width-interchange", frm=["bit-shear-interface","matrix-shear-cost","recursive-power-saving","multitape-streams"],
 adds=[b("e","chunk width","the number of radix digits in each of the two interchanged chunks, a power of $m$","count")])
A38=inf("A3.8","Padding and a base-$m$ decomposition extend this to any widths: two address fields of $u$ bits are interchanged in $O(Vu^\\tau)$ time.",
 "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.", frm=["logarithms-floor-and-ceiling","radix-representation-and-carry-propagation"])
A3=show("A3","Two disjoint address fields of $u$ bits in an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, although the intermediate steps XOR data together.",
 "build a fixed linear network with a rank deficit $s<Wm$, turn its edges into shears of address fields, and recurse",
 expl("The rank deficit of the network gives a recurrence whose per-level growth is below the width growth.","$m$, the resulting recurrence saves a power of the chunk width."),
 [A31,A32,A33,A34,A35,A36,A37,A38],
 page="chunk-interchange", frm=["multitape-streams","controlled-shifts","binary-representation-bit-strings-and-xor","permutations-and-bijections"],
 adds=[b("u","chunk width in bits","the number of bits in each of the two interchanged address fields","count"),
       b("\\tau","interchange exponent","a fixed rational exponent below $1$ in the cost $O(Vu^\\tau)$"),
       b("m","label dimension","the dimension of the fixed label space, and the factor by which the recursive width grows","count"),
       b("W","wire count","the number of wires of the bit network, each carrying one role stream","count"),
       b("s","call count","the total rank of the edge differences, i.e. the number of smaller interchanges one node uses","count")],
 salient="The exponent is strictly below one although each level does work proportional to the whole volume, because the smaller calls together touch only a fraction $s/W<m^\\tau$ of what a width-$m$ increase would suggest.")

# A4: butterfly layers
p1=show("A4.1","On selected bits, $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$ with $C=aI+bX$, and each edge of the complex network is a product of translation kernels, one per residual basis vector.",
 "express the butterfly through the two-point kernel $C$ and phase frames of binary labels",
 reco("The kernel C is a product of Hadamards and a phase, so frames diagonalized by Hadamards turn into products of translations, which the recursive network can apply on smaller groups."),
 [inf("A4.1a","The total number of residual basis vectors over all edges is $s_{\\rm c}<W_{\\rm c}m$.",
      " s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}", deferred=True),
  inf("A4.1b","The normalized butterfly layer on $D$ selected bits equals phase-conjugated $C^{\\otimes D}$ up to a scalar.",
      " H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.")],
 page="phase-frames", frm=["subspace-labels","frames-on-arrays","complex-numbers","gaussian-elimination","matrices-invertibility-and-rank"])
p2=inf("A4.2","Adding (XOR) selected bits of one address chunk into another is done by a constant number of cyclic shifts of whole chunk ranges plus deterministic repair of a small exceptional set of addresses.",
 "At the selected positions $j_i=\\rho+iK$, numbered from the least", page="packed-selected-bit-addition",
 frm=["chunk-interchange","controlled-shifts","binary-representation-bit-strings-and-xor"])
p3=show("A4.3","Unrolling the recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ gives total cost $O(Vd^{\\lambda'})$ for $d$ axes, with $\\lambda'<1$.",
 "set up the recurrence for time divided by volume, now with $s=s_{\\rm c}$ children, and sum it",
 reco("The same rank deficit s<Wm as for address interchange makes each level's normalized cost grow by a factor below m."),
 [inf("A4.3a","Each node makes $s$ calls on slots of $e/m$ chunks and volume $V/W$.",
      " F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
  inf("A4.3b","Summing over levels and base-$m$ pieces gives $O(d^{\\lambda'})$ for a fixed $\\lambda'<1$.",
      "=O(d^{\\lambda'})")],
 frm=["recursive-power-saving"])
p4=inf("A4.4","Intermediate values are exact Gaussian dyadics whose denominators and magnitudes grow by $o(p)$ guard bits, so one truncation follows the completed layer.",
 "\\(\\Delta=o(p)\\), and the full coefficient width is \\(O(p)\\), as", page="guard-bits",
 frm=["fixed-point-precision","phase-frames","rational-numbers-and-dyadic-fractions"])
p5=inf("A4.5","The simultaneous normalized layer returns $Q_p(\\mathcal H z)$ with error below $\\sqrt2\\,2^{-p}$ in time $O(Vd^{\\lambda'})$.",
 "coefficient order, and component format in $O(Vd^{\\lambda'})$ time,", frm=["fixed-point-precision"])
A4=show("A4","The two-point butterfly $H_0$ is applied to the same bit position of $d$ address chunks at once, on polynomial records, in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$ instead of $d$ whole-array passes.",
 "build the layer from the kernel $C$ by the same rank-deficit recursion, with packed bit changes and guard bits",
 expl("Separate butterfly factors would need D whole-array passes; the recursion gets a power saving in d.","$\\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly"),
 [p1,p2,p3,p4,p5],
 page="simultaneous-butterfly-layer", frm=["phase-frames","packed-selected-bit-addition","guard-bits","recursive-power-saving","radix-two-fft","fixed-point-precision","chunk-interchange"],
 adds=[b("d","axis count","the number of address chunks (transform axes) on which the layer acts at once","count"),
       b("\\lambda'","layer exponent","a fixed rational exponent below $1$ in the layer cost $O(Vd^{\\lambda'})$")])

A=show("A","Two fast tape procedures exist: exact interchange of address fields and simultaneous butterfly layers, both with a power saving in the logarithmic factor.",
 "obtain each procedure from a fixed linear network whose total edge rank is below the number of wires times the dimension",
 expl("Scanning the array once per transform level already costs n log n, so both movement and arithmetic must be sped up.","We therefore need savings in both movement and arithmetic."),
 [A1,A2,A3,A4])

# ---------- B ----------
B1=show("B1","Synthetic transforms over $\\mathbb C[y]/(y^r+1)$ use $\\omega_t=y^{2r/t}$, so twiddles are signed coefficient shifts; the forward and opposite versions invert each other up to $1/t$ in stored order.",
 "use powers of $y$ as roots of unity and run the radix-two decimation recursion",
 reco("Multiplying by a power of y only permutes and negates coefficients, so the usual twiddle multiplications cost a linear scan rather than a full multiplication."),
 [inf("B1a","Multiplication by $y^a$ permutes coefficients up to sign and is an isometry.",
      "by $y^a$, for any integer $a$, permutes the coefficients and changes"),
  inf("B1b","Character cancellation gives $F_t^+F_t^-=t^{-1}I$.",
      "F_t^+F_t^-=t^{-1}I."),
  inf("B1c","The procedures that write and consume the bit-reversed order implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
      " B_tF_t^-,\\qquad F_t^+B_t^{-1},")],
 page="synthetic-transforms", frm=["negacyclic-ring","radix-two-fft","euler-s-formula-and-roots-of-unity"])
B2=inf("B2","A positional address layout places the selected bits of all axes at a common offset in consecutive $K$-bit chunks so each round is one simultaneous layer; the transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
 "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right).", page="synthetic-transform-layout",
 frm=["synthetic-transforms","simultaneous-butterfly-layer","chunk-interchange"])
B3=inf("B3","Products of ring polynomials are computed exactly by signed Kronecker substitution, using the established multiplier as a subroutine, in time $O(rp\\log(rp))$.",
 "numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time", page="signed-kronecker-packing",
 frm=["negacyclic-ring","hvdh-multiplier","fixed-point-precision","radix-representation-and-carry-propagation"])
B4=inf("B4","Convolution over the ring is computed by transforming both operands, multiplying pointwise in the retained stored order, and applying the opposite transform, with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
 "Perform both forward transforms and retain their common $LB$ order.", page="synthetic-convolution",
 frm=["synthetic-transform-layout","signed-kronecker-packing","discrete-fourier-transform"])
B=show("B","Convolution over the polynomial ring $\\mathbb C[y]/(y^r+1)$ on several axes runs in time dominated by simultaneous layers and chunk interchanges.",
 "evaluate the convolution by synthetic transforms laid out on tape so that each round is one simultaneous layer",
 reco("Convolution becomes pointwise multiplication after a transform, and the synthetic transform has only butterflies, signed shifts and address moves, which are exactly the operations the two tape procedures accelerate."),
 [B1,B2,B3,B4])

# ---------- C ----------
C1=inf("C1","Gaussian resampling rewrites the prime-length transform as $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with contractions $A,B_0$ and power-of-two length $t$, keeping both permutations inside the transform.",
 "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.", page="gaussian-resampling",
 frm=["discrete-fourier-transform","fixed-point-precision","rounding-and-square-roots","norms-absolute-value-and-triangle-inequality"])
C2=inf("C2","Applying the one-dimensional maps line by line along each of $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ on the padded box, exposing each axis with chunk interchanges.",
 "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,", page="tensor-resampling",
 frm=["gaussian-resampling","chunk-interchange"])
C3=inf("C3","Bluestein's chirp identity writes $QF_{\\boldsymbol t}$ as chirp multiplication, a cyclic convolution with the chirp array, and chirp multiplication again, so $Q$ is never executed.",
 " \\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}.", page="bluestein-chirp",
 frm=["discrete-fourier-transform","convolution-multiplication","gaussian-resampling"])
C4=inf("C4","Because a permutation commutes with pointwise products, applying $RF_{\\boldsymbol s}$ to both operands and $RF_{\\boldsymbol s}^+$ to their product gives $(u*v)/S^2$ without undoing $R$.",
 "=\\frac{u*v}{S^2}.", page="permutation-cancellation",
 frm=["gaussian-resampling","discrete-fourier-transform","permutations-and-bijections"])
C=show("C","The transforms on prime-length axes needed for the digit convolution reduce to power-of-two tensor transforms plus a convolution, with no full sorts.",
 "use Gaussian resampling with the two coordinate permutations left inside the identity, and absorb the middle permutation into a chirp convolution",
 expl("The usual implementation of Gaussian resampling sorts twice on each coordinate; retaining both permutations in the formula avoids those sorts.","We retain both permutations in the transform formula and"),
 [C1,C2,C3,C4])

# ---------- D ----------
D1=show("D1","Sizes are $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T$ near $4n/b$ split into $d$ axis lengths $r/2$ or $r$, and distinct odd primes $s_i$ just below $t_i$ with $T/2<S<T$.",
 "fix rational exponents first, then derive all sizes and find the primes by prime-interval estimates",
 reconst("The reduction needs many exponents to satisfy several inequalities at once, and the primes must be close to the powers of two for resampling to work, so they are fixed together at the start."),
 [inf("D1a","The exponents are fixed rationals, including $\\kappa=2^{-182}$.",
      " C_1=20,\\qquad \\epsilon=2^{-75},\\qquad \\kappa=2^{-182}."),
  inf("D1b","The sizes $b,p,d,K,T,r$ are defined from $n$.",
      " b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
  inf("D1c","The primes satisfy $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, pairwise coprime, and $T/2<S<T$.",
      "Together with $s_i<t_i$, this gives $T/2<S<T$.")],
 page="parameter-choice", frm=["crt-cyclic-convolution","gaussian-resampling","synthetic-transform-layout","primes-coprimality-and-gcd","trial-division-and-primality-search","logarithms-floor-and-ceiling"])
D2=inf("D2","The map $x\\mapsto\\prod_i x_i^{\\mu_i}$ is an algebra isomorphism that turns one cyclic convolution of length $S$ into a convolution over the pairwise coprime axes, implemented by triangular controlled shifts.",
 "$\\Phi$ is an isomorphism and preserves cyclic convolution.", page="crt-cyclic-convolution",
 frm=["convolution-multiplication","controlled-shifts","chunk-interchange","modular-arithmetic-and-congruences","primes-coprimality-and-gcd"])
D3=inf("D3","Multiplying coefficient $k$ of the last cyclic coordinate by $\\zeta^k$ maps cyclic convolution of length $r$ to the ring modulo $y^r+1$, so the ring convolution computes complex cyclic convolution.",
 "Untwisting therefore recovers the cyclic coefficient with the correct", page="coefficient-twist",
 frm=["negacyclic-ring","synthetic-convolution","convolution-multiplication","euler-s-formula-and-roots-of-unity"])
D4=inf("D4","The source transform is applied to both digit arrays.",
 "Compute $\\widetilde{\\mathscr F}(u)$ and")
D5=inf("D5","Multiply pointwise, apply the opposite transform, and undo the scales: the two factors $S$ and $2^{2b+4}$ restore the integer digit convolution.",
 "The two occurrences of $S$ in this algorithm undo different")
D=show("D","Multiplication: split into radix digits, map by the CRT address map, apply the source transform to both operands, multiply pointwise, apply the opposite transform, undo scales, round and propagate carries.",
 "choose parameters, place the digit list on distinct prime cyclic axes, then run resampling, chirp convolution and its inverse",
 reco("Integer multiplication is a convolution of digits; a transform diagonalizes convolution, and the resampled power-of-two form is what the fast tape procedures can evaluate."),
 [D1,D2,D3,D4,D5],
 page="multiplication-algorithm", frm=["parameter-choice","crt-cyclic-convolution","tensor-resampling","bluestein-chirp","permutation-cancellation","coefficient-twist","convolution-multiplication"])

# ---------- E ----------
E=show("E","Every intermediate array stays in the unit disk, accumulated errors stay below $1/2$ per coefficient, so rounding returns the exact integer coefficients and carry propagation gives the $2n$-bit product.",
 "propagate disk norms and errors through each computed step, then round and carry",
 reco("The algorithm computes approximations, so exactness needs an explicit error bound smaller than one half after all scalings."),
 [inf("E1","Each computed array has bounded norm, so every call is legal and the first scaled result lies in the disk.",
      "This proves the disk bound for the computed first scaled result."),
  inf("E2","The final absolute error is below $1/2$.",
      "<448b\\,2^{-b+\\gamma}"),
  inf("E3","The nearest integer is therefore the unique correct coefficient.",
      "that value the unique correct coefficient."),
  inf("E4","Carry propagation yields exactly $2n$ output bits.",
      "The exact product is less")],
 page="exact-recovery", frm=["multiplication-algorithm","fixed-point-precision","norms-absolute-value-and-triangle-inequality","rounding-and-square-roots","radix-representation-and-carry-propagation"])

# ---------- F ----------
F=show("F","Dividing each phase's cost by $Tp=\\Theta(n)$ gives seven dominant powers of $p$, each at most $1-2\\kappa$, so the total is $O(n(\\log n)^{1-\\kappa})$.",
 "tabulate normalized costs and compare their exponents with $1-2\\kappa$",
 reco("The exponents were fixed rationals, so a finite list of explicit margins below one shows that a power of log n is saved."),
 [inf("F1","The dominant costs are seven powers of $p$ with margins $g_1,\\dots,g_7$ below one.",
      "The seven dominant powers in Table~\\ref{tab:costs} have the following"),
  inf("F2","The smallest margin is $2^{-181}=2\\kappa$.",
      "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
  inf("F3","The chunk exchanges for the layout cost $O(pK^{\\tau-1})$ normalized, from $O(p/K)$ exchanges of width $K$.",
      " O(p/K)\\,K^\\tau=O(pK^{\\tau-1})."),
  inf("F4","Each of the seven powers is at most $1-2\\kappa$, and powers of $\\log p$ are absorbed.",
      "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
  inf("F5","The complete bound is $O(n(\\log n)^{1-\\kappa})$ for $\\kappa=2^{-182}$.",
      " O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).")],
 page="time-bound-accounting", frm=["multiplication-algorithm","chunk-interchange","simultaneous-butterfly-layer","tensor-resampling","signed-kronecker-packing"],
 salient="$\\kappa=2^{-182}$ is half of the smallest of the seven margins, $2^{-181}$, which comes from the chunk-exchange row ($g_2=\\epsilon c(1-\\tau)$): the exponent is limited by how little the interchange saves.")

root=show("R","A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "put fast address interchange and simultaneous butterfly layers inside the Gaussian-resampling and synthetic-transform reduction of multiplication to convolution, then verify exactness and cost",
 expl("Scanning n bits at each of log n transform levels costs n log n already, so the savings must come in both data movement and arithmetic.","We therefore need savings in both movement and arithmetic."),
 [A,B,C,D,E,F],
 page="multiplication-below-nlogn", frm=["multiplication-algorithm","exact-recovery","time-bound-accounting","hvdh-multiplier","big-o","turing-machines"],
 adds=[b("n","input length","the number of bits of each factor","count"),
       b("\\kappa","saving exponent","the fixed constant $2^{-182}$ by which the power of the logarithm is lowered")])
json.dump({"root":root}, open(P+'exegenius/tasks/0003-argument.answer.json','w'), indent=1)

# check quotes order
def walk(n, out):
    if n["intention"]=="infer": out.append(n)
    for c in n.get("children",[]): walk(c,out)
out=[]; walk(root,out)
prev=-1; bad=0
for n in out:
    q=n["quote"]["quote"]
    i=SRC.find(q)
    if i<0: print("MISSING",n["id"],repr(q)); bad+=1; continue
    if n.get("deferred"): continue
    if i<prev: print("ORDER",n["id"],i,prev); bad+=1
    prev=max(prev,i) if i>=prev else prev
    # uniqueness
    if SRC.count(q)>1: print("multi",n["id"],SRC.count(q))
# motivation quotes
def walk2(n):
    m=n.get("motivation")
    if m and m.get("quote") and SRC.find(m["quote"]["quote"])<0: print("MOTMISS",n["id"],m["quote"]["quote"])
    for c in n.get("children",[]): walk2(c)
walk2(root)
print("bad",bad)
