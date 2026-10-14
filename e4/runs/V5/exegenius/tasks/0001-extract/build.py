import json
P='paper'
def ev(*qs): return [{"source":P,"quote":q} for q in qs]
def sym(s,n,m,r="direct"): return {"symbol":s,"name":n,"meaning":m,"relation":r}
C=[]
def add(id,name,gloss,requires,known=False,evidence=(),title=None,symbols=None,aliases=()):
    d={"id":id,"name":name,"aliases":list(aliases),"gloss":gloss,"requires":requires,"known":known,"evidence":ev(*evidence)}
    if title: d["title"]=title
    if symbols: d["symbols"]=symbols
    C.append(d)

add("big-o","Big-O notation","Asymptotic upper bound on a running time as a function of input size.",[],True)
add("polynomials","Polynomials","Sums of coefficients times powers of an indeterminate, added and multiplied coefficientwise.",[],True)
add("complex-numbers","Complex numbers","Numbers a+bi with i²=−1, including roots of unity e^{2πi/k} of modulus one.",[],True)
add("tape-basics","Basic Turing machines and tapes","A finite-control machine reading and writing symbols on tapes with moving heads.",[],True)

add("fixed-tape-model","Fixed finite-tape Turing machine model","The cost model: one fixed finite alphabet, a fixed finite number of one-dimensional tapes, each step touching one cell per tape, and cost counted in bit operations on n-bit inputs x#y with output the 2n-bit product.",["tape-basics","big-o"],
    evidence=["A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.","Fixed tracks and finitely many work tapes change time by a fixed factor."])
add("nlogn-conjecture","The n log n conjecture and the history of multiplication","Schönhage and Strassen's 1971 O(n log n log log n) bound with the conjecture that n log n is optimal, followed by Fürer's and others' improvements up to Harvey–van der Hoeven's unconditional O(n log n).",["fixed-tape-model"],
    evidence=["proposed $n\\log n$ as the optimal order of growth","Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper"])
add("hvdh-multiplier","Established O(n log n) multiplier as a subroutine","The previously known O(N log N) fixed-tape integer multiplier, used as an ordinary black box on short inputs, never recursively invoking the new algorithm.",["nlogn-conjecture"],
    evidence=["This is an independent subroutine.","they do not invoke the improved theorem recursively"])

add("convolution","Cyclic convolution","The product rule f*g on a cyclic group (or product of cyclic groups), equal to polynomial multiplication modulo x^S−1.",["polynomials"],
    evidence=["let $*$ denote cyclic convolution in the displayed"])
add("dft","Normalized discrete Fourier transform F_q","Length-q transform with entries averaged over roots of unity; it turns convolution into pointwise multiplication (F(u*v)=S·Fu·Fv) and has inverse F⁺ up to normalization.",["complex-numbers","convolution"],
    title="Normalized discrete Fourier transform $F_q$",
    symbols=[sym("F_q","normalized transform","The map sending a length-q complex vector u to the vector whose kth entry is (1/q) times the sum of u_j e^{-2πijk/q}."),
             sym("q","transform length","The number of complex entries in the vector being transformed.","count")],
    evidence=["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}","Each normalized Fourier transform above is a contraction"])
add("butterfly","Two-point butterfly H₀ and the radix-two recursion","The map H₀(u,v)=((u+v)/2,(u−v)/2) and its use in the decimation-in-frequency recursion that splits a length-t transform into two half-length ones after a twiddle multiplication.",["dft"],
    title="Two-point butterfly $H_0$ and the radix-two recursion",
    symbols=[sym("H_0","butterfly map","The averaging map sending a pair (u,v) to ((u+v)/2,(u−v)/2).")],
    evidence=["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)","decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"])
add("ring-mod-yr-plus-1","Polynomial ring modulo y^r+1","Polynomials with complex coefficients of degree < r where y^r=−1, so multiplying by a power of y permutes coefficients with sign changes (a signed shift) and y supplies roots of unity.",["polynomials","complex-numbers"],
    title="Polynomial ring modulo $y^r+1$",
    symbols=[sym("y","ring variable","The indeterminate with y^r = −1; its powers act as roots of unity."),
             sym("r","record length","The number of complex coefficients in a polynomial record; a power of two.","count")],
    aliases=["negacyclic ring"],
    evidence=["\\mathcal R_r=\\mathbb C[y]/(y^r+1)","Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes"])
add("synthetic-transform","Synthetic polynomial transforms","Fourier transforms over the ring C[y]/(y^r+1) whose roots of unity ω_t=y^{2r/t} are powers of y, so twiddle multiplications are signed shifts; evaluated by radix-two butterfly rounds.",["dft","butterfly","ring-mod-yr-plus-1"],
    aliases=["Nussbaumer polynomial transforms"],
    evidence=["These are the synthetic polynomial transforms of Nussbaumer and Quandalle and","For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$."])
