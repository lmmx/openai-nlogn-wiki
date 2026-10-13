import json
P="paper"
cs=[]
def c(id,name,gloss,req,ev=(),known=False,title=None,symbols=None,aliases=()):
    d=dict(id=id,name=name,aliases=list(aliases),gloss=gloss,requires=list(req),known=known,evidence=[dict(source=P,quote=q) for q in ev])
    if title: d["title"]=title; d["symbols"]=symbols
    cs.append(d)
def sym(s,n,m,r="direct"): return dict(symbol=s,name=n,meaning=m,relation=r)

c("big-o","Big-O notation","Asymptotic upper bounds on running time.",[],known=True)
c("polynomials","Polynomials","Polynomials, their coefficients, multiplication and reduction modulo a polynomial.",[],known=True)
c("complex-numbers","Complex numbers","Complex arithmetic, roots of unity and the unit circle.",[],known=True)
c("basic-turing-machines","Turing machines and tapes","Basic Turing machines with tapes, heads and steps.",[],known=True)

c("multitape-model","Fixed multitape Turing machine model","The computation model: one fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step reading/writing one cell per tape and moving each head by at most one cell; time is the number of steps.",["basic-turing-machines","big-o"],
  ["A machine has one fixed finite alphabet and one fixed finite number of","one-dimensional tapes. A step reads and writes at most one cell on each","tape and moves each head by at most one cell."][:0] or ["A machine has one fixed finite alphabet and one fixed finite number of"])
c("nlogn-conjecture","Multiplication history and the n log n conjecture","Schönhage–Strassen's O(n log n log log n) multiplier, their conjecture that n log n is optimal, and the Harvey–van der Hoeven O(n log n) algorithm that the paper beats by a power of log n.",["multitape-model","big-o"],
  ["and proposed $n\\log n$ as the optimal order of growth","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper"])
c("convolution-dft","Convolution and the discrete Fourier transform","Cyclic convolution of coefficient lists, and the DFT that turns it into pointwise multiplication; the inverse transform uses the opposite-sign root and a 1/size normalization.",["polynomials","complex-numbers"],
  ["Splitting the inputs into radix digits reduces multiplication to","$F_t^+F_t^-=t^{-1}I.$"][:1])
c("radix-digit-convolution","Multiplication as convolution of radix digits","Splitting each n-bit operand into short radix-2^b digits turns integer multiplication into a convolution of small integer coefficient lists, followed by rounding and carry propagation to get the exact binary product.",["convolution-dft"],
  ["Splitting the inputs into radix digits reduces multiplication to","convolution of short integer coefficients."])
c("fft-butterfly","FFT butterflies","A two-point butterfly combines two values u,v into (u+v)/2 and (u-v)/2; an FFT is built from layers of these acting on address bits, one layer per level, so scanning the array at each level costs n log n.",["convolution-dft","big-o"],
  ["Scanning an array of $\\Theta(n)$ stored bits at each of","$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$."])
c("negacyclic-ring","Polynomial ring modulo y^r + 1","Complex polynomials of degree below r with multiplication reduced by y^r = −1; powers of y act as roots of unity and multiplying by one is a signed shift of the coefficient list.",["polynomials","complex-numbers"],
  ["one coordinate\nis stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two."] if False else ["is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two."],
  title="Polynomial ring modulo $y^r + 1$",
  symbols=[sym("y","polynomial variable","The formal variable of the polynomial, whose powers play the role of roots of unity."),
           sym("r","ring length","The number of complex coefficients in a polynomial; a power of two and the degree bound of the ring elements.","count")])
c("synthetic-transforms","Synthetic polynomial transforms","Nussbaumer-style Fourier transforms over the negacyclic ring in which roots of unity are powers of y, so multiplications by roots are signed shifts and only butterflies and shifts remain; forward transforms keep the same frequency order and the opposite transform consumes it.",["negacyclic-ring","fft-butterfly"],
  ["synthetic polynomial transforms of Nussbaumer and Quandalle and"," serve as roots of unity in the remaining axes, and multiplication by"][:1])
c("multidimensional-transform","Multidimensional transforms with tensor structure","A transform on an array indexed by several axes is the tensor product of one-dimensional transforms along each axis; the paper uses d axes of power-of-two length.",["convolution-dft"],
  ["it replaces the Fourier transforms needed for"," this convolution by multidimensional transforms whose axis lengths are"][:1])
