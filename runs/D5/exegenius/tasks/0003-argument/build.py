import json
src=open('/home/user/openai-nlogn-wiki/runs/D5/sources/paper.tex').read()
pos=[0]
def inf(id,claim,q,page=None,frm=(),salient=None):
    i=src.find(q,pos[0]); assert i>=0,(id,q)
    pos[0]=i+len(q)
    n={"id":id,"intention":"infer","claim":claim,"quote":{"source":"paper","quote":q},"from":list(frm)}
    if page:n["page"]=page
    if salient:n["salient"]=salient
    return n
def mot(text,src_,q=None):
    m={"text":text,"source":src_}
    if q:
        assert q in src,q
        m["quote"]={"source":"paper","quote":q}
    return m
def show(id,claim,method,motiv,children,page=None,frm=(),adds=None,salient=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":motiv,"children":children,"from":list(frm)}
    if page:n["page"]=page
    if adds:n["adds"]=adds
    if salient:n["salient"]=salient
    return n
def B(sym,name,meaning,rel="direct"):
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}

S11=inf("S1.1","Splitting, digit moves and row splits on an array of volume $V$ are linear-time scans.",
 "Each of the following operations on an array of","stream-scans",["multitape-model","array-indexing-by-tuples-and-mixed-radix","basic-complexity-of-tape-computation"])
S12=inf("S1.2","Updating a later address field by an offset computed from earlier control fields, or scaling it by a rational unit, costs $O(V)$.",
 "Multiplication of $y$ by any of the specified rational units, and its","controlled-shifts",["modular-arithmetic","rational-numbers-and-dyadic-fractions","stream-scans"])
S131=inf("S1.3.1","A network of pointwise linear gates with invertible frames $D_v$ leaves, along a route, only an endpoint operator on every role.",
 "called its \\emph{frame}.","linear-network-frames",["linear-algebra-over-a-field","permutations-and-sorting"])
S132=inf("S1.3.2","Two fixed networks built from three-element subsets of $[h]$ have nested subspace labels whose edge rank changes sum to $s<Wm$.",
 "The sum of the rational ranks of all edge differences is","subset-subspace-networks",["linear-network-frames","the-field-with-two-elements","gaussian-integers","rational-numbers-and-dyadic-fractions"],
 salient="The total rank change $s$ is strictly less than $Wm$ (a tiny but positive relative deficit); the page should explain why the subset-intersection construction with gather, scatter and auxiliary wires produces this strict deficit.")
S133=inf("S1.3.3","A call at parameter $mf$ makes $s<Wm$ calls at parameter $f$ on volume $V/W$, so the per-volume cost grows by $s/W<m^{\\tau}$ per multiplication of the parameter by $m$, a power saving.",
 "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,","recursive-saving",["recurrences-and-geometric-sums","subset-subspace-networks"],
 salient="Cost per volume grows by less than a factor $m$ each time the parameter is multiplied by $m$; this strict inequality is what turns a recursion into a power $u^{\\tau}$ with $\\tau<1$.")
S13=show("S1.3","Two fixed linear networks exchange banks of values and restore auxiliary values, with strictly fewer than $Wm$ smaller calls in total.",
 "construct a linear network with frames, label it by subspaces, and read off a recurrence",
 mot("The saving cannot come from the arithmetic alone: a network whose edges are cheap changes of representation lets a call be reduced to fewer smaller calls than a naive split, which is the strict inequality the recursion exploits.","explicit","is the source of the power saving."),
 [S131,S132,S133],frm=[],
 adds=[B("s","smaller call count","the total number of smaller calls (sum of edge ranks) the network needs","count"),
       B("W","wire count","the number of wires (roles) in the network","count"),
       B("m","label dimension","the dimension of the fixed space carrying the subspace labels, equal to $h^3$")])
S141=inf("S1.4.1","Every rational matrix factors as $E_1\\Pi E_2$ with $E_1,E_2$ lower triangular and $\\Pi$ a partial permutation of rank-many ones.",
 "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",None,["triangular-matrices-and-elementary-operations","linear-algebra-over-a-field","controlled-shifts"])
