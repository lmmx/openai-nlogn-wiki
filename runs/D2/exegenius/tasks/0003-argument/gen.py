import json
src=open('/home/user/openai-nlogn-wiki/runs/D2/sources/paper.tex').read()
def Q(t): return {"source":"paper","quote":t}
def inf(id,claim,q,**kw):
    d={"id":id,"intention":"infer","claim":claim,"quote":Q(q)}; d.update(kw); return d
def M(text,source,quote=None):
    return {"text":text,"source":source,"quote":Q(quote) if quote else None}
def show(id,claim,method,mot,children,**kw):
    d={"id":id,"intention":"show","claim":claim,"method":method,"motivation":mot,"children":children}; d.update(kw); return d

A=show("S1","Two equal-width address chunks of $u$ digits in an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$.",
 "build a fixed linear network that exchanges two banks with restored scratch, label its edges so that edge matrices have small total rank, and recurse on smaller interchanges",
 M("Plain address rearrangement costs a full scan per level, so a recursion in which the total number of smaller calls is below (wires x parameter) is needed to save a power of the chunk width.","explicit","Because the sum of these ranks is less than the number of wires times"),
 [
 show("S1.1","A fixed linear network of gates on wires (roles), applied to arrays, can have each wire carry an invertible frame, so that only the change of frame on each edge has to be implemented.",
  "attach a frame to every source, gate and sink and observe that frames commute with pointwise gates",
  M("Pointwise gates act on matching addresses, so a common frame at a gate leaves the gate unchanged and intermediate frames cancel; only edges cost anything.","recoverable"),
  [inf("S1.1a","Each wire's stored array is $D_vg$ for the logical array $g$, with the frame $D_v$ invertible and shared by all incidences of a gate.","We call $D_v$ its frame: the stored")],
  page="linear-network",from_=["fixed-tape-model","elementary-streams","graphs-and-networks","matrices-and-linear-maps"]),
 show("S1.2","For arbitrary initial scratch values, the scalar network exchanges the two banks with a sign and restores every scratch value.",
  "schedule the operation, then undo the unwanted scratch contributions so arbitrary initial values cancel",
  M("The tape machine cannot assume scratch arrays are zero, so the net effect must be independent of their initial contents.","recoverable"),
  [inf("S1.2a","A forward invocation changes $y_S$ to $y_S+x_S$ for arbitrary scratch values; three stages exchange the banks and restore scratch.","For arbitrary initial values of its auxiliary wires, a forward")],
  page="transparent-restoration",from_=["linear-network","binary-representation-and-bit-operations"]),
 show("S1.3","Three-element subsets give nested nondegenerate subspace labels whose dimension changes count the smaller operations on each edge.",
  "assign subspaces from indicator vectors of 3-subsets using orthogonality of intersection-count inner products",
  M("The cost of a frame change on an edge is its rank, and nested labels make that rank equal the dimension drop, which can then be counted exactly.","reconstructed"),
  [inf("S1.3a","Every edge joins comparable nondegenerate labels and the total dimension lost is $Wm-2N+2L$.","Every edge joins comparable nondegenerate labels.  The only decreasing")],
  page="triple-subspace-labels",from_=["linear-network","subsets-and-counting","matrices-and-linear-maps"]),
 show("S1.4","The edges of the finite network need $s<Wm$ smaller calls in total, so a call on volume $V$ at parameter $m f$ costs $s$ calls at parameter $f$ on volume $V/W$ with $s/W<m^\\tau$.",
  "turn the strict rank inequality into a recurrence whose per-volume growth is below $m$",
  M("Dividing by volume, multiplying the parameter by $m$ multiplies cost by only $s/W<m$, which gives a power saving instead of linear growth.","explicit","This strict inequality"),
  [inf("S1.4a","Both relative rank deficits exceed $20\\cdot2^{-50}$, so $s/W<m^\\tau$ with $\\tau=1-2^{-50}$.","Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.")],
  page="rank-saving",from_=["triple-subspace-labels","recurrences-and-amortized-cost-accounting"],
  salient="The total number of smaller calls is strictly below W m, so the recursive per-volume growth s/W is strictly below m, giving an exponent tau < 1."),
 show("S1.5","Every rational matrix factors as $E_1\\Pi E_2$ with lower triangular $E_1,E_2$ and a partial permutation of rank-many ones, so an edge matrix of rank $a$ costs $a$ smaller interchanges plus tape-order shears.",
  "eliminate with lower triangular operations in tape order",
  M("Tape scans can only update a later field from earlier ones, so frame changes must be lower triangular in tape order.","explicit","Lower triangular changes of coordinates"),
  [inf("S1.5a","Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ lower triangular.","Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization")],
  page="bruhat-shear",from_=["matrices-and-linear-maps","elementary-streams"]),
 inf("S1.6","There is a fixed $0<\\tau<1$ and one fixed multitape procedure interchanging two $u$-digit address chunks of an array of volume $V$ in $O(Vu^\\tau)$ steps.","There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape")
 ],page="chunk-interchange",from_=["fixed-tape-model","elementary-streams"],
 adds=[{"symbol":"u","name":"chunk width","meaning":"the number of digits in each of the two address chunks being interchanged","relation":"count"},
       {"symbol":"V","name":"array volume","meaning":"the number of stored bits of the array","relation":"count"}])

