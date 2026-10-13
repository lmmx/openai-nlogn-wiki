import json
def Q(q): return {"source":"paper","quote":q}
def inf(id,claim,q,page=None,frm=(),deferred=False,salient=None):
    d={"id":id,"intention":"infer","claim":claim,"quote":Q(q),"from":list(frm)}
    if page:d["page"]=page
    if deferred:d["deferred"]=True
    if salient:d["salient"]=salient
    return d
def show(id,claim,method,mot,src,children,page=None,frm=(),adds=None,salient=None,mq=None):
    d={"id":id,"intention":"show","claim":claim,"method":method,
       "motivation":{"text":mot,"source":src,"quote":Q(mq) if mq else None},
       "children":children,"from":list(frm)}
    if page:d["page"]=page
    if adds:d["adds"]=adds
    if salient:d["salient"]=salient
    return d
b=lambda s,n,m,r:{"symbol":s,"name":n,"meaning":m,"relation":r}

net=show("S1.1","Both tape procedures come from fixed linear networks whose calls are smaller instances of the same procedure, with $s<Wm$ smaller calls over $W$ roles in an $m$-dimensional space, giving a power saving.",
 "build a fixed linear network with frames, restore auxiliaries, and recurse on a strict call-count inequality",
 "A direct scan costs a full pass per level; a network whose edges are smaller calls of the same procedure lets a strict inequality on call counts compound into a power saving.","recoverable",
 [
 inf("S1.1.1","A fixed linear network exchanges two banks of values; wires are roles and each gate has an invertible frame, so intermediate frames cancel and leave the endpoint operator on each of the $W$ role arrays.",
  "We construct two fixed linear networks that exchange two banks of values","linear-network",["matrices-invertibility-and-linear-maps","tape-streams"]),
 inf("S1.1.2","Auxiliary scalar values are subtracted, used and added back, so the result is exact for any initial auxiliary contents.",
  "For arbitrary initial values of its auxiliary wires, a forward",
  "restored-auxiliaries",["linear-network"]),
 inf("S1.1.3","The endpoint operator for the bit procedure is the address shear $(H,D)\\mapsto(H+D,D)$, which with two linear-cost updates completes an interchange.",
  "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization","address-shear",["matrices-invertibility-and-linear-maps","modular-arithmetic-and-congruences","linear-network"]),
 inf("S1.1.4","Subspaces of a fixed $m$-dimensional space attached to gates, built from three-element subsets with gather, scatter and auxiliary wires, make the total number $s$ of smaller calls satisfy $s<Wm$.",
  "The scalar network already has the required signed exchange. We now","subset-network",["vector-spaces-subspaces-and-dimension","linear-network","restored-auxiliaries"],
  salient="The count of smaller calls is strictly below Wm, the fact on which the whole power saving rests."),
 inf("S1.1.5","Since $s/W<m$, multiplying the parameter by $m$ raises the per-volume cost by less than a factor $m$, so the cost is the volume times a power of the parameter below 1.",
  "Choose a rational number $\\tau\\in(0,1)$ with $s/W<m^\\tau$.","recursive-saving",["mathematical-induction-and-recurrences","subset-network"],
  salient="The exponent is strictly below 1 although every level only saves an arbitrarily small fraction, because the strict inequality s/W<m compounds under repeated multiplication of the parameter."),
 ],adds=[b("W","number of roles","The number of roles (wires) in the network, among which rows are distributed cyclically.","count"),
         b("m","space dimension","The dimension of the fixed space whose subspaces are attached to the gates and by which the parameter is multiplied per recursion.","count"),
         b("s","smaller calls","The total number of smaller calls of the same procedure used by the network.","count")],
 mq="The decisive property is that the total")
net["motivation"]["quote"]=None

S1=show("S1","Two fast tape procedures exist: interchange of two address fields of $u$ bits in time $O(Vu^\\tau)$ and a simultaneous butterfly layer in time $O(Vd^{\\lambda'})$, with $\\tau,\\lambda'<1$ and $V$ the stored bit volume.",
 "construct each procedure from a linear network and extract a power saving",
 "Scanning the array at each of the Theta(log n) transform levels already costs n log n, so savings are needed in both movement and arithmetic.","explicit",
 [net,
  inf("S1.2","Interchanging two disjoint contiguous address fields of $u$ bits in an array of stored bit volume $V$ costs $O(Vu^\\tau)$ for a fixed $\\tau<1$, using XOR combinations of data.",
   "interchanges two disjoint contiguous address fields","address-interchange",["net-placeholder"]),
  ],page=None,frm=["tape-streams","multitape-model"],
 mq="We therefore need savings in both movement and arithmetic. Two tape",
 adds=[b("V","stored bit volume","The number of bits stored in the array being processed.","count")])
