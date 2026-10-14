import json, re, sys
C=[]
def c(id,name,gloss,req,evid,known=False,aliases=None,title=None,symbols=None):
    d=dict(id=id,name=name,aliases=aliases or [],gloss=gloss,requires=req,known=known,
           evidence=[dict(source="paper",quote=q) for q in evid])
    if title: d["title"]=title
    if symbols: d["symbols"]=[dict(symbol=s,name=n,meaning=m,relation=r) for s,n,m,r in symbols]
    C.append(d)

# known
c("big-o","Big-O notation","Asymptotic upper bounds on running time such as O(n log n).",[],[],True)
c("polynomials","Polynomials","Expressions Σ aₖ xᵏ with coefficients, their addition and multiplication.",[],[],True)
c("complex-numbers","Complex numbers","Numbers a+bi with i²=−1, with modulus, conjugate and unit-modulus phases e^{iθ}.",[],[],True)
c("turing-machine-tapes","Multitape Turing machine","A machine with finitely many states, a finite alphabet and one-dimensional tapes whose heads move one cell per step.",[],[],True)

c("linear-algebra-basics","Matrices, rank, subspaces and orthogonality","Matrices over a field, their rank, subspaces, orthogonal complements under a bilinear form, and tensor products of spaces.",[],
  ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])
c("modular-arithmetic","Modular arithmetic and the Chinese remainder theorem","Arithmetic on residues mod q, units, inverses mod q, gcd, and the fact that coprime moduli split a residue ring into a product.",[],
  ["Uniqueness follows from $\\gcd(Q,c)=1$"])
c("convolution","Convolution and cyclic convolution","The product of two coefficient lists as polynomials; cyclic convolution wraps indices mod a length, so that it is multiplication in C[x]/(x^S−1).",["polynomials"],
  ["Splitting the inputs into radix digits reduces multiplication to\nconvolution of short integer coefficients."])
c("dft","Discrete Fourier transform and the convolution theorem","The length-q transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q} built from roots of unity; it turns convolution into pointwise product and is inverted by the opposite-sign transform.",["complex-numbers","convolution"],
  ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}"])
c("fft-butterfly","Butterfly and FFT recursion","The fast evaluation of a length-t transform by pairing entries z_k and z_{k+t/2}, applying a two-point butterfly, multiplying by twiddle roots and recursing on both halves.",["dft"],
  ["the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for\n$0\\leq k<t/2$"])
c("multidimensional-transform","Multidimensional transform (tensor product)","A transform on an array indexed by several axes, equal to applying the one-dimensional transform along each axis in turn; convolution on a product of cyclic groups is diagonalised by it.",["dft","convolution"],
  ["it replaces the Fourier transforms needed for\nthis convolution by multidimensional transforms whose axis lengths are\npowers of two"])
c("nlogn-conjecture","The n log n optimality conjecture","Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of multiplication cost on multitape Turing machines; the paper refutes any eventual Ω(n log n) lower bound for a fixed machine.",["big-o","turing-machine-tapes"],
  ["disproves the $n\\log n$ optimality\nconjecture of Sch\\\"onhage and Strassen in this model"],
  title="The $n\\log n$ optimality conjecture",symbols=[("n","input length","The number of bits in each of the two integers being multiplied.","count")])
c("nlogn-multiplier-subroutine","The established O(n log n) multiplier as a subroutine","Harvey and van der Hoeven's existing O(N log N) integer multiplication, called as an ordinary black box on shorter records (not the improved algorithm).",["big-o","turing-machine-tapes"],
  ["Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine\ncalls; they do not invoke the improved theorem recursively."])
c("fixed-point-disk-grid","Fixed-point disk grid and truncation","Complex numbers of modulus at most 1 whose real and imaginary parts are multiples of 2^{−p}, stored as signed two's-complement numerators, with Q_p truncating toward zero.",["complex-numbers"],
  ["A disk array has norm at most one."])
c("contractions-and-error","Contractions and error accumulation","A linear map is a contraction if it does not increase the maximum-modulus norm; approximate algorithms for contractions compose with errors that add.",["linear-algebra-basics","fixed-point-disk-grid"],
  ["Composing such algorithms\nadds their errors"])
