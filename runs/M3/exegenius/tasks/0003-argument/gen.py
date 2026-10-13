import json
def ev(q): return {"source":"paper","quote":q}
def inf(id,claim,q,page=None,frm=None,sal=None):
    d={"id":id,"intention":"infer","claim":claim,"quote":ev(q),"from":frm or []}
    if page: d["page"]=page
    if sal: d["salient"]=sal
    return d
def mot(t,s="reconstructed",q=None):
    return {"text":t,"source":s,"quote":ev(q) if q else None}
def b(sym,name,meaning,rel="direct"): return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel}

s21={"id":"S2.1","intention":"show","page":"address-interchange",
 "claim":"Two disjoint contiguous address fields of $u$ bits in a Cartesian-product array of volume $V$ can be interchanged in time $O(Vu^\\tau)$ for a fixed $\\tau<1$.",
 "method":"Build a fixed linear network with a rank saving, use it recursively on streams of volume $V/W$, and turn each edge into smaller interchanges",
 "motivation":mot("Scanning the array once per transform level already costs n log n, so the interchange itself must be made cheaper than a full scan per level; a network of linear combinations whose gates need fewer smaller calls than $Wm$ gives a recursion whose cost grows by a factor $s/W<m$ per level.","explicit","Scanning an array of $\\Theta(n)$ stored bits at each of"),
 "salient":"The final effect is an exact permutation although the intermediate steps form XOR combinations of data, and the cost exponent $\\tau$ is strictly below 1.",
 "from":["stream-operations","multitape-model","xor-and-bitwise-operations","cartesian-products-and-multidimensional-arrays","matrices-and-linear-maps","vector-spaces-subspaces-dimension-and-rank","permutations-and-permutation-matrices","divide-and-conquer-recurrences"],
 "adds":[b("V","stored bit volume","The number of stored bits of the array being rearranged.","count"),
         b("W","number of roles","The number of wire roles in the fixed linear network, among which rows are distributed cyclically.","count"),
         b("m","space dimension","The dimension of the fixed space whose nested subspaces are attached to the gates.","count"),
         b("s","number of smaller calls","The total number of smaller calls of the procedure used by the network.","count")],
 "children":[
  inf("S2.1.1","A fixed linear network exchanges two banks of values with signs and restores every auxiliary value, and rows of an array are distributed cyclically among its $W$ roles.","Each procedure arises from its own fixed linear network that exchanges two",page="linear-network",frm=["cartesian-products-and-multidimensional-arrays"]),
  inf("S2.1.2","Choosing an invertible frame operator at each gate makes the intermediate frames cancel, so a route applies only an endpoint operator such as an address shear.","interpretation is defined by applying the inverse input frame. Thus the",page="frames",frm=["linear-network","matrices-and-linear-maps"]),
  inf("S2.1.3","Nested subspaces of an $m$-dimensional space attached to the gates, built from three-element subset intersections, give a network with total number $s$ of smaller calls less than $Wm$.","number $s$ of smaller calls satisfies $s<Wm$.",page="finite-network-subspaces",frm=["linear-network","frames","finite-sets-and-subset-operations","vector-spaces-subspaces-dimension-and-rank"],sal="The total number of smaller calls is strictly below $Wm$, the strict inequality on which the whole power saving rests."),
  inf("S2.1.4","A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$, which raises the volume-normalized cost by a factor $s/W<m$ and so gives a cost $O(Vu^\\tau)$ with $\\tau<1$.","is the source of the power saving. The later tape and arithmetic",page="recursive-saving",frm=["finite-network-subspaces","divide-and-conquer-recurrences"],sal="A strict inequality $s/W<m$ per level of the recursion yields a polynomial saving in the number of digits $u$, a power of the logarithm of the input size."),
  inf("S2.1.5","Every rational matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ lower triangular and $\\Pi$ a partial permutation with $a$ ones, so a shear of rank $a$ needs only $a$ interchanges in tape order.","Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",page="lower-triangular-factorization",frm=["gaussian-elimination-and-triangular-matrices","matrices-and-linear-maps"]),
  inf("S2.1.6","Two disjoint contiguous address chunks of $e=m^k$ digits can be interchanged in $O(Ve^\\tau)$ time, preserving every other address field.","The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",frm=["recursive-saving","lower-triangular-factorization"]),
 ]}

