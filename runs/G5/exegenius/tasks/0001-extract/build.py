import json, re, sys
src = open('/home/user/openai-nlogn-wiki/runs/G5/sources/paper.tex', encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s)
nsrc = norm(src)

C = []
def add(id, name, gloss, requires, quotes=(), known=False, aliases=(), title=None, symbols=None):
    d = dict(id=id, name=name, aliases=list(aliases), gloss=gloss, requires=list(requires),
             known=known, evidence=[dict(source='paper', quote=q) for q in quotes])
    if title:
        d['title'] = title
        d['symbols'] = symbols
    C.append(d)

# known
add('big-o','Big-O notation','Asymptotic upper bounds on running time such as O(n log n).',[],known=True)
add('multitape-tm','Turing machines with tapes','A Turing machine reads and writes cells on one or more tapes with moving heads, one step at a time.',[],known=True)
add('polynomials','Polynomials','Sums of coefficients times powers of a variable, multiplied by convolving coefficient lists.',[],known=True)
add('complex-numbers','Complex numbers','Numbers a + bi with i² = −1, with modulus and phase.',[],known=True)
add('roots-of-unity','Roots of unity','Complex numbers ω with ω^t = 1; powers of a primitive one cycle through all of them.',[],known=True)
add('modular-arithmetic','Modular arithmetic','Arithmetic with remainders modulo an integer, including units, inverses and gcd.',[],known=True)
add('binary-arithmetic','Binary integers and XOR','Binary representation of integers, bitwise XOR, carries, and fixed-width two\'s-complement words.',[],known=True)
add('linear-algebra','Basic linear algebra','Matrices, rank, subspaces, tensor products and orthogonal projection.',[],known=True)

add('fixed-tape-model','Fixed finite-tape Turing machine model',
    'The computation model: one fixed machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, whose steps move each head by at most one cell.',
    ['multitape-tm'],
    ['A machine has one fixed finite alphabet and one fixed finite number of',
     'Fixed tracks and finitely many work tapes change time by a fixed factor.'])
add('nlogn-conjecture','Optimality conjecture for multiplication',
    'Schönhage and Strassen\'s 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine, which the paper refutes.',
    ['multitape-tm','big-o'],
    ['proposed $n\\log n$ as the optimal order of growth',
     'disproves the $n\\log n$ optimality conjecture'],
    aliases=['n log n conjecture'])
add('nlogn-multiplier','Established n log n multiplier',
    'The Harvey–van der Hoeven O(N log N) multiplication algorithm for N-bit integers, used here only as an ordinary subroutine on short inputs.',
    ['nlogn-conjecture','fixed-tape-model'],
    ['Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine',
     'Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper'])

add('stream-scans','Array order and linear-time stream scans',
    'Arrays are stored in lexicographic address order on tape; splitting on a digit, moving a digit, applying a pointwise map and merging all cost O(V) for volume V.',
    ['fixed-tape-model','binary-arithmetic'],
    ['volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes',
     'An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in'])
add('controlled-shifts','Controlled cyclic shifts and rational scalings',
    'A target address field can be rotated by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time.',
    ['stream-scans','modular-arithmetic'],
    ['The next operations are linear because their target field follows their control fields.',
     'y\\longmapsto y+a(\\text{controls})\\pmod Q'])

add('convolution','Cyclic convolution',
    'The operation combining two coefficient arrays so that coefficient j of the result sums products of entries whose indices add to j modulo the length; it is polynomial multiplication with wraparound.',
    ['polynomials','modular-arithmetic'],
    ['Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.',
     'let $*$ denote cyclic convolution in the displayed'])
add('radix-digit-reduction','Reducing integer multiplication to digit convolution',
    'Writing each integer as a polynomial in 2^b with b-bit digits turns the product into a convolution of digit lists; padding avoids wraparound, and rounding plus carry propagation recover the bits.',
    ['convolution','binary-arithmetic'],
    ['Write the two inputs as polynomials in $2^b$, each with',
     'Thus convolution modulo $x^S-1$ has no nonzero wraparound.'])