c("guard-bits-dyadic","Exact Gaussian dyadic arithmetic and guard bits","Intermediate values with power-of-two denominators are kept exact by allocating extra integer and fractional guard bits, and rounded only once after a whole layer.",["fixed-point-disk-grid"],
  ["Intermediate values are exact Gaussian dyadics,\nwhose real and imaginary parts have power-of-two denominators."])

# tape machinery
c("tape-address-arrays","Arrays, addresses, rows and volume on tape","Arrays with multi-field addresses stored in lexicographic order on a tape, with address fields, row fields, prefix and suffix, spectator fields and logical volume V in bits.",["turing-machine-tapes"],
  ["An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in\nlexicographic order, with the first coordinate most significant."])
c("elementary-stream-operations","Elementary stream operations","Linear-time tape scans: permuting two digit positions, moving a digit, splitting into streams and merging, and splitting whole rows cyclically into W streams.",["tape-address-arrays","big-o"],
  ["Each of the following operations on an array of\nvolume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes"])
c("controlled-shifts","Controlled shifts","Updating a later address field by an offset computed from earlier fields (y ↦ y+a mod q^b), or multiplying it by a rational unit, in linear time.",["elementary-stream-operations","modular-arithmetic"],
  ["The next operations are linear because their target field follows their\ncontrol fields."])
c("row-splitting","Row splitting among roles with padding","Distributing whole rows cyclically among the W wire roles, after padding the row count to a multiple of a power of W, so each role stream has volume V/W.",["tape-address-arrays","elementary-stream-operations"],
  ["Distribute rows cyclically among the $W$ roles, padding the row count\nfor each prefix to a multiple of $W$."])
c("fixed-tape-recursion","Depth-first recursion on fixed tapes","Running recursive calls with finitely many tapes by parking inactive role streams on a stack tape, copying the active one to the child, and restoring afterwards, at cost linear in the parent's volume.",["elementary-stream-operations"],
  ["Reserve $W$ role tapes, a fixed set of\nI/O and elementary-operation work tapes, one parking stack tape, and a\nseparate descriptor stack."])

# network
c("linear-network-roles","Linear network with roles and restored scratch","A fixed network of linear gates on wires (roles) that exchanges two banks of values with signs while restoring every auxiliary (scratch) wire whatever its initial contents.",["linear-algebra-basics"],
  ["Each procedure arises from its own fixed linear network that exchanges two\nbanks of values, with prescribed signs, and restores every auxiliary\nvalue."])
c("triple-subset-gadget","Three-subset gather, scatter and side-wire gadget","The scalar gadget on three-element subsets of [100]: copy, gather, scatter and side injection with intersection-size coefficients, scheduled in 8 rows so that y_S gains x_S independently of scratch values.",["linear-network-roles"],
  ["The construction uses\nthree-element subsets: gather and scatter create coefficients depending\non intersection size, and auxiliary wires cancel the unwanted\ncoefficients."])
c("frames","Frames and edge operators","Invertible operators D_v on a wire's address-indexed array attached to each network vertex; a common frame commutes with pointwise linear gates, so only edges D_v D_u⁻¹ need implementing and the endpoints determine the net operator.",["linear-network-roles","linear-algebra-basics"],
  ["We call $D_v$ its frame: the stored\narray is $D_vg$ when the logical array is $g$."])
c("subspace-labels-rank-deficit","Nested subspace labels and rank deficit","Nondegenerate subspaces of a fixed m-dimensional space attached to gates and terminals, nested along edges, so that the total dimension change s over all edges is strictly less than W·m, where W is the wire count.",["triple-subset-gadget","frames","linear-algebra-basics"],
  ["The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$."])
c("address-shear","Address shear interface","The endpoint operator of the bit network: fields H, D over a residue ring updated by (H,D) ↦ (H+MD,D), with matrices M at vertices whose differences give rank-many smaller interchanges per edge.",["frames","subspace-labels-rank-deficit","modular-arithmetic"],
  ["that endpoint operator is an address shear:\ntwo fields, written as vectors $H,D$ over a common residue ring, are\nupdated by $(H,D)\\mapsto(H+D,D)$"])
c("triangular-factorization","Lower triangular factorization and matrix shear cost","Every rational matrix factors as E₁ΠE₂ with E₁, E₂ lower triangular and Π a partial permutation with rank-many ones, so a shear by A costs rank(A) interchanges plus linear work.",["linear-algebra-basics","controlled-shifts","address-shear"],
  ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])