s22=inf("S2.2","Simultaneous normalized butterfly layers applying $H_0$ at the same bit position in each of at most $d$ address chunks cost $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$, with coefficient error less than $\\sqrt2\\,2^{-p}$.","there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure,",page="fast-butterfly-layer",
  frm=["linear-network","frames","finite-network-subspaces","recursive-saving","address-interchange","butterfly","poly-ring-yr1","complex-fixed-point","dyadic-rationals-and-fixed-point-numbers","absolute-value-norms-and-error-bounds"],
  sal="The cost exponent $\\lambda'$ is strictly below 1, from the same strict rank saving $s<Wm$ that gives the address interchange, and intermediate values are exact with one truncation after the contractive layer.")

s2={"id":"S2","intention":"show","claim":"Two tape procedures, the address interchange and the simultaneous butterfly layer, cost $O(Vu^\\tau)$ and $O(Vd^{\\lambda'})$ for fixed $\\tau,\\lambda'<1$ on stored bit volume $V$.",
 "method":"Obtain both procedures from fixed linear networks with a strict rank saving and recurse","motivation":mot("Both the movement of data and the arithmetic of a transform layer must be cheaper than a full scan per level, and both can be expressed as a fixed linear network exchanging banks of values.","explicit","Each procedure arises from its own fixed linear network that exchanges two"),
 "children":[s21,s22]}

s3={"id":"S3","intention":"show","claim":"Convolution over the ring $\\mathbb C[y]/(y^r+1)$ on the remaining axes is computed with cost small enough to be dominated by the fast layers and interchanges.",
 "method":"Use synthetic polynomial transforms on a retained layout, with pointwise ring products by signed packing","motivation":mot("In the ring modulo $y^r+1$ roots of unity are powers of $y$, so multiplying by a root is a signed shift, leaving only address rearrangements and butterflies, which are exactly the two accelerated tape procedures.","explicit","this representation, the transform calculation consists of address"),
 "from":["dft-roots-of-unity","poly-ring-yr1","convolution","fast-fourier-transform-idea","complex-fixed-point"],
 "children":[
  inf("S3.1","Synthetic characters cancel, so the forward and opposite synthetic transforms invert each other up to a scale, $F_t^+F_t^-=t^{-1}I$.","F_t^+F_t^-=t^{-1}I.",page="synthetic-transforms",frm=["dft-roots-of-unity","poly-ring-yr1"]),
  inf("S3.2","On a retained layout parallel butterfly layers and address interchanges compute a $d$-axis synthetic transform at the stated cost and keep the frequency order through the pointwise product.","The procedure constructs an explicit positional",page="transform-layout",frm=["synthetic-transforms","fast-butterfly-layer","address-interchange"]),
  inf("S3.3","Polynomial products in the ring of $r$ complex coefficients are computed exactly by signed packing (Kronecker substitution) and the ordinary $O(n\\log n)$ multiplier, in time $O(rp\\log(rp))$.","$O(rp\\log(rp))$ on a fixed number of tapes.",page="signed-packing",frm=["poly-ring-yr1","big-o"]),
  inf("S3.4","Convolution on the remaining axes over the ring uses two forward transforms, pointwise polynomial products and the opposite transform on the retained layout.","Perform both forward transforms and retain their common $LB$ order.",page="normalized-convolution",frm=["transform-layout","signed-packing","convolution"]),
 ]}