add('dft','Discrete Fourier transform and convolution theorem',
    'The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns cyclic convolution into pointwise multiplication.',
    ['roots-of-unity','convolution','complex-numbers'],
    ['(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}',
     'The normalized convolution rule is'],
    aliases=['Fourier transform','DFT'])
add('fft-butterfly','Radix-2 FFT butterflies',
    'A length-t transform is computed in log t levels, each pairing entries k and k+t/2 with the two-point butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and a twiddle multiplication.',
    ['dft'],
    ['decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$',
     'H_0=\\frac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}'],
    aliases=['butterfly','decimation in frequency'])
add('multidimensional-transform','Multidimensional transforms on power-of-two axes',
    'A transform over several axes is the tensor product of one-dimensional transforms, applied axis by axis to an array indexed by a product of axis lengths.',
    ['dft','fft-butterfly'],
    ['multidimensional transforms whose axis lengths are powers of two',
     'F_{\\boldsymbol t}^\\pm=\\bigotimes_{i=1}^D F_{t_i}^\\pm'],
    aliases=['tensor transform'])

add('crt-prime-axes','Chinese-remainder map onto distinct prime axes',
    'A ring isomorphism sends a length-S cyclic convolution to a multidimensional cyclic convolution on pairwise coprime axes s_i; on tape it is a sequence of triangular controlled shifts.',
    ['radix-digit-reduction','modular-arithmetic','controlled-shifts','multidimensional-transform'],
    ['$\\Phi$ is an isomorphism and preserves cyclic convolution',
     'Cyclic convolution on distinct prime axes'],
    aliases=['Chinese remainder address map'])
add('gaussian-resampling','Gaussian resampling',
    'The Harvey–van der Hoeven technique expressing a Fourier transform of prime-like length s through one of a larger power-of-two length t, using Gaussian-weighted contractions A and B₀ and two coordinate permutations.',
    ['dft','multidimensional-transform'],
    ['Gaussian resampling connects these two shapes.',
     'Its usual implementation sorts twice on each'])
add('chirp-identity','Bluestein chirp identity',
    'A phase-weighted identity that rewrites a Fourier transform, including its frequency permutation, as a cyclic convolution with a chirp array a_j = exp(−πi Σ s_i j_i²/t_i) between pointwise phase multiplications.',
    ['dft','convolution','multidimensional-transform'],
    ["Next, Bluestein's chirp identity converts the middle transform,",
     'a_{\\boldsymbol j}'],
    aliases=['Bluestein conversion','chirp'])
add('retained-permutations','Resampling with retained permutations',
    'Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform formula R F_s = 2^γ B₀ Q F_t A; the source permutation then cancels across the two forward transforms and the opposite one.',
    ['gaussian-resampling','chirp-identity','multidimensional-transform'],
    ['We retain both permutations in the transform formula and compute that formula directly.',
     'Section~\\ref{sec:resampling} retains the'])

add('polynomial-ring','Polynomial ring modulo yʳ + 1',
    'Complex polynomials of degree below r with y^r = −1, so that multiplying by a power of y is a signed shift of the coefficient list; powers of y serve as roots of unity.',
    ['polynomials','complex-numbers'],
    ['\\mathcal R_r=\\mathbb C[y]/(y^r+1)',
     'Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes'],
    aliases=['negacyclic ring'],
    title='Polynomial ring modulo $y^r+1$',
    symbols=[dict(symbol='y',name='ring variable',meaning='The formal variable of the polynomials, subject to the relation y^r = −1.',relation='direct'),
             dict(symbol='r',name='record length',meaning='The number of complex coefficients in one polynomial record, a power of two.',relation='count')])
add('synthetic-transform','Synthetic polynomial transform',
    'A Fourier transform whose roots of unity are powers ω_t = y^{2r/t} of the ring variable, so twiddle multiplications are exact signed shifts and only butterflies cost arithmetic.',
    ['polynomial-ring','fft-butterfly','multidimensional-transform'],
    ['For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.',
     'The polynomial roots and radix-two butterflies belong to the fast'],
    aliases=['Nussbaumer polynomial transform'])
