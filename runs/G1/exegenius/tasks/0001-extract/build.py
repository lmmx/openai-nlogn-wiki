import json,re,sys
src=open('/home/user/openai-nlogn-wiki/runs/G1/sources/paper.tex').read()
def norm(s): return re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'")).strip()
S=norm(src)
C=[]
def add(id,name,gloss,req,quotes=(),known=False,aliases=(),title=None,symbols=None):
    d=dict(id=id,name=name,aliases=list(aliases),gloss=gloss,requires=list(req),known=known,
           evidence=[{"source":"paper","quote":q} for q in quotes])
    if title: d['title']=title; d['symbols']=symbols
    C.append(d)
add('big-o-notation','Big-O notation','Asymptotic upper bound notation O(f(n)) for running times.',[],known=True)
add('polynomials','Polynomials','Sums of powers of a variable with coefficients, with addition and multiplication.',[],known=True)
add('complex-numbers','Complex numbers','Numbers a + bi with i² = −1, with modulus, conjugation and unit-modulus phases e^{iθ}.',[],known=True)
add('turing-machine-tapes','Multitape Turing machines','A machine with a finite alphabet, finite control and a fixed number of one-dimensional tapes whose heads each move at most one cell per step.',[],known=True)
add('nlogn-conjecture','The n log n conjecture and multiplication history','Schönhage and Strassen conjectured that n log n is the optimal multiplication cost on multitape Turing machines; Schönhage–Strassen, Fürer and Harvey–van der Hoeven gave successively better upper bounds down to O(n log n).',
    ['big-o-notation','turing-machine-tapes'],
    ["Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper","disproves the $n\\log n$ optimality conjecture"],aliases=['Schönhage–Strassen conjecture'])
add('hvdh-multiplier','Harvey–van der Hoeven O(n log n) multiplier','The established O(N log N) multitape algorithm for multiplying N-bit integers, used here only as an ordinary subroutine for short integers.',
    ['nlogn-conjecture'],["Harvey and van der Hoeven proved the unconditional","To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van der"])
add('dft','Discrete Fourier transform','The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} sending q complex values to their q frequency components.',['complex-numbers'],
    ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}"],aliases=['Fourier transform'])
add('cyclic-convolution','Cyclic convolution','The product of two length-q sequences viewed as polynomials modulo x^q − 1, so that indices wrap around cyclically.',['polynomials'],
    ["cyclic convolution on the product of the coordinate groups"],aliases=['convolution'])
add('convolution-theorem','Convolution theorem','The Fourier transform turns cyclic convolution into pointwise multiplication (up to normalization), so a convolution costs two forward transforms, a pointwise product and one inverse transform.',['dft','cyclic-convolution'],
    ["The normalized convolution rule is"])
add('fft-butterfly','FFT butterflies (decimation in frequency)','The recursive FFT step that pairs entries z_k and z_{k+t/2}, replaces them by their half-sum and half-difference, multiplies one output by a root of unity and recurses on both halves.',['dft','complex-numbers'],
    ["the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for","H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)"],aliases=['butterfly','two-point butterfly'])
add('integer-mult-as-convolution','Integer multiplication as radix-digit convolution','Splitting each integer into digits in a fixed radix turns the product into a convolution of the digit sequences, whose coefficients are then carried into binary.',['cyclic-convolution','big-o-notation'],
    ["Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients."])
add('multidimensional-transform','Multidimensional (tensor) transform','The Fourier transform on a product of axes, applied as the tensor product of one-dimensional transforms along each axis.',['dft','convolution-theorem'],
    ["multidimensional transforms whose axis lengths are powers of two"],aliases=['tensor transform'])
add('crt-axis-map','Chinese-remainder address map','An isomorphism sending a cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to a convolution on d prime-length cyclic axes, implemented here by triangular controlled shifts.',['cyclic-convolution','multidimensional-transform','integer-mult-as-convolution'],
    ["placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution"],aliases=['Agarwal–Cooley map'])
