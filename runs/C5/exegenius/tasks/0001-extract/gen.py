import json
C=[]
def add(id,name,gloss,req,quotes=(),known=False,title=None,symbols=None,aliases=()):
    d=dict(id=id,name=name,aliases=list(aliases),gloss=gloss,requires=[] if known else req,known=known,
           evidence=[dict(source="paper",quote=q) for q in quotes])
    if title: d["title"]=title; d["symbols"]=symbols
    C.append(d)
def S(sym,name,meaning,rel="direct"): return dict(symbol=sym,name=name,meaning=meaning,relation=rel)
add("big-o","Big-O notation","Asymptotic upper bounds on running time.",[],known=True)
add("polynomials","Polynomials","Sums of coefficients times powers of a variable, with addition and multiplication.",[],known=True)
add("complex-numbers","Complex numbers","Numbers a+bi, including roots of unity.",[],known=True)
add("turing-machine-basics","Turing machines and tapes","Machines with finite control reading and writing cells on tapes.",[],known=True)
add("multitape-model","Fixed multitape Turing machine model","One fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads/writes one cell per tape and moves each head at most one cell, so moving data costs time.",["turing-machine-basics","big-o"],
    ["A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."])
add("nlogn-conjecture","The n log n conjecture and history","Schönhage and Strassen proposed n log n as optimal multiplication cost; Schönhage–Strassen, Fürer and Harvey–van der Hoeven reduced upper bounds down to O(n log n).",["multitape-model","big-o"],
    ["Sch\\\"onhage and Strassen proved in 1971 that two $n$-bit integers can"],
    title="The $n\\log n$ conjecture and history",symbols=[S("n","input length","The number of bits of each multiplicand.","count")])
add("hh-multiplier","Established O(n log n) multiplier","The Harvey–van der Hoeven O(n log n) multiplication algorithm, used here only as an ordinary subroutine for small products.",["nlogn-conjecture"],
    ["Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine"],
    title="Established $O(n\\log n)$ multiplier",symbols=[S("n","input length","The number of bits of each multiplicand in the subroutine call.","count")])
add("dft-roots-of-unity","Discrete Fourier transform and roots of unity","Evaluating a polynomial at all powers of a root of unity; the fast version is the FFT, built from layers of two-point butterflies.",["polynomials","complex-numbers","big-o"],
    ["Scanning an array of $\\Theta(n)$ stored bits at each of"])
add("cyclic-convolution","Convolution and the convolution theorem","Multiplying polynomials (mod x^N−1 for cyclic) by transforming, multiplying pointwise, and inverse transforming; integer multiplication reduces to it by splitting into radix digits.",["dft-roots-of-unity"],
    ["Splitting the inputs into radix digits reduces multiplication to"])
add("multidimensional-transform","Multidimensional transforms","A transform on an array with several axes, applied axis by axis; axis lengths such as primes or powers of two determine cost and layout.",["cyclic-convolution"],
    ["it replaces the Fourier transforms needed for"])
add("crt-prime-axes","Chinese-remainder map to prime cyclic axes","A Chinese-remainder address map placing a coefficient list onto a product of distinct prime cyclic axes while preserving convolution.",["multidimensional-transform"],
    ["placed on a product of"])
add("gaussian-resampling","Gaussian resampling","Harvey–van der Hoeven identity expressing each Fourier transform on prime-length axes through a power-of-two tensor transform, with contraction bounds on the error.",["multidimensional-transform","fixed-point-precision"],
    ["Gaussian",])
add("bluestein-chirp","Bluestein chirp identity","Rewrites a transform as a cyclic convolution by multiplying by chirp phases.",["cyclic-convolution"],
    ["Bluestein's chirp identity converts the middle transform,"])
add("ring-y-r-plus-1","Polynomial ring modulo y^r + 1","The ring of polynomials with complex coefficients in y modulo y^r+1, r a power of two; powers of y act as roots of unity and multiplying by one is a signed shift of the coefficient list.",["polynomials","complex-numbers"],
    ["one coordinate\nis stored as the coefficient list of a polynomial modulo $y^r+1$".replace("\n"," ")],
    title="Polynomial ring modulo $y^r+1$",symbols=[S("y","ring variable","The indeterminate of the polynomials.") ,S("r","ring degree","The number of complex coefficients in a polynomial; a power of two.","count")])