B=show("S2","The synthetic Fourier transform over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ is a contraction with exact inverse pair up to a factor and is computed on a tape layout with simultaneous butterfly layers.",
 "use roots of unity that are signed shifts, compute butterfly levels in simultaneous layers, and lay out axes so chunk swaps bring selected bits together",
 M("A transform has about log n butterfly levels, so each level must cost less than a whole-array pass; roots y^(2r/t) make twiddles cheap signed shifts.","explicit","Scanning an array of $\\Theta(n)$ stored bits at each of"),
 [
 show("S2.1","A layer applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit in $d$ address chunks of complex fixed-point polynomial records costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
  "run the same linear-network recursion on a complex network with phase frames, using packed bit additions, then normalize and truncate once",
  M("Separate butterfly factors would need D whole-array passes; the network gives a rank saving again, so d chunks cost d^lambda'.","explicit","whereas separate butterfly factors would require $D$ whole-array passes"),
  [
  show("S2.1a","The kernel $C=HSH=aI+bX$ gives the complex network's edge frame changes as products of translation kernels on binary subspaces over Gaussian dyadic numbers.",
   "express the edge differences of phase frames by orthonormal binary residual bases",
   M("Binary orthonormal residuals make each edge change a product of simple two-point kernels, mirroring the bit network.","recoverable"),
   [inf("S2.1a1","The phase-frame difference of an edge is a product of one translation kernel per basis vector of the edge residual.","Hold the unselected address bits fixed and regard the stored complex")],
   page="phase-frames",from_=["butterfly","linear-network","triple-subspace-labels","gaussian-integers-and-dyadic-rationals"]),
  show("S2.1b","Selected bits across address chunks of many axes can be added at once on packed records, with the small exceptional set of addresses repaired by sorting.",
   "pack records so most addresses are handled by a uniform scan and repair the exceptional ones by sorting",
   M("The exceptional set is a vanishing fraction because K grows faster than log p, so sorting only it is affordable.","explicit","make the exceptional set in a packed change of address bits small enough"),
   [inf("S2.1b1","Packed selected-bit addition on a rectangle of $R$-bit records is a linear tape scan plus a small sort.","Packed selected-bit addition on one rectangle")],
   page="packed-bit-addition",from_=["elementary-streams","sorting-and-permutations","chunk-interchange"]),
  inf("S2.1c","The simultaneous normalized butterfly layer on $d$ chunks costs $O(Vd^{\\lambda'})$ with error below $\\sqrt2\\,2^{-p}$ after a single truncation.","Fix positive constants $a_d\\le b_d$ and $a_r\\le b_r$, and fix")
  ],page="simultaneous-butterfly-layer",from_=["fixed-point-contraction","butterfly","chunk-interchange","rank-saving"]),
 inf("S2.2","With $\\omega_t=y^{2r/t}$, the transforms $F_t^\\pm$ are contractions and $F_t^+F_t^-=t^{-1}I$.","If $j$ is an integer, then"),
 inf("S2.3","On a layout that places selected bits in consecutive chunks, the synthetic transform costs a sum of prefix-move, chunk-exchange and simultaneous-round terms.","Fix the rational parameters and positive comparison constants")
 ],page="synthetic-transform",from_=["ring-y-r-plus-1","dft","butterfly","chunk-interchange","phase-frames","roots-of-unity"])

