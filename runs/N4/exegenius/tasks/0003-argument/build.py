import json, sys
D='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N4/'
src=open(D+'sources/paper.tex').read()
def Q(s):
    assert s in src, s
    return {"source":"paper","quote":s}
def B(sym,name,meaning,rel="direct"):
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}
def show(id,claim,method,mot,children,page=None,frm=(),adds=None,salient=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":mot,"children":children,"page":page,"from":list(frm)}
    if adds: n["adds"]=adds
    if salient: n["salient"]=salient
    return n
def infer(id,claim,quote,page=None,frm=(),deferred=False,salient=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":Q(quote),"page":page,"from":list(frm)}
    if deferred: n["deferred"]=True
    if salient: n["salient"]=salient
    return n
def M(text,src_,quote=None):
    m={"text":text,"source":src_}
    if quote: m["quote"]=Q(quote)
    return m

S0=infer("S0","Splitting each $n$-bit input into radix-$2^b$ digits reduces the product to a convolution of short integer coefficient sequences followed by carry propagation.",
 "Splitting the inputs into radix digits reduces multiplication to",
 page="radix-digit-convolution",frm=["cyclic-convolution","polynomial-multiplication-as-convolution","positional-radix-representation","binary-addition-with-carries"])

S11=show("S1.1","The three-stage scalar network sends $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ and restores every scratch wire, whatever its initial value.",
 "build a forward invocation $y\\gets y+x$ from copy, gather, scatter and side-injection gates with a restoring schedule, then compose three invocations like an XOR swap",
 M("Three additions $y\\gets y+x$, $x\\gets x-y$, $y\\gets y+x$ realize a signed exchange, so it suffices to make one addition step out of cheap gates that restore their scratch wires.","recoverable"),
 [
  infer("S1.1.1","A forward invocation's schedule first subtracts the effect of the old scratch values, then adds the source effect and finally restores the scratch values, so its net effect is independent of the initial scratch contents.",
   "the next four introduce the source values and add their effect to the",
   page="scratch-restoration",frm=["linear-network","linear-combinations-and-linear-maps"]),
  infer("S1.1.2","Gathering through central wires gives coefficients depending on $|S\\cap T|$, and the side wires cancel the unwanted ones, so each forward invocation computes $y\\gets y+x$.",
   "Thus both net maps are $y\\gets y+x$.",
   page="triple-intersection-construction",frm=["linear-network","scratch-restoration","binomial-coefficients","sets-cartesian-products-and-indicator-vectors","the-two-element-field"]),
  infer("S1.1.3","Composing a forward, an inverse and a forward invocation over the three stages sends $(x,y)$ to $(-y,x)$.",
   "Starting from $(x,y)$, the three stages give"),
 ],page="linear-network",frm=["linear-combinations-and-linear-maps","matrix-rank"])

S13=show("S1.3","Nested nondegenerate subspaces of the $m$-dimensional label space can be attached to all vertices so that the absolute label-dimension changes over all edges sum to $Wm-2N+2L$ with $L=Ich$.",
 "use triple indicator vectors under a bilinear form in which neighbors are orthogonal, form the tensor cube, and expose one tensor factor per stage",
 M("The cost of an edge is the dimension of its orthogonal residual, so labels that only lose dimension on the central return edges keep the total small.","explicit",
   "The saving will come from keeping the total dimension lost on decreasing\nedges small relative to $N$."),
 [
  infer("S1.3.1","Under the form $x^{\\mathsf T}(I-J/9)y$ over $\\mathbb Q$, or the dot product over $\\mathbb F_2$, every triple line is nondegenerate and neighboring triple lines are orthogonal.",
   "Thus every triple line is nondegenerate, and neighboring triple lines\nare orthogonal, in the label field belonging to either construction.",
   frm=["bilinear-form","sets-cartesian-products-and-indicator-vectors","dot-product-and-orthogonality"]),
  infer("S1.3.2","With the stage-by-stage gate labels, the only decreasing edges are the central-wire returns, each losing dimension $h$.",
   "The only decreasing\nedges are the central-wire edges from time 3 to time 4; their dimension\nloss is $h$.",
   frm=["tensor-product","vector-spaces-and-subspaces"]),
 ],page="subspace-labels",frm=["bilinear-form","tensor-product","frames","triple-intersection-construction","linear-independence-basis-and-dimension"])

S1=show("S1","There are two fixed finite linear networks, a bit network over $\\mathbb F_2$ and a complex network over $\\mathbb Z[i,1/2]$, each exchanging two banks with prescribed signs while restoring scratch values, whose frames cost $s<Wm$ smaller calls in total and whose endpoint operators are the address shear and the $C^{\\otimes m}$ layer.",
 "construct the scalar network, transfer it to arrays with frames, attach nested subspace labels, count residual dimensions, and read off the two interfaces",
 M("When values become arrays split among the $W$ roles, each edge costs smaller calls in proportion to its rank, so a total $s$ strictly below $Wm$ is what makes the recursion save a power.","explicit",
   "The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$."),
 [
  S11,
  infer("S1.2","Giving each vertex an invertible frame $D_v$ and each edge $D_vD_u^{-1}$, a pointwise gate commutes with its common frame, so the network on arrays implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$.",
   "Thus the common frame commutes with the pointwise gate, and\nthe invariant continues to the sinks.",
   page="frames",frm=["linear-network","elementary-streams","invertible-matrices","pointwise-operations"]),
  S13,
  infer("S1.4","The loss ratios are $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$, both below $1/2$.",
   "In particular, both are smaller than $1/2$."),
  infer("S1.5","With projection matrices as frames and $-P_{U_a}$ at the $X_a$ sources, the bit network has endpoint difference $I_m$ on every role and total edge rank $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
   "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
   page="rational-matrix-interface",frm=["subspace-labels","address-shear","rank-saving","matrix-rank"]),
  infer("S1.6","With phase frames $\\mathcal C_U$, every edge of the complex network is a product of one two-point kernel per residual basis vector, totalling $s_{\\rm c}<W_{\\rm c}m$, and the endpoints telescope to $C^{\\otimes m}$ on every role.",
   "bank exchange, telescoping these phase frames gives $C^{\\otimes m}$",
   page="binary-phase-interface",frm=["subspace-labels","butterfly-h0","gaussian-dyadics","rank-saving","tensor-product"]),
  infer("S1.7","Both networks satisfy $s/W<m^{\\tau}$ with the fixed rational exponent $\\tau=1-2^{-50}$, so the recurrence $F_k\\le(s/W)F_{k-1}+O(1)$ gives a power saving.",
   "For both recurrences we may use the fixed rational exponent",
   page="recursive-power-saving",frm=["rank-saving","frames","recurrence-relations","geometric-series","logarithms"],
   salient="The relative deficits are tiny (about $10^{-11}$), yet any strict deficit gives an exponent below one."),
 ],page="rank-saving",frm=["linear-network","frames","matrix-rank","subspace-labels"],
 adds=[B("W","wire count","The number of wires (roles) of the network, including scratch wires.","count"),
       B("m","label dimension","The dimension $h^3=10^6$ of the tensor label space attached to the network.","count"),
       B("N","data role count","The number $v^3$ of positions $a$ in each data bank.","count"),
       B("L","dimension loss","The total dimension lost on the decreasing edges of the network.","count")],
 salient="The saving $s<Wm$ is strict for both networks even though $W$ and $m$ are astronomically large fixed numbers.")

S2=show("S2","Exchanging two disjoint $u$-bit address fields of an array of logical volume $V$ costs $O(Vu^{\\tau})$ with $\\tau<1$.",
 "turn each bit-network edge shear into rank-many smaller interchanges by a lower triangular factorization, run the network recursively on role streams to get the shear $H\\gets H+D$, complete the interchange by two linear updates, and remove width and row restrictions",
 M("An edge of rank $a$ costs $a$ smaller interchanges on volume $V/W$, so the strict rank saving turns into a recurrence that saves a power of the width.","explicit",
   "Because the sum of these ranks is less than the number of wires times\n$m$, the resulting recurrence saves a power of the chunk width."),
 [
  infer("S2.1","Every rational matrix of rank $a$ factors as $E_1\\Pi E_2$ with invertible lower triangular $E_1,E_2$ and a partial permutation $\\Pi$ with $a$ ones.",
   "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
   page="lower-triangular-factorization",frm=["matrix-rank","triangular-and-diagonal-matrices","permutation-matrices","invertible-matrices"]),
  infer("S2.2","A shear $(H,D)\\mapsto(H+AD,D)$ with $A$ of rank $a$ takes exactly $a$ field interchanges plus $O(V)$ work, since lower triangular updates run in tape order.",
   "can be performed with exactly $a$ interchanges of pairs of $b$-digit\nfields and $O(V)$ further work.",
   frm=["lower-triangular-factorization","controlled-shifts"]),
  infer("S2.3","Running the bit network with shears as frames on $W$ row-split role streams makes $s$ recursive calls on volume $V/W$, giving $F_k\\le(s/W)F_{k-1}+O(1)$ and $F_k=O(e^{\\tau})$ for widths $e=m^k$.",
   "Hence $F_k=O(e^\\tau)$.",
   frm=["rational-matrix-interface","recursive-power-saving","address-shear","frames"]),
  infer("S2.4","Using high digits as rows and handling general widths, the interchange of two $u$-bit chunks costs $O(Vu^{\\tau})$ for every shape.",
   "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.",
   frm=["elementary-streams"]),
 ],page="chunk-interchange",frm=["rational-matrix-interface","lower-triangular-factorization","controlled-shifts","recursive-power-saving","elementary-streams","address-shear"],
 adds=[B("u","field width","The number of bits in each of the two exchanged address fields.","count"),
       B("V","logical volume","The number of stored bits of the array being processed.","count"),
       B("\\tau","interchange exponent","The fixed exponent $1-2^{-50}$ below one in the interchange cost.")],
 salient="The final effect is an exact permutation, yet it is computed through XOR combinations of data.")

S3=show("S3","Applying $H_0$ at the same bit position of $D\\le d$ address chunks of polynomial records costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, with error below $\\sqrt2\\,2^{-p}$.",
 "write $H_0^{\\otimes D}$ as phase wrappers around $C^{\\otimes D}$, run the complex network recursively with binary basis changes done by packed selected-bit additions, bound the dyadic growth, and truncate once",
 M("The complex network's endpoint is $C^{\\otimes m}$ and its edges are products of two-point kernels on fewer selected bits, so the rank saving applies once $C$ is converted to $H_0$ by exact phases.","recoverable"),
 [
  infer("S3.1","Exact Gaussian dyadic phases convert the $C$ layer into the normalized butterfly layer: $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
   "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
   frm=["butterfly-h0","gaussian-dyadics","binary-phase-interface"]),
  infer("S3.2","Binary row additions of selected bits across chunks are done by a constant number of whole-chunk cyclic shifts and moves followed by deterministic repair of a bounded exceptional set.",
   "The construction first uses a constant number\nof cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of\naddresses.",
   page="packed-selected-bit-addition",frm=["chunk-interchange","controlled-shifts","elementary-streams"]),
  infer("S3.3","The $s$ child calls on volume $V/W$ give $F(e)\\le(s/W)F(e/m)+O((eK)^{\\tau}+1)$, which unrolls to $O(d^{\\lambda'})$.",
   "Dividing by\nthe current volume \\(V\\) gives the factor \\(s/W\\).",
   frm=["recursive-power-saving","binary-phase-interface"]),
  infer("S3.4","Explicit guard widths bound denominator and magnitude growth of the exact intermediate values within one layer.",
   "We now give explicit constants that bound\ndenominator and magnitude growth within one layer.",
   frm=["gaussian-dyadics","fixed-point-approximation"]),
  infer("S3.5","The procedure returns the truncated layer $Q_p(\\mathcal Hz)$ in $O(Vd^{\\lambda'})$ time.",
   "coefficient order, and component format in $O(Vd^{\\lambda'})$ time,",
   frm=["fixed-point-approximation"]),
 ],page="simultaneous-butterfly-layer",frm=["binary-phase-interface","packed-selected-bit-addition","recursive-power-saving","chunk-interchange","fixed-point-approximation","butterfly-h0","gaussian-dyadics"],
 adds=[B("d","axis bound","The maximum number of address chunks whose selected bits are processed together.","count"),
       B("\\lambda'","layer exponent","The fixed exponent $1-2^{-54}$ below one in the layer cost.")],
 salient="All $D$ butterfly factors together cost less than $D$ separate passes, by a power $d^{\\lambda'}$ with $\\lambda'<1$.")

S4=show("S4","Normalized cyclic convolution $\\mathcal M_r$ of arrays over $\\mathbb C[y]/(y^r+1)$ on power-of-two axes is approximated with error below $\\sqrt2M(3\\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ plus packed products.",
 "compute two forward synthetic transforms on a layout built by chunk interchanges with simultaneous layers, multiply pointwise by signed packing, and apply the opposite transform in the stored frequency order",
 M("In the ring, the needed roots of unity are powers of $y$, so the transforms reduce to signed shifts, butterflies and address moves, exactly what the two tape procedures accelerate.","explicit",
   "Powers of $y$ then\nserve as roots of unity in the remaining axes, and multiplication by\nsuch a root is a signed shift of the coefficient list."),
 [
  infer("S4.1","Synthetic transforms over $\\mathcal R_r$ use powers of $y$ as roots of unity, which act by exact signed permutations of coefficient lists.",
   "Their entries will be short polynomials in a quotient\nwhere the required roots of unity act by exact signed permutations\nof coefficient lists.",
   page="synthetic-transform",frm=["negacyclic-ring","discrete-fourier-transform","butterfly-h0"]),
  infer("S4.2","On the layout placing selected bits at a common offset, each transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ and the opposite transform consumes the stored frequency order.",
   "The forward procedure may retain its output layout for a\npointwise product and the following opposite procedure.",
   frm=["simultaneous-butterfly-layer","chunk-interchange","synthetic-transform"]),
  infer("S4.3","Signed Kronecker packing computes each normalized ring product $Q_p(fg/r)$ in $O(rp\\log(rp))$ time with one call to the $O(N\\log N)$ multiplier.",
   "numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time",
   page="signed-packing",frm=["negacyclic-ring","harvey-van-der-hoeven-multiplier","fixed-point-approximation","polynomial-multiplication-as-convolution"]),
  infer("S4.4","Composing the transforms and pointwise products approximates $\\mathcal M_r$ with error below $\\sqrt2M(3\\ell+1)2^{-p}$.",
   "$\\mathcal M_r$ on disk grid operands has an approximation with error",
   frm=["fixed-point-approximation"]),
 ],page="synthetic-convolution",frm=["synthetic-transform","simultaneous-butterfly-layer","chunk-interchange","signed-packing","negacyclic-ring"],
 adds=[B("r","record length","The power-of-two number of complex coefficients in each polynomial record.","count"),
       B("T","transform size","The product of the power-of-two axis lengths of the array.","count"),
       B("p","working precision","The number of fractional bits of each fixed-point coefficient.","count")])

S5=show("S5","The source Fourier transform on pairwise coprime axes factors through Gaussian contractions and a power-of-two transform whose target permutation is absorbed by a chirp, and whose source permutation cancels in convolution.",
 "apply Gaussian resampling with both coordinate permutations kept in the identity, take tensor products over axes, convert the middle transform by Bluestein's chirp, and let the source permutation cancel",
 M("Sorting twice on each coordinate would cost full passes, so keeping both permutations in the formula avoids them.","explicit",
   "Its usual implementation sorts twice on each\ncoordinate. We retain both permutations in the transform formula and\ncompute that formula directly."),
 [
  infer("S5.1","For coprime $s<t$, $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with linear contractions $A,B_0$ computable to error below $p^2$.",
   "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",
   page="gaussian-resampling",frm=["discrete-fourier-transform","fixed-point-approximation","gaussian-function","greatest-common-divisor-and-coprimality"]),
  infer("S5.2","Tensoring over axes gives the multidimensional interface, with axis movement supplied by chunk interchanges.",
   "The chunk-swap algorithm supplies the movement of the\nphysical axis fields, including its cost when the number of axes grows.",
   frm=["tensor-product","chunk-interchange"]),
  infer("S5.3","The permuted middle transform $QF_{\\boldsymbol t}$ equals a chirp multiplication, a cyclic convolution with the chirp, and another chirp multiplication.",
   "The chirp identity below performs the frequency change\nin $Q$ without applying $Q$ as a separate permutation of the array.",
   page="bluestein-chirp",frm=["discrete-fourier-transform","cyclic-convolution"]),
  infer("S5.4","The retained source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite transform, giving $(u*v)/S^2$.",
   "The second identity shows how the\nretained source permutation $R$ cancels when computing a convolution.",
   frm=["cyclic-convolution","permutations-and-bijections"]),
 ],page="retained-permutations",frm=["gaussian-resampling","bluestein-chirp","cyclic-convolution","chunk-interchange"])

S6=infer("S6","The map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is an algebra isomorphism turning cyclic convolution of length $S=\\prod_is_i$ into convolution on pairwise coprime axes, implemented by triangular controlled shifts.",
 "Hence\n$\\Phi$ is an isomorphism and preserves cyclic convolution.",
 page="crt-address-map",frm=["cyclic-convolution","controlled-shifts","chinese-remainder-theorem","modular-arithmetic"])
S7=infer("S7","Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps cyclic convolution modulo $x^r-1$ onto negacyclic multiplication in $\\mathbb C[y]/(y^r+1)$.",
 "Untwisting therefore recovers the cyclic coefficient with the correct\nsign.",
 page="coefficient-twist",frm=["negacyclic-ring","cyclic-convolution","roots-of-unity"])
S8=infer("S8","After removing the known scales the coefficient error is below $1/2$, so rounding and carry propagation give the exact $2n$-bit product.",
 "The strict error below $1/2$ makes the nearest integer to\nthat value the unique correct coefficient.",
 page="exact-recovery",frm=["fixed-point-approximation","radix-digit-convolution","rounding-to-the-nearest-integer","binary-addition-with-carries"])
S9=show("S9","With fixed rational exponents and sizes $d\\approx p^{\\epsilon}$, $K\\approx d^c$, every normalized cost-table term is at most $p^{1-2\\kappa}$, so the total time is $O(n(\\lg n)^{1-\\kappa})$.",
 "fix rational exponents satisfying all layer and guard conditions, list the normalized costs, and compute each margin below one",
 M("Each procedure's saving is a power of $p$ depending on the exponents, so a single explicit choice must make all margins positive at once; the smallest margin sets $\\kappa$.","recoverable"),
 [
  infer("S9.1","Take $\\tau=\\sigma=1-2^{-50}$, $\\lambda'=1-2^{-54}$, $c=2^{-56}$, $\\epsilon=2^{-75}$, $\\delta=1/16$ and $\\kappa=2^{-182}$.",
   "These constants are deliberately conservative; no optimization is claimed.",deferred=True),
  infer("S9.2","The seven dominant powers in the cost table have margins below one whose minimum is $2^{-181}=2\\kappa$, attained by the chunk exchanges.",
   "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
   salient="The bottleneck margin $\\epsilon c(1-\\tau)=2^{-181}$ is a product of three small exponents, which is why $\\kappa$ is so small."),
  infer("S9.3","Since every fixed power of $\\log p$ is eventually at most $p^{\\kappa}$, the total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
   "Each of the seven displayed powers is at most $1-2\\kappa$ by",
   frm=["logarithms","big-o"]),
 ],page="parameter-choice",frm=["simultaneous-butterfly-layer","chunk-interchange","gaussian-resampling","synthetic-convolution"],
 adds=[B("\\epsilon","dimension exponent","The fixed exponent with $d=\\Theta(p^{\\epsilon})$ axes."),
       B("c","chunk exponent","The fixed exponent with chunk width $K=\\lfloor d^c\\rfloor$."),
       B("K","chunk width","The number of address bits in each chunk.","count"),
       B("\\delta","resampling exponent","The fixed small exponent $1/16$ in the Gaussian resampling cost bounds.")])

root=show("S","A single deterministic fixed-tape Turing machine computes the exact product of two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "reduce multiplication through radix digits, a CRT address map, Gaussian resampling and a coefficient twist to convolution over $\\mathbb C[y]/(y^r+1)$, accelerate its address moves and butterfly layers with two tape procedures derived from finite linear networks with a rank saving, recover the product exactly, and balance the parameters",
 M("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both data movement and butterfly arithmetic must each save a power of the logarithm.","explicit",
   "We therefore need savings in both movement and arithmetic."),
 [S0,S1,S2,S3,S4,S5,S6,S7,S8,S9],
 page="main-theorem",frm=["n-log-n-conjecture","harvey-van-der-hoeven-multiplier","multitape-turing-machine","worst-case-running-time","deterministic-algorithm"],
 adds=[B("n","input length","The number of bits in each of the two input integers.","count"),
       B("\\kappa","saving exponent","The fixed exponent $2^{-182}$ by which the logarithmic factor is reduced.")],
 salient="The saving below $n\\log n$ is a strict power of the logarithm, though with the tiny exponent $\\kappa=2^{-182}$, refuting the conjectured $\\Omega(n\\log n)$ bound in this model.")

# order check
def walk(n,out):
    if n["intention"]=="infer": out.append((n["id"],src.index(n["quote"]["quote"]),n.get("deferred",False)))
    for c in n.get("children",[]): walk(c,out)
o=[];walk(root,o);last=-1
for i,p,d in o:
    if d: continue
    if p<last: print("ORDER",i)
    last=p
json.dump({"root":root},open(D+'exegenius/tasks/0003-argument.answer.json','w'),indent=1,ensure_ascii=False)
print("ok")