add("synthetic-transforms","Synthetic polynomial transforms","Nussbaumer-style transforms whose roots of unity are powers of y in the ring, so multiplications by roots are signed shifts, leaving only shifts, address rearrangements and butterflies.",["ring-y-r-plus-1","dft-roots-of-unity","butterfly-layer"],
    ["serve as roots of unity in the remaining axes, and multiplication by"])
add("phase-twist","Phase twist to the negative-wrap ring","A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap after untwisting.",["ring-y-r-plus-1","cyclic-convolution"],
    ["A phase twist changes the last cyclic coordinate into a polynomial"])
add("signed-packing","Signed packing (Kronecker substitution)","Packing polynomial coefficients into a single integer with signs so ring products reduce to integer products done by the established multiplier.",["hh-multiplier","polynomials"],
    ["Signed coefficient"])
add("fixed-point-precision","Fixed-point complex coefficients and exact recovery","Numerical arrays hold complex fixed-point dyadic numbers; errors are bounded below 1/2 so rounding recovers exact integer coefficients.",["complex-numbers"],
    ["proves that the recovered"])
add("address-fields-layout","Array addresses, fields and tape layout","Arrays are stored on tape in row-major address order; address bit-fields (chunks) are contiguous and permuting them costs more than scanning.",["multitape-model"],
    ["interchanging fields whose numbers of digits grow"])
add("linear-network","Linear networks with restored auxiliary values","A fixed network of gates exchanging two banks of values with signs, with roles for each wire, whose auxiliary values are restored so the effect is exact for arbitrary initial auxiliary contents.",["address-fields-layout"],
    ["Each procedure arises from its own fixed linear network that exchanges two"])
add("frames","Frames of a linear network","Invertible linear operators attached to sources, gates and sinks changing how a logical array is stored; intermediate frames cancel leaving an endpoint operator.",["linear-network"],
    ["we call $D_v$ its frame"] if False else ["The representation of a role's array may change along the network."])
add("subset-subspace-labels","Subset-intersection subspace labels","Subspaces of a fixed m-dimensional space attached to gates using three-element subsets, nested along edges so dimension drops count smaller calls and the total s<Wm.",["linear-network"],
    ["The construction uses\nthree-element subsets".replace("\n"," ")])
add("recursive-saving","Recursive power saving from s<Wm","A call at parameter mf makes s<Wm calls at parameter f on volume V/W streams, so per-volume cost grows by a factor below m, giving a power saving.",["subset-subspace-labels","frames"],
    ["This strict inequality"])
add("address-shear","Address shear and triangular factorization","The endpoint operator (H,D)↦(H+D,D) on address fields; a rank-reducing lower-triangular factorization lets two further linear updates complete an interchange.",["frames","address-fields-layout"],
    ["an address shear"])
add("fast-address-interchange","Fast interchange of address fields","Swaps two disjoint contiguous u-bit address fields of an array of stored volume V in cost O(V u^τ), τ<1, using XOR combinations whose final effect is an exact permutation.",["recursive-saving","address-shear"],
    ["Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."],
    title="Fast interchange of address fields in cost $O(Vu^\\tau)$",symbols=[S("V","stored bit volume","The number of stored bits in the array.","count"),S("u","field width","The number of bits in each interchanged address field.","count"),S("\\tau","savings exponent","A fixed constant below 1 controlling the cost.")])
add("butterfly-layer","Two-point butterfly H₀","The operation (u,v)↦((u+v)/2,(u−v)/2) applied coefficientwise.",["complex-numbers","polynomials"],
    ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)"],
    title="Two-point butterfly $H_0(u,v)$",symbols=[S("H_0","butterfly map","The map sending a pair to its half-sum and half-difference."),S("u","first input","The first value of the pair."),S("v","second input","The second value of the pair.")])
add("fast-butterfly-layers","Fast simultaneous butterfly layers","Applies H₀ simultaneously on the same selected bit of at most d address chunks in cost O(V d^λ′), via the linear network with phase frames and a single final truncation.",["recursive-saving","butterfly-layer","fixed-point-precision","fast-address-interchange"],
    ["the cost is $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$"],
    title="Fast simultaneous butterfly layers in cost $O(Vd^{\\lambda'})$",symbols=[S("V","stored bit volume","The number of stored bits in the arrays.","count"),S("d","chunk count","The number of equal-width address chunks in which the same bit is selected.","count"),S("\\lambda'","savings exponent","A fixed constant below 1 controlling the cost.")])