add("stored-order","Retained bit-reversed frequency order","The forward synthetic transform writes outputs in bit-reversed slots; the pointwise product and the opposite-sign transform consume that same order, so no reordering is executed.",["synthetic-transform"],
    evidence=["The two forward synthetic transforms retain the same frequency order through their pointwise product","Let $B_t$ denote this record permutation: it moves the entry at $j$"])

add("fixed-point","Fixed-point grid arrays with precision p","Complex numbers of modulus at most 1 stored as signed two's-complement integers scaled by 2^{-p}, with truncation toward zero after each completed step and error tracked as multiples of 2^{-p}.",["complex-numbers","big-o"],
    title="Fixed-point grid arrays with precision $p$",
    symbols=[sym("p","precision","The number of fractional bits kept in each real or imaginary component.","count")],
    evidence=["$p$-bit grid array has real and imaginary coefficient parts in","A single truncation follows the completed contractive layer."])
add("dyadic-exact","Exact Gaussian dyadic evaluation of a layer","Intermediate values of a butterfly layer are Gaussian integers over powers of two, computed exactly with enough guard bits, with a single truncation at the end.",["fixed-point"],
    evidence=["Intermediate values are exact Gaussian dyadics,","The entire layer is evaluated exactly before one final truncation."])

add("streams","Array streams, address fields and elementary scans","Arrays are stored in lexicographic address order on tapes with logical volume V bits; splitting, merging, and fixed permutations of digits cost O(V) by linear scans.",["fixed-tape-model"],
    evidence=["is stored in lexicographic order, with the first coordinate most significant","The \\emph{logical volume} $V$ is the number of stored data bits.","takes $O(V)$ steps on a fixed number of one-dimensional tapes"])
add("controlled-shifts","Controlled shifts and fixed rational scalings","Updating a later address field by an offset computed from earlier fields, or multiplying it by a fixed unit modulo q^b, in linear time using split and merge of consecutive blocks.",["streams"],
    evidence=["Controlled shifts and fixed rational scalings"])

add("linear-algebra","Subspaces, rank and orthogonal complements","Vector subspaces, matrix rank, bilinear forms, orthogonal complements, projections and tensor products, over the rationals or F₂.",[],
    evidence=["is the orthogonal complement of the smaller label inside the larger one"])
add("three-subset-pairing","Triple indicator vectors and intersection pairings","Indicator vectors of three-element subsets of a 100-element set, whose bilinear pairings give |S∩T| mod 2 over F₂ or |S∩T|−1 over Q, making neighboring triples orthogonal.",["linear-algebra"],
    evidence=["are the intersection count modulo two and the intersection count minus one","\\langle t_S,t_T\\rangle=|S\\cap T|-1"])
add("scalar-exchange-network","Scalar exchange network with restored scratch wires","A fixed linear network of gates (copy, gather, scatter, side injection) acting on banks X,Y and scratch wires, which sends (X,Y) to (−Y,X) in three stages and restores arbitrary initial scratch values.",["three-subset-pairing","linear-algebra"],
    evidence=["We construct two fixed linear networks that exchange two banks of values while restoring every auxiliary value.","This cancellation of arbitrary initial scratch values is a linear"])
add("frames","Frames and the common-frame identity","Assigning an invertible operator D_v to each vertex so that stored arrays are D_v applied to logical arrays; pointwise gates commute with the common frame, so the network implements D_out S D_in^{-1} with only edge changes D_v D_u^{-1} to pay for.",["scalar-exchange-network"],
    evidence=["We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$.","Thus the intermediate frames cancel"])
add("subspace-labels","Subspace labels and the rank saving s<Wm","Nested nondegenerate subspaces of an m-dimensional space attached to gates and terminals so the total rank of edge changes satisfies s<Wm.",["frames","three-subset-pairing"],
    title="Subspace labels and the rank saving $s<Wm$",
    symbols=[sym("s","total edge rank","The number of smaller calls needed, equal to the sum of the ranks of all edge differences.","count"),
             sym("W","wire count","The number of wires, including scratch wires, in the network.","count"),
             sym("m","label dimension","The dimension of the ambient label space.")],
    evidence=["A label is a nondegenerate subspace of a fixed bilinear space.","The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$."])
add("bit-network","Bit network and its shear interface","The F₂ network with W_b wires and rational labels whose endpoint matrices differ by the identity on every input role, giving the address shear H←H+D with s_b<W_b·m.",["subspace-labels"],
    evidence=["The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,"])
