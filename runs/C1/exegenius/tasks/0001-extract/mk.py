import json
P="paper"
def c(id,name,gloss,req,quotes=(),known=False,title=None,symbols=None):
    d=dict(id=id,name=name,aliases=[],gloss=gloss,requires=req,known=known,evidence=[{"source":P,"quote":q} for q in quotes])
    if title:
        d["title"]=title; d["symbols"]=symbols
    return d
C=[
c("big-o","Big-O notation","Asymptotic upper bound on growth.",[],known=True),
c("polynomials","Polynomials","Sums of powers of a variable with coefficients.",[],known=True),
c("complex-numbers","Complex numbers","Numbers a+bi with i²=−1.",[],known=True),
c("multitape-tm","Multitape Turing machine","A deterministic Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes.",[],known=True),
c("nlogn-conjecture","Schönhage–Strassen n log n conjecture","The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers.",["big-o","multitape-tm"],["proposed $n\\log n$ as the optimal order of growth"]),
c("dft-convolution","Convolution and discrete Fourier transform","Convolution of coefficient lists is computed by transforming, multiplying pointwise and inverting the transform, using roots of unity.",["polynomials","complex-numbers"],["Splitting the inputs into radix digits reduces multiplication to"]),
c("radix-digit-convolution","Multiplication as digit convolution","Splitting each input into radix digits turns the integer product into a convolution of short integer coefficients, followed by carry propagation.",["dft-convolution"],["Splitting the inputs into radix digits reduces multiplication to"]),
c("tape-streams","Elementary tape streams and scans","Array layouts on tapes with address fields, scans, controlled shifts and fixed rational scalings, each costing linear time in stored bit volume.",["multitape-tm","big-o"],["\\section{The machine model and elementary streams}"]),
c("poly-ring-y-r-1","Polynomial ring modulo y^r + 1","Polynomials in y with complex coefficients modulo y^r+1, where powers of y act as roots of unity and multiplication by them is a signed shift.",["polynomials","complex-numbers"],["is stored as the coefficient list of a polynomial modulo $y^r+1$"],title="Polynomial ring modulo $y^r+1$",symbols=[
 {"symbol":"y","name":"ring variable","meaning":"The indeterminate of the polynomials, whose powers serve as roots of unity.","relation":"direct"},
 {"symbol":"r","name":"coefficient count","meaning":"The number of complex coefficients in a polynomial of the ring, a power of two.","relation":"count"}]),
c("synthetic-transforms","Synthetic polynomial transforms","Fourier-type transforms over the polynomial ring where roots of unity are powers of y, so root multiplications are signed shifts and the work is butterflies, shifts and address rearrangements.",["dft-convolution","poly-ring-y-r-1"],["synthetic polynomial transforms of Nussbaumer and Quandalle"]),
c("gaussian-resampling","Gaussian resampling","The Harvey–van der Hoeven identity expressing a transform of arbitrary axis length through a transform with power-of-two axis lengths.",["dft-convolution"],["power-of-two tensor transform"]),
c("crt-address-map","Chinese-remainder address map","A map placing the coefficient list on a product of distinct prime cyclic axes that preserves convolution.",["dft-convolution","radix-digit-convolution"],["by a Chinese-remainder map that preserves"]),
c("bluestein-chirp","Bluestein chirp identity","Rewrites a transform as a normalized cyclic convolution via chirp phase factors.",["dft-convolution"],["Bluestein's chirp identity converts the middle transform"]),
c("signed-packing","Signed packing (Kronecker substitution)","Packing polynomial coefficients into one long integer with signs so ring products are computed by an ordinary O(n log n) integer multiplier.",["poly-ring-y-r-1","radix-digit-convolution"],["is a form of Kronecker substitution"]),
c("fixed-point-precision","Fixed-point precision and exact recovery","Complex fixed-point coefficients with dyadic intermediates, one truncation, and an error bound below 1/2 that allows exact rounding and carry propagation.",["complex-numbers","radix-digit-convolution"],["coefficient error is strictly below $1/2$"]),
c("gate-frames","Linear networks with frames and roles","A fixed linear network exchanging banks of values; roles are wire positions and an invertible frame operator per gate makes intermediate representations cancel.",["tape-streams"],["We call $D_v$ its frame"]),
c("finite-network-subspaces","Finite networks with rank saving","Networks built from three-element subsets with nested subspaces so the number s of smaller calls satisfies s<Wm.",["gate-frames"],["The decisive property is that the total"]),
c("recursive-power-saving","Recursive power saving","Recursive calls at parameter mf use s<Wm calls at parameter f on volume V/W each, giving cost per volume growth with an exponent below 1.",["finite-network-subspaces","big-o"],["is the source of the power saving"]),
c("address-interchange","Fast interchange of address chunks","Interchanges two address fields of u bits in cost O(V u^τ), τ<1, through XOR combinations whose final effect is an exact permutation.",["recursive-power-saving","tape-streams"],["The first procedure interchanges two disjoint contiguous address fields"]),
c("fast-butterfly-layers","Simultaneous butterfly layers","Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected address bits of d chunks at cost O(V d^λ'), λ'<1.",["recursive-power-saving","fixed-point-precision","synthetic-transforms"],["The second procedure applies"]),
c("main-theorem","Integer multiplication in O(n (lg n)^(1−κ)) time","A fixed deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)), κ=2^−182, disproving the n log n optimality conjecture in that model.",["nlogn-conjecture","address-interchange","fast-butterfly-layers","gaussian-resampling","crt-address-map","bluestein-chirp","signed-packing","fixed-point-precision","synthetic-transforms"],["Its worst-case running time satisfies"],title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",symbols=[
 {"symbol":"n","name":"input length","meaning":"The number of bits of each integer factor.","relation":"count"},
 {"symbol":"\\kappa","name":"power saving","meaning":"The constant 2^{-182} giving the exponent saving in the logarithmic factor.","relation":"direct"}]),
]
json.dump({"target":"main-theorem","concepts":C},open("exegenius/tasks/0001-extract.answer.json","w"),indent=1,ensure_ascii=False)
extra={
"poly-ring-y-r-1":"\\mathcal R_r=\\mathbb C[y]/(y^r+1)",
"synthetic-transforms":"\\begin{lemma}[Synthetic character cancellation]",
"gaussian-resampling":"\\begin{lemma}[Resampling without executing the two permutations]",
"crt-address-map":"The transform lengths needed for the integer product are pairwise coprime,",
"bluestein-chirp":"\\begin{lemma}[Chirp and permutation cancellation]",
"signed-packing":"\\begin{lemma}[Signed packing and normalized ring multiplication]",
"fixed-point-precision":"Address permutations and intermediate dyadic arithmetic are",
"gate-frames":"We call the name of a wire its",
"finite-network-subspaces":"Let $\\mathcal T$ be the set of three-element subsets of $[h]$.",
"recursive-power-saving":"the resulting recurrence saves a power of the chunk width.",
"address-interchange":"\\begin{proposition}[Power-width interchange with rows]",
"fast-butterfly-layers":"\\begin{proposition}[Simultaneous normalized butterfly layer]",
"radix-digit-convolution":"The source-transform procedures now supply the three transforms needed",
"tape-streams":"\\begin{lemma}[Controlled shifts and fixed rational scalings]",
"dft-convolution":"\\begin{lemma}[Convolution from the retained transform layout]" ,
"main-theorem":"For the cost calculation put $V=Tp=\\Theta(n)$.",
}
extra["dft-convolution"]="\\begin{proposition}[Convolution from the retained transform layout]"
d=json.load(open("exegenius/tasks/0001-extract.answer.json"))
for k in d["concepts"]:
    if k["id"] in extra: k["evidence"].append({"source":P,"quote":extra[k["id"]]})
json.dump(d,open("exegenius/tasks/0001-extract.answer.json","w"),indent=1,ensure_ascii=False)