# fix S1.2: address-interchange needs be the page with network children => restructure
S1["children"]=[
 show("S1.1","Address interchange of two $u$-bit fields of an array of stored bit volume $V$ costs $O(Vu^\\tau)$ for a fixed $\\tau<1$, using XOR combinations of data.",
  net["method"],net["motivation"]["text"],"recoverable",net["children"],page="address-interchange",
  frm=["tape-streams","multitape-model"],adds=net["adds"],
  salient="The exponent tau is strictly below 1 although the final effect is an exact permutation built only of XOR combinations."),
 inf("S1.2","Applying $H_0$ simultaneously at the same bit position in $d$ address chunks of the numerical arrays costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, with a single truncation after the layer.",
  "Simultaneous normalized butterfly layer","fast-butterfly-layer",["butterfly","fixed-point-precision","address-interchange","linear-network","recursive-saving"],deferred=False,
  salient="The same strict power saving lambda'<1 arises for arithmetic as tau<1 does for movement, from the same network-and-recursion mechanism."),
]
S1["adds"]=[]
S1["from"]=[]
S1["children"][0]["from"]=["tape-streams"]

rest=[
 inf("S2","The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.",
  "Agarwal and Cooley used the Chinese remainder","crt-address-map",["convolution","prime-numbers-and-coprimality","modular-arithmetic-and-congruences","cyclic-and-negacyclic-indexing","cartesian-products-and-index-tuples"]),
 inf("S3","Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform, with source and target permutations retained in the identity rather than executed as sorts.",
  "Resampling without executing the two permutations","gaussian-resampling",["fourier-transform","multidimensional-transform","permutations-and-bijections"]),
 inf("S4","Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution.",
  "Chirp and permutation cancellation","bluestein-chirp",["fourier-transform","cyclic-and-negacyclic-indexing"]),
 inf("S5","A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$ whose negative wrap gives the original cyclic wrap after untwisting.",
  "obtained from the synthetic convolution by a coefficient twist.","phase-twist",["polynomial-ring","cyclic-and-negacyclic-indexing"]),
 show("S6","Convolution over the polynomial ring on the remaining axes is computed with synthetic transforms in retained frequency order and packed polynomial products.",
  "use synthetic transforms for the evaluation and signed packing for the pointwise products",
  "Powers of y act as roots of unity so root multiplications are signed shifts, and the pointwise polynomial products reduce to integer multiplication.","recoverable",
  [inf("S6.1","The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order.",
    "Transform layout and cost","transform-layout",["synthetic-transforms","polynomial-ring","address-interchange","fast-butterfly-layer"],
    salient="One frequency order is shared by both forward transforms, the product and the opposite transform, so no reordering is needed between them."),
   inf("S6.2","Polynomial products are computed by signed packing into one integer and the established $O(n\\log n)$ multiplier as an ordinary subroutine.",
    "Signed packing and normalized ring multiplication","signed-packing",["polynomial-ring","nlogn-conjecture"])],
  frm=["synthetic-transforms","polynomial-ring"]),
 inf("S7","Known normalizations and digit scales are removed, the recovered coefficient error is below $1/2$ so rounding is exact, and carries yield the exact binary product.",
  "To propagate carries, let $Q_0=2^b$.","carry-propagation",["fixed-point-precision","dyadic-rationals-and-fixed-point-numbers","sup-norm-and-rounding-error-bounds","schoolbook-multiplication-and-linear-time-addition","convolution"],
  salient="The recovered coefficient error is strictly below 1/2, which is what makes rounding exact."),
]
root=show("S0","Two $n$-bit integers can be multiplied exactly by a deterministic multitape machine in time $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
 "reduce multiplication through a chain of convolution problems down to polynomial-ring convolution, evaluated with the fast tape procedures",
 "The standard transform-based approach costs n log n at best; the chain of reductions puts the problem in a form where transforms are made only of address moves, shifts and butterflies, which the two fast procedures speed up by a power of log n.","recoverable",
 [S1]+rest,page="target",frm=["multitape-model","nlogn-conjecture","convolution","big-o","binary-representation-and-bit-operations","floors-ceilings-and-logarithms","asymptotic-notation-beyond-big-o"],
 adds=[b("\\kappa","saving exponent","The fixed constant giving the power saving $(\\lg n)^{-\\kappa}$ over $n\\lg n$.","direct")])
root["children"][0]["from"]=["turing-machine"]

c=root["children"][0]["children"][0]["children"]
c[2],c[3]=c[3],c[2]
c[3]["from"]=["matrices-invertibility-and-linear-maps","modular-arithmetic-and-congruences","linear-network"]
c[2]["from"]=["vector-spaces-subspaces-and-dimension","linear-network","restored-auxiliaries"]
c[4]["from"]=["mathematical-induction-and-recurrences","subset-network","address-shear"]
r=root["children"]
r[1]["deferred"]=True
r[5]["children"][0]["deferred"]=True
r[5]["children"][1]["deferred"]=True
json.dump({"root":root},open("exegenius/tasks/0003-argument.answer.json","w"),indent=1)
