import json
C=[]
def c(id,name,gloss,req=(),known=False,ev=(),title=None,symbols=None,aliases=()):
    d=dict(id=id,name=name,aliases=list(aliases),gloss=gloss,requires=list(req),known=known,
           evidence=[dict(source="paper",quote=q) for q in ev])
    if title: d["title"]=title
    if symbols: d["symbols"]=[dict(symbol=a,name=b,meaning=m,relation=r) for a,b,m,r in symbols]
    C.append(d)
D="direct";N="count"
c("big-o","Big-O notation","Asymptotic upper bounds on running time.",known=True)
c("polynomials","Polynomials","Sums of powers of a variable with coefficients, and their products.",known=True)
c("complex-numbers","Complex numbers","Numbers a+bi, with modulus, conjugates and roots of unity.",known=True)
c("multitape-tm","Turing machines and tapes","Basic Turing machines with tapes and heads.",known=True)
c("roots-of-unity","Roots of unity","Complex numbers whose powers return to 1, such as e^{2πi/q}.",known=True)

c("nlogn-conjecture","Schönhage–Strassen n log n conjecture and history","Schönhage and Strassen's 1971 multiplication bound O(n log n log log n) and their conjecture that n log n is optimal; later work (Fürer, Harvey–van der Hoeven) reached O(n log n) unconditionally.",
  ["big-o","multitape-tm"],ev=["proposed $n\\log n$ as the optimal order of growth","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper"])
c("fixed-tape-model","Fixed-tape machine model and cost of scans","One fixed finite alphabet and a fixed finite number of one-dimensional tapes; one step touches one cell per tape, so rearranging growing fields costs real time.",
  ["multitape-tm"],ev=["A machine has one fixed finite alphabet and one fixed finite number of","We distinguish moving one digit in a fixed radix"])
c("elementary-streams","Elementary stream operations and controlled shifts","Linear-time tape scans: swapping or moving a digit, splitting into streams and merging, and updating a field by an offset computed from earlier fields.",
  ["fixed-tape-model"],ev=["Each of the following operations on an array of","costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the"])
c("dft","Discrete Fourier transform","The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πi jk/q}; a contraction in the max norm.",
  ["complex-numbers","roots-of-unity","polynomials"],
  title="Normalized discrete Fourier transform $F_q$",
  symbols=[("F_q","transform","The normalized Fourier transform acting on vectors of length q.",D),("q","transform length","The number of coordinates of the vector being transformed.",N)],
  ev=["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}"],aliases=["Fourier transform"])
c("convolution","Cyclic convolution","Convolution of arrays on a product of cyclic groups; the transform turns it into a pointwise product, so convolutions are computed by transform, multiply, inverse transform.",
  ["dft","polynomials"],ev=["let $*$ denote cyclic convolution in the displayed","denotes cyclic convolution on the product of the coordinate groups"])
c("butterfly","Two-point butterfly H₀","The map H0(u,v)=((u+v)/2,(u−v)/2), the basic step of radix-2 fast transforms; a transform has about log n levels of butterfly layers.",
  ["dft"],title="Two-point butterfly $H_0$",
  symbols=[("H_0","butterfly map","The map sending a pair (u,v) to ((u+v)/2,(u-v)/2).",D)],
  ev=["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)"])
c("radix-digit-convolution","Multiplication as convolution of radix digits","Splitting each integer into radix-2^b digits turns the product into a convolution of short digit sequences, recovered into an integer by rounding and carry propagation.",
  ["convolution"],ev=["Splitting the inputs into radix digits reduces multiplication to","convolution of short integer coefficients"])
c("harvey-hoeven-multiplier","Established O(n log n) multiplier as a subroutine","The Harvey–van der Hoeven multitape integer multiplier with cost O(N log N), called as an ordinary subroutine on short inputs.",
  ["nlogn-conjecture"],ev=["Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine","with cost\n$O(N\\log(2N))$ on $N$-bit inputs".replace("\n"," ")])