c("recursive-power-saving","Recursive power saving","When a size-mf call uses s calls of size f on streams of volume V/W with s<Wm, the normalized cost satisfies F_k ≤ (s/W)F_{k−1}+O(1), giving cost O(V e^τ) with τ<1 instead of a factor e.",["big-o","subspace-labels-rank-deficit","fixed-tape-recursion"],
  ["After dividing cost by volume, multiplying the parameter by $m$\nincreases the recursive contribution by $s/W<m$. This strict inequality\nis the source of the power saving."])
c("address-chunk-interchange","Fast address-chunk interchange","The first tape procedure: swapping two disjoint u-bit address chunks of an array by recursion on the bit network in O(V u^τ) time for a fixed τ<1, intermediate steps computing XORs but the final effect an exact permutation.",["address-shear","triangular-factorization","recursive-power-saving","row-splitting","fixed-tape-recursion"],
  ["The first procedure interchanges two disjoint contiguous address fields\nof $u$ bits in an array whose addresses form a complete Cartesian\nproduct. Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."])
c("butterfly-and-phase-kernels","Butterfly kernel H₀ and phase kernel C","The two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) and the kernel C=aI+bX with a=(1+i)/2, b=(1−i)/2, related by H₀=b·S·C·S with S=diag(1,i), so a layer of H₀ equals phases times a layer of C.",["complex-numbers","fft-butterfly","linear-algebra-basics"],
  ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)","H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D"],
  title="Butterfly kernel $H_0$ and phase kernel $C$",
  symbols=[("H_0","butterfly kernel","The two-point map (u,v) ↦ ((u+v)/2,(u−v)/2) acting on a pair of complex values.","direct"),
           ("C","phase kernel","The 2×2 matrix aI+bX with a=(1+i)/2, b=(1−i)/2 that conjugates to the butterfly via phases.","direct")])
c("binary-phase-interface","Binary phase interface","The complex network with binary labels, in which each edge's frame change is a product of translation kernels aI+bX_v, one per residual basis vector, so that telescoping gives C⊗m on every role.",["frames","subspace-labels-rank-deficit","butterfly-and-phase-kernels"],
  ["After source and sink diagonal corrections, and undoing the signed\nbank exchange, telescoping these phase frames gives $C^{\\otimes m}$\non every role, including auxiliary roles."])
c("packed-selected-bit-addition","Packed selected-bit addition","XORing corresponding selected bits of two address chunks across many chunks at once, using a temporary third chunk, a few cyclic shifts, and a deterministic repair of a small exceptional set of addresses.",["address-chunk-interchange","controlled-shifts","elementary-stream-operations"],
  ["We implement a binary\nrow addition on corresponding selected bits in two\naddress chunks."])
c("simultaneous-butterfly-layer","Simultaneous butterfly layer","The second tape procedure: applying H₀ at the same bit position in d address chunks of every record in O(V d^λ') time, evaluated exactly with guard bits and truncated once.",["butterfly-and-phase-kernels","binary-phase-interface","packed-selected-bit-addition","row-splitting","recursive-power-saving","guard-bits-dyadic","fixed-tape-recursion"],
  ["Each record is a polynomial with complex fixed-point coefficients, and\n$H_0$ acts coefficientwise.","the cost is $O(Vd^{\\lambda'})$ for a\nfixed $\\lambda'<1$"])

# transforms
c("polynomial-ring-mod-y-r-plus-1","Polynomial ring modulo y^r + 1","The ring of complex polynomials of degree < r with y^r = −1; multiplication by a power of y is a signed shift of the coefficient list.",["polynomials","complex-numbers"],
  ["one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two"],
  title="Polynomial ring modulo $y^r + 1$",
  symbols=[("y","ring variable","The formal variable whose powers act as roots of unity in the ring.","direct"),
           ("r","record length","The number of complex coefficients in a polynomial record, a power of two.","count")])
c("synthetic-polynomial-transform","Synthetic polynomial transform","A multidimensional transform over the ring mod y^r+1 whose roots of unity are powers of y, so twiddle multiplications are signed shifts and only butterflies cost arithmetic.",["polynomial-ring-mod-y-r-plus-1","fft-butterfly","multidimensional-transform"],
  ["Powers of $y$ then\nserve as roots of unity in the remaining axes, and multiplication by\nsuch a root is a signed shift of the coefficient list."])
