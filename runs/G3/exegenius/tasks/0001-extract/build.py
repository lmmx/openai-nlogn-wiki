import json, re, sys
src = open('/home/user/openai-nlogn-wiki/runs/G3/sources/paper.tex').read()
def norm(s): return re.sub(r'\s+', ' ', s)
nsrc = norm(src)

C = []
def add(id, name, gloss, requires, quotes, known=False, aliases=None, title=None, symbols=None):
    d = dict(id=id, name=name, aliases=aliases or [], gloss=gloss, requires=requires, known=known,
             evidence=[dict(source='paper', quote=q) for q in quotes])
    if title: d['title'] = title
    if symbols: d['symbols'] = symbols
    C.append(d)

add('big-o','Big-O notation','Asymptotic upper bounds such as O(n log n) on running time.',[],[],known=True)
add('polynomials','Polynomials','Expressions Σ aₖ yᵏ with coefficients, added and multiplied coefficientwise with exponent addition.',[],[],known=True)
add('complex-numbers','Complex numbers','Numbers a + bi with i² = −1, including roots of unity e^{2πik/q} of modulus one.',[],[],known=True)
add('turing-machine','Multitape Turing machine','A machine with a finite alphabet and several one-dimensional tapes, each step reading and writing one cell per tape and moving each head by at most one cell.',[],[],known=True)

add('mult-history','History of fast multiplication and the n log n conjecture',
 'Schönhage–Strassen (1971) multiplied n-bit integers in O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Fürer and later work reduced the extra factor, and Harvey and van der Hoeven reached O(n log n).',
 ['big-o','turing-machine'],
 ['Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper bound',
  'disproves the $n\\log n$ optimality conjecture'])

add('radix-convolution','Integer product as digit-polynomial convolution',
 'Writing each n-bit input in radix 2^b gives digit polynomials whose ordinary product has coefficients below 2^{3b}, so the integer product is the convolution of the digit lists followed by carry propagation.',
 ['polynomials'],
 ['Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.',
  'Write the two inputs as polynomials in $2^b$, each with $q=\\lceil n/b\\rceil$ nonnegative digits.'])

add('dft-convolution','Discrete Fourier transform and cyclic convolution',
 'The normalized length-q transform (F_q u)_k = (1/q) Σ u_j e^{−2πijk/q} turns cyclic convolution into pointwise multiplication, and its opposite-sign transform inverts it up to scale.',
 ['complex-numbers','polynomials'],
 ['(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}',
  'The normalized convolution rule is'])

add('multidim-transform','Multidimensional transforms on product axes',
 'A transform on an array indexed by a product of axes, defined as the tensor product of one-dimensional transforms and computed one axis (coordinate line) at a time.',
 ['dft-convolution'],
 ['it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two',
  'apply the one-dimensional maps to one coordinate line at a time'])

add('modular-crt','Modular arithmetic and the Chinese remainder theorem',
 'Residues modulo pairwise coprime moduli determine a number modulo their product, so a cyclic index of length s₁⋯s_d splits into independent coordinates modulo each sᵢ.',
 [],
 ['Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution'])

add('crt-prime-axes','Chinese-remainder address map to prime axes',
 'A ring isomorphism sending x to ∏ xᵢ^{μᵢ} that places a length-S cyclic coefficient list on a product of cyclic axes of pairwise coprime (prime) lengths while preserving convolution; the induced address change is a sequence of triangular controlled shifts.',
 ['modular-crt','radix-convolution','dft-convolution','controlled-shifts'],
 ['the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution',
  'Hence $\\Phi$ is an isomorphism and preserves cyclic convolution.'])

add('fixed-point-grid','Fixed-point complex numbers on a disk grid',
 'Complex values with real and imaginary parts that are integer multiples of 2^{−p} inside the unit disk, stored as two signed two\'s-complement words, with truncation toward zero to the grid.',
 ['complex-numbers'],
 ['A $p$-bit grid array has real and imaginary coefficient parts in $2^{-p}\\mathbb Z$.',
  'a signed $w_{\\rm c}$-bit two\'s-complement word for $a$'])

add('contraction-error','Contractions and error accumulation',
 'A linear map that never increases the maximum coordinate modulus is a contraction, so approximation errors of composed steps add and every normalized transform keeps values inside the unit disk.',
 ['fixed-point-grid','dft-convolution'],
 ['Composing such algorithms adds their errors',
  'Each normalized Fourier transform above is a contraction'])

