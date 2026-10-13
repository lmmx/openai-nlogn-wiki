import json
P="paper"
def E(*q): return [{"source":P,"quote":x} for x in q]
def S(s,n,m,r="direct"): return {"symbol":s,"name":n,"meaning":m,"relation":r}
C=[]
def add(id,name,gloss,req,ev=None,known=False,title=None,symbols=None,aliases=None):
    d={"id":id,"name":name,"aliases":aliases or [],"gloss":gloss,"requires":req,"known":known,"evidence":ev or []}
    if title: d["title"]=title; d["symbols"]=symbols
    C.append(d)
add("big-o","Big-O notation","Asymptotic upper-bound notation for running time.",[],known=True)
add("polynomials","Polynomials","Expressions in a variable with coefficients, added and multiplied termwise.",[],known=True)
add("complex-numbers","Complex numbers","Numbers a+bi with roots of unity and arithmetic.",[],known=True)
add("multitape-tm","Multitape Turing machine","Deterministic machine with finite alphabet and a fixed finite number of tapes, one cell read/written per tape per step.",[],known=True)
add("multiplication-history","Integer multiplication complexity and the n log n conjecture","Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).",["multitape-tm","big-o"],
 E("proposed $n\\log n$ as the optimal order of growth","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper"))
add("convolution","Convolution","Combining two coefficient sequences so each output sums products of entries whose indices add; this is polynomial multiplication.",["polynomials"],
 E("Splitting the inputs into radix digits reduces multiplication to\nconvolution of short integer coefficients."))
add("dft-fft","Discrete Fourier transform and butterflies","Evaluating a sequence at roots of unity, turning convolution into pointwise products, computed by log-depth layers of two-point butterfly operations.",["convolution","complex-numbers"],
 E("two-point butterfly operations","the transform calculation consists of address\nrearrangements, signed shifts, and two-point butterfly operations"))
add("digit-convolution-reduction","Multiplication by radix-digit convolution","Split each integer into radix digits, convolve digit lists, then recover exact integer by rounding, rescaling and carry propagation.",["convolution","dft-fft"],
 E("This produces the radix-$2^b$ digits", "Splitting the inputs into radix digits reduces multiplication to","propagates carries to\nobtain the exact binary product"))
add("cyclic-crt-axes","Chinese-remainder map to prime cyclic axes","A Chinese-remainder address map placing the digit list on a product of cyclic axes of distinct prime lengths, preserving convolution.",["convolution"],
 E("placed on a product of\ndistinct prime cyclic axes by a Chinese-remainder map that preserves\nconvolution"))
add("multidim-transform","Multidimensional transform","A Fourier transform on an array with several axes, applied along each axis in turn.",["dft-fft"],
 E("multidimensional transforms whose axis lengths are\npowers of two"))
add("gaussian-resampling","Gaussian resampling","Harvey–van der Hoeven identity expressing a Fourier transform of prime-length axes through a power-of-two tensor transform, with source and target permutations.",["multidim-transform","cyclic-crt-axes"],
 E("Resampling without executing the two permutations", "Tensor interface", "Gaussian\nresampling then expresses each source Fourier transform through a\npower-of-two tensor transform","Gaussian-resampling reduction of Harvey and van der Hoeven"))
add("bluestein-chirp","Bluestein chirp identity","Rewrites a Fourier transform of arbitrary length as a convolution multiplied by chirp phases.",["convolution","dft-fft"],
 E("Chirp and permutation cancellation", "Bluestein's chirp identity converts the middle transform"))
add("poly-ring-negacyclic","Polynomial ring modulo y^r + 1","Complex polynomials in y of degree below r with y^r = -1; powers of y act as roots of unity and multiplying by them is a signed shift of coefficients.",["polynomials","complex-numbers"],
 E("one coordinate\nis stored as the coefficient list of a polynomial modulo $y^r+1$","multiplication by\nsuch a root is a signed shift of the coefficient list"),
 title="Polynomial ring modulo $y^r+1$",symbols=[S("y","polynomial variable","The indeterminate whose powers serve as roots of unity."),S("r","ring size","The power of two giving the number of coefficients in a polynomial; y^r+1 = 0.","count")])
add("phase-twist","Last-coordinate phase twist","Multiplying by diagonal phases so a cyclic coordinate becomes a negative-wrap (mod y^r+1) coordinate; removing the twist restores cyclic wrap.",["poly-ring-negacyclic","bluestein-chirp"],
 E("A phase twist changes the last cyclic coordinate into a polynomial\nmodulo $y^r+1$"))
add("synthetic-transforms","Synthetic polynomial transforms","Nussbaumer-style transforms using powers of y as roots of unity so each twiddle multiplication is a shift.",["poly-ring-negacyclic","multidim-transform"],
 E("Synthetic character cancellation", "These are the\nsynthetic polynomial transforms of Nussbaumer and Quandalle and\nNussbaumer"))
add("normalized-ring-products","Packed polynomial products","Pointwise polynomial products in the ring computed via signed packing (Kronecker substitution) and the standard O(n log n) multiplier as a subroutine.",["poly-ring-negacyclic","multiplication-history"],
 E("Signed packing and normalized ring multiplication", "Their polynomial products\nuse signed packing and the established $O(n\\log n)$ multiplier as an\nordinary subroutine."))