s4={"id":"S4","intention":"show","claim":"Prime-length Fourier transforms on the source axes reduce to power-of-two $d$-axis transforms of precision $p$ followed by a normalized cyclic convolution.",
 "method":"Gaussian resampling with the source and target permutations kept inside the transform, then Bluestein's chirp identity on the middle transform","motivation":mot("A prime-length transform has no fast power-of-two structure, so it is expressed through a power-of-two tensor transform, and the middle transform with its permutation becomes a convolution that the ring machinery can compute without executing separate full sorts.","explicit","Gaussian resampling\nthen expresses each source Fourier transform through a"),
 "from":["dft-roots-of-unity","fast-fourier-transform-idea","complex-fixed-point","prime-numbers-and-coprimality"],
 "children":[
  inf("S4.1","Each prime-length transform is expressed through a power-of-two tensor transform by contractions, with source and target permutations retained in the transform identity.","There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and",page="gaussian-resampling",frm=["dft-roots-of-unity","permutations-and-permutation-matrices","complex-fixed-point"]),
  inf("S4.2","Bluestein's chirp identity turns the middle transform, with its target permutation, into a normalized cyclic convolution.","Then $a$ has period $t_i$ in coordinate $i$, and",page="bluestein-chirp",frm=["gaussian-resampling","convolution","euler-s-formula-and-unit-circle"]),
 ]}
s4["motivation"]["quote"]=None; s4["motivation"]["source"]="recoverable"

s5=inf("S5","The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.","The coordinate of $\\Phi(x^k)$ in axis $i$ is",page="crt-prime-axes",frm=["convolution","radix-reduction","modular-arithmetic-and-congruences","prime-numbers-and-coprimality"])
s6=inf("S6","A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, and its negative wrap gives the original cyclic wrap after untwisting.","Untwisting therefore recovers the cyclic coefficient with the correct",page="phase-twist",frm=["poly-ring-yr1","convolution","euler-s-formula-and-unit-circle"])
s7=inf("S7","The multiplication algorithm reads digits, applies the address map, three transforms, exact scalings, rounding and carries.","The source-transform procedures now supply the three transforms needed",frm=["crt-prime-axes","gaussian-resampling","bluestein-chirp","phase-twist","normalized-convolution","radix-reduction"])
s8=inf("S8","Removing known normalizations leaves coefficient error strictly below $1/2$, so rounding and carry propagation give the exact binary product.","The strict error below $1/2$ makes the nearest integer to",page="exact-recovery",frm=["radix-reduction","complex-fixed-point","absolute-value-norms-and-error-bounds","positional-radix-and-digit-expansion"],sal="The error margin is strictly below $1/2$ with room to spare for the chosen precision $p=6b$.")
s9=inf("S9","With the fixed rational parameters every cost-table term is at most $p^{1-2\\kappa}$, and the total time is $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.","$O(n(\\lg n)^{1-\\kappa})$ for every input length and produces precisely",frm=["worst-case-running-time-and-turing-machine-step-counting"],sal="The tiny value $\\kappa=2^{-182}$ results from conservative fixed exponents; seven normalized cost terms each have power at most $1-2\\kappa$.")

root={"id":"S0","intention":"show","page":"main-theorem",
 "claim":"A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in time $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$, with $p$ bits of working precision, $d$ transform axes of length about $r$.",
 "method":"Reduce the product to a convolution through a chain of representation changes, evaluate it with the two fast tape procedures, then recover the exact product and sum the costs",
 "motivation":mot("Multiplication is a convolution of digits, convolution is computed by transforms, and the cost of transforms is dominated by address movement and butterflies, so a power saving in those two procedures gives a power saving in the whole product.","explicit","Scanning an array of $\\Theta(n)$ stored bits at each of"),
 "from":["nlogn-conjecture","multitape-model","convolution","dft-roots-of-unity","poly-ring-yr1","butterfly","synthetic-transforms","complex-fixed-point","big-o","binary-representation-of-integers","logarithms-and-floor-ceiling","turing-machine"],
 "adds":[b("p","working precision","The number of fractional bits kept in complex fixed-point numbers.","count"),
         b("d","number of axes","The number of power-of-two transform axes.","count"),
         b("r","ring length","The number of complex coefficients in a record of the ring modulo $y^r+1$.","count")],
 "children":[
  inf("S1","Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.","Splitting the inputs into radix digits reduces multiplication to",page="radix-reduction",frm=["convolution","positional-radix-and-digit-expansion","binary-representation-of-integers"]),
  s2,s3,s4,s5,s6,s7,s8,s9]}
# motivations needed for explicit quote checks: fix questionable ones
json.dump({"root":root},open("/home/user/openai-nlogn-wiki/runs/M3/exegenius/tasks/0003-argument.answer.json","w"),indent=1)
