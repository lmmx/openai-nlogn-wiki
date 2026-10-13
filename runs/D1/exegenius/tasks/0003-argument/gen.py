import json
src=open('/home/user/openai-nlogn-wiki/runs/D1/sources/paper.tex').read()
def Q(t):
    assert t in src, t
    return {"source":"paper","quote":t}
def mot(text,src_,q=None):
    return {"text":text,"source":src_,"quote":Q(q) if q else None}
def inf(id,claim,q,page=None,frm=None,deferred=False,salient=None):
    d={"id":id,"intention":"infer","claim":claim,"quote":Q(q),"page":page,"from":frm or []}
    if deferred:d["deferred"]=True
    if salient:d["salient"]=salient
    return d
def show(id,claim,method,motivation,children,page=None,frm=None,salient=None,adds=None):
    d={"id":id,"intention":"show","claim":claim,"method":method,"motivation":motivation,"children":children,"page":page,"from":frm or []}
    if salient:d["salient"]=salient
    if adds:d["adds"]=adds
    return d
def b(sym,name,meaning,rel="direct"):
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}

A=inf("S1","A multitape machine with fixed alphabet and tapes can do elementary scans, permutations of digit pairs and controlled shifts on arrays in lexicographic order in time linear in the volume.",
 "A machine has one fixed finite alphabet and one fixed finite number of","tape-layout-streams",
 ["multitape-tm","deterministic-algorithms-and-tape-scans","multidimensional-arrays-and-tensors","mixed-radix-and-positional-digit-expansion","permutations"])

B1=inf("S2.1","A fixed linear network exchanges two banks of values and restores auxiliary values; applied to arrays of volume $V$ with an invertible frame per gate, intermediate frames cancel and only an endpoint operator remains.",
 "We construct two fixed linear networks that exchange two banks of values","linear-network-frames",
 ["linear-algebra-over-a-field","permutations","tape-layout-streams"])
B2=inf("S2.2","The three-element-subset construction gives a bit network with $W$ wires whose edge differences have total rank $s<Wm$.",
 "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,","subset-intersection-network",
 ["basic-finite-set-combinatorics","linear-algebra-over-a-field","linear-network-frames"],
 salient="The strict inequality $s<Wm$: the total number of smaller calls is below the trivial count, which is the source of every later power saving; it comes from auxiliary wires cancelling the intersection-size coefficients.")
B3=inf("S2.3","A call at parameter $mf$ uses $s<Wm$ calls at parameter $f$ on streams of volume $V/W$, so the cost per volume grows like a power $m^\\tau$ with $\\tau<1$.",
 "For both recurrences we may use the fixed rational exponent","recursive-power-saving",
 ["geometric-series-and-recurrences","big-o","logarithms-floor-and-ceiling","subset-intersection-network","linear-network-frames"],
 salient="Exponent strictly below 1 (here $1-2^{-50}$): the ratio $s/W<m$ makes each recursion level cost less than a factor $m$ per volume.")
B4=inf("S2.4","The address shear $(H,D)\\mapsto(H+D,D)$ with a rational matrix is done in linear time per fixed matrix via lower-triangular (Bruhat-type) factorization in tape order.",
 "\\begin{lemma}[The cost of a rational matrix shear]","address-shear",
 ["linear-algebra-over-a-field","modular-arithmetic","primes-gcd-and-coprimality","tape-layout-streams","linear-network-frames"])
B5=inf("S2.5","Two disjoint address fields of $u$ digits can be interchanged for arbitrary width in time $O(Vu^\\tau)$.",
 "\\begin{lemma}[Arbitrary-width interchange]",None,[])