c("fixed-point-contraction","Fixed-point grids, contractions and error","Values are complex numbers in the unit disk on a grid 2^-p Z[i]; maps that never grow the max norm (contractions) let truncation errors add rather than blow up.",
  ["complex-numbers","big-o"],ev=["Composing such algorithms\nadds their errors".replace("\n"," "),"Each normalized Fourier transform above is a contraction"])
c("ring-y-r-plus-1","Polynomial ring modulo y^r + 1","Polynomials with complex coefficients of degree < r where y^r = −1 (negacyclic); multiplying by a power of y is a signed shift of the coefficient list.",
  ["polynomials","complex-numbers"],title="Polynomial ring $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$",
  symbols=[("\\mathcal R_r","ring","The ring of complex polynomials in y of degree below r with y^r identified with -1.",D),("r","record length","The number of complex coefficients in a polynomial record; a power of two.",N),("y","ring variable","The polynomial variable, whose powers act as roots of unity.",D)],
  ev=["\\mathcal R_r=\\mathbb C[y]/(y^r+1)","Multiplication\nby $y^a$, for any integer $a$, permutes the coefficients and changes\nsome signs".replace("\n"," ")])
c("synthetic-transform","Synthetic polynomial transform","A Fourier transform over the ring R_r using ω_t = y^{2r/t} as root of unity, so twiddle multiplications are signed shifts; its inverse pairs are exact up to a factor.",
  ["ring-y-r-plus-1","dft","butterfly"],title="Synthetic transform $F_t^{\\pm}$ over $\\mathcal R_r$",
  symbols=[("F_t^{\\pm}","synthetic transform","The forward (+) or opposite (−) sign transform of length t over the ring.",D),("t","transform length","The number of ring entries along an axis; a power of two dividing 2r.",N),("\\mathcal R_r","ring","The polynomial ring modulo y^r+1.",D),("r","record length","The number of complex coefficients in a record.",N)],
  ev=["define $\\omega_t=y^{2r/t}$","The ring has zero divisors, so we verify character cancellation"])
c("bluestein-chirp","Chirp identity and permutation cancellation","Bluestein's identity rewrites the permuted transform Q F_t as a chirp multiplication, a cyclic convolution, and another chirp; the retained source permutation R cancels across two forward and one inverse transform.",
  ["convolution","dft"],ev=["Bluestein's chirp identity converts the middle transform","The chirp identity below performs the frequency change"],aliases=["Bluestein"])
c("gaussian-resampling","Gaussian resampling","The Harvey–van der Hoeven identity expressing a Fourier transform of coprime (prime) length s through one of power-of-two length t via contractions A and B0, at cost O(t p^{3/2+δ} α) per line.",
  ["dft","fixed-point-contraction","harvey-hoeven-multiplier"],ev=["Gaussian resampling\nthen expresses each source Fourier transform through a\npower-of-two tensor transform.".replace("\n"," "),"P_sF_s=2^{2\\alpha^2}B_0P_tF_tA"])
c("retained-permutations","Resampling with the permutations left in the transform","Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform identity and cancel, so no separate full sorts are executed.",
  ["gaussian-resampling","bluestein-chirp"],ev=["We retain both permutations in the transform formula and","Resampling without executing the two permutations"])
c("crt-prime-axes","Chinese-remainder address map to prime cyclic axes","A convolution-preserving map Φ places the radix-digit list on a product of distinct prime cyclic axes, implemented by triangular controlled shifts and axis moves.",
  ["radix-digit-convolution","elementary-streams"],ev=["placed on a product of\ndistinct prime cyclic axes by a Chinese-remainder map that preserves\nconvolution".replace("\n"," ")])
c("coefficient-twist","Coefficient twist to the negacyclic ring","Scaling coefficient k by ζ^k with ζ=e^{πi/r} maps cyclic convolution in the last coordinate to polynomial multiplication modulo y^r+1, with the negative wrap undoing to the cyclic wrap.",
  ["ring-y-r-plus-1","convolution"],ev=["A phase twist changes the last cyclic coordinate into a polynomial","multiplying coefficient $k$ by the nonzero number $\\zeta^k$"])
