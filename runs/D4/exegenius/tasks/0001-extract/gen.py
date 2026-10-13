import json
def E(q): return [{"source":"paper","quote":q}]
C=[]
def add(id,name,gloss,req,ev=None,known=False,title=None,symbols=None,aliases=None):
    d={"id":id,"name":name,"aliases":aliases or [],"gloss":gloss,"requires":[] if known else req,"known":known,"evidence":[] if known else E(ev)}
    if title: d["title"]=title; d["symbols"]=symbols
    C.append(d)
for i,n,g in [("big-o","Big-O notation","Asymptotic upper bounds on running time."),
 ("polynomials","Polynomials","Sums of coefficients times powers of a variable, with addition and multiplication."),
 ("complex-numbers","Complex numbers","Numbers a+bi with real and imaginary parts, including roots of unity."),
 ("turing-tapes","Multitape Turing machines","Machines with finitely many tapes, heads, and a finite alphabet, one step reading and writing each tape.")]:
    add(i,n,g,[],known=True)
add("fixed-tape-model","Fixed-tape machine model and stream scans","The cost model: one fixed alphabet and a fixed number of one-dimensional tapes, where moving data by a bounded number of scans is cheap but permuting growing fields is not.",["turing-tapes","big-o"],"A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.")
add("convolution-dft","Convolution and the discrete Fourier transform","Convolution multiplies coefficient lists as polynomials; a Fourier transform at roots of unity turns it into pointwise products.",["polynomials","complex-numbers"],"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.")
add("mult-to-convolution","Integer multiplication as digit convolution","Splitting each n-bit integer into radix digits turns the product into a convolution of short integer coefficients, followed by carry propagation.",["convolution-dft"],"Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.")
add("nlogn-conjecture","History and the n log n conjecture","Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).",["big-o","fixed-tape-model","mult-to-convolution"],"Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper bound~\\cite{HarveyHoeven2021}.")
add("ring-mod-y-r-plus-1","Polynomial ring modulo y^r + 1","Complex polynomials in y reduced with y^r = −1, where powers of y act as roots of unity and multiplying by them is a signed shift.",["polynomials","complex-numbers"],"one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two",
  title="Polynomial ring modulo $y^r + 1$",symbols=[
  {"symbol":"y","name":"ring variable","meaning":"The polynomial variable whose powers serve as roots of unity.","relation":"direct"},
  {"symbol":"r","name":"ring degree","meaning":"The power-of-two number of coefficients of a ring element, with y^r equal to −1.","relation":"count"}])
add("synthetic-transforms","Synthetic polynomial transforms","Fourier-type transforms using powers of y in the ring as roots of unity, built from address rearrangements, signed shifts and butterflies.",["ring-mod-y-r-plus-1","convolution-dft","butterfly"],"These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer")
add("butterfly","Two-point butterfly","The operation H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of values, the building block of transform layers.",["complex-numbers"],"\\[\n H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)\n\\]" if False else "applies\n\\[\n H_0(u,v)")
add("gaussian-resampling","Gaussian resampling","The Harvey–van der Hoeven reduction replacing arbitrary-length Fourier transforms by multidimensional transforms with power-of-two axis lengths.",["convolution-dft"],"it replaces the Fourier transforms needed for\nthis convolution by multidimensional transforms whose axis lengths are\npowers of two")
add("crt-prime-axes","Chinese-remainder map to prime cyclic axes","Placing the radix-digit coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.",["mult-to-convolution","fixed-tape-model"],"placed on a product of\ndistinct prime cyclic axes by a Chinese-remainder map that preserves\nconvolution")
add("bluestein-chirp","Bluestein chirp conversion","Bluestein's chirp identity rewrites a transform of arbitrary length as a cyclic convolution.",["convolution-dft"],"Bluestein's chirp identity converts the middle transform")
add("phase-twist","Coefficient twist to the negative wrap","Multiplying coefficients by phases turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap reproduces the cyclic wrap after untwisting.",["bluestein-chirp","ring-mod-y-r-plus-1"],"A phase twist changes the last cyclic coordinate into a polynomial\nmodulo $y^r+1$")
add("signed-packing","Signed packing (Kronecker substitution)","Packing signed polynomial coefficients into one integer so that a polynomial product is computed by an ordinary integer multiplication.",["mult-to-convolution","polynomials"],"Signed coefficient\npacking is a form of Kronecker substitution")
add("polynomial-products","Exact normalized polynomial products","Ring products in the transformed domain computed by signed packing and the established O(n log n) multiplier used as an ordinary subroutine.",["signed-packing","ring-mod-y-r-plus-1","nlogn-conjecture"],"Their polynomial products\nuse signed packing and the established $O(n\\log n)$ multiplier as an\nordinary subroutine.")
add("fixed-point-dyadics","Fixed-point complex coefficients and exact dyadics","Records hold complex fixed-point coefficients; layers are exact Gaussian dyadics with power-of-two denominators and a single truncation afterwards.",["complex-numbers","butterfly"],"Intermediate values are exact Gaussian dyadics")
add("linear-network-frames","Linear networks with frames and restored auxiliaries","A fixed linear network exchanges two banks of roles with signs; frames D_v change array representation along edges, intermediate frames cancel, and auxiliary values are restored.",["fixed-tape-model"],"Each procedure arises from its own fixed linear network that exchanges two\nbanks of values, with prescribed signs, and restores every auxiliary\nvalue.")
add("subset-network","Finite network from three-element subsets","A finite network with nested subspaces of an m-dimensional space attached to gates, built from three-element subset intersection counts, with total smaller calls s < Wm.",["linear-network-frames"],"The construction uses\nthree-element subsets: gather and scatter create coefficients depending\non intersection size, and auxiliary wires cancel the unwanted\ncoefficients.")
add("recursive-saving","Recursive power saving","Applying the network at parameter mf uses s calls at parameter f on streams of volume V/W, and s < Wm makes the per-volume cost grow like a power below 1.",["subset-network","big-o"],"This strict inequality\nis the source of the power saving.")
add("address-shear","Address shear and triangular factorization","The endpoint operator (H,D) ↦ (H+D,D) on address fields, implemented through lower-triangular factors with rank reduction.",["linear-network-frames"],"that operator is an address shear")if False else None
add("address-shear","Address shear and triangular factorization","The endpoint operator (H,D) ↦ (H+D,D) on address fields over a residue ring, implemented via lower-triangular factorization.",["linear-network-frames"],"are\nupdated by $(H,D)\\mapsto(H+D,D)$")
add("fast-address-interchange","Fast interchange of address chunks","Interchanging two disjoint contiguous address fields of u bits at cost O(V u^τ), τ<1, via XOR combinations that end as an exact permutation.",["recursive-saving","address-shear","fixed-tape-model"],"The first procedure interchanges two disjoint contiguous address fields")
add("fast-butterfly-layers","Simultaneous fast butterfly layers","Applying H₀ on the same selected bit of up to d address chunks at once at cost O(V d^λ′), λ′<1, with phase frames and a single truncation.",["recursive-saving","butterfly","fixed-point-dyadics","fast-address-interchange"],"The second procedure applies")
add("transform-layout","Synthetic transform layout with retained frequency order","Layout on which the parallel layers apply; forward transforms keep the same frequency order through the pointwise product and the inverse consumes it.",["synthetic-transforms","fast-butterfly-layers","fast-address-interchange"],"The two forward synthetic transforms\nretain the same frequency order through their pointwise product")
add("permutation-cancellation","Retained permutations cancelling","Source and target coordinate permutations are kept inside the transform identity and cancel across the forward transforms, product and inverse, avoiding full sorts.",["gaussian-resampling","transform-layout"],"so they need not be executed as separate full sorts")
add("exact-recovery","Rounding, rescaling and carry propagation","Known normalizations and digit scales are removed, coefficient error is shown below 1/2, and carries yield the exact binary product.",["fixed-point-dyadics","mult-to-convolution"],"proves that the recovered\ncoefficient error is strictly below $1/2$")
add("multiplication-algorithm","The assembled multiplication algorithm","Pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery.",["crt-prime-axes","gaussian-resampling","bluestein-chirp","phase-twist","polynomial-products","permutation-cancellation","transform-layout","exact-recovery"],"Figure~\\ref{fig:multiplication-flow} summarizes these reductions.")
add("main-theorem","Integer multiplication below n log n","A deterministic fixed-tape Turing machine multiplies n-bit integers in O(n (lg n)^(1−κ)) time with κ=2^(−182), disproving the n log n optimality conjecture in this model.",["multiplication-algorithm","nlogn-conjecture","big-o"],"We give a deterministic algorithm that multiplies two $n$-bit integers\nin $O(n(\\lg n)^{1-\\kappa})$ worst-case time")