c("frequency-order-retention","Retained frequency order","Leaving transform outputs in the bit-reversed order the recursion writes them, so the pointwise product and the opposite transform consume that order without a separate permutation.",["synthetic-polynomial-transform"],
  ["The two forward synthetic transforms\nretain the same frequency order through their pointwise product"])
c("synthetic-transform-layout","Transform layout for parallel layers","The tape layout that places the selected bits of the participating axes at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so each transform round is one simultaneous butterfly layer.",["synthetic-polynomial-transform","simultaneous-butterfly-layer","address-chunk-interchange"],
  ["To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round,\nwe must place the selected bits of the participating axes at a common\noffset in consecutive $K$-bit chunks."])
c("signed-packing","Signed packing (Kronecker substitution)","Evaluating integer-coefficient polynomials at 2^{4p} to turn polynomial products into integer products, with signed carries and centered extraction of coefficients.",["polynomial-ring-mod-y-r-plus-1","nlogn-multiplier-subroutine"],
  ["Signed coefficient\npacking is a form of Kronecker substitution"])
c("synthetic-convolution","Ring convolution from the retained transform layout","Normalized convolution over the ring: two forward synthetic transforms, pointwise ring products by signed packing, then the opposite transform, with error below √2 M(3ℓ+1)2^{−p}.",["synthetic-polynomial-transform","frequency-order-retention","synthetic-transform-layout","signed-packing","contractions-and-error"],
  ["Perform both forward transforms and retain their common $LB$ order."])
c("phase-twist","Phase twist from cyclic to negacyclic","Multiplying coefficient k of the last cyclic axis by ζ^k with ζ=e^{πi/r} turns x^r−1 into y^r+1, so complex cyclic convolution is computed by ring convolution and the untwist.",["polynomial-ring-mod-y-r-plus-1","convolution","fixed-point-disk-grid"],
  ["A phase twist changes the last cyclic coordinate into a polynomial\nmodulo $y^r+1$"])

# reduction to power of two
c("gaussian-resampling","Gaussian resampling","Harvey–van der Hoeven's identity converting a Fourier transform of prime-ish length s into one of larger length t via Gaussian-weighted maps S and T, with a near-identity correction N.",["dft","multidimensional-transform","contractions-and-error"],
  ["Gaussian resampling\nconnects these two shapes."])
c("resampling-permutations-retained","Resampling with the permutations left in the transform","The paper's variant P_s F_s = 2^{2α²} B₀ P_t F_t A that keeps the coordinate permutations in the identity instead of executing two sorts per axis.",["gaussian-resampling"],
  ["We retain both permutations in the transform formula and\ncompute that formula directly."])
c("bluestein-chirp","Bluestein chirp identity","Rewriting a transform as pointwise chirp phases around a cyclic convolution with a chirp kernel, which here also absorbs the target permutation.",["dft","convolution","resampling-permutations-retained"],
  ["Bluestein's chirp identity converts the middle transform,\nincluding its target permutation, into normalized cyclic convolution."])
c("permutation-cancellation","Source permutation cancellation","The retained source permutation R cancels across two forward source transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².",["dft","convolution","resampling-permutations-retained"],
  ["the source permutation retained during resampling cancels"])
c("crt-address-map","Chinese-remainder address map","An algebra isomorphism from cyclic convolution of length S=∏s_i (s_i pairwise coprime) to convolution on the product of cyclic axes, implemented by triangular controlled shifts.",["convolution","modular-arithmetic","controlled-shifts","multidimensional-transform"],
  ["used the Chinese remainder\ntheorem to convert one cyclic convolution into multidimensional cyclic\nconvolution"])
c("integer-as-digit-convolution","Integer product as radix-digit convolution","Writing both inputs in base 2^b with q digits, the integer product is the convolution of the digit lists; padding to length S exceeds the degree so no wraparound occurs and coefficients stay below 2^{3b}.",["convolution","polynomials"],
  ["Thus convolution modulo $x^S-1$ has no nonzero wraparound."])