S142=inf("S1.4.2","A shear $(H,D)\\mapsto(H+AD,D)$ costs $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
 "can be performed with exactly $a$ interchanges of pairs of $b$-digit",None,["controlled-shifts"])
S14a=show("S1.4.0","A matrix shear costs $O(V)$ plus one smaller interchange per unit of rank.","factor the matrix into triangular pieces so each piece is a sequence of controlled shifts",
 mot("Controlled shifts only update a later field from earlier ones, so a change of coordinates must be triangular in tape order; the factorization reduces any rational matrix to that form.","recoverable"),
 [S141,S142],page="lower-triangular-shear",frm=["controlled-shifts"])
S143=inf("S1.4.3","For power widths $e=m^k$ with enough rows, two chunks interchange in $O(Ve^{\\tau})$ time by recursion on the network.",
 "The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",None,["recursive-saving","linear-network-frames","subset-subspace-networks","stream-scans"],
 salient="Although every intermediate step forms XOR combinations of data, the final effect is an exact permutation, valid for arbitrary initial auxiliary values; the page should explain why the restoring schedule cancels the auxiliary contributions.")
S144=inf("S1.4.4","For arbitrary width $u$ and shape, the interchange $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ costs $O(Vu^{\\tau})$ with a fixed $\\tau<1$.",
 "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.")
S14=show("S1.4","Two disjoint address fields of $u$ digits can be interchanged in time $O(Vu^{\\tau})$ for a fixed $\\tau<1$.",
 "apply the recursive saving to the bit network, with edges realized by shears",
 mot("Each edge matrix of rank $a$ needs $a$ smaller interchanges, and the ranks sum to less than the number of wires times $m$, so the recurrence saves a power of the chunk width.","recoverable"),
 [S14a,S143,S144],page="address-interchange",frm=["recursive-saving","stream-scans"],
 adds=[B("\\tau","interchange exponent","a fixed exponent below 1 in the interchange cost $O(Vu^{\\tau})$"),
       B("u","field width","the number of digits of each interchanged address field","count")])
S151=inf("S1.5.1","Phase frames express a tensor product of the two-point kernel $C$ on selected bits through smaller groups and binary changes of basis.",
 "We first construct tensor products of the auxiliary two-point kernel",None,["subset-subspace-networks","linear-network-frames"])
S152=inf("S1.5.2","Selected address bits can be changed by packed additions on a rectangle, with exceptional addresses repaired by sorting.",
 "\\begin{lemma}[Packed selected-bit addition on one rectangle]",None,["stream-scans","controlled-shifts"])
S153=inf("S1.5.3","Applying $H_0$ simultaneously on the same bit of $d$ address chunks costs $O(Vd^{\\lambda'})$ with one truncation after the contractive layer.",
 "\\begin{proposition}[Simultaneous normalized butterfly layer]",None,["fixed-point-precision","address-interchange"],
 salient="The cost is $O(Vd^{\\lambda'})$ with $\\lambda'<1$, so $d$ layers cost less than $d$ whole-array passes; the page should explain this from the recursive saving.")
S15=show("S1.5","A normalized butterfly layer on the same bit position of $d$ address chunks costs $O(Vd^{\\lambda'})$ instead of $d$ whole-array passes.",
 "reuse the recursive saving on the complex phase network, with chunk moves for changes of basis",
 mot("Separate butterfly factors would need $d$ whole-array passes; the same network trick that speeds the interchange gives a sub-linear cost in $d$ for a simultaneous layer.","recoverable"),
 [S151,S152,S153],page="simultaneous-butterfly-layer",frm=["recursive-saving","address-interchange","fixed-point-precision","fft-butterfly","negacyclic-ring"],
 adds=[B("d","axis count","the number of address chunks (transform axes) acted on at once","count"),
       B("\\lambda'","layer exponent","a fixed exponent below 1 in the layer cost $O(Vd^{\\lambda'})$")])