X={
"fixed-tape-model":["Each of the following operations on an array of\nvolume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:"],
"convolution-dft":["F_t^+F_t^-=t^{-1}I"],
"mult-to-convolution":["Propagate radix-$2^b$ carries in increasing coefficient order."],
"ring-mod-y-r-plus-1":["Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes\nthe summands and multiplies their sum by\n$y^{rj_0}=-1$."],
"synthetic-transforms":["\\begin{lemma}[Synthetic character cancellation]"],
"butterfly":["\\begin{proposition}[Simultaneous normalized butterfly layer]"],
"gaussian-resampling":["\\begin{lemma}[Resampling without executing the two permutations]","P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."],
"crt-prime-axes":["CRT and axis layouts"],
"bluestein-chirp":["\\begin{lemma}[Chirp and permutation cancellation]"],
"signed-packing":["\\begin{lemma}[Signed packing and normalized ring multiplication]"],
"polynomial-products":["\\begin{proposition}[Convolution from the retained transform layout]"],
"fixed-point-dyadics":["Address permutations and intermediate dyadic arithmetic are\nexact."],
"linear-network-frames":["\\begin{lemma}\\label{lem:scalar-motifs}","and restores every auxiliary value."],
"subset-network":["\\begin{lemma}\\label{lem:motif-residuals}","\\begin{proposition}\\label{prop:bit-motif-interface}","\\begin{proposition}\\label{prop:complex-motif-interface}"],
"recursive-saving":["Choose a rational number $\\tau\\in(0,1)$ with $s/W<m^\\tau$."],
"address-shear":["\\begin{lemma}[Lower triangular factorization]","\\begin{lemma}[The cost of a rational matrix shear]"],
"fast-address-interchange":["\\begin{proposition}[Power-width interchange with rows]","\\begin{lemma}[Arbitrary-width interchange]"],
"fast-butterfly-layers":["\\begin{lemma}[Packed selected-bit addition on one rectangle]","\\begin{definition}[Grouped packed stream]"],
"transform-layout":["\\begin{lemma}[Transform layout and cost]"],
"permutation-cancellation":["\\begin{lemma}[Tensor interface]"],
"exact-recovery":["Round the represented real\nvalues to the nearest integers."],
"multiplication-algorithm":["Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain\nsource arrays $u,v$."],
"main-theorem":["\\kappa=2^{-182}","Chunk exchanges for transform layout"],
}
for c in C:
    for q in X.get(c["id"],[]): c["evidence"].append({"source":"paper","quote":q})
C=[c for c in C if c]
json.dump({"target":"main-theorem","concepts":C},open("/home/user/openai-nlogn-wiki/runs/D4/exegenius/tasks/0001-extract.answer.json","w"),indent=1)