add('gaussian-resampling','Gaussian resampling with permutations retained',
 'An identity P_s F_s = 2^{2α²} B₀ P_t F_t A (tensored over axes) expressing a Fourier transform of prime-related length s through a transform of power-of-two length t using Gaussian-weighted contractions A and B₀, with the coordinate permutations kept inside the formula.',
 ['dft-convolution','multidim-transform','contraction-error','modular-crt'],
 ['Gaussian resampling connects these two shapes.',
  'We retain both permutations in the transform formula and compute that formula directly.'])

add('chirp-identity','Bluestein chirp identity',
 'Multiplying by a quadratic-phase chirp before and after a cyclic convolution with the chirp reproduces the permuted Fourier transform Q F_t, so a transform becomes a convolution.',
 ['dft-convolution','multidim-transform'],
 ['Bluestein\'s chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution.'])

add('permutation-cancel','Source permutation cancellation',
 'The coordinate permutation R retained in the source transform cancels across the two forward transforms, their pointwise product and the opposite-sign transform, so the product is exactly u*v/S².',
 ['gaussian-resampling','multidim-transform','modular-crt'],
 ['the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform'])

add('negacyclic-ring','Negacyclic ring ℂ[y]/(yʳ + 1)',
 'The ring of complex polynomials of degree below r taken modulo yʳ + 1, in which multiplying by a power of y is a signed shift of the coefficient list.',
 ['polynomials','complex-numbers'],
 ['\\mathcal R_r=\\mathbb C[y]/(y^r+1)',
  'multiplication by such a root is a signed shift of the coefficient list'],
 title='Negacyclic ring $\\mathbb C[y]/(y^r + 1)$',
 symbols=[
  dict(symbol='\\mathbb C',name='complex numbers',meaning='The field of complex numbers from which the polynomial coefficients are taken.',relation='direct'),
  dict(symbol='y',name='ring variable',meaning='The indeterminate of the polynomials, whose powers act as roots of unity.',relation='direct'),
  dict(symbol='r',name='coefficient count',meaning='The number of complex coefficients in a ring element, which is a power of two.',relation='count')])

add('synthetic-transforms','Synthetic polynomial transforms',
 'Fourier-type transforms F_t^± over the negacyclic ring using the roots ω_t = y^{2r/t}, so multiplication by a root is a free signed shift; their character sums cancel to give F⁺F⁻ = I/t.',
 ['negacyclic-ring','dft-convolution','multidim-transform'],
 ['These are the synthetic polynomial transforms of Nussbaumer and Quandalle',
  'For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.'])

add('butterfly-order','Radix-2 butterflies and stored frequency order',
 'The decimation-in-frequency recursion applies the two-point butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and a twiddle shift at each level, writing outputs in bit-reversed order that the opposite transform consumes directly.',
 ['synthetic-transforms'],
 ['The two outputs of $H_0$ occupy these same slots',
  'entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$'])

add('phase-twist','Phase twist from cyclic to negacyclic wrap',
 'Multiplying coefficient k of the last cyclic axis by e^{πik/r} makes a length-r cyclic coordinate a polynomial modulo yʳ + 1, and the negative wrap becomes the correct cyclic wrap after untwisting.',
 ['negacyclic-ring','dft-convolution','synthetic-convolution'],
 ['A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed.'])

add('stream-scans','Elementary stream scans on tapes',
 'Splitting, merging, digit moves and row-wise stream splitting on a lexicographically stored array cost O(V) steps for volume V on a fixed number of tapes, with counters and head returns included.',
 ['turing-machine','big-o'],
 ['takes $O(V)$ steps on a fixed number of one-dimensional tapes',
  'An array with address set $[a_1]\\times\\cdots\\times[a_t]$ is stored in lexicographic order'])

add('controlled-shifts','Controlled cyclic shifts of an address field',
 'Updating a target field y mod q^b by an offset computed from earlier control fields, or multiplying it by a unit, costs O(V) on tape by splitting each fiber at the offset and merging the pieces swapped.',
 ['stream-scans','modular-crt'],
 ['Suppose a target field $y\\in[Q]$ follows its control fields',
  'y\\longmapsto y+a(\\text{controls})\\pmod Q'])

