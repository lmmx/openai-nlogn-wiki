import json, sys, re
ROOT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2V"
SRC = open(ROOT + "/sources/paper.tex").read()

def ev(q):
    return {"source": "paper", "quote": q}

def bind(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

def leaf(id, claim, quote, frm=None, page=None, salient=None, deferred=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if deferred: n["deferred"] = True
    return n

def show(id, claim, method, mot, children, page=None, frm=None, salient=None, adds=None):
    text, src, quote = mot
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": text, "source": src, "quote": ev(quote) if quote else None},
         "children": children, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

R = "recoverable"; E = "explicit"; C = "reconstructed"

# ---------------------------------------------------------------- S2.1 finite networks
gadget = show(
 "S2.1.1",
 r"For arbitrary initial scratch values, one forward invocation of the gather, scatter and side-injection gadget indexed by three-element subsets changes $y_S$ to $y_S+x_S$ and changes nothing else.",
 "Compute the net change of the eight-row schedule on the target: the first two rows cancel the old scratch contents, the next rows add the central and side contributions, the last rows restore the scratch; then read off the coefficient of $x_T$ in $y_S$ as a function of $|S\\cap T|$",
 ("The net target change is a fixed linear combination of the inputs alone, so it suffices to compute its coefficients; these depend only on the intersection size $|S\\cap T|$, which the side wires can correct pair by pair.", R, None),
 [
  leaf("S2.1.1a", r"The first two rows subtract $\mathcal J a+\mathcal R c$ from $y$, the middle rows add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$ and the last rows restore $c,a$, so the net target change $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ does not depend on the scratch values $a,c$.",
       r"If the initial side and central vectors are $a,c$, the first two rows"),
  leaf("S2.1.1b", r"In the bit construction the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$; the side wires cancel exactly the intersection-one cases, intersection zero or two already give zero, and the self coefficient is one.",
       r"In the bit case, the central coefficient from $x_T$ to $y_S$ is"),
  leaf("S2.1.1c", r"In the complex construction the central coefficient is $(|S\cap T|-1)/2$; the side wires cancel it for distinct triples with intersection zero or two, intersection one contributes zero, and the self coefficient is one.",
       r"In the complex case, the central coefficient is $(|S\cap T|-1)/2$."),
 ],
 page="triple-gadget",
 frm=["bitwise-xor","modular-arithmetic-and-residues","rational-numbers-dyadic-rationals-and-exact-arithmetic","quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o"],
 salient=r"Two quite different constructions (bits over $\mathbb F_2$ with central coefficient $|S\cap T|\bmod 2$, and Gaussian dyadics with central coefficient $(|S\cap T|-1)/2$) both end with exactly the net map $y\leftarrow y+x$: the self coefficient is $1$ in both because $|S\cap S|=3$, and the side wires are tuned to kill the other intersection sizes.")

bank = leaf("S2.1.2",
 r"Running the forward schedule from $X$ to $Y$, the inverse schedule from $Y$ to $X$, and the forward schedule again sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restores every scratch wire.",
 r"$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
 frm=["triple-gadget"], page="bank-exchange-network")

frames = leaf("S2.1.3",
 r"If every wire touched by a gate carries its array in the same invertible frame $D_v$, the pointwise linear gate commutes with the frame, so the whole network implements $D_{\mathrm{out}}\,\mathsf S\,D_{\mathrm{in}}^{-1}$ and only the edge changes $D_vD_u^{-1}$ cost anything.",
 r"Thus the common frame commutes with the pointwise gate, and",
 frm=["bank-exchange-network","matrices-invertibility-and-rank","algebraic-structures-groups-rings-and-isomorphisms"], page="frames")

labels = show(
 "S2.1.4",
 r"Attaching to the gates and terminals of the $W$-wire bank-exchange network nondegenerate subspaces of an $m$-dimensional space, nested along every edge, makes the dimension changes along edges total $s=Wm-N+2L<Wm$.",
 "Count the dimension changes: the terminal labels fix the signed total, every decrease is confined to one edge per central wire, and the total loss $L$ is bounded against the bank size $N$",
 ("The saving is the gap between the sum of absolute label changes and $Wm$, and it is controlled by keeping the dimension lost on decreasing edges small.", E, r"The saving will come from keeping the total dimension lost on decreasing"),
 [
  leaf("S2.1.4a", r"The terminal labels give source dimensions summing to $N$ and sink dimensions summing to $Wm-N$, so the signed dimension changes along edges total $Wm-2N$ because the contributions at gates cancel.",
       r"The source dimensions sum to $N$ and the sink dimensions to $Wm-N$."),
  leaf("S2.1.4b", r"The only decreasing edges are the central-wire edges between times 3 and 4, each losing $h=100$ dimensions; every other edge joins a label to a larger or equal one.",
       r"edges are the central-wire edges from time 3 to time 4; their dimension"),
  leaf("S2.1.4c", r"With $L$ the total dimension lost on the decreasing edges, replacing signed by absolute changes adds $2L$, so the absolute changes total $Wm-2N+2L$.",
       r"There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
  leaf("S2.1.4d", r"The loss ratios are $L/N=100/539$ for the bit network and $101/539$ for the complex network, so $L<N/2$ in both.",
       r"In particular, both are smaller than $1/2$."),
  leaf("S2.1.4e", r"The $N$ negative source projections cost one extra rank each, so the sum of edge ranks is $s=Wm-N+2L$, which is strictly below $Wm$ because $N-2L>0$.",
       r"Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$."),
 ],
 frm=["bilinear-orthogonal","frames","bank-exchange-network","triple-gadget","vector-spaces-basis-and-dimension","matrices-invertibility-and-rank"],
 salient=r"The rank sum $s$ is only barely below $Wm$ (relative deficit about $10^{-11}$), yet strictly below. The deficit equals $N-2L$ and is positive only because the unavoidable loss on the central wires is a fraction $100/539$ (resp. $101/539$) of $N$, below one half.",
 adds=[bind("N","bank size","number of triples $a$, i.e. the number of wires in each of the data banks $X$ and $Y$","count"),
       bind("L","decreasing-edge loss","total dimension lost along all decreasing edges","count")])

phase = show(
 "S2.1.5",
 r"In the complex network with binary labels and Gaussian dyadic scalars, each edge's frame change is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual, and after endpoint corrections every role, scratch roles included, carries $C^{\otimes m}$, using $s<Wm$ kernels in total.",
 "Use that Hamming weight is additive modulo four on orthogonal binary vectors to turn each label change into one phase per residual basis vector, rewrite each phase as a translation kernel by conjugating with $H$, and telescope along the network",
 ("Weight modulo four is the quantity the binary labels make additive, so the phase frames $i^{q_U(x)}$ change by one simple factor per residual basis vector.", R, None),
 [
  leaf("S2.1.5a", r"For orthogonal binary vectors the supports meet in an even number of positions, so Hamming weight is additive modulo four, which gives $q_V(x)-q_U(x)=\sum_{v}\operatorname{wt}(v)[v\cdot x]\pmod 4$ over an orthonormal basis of the residual.",
       r"If $z\cdot w=0$, the intersection cardinality is even, so weight is"),
  leaf("S2.1.5b", r"Because each basis vector has odd weight, each phase is $i^{\pm[v\cdot x]}=\frac{1\pm i}{2}+\frac{1\mp i}{2}(-1)^{v\cdot x}$, and conjugation by $H$ turns the character $(-1)^{v\cdot x}$ into the translation $X_v$, giving the kernel $aI+bX_v$ or its inverse.",
       r"The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the"),
  leaf("S2.1.5c", r"After the $Z$-sign and phase corrections on the $X_a\to Y_a$ route (using $C=iZC^{-1}Z$) and after undoing the bank exchange, every role carries $C^{\otimes m}$.",
       r"the required forward tensor product."),
 ],
 page="phase-kernel-network",
 frm=["bilinear-orthogonal","subspace-labels","frames","bitwise-xor","complex-numbers","matrices-invertibility-and-rank"],
 salient=r"Every role of the network, data banks and scratch wires alike, ends with the same operator $C^{\otimes m}$, although the edges along the way carry many different kernels.")

power_tau = show(
 "S2.1.6",
 r"For $\tau=1-2^{-50}$ the rank sum satisfies $s/W<m^\tau$ for both networks.",
 "Compare the relative rank deficit with the exponential lower bound $m^{1-\\varepsilon}>m(1-\\varepsilon\\log m)$",
 ("A strict rank deficit of the network must be turned into a concrete exponent below one, and this is done by comparing it with the first-order expansion of $m^{-\\varepsilon}$.", R, None),
 [
  leaf("S2.1.6a", r"Both relative rank deficits $\eta=(Wm-s)/(Wm)$ exceed $20\cdot2^{-50}$.",
       r"Both exact deficits displayed above are greater than $20\cdot2^{-50}$."),
  leaf("S2.1.6b", r"Since $m<2^{20}$ one has $m^{1-2^{-50}}>m(1-20\cdot2^{-50})>m(1-\eta)$, that is $s/W<m^{\tau}$.",
       r">m(1-20\cdot2^{-50})>m(1-\eta)"),
 ],
 salient=r"The exponent is only $2^{-50}$ below one, because the rank deficit of $s$ below $Wm$ is tiny (about $10^{-11}$ of $Wm$); a strict but minute deficit is all a power saving needs.")

networks = show(
 "S2.1",
 r"There are two fixed linear networks of $W$ wires that exchange two banks of values and restore every scratch value, with labels in an $m$-dimensional space whose edge dimension changes total $s<Wm$, indeed $s/W<m^\tau$ with $\tau=1-2^{-50}$.",
 "Build the network gadget by gadget (subset gadget, three-stage exchange, frame bookkeeping), then attach nested subspace labels to bound the total edge rank, and finally derive each network's interface and the explicit exponent",
 ("The cost of an edge is the number of smaller operations it needs, so the labels must be chosen to keep the edge changes cheap.", E, r"choose its intermediate labels to make the changes of frame inexpensive."),
 [gadget, bank, frames, labels, phase, power_tau],
 page="subspace-labels",
 frm=["bilinear-orthogonal","triple-gadget","bank-exchange-network","frames","vector-spaces-basis-and-dimension"])

# ---------------------------------------------------------------- S2.2 chunk interchange
tri = leaf("S2.2.1",
 r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones.",
 r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization",
 frm=["matrices-invertibility-and-rank","permutations-and-permutation-matrices","rational-numbers-dyadic-rationals-and-exact-arithmetic"], page="triangular-factorization")

shear = show(
 "S2.2.2",
 r"For a rational $m\times m$ matrix $A$ of rank $a$, the address update $(H,D)\mapsto(H+AD,D)$ over the integers modulo a power of a fixed odd prime takes exactly $a$ interchanges of pairs of fields plus $O(V)$ further work.",
 "Factor $A=E_1\\Pi E_2$, perform the lower triangular factors by controlled shifts in linear time, and perform each one of $\\Pi$ with a single interchange wrapped between two controlled shifts",
 ("Triangular changes of coordinates only add earlier fields to later ones, which is the linear-time direction of controlled shifts, so only the partial permutation $\\Pi$ needs genuine interchanges.", R, None),
 [
  leaf("S2.2.2a", r"A lower triangular transformation of the fields of $H$ (or of $D$) costs $O(V)$ by controlled shifts and unit scalings, updating coordinates in descending physical order.",
       r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
  leaf("S2.2.2b", r"Each one of $\Pi$ calls for $H_i\leftarrow H_i+D_j$, done by $D_j\leftarrow D_j+H_i$, an interchange $(H_i,D_j)\leftarrow(D_j,H_i)$, and $D_j\leftarrow H_i-D_j$, which uses exactly one interchange, so $a$ ones cost $a$ interchanges.",
       r"On an initial pair $(h,d)$ this sequence yields $(h+d,d)$."),
 ],
 page="matrix-shear",
 frm=["controlled-shifts","triangular-factorization","stream-arrays","matrices-invertibility-and-rank","modular-arithmetic-and-residues"],
 salient=r"The number of interchanges equals the rank $a$ of $A$, not the matrix size $m$; this is why the dimension changes (ranks) of the edges, and not the full dimension, are what is paid for.")

power_width = show(
 "S2.2.3",
 r"If the row count before both chunks is divisible by $W^k$, two chunks of $e=m^k$ radix-$q$ digits are interchanged in $O(Ve^\tau)$ time.",
 "Run the bank-exchange network with address-shear frames on $W$ role streams of volume $V/W$; each edge is a shear costing rank-many smaller interchanges, so the cost per volume obeys a recurrence with ratio $s/W<m^\\tau$",
 ("Multiplying the width by $m$ multiplies the recursive contribution only by $s/W<m$, and this strict inequality is what yields a power saving.", E, r"is the source of the power saving."),
 [
  leaf("S2.2.3a", r"Split rows cyclically into $W$ role streams, each of volume $V/W$ and with the same remaining shape, so the network gates act pointwise on matching addresses.",
       r"Split whole rows cyclically into $W$ role streams within each prefix"),
  leaf("S2.2.3b", r"On each network edge $e'$ apply the shear $\Phi_{A_{e'}}$ to that role stream, implemented by recursively interchanging each pivot pair of fields of $e/m$ digits.",
       r"Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair"),
  leaf("S2.2.3c", r"By the common-frame identity the frames cancel, leaving the shear $H\leftarrow H+D$ on every row, scratch roles included, whatever their initial contents.",
       r"is $H\leftarrow H+D$ on every original row, including rows assigned"),
  leaf("S2.2.3d", r"The three updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ interchange the chunks; only the middle shear uses the network and the others cost $O(V)$.",
       r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
  leaf("S2.2.3e", r"The shear step makes exactly $s$ recursive calls, each on one role stream of volume $V/W$.",
       r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
  leaf("S2.2.3f", r"The cost per volume therefore satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
       r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
  leaf("S2.2.3g", r"Since $s/W<m^\tau$, the geometric sum $\sum_{j\le k}(s/W)^j$ is $O(m^{k\tau})$, so $F_k=O(e^\tau)$.",
       r"For $a=s/W<m^\tau$ the geometric sum"),
 ],
 page="power-width-interchange",
 frm=["bank-exchange-network","frames","subspace-labels","matrix-shear","stream-arrays","controlled-shifts"],
 salient=r"The cost per volume grows only like $e^\tau$ with $\tau<1$, a power saving over the naive cost linear in the width $e$, and this is exactly because the branching ratio $s/W$ is strictly less than $m^\tau$ while the width grows by the factor $m$ at each level.",
 adds=[bind("e","chunk digit count","number of radix-$q$ digits in each of the two chunks, equal to $m^k$","count"),
       bind("k","recursion depth","number of times the width has been multiplied by $m$","count"),
       bind("F_k","normalized cost","uniform upper bound for the time divided by the logical volume when the chunks have $m^k$ digits","direct")])

arbitrary = show(
 "S2.2.4",
 r"For chunks of arbitrary width $u$ bits in an arbitrary bit array, the interchange costs $O(Vu^\tau)$.",
 "Reduce arbitrary widths to power-width pieces: take rows from the chunks' own high digits, pad the rows, split the remaining width in base $m$, and pad binary chunks to a radix-$q$ range",
 ("The power-width procedure needs many rows and a width $m^k$, and both can be supplied cheaply from the chunks' own digits.", E, r"Rows for a general array can be supplied by a few of its own high digits."),
 [
  leaf("S2.2.4a", r"Interchange the top $\rho=O(\log e)$ digits of the chunks one pair at a time and join them, so the two top fields form a row field of range at least $W^k$ before both remaining chunks.",
       r"Write each chunk as its top $\rho$ digits followed by its remaining"),
  leaf("S2.2.4b", r"Pad the row count to a multiple of $W^k$, which at most doubles the volume.",
       r"R'=W^k\left\lceil R/W^k\right\rceil<2R."),
  leaf("S2.2.4c", r"Write the remaining width in base $m$ and apply the power-width interchange to $a_j$ pairs of pieces of width $m^j$.",
       r"e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m."),
  leaf("S2.2.4d", r"The piece costs add up geometrically to $O(Ve^\tau)$.",
       r"O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)."),
  leaf("S2.2.4e", r"Pad binary chunks of $u$ bits to a radix-$q$ range with $e=O(u)$ digits, which enlarges the volume by a fixed factor, so the bound becomes $O(Vu^\tau)$.",
       r"Finally, for binary chunks let $e$ be the least integer with"),
 ],
 frm=["power-width-interchange","stream-arrays","logarithms-floors-ceilings-and-powers-of-two"])

chunk = show(
 "S2.2",
 r"Two disjoint address chunks of $u$ bits in any bit array of volume $V$ can be interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$, although the intermediate steps form XOR combinations of data.",
 "Turn the bit network into a recursive tape procedure: edge rank counts smaller interchanges through address shears, solve the resulting recurrence for power widths, then remove the width and row restrictions",
 ("Because the sum of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", E, r"Because the sum of these ranks is less than the number of wires times"),
 [tri, shear, power_width, arbitrary],
 page="chunk-swap",
 frm=["stream-arrays","controlled-shifts","subspace-labels","fixed-tape-model","bitwise-xor"],
 adds=[bind("u","chunk width","number of bits in each of the two address chunks being interchanged","count")])

# ---------------------------------------------------------------- S2.3 simultaneous layer
b1 = show(
 "S2.3.1",
 r"A $C^{\otimes e}$ layer on $e=mf$ selected axes reduces to $s$ child layers on $f$ axes plus a fixed number of binary row additions, and $C$ determines $H_0$ through $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$.",
 "Conjugate each edge's product of kernels by a change of basis $\\mathcal P_M$ so that the residual directions become the first coordinate directions, one child per direction, and express $\\mathcal P_M$ by row additions",
 ("Phase frames express a $C$ tensor product through smaller groups of selected bits, separated by binary changes of basis.", E, r"frames express a $C$ tensor product using smaller groups of"),
 [
  leaf("S2.3.1a", r"The two-point kernel $C$ satisfies $H_0=b\mathsf SC\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=-iZCZ$ with Gaussian dyadic coefficients only.",
       r"H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"),
  leaf("S2.3.1b", r"Extending the residual basis to a basis of $\mathbb F_2^m$ and using it as the columns of $M$, each edge's frame change equals $\mathcal P_M\bigl(\prod_j C_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$ for the address permutation $\mathcal P_M$.",
       r"Extend $v_1,\ldots,v_{\rho_{\rm edge}}$ to a basis of $\mathbb F_2^m$ and take these vectors as"),
  leaf("S2.3.1c", r"After $\mathcal P_M^{-1}$ on each column, each of the $\rho_{\rm edge}$ residual directions is one child call on the $f$ axes of one slot; an inverse kernel needs only a forward child plus sign and phase wrappers, so the edges give exactly $s$ children.",
       r"$1\le h\le\rho_{\rm edge}$, apply $(C^{\epsilon_h})^{\otimes f}$ to the"),
  leaf("S2.3.1d", r"Gaussian elimination writes $M$ as a fixed number of elementary row additions, and one row addition XORs the corresponding selected bits of two whole slots.",
       r"Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$"),
  leaf("S2.3.1e", r"On all $D$ selected coordinates the normalized butterfly layer is $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $\mathcal S_D$ a diagonal phase, so the exact $C$ layer converts to the $H_0$ layer by Gaussian dyadic phase operations.",
       r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D."),
 ],
 frm=["phase-kernel-network","butterfly-layers","bitwise-xor","complex-numbers"],
 adds=[bind("D","layer axis count","number of address chunks, at most $d$, on whose selected bits the layer acts","count"),
       bind("f","slot size","number of axis chunks in each of the $m$ slots of a group","count")])

b2 = show(
 "S2.3.2",
 r"A binary row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on the selected bit of each of $f$ chunks costs $O(V(L^\tau+1))$ in total, restoring a third chunk $z$ whatever its initial contents.",
 "Pack the $f$ one-bit additions into eight whole-chunk cyclic shifts that act correctly whenever the guard bits of each segment avoid carries, then repair the explicitly bounded set of bad addresses by sorting only the extracted records",
 ("Doing the $f$ additions one after another would again cost $f$ passes, so they are packed into whole-chunk shifts, with a small explicit exceptional set repaired deterministically.", R, None),
 [
  leaf("S2.3.2a", r"Eight conditional $\pm1$ additions on the pair $(u,w)$ flip the parity of $u$ exactly when the control is 1 and restore the auxiliary integer $w$.",
       r"is flipped precisely when $c=1$, both quotients under division by two are"),
  leaf("S2.3.2b", r"Applying each line to all $f-1$ segments simultaneously is a single cyclic shift of a whole chunk by an offset depending only on the other two chunks, so it costs one swap-conjugated linear pass.",
       r"Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all"),
  leaf("S2.3.2c", r"Segments with guard values in $[10,2^{K-1}-11]$ never carry into neighbours, and the bad addresses form a fraction at most $\delta_{\rm bad}=80(f-1)2^{-K}$ of all addresses, independently of the payload.",
       r"There are exactly twenty excluded values for each guard in"),
  leaf("S2.3.2d", r"Each rotation is realized by chunk interchanges of width $L=fK$ costing $O(VL^\tau)$, a controlled cyclic shift in $O(V)$, and the undoing interchange.",
       r"Pass only $L$ and these three positive canonical lengths to"),
  leaf("S2.3.2e", r"The bad records are extracted, tagged with their destination ranks, stably radix-sorted and reinserted, which applies the ideal permutation everywhere.",
       r"To implement the correction, scan the stream with a record-rank counter."),
  leaf("S2.3.2f", r"The movement costs $O(V(L^\tau+1))$ and the scans and the sorted exceptional stream add only lower-order terms when $K/\log p\to\infty$.",
       r"The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans"),
 ],
 page="packed-selected-bits",
 frm=["chunk-swap","controlled-shifts","stream-arrays","bitwise-xor","modular-arithmetic-and-residues"],
 adds=[bind("L","slot width","number of address bits $fK$ in one slot of $f$ chunks","count")])

b3 = show(
 "S2.3.3",
 r"Splitting complete rows among the $W$ roles gives each of the $s$ children volume $V/W$, so the cost per volume of a layer on $e$ chunks obeys $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and unrolls to $O(d^{\lambda'})$.",
 "Obtain rows from the first $q_0$ chunks, send whole rows to the $W$ roles, recurse down to a cutoff $e<d^{\\beta}$ with individual kernels, and sum the internal and leaf contributions over a base-$m$ partition of the chunks",
 ("Splitting complete rows among the network's wire roles reduces the volume of each recursive call by the factor $W$.", E, r"the network's wire roles then reduces the volume of each recursive"),
 [
  leaf("S2.3.3a", r"Apply $C$ individually to the first $q_0=O(\log d)$ chunks and use their bits as a row index of range at least $W^{k_0}$, padding rows to a multiple of $W^{k_0}$ (the volume at most doubles).",
       r"regard their concatenated bits as one row index."),
  leaf("S2.3.3b", r"Each recursive edge call acts on one role stream whose volume is exactly $1/W$ of its parent's volume.",
       r"one role stream with volume exactly \(1/W\) of its parent's logical"),
  leaf("S2.3.3c", r"With $F(e)$ the time divided by the current volume, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ below the cutoff $e<d^\beta$.",
       r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
  leaf("S2.3.3d", r"At an internal node $K\le e^{c/\beta}$, so the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.",
       r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\)."),
  leaf("S2.3.3e", r"Since $a=s/W<m^\lambda$, the internal costs sum geometrically to $O(e^\lambda)$.",
       r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)."),
  leaf("S2.3.3f", r"The leaves, each of fewer than $d^\beta$ chunks, contribute at most $O(e^\sigma d^{\beta(1-\sigma)})$.",
       r"O(a^ju)\le O(e^\sigma u^{1-\sigma})"),
  leaf("S2.3.3g", r"Adding the logarithmically many base-$m$ groups gives $O(d^{\lambda'})$ for any fixed $\lambda'$ with $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1$.",
       r"\bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right)"),
 ],
 frm=["power-width-interchange","chunk-swap","packed-selected-bits"])

b4 = show(
 "S2.3.4",
 r"Every intermediate coefficient of the whole layer is an exact Gaussian dyadic needing only $p+\Delta$ fractional bits and $\Delta+3$ integer bits with $\Delta=o(p)$, so the layer is exact until its single final truncation.",
 "Bound the arithmetic dependency depth of the recursion by $A(e)\\le sA(e/m)+E$, then convert depth into denominator and magnitude growth",
 ("The accelerated network is evaluated exactly, so one must show that the dyadic denominators and magnitudes stay within $O(p)$ bits.", E, r"evaluated exactly before one final truncation."),
 [
  leaf("S2.3.4a", r"The arithmetic dependency depth satisfies $A(e)\le sA(e/m)+E$ at an internal node, because all $s$ child calls are concatenated.",
       r"A(e)\le sA(e/m)+E"),
  leaf("S2.3.4b", r"Unrolling gives $A(e)\le 8B^2d^{\nu+1}$, polynomial in $d$.",
       r"A(e)\le 8dB^{k+1}\le8B^2d^{\nu+1}."),
  leaf("S2.3.4c", r"A value at arithmetic depth $j$ lies in $2^{-(p+j)}\mathbb Z[i]$ with modulus at most $2^j$, so $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits hold every intermediate exactly, with $\Delta=\lceil C_0d^{C_1}\rceil$.",
       r"lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most"),
  leaf("S2.3.4d", r"Choosing $\epsilon C_1<1$ makes $\Delta=o(p)$, so the exact width stays $O(p)$.",
       r"Choose \(\epsilon C_1<1\)."),
 ],
 frm=["fixed-point-disk-grid","phase-kernel-network"],
 adds=[bind("\\Delta","guard width","number of extra fractional bits (and of extra integer bits) reserved so that all intermediate values are exact","count")])

simul = show(
 "S2.3",
 r"Applying the normalized butterfly $H_0$ to one bit position in each of $D\le d$ address chunks of polynomial records takes $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$, exact until one final truncation with error below $\sqrt2\,2^{-p}$.",
 "Express the $C^{\\otimes D}$ layer through the complex bank-exchange network's phase frames recursively, implement the binary basis changes by packed whole-chunk operations, split rows among the roles for volume $V/W$ per child, bound the dyadic growth, and convert $C$ to $H_0$",
 ("Separate butterfly factors would need $D$ whole-array passes, while the simultaneous layer costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.", E, r"$\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly"),
 [b1, b2, b3, b4,
  leaf("S2.3.5", r"Combining the row construction and the recurrence gives total time $O(Vd^{\lambda'})$ on fixed tapes, including padding, repair and cleanup.",
       r"above give total time $O(Vd^{\lambda'})$ on fixed tapes, including"),
  leaf("S2.3.6", r"Every row of $H_0^{\otimes D}$ has absolute row sum one, so disk arrays stay in the disk and the final truncation $Q_p$ changes each coefficient by less than $\sqrt2\,2^{-p}$.",
       r"Finally, every row of $\mathcal H$ has"),
 ],
 page="simultaneous-butterfly-layer",
 frm=["phase-kernel-network","butterfly-layers","fixed-point-disk-grid","chunk-swap","packed-selected-bits","negacyclic-ring"],
 adds=[bind("\\lambda'","butterfly exponent","fixed exponent less than 1 in the cost $O(Vd^{\\lambda'})$ of a simultaneous layer","direct")])

tools = show(
 "S2",
 r"Two fast tape procedures exist: interchange of two $u$-bit address chunks in $O(Vu^\tau)$ time, and a simultaneous normalized butterfly layer on $d$ chunks in $O(Vd^{\lambda'})$ time, with $\tau,\lambda'<1$, both obtained from a network of $W$ wires whose edge ranks total $s<Wm$.",
 "Construct a fixed linear network exchanging two banks with a rank saving, then use it twice recursively: with bit values for address interchange, with Gaussian dyadic values for the butterfly layer",
 ("The decisive property of the network is that the total number $s$ of smaller calls is less than $Wm$.", E, r"number $s$ of smaller calls satisfies $s<Wm$."),
 [networks, chunk, simul],
 frm=["fixed-tape-model","stream-arrays"],
 adds=[bind("V","stored volume","number of stored data bits of the array being processed","count"),
       bind("W","wire count","number of wires, i.e. roles, of the bank-exchange network","count"),
       bind("m","label dimension","dimension of the ambient label space, which is also the number of digit fields per piece in the recursion","count"),
       bind("s","total edge rank","sum over all edges of the rank of the edge change, i.e. the number of smaller calls per network invocation","count"),
       bind("\\tau","interchange exponent","fixed exponent below 1 with $s/W<m^{\\tau}$","direct")])

# ---------------------------------------------------------------- S3 transforms
s311 = leaf("S3.1.1",
 r"Although $\mathbb C[y]/(y^r+1)$ has zero divisors, $\sum_{k=0}^{t-1}\omega_t^{jk}$ is $t$ if $t\mid j$ and $0$ otherwise, so $F_t^+F_t^-=t^{-1}I$.",
 r"the summands and multiplies their sum by",
 frm=["negacyclic-ring","dft-cyclic-convolution","algebraic-structures-groups-rings-and-isomorphisms","geometric-series-and-orthogonality-of-sums-of-roots-of-unity"],
 page="synthetic-transform",
 salient=r"The orthogonality of characters holds in a ring with zero divisors, where one cannot divide by $\omega_t^j-1$: shifting the index by $t/2^{v+1}$ multiplies the sum by $y^{rj_0}=-1$, forcing the sum to vanish.")

s312 = show(
 "S3.1.2",
 r"Decimation in frequency computes $F_t^-$ with two-point butterflies $H_0$ and twiddle monomials, leaving the frequencies in bit-reversed order, which the opposite transform consumes directly.",
 "Recurse on the two halves of each length-$t$ array after one butterfly-and-twiddle level, track which slots hold which frequency bits, and run the levels backwards for the opposite transform",
 ("Computing the transform level by level in place leaves the frequency bits in reverse significance, so the opposite procedure should simply traverse the levels in reverse.", R, None),
 [
  leaf("S3.1.2a", r"Decimation in frequency pairs $z_k$ with $z_{k+t/2}$, replaces them by the butterfly $H_0$, multiplies the second output by $\omega_t^{-k}$ and recurses on both halves; this computes $F_t^-$.",
       r"the $b=1$ output by $\omega_t^{-k}$, and then apply the length-$t/2$"),
  leaf("S3.1.2b", r"After all rounds the frequency bits sit from low to high in the slots from high to low, so the entry of frequency $j$ is stored at slot $\operatorname{rev}_a(j)$ with no explicit sorting.",
       r"After all $a$ rounds, the named slots from high to low therefore"),
  leaf("S3.1.2c", r"Traversing the recursion in reverse implements $F_t^+B_t^{-1}$, so the two exact procedures are $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
       r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
  leaf("S3.1.2d", r"On several axes the twiddle of one axis commutes with the butterflies of the others, so a round is one parallel butterfly $\mathcal H$ followed by one recordwise monomial multiplication $y^E$.",
       r"Consequently the individual axis steps may be grouped as a parallel"),
 ],
 page="butterfly-layers",
 frm=["synthetic-transform","dft-cyclic-convolution","multidim-transform","permutations-and-permutation-matrices"],
 salient=r"The transform output is left in bit-reversed order and never sorted: the opposite transform reads exactly that stored order, so the reversal is never paid for.")

s31 = show(
 "S3.1",
 r"The forward synthetic transform of $M$ records and its opposite procedure, run on an explicit layout permutation $L$, have error below $\sqrt2\,\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.",
 "Realize each decimation-in-frequency round as a simultaneous butterfly layer after a layout permutation that puts the selected bits of all axes at a common offset in consecutive $K$-bit chunks, and charge the layout, the prefix rounds and the layer rounds separately",
 ("The simultaneous layer needs the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks.", E, r"we must place the selected bits of the participating axes at a common"),
 [s311, s312,
  leaf("S3.1.3", r"Moving at most $O(dK)$ bit slots into a prefix, at cost $O(TpdK)$, leaves each long or short axis as $\lfloor(\ell-1)/K\rfloor$ consecutive $K$-bit chunks.",
       r"outside the prefix now consists of $q$ consecutive $K$-bit chunks."),
  leaf("S3.1.4", r"Rearranging the chunks so that chunk $j$ of all axes are adjacent takes fewer than $d\ell/K$ exchanges of width-$K$ chunks, each $O(TpK^\tau)$, so the layout costs $O(Tp\cdot pK^{\tau-1})$.",
       r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
  leaf("S3.1.5", r"Each round on the remaining chunks selects the same bit offset in $d-1$ consecutive $K$-bit chunks, so it is one simultaneous layer; at most $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$.",
       r"The simultaneous-layer procedure therefore applies at cost"),
  leaf("S3.1.6", r"The at most $K$ rounds on bits left in the prefix are done bit by bit at cost $O(TpdK)$.",
       r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
  leaf("S3.1.7", r"A contraction does not increase an accumulated error and each round adds one truncation error below $\sqrt2\,2^{-p}$, so at most $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$ and keep values in the disk.",
       r"zero error, at most $\ell$ rounds therefore"),
 ],
 page="transform-layout",
 frm=["synthetic-transform","butterfly-layers","simultaneous-butterfly-layer","chunk-swap","stream-arrays","fixed-point-disk-grid","negacyclic-ring"])

s321 = show(
 "S3.2.1",
 r"Two disk-grid polynomials $f,g$ modulo $y^r+1$ are multiplied exactly, and $Q_p(fg/r)$ is returned, in time $O(rp\log(rp))$ using four products of integers of $O(rp)$ bits.",
 "Signed Kronecker substitution: evaluate the integer-coefficient parts at $B_0=2^{4p}$, multiply the resulting integers with the established $O(N\\log N)$ multiplier, and recover signed coefficients by centered carries",
 ("The reduction to integer products is a signed form of Kronecker substitution, so the established integer multiplier can do the polynomial products.", R, None),
 [
  leaf("S3.2.1a", r"Evaluating each integer-coefficient part at $B_0=2^{4p}$ gives signed integers of at most $4pr$ bits, formed by a carry in $\{-1,0\}$ per block.",
       r"Set $B_0=2^{4p}$"),
  leaf("S3.2.1b", r"Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<B_0/2$, so the centered residue modulo $B_0$ identifies each coefficient and the extraction carry stays in $\{0,1\}$.",
       r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
  leaf("S3.2.1c", r"Four exact integer products dominate the linear packing, extraction, negacyclic wrapping and truncation passes.",
       r"Four exact integer products dominate the linear"),
 ],
 page="signed-kronecker-packing",
 frm=["nlogn-subroutine","negacyclic-ring","polynomials","convolution-as-polynomial-multiplication","logarithms-floors-ceilings-and-powers-of-two"])

s32 = show(
 "S3.2",
 r"The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathbb C[y]/(y^r+1)$ is approximated with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
 "Run two forward synthetic transforms, keep their outputs in the retained layout order, multiply the $M$ pairs of polynomial records pointwise by signed packing, and apply the opposite transform to that same order",
 ("The same record permutation applied to both operands commutes with pointwise multiplication, so the forward outputs can be multiplied in their retained order.", E, r"forward outputs in their retained order and pass that order directly"),
 [s321,
  leaf("S3.2.2", r"Perform both forward transforms and retain their common layout order, multiply pointwise with the packing lemma, apply the opposite procedure to that order and multiply exactly by $M=T/r$.",
       r"Perform both forward transforms and retain their common $LB$ order."),
  leaf("S3.2.3", r"The normalization identity $MF^+_{\boldsymbol t}\bigl(((F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g))/r\bigr)=(f*g)/(rM)$ identifies the result with $\mathcal M_r(f,g)$.",
       r"To check normalization, expansion of the finite sums gives"),
  leaf("S3.2.4", r"The three transform errors and the product truncation total less than $3\delta+\eta$ with $\delta=\sqrt2\ell2^{-p}$, and the final exact multiplication by $M$ gives error below $\sqrt2\,M(3\ell+1)2^{-p}$.",
       r"The final exact multiplication by $M$ therefore gives error less than"),
  leaf("S3.2.5", r"The $M=T/r$ pointwise products cost $O(Tp\log(rp))$ in total, in addition to the three transforms.",
       r"There are $M=T/r$ pointwise polynomial products."),
 ],
 page="ring-convolution",
 frm=["signed-kronecker-packing","transform-layout","synthetic-transform","dft-cyclic-convolution","multidim-transform","fixed-point-disk-grid","convolution-as-polynomial-multiplication"],
 adds=[bind("M","record count","number $T/r$ of polynomial records in the array over the ring, equal to the product of the first $d-1$ axis lengths","count")])

transforms = show(
 "S3",
 r"Convolution over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes can be computed with synthetic transforms in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time.",
 "Evaluate the transforms by radix-2 butterfly rounds whose twiddles are signed coefficient shifts, lay out the data so that each round is one simultaneous layer, and multiply pointwise in the retained frequency order",
 ("In the polynomial ring the roots of unity are powers of $y$, so a twiddle multiplication is only a signed shift, leaving address movement and two-point butterflies as the real cost.", E, r"are exact signed permutations"),
 [s31, s32],
 frm=["negacyclic-ring"])

# ---------------------------------------------------------------- S4 resampling
s41 = show(
 "S4.1",
 r"The tensor form $R F_{\boldsymbol s}=2^{\gamma}\mathcal B_0\,Q\,F_{\boldsymbol t}\,\mathcal A$ expresses a source transform of prime lengths $s_i$ through a power-of-two transform, with the permutations $R$ and $Q$ kept inside the identity and implementable at cost $O(dTp^{3/2+\delta}\alpha)$.",
 "Prove the one-dimensional Gaussian-resampling identity with contractions $A$ and $B_0$ built from a Neumann inverse, then tensor it over the axes of a padded box, charging the movement of axes with the fast interchange",
 ("Gaussian resampling connects the coprime lengths to the power-of-two synthetic transforms, and keeping the permutations in the identity avoids two sorts per coordinate.", R, None),
 [
  leaf("S4.1.1", r"The Gaussian identity gives $\mathsf T P_sF_s=P_tF_t\mathsf S$ for two explicit Gaussian-weighted interpolation maps.",
       r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
  leaf("S4.1.2", r"Because $\|N-I\|<1/2$ for the nearest-sample correction $N=C\mathsf T\mathsf D$, the operator $N$ is invertible by the Neumann series.",
       r"by the Neumann series."),
  leaf("S4.1.3", r"Setting $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ gives contractions with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.",
       r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$."),
  leaf("S4.1.4", r"The cited ordered numerical maps give fixed multitape approximations of $A$ and $B_0$ with error below $p^2$ and time $O(tp^{3/2+\delta}\alpha)$.",
       r"Contraction of the exact maps yields errors less than $16p<p^2$ and"),
  leaf("S4.1.5", r"Tensoring the one-dimensional identity over the $d$ axes gives $R F_{\boldsymbol s}=2^{\gamma}\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.",
       r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
  leaf("S4.1.6", r"At most $T/t_i$ lines are processed for axis $i$, so the line algorithms cost $O(dTp^{3/2+\delta}\alpha)$ in total.",
       r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
  leaf("S4.1.7", r"Exposing and restoring one axis needs $O(d)$ adjacent interchanges, so all axes cost $O(Tp\,d^2(1+\ell^\tau))$ by the fast chunk interchange.",
       r"costs $O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs"),
 ],
 page="resampling-no-sort",
 frm=["gaussian-resampling","multidim-transform","dft-cyclic-convolution","fixed-point-disk-grid","chunk-swap","gaussian-function","norms-and-the-triangle-inequality"])

s42 = show(
 "S4.2",
 r"The chirp identity $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$ evaluates the target permutation without executing it, and the source permutation cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.",
 "Verify the chirp formula coefficient by coefficient (Bluestein), then use that a coordinate permutation commutes with pointwise products and with the opposite transform to cancel $R$",
 ("The chirp identity performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.", E, r"in $Q$ without applying $Q$ as a separate permutation of the array."),
 [
  leaf("S4.2.1", r"The coefficient of $u_{\boldsymbol k}$ in the chirp expression is $\frac1T\exp\bigl(2\pi i\sum_i s_ij_ik_i/t_i\bigr)$, which is exactly the coefficient of $QF_{\boldsymbol t}$.",
       r"The coefficient of $u_{\boldsymbol k}$ in the right side of"),
  leaf("S4.2.2", r"For units $c$ modulo $q$ one has $F_q^+R_c=R_c^{-1}F_q^+$, so $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
       r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
  leaf("S4.2.3", r"The convolution rule and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$ give $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$.",
       r"=\frac1S F_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)"),
 ],
 page="chirp-permutation-cancel",
 frm=["bluestein-chirp","dft-cyclic-convolution","multidim-transform","resampling-no-sort","permutations-and-permutation-matrices"],
 salient=r"The source permutation $R$ disappears entirely from the final convolution, so it never has to be executed: it cancels across the two forward transforms, the pointwise product and the opposite transform because permutations commute with pointwise products and $RF^+_{\boldsymbol s}R=F^+_{\boldsymbol s}$.")

resamp = show(
 "S4",
 r"Gaussian resampling together with a chirp identity lets power-of-two synthetic transforms compute convolutions of pairwise coprime prime lengths $s_i$ without executing the source or target coordinate permutations.",
 "Keep the source and target permutations inside the transform identity: tensor the resampling identity, evaluate the middle transform with the chirp, and cancel the source permutation across the three transforms",
 ("The usual implementation of Gaussian resampling sorts twice on each coordinate; retaining both permutations in the formula avoids those full sorts.", E, r"coordinate. We retain both permutations in the transform formula and"),
 [s41, s42],
 frm=["gaussian-resampling"])

# ---------------------------------------------------------------- S5 assembly
pc = show(
 "S5.1",
 r"The choices $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^{\epsilon}\rfloor$, a power of two $T\in[4n/b,8n/b)$, axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$, and distinct odd primes $s_i$ just below $t_i$ give $Tp=\Theta(n)$, $T/2<S<T$ and every hypothesis of the interfaces.",
 "Fix rational exponents with large slack, derive the sizes from $n$, find the prime lengths in disjoint intervals just below $t_i$ using a prime-counting bound, and check the resampling hypotheses",
 ("The prime lengths must be close to the powers of two so that their product fills a fixed fraction of the padded box and the ratios leave room for resampling.", E, r"$t_i$: their product must occupy a fixed fraction of the padded box,"),
 [
  leaf("S5.1.1", r"Fixed rational exponents are chosen, including $\epsilon=2^{-75}$, $c=2^{-56}$, $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$ and $\kappa=2^{-182}$.",
       r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
  leaf("S5.1.2", r"Put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$.",
       r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
  leaf("S5.1.3", r"These definitions give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.",
       r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
  leaf("S5.1.4", r"Each interval $((1-2\eta)t_i,(1-\eta)t_i]$ with $\eta=1/(4d)$ contains more than $d$ primes, so distinct odd primes $s_i$ in these intervals exist.",
       r"We may therefore choose distinct odd primes satisfying"),
  leaf("S5.1.5", r"Multiplying the lower bounds on $s_i$ gives $S/T>(1-1/(2d))^d>1/2$, so $T/2<S<T$.",
       r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
  leaf("S5.1.6", r"Since $\theta_i>\eta$, $\alpha^4\theta_i>p$ and $2\le\alpha<\sqrt p$ with $\gamma=2d\alpha^2=o(b)$, every hypothesis of the resampling lemma holds.",
       r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
  leaf("S5.1.7", r"The product of the two digit polynomials has degree below $S$, so convolution modulo $x^S-1$ has no nonzero wraparound.",
       r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
  leaf("S5.1.8", r"Every product coefficient satisfies $0\le c_j\le q(2^b-1)^2<2^{3b}$.",
       r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
 ],
 page="parameter-choice",
 frm=["resampling-no-sort","transform-layout","simultaneous-butterfly-layer","primes-divisibility-gcd-and-coprimality","logarithms-floors-ceilings-and-powers-of-two","radix-digit-convolution"],
 adds=[bind("\\eta","prime gap fraction","relative width $1/(4d)$ of the intervals below $t_i$ in which the primes $s_i$ are chosen","direct")])

crt = show(
 "S5.2",
 r"The map $x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ to the product of cyclic axes of lengths $s_i$, sending one cyclic convolution of length $S$ to a convolution on $d$ axes, and costs $O(Tp\,d^2(1+\ell^\tau))$ with padding.",
 "Chinese remainder theorem: use the mixed-radix coordinates so that each new coordinate depends only on lower-index digits, and update the axes in descending order by controlled cyclic shifts",
 ("The coordinate powers are chosen so that the change of order becomes a sequence of controlled cyclic shifts.", E, r"algebraic split, with coordinate powers that make the change of order a"),
 [
  leaf("S5.2.1", r"The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$, so it defines an algebra map, and it is an isomorphism because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime.",
       r"respects $x^S=1$, so it defines an algebra map."),
  leaf("S5.2.2", r"The coordinate of $\Phi(x^k)$ on axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$ in the mixed-radix digits $a_j$ of $k$.",
       r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
  leaf("S5.2.3", r"Updating the axes in the order $i=d,d-1,\ldots,1$ means that each target is computed from still-unchanged lower-index controls, a prefix-controlled cyclic shift on the valid interval.",
       r"order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}."),
  leaf("S5.2.4", r"With the fast axis reversals, the map, its inverse and the padding operations cost $O(Tp\,d^2(1+\ell^\tau))$.",
       r"O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."),
 ],
 page="crt-axis-map",
 frm=["controlled-shifts","chunk-swap","stream-arrays","primes-divisibility-gcd-and-coprimality","algebraic-structures-groups-rings-and-isomorphisms","modular-arithmetic-and-residues"],
 adds=[bind("S","convolution length","product $s_1\\cdots s_d$ of the pairwise coprime prime axis lengths","count"),
       bind("s_i","prime axis length","the odd prime length of the $i$th cyclic axis, just below $t_i$","count"),
       bind("t_i","power-of-two axis length","the length, $r/2$ or $r$, of the $i$th power-of-two axis","count"),
       bind("\\alpha","Gaussian width parameter","integer $\\lceil(12d^2b)^{1/4}\\rceil$ controlling the Gaussian window of the resampling maps","direct"),
       bind("\\gamma","resampling scale exponent","$2d\\alpha^2$, the exponent of the exact power-of-two scale in the resampling identity","direct"),
       bind("b","digit width","$\\lceil\\log_2n\\rceil$, the number of bits in each radix digit","count")])

twist = show(
 "S5.3",
 r"Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ is a ring isomorphism from $\mathbb C[x]/(x^r-1)$ to $\mathbb C[y]/(y^r+1)$, so complex cyclic convolution on the last axis is computed by the ring convolution.",
 "Check the twist is well defined and diagonal on bases, verify that the negative wrap becomes the cyclic wrap after the twist, and place it around the ring convolution",
 ("The power-of-two complex convolution needed by the chirp identity is obtained from the synthetic convolution by a coefficient twist.", E, r"obtained from the synthetic convolution by a coefficient twist."),
 [
  leaf("S5.3.1", r"The map $x_d\mapsto\zeta y$ is well defined since $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal on the monomial bases, hence an isomorphism.",
       r"is well defined, since $(\zeta y)^r=(-1)(-1)=1$."),
  leaf("S5.3.2", r"For $k+l=j+hr$ with $h\in\{0,1\}$ the twisted product term has factor $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the right sign.",
       r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j."),
  leaf("S5.3.3", r"Hence $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$, a bilinear contraction.",
       r"Consequently, with $\mathcal M_r$ from"),
 ],
 page="coefficient-twist",
 frm=["negacyclic-ring","fixed-point-disk-grid","dft-cyclic-convolution","complex-numbers","euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle"],
 salient=r"The sign $(-1)^h$ introduced by the negative wrap is exactly cancelled by $\zeta^{rh}=(-1)^h$, so the same factor $\zeta^j$ appears whether or not the index wraps around.")

src = show(
 "S5.4",
 r"The computed source transform $\widetilde{\mathscr F}$ (Gaussian maps $\mathcal A$, chirp transform by twisted ring convolution, then $\mathcal B_0$ and an exact power-of-two scale) has exact counterpart $RF_{\boldsymbol s}$, and its opposite-sign version has counterpart $RF^+_{\boldsymbol s}$.",
 "Evaluate the middle factor $QF_{\\boldsymbol t}$ with the chirp identity and the twisted complex convolution, then compose it with the two Gaussian maps and the scale $2^\\gamma$, and obtain the opposite sign by conjugation",
 ("The tensor identity needs the middle transform $QF_{\\boldsymbol t}$, which the chirp identity turns into one cyclic convolution and two pointwise phase products.", R, None),
 [
  leaf("S5.4.1", r"Chirp phases cost $O(dp^{1+\delta})$ per entry, so chirp construction costs $O(Tdp^{1+\delta})$ in total.",
       r"Thus chirp construction costs $O(Td p^{1+\delta})$ in total."),
  leaf("S5.4.2", r"The computed chirp transform multiplies by $\overline{\widetilde a}$, convolves with the kernel $\widetilde a$ by the twisted ring convolution, and multiplies by $\overline{\widetilde a}$ again.",
       r"Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data"),
  leaf("S5.4.3", r"The source transform applies the linewise approximation of $\mathcal A$, then the chirp transform, then the approximation of $\mathcal B_0$, then multiplies the numerators by $2^\gamma$.",
       r"$\widetilde{\mathscr F}$ for the following procedure: apply the linewise"),
  leaf("S5.4.4", r"Its exact counterpart is $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
       r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A"),
  leaf("S5.4.5", r"Conjugating the input and output gives the opposite-sign procedure, with exact counterpart $RF^+_{\boldsymbol s}$.",
       r"its exact counterpart is $RF_{\boldsymbol s}^{+}$ by"),
 ],
 page="source-transform",
 frm=["gaussian-resampling","resampling-no-sort","chirp-permutation-cancel","bluestein-chirp","coefficient-twist","ring-convolution","fixed-point-disk-grid"])

alg = show(
 "S5.5",
 r"The algorithm splits the operands into radix-$2^b$ digits, maps by $\Phi$ to the prime axes, takes two source transforms, multiplies pointwise, applies the opposite-sign transform with the two scalings by $S$, rounds, undoes $\Phi$ and propagates carries to output the $2n$-bit product.",
 "Compose the stages in order: digit conversion, axis map, two forward source transforms, pointwise product, opposite transform with exact scalings, rounding, inverse axis map, carries",
 ("The source-transform procedures supply the three transforms needed for the radix-digit convolution.", E, r"The source-transform procedures now supply the three transforms needed"),
 [
  leaf("S5.5.0", r"Read each operand backward in groups of $b$ bits to obtain the radix-$2^b$ digits, written as exact grid values of norm below $1/4$.",
       r"its least significant end in groups of $b$ bits."),
  leaf("S5.5.1", r"Apply the coefficient-address map $\Phi$ with its padded layout to obtain the source arrays $u,v$.",
       r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
  leaf("S5.5.2", r"Compute the source transforms $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.",
       r"Compute $\widetilde{\mathscr F}(u)$ and"),
  leaf("S5.5.3", r"Multiply corresponding coefficients exactly and truncate each part toward zero to $p$ fractional bits, giving the array $z$.",
       r"Multiply corresponding complex coefficients exactly and truncate"),
  leaf("S5.5.4", r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$.",
       r"Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
  leaf("S5.5.5", r"Multiply the numerators exactly by $2^{2b+4}S$, round the real parts to integers, and apply $\Phi^{-1}$ with removal of padding.",
       r"Multiply the grid numerators of $\widetilde w$ exactly by"),
  leaf("S5.5.6", r"Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.",
       r"Propagate radix-$2^b$ carries in increasing coefficient order."),
  leaf("S5.5.7", r"The two scalings by $S$ undo different normalizations: after the three transforms the exact result is $(u*v)/S^2$, the first scale gives $(u*v)/S$, and the second gives $2^{2b+4}(u*v)$.",
       r"The two occurrences of $S$ in this algorithm undo different"),
 ],
 page="multiplication-algorithm",
 frm=["crt-axis-map","source-transform","radix-digit-convolution","parameter-choice","chirp-permutation-cancel","coefficient-twist"],
 salient=r"The scale $S$ is applied twice, for two different reasons: one factor $1/S$ comes from $F^+F=I/S$ and the other from the convolution rule $F(u*v)=S\,Fu\cdot Fv$, so one multiplication by $S$ is needed per normalization.")

rec = show(
 "S5.6",
 r"The recovered coefficient error is below $1/2$, so rounding gives the exact integer convolution coefficients, and radix-$2^b$ carry propagation yields the exact $2n$-bit product.",
 "Propagate sup-norm errors through each contraction and bilinear product, stay inside the disk with explicit margins, then compare the error scaled back by $2^{2b+4}S$ with $1/2$",
 ("Rounding is only correct when the accumulated error is below one half, so every approximation step must be bounded in the sup norm.", R, None),
 [
  leaf("S5.6.1", r"For bilinear contractions with disk operands, the errors of the two operands add.",
       r"When all four operands are in the disk, their two errors therefore add."),
  leaf("S5.6.2", r"The normalized ring convolution has error below $5T\log_2T$ units of $2^{-p}$.",
       r"E_{\rm ring}:=M(3L+2)<5TL."),
  leaf("S5.6.3", r"The computed complex convolution has error below $6T\log_2T$ units.",
       r"<(E_{\rm ring}+4+4+4)h_p<6TLh_p."),
  leaf("S5.6.4", r"The chirp transform has error below $8T\log_2T$ units.",
       r"<(6TL+2+4+4)h_p<8TLh_p."),
  leaf("S5.6.5", r"The source transform, with its scale $2^\gamma$, has error below $E_s=9\cdot2^\gamma T\log_2T$ units.",
       r"E_s=9\,2^\gamma TL,"),
  leaf("S5.6.6", r"After the opposite transform and the first scale by $S$ the error is below $E_w=S(3E_s+2)<28\cdot2^\gamma T^2\log_2T$ units.",
       r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
  leaf("S5.6.7", r"Scaling back by $2^{2b+4}S$ and using $p=6b$ the final error is below $448b\,2^{-3b/4}<1/2$.",
       r"\le448b\,2^{-3b/4}<\frac12."),
  leaf("S5.6.8", r"Since the true coefficients are integers and the error is below $1/2$, the nearest integer to each represented value is the correct coefficient.",
       r"The strict error below $1/2$ makes the nearest integer to"),
  leaf("S5.6.9", r"The carries $k_{j+1}=\lfloor(c_j+k_j)/2^b\rfloor$ with digits $d_j=(c_j+k_j)\bmod2^b$ stay below $2^{2b}$ and give the first $j$ radix digits of the product.",
       r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad"),
  leaf("S5.6.10", r"The product is below $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.",
       r"than $2^{2n}$; all bits above position $2n-1$ are therefore zero."),
 ],
 page="exact-recovery",
 frm=["fixed-point-disk-grid","norms-and-the-triangle-inequality","source-transform","chirp-permutation-cancel","ring-convolution","parameter-choice","coefficient-twist","rational-numbers-dyadic-rationals-and-exact-arithmetic"],
 salient=r"Precision $p=6b$ leaves a final error of only $448b\,2^{-3b/4}$, exponentially small below $1/2$, even after the resampling scale $2^\gamma$ with $\gamma=o(b)$ and the growth $2^{2b+4}ST^2$ are charged against it.")

cost = show(
 "S5.7",
 r"Each of the seven dominant normalized costs is at most $p^{1-2\kappa}$, so the total time is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
 "Tabulate the cost of each operation divided by $Tp$, express each as a power of $p$ in terms of the fixed exponents, and check that the smallest margin below one is $2\\kappa$",
 ("A fixed power of $\\log p$ must be absorbed by an explicit slack below the exponent one, which a table of margins provides.", E, r"This explicit slack will cover"),
 [
  leaf("S5.7.1", r"With $V=Tp=\Theta(n)$ every padded array has $\Theta(V)$ stored bits, and costs are listed divided by $V$.",
       r"For the cost calculation put $V=Tp=\Theta(n)$."),
  leaf("S5.7.2", r"The seven margins below one are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$.",
       r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
  leaf("S5.7.3", r"Hence $\min_ig_i=2^{-181}=2\kappa$.",
       r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
  leaf("S5.7.4", r"The layout exchanges cost $O(p/K)\,K^\tau=O(pK^{\tau-1})$ per unit volume, with power $1-\epsilon c(1-\tau)$ of $p$.",
       r"O(p/K)\,K^\tau=O(pK^{\tau-1})."),
  leaf("S5.7.5", r"The at most $\ell$ simultaneous rounds cost $O(Vd^{\lambda'})$ each.",
       r"Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$"),
  leaf("S5.7.6", r"The Gaussian line maps cost $dp^{1/2+\delta}\alpha$ per unit volume, with $\alpha=\Theta(p^{1/4+\epsilon/2})$.",
       r"$\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$."),
  leaf("S5.7.7", r"The packed polynomial products use the established multiplier on records of length $O(rp)=o(n)$ and do not call the improved algorithm.",
       r"$O(rp)=o(n)$; they do not call the improved algorithm being constructed."),
  leaf("S5.7.8", r"The compact sorting of exceptional addresses costs $o(V)$ in total.",
       r"O(Vp^{A'}2^{-K})=o(V)"),
  leaf("S5.7.9", r"Each of the seven displayed powers is at most $1-2\kappa$.",
       r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
  leaf("S5.7.10", r"Any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
       r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."),
  leaf("S5.7.11", r"Below a fixed cutoff use schoolbook multiplication, absorbing the finitely many smaller lengths into the constant, giving one fixed machine for all $n$.",
       r"Fix one cutoff beyond all the size, precision, margin and layout"),
 ],
 page="cost-accounting",
 frm=["parameter-choice","transform-layout","simultaneous-butterfly-layer","chunk-swap","resampling-no-sort","signed-kronecker-packing","nlogn-subroutine","stream-arrays"],
 salient=r"The saving exponent $\kappa=2^{-182}$ is half the smallest of seven margins, $2^{-181}=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}$, which comes from the layout-exchange row and is the product of the three tiny exponents $\epsilon$, $c$ and $1-\tau$.")

assembly = show(
 "S5",
 r"With sizes chosen and transforms assembled, the algorithm outputs the exact $2n$-bit product in $O(n(\lg n)^{1-\kappa})$ time.",
 "Choose compatible parameters for all procedures, define the algorithm, prove that the error is below one half so the recovered integers are exact, and sum the cost table",
 ("The remaining work is to choose compatible parameters, recover the integer coefficients from their approximations, and account for the remaining tape operations.", E, r"the integer coefficients from their approximations, and account for the"),
 [pc, crt, twist, src, alg, rec, cost])

root = show(
 "S0",
 r"A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.",
 "Reduce the product to a convolution of radix digits, evaluate that convolution by transforms whose address movement and butterfly layers are accelerated by two rank-saving tape procedures, then fix parameters, show exact recovery and add up the costs",
 ("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $n\\log n$, so both movement and arithmetic of the transforms must be sped up.", E, r"We therefore need savings in both movement and arithmetic."),
 [
  leaf("S1", r"Writing each operand as a polynomial in a power of two $2^b$ reduces multiplication to a convolution of short integer digit lists, followed by carry propagation.",
       r"Splitting the inputs into radix digits reduces multiplication to",
       frm=["convolution-as-polynomial-multiplication","binary-representation-of-integers","polynomials"], page="radix-digit-convolution"),
  tools, transforms, resamp, assembly,
 ],
 page="main-theorem",
 frm=["n-log-n-conjecture","fixed-tape-model","nlogn-subroutine","multitape-machine-cost-model-and-linear-time-scans","big-o"],
 adds=[bind("n","operand length","number of bits of each of the two integers being multiplied","count"),
       bind("p","precision","number of fractional bits kept in each fixed-point real or imaginary part","count"),
       bind("d","axis count","number of power-of-two axes, equal to the number of address chunks in a layer","count"),
       bind("r","record length","number of complex coefficients in a polynomial record modulo $y^r+1$, a power of two","count"),
       bind("K","chunk width","number of address bits in each chunk of a simultaneous layer","count"),
       bind("T","padded size","number of entries of the padded power-of-two box, the product of the axis lengths","count"),
       bind("\\ell","log record length","the base-two logarithm of $r$","direct")])

out = {"root": root}
json.dump(out, open(ROOT + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)

# ------------------------------------------------- checks
pos = 0; bad = 0
def walk(n):
    global pos, bad
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        i = SRC.find(q, pos)
        if i < 0:
            j = SRC.find(q)
            print("QUOTE", "OUT OF ORDER" if j >= 0 else "MISSING", n["id"], q[:60], "first at line", (SRC[:j].count("\n")+1) if j>=0 else None)
            bad += 1
        else:
            if SRC.count(q) > 1: print("note multi-occurrence", n["id"], SRC.count(q))
            pos = i + len(q)
    else:
        if n["motivation"]["quote"] and SRC.find(n["motivation"]["quote"]["quote"]) < 0:
            print("MOTIV QUOTE MISSING", n["id"]); bad += 1
        for c in n["children"]: walk(c)
walk(root)
print("bad:", bad)