S1=show("S1","Two tape procedures, fast address interchange and fast simultaneous butterfly layers, make address movement and Fourier layers cost less than a full scan per level.",
 "build the elementary scans, then the network-based recursive saving, then the two accelerated procedures",
 mot("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both movement and arithmetic.","explicit","We therefore need savings in both movement and arithmetic."),
 [S11,S12,S13,S14,S15],frm=["fft-butterfly"])
# S2
S21=inf("S2.1","Synthetic Fourier transforms over $\\mathbb C[y]/(y^r+1)$ use powers of $y$ as roots, are invertible up to $1/t$, and keep frequency order.",
 "F_t^+F_t^-=t^{-1}I.","synthetic-transforms",["negacyclic-ring","fft-butterfly","convolution-dft"],
 salient="The forward transforms keep the same frequency order through the pointwise product and the opposite transform consumes that order, so no reordering is ever executed.")
S22=inf("S2.2","Arranging the array so the simultaneous layers apply gives a transform at the stated layout cost.",
 "\\begin{lemma}[Transform layout and cost]",None,["simultaneous-butterfly-layer","address-interchange","stream-scans"])
S23=inf("S2.3","Ring elements with Gaussian-integer coefficients are multiplied exactly by signed Kronecker packing into long integers and the established $O(N\\log N)$ multiplier.",
 "One can compute the exact Gaussian integer","signed-packing-products",["negacyclic-ring","gaussian-integers","schoolbook-multiplication-and-divide-and-conquer","nlogn-conjecture"])
S24=inf("S2.4","Two forward transforms, a pointwise packed product and the opposite transform give the convolution over the ring at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
 "\\begin{proposition}[Convolution from the retained transform layout]",None,["synthetic-transforms","signed-packing-products"])
S2=show("S2","Convolution over $\\mathbb C[y]/(y^r+1)$ on $T$ entries is computed at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
 "transform both operands, multiply pointwise, transform back",
 mot("The convolution theorem turns convolution into pointwise products after a transform; here the transforms are the synthetic ones that the fast layers accelerate.","recoverable","is stored, because the opposite transform consumes that same order") if False else mot("The convolution theorem turns convolution into pointwise products after a transform; the synthetic transforms are the ones the fast layers accelerate, and the opposite transform must consume the stored frequency order.","reconstructed"),
 [S21,S22,S23,S24],page="transform-layout-cost",frm=["synthetic-transforms","signed-packing-products","simultaneous-butterfly-layer","address-interchange"],
 adds=[B("r","ring length","the number of complex coefficients in a ring element, a power of two","count"),
       B("\\ell","log ring length","$\\log_2 r$, the number of butterfly rounds per axis"),
       B("K","chunk width","the number of bits in each address chunk","count"),
       B("T","array size","the number of array entries, the product of the axis lengths","count"),
       B("p","precision","the number of fractional bits of each coefficient","count")])
# S3
S31=inf("S3.1","In one dimension, $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with contractions $A,B_0$ computed in time $O(tp^{3/2+\\delta}\\alpha)$, without executing the permutations.",
 "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and",None,["gaussian-resampling","convolution-dft","fixed-point-precision"])
S32=inf("S3.2","The identity tensors over $d$ axes, with line maps costing $O(dTp^{3/2+\\delta}\\alpha)$ and axis exposure costing $O(Tpd^2(1+\\ell^{\\tau}))$.",
 "\\begin{lemma}[Tensor interface]")
S3=show("S3","The Fourier transform of pairwise coprime lengths $s_i$ is expressed through power-of-two transforms with the coordinate permutations kept in the identity.",
 "keep the source and target permutations inside the Gaussian-resampling identity and tensor it over $d$ axes",
 mot("The usual implementation sorts twice on each coordinate; retaining both permutations in the formula avoids the full sorts, which would cost $n\\log n$.","explicit","Its usual implementation sorts twice on each"),
 [S31,S32],page="resampling-no-sort",frm=["gaussian-resampling","multidimensional-transform","address-interchange"])
S4=inf("S4","A chirp identity writes $QF_{\\boldsymbol t}$ as a chirp multiplication around a cyclic convolution, and the source permutation $R$ cancels across the two forward transforms and the opposite transform.",
 "Complex conjugation of the input and output of an algorithm for","bluestein-chirp",["convolution-dft","gaussian-resampling"],
 salient="The retained permutation cancels across two forward transforms, their pointwise product and the opposite-sign transform, yielding $(u*v)/S^2$ without any sorting.")
