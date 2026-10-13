import json
def Q(t): return {"source":"paper","quote":t}
def inf(id,claim,quote,page=None,frm=(),deferred=False,salient=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":Q(quote),"from":list(frm)}
    if page:n["page"]=page
    if deferred:n["deferred"]=True
    if salient:n["salient"]=salient
    return n
def show(id,claim,method,mot,src,children,page=None,frm=(),adds=None,salient=None,mq=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,
       "motivation":{"text":mot,"source":src,"quote":Q(mq) if mq else None},
       "children":children,"from":list(frm)}
    if page:n["page"]=page
    if adds:n["adds"]=adds
    if salient:n["salient"]=salient
    return n
def B(s,name,mean,rel="count"): return {"symbol":s,"name":name,"meaning":mean,"relation":rel}

S1=inf("S1","Schönhage and Strassen conjectured that $n\\log n$ is the optimal order of multiplication cost, and Harvey and van der Hoeven reached $O(n\\log n)$, so only a power saving in the log factor can beat it.",
  "proposed $n\\log n$ as the optimal order of growth","multiplication-history")
S2=inf("S2","Splitting both integers into radix digits reduces multiplication to convolution of short integer coefficient lists.",
  "Splitting the inputs into radix digits reduces multiplication to","digit-convolution-reduction",["convolution","binary-representation-of-integers","integer-addition-multiplication-and-carry-propagation"])
S31=inf("S3.1","Moving data between $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$ by plain scanning, so both movement and arithmetic must be made cheaper.",
  "$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$.","address-interchange-bottleneck",["tape-streams","sorting-and-linear-tape-scans","multitape-tm"])
S321=inf("S3.2.1","A fixed linear network exchanges two banks of values with signs and restores auxiliary values; each wire has a role and invertible frames $D_v$ change its stored representation, cancelling across the network.",
  "We construct two fixed linear networks that exchange two banks of values","linear-network-roles",["matrices-rank-and-invertibility","vector-spaces-subspaces-and-linear-maps"],deferred=True)
S322=inf("S3.2.2","A fixed finite network with nested subspaces attached to gates, built from three-element subsets with gather/scatter and cancelling auxiliary wires, makes the total number $s$ of smaller calls satisfy $s<Wm$.",
  "\\begin{lemma}\\label{lem:motif-residuals}","finite-subset-network",["linear-network-roles","sets-subsets-functions-and-permutations","vector-spaces-subspaces-and-linear-maps"],deferred=True)
S323=inf("S3.2.3","A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ each, so cost per volume grows by $s/W<m$ per multiplication of the parameter by $m$, a power saving.",
  "\\subsection{Explicit rational bounds for the two recurrences}","recursive-saving",["finite-subset-network","linear-network-roles","recurrence-relations-and-the-master-theorem"],deferred=True,
  salient="The saving is a strict inequality $s/W<m$ that holds uniformly at every recursion level, which turns into a power of the parameter rather than a constant factor.")
S32=show("S3.2","Both tape procedures come from a fixed linear network whose total number $s$ of smaller calls is less than $Wm$, and the recursion on it saves a power of the parameter.",
  "build a finite network with a rank deficit, then recurse on it","Each procedure is a network of pointwise gates on $W$ role streams; making the gates' edge changes cost fewer smaller calls than the trivial bound gives a recurrence with contraction, as one needs a strict saving in each recursion level.","reconstructed",
  [S321,S322,S323],
  adds=[B("W","number of roles","the number of wires (roles) of the fixed network, among which rows are distributed"),
        B("m","parameter base","the dimension of the fixed space whose subspaces are attached to gates and the factor by which the parameter is multiplied per recursion level","direct"),
        B("s","number of smaller calls","the total number of smaller calls of the procedure needed by all edges of the network")])
S331=inf("S3.3.1","Every rational matrix factors as lower-triangular times partial permutation times lower-triangular, so an address shear $(H,D)\\mapsto(H+D,D)$ costs by rank.",
  "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization","address-shear-factorization",["controlled-shifts","matrices-rank-and-invertibility","gaussian-elimination"],deferred=True)
S332=inf("S3.3.2","Interchanging two address fields via XOR combinations of data and address shears costs $O(Vu^\\tau)$ with $\\tau<1$, the final effect being an exact permutation.",
  "Choose a rational number $\\tau\\in(0,1)$ with $s/W<m^\\tau$.","fast-address-interchange",["recursive-saving","xor-and-bitwise-operations"],deferred=True,
  salient="The cost exponent $\\tau$ is strictly below 1 although the final effect is only a permutation; it is obtained from $s/W<m^\\tau$.")
S33=show("S3.3","Two disjoint contiguous address fields of $u$ bits in an array of volume $V$ can be interchanged in time $O(Vu^\\tau)$ with a fixed $\\tau<1$.",
  "instantiate the bit network with rational subspaces and implement edges by address shears","The address interchange is a permutation whose cost can be cut by the network recursion, and the edge operators are address shears that a factorization makes cheap.","recoverable",
  [S331,S332],frm=["recursive-saving","controlled-shifts"])
S341=inf("S3.4.1","Intermediate values of a butterfly layer are exact Gaussian dyadics and a single truncation follows the completed contractive layer.",
  "Intermediate values are exact Gaussian dyadics,","fixed-point-dyadics",["complex-numbers","fixed-point-and-finite-precision-arithmetic","norms-error-bounds-and-triangle-inequality"],deferred=True)
S342=inf("S3.4.2","Phase frames express a butterfly layer on selected bits through smaller groups of selected bits separated by binary changes of basis.",
  "Hold the unselected address bits fixed and regard the stored complex","",deferred=True)
del S342["from"]
S343=inf("S3.4.3","Adding selected bit positions across rectangles of packed records on tapes costs linear time with a deterministic repair of exceptional addresses.",
  "\\begin{lemma}[Packed selected-bit addition on one rectangle]","packed-selected-bit-addition",["controlled-shifts","fast-address-interchange","xor-and-bitwise-operations"],deferred=True)
S344=inf("S3.4.4","The simultaneous normalized butterfly layer on at most $d$ chunks costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
  "\\begin{proposition}[Simultaneous normalized butterfly layer]",None,deferred=True,
  salient="The exponent $\\lambda'$ is strictly below 1: $d$ separate butterfly factors would cost $D$ passes over the array.")
S34=show("S3.4","Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ simultaneously to selected coordinate bits of numerical arrays costs $O(Vd^{\\lambda'})$ with a fixed $\\lambda'<1$.",
  "instantiate the complex phase network and bound its numerical layout and precision","A butterfly layer is a linear pointwise operation, so the same network trick that cheapens the address interchange applies, provided the dyadic values stay exact and the packed address changes are cheap.","recoverable",
  [S341,S342,S343,S344],page="fast-butterfly-layers",frm=["recursive-saving","fast-address-interchange"])
S3=show("S3","Two tape procedures, a fast address-field interchange and a simultaneous butterfly layer, cheapen both data movement and arithmetic of the transform levels.",
  "supply two fast procedures from one linear-network construction","Plain movement and arithmetic cost n log n over log n levels, so a power saving needs both to be cheaper; one network idea provides both.","explicit",
  [S31,S32,S33,S34],mq="We therefore need savings in both movement and arithmetic.",
  adds=[B("V","stored bit volume","the number of stored bits of the array operated on"),
        B("u","field width","the number of address digits (bits) in each of the two interchanged address fields"),
        B("d","chunk count","the maximum number of equal-width address chunks whose selected bits are butterflied simultaneously"),
        B("\\tau","interchange exponent","the fixed exponent below 1 in the address interchange cost","direct"),
        B("\\lambda'","butterfly exponent","the fixed exponent below 1 in the butterfly layer cost","direct")])
S41=inf("S4.1","The radix-digit list is placed on a product of cyclic axes of distinct prime lengths by a Chinese-remainder address map that preserves convolution.",
  "\\subsection{An explicit cyclic-convolution layout}","cyclic-crt-axes",["chinese-remainder-theorem","convolution","multidimensional-arrays-and-mixed-radix-indexing","cyclic-groups-and-products-of-groups"],deferred=True)
S42=inf("S4.2","Gaussian resampling expresses each prime-length Fourier transform through a power-of-two tensor transform with source and target permutations retained.",
  "\\begin{lemma}[Resampling without executing the two permutations]","gaussian-resampling",["dft-fft","multidim-transform","cyclic-crt-axes","roots-of-unity"],deferred=True)
S43=inf("S4.3","Bluestein's chirp identity turns the middle transform into a normalized cyclic convolution multiplied by chirp phases.",
  "\\begin{lemma}[Chirp and permutation cancellation]","bluestein-chirp",["dft-fft","convolution","gaussian-resampling"],deferred=True)
S44=inf("S4.4","A last-coordinate phase twist turns a cyclic coordinate into a polynomial coordinate modulo $y^r+1$; removing the twist restores the cyclic wrap.",
  "\\subsection{Complex convolution by a coefficient twist}","phase-twist",["poly-ring-negacyclic","roots-of-unity","bluestein-chirp"],deferred=True)
S451=inf("S4.5.1","Synthetic polynomial transforms use powers of $y$ as roots of unity, so twiddles are signed shifts, and two forward transforms retain one frequency order through the pointwise product.",
  "\\begin{lemma}[Transform layout and cost]","synthetic-transforms",["poly-ring-negacyclic","dft-fft","multidim-transform"],deferred=True)
S452=inf("S4.5.2","Pointwise polynomial products in the ring are computed by signed packing (Kronecker substitution) and the standard $O(n\\log n)$ multiplier as an ordinary subroutine.",
  "\\begin{lemma}[Signed packing and normalized ring multiplication]","normalized-ring-products",["polynomials","poly-ring-negacyclic","integer-addition-multiplication-and-carry-propagation"],deferred=True)
S45=show("S4.5","Convolution over the remaining axes is computed over $\\mathbb C[y]/(y^r+1)$ by forward synthetic transforms, pointwise ring products and the opposite transform.",
  "transform, multiply pointwise, transform back","This is the convolution theorem: transforms turn convolution into pointwise products, and the ring makes twiddle multiplications shifts.","recoverable",
  [S451,S452],frm=["convolution","dft-fft"])
S4=show("S4","The digit convolution reduces, by a chain of changes of problem and representation, to convolution over $\\mathbb C[y]/(y^r+1)$.",
  "chain of reductions: prime cyclic axes, power-of-two axes, polynomial ring","The fast tape procedures and synthetic transforms apply only to power-of-two axes with negacyclic ring coordinate, while the digit convolution has no such shape.","reconstructed",
  [S41,S42,S43,S44,S45],frm=["convolution","dft-fft"])
S51=inf("S5.1","The known normalizations and digit scales are removed, the recovered coefficient error is strictly below $1/2$, and carries are propagated to give the exact binary product.",
  "\\subsection{Precision and exact recovery}","precision-exact-recovery",["fixed-point-and-finite-precision-arithmetic","norms-error-bounds-and-triangle-inequality","floor-ceiling-logarithms-and-rounding","integer-addition-multiplication-and-carry-propagation"],deferred=True)
S52=inf("S5.2","A compatible choice of rational parameters makes all terms in the cost table fit $O(n(\\lg n)^{1-\\kappa})$.",
  "\\subsection{The complete time bound}",None,["constants-asymptotic-functions-and-polylog-factors","big-o"],deferred=True)
S5=show("S5","The approximate transforms recover the exact integer product, and the total cost is $O(n(\\lg n)^{1-\\kappa})$.",
  "bound the rounding error below 1/2 and then add up costs","Rounding to the nearest integer is exact only once the error is below 1/2; the cost is a sum over steps controlled by the chosen parameters.","recoverable",
  [S51,S52])
S6=inf("S6","The power saving gives a limit of zero for $T_A(n)/(n\\lg n)$, so the $n\\log n$ lower bound conjecture fails in this model.",
  "The power saving proved here gives a limit of zero through all input lengths,",None,["multiplication-history"])
root=show("S0","A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
  "reduce to convolution, accelerate transforms by two network-based tape procedures, then recover the product","Beating n log n needs a power saving in the log factor, which requires cheaper transform levels (S3) inside the standard multiplication-by-convolution reduction (S2, S4) with exact recovery (S5).","reconstructed",
  [S1,S2,S3,S4,S5,S6],page="main-theorem",frm=["multitape-tm","big-o"],
  salient="$\\kappa=2^{-182}$ is an astronomically small exponent; it is the product of the saving exponents from the recursions, so only a tiny power of log is saved.",
  adds=[B("\\kappa","saving exponent","the fixed positive exponent of the log factor saving, $2^{-182}$","direct")])
json.dump({"root":root},open("/home/user/openai-nlogn-wiki/runs/C2/exegenius/tasks/0003-argument.answer.json","w"),indent=1,ensure_ascii=False)
