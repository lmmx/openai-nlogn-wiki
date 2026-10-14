import json, sys
P='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/S6F4SM/'
def ev(q): return {"source":"paper","quote":q}
def inf(id,claim,q,frm=None,page=None,salient=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":ev(q),"from":frm or []}
    if page:n["page"]=page
    if salient:n["salient"]=salient
    return n
def sh(id,claim,method,mot,src,children,frm=None,page=None,adds=None,salient=None,mq=None):
    m={"text":mot,"source":src}
    if mq: m["quote"]=ev(mq)
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":m,"children":children,"from":frm or []}
    if page:n["page"]=page
    if adds:n["adds"]=[{"symbol":a,"name":b,"meaning":c,"relation":d} for a,b,c,d in adds]
    if salient:n["salient"]=salient
    return n
D,C="direct","count"

T1=inf("T1","An array on address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order with implicit addresses; $V$ is the number of stored data bits.",
 "An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in",["multitape-tm","permutations-and-cartesian-products"],"tape-address-model")
T2=inf("T2","For a fixed radix $q$, permuting two digits, moving a digit, splitting on a digit with a pointwise map and merging, and dealing whole rows cyclically to $W$ streams each take $O(V)$ steps.",
 "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",["tape-address-model","sorting-and-data-movement-on-tapes"],"elementary-stream-ops")
T3=inf("T3","A target field $y$ following its control fields can be updated by $y\\mapsto y+a(\\text{controls})\\pmod Q$ in $O(V)$ time by splitting each fiber at the offset and merging the pieces in the opposite order.",
 "y\\longmapsto y+a(\\text{controls})\\pmod Q",["elementary-stream-ops","modular-arithmetic"],"controlled-shift")
R2=sh("R2","Linear-time tape scans on arrays in lexicographic order are available as building blocks for the two fast procedures.",
 "state the elementary scans and shifts that later procedures call","The section announces that it supplies the elementary scans the interchange procedure uses.","recoverable",[T1,T2,T3])

# K1
K1=sh("K1","With $h=100$, $v=\\binom h3$, $N=v^3$ and $m=h^3$, a fixed linear network on $W$ wires exchanges the banks $X_a,Y_a$ with signs, restoring every scratch wire for arbitrary initial scratch values.",
 "eight-row schedule of copy, gather, scatter and side injection, then cancel the scratch contribution by linearity",
 "The first two rows remove the old scratch values and the last two restore them, a linear case of transparent computation.","explicit",
 [inf("K1.0","Fix the ground-set size $h=100$ so that $v=\\binom h3=161700$, $N=v^3$ and the label dimension is $m=h^3=10^6$.","h=100,\\qquad v=\\binom h3=161700,\\qquad",["binary-representation-and-bit-operations"]),
  inf("K1.1","The net target change of one invocation is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independent of the initial scratch values $a,c$.","$(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independently of"),
  inf("K1.2","Over $\\mathbb F_2$ the central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod 2$, and the side injection cancels exactly the intersection-one cases.","In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
  inf("K1.3","In both constructions (bit and complex) the net map of an invocation is $y\\gets y+x$.","Thus both net maps are $y\\gets y+x$."),
  inf("K1.4","Three invocations (stages 1, 2, 3) send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, i.e. $(X_a,Y_a)\\mapsto(-Y_a,X_a)$.","The inverse schedule with logical source $Y$ and target $X$ effects"),
  inf("K1.5","Each triple has $z_{\\rm b}=3\\binom{97}{2}=13968$ neighbours in the bit construction.","z_{\\rm b}=3\\binom{97}{2}=13968,\\qquad"),
  inf("K1.6","The bit network has $W_{\\rm b}=2N+I(vz_{\\rm b}+c_{\\rm b})$ wires, a fixed number independent of the input length.","W_{\\rm b}&=2N+I(vz_{\\rm b}+c_{\\rm b})")],
 ["linear-algebra-basics","finite-field-f2-arithmetic","permutations-and-cartesian-products"],"linear-network",mq="the following schedule remove the effect of the old scratch values;",
 adds=[("h","ground-set size","The size of the ground set of which the three-element subsets index the data wires.",D),
       ("N","bank size","The number of data wires in each of the two banks.",C),
       ("W_{\\rm b}","bit wire count","The total number of wires of the bit network, scratch wires included.",C)])

K2=sh("K2","Giving every vertex an invertible frame $D_v$ on wire arrays makes pointwise gates commute with frames, so only the endpoint operator $D_{\\rm out}D_{\\rm in}^{-1}$ is applied to each role.",
 "induct along edges and gates on the invariant 'stored array = frame applied to logical array'",
 "Once the scalar routing is fixed, intermediate frames can be chosen freely to make each edge change cheap.","explicit",
 [inf("K2.1","At every vertex the stored array equals $D_v$ applied to the logical array; by linearity a gate commuting with the common frame preserves this invariant.","At a vertex $v$, the invariant is that the stored array equals $D_v$ applied"),
  inf("K2.2","Hence a route from input role $w$ to output role $\\rho(w)$ applies only the endpoint operator, and the intermediate frames can be chosen to make each edge change inexpensive.","intermediate frames can then be chosen to make each edge change inexpensive.")],
 ["linear-network","vectors-matrices-and-invertibility"],"common-frame-principle",mq="intermediate frames can then be chosen to make each edge change inexpensive.")

K3=sh("K3","Nested nondegenerate subspaces of $F^{\\otimes3}$ can be attached to gates and terminals so that the total rank $s$ of all edge differences is below $Wm$.",
 "attach subspace labels from three-element subsets, count the dimension changes (only the central 3-to-4 edges decrease) and add the extra source ranks",
 "The labels are chosen so that the changes of frame become inexpensive.","explicit",
 [inf("K3.1","In the bit network the label space is $F=\\mathbb Q^h$ with form $x^{\\mathsf T}(I-J/9)y$, for which $\\langle t_S,t_T\\rangle=|S\\cap T|-1$.","For the bit network, let $F=\\mathbb Q^h$ with bilinear form"),
  inf("K3.2","In the complex network the label space is $F=\\mathbb F_2^h$ with the dot product, and $t_T\\cdot t_T=1$.","For the complex network, take instead $F=\\mathbb F_2^h$ with the"),
  inf("K3.3","Every triple line is nondegenerate and neighbouring triple lines are orthogonal, which makes the nested subspace assignments possible.","Thus every triple line is nondegenerate, and neighboring triple lines"),
  inf("K3.4","Source dimensions sum to $N$ and sink dimensions to $Wm-N$, so signed dimension changes sum to $Wm-2N$.","The source dimensions sum to $N$ and the sink dimensions to $Wm-N$."),
  inf("K3.5","If decreasing edges lose total dimension $L$, the sum of absolute dimension changes is $Wm-2N+2L$.","dimension $L$, the sum of absolute changes is $Wm-2N+2L$."),
  inf("K3.6","The only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$.","edges are the central-wire edges from time 3 to time 4; their dimension"),
  inf("K3.7","There are $Ic$ decreasing edges, each of loss $h$, so $L=Ich$; replacing signed changes by absolute ones adds $2L$.","There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
  inf("K3.8","The loss ratios satisfy $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both below $1/2$.","In particular, both are smaller than $1/2$."),
  inf("K3.9","With projections $P_U$ as matrices, the endpoint difference $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ holds for every input role, so the same shear acts on every role.","M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m",
      salient=None),
  inf("K3.10","Exception: the $N$ negative source projections each add one rational rank beyond the dimension change, so $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$ and the deficit $N-2L_{\\rm b}$ is positive.","Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
  inf("K3.11","In the complex network, telescoping the phase frames $\\mathcal C_U$ gives $C^{\\otimes m}$ on every role, scratch roles included.","bank exchange, telescoping these phase frames gives $C^{\\otimes m}$"),
  inf("K3.12","For the complex network $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$, with deficit $2N-2L_{\\rm c}>0$.","The deficit is $2N-2L_{\\rm c}>0$."),
  inf("K3.13","The exponent is fixed as $\\tau=\\sigma=1-2^{-50}$.","\\tau=\\sigma=1-2^{-50}."),
  inf("K3.14","Both relative deficits exceed $20\\cdot2^{-50}$, and $m<2^{20}$ gives $\\log m<20$, hence $m^{1-2^{-50}}>m(1-20\\cdot2^{-50})>m(1-\\eta)$.","Both exact deficits displayed above are greater than $20\\cdot2^{-50}$."),
  inf("K3.15","Consequently $s_{\\rm b}/W_{\\rm b}<m^\\tau$ and $s_{\\rm c}/W_{\\rm c}<m^\\sigma$ with $0<\\tau=\\sigma<1$.","\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,")],
 ["linear-algebra-basics","linear-network","common-frame-principle","finite-field-f2-arithmetic","norms-absolute-values-and-error-bounds"],"subset-intersection-labels",mq="choose its intermediate labels to make the changes of frame inexpensive.",
 salient="The total rank s is strictly below Wm even though each of the W wires could change by m ranks, and the edge change is the same shear on every role, scratch roles included; the saving comes from the central wires being the only ones that shrink and from the extra source ranks (N) being smaller than the 2N saved on increases.",
 adds=[("L","total loss","The total dimension lost on the decreasing edges.",D),
       ("s","call count","The sum over all edges of the rank of the edge difference, i.e. the number of smaller calls per invocation.",C),
       ("\\tau","bit saving exponent","A rational exponent with s/W below m^tau.",D),
       ("\\sigma","complex saving exponent","The corresponding exponent for the complex network.",D)])

K4=sh("K4","A rank-$a$ shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
 "factor $A=E_1\\Pi E_2$ with lower-triangular $E_i$ and a partial permutation $\\Pi$, then do each one of $\\Pi$ as three updates around one swap",
 "Lower triangular changes of coordinates can be performed entirely in the linear-time direction of the controlled shifts.","explicit",
 [inf("K4.1","Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.","Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"),
  inf("K4.2","Apply $E_2$ to $D$ and $E_1^{-1}$ to $H$, add $\\Pi D$ to $H$, then apply $E_1$ to $H$ and $E_2^{-1}$ to $D$; the triangular parts cost $O(V)$.","For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
  inf("K4.3","Each one of $\\Pi$ calls for $H_i\\leftarrow H_i+D_j$, done by $D_j\\leftarrow D_j+H_i$, a swap of $H_i,D_j$, and $D_j\\leftarrow H_i-D_j$.","D_j\\leftarrow D_j+H_i,\\qquad"),
  inf("K4.4","The shear uses exactly one interchange per one of $\\Pi$, hence $a$ interchanges, which is the number of recursive calls.","There are $a$ ones, which proves the")],
 ["controlled-shift","linear-algebra-basics","elementary-stream-ops"],"address-shear",mq="can be performed entirely in this direction.")

KA_unroll=sh("KA.7","From $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\\tau$ one gets $F_k=O(e^\\tau)$.",
 "unroll the recurrence into a geometric sum and bound it in the two cases $a\\le1$ and $a>1$",
 "The recurrence has the form F_k <= a F_{k-1} + O(1), whose solution is a geometric sum.","recoverable",
 [inf("KA.7a","The recurrence is $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$, because each of the $s$ calls acts on a stream of volume $V/W$.","F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."),
  inf("KA.7b","For $a=s/W<m^\\tau$ the sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$.","For $a=s/W<m^\\tau$ the geometric sum"),
  inf("KA.7c","If $a\\le1$ the sum is at most $k+1=O(m^{k\\tau})$; if $a>1$ it is $O(a^k)$.","most $k+1=O(m^{k\\tau})$; if $a>1$, it is $O(a^k)$."),
  inf("KA.7d","Hence $F_k=O(e^\\tau)$ for $e=m^k$.","Hence $F_k=O(e^\\tau)$.")],
 ["recurrences-and-induction"])

KA9=sh("KA.9","For arbitrary width $u$, two chunks of $u$ bits can be interchanged in $O(Vu^\\tau)$ steps, by padding to a power width and decomposing the width in base $m$.",
 "swap the top $\\rho$ digits one pair at a time to create enough rows, pad rows to a multiple of $W^k$, and split the remaining width into base-$m$ pieces",
 "Rows for a general array can be supplied by a few of its own high digits.","explicit",
 [inf("KA.9a","Fix $k=\\lceil\\log_m e\\rceil$ and $\\rho=\\lceil k\\log W/(2\\log q)\\rceil$ with $1\\le\\rho<e$ eventually.","There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape"),
  inf("KA.9b","Exchanging the top $\\rho$ digits of each chunk gives a row field of range $R=q^{2\\rho}\\ge W^k$ at cost $O(V\\rho)$.","R=q^{2\\rho}\\ge W^k"),
  inf("KA.9c","Padding rows to $R'=W^k\\lceil R/W^k\\rceil<2R$ at most doubles the volume.","R'=W^k\\left\\lceil R/W^k\\right\\rceil<2R."),
  inf("KA.9d","Writing $e-\\rho=\\sum_j a_jm^j$ with $a_j<m$ and calling the power-width interchange on each piece costs $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^\\tau)$.","O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)."),
  inf("KA.9e","For binary chunks of $u$ bits take the least $e$ with $q^e\\ge2^u$ and pad numerically, at a fixed factor in volume, so the cost is $O(Vu^\\tau)$.","Finally, for binary chunks let $e$ be the least integer with")],
 ["address-shear","elementary-stream-ops","controlled-shift"],mq="Rows for a general array can be supplied by a few of its own high digits.")

KA=sh("KA","Two disjoint address chunks of $e=m^k$ digits each can be interchanged in $O(Ve^\\tau)$ steps, with $\\tau<1$ fixed.",
 "split rows into $W$ role streams, run the bit network with frames $\\Phi_M$ so that only the middle shear $H\\leftarrow H+D$ is recursive, and unroll the recurrence",
 "An edge matrix of rank $a$ will require $a$ smaller interchanges, and the ranks sum to less than $Wm$.","explicit",
 [inf("KA.1","Split whole rows cyclically into $W$ role streams within each prefix; each stream has volume $V/W$.","Split whole rows cyclically into $W$ role streams within each prefix"),
  inf("KA.2","On every circuit edge apply the shear $\\Phi_{A_e}$ to that role stream, implemented by interchanging each pivot pair of $b=e/m$ digit fields recursively.","$\\Phi_{A_e}$ to that role stream; implement it by"),
  inf("KA.3","By the frame identity the output satisfies $f'_{\\rho(w)}=\\Phi_{I_m}f_w$, the shear $H\\leftarrow H+D$ on every original row, scratch rows included.","=\\Phi_{I_m}f_w,"),
  inf("KA.4","Performing $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ sends $(H,D)$ to $(D,H)$; only the middle shear uses the circuit.","D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,"),
  inf("KA.5","The number of recursive calls equals the sum of the edge ranks, exactly $s$.","The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  KA_unroll,
  inf("KA.8","Scheduling the $s$ child calls on a fixed number of tapes costs only the additional $O(V)$ term at each node, by parking inactive role streams on a stack.","Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
  KA9],
 ["address-shear","controlled-shift","elementary-stream-ops","common-frame-principle","subset-intersection-labels","recurrences-and-induction"],"address-chunk-interchange",mq="An edge matrix of rank $a$ will require $a$ smaller interchanges.",
 adds=[("e","chunk width","The number of radix-q digits in each of the two chunks, a power m^k.",C),
       ("W","wire count","The number of wire roles, hence of role streams.",C)])

KB1=sh("KB.1","A simultaneous $C$-layer on $e=mf$ axes needs $s_{\\rm c}$ smaller $C$-layers on $f$ axes, and $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
 "express each edge's phase frame change as a product of two-point kernels $C=aI+bX$ in an orthonormal basis of the residual, conjugated by a binary basis change",
 "The phase identities express an edge's residual operator as a product of two-point kernels on selected directions.","explicit",
 [inf("KB.1a","The kernel is $C=H\\mathsf SH=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$.","C=H\\mathsf SH=aI+bX"),
  inf("KB.1b","Then $H_0=b\\mathsf SC\\mathsf S$, $C^2=X$ and $C^4=I$.","H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,"),
  inf("KB.1c","An edge's frame change is a product of one kernel $(aI+bX_{v_j})^{\\epsilon_j}$ per vector of an orthonormal basis of its residual.","=\\prod_{j=1}^{\\rho_{\\rm edge}}(aI+bX_{v_j})^{\\epsilon_j},"),
  inf("KB.1d","Conjugating by a binary basis change $\\mathcal P_M$ puts the residual basis in the first coordinate directions.","=\\mathcal P_M\\left(\\prod_{j=1}^{\\rho_{\\rm edge}}C_{e_j}^{\\epsilon_j}\\right)"),
  inf("KB.1e","A group of $e=mf$ axis chunks is divided into $m$ slots of $f$ chunks; each kernel becomes one child on the $f$ axes of a slot.","For the array layout used below, take a group of $e=mf$ consecutive"),
  inf("KB.1f","A negative kernel needs only one forward child, since $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$.","=(-i)^f Z^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}."),
  inf("KB.1g","The network gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.","$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
  inf("KB.1h","Applying the identities on all selected coordinates gives $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.","H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.")],
 ["common-frame-principle","subset-intersection-labels","rank-saving-recurrence","butterfly","complex-numbers","finite-field-f2-arithmetic"],"phase-frame-kernel",mq="phase identities below express an edge's residual operator as a product of",
 adds=[("C","two-point kernel","The 2x2 matrix aI+bX applied to one selected bit.",D),
       ("D","layer width","The number of selected axes in the simultaneous layer.",C),
       ("f","slot width","The number of chunks in one of the m slots of a group.",C)])

KB2=sh("KB.2","Adding the bit at the same position $j_i=\\rho+iK$ of chunk $x$ into chunk $y$ for $0\\le i<f$ takes $O(V(L^\\tau+1))$ with $L=fK$, restoring chunk $z$.",
 "perform eight cyclic shifts that add packed segments with no carries between them, then repair the explicitly bounded set of exceptional addresses by sorting",
 "A binary row addition on corresponding selected bits is needed to implement the binary basis changes.","explicit",
 [inf("KB.2a","The rectangle has chunks of $L=fK$ bits with $K\\ge6$, $f\\ge1$ and selected offset $0\\le\\rho<K$.","Let $R\\ge1$, $K\\ge6$, $f\\ge1$, $L=fK$, and $0\\le\\rho<K$."),
  inf("KB.2b","The procedure performs $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ for $0\\le i<f$ and restores the chunk $z$ for every initial value.","y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}"),
  inf("KB.2c","The bad fraction is $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$ and the time is $O(V(L^\\tau+1)+MA_{\\rm rect}^3+\\delta_{\\rm bad}MA_{\\rm rect}(R+A_{\\rm rect}))$.","With $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$, its time is"),
  inf("KB.2d","The eight conditional additions to $u,w$ with control $c$ give $(u',w')=(u+c(1-2(u\\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$ and $w$ is restored.","\\bigl(u+c(1-2(u\\bmod2)),\\ w\\bigr)."),
  inf("KB.2e","Each line is one cyclic shift of the target chunk by an offset that does not depend on that chunk, so it is a bijection of the rectangle.","The shift offset never depends on its target chunk, so each line is a"),
  inf("KB.2f","Exceptional addresses, where segments could carry into each other, form a set $\\mathcal B$ with $|\\mathcal B|\\le\\delta_{\\rm bad}M$.","|\\mathcal B|\\le\\delta_{\\rm bad}M."),
  inf("KB.2g","Each exceptional address $q$ is repaired deterministically by computing its destination $q'$ and sorting the extracted records, which is negligible when $K/\\log p\\to\\infty$.","For a current exceptional address $q$, compute")],
 ["address-chunk-interchange","controlled-shift","elementary-stream-ops","modular-arithmetic"],"packed-selected-bit-addition",mq="We implement a binary row addition on corresponding selected bits in two")

KB3=sh("KB.3","A normalized layer on $D$ selected axes of $e\\le d$ chunks costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
 "recurrence on the number $e$ of axes: $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, stopping at $e<d^\\beta$, summed over a base-$m$ partition of $D-q_0$",
 "Each child call acts on volume V/W, so after dividing by volume the recursion gains the factor s/W per level.","recoverable",
 [inf("KB.3a","An internal node of $e=m^k$ chunks is split into $m$ slots of $e/m$ chunks and makes exactly $s$ child calls.","First consider an internal node containing \\(e=m^k\\) consecutive"),
  inf("KB.3b","Basis changes, scalar gates and reassembly cost $O(V((eK)^\\tau+1))$ at the node.","O\\bigl(V((eK)^\\tau+1)\\bigr)"),
  inf("KB.3c","Case $D\\le q_0$: use individual $C$ kernels at cost $O(V\\log d)$.","If \\(D\\le q_0\\), use individual \\(C\\) kernels, at cost \\(O(V\\log d)\\)."),
  inf("KB.3d","Otherwise the first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks are done individually and serve as row index of range $2^{q_0K}\\ge W^{k_0}$, $k_0=\\lceil\\log_md\\rceil$.","length \\(R_{\\rm row}=2^{q_0K}\\ge W^{k_0}\\), since \\(K\\ge1\\) for sufficiently"),
  inf("KB.3e","A row index $u=Wg+w$ sends the whole row to role $w$, so every child has volume exactly $1/W$ of its parent's.","one role stream with volume exactly \\(1/W\\) of its parent's logical"),
  inf("KB.3f","With $\\beta=1/2$ and $\\max\\{\\tau,\\sigma\\}<\\lambda<1$, $\\tau(1+c/\\beta)<\\lambda$: $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ and $F(e)=O(e)$ for $e<d^\\beta$.","F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
  inf("KB.3g","At an internal node $e\\ge d^\\beta$, so $K\\le d^c\\le e^{c/\\beta}$ and the overhead is $O(e^{\\tau(1+c/\\beta)}+1)=O(e^\\lambda)$.","O(e^{\\tau(1+c/\\beta)}+1)=O(e^\\lambda)"),
  inf("KB.3h","Since $a=s/W\\le m^\\sigma<m^\\lambda$ the internal costs sum to $Ce^\\lambda\\sum_j(a/m^\\lambda)^j=O(e^\\lambda)$.","C e^\\lambda\\sum_{j\\ge0}(a/m^\\lambda)^j=O(e^\\lambda)."),
  inf("KB.3i","Leaves with $u=e/m^j<d^\\beta$ chunks contribute $O(a^ju)\\le O(e^\\sigma d^{\\beta(1-\\sigma)})$ using $a^j\\le m^{j\\sigma}=(e/u)^\\sigma$.","O(e^\\sigma d^{\\beta(1-\\sigma)})."),
  inf("KB.3j","Writing $D-q_0=\\sum_ja_jm^j$ in base $m$ splits the remaining chunks into at most $(m-1)(1+\\lfloor\\log_md\\rfloor)$ pieces.","Write \\(D-q_0=\\sum_j a_jm^j\\) in base \\(m\\), with \\(0\\le a_j<m\\)."),
  inf("KB.3k","Adding the pieces gives $O(\\log(2d)[d^\\lambda+d^{\\sigma+\\beta(1-\\sigma)}+1])=O(d^{\\lambda'})$ for any fixed $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.","bigl[d^\\lambda+d^{\\sigma+\\beta(1-\\sigma)}+1\\bigr]\\right)")],
 ["recurrences-and-induction","rank-saving-recurrence","phase-frame-kernel","packed-selected-bit-addition"],
 adds=[("d","axis count","The maximum number of simultaneous axes, d = Theta(p^epsilon).",C),
       ("K","chunk width","The number of address bits in each chunk, K = floor(d^c).",C),
       ("\\lambda","intermediate exponent","An exponent between max(tau,sigma) and 1 bounding the node overhead.",D),
       ("\\lambda'","layer exponent","The exponent in the final bound O(V d^{lambda'}).",D),
       ("\\beta","stopping exponent","The constant 1/2 such that recursion stops at e < d^beta.",D),
       ("q_0","row chunks","The number of leading chunks used as row index.",C)])

KB4=sh("KB.4","The whole normalized layer is evaluated exactly with $O(p)$-bit guarded dyadics and followed by a single truncation $Q_p$, with error below $\\sqrt2\\,2^{-p}$.",
 "keep all intermediate values as exact Gaussian dyadics with guard bits and truncate once",
 "A single truncation after the completed contractive layer keeps the error at one rounding.","explicit",
 [inf("KB.4a","The layer parameters satisfy $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$ and $\\epsilon C_1<1$.","\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1,"),
  inf("KB.4b","The procedure returns $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time.","coefficient order, and component format in $O(Vd^{\\lambda'})$ time,"),
  inf("KB.4c","It uses at most $p+\\lceil C_0d^{C_1}\\rceil$ fractional bits, which is $o(p)$ extra since $\\epsilon C_1<1$.","at most $p+\\lceil C_0d^{C_1}\\rceil$ fractional bits and"),
  inf("KB.4d","Every row of $\\mathcal H$ has absolute row sum one, so $\\mathcal H$ maps disk arrays to disk arrays and truncation errs by less than $\\sqrt2\\,2^{-p}$.","absolute row sum one. Thus $\\mathcal H$ maps disk arrays to disk")],
 ["fixed-point-truncation","butterfly","norms-absolute-values-and-error-bounds"],
 mq="truncation follows the completed contractive layer.")

KB=sh("KB","Applying $H_0$ at the same bit offset in $d$ address chunks of a polynomial-record array costs $O(Vd^{\\lambda'})$ for fixed $\\lambda'<1$.",
 "evaluate the layer exactly through the phase-frame network, with the same recursive rank saving and packed chunk moves for the binary basis changes",
 "Splitting complete rows among the network's wire roles reduces the volume of each recursive call.","explicit",
 [KB1,KB2,KB3,KB4],
 ["rank-saving-recurrence","phase-frame-kernel","packed-selected-bit-addition","address-chunk-interchange","fixed-point-truncation","butterfly","polynomial-ring-mod"],"fast-butterfly-layer",mq="the network's wire roles then reduces the volume of each recursive")

K=sh("K","Running a fixed linear exchange network with $s<Wm$ smaller calls per invocation, each on a role stream of volume $V/W$, gives cost per volume $F=O(e^\\tau)$ with $\\tau<1$, a power saving in the parameter $e$.",
 "build a linear network whose frame changes are smaller calls of the same procedure, show the call count satisfies $s<Wm$, then unroll the recurrence $F_k\\le(s/W)F_{k-1}+O(1)$; carry it out for the bit network (address interchange) and the complex network (butterfly layer)",
 "Multiplying the parameter by m multiplies the recursive contribution by s/W<m, which is the source of the power saving.","explicit",
 [K1,K2,K3,K4,KA,KB],
 ["linear-network","common-frame-principle","subset-intersection-labels","address-shear","linear-algebra-basics","recurrences-and-induction","tape-address-model","elementary-stream-ops","controlled-shift"],"rank-saving-recurrence",
 mq="increases the recursive contribution by $s/W<m$. This strict inequality",
 salient="A saving of a power e^tau, tau<1, rather than a constant factor: the per-level growth s/W of the recursion is strictly less than the branching m of the parameter, because s<Wm. The exponent tau = 1-2^{-50} is tiny but fixed, and the same count works for scratch wires with arbitrary contents.",
 adds=[("m","label dimension","The dimension h^3 of the label space F tensor 3, equal to the factor by which the parameter shrinks per level.",C),
       ("W","wire count","The number of wires of the network, equal to the number of role streams.",C),
       ("F_k","cost per volume","The time divided by logical volume for a call at parameter m^k.",D)])

R1=inf("R1","Splitting the inputs into radix-$2^b$ digits reduces integer multiplication to a convolution of short integer coefficients, each below $2^{3b}$.",
 "Splitting the inputs into radix digits reduces multiplication to",["cyclic-convolution","polynomials","binary-representation-and-bit-operations"],"radix-digit-convolution")

S1=sh("S1","A normalized transform over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with root $\\omega_t=y^{2r/t}$ is computed by radix-two butterfly rounds in bit-reversed order, and its opposite consumes that order.",
 "decimation in frequency with twiddle monomials, then reverse the rounds for the opposite transform",
 "The opposite transform consumes the same stored frequency order after a pointwise product.","explicit",
 [inf("S1.1","For a power of two $t$ dividing $2r$ put $\\omega_t=y^{2r/t}$; multiplication by it is a signed coefficient shift.","For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$."),
  inf("S1.2","Character cancellation gives $F_t^+F_t^-=t^{-1}I$ although $\\mathcal R_r$ has zero divisors.","F_t^+F_t^-=t^{-1}I."),
  inf("S1.3","The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, and multiplies the $b=1$ output by $\\omega_t^{-k}$.","decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"),
  inf("S1.4","After all rounds the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$, the bit-reversed position.","entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$."),
  inf("S1.5","The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, so the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.","B_tF_t^-,\\qquad F_t^+B_t^{-1},"),
  inf("S1.6","With the layout, one transform of $T$ entries costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ and has error less than $\\sqrt2\\ell2^{-p}$.","O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right).")],
 ["polynomial-ring-mod","dft","butterfly","multidimensional-dft","address-chunk-interchange"],"synthetic-transform",mq="We now implement the normalized Fourier transforms needed for")

S2=sh("S2","Two disk-grid polynomials in $\\mathcal R_r$ are multiplied exactly with four integer products of $O(rp)$ bits in time $O(rp\\log(rp))$.",
 "evaluate coefficients at $B_0=2^{4p}$ to get integers, multiply with the established multiplier, read back by centered residues",
 "It is a signed form of Kronecker substitution.","explicit",
 [inf("S2.1","The numerators of $fg$ and then $Q_p(fg/r)$ are computed in time $O(rp\\log(rp))$ on a fixed number of tapes.","$O(rp\\log(rp))$ on a fixed number of tapes."),
  inf("S2.2","Set $B_0=2^{4p}$ and $A_u=u(B_0)$ for $u\\in\\{a,b,c,e\\}$.","Set $B_0=2^{4p}$"),
  inf("S2.3","Every product coefficient obeys $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so centered residues modulo $B_0$ identify coefficients.","|h_j|\\leq r2^{2p}<2^{3p}<B_0/2.")],
 ["established-multiplier","polynomial-ring-mod","fixed-point-truncation"],"signed-packing",mq="reduction is a signed form of Kronecker substitution; compare")

S3=sh("S3","Normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathcal R_r$ on $d-1$ axes is computed from two forward synthetic transforms in the same order, pointwise products divided by $r$, and the opposite transform.",
 "transform, multiply pointwise by signed packing, and transform back, using the convolution theorem",
 "Retaining the frequency order lets the opposite transform consume it without any sort.","recoverable",
 [inf("S3.1","$\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}$ is a bilinear contraction.","\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}."),
  inf("S3.2","The error is less than $\\sqrt2M(3\\ell+1)2^{-p}$.","\\sqrt2\\,M(3\\ell+1)2^{-p}"),
  inf("S3.3","The cost is $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.","+\\log(rp)\\right]\\right)."),
  inf("S3.4","Perform both forward transforms and retain their common order, multiply by Lemma S2, then apply the opposite procedure.","Perform both forward transforms and retain their common $LB$ order."),
  inf("S3.5","Multiply the result exactly by $M=T/r$.","to that order, and multiply its result exactly by $M=T/r$."),
  inf("S3.6","The convolution theorem $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$ gives the normalization.","=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g).")],
 ["synthetic-transform","signed-packing","cyclic-convolution","dft"],"ring-convolution")

R3=sh("R3","Convolution over the polynomial ring $\\mathbb C[y]/(y^r+1)$ is available at cost $O(Tp[\\cdot])$ using the fast layers.",
 "build the synthetic transforms from the fast layers and chunk swaps, then multiply pointwise",
 "The sources apply the simultaneous layers on a suitable tape layout and retain the resulting frequency order through convolution.","explicit",
 [S1,S2,S3],["fast-butterfly-layer","address-chunk-interchange","polynomial-ring-mod"],mq="The work here is to apply the simultaneous layers on a suitable tape")

G=sh("G","Gaussian resampling expresses $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ for prime $s<t$ with $t$ a power of two, and tensors over $d$ axes with $\\gamma=2d\\alpha^2$.",
 "contract Gaussian-weighted maps $A,B_0$ around a longer power-of-two transform, keeping the two coordinate permutations inside the identity",
 "Its usual implementation sorts twice on each coordinate; retaining both permutations avoids full sorts.","explicit",
 [inf("G.1","Resampling needs $\\theta:=t/s-1>p/\\alpha^4$ with $\\gcd(s,t)=1$.","\\theta:=t/s-1>p/\\alpha^4."),
  inf("G.2","The permutations are $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$.","(P_su)_j=u_{tj},\\qquad (P_tv)_k=v_{-sk}."),
  inf("G.3","There are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.","P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."),
  inf("G.4","Approximations of $A,B_0$ have error less than $p^2$ and time $O(tp^{3/2+\\delta}\\alpha)$ per line.","O(tp^{3/2+\\delta}\\alpha)."),
  inf("G.5","Tensoring: $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $R,Q$ the tensor permutations.","=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,"),
  inf("G.6","The total line cost is $O(dTp^{3/2+\\delta}\\alpha)$, independent of $d$ in the constant.","$O(dTp^{3/2+\\delta}\\alpha)$, with a constant independent of $d$.")],
 ["dft","multidimensional-dft","norms-absolute-values-and-error-bounds","established-multiplier"],"gaussian-resampling",mq="whereas the synthetic transforms use powers of two. Gaussian resampling")

B=sh("B","The permuted transform is a chirp-weighted cyclic convolution: $QF_{\\boldsymbol t}u=\\bar a\\cdot(a*(\\bar a\\cdot u))/T$ with $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$.",
 "check the coefficient of $u_{\\boldsymbol k}$ on both sides: the chirps combine to $\\exp(2\\pi i\\sum s_ij_ik_i/t_i)$",
 "A transform with its target permutation turns into a normalized convolution that the ring convolution can compute.","recoverable",
 [inf("B.1","Define $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$; it has period $t_i$ because every $t_i$ is even.","=\\exp\\left(-\\pi i\\sum_{i=1}^d\\frac{s_i j_i^2}{t_i}\\right)."),
  inf("B.2","$QF_{\\boldsymbol t}u=\\bar a\\cdot\\frac{a*(\\bar a\\cdot u)}{T}$.","\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}."),
  inf("B.3","The coefficient of $u_{\\boldsymbol k}$ is $\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$, which is what $Q$ reads from the negative-sign transform.","=\\frac1T\\exp\\left(2\\pi i\\sum_i")],
 ["roots-of-unity","dft","cyclic-convolution","multidimensional-dft"],"bluestein-chirp")

PC=sh("PC","The source permutation cancels: $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$ with $S=\\prod_is_i$.",
 "use $RF^+R=F^+$ and the convolution rule",
 "We retain both permutations in the transform formula and compute it directly.","explicit",
 [inf("PC.2","Since each $t_i$ is a unit modulo $s_i$, $F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$.","$F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence"),
  inf("PC.3","Hence $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$ and permutations commute with pointwise products.","$RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$."),
  inf("PC.4","With $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)(F_{\\boldsymbol s}v)$ and $F^+F=I/S$ the result is $(u*v)/S^2$.","=\\frac{u*v}{S^2},"),
  inf("PC.5","So $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)(RF_{\\boldsymbol s}v)]=(u*v)/S^2$, the source permutation having cancelled.","proving \\eqref{eq:source-permutation-cancel}.")],
 ["dft","multidimensional-dft","gaussian-resampling","primes-coprimality-and-gcd","permutations-and-cartesian-products"],"permutation-cancellation",mq="coordinate. We retain both permutations in the transform formula and")

R4=sh("R4","The pairwise coprime (prime-length) source transforms are expressed through the power-of-two synthetic transforms by Gaussian resampling, with permutations retained and the middle transform made a convolution.",
 "Gaussian resampling, then Bluestein chirp, then permutation cancellation",
 "The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two.","explicit",
 [G,B,PC],["dft","multidimensional-dft"],mq="The transform lengths needed for the integer product are pairwise coprime,")

PR=sh("PR","The parameters are $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, padded size $T\\in[4n/b,8n/b)$, axis lengths $t_i\\in\\{r/2,r\\}$ and primes $s_i$ just below $t_i$ with $T/2<S<T$.",
 "fix rational exponents, derive all sizes from $n$, and check by prime-interval estimates that the resampling hypotheses hold",
 "The distinct prime lengths must be close to the powers of two so that their product fills a fixed fraction of the box while leaving enough separation for resampling.","explicit",
 [inf("PR.1","The exponents are $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$, $\\delta=1/16$.","\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16},"),
  inf("PR.2","Further $\\lambda=1-2^{-52}$ and $c=2^{-56}$.","\\lambda=1-2^{-52},\\qquad c=2^{-56},\\qquad"),
  inf("PR.3","And $\\lambda'=1-2^{-54}$.","\\lambda'=1-2^{-54},"),
  inf("PR.4","Finally $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$.","C_1=20,\\qquad \\epsilon=2^{-75},\\qquad \\kappa=2^{-182}."),
  inf("PR.5","Put $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$.","b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
  inf("PR.6","Take the power of two $T\\in[4n/b,8n/b)$.","Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
  inf("PR.7","Choose axis lengths $t_i\\in\\{r/2,r\\}$ with $\\prod_it_i=T$ and $t_d=r$.","t_i\\in\\{r/2,r\\},\\qquad \\prod_i t_i=T,\\qquad t_d=r."),
  inf("PR.8","Then $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$, $r=2^{\\Theta(p^{1-\\epsilon})}$.","Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),\\quad"),
  inf("PR.9","Set $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, $\\gamma=2d\\alpha^2$, $\\eta=1/(4d)$.","\\alpha=\\left\\lceil(12d^2b)^{1/4}\\right\\rceil,"),
  inf("PR.10","The interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains many primes for $x=r/2$ and $x=r$.","(1-2\\eta)x<q\\leq(1-\\eta)x"),
  inf("PR.11","Choose distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$.","(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i."),
  inf("PR.12","By Bernoulli, $S/T>(1-1/(2d))^d>1/2$ and hence $T/2<S<T$.","Together with $s_i<t_i$, this gives $T/2<S<T$."),
  inf("PR.13","Then $\\alpha^4\\theta_i>3db\\ge6b=p$, so the resampling hypothesis holds.","\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\geq6b=p."),
  inf("PR.14","The product has degree $2q-2<2n/b\\le T/2<S$, so cyclic convolution modulo $x^S-1$ has no wraparound.","2q-2<2n/b\\le T/2<S."),
  inf("PR.15","Every product coefficient obeys $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.","0\\le c_j\\le q(2^b-1)^2<2^{3b},")],
 ["radix-digit-convolution","gaussian-resampling","primes-coprimality-and-gcd","logarithms-and-iterated-logarithm-notation","floor-ceiling-and-summation-notation","fast-butterfly-layer","address-chunk-interchange"],"parameter-choice",mq="while each ratio $t_i/s_i$ must leave enough separation for resampling.",
 adds=[("b","digit size","The radix exponent b=ceil(log2 n) of the input digits.",D),
       ("p","precision","The number of fractional bits 6b of the fixed-point grid.",C),
       ("T","padded size","The power of two in [4n/b, 8n/b) equal to the product of the axis lengths.",D),
       ("t_i","axis length","The length of axis i, either r/2 or r.",D),
       ("s_i","prime length","The distinct prime just below t_i used as a source axis length.",D),
       ("S","source size","The product of the s_i, between T/2 and T.",D),
       ("\\ell","log record length","The base-two logarithm of the record length r.",D),
       ("\\epsilon","axis exponent","The exponent 2^{-75} with d about p^epsilon.",D),
       ("c","chunk exponent","The exponent 2^{-56} with K about d^c.",D),
       ("\\alpha","resampling parameter","The Gaussian width parameter of order p^{1/4+epsilon/2}.",D)])

CR=sh("CR","The Agarwal--Cooley map $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ is an isomorphism $\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$ preserving convolution, computed with triangular controlled shifts in $O(Tp\\,d^2(1+\\ell^\\tau))$.",
 "write the index mixed-radix and update axes from last to first with prefix-controlled cyclic shifts",
 "The Chinese remainder theorem converts one cyclic convolution into multidimensional cyclic convolution.","explicit",
 [inf("CR.1","Put $P_i=\\prod_{j<i}s_j$ and $\\mu_i=P_i^{-1}\\pmod{s_i}$.","P_i=\\prod_{j<i}s_j,\\qquad \\mu_i=P_i^{-1}\\pmod{s_i}."),
  inf("CR.2","Define $\\Phi$ by $x\\mapsto\\prod_ix_i^{\\mu_i}$.","\\qquad x\\longmapsto\\prod_i x_i^{\\mu_i}"),
  inf("CR.3","The image of $x$ has order $S$, so its powers run through all target monomials once and $\\Phi$ is an isomorphism preserving cyclic convolution.","$\\Phi$ is an isomorphism and preserves cyclic convolution."),
  inf("CR.4","With $k=\\sum_ja_jP_j$ the axis-$i$ coordinate of $\\Phi(x^k)$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$.","b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}."),
  inf("CR.5","Updating targets in the order $i=d,d-1,\\dots,1$ uses the original lower digits; each update is a prefix-controlled cyclic shift on the valid interval $[0,s_i)$.","order $i=d,d-1,\\ldots,1$ using \\eqref{eq:triangular-crt}."),
  inf("CR.6","Reversing the $d$ axes costs $O(d^2)$ adjacent swaps, so $\\Phi$ costs $O(Tp\\,d^2(1+\\ell^\\tau))$.","O\\bigl(Tp\\,d^2(1+\\ell^\\tau)\\bigr).")],
 ["chinese-remainder-theorem","controlled-shift","address-chunk-interchange","cyclic-convolution","modular-arithmetic"],"crt-address-map",mq="theorem to convert one cyclic convolution into multidimensional cyclic")

PT=sh("PT","The twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ is an isomorphism $\\mathbb C[x_d]/(x_d^r-1)\\to\\mathcal R_r$ whose negative wrap restores the cyclic wrap after untwisting.",
 "multiply coefficient $k$ by $\\zeta^k$ and check the wrap sign case by case ($h\\in\\{0,1\\}$)",
 "The power-of-two complex convolution of the chirp identity is obtained from the synthetic convolution by a coefficient twist.","explicit",
 [inf("PT.1","The map $x_d\\mapsto\\zeta y$ is well defined since $(\\zeta y)^r=(-1)(-1)=1$.","\\qquad x_d\\longmapsto\\zeta y"),
  inf("PT.2","On the coefficient bases it is diagonal, multiplying coefficient $k$ by $\\zeta^k$.","multiplying coefficient $k$ by the nonzero number $\\zeta^k$."),
  inf("PT.3","For $k+l=j+hr$ with $h\\in\\{0,1\\}$, the factor is $\\zeta^{k+l}(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient.","\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j."),
  inf("PT.4","Hence $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",":=D_-\\iota^{-1}")],
 ["polynomial-ring-mod","roots-of-unity","complex-numbers"],"phase-twist",mq="The power-of-two complex convolution used in the chirp identity is")

MA=sh("MA","The multiplication algorithm turns radix digits into the exact product by $\\Phi$, two source transforms, a pointwise product, the opposite transform, two rescalings, rounding and carries.",
 "run the pipeline of the flow figure and read off that the two scales $S$ and $2^{2b+4}$ undo the normalizations",
 "Each stage reduces to the next problem: digits, prime axes, power-of-two axes, polynomial ring.","recoverable",
 [inf("MA.1","Apply $\\Phi$ with padded layout to obtain the source arrays $u,v$.","\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"),
  inf("MA.2","Compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$ by resampling, chirp convolution and resampling.","\\item Compute $\\widetilde{\\mathscr F}(u)$ and"),
  inf("MA.3","Multiply corresponding coefficients exactly and truncate to $p$ fractional bits.","\\item Multiply corresponding complex coefficients exactly and truncate"),
  inf("MA.4","Compute the opposite transform of the product and multiply by $S$.","\\item Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
  inf("MA.5","Multiply by $2^{2b+4}S$ and round to the nearest integer.","\\item Multiply the grid numerators of $\\widetilde w$ exactly by"),
  inf("MA.6","Propagate radix-$2^b$ carries and output exactly $2n$ bits.","\\item Propagate radix-$2^b$ carries in increasing coefficient order."),
  inf("MA.7","The two occurrences of $S$ undo different normalizations; after the first scale the exact value is $w=(u*v)/S$.","The two occurrences of $S$ in this algorithm undo different"),
  inf("MA.8","The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\\Phi$ is the original integer coefficient convolution.","$2^{2b+4}(u*v)$, whose inverse image under $\\Phi$ is the original")],
 ["crt-address-map","gaussian-resampling","bluestein-chirp","permutation-cancellation","phase-twist","ring-convolution","radix-digit-convolution","parameter-choice"],"multiplication-algorithm")

ER=sh("ER","The accumulated coefficient error is below $1/2$, so rounding gives the exact integer coefficients and carries yield the $2n$-bit product.",
 "track the error through each contraction in units of $2^{-p}$, then bound it after the final scales",
 "The error must be strictly below one half for the nearest integer to be the unique correct coefficient.","explicit",
 [inf("ER.1","Each synthetic transform has error less than $\\sqrt2\\ell2^{-p}<L2^{-p}$ with $L=\\log_2T$.","$\\sqrt2\\ell\\,2^{-p}<L2^{-p}$, where $L=\\log_2T$, for all"),
  inf("ER.2","Ring convolution error is $E_{\\rm ring}:=M(3L+2)<5TL$.","E_{\\rm ring}:=M(3L+2)<5TL."),
  inf("ER.3","The first scaling gives $w=(u*v)/S$ with error below $E_w=S(3E_s+2)<28\\,2^\\gamma T^2L$.","E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L."),
  inf("ER.4","After the second scaling the final error is less than $448b\\,2^{-3b/4}<1/2$.","<448b\\,2^{-b+\\gamma}"),
  inf("ER.5","The strict error below $1/2$ makes the nearest integer the unique correct coefficient, fitting in a $(3b+1)$-bit word.","The strict error below $1/2$ makes the nearest integer to")],
 ["fixed-point-truncation","norms-absolute-values-and-error-bounds","radix-digit-convolution"],"exact-recovery",mq="disk bounds needed by every call and proves that the final error is")

rows=[("Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$","Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, power $\\epsilon(1+c)$ of $p$."),
("Chunk exchanges for transform layout & $pK^{\\tau-1}$ & $1-\\epsilon c(1-\\tau)$","Chunk exchanges for layout cost $pK^{\\tau-1}$, power $1-\\epsilon c(1-\\tau)$ of $p$, from $O(p/K)$ width-$K$ exchanges each $O(VK^\\tau)$."),
("Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$","The at most $\\ell$ simultaneous rounds cost $\\ell d^{\\lambda'}$, power $1-\\epsilon(1-\\lambda')$ of $p$."),
("CRT and axis layouts & $d^2(1+\\ell^\\tau)$ & $\\tau+\\epsilon(2-\\tau)$","CRT and axis layouts cost $d^2(1+\\ell^\\tau)$, power $\\tau+\\epsilon(2-\\tau)$ of $p$."),
("Gaussian line maps & $dp^{1/2+\\delta}\\alpha$ & $3/4+\\delta+3\\epsilon/2$","Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, power $3/4+\\delta+3\\epsilon/2$ of $p$."),
("Chirps, twists and scalar products & $dp^\\delta$ & $\\epsilon+\\delta$","Chirps, twists and scalar products cost $dp^\\delta$, power $\\epsilon+\\delta$ of $p$."),
("Packed polynomial products & $\\log(rp)$ & $1-\\epsilon$","Packed polynomial products cost $\\log(rp)$, power $1-\\epsilon$ of $p$.")]
TAch=[inf("TA.%d"%(i+1),c,q) for i,(q,c) in enumerate(rows)]
TAch+= [inf("TA.8","The seven margins below one are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4=1-\\tau-\\epsilon(2-\\tau)$, $g_5=1/4-\\delta-3\\epsilon/2$, $g_6=1-\\delta-\\epsilon$, $g_7=\\epsilon$.","g_1&=1-\\epsilon(1+c),\\qquad"),
 inf("TA.9","Substitution gives $g_2=2^{-181}$, $g_3=2^{-129}$, $g_7=2^{-75}$, $g_4>2^{-51}$, and the rest larger, so $\\min_ig_i=2^{-181}=2\\kappa$.","Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
 inf("TA.10","Each of the seven powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.","Each of the seven displayed powers is at most $1-2\\kappa$ by"),
 inf("TA.11","Hence the total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.","O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})."),
 inf("TA.12","Below a fixed cutoff use schoolbook multiplication, giving worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every $n$.","$O(n(\\lg n)^{1-\\kappa})$ for every input length and produces precisely")]
TA=sh("TA","Dividing every cost by $V=Tp=\\Theta(n)$, the seven dominant powers of $p$ are each at most $1-2\\kappa$ with $\\kappa=2^{-182}$, giving total time $O(n(\\lg n)^{1-\\kappa})$.",
 "tabulate the normalized cost of every stage as a power of $p$ and compare each with $1-2\\kappa$",
 "The explicit slack of the smallest margin covers any remaining fixed power of log p.","explicit",
 TAch,["parameter-choice","address-chunk-interchange","fast-butterfly-layer","crt-address-map","gaussian-resampling","ring-convolution","exact-recovery","big-o","big-omega-theta-and-little-o-notation"],"time-accounting",mq="This explicit slack will cover",
 salient="All seven dominant exponents leave a margin below one, and the smallest, 2^{-181} = 2 kappa, comes from the chunk-exchange row g_2 = epsilon c (1-tau), a product of the three tiny exponents epsilon=2^{-75}, c=2^{-56} and 1-tau=2^{-50}.")

R5=sh("R5","Placing the procedures inside the multiplication reduction, with every change of representation accounted for, gives the exact $2n$-bit product.",
 "choose parameters, map to prime axes, run the pipeline, and prove exact recovery",
 "The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation.","explicit",
 [PR,CR,PT,MA,ER],["ring-convolution","gaussian-resampling","permutation-cancellation"],mq="The remaining proof places these procedures inside the multiplication")

root=sh("S0","A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$.",
 "reduce multiplication to convolution, evaluate it with Fourier-type transforms whose address moves and butterfly layers are accelerated by recursive rank-saving networks, and add up the costs",
 "Scanning Theta(n) bits at each of Theta(log n) transform levels already costs n log n, so both movement and arithmetic must be sped up by a power of the log.","explicit",
 [R1,R2,K,R3,R4,R5,TA],
 ["integer-multiplication-conjecture","established-multiplier","polynomial-ring-mod","fixed-point-truncation","linear-algebra-basics","dft","multidimensional-dft","butterfly","cyclic-convolution","big-o","multitape-tm","logarithms-and-iterated-logarithm-notation"],"main-theorem",
 mq="We therefore need savings in both movement and arithmetic.",
 salient="The saving is a power of the logarithm, kappa = 2^{-182}, tiny but strict; it traces to the strict inequality s < Wm of the rank-saving networks.",
 adds=[("n","input length","The number of bits of each input integer.",C),
       ("\\kappa","saving exponent","The constant 2^{-182} by which the power of lg n is reduced.",D)])

json.dump({"root":root},open(P+'exegenius/tasks/0003-argument.answer.json','w'),indent=1)

# verification
src=open(P+'sources/paper.tex').read()
pos=0;bad=0
def walk(n):
    global pos,bad
    if n['intention']=='infer':
        q=n['quote']['quote'];i=src.find(q)
        if i<pos:
            j=src.find(q)
            print("ORDER/MISSING",n['id'],'present anywhere' if j>=0 else 'ABSENT',q[:60]);bad+=1
        else: pos=i
    else:
        for c in n['children']: walk(c)
walk(root)
def allq(n):
    m=n.get('motivation')
    if m and m.get('quote') and m['quote']['quote'] not in src: print("MOT ABSENT",n['id'])
    for c in n.get('children',[]): allq(c)
allq(root)
ids=[];
def col(n):
    ids.append(n['id']);[col(c) for c in n.get('children',[])]
col(root);print(len(ids),len(set(ids)),'bad',bad)