c("crt-address-map","Chinese-remainder coefficient address map","Map Φ placing the radix-digit coefficient list on a product of pairwise-coprime cyclic axes by the Chinese remainder theorem so that convolution is preserved, implemented by triangular controlled shifts.",["convolution-dft","multidimensional-transform","controlled-shifts"],
  ["Agarwal and Cooley used the Chinese remainder"])
c("gaussian-resampling","Gaussian resampling","The Harvey–van der Hoeven identity expressing a Fourier transform of prime-ish length s through a transform of power-of-two-axis length t via contractive Gaussian maps A and B; the paper keeps the source and target coordinate permutations inside the identity instead of sorting.",["multidimensional-transform","fixed-point-precision"],
  ["Gaussian resampling\nthen expresses each source Fourier transform through a"] if False else ["Our starting point is the"," Gaussian-resampling reduction of Harvey and van der Hoeven"][:0] or ["Gaussian-resampling reduction of Harvey and van der Hoeven"])
c("bluestein-chirp","Bluestein chirp conversion","Bluestein's chirp identity rewrites a Fourier transform (with its permutation) as a pointwise chirp multiplication around a cyclic convolution, and permutations cancel across the two forward transforms and the inverse.",["convolution-dft","negacyclic-ring","gaussian-resampling"],
  ["Next, Bluestein's chirp identity converts the middle transform,"])
c("coefficient-twist","Phase twist from cyclic to negacyclic","Twisting coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution of length r to the ring modulo y^r+1, whose negative wrap restores the cyclic wrap.",["negacyclic-ring","complex-numbers"],
  ["A phase twist changes the last cyclic coordinate into a polynomial"])
c("signed-packing-products","Signed packing of polynomial products","Kronecker-substitution style packing of ring elements with Gaussian-integer coefficients into long integers, multiplied by the established O(n log n) multiplier used as an ordinary subroutine.",["negacyclic-ring","nlogn-conjecture","fixed-point-precision"],
  ["Signed coefficient"," packing is a form of Kronecker substitution"][:0] or ["use signed packing and the established $O(n\\log n)$ multiplier as an"])
c("fixed-point-precision","Dyadic fixed-point arithmetic and rounding","Complex coefficients stored as fixed-point Gaussian dyadics with p fractional bits; exact intermediate values, a single truncation after contractive layers, and error tracking so the final coefficient error is below 1/2.",["complex-numbers","multitape-model"],
  ["Intermediate values are exact Gaussian dyadics,","proves that the recovered"][:1])
c("stream-scans","Array order and elementary stream operations","Arrays are stored in lexicographic order with implicit addresses; splitting by digits, moving a digit, and splitting rows among roles are linear-time scans.",["multitape-model"],
  ["An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in"])
c("controlled-shifts","Controlled shifts and rational scalings","Updating a later address field by an offset computed from earlier control fields, or multiplying it by a rational unit mod q^b, in linear time using whole-block splits and merges.",["stream-scans"],
  ["\\begin{lemma}[Controlled shifts and fixed rational scalings]"])
c("linear-network-frames","Linear networks with frames","A fixed network of pointwise linear gates on wires (roles); giving each vertex an invertible frame operator D_v acting on address-indexed arrays lets gates stay pointwise while edges apply D_v D_u^{-1}, leaving an endpoint operator on every role.",["stream-scans","polynomials"],
  ["We call $D_v$ its frame: the stored","array is $D_vg$ when the logical array is $g$."])
c("subset-subspace-networks","Finite networks from three-element subsets","Two fixed networks (a bit network over Q and a complex Gaussian-dyadic one over F_2) with nested subspace labels built from triples of [h], whose edge rank changes sum to s < Wm; this strict deficit is the source of the power saving.",["linear-network-frames"],
  ["The decisive property is that the total","number $s$ of smaller calls satisfies $s<Wm$."])
c("recursive-saving","Recursive power saving","A call at parameter mf uses s < Wm calls at parameter f on streams of volume V/W, so the per-volume cost grows by a factor s/W < m when the parameter is multiplied by m, giving cost V·e^τ with τ<1.",["subset-subspace-networks","big-o"],
  ["is the source of the power saving."])
c("lower-triangular-shear","Lower triangular factorization and matrix shear","Every rational matrix factors as E1·Π·E2 with E1,E2 lower triangular, so a coordinate change on address fields is a sequence of controlled shifts in tape order and costs O(V) times a rank-dependent number of smaller operations.",["controlled-shifts"],
  ["\\begin{lemma}[Lower triangular factorization]"])
