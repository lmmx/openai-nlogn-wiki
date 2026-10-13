import json, re
P="/home/user/openai-nlogn-wiki/runs/G2/"
src=open(P+"sources/paper.tex").read()
norm=lambda s: re.sub(r"\s+","",s)
S=norm(src)
C=[]
def c(id,name,gloss,req,q=(),known=False,title=None,symbols=None,aliases=()):
    d=dict(id=id,name=name,aliases=list(aliases),gloss=gloss,requires=list(req),known=known,
           evidence=[dict(source="paper",quote=x) for x in q])
    if title: d["title"]=title; d["symbols"]=symbols
    C.append(d)
c("big-o","Big-O notation","Asymptotic upper bound on growth rate of a running time.",[],known=True)
c("polynomials","Polynomials","Expressions Σ a_k y^k added and multiplied by collecting powers.",[],known=True)
c("complex-numbers","Complex numbers","Numbers a+bi with i²=-1, including unit-modulus roots of unity e^{2πi/k}.",[],known=True)
c("multitape-turing-machine","Multitape Turing machine","A machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, each step reading, writing and moving one cell per tape.",[],known=True)
c("xor-bits","Bit XOR","Addition of bits modulo 2.",[],known=True)
c("nlogn-conjecture","The n log n conjecture and prior bounds","Schönhage–Strassen's 1971 bound O(n log n log log n), their conjecture that n log n is optimal, and Harvey–van der Hoeven's O(n log n) upper bound for multitape machines.",["big-o","multitape-turing-machine"],
  ["proposed $n\\log n$ as the optimal order of growth","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper"],aliases=["Schönhage–Strassen conjecture"])
c("tape-streams","Arrays as tape streams and elementary scans","Arrays stored in lexicographic address order on tapes, with logical volume V (number of stored bits), whose splitting, merging and digit moves cost linear time.",["multitape-turing-machine"],
  ["An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in","The \\emph{logical volume} $V$ is the number of stored data bits.","Each of the following operations on an array of"])
c("controlled-shift","Controlled shifts and rational scalings","A linear-time tape operation that adds an offset, computed from earlier control fields, to a later address field modulo a prime power, or multiplies it by a rational unit.",["tape-streams"],
  ["Suppose a target field $y\\in[Q]$ follows its control fields","Controlled shifts and fixed rational scalings"])
c("fixed-point-dyadics","Fixed-point and Gaussian dyadic arithmetic","Complex numbers stored as signed two's-complement grid numerators over 2^p, added and scaled exactly with guard bits and truncated once toward zero.",["complex-numbers","tape-streams"],
  ["Intermediate values are exact Gaussian dyadics,","$p$-bit grid array has real and imaginary coefficient parts in"])
c("dft","Discrete Fourier transform","The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πijk/q} on length-q vectors, a contraction in the max norm.",["complex-numbers","polynomials"],
  ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}"])
c("cyclic-convolution","Cyclic convolution","The product of two coefficient arrays indexed by ℤ/tℤ (or a product of such groups) as in multiplication of polynomials modulo x^t−1; the Fourier transform turns it into pointwise multiplication.",["polynomials","dft"],
  ["let $*$ denote cyclic convolution in the displayed","Cyclic convolution on distinct prime axes"])
c("multiplication-as-convolution","Multiplication as convolution of radix digits","Splitting both integers into radix-2^b digits makes the product a convolution of the digit coefficient lists, followed by carry propagation.",["cyclic-convolution","big-o"],
  ["Splitting the inputs into radix digits reduces multiplication to","Propagate radix-$2^b$ carries in increasing coefficient order."])
c("multidimensional-transform","Multidimensional transform","The tensor product of one-dimensional Fourier transforms along several axes, computing convolution on a product of cyclic groups.",["dft","cyclic-convolution"],
  ["multidimensional transforms whose axis lengths are","F_{\\boldsymbol q}:=\\bigotimes_iF_{q_i}"])
