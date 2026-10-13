import json
P="paper"
def c(id,name,gloss,req,ev=(),known=False,title=None,symbols=None,aliases=()):
    d=dict(id=id,name=name,aliases=list(aliases),gloss=gloss,requires=list(req),known=known,evidence=[dict(source=P,quote=q) for q in ev])
    if title: d["title"]=title
    if symbols: d["symbols"]=[dict(symbol=s,name=n,meaning=m,relation=r) for s,n,m,r in symbols]
    return d
C=[]
C.append(c("big-o","Big-O notation","Asymptotic upper bounds on running time.",[],known=True))
C.append(c("polynomials","Polynomials","Sums of coefficients times powers of a variable, and their products.",[],known=True))
C.append(c("complex-numbers","Complex numbers","Numbers a+bi, with modulus and roots of unity e^{2πi/k}.",[],known=True))
C.append(c("turing-machine","Turing machines and tapes","Machines with a finite alphabet, finite states and tapes read and written by heads.",[],known=True))
C.append(c("multitape-model","Fixed multitape Turing machine model","The bit-complexity model: one deterministic machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, where moving data costs time.",["turing-machine","big-o"],
 ["on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes"]))
C.append(c("nlogn-conjecture","Schönhage–Strassen n log n conjecture and history","Schönhage and Strassen's O(n log n log log n) multiplication and their conjecture that n log n is optimal, followed by Fürer and Harvey–van der Hoeven reaching O(n log n).",["multitape-model"],
 ["proposed $n\\log n$ as the optimal order of growth","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper"]))
C.append(c("dft-convolution","Discrete Fourier transform and convolution","The DFT evaluates a sequence at roots of unity; pointwise multiplication of transforms corresponds to convolution of sequences, which is how products are computed.",["complex-numbers","polynomials"],
 ["Splitting the inputs into radix digits reduces multiplication to\nconvolution of short integer coefficients."] ))
C.append(c("radix-digit-reduction","Multiplication as convolution of radix digits","Splitting each n-bit operand into short radix-2^b digits makes the integer product a convolution of digit lists, followed by carry propagation.",["dft-convolution","big-o"],
 ["Splitting the inputs into radix digits reduces multiplication to"]))
C.append(c("hvdh-multiplier","Established O(n log n) multiplier (subroutine)","The Harvey–van der Hoeven O(n log n) integer multiplier, used here only as an ordinary subroutine for short products.",["nlogn-conjecture"],
 ["Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine"]))
C.append(c("cyclic-crt","Chinese-remainder map to prime cyclic axes","Placing the digit list on a product of cyclic axes of distinct prime lengths by a Chinese-remainder address map that preserves convolution.",["radix-digit-reduction"],
 ["placed on a product of\ndistinct prime cyclic axes by a Chinese-remainder map that preserves\nconvolution"]))
C.append(c("gaussian-resampling","Gaussian resampling","Harvey–van der Hoeven's reduction of a Fourier transform of coprime length to a transform with power-of-two axis lengths, using Gaussian-weighted resampling maps that are contractions.",["dft-convolution","cyclic-crt"],
 ["Gaussian\nresampling then expresses each source Fourier transform through a\npower-of-two tensor transform","Gaussian resampling\nconnects these two shapes."]))
C.append(c("resampling-keep-permutations","Resampling with permutations left in the transform","Keeping the source and target coordinate permutations inside the transform identity so they cancel across the forward and inverse transforms instead of being executed as sorts.",["gaussian-resampling","fast-address-interchange"],
 ["Section~\\ref{sec:resampling} retains the\nsource and target coordinate permutations in the transform identity","We retain both permutations in the transform formula and\ncompute that formula directly."]))
C.append(c("bluestein","Bluestein's chirp identity","Rewriting a DFT as a convolution with a chirp (quadratic phase) sequence.",["dft-convolution"],
 ["Bluestein's chirp identity converts the middle transform"]))
C.append(c("polynomial-ring","Polynomial ring modulo y^r + 1","Complex polynomials of degree below r with y^r = -1; multiplying by a power of y is a signed cyclic shift of the coefficient list.",["polynomials","complex-numbers"],
 ["one coordinate\nis stored as the coefficient list of a polynomial modulo $y^r+1$","multiplication by such a root is a signed shift of the coefficient list"],
 title="Polynomial ring modulo $y^r + 1$",symbols=[("r","ring size","A power of two giving the number of complex coefficients in a polynomial of the ring.","count"),("y","ring variable","The indeterminate of the polynomials, satisfying y^r = -1.","direct")]))
C.append(c("coefficient-twist","Coefficient twist from cyclic to negacyclic","Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns cyclic convolution of length r into multiplication modulo y^r+1, with the wrap sign cancelling.",["polynomial-ring","dft-convolution"],
 ["A phase twist changes the last cyclic coordinate into a polynomial\nmodulo $y^r+1$"]))
