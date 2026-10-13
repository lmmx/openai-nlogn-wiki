import json
P=lambda q:{"source":"paper","quote":q}
C=[]
def c(id,name,gloss,req,ev=(),known=False,title=None,symbols=None,aliases=()):
    d={"id":id,"name":name,"aliases":list(aliases),"gloss":gloss,"requires":list(req),"known":known,"evidence":[P(q) for q in ev]}
    if title: d["title"]=title; d["symbols"]=symbols
    C.append(d)
def b(s,n,m,r="direct"): return {"symbol":s,"name":n,"meaning":m,"relation":r}
c("big-o","Big-O notation","Asymptotic upper bound notation.",[],known=True)
c("polynomials","Polynomials","Polynomials and arithmetic on them.",[],known=True)
c("complex-numbers","Complex numbers","Complex arithmetic, modulus, roots of unity.",[],known=True)
c("turing-tapes","Basic Turing machines and tapes","Turing machines with tapes and heads.",[],known=True)
c("multitape-model","Fixed multitape machine model and scans","A Turing machine with one fixed finite alphabet and a fixed number of one-dimensional tapes; moving data is paid for by scanning tapes, so a pass over n bits costs Θ(n).",["turing-tapes","big-o"],
  ["A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.","Scanning an array of $\\Theta(n)$ stored bits at each of"])
c("conjecture","Schönhage–Strassen n log n conjecture and history","Schönhage and Strassen's 1971 O(n log n log log n) multiplication and their conjecture that n log n is optimal, with Harvey–van der Hoeven's O(n log n) the previous best.",["multitape-model"],
  ["proposed $n\\log n$ as the optimal order of growth","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper"])
c("dft-convolution","Discrete Fourier transform and cyclic convolution","The length-q DFT (normalized by 1/q) turns cyclic convolution into pointwise multiplication; inverse transform has opposite sign in the exponent.",["complex-numbers"],
  ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q},","Each normalized Fourier transform above is a contraction"])
c("radix-digit-convolution","Multiplication as convolution of radix digits","Writing both integers in a radix turns their product into a convolution of short integer coefficient lists, followed by carry propagation.",["dft-convolution","polynomials"],
  ["Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients."])
c("kronecker-packing","Signed Kronecker packing","Packing polynomial coefficients (including negative ones) into one large integer so that a polynomial product becomes an integer product.",["polynomials"],
  ["The reduction is a signed form of Kronecker substitution"])
c("hvdh-multiplier","Harvey–van der Hoeven O(n log n) multiplier as subroutine","The established O(N log N) fixed-tape integer multiplier, used as an ordinary subroutine for short polynomial records.",["conjecture","kronecker-packing"],
  ["we use the fixed-tape integer multiplier of Harvey and van der Hoeven"])
c("crt-prime-axes","Chinese-remainder map to prime cyclic axes","A Chinese-remainder address map placing the coefficient list on a product of distinct prime cyclic axes, preserving convolution.",["dft-convolution","multitape-model"],
  ["Chinese-remainder map that preserves convolution"])
c("gaussian-resampling","Gaussian resampling","Harvey–van der Hoeven's method expressing a Fourier transform of coprime length through a power-of-two tensor transform, via Gaussian-weighted interpolation.",["dft-convolution","crt-prime-axes"],
  ["Gaussian resampling connects these two shapes.","Its usual implementation sorts twice on each coordinate."])
c("bluestein-chirp","Bluestein chirp identity","Rewrites a DFT of arbitrary length as a cyclic convolution sandwiched between pointwise phase (chirp) multiplications.",["dft-convolution"],
  ["Next, Bluestein's chirp identity converts the middle transform,"])