add('stored-frequency-order','Retained frequency order of the transforms',
    'The forward transform writes frequency j into slot rev(j), and the opposite transform consumes exactly that bit-reversed order, so no reordering sort is needed between the two.',
    ['synthetic-transform'],
    ['The recursion writes its outputs directly in this order',
     'because the opposite transform consumes that same order'])
add('coefficient-twist','Phase twist to a negacyclic wrap',
    'Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns convolution modulo x^r − 1 into convolution modulo y^r + 1 on the last axis, and untwisting restores the cyclic wrap.',
    ['polynomial-ring','convolution','roots-of-unity'],
    ['A phase twist changes the last cyclic coordinate into a polynomial',
     'is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.'])
add('signed-packing','Signed Kronecker packing of polynomial products',
    'Ring elements are evaluated at B₀ = 2^{4p} as signed integers, multiplied with the established multiplier, and unpacked by centered residues and carries, giving exact polynomial products.',
    ['nlogn-multiplier','polynomial-ring','binary-arithmetic'],
    ['The reduction is a signed form of Kronecker substitution',
     'Multiply the four'])
add('fixed-point-disk','Disk-grid fixed-point arithmetic',
    'Complex values in the unit disk stored as 2^{-p} times Gaussian-integer numerators in two\'s complement; layers are computed exactly in Gaussian dyadics with guard bits and then truncated toward zero by Q_p.',
    ['complex-numbers','binary-arithmetic'],
    ['$p$-bit grid array has real and imaginary coefficient parts in',
     'Intermediate values are exact Gaussian dyadics,'],
    aliases=['Gaussian dyadics','truncation Q_p'])

add('subset-gadgets','Three-element subset gadgets',
    'Copy, side-injection, gather and scatter maps on indicator vectors of three-element subsets whose net effect adds x_S to y_S, because central coefficients depend only on intersection sizes and side wires cancel the unwanted ones.',
    ['linear-algebra','binary-arithmetic'],
    ['three-element subsets: gather and scatter create coefficients depending on intersection size',
     'The following maps specify the construction.'])
add('bank-exchange-network','Linear bank-exchange network with restored scratch wires',
    'A fixed network of linear gates on wires that, using three stages of the subset gadgets, exchanges two data banks (X,Y)→(−Y,X) while restoring every auxiliary scratch wire to its arbitrary initial value.',
    ['subset-gadgets','binary-arithmetic'],
    ['We construct two fixed linear networks that exchange two banks of values',
     'For arbitrary initial values of its auxiliary wires, a forward'])
add('frames','Frames and the common-frame identity',
    'An invertible linear operator D_v on each wire\'s address-indexed array at each vertex; because gates are pointwise and linear they commute with a common frame, so the network realizes D_out S D_in^{-1}.',
    ['bank-exchange-network','linear-algebra'],
    ['We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$.',
     'D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}'])
add('subspace-labels','Nested subspace labels and orthogonal residuals',
    'Each gate and terminal carries a nondegenerate subspace of a fixed bilinear space, adjacent labels are nested, and the orthogonal residual of an edge has dimension equal to the label change, so the total rank cost is Wm − 2N + 2L.',
    ['frames','subset-gadgets','linear-algebra'],
    ['A label is a nondegenerate subspace of a fixed bilinear space.',
     'Every edge joins comparable nondegenerate labels.'])
add('bit-network-interface','Bit network and its rational matrix interface',
    'Using XOR gates and projections P_U as frame matrices, the bit network permutes its roles and the endpoint matrices differ by the identity, so the net effect on arrays is the shear H ← H + D.',
    ['subspace-labels','frames'],
    ['The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,',
     'M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m'])
add('rank-saving','Rank saving of the finite networks',
    'The sum s of edge ranks is strictly less than the wire count W times the dimension m, so a recursive call on width m·f uses s calls on volume V/W each and the cost per volume grows by s/W < m, which gives the power saving.',
    ['bit-network-interface'],
    ['This strict inequality is the source of the power saving.',
     'number $s$ of smaller calls satisfies $s<Wm$'],
    aliases=['recursive saving'])
add('two-point-kernel','Two-point phase kernel C',
    'The 2×2 kernel C = H S H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying C² = X and C⁴ = I and related to the butterfly by H₀ = b S C S.',
    ['fft-butterfly','complex-numbers','linear-algebra'],
    ['H_0=b\\mathsf SC\\mathsf S',
     'C=H\\mathsf SH=aI+bX'])