c("crt-address-map","Chinese-remainder address map","An algebra isomorphism Φ sending x to Π x_i^{μ_i} that turns cyclic convolution of length S=Πs_i (pairwise coprime) into convolution on the product of cyclic axes, implemented by triangular controlled shifts.",["multidimensional-transform","controlled-shift","tape-streams"],
  ["Agarwal and Cooley used the Chinese remainder","x\\longmapsto\\prod_i x_i^{\\mu_i}","$\\Phi$ is an isomorphism and preserves cyclic convolution."],aliases=["Φ"])
c("ring-mod-y-r-plus-1","Polynomial ring modulo y^r + 1","The ring of complex polynomials of degree below r in which y^r = −1, so powers of y are roots of unity and multiplying by y^a is a signed cyclic shift of coefficients.",["polynomials","complex-numbers"],
  ["\\mathcal R_r=\\mathbb C[y]/(y^r+1)","by $y^a$, for any integer $a$, permutes the coefficients and changes"],
  title="Polynomial ring modulo $y^r + 1$",
  symbols=[dict(symbol="y",name="ring variable",meaning="The indeterminate of the polynomials, whose powers act as roots of unity.",relation="direct"),
           dict(symbol="r",name="record length",meaning="The number of complex coefficients in a polynomial record, a power of two.",relation="count")],aliases=["negacyclic ring"])
c("two-point-butterfly","Two-point butterfly layer","The map H₀(u,v)=((u+v)/2,(u−v)/2) applied to pairs, whose repeated layers build a radix-2 fast Fourier transform.",["dft"],
  ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)"],aliases=["butterfly","H₀"])
c("synthetic-transform","Synthetic polynomial transform","A Fourier transform over the ring ℂ[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, so multiplications by roots are exact signed shifts and only butterflies remain.",["ring-mod-y-r-plus-1","two-point-butterfly","multidimensional-transform"],
  ["For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.","synthetic polynomial transforms of Nussbaumer and Quandalle"],aliases=["Nussbaumer polynomial transform"])
c("kronecker-packing","Signed packing for ring products","Multiplying two polynomials in the ring by packing signed coefficients into big integers (Kronecker substitution) and calling an O(N log N) integer multiplier.",["ring-mod-y-r-plus-1","nlogn-multiplier"],
  ["reduction is a signed form of Kronecker substitution","Signed packing and normalized ring multiplication"])
c("nlogn-multiplier","The established O(N log N) multiplier","The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log 2N) on N-bit inputs, used only as an ordinary subroutine on short inputs.",["nlogn-conjecture","multiplication-as-convolution"],
  ["$O(N\\log(2N))$ on $N$-bit inputs","they do not invoke the improved theorem recursively"])
c("linear-algebra-orthogonality","Subspaces, bilinear forms and orthogonal complements","A subspace of a vector space with a nondegenerate bilinear form, its orthogonal complement, the projection onto it, and the dimension (rank) of the difference of two nested subspaces.",[],
  ["A label is a nondegenerate subspace of a fixed bilinear space.","the \\emph{orthogonal residual} is the orthogonal complement of the smaller label inside"])
c("linear-network","Linear network with restored scratch wires","A fixed circuit of linear gates on wires that exchanges two banks of values with a sign while arbitrary initial values on auxiliary scratch wires are cancelled and restored.",["xor-bits"],
  ["A gate is a fixed linear map on a specified","For arbitrary initial values of its auxiliary wires, a forward","Each procedure arises from its own fixed linear network that exchanges two"],aliases=["motif network","restoration schedule"])
c("triple-subset-gadgets","Triple-subset intersection gadgets","Gather, scatter and side-injection gates indexed by three-element subsets of a 100-element set, whose coefficients depend on intersection size and whose side wires cancel the unwanted terms.",["linear-network","linear-algebra-orthogonality"],
  ["three-element subsets: gather and scatter create coefficients depending","Let $\\mathcal T$ be the set of three-element subsets of $[h]$."])
