import json, re, sys
P='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1W/'
SRC=open(P+'sources/paper.tex').read()

def ev(q): return {"source":"paper","quote":q}
def mot(text, src, q=None):
    return {"text":text,"source":src,"quote":ev(q) if q else None}
def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    return {"id":id,"intention":"show","claim":claim,"method":method,"motivation":motivation,
            "children":children,"page":page,"from":frm or [],"adds":adds or [],"salient":salient}
def infer(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    d={"id":id,"intention":"infer","claim":claim,"quote":ev(quote),"page":page,"from":frm or [],
       "salient":salient}
    if deferred: d["deferred"]=True
    return d
def B(symbol,name,meaning,rel="direct"):
    return {"symbol":symbol,"name":name,"meaning":meaning,"relation":rel}

# ---------------- S1: finite networks ----------------
network = show("S1.1",
 "For arbitrary initial scratch values, the eight-row copy/gather/scatter/side-injection schedule adds $x_S$ to $y_S$ and changes nothing else, and three such invocations exchange the two banks as $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ with every scratch wire restored.",
 "Check the eight-row schedule algebraically: the first two rows cancel the old scratch contribution, the middle rows add the source's effect, the last rows restore the scratch wires.",
 mot("Because the scratch wires start with arbitrary values, the schedule must cancel their effect before and after using them; a purely algebraic check of the rows shows the net map is independent of those values.","explicit",
     "the following schedule remove the effect of the old scratch values;"),
 [
 infer("S1.1.1","Rows 0 and 1 subtract the old side-injection and scatter contributions $\\mathcal J a+\\mathcal R c$ from $y$, where $a,c$ are the initial side and central scratch vectors.",
       "If the initial side and central vectors are $a,c$, the first two rows"),
 infer("S1.1.2","Rows 2 to 7 add $\\mathcal R(c+\\mathcal Gx)+\\mathcal J(a+\\mathcal Vx)$ and restore $c,a$, so the net change of $y$ is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, independent of $a,c$.",
       "Rows 6 and 7 restore $c,a$."),
 infer("S1.1.3","Over $\\mathbb F_2$ the central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod 2$; the side injection cancels the intersection-one neighbours, intersections zero and two already contribute zero, and the self coefficient is one, so the net map is $y\\gets y+x$.",
       "In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
 infer("S1.1.4","Over $\\mathbb Z[i,1/2]$ the central coefficient is $(|S\\cap T|-1)/2$; the side injection cancels it for intersections zero and two, intersection one contributes zero and the self coefficient is one, so again $y\\gets y+x$.",
       "In the complex case, the central coefficient is $(|S\\cap T|-1)/2$."),
 infer("S1.1.5","A forward invocation $X\\to Y$ at stage 1, the inverse schedule $Y\\to X$ at stage 2 and a forward invocation $X\\to Y$ at stage 3 send $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, restoring every scratch wire.",
       "The inverse schedule with logical source $Y$ and target $X$ effects"),
 ], page="network",
 frm=["boolean-gates-and-circuits","binary-field-f2-and-xor","sets-subsets-and-basic-combinatorics","dyadic-rationals-and-binary-fractions"])

frames = show("S1.2",
 "If each array on a wire is given an invertible address-space operator (a frame) at every vertex, and all incidences of a gate share one frame, then the network acts on the role arrays as $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$, so only the endpoint frames matter and each edge merely changes the frame.",
 "Maintain the invariant that the stored array is the frame applied to the logical array, and check it at sources, edges and pointwise gates.",
 mot("Once the scalar routing is fixed the endpoint frames determine the operator on every route, so the intermediate frames are free and can be chosen to make each edge cheap.","explicit",
     "intermediate frames can then be chosen to make each edge change inexpensive."),
 [
 infer("S1.2.1","At a vertex $v$ the stored array equals $D_v$ applied to the logical array; this holds at the sources by defining the logical input as $D_{\\rm in}^{-1}f$, and an edge $u\\to v$ changes $D_u\\varphi$ into $D_v\\varphi$ by applying $D_vD_u^{-1}$.",
       "At a vertex $v$, the invariant is that the stored array equals $D_v$ applied"),
 infer("S1.2.2","A pointwise linear gate commutes with a frame shared by all its incidences, because $R$-linearity gives $\\sum_j c_jD_v\\varphi_j=D_v(\\sum_j c_j\\varphi_j)$.",
       "Thus the common frame commutes with the pointwise gate, and"),
 infer("S1.2.3","The implemented operator is therefore the endpoint-frame sandwich $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$; for a signed role permutation, route $w$ applies $\\varepsilon_w D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$, for auxiliary roles too.",
       "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}."),
 ], page="frames",
 frm=["vectors-matrices-and-linear-maps","functions-bijections-and-permutations","network","array-order"],
 salient="The overall effect on each role depends only on the endpoint frames: all intermediate frames cancel, including on auxiliary roles carrying arbitrary scratch values.")

labels = show("S1.3",
 "Attaching to gates and terminals nondegenerate subspaces of the tensor-cube space $F^{\\otimes 3}$ built from indicator vectors of three-element subsets gives labels that are nested along every edge and orthogonal between neighbouring triples.",
 "Build the labels from indicator vectors $t_T$ of three-element subsets, whose pairings $|S\\cap T|-1$ make neighbouring triples orthogonal, tensor them three times and prescribe stage-by-stage transitions and a gate-label table.",
 mot("The labels must make every frame change cheap, which needs the label on one end of an edge to contain the label on the other; orthogonality of neighbouring triples is what makes the inclusions possible.","explicit",
     "choose its intermediate labels to make the changes of frame inexpensive."),
 [
 infer("S1.3.1","A label is a nondegenerate subspace of a fixed bilinear space, and on every edge one label contains the other; the orthogonal residual (complement of the smaller label in the larger) has dimension equal to the change in label dimension.",
       "A label is a nondegenerate subspace of a fixed bilinear space. On every"),
 infer("S1.3.2","For triple indicator vectors, $\\langle t_S,t_T\\rangle=|S\\cap T|-1$, so every triple line is nondegenerate and neighbouring triple lines are orthogonal in the label field of either construction.",
       "\\langle t_S,t_T\\rangle=|S\\cap T|-1,"),
 infer("S1.3.3","The ambient label space $\\mathcal F=F^{\\otimes 3}$ is nondegenerate of dimension $m$, with $U_a$ the line spanned by $u_a=t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$, and the terminal labels are $U_a,\\mathcal F$ on $X_a$, $0,U_a^\\perp$ on $Y_a$, and $0,\\mathcal F$ on scratch roles.",
       "The ambient label space is $\\mathcal F=F^{\\otimes3}$ with its tensor"),
 infer("S1.3.4","In stage $j$ the incoming and outgoing labels of the data wires fit together from stage to stage, with $A'=A\\otimes F$ and $P'=P\\otimes\\langle t\\rangle$, from $U_a,0$ at stage 1 to $\\mathcal F,U_a^\\perp$ at stage 3.",
       "We prescribe the following transition for each data wire in the stage,"),
 infer("S1.3.5","On a side wire the inclusion $P\\otimes\\langle t_X\\rangle\\subset P\\otimes t_Y^\\perp$ holds precisely because neighbouring triples are orthogonal.",
       "The first inclusion is possible because $t_X\\perp t_Y$."),
 infer("S1.3.6","The gate labels at the eight times of an invocation are given by the table, all tensored by $Q$ and nondegenerate, so each gate has one label common to all its wires.",
       "All labels are tensored by $Q$ and viewed as subspaces of $\\mathcal F$."),
 ], page="subset-labels",
 frm=["matrix-basics","sets-subsets-and-basic-combinatorics","vectors-matrices-and-linear-maps","network"])

rank = show("S1.4",
 "The total rank (number of smaller calls) of all edge differences of the bit network is $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$ with $L_{\\rm b}<N/2$, hence strictly below $W_{\\rm b}m$; the complex network satisfies $s_{\\rm c}<W_{\\rm c}m$ in the same way.",
 "Count dimension changes along the edges: signed changes telescope to $Wm-2N$, the decreasing edges add twice their total loss $L$, the $N$ negative source projections add $N$ more, and the loss ratio $L/N$ is exactly computed to be below $1/2$.",
 mot("The saving comes from keeping the total dimension lost on decreasing edges small relative to $N$, so the argument is an exact bookkeeping of dimension changes.","explicit",
     "The saving will come from keeping the total dimension lost on decreasing"),
 [
  show("S1.4.1",
   "Summing absolute dimension changes over all edges gives $Wm-2N+2L$, where the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$, so $L=Ich$.",
   "Telescope the signed dimension changes at every gate, then add twice the loss on the decreasing edges.",
   mot("At each gate every touched wire has the same label on its incoming and outgoing incidence, so signed changes cancel and only the terminals (sources of total dimension $N$, sinks $Wm-N$) contribute; absolute values differ from signed values only on decreasing edges.","recoverable"),
   [
   infer("S1.4.1.1","Every edge joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, with dimension loss $h$.",
         "Every edge joins comparable nondegenerate labels.  The only decreasing"),
   infer("S1.4.1.2","With $c$ central wires per invocation, $I$ invocations and $W$ wires in total, $L=Ich$ and the sum of absolute changes equals $Wm-2N+2L$.",
         "L=Ich,\\qquad"),
   infer("S1.4.1.3","Label dimension is nondecreasing along every edge except center $3\\to4$, which removes $P\\otimes F\\otimes Q$; the interstage edges and terminal labels create no other change.",
         "Label dimension is nondecreasing along every edge except center $3\\to4$, which removes"),
   infer("S1.4.1.4","The signed sum of dimension changes telescopes at every gate, because each touched wire has one incoming and one outgoing incidence with the same gate label.",
         "The signed sum of dimension changes telescopes at every gate: each"),
   infer("S1.4.1.5","The source dimensions sum to $N$ and the sink dimensions to $Wm-N$, so the signed increase is $Wm-2N$.",
         "The sum of source dimensions is $N$, while the sum of"),
   infer("S1.4.1.6","There are $Ic$ decreasing edges, each of loss $h$, and replacing signed by absolute changes adds $2L$.",
         "There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
   ], adds=[]),
  infer("S1.4.2","The loss ratios are exactly $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both smaller than $1/2$.",
        "In particular, both are smaller than $1/2$."),
  show("S1.4.3",
   "For the rational interface, each edge difference of projection matrices has rank equal to the change in label dimension, except on the $N$ negative source projections, which add rank one each.",
   "Assign the projection $P_U$ to every vertex of label $U$ and a negative projection to $X_a$ sources, then compute the rank of $M_{\\rm head}-M_{\\rm tail}$ edge by edge.",
   mot("The tape procedure needs rational matrices whose differences along edges have a small rank, so the label dimension count must be converted into a count of ranks, taking care of the one place where the matrix change is larger than the dimension change.","reconstructed"),
   [
   infer("S1.4.3.1","Each gate or sink with label $U$ gets the projection $P_U$ onto $U$ along $U^\\perp$, and each source $X_a$ gets $-P_{U_a}$ (all other sources get zero).",
         "Assign the source matrix $-P_{U_a}$"),
   infer("S1.4.3.2","For nondegenerate $U\\subset V$, $P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its orthogonal complement, so its rank is $\\dim V-\\dim U$, and reversing the edge only negates it.",
         "$P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its"),
   infer("S1.4.3.3","The only exceptions to rank equal to dimension change are the $N$ negative source projections.",
         "The only exceptions are the $N$ negative source projections."),
   infer("S1.4.3.4","At stage 1, $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so its first edge matrix is $2P_{U_a}$, of rational rank one, where the dimension change was zero.",
         "Its first edge matrix is therefore $2P_{U_a}$, of rational rank one,"),
   ]),
  infer("S1.4.4","Hence $s_{\\rm b}=\\sum_e\\operatorname{rank}_{\\mathbb Q}(M_{\\mathrm{head}(e)}-M_{\\mathrm{tail}(e)})=W_{\\rm b}m-N+2L_{\\rm b}$, whose deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
        "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
 ], page="rank-saving",
 frm=["matrix-basics","subset-labels","frames","network","vectors-matrices-and-linear-maps"],
 adds=[B("N","bank size","the number of entries in each data bank, equal to the sum of the source label dimensions","count"),
       B("L","dimension lost","the total dimension lost on the decreasing edges of the network","count")],
 salient="The deficit $Wm-s$ is strictly positive yet tiny (relative deficit $\\eta_{\\rm b}=339/22587335000000$): the whole power saving rests on $L<N/2$, because the only losses are the central edges from time 3 to time 4.")

bitnet = show("S1.5",
 "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates, sends its input to the permutation $\\rho$, and its rational matrices satisfy $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ for every input role $w$, with rank sum $s_{\\rm b}<W_{\\rm b}m$.",
 "Evaluate the endpoint matrix difference role by role.",
 mot("By the common-frame identity only the endpoint matrices matter on each route, so it suffices to compute sink minus source for each kind of role.","recoverable"),
 [
  infer("S1.5.1","For an input $X_a$ the endpoint difference is $P_{U_a^\\perp}-(-P_{U_a})=I_m$.",
        "$P_{U_a^\\perp}-(-P_{U_a})=I_m$"),
  infer("S1.5.2","Every other role has zero source matrix and identity sink matrix, so the same difference $I_m$ occurs on every role, including auxiliary ones.",
        "Every other role has zero source"),
 ], page="bit-network",
 frm=["rank-saving","frames","network","subset-labels","binary-field-f2-and-xor","modular-arithmetic"],
 salient="Every role, including the scratch roles with arbitrary contents, receives the same endpoint operator, the shear $(H,D)\\mapsto(H+D,D)$.")

phase = show("S1.6",
 "The complex phase network with binary labels has, on each edge, a frame change that is a product of one two-point kernel $aI+bX_v$ (or its inverse) per orthonormal residual vector, total length $s_{\\rm c}<W_{\\rm c}m$, and endpoint operator $C^{\\otimes m}$ on every role.",
 "Express the phase-frame change of each edge as a product of translation kernels over an orthonormal basis of the residual, count the kernels, and telescope the frames to the endpoints with correcting signs.",
 mot("The numerical butterfly layer needs the same recursive structure as the bit interchange, so one needs a network whose edges are products of two-point kernels and whose endpoints give the same operator on every role.","reconstructed"),
 [
  infer("S1.6.0","Every nonzero orthogonal residual of a binary label edge has an orthonormal basis, because it is nondegenerate and nonalternating (it contains a norm-one vector).",
        "For completeness, every nondegenerate nonalternating binary symmetric", deferred=True),
  infer("S1.6.1","For each edge the phase-frame difference $\\mathcal C_V\\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$, or its inverse, per vector $v$ of an orthonormal basis of the edge residual.",
        "$\\mathcal C_V\\mathcal C_U^{-1}$ is a product of one translation"),
  infer("S1.6.2","The sum of the basis lengths is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}<W_{\\rm c}m$.",
        "s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}"),
  infer("S1.6.3","After source and sink diagonal corrections and undoing the signed bank exchange, telescoping the phase frames gives $C^{\\otimes m}$ on every role, including auxiliary roles.",
        "telescoping these phase frames gives $C^{\\otimes m}$"),
  infer("S1.6.4","The one exceptional pair $X_a\\to Y_a$, whose operator carries $C^{-1}$ on the 27 coordinates of $\\operatorname{supp}(u)$, is repaired by $Z$-conjugation, since $C=iZC^{-1}Z$.",
        "the identity $C=iZC^{-1}Z$ turns each of them into $C$."),
 ], page="phase-network",
 frm=["network","frames","subset-labels","rank-saving","butterfly-fft","complex-numbers","binary-field-f2-and-xor","dyadic-rationals-and-binary-fractions"],
 salient="As for the bit network, every role including the auxiliary ones receives the same operator, here $C^{\\otimes m}$.")

S1 = show("S1",
 "Two fixed finite linear networks exchange two banks of values and restore every scratch wire, and the total number $s$ of smaller calls their frame changes require is strictly below $Wm$ (with $s_{\\rm b}<W_{\\rm b}m$, $s_{\\rm c}<W_{\\rm c}m$).",
 "Build a scalar exchange network, give each array on a wire an invertible frame so only endpoint frames matter, attach nested subspace labels to the gates, and count the rank of all frame changes.",
 mot("The saving of the whole paper rests on one property of these networks, that the total number of smaller calls is below the number of wires times the dimension.","explicit",
     "the subspace assignments. The decisive property is that the total"),
 [network, frames, labels, rank, bitnet, phase])

# ---------------- S2: chunk interchange ----------------
lowtri = show("S2.1.1",
 "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
 "Eliminate by pivots: choose the topmost nonzero row and its rightmost nonzero entry, clear its row and column with lower triangular elementary operations, delete the pivot row and column and repeat.",
 mot("Updates on tape can use earlier fields to change later ones, so only lower triangular operations are cheap; this is the Bruhat factorization with coordinate order reversed.","explicit",
     "can be performed entirely in this direction."),
 [
  infer("S2.1.1.1","If $A\\ne0$, choose the topmost nonzero row and its rightmost nonzero entry as pivot, clear the entries to its left by right multiplication and those below it by left multiplication by lower triangular elementary matrices, and scale the pivot to one.",
        "Otherwise choose the topmost"),
  infer("S2.1.1.2","Deleting the pivot row and column and repeating leaves lower triangular operations on the remaining indices, so the final partial permutation has exactly $a$ ones and $E_1=L^{-1}$, $E_2=R^{-1}$.",
        "Delete the pivot row and column from the active index sets, retaining"),
 ], page="lower-triangular", frm=["vectors-matrices-and-linear-maps"])

mshear = show("S2.1",
 "For a rational matrix $A$ of rank $a$, the shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ is performed by triangular controlled shifts and exactly $a$ interchanges of $b$-digit fields, plus $O(V)$ further work.",
 "Factor $A=E_1\\Pi E_2$, transform by the triangular factors in linear time, and realise each one of $\\Pi$ as $H_i\\leftarrow H_i+D_j$ using a single interchange sandwiched between two controlled shifts.",
 mot("A triangular change of coordinates can be done with controlled cyclic shifts in linear time, so the only expensive part of the shear is the partial permutation $\\Pi$, whose cost is the number $a$ of its ones.","explicit",
     "can be performed entirely in this direction."),
 [
  lowtri,
  infer("S2.1.2","A lower triangular transformation of $H$ or $D$ costs $O(V)$: update coordinates in descending physical order, multiplying by a diagonal unit and adding a fixed linear combination of earlier coordinates, by the controlled shifts lemma.",
        "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
  infer("S2.1.3","For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
        "For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
  infer("S2.1.4","Each one of $\\Pi$ at position $(i,j)$ is realised by $D_j\\leftarrow D_j+H_i$, then swapping $(H_i,D_j)$, then $D_j\\leftarrow H_i-D_j$, which sends $(h,d)$ to $(h+d,d)$.",
        "D_j\\leftarrow D_j+H_i,\\qquad"),
  infer("S2.1.5","This uses just one interchange per one of $\\Pi$, hence exactly $a$ interchanges, and the number of recursive calls is the rational rank $a$.",
        "It uses just one interchange."),
 ], page="matrix-shear",
 frm=["controlled-shifts","modular-arithmetic","vectors-matrices-and-linear-maps","primes-coprimality-and-gcd","array-order"])

recur = show("S2.2.6",
 "If the normalized cost $F_k$ of interchanging two chunks of $e=m^k$ digits satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\\tau$, then $F_k=O(e^\\tau)$, a strict power saving.",
 "Count recursive calls (exactly $s$, each on volume $V/W$), divide by the volume to get a recurrence with ratio $s/W$, and sum the resulting geometric series using $s/W<m^\\tau$.",
 mot("The rank deficit $s<Wm$ says the branching ratio $s/W$ is slightly below the factor $m$ by which the chunk width grows per level, so the solution grows like $e^\\tau$ with $\\tau<1$ instead of like $e$.","recoverable"),
 [
  infer("S2.2.6.1","The exact bound $\\eta_{\\rm b}$ and $\\eta_{\\rm c}$ on the relative rank deficits exceed $20\\cdot 2^{-50}$.",
        "Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.", deferred=True),
  infer("S2.2.6.2","Since $m<2^{20}$ and $\\log m<20$, $m^{1-2^{-50}}=m\\exp(-2^{-50}\\log m)>m(1-20\\cdot2^{-50})>m(1-\\eta)$, which gives $s_{\\rm b}/W_{\\rm b}<m^\\tau$ with $\\tau=1-2^{-50}$ (and likewise $s_{\\rm c}/W_{\\rm c}<m^\\sigma$).",
        ">m(1-20\\cdot2^{-50})>m(1-\\eta)", deferred=True),
  infer("S2.2.6.3","The number of recursive calls is the sum of the edge ranks, exactly $s$.",
        "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  infer("S2.2.6.4","Each recursive call acts on one role stream of volume $V/W$, retaining all other fields as spectators, while splitting, merging, gates and triangular operations cost $O(V)$ at the node.",
        "Each acts on one role stream of volume $V/W$, retaining all other"),
  infer("S2.2.6.5","Hence the uniform bound on time divided by volume satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
        "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."),
  infer("S2.2.6.6","For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^ka^j$ is $O(m^{k\\tau})$: if $a\\le1$ it is at most $k+1=O(m^{k\\tau})$, and if $a>1$ it is $O(a^k)$.",
        "For $a=s/W<m^\\tau$ the geometric sum"),
  infer("S2.2.6.7","Hence $F_k=O(e^\\tau)$.",
        "Hence $F_k=O(e^\\tau)$."),
  infer("S2.2.6.8","Scheduling the recursive calls on a fixed number of tapes by a depth-first schedule with a parking stack for the inactive role streams adds only $O(V)$ at each node, so the recurrence holds with fixed tapes.",
        "\\paragraph{A fixed-tape depth-first schedule.}"),
 ], page="power-saving-recurrence",
 frm=["rank-saving","proof-by-induction-and-recursion","logarithms-and-exponentials","asymptotic-notation-beyond-big-o"],
 adds=[B("F_k","normalized cost","the time of an interchange of width $m^k$ divided by the logical volume","direct"),
       B("e","chunk width","the number $m^k$ of digits in each of the two chunks being interchanged","count")],
 salient="The saving is a genuine power $e^\\tau$ with $\\tau<1$ although $s/W$ falls below $m$ by a tiny relative margin: the series is dominated by its largest term, growing by $s/W<m^\\tau$ per level while the width grows by $m$.")

pint = show("S2.2",
 "Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\\tau)$ time when a row field preceding both chunks has length divisible by $W^k$, for any rational $\\tau\\in(0,1)$ with $s/W<m^\\tau$.",
 "Split the rows among the $W$ roles of the bit network, apply the shear $H\\leftarrow H+D$ on each edge by a matrix shear (recursive smaller interchanges), run the gates pointwise, merge, and compose three shears into a swap.",
 mot("The network performs the shear on every role with the endpoint frames, so each edge only needs a cheaper shear of a smaller width, which is the same operation recursively.","recoverable"),
 [
  infer("S2.2.1","Split whole rows cyclically into $W$ role streams within each prefix; each stream has the same remaining shape, volume $V/W$ and row count divisible by $W^{k-1}$.",
        "Split whole rows cyclically into $W$ role streams within each prefix"),
  infer("S2.2.2","On every circuit edge apply the address permutation $\\Phi_{A_e}$ to that role stream, implemented by the matrix shear lemma through recursive interchanges of the pivot pairs of $b=e/m$-digit fields, and execute each gate pointwise at matching addresses.",
        "On every circuit edge apply"),
  infer("S2.2.3","A common address permutation commutes with every pointwise bit gate, so by the frame identity the output is $f'_{\\rho(w)}=\\Phi_{M_{\\mathrm{out}(\\rho(w))}}\\Phi_{-M_{\\mathrm{in}(w)}}f_w=\\Phi_{I_m}f_w$.",
        "because a common address permutation commutes with every pointwise"),
  infer("S2.2.4","Merging row $g$ of output role $\\rho(w)$ back to original row $Wg+(w-1)$ undoes $\\rho$, leaving $H\\leftarrow H+D$ on every original row, including rows assigned to scratch roles with arbitrary initial values.",
        "Merge by returning row $g$ of"),
  infer("S2.2.5","Performing $D\\leftarrow D-H$, then $H\\leftarrow H+D$ through the circuit, then $D\\leftarrow H-D$ sends $(H,D)$ to $(D,H)$; only the middle shear uses the circuit and the other two are linear-cost updates of the later group.",
        "To interchange the two full chunks, perform"),
  recur,
 ], page="power-interchange",
 frm=["bit-network","frames","stream-ops","array-order","controlled-shifts"],
 salient="Although every intermediate step forms XOR combinations of the data on the role streams, the final effect is an exact interchange of the two chunks, correct for arbitrary initial scratch contents.")

widthrem = show("S2.3",
 "Arbitrary equal widths $u$, arbitrary prefix, gap and suffix, and arbitrary row counts are handled with only $O(Vu^\\tau)$ cost, by supplying rows from a few high digits, padding, and splitting the remaining width in base $m$.",
 "Exchange a few top digits one pair at a time to create a row field, pad it to a multiple of $W^k$, write the remaining width in base $m$ and apply the power-width interchange to each corresponding piece, then undo the preparation and pad binary widths to powers of $q$.",
 mot("The power-width interchange needs a width $m^k$ and enough rows; both restrictions can be removed at a cost smaller than the final bound.","explicit",
     "Rows for a general array can be supplied by a few of its own high digits."),
 [
  infer("S2.3.1","Write each chunk as its top $\\rho$ digits and its remaining digits, interchange the high digits one pair at a time and join them, which costs $O(V\\rho)$ and yields a row field of range $R=q^{2\\rho}\\ge W^k$ before both remaining chunks.",
        "Write each chunk as its top $\\rho$ digits followed by its remaining"),
  infer("S2.3.2","Append zero rows within each prefix so the row count is $R'=W^k\\lceil R/W^k\\rceil<2R$, at most doubling the volume.",
        "Append zero rows, separately within"),
  infer("S2.3.3","Write the remaining width as $e-\\rho=\\sum_{j=0}^k a_jm^j$ with $0\\le a_j<m$ and partition each chunk into $a_j$ pieces of width $m^j$.",
        "Write the remaining width in base $m$:"),
  infer("S2.3.4","Applying the power-width interchange to each pair of pieces costs $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^\\tau)$, a geometric sum since $a_j<m$ and $m^k<me$.",
        "O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)."),
  infer("S2.3.5","For binary chunks, pad the two ranges from $[2^u]$ to $[q^e]$ with a fixed volume factor below $q^2$, interchange, and scan away the padded entries, so the bound is $O(Vu^\\tau)$ since $e=O(u)$.",
        "Finally, for binary chunks let $e$ be the least integer with"),
  infer("S2.3.6","For chunks whose widths differ by one bit, move the extra leading bit and interchange the equal-width parts, which adds one single-bit move costing $O(V)$.",
        "For widths differing by one bit, choose the leading bit of the longer"),
 ])

S2 = show("S2",
 "Two disjoint address chunks of $u$ bits, with any prefix, gap and suffix, can be interchanged in an array of volume $V$ in $O(Vu^\\tau)$ tape steps for a fixed $\\tau<1$ ($\\tau=1-2^{-50}$).",
 "Use the bit network recursively: an edge matrix of rank $a$ costs $a$ smaller interchanges, so the interchange of width $e$ reduces to $s$ interchanges of width $e/m$ on streams of volume $V/W$; then remove the width and row restrictions.",
 mot("Because the sum of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.","explicit",
     "Because the sum of these ranks is less than the number of wires times"),
 [mshear, pint, widthrem],
 page="chunk-interchange",
 frm=["fixed-tape-model","array-order","stream-ops","functions-bijections-and-permutations","bit-network","rank-saving"],
 adds=[B("u","chunk width","the number of bits in each of the two address chunks being interchanged","count"),
       B("\\tau","interchange exponent","the fixed rational exponent below one in the interchange cost bound, $\\tau=1-2^{-50}$","direct")],
 salient="Although the final effect is an exact permutation, the intermediate steps form pointwise XOR combinations of data, and the permutation is exact for arbitrary initial auxiliary values.")

# ---------------- S3: simultaneous butterfly layer ----------------
packed = show("S3.2",
 "For $f$ chunks at once, $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ at the selected bits $j_i=\\rho+iK$ is performed with eight cyclic shifts of whole chunk ranges that restore a third scratch chunk $z$, followed by a deterministic correction of the small explicit set $\\mathcal B$ of addresses whose guard values fail.",
 "Run eight packed additions that flip the parity of $u$ when the control is one and restore $w$, check that they agree with the ideal XORs outside the bad set, bound the bad set by a union bound over the guards, and repair it by sorting the extracted records.",
 mot("Instead of $f$ separate chunk operations, one packed rotation handles all selected positions together, and the only failures are carries between neighbouring segments, which depend on addresses alone and can be corrected deterministically.","explicit",
     "address chunks. A third chunk supplies temporary address bits; its arbitrary"),
 [
  infer("S3.2.1","With control $c=1$, the first four operations induce the cycle $(00\\ 01\\ 10)$ on parities of $(u,w)$ in every square and the last four induce $(01\\ 10\\ 11)$; with $c=0$ nothing changes.",
        "If $c=0$, these operations do nothing. If $c=1$, the first four operations"),
  infer("S3.2.2","The composition of the eight operations gives $(u',w')=(u+c(1-2(u\\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, and the auxiliary integer $w$ is restored.",
        "Consequently the complete output is"),
  infer("S3.2.3","A line updating $y$ by sign $\\varepsilon$ and testing parity $b$ of $z$ is the single cyclic shift $y\\leftarrow y+\\varepsilon\\sum_i2^{j_i}[x_{j_i}=1][z_{j_i}=b]\\pmod{2^L}$ of the whole chunk range, a bijection since the offset never depends on the target.",
        "Physically, a line updating $y$ by sign $\\varepsilon$"),
  infer("S3.2.4","Outside the bad set $\\mathcal B$ of addresses where some used guard value fails $10\\le g\\le2^{K-1}-11$, no segment carries into or borrows from its neighbour, so the packed map agrees with the ideal XOR map.",
        "Let $\\mathcal B$ consist of the addresses for which"),
  infer("S3.2.5","Each guard excludes exactly twenty of $2^{K-1}$ values, so the union bound over $2(f-1)$ guards gives $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$, independent of record values.",
        "the union bound over the $2(f-1)$ guards gives"),
  infer("S3.2.6","To repair $\\mathcal B$, scan the stream with a record-rank counter, extract exactly the records of $\\mathcal B$, attach each destination rank computed by reversing the eight shifts and applying the XORs, sort them stably by radix sort, and reinsert them.",
        "To implement the correction, scan the stream with a record-rank counter."),
  infer("S3.2.7","The omitted most significant selected position is handled by a single two-bit XOR costing $O(V)$; when $f=1$ the shifts and $\\mathcal B$ are trivial and this step is the whole algorithm.",
        "Finally apply the two-bit XOR to $x_{j_{f-1}},y_{j_{f-1}}$ by"),
  infer("S3.2.8","The movement costs $O(V(L^\\tau+1))$ and the repair adds $O(MA_{\\rm rect}^3+\\delta_{\\rm bad}MA_{\\rm rect}(R+A_{\\rm rect}))$, which is $O(V(L^\\tau+1))$ when $K/\\log p\\to\\infty$ and the record length exceeds every fixed polynomial in $p$.",
        "The movement costs $O(V(L^\\tau+1))$."),
 ], page="packed-bit-addition",
 frm=["chunk-interchange","controlled-shifts","stream-ops","binary-field-f2-and-xor","modular-arithmetic"])

batching = show("S3.4",
 "Calling the complex network on $e=mf$ selected axes needs $s$ child calls on $f$ axes of volume $V/W$ each, with node overhead $O(V((eK)^\\tau+1))$, so the normalized cost satisfies $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ and totals $O(Vd^{\\lambda'})$.",
 "Obtain rows from the first few chunks, split rows among the $W$ roles to give each child exactly $1/W$ of the volume, write the recurrence, and sum it as for the interchange, stopping the recursion at small widths and splitting $D$ in base $m$.",
 mot("Splitting complete rows among the network's wire roles reduces the volume of each recursive call, exactly as in the interchange, so the same rank saving $s/W<m^\\sigma$ yields a power saving in the number of axes.","explicit",
     "the network's wire roles then reduces the volume of each recursive"),
 [
  infer("S3.4.1","At an internal node with $e=m^k$ active chunks, the binary changes of basis, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\\tau+1))$, using the packed row addition on slots of $(e/m)K$ address bits.",
        "First consider an internal node containing \\(e=m^k\\) consecutive"),
  infer("S3.4.2","A row index $u=Wg+w$ is sent entirely to physical wire role $w$, so every role stream has the same remaining address shape and the scratch roles are supplied from existing rows.",
        "and send that entire row to physical wire role \\(w\\), indexed there"),
  infer("S3.4.3","Each recursive edge call acts on one role stream with volume exactly $1/W$ of its parent's logical volume.",
        "one role stream with volume exactly \\(1/W\\) of its parent's logical"),
  infer("S3.4.4","Writing $F(e)$ for time divided by the current volume, $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ with $F(e)=O(e)$ for $e<d^\\beta$.",
        "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
  infer("S3.4.5","Since $a=s/W\\le m^\\sigma<m^\\lambda$, the internal costs sum to $O(e^\\lambda)$ and the leaves contribute at most $O(e^\\sigma d^{\\beta(1-\\sigma)})$.",
        "Since \\(a\\le m^\\sigma<m^\\lambda\\), the internal"),
  infer("S3.4.6","Writing $D-q_0=\\sum_ja_jm^j$ in base $m$ and adding the piece costs and the row preprocessing gives the total $O(\\log(2d)[d^\\lambda+d^{\\sigma+\\beta(1-\\sigma)}+1])=O(d^{\\lambda'})$ per unit volume.",
        "Write \\(D-q_0=\\sum_j a_jm^j\\) in base \\(m\\), with \\(0\\le a_j<m\\)."),
  infer("S3.4.7","Hence the simultaneous layer on $D\\le d$ axes costs $O(Vd^{\\lambda'})$ for any fixed $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$.",
        "=O(d^{\\lambda'})"),
 ])

S3 = show("S3",
 "The two-point butterfly $H_0$ can be applied simultaneously at the same bit offset in $D\\le d$ address chunks, on records of $r$ complex fixed-point coefficients, in $O(Vd^{\\lambda'})$ time for a fixed $\\lambda'<1$, with one final truncation of error below $\\sqrt2\\,2^{-p}$.",
 "Recurse on the complex phase network: conjugate each edge's kernels to slot coordinates by binary changes of basis (packed selected-bit additions), call the smaller layer on each slot with rows split among the wire roles, bound the recurrence and guard widths, and convert $C^{\\otimes D}$ to $H_0^{\\otimes D}$.",
 mot("Applying $H_0$ on each of $D$ axes separately would need $D$ whole-array passes, so one reuses the rank-saving network, whose phase frames express a $C$ tensor product through smaller groups of selected bits separated by binary changes of basis.","explicit",
     "selected bits, separated by binary changes of basis. We implement those"),
 [
  infer("S3.1","An edge from label $U_-$ to $U_+$ has frame change $\\prod_{j=1}^{\\rho_{\\rm edge}}(aI+bX_{v_j})^{\\epsilon_j}$ over an orthonormal basis $v_1,\\ldots,v_{\\rho_{\\rm edge}}$ of its residual, with $\\epsilon_j=\\pm1$ and $\\rho_{\\rm edge}$ kernels also on decreasing edges.",
        "Proposition~\\ref{prop:complex-motif-interface} gives the frame change"),
  infer("S3.1b","Conjugating by the address permutation $\\mathcal P_M$, with the residual basis as the first columns of $M\\in\\mathrm{GL}(m,\\mathbb F_2)$, turns each kernel into a child operation $(C^{\\epsilon_h})^{\\otimes f}$ on the $f$ bits of one slot; inverse children need no new call since $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$.",
        "To implement \\eqref{eq:phase-edge-coordinate} on the group, first apply"),
  infer("S3.1c","Applying the finite network with these column frames to $e=mf$ selected axes needs exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and yields $C^{\\otimes e}$ on every role.",
        "Apply the finite network with these column frames to a group of"),
  infer("S3.1d","The normalized layer is $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, with diagonal Gaussian-dyadic phases $\\mathcal S_D$ and an exact scalar $b^D$.",
        "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."),
  packed,
  infer("S3.3","A fixed binary change of basis in $\\mathrm{GL}(m,\\mathbb F_2)$ is a product of a fixed number of elementary row additions (a row exchange is three), each a packed selected-bit addition on whole slots, so the change of basis and its inverse cost $O(V((eK)^\\tau+1))$.",
        "An invertible matrix over $\\mathbb F_2$ of fixed order $m\\ge3$ is a"),
  batching,
  infer("S3.5","The accelerated network is evaluated exactly: with $E=64(W+m+1)^3$, $B=s+E$ and $C_1=20$, denominator and magnitude growth in one layer are bounded by $\\lceil C_0d^{C_1}\\rceil$ bits, which is $o(p)$ because $\\epsilon C_1<1$, so all intermediate coefficients have $O(p)$ bits.",
        "For the complex network, let"),
  infer("S3.6","Equation $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ converts the exact $C$-layer to $\\mathcal H$, and the single final truncation toward zero keeps coefficients in the unit disk with error below $\\sqrt2\\,2^{-p}$, since every row of $\\mathcal H$ has absolute row sum one.",
        "Finally, every row of $\\mathcal H$ has"),
 ], page="simultaneous-layer",
 frm=["phase-network","power-saving-recurrence","chunk-interchange","fixed-point-disk-grid","polynomials","butterfly-fft","controlled-shifts","stream-ops"],
 adds=[B("K","chunk size","the number of address bits in each address chunk, $K=\\lfloor d^c\\rfloor$","count"),
       B("\\lambda'","layer exponent","the fixed rational exponent below one in the simultaneous layer cost bound","direct")],
 salient="Applying $H_0$ on up to $d$ axes at once costs only $O(Vd^{\\lambda'})$ with $\\lambda'<1$, much less than the $d$ whole-array passes of separate butterflies, for the same reason as the interchange: $s/W<m^\\sigma$.")

# ---------------- S4: ring convolution ----------------
synth = show("S4.1.1",
 "Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$, with roots of unity $\\omega_t=y^{2r/t}$, the radix-two decimation-in-frequency recursion computes the normalized transform $F_t^-$ with outputs in bit-reversed slot order, and a reverse procedure computes $F_t^+B_t^{-1}$ from that stored order; twiddles are exact signed shifts of coefficient lists.",
 "Verify character cancellation directly in the ring (which has zero divisors), then run the two-point butterfly recursion with twiddle multiplications by powers of $y$, track which slots hold frequency bits, and group the rounds of several axes.",
 mot("Every root of unity is a power of $y$, so multiplication by it permutes coefficients and changes signs; only the butterflies cost arithmetic.","explicit",
     "where the required roots of unity act by exact signed permutations"),
 [
  infer("S4.1.1.1","Since $\\sum_{k=0}^{t-1}\\omega_t^{jk}=t$ if $t\\mid j$ and $0$ otherwise, $F_t^+F_t^-=t^{-1}I$.",
        "F_t^+F_t^-=t^{-1}I."),
  infer("S4.1.1.2","When $t\\nmid j$, shifting $k$ by $t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$, so the sum is zero since the additive group of $\\mathcal R_r$ has no two-torsion.",
        "Hence the sum is zero, since the additive group of"),
  infer("S4.1.1.3","The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the $b=1$ output by $\\omega_t^{-k}$ and recurses on the two branches, computing $F_t^-$.",
        "the $b=1$ output by $\\omega_t^{-k}$"),
  infer("S4.1.1.4","After all $a=\\log_2t$ rounds the entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$, so the stored order is the bit reversal $B_t$.",
        "$\\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the"),
  infer("S4.1.1.5","The procedure consuming this stored order traverses the recursion in reverse, so the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
        "The procedure consuming this stored order traverses the recursion in"),
  infer("S4.1.1.6","The twiddle of one axis depends only on that axis's address bits, so the steps of $D$ axes group into one parallel butterfly $\\mathcal H$ followed by one recordwise monomial $J_E$.",
        "Consequently the individual axis steps may be grouped as a parallel"),
 ], page="synthetic-transform",
 frm=["polynomial-ring-mod","butterfly-fft","dft","multidim-transform","convolution-theorem"],
 salient="Twiddle multiplications cost no arithmetic: roots of unity are powers of $y$, so only the two-point butterflies do arithmetic.")

layout = show("S4.1",
 "A layout permutation $L$ that puts the selected bits of all participating axes at a common offset in consecutive $K$-bit chunks lets every radix-two round be one simultaneous layer; the forward transform $LBF_{\\boldsymbol t}^-$ and its opposite $F_{\\boldsymbol t}^+B^{-1}L^{-1}$ cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
 "Move a few slots to a prefix, exchange chunks into the required order, apply one simultaneous layer per round on the remaining chunks and individual butterflies on the prefix slots, implement twiddles as signed shifts, and track the exact operator order.",
 mot("To apply the simultaneous layer in a transform round, the selected bits of the participating axes must sit at a common offset in consecutive chunks.","explicit",
     "we must place the selected bits of the participating axes at a common"),
 [
  synth,
  infer("S4.1.2","Listing the slots to move to a prefix (the top slot of each long axis, then the $b$ lowest slots of each axis) and moving them costs $O(TpdK)$, leaving $q$ consecutive $K$-bit chunks on each axis.",
        "Form a list of the slots to move to a prefix."),
  infer("S4.1.3","Scanning target positions and exchanging chunks that differ uses at most $Dq-1$ exchanges of width-$K$ chunks, costing $O(Tp\\,pK^{\\tau-1})$ since $d\\ell=O(p)$.",
        "To obtain this order, scan its target positions from left to right."),
  infer("S4.1.4","Each round on the remaining chunks selects the same bit offset in $D$ consecutive chunks, so the simultaneous layer applies at cost $O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total.",
        "The simultaneous-layer procedure therefore applies at cost"),
  infer("S4.1.5","Rounds on prefix slots process the participating bits individually at width $p+D+O(1)=O(p)$, with at most $b+1\\le K$ rounds, costing $O(TpdK)$.",
        "In a round on prefix slots, process the participating bits individually."),
  infer("S4.1.6","Multiplying by the monomial $y^E$ modulo $y^r+1$ is a split of the coefficient list before position $r-s$, a swap of the two pieces, a negation of the moved tail and a common sign $(-1)^e$, with no coefficient sort.",
        "To implement the monomial, write $E=er+s$ with $0\\leq s<r$."),
  infer("S4.1.7","A contraction does not increase the error and one truncation adds less than $\\sqrt2\\,2^{-p}$ per round, so at most $\\ell$ rounds give error below $\\sqrt2\\,\\ell\\,2^{-p}$ and keep the disk.",
        "Both the contraction and truncation preserve the disk."),
  infer("S4.1.8","The exact operators are $(L\\mathcal D_-L^{-1})L=LBF_{\\boldsymbol t}^-$ forward and $L^{-1}(L\\mathcal D_+L^{-1})=F_{\\boldsymbol t}^+B^{-1}L^{-1}$ opposite, so the forward output may be kept in layout $LB$ for the pointwise product.",
        "It remains to identify the order of the full procedures."),
 ], page="transform-layout",
 frm=["simultaneous-layer","chunk-interchange","butterfly-fft","stream-ops","multidim-transform"],
)

kron = show("S4.2",
 "Two disk-grid polynomials $f,g\\in\\mathcal R_r$ can be multiplied exactly, and $Q_p(fg/r)$ returned, in $O(rp\\log(rp))$ time using the established $O(N\\log N)$ integer multiplier on four signed evaluation products.",
 "Evaluate the integer coefficient polynomials at $B_0=2^{4p}$ as signed integers, multiply with the established integer multiplier, extract the centered coefficients, and wrap negacyclically.",
 mot("Signed packing is a form of Kronecker substitution: a polynomial product becomes an integer product if the base exceeds twice the largest product coefficient.","explicit",
     "reduction is a signed form of Kronecker substitution; compare"),
 [
  infer("S4.2.1","With $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ and $B_0=2^{4p}$, evaluate $A_u=u(B_0)$ for $u\\in\\{a,b,c,e\\}$; each magnitude fits in $4pr$ bits.",
        "Set $B_0=2^{4p}$"),
  infer("S4.2.2","The four evaluation products $A_aA_c,A_bA_e,A_aA_e,A_bA_c$ are computed by the established multiplier on absolute values with signs restored.",
        "Multiply the four"),
  infer("S4.2.3","Every coefficient of any ordinary product satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so the next coefficient is identified by its centered residue modulo $B_0$ after lower coefficients are removed.",
        "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2."),
  infer("S4.2.4","Extraction proceeds block by block with a carry in $\\{0,1\\}$, taking at each step the unique representative of $q_j+\\rho_j$ in $[-B_0/2,B_0/2)$, which equals $h_j$ by the separation bound.",
        "Put $\\rho_0=0$.  At block $j$, let $\\widehat h_j$ be the unique"),
  infer("S4.2.5","The real and imaginary numerator streams $ac-be$ and $ae+bc$ are reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$, and each result has $|H_j|\\le r2^{2p}$.",
        "The real and imaginary numerator streams are respectively"),
  infer("S4.2.6","Four exact integer products on $O(rp)$-bit inputs dominate the linear packing, extraction, wrapping and truncation costs, giving $O(rp\\log(rp))$.",
        "Four exact integer products dominate the linear"),
 ], page="kronecker-packing",
 frm=["nlogn-multiplier","polynomial-ring-mod","positional-number-representation-and-carries","polynomials"])

ringconv = show("S4",
 "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\\mathcal R_r$ is computed by two forward synthetic transforms in the retained layout, pointwise ring products by signed packing, and the opposite transform consuming the same stored order, with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
 "Build the synthetic transforms on the layout, multiply pointwise in the retained order using signed packing, apply the opposite transform, and verify the normalization with the convolution theorem and the error by bilinear contraction bounds.",
 mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so no sorting back to natural order is needed between the forward and opposite transforms.","explicit",
     "forward outputs in their retained order and pass that order directly"),
 [
  layout, kron,
  infer("S4.3","Perform both forward transforms and retain their common $LB$ order, multiply the corresponding polynomial records by the signed packing lemma, apply the opposite procedure to that order, and multiply exactly by $M=T/r$.",
        "Perform both forward transforms and retain their common $LB$ order."),
  infer("S4.4","By the convolution theorem $F_{\\boldsymbol t}^-(f*g)=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)$ and $F_{\\boldsymbol t}^+F_{\\boldsymbol t}^-=I/M$, so $MF_{\\boldsymbol t}^+\\bigl(F_{\\boldsymbol t}^-f\\cdot F_{\\boldsymbol t}^-g/r\\bigr)=(f*g)/(rM)$.",
        "To check normalization, expansion of the finite sums gives"),
  infer("S4.5","With forward errors below $\\delta=\\sqrt2\\ell 2^{-p}$, the pointwise-product map $P$ is a bilinear contraction, so the product error is below $2\\delta+\\eta$, the opposite transform adds below $\\delta$, and scaling by $M$ gives error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
        "For the error estimate, put"),
  infer("S4.6","There are $M=T/r$ pointwise polynomial products costing $O(Tp\\log(rp))$ in total, in addition to the three transform costs and a linear exact scaling.",
        "There are $M=T/r$ pointwise polynomial products."),
 ], page="ring-convolution",
 frm=["convolution-theorem","multidim-transform","cyclic-convolution","polynomial-ring-mod","fixed-point-disk-grid"],
 salient="The bit-reversed frequency order produced by the forward transforms is never undone: it is carried through the pointwise product straight into the opposite transform.")

# ---------------- S5: resampling ----------------
gauss = show("S5.1",
 "For coprime lengths $s<t$ with $t/s-1>p/\\alpha^4$ there are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable in $O(tp^{3/2+\\delta}\\alpha)$ time, and the identity tensors to $d$ axes at the cost of padding and moving axes.",
 "Use Harvey and van der Hoeven's Gaussian resampling identity and Neumann inverse, keep the coordinate permutations $P_s,P_t$ inside the identity instead of sorting, cite the ordered numerical maps for the cost, and tensor line by line.",
 mot("The transform lengths needed for the integer product are pairwise coprime whereas the synthetic transforms use powers of two, and Gaussian resampling connects these two shapes.","explicit",
     "whereas the synthetic transforms use powers of two. Gaussian resampling"),
 [
  infer("S5.1.1","There are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ for $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$.",
        "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and"),
  infer("S5.1.2","The exact Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the estimate $\\|N-I\\|<2^{-\\alpha^2\\theta}<1/2$ hold, so $N=C\\mathsf T\\mathsf D$ is invertible by a Neumann series.",
        "The exact Gaussian identity and inverse estimate proved in"),
  infer("S5.1.3","Setting $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$ with the normalizations $\\mathsf S'=\\mathsf S/2$, $\\mathsf J'=N^{-1}/2$, $\\mathsf D'=2^{-(2\\alpha^2-2)}\\mathsf D$ gives contractions whose product of scales is $2^{-2\\alpha^2}$.",
        "Now set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$."),
  infer("S5.1.4","The ordered numerical maps $\\widetilde{\\mathsf S}'$, $\\widetilde{\\mathsf J}'$, $\\widetilde{\\mathsf D}'$ and the selection $C$ give approximations $\\widetilde A,\\widetilde B_0$ with error below $p^2$ and time $O(tp^{3/2+\\delta}\\alpha)$.",
        "\\paragraph{Ordered numerical maps.}"),
  infer("S5.1.5","The permutations $P_s,P_t$ remain in the transform identity, whereas the original proof implemented them by two label-and-sort operations costing $O(tp\\log t)$ each.",
        "In \\eqref{eq:no-sort-one-dimensional} these permutations remain in the"),
  infer("S5.1.6","Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, and the linewise implementations have error below $dp^2$.",
        "Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
  infer("S5.1.7","At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$, so the total time is $O(dTp^{3/2+\\delta}\\alpha)$.",
        "At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
  infer("S5.1.8","Exposing and restoring one axis needs $O(d)$ adjacent interchanges of $\\ell$-bit or $(\\ell-1)$-bit address fields, each costing $O(Tp(1+\\ell^\\tau))$, hence $O(Tp\\,d^2(1+\\ell^\\tau))$ for all axes.",
        "To move an axis past its neighbor, interchange their"),
 ], page="gaussian-resampling",
 frm=["dft","multidim-transform","fixed-point-disk-grid","exponential-function-and-gaussian-function","vector-norms-and-error-bounds","chunk-interchange"])

chirp = show("S5.2",
 "For even $t_i$, the permuted transform factors as $QF_{\\boldsymbol t}u=\\overline a\\cdot\\bigl(a*(\\overline a\\cdot u)\\bigr)/T$ with the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_is_ij_i^2/t_i)$, a pointwise phase, a cyclic convolution and another pointwise phase.",
 "Compute the coefficient of $u_{\\boldsymbol k}$ on the right side with the chirp's periodicity and compare it with the coefficient of $QF_{\\boldsymbol t}$.",
 mot("The factor $QF_{\\boldsymbol t}$ can be computed from a cyclic convolution and two pointwise phase multiplications, which avoids applying $Q$ as a separate permutation of the array.","explicit",
     "computed from a cyclic convolution and two pointwise phase"),
 [
  infer("S5.2.1","Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\\pi is_i(2j_i+t_i)$, an integral multiple of $2\\pi i$ (as $t_i$ is even), so $a$ has period $t_i$ in coordinate $i$.",
        "Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
  infer("S5.2.2","The coefficient of $u_{\\boldsymbol k}$ on the right side is $\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$, precisely the coefficient in $QF_{\\boldsymbol t}$ since $Q$ reads frequency $-s_ij_i$ from the negative-sign transform.",
        "The coefficient of $u_{\\boldsymbol k}$ in the right side of"),
 ], page="chirp-identity",
 frm=["dft","cyclic-convolution","multidim-transform","complex-numbers","gaussian-resampling"])

permc = show("S5.3",
 "The source permutation $R$ retained by resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform: $(RF_{\\boldsymbol s}^+)\\bigl[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)\\bigr]=(u*v)/S^2$ with $S=\\prod_is_i$.",
 "Show $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$ by a change of summation variable, push the permutation through the pointwise product, and use the normalized convolution rule.",
 mot("The retained source permutation $R$ cancels when computing a convolution, so no sort is executed.","explicit",
     "retained source permutation $R$ cancels when computing a convolution."),
 [
  infer("S5.3.1","For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$.",
        "For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$."),
  infer("S5.3.2","Each $t_i$ is a unit modulo $s_i$, so tensoring gives $F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$; a coordinate permutation also commutes with pointwise products.",
        "$F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence"),
  infer("S5.3.3","The normalized convolution rule is $F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)\\cdot(F_{\\boldsymbol s}v)$.",
        "The normalized convolution rule is"),
  infer("S5.3.4","With $F_{\\boldsymbol s}^+F_{\\boldsymbol s}=I/S$ the two normalizations give $F_{\\boldsymbol s}^+(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)=(u*v)/S^2$.",
        "The two normalizations give"),
 ], page="permutation-cancellation",
 frm=["gaussian-resampling","dft","convolution-theorem","modular-arithmetic","functions-bijections-and-permutations","primes-coprimality-and-gcd"],
 salient="The permutation $R$ is applied by each forward transform, yet it does not appear in the final convolution $(u*v)/S^2$: it cancels, so the two sorts of the original resampling are never executed.")

S5 = show("S5",
 "Fourier transforms of pairwise coprime lengths needed for the digit convolution reduce to power-of-two tensor transforms plus a chirp convolution, with the source and target coordinate permutations retained in the formulas and cancelled across the convolution so that no full sort is executed.",
 "Gaussian resampling to power-of-two lengths with the permutations retained, Bluestein's chirp identity for the middle transform, and cancellation of the source permutation.",
 mot("Its usual implementation sorts twice on each coordinate; retaining both permutations in the transform formula and computing it directly avoids those sorts.","explicit",
     "coordinate. We retain both permutations in the transform formula and"),
 [gauss, chirp, permc])

# ---------------- S6: multiplication algorithm ----------------
primes = show("S6.1",
 "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$, $\\eta=1/(4d)$, can be found deterministically, with $T/2<S<T$ for $S=\\prod_is_i$ and the separation $\\alpha^4\\theta_i>p$ required by resampling, in $n^{o(1)}$ time.",
 "Use the explicit prime-interval bound to show each interval contains more than $d$ primes, choose distinct primes, bound $S/T$ by Bernoulli's inequality, check the resampling hypotheses, and bound the deterministic search.",
 mot("The product of the prime lengths must occupy a fixed fraction of the padded box while each ratio $t_i/s_i$ must leave enough separation for resampling.","explicit",
     "The distinct prime lengths $s_i$ must be close to the powers of two"),
 [
  infer("S6.1.1","For $0<\\eta<1/4$ and $x>e^{2/\\eta}$, the interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains at least $\\eta x/(2\\log x)$ primes (Harvey and van der Hoeven, from Rosser and Schoenfeld).",
        "(1-2\\eta)x<q\\leq(1-\\eta)x"),
  infer("S6.1.2","For both $x=r/2$ and $x=r$ this count exceeds $d$ and the two intervals are disjoint, so distinct odd primes can be chosen with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$.",
        "(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i."),
  infer("S6.1.3","Multiplying the lower bounds and applying strict Bernoulli inequality gives $S/T>(1-1/(2d))^d>1/2$, and with $s_i<t_i$ this gives $T/2<S<T$.",
        "applying strict Bernoulli inequality gives"),
  infer("S6.1.4","With $\\theta_i=t_i/s_i-1>\\eta$, $\\alpha^4\\theta_i>12d^2b/(4d)=3db\\ge6b=p$, so every hypothesis of the one-dimensional resampling lemma holds.",
        "\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\geq6b=p."),
  infer("S6.1.5","The machine finds the primes by scanning the two intervals and trial division, in $O(dr^{3/2}\\operatorname{poly}(p))=n^{o(1)}=o(n)$ time.",
        "The machine finds these primes by scanning the two intervals"),
 ], page="prime-lengths",
 frm=["primes-coprimality-and-gcd","logarithms-and-exponentials","gaussian-resampling"],
 adds=[B("s_i","prime source length","the prime length of the $i$th source axis","direct"),
       B("t_i","power-of-two axis length","the length of the $i$th padded axis, equal to $r/2$ or $r$","direct"),
       B("S","source size","the product of the prime source lengths $s_i$","count"),
       B("\\eta","relative gap","the relative distance $1/(4d)$ separating each prime length from its power of two","direct")])

intconv = show("S6.2",
 "Writing both $n$-bit inputs in radix $2^b$ with $q=\\lceil n/b\\rceil$ digits, the product's digit coefficients are the convolution of the digit lists, equal to cyclic convolution modulo $x^S-1$ because the product degree $2q-2<S$, and each coefficient is below $2^{3b}$.",
 "Treat each input as a polynomial in $2^b$, compare degrees with the cyclic length, and bound the coefficients.",
 mot("A product of polynomials in $2^b$ has digit sequence the convolution of the digit sequences, and zero padding to length $S$ prevents wraparound, so a cyclic convolution of length $S$ suffices.","recoverable"),
 [
  infer("S6.2.1","Write the two inputs as polynomials in $2^b$ with $q=\\lceil n/b\\rceil$ nonnegative digits each; their product has degree at most $2q-2<2n/b\\le T/2<S$.",
        "Write the two inputs as polynomials in $2^b$, each with"),
  infer("S6.2.2","Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
        "Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
  infer("S6.2.3","Every product coefficient satisfies $0\\le c_j\\le q(2^b-1)^2<2^{3b}$ since $q\\le n\\le2^b$.",
        "0\\le c_j\\le q(2^b-1)^2<2^{3b},"),
 ], page="int-as-convolution",
 frm=["cyclic-convolution","positional-number-representation-and-carries","polynomials"],
 adds=[B("b","digit width","the number of bits in each radix digit, $b=\\lceil\\log_2n\\rceil$","count")])

crt = show("S6.3",
 "The map $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\ldots,x_d]/(x_i^{s_i}-1)$, $x\\mapsto\\prod_ix_i^{\\mu_i}$, is a convolution-preserving isomorphism implemented on tape by $d$ triangular prefix-controlled cyclic shifts, and it and its inverse with padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
 "Define the algebra map by the Chinese remainder theorem with unit exponents $\\mu_i=P_i^{-1}\\bmod s_i$, show it is a bijection on basis monomials, write the axis coordinates in triangular form, and perform each as a controlled cyclic shift after reordering axes.",
 mot("The change of ordinary coefficient order into the order of the source tensor is the Chinese remainder split of a cyclic convolution into a multidimensional one, with coordinate powers making the change of order a sequence of controlled cyclic shifts.","explicit",
     "To use the source tensor, we first place the ordinary coefficient stream"),
 [
  infer("S6.3.1","The assignment respects $x^S=1$, so it defines an algebra map.",
        "so it defines an algebra map"),
  infer("S6.3.2","Since each $\\mu_i$ is a unit and the $s_i$ are pairwise coprime, the powers of the image of $x$ run through all $S$ target basis monomials exactly once, so $\\Phi$ is an isomorphism preserving cyclic convolution.",
        "$\\Phi$ is an isomorphism and preserves cyclic convolution."),
  infer("S6.3.3","With $k=\\sum_ja_jP_j$, the coordinate of $\\Phi(x^k)$ in axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, because terms with $j>i$ are divisible by $s_i$ and $\\mu_iP_i=1$.",
        "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}."),
  infer("S6.3.4","After reordering the padded axes to $(a_1,\\ldots,a_d)$, updating targets in the order $i=d,d-1,\\ldots,1$ uses only unchanged lower-index controls; each update rotates the valid interval $[0,s_i)$ and fixes $[s_i,t_i)$, so zero padding stays zero.",
        "Update the targets in the"),
  infer("S6.3.5","Each triangular update is a prefix-controlled cyclic shift: prepare the offset, split the valid target interval into two pieces and merge them in the opposite order.",
        "Each triangular update is a prefix-controlled cyclic shift."),
  infer("S6.3.6","Reversing all axes uses $O(d^2)$ adjacent moves, each an equal-width chunk swap plus a fixed number of linear passes, so $\\Phi$, its inverse and the padding cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
        "uses $O(d^2)$ such moves."),
 ], page="crt-axis-map",
 frm=["controlled-shifts","cyclic-convolution","primes-coprimality-and-gcd","modular-arithmetic","chunk-interchange"])

negtwist = show("S6.4.1",
 "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ is an isomorphism $\\mathbb C[x_d]/(x_d^r-1)\\to\\mathcal R_r$, $x_d\\mapsto\\zeta y$, which turns cyclic convolution on the last axis into convolution modulo $y^r+1$ and preserves the sup norm.",
 "Check the map is well defined and diagonal on coefficients, then check that the negative wrap of the ring exactly cancels the twist.",
 mot("A wrapped product term picks up $\\zeta^r=-1$ from the twist and $-1$ from the negacyclic wrap, so signs cancel and the cyclic coefficient is recovered by untwisting.","recoverable"),
 [
  infer("S6.4.1.1","The map $x_d\\mapsto\\zeta y$ is well defined since $(\\zeta y)^r=(-1)(-1)=1$.",
        "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."),
  infer("S6.4.1.2","On the bases $(x_d^k)$ and $(y^k)$ it multiplies coefficient $k$ by the nonzero number $\\zeta^k$, so it is an isomorphism with inverse multiplying by $\\zeta^{-k}$, and both preserve the sup norm.",
        "multiplying coefficient $k$ by the nonzero number $\\zeta^k$."),
  infer("S6.4.1.3","For $k+l=j+hr$ with $h\\in\\{0,1\\}$, a product term has factor $\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
        "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j."),
 ], page="negacyclic-twist",
 frm=["polynomial-ring-mod","cyclic-convolution","complex-numbers"])

cconv = show("S6.4",
 "Normalized complex cyclic convolution $f*g/T$ on power-of-two axes is computed on grids by twisting the last axis into $\\mathcal R_r$, convolving the first $d-1$ axes over the ring, and untwisting, with each phase product followed by one truncation.",
 "Twist both operands by $\\zeta^k$, call the ring convolution, and untwist by $\\zeta^{-k}$, computing the phases as disk-grid approximations.",
 mot("The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist.","explicit",
     "obtained from the synthetic convolution by a coefficient twist."),
 [
  negtwist,
  infer("S6.4.2","Computed disk-grid phases $\\widetilde\\theta_k^\\pm$ approximating $\\zeta^{\\pm k}$ with error below $2\\cdot2^{-p}$ are obtained at cost $O(p^{1+\\delta})$ each, using the exponential routine.",
        "For $0\\le k<r$, obtain disk-grid approximations"),
  infer("S6.4.3","Each phase product is computed exactly as a dyadic product and then truncated by $Q_p$, giving the sequence $f'=Q_p(\\widetilde\\theta^+f)$, $g'=Q_p(\\widetilde\\theta^+g)$, $h'=\\widetilde{\\mathcal M}_r(\\iota f',\\iota g')$ and output $Q_p(\\widetilde\\theta^-\\iota^{-1}h')$, at twist cost $O(Tp^{1+\\delta})$.",
        "Each phase product is computed exactly as a dyadic product before"),
 ], page="complex-convolution",
 frm=["ring-convolution","polynomial-ring-mod","fixed-point-disk-grid","complex-numbers"])

srct = show("S6.5",
 "The source transform $\\widetilde{\\mathscr F}$ of a disk-grid tensor of norm at most $.5$ applies the Gaussian map $\\mathcal A$ line by line, the chirp transform through complex convolution, the map $\\mathcal B_0$, and the exact scale $2^\\gamma$, approximating $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$; its opposite-sign version is obtained by complex conjugation.",
 "Compose the Gaussian expansion, the chirp-identity evaluation of the middle transform by one complex convolution with two phase multiplications, the compression map and an exact power-of-two shift, and obtain the opposite sign by conjugating input and output.",
 mot("The complex convolution evaluates the middle factor $QF_{\\boldsymbol t}$ in the resampling identity, which together with the Gaussian maps gives the transform of coprime length.","explicit",
     "We next use the complex convolution to evaluate the middle factor"),
 [
  infer("S6.5.1","The chirp numerators $-\\sum_is_ij_i^2(r/t_i)\\bmod 2r$ have $O(p)$ bits with $r/t_i\\in\\{1,2\\}$, and chirp construction costs $O(Tdp^{1+\\delta})$ in total.",
        "All integers have $O(p)$ bits and $r/t_i\\in\\{1,2\\}$."),
  infer("S6.5.2","For a disk-grid target tensor $x$ of norm at most $.6$ the computed chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$ and $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot y_0)$.",
        "norm at most $.6$, the computed chirp transform forms the arrays"),
  infer("S6.5.3","The procedure $\\widetilde{\\mathscr F}$ applies the linewise approximation to $\\mathcal A$, the chirp transform $\\widetilde{\\mathscr C}$, the linewise approximation to $\\mathcal B_0$, and multiplies the grid numerators exactly by $2^\\gamma$.",
        "$\\widetilde{\\mathscr F}$ for the following procedure: apply the linewise"),
  infer("S6.5.4","Its exact counterpart is $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
        "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A"),
  infer("S6.5.5","The opposite-sign procedure is $\\widetilde{\\mathscr F}^{+}(z)=\\overline{\\widetilde{\\mathscr F}(\\overline z)}$, with exact counterpart $RF_{\\boldsymbol s}^{+}$.",
        "=\\overline{\\widetilde{\\mathscr F}(\\overline z)};"),
 ], page="source-transform",
 frm=["gaussian-resampling","chirp-identity","permutation-cancellation","complex-convolution","prime-lengths","fixed-point-disk-grid"])

exact = show("S6.7",
 "The recovered coefficients have absolute error below $448b\\,2^{-3b/4}<1/2$, so rounding gives the integer convolution coefficients exactly, and propagating radix-$2^b$ carries outputs exactly the $2n$ product bits.",
 "Track disk margins and errors through every computed step with bilinear and linear contraction bounds, undo the normalizations by exact scalings, show the final error is below one half, round, and carry.",
 mot("Every step is computed on a grid with errors that add under composition, so one bounds the total error of the recovered coefficient and compares it with one half; the true coefficients are integers.","recoverable"),
 [
  infer("S6.7.1","In the coefficient sup norm with unit $h_p=2^{-p}$, a linear contraction propagates input error without increasing it, a bilinear contraction adds the two operand errors, and a computed phase product has error below $4h_p$ and does not increase the norm.",
        "Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this"),
  infer("S6.7.2","The normalized ring convolution has error below $E_{\\rm ring}=M(3L+2)<5TL$ and its output has norm below $.701$, so it stays in the disk without clipping.",
        "E_{\\rm ring}:=M(3L+2)<5TL."),
  infer("S6.7.3","A computed chirp transform of an input of norm at most $.6$ has output norm below $.701$ and error below $8TLh_p$.",
        "For a disk-grid chirp input $x$ with $\\|x\\|\\le.6$, the previously"),
  infer("S6.7.4","A source transform of an input of norm at most $.5$ has error below $E_sh_p$ with $E_s=9\\,2^\\gamma TL$ and norm below $.501$.",
        "E_s=9\\,2^\\gamma TL,"),
  infer("S6.7.5","With $z=Q_p(\\widetilde U\\cdot\\widetilde V_1)$ of norm below $.5$, $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.",
        "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$."),
  infer("S6.7.6","By cancellation of the permutation $G(U\\cdot V_1)=(u*v)/S^2$, so the opposite transform of $z$ is within $(3E_s+2)h_p$ of it, and after the exact scale by $S$ the array $\\widetilde w$ approximates $w=(u*v)/S$ with error below $E_wh_p$, $E_w=S(3E_s+2)<28\\,2^\\gamma T^2L$.",
        "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L."),
  infer("S6.7.7","The unscaled integer coefficient array is $2^{2b+4}Sw$, and since $S\\le T<2^b$, $L<b$ and $\\gamma=o(b)$, the final absolute error is less than $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$.",
        "2^{2b+4}S\\cdot28\\,2^\\gamma T^2L\\cdot2^{-6b}"),
  infer("S6.7.8","Because the true coefficients are integers and the error is strictly below $1/2$, the nearest integer to each represented value is the correct coefficient, in $[0,2^{3b})$, and fits in one signed $(3b+1)$-bit word.",
        "that value the unique correct coefficient."),
  infer("S6.7.9","With $Q_0=2^b$, the carries $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$ and the invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$, so the digits $d_j$ are the product's radix digits.",
        "To propagate carries, let $Q_0=2^b$."),
  infer("S6.7.10","The product is below $2^{2n}$, so removing only zero padding bits and keeping leading zeros outputs exactly $2n$ bits, also for zero inputs.",
        "Zero inputs obey the same invariant and"),
 ], page="exact-recovery",
 frm=["fixed-point-disk-grid","vector-norms-and-error-bounds","positional-number-representation-and-carries","floor-ceiling-and-rounding","int-as-convolution","permutation-cancellation"],
 salient="The final error $448b\\,2^{-b+\\gamma}$ is exponentially small in $b$, far below $1/2$, because precision $p=6b$ leaves about $4b$ spare bits after undoing the scales $2^{2b+4}S$, and $\\gamma=o(b)$.")

mult = show("S6",
 "The algorithm splits both $n$-bit inputs into radix-$2^b$ digits, places them on the source tensor by the coefficient-address map, applies the source transform to each, multiplies pointwise, applies the opposite-sign transform with scalings, rounds and propagates carries to output exactly the $2n$-bit product, in time $O(Tp\\,p^{1-\\kappa})$.",
 "Reduce multiplication to a cyclic convolution of digit lists on pairwise coprime prime axes, compute the convolution with transforms of coprime length obtained by resampling, and recover the exact integer coefficients by rounding and carrying.",
 mot("The source-transform procedures supply the three transforms needed for the radix-digit convolution: two forward transforms, a pointwise product and one opposite transform.","explicit",
     "The source-transform procedures now supply the three transforms needed"),
 [
  primes, intconv, crt, cconv, srct,
  infer("S6.6","Multiply the two transformed arrays coefficientwise exactly, truncating each real and imaginary part to $p$ fractional bits to give $z$; then compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$.",
        "Multiply corresponding complex coefficients exactly and truncate"),
  infer("S6.6b","By the cancellation lemma the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$; the second scale $2^{2b+4}S$ undoes the input scales and the remaining $S$, giving the original integer coefficient convolution.",
        "The two occurrences of $S$ in this algorithm undo different"),
  exact,
 ], page="mult-algorithm",
 frm=["int-as-convolution","crt-axis-map","source-transform","exact-recovery","permutation-cancellation","prime-lengths","complex-convolution","cyclic-convolution"],
 adds=[])

# ---------------- S7: parameter balance ----------------
rows = [
 ("S7.2.1","Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $p^{\\epsilon(1+c)}$ of $p$.","Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$"),
 ("S7.2.2","Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, a power $p^{1-\\epsilon c(1-\\tau)}$ of $p$, because $O(p/K)$ exchanges of width $K$ each cost $O(VK^\\tau)$.","Chunk exchanges for transform layout & $pK^{\\tau-1}$ & $1-\\epsilon c(1-\\tau)$"),
 ("S7.2.3","The simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, a power $p^{1-\\epsilon(1-\\lambda')}$ of $p$, as at most $\\ell$ rounds cost $O(Vd^{\\lambda'})$ each.","Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$"),
 ("S7.2.4","The Chinese-remainder map and axis layouts cost $d^2(1+\\ell^\\tau)$, a power $p^{\\tau+\\epsilon(2-\\tau)}$ of $p$.","CRT and axis layouts & $d^2(1+\\ell^\\tau)$ & $\\tau+\\epsilon(2-\\tau)$"),
 ("S7.2.5","The Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, a power $p^{3/4+\\delta+3\\epsilon/2}$ of $p$, since $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$.","Gaussian line maps & $dp^{1/2+\\delta}\\alpha$ & $3/4+\\delta+3\\epsilon/2$"),
 ("S7.2.6","Chirps, twists and scalar products cost $dp^\\delta$, a power $p^{\\epsilon+\\delta}$ of $p$.","Chirps, twists and scalar products & $dp^\\delta$ & $\\epsilon+\\delta$"),
 ("S7.2.7","The packed polynomial products cost $\\log(rp)=O(p^{1-\\epsilon})$ per unit volume, as there are $T/r$ records each needing four integer products on $O(rp)$ bits.","Packed polynomial products & $\\log(rp)$ & $1-\\epsilon$"),
]
rownodes=[infer(i,c,q) for i,c,q in rows]

balance = show("S7",
 "With $p=\\Theta(\\log n)$, $d=\\lfloor b^\\epsilon\\rfloor$ axes, chunk size $K$, ring dimension $r=2^{\\Theta(p/d)}$ and the exponents $\\tau=1-2^{-50}$, $\\lambda'=1-2^{-54}$, $c=2^{-56}$, $\\epsilon=2^{-75}$, $\\delta=1/16$, every row of the cost table has normalized power of $p$ at most $1-2\\kappa$, giving total time $O(Tp\\,p^{1-\\kappa})=O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
 "Tabulate the normalized cost of each operation (divided by $V=Tp$), take the exponent of $p$ in each row, compute the margin $g_i$ below one for each dominant row, and absorb any fixed power of $\\log p$ in the smallest margin.",
 mot("The explicit slack in the smallest margin covers any remaining fixed power of $\\log p$, so the overall exponent is $1-\\kappa$ where $2\\kappa$ is the smallest margin.","explicit",
     "This explicit slack will cover"),
 [
  infer("S7.0","The fixed rational parameters are $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$, $\\delta=1/16$, $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $C_1=20$, $\\epsilon=2^{-75}$, $\\kappa=2^{-182}$, satisfying all layer and dimension-exponent conditions.",
        "Take the following fixed rational numbers:", deferred=True),
  infer("S7.0b","The size parameters are $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, with $T\\in[4n/b,8n/b)$ a power of two, $r=2^{\\lceil(\\log_2T)/d\\rceil}$ and each axis length $r/2$ or $r$.",
        "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,", deferred=True),
  infer("S7.1","The cost table lists the operations' costs divided by $V=Tp=\\Theta(n)$, where each coefficient representation has $O(p)$ bits and a fixed number of repeated transforms is absorbed in the constants.",
        "Table~\\ref{tab:costs} lists costs after division"),
  show("S7.2",
   "Seven dominant rows of the cost table each have a normalized cost whose exponent of $p$ is below one by a computable margin.",
   "For each operation, bound the normalized cost by the lemma that proves it and substitute the size relations $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ to read off the power of $p$.",
   mot("Each row is the cost of one of the operations already analysed, divided by the volume; substituting the parameter sizes expresses each as a power of $p$.","recoverable"),
   rownodes),
  infer("S7.3","The seven margins below one are $g_1=1-\\epsilon(1+c)$, $g_2=\\epsilon c(1-\\tau)$, $g_3=\\epsilon(1-\\lambda')$, $g_4=1-\\tau-\\epsilon(2-\\tau)$, $g_5=1/4-\\delta-3\\epsilon/2$, $g_6=1-\\delta-\\epsilon$, $g_7=\\epsilon$, and direct substitution gives $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.",
        "g_1>\\frac12,\\quad g_2=2^{-181},\\quad g_3=2^{-129},"),
  infer("S7.4","Thus $\\min_ig_i=2^{-181}=2\\kappa$, attained by $g_2=\\epsilon c(1-\\tau)=2^{-75}\\cdot2^{-56}\\cdot2^{-50}$ from the chunk-exchange row.",
        "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
  infer("S7.5","Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
        "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
  infer("S7.6","Fixing one cutoff beyond all the size, precision, margin and layout conditions and using schoolbook multiplication below it, the single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length and outputs exactly the $2n$-bit product.",
        "Fix one cutoff beyond all the size, precision, margin and layout"),
 ], page="parameter-balance",
 frm=["simultaneous-layer","transform-layout","chunk-interchange","gaussian-resampling","ring-convolution","crt-axis-map","prime-lengths","logarithms-and-exponentials","asymptotic-notation-beyond-big-o"],
 salient="The exponent $\\kappa=2^{-182}$ is half the smallest margin $g_2=\\epsilon c(1-\\tau)=2^{-181}$: three tiny exponents multiply, namely the axis exponent $\\epsilon=2^{-75}$, the chunk exponent $c=2^{-56}$ and the interchange saving $1-\\tau=2^{-50}$, since the exchange row $pK^{\\tau-1}$ with $K=p^{\\epsilon c}$ is only $p^{-\\epsilon c(1-\\tau)}$ below $p$.")

# ---------------- root ----------------
root = show("S0",
 "There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture in this model.",
 "Reduce multiplication to a convolution computed by transforms of coprime length, and obtain a power saving in the logarithmic factor from two tape procedures (fast address interchange and simultaneous butterfly layers), each built on a finite linear network with a rank saving $s<Wm$; then assemble the exact product and balance the parameters.",
 mot("Scanning an array of $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both movement and arithmetic.","explicit",
     "We therefore need savings in both movement and arithmetic."),
 [S1, S2, S3, ringconv, S5, mult, balance,
  infer("S0.1","An eventual lower bound $T_A(n)\\ge c_An\\lg n$ for every fixed machine is refuted by one machine with $\\liminf T_A(n)/(n\\lg n)=0$, and the power saving gives limit zero through all input lengths, so the $n\\log n$ optimality conjecture fails in this model.",
        "Its negation requires one machine satisfying", deferred=True)],
 page="main-theorem",
 frm=["fixed-tape-model","nlogn-conjecture","tape-machines","big-o","logarithms-and-exponentials","determinism-and-exact-versus-approximate-computation","nlogn-multiplier"],
 adds=[B("n","input length","the number of bits in each of the two input integers","count"),
       B("\\kappa","saving exponent","the fixed constant $2^{-182}$ by which the logarithmic factor is reduced","direct"),
       B("p","working precision","the number of fractional bits of the fixed-point numbers, $p=6b=\\Theta(\\log n)$","count"),
       B("d","number of axes","the number of axes of the transform tensor, $d=\\lfloor b^\\epsilon\\rfloor$","count"),
       B("V","stored volume","the number of stored data bits of the array being processed","count"),
       B("W","number of wires","the number of wires, including scratch wires, of the finite linear network","count"),
       B("m","label dimension","the dimension of the label space of the network","count"),
       B("s","total rank","the sum of the ranks of all edge differences, which is the number of smaller calls per network invocation","count"),
       B("T","padded box size","the number of entries of the padded array, a power of two equal to the product of the axis lengths","count"),
       B("\\ell","ring log-dimension","the base-two logarithm of the ring dimension $r$","count")])

json.dump({"root":root}, open(P+'exegenius/tasks/0003-argument.answer.json','w'), indent=1)

# ---------------- verification ----------------
def walk(n, out):
    out.append(n)
    for c in n.get('children',[]) or []:
        walk(c,out)
nodes=[]; walk(root,nodes)
ids=[n['id'] for n in nodes]
assert len(ids)==len(set(ids)), [i for i in ids if ids.count(i)>1]
last=-1; bad=False
for n in nodes:
    if n['intention']=='infer':
        q=n['quote']['quote']; c=SRC.count(q)
        if c==0: print("MISSING",n['id'],repr(q)); bad=True; continue
        if c>1: print("MULTI",c,n['id'],repr(q))
        pos=SRC.index(q)
        if not n.get('deferred'):
            if pos<=last: print("ORDER",n['id'],pos,last,SRC[:pos].count('\n')+1)
            last=max(last,pos) if pos>last else last
    else:
        m=n['motivation']
        if m['quote'] and SRC.count(m['quote']['quote'])==0: print("MOTMISSING",n['id'],repr(m['quote']['quote']))
        if m['source']=='explicit' and not m['quote']: print("EXPLICIT w/o quote",n['id'])
print(len(nodes),"nodes")
# pages
pages=[n.get('page') for n in nodes if n.get('page')]
print(len(pages),len(set(pages)))