add("fast-synthetic-transform","Synthetic transforms with retained frequency order","Forward synthetic transforms keep the same frequency order through their pointwise product and the opposite transform consumes it, using fast butterfly layers and interchanges.",["synthetic-transforms","fast-butterfly-layers","fast-address-interchange"],
    ["The two forward synthetic transforms"])
add("retained-permutations","Resampling with permutations left in the transform","The source and target coordinate permutations stay inside the transform identity and cancel across forward, product and inverse transforms instead of being sorted separately.",["gaussian-resampling","bluestein-chirp","fast-address-interchange"],
    ["Section~\\ref{sec:resampling} retains the"])
add("multiplication-assembly","Assembling the exact product","Chain: radix digits, CRT prime axes, Gaussian resampling and chirps, phase twist, ring convolution; then rescale, round and propagate carries; cost table summed.",["crt-prime-axes","retained-permutations","phase-twist","signed-packing","fast-synthetic-transform","fixed-point-precision"],
    ["propagates carries to"])
add("main-theorem","Integer multiplication in O(n (lg n)^(1−κ)) time","A deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n conjecture in this model.",["multiplication-assembly","nlogn-conjecture"],
    ["Its worst-case running time satisfies"],
    title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
    symbols=[S("n","input length","The number of bits of each integer.","count"),S("\\lg n","logarithm","The larger of the ceiling of log base 2 of n and 1."),S("\\kappa","savings exponent","The constant 2^{-182}.")])
print(json.dumps(dict(target="main-theorem",concepts=C),indent=1),file=open("/home/user/openai-nlogn-wiki/runs/C5/exegenius/tasks/0001-extract.answer.json","w"))
X={
"linear-network":["We construct two fixed linear networks that exchange two banks of values","and restores every auxiliary value."],
"subset-subspace-labels":["Let $\\mathcal T$ be the set of three-element subsets of $[h]$.","=177176569088785861287000000<W_{\\rm b}m."],
"frames":["The sum of the rational ranks of all edge differences is","a common representation on all wires at a gate lets that gate act"],
"recursive-saving":["Choose a rational number $\\tau\\in(0,1)$ with $s/W<m^\\tau$."],
"address-shear":["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization","can be performed with exactly $a$ interchanges of pairs of $b$-digit"],
"fast-address-interchange":["The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every","in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$."],
"butterfly-layer":["The intended operation is the tensor product"],
"fast-butterfly-layers":["\\begin{proposition}[Simultaneous normalized butterfly layer]","whereas separate butterfly"],
"address-fields-layout":["The array has complete address set"],
"synthetic-transforms":["For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.","\\begin{lemma}[Synthetic character cancellation]"],
"fast-synthetic-transform":["\\begin{lemma}[Transform layout and cost]"],
"signed-packing":["\\begin{lemma}[Signed packing and normalized ring multiplication]"],
"cyclic-convolution":["\\begin{proposition}[Convolution from the retained transform layout]"],
"retained-permutations":["\\begin{lemma}[Resampling without executing the two permutations]","P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."],
"gaussian-resampling":["\\begin{lemma}[Tensor interface]"],
"multidimensional-transform":["F_{\\boldsymbol q}:=\\bigotimes_iF_{q_i}."],
"bluestein-chirp":["\\begin{lemma}[Chirp and permutation cancellation]"],
"fixed-point-precision":["The output is a disk"],
"multiplication-assembly":["The source-transform procedures now supply the three transforms needed","Propagate radix-$2^b$ carries in increasing coefficient order."],
"crt-prime-axes":["Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain"],
"main-theorem":["For the cost calculation put $V=Tp=\\Theta(n)$."],
"phase-twist":["\\subsection{Complex convolution by a coefficient twist}"],
}
for c in C:
    for q in X.get(c["id"],[]): c["evidence"].append(dict(source="paper",quote=q))
json.dump(dict(target="main-theorem",concepts=C),open("/home/user/openai-nlogn-wiki/runs/C5/exegenius/tasks/0001-extract.answer.json","w"),indent=1)