c("ring-y-r","Polynomial ring modulo y^r + 1","The ring of polynomials over ℂ modulo y^r+1, where powers of y are roots of unity and multiplication by y^a is a signed cyclic shift of coefficients; norm is the max coefficient modulus.",["polynomials","complex-numbers"],
  ["\\mathcal R_r=\\mathbb C[y]/(y^r+1),","A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$"],
  title="Polynomial ring modulo $y^r + 1$",symbols=[b("y","indeterminate","The formal variable of the polynomials."),b("r","ring size","The number of complex coefficients in a record, a power of two.","count")])
c("synthetic-transform","Synthetic polynomial transforms","Nussbaumer–Quandalle transforms over the ring with roots of unity ω_t = y^{2r/t} acting as signed shifts, computed by radix-two butterflies; frequency order is retained through the pointwise product.",["ring-y-r","dft-convolution"],
  ["For a power of two $t$ dividing $2r$, define","The polynomial roots and radix-two butterflies belong to the fast"])
c("phase-twist","Phase twist to the polynomial ring","A phase multiplication converting the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap after untwisting.",["ring-y-r","bluestein-chirp"],
  ["A phase twist changes the last cyclic coordinate into a polynomial"])
c("retained-permutations","Retained permutations cancelling in transforms","Keeping the source and target coordinate permutations of resampling inside the transform formula so that they cancel across the forward transforms, product and inverse instead of being sorted.",["gaussian-resampling","bluestein-chirp","synthetic-transform"],
  ["We retain both permutations in the transform formula and compute that formula directly."])
c("fixed-point-precision","Fixed-point precision and exact recovery","Complex values are stored on a 2^{-p} grid with truncation errors; composing contractive approximations adds errors, and final coefficient error below 1/2 lets rounding and carries recover the exact integer product.",["complex-numbers","dft-convolution"],
  ["the recovered coefficient error is strictly below $1/2$","Composing such algorithms adds their errors"])
c("gaussian-dyadics","Exact Gaussian dyadic arithmetic with single truncation","Intermediate values are kept exactly as complex numbers with power-of-two denominators, with one truncation after a completed contractive layer.",["fixed-point-precision"],
  ["Intermediate values are exact Gaussian dyadics,","A single\ntruncation follows the completed contractive layer."])
c("butterfly-h0","Simultaneous butterfly layer H₀","The two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) applied coefficientwise to selected coordinate bits of many address chunks at once.",["ring-y-r","synthetic-transform"],
  ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)"],
  title="Butterfly layer $H_0(u,v)$",symbols=[b("H_0","butterfly map","The map sending a pair of values to their half-sum and half-difference."),b("u","first value","The first input of the two-point butterfly."),b("v","second value","The second input of the two-point butterfly.")])
c("linear-network-frames","Linear exchange networks with frames and roles","A fixed linear network of gates on wires (roles) exchanging two banks of values and restoring auxiliary values; with invertible frames D_v per vertex, gates act pointwise and intermediate frames cancel, leaving an endpoint operator on each role array.",["multitape-model","polynomials"],
  ["A wire's fixed place in the network is called its role.","We call $D_v$ its frame","and restores every auxiliary value."])
c("subset-intersection-network","Three-element subset construction with rank saving","Subspaces of an m-dimensional space labelled by three-element subsets, using gather/scatter and auxiliary wires, make adjacent edge operators nested so the total number s of smaller calls is less than W·m.",["linear-network-frames"],
  ["The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.","The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$."])
c("recursive-power-saving","Recursive power saving from s < Wm","A recursive call at parameter mf uses s calls at parameter f on volume V/W each, so the per-volume cost multiplies by s/W < m, giving cost V·(parameter)^θ with θ<1.",["subset-intersection-network","big-o"],
  ["This strict inequality is the source of the power saving."])
c("lower-triangular-shear","Address shear and lower triangular factorization","Bruhat-style factorization into lower triangular factors with reversed coordinate order; a shear (H,D)→(H+D,D) updates later fields from earlier ones in linear time on tape.",["multitape-model","polynomials"],
  ["updated by $(H,D)\\mapsto(H+D,D)$","Lower triangular changes of coordinates"])
