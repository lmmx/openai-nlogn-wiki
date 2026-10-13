import json
def Q(q): return {"source":"paper","quote":q}
def inf(id,claim,q,page=None,frm=None,deferred=False,salient=None):
    d={"id":id,"intention":"infer","claim":claim,"quote":Q(q),"page":page,"from":frm or []}
    if deferred:d["deferred"]=True
    if salient:d["salient"]=salient
    return d
def mot(t,s="reconstructed",q=None): return {"text":t,"source":s,"quote":Q(q) if q else None}
S4=[
 inf("S4.1","Elementary scans, controlled shifts and fixed scalings on tape streams each cost linear time in the stored volume $V$.","the elementary scans it uses.",page="tape-streams",frm=["multitape-tm","tensor-kronecker-product-and-multidimensional-arrays"]),
 inf("S4.2","A fixed linear network exchanging banks of values, with an invertible frame per gate, restores all auxiliary values and leaves only the endpoint operator on every role array.","pointwise without disturbing the representation.",page="gate-frames",frm=["vectors-matrices-and-linear-maps","tape-streams"]),
 inf("S4.3","Networks built from three-element subsets with nested subspaces of an $m$-dimensional space need only $s<Wm$ smaller calls.","Let $\\mathcal T$ be the set of three-element subsets of $[h]$.",page="finite-network-subspaces",frm=["gate-frames"]),
 inf("S4.4","A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ each, so cost per volume grows with an exponent below 1.","Because the sum of these ranks is less than the number of wires times",page="recursive-power-saving",frm=["finite-network-subspaces","recurrence-relations-and-geometric-sums"],salient="The recursive contribution grows by the factor s/W, which is strictly below m because s<Wm, giving a power saving rather than a constant-factor one."),
 inf("S4.5","Two address fields of $u$ bits are interchanged in cost $O(Vu^\\tau)$ with $\\tau<1$, by XOR combinations whose final effect is an exact permutation.","The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",page="address-interchange",frm=["recursive-power-saving","sorting-and-permutations"],salient="Intermediate steps are XOR combinations of data, yet the final effect is an exact permutation for arbitrary initial auxiliary values."),
 inf("S4.6","The layer $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied simultaneously on selected address bits of $d$ chunks in cost $O(Vd^{\\lambda'})$ with $\\lambda'<1$.","We will obtain cost $O(Vd^{\\lambda'})$, with",page="fast-butterfly-layers",frm=["recursive-power-saving","address-interchange","floating-and-fixed-point-numbers-and-rounding"]),
]
S5x=[
 inf("S5.1","The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a convolution-preserving Chinese-remainder map.","\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain",page="crt-address-map",frm=["radix-digit-convolution","primes-and-coprimality","modular-arithmetic"]),
 inf("S5.2","Gaussian resampling expresses each source Fourier transform through a transform with power-of-two axis lengths.","We retain both permutations in the transform formula and",page="gaussian-resampling",frm=["dft-convolution","crt-address-map"]),
 inf("S5.3","Bluestein's chirp identity turns the middle transform into a normalized cyclic convolution.","computed from a cyclic convolution and two pointwise phase",page="bluestein-chirp",frm=["gaussian-resampling","dft-convolution"]),
 inf("S5.4","Polynomial products in the ring are computed by signed packing and the $O(n\\log n)$ multiplier as a subroutine.","reduction is a signed form of Kronecker substitution; compare",page="signed-packing",frm=["poly-ring-y-r-1","synthetic-transforms"]),
]
S5=[S5x[3],S5x[1],S5x[2],S5x[0]]
root={"id":"S0","intention":"show","claim":"A fixed deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "method":"reduce the product to convolution over a polynomial ring, speed up its transforms with two tape procedures having a recursive power saving, then recover the exact product by rounding",
 "motivation":mot("Plain transforms cost n log n by scanning n bits at each of log n levels, so the logarithmic factor itself must shrink; this needs a faster tape procedure for data movement and arithmetic, plus a reduction placing multiplication where those procedures apply.","explicit","Scanning an array of $\\Theta(n)$ stored bits at each of"),
 "page":"main-theorem","from":["nlogn-conjecture","big-o","multitape-tm","dft-convolution","logarithms-and-floor-ceiling"],
 "salient":"The saving is a genuine power of the logarithm, but with the astronomically small exponent kappa=2^-182.",
 "children":[
  inf("S1","Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.","Splitting the inputs into radix digits reduces multiplication to",page="radix-digit-convolution",frm=["dft-convolution","binary-representation-of-integers","schoolbook-multiplication-and-basic-divide-and-conquer"],deferred=True),
  inf("S2","One coordinate is stored as a polynomial modulo $y^r+1$, so powers of $y$ are roots of unity.","For an integer $r\\geq 2$ that is a power of two, put",page="poly-ring-y-r-1",frm=["polynomials","complex-numbers","roots-of-unity"]),
  inf("S3","Multiplication by a root of unity in the remaining axes is a signed shift, so synthetic transforms consist of shifts, butterflies and rearrangements.","For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",page="synthetic-transforms",frm=["poly-ring-y-r-1","dft-convolution"]),
  {"id":"S4","intention":"show","claim":"The address rearrangements and butterfly layers of the synthetic transforms cost $O(Vu^\\tau)$ and $O(Vd^{\\lambda'})$ for stored bit volume $V$, a power saving below the linear-per-level cost.",
   "method":"build each procedure from a fixed linear network whose smaller calls number $s<Wm$ and recurse","page":None,"from":[],
   "motivation":mot("Each procedure is a fixed network whose edges are smaller calls of the same procedure; a rank saving s<Wm makes the recursion beat linear cost per level, so the networks, their saving and the two instances are shown in that order.","explicit","The decisive property is that the total"),
   "adds":[{"symbol":"V","name":"stored bit volume","meaning":"The number of bits stored in the array being processed.","relation":"count"},
          {"symbol":"W","name":"number of roles","meaning":"The number of wire positions (roles) in the network.","relation":"count"},
          {"symbol":"m","name":"subspace dimension","meaning":"The dimension of the fixed space whose subspaces are attached to gates.","relation":"count"},
          {"symbol":"s","name":"number of calls","meaning":"The number of smaller calls the network uses.","relation":"count"}],
   "children":S4},
  {"id":"S5","intention":"show","claim":"The convolution of the digit list is computed by convolution over the polynomial ring using the transforms of S4.",
   "method":"chain of reductions taken from the ring end: ring products, resampling and chirps, then the prime-axis address map","page":None,"from":[],
   "motivation":mot("The fast procedures only apply to power-of-two axes over the polynomial ring, so the digit convolution is moved there step by step while preserving convolution.","recoverable"),
   "children":S5},
  inf("S6","Known normalizations are removed, the coefficient error is below $1/2$, and rounding with carry propagation gives the exact binary product.","less than $1/2$; it also justifies the rounding, carries, and output",page="fixed-point-precision",frm=["floating-and-fixed-point-numbers-and-rounding","bluestein-chirp"]),
  inf("S7","A compatible choice of rational parameters makes every term of the cost table fit $O(n(\\lg n)^{1-\\kappa})$.","For the cost calculation put $V=Tp=\\Theta(n)$. The fixed-width coefficient",frm=[])
 ]}
c=root["children"]; root["children"]=[c[0],c[3],c[1],c[2],c[4],c[5],c[6]]
json.dump({"root":root},open("exegenius/tasks/0003-argument.answer.json","w"),indent=1)
