import json
def Q(q): return {"source":"paper","quote":q}
def inf(i,claim,q,page=None,frm=(),deferred=False,salient=None):
    d={"id":i,"intention":"infer","claim":claim,"quote":Q(q),"from":list(frm)}
    if page: d["page"]=page
    if deferred: d["deferred"]=True
    if salient: d["salient"]=salient
    return d
def show(i,claim,method,mot,src,children,page=None,frm=(),salient=None,mq=None,adds=None):
    m={"text":mot,"source":src}
    if mq: m["quote"]=Q(mq)
    d={"id":i,"intention":"show","claim":claim,"method":method,"motivation":m,"children":children,"from":list(frm)}
    if page: d["page"]=page
    if salient: d["salient"]=salient
    if adds: d["adds"]=adds
    return d
root=show("S0","A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time, $\\kappa=2^{-182}$.",
 "Reduce multiplication to convolution over $\\mathbb C[y]/(y^r+1)$ evaluated by synthetic transforms, and speed up the two bottleneck tape operations (address interchange, butterfly layers) by a recursive power saving",
 "Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$, so savings are needed in both data movement and arithmetic.","explicit",
 [
 inf("S1","Schönhage and Strassen proposed $n\\log n$ as optimal and Harvey and van der Hoeven reached $O(n\\log n)$; the goal is a power saving below it.","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper","nlogn-conjecture",["big-o","karatsuba-and-schoolbook-multiplication"]),
 show("S2","Address interchange and simultaneous butterfly layers can be done with a power saving in the logarithmic factor.",
  "Build fixed linear networks with frames whose total number of smaller calls satisfies $s<Wm$, then recurse",
  "Both procedures arise from their own fixed linear network, and a strict inequality between calls and roles gives a power rather than linear growth.","recoverable",
  [
  inf("S2.1","A fixed linear network exchanging two banks of values and restoring auxiliary values lets an array gate act pointwise, with frames cancelling so the endpoint operator is the desired one.","We construct two fixed linear networks that exchange two banks of values","linear-networks-frames",["array-streams","matrices-linear-maps-and-rank","permutations","linear-time-scanning-of-tapes"]),
  inf("S2.2","Subspaces from three-element subsets, gather, scatter and scratch wires make the total number $s$ of smaller calls less than $Wm$.","The saving will come from keeping the total dimension lost on decreasing","subset-networks",["linear-networks-frames","sets-products-and-tuples","matrices-linear-maps-and-rank"]),
  inf("S2.3","Since $s<Wm$, a recursion with $s$ calls on volume $V/W$ costs $O(V\\cdot\\text{parameter}^{\\tau})$ with $\\tau<1$ (explicitly $\\tau=1-2^{-50}$).","Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.","recursive-saving",["subset-networks","recurrences-and-divide-and-conquer","logarithms-and-exponents","asymptotic-constants-and-small-epsilon-exponents"],
     salient="The saving is a power, not a constant: the strict inequality $s<Wm$ makes the cost per volume grow by a factor below $m$ whenever the parameter is multiplied by $m$."),
  show("S2.4","Two disjoint address fields of $u$ bits in an array of volume $V$ can be interchanged in time $O(Vu^\\tau)$, $\\tau<1$.",
   "Realize the bit network's edge operators as address shears done in tape order, then recurse with the saving",
   "Edge operators must be done in tape order at cost scaling with rank, so that rank sums below $Wm$ give a power saving.","recoverable",
   [
   inf("S2.4.1","Any rational matrix factors as lower triangular times partial permutation times lower triangular, so address shears are done in tape order at cost scaling with rank.","is the Bruhat factorization for arbitrary matrices, with coordinate order","lower-triangular-shear",["matrices-linear-maps-and-rank","modular-arithmetic-and-residue-rings","linear-time-scanning-of-tapes"]),
   inf("S2.4.2","Chunks of $e$ digits are interchanged in $O(Ve^\\tau)$ time.","can be interchanged in $O(Ve^\\tau)$ time, preserving every",None,["recursive-saving"]),
   ],page="address-interchange",frm=["array-streams","linear-networks-frames","subset-networks","recursive-saving","permutations"]),
  inf("S2.5","Simultaneous butterfly layers on same bit position of up to $d$ address chunks cost $O(Vd^{\\lambda'})$ with $\\lambda'<1$, instead of $d$ whole-array passes.","We will obtain cost $O(Vd^{\\lambda'})$, with","fast-butterfly-layers",["butterfly","ring-ymr","fixed-point-exactness","linear-networks-frames","subset-networks","recursive-saving","address-interchange","complex-numbers","floating-point-and-rounding-errors"]),
  ]),
 show("S3","Convolution over $\\mathbb C[y]/(y^r+1)$ can be computed by synthetic transforms and exact packed polynomial products.",
  "Evaluate synthetic Fourier transforms by fast butterfly layers and multiply entries by signed packing",
  "Powers of $y$ act as roots of unity so root multiplications are signed shifts, leaving only butterflies and polynomial products.","explicit",
  [
  inf("S3.1","Synthetic transforms over the ring use powers of $y$ as roots of unity, with butterfly layers and a retained frequency order.","where the required roots of unity act by exact signed permutations","synthetic-transforms",["ring-ymr","butterfly","dft-convolution","fast-butterfly-layers","address-interchange"]),
  inf("S3.2","Ring polynomials are multiplied exactly by signed Kronecker packing into the Harvey–van der Hoeven integer multiplier.","reduction is a signed form of Kronecker substitution; compare","signed-packing",["hh-multiplier","ring-ymr","fixed-point-exactness","binary-representation-of-integers"]),
  ],mq="Powers of $y$ then\nserve as roots of unity in the remaining axes, and multiplication by\nsuch a root is a signed shift of the coefficient list."),
 show("S4","The integer product is obtained from the convolution over the ring by a pipeline of reductions with controlled error.",
  "Chain radix-digit convolution, prime axes, Gaussian resampling, chirp convolution and phase twist, then rescale, round and carry",
  "Each reduction changes the problem into one nearer to power-of-two axes where synthetic transforms apply.","recoverable",
  [
  inf("S4.1","Splitting into radix digits turns integer multiplication into convolution of short integer coefficient lists.","Read each stored operand backward from","radix-convolution",["dft-convolution","binary-representation-of-integers"],deferred=True),
  inf("S4.2","A Chinese-remainder map places the coefficient list on distinct prime cyclic axes, preserving convolution.","theorem to convert one cyclic convolution into multidimensional cyclic","crt-prime-axes",["prime-numbers-and-coprimality","modular-arithmetic-and-residue-rings","radix-convolution"],deferred=True),
  inf("S4.3","Gaussian resampling expresses each Fourier transform through a power-of-two transform, keeping the two permutations in the formula.","[Resampling without executing the two permutations]","gaussian-resampling",["dft-convolution","crt-prime-axes","permutations","fixed-point-exactness"]),
  inf("S4.4","Bluestein's chirp identity converts the middle transform with its permutation into cyclic convolution, and the retained permutations cancel.","[Chirp and permutation cancellation]","bluestein-chirp",["dft-convolution","permutations"]),
  inf("S4.5","Error stays below $1/2$ so rounding recovers the coefficients exactly.","\\subsection{Precision and exact recovery}",None,["fixed-point-exactness","floating-point-and-rounding-errors"]),
  inf("S4.6","With compatible parameters every term of the cost table is within $O(n(\\lg n)^{1-\\kappa})$.","For the cost calculation put $V=Tp=\\Theta(n)$.",None,["address-interchange","fast-butterfly-layers","big-o"]),
  ],page="multiplication-algorithm",frm=["synthetic-transforms","signed-packing","ring-ymr","fixed-point-exactness","hh-multiplier","nlogn-conjecture"]),
 ],page="main-result",frm=["nlogn-conjecture","multitape-tm","binary-representation-of-integers","asymptotic-constants-and-small-epsilon-exponents"],
 mq="Scanning an array of $\\Theta(n)$ stored bits at each of\n$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$.",
 salient="The saving is a tiny but strict power $\\kappa=2^{-182}$ of the logarithm, coming from the strict inequality $s<Wm$.")
json.dump({"root":root},open("/home/user/openai-nlogn-wiki/runs/M1/exegenius/tasks/0003-argument.answer.json","w"),indent=1,ensure_ascii=False)