c("signed-packing","Signed packing of polynomial records","A signed Kronecker substitution packs a polynomial's coefficients into one big integer, multiplied by the O(N log N) multiplier and unpacked, giving ring multiplication in O(rp log(rp)).",
  ["ring-y-r-plus-1","harvey-hoeven-multiplier","fixed-point-contraction"],ev=["Signed packing and normalized ring multiplication","The reduction\nis a signed form of Kronecker substitution".replace("\n"," ")])
c("linear-network","Linear network with roles, frames and restored scratch","A fixed network of linear gates on wires (roles) exchanging two banks with signs, restoring every scratch value for arbitrary initial contents; applied to arrays, each wire gets an invertible frame whose change on an edge is what must be implemented.",
  ["elementary-streams"],ev=["A wire's fixed place in the network\nis called its role.".replace("\n"," "),"We call $D_v$ its frame"])
c("transparent-restoration","Restoring scratch values (transparent computation)","The schedule subtracts old scratch contributions, performs the operation, and undoes it so arbitrary initial auxiliary values cancel.",
  ["linear-network"],ev=["The first two rows of\nthe following schedule remove the effect of the old scratch values".replace("\n"," ")])
c("triple-subspace-labels","Three-element subsets and nested subspace labels","Indicator vectors of 3-subsets of [h] have intersection-count inner products; orthogonality gives nested nondegenerate subspaces whose dimension drops (orthogonal residuals) count the smaller operations on an edge.",
  ["linear-network"],ev=["\\langle t_S,t_T\\rangle=|S\\cap T|-1","the \\emph{orthogonal residual} is the orthogonal complement of the smaller label inside"])
c("rank-saving","Total smaller calls below W m","In the finite network the edges need s<Wm smaller calls in total, so a recursive call at parameter m·f uses s calls at parameter f on volume V/W, whose per-volume cost grows by s/W<m, giving a power saving.",
  ["triple-subspace-labels","linear-network"],title="Rank saving $s<Wm$",
  symbols=[("s","total smaller calls","The number of smaller calls summed over all network edges.",N),("W","number of roles","The number of wire roles among which rows are distributed.",N),("m","network dimension","The dimension of the label space, equal to the factor by which the parameter grows per recursion level.",D)],
  ev=["The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$.".replace("\n"," "),"This strict inequality\nis the source of the power saving.".replace("\n"," ")])
c("bruhat-shear","Lower-triangular factorization and address shear","Every rational matrix factors as E1 Π E2 with lower triangular E1,E2 and a partial permutation of rank-many ones; so an edge matrix of rank a costs a smaller interchanges, and the shear (H,D)→(H+D,D) is done in tape order.",
  ["elementary-streams","linear-network"],ev=["A=E_1\\Pi E_2","The required factorization\nis the Bruhat factorization for arbitrary matrices".replace("\n"," ")])
c("chunk-interchange","Fast interchange of address chunks","Interchanging two equal-width address fields of u digits in an array of volume V in O(V u^τ), τ<1, via XOR-style combinations whose final effect is an exact permutation.",
  ["rank-saving","bruhat-shear","transparent-restoration","elementary-streams"],
  title="Chunk interchange in $O(Vu^\\tau)$",
  symbols=[("V","bit volume","The number of stored bits in the array.",N),("u","chunk width","The number of address bits (digits) in each interchanged chunk.",N),("\\tau","saving exponent","A fixed exponent strictly below 1 in the cost bound.",D)],
  ev=["Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$.","(p,h,g,d,z)\\longmapsto(p,d,g,h,z)"])
c("phase-frames","Phase kernel C and complex network","The kernel C=H S H=aI+bX with C²=X and H₀=b S C S lets the complex network's frame changes be products of translation kernels on binary subspaces, over Gaussian dyadic numbers.",
  ["linear-network","triple-subspace-labels","butterfly"],ev=["C=H\\mathsf SH=aI+bX","H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X"])