c("chunk-interchange","Interchange of address chunks in time O(Vu^τ)","Interchanging two disjoint contiguous u-bit address fields of an array by XOR combinations of intermediate data and the bit network, with exact final permutation for arbitrary auxiliary values.",["recursive-power-saving","lower-triangular-shear"],
  ["The first procedure interchanges two disjoint contiguous address fields","Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$.","its intermediate steps form pointwise XOR combinations of data"],
  title="Address chunk interchange in time $O(Vu^\\tau)$",symbols=[b("V","bit volume","The number of stored bits in the array.","count"),b("u","field width","The number of bits in each interchanged address field.","count"),b("\\tau","saving exponent","A fixed constant less than 1 in the cost exponent.")])
c("phase-frames","Phase frames for simultaneous butterflies","Diagonal phase frames express a tensor product of the auxiliary kernel C on many selected bits via smaller groups of bits separated by binary changes of basis implemented as whole-chunk moves.",["linear-network-frames","butterfly-h0","chunk-interchange","gaussian-dyadics"],
  ["frames express a $C$ tensor product using smaller groups of selected bits"])
c("fast-butterfly-layer","Fast simultaneous butterfly layer in time O(Vd^λ′)","Applying H₀ to the same bit in d address chunks of the polynomial array in cost O(V d^λ′) instead of d full passes.",["phase-frames","recursive-power-saving","ring-y-r"],
  ["We will obtain cost $O(Vd^{\\lambda'})$"],
  title="Simultaneous butterfly layer in time $O(Vd^{\\lambda'})$",symbols=[b("V","bit volume","The logical number of stored bits in the array.","count"),b("d","chunk count","The number of selected address chunks, at most the bound on active axes.","count"),b("\\lambda'","saving exponent","A fixed constant less than 1.")])
c("transform-layout","Synthetic transform layout and convolution","Layout on tape on which the parallel layers apply and the pointwise-multiplied transforms are inverted, with polynomial products by signed packing and the Harvey–van der Hoeven multiplier.",["synthetic-transform","fast-butterfly-layer","chunk-interchange","hvdh-multiplier","kronecker-packing"],
  ["To multiply the polynomial records, we use the fixed-tape integer"])
c("tensor-resampling","Tensor resampling over growing dimension","Applying one-dimensional resampling maps line by line over many coordinates, with axis movement done by chunk interchange.",["gaussian-resampling","retained-permutations","chunk-interchange"],
  ["The chunk-swap algorithm supplies the movement of the physical axis fields"])
c("parameter-choice","Compatible parameter choice and cost accounting","A fixed rational choice (τ, λ′, ε, κ=2^{-182}, ...) making all cost terms fit the final bound.",["transform-layout","tensor-resampling","fixed-point-precision"],
  ["These constants are deliberately conservative; no optimization is claimed."])
c("main-theorem","Integer multiplication in O(n (lg n)^(1−κ)) time","Deterministic fixed-tape machine multiplying n-bit integers exactly in O(n(lg n)^{1−κ}) with κ=2^{-182}, refuting the n log n optimality conjecture; built from radix convolution, CRT axes, Gaussian resampling, chirps, the polynomial ring and fast chunk and butterfly operations.",
  ["conjecture","radix-digit-convolution","crt-prime-axes","phase-twist","parameter-choice","tensor-resampling","transform-layout","fixed-point-precision"],
  ["disproves the $n\\log n$ optimality conjecture","computes this exact product for every $n\\ge1$ and every pair of $n$-bit"],
  title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",symbols=[b("n","input length","The number of bits in each operand.","count"),b("\\kappa","power saving","The constant 2^{-182} in the exponent.")])
json.dump({"target":"main-theorem","concepts":C},open("/home/user/openai-nlogn-wiki/runs/C4/exegenius/tasks/0001-extract.answer.json","w"),ensure_ascii=False,indent=1)