add('fixed-point-arithmetic','Fixed-point and Gaussian dyadic arithmetic','Complex values stored as signed two\'s-complement integers times 2^{−p}; additions, halvings and multiplications by i are exact with enough guard bits, and truncation Q_p to the grid has error below √2·2^{−p}.',['complex-numbers','turing-machine-tapes'],
    ["Intermediate values are exact Gaussian dyadics,","\\|Q_p z-z\\|_\\infty<\\sqrt2\\,2^{-p}"],aliases=['disk grid array','Gaussian dyadics'])
add('contraction-error','Linear contractions and error accumulation','A map that does not increase the maximum-modulus norm; applying contractions to approximate inputs never enlarges the input error, so errors of composed approximations add.',['complex-numbers','fixed-point-arithmetic'],
    ["A linear contraction propagates an input error without increasing it."])
add('gaussian-resampling','Gaussian resampling','Harvey–van der Hoeven\'s identity expressing a prime-length Fourier transform through a power-of-two-length one via Gaussian-weighted contractions A and B_0; the two coordinate permutations are left inside the identity rather than sorted.',['multidimensional-transform','contraction-error','fixed-point-arithmetic'],
    ["Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform.","Resampling without executing the two permutations"],aliases=['Gaussian resampling without sorting'])
add('bluestein-chirp','Bluestein chirp identity','Rewrites a Fourier transform as two pointwise multiplications by a chirp phase around a cyclic convolution with the chirp, so the middle transform (with its target permutation) becomes a convolution.',['dft','cyclic-convolution'],
    ["Bluestein's chirp identity converts the middle transform,"],aliases=['chirp'])
add('permutation-cancellation','Cancellation of the retained source permutation','The coordinate permutation retained in the resampling identity cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².',['gaussian-resampling','bluestein-chirp','convolution-theorem'],
    ["the source permutation retained during resampling cancels"])
add('prime-axis-lengths','Prime source lengths near powers of two','Choice of distinct primes s_i slightly below the power-of-two axis lengths t_i (using a prime-interval estimate) so that their product fills a fixed fraction of the padded box while each ratio t_i/s_i leaves room for resampling.',['crt-axis-map','gaussian-resampling'],
    ["The distinct prime lengths $s_i$ must be close to the powers of two"])
add('negacyclic-ring','Polynomial ring modulo y^r + 1','The ring of complex polynomials of degree below r in which y^r = −1, so multiplying by a power of y shifts the coefficient list with sign changes.',['polynomials','complex-numbers'],
    ["is stored as the coefficient list of a polynomial modulo $y^r+1$","\\mathcal R_r=\\mathbb C[y]/(y^r+1)"],
    title='Polynomial ring modulo $y^r + 1$',aliases=['negacyclic ring'],
    symbols=[{"symbol":"y","name":"ring variable","meaning":"The indeterminate of the polynomials, subject to the relation y^r + 1 = 0.","relation":"direct"},
             {"symbol":"r","name":"record length","meaning":"The number of complex coefficients in a polynomial record, a power of two.","relation":"count"}])
add('synthetic-roots','Synthetic roots of unity','In the negacyclic ring, powers of y serve as roots of unity ω_t = y^{2r/t}, and multiplying by one is an exact signed shift of the coefficient list with no arithmetic.',['negacyclic-ring','dft'],
    ["Powers of $y$ then serve as roots of unity in the remaining axes","Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs"])
add('synthetic-transform','Synthetic polynomial transform','A Fourier transform over the negacyclic ring (Nussbaumer–Quandalle) that uses powers of y as roots and is computed by butterflies, signed shifts and address rearrangements.',['synthetic-roots','fft-butterfly','multidimensional-transform','convolution-theorem'],
    ["These are the synthetic polynomial transforms of Nussbaumer"],aliases=['polynomial transform'])
add('phase-twist','Coefficient phase twist','Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns cyclic convolution of length r into convolution modulo y^r + 1 (negative wrap), and untwisting restores the cyclic wrap.',['negacyclic-ring','cyclic-convolution'],
    ["A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$"])
add('kronecker-packing','Signed Kronecker packing of polynomial products','Evaluating integer-coefficient polynomials at a large base B_0 packs them into integers so that one large integer multiplication yields all coefficients of the product, with signs handled by centered residues.',['polynomials','hvdh-multiplier','fixed-point-arithmetic'],
    ["Signed coefficient packing is a form of Kronecker substitution","Signed packing and normalized ring multiplication"],aliases=['Kronecker substitution'])
