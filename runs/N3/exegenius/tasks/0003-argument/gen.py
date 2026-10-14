import json, sys
base = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N3/'
src = open(base+'sources/paper.tex').read()

def ev(q): return {"source": "paper", "quote": q}
def inf(id, claim, q, page=None, frm=(), salient=None, deferred=False):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(q), "page": page, "from": list(frm)}
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n
def show(id, claim, method, mot, children, page=None, frm=(), salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": mot,
         "children": children, "page": page, "from": list(frm)}
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n
def mot(text, source, q=None):
    m = {"text": text, "source": source}
    if q: m["quote"] = ev(q)
    return m
def b(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

networks = show("S1.3",
 "Two fixed linear networks with $W$ wires exchange two banks of values, restore every scratch value, and admit nested subspace labels whose total edge rank $s$ satisfies $s<Wm$.",
 "build a three-stage scalar bank exchange, verify that frames commute with pointwise gates, attach nested subspace labels from triple-intersection pairings, and read off the rational and binary interfaces",
 mot("The cost of every change of representation along an edge is counted by its label dimension change, so a small total dimension loss is exactly what makes the recursive calls fewer than the wires times m.", "explicit",
     "The saving will come from keeping the total dimension lost on decreasing"),
 [
  inf("S1.3.1", "Three stages of copy, gather, scatter and side-injection invocations send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ for arbitrary initial scratch values, restoring every auxiliary value.",
      "and restores every auxiliary value.  In the bit construction this is the", page="bank-exchange",
      frm=["linear-network","scratch-restoration","triple-intersection","exclusive-or-and-arithmetic-modulo-2"],
      salient="The net effect is independent of the arbitrary initial scratch values, which are all restored."),
  inf("S1.3.2", "If every vertex $v$ carries an invertible frame $D_v$, common to all incidences of a gate, the network on arrays implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so intermediate frames cancel.",
      "$c_j\\in R$.  Thus the common frame commutes with the pointwise gate, and", page="frames",
      frm=["linear-network","linear-algebra"]),
  inf("S1.3.3", "Every edge joins comparable nondegenerate labels in the $m$-dimensional space $F^{\\otimes3}$, the only decreasing edges are central-wire returns of loss $h$, and the total absolute dimension change is $Wm-2N+2L$ with $L<N/2$.",
      "edges are the central-wire edges from time 3 to time 4; their dimension", page="subspace-labels",
      frm=["bilinear-forms","triple-intersection","linear-algebra","bank-exchange"],
      salient="The total dimension change falls strictly short of $Wm$, since the loss ratio $L/N$ is $100/539$ or $101/539$, below $1/2$."),
  inf("S1.3.4", "With projection matrices $P_U$ as frames, the bit network routes every role through the endpoint shear $I_m$ while its edge differences have total rational rank $s_{\\rm b}<W_{\\rm b}m$.",
      "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,", page="rational-shear-interface",
      frm=["frames","subspace-labels","address-shear","bank-exchange","linear-algebra"]),
  inf("S1.3.5", "With binary phase frames $\\mathcal C_U$, each edge change is a product of one kernel $aI+bX_v$ per orthonormal residual vector, $s_{\\rm c}<W_{\\rm c}m$ in total, and the endpoints telescope to $C^{\\otimes m}$ on every role.",
      "After source and sink diagonal corrections, and undoing the signed", page="phase-frames",
      frm=["frames","subspace-labels","bank-exchange","hamming-weight","gaussian-dyadics","exclusive-or-and-arithmetic-modulo-2"]),
  inf("S1.3.6", "Both relative deficits exceed $20\\cdot2^{-50}$, so $s/W<m^\\tau$ with the fixed rational exponent $\\tau=1-2^{-50}$ for both networks.",
      "For both recurrences we may use the fixed rational exponent",
      frm=["logarithms-and-exponentials"]),
 ],
 frm=["linear-network","linear-algebra"],
 salient="The strict inequality $s<Wm$: fewer smaller calls than wires times the dimension.",
 adds=[b("W","wire count","The number of wires in the finite network, including scratch wires.","count"),
       b("m","label dimension","The dimension of the ambient label space, $h^3=10^6$.","count"),
       b("s","total edge rank","The total number of smaller calls, the sum over edges of label dimension changes or rational ranks.","count")])

interchange = show("S1.4",
 "Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$.",
 "factor each edge shear into lower triangular maps and $a$ smaller interchanges, run the bit network recursively on power widths with rows split among the $W$ roles, then remove the width and row restrictions",
 mot("An edge matrix of rank a costs a smaller interchanges, so the rank sum s below Wm turns into a recurrence that saves a power of the chunk width.", "explicit",
     "Because the sum of these ranks is less than the number of wires times"),
 [
  inf("S1.4.1", "Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with invertible lower triangular $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones.",
      "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization", page="lower-triangular-factorization",
      frm=["linear-algebra","gaussian-elimination","special-matrices"]),
  inf("S1.4.2", "The shear $(H,D)\\mapsto(H+AD,D)$ by a rational matrix of rank $a$ takes exactly $a$ interchanges of field pairs plus $O(V)$ work.",
      "can be performed with exactly $a$ interchanges of pairs of $b$-digit", page="matrix-shear-cost",
      frm=["lower-triangular-factorization","controlled-shifts","address-shear","prime-numbers-and-trial-division"]),
  show("S1.4.3", "Two chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^\\tau)$ time when a preceding row field has length divisible by $W^k$.",
       "split rows cyclically among the $W$ roles, apply each edge shear by smaller interchanges, run gates pointwise, read off the shear $H\\leftarrow H+D$, complete the interchange, and solve the volume-normalized recurrence on a depth-first fixed-tape schedule",
       mot("The common-frame identity with address-shear frames turns the network's endpoint condition into the same shear on every row, and each edge costs as many half-size calls as its rank, each on a stream of volume V/W.", "recoverable"),
       [
        inf("S1.4.3.1", "Using frames $\\Phi_M$ on the role streams, the network applies the shear $H\\leftarrow H+D$ on every original row, including rows of scratch roles.",
            "is $H\\leftarrow H+D$ on every original row, including rows assigned", page="address-shear",
            frm=["array-layout","controlled-shifts","elementary-streams"]),
        inf("S1.4.3.2", "The updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ send $(H,D)$ to $(D,H)$, and only the middle one uses the circuit.",
            "sends $(H,D)$ to $(D,H)$.", frm=["modular-arithmetic"]),
        inf("S1.4.3.3", "The normalized cost obeys $F_k\\le(s/W)F_{k-1}+O(1)$, and $s/W<m^\\tau$ gives $F_k=O(e^\\tau)$.",
            "Hence $F_k=O(e^\\tau)$.", page="rank-deficit-recursion",
            frm=["subspace-labels","recurrence-relations","geometric-series","big-o"],
            salient="A strict power saving $e^\\tau$ with $\\tau<1$, coming only from $s/W<m$."),
        inf("S1.4.3.4", "Parking inactive role streams on a stack gives a depth-first schedule on a fixed number of tapes with only $O(V)$ extra work per node.",
            "No scan passes through a parked ancestor.  Cleanup is always limited to", frm=["stacks","multitape-turing-machine"]),
       ], page="power-width-interchange",
       frm=["rational-shear-interface","frames","matrix-shear-cost","elementary-streams"]),
  inf("S1.4.4", "Supplying rows from a few high digits, padding, and splitting the width in base $m$ give the interchange of arbitrary $u$-bit chunks in $O(Vu^\\tau)$ steps.",
      "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.", frm=["power-width-interchange","elementary-streams","positional-number-systems-with-a-general-radix"]),
 ], page="fast-chunk-interchange", frm=["array-layout","elementary-streams","controlled-shifts"],
 salient="Although the final effect is an exact permutation, the procedure computes XOR combinations of data, and its cost per bit grows only like $u^\\tau$, less than linearly in the width.")

layer = show("S1.5",
 "A normalized butterfly $H_0$ on the same bit of up to $d$ address chunks can be applied to polynomial records in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$ and a single final truncation.",
 "express $H_0^{\\otimes D}$ through $C^{\\otimes D}$, recurse through the complex network's phase frames, implement binary basis changes by packed selected-bit additions, bound guard widths, and evaluate exactly before truncating",
 mot("Separate butterfly factors would each cost a whole-array pass; the complex network replaces them by fewer, smaller recursive calls on volume V/W.", "explicit",
     "factors would require $D$ whole-array passes."),
 [
  inf("S1.5.1", "The phase-frame construction reduces $C^{\\otimes e}$ on a group of $e=mf$ selected bits to $s_{\\rm c}$ child calls on $f$ bits, with all wrappers exact Gaussian dyadic operations, and $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
      "parallel butterfly layer is exact up to its prescribed final truncation.",
      frm=["phase-frames","normalized-butterfly","gaussian-dyadics","gaussian-elimination"]),
  show("S1.5.2", "Selected bits of one address chunk can be XORed into another, restoring a third scratch chunk, in time $O(V(L^\\tau+1))$ on the transform layouts.",
       "eight controlled cyclic rotations of whole chunk ranges, then deterministic sorting repair of the exceptional addresses",
       mot("The rotations act on whole chunk ranges in linear time and are correct away from a small, explicitly known set of addresses, which is cheap to fix by sorting because that set is a $2^{-K}$ fraction.", "recoverable"),
       [
        inf("S1.5.2.1", "On one rectangle the procedure performs $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ and restores the scratch chunk $z$, within the stated time.",
            "It preserves the spectator coordinates, all other chunk bits, and every",
            frm=["fast-chunk-interchange","controlled-shifts","radix-sort-and-stable-sorting"]),
        inf("S1.5.2.2", "The same bound holds for grouped rectangles, as the layer recursion requires.",
            "\\begin{lemma}[Packed selected-bit addition for grouped rectangles]", deferred=True),
       ], page="packed-selected-bit-addition",
       frm=["fast-chunk-interchange","controlled-shifts","elementary-streams","exclusive-or-and-arithmetic-modulo-2"]),
  inf("S1.5.3", "With rows split among the roles, the normalized cost obeys $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which unrolls to $O(d^{\\lambda'})$.",
      "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),", frm=["rank-deficit-recursion","recurrence-relations","geometric-series"]),
  inf("S1.5.4", "Denominator and magnitude growth inside one layer is bounded by $\\lceil C_0d^{C_1}\\rceil=o(p)$ bits, so exact evaluation fits in $O(p)$-bit words.",
      "The accelerated network is evaluated exactly until an entire", frm=["gaussian-dyadics","fixed-point-binary-numbers","two-s-complement"]),
  inf("S1.5.5", "The procedure returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$.",
      "The procedure returns $Q_p(\\mathcal H z)$ in the same array,", frm=["gaussian-dyadics"]),
 ], page="simultaneous-butterfly-layer",
 frm=["normalized-butterfly","gaussian-dyadics","phase-frames","packed-selected-bit-addition","negacyclic-ring"],
 salient="All $D$ butterfly factors together cost only $d^{\\lambda'}$ passes with $\\lambda'<1$ instead of $D$ passes.")

tools = show("S1", "Interchanging $u$-bit address chunks costs $O(Vu^\\tau)$ and a simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\\lambda'})$, with $\\tau,\\lambda'<1$.",
 "supply linear elementary scans, build two finite networks with a rank deficit, and turn each network into a volume-normalized recursion on tape",
 mot("Scanning all data at each of the logarithmically many transform levels already costs n log n, so both data movement and butterfly arithmetic must cost less than one pass per level.", "explicit",
     "We therefore need savings in both movement and arithmetic."),
 [
  inf("S1.1", "Moving or permuting single radix digits of addresses, splitting and merging streams on a digit, and distributing rows cyclically among $W$ streams each take $O(V)$ steps.",
      "Each of the following operations on an array of", page="elementary-streams",
      frm=["array-layout","multitape-turing-machine","amortized-cost-of-a-binary-counter","lexicographic-order"]),
  inf("S1.2", "An update $y\\mapsto y+a(\\text{controls})\\bmod Q$ of a field following its controls, and multiplication by fixed rational units, cost $O(V)$.",
      "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the", page="controlled-shifts",
      frm=["elementary-streams","modular-arithmetic","greatest-common-divisor-and-the-extended-euclidean-algorithm"]),
  networks, interchange, layer,
 ], frm=["multitape-turing-machine","array-layout"])

reduction = show("S2",
 "Exact multiplication of two $n$-bit integers reduces to synthetic transforms and packed ring products whose total cost is $O(n(\\lg n)^{1-\\kappa})$.",
 "compute synthetic transforms with the fast layers, build normalized ring convolution, express prime-length transforms by resampling with retained permutations and chirps, then assemble radix digits, the CRT map, the twist, precision and parameters",
 mot("Splitting into radix digits turns the product into a convolution, and each reduction changes the convolution into a shape whose transforms are signed shifts and butterflies accelerated by the two tape procedures.", "explicit",
     "Splitting the inputs into radix digits reduces multiplication to"),
 [
  show("S2.1", "Normalized synthetic transforms $F_{\\boldsymbol t}^\\pm$ over $\\mathcal R_r$ on $d-1$ power-of-two axes are computed in a retained stored order at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
       "decimation-in-frequency with polynomial roots of unity in stored bit-reversed order, grouped into simultaneous rounds on a chunked layout",
       mot("In the quotient ring the needed roots of unity are powers of y, so each twiddle is an exact signed permutation of coefficients and a level consists only of butterflies and shifts.", "explicit",
           "where the required roots of unity act by exact signed permutations"),
       [
        show("S2.1.1", "The decimation-in-frequency recursion with $\\omega_t=y^{2r/t}$ computes $B_tF_t^-$ and the reverse procedure computes $F_t^+B_t^{-1}$.",
             "check character cancellation directly, then follow the recursion's branch bits into bit-reversed slots",
             mot("The ring has zero divisors, so the usual geometric-sum cancellation must be checked by a shift argument, and recording where outputs land avoids moving frequency indices.", "recoverable"),
             [
              inf("S2.1.1.1", "$\\sum_k\\omega_t^{jk}$ is $t$ or $0$ according as $t\\mid j$, so $F_t^+F_t^-=t^{-1}I$.",
                  "The ring has zero divisors, so we verify character cancellation", frm=["negacyclic-ring","discrete-fourier-transform"]),
              inf("S2.1.1.2", "The outputs are written in bit-reversed order $B_t$ without moving whole frequency indices.",
                  "directly in this order; it does not move whole frequency indices.", frm=["normalized-butterfly","binary-representation-of-integers"]),
             ], page="synthetic-transform", frm=["negacyclic-ring","normalized-butterfly","discrete-fourier-transform"]),
        inf("S2.1.2", "Placing selected bits at a common offset in $K$-bit chunks makes each round one simultaneous layer, with layout and restoration charged in the cost.",
            "Both layout construction and final restoration are charged in this", page="transform-layout",
            frm=["synthetic-transform","simultaneous-butterfly-layer","fast-chunk-interchange","elementary-streams"]),
       ]),
  show("S2.2", "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/(rM)$ over $\\mathcal R_r$ is approximated with error below $\\sqrt2M(3\\ell+1)2^{-p}$ at the transform cost plus $O(Tp\\log(rp))$.",
       "two forward synthetic transforms kept in the same stored order, packed pointwise ring products, and the opposite transform consuming that order",
       mot("A record permutation applied to both operands commutes with the pointwise product, so the stored frequency order never has to be undone.", "explicit",
           "Pointwise multiplication commutes with applying the same record"),
       [
        inf("S2.2.1", "Two disk-grid polynomials of $\\mathcal R_r$ are multiplied exactly by signed Kronecker packing and returned as $Q_p(fg/r)$ in $O(rp\\log(rp))$ time.",
            "One can compute the exact Gaussian integer", page="signed-packing",
            frm=["hvdh-multiplier","negacyclic-ring","gaussian-dyadics","two-s-complement"]),
        inf("S2.2.2", "Since $LB$ permutes records, $P(LBu,LBv)=LBP(u,v)$, so the opposite transform applied to the stored product gives $\\mathcal M_r(f,g)$.",
            "Since $LB$ permutes records and leaves their polynomial suffixes", frm=["cyclic-convolution","discrete-fourier-transform"]),
        inf("S2.2.3", "Errors of the three transforms and the product add to less than $\\sqrt2M(3\\ell+1)2^{-p}$.",
            "The final exact multiplication by $M$ therefore gives error less than", frm=["triangle-inequality"]),
       ], page="synthetic-convolution", frm=["synthetic-transform","transform-layout","signed-packing","cyclic-convolution"]),
  show("S2.3", "The tensor transform on prime lengths satisfies $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with contractions $\\mathcal A,\\mathcal B_0$ computable linewise.",
       "adapt the Gaussian resampling identity keeping both coordinate permutations in the formula, then tensor over axes using chunk swaps to expose lines",
       mot("The usual implementation sorts twice per coordinate; keeping the permutations inside the identity avoids executing those sorts.", "explicit",
           "Its usual implementation sorts twice on each"),
       [
        inf("S2.3.1", "Harvey and van der Hoeven's Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and inverse estimate give $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with contractions $A,B_0$.",
            "The exact Gaussian identity and inverse estimate proved in", page="gaussian-resampling",
            frm=["discrete-fourier-transform","permutations"]),
        inf("S2.3.2", "Tensoring over the $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$.",
            "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,", frm=["gaussian-resampling"]),
        inf("S2.3.3", "Exposing and restoring all lines in the padded box costs $O(Tp\\,d^2(1+\\ell^\\tau))$ via chunk swaps.",
            "then exposing and restoring all the lines costs", frm=["fast-chunk-interchange"]),
       ], page="no-sort-resampling", frm=["gaussian-resampling","discrete-fourier-transform","hvdh-multiplier"]),
  inf("S2.4", "With chirp $a$, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, so the middle transform with its target permutation is a normalized cyclic convolution.",
      "multiplications. The chirp identity below performs the frequency change", page="bluestein-chirp",
      frm=["no-sort-resampling","cyclic-convolution","discrete-fourier-transform","complex-numbers"]),
  inf("S2.5", "$(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$, so the retained source permutation cancels.",
      "proving \\eqref{eq:source-permutation-cancel}. Finally, conjugation", page="source-permutation-cancellation",
      frm=["no-sort-resampling","cyclic-convolution","discrete-fourier-transform","modular-arithmetic"],
      salient="The source permutation $R$ never has to be executed: it cancels exactly across the forward and opposite transforms."),
  show("S2.6", "The assembled algorithm outputs the exact $2n$-bit product in $O(n(\\lg n)^{1-\\kappa})$ time.",
       "fix rational parameters, convert digits, apply the CRT address map, the source transforms built from resampling, chirps and the twist, then prove error below $1/2$ and tabulate costs",
       mot("Each reduction preserves convolution exactly, so it only remains to check that the accumulated numerical error leaves the integers recoverable and that every normalized cost is a power of p below one.", "recoverable"),
       [
        inf("S2.6.1", "Fixed rationals $\\tau=1-2^{-50}$, $\\lambda'=1-2^{-54}$, $\\epsilon=2^{-75}$, $c=2^{-56}$, $\\kappa=2^{-182}$ satisfy all layer and dimension conditions.",
            "These constants are deliberately conservative; no optimization is claimed.", frm=["rank-deficit-recursion"]),
        inf("S2.6.2", "With $q=\\lceil n/b\\rceil$ digits in base $2^b$, the product's digits are a convolution modulo $x^S-1$ with no wraparound and coefficients below $2^{3b}$.",
            "Thus convolution modulo $x^S-1$ has no nonzero wraparound.  Every product", page="radix-digit-convolution",
            frm=["integer-multiplication-problem","cyclic-convolution","positional-number-systems-with-a-general-radix","schoolbook-multiplication"]),
        inf("S2.6.3", "$x\\mapsto\\prod_ix_i^{\\mu_i}$ is an isomorphism onto the product of prime cyclic axes, preserving convolution, and is implemented by triangular controlled shifts.",
            "$\\Phi$ is an isomorphism and preserves cyclic convolution.", page="crt-address-map",
            frm=["chinese-remainder-theorem","cyclic-convolution","controlled-shifts","radix-digit-convolution"]),
        inf("S2.6.4", "The twist $x_d\\mapsto\\zeta y$ turns complex cyclic convolution on the last axis into negacyclic convolution over $\\mathcal R_r$, with the wrap recovered after untwisting.",
            "Untwisting therefore recovers the cyclic coefficient with the correct", page="coefficient-twist",
            frm=["negacyclic-ring","cyclic-convolution","complex-numbers"]),
        inf("S2.6.5", "Composing $\\widetilde{\\mathcal A}$, the chirp transform and $\\widetilde{\\mathcal B}_0$ computes $RF_{\\boldsymbol s}$, and conjugation gives $RF_{\\boldsymbol s}^+$.",
            "its exact counterpart is $RF_{\\boldsymbol s}^{+}$ by",
            frm=["no-sort-resampling","bluestein-chirp","coefficient-twist","synthetic-convolution","source-permutation-cancellation"]),
        inf("S2.6.6", "Two forward source transforms, a pointwise product, the opposite transform and two scalings by $S$ recover $2^{2b+4}(u*v)$.",
            "The two occurrences of $S$ in this algorithm undo different",
            frm=["source-permutation-cancellation","crt-address-map"]),
        inf("S2.6.7", "The recovered coefficient error is below $1/2$, so rounding, $\\Phi^{-1}$ and radix-$2^b$ carries give the exact product.",
            "$H_j/2^p$.  The strict error below $1/2$ makes the nearest integer to", page="exact-recovery",
            frm=["radix-digit-convolution","crt-address-map","synthetic-convolution","source-permutation-cancellation","binary-addition-with-carry-propagation","triangle-inequality"],
            salient="Despite many approximate stages, the total error stays strictly below $1/2$, making the result exact."),
        inf("S2.6.8", "Every normalized cost in the table is at most $p^{1-2\\kappa}$, since the smallest margin is $2^{-181}=2\\kappa$.",
            "Thus $\\min_i g_i=2^{-181}=2\\kappa$.  This explicit slack will cover", page="parameter-choice",
            frm=["simultaneous-butterfly-layer","fast-chunk-interchange","synthetic-convolution","no-sort-resampling","polynomial-time-and-polylogarithmic-cost"],
            salient="The saving exponent $\\kappa=2^{-182}$ is tiny, set by the smallest margin $\\epsilon c(1-\\tau)$."),
        inf("S2.6.9", "With schoolbook multiplication below a cutoff, one fixed machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every $n$.",
            "$O(n(\\lg n)^{1-\\kappa})$ for every input length and produces precisely",
            frm=["schoolbook-multiplication","worst-case-running-time"]),
       ]),
 ], frm=["integer-multiplication-problem","hvdh-multiplier"])

root = show("S0",
 "One deterministic fixed-alphabet multitape Turing machine computes the exact product of two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture in that model.",
 "build two sublinear-per-level tape procedures from finite linear networks with a rank deficit, then chain the known reductions from integer product to synthetic polynomial transforms and bound every cost",
 mot("The Harvey-van der Hoeven route already reduces multiplication to transform levels made of address rearrangements, signed shifts and butterflies; scanning all data per level costs n log n, so beating it needs savings in both movement and arithmetic.", "explicit",
     "We therefore need savings in both movement and arithmetic."),
 [tools, reduction], page="main-theorem",
 frm=["integer-multiplication-problem","nlogn-conjecture","hvdh-multiplier","multitape-turing-machine","big-o","deterministic-computation"],
 salient="The exponent $1-\\kappa$ is strictly below one, so the bound beats $n\\log n$ by a power of $\\log n$, which the conjectured lower bound forbids.",
 adds=[b("\\kappa","saving exponent","The fixed power of $\\lg n$ saved over $n\\lg n$, equal to $2^{-182}$."),
       b("n","input length","The number of bits in each input integer.","count")])

# verify quotes and order
pos = -1; ok = True
def walk(n):
    global pos, ok
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        c = src.count(q)
        i = src.find(q)
        if c == 0: print("MISSING", n["id"], q); ok = False
        elif c > 1: print("MULTI", n["id"], c, q)
        if not n.get("deferred"):
            if i < pos: print("ORDER", n["id"]); ok = False
            pos = max(pos, i)
    m = n.get("motivation")
    if m and m.get("quote") and m["quote"]["quote"] not in src: print("MOTQ", n["id"]); ok=False
    for ch in n.get("children", []): walk(ch)
walk(root)
json.dump({"root": root}, open(base+'exegenius/tasks/0003-argument.answer.json','w'), indent=1, ensure_ascii=False)
print("ok" if ok else "problems")