B=show("S2","Two disjoint address fields of $u$ digits in an array of volume $V$ can be exchanged in time $O(Vu^\\tau)$ with $\\tau<1$, the final map being an exact permutation.",
 "Build a fixed linear exchange network with a rank saving, realize its edges by address shears, and recurse on smaller interchanges",
 mot("A rank saving in the network makes the interchange recurrence save a power of the field width, instead of paying a full pass per level.","explicit","$m$, the resulting recurrence saves a power of the chunk width."),
 [B1,B2,B3,B4,B5],"address-interchange",["tape-layout-streams","permutations","big-o"],
 salient="Cost exponent $\\tau<1$ even though the intermediate steps are XOR-like combinations of data and the end result is an exact permutation for any initial auxiliary values.",
 adds=[b("V","stored volume","Number of stored bits of the array being rearranged.","count"),
  b("u","field width","Number of radix digits in each exchanged address field.","count"),
  b("\\tau","interchange exponent","Fixed exponent below 1 in the interchange cost.","direct"),
  b("W","number of wires","Number of wires (roles) of the linear network.","count"),
  b("m","network dimension","Dimension of the fixed space carrying the subspace labels; also the factor by which the parameter grows per recursion.","direct"),
  b("s","number of smaller calls","Number of smaller calls a recursive call makes, summed over the edges of the network.","count")])

C1=inf("S3.1","Selected bits (at positions $\\rho+iK$) of grouped address chunks can be added (XORed) in one packed pass.",
 "\\begin{lemma}[Packed selected-bit addition on one rectangle]","packed-selected-bit-addition",
 ["binary-representation-and-bit-operations","address-interchange","tape-layout-streams"])
C2=inf("S3.2","The butterfly $H_0$ applied simultaneously on the same bit of $d$ address chunks of polynomial records costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, exact until one truncation.",
 "\\begin{proposition}[Simultaneous normalized butterfly layer]",None,[])
C=show("S3","Applying $H_0$ on the same bit position of up to $d$ address chunks of polynomial records costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, with all intermediate values exact Gaussian dyadics and a single truncation.",
 "Use the complex-valued network with phase frames, implement frame changes by packed selected-bit additions and chunk moves, and recurse",
 mot("Doing the $d$ butterflies one axis at a time takes $d$ whole-array passes; the network recursion yields a power saving over that.","explicit","factors would require $D$ whole-array passes."),
 [C1,C2],"simultaneous-butterfly-layer",
 ["fixed-point-dyadic","butterfly","complex-numbers","linear-network-frames","recursive-power-saving","address-interchange","elementary-gaussian-integers-and-dyadic-rationals"],
 salient="Exponent $\\lambda'<1$: the cost of a layer on $d$ axes is a power of $d$ below the $d$ passes of separate butterflies, matching the rank saving of the network.",
 adds=[b("d","number of axes","Number of address chunks on which the butterfly is applied simultaneously.","count"),
  b("\\lambda'","layer exponent","Fixed exponent below 1 in the simultaneous butterfly layer cost.","direct")])

D1=inf("S4.1","Synthetic Fourier transforms over the ring modulo $y^r+1$ are laid out on tape so that the parallel layers apply, with a stored frequency order retained for the inverse.",
 "\\begin{lemma}[Transform layout and cost]",None,[])
D2=inf("S4.2","Products of polynomials over the ring are obtained exactly from one integer product by signed packing, using the known $O(n\\log n)$ multiplier as a subroutine.",
 "\\begin{lemma}[Signed packing and normalized ring multiplication]","signed-packing",
 ["negacyclic-ring","nlogn-multiplier","polynomials","binary-representation-and-bit-operations","norms-error-bounds-and-rounding"])
D3=inf("S4.3","Convolution over the ring is computed from two forward synthetic transforms, a pointwise product and the opposite transform, with bounded error.",
 "\\begin{proposition}[Convolution from the retained transform layout]",None,[])
D=show("S4","Convolution over $\\mathbb C[y]/(y^r+1)$ can be computed by synthetic transforms that use the simultaneous butterfly layers.",
 "Do Fourier transforms over the ring with powers of $y$ as roots of unity, so roots act as signed shifts and the remaining work is butterflies, applied on a suitable layout",
 mot("Powers of y are roots of unity acting by exact signed permutations of coefficient lists, so only butterfly layers cost arithmetic.","explicit","where the required roots of unity act by exact signed permutations"),
 [D1,D2,D3],"synthetic-transform",
 ["dft","negacyclic-ring","butterfly","address-interchange","convolution"])

E1=inf("S5.1","Gaussian resampling expresses a Fourier transform of a prime-power-free length $t$ through a power-of-two transform without executing the two coordinate permutations.",
 "\\begin{lemma}[Resampling without executing the two permutations]",None,[])