add('signed-packing','Signed packing of polynomial products',
 'A Kronecker-substitution reduction that evaluates polynomials at 2^{4p}, multiplies the resulting integers with the established O(N log N) multiplier, and extracts signed coefficients to get exact products in the negacyclic ring.',
 ['negacyclic-ring','mult-history','polynomials'],
 ['reduction is a signed form of Kronecker substitution',
  'Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine calls'])

add('linear-spaces','Subspaces, orthogonal complements and bilinear forms',
 'Linear subspaces of a vector space with a nondegenerate bilinear form, their orthogonal complements, projections and dimensions, used to label network vertices.',
 [],
 ['A label is a nondegenerate subspace of a fixed bilinear space.'])

add('matrix-shear','Matrix shears and triangular factorization',
 'The address map (H,D) → (H+AD,D) for a rational matrix A of rank a is done with exactly a field interchanges plus linear-cost triangular updates, using the factorization A = E₁ΠE₂ with E₁,E₂ lower triangular.',
 ['linear-spaces','controlled-shifts'],
 ['Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization',
  'can be performed with exactly $a$ interchanges of pairs of $b$-digit fields'])

add('common-frame','Frames and pointwise gates',
 'Giving every wire at a gate the same invertible linear operator on its address-indexed array lets the pointwise linear gate commute with it, so only endpoint frames determine the net operator and edges change frames cheaply.',
 ['linear-spaces','stream-scans'],
 ['assign an invertible $R$-linear operator $D_v$ on $R^\\Omega$, called its \\emph{frame}',
  'G(D_vg_1,\\ldots,D_vg_t)=D_vG(g_1,\\ldots,g_t)'])

add('scratch-network','Scratch-restoring bank-exchange network',
 'A fixed network of pointwise linear gates built from copy, gather, scatter and side wires over three-element subsets that exchanges two data banks in three stages and returns every auxiliary scratch wire to its arbitrary initial value.',
 ['linear-spaces'],
 ['We construct two fixed linear networks that exchange two banks of values while restoring every auxiliary value.',
  'For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.'])

add('subspace-labels','Nested subspace labels and the rank saving',
 'Subspaces of an m-dimensional space attached to gates and terminals, nested along edges, so that the sum of edge ranks s is strictly less than the wire count W times m.',
 ['scratch-network','common-frame','linear-spaces'],
 ['The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.',
  'The subsets at adjacent vertices are nested.' ] if False else
 ['The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.'])

add('rank-saving-recurrence','Recursion with a strict rank saving',
 'Each call at parameter mf makes s calls at parameter f on streams of volume V/W, so the normalized cost obeys F_k ≤ (s/W)F_{k−1} + O(1) and, because s/W < m, grows like m^{kτ} with τ < 1.',
 ['subspace-labels','matrix-shear','stream-scans'],
 ['This strict inequality is the source of the power saving.',
  'F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)'])

add('address-interchange','Fast address chunk interchange',
 'Two disjoint equal-width address chunks of u bits are exchanged in O(V u^τ) time for a fixed τ < 1 by computing XOR combinations of intermediate streams through the bit network, even though the net effect is an exact permutation.',
 ['rank-saving-recurrence','matrix-shear','common-frame','stream-scans'],
 ['The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every other address field',
  '(p,h,g,d,z)\\longmapsto(p,d,g,h,z)'])

add('phase-frames','Phase frames and the two-point kernel C',
 'Over binary labels the frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} turn each edge into a product of translation kernels aI + bX_v built from C = H S H, with H₀ = b S C S.',
 ['subspace-labels','common-frame','linear-spaces','complex-numbers'],
 ['C=H\\mathsf SH=aI+bX',
  'H_0=b\\mathsf SC\\mathsf S'])

add('packed-bit-addition','Packed addition on selected address bits',
 'A binary row addition y_j ← y_j ⊕ x_j on the same bit position of several address chunks, done by a constant number of whole-chunk cyclic shifts plus a deterministic repair of a small exceptional address set.',
 ['address-interchange','controlled-shifts'],
 ['We implement a binary row addition on corresponding selected bits in two address chunks.'])

add('butterfly-layer','Fast simultaneous butterfly layer',
 'The two-point butterfly H₀ applied at once to one bit position of each of up to d address chunks of polynomial records costs O(V d^λ′) with λ′ < 1, evaluated exactly in Gaussian dyadics and truncated once.',
 ['phase-frames','packed-bit-addition','rank-saving-recurrence','butterfly-order','fixed-point-grid'],
 ['simultaneously on selected coordinate bits of the numerical arrays',
  'A single truncation follows the completed contractive layer.'])

