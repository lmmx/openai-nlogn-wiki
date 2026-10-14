import json, sys
BASE='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4W/'
SRC=open(BASE+'sources/paper.tex').read()

def ev(q): return {"source":"paper","quote":q}
def inf(id, claim, quote, page=None, frm=(), salient=None, deferred=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":ev(quote),"from":list(frm)}
    if page: n["page"]=page
    if salient: n["salient"]=salient
    if deferred: n["deferred"]=True
    return n
def show(id, claim, method, mot_text, mot_src, children, page=None, frm=(), mot_quote=None, salient=None, adds=None):
    m={"text":mot_text,"source":mot_src}
    if mot_quote: m["quote"]=ev(mot_quote)
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":m,"children":children,"from":list(frm)}
    if page: n["page"]=page
    if salient: n["salient"]=salient
    if adds: n["adds"]=adds
    return n
def b(sym,name,meaning,rel="count"): return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}

# ---------------- Key step: rank-saving recurrence ----------------
K1=inf("S2.4.1","A fixed scalar network of $W$ wires, with copy, gather, scatter and side-injection gates run in eight rows, adds $x_S$ to $y_S$ for arbitrary initial scratch values, and three such stages exchange the banks $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ while restoring every scratch wire.",
 "For arbitrary initial values of its auxiliary wires, a forward", page="linear-network",
 frm=["vectors-matrices-and-invertibility","finite-field-f2-arithmetic","permutations-and-cartesian-products"])

K2=show("S2.4.2","Replacing each scalar by an array and giving every vertex an invertible frame $D_v$ makes the array network apply only the endpoint operator $D_{\\rm out}D_{\\rm in}^{-1}$ to each role, while an edge pays only the change of frame $D_vD_u^{-1}$.",
 "Let a pointwise linear gate commute with a common frame, so that the frames along a route telescope",
 "A frame is an invertible linear operator on the array of one wire; a pointwise gate combines values at one address, so it commutes with any frame shared by all its wires, and the intermediate frames cancel along a route.",
 "recoverable",
 [inf("S2.4.2.1","At a gate $G$ whose wires all carry the same frame $D_v$, $G(D_vg_1,\\ldots,D_vg_t)=D_vG(g_1,\\ldots,g_t)$.",
      "Thus the common frame commutes with the pointwise gate, and"),
  inf("S2.4.2.2","The implemented array operator is $D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}$, so a route from role $w$ to role $\\rho(w)$ applies $D_{\\rm sink(\\rho(w))}D_{\\rm source(w)}^{-1}$ to its array.",
      "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}."),
  inf("S2.4.2.3","Once the scalar routing is fixed, only the endpoint frames determine the operator on each route, so the intermediate frames may be chosen to make each edge change inexpensive.",
      "intermediate frames can then be chosen to make each edge change inexpensive.")],
 page="common-frame-principle", frm=["linear-network","vectors-matrices-and-invertibility"],
 salient="Every intermediate frame cancels: the same endpoint operator (the shear $H\\leftarrow H+D$, or the layer $C^{\\otimes e}$) is applied to every role, including scratch roles whose contents are arbitrary.")

K3=show("S2.4.3","Nested nondegenerate subspaces of $\\mathbb F^{\\otimes 3}$ attached to the gates and terminals make the total rank change of all edges $s<Wm$ for both the bit network and the complex network.",
 "Attach subspace labels built from three-element subsets so that every edge change is an orthogonal residual whose dimension counts the smaller calls, and count dimensions",
 "The cost of an edge is the dimension of its orthogonal residual, so the labels are chosen to keep the total dimension lost on decreasing edges small relative to $N$.",
 "explicit",
 [inf("S2.4.3.1","Indicator vectors of triples satisfy $\\langle t_S,t_T\\rangle=|S\\cap T|-1$, so each triple line is nondegenerate and neighboring triple lines are orthogonal; gather and scatter coefficients depend on the intersection size and side wires cancel the unwanted ones.",
      "\\langle t_S,t_T\\rangle=|S\\cap T|-1,"),
  inf("S2.4.3.2","Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, so $L=Ich$ and the sum of absolute dimension changes is $Wm-2N+2L$.",
      "Every edge joins comparable nondegenerate labels.  The only decreasing"),
  inf("S2.4.3.3","The total loss on decreasing edges satisfies $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both below $1/2$.",
      "\\frac{L_{\\rm b}}{N}=\\frac{100}{539},",
      salient="The loss ratio is a fixed rational just under $1/5$, comfortably below the threshold $1/2$ that the strict saving needs."),
  show("S2.4.3.4","In the bit network the sum of rational ranks of the edge differences is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$, and the endpoint matrices differ by $I_m$ on every input role.",
       "Convert each edge's label change into a matrix of equal rank, and then add the $N$ source ranks that the dimension count misses",
       "The edge matrix is a difference of orthogonal projections, whose rank equals the dimension change, so the rank sum follows from the dimension count plus the source exceptions.",
       "recoverable",
       [inf("S2.4.3.4.1","For nondegenerate $U\\subset V$, the projection difference $P_V-P_U$ has rank $\\dim V-\\dim U$, and reversing the edge negates it without changing its rank.",
            "orthogonal complement.  Its rank is $\\dim V-\\dim U$; reversing the"),
        inf("S2.4.3.4.2","The only exceptions are the $N$ negative source projections $-P_{U_a}$, whose first edge has rank one though the dimension change was zero, so $N$ extra ranks are added to the sum.",
            "The only exceptions are the $N$ negative source projections."),
        inf("S2.4.3.4.3","The deficit of $s_{\\rm b}$ from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
            "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.")],
       frm=["linear-algebra-basics"],
       salient="The whole saving is the deficit $N-2L>0$: although it is tiny relative to $W_{\\rm b}m$, it is strictly positive because $L<N/2$."),
  inf("S2.4.3.5","In the complex network the binary labels give phase-frame differences that are products of one kernel $aI+bX_v$ per orthonormal basis vector of the residual, with total length $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$.",
      "The sum of these basis lengths is")],
 page="subset-intersection-labels", frm=["linear-algebra-basics","linear-network","common-frame-principle","finite-field-f2-arithmetic"],
 mot_quote="The saving will come from keeping the total dimension lost on decreasing",
 salient="The rank sum falls short of $Wm$ only by the positive deficit $N-2L$ (bit) or $2N-2L$ (complex), and the shortfall arises only because just the central-wire edges from time 3 to time 4 lose dimension.")