E2=inf("S5.2","In the chirp identity the source permutation cancels across the two forward transforms, the pointwise product and the opposite transform.",
 "\\begin{lemma}[Chirp and permutation cancellation]","permutation-cancellation",
 ["gaussian-resampling","bluestein-chirp","permutations","dft","convolution"])
E=show("S5","Fourier transforms of pairwise coprime lengths reduce to power-of-two tensor transforms with the permutations retained in the transform formula.",
 "Gaussian resampling with the source and target permutations kept inside the formula",
 mot("Resampling usually sorts twice per coordinate, which costs full passes; keeping the permutations in the formula avoids executing them.","explicit","coordinate. We retain both permutations in the transform formula and"),
 [E1,E2],"gaussian-resampling",["dft","permutations","norms-error-bounds-and-rounding","roots-of-unity-and-euler-s-formula","synthetic-transform"])

F1=inf("S6.1","Splitting each operand into radix-$2^b$ digits reduces the integer product to a convolution of digit lists, followed by carry propagation.",
 "The source-transform procedures now supply the three transforms needed","radix-digit-reduction",
 ["convolution","schoolbook-carry-addition","mixed-radix-and-positional-digit-expansion"],deferred=True)
F2=inf("S6.2","The digit list is reindexed by the Chinese remainder theorem onto cyclic axes of distinct prime lengths, preserving convolution.",
 "To use the source tensor, we first place the ordinary coefficient stream","crt-prime-axes",
 ["convolution","modular-arithmetic","primes-gcd-and-coprimality","mixed-radix-and-positional-digit-expansion","address-shear"])
F3=inf("S6.3","Bluestein's chirp identity and a phase twist turn the middle transform into a convolution whose last axis is negacyclic modulo $y^r+1$.",
 "The power-of-two complex convolution used in the chirp identity is","bluestein-chirp",
 ["dft","convolution","negacyclic-ring","roots-of-unity-and-euler-s-formula","complex-numbers"])
F4=inf("S6.4","All transforms keep the coefficient error below $1/2$, so rounding and carry propagation give the exact product.",
 "$C_1=20$, so $\\epsilon C_1<1$ makes its coefficient width $O(p)$.","precision-exact-recovery",
 ["norms-error-bounds-and-rounding","schoolbook-carry-addition","fixed-point-dyadic"])
F5=inf("S6.5","With a fixed rational choice of exponents, including $\\kappa=2^{-182}$, each cost term divided by volume is a power of $p$ below one, so the total is $O(n(\\lg n)^{1-\\kappa})$.",
 "For the cost calculation put $V=Tp=\\Theta(n)$. The fixed-width coefficient","parameter-cost-accounting",
 ["big-o","logarithms-floor-and-ceiling","geometric-series-and-recurrences","address-interchange","simultaneous-butterfly-layer"],
 salient="The tiny value $\\kappa=2^{-182}$: it is the smallest of the power-saving margins of the cost table, each of which is a fixed rational just below one.")
F=show("S6","The product of two $n$-bit integers is reduced step by step to convolution over $\\mathbb C[y]/(y^r+1)$, recovered exactly, and its total cost is bounded.",
 "Chain reductions (digits, prime axes, power-of-two axes, polynomial ring), then recover the product and account for every cost term",
 mot("Each reduction changes the problem to a shape the fast tape procedures serve; the chain ends in a ring convolution whose transforms are the cheap synthetic ones.","recoverable"),
 [F1,F2,F3,F4,F5],None,[])

root=show("R","A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "Build two fast tape procedures (address interchange and simultaneous butterfly layers) with power savings, use them in synthetic transforms, and place those in the reduction of multiplication to convolution",
 mot("Scanning the data at each of the log n transform levels already costs n log n, so savings are needed in both data movement and arithmetic.","explicit","We therefore need savings in both movement and arithmetic."),
 [A,B,C,D,E,F],"main-result",["nlogn-multiplier","big-o","multitape-tm","logarithms-floor-and-ceiling"],
 salient="The exponent $1-\\kappa$ with the tiny $\\kappa=2^{-182}$: a power saving over $n\\log n$, however small, refuting the $n\\log n$ optimality conjecture.")
json.dump({"root":root},open('../0003-argument.answer.json','w'),indent=1)
