import json
def ev(q): return {"source":"paper","quote":q}
def inf(id,claim,q,page=None,frm=(),deferred=False,salient=None):
    d={"id":id,"intention":"infer","claim":claim,"quote":ev(q),"page":page,"from":list(frm)}
    if deferred:d["deferred"]=True
    if salient:d["salient"]=salient
    return d
def mot(t,s="reconstructed",q=None): return {"text":t,"source":s,"quote":ev(q) if q else None}
net=[
 inf("T3","A fixed linear network with roles and frames exchanges two banks of values, so intermediate frames cancel and a call reduces to smaller calls.","Each procedure arises from its own fixed linear network that exchanges two","linear-network-frames",["tape-streams","direct-product-of-sets-and-multidimensional-arrays","linear-algebra-over-the-reals-and-complex-numbers"],True),
 inf("T4","Three-element subsets give a finite network whose total number of smaller calls s satisfies $s<Wm$.","The finite construction in Section~\\ref{sec:finite-networks} attaches","subset-intersection-network",["linear-network-frames","basic-counting-and-combinatorics"],True,"The count s of smaller calls is strictly below W m, which is what later gives a power saving."),
 inf("T5","A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ streams, so cost per volume grows like a power less than 1 of the parameter.","A recursive call at parameter $mf$ therefore uses $s$ calls at parameter","recursive-power-saving",["subset-intersection-network","induction-and-recurrences"],True,"Cost per volume is a power of the parameter with exponent below 1, not linear, because s/W<m strictly."),
 inf("T6","Two disjoint address fields of $u$ bits can be interchanged in an array in $O(Vu^\\tau)$ time with $\\tau<1$.","The first procedure interchanges two disjoint contiguous address fields","address-interchange",["recursive-power-saving","binary-xor-and-bitwise-operations","permutations-and-bijections"],True,"The intermediate steps are XOR combinations of data, yet the final result is an exact permutation for arbitrary auxiliary values."),
 inf("T7","The layer $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the same bit of at most $d$ address chunks costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.","The second procedure applies","simultaneous-butterfly",["recursive-power-saving","address-interchange","fixed-point-and-rounding-arithmetic"],True),
]
tape={"id":"T","intention":"show","claim":"The synthetic-transform address rearrangements and butterfly layers can be done faster than by scanning the whole array at each of $\\Theta(\\log n)$ levels.",
 "method":"build two tape procedures from linear networks and a recursive power saving","motivation":mot("Plain scans at each of Theta(log n) levels cost Theta(n log n), so both movement and arithmetic need a saving; the network recursion supplies a strict power saving.","explicit","Scanning an array of $\\Theta(n)$ stored bits at each of"),
 "page":None,"from":[],
 "children":[inf("T1","Elementary tape operations (scans in address order, stream operations, controlled shifts) cost linear time.","Those changes are implemented by whole-chunk moves and","tape-streams",["multitape-model","turing-tapes"],True)]+net}
tape["motivation"]["quote"]=ev("We therefore need savings in both movement and arithmetic.")
root={"id":"S0","intention":"show","claim":"A multitape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "method":"chain reductions from the integer product to a convolution over $\\mathbb C[y]/(y^r+1)$, compute it with accelerated synthetic transforms, then recover the exact product",
 "motivation":mot("Each stage changes the problem into one whose transform uses only shifts, address rearrangements and butterflies, which the two fast tape procedures speed up; precision analysis then gives exactness.","recoverable"),
 "page":"main-result","from":["multitape-model","nlogn-conjecture-history","big-o","logarithms-and-powers-of-two"],
 "salient":"The logarithmic factor has the strict power (lg n)^{1-kappa} with a tiny fixed kappa, below the conjectured n log n.",
 "children":[
  inf("S1","Splitting both integers into radix digits turns the product into a convolution of short digit lists followed by carry propagation.","Splitting the inputs into radix digits reduces multiplication to","convolution-reduction",["binary-representation-and-radix-digits","schoolbook-multiplication-and-convolution-of-sequences"]),
  inf("S2","A Chinese-remainder address map places the digit list on distinct prime cyclic axes, preserving convolution.","First, the radix-digit coefficient list is placed on a product of","crt-prime-axes",["convolution-reduction","prime-numbers-and-coprimality","modular-arithmetic-and-congruences","cyclic-groups-and-z-mz"]),
  inf("S3","Gaussian resampling expresses each Fourier transform of arbitrary axis length through a power-of-two tensor transform, keeping permutations in the identity.","resampling then expresses each source Fourier transform through a","gaussian-resampling",["fourier-transform-butterflies","crt-prime-axes","permutations-and-bijections"]),
  inf("S4","Bluestein's chirp identity converts the middle transform with its target permutation into normalized cyclic convolution.","Next, Bluestein's chirp identity converts the middle transform,","bluestein-chirp",["gaussian-resampling","fourier-transform-butterflies"]),
  inf("S5","A phase twist makes the last cyclic coordinate a polynomial modulo $y^r+1$ whose negative wrap restores the cyclic wrap after untwisting.","A phase twist changes the last cyclic coordinate into a polynomial","phase-twist",["poly-ring-mod","bluestein-chirp"]),
  {"id":"S6","intention":"show","claim":"Convolution over $\\mathbb C[y]/(y^r+1)$ on the remaining axes is computed exactly and fast.",
   "method":"use synthetic transforms whose twiddles are signed shifts, accelerated by the fast tape procedures, with polynomial products by signed packing",
   "motivation":mot("In the ring, powers of y act as roots of unity and multiplying by them is a signed shift, leaving only rearrangements, shifts and butterflies, which the fast procedures speed up.","explicit","Powers of $y$ then"),
   "page":"synthetic-transforms","from":["poly-ring-mod","fourier-transform-butterflies"],
   "children":[
    inf("S6.1","Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it.","The two forward synthetic transforms",None,["poly-ring-mod","fourier-transform-butterflies"]),
    tape,
    inf("S6.2","Pointwise polynomial products use Kronecker-style signed packing and the established $O(n\\log n)$ multiplier as a subroutine.","use signed packing and the established $O(n\\log n)$ multiplier as an","signed-packing",["poly-ring-mod","karatsuba-and-divide-and-conquer-multiplication"])]},
  inf("S7","Fixed-point error of the recovered coefficients is below $1/2$, so rounding, rescaling and carry propagation give the exact product.","the known normalizations and digit scales, proves that the recovered","precision-exact-recovery",["fixed-point-and-rounding-arithmetic","error-bounds-and-the-triangle-inequality","convolution-reduction"])]}
json.dump({"root":root},open("exegenius/tasks/0003-argument.answer.json","w"),indent=1)