c("address-interchange","Fast address-field interchange","Interchange of two disjoint contiguous address fields of u digits in time O(V u^τ) with a fixed τ<1, via XOR combinations of intermediate streams that finally give an exact permutation for arbitrary auxiliary values.",["recursive-saving","lower-triangular-shear","subset-subspace-networks"],
  ["Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$.","The final permutation is","exact for arbitrary initial auxiliary values."],
  title="Address-field interchange in time $O(Vu^\\tau)$",
  symbols=[sym("V","stored bit volume","The number of stored data bits in the array.","count"),
           sym("u","field width","The number of radix digits in each of the two interchanged address fields.","count"),
           sym("\\tau","interchange exponent","A fixed constant strictly less than one controlling the cost.")])
c("simultaneous-butterfly-layer","Fast simultaneous butterfly layer","Applying the H_0 butterfly on the same bit position of d address chunks at once, using phase frames, binary changes of basis by chunk moves and the recursive saving, in time O(V d^λ') instead of d whole-array passes.",["recursive-saving","address-interchange","fft-butterfly","fixed-point-precision","negacyclic-ring"],
  ["and the cost is $O(Vd^{\\lambda'})$ for a","fixed $\\lambda'<1$."],
  title="Simultaneous butterfly layer in time $O(Vd^{\\lambda'})$",
  symbols=[sym("V","stored bit volume","The number of stored data bits in the array.","count"),
           sym("d","number of chunks","The number of equal-width address chunks (axes) whose selected bit gets a butterfly simultaneously.","count"),
           sym("\\lambda'","layer exponent","A fixed constant strictly less than one controlling the cost.")])
c("transform-layout-cost","Synthetic transform layout and convolution cost","Arranging the array so the simultaneous layers apply with frequency order retained, giving a convolution over the ring from two forward transforms, a pointwise product (via signed packing) and an opposite transform at cost O(Tp[dK+pK^{τ-1}+ℓd^{λ'}+log(rp)]).",["synthetic-transforms","simultaneous-butterfly-layer","address-interchange","signed-packing-products"],
  ["\\begin{lemma}[Transform layout and cost]"])
c("resampling-no-sort","Resampling without executing the permutations","Lemma stating P_sF_s = 2^{2α²} B_0 P_tF_t A with coordinate permutations kept in the identity and tensored over d axes, so no full sorts are needed.",["gaussian-resampling","multidimensional-transform"],
  ["\\begin{lemma}[Resampling without executing the two permutations]"])
c("parameter-choice-cost","Parameter choice and total cost accounting","Choosing b=⌈log n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log T/d⌉} and fixed rational exponents with κ=2^{-182}, then summing the normalized cost table, every row of which is a power of p below 1.",["transform-layout-cost","resampling-no-sort","bluestein-chirp","crt-address-map","coefficient-twist","radix-digit-convolution"],
  ["Take the following fixed rational numbers:","The strict final inequality absorbs the logarithmic number of groups in"][:1])
c("main-theorem","Integer multiplication below n log n","A deterministic fixed multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it chains CRT map, Gaussian resampling, chirps, twist and synthetic transforms accelerated by the fast interchange and butterfly layers.",["parameter-choice-cost","nlogn-conjecture","radix-digit-convolution","fixed-point-precision"],
  ["computes this exact product for every $n\\ge1$ and every pair of $n$-bit","T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right),"])

c("scalar-motif-schedule","Gather–scatter schedule with restored scratch","Eight-row schedule of pointwise gates (subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy) that adds a source into a target for arbitrary initial scratch values and restores them; three such invocations exchange banks X,Y up to sign.",["subset-subspace-networks"],
  ["For arbitrary initial values of its auxiliary wires, a forward","invocation changes $y_S$ to $y_S+x_S$ and leaves every other value","(X_a,Y_a)\\longmapsto(-Y_a,X_a)","This cancellation of arbitrary initial scratch values is a linear"])
c("rank-budget-labels","Subspace labels and rank budget","Assigning nested nondegenerate subspaces to gates so that only the central-wire edges from time 3 to 4 decrease dimension (by h), giving a total dimension change Wm-2N+2L below Wm.",["scalar-motif-schedule"],
  ["Every edge joins comparable nondegenerate labels.  The only decreasing","edges are the central-wire edges from time 3 to time 4; their dimension","\\sum_{e}\\bigl|\\dim U_{\\mathrm{head}(e)}-","=Wm-2N+2L."][:3])