add("tape-streams","Tape scans and address layout","Arrays stored in address order on tapes; scans move data in linear time but rearranging address fields with growing digit counts is costly.",["multitape-tm"],
 E("takes $O(V)$ steps on a fixed number of one-dimensional tapes", "We distinguish moving one\ndigit in a fixed radix, which needs a bounded number of scans, from\ninterchanging fields whose numbers of digits grow."))
add("address-interchange-bottleneck","Address rearrangement cost","Scanning Θ(n) bits at each of Θ(log n) levels costs n log n, so both movement and arithmetic must be cheapened.",["tape-streams","dft-fft"],
 E("Scanning an array of $\\Theta(n)$ stored bits at each of\n$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$."))
add("linear-network-roles","Linear networks, roles and frames","A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; wires have roles and invertible frames D_v change the stored representation, cancelling across the network.",["tape-streams","polynomials"],
 E("For arbitrary initial values of its auxiliary wires, a forward\ninvocation changes $y_S$ to $y_S+x_S$ and leaves every other value\nunchanged.", "A wire's fixed place in the network is called its role.","We call $D_v$ its frame"))
add("finite-subset-network","Finite network from three-element subsets","Fixed network with nested subspaces attached to gates, built using three-element subsets and gather/scatter with cancelling auxiliary wires, giving s<Wm smaller calls.",["linear-network-roles"],
 E("Every edge joins comparable nondegenerate labels.", "The construction uses\nthree-element subsets","The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$."))
add("recursive-saving","Recursive saving giving a power of log","Calling parameter mf uses s<Wm calls at parameter f on volume V/W each, so cost per volume grows by factor s/W<m per multiplication of the parameter, giving a power saving.",["finite-subset-network","big-o"],
 E("This strict inequality\nis the source of the power saving."))

add("address-shear-factorization","Rational matrix shear and lower-triangular factorization","Every rational matrix factors as lower-triangular times partial permutation times lower-triangular, so an address shear (H,D)->(H+D,D) costs by rank.",["tape-streams","polynomials"],
 E("Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization","Lower triangular factorization"))
add("controlled-shifts","Controlled shifts and rational scalings","Linear-time stream operations adding control-field-dependent offsets to a target field.",["tape-streams"],
 E("Controlled shifts and fixed rational scalings"))
add("packed-selected-bit-addition","Packed selected-bit addition","Adds selected bit positions across grouped rectangles of packed records on tapes, used inside fast butterfly layers.",["tape-streams","fixed-point-dyadics"],
 E("Packed selected-bit addition on one rectangle","Packed selected-bit addition for grouped rectangles"))
add("fast-address-interchange","Fast address-field interchange","Interchanges two contiguous address fields via XOR combinations of data and address shears, with an exact final permutation.",["recursive-saving","address-interchange-bottleneck","address-shear-factorization","controlled-shifts"],
 E("in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.", "Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."),
 title="Fast interchange of $u$-bit address fields at cost $O(Vu^\\tau)$",
 symbols=[S("V","stored bit volume","The number of stored bits in the array.","count"),S("u","field width","The number of bits in each interchanged address field.","count"),S("\\tau","cost exponent","A fixed constant below 1 giving the power saving.")])
add("fixed-point-dyadics","Fixed-point complex dyadics","Complex numbers with power-of-two denominators used exactly in intermediate values and truncated once after a contractive layer.",["complex-numbers"],
 E("Intermediate values are exact Gaussian dyadics"))
add("fast-butterfly-layers","Simultaneous butterfly layers","Applies H_0(u,v)=((u+v)/2,(u-v)/2) to selected coordinate bits of numerical arrays, via the linear network, at cost O(V d^λ').",["recursive-saving","dft-fft","fixed-point-dyadics","synthetic-transforms","packed-selected-bit-addition","controlled-shifts"],
 E("Simultaneous normalized butterfly layer", "Each record is a polynomial with complex fixed-point coefficients, and\n$H_0$ acts coefficientwise."),
 title="Simultaneous butterfly layer $H_0$ at cost $O(Vd^{\\lambda'})$",
 symbols=[S("H_0","butterfly map","The map sending (u,v) to ((u+v)/2,(u-v)/2)."),S("V","stored bit volume","The number of stored bits in the arrays.","count"),S("d","chunk count","The number of equal-width address chunks in which one bit position is selected.","count"),S("\\lambda'","cost exponent","A fixed constant below 1 giving the power saving.")])
add("precision-exact-recovery","Precision analysis and exact recovery","Bounds the rounding error of the whole fixed-point pipeline strictly below 1/2, removes normalizations and propagates carries.",["fixed-point-dyadics","digit-convolution-reduction"],
 E("Precision and exact recovery", "proves that the recovered\ncoefficient error is strictly below $1/2$"))
add("main-theorem","Integer multiplication in O(n (lg n)^(1-κ)) time","Deterministic multitape TM multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, disproving the n log n conjecture in that model.",
 ["multiplication-history","gaussian-resampling","bluestein-chirp","phase-twist","synthetic-transforms","normalized-ring-products","fast-address-interchange","fast-butterfly-layers","precision-exact-recovery","digit-convolution-reduction"],
 E("The complete time bound", "These constants are deliberately conservative; no optimization is claimed.", "T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right)","disproves the $n\\log n$ optimality conjecture"),
 title="Multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
 symbols=[S("n","input length","The number of bits of each integer.","count"),S("\\kappa","saving exponent","The constant 2^{-182} giving the power saving in the log factor.")])
json.dump({"target":"main-theorem","concepts":C},open("/home/user/openai-nlogn-wiki/runs/C2/exegenius/tasks/0001-extract.answer.json","w"),indent=1)