c("parameter-choice","Parameter choices and padded box","The sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T in [4n/b,8n/b), r=2^⌈(log₂T)/d⌉ and axis lengths t_i∈{r/2,r}, with α, γ, η and fixed rational exponents.",["multidimensional-transform","polynomial-ring-mod-y-r-plus-1","gaussian-resampling"],
  ["Take the power of two $T$ in $[4n/b,8n/b)$"])
c("prime-source-lengths","Prime source lengths","Distinct odd primes s_i in (1−2η)t_i < s_i ≤ (1−η)t_i near each power of two t_i, found by deterministic trial division, so that T/2<S<T and each ratio t_i/s_i leaves enough separation for resampling.",["parameter-choice","modular-arithmetic","gaussian-resampling"],
  ["The distinct prime lengths $s_i$ must be close to the powers of two"])
c("source-transform","Source transform pipeline","The approximate source transform: resample with A along each axis, apply the chirp transform via ring convolution, compress with B₀, and rescale by 2^γ, equal to R F_s.",["resampling-permutations-retained","bluestein-chirp","phase-twist","synthetic-convolution","prime-source-lengths"],
  ["computed chirp transform $\\widetilde{\\mathscr C}$"])
c("exact-recovery","Exact recovery by scaling, rounding and carries","Removing the known normalizations S and 2^{2b+4}, proving the coefficient error is below 1/2, rounding to integers and propagating radix-2^b carries to the exact 2n-bit product.",["contractions-and-error","integer-as-digit-convolution","fixed-point-disk-grid"],
  ["proves that the recovered\ncoefficient error is strictly below $1/2$, and propagates carries to\nobtain the exact binary product"])
c("multiplication-algorithm","The multiplication algorithm","The six steps: form radix digits, apply the address map Φ, compute two source transforms, multiply pointwise, apply the opposite transform, rescale, round and carry.",["integer-as-digit-convolution","crt-address-map","source-transform","permutation-cancellation","exact-recovery","parameter-choice"],
  ["Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain\nsource arrays $u,v$."])
c("cost-analysis","Cost analysis and the exponent κ","The table of normalized costs per Tp, each at most p^{1−2κ}, with the smallest margin 2^{−181}=2κ, giving total O(n (lg n)^{1−κ}) for κ=2^{−182}.",["multiplication-algorithm","address-chunk-interchange","simultaneous-butterfly-layer","synthetic-transform-layout","big-o"],
  ["Thus $\\min_i g_i=2^{-181}=2\\kappa$."],
  title="Cost analysis and the exponent $\\kappa$",
  symbols=[("\\kappa","power saving exponent","The fixed constant 2^{-182} by which the logarithmic factor is reduced.","direct")])
c("integer-multiplication-below-nlogn","Integer multiplication in O(n (lg n)^(1−κ)) time","The main theorem: one deterministic fixed-alphabet, fixed-tape Turing machine multiplies n-bit integers in O(n(lg n)^{1−κ}) worst-case time, refuting the n log n conjecture, via synthetic transforms accelerated by the interchange and butterfly procedures.",["multiplication-algorithm","cost-analysis","nlogn-conjecture"],
  ["We give a deterministic algorithm that multiplies two $n$-bit integers\nin $O(n(\\lg n)^{1-\\kappa})$ worst-case time"],
  title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
  symbols=[("n","input length","The number of bits in each of the two integers being multiplied.","count"),
           ("\\kappa","power saving exponent","The fixed constant 2^{-182} by which the logarithmic factor is reduced.","direct")])

ids={d["id"] for d in C}
assert len(ids)==len(C)
for d in C:
    for r in d["requires"]: assert r in ids,(d["id"],r)
# acyclic
import graphlib
graphlib.TopologicalSorter({d["id"]:d["requires"] for d in C}).prepare()
src=open("/home/user/openai-nlogn-wiki/runs/P1/sources/paper.tex").read()
norm=lambda s: re.sub(r"\s+","",s.replace("’","'").replace("“",'"').replace("”",'"'))
ns=norm(src)
for d in C:
    for e in d["evidence"]:
        if norm(e["quote"]) not in ns: print("MISSING",d["id"],e["quote"][:60])
    if not d["known"] and not d["evidence"]: print("NOEV",d["id"])
json.dump(dict(target="integer-multiplication-below-nlogn",concepts=C),open("/home/user/openai-nlogn-wiki/runs/P1/exegenius/tasks/0001-extract.answer.json","w"),indent=1,ensure_ascii=False)