C=show("S3","Convolution over $\\mathcal R_r$ on a multi-axis array is computed from two forward synthetic transforms in the same frequency order, a pointwise product and the opposite transform, with error below $\\sqrt2 M(3\\ell+1)2^{-p}$.",
 "transform, multiply pointwise, and inverse transform, using the big-integer multiplier only for the pointwise ring products",
 M("Convolution becomes a pointwise product after a Fourier transform, and keeping the frequency order avoids separate permutations.","explicit","retain the same frequency order through their pointwise product"),
 [
 show("S3.1","Multiplying two polynomial records modulo $y^r+1$ is done by signed Kronecker packing into one big integer in $O(rp\\log(rp))$ time.",
  "pack coefficients with signs into a single integer, multiply with the O(N log N) multiplier and unpack",
  M("Records have only O(rp) bits, much shorter than n, so the established multiplier can be called as an ordinary subroutine.","explicit","This is an independent subroutine."),
  [inf("S3.1a","For $r=2^\\ell<2^p$ the exact numerators of $fg$ and $Q_p(fg/r)$ are computed in $O(rp\\log(rp))$ time.","Let $r=2^\\ell<2^p$ with integers $\\ell\\geq1$ and $p\\geq2$, and fix $C_w>1$.")],
  page="signed-packing",from_=["harvey-hoeven-multiplier","ring-y-r-plus-1"]),
 inf("S3.2","Under the layout hypotheses, $\\mathcal M_r$ has an approximation with the stated error and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.","Under the hypotheses of Lemma~\\ref{lem:synthetic-transform-cost},")
 ],page="synthetic-convolution",from_=["convolution","synthetic-transform","simultaneous-butterfly-layer","chunk-interchange","harvey-hoeven-multiplier","fixed-point-contraction"])

D=show("S4","The Fourier transforms of coprime lengths needed for the product are expressed through power-of-two tensor transforms with the source and target permutations left inside the transform and cancelling.",
 "use Gaussian resampling and Bluestein's chirp, never executing the two permutations",
 M("Sorting twice per coordinate is the usual cost of resampling; keeping the permutations inside the identity avoids the full sorts.","explicit","Its usual implementation sorts twice on each"),
 [
 show("S4.1","A Fourier transform of length $s$ coprime to $t$ equals $2^{2\\alpha^2}B_0P_tF_tA$ up to a permutation, with contractions $A,B_0$ computable in $O(tp^{3/2+\\delta}\\alpha)$.",
  "apply the Harvey-van der Hoeven resampling identity with contractions A and B0",
  M("Powers of two are what the synthetic transforms need while the digit lengths must be coprime, so the identity bridges the two lengths.","explicit","Gaussian resampling"),
  [inf("S4.1a","There are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, and approximations with error below $p^2$ and time $O(tp^{3/2+\\delta}\\alpha)$.","There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and")],
  page="gaussian-resampling",from_=["dft","fixed-point-contraction","harvey-hoeven-multiplier","prime-numbers-and-coprimality"]),
 inf("S4.2","Applying the one-dimensional maps line by line gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ on the tensor product.","Suppose every pair $(s_i,t_i)$, $1\\leq i\\leq d$, satisfies"),
 show("S4.3","The permuted middle transform $QF_{\\boldsymbol t}$ equals a chirp multiplication, a cyclic convolution and another chirp, and the retained source permutation $R$ cancels across the transforms.",
  "use Bluestein's identity",
  M("The chirp turns the permuted frequency change into a convolution, which the synthetic convolution can compute.","recoverable"),
  [inf("S4.3a","$QF_{\\boldsymbol t}u=\\overline a\\cdot\\frac{a*(\\overline a\\cdot u)}{T}$ for the chirp array $a$.","assume every $t_i$ is even. For $\\boldsymbol j\\in\\mathbb Z^d$, define")],
  page="bluestein-chirp",from_=["convolution","dft","sums-and-product-notation-euler-s-formula"])
 ],page="retained-permutations",from_=["dft","fixed-point-contraction","chunk-interchange","harvey-hoeven-multiplier"])