c("packed-bit-addition","Packed selected-bit addition","Adding the selected bit across address chunks of many axes at once on packed records, with a small exceptional set of addresses repaired by sorting.",
  ["elementary-streams","chunk-interchange"],ev=["Packed selected-bit addition on one rectangle","Also $K/\\log p\\to\\infty$, which will"])
c("simultaneous-butterfly-layer","Simultaneous butterfly layer","Applies H₀ to the same bit position in d address chunks of complex fixed-point polynomial records in one pass, costing O(V d^λ') instead of d whole-array passes, with exact Gaussian dyadic intermediates and a single final truncation.",
  ["phase-frames","rank-saving","chunk-interchange","packed-bit-addition","butterfly","fixed-point-contraction","ring-y-r-plus-1"],
  title="Simultaneous butterfly layer in $O(Vd^{\\lambda'})$",
  symbols=[("V","bit volume","The number of stored bits in the logical array.",N),("d","selected axes","The number of address chunks whose selected bit gets a butterfly simultaneously.",N),("\\lambda'","layer exponent","A fixed exponent strictly below 1 in the layer cost.",D)],
  ev=["the cost is $O(Vd^{\\lambda'})$ for a","Simultaneous normalized butterfly layer"])
c("synthetic-convolution","Convolution from the retained transform layout","Convolution over R_r on a multi-axis array: two forward synthetic transforms keep the same frequency order, multiply pointwise by signed packing, and the opposite transform consumes that order, using layers on a layout built from chunk swaps.",
  ["synthetic-transform","simultaneous-butterfly-layer","signed-packing","chunk-interchange","convolution"],ev=["Convolution from the retained transform layout","The two forward synthetic transforms\nretain the same frequency order through their pointwise product".replace("\n"," ")])
c("parameter-choice","Parameter choice and cost table","With b=⌈log₂n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉}, every term of the normalized cost table is p^{1−margin}, so the total is O(Tp·p^{1−g}) = O(n (lg n)^{1−κ}).",
  ["synthetic-convolution","retained-permutations","crt-prime-axes","coefficient-twist"],ev=["The seven dominant powers in Table~\\ref{tab:costs} have the following","\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16}"])
c("exact-recovery","Precision, rounding and carries","Rescaling by the known normalizations, showing the coefficient error is below 1/2, rounding to integers, and propagating radix carries yield the exact 2n-bit product.",
  ["fixed-point-contraction","radix-digit-convolution"],ev=["proves that the recovered\ncoefficient error is strictly below $1/2$".replace("\n"," "),"Propagate radix-$2^b$ carries in increasing coefficient order."])
c("multiplication-algorithm","The multiplication algorithm pipeline","Digits, Φ to prime axes, two source transforms via Gaussian resampling and chirp convolution, pointwise product, opposite transform, scale, round, Φ⁻¹, carry.",
  ["crt-prime-axes","retained-permutations","bluestein-chirp","coefficient-twist","synthetic-convolution","exact-recovery","parameter-choice","gaussian-resampling"],ev=["The source-transform procedures now supply the three transforms needed","Compute $\\widetilde{\\mathscr F}^{+}(z)$"])
c("main-theorem","Integer multiplication in O(n (lg n)^{1−κ})","A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^{1−κ}) with κ=2^{-182}, disproving the n log n optimality conjecture in that model.",
  ["multiplication-algorithm","nlogn-conjecture","fixed-tape-model"],title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$",
  symbols=[("n","operand length","The number of bits in each input integer.",N),("\\lg n","log length","The larger of the ceiling of log base 2 of n and 1.",D),("\\kappa","saving exponent","The fixed constant 2^{-182} giving the power saving in the logarithm.",D)],
  ev=["T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right)","disproves the $n\\log n$ optimality conjecture"])
json.dump(dict(target="main-theorem",concepts=C),open("/home/user/openai-nlogn-wiki/runs/D2/exegenius/tasks/0001-extract.answer.json","w"),indent=1)