add('stream-operations','Array layout and elementary tape streams','Arrays stored in lexicographic address order on tape, with linear-time scans that permute digit positions, split into aligned streams, apply pointwise maps and merge them back.',['turing-machine-tapes'],
    ["An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order, with the first coordinate most significant.","Elementary stream operations"],aliases=['address fields'])
add('controlled-shifts','Controlled cyclic shifts of an address field','A target address field is shifted cyclically by an offset computed from earlier control fields in linear time, which also gives multiplication by fixed units modulo q^b.',['stream-operations'],
    ["Controlled shifts and fixed rational scalings"])
add('subset-intersection-gates','Three-element subset gates (copy, gather, scatter, side wires)','Fixed linear maps indexed by three-element subsets of {1..100} whose coefficients depend on intersection size; auxiliary side and center wires cancel the unwanted coefficients and are restored afterwards.',[],
    ["The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.","Alon's presentation of the Frankl--Wilson construction"])
add('bank-exchange-network','Scratch-restoring bank-exchange network','A fixed linear network of wires and gates that, in three stages, exchanges two banks of values with prescribed signs and restores every auxiliary scratch value whatever its initial content.',['subset-intersection-gates'],
    ["Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.","For arbitrary initial values of its auxiliary wires, a forward invocation changes"])
add('frames-network','Frames: changing representation along a network','Arrays replace scalars on wires; each vertex has an invertible frame operator D_v, edges apply D_v D_u^{-1}, and pointwise linear gates commute with the common frame, so the whole network acts as D_out S D_in^{-1}.',['bank-exchange-network'],
    ["We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$."],aliases=['frame','role'])
add('subspace-rank-saving','Subspace labels and the rank deficit','Nested subspaces of a fixed bilinear space attached to gates and terminals make each edge cost its rank in smaller operations; the total s of these ranks is strictly less than W·m, where W is the wire count and m the label-space dimension.',['frames-network','subset-intersection-gates'],
    ["The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.","orthogonal residual"],aliases=['rank saving'])
add('recursive-power-saving','Recursive power saving','A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume obeys F_k ≤ (s/W)F_{k−1} + O(1) with s/W < m, giving cost O(V e^τ) for some fixed τ < 1.',['subspace-rank-saving','big-o-notation'],
    ["This strict inequality is the source of the power saving.","F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."])
add('lower-triangular-factorization','Lower triangular (Bruhat-type) factorization','Every rational matrix A of rank a factors as E_1 Π E_2 with E_1, E_2 invertible lower triangular and Π a partial permutation matrix with a ones.',[],
    ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])
add('matrix-shear-cost','Cost of a rational matrix shear','The address map (H,D) ↦ (H + AD, D) of rank a is performed with exactly a interchanges of pairs of b-digit fields plus linear work, by factoring A and using three controlled updates around each swap.',['lower-triangular-factorization','controlled-shifts'],
    ["can be performed with exactly $a$ interchanges of pairs of $b$-digit"])
add('address-interchange','Address-chunk interchange','The first tape procedure: it swaps two disjoint address chunks of u bits in a complete array of volume V in time O(V u^τ) for a fixed τ < 1, internally using XOR combinations of intermediate data yet ending as an exact permutation.',['recursive-power-saving','matrix-shear-cost','stream-operations'],
    ["The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product.","Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."],aliases=['chunk swap','address rearrangement'])
add('binary-phase-interface','Phase frames and the C kernel','Over Gaussian dyadic values, the phase frame changes between binary subspace labels are products of two-point kernels aI + bX_v (a=(1+i)/2, b=(1−i)/2), one per orthonormal residual vector, and telescope to C^{⊗m} on every role.',['frames-network','subspace-rank-saving','complex-numbers'],
    ["per vector in an orthonormal basis","C=H\\mathsf SH=aI+bX"],aliases=['complex phase network'])