add('transform-layout','Tape layout for synthetic transforms',
 'A positional permutation of record addresses puts the selected bits of all participating axes at a common offset in consecutive K-bit chunks, so each transform round is one simultaneous butterfly layer.',
 ['address-interchange','butterfly-layer','butterfly-order','synthetic-transforms'],
 ['The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes'])

add('synthetic-convolution','Convolution from the retained transform layout',
 'Two forward synthetic transforms keep their common stored frequency order, the ring records are multiplied pointwise by signed packing, and the opposite transform consumes that order to give normalized convolution over the negacyclic ring.',
 ['transform-layout','signed-packing','contraction-error','synthetic-transforms'],
 ['Perform both forward transforms and retain their common $LB$ order.'])

add('parameter-choice','Parameter choices and prime source lengths',
 'The padded box size T, precision p = 6b, number of axes d, chunk width K, ring size r and distinct odd primes sᵢ just below the power-of-two axis lengths tᵢ are chosen so the resampling and layer hypotheses hold.',
 ['gaussian-resampling','crt-prime-axes','radix-convolution'],
 ['b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor',
  'We may therefore choose distinct odd primes satisfying'])

add('exact-recovery','Exact recovery by rounding and carries',
 'Because the accumulated numerical error on every recovered coefficient is below 1/2, rounding gives the exact integer convolution coefficients, and radix-2^b carry propagation yields the 2n-bit product.',
 ['radix-convolution','contraction-error','fixed-point-grid'],
 ['Round the represented real values to the nearest integers.',
  'Propagate radix-$2^b$ carries in increasing coefficient order.'])

add('cost-table','Cost accounting and the exponent κ',
 'Dividing every step\'s cost by the volume Tp gives seven dominant powers of p, each at most 1 − 2κ, which with κ = 2^{−182} yields total time O(n (lg n)^{1−κ}).',
 ['parameter-choice','address-interchange','butterfly-layer','transform-layout','gaussian-resampling','chirp-identity','signed-packing'],
 ['Thus $\\min_i g_i=2^{-181}=2\\kappa$.',
  'O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})'])

add('multiplication-algorithm','The multiplication algorithm',
 'Convert inputs to radix-2^b digit lists, map them by the Chinese-remainder address map, apply the resampled chirp source transform to each, multiply pointwise, apply the opposite transform, rescale, round, undo the address map and propagate carries.',
 ['crt-prime-axes','gaussian-resampling','chirp-identity','permutation-cancel','phase-twist','synthetic-convolution','exact-recovery','radix-convolution','parameter-choice'],
 ['Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain source arrays $u,v$.'])

add('main-theorem','Integer multiplication in O(n (lg n)^(1−κ)) time',
 'A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.',
 ['multiplication-algorithm','cost-table','mult-history'],
 ['We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time',
  'disproves the $n\\log n$ optimality conjecture'],
 title='Integer multiplication in $O(n(\\lg n)^{1-\\kappa})$ time',
 symbols=[
  dict(symbol='n',name='input length',meaning='The number of bits in each of the two operands.',relation='count'),
  dict(symbol='\\kappa',name='saving exponent',meaning='The fixed constant 2^{-182} giving the power saving in the logarithmic factor.',relation='direct')])

ids = {c['id'] for c in C}
assert len(ids)==len(C)
for c in C:
    for r in c['requires']: assert r in ids,(c['id'],r)
    if c['known']: assert not c['requires']
    for e in c['evidence']:
        if norm(e['quote']) not in nsrc: print('MISSING',c['id'],e['quote']); sys.exit(1)
    if not c['known']: assert c['evidence'],c['id']
# cycle check
color={}
def dfs(u):
    color[u]=1
    for v in next(c for c in C if c['id']==u)['requires']:
        if color.get(v)==1: raise Exception('cycle %s %s'%(u,v))
        if v not in color: dfs(v)
    color[u]=2
for i in ids:
    if i not in color: dfs(i)
json.dump(dict(target='main-theorem',concepts=C),open('/home/user/openai-nlogn-wiki/runs/G3/exegenius/tasks/0001-extract.answer.json','w'),indent=1,ensure_ascii=False)
print('ok',len(C))