add('phase-interface','Binary phase interface of the complex network',
    'With Gaussian-dyadic scalars and binary labels, each edge\'s frame change is a product of translation kernels aI + bX_v, one per residual basis vector, and telescoping the frames yields C^{⊗m} on every role.',
    ['subspace-labels','frames','two-point-kernel','bank-exchange-network'],
    ['is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis',
     'telescoping these phase frames gives $C^{\\otimes m}$'])

add('matrix-factorization','Lower-triangular factorization of a matrix',
    'Every rational m×m matrix of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.',
    ['linear-algebra'],
    ['A=E_1\\Pi E_2','the Bruhat factorization for arbitrary matrices, with coordinate order'],
    aliases=['Bruhat factorization'])
add('matrix-shear','Rank-bounded matrix shear on address fields',
    'The permutation (H,D) ↦ (H + AD, D) of address fields over Z/q^b costs exactly rank(A) interchanges of b-digit fields plus linear work, since triangular parts are controlled shifts.',
    ['matrix-factorization','controlled-shifts'],
    ['can be performed with exactly $a$ interchanges of pairs of $b$-digit',
     '(H,D)\\longmapsto(H+AD,D)'])
add('power-width-interchange','Recursive power-width interchange',
    'For width e = m^k, a shear circuit built from the bit network turns one interchange of two e-digit chunks into s interchanges of width e/m on role streams of volume V/W, giving cost O(V e^τ).',
    ['rank-saving','matrix-shear','bit-network-interface','stream-scans'],
    ['The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every',
     'D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D'])
add('address-interchange','Fast address-chunk interchange',
    'Exchanging two disjoint contiguous address fields of u bits in an array with product address set costs O(V u^τ) for a fixed τ < 1, although intermediate steps form XOR combinations of data.',
    ['power-width-interchange','stream-scans'],
    ['The first procedure interchanges two disjoint contiguous address',
     'by the address permutation',
     'in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$'],
    aliases=['chunk swap','arbitrary-width interchange'])
add('packed-selected-bit-addition','Packed selected-bit addition with repair',
    'XORing one selected bit position of f chunks into another chunk is done by a few cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small set of addresses where guard values fail.',
    ['address-interchange','controlled-shifts'],
    ['We implement a binary row addition on corresponding selected bits in two address chunks.',
     'y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}'])
add('simultaneous-butterfly-layer','Simultaneous butterfly layer',
    'The butterfly H₀ applied at once to the same bit position of up to d address chunks of polynomial-record arrays, computed via C^{⊗D} on the phase network, at cost O(V d^{λ\'}) instead of d passes.',
    ['phase-interface','packed-selected-bit-addition','fixed-point-disk','two-point-kernel','rank-saving','polynomial-ring'],
    ['simultaneously on selected coordinate bits of the numerical arrays',
     'the cost is $O(Vd^{\\lambda\'})$ for a fixed $\\lambda\'<1$.',
     'H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D'],
    aliases=['fast butterfly layer'])
add('transform-layout','Transform layout for parallel butterfly rounds',
    'A positional address permutation moves the selected bits of all axes into common-offset consecutive K-bit chunks so each transform round is one simultaneous butterfly layer; it costs O(Tp[dK + pK^{τ−1} + ℓ d^{λ\'}]).',
    ['synthetic-transform','simultaneous-butterfly-layer','address-interchange','stored-frequency-order'],
    ['we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks',
     'The procedure constructs an explicit positional layout permutation $L$ of record addresses'])
add('ring-convolution','Convolution from the retained transform layout',
    'Two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform, all in one retained order, give the normalized convolution (f*g)/(rM) over the polynomial ring with explicit error.',
    ['transform-layout','signed-packing','stored-frequency-order','convolution','fixed-point-disk'],
    ['Perform both forward transforms and retain their common $LB$ order.',
     '\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}'])

