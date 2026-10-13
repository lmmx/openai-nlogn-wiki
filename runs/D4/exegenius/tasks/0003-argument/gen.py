import json
S=open('sources/paper.tex').read()
def Q(q):
    assert q in S, q
    return {"source":"paper","quote":q}
def inf(id,claim,q,page=None,frm=(),deferred=False,salient=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":Q(q),"from":list(frm)}
    if page:n["page"]=page
    if deferred:n["deferred"]=True
    if salient:n["salient"]=salient
    return n
def show(id,claim,method,mot,src,children,page=None,frm=(),quote=None,adds=None,salient=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,
       "motivation":{"text":mot,"source":src,"quote":Q(quote) if quote else None},
       "children":children,"from":list(frm)}
    if page:n["page"]=page
    if adds:n["adds"]=adds
    if salient:n["salient"]=salient
    return n
def B(sym,name,meaning,rel="count"):
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}

R31=inf("S1.1","A fixed linear network exchanges two banks of values with signs, frames $D_v$ change representation along edges so that intermediate frames cancel, and auxiliary values are restored.",
 "assign an invertible $R$-linear operator","linear-network-frames",
 ["linear-algebra-over-the-rationals","matrix-and-block-notation"])
R32=inf("S1.2","For the bit procedure the endpoint operator is the address shear $(H,D)\\mapsto(H+D,D)$ over a residue ring, implemented through lower-triangular factorization.",
 "can be performed with exactly $a$ interchanges of pairs of $b$-digit","address-shear",
 ["linear-network-frames","gaussian-elimination-and-the-general-linear-group-over-f2","modular-arithmetic","linear-algebra-over-the-rationals"])
R33=inf("S1.3","A finite network with nested subspaces of an $m$-dimensional space attached to its gates, built from three-element subset intersection counts, has total number $s$ of smaller calls with $s<Wm$.",
 "=177176569088785861287000000<W_{\\rm b}m.","subset-network",
 ["linear-network-frames","binomial-coefficients-and-basic-counting","linear-algebra-over-the-rationals"])
R34=inf("S1.4","Applying the network at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, and $s<Wm$ makes the cost per unit volume grow like a power of the parameter below 1.",
 "\\qquad 0<\\tau=\\sigma<1.","recursive-saving",
 ["subset-network","linear-network-frames","recurrences-and-divide-and-conquer"],
 salient="The saving needs only the strict inequality $s<Wm$: a barely smaller number of subcalls than the naive $Wm$ compounds into a power below 1 at every recursion level.")
R35=inf("S1.5","Two disjoint contiguous address fields of $u$ bits in an array with a complete Cartesian product of addresses can be interchanged in time $O(Vu^{\\tau})$ for a fixed $\\tau<1$, ending as an exact permutation.",
 "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.","fast-address-interchange",
 ["address-shear","recursive-saving","fixed-tape-model","bitwise-xor"])
R36a=inf("S1.6.1","Intermediate values of a layer are exact Gaussian dyadics (real and imaginary parts with power-of-two denominators) and a single truncation follows the completed contractive layer.",
 "are exact Gaussian dyadic operations.  Thus, once the physical binary","fixed-point-dyadics",["complex-numbers","binary-representation-of-integers","basic-real-error-bounds"])
R36=show("S1.6","The butterfly $H_0$ can be applied simultaneously on the same bit position in at most $d$ address chunks at cost $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$.",
 "run the recursive linear-network construction on a numerical layer, with phase frames, exact dyadic intermediates and one truncation",
 "The numerical layer arises from the same kind of fixed network as the address interchange, so the same strict saving applies once phase frames and exact dyadic arithmetic keep every edge a smaller call of the same procedure.",
 "recoverable",[R36a],page="fast-butterfly-layers",
 frm=["butterfly","synthetic-transforms","recursive-saving","fast-address-interchange","linear-network-frames"])
# the cost bound child quote placed first
R36b=inf("S1.6.0","On the layouts used, selecting one bit in each of at most $d$ equal-width chunks, the layer costs $O(Vd^{\\lambda'})$.",
 "coefficient order, and component format in $O(Vd^{\\lambda'})$ time,",None,[])
R36["children"].append(R36b)

R3=show("S1","Two tape procedures, fast address interchange and simultaneous fast butterfly layers, cut the cost of address rearrangement and of transform layers by a power of the logarithm.",
 "derive both from a fixed linear network with a strict deficit in the number of smaller calls and recurse",
 "A power saving needs a recursion whose subcalls cost slightly less in total than the work they replace; the network provides exactly this strict deficit.",
 "explicit",[R31,R33,R34,R32,R35,R36],quote="is the source of the power saving.",
 frm=["fixed-tape-model"],
 adds=[B("V","stored volume","the number of stored bits in the array being processed"),
       B("W","number of roles","the number of roles (wires) of the fixed linear network that are distributed among streams"),
       B("m","space dimension","the dimension of the fixed space whose subspaces are attached to gates"),
       B("s","number of smaller calls","the total number of smaller calls of the procedure the network uses")])
# fix: R3 quote and R34 quote duplicate => fine (explicit motivation quote need not be in DFS order check)

R41=inf("S2.1","Splitting each $n$-bit integer into radix digits turns the product into a convolution of short integer coefficients, followed by carry propagation.",
 "Thus convolution modulo $x^S-1$ has no nonzero wraparound.","mult-to-convolution",
 ["convolution-dft","schoolbook-integer-multiplication-and-carries","polynomials"])