C.append(c("synthetic-transform","Synthetic polynomial transform","A Nussbaumer-style Fourier transform over the polynomial ring whose roots of unity are powers of y, so multiplications are signed shifts; computed by radix-two butterflies.",["polynomial-ring","dft-convolution","butterfly-h0"],
 ["These are the\nsynthetic polynomial transforms of Nussbaumer and Quandalle"]))
C.append(c("butterfly-h0","Two-point butterfly H₀","The map (u,v) ↦ ((u+v)/2,(u−v)/2) applied coefficientwise; layers of these make up a radix-two transform.",["dft-convolution"],
 ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)"]))
C.append(c("signed-packing","Signed packing (Kronecker substitution)","Multiplying ring polynomials exactly by packing their integer coefficients, including negative ones, into long integers and calling the integer multiplier.",["polynomial-ring","hvdh-multiplier"],
 ["The\nreduction is a signed form of Kronecker substitution"]))
C.append(c("ring-convolution","Exact normalized convolution over the polynomial ring","Convolution on the remaining axes via forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same frequency order.",["synthetic-transform","signed-packing","coefficient-twist"],
 ["The two forward synthetic transforms\nretain the same frequency order through their pointwise product"]))
C.append(c("stream-operations","Tape streams, array order and elementary scans","Arrays stored in row-major address order on tapes, with linear-time scans, controlled shifts and affine updates of later fields from earlier ones.",["multitape-model"],
 ["\\section{The machine model and elementary streams}"]))
C.append(c("linear-network-frames","Linear network with roles and frames","A fixed linear network exchanging two banks of values with signs and restoring auxiliary wires; applied to arrays by giving each wire an invertible frame operator so that intermediate frames cancel and only an endpoint operator remains.",["stream-operations","polynomials"],
 ["A wire's fixed place in the network\nis called its role.","the common frame commutes with the gate","Thus the\nintermediate frames cancel"]))
C.append(c("subset-intersection-labels","Subset-intersection subspace labels","Nested subspaces spanned by tensor products of three-element-subset indicator vectors (Frankl–Wilson/Alon style), giving a network whose total edge rank s is less than W·m.",["linear-network-frames"],
 ["The construction uses\nthree-element subsets","The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$."]))
C.append(c("recursive-saving","Recursive power saving from rank deficit","A call at parameter m·f uses s < W·m calls at parameter f on volume V/W, so normalized cost grows by factor s/W < m per level, giving cost V·(parameter)^{τ} with τ < 1.",["subset-intersection-labels","big-o"],
 ["This strict inequality\nis the source of the power saving."]))
C.append(c("lower-triangular-factorization","Lower triangular (Bruhat-type) factorization and matrix shear","Every rational matrix of rank a factors as E₁ΠE₂ with E_i lower triangular and Π a partial permutation with a ones, so a shear costs only a smaller interchanges plus linear-time updates.",["stream-operations"],
 ["has a factorization\n\\[\n A=E_1\\Pi E_2,","Every rational $m\\times m$ matrix $A$ of rank $a$"]))
C.append(c("fast-address-interchange","Fast interchange of address chunks","Interchanging two contiguous address fields of u bits in a Cartesian-product array, by XOR/shear combinations through the bit network, at cost O(V u^τ) for fixed τ < 1.",["recursive-saving","lower-triangular-factorization"],
 ["The first procedure interchanges two disjoint contiguous address fields\nof $u$ bits","Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."],
 title="Fast address interchange at cost $O(Vu^\\tau)$",symbols=[("V","stored bit volume","The number of stored bits in the array.","count"),("u","field width","The number of bits in each of the two address fields being interchanged.","count"),("\\tau","saving exponent","A fixed constant below 1 giving the power of u in the cost.","direct")]))
C.append(c("simultaneous-butterfly-layer","Simultaneous butterfly layer","Applying H₀ at the same bit position of up to d address chunks at once on records of complex fixed-point polynomials, using the complex phase network, at cost O(V d^λ′).",["recursive-saving","butterfly-h0","fast-address-interchange","fixed-point-precision"],
 ["The second procedure applies","the cost is $O(Vd^{\\lambda'})$ for a\nfixed $\\lambda'<1$"],
 title="Simultaneous butterfly layer at cost $O(Vd^{\\lambda'})$",symbols=[("V","stored bit volume","The number of stored bits in the numerical arrays.","count"),("d","chunk count","The number of equal-width address chunks in which the same bit position is selected.","count"),("\\lambda'","layer exponent","A fixed constant below 1 giving the power of d in the cost.","direct")]))
C.append(c("fixed-point-precision","Fixed-point dyadic precision and exact recovery","Coefficients stored as p-bit grid values on the unit disk, with truncation errors tracked through contractions so the final integer coefficient error is below 1/2.",["complex-numbers"],
 ["A single\ntruncation follows the completed contractive layer."]))
C.append(c("parameter-choice","Fixed rational parameter choice","The conservative constants (τ, λ, λ′, ε, δ, κ = 2^{-182}) chosen compatibly so all terms in the cost table fit the main bound.",["fast-address-interchange","simultaneous-butterfly-layer","resampling-keep-permutations","ring-convolution","fixed-point-precision"],
 ["These constants are deliberately conservative; no optimization is claimed."]))
C.append(c("multiplication-algorithm","Complete multiplication algorithm and cost","Digits → CRT address map → forward synthetic Gaussian-resampled transforms of both operands → pointwise product → inverse transform → rescale, round and carry to get the exact product.",["radix-digit-reduction","cyclic-crt","resampling-keep-permutations","bluestein","ring-convolution","parameter-choice"],
 ["The source-transform procedures now supply the three transforms needed\nfor the radix-digit convolution."]))
C.append(c("main-theorem","Multiplication in O(n (lg n)^{1-κ}) time","The deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time with κ = 2^{-182}, disproving the n log n optimality conjecture in this model.",["multiplication-algorithm","nlogn-conjecture"],
 ["T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right),","disproves the $n\\log n$ optimality\nconjecture of Sch\\\"onhage and Strassen in this model"],
 title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",symbols=[("n","operand length","The number of bits in each input integer.","count"),("\\kappa","saving exponent","The fixed positive constant 2^{-182} giving the power saving in the logarithmic factor.","direct")],aliases=["Theorem 1"]))

EX={
"nlogn-conjecture":["Sch\\\"onhage and Strassen conjectured $n\\log n$ as the optimal order of\nmultiplication cost"],
"signed-packing":["The reduction is a signed form of Kronecker substitution","Set $B_0=2^{4p}$"],
"hh-nlogn-multiplier":["with cost\n$O(N\\log(2N))$ on $N$-bit inputs.  This is an independent subroutine."],
"poly-ring-mod-yr1":["$\\mathcal R_r=\\mathbb C[y]/(y^r+1)$"],
"synthetic-transforms":["For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.","\\begin{lemma}[Synthetic character cancellation]"],
"exact-ring-products":["\\begin{lemma}[Signed packing and normalized ring multiplication]","\\begin{proposition}[Convolution from the retained transform layout]"],
"crt-prime-axes":["The transform lengths needed for the integer product are pairwise coprime,\nwhereas the synthetic transforms use powers of two."],
"gaussian-resampling":["\\begin{lemma}[Resampling without executing the two permutations]","Its usual implementation sorts twice on each\ncoordinate. We retain both permutations in the transform formula"],
"bluestein-chirp":["\\begin{lemma}[Chirp and permutation cancellation]","The chirp identity below performs the frequency change\nin $Q$ without applying $Q$ as a separate permutation of the array."],
"phase-twist":["Untwisting therefore recovers the cyclic coefficient with the correct\nsign."],
"linear-networks-frames":["\\begin{proposition}\\label{prop:complex-motif-interface}".replace("\\begin{proposition}\\label{prop:complex-motif-interface}","Its phase-frame difference\n$\\mathcal C_V\\mathcal C_U^{-1}$ is a product of one translation\nkernel")],
"subset-network-construction":["Let $\\mathcal T$ be the set of three-element subsets of $[h]$."],
"recursive-saving":["Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width."],
"restoring-auxiliary":["We call all these auxiliary wires\n\\emph{scratch wires}; their initial values may be arbitrary."],
"address-shear":["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"],
"address-interchange":["\\begin{lemma}[Arbitrary-width interchange]","The chunks can be interchanged in $O(Ve^\\tau)$ time"],
"butterfly-layer":["\\begin{proposition}[Simultaneous normalized butterfly layer]","The intended operation is the tensor product\nof $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits"],
"fixed-point-precision":["Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this\nsubsection."],
"transform-layout":["\\begin{lemma}[Transform layout and cost]","We also specify where each frequency entry\nis stored"],
"main-algorithm":["Table~\\ref{tab:costs} lists costs after division\nby $V$","Read each stored operand backward from\nits least significant end in groups of $b$ bits."],
"radix-digit-reduction":["Propagate radix-$2^b$ carries in increasing coefficient order."],
"stream-operations":["\\begin{lemma}[Elementary stream operations]"],
"phase-twist ":[],
}
for cc in C:
    for q in EX.get(cc["id"],[]):
        cc["evidence"].append(dict(source=P,quote=q))
C=[x for x in C]
json.dump(dict(target="main-theorem",concepts=C),open("/home/user/openai-nlogn-wiki/runs/B4/exegenius/tasks/0001-extract.answer.json","w"),indent=1)