K4=inf("S2.4.4","Because the relative rank deficits exceed $20\\cdot2^{-50}$ and $\\log m<20$, the fixed rational exponent $\\tau=\\sigma=1-2^{-50}$ gives $s/W<m^\\tau$ for both networks.",
 "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,", frm=["subset-intersection-labels","recurrences-and-induction"],
 salient="A single exponent $1-2^{-50}$ serves both networks even though their relative rank deficits differ.")

K5=show("S2.4.5","A rational $m\\times m$ shear $(H,D)\\mapsto(H+AD,D)$ of rank $a$ costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
 "Factor $A=E_1\\Pi E_2$ with lower triangular $E_1,E_2$, so that all work except the $a$ single-pair swaps is a controlled shift in tape order",
 "Controlled shifts update a later field from earlier fields in linear time, so a change of coordinates that is lower triangular costs only $O(V)$ and the rank of $A$ alone sets the number of recursive swaps.",
 "explicit",
 [inf("S2.4.5.1","Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
      "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"),
  inf("S2.4.5.2","Each one of $\\Pi$ at position $(i,j)$ gives $H_i\\leftarrow H_i+D_j$ by $D_j\\leftarrow D_j+H_i$, one interchange, and $D_j\\leftarrow H_i-D_j$, so the shear uses exactly $a$ interchanges.",
      "can be performed with exactly $a$ interchanges of pairs of $b$-digit")],
 page="address-shear", frm=["linear-algebra-basics","controlled-shift","elementary-stream-ops","modular-arithmetic"],
 mot_quote="earlier fields in linear time.  Lower triangular changes of coordinates",
 salient="The cost depends on the rank $a$ and not on the size of $A$: an edge matrix of low rank needs few recursive swaps.")

K6=show("S2.4.6","Running the network with each edge change done by smaller interchanges on role streams of volume $V/W$ gives cost per volume $F_0=O(1)$, $F_k\\le(s/W)F_{k-1}+O(1)$, and hence $F_k=O(e^\\tau)$ with $\\tau<1$.",
 "Split rows among the $W$ roles, charge $s$ smaller calls of volume $V/W$ at each node, and sum the geometric series using $s/W<m^\\tau$",
 "Each of the $s$ child calls acts on a stream with $1/W$ of the volume, so dividing by volume multiplies the recursive term by $s/W$; since this factor is below $m$ the sum over $\\log_m e$ levels grows only like a power below $e$.",
 "recoverable",
 [inf("S2.4.6.1","Whole rows are split cyclically into $W$ role streams of identical shape, each of logical volume $V/W$.",
      "Split whole rows cyclically into $W$ role streams within each prefix"),
  inf("S2.4.6.2","The chunk interchange is the three shears $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ in which only the middle shear uses the network.",
      "Only the middle shear uses the circuit.  The other two"),
  inf("S2.4.6.3","The number of recursive calls is the sum of the edge ranks, exactly $s$, each acting on one role stream.",
      "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  inf("S2.4.6.4","Dividing time by volume gives the recurrence $F_0=O(1)$, $F_k\\le(s/W)F_{k-1}+O(1)$.",
      "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."),
  show("S2.4.6.5","For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$, so $F_k=O(e^\\tau)$ for $e=m^k$.",
       "Sum the geometric series, treating the cases $a\\le1$ and $a>1$ separately",
       "The two regimes of the ratio $a$ give different dominant terms, but both are bounded by $m^{k\\tau}$ when $a<m^\\tau$.",
       "recoverable",
       [inf("S2.4.6.5.1","If $a\\le1$ the sum is at most $k+1=O(m^{k\\tau})$.",
            "$\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$.  If $a\\le1$, the sum is at"),
        inf("S2.4.6.5.2","If $a>1$ the sum is $O(a^k)$, which is $O(m^{k\\tau})$ because $a<m^\\tau$.",
            "most $k+1=O(m^{k\\tau})$; if $a>1$, it is $O(a^k)$."),
        inf("S2.4.6.5.3","Hence $F_k=O(e^\\tau)$.",
            "Hence $F_k=O(e^\\tau)$.")],
       frm=["recurrences-and-induction"]),
  inf("S2.4.6.6","Parking and restoring the other $W-1$ role streams and copying costs $O(V)$ per node, so the factor $s/W$ is not inflated by temporary storage.",
      "Each push, pop, copy, positioning operation, or erasure moves $O(V)$")],
 frm=["address-shear","linear-network","common-frame-principle","recurrences-and-induction"])