c("frames","Frames on wire arrays","Invertible linear operators D_v on each wire's address-indexed array so that stored array = D_v applied to the logical array, commuting with pointwise gates so only edge changes D_v D_u^{-1} cost anything.",["linear-network"],
  ["We call $D_v$ its frame: the stored","G(D_vg_1,\\ldots,D_vg_t)=D_vG(g_1,\\ldots,g_t)."])
c("rank-deficit-labels","Nested subspace labels and the rank deficit","Subspaces attached to gates and terminals so that adjacent labels are nested and the total rank s of all edge changes is strictly below the wire count times dimension, s < Wm.",["triple-subset-gadgets","frames","linear-algebra-orthogonality"],
  ["The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$.","The only decreasing\nedges are the central-wire edges from time 3 to time 4"],aliases=["s<Wm"])
c("recursive-power-saving","Recursive power saving from the rank deficit","A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume grows like m^τ rather than m, with τ<1 because s/W<m.",["rank-deficit-labels","tape-streams"],
  ["This strict inequality\nis the source of the power saving.","A recursive call at parameter $mf$ therefore uses $s$ calls at parameter"])
c("lower-triangular-factorization","Lower triangular factorization","Every rational matrix A of rank a equals E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones.",["linear-algebra-orthogonality"],
  ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization","A=E_1\\Pi E_2,"])
c("matrix-shear","Matrix shear on address fields","The address permutation (H,D)→(H+AD,D) modulo a prime power, which costs exactly rank(A) interchanges of b-digit fields plus linear work.",["lower-triangular-factorization","controlled-shift"],
  ["(H,D)\\longmapsto(H+AD,D)","can be performed with exactly $a$ interchanges of pairs of $b$-digit"])
c("fast-chunk-interchange","Fast interchange of address chunks","Swapping two disjoint contiguous address fields of u bits in an array of volume V in time O(V u^τ) for fixed τ<1, via XOR combinations of intermediate streams that finally form an exact permutation.",["recursive-power-saving","matrix-shear","frames","tape-streams","xor-bits"],
  ["Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$.","The first procedure interchanges two disjoint contiguous address","Power-width interchange with rows"])
c("phase-frames","Binary phase frames and the two-point kernel C","Frames C_U=H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} over Gaussian dyadics, whose edge changes are products of translation kernels aI+bX, composing to C^{⊗m} on every role.",["frames","rank-deficit-labels","two-point-butterfly","fixed-point-dyadics"],
  ["\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}_x(i^{q_U(x)})H^{\\otimes m}.","C=H\\mathsf SH=aI+bX","Phase-frame difference"] if False else ["\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}_x(i^{q_U(x)})H^{\\otimes m}.","C=H\\mathsf SH=aI+bX"])
c("packed-selected-bit-addition","Packed selected-bit addition","Adding corresponding selected bits of two address chunks using a third temporary chunk, via cyclic whole-chunk shifts plus a deterministic correction of an explicit small set of exceptional addresses.",["fast-chunk-interchange","controlled-shift"],
  ["We implement a binary row addition on corresponding selected bits in two","Packed selected-bit addition on one rectangle"])
c("simultaneous-butterfly-layer","Simultaneous butterfly layer","One H₀ butterfly at the same bit offset in up to d address chunks applied to all polynomial records at cost O(V d^{λ'}) for fixed λ'<1, evaluated exactly in dyadics with one final truncation.",["phase-frames","packed-selected-bit-addition","recursive-power-saving","synthetic-transform","fixed-point-dyadics"],
  ["We will obtain cost $O(Vd^{\\lambda'})$, with","Simultaneous normalized butterfly layer"])
c("synthetic-transform-layout","Synthetic transform tape layout","A tape layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that parallel layers apply, with the frequency order retained.",["simultaneous-butterfly-layer","fast-chunk-interchange","synthetic-transform"],
  ["we must place the selected bits of the participating axes at a common","Transform layout and cost"])
c("synthetic-convolution","Normalized convolution over the ring","Convolution of arrays over ℂ[y]/(y^r+1) as inverse transform of the pointwise product of forward transforms in the same frequency order, scaled by 1/T, with polynomial products done by signed packing.",["synthetic-transform-layout","kronecker-packing","cyclic-convolution"],
  ["\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}.","Convolution from the retained transform layout"])
c("phase-twist","Last-coordinate phase twist","The isomorphism x_d→ζy, ζ=e^{πi/r}, from ℂ[x_d]/(x_d^r−1) to ℂ[y]/(y^r+1) that turns cyclic wrap into negacyclic wrap and back.",["ring-mod-y-r-plus-1","cyclic-convolution"],
  ["is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.","last-coordinate\\\\phase twist"])
c("gaussian-resampling","Gaussian resampling","The Harvey–van der Hoeven method that expresses a Fourier transform of length s (coprime lengths) through a transform whose axis lengths are powers of two, via contractive Gaussian maps.",["multidimensional-transform","fixed-point-dyadics"],
  ["Gaussian resampling\nconnects these two shapes.","power-of-two tensor transform"])
c("resampling-without-sorting","Resampling with permutations left in the transform","The identity P_s F_s = 2^{2α²} B₀ P_t F_t A (and its tensor form) keeping both coordinate permutations inside the formula instead of sorting twice on each coordinate.",["gaussian-resampling"],
  ["We retain both permutations in the transform formula and","Resampling without executing the two permutations"])
c("bluestein-chirp","Bluestein chirp identity","A Fourier transform (with its permutation) rewritten as a pointwise chirp multiplication, a cyclic convolution with the chirp, and another chirp multiplication; the source permutation cancels across the product of two transforms.",["resampling-without-sorting","cyclic-convolution"],
  ["Next, Bluestein's chirp identity converts the middle transform,","Chirp and permutation cancellation"])
c("error-and-exact-recovery","Error bounds and exact recovery","Contraction-based accumulation of approximation errors through all steps, removal of known normalizations and scales, showing the coefficient error is below 1/2 so rounding gives exact integers.",["fixed-point-dyadics","multiplication-as-convolution"],
  ["coefficient error is strictly below $1/2$","Precision and exact recovery"])
c("parameter-choice","Parameter choice and cost table","Fixed rational exponents (τ=σ=1−2^{−50}, ε=2^{−75}, κ=2^{−182}, …) and sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉} making every cost term a power of p below one.",["simultaneous-butterfly-layer","synthetic-transform-layout","gaussian-resampling","big-o"],
  ["\\epsilon=2^{-75},\\qquad \\kappa=2^{-182}.","Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$\\\\"])
c("multiplication-algorithm","The multiplication algorithm","Digit extraction, the Chinese-remainder map, two forward source transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation yielding the exact 2n-bit product.",["multiplication-as-convolution","crt-address-map","bluestein-chirp","phase-twist","synthetic-convolution","error-and-exact-recovery","resampling-without-sorting"],
  ["\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain","The source-transform procedures now supply the three transforms needed"])
c("main-theorem","Integer multiplication in O(n (lg n)^(1−κ)) time","A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{−182}, refuting the n log n optimality conjecture in this model.",["multiplication-algorithm","parameter-choice","nlogn-conjecture","nlogn-multiplier"],
  ["T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right)","There is one deterministic Turing machine $A$, with a fixed finite"],
  title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
  symbols=[dict(symbol="n",name="input length",meaning="The number of bits in each of the two integers being multiplied.",relation="count"),
           dict(symbol="\\kappa",name="saving exponent",meaning="The fixed constant 2^{-182} giving the power saving in the logarithmic factor.",relation="direct")])
bad=0
for d in C:
    for e in d["evidence"]:
        if norm(e["quote"]) not in S: print("MISSING",d["id"],repr(e["quote"])); bad+=1
    if not d["known"] and not d["evidence"]: print("NOEV",d["id"])
ids={d["id"] for d in C}
for d in C:
    for r in d["requires"]:
        if r not in ids: print("BADREQ",d["id"],r)
json.dump(dict(target="main-theorem",concepts=C),open(P+"exegenius/tasks/0001-extract.answer.json","w"),ensure_ascii=False,indent=1)
print(len(C),bad)