add("lower-triangular-factorization","Lower-triangular factorization of a matrix","Every rational matrix A of rank a equals E₁ΠE₂ with E₁,E₂ lower triangular and Π a partial permutation with a ones.",["linear-algebra"],
    evidence=["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])
add("address-shear","Address shear costing rank-many interchanges","The permutation (H,D)↦(H+AD,D) of address fields mod q^b is done with exactly rank(A) field interchanges plus linear work, using triangular factors and controlled shifts.",["lower-triangular-factorization","controlled-shifts","bit-network"],
    evidence=["The cost of a rational matrix shear"])
add("power-saving-recursion","Power saving from a rank-deficit recursion","Because the network makes s<Wm calls on streams of volume V/W, the per-volume cost recurrence F_k ≤ (s/W)F_{k−1}+O(1) with s/W<m^τ gives cost O(e^τ) at width e=m^k, with depth-first scheduling on fixed tapes.",["subspace-labels","big-o"],
    evidence=["This strict inequality is the source of the power saving.","$F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).$"[:0] or "A fixed-tape depth-first schedule"])
add("chunk-interchange","Address-chunk interchange in O(Vu^τ) time","Exchanging two disjoint contiguous u-bit address fields of an array of volume V by XOR combinations of intermediate data, in time O(V u^τ) for a fixed τ<1; the final effect is an exact permutation.",["address-shear","power-saving-recursion","streams","bit-network"],
    title="Address-chunk interchange in $O(Vu^\\tau)$ time",
    symbols=[sym("V","stored volume","The number of stored data bits in the array."),
             sym("u","chunk width","The number of bits in each of the two address fields being interchanged.","count"),
             sym("\\tau","interchange exponent","A fixed constant below 1, namely 1−2^{-50}.")],
    evidence=["Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$.","Arbitrary-width interchange"])

add("phase-frames","Binary phase frames and the two-point kernel C","The complex network with binary labels, frames given by Hadamard-conjugated phases i^{wt(P_U x)}, so each edge is a product of translation kernels aI+bX_v and the endpoints give C⊗…⊗C on every role, where C=H·diag(1,i)·H and H₀=b·S·C·S.",["subspace-labels","frames","butterfly"],
    evidence=["Phase frames for a simultaneous butterfly layer","C=H\\mathsf SH=aI+bX"])
add("packed-selected-bits","Packed selected-bit addition","Adding corresponding selected bits of address chunks (a binary row addition) via a constant number of whole-chunk cyclic shifts, then repairing an explicitly bounded exceptional set of addresses.",["chunk-interchange","controlled-shifts"],
    evidence=["Packed selected-bit addition on one rectangle"])
add("simultaneous-layer","Simultaneous butterfly layer in O(Vd^λ') time","Applying H₀ to the same bit position of D≤d address chunks of a polynomial array at once, via the phase network and recursion on e=mf axes, in time O(V d^λ') instead of D passes.",["phase-frames","packed-selected-bits","power-saving-recursion","dyadic-exact","chunk-interchange","ring-mod-yr-plus-1"],
    title="Simultaneous butterfly layer in $O(Vd^{\\lambda'})$ time",
    symbols=[sym("V","stored volume","The number of stored data bits in the array."),
             sym("d","axis count","The maximum number of address chunks (axes) whose selected bits are butterflied together.","count"),
             sym("\\lambda'","layer exponent","A fixed constant below 1, namely 1−2^{-54}.")],
    evidence=["Simultaneous normalized butterfly layer","the cost is $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$"])
add("transform-layout","Synthetic transform layout and cost","Placing the selected bits of participating axes at a common offset in K-bit chunks so that each synthetic transform round uses the simultaneous layer, with total cost O(Tp[dK+pK^{τ−1}+ℓd^{λ'}]).",["synthetic-transform","stored-order","simultaneous-layer","chunk-interchange","fixed-point"],
    evidence=["Transform layout and cost"])
add("signed-packing","Signed packing of polynomial products","Evaluating polynomials at 2^{4p} (a signed Kronecker substitution) so one product in the ring is four integer products by the established multiplier, then reading centered coefficients back.",["hvdh-multiplier","ring-mod-yr-plus-1","fixed-point"],
    evidence=["packing is a form of Kronecker substitution","Signed packing and normalized ring multiplication"])
add("synthetic-convolution","Convolution from the retained transform layout","Two forward synthetic transforms, a pointwise ring product by signed packing, and the opposite transform give normalized convolution over C[y]/(y^r+1) with error about 3ℓ·M·2^{-p}.",["transform-layout","signed-packing","stored-order"],
    evidence=["Convolution from the retained transform layout"])

add("digit-convolution","Multiplication as radix-digit convolution","Writing both inputs in radix 2^b with q=⌈n/b⌉ digits, the product coefficients are a convolution with capacity below 2^{3b}, and padding to length S avoids wraparound.",["convolution","polynomials","fixed-tape-model"],
    evidence=["Splitting the inputs into radix digits reduces multiplication to","Thus convolution modulo $x^S-1$ has no nonzero wraparound."])
add("crt-cyclic-axes","Chinese-remainder map to prime cyclic axes","Using pairwise coprime lengths s_i, a length-S cyclic convolution becomes convolution on a product of cyclic axes through the map x↦∏x_i^{μ_i}, realized by triangular controlled shifts.",["convolution","controlled-shifts"],
    aliases=["Agarwal–Cooley"],
    evidence=["Chinese-remainder map that preserves convolution"])
add("gaussian-resampling","Gaussian resampling","Harvey–van der Hoeven's identity expressing a Fourier transform of prime-related length s through a power-of-two length t≥s transform via Gaussian-weighted contractions A and B₀, with a small error N−I.",["dft","fixed-point"],
    evidence=["Gaussian-resampling reduction of Harvey and van der Hoeven","resampling then expresses each source Fourier transform through a power-of-two tensor transform"])
add("bluestein-chirp","Bluestein chirp identity","A Fourier transform as a pointwise phase multiplication, a cyclic convolution with a chirp array, and another phase multiplication.",["dft","convolution"],
    evidence=["Bluestein's chirp identity converts the middle transform"])
add("retained-permutations","Retaining resampling permutations in the transform","The coordinate permutations of resampling stay inside the transform formula, so the chirp absorbs the target permutation and the source permutation cancels across two forward transforms, a pointwise product and the opposite transform.",["gaussian-resampling","bluestein-chirp","chunk-interchange"],
    evidence=["the source permutation retained during resampling cancels across the two forward source transforms"])
add("phase-twist","Coefficient twist from cyclic to negacyclic","Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps C[x]/(x^r−1) isomorphically onto C[y]/(y^r+1) so negative wrap becomes cyclic wrap.",["ring-mod-yr-plus-1","convolution"],
    evidence=["A phase twist changes the last cyclic coordinate into a polynomial"])
add("size-parameters","Size parameters and prime source lengths","Choice b=⌈log₂n⌉, p=6b, d≈b^ε, K≈d^c, T≈n/b a power of two, axis lengths r/2 or r, and distinct odd primes s_i just below t_i, so that Tp=Θ(n) and r outgrows every power of p.",["crt-cyclic-axes","gaussian-resampling","ring-mod-yr-plus-1","fixed-point"],
    evidence=["Take the power of two $T$ in $[4n/b,8n/b)$, and let","The distinct prime lengths $s_i$ must be close to the powers of two"])
add("exact-recovery","Exact recovery by rounding and carry propagation","Undoing known scales S and 2^{2b+4}, showing the coefficient error is below 1/2, rounding to integers, and propagating radix-2^b carries to obtain the exact 2n-bit product.",["digit-convolution","fixed-point"],
    evidence=["coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product"])
add("multiplication-algorithm","The assembled multiplication algorithm","Digits are placed on prime axes by the CRT map, two source transforms (Gaussian resampling with chirp convolution over the ring via twist, using synthetic convolution) and one opposite transform give the digit convolution, then rescale, round and carry.",["digit-convolution","crt-cyclic-axes","gaussian-resampling","bluestein-chirp","retained-permutations","phase-twist","synthetic-convolution","size-parameters","exact-recovery"],
    evidence=["The two occurrences of $S$ in this algorithm undo different","Integer product\\\\radix-digit convolution"[:0] or "The multiplication algorithm"])
add("cost-accounting","Cost accounting and the exponent κ","Dividing each term by Tp gives powers of p with margins g_i below one; the smallest margin is 2κ with κ=2^{-182}, absorbing any polylog factor.",["multiplication-algorithm","chunk-interchange","simultaneous-layer","transform-layout"],
    evidence=["Thus $\\min_i g_i=2^{-181}=2\\kappa$."])
add("main-theorem","Integer multiplication in O(n (lg n)^{1−κ}) time","A deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.",["multiplication-algorithm","cost-accounting","nlogn-conjecture"],
    title="Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time",
    symbols=[sym("n","input length","The number of bits in each of the two integers multiplied.","count"),
             sym("\\kappa","saving exponent","The fixed constant 2^{-182} giving the power saving in the logarithmic factor.")],
    aliases=["Theorem 1"],
    evidence=["We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time, with","disproves the $n\\log n$ optimality conjecture"])
json.dump({"target":"main-theorem","concepts":C},open("/home/user/openai-nlogn-wiki/runs/P5/exegenius/tasks/0001-extract.answer.json","w"),indent=1)