E=show("S5","The multiplication algorithm maps the radix digits through $\\Phi$ to prime axes, takes two source transforms, multiplies pointwise, takes the opposite transform, scales, rounds, applies $\\Phi^{-1}$ and propagates carries.",
 "reduce the integer product to a convolution of digits and evaluate it with the previous machinery",
 M("Multiplication of integers is convolution of digit sequences, so a convolution routine yields the product.","explicit","Splitting the inputs into radix digits reduces multiplication to"),
 [
 show("S5.1","Splitting each integer into radix-$2^b$ digits makes the product a convolution modulo $x^S-1$ without wraparound.",
  "write the integers as polynomials in 2^b and check capacity",
  M("The degree of the product is below S, so cyclic convolution of length S equals the ordinary product.","recoverable"),
  [inf("S5.1a","The product has degree at most $2q-2<S$ so convolution modulo $x^S-1$ has no nonzero wraparound.","Thus convolution modulo $x^S-1$ has no nonzero wraparound.")],
  page="radix-digit-convolution",from_=["convolution","binary-representation-and-bit-operations","schoolbook-and-divide-and-conquer-multiplication"]),
 show("S5.2","A convolution-preserving map $\\Phi$ places the radix-digit list on a product of distinct prime cyclic axes, implemented by controlled shifts and axis moves.",
  "use the Chinese remainder theorem to split one cyclic convolution into a multidimensional one",
  M("Resampling needs pairwise coprime axis lengths, which the CRT split provides.","recoverable"),
  [inf("S5.2a","For pairwise coprime $s_i$, $x\\mapsto\\prod_i x_i^{\\mu_i}$ is a convolution-preserving map implemented by controlled cyclic shifts.","Let $s_1,\\ldots,s_d$ be the pairwise coprime")],
  page="crt-prime-axes",from_=["chinese-remainder-theorem","convolution","chunk-interchange","elementary-streams"]),
 show("S5.3","Scaling coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ turns the cyclic convolution in the last coordinate into polynomial multiplication modulo $y^r+1$.",
  "twist coefficients so that the negative wrap undoes to the cyclic wrap",
  M("The synthetic convolution only handles the negacyclic ring, so the cyclic convolution of the chirp identity must be converted.","explicit","The power-of-two complex convolution used in the chirp identity is"),
  [inf("S5.3a","The map $x_d\\mapsto\\zeta y$ is an isomorphism preserving the coefficient sup norm, and the wrap factor is $\\zeta^j$.","is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.")],
  page="coefficient-twist",from_=["ring-y-r-plus-1","convolution","roots-of-unity"]),
 inf("S5.4","The algorithm applies $\\Phi$, two source transforms, a pointwise product, the opposite transform, two scalings, rounding, $\\Phi^{-1}$ and carry propagation.","The source-transform procedures now supply the three transforms needed")
 ],page="multiplication-algorithm",from_=["fast-fourier-transform","retained-permutations","synthetic-convolution"])

F=show("S6","The recovered coefficient error is below $1/2$, so rounding gives the exact integer coefficients and carries give the exact $2n$-bit product.",
 "track the errors of the contractions and the scales, then round",
 M("The integer coefficients are recovered exactly only if the accumulated error is below 1/2.","recoverable"),
 [inf("S6.1","The final absolute error is below $1/2$, so the nearest integer is the unique correct coefficient.","The strict error below $1/2$ makes the nearest integer to")],
 page="exact-recovery",from_=["fixed-point-contraction","rounding-and-floating-or-fixed-point-error"])

G=show("S7","With $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$ and $K=\\lfloor d^c\\rfloor$, every term of the normalized cost table is at most $p^{1-2\\kappa}$, so the total is $O(n(\\lg n)^{1-\\kappa})$.",
 "choose compatible parameters and bound each cost-table row",
 M("Each procedure saves only a small power, so the parameters must balance all rows of the cost table to leave a positive margin.","recoverable"),
 [inf("S7.1","The total cost is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.","O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).")],
 page="parameter-choice",from_=["floor-ceiling-logarithms-and-exponents","big-o","simultaneous-butterfly-layer","gaussian-resampling","signed-packing"],
 salient="All seven dominant powers of p in the cost table have a positive margin below one, and the smallest margin is 2^-181 = 2 kappa.")

root=show("S0","A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
 "reduce integer multiplication to a Fourier convolution evaluated with two fast tape procedures, then bound error and cost",
 M("Scanning Theta(n) bits at each of Theta(log n) transform levels costs n log n, so power savings are needed in both movement and arithmetic.","explicit","We therefore need savings in both movement and arithmetic."),
 [A,B,C,D,E,F,G],page="main-theorem",from_=["nlogn-conjecture","harvey-hoeven-multiplier","multitape-tm","big-o"])

def fix(n):
    if "from_" in n: n["from"]=n.pop("from_")
    for c in n.get("children",[]): fix(c)
fix(root)
# order check
pos=0
def walk(n):
    global pos
    if n["intention"]=="infer":
        q=n["quote"]["quote"]; i=src.find(q,pos)
        assert q in src, q
        assert i>=0,("order",n["id"],q)
        pos=i+len(q)
    for c in n.get("children",[]): walk(c)
walk(root)
for n in [root]:
    pass
json.dump({"root":root},open('/home/user/openai-nlogn-wiki/runs/D2/exegenius/tasks/0003-argument.answer.json','w'),indent=1)