add('parameter-regime','Parameter regime for input length n',
    'All sizes are tied to b = ⌈log₂ n⌉: precision p = 6b, d = ⌊b^ε⌋ axes, K = ⌊d^c⌋, padded size T about n/b, record length r = 2^{⌈log₂T/d⌉} so that Tp = Θ(n) and r grows faster than any power of p.',
    ['radix-digit-reduction','multidimensional-transform','fixed-point-disk'],
    ['b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,',
     'Take the power of two $T$ in $[4n/b,8n/b)$'])
add('prime-lengths','Prime source lengths near powers of two',
    'Distinct odd primes s_i with (1−2η)t_i < s_i ≤ (1−η)t_i are found by deterministic search, so S = ∏s_i lies in (T/2, T) and each ratio t_i/s_i leaves enough separation for Gaussian resampling.',
    ['parameter-regime','gaussian-resampling','crt-prime-axes'],
    ['The distinct prime lengths $s_i$ must be close to the powers of two',
     '(1-2\\eta)t_i<s_i\\leq(1-\\eta)t_i'])
add('precision-recovery','Error analysis and exact recovery of the product',
    'Every call returns disk-grid values with bounded error and norm margins; after removing the known scales the coefficient error is below 1/2, so rounding gives the exact integer coefficients and carries give the product.',
    ['fixed-point-disk','radix-digit-reduction','ring-convolution','retained-permutations'],
    ['proves that the recovered coefficient error is strictly below $1/2$',
     'Scales and disk margins'])
add('multiplication-algorithm','The multiplication algorithm',
    'Digits are placed on prime axes by the CRT map, transformed by resampling, chirp and polynomial-ring convolution, multiplied pointwise, transformed back with the opposite sign, rescaled, rounded and carry-propagated to give the 2n-bit product.',
    ['crt-prime-axes','retained-permutations','chirp-identity','coefficient-twist','ring-convolution','prime-lengths','parameter-regime','precision-recovery','radix-digit-reduction'],
    ['The source-transform procedures now supply the three transforms needed for the radix-digit convolution.',
     'Propagate radix-$2^b$ carries in increasing coefficient order.'])
add('time-bound','Complete time bound and the power saving',
    'Dividing costs by Tp, the seven dominant terms (layout moves, chunk exchanges, butterfly rounds, CRT layouts, Gaussian line maps, chirps, packed products) have exponents at most 1 − 2κ of p, giving O(n (log n)^{1−κ}).',
    ['multiplication-algorithm','address-interchange','simultaneous-butterfly-layer','transform-layout','parameter-regime'],
    ['Thus $\\min_i g_i=2^{-181}=2\\kappa$.',
     'The complete large-input bound is consequently'])
add('main-theorem','Integer multiplication in O(n (lg n)^(1−κ)) time',
    'One deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, beating the n log n conjecture by a power of the logarithm.',
    ['time-bound','multiplication-algorithm','nlogn-conjecture','fixed-tape-model'],
    ['T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right)',
     'computes this exact product for every $n\\ge1$ and every pair of $n$-bit',
     'We give a deterministic algorithm that multiplies two $n$-bit integers'],
    aliases=['main theorem'],
    title='Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time',
    symbols=[dict(symbol='n',name='input length',meaning='The number of bits in each of the two integers being multiplied.',relation='count'),
             dict(symbol='\\kappa',name='saving exponent',meaning='The fixed constant 2^{-182} by which the power of the logarithm is reduced below 1.',relation='direct')])

ids = {c['id'] for c in C}
ok = True
for c in C:
    for r in c['requires']:
        if r not in ids: print('bad req', c['id'], r); ok = False
    for e in c['evidence']:
        if norm(e['quote']) not in nsrc:
            print('MISSING', c['id'], e['quote']); ok = False
    if not c['known'] and not c['evidence']: print('noevid', c['id']); ok=False
    if c['known'] and c['requires']: ok=False
# cycle check
import graphlib
ts = graphlib.TopologicalSorter({c['id']: c['requires'] for c in C})
ts.prepare()
out = {'target':'main-theorem','concepts':C}
json.dump(out, open('/home/user/openai-nlogn-wiki/runs/G5/exegenius/tasks/0001-extract.answer.json','w'), ensure_ascii=False, indent=1)
print('ok' if ok else 'PROBLEMS', len(C))