R42=inf("S2.2","The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.",
 "$\\Phi$ is an isomorphism and preserves cyclic convolution.","crt-prime-axes",
 ["mult-to-convolution","prime-numbers-and-coprimality","modular-arithmetic"])
R43=inf("S2.3","Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.",
 "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and","gaussian-resampling",
 ["convolution-dft","mult-to-convolution"],deferred=True)
R44=inf("S2.4","Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution.",
 "\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}.","bluestein-chirp",
 ["convolution-dft","roots-of-unity-and-euler-s-formula"],deferred=True)
R45=inf("S2.5","A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$, whose negative wrap gives the original cyclic wrap after untwisting.",
 "Untwisting therefore recovers the cyclic coefficient with the correct","phase-twist",
 ["ring-mod-y-r-plus-1","roots-of-unity-and-euler-s-formula"])
R461=inf("S2.6.1","The two forward synthetic transforms retain the same frequency order through the pointwise product and the opposite transform consumes that order.",
 "The forward procedure may retain its output layout for a","transform-layout",
 ["synthetic-transforms","fast-butterfly-layers","fast-address-interchange"],deferred=True)
R462=inf("S2.6.2","The ring products in the transformed domain are computed by signed packing and the established $O(n\\log n)$ multiplier used as an ordinary subroutine.",
 "One can compute the exact Gaussian integer","polynomial-products",
 ["signed-packing","ring-mod-y-r-plus-1","nlogn-conjecture","fixed-tape-model"],deferred=True)
R46=show("S2.6","Convolution over the remaining axes is computed over $\\mathbb{C}[y]/(y^r+1)$ by synthetic transforms.",
 "evaluate with synthetic polynomial transforms using powers of $y$ as roots of unity",
 "In the ring modulo $y^r+1$ powers of $y$ are roots of unity and multiplying by one is a signed shift, so the transform needs only rearrangements, shifts and butterflies.",
 "explicit",[R461,R462],page="synthetic-transforms",quote="serve as roots of unity in the remaining axes",
 frm=["ring-mod-y-r-plus-1","butterfly","convolution-dft","roots-of-unity-and-euler-s-formula","fast-fourier-transform-idea"])
R47=inf("S2.7","The source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform, so no full sorts are executed.",
 "=\\frac{u*v}{S^2}.","permutation-cancellation",
 ["gaussian-resampling","bluestein-chirp","transform-layout","sorting-and-permutations"],deferred=True,
 salient="The permutations that resampling introduces are never executed: they appear in the forward and inverse transforms with opposite roles and cancel.")
R48=inf("S2.8","Known normalizations and digit scales are removed, the coefficient error is below $1/2$, and carries yield the exact binary product.",
 "that value the unique correct coefficient.","exact-recovery",
 ["mult-to-convolution","basic-real-error-bounds","schoolbook-integer-multiplication-and-carries"])
R4=show("S2","The product of two $n$-bit integers is computed exactly by the pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery.",
 "reduce multiplication through successive changes of problem to a convolution over the polynomial ring and then undo the reductions",
 "Each arrow of the pipeline changes the problem or its representation so that the final convolution has power-of-two axes over $\\mathbb{C}[y]/(y^r+1)$, where the fast tape procedures apply; known rescaling and rounding then recover the integer product.",
 "recoverable",[R41,R42,R43,R44,R45,R46,R47,R48],page="multiplication-algorithm",
 frm=["convolution-dft","fixed-tape-model"])
R5=inf("S3","With a compatible choice of rational parameters every term of the cost table fits the bound $O(n(\\lg n)^{1-\\kappa})$.",
 "$O(n(\\lg n)^{1-\\kappa})$ for every input length and produces precisely",None,[])
R2=inf("S0.2","The machine model has one fixed finite alphabet and a fixed finite number of one-dimensional tapes; moving one digit in a fixed radix takes a bounded number of scans, but interchanging fields with growing numbers of digits does not.",
 "takes $O(V)$ steps on a fixed number of one-dimensional tapes:","fixed-tape-model",["turing-tapes","big-o"],deferred=True)
R1=inf("S0.1","Schönhage and Strassen gave $O(n\\log n\\log\\log n)$ and proposed $n\\log n$ as optimal; Harvey and van der Hoeven reached $O(n\\log n)$.",
 "Sch\\\"onhage and Strassen proved in 1971 that two $n$-bit integers can","nlogn-conjecture",["big-o"])
root=show("S0","A deterministic fixed-tape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture in this model.",
 "reduce multiplication to a ring convolution whose transforms are accelerated by two fast tape procedures, then account for the cost",
 "Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$, so beating it needs savings in both data movement and arithmetic.",
 "explicit",[R1,R2,R3,R4,R5],page="main-theorem",quote="We therefore need savings in both movement and arithmetic.",
 frm=["big-o","turing-tapes","exponentials-logarithms-and-iterated-logarithm-bounds"],
 salient="The saving is a genuine power $(\\lg n)^{-\\kappa}$ of the logarithm, with an astronomically small $\\kappa=2^{-182}$, rather than a $\\log\\log$ or $\\log^*$ factor.")
json.dump({"root":root},open('exegenius/tasks/0003-argument.answer.json','w'),indent=1,ensure_ascii=False)