K=show("S2.4","Because the fixed exchange network has $W$ wires of rank-$m$ labels and total edge rank $s<Wm$, running it with edge changes done by $s$ smaller calls on streams of volume $V/W$ gives cost per volume $F_k\\le(s/W)F_{k-1}+O(1)$ and $F_k=O(e^\\tau)$ for a fixed $\\tau<1$.",
 "Build a fixed linear exchange network with restored scratch wires and a strict rank deficit $s<Wm$, give it frames so each edge is a smaller call, and unroll the cost-per-volume recurrence",
 "Multiplying the parameter by $m$ multiplies the work by $s/W$, which is strictly below $m$; this strict inequality, and nothing else, is the source of the power saving.",
 "explicit",
 [K1,K2,K3,K4,K5,K6],
 page="rank-saving-recurrence",
 frm=["linear-network","common-frame-principle","subset-intersection-labels","address-shear","tape-address-model","elementary-stream-ops","recurrences-and-induction"],
 mot_quote="increases the recursive contribution by $s/W<m$. This strict inequality",
 salient="The saving is a power of the parameter although $s/W$ is below $m$ only by a relative margin of about $10^{-11}$ to $10^{-13}$: any strict $s<Wm$ gives a fixed exponent $\\tau<1$.",
 adds=[b("W","wire count","the number of wires of the fixed network, including scratch wires"),
       b("m","label dimension","the dimension of the label space, equal to the number of fields in each address vector"),
       b("s","smaller calls","the number of smaller calls, the sum of the ranks of all edge differences")])

# ---------------- toolbox ----------------
T1=inf("S2.1","An array on address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order with its address implicit in position; its logical volume $V$ is the number of stored data bits.",
 "An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in", page="tape-address-model",
 frm=["multitape-tm","binary-representation-and-bit-operations","permutations-and-cartesian-products"])
T2=inf("S2.2","Permuting two radix-$q$ digits, moving a digit, splitting on a digit and merging, and dealing whole rows cyclically to $W$ streams each take $O(V)$ steps on a fixed number of tapes.",
 "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:", page="elementary-stream-ops",
 frm=["tape-address-model","sorting-and-data-movement-on-tapes","finite-alphabet-encodings-and-constant-factor-simulation"])
T3=inf("S2.3","An update $y\\mapsto y+a(\\text{controls})\\pmod Q$ of a target field that follows its control fields costs $O(V)$, by splitting each fiber at the offset and merging the two pieces in the opposite order.",
 "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the", page="controlled-shift",
 frm=["tape-address-model","elementary-stream-ops","modular-arithmetic","primes-coprimality-and-gcd"])

# ---------------- procedure 1 ----------------
P1=show("S2.5","Two disjoint address chunks of $u$ bits, $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$, can be interchanged on tape in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, with an exact permutation as final effect for arbitrary scratch contents.",
 "Interchange the chunks by three address shears and execute the middle shear through the bit network with the rank-saving recursion, handling general widths and row counts by padding and a base-$m$ expansion",
 "Only the middle of three shears needs the network, so the recursive saving applies to the interchange while the other two shears are linear-time controlled shifts.",
 "explicit",
 [inf("S2.5.1","For arbitrary widths $u$ and shapes, the permutation $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ is performed in $O(Vu^\\tau)$ steps, including padding, unpadding and cleanup.",
      "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.",
      frm=["rank-saving-recurrence"]),
  inf("S2.5.2","The row field needed to split into $W$ roles is supplied by the top $\\rho$ digits of each chunk, which are exchanged and joined at cost $O(V\\rho)$, then padded to a multiple of $W^k$ rows.",
      "Append zero rows, separately within"),
  inf("S2.5.3","Writing the remaining width in base $m$ as $e-\\rho=\\sum_j a_jm^j$ with $a_j<m$ and applying the power-width interchange of the rank-saving recursion to $a_j$ pieces of width $m^j$ costs $O(Ve^\\tau)$ in total.",
      "Write the remaining width in base $m$:"),
  inf("S2.5.4","For binary chunk widths $u$ one pads $[2^u]$ to $[q^e]$ with $e=O(u)$ and removes the padding, giving the bound $O(Vu^\\tau)$ for arbitrary $u$.",
      "Finally, for binary chunks let $e$ be the least integer with")],
 page="address-chunk-interchange",
 frm=["rank-saving-recurrence","address-shear","elementary-stream-ops","controlled-shift","tape-address-model"],
 mot_quote="componentwise.  Only the middle shear uses the circuit.  The other two",
 salient="Although the intermediate steps form XOR combinations of the data, the final effect is an exact permutation, correct for arbitrary initial scratch values.")

# ---------------- procedure 2 ----------------
PF1=show("S2.6.1","The normalized layer is $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$, and each edge of the complex network factors into one two-point kernel $C=aI+bX$ per residual basis vector, so a $C$-layer on $e=mf$ axes needs $s$ layers on $f$ axes.",
 "Rewrite $H_0$ through the kernel $C$ whose powers are translations in the phase frame, so that the network edges reduce to smaller $C$-layers",
 "The network's frame changes are products of translation kernels $aI+bX_v$, so the layer to be accelerated has to be expressed through $C$ rather than $H_0$ itself.",
 "recoverable",
 [inf("S2.6.1.1","The two-point kernel $C=H\\mathsf SH=aI+bX$ satisfies $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=-iZCZ$.",
      "H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad"),
  inf("S2.6.1.2","An arbitrary residual basis is moved into coordinate position by a change of basis in $\\operatorname{GL}(m,\\mathbb F_2)$ applied to each column, after which each basis vector gives one child $(C^{\\pm1})^{\\otimes f}$ on the $f$ axes of one slot.",
      "To implement \\eqref{eq:phase-edge-coordinate} on the group, first apply"),
  inf("S2.6.1.3","Summing its residual dimensions gives exactly $s_{\\rm c}$ child calls on $e/m$ axes, and an inverse child costs one forward call by $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$.",
      "Summing its residual dimensions gives exactly"),
  inf("S2.6.1.4","On all selected coordinates $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$ with $\\mathcal S_D$ the diagonal phase $i^{x_1+\\cdots+x_D}$.",
      "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.")],
 page="phase-frame-kernel",
 frm=["rank-saving-recurrence","subset-intersection-labels","common-frame-principle","linear-algebra-basics","butterfly","complex-numbers","finite-field-f2-arithmetic"])