c("bit-network-interface","Bit network interface","The bit network (pointwise XOR gates, rational matrices) sends its input to a permutation with endpoint matrices differing by identity and total rational rank s_b < W_b m.",["rank-budget-labels"],
  ["The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,","M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m"])
c("complex-network-interface","Complex phase network interface","The complex network edges are products of translation kernels aI+bX_v, one per basis vector of the edge residual, with total length s_c < W_c m; telescoping gives C tensor m on every role.",["rank-budget-labels","phase-frames"],
  ["For each edge of the complex network, write $U,V$ for its tail and","After source and sink diagonal corrections, and undoing the signed"])
c("phase-frames","Phase frames for butterfly layers","With C = HSH = aI + bX (a=(1+i)/2, b=(1-i)/2) one has H_0 = b S C S, C^2 = X, C^4 = I, so a simultaneous butterfly layer is a scalar times S C^{⊗D} S, and C^{⊗D} is implemented by smaller groups via the complex network.",["fft-butterfly","complex-numbers"],
  ["C=H\\mathsf SH=aI+bX,\\qquad a=\\frac{1+i}{2},\\quad b=\\frac{1-i}{2}.","H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad","H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."])
c("packed-selected-bit-addition","Packed selected-bit addition","Linear-time XOR/addition of the bit at a common offset of several address chunks on rectangle or grouped-stream layouts, used to change selected address bits; exceptional addresses are repaired by sorting.",["stream-scans","controlled-shifts"],
  ["\\begin{lemma}[Packed selected-bit addition on one rectangle]","\\begin{lemma}[Packed selected-bit addition for grouped rectangles]","\\begin{definition}[Grouped packed stream]"])
c("synthetic-character-cancellation","Synthetic character cancellation and inversion","The sum of ω_t^{jk} over k is t if t divides j and 0 otherwise, hence F_t^+ F_t^- = t^{-1} I; the decimation-in-frequency recursion for the transform follows.",["synthetic-transforms"],
  ["\\begin{lemma}[Synthetic character cancellation]","(F_t^-z)_{2h+b}","\\|Q_p z-z\\|_\\infty<\\sqrt2\\,2^{-p},\\qquad"][:2])

extra={
"multitape-model":["For a binary string $x$ of length $n$, let $\\operatorname{val}(x)$ be"],
"fixed-point-precision":["\\|Q_p z-z\\|_\\infty<\\sqrt2\\,2^{-p},\\qquad","2^{2b+4}S\\cdot28\\,2^\\gamma T^2L\\cdot2^{-6b}","0\\le c_j\\le q(2^b-1)^2<2^{3b},"],
"synthetic-transforms":["(F_t^-z)_{2h+b}"],
"gaussian-resampling":["\\mathsf T P_sF_s=P_tF_t\\mathsf S,"],
"resampling-no-sort":["P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.","RF_{\\boldsymbol s}","\\begin{lemma}[Tensor interface]"],
"bluestein-chirp":["\\begin{lemma}[Chirp and permutation cancellation]","\\frac{u*v}{S^2}."],
"signed-packing-products":["\\begin{lemma}[Signed packing and normalized ring multiplication]","|h_j|\\leq r2^{2p}<2^{3p}<B_0/2."],
"transform-layout-cost":["\\begin{proposition}[Convolution from the retained transform layout]"],
"stream-scans":["\\begin{lemma}[Elementary stream operations]"],
"crt-address-map":["b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}."],
"lower-triangular-shear":["\\begin{lemma}[The cost of a rational matrix shear]"],
"address-interchange":["\\begin{proposition}[Power-width interchange with rows]","\\begin{lemma}[Arbitrary-width interchange]","F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."],
"recursive-saving":["F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."],
"simultaneous-butterfly-layer":["\\begin{proposition}[Simultaneous normalized butterfly layer]"],
"parameter-choice-cost":["\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16},\\\\","\\alpha\\le2(12d^2b)^{1/4},\\qquad"],
"bit-network-interface":[],
"subset-subspace-networks":["\\langle t_S,t_T\\rangle=|S\\cap T|-1,"],
}
for d in cs:
    for q in extra.get(d["id"],[]): d["evidence"].append(dict(source=P,quote=q))
json.dump(dict(target="main-theorem",concepts=cs),open("/home/user/openai-nlogn-wiki/runs/D5/exegenius/tasks/0001-extract.answer.json","w"),indent=1)