# S5
S51=inf("S5.1","The coefficient list is placed on pairwise coprime cyclic axes by the Chinese remainder map $\\Phi$, preserving convolution, using controlled cyclic shifts.",
 "sequence of controlled cyclic shifts.","crt-address-map",["radix-digit-convolution","convolution-dft","divisibility-primes-and-coprimality","controlled-shifts","lower-triangular-shear","address-interchange"])
S52=inf("S5.2","The twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ turns cyclic convolution of length $r$ into the ring modulo $y^r+1$.",
 "obtained from the synthetic convolution by a coefficient twist.","coefficient-twist",["negacyclic-ring","convolution-dft","complex-numbers"],
 salient="The negative wrap of the ring cancels with the twist phases, $\\zeta^{k+l}(-1)^h=\\zeta^j$, so the cyclic wrap is restored exactly.")
S53=inf("S5.3","The chirp phases and the middle transform are evaluated with the complex convolution and composed with the Gaussian maps.",
 "We next use the complex convolution to evaluate the middle factor",None,["bluestein-chirp","coefficient-twist","transform-layout-cost","resampling-no-sort"])
S54=inf("S5.4","Digit extraction, $\\Phi$, three transforms, a pointwise product, two rescalings, rounding and carry propagation produce the product.",
 "The source-transform procedures now supply the three transforms needed",None,["radix-digit-convolution","crt-address-map","stream-scans"])
S55=inf("S5.5","The coefficient error is strictly below $1/2$, so rounding recovers the exact integer coefficients.",
 "The strict error below $1/2$ makes the nearest integer to","fixed-point-precision",["rounding-and-approximation-error","rational-numbers-and-dyadic-fractions","euclidean-norm-and-inequalities","gaussian-integers"])
S56=inf("S5.6","With $b=\\lceil\\log n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$ and fixed rational exponents, every row of the cost table is a power of $p$ at most $1-2\\kappa$, giving $O(n(\\lg n)^{1-\\kappa})$.",
 "Each of the seven displayed powers is at most $1-2\\kappa$ by","parameter-choice-cost",["logarithms-floors-and-ceilings","transform-layout-cost","resampling-no-sort","crt-address-map","coefficient-twist","fixed-point-precision"],
 salient="Every row of the normalized cost table is a power of $p$ strictly below 1, uniformly, which is why the total saves a power $\\kappa$ of the logarithm.")
S5=show("S5","Chain the CRT map, twist and chirp procedures with the transforms, recover the integer coefficients exactly, and total the cost.",
 "assemble the reductions of the pipeline and account for every representation change",
 mot("Each stage only changes problem or representation, so the exact product follows from known rescalings, rounding and carries once every stage's cost and error is bounded.","recoverable"),
 [S51,S52,S53,S54,S55,S56],frm=["radix-digit-convolution"])
root=show("S0","A deterministic fixed multitape Turing machine multiplies two $n$-bit integers in time $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
 "reduce multiplication to a convolution over $\\mathbb C[y]/(y^r+1)$ via CRT, Gaussian resampling, chirps and a twist, and evaluate its transforms with fast interchange and butterfly layers",
 mot("Splitting into radix digits reduces multiplication to convolution; the transforms need power-of-two axes and polynomial roots of unity, and the two tape procedures supply the saving. The text builds the tape tools first and then the reductions.","recoverable"),
 [S1,S2,S3,S4,S5],page="main-theorem",
 frm=["multitape-model","nlogn-conjecture","radix-digit-convolution","convolution-dft","multidimensional-transform","big-o","polynomials"],
 salient="The saving is a power of $\\lg n$ (the exponent $\\kappa=2^{-182}$ is tiny but positive), not a $\\log\\log$ factor.")
json.dump({"root":root},open('/home/user/openai-nlogn-wiki/runs/D5/exegenius/tasks/0003-argument.answer.json','w'),indent=1)