PF2=show("S2.6.2","A binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ at the same bit position of $f$ chunks costs $O(V(L^\\tau+1))$, exactly and for every initial value of the third chunk.",
 "Perform eight whole-chunk cyclic shifts that equal the XORs away from a small exceptional set of addresses, then repair that set deterministically by sorting",
 "Cyclic shifts of whole chunks are cheap and chunk-wide, but carries between adjacent segments make them wrong at a few addresses; those addresses depend only on guard values, so they can be listed and fixed separately.",
 "recoverable",
 [inf("S2.6.2.1","The packed procedure takes time $O(V(L^\\tau+1)+MA^3+\\delta_{\\rm bad}MA(R+A))$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.",
      "With $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$, its time is"),
  inf("S2.6.2.2","For a Boolean control $c$, the eight operations on $(u,w)$ flip the parity of $u$ exactly when $c=1$ and restore the arbitrary integer $w$.",
      "If $c=0$, these operations do nothing. If $c=1$, the first four operations"),
  inf("S2.6.2.3","The shifts agree with the ideal XORs outside the set $\\mathcal B$ of addresses with a guard value in the bad range, and $|\\mathcal B|\\le\\delta_{\\rm bad}M$ independently of the payload.",
      "|\\mathcal B|\\le\\delta_{\\rm bad}M."),
  inf("S2.6.2.4","The remaining records are extracted, given their destination ranks, sorted by stable binary radix sort and reinserted, which implements the ideal map everywhere.",
      "Hold the full stream untouched")],
 page="packed-selected-bit-addition",
 frm=["address-chunk-interchange","controlled-shift","elementary-stream-ops","sorting-and-data-movement-on-tapes","modular-arithmetic"],
 salient="The set of addresses where the packed shifts fail has density at most $80(f-1)2^{-K}$, uniform over all payloads, so the repair is cheap in the worst case.")