add('packed-selected-bit-addition','Packed selected-bit addition','Adds (XORs) the same bit position of f address chunks of one field into another, using a few cyclic shifts of whole chunks and a correction of an explicitly bounded set of exceptional addresses.',['address-interchange','controlled-shifts'],
    ["We implement a binary row addition on corresponding selected bits in two address chunks."])
add('simultaneous-butterfly-layer','Simultaneous butterfly layer','The second tape procedure: applies H_0(u,v) = ((u+v)/2,(u−v)/2) to one selected bit in each of up to d address chunks at once on polynomial records, in time O(V d^λ\') for fixed λ\' < 1, evaluated exactly and truncated once.',['binary-phase-interface','packed-selected-bit-addition','address-interchange','fft-butterfly','fixed-point-arithmetic','negacyclic-ring','recursive-power-saving'],
    ["simultaneously on selected coordinate bits of the numerical arrays.","the cost is $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$."],aliases=['parallel butterfly layer'])
add('synthetic-transform-layout','Tape layout of synthetic transforms','A layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that simultaneous layers and chunk interchanges evaluate the synthetic transform while keeping a fixed frequency order.',['synthetic-transform','simultaneous-butterfly-layer','address-interchange'],
    ["we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks."],aliases=['retained frequency order'])
add('synthetic-convolution','Convolution over the polynomial ring','Two forward synthetic transforms, polynomial products of each record by signed packing, and the opposite transform consuming the same stored frequency order give the normalized ring convolution.',['synthetic-transform-layout','kronecker-packing'],
    ["The two forward synthetic transforms retain the same frequency order through their pointwise product"])
add('exact-recovery','Exact recovery by rounding and carries','Scaling out the known normalizations, showing the total coefficient error is below 1/2, rounding to integers and propagating radix carries yields the exact 2n-bit product.',['contraction-error','integer-mult-as-convolution','fixed-point-arithmetic'],
    ["proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product."])
add('parameter-choice','Parameter choice and time bound','Fixed rational exponents and sizes (p = 6⌈log n⌉, d ≈ p^ε, T ≈ n/log n, κ = 2^{−182}) make every cost row of the table a power of p below 1, so the total is O(n (lg n)^{1−κ}).',['synthetic-transform-layout','gaussian-resampling','address-interchange','prime-axis-lengths','big-o-notation'],
    ["Take the following fixed rational numbers:","Thus $\\min_i g_i=2^{-181}=2\\kappa$."])
add('multiplication-algorithm','The multiplication algorithm','Digits are placed on prime axes by the CRT map, transformed by Gaussian-resampled, chirped, synthetic transforms, multiplied pointwise, transformed back, rescaled, rounded and carried to give the exact product.',['integer-mult-as-convolution','crt-axis-map','gaussian-resampling','bluestein-chirp','phase-twist','synthetic-convolution','permutation-cancellation','exact-recovery','prime-axis-lengths'],
    ["The source-transform procedures now supply the three transforms needed for the radix-digit convolution."])
add('sub-nlogn-multiplication','Integer multiplication below n log n','A deterministic fixed-tape Turing machine that multiplies n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture by replacing address rearrangement and Fourier layers with faster recursive tape procedures.',
    ['multiplication-algorithm','parameter-choice','nlogn-conjecture'],
    ["We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time"],aliases=['main theorem'])
ans={'target':'sub-nlogn-multiplication','concepts':C}
bad=0
for c in C:
    for e in c['evidence']:
        if norm(e['quote']) not in S: print('MISSING',c['id'],e['quote']); bad+=1
ids={c['id'] for c in C}
for c in C:
    for r in c['requires']:
        assert r in ids,(c['id'],r)
# cycle check
state={}
def dfs(n,st):
    if state.get(n)==1: raise Exception('cycle '+n)
    if state.get(n)==2: return
    state[n]=1
    for r in next(c for c in C if c['id']==n)['requires']: dfs(r,st)
    state[n]=2
for c in C: dfs(c['id'],0)
json.dump(ans,open('/home/user/openai-nlogn-wiki/runs/G1/exegenius/tasks/0001-extract.answer.json','w'),ensure_ascii=False,indent=1)
print('bad',bad,len(C))