PF3=show("S2.6.3","With rows supplied by the first $q_0$ chunks, the recursion $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ unrolls to $O(d^{\\lambda'})$ per volume for the whole simultaneous layer.",
 "Unroll the recurrence of the complex network with the packed chunk moves as node overhead, stopping at $e<d^{\\beta}$ and partitioning the remaining chunks in base $m$",
 "Each node of the recursion pays the packed basis changes at cost $(eK)^\\tau$ per volume while the number of children grows by $s/W<m^\\sigma$, so the same geometric sum as before applies.",
 "recoverable",
 [inf("S2.6.3.1","Splitting a row index $u=Wg+w$ and sending that row to role $w$ makes each child edge call act on a stream of $1/W$ of the parent's volume.",
      "At a node, write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),"),
  inf("S2.6.3.2","The cost per volume satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ with $F(e)=O(e)$ for $e<d^\\beta$.",
      "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
  inf("S2.6.3.3","Internal costs sum to $O(e^\\lambda)$ because $a=s/W<m^\\lambda$, and the leaves contribute $O(e^\\sigma d^{\\beta(1-\\sigma)})$.",
      "\\le O(e^\\sigma d^{\\beta(1-\\sigma)})."),
  inf("S2.6.3.4","Adding the base-$m$ pieces and the row preprocessing gives $O(d^{\\lambda'})$ for any fixed $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
      "=O(d^{\\lambda'})"),
  inf("S2.6.3.5","With guard width $\\lceil C_0d^{C_1}\\rceil=o(p)$ every intermediate dyadic is exact, so the whole layer is evaluated exactly before one truncation $Q_p$.",
      "Choose \\(\\epsilon C_1<1\\).  Since \\(d=\\Theta(p^\\epsilon)\\),"),
  inf("S2.6.3.6","The procedure returns $Q_p(\\mathcal H z)$ in $O(Vd^{\\lambda'})$ time with every coefficient in the unit disk and error less than $\\sqrt2\\,2^{-p}$.",
      "The procedure returns $Q_p(\\mathcal H z)$ in the same array,")],
 frm=["rank-saving-recurrence","fixed-point-truncation","recurrences-and-induction"])

P2=show("S2.6","$H_0$ applied at the same bit offset in $d$ address chunks of an array of polynomial records, followed by one truncation $Q_p$, costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
 "Evaluate the layer exactly through the phase-frame network, with the basis changes done by packed whole-chunk moves, before a single truncation",
 "Applying $H_0$ separately on $D$ axes needs $D$ whole-array passes, while the rank-saving recursion can combine them.",
 "explicit",
 [PF1,PF2,PF3],
 page="fast-butterfly-layer",
 frm=["rank-saving-recurrence","address-chunk-interchange","packed-selected-bit-addition","phase-frame-kernel","fixed-point-truncation","polynomial-ring-mod","butterfly"],
 mot_quote="factors would require $D$ whole-array passes.")

S2=show("S2","Two tape procedures, an interchange of address chunks in $O(Vu^\\tau)$ and a simultaneous butterfly layer in $O(Vd^{\\lambda'})$ with $\\tau,\\lambda'<1$, save a power of the logarithm in movement and in arithmetic.",
 "Derive both procedures from fixed linear networks that exchange two banks of values and restore all scratch values, whose recursive use has total edge rank below the trivial bound",
 "A scan of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $n\\log n$, so both address movement and butterfly arithmetic must become cheaper by a power.",
 "explicit",
 [T1,T2,T3,K,P1,P2],
 mot_quote="Each procedure arises from its own fixed linear network that exchanges two",
 frm=["multitape-tm","sorting-and-data-movement-on-tapes"])

# ---------------- S3: ring convolution ----------------
SY=show("S3.1","The synthetic transform $F_t^-$ over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with root $\\omega_t=y^{2r/t}$, computed by radix-two butterfly rounds with monomial twiddles, stores outputs in bit-reversed order, and the reverse procedure computes $F_t^+B_t^{-1}$.",
 "Run decimation in frequency with $\\omega_t=y^{2r/t}$ acting as a signed coefficient shift, and consume the retained bit-reversed order in reverse",
 "Powers of $y$ are exact roots of unity that act by signed shifts, so a transform needs only half-sums, half-differences and signed shifts, with no sort to undo bit reversal.",
 "explicit",
 [inf("S3.1.1","Character sums vanish: $\\sum_{k}\\omega_t^{jk}$ equals $t$ if $t\\mid j$ and $0$ otherwise, whence $F_t^+F_t^-=t^{-1}I$ although the ring has zero divisors.",
      "\\qquad F_t^+F_t^-=t^{-1}I."),
   inf("S3.1.2","Each level pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\\omega_t^{-k}$ and recurses on both branches.",
       "The length-one procedure is the identity.  For $t\\geq2$, the"),
   inf("S3.1.3","After all rounds the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$, and the reverse procedure applies the inverse monomial then $H_0$ to give $F_t^+B_t^{-1}$.",
       "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$."),
   inf("S3.1.4","On $D$ axes a round groups into one parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$ of exponent $E$ depending only on the address, so each round is a contraction.",
       "Consequently the individual axis steps may be grouped as a parallel")],
 page="synthetic-transform",
 frm=["polynomial-ring-mod","dft","multidimensional-dft","butterfly","roots-of-unity","fast-fourier-transform-and-divide-and-conquer","ring-and-group-notions-for-polynomials"],
 mot_quote="serve as roots of unity in the remaining axes, and multiplication by")

SP=show("S3.3","A product of two disk grid polynomials in $\\mathcal R_r$ is computed exactly and returned as $Q_p(fg/r)$ in time $O(rp\\log(rp))$ by four integer products with the established multiplier.",
 "Evaluate the integer-coefficient polynomials at $B_0=2^{4p}$ with signed digits, multiply the resulting integers, and read the coefficients back by centered residues",
 "Evaluating at $2^{4p}$ turns a polynomial product into one integer product, and the coefficient bound $2^{3p}<B_0/2$ lets signed coefficients be recovered unambiguously.",
 "recoverable",
 [inf("S3.3.1","One can compute the exact Gaussian integer numerators of $fg$ and return $Q_p(fg/r)$ in time $O(rp\\log(rp))$.",
      "$O(rp\\log(rp))$ on a fixed number of tapes."),
  inf("S3.3.2","Each coefficient of an ordinary product satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so the next coefficient is identified by its centered residue modulo $B_0$.",
      "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2."),
  inf("S3.3.3","Extraction uses a carry $\\rho_j\\in\\{0,1\\}$ at block $j$ and the unique integer $\\widehat h_j\\in[-B_0/2,B_0/2)$ congruent to $q_j+\\rho_j$, which equals $h_j$ by the separation bound.",
      "At block $j$, let $\\widehat h_j$ be the unique"),
  inf("S3.3.4","Reduction modulo $y^r+1$ subtracts the coefficient at $j+r$ from that at $j$, and the normalized product stays in the disk because each coefficient averages $r$ signed products.",
      "The real and imaginary numerator streams are respectively")],
 page="signed-packing",
 frm=["established-multiplier","polynomial-ring-mod","fixed-point-truncation","polynomials","norms-absolute-values-and-error-bounds"])

S3=show("S3","The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathcal R_r$ on $d-1$ axes is computed with error below $\\sqrt2M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
 "Take two forward synthetic transforms keeping the same frequency order, multiply pointwise by signed packing, divide by $r$, and apply the opposite transform, with the fast layers and chunk swaps inside",
 "Pointwise multiplication commutes with the same record permutation on both operands, so the retained order can be passed directly to the opposite transform.",
 "explicit",
 [SY,
  inf("S3.2","The transform layout $L$ (prefix moves and at most $O(p/K)$ chunk exchanges) and the simultaneous rounds give a forward transform of error less than $\\sqrt2\\ell2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
      "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right).",
      frm=["synthetic-transform","fast-butterfly-layer","address-chunk-interchange"]),
  SP,
  inf("S3.4","The expansion $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$ with $F^+F^-=I/M$ identifies the scaled transform pipeline with $\\mathcal M_r(f,g)$, and its error and cost are the stated ones.",
      "Perform both forward transforms and retain their common $LB$ order.",
      frm=["synthetic-transform","signed-packing"])],
 page="ring-convolution",
 frm=["cyclic-convolution","polynomial-ring-mod","synthetic-transform","signed-packing","fast-butterfly-layer","address-chunk-interchange","dft","multidimensional-dft","established-multiplier"],
 mot_quote="permutation $LB$ to both operands.  We may therefore multiply the")

# ---------------- S4: resampling ----------------
CH=inf("S4.6","The permuted transform is a chirp-weighted convolution $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$ with $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$.",
 "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because", page="bluestein-chirp",
 frm=["dft","multidimensional-dft","cyclic-convolution","complex-numbers","roots-of-unity"])
PC=inf("S4.7","The source permutation $R$ cancels: $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
 "because a coordinate permutation commutes with pointwise products.", page="permutation-cancellation",
 frm=["bluestein-chirp","gaussian-resampling","dft","cyclic-convolution","primes-coprimality-and-gcd"],
 salient="The permutation $R$ occurs once on each side of the pointwise product and cancels exactly, so neither the source nor the target permutation is ever executed as a sort.")
S4=show("S4","A Fourier transform on prime axes of lengths $s_i$ is computed as $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with power-of-two $t_i$, the permutations $R,Q$ left in the formula and the middle transform turned into a normalized convolution.",
 "Express each prime-length transform through a longer power-of-two transform by Gaussian-weighted contractions, tensor over the axes, keep the coordinate permutations inside the identity, and convert the middle transform to a convolution by a chirp",
 "The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two.",
 "explicit",
 [inf("S4.1","For coprime $s<t$ with $\\theta=t/s-1>p/\\alpha^4$ there are linear contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
      "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."),
  inf("S4.2","The approximations to $A$ and $B_0$ have error less than $p^2$ and cost $O(tp^{3/2+\\delta}\\alpha)$ on a line of length $t$, with no sorting of the permutations $P_s,P_t$.",
      " O(tp^{3/2+\\delta}\\alpha)."),
  inf("S4.3","Tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
      "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,"),
  inf("S4.4","The linewise maps cost $O(dTp^{3/2+\\delta}\\alpha)$ with error below $dp^2$.",
      "$O(dTp^{3/2+\\delta}\\alpha)$, with a constant independent of $d$."),
  inf("S4.5","Exposing and restoring all lines in the padded box by adjacent axis interchanges costs $O(Tpd^2(1+\\ell^\\tau))$.",
      "then exposing and restoring all the lines costs",
      frm=["address-chunk-interchange"]),
  CH, PC],
 page="gaussian-resampling",
 frm=["dft","multidimensional-dft","fixed-point-truncation","established-multiplier","address-chunk-interchange","norms-absolute-values-and-error-bounds"],
 mot_quote="The transform lengths needed for the integer product are pairwise coprime,")

# ---------------- S5: assembly ----------------
PCH=show("S5.1","The sizes $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$ and distinct primes $s_i$ just below $t_i\\in\\{r/2,r\\}$ with $T/2<\\prod s_i<T$ satisfy every hypothesis of the tape lemmas and of resampling, with $Tp=\\Theta(n)$.",
 "Fix rational exponents with explicit margins, then choose the box, the precision and the prime lengths so that all hypotheses hold",
 "The resampling lemma needs $\\theta_i=t_i/s_i-1>p/\\alpha^4$ and a product of primes occupying a fixed fraction of the padded box, which forces the $s_i$ into intervals just below the powers of two.",
 "recoverable",
 [inf("S5.1.1","The fixed rational choice $\\tau=\\sigma=1-2^{-50}$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $\\epsilon=2^{-75}$ satisfies all layer conditions.",
      "\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16},\\\\"),
  inf("S5.1.2","Set $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$, with $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
      "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
  inf("S5.1.3","The interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains more than $d$ primes for $x\\in\\{r/2,r\\}$, so distinct odd primes $s_i$ can be chosen with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$.",
      "contains at least $\\eta x/(2\\log x)$ primes."),
  inf("S5.1.4","Then $T/2<S<T$ and $\\alpha^4\\theta_i>p$, so every hypothesis of the one-dimensional resampling lemma holds.",
      "Together with $s_i<t_i$, this gives $T/2<S<T$.")],
 page="parameter-choice",
 frm=["gaussian-resampling","ring-convolution","primes-coprimality-and-gcd","logarithms-and-iterated-logarithm-notation","floor-ceiling-and-summation-notation"])

RDC=show("S5.2","With $q=\\lceil n/b\\rceil$ digits per input, the integer product is the polynomial product whose coefficients are below $2^{3b}$, and convolution modulo $x^S-1$ has no wraparound.",
 "Write each input as a polynomial in $2^b$ and pad so the cyclic convolution of length $S$ contains the whole product",
 "Cyclic convolution agrees with the ordinary polynomial product when the product's degree is below the length, and small digits make the coefficients small enough to be recovered by rounding.",
 "recoverable",
 [inf("S5.2.1","The product has degree at most $2q-2<S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
      "Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
  inf("S5.2.2","Every product coefficient obeys $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
      "0\\le c_j\\le q(2^b-1)^2<2^{3b},")],
 page="radix-digit-convolution", frm=["cyclic-convolution","polynomials","binary-representation-and-bit-operations"])

CRT=show("S5.3","The Agarwal--Cooley map $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\ldots,x_d]/(x_i^{s_i}-1)$, $x\\mapsto\\prod_i x_i^{\\mu_i}$, is a convolution-preserving isomorphism implemented by triangular controlled shifts in time $O(Tp\\,d^2(1+\\ell^\\tau))$.",
 "Send $x$ to the product of $x_i^{\\mu_i}$ with $\\mu_i=P_i^{-1}\\bmod s_i$, so the new coordinates are lower triangular in the mixed-radix digits and every update is a controlled shift",
 "A single cyclic convolution of length $S=\\prod s_i$ with pairwise coprime $s_i$ is a convolution on distinct prime axes by the Chinese remainder theorem, and the coordinate powers $\\mu_i$ make the change of order a sequence of controlled cyclic shifts.",
 "recoverable",
 [inf("S5.3.1","$\\Phi$ is an isomorphism and preserves cyclic convolution, because the image of $x$ has order $S$ and runs through all target monomials exactly once.",
      "$\\Phi$ is an isomorphism and preserves cyclic convolution."),
  inf("S5.3.2","The coordinate of $\\Phi(x^k)$ in axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, depending only on lower-index digits.",
      "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}."),
  inf("S5.3.3","The map, its inverse and their padding operations cost $O(Tp\\,d^2(1+\\ell^\\tau))$ by $d$ controlled shifts and $O(d^2)$ axis moves by chunk interchange.",
      "their padding operations cost",
      frm=["address-chunk-interchange"])],
 page="crt-address-map",
 frm=["cyclic-convolution","chinese-remainder-theorem","primes-coprimality-and-gcd","controlled-shift","address-chunk-interchange","modular-arithmetic"],
 salient="The offset for target $i$ depends only on lower-index digits, so the updates in order $i=d,\\ldots,1$ always read original controls.")

TW=show("S5.4","The coefficient twist $\\Theta:x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ is an isomorphism from $\\mathbb C[x_d]/(x_d^r-1)$ to $\\mathcal R_r$ that turns the negative wrap into the cyclic wrap.",
 "Multiply coefficient $k$ by $\\zeta^k$ so that the sign $(-1)^h$ of the negacyclic wrap is cancelled by $\\zeta^{rh}=(-1)^h$",
 "A cyclic last coordinate has no polynomial roots of unity in $y^r+1$, but twisting by half a period makes the two wraps differ exactly by the sign that $\\zeta^r=-1$ absorbs.",
 "recoverable",
 [inf("S5.4.1","The map $\\Theta$ is diagonal on the bases, multiplying coefficient $k$ by the nonzero number $\\zeta^k$, so it is an isomorphism preserving the sup norm.",
      "multiplying coefficient $k$ by the nonzero number $\\zeta^k$."),
  inf("S5.4.2","Writing $k+l=j+hr$ with $h\\in\\{0,1\\}$, a twisted term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
      "Untwisting therefore recovers the cyclic coefficient with the correct")],
 page="phase-twist", frm=["polynomial-ring-mod","cyclic-convolution","roots-of-unity","complex-numbers"])

ALG=show("S5.5","The algorithm forms radix digits, applies $\\Phi$, runs two source transforms, multiplies pointwise, runs the opposite transform, rescales, rounds and propagates carries, with the last coordinate twisted into $\\mathcal R_r$ inside the chirp convolution.",
 "Compose the chirp convolution (twist plus ring convolution) into the source transform $\\mathscr F$, and use it three times so the retained permutation cancels",
 "Two forward source transforms, a pointwise product and an opposite transform give the convolution of the digit arrays, and the permutation cancellation lets each use the retained form.",
 "recoverable",
 [inf("S5.5.1","The computed chirp transform multiplies by $\\overline{\\widetilde a}$, convolves with $\\widetilde a$ and multiplies by $\\overline{\\widetilde a}$ again, using the twisted ring convolution.",
      "Thus $\\widetilde a$ is the convolution kernel and $x_0$ is the data"),
  inf("S5.5.2","The source transform applies $\\mathcal A$, the chirp transform and $\\mathcal B_0$, then multiplies by $2^\\gamma$; its exact counterpart is $\\mathscr F=RF_{\\boldsymbol s}$.",
      "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A"),
  inf("S5.5.3","Apply the coefficient-address map $\\Phi$ with padding to the digit arrays to obtain $u,v$.",
      "Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"),
  inf("S5.5.4","Compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
      "Compute $\\widetilde{\\mathscr F}(u)$ and"),
  inf("S5.5.5","Multiply corresponding coefficients exactly and truncate toward zero to obtain $z$.",
      "Multiply corresponding complex coefficients exactly and truncate"),
  inf("S5.5.6","Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its numerators exactly by $S$.",
      "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
  inf("S5.5.7","Multiply by $2^{2b+4}S$, round to the nearest integers, apply $\\Phi^{-1}$ to restore the coefficient order.",
      "Multiply the grid numerators of $\\widetilde w$ exactly by"),
  inf("S5.5.8","Propagate radix-$2^b$ carries in increasing coefficient order and output $2n$ bits.",
      "Propagate radix-$2^b$ carries in increasing coefficient order."),
  inf("S5.5.9","The two occurrences of $S$ undo different normalizations: after the first scale the exact result is $(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$.",
      "The two occurrences of $S$ in this algorithm undo different")],
 page="multiplication-algorithm",
 frm=["radix-digit-convolution","crt-address-map","phase-twist","bluestein-chirp","gaussian-resampling","permutation-cancellation","ring-convolution","parameter-choice","fixed-point-truncation"])

ER=show("S5.6","The accumulated coefficient error after the second rescaling is below $1/2$, so rounding gives the exact integer coefficients, and radix-$2^b$ carries produce the $2n$-bit product.",
 "Track the error of each computed map through bilinear contraction bounds and norms, scale by the known factors, and then round and propagate carries",
 "The true coefficients are integers and the scale by $2^{2b+4}S$ shrinks the grid error $2^{-6b}$ enough, so if the error is below $1/2$ the nearest integer is the coefficient.",
 "recoverable",
 [inf("S5.6.1","The scaled digits are exact grid values of norm below $1/4$, and the computed transforms have norm below $.26$, so their pointwise product is a legal disk input.",
      "The scaled radix digits in $u,v$ are exact $p$-bit grid values of norm"),
  inf("S5.6.2","The first scaled result $\\widetilde w$ approximates $w=(u*v)/S$ with error below $E_w=S(3E_s+2)<28\\,2^\\gamma T^2L$ times $2^{-p}$.",
      "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L."),
  inf("S5.6.3","After the second scaling by $2^{2b+4}S$ the final absolute error is below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$.",
      "<448b\\,2^{-b+\\gamma}"),
  inf("S5.6.4","The strict error bound below $1/2$ makes the nearest integer the unique correct coefficient, and the coefficient lies in $[0,2^{3b})$.",
      "$H_j/2^p$.  The strict error below $1/2$ makes the nearest integer to"),
  inf("S5.6.5","The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$ with the invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$.",
      "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$.")],
 page="exact-recovery",
 frm=["fixed-point-truncation","radix-digit-convolution","norms-absolute-values-and-error-bounds","floor-ceiling-and-summation-notation"])

TA=show("S5.7","Dividing every cost by $V=Tp=\\Theta(n)$ gives seven dominant powers of $p$, each at most $1-2\\kappa$ with $\\kappa=2^{-182}$, so the total cost is $O(n(\\lg n)^{1-\\kappa})$.",
 "Tabulate the cost of every operation normalized by $V$, read off its power of $p$, and compare each with the margin $g_i$",
 "Every layout move, transform round, resampling line and product is a fixed number of passes over a volume-$V$ array times a factor; the factors are powers of $p$ whose exponents must all be below one by a fixed margin.",
 "recoverable",
 [inf("S5.7.1","The cost of all operations is measured as a multiple of $V=Tp=\\Theta(n)$, and a fixed number of repeated transforms is included in the constants.",
      "For the cost calculation put $V=Tp=\\Theta(n)$. The fixed-width coefficient"),
  inf("S5.7.2","Prefix-slot moves and individual butterfly rounds cost $dK$, of order $p^{\\epsilon(1+c)}$.",
      "Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$\\\\"),
  inf("S5.7.3","Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, of order $p^{1-\\epsilon c(1-\\tau)}$.",
      "Chunk exchanges for transform layout & $pK^{\\tau-1}$ & $1-\\epsilon c(1-\\tau)$\\\\"),
  inf("S5.7.4","Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, of order $p^{1-\\epsilon(1-\\lambda')}$.",
      "Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$\\\\"),
  inf("S5.7.5","CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, of order $p^{\\tau+\\epsilon(2-\\tau)}$.",
      "CRT and axis layouts & $d^2(1+\\ell^\\tau)$ & $\\tau+\\epsilon(2-\\tau)$\\\\"),
  inf("S5.7.6","Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, of order $p^{3/4+\\delta+3\\epsilon/2}$.",
      "Gaussian line maps & $dp^{1/2+\\delta}\\alpha$ & $3/4+\\delta+3\\epsilon/2$\\\\"),
  inf("S5.7.7","Chirps, twists and scalar products cost $dp^\\delta$, of order $p^{\\epsilon+\\delta}$.",
      "Chirps, twists and scalar products & $dp^\\delta$ & $\\epsilon+\\delta$\\\\"),
  inf("S5.7.8","Packed polynomial products cost $\\log(rp)$, of order $p^{1-\\epsilon}$.",
      "Packed polynomial products & $\\log(rp)$ & $1-\\epsilon$\\\\"),
  inf("S5.7.9","The margins below one are $g_1,\\ldots,g_7$ with minimum $2^{-181}=2\\kappa$, attained by the chunk-exchange row $g_2=\\epsilon c(1-\\tau)$.",
      "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
      salient="The smallest margin $2^{-181}$ comes from the chunk-exchange row, $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}$, which multiplies the three tiny exponents of the construction."),
  inf("S5.7.10","Each of the seven powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, giving $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
      "Each of the seven displayed powers is at most $1-2\\kappa$ by")],
 page="time-accounting",
 frm=["parameter-choice","multiplication-algorithm","address-chunk-interchange","fast-butterfly-layer","ring-convolution","gaussian-resampling","crt-address-map","phase-twist","rank-saving-recurrence","fixed-point-truncation"],
 salient="Seven different operations each contribute a power of $p$ strictly below one, and the final exponent $1-\\kappa$ is dictated by the smallest of the seven margins.")

S5=show("S5","The pipeline of radix-digit convolution, Chinese-remainder address map, two source transforms with resampling and chirp convolution, pointwise product, opposite transform, rescale, round and carry computes the exact $2n$-bit product within the cost table.",
 "Choose compatible parameters for the procedures, recover the integer coefficients from their approximations, and account for every remaining tape operation",
 "The algorithm needs one consistent choice of sizes for all lemmas, an error analysis showing the rounding is exact, and a cost table showing every term is below the claimed bound.",
 "explicit",
 [PCH,RDC,CRT,TW,ALG,ER,TA],
 mot_quote="exact.  We choose compatible parameters for these procedures, recover",
 frm=["gaussian-resampling","ring-convolution","cyclic-convolution"],
 adds=[b("b","digit width","the number of bits of each radix digit, equal to $\\lceil\\log_2 n\\rceil$"),
       b("p","precision","the number of fractional bits of each stored coordinate, equal to $6b$"),
       b("d","axis count","the number of power-of-two transform axes"),
       b("T","box size","the number of entries of the padded power-of-two box")])

S1=inf("S1","Schönhage and Strassen's $n\\log n$ order was met from above by the $O(n\\log n)$ algorithm of Harvey and van der Hoeven, so a further saving must beat a logarithmic factor by a power.",
 "Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper", page="integer-multiplication-conjecture",
 frm=["big-o","multitape-tm","logarithms-and-iterated-logarithm-notation","big-omega-theta-and-little-o-notation"])

ROOT=show("S0","A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
 "Reduce integer multiplication to a convolution evaluated by multidimensional transforms, and speed up the data movement and butterfly arithmetic of those transforms by two tape procedures that each save a power of the logarithm",
 "Scanning the array at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so a power saving needs savings in both address movement and arithmetic.",
 "explicit",
 [S1,S2,S3,S4,S5],
 page="main-theorem", frm=["integer-multiplication-conjecture","time-accounting","multiplication-algorithm"],
 mot_quote="$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$.")

ans={"root":ROOT}

# ---- verification of quotes and order ----
errs=[]
seq=[]
def walk(n):
    if n["intention"]=="infer":
        q=n["quote"]["quote"]
        c=SRC.count(q)
        if c!=1: errs.append((n["id"],"count",c,q))
        pos=SRC.find(q)
        seq.append((n["id"],pos,n.get("deferred")))
    else:
        mq=n["motivation"].get("quote")
        if mq:
            c=SRC.count(mq["quote"])
            if c!=1: errs.append((n["id"],"mot count",c,mq["quote"]))
        for ch in n["children"]: walk(ch)
walk(ROOT)
last=-1
for i,p,d in seq:
    if d: continue
    if p<last: errs.append((i,"order",p,last))
    last=max(last,p)
for e in errs: print("ERR",e)
print(len(seq),"infer steps")
json.dump(ans,open(BASE+'exegenius/tasks/0003-argument.answer.json','w'),ensure_ascii=False,indent=1)
