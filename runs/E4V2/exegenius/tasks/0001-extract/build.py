import json, re, sys
src = open('/home/user/openai-nlogn-wiki/runs/P2/sources/paper.tex', encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
S = norm(src)

C = []
def add(id, name, gloss, requires, quotes, known=False, aliases=(), title=None, symbols=None):
    d = dict(id=id, name=name, aliases=list(aliases), gloss=gloss, requires=list(requires), known=known,
             evidence=[dict(source='paper', quote=q) for q in quotes])
    if title: d['title'] = title
    if symbols: d['symbols'] = symbols
    C.append(d)

# known
add('big-o','Big-O notation','Asymptotic upper bounds on running time such as O(n log n).',[],[],known=True)
add('polynomials','Polynomials','Sums of powers of an indeterminate with coefficients, multiplied by collecting terms.',[],[],known=True)
add('complex-numbers','Complex numbers','Numbers a + bi with i² = −1, with modulus and the unit-modulus numbers e^{iθ}.',[],[],known=True)
add('turing-machine','Multitape Turing machine','A machine with a finite alphabet, a finite control and a fixed number of tapes, each read and written one cell per step by a head.',[],[],known=True)
add('bitwise-xor','Bitwise XOR and arithmetic mod 2','Addition of bits modulo 2, so that x ⊕ x = 0.',[],[],known=True)

add('integer-multiplication-problem','Exact integer multiplication on a multitape Turing machine',
 'Given x#y with x,y n-bit binary strings, output the 2n-bit binary product; cost is the number of steps of one fixed machine with a fixed alphabet and a fixed number of one-dimensional tapes, and lg n = max(⌈log₂ n⌉, 1).',
 ['turing-machine','big-o'],
 ["Write $\\lg n=\\max\\{\\lceil\\log_2 n\\rceil,1\\}$.",
  "A machine has one fixed finite alphabet and one fixed finite number of",
  "its nonnegative integer value, with the leftmost bit most significant."])

add('optimality-conjecture','Schönhage–Strassen n log n optimality conjecture',
 'The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, which is stated here as an eventual lower bound T_A(n) ≥ c·n lg n for every fixed machine A; the paper refutes it.',
 ['integer-multiplication-problem'],
 ["disproves the $n\\log n$ optimality conjecture",
  "machine, and proposed $n\\log n$ as the optimal order of growth",
  "Its negation requires one machine satisfying"],
 aliases=['n log n conjecture'])

add('harvey-hoeven-multiplier','Established O(n log n) multiplier (Harvey–van der Hoeven)',
 'The previously known fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records and never recursively on the improved theorem.',
 ['integer-multiplication-problem'],
 ["Harvey and van der Hoeven reached the unconditional $O(n\\log n)$ upper",
  "Calls to the established $O(n\\log n)$ multiplier are ordinary subroutine"])

add('dft','Normalized discrete Fourier transform',
 'The map sending a length-q vector u to (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}; the opposite-sign transform F⁺ uses e^{+2πi jk/q}, and each is a contraction in the max-modulus norm.',
 ['complex-numbers'],
 ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q}",
  "Each normalized Fourier transform above is a contraction, since each"],
 aliases=['Fourier transform'])

add('cyclic-convolution','Cyclic convolution and the convolution theorem',
 'The convolution f*g on a cyclic group, which the Fourier transform turns into a pointwise product (F(u*v) = S·(Fu)·(Fv) with size normalizations), so convolution can be computed by transform, pointwise multiply, inverse transform.',
 ['dft','polynomials'],
 ["cyclic convolution on the product of the coordinate groups and a dot",
  "$F_{\\boldsymbol s}(u*v)=S(F_{\\boldsymbol s}u)\\mathbin{\\cdot}"],
 aliases=['convolution'])

add('multiplication-by-convolution','Integer multiplication as convolution of radix digits',
 'Write each operand as a polynomial in 2^b with radix-2^b digit coefficients; the product coefficients are a convolution of digit lists (each below 2³ᵇ), padded so cyclic convolution has no wraparound, and carries recover the integer product.',
 ['cyclic-convolution','integer-multiplication-problem','polynomials'],
 ["Splitting the inputs into radix digits reduces multiplication to",
  "Thus convolution modulo $x^S-1$ has no nonzero wraparound."])

add('fft-butterfly','Two-point butterfly and radix-2 fast Fourier transform',
 'The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) pairs entries half a block apart; a decimation-in-frequency transform of length 2^a applies butterflies and twiddle-factor multiplications over a levels and leaves the output in bit-reversed order.',
 ['dft'],
 ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)",
  "decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"],
 aliases=['butterfly','FFT'])

add('linear-algebra-basics','Matrix rank, subspaces and orthogonal complements',
 'Vector subspaces, rank and dimension of a matrix, projections onto a subspace along its orthogonal complement, and bilinear forms (nondegenerate when no nonzero vector is orthogonal to the whole space).',
 [],
 ["$P_V-P_U$ is the identity on $V\\cap U^\\perp$ and zero on its",
  "A label is a nondegenerate subspace of a fixed bilinear space."])

add('tensor-product','Tensor products of operators and arrays',
 'The Kronecker product of linear maps or index sets, so an operator on several coordinates (columns, axes) acting identically on each is written as a tensor power.',
 ['linear-algebra-basics'],
 ["For the tensor product, apply the one-dimensional maps to one coordinate",
  "The ambient label space is $\\mathcal F=F^{\\otimes3}$ with its tensor"])

add('multidimensional-transform','Multidimensional transform on a tensor of axes',
 'The tensor product F_{q₁}⊗…⊗F_{q_d} of one-dimensional Fourier transforms over d axes, computed one axis (line) at a time, with multidimensional cyclic convolution handled the same way.',
 ['dft','cyclic-convolution','tensor-product'],
 ["this convolution by multidimensional transforms whose axis lengths are",
  "F_{\\boldsymbol q}:=\\bigotimes_iF_{q_i}."])

add('fixed-point-disk-arithmetic','Disk-grid fixed-point arithmetic, contractions and error',
 'Complex numbers with real and imaginary parts that are multiples of 2^{−p} in the unit disk, stored as two signed two\'s-complement words; Q_p truncates toward zero, linear contractions do not increase the max norm, and errors of composed approximations add.',
 ['complex-numbers'],
 ["\\mathbb D_p=\\{2^{-p}(a+ib):a,b\\in\\mathbb Z,\\ a^2+b^2\\leq 2^{2p}\\}",
  "An approximation $\\widetilde L:\\mathbb D_p^a\\to\\mathbb D_p^b$",
  "Composing such algorithms adds their errors"],
 aliases=['disk grid','truncation Q_p'])

add('elementary-streams','Array order and elementary stream scans',
 'Arrays stored in lexicographic order on a tape, with address fields and rows; fixed digit permutations, digit moves, splitting into aligned streams, pointwise maps and merging are done in time linear in the volume with counters and rewinds charged.',
 ['turing-machine','big-o'],
 ["lexicographic order, with the first coordinate most significant.",
  "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
  "The \\emph{logical volume} $V$ is the number of stored data bits."])

add('controlled-cyclic-shifts','Controlled cyclic shifts and fixed rational scalings',
 'Updating a target address field y ↦ y + a(controls) mod q^b, where the controls precede the target on tape, by splitting each fiber into two pieces and merging in swapped order in linear time; also multiplication by fixed rational units mod q^b.',
 ['elementary-streams'],
 ["Controlled shifts and fixed rational scalings",
  "Suppose a target field $y\\in[Q]$ follows its control fields, each control"])

add('crt-address-map','Chinese-remainder address map to distinct prime axes',
 'An algebra isomorphism x ↦ Π x_i^{μ_i} turning one cyclic convolution of length S = Π s_i (pairwise coprime) into a d-dimensional cyclic convolution on prime axes, implemented as triangular controlled shifts plus axis reordering and zero padding.',
 ['multidimensional-transform','multiplication-by-convolution','controlled-cyclic-shifts'],
 ["Cyclic convolution on distinct prime axes",
  "theorem to convert one cyclic convolution into multidimensional cyclic",
  "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}"],
 aliases=['Agarwal–Cooley map','Φ'])

add('gaussian-resampling','Gaussian resampling with permutations left in the transform',
 'Replaces a Fourier transform of length s (coprime to t, s<t) by one of length t via Gaussian-weighted contractions A and B₀, with P_s F_s = 2^{2α²} B₀ P_t F_t A, where the two coordinate permutations P_s, P_t stay inside the formula instead of being sorted separately; applied axis by axis for a tensor.',
 ['multidimensional-transform','fixed-point-disk-arithmetic'],
 ["The transform lengths needed for the integer product are pairwise coprime,",
  "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA",
  "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A"],
 aliases=['Gaussian resampling'])

add('bluestein-chirp','Bluestein chirp identity',
 'Writes the (permuted) transform Q·F_t as pointwise multiplication by a chirp ā, a cyclic convolution with the chirp a, and another pointwise multiplication by ā, so a transform becomes a normalized cyclic convolution.',
 ['cyclic-convolution','gaussian-resampling'],
 ["Next, Bluestein's chirp identity converts the middle transform,",
  "computed from a cyclic convolution and two pointwise phase",
  "QF_{\\boldsymbol t}u"],
 aliases=['chirp identity'])

add('permutation-cancellation','Source permutation cancellation',
 'Because the coordinate permutation R commutes with pointwise products and R F⁺ R = F⁺, the retained permutation in R F_s cancels across two forward transforms, a pointwise product and the opposite transform, giving (u*v)/S².',
 ['gaussian-resampling','cyclic-convolution'],
 ["retained source permutation $R$ cancels when computing a convolution.",
  "Finally, the source permutation retained during resampling cancels"])

add('polynomial-ring-mod','Polynomial ring modulo yʳ + 1',
 'The ring of complex polynomials of degree less than r with y^r = −1, where multiplying by a power of y permutes the coefficients with sign changes (a signed shift) and so acts as an isometry in the max coefficient norm.',
 ['polynomials','complex-numbers'],
 ["\\mathcal R_r=\\mathbb C[y]/(y^r+1)",
  "is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two."],
 aliases=['negacyclic ring'],
 title='Polynomial ring modulo $y^r + 1$',
 symbols=[dict(symbol='y',name='ring indeterminate',meaning='The formal variable of the polynomials, a root of −1 raised to the r-th power, whose powers serve as roots of unity.',relation='direct'),
          dict(symbol='r',name='polynomial length',meaning='The number of complex coefficients in a stored polynomial, a power of two.',relation='count')])

add('coefficient-twist','Coefficient twist from cyclic to negacyclic wrap',
 'The isomorphism C[x]/(x^r−1) → C[y]/(y^r+1), x ↦ ζy with ζ = e^{πi/r}, which multiplies coefficient k by ζ^k so the negative wrap of the ring becomes the cyclic wrap after untwisting.',
 ['polynomial-ring-mod','cyclic-convolution'],
 ["A phase twist changes the last cyclic coordinate into a polynomial",
  "x_d\\longmapsto\\zeta y"])

add('synthetic-transform','Synthetic polynomial transform',
 'A Fourier transform over the polynomial ring with roots of unity ω_t = y^{2r/t}, so twiddle multiplications are signed shifts; computed by butterflies H₀ and twiddles, leaving outputs in bit-reversed frequency order that is retained through the pointwise product and consumed by the opposite transform.',
 ['polynomial-ring-mod','fft-butterfly','multidimensional-transform'],
 ["synthetic polynomial transforms of Nussbaumer and Quandalle and",
  "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",
  "retain the same frequency order through their pointwise product, and"],
 aliases=['Nussbaumer polynomial transform'])

add('signed-packing','Signed packing of polynomial products (Kronecker substitution)',
 'Evaluating integer polynomials at B₀ = 2^{4p} to get integers, multiplying them with the established multiplier, and extracting signed coefficients by centered residues, then reducing modulo y^r + 1, to multiply ring elements in O(rp log(rp)).',
 ['harvey-hoeven-multiplier','polynomial-ring-mod'],
 ["reduction is a signed form of Kronecker substitution; compare",
  "Signed packing and normalized ring multiplication"])

add('scalar-exchange-network','Linear exchange network with restored scratch wires',
 'A fixed network of linear gates (copy, gather, scatter, side injection) built on triples of an h-element set that exchanges two banks of values (X,Y) ↦ (−Y,X) in three stages while restoring all scratch wires whatever their initial values.',
 ['bitwise-xor'],
 ["Each procedure arises from its own fixed linear network that exchanges two",
  "For arbitrary initial values of its auxiliary wires, a forward",
  "(X_a,Y_a)\\longmapsto(-Y_a,X_a)"],
 aliases=['finite network','motif'])

add('frames','Frames: changing array representation along network edges',
 'Replacing each scalar by an array and attaching an invertible linear operator D_v (frame) to each vertex lets pointwise gates commute with the frame, so the net effect on a route is the endpoint operator D_sink D_source^{-1}.',
 ['scalar-exchange-network','linear-algebra-basics'],
 ["We call $D_v$ its frame: the stored",
  "D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}",
  "At a pointwise linear gate $G$, the common frame commutes with the gate:"],
 aliases=['common-frame identity'])

add('subspace-labels-rank-saving','Nested subspace labels and the total-rank saving',
 'Subspaces of a bilinear space built from triple indicator vectors are attached to gates so adjacent labels are nested; edge cost is the dimension of the orthogonal residual, and the total s over all edges is less than (number of wires) × (space dimension).',
 ['frames','tensor-product'],
 ["The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.",
  "the \\emph{orthogonal residual} is the orthogonal complement of the smaller label inside",
  "\\langle t_S,t_T\\rangle=|S\\cap T|-1"],
 aliases=['rank deficit','orthogonal residual'])

add('rational-matrix-interface','Bit-network rational matrix interface',
 'Assigns rational matrices M_v to gates and terminals of the bit network so that endpoint differences equal the identity and the edge ranks sum to s_b < W_b·m, giving the exponent τ = 1 − 2^{-50} with s/W < m^τ.',
 ['subspace-labels-rank-saving'],
 ["M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m",
  "\\tau=\\sigma=1-2^{-50}"])

add('lower-triangular-factorization','Lower triangular factorization of a matrix',
 'Every rational m×m matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.',
 ['linear-algebra-basics'],
 ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
  "Lower triangular factorization"],
 aliases=['Bruhat factorization'])

add('address-shear-cost','Cost of a rational matrix shear',
 'The address map (H,D) ↦ (H + AD, D) over Z/q^b for a matrix A of rank a is done with exactly a interchanges of b-digit fields plus linear work, by triangular controlled shifts around each pivot and the three-step swap trick.',
 ['lower-triangular-factorization','controlled-cyclic-shifts'],
 ["The cost of a rational matrix shear",
  "(H_i,D_j)\\leftarrow(D_j,H_i),\\qquad"])

add('fixed-tape-recursion-schedule','Depth-first schedule of recursive calls on fixed tapes',
 'Recursive calls on W role streams are run on a fixed set of tapes by parking inactive streams on a stack, copying the active stream to the child, and restoring on return, at O(V) extra cost per node.',
 ['elementary-streams'],
 ["Before a recursive call, append the $W-1$ inactive role streams to the",
  "A fixed-tape depth-first schedule."])

add('power-width-interchange','Recursive power-width chunk interchange',
 'Splits rows cyclically into W role streams, applies the network with shear frames on each edge (s recursive interchanges of chunks of width e/m, each on volume V/W), giving F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ), because s/W < m^τ.',
 ['rational-matrix-interface','address-shear-cost','fixed-tape-recursion-schedule','frames'],
 ["Power-width interchange with rows",
  "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)",
  "is the source of the power saving."])

add('chunk-interchange','Fast interchange of address chunks',
 'Exchanging two disjoint equal-width address chunks (p,h,g,d,z) ↦ (p,d,g,h,z) of u bits in O(V u^τ) time, τ < 1, for arbitrary shapes; internally the permutation is a sequence of XOR combinations.',
 ['power-width-interchange'],
 ["(p,h,g,d,z)\\longmapsto(p,d,g,h,z)",
  "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.",
  "Arbitrary-width interchange"],
 aliases=['address interchange','chunk swap'])

add('phase-kernel','Two-point phase kernel C',
 'The 2×2 matrix C = H S H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying C² = X, C⁴ = I and H₀ = b·S·C·S, so a butterfly equals a diagonal phase, a C kernel, and another phase.',
 ['fft-butterfly','tensor-product'],
 ["C=H\\mathsf SH=aI+bX",
  "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D"])

add('phase-frame-interface','Binary phase interface of the complex network',
 'Using frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels, every edge change is a product of translation kernels aI + bX_v, one per orthonormal residual basis vector, so s_c smaller calls of C^{⊗} suffice and the whole network realizes C^{⊗m} on every role.',
 ['phase-kernel','subspace-labels-rank-saving','frames'],
 ["q_U(x)=\\operatorname{wt}(P_Ux)\\pmod4.",
  "is a product of one translation",
  "Phase frames for a simultaneous butterfly layer"],
 aliases=['phase frames'])

add('packed-selected-bit-addition','Packed selected-bit addition on one rectangle',
 'XORs the selected bits of several chunks into another chunk with a few whole-chunk cyclic shifts that act as packed single-bit additions away from carry-prone guard values, then repairs the small explicitly identified bad set of addresses by sorting, restoring a third scratch chunk.',
 ['chunk-interchange','controlled-cyclic-shifts','bitwise-xor'],
 ["Packed selected-bit addition on one rectangle",
  "\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}",
  "y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}"],
 aliases=['packed change of address bits'])

add('guard-width-exactness','Exact Gaussian dyadic evaluation with guard bits',
 'All intermediate values in one butterfly layer are exact Gaussian dyadics (real and imaginary parts with power-of-two denominators), so extra guard bits of width O(d^{C₁}) bound growth and a single truncation follows the completed contractive layer.',
 ['fixed-point-disk-arithmetic'],
 ["Intermediate values are exact Gaussian dyadics,",
  "A single truncation follows the completed contractive layer.",
  "The accelerated network is evaluated exactly until an entire"])

add('simultaneous-butterfly-layer','Simultaneous normalized butterfly layer',
 'Applies H₀ at once to the same bit position of D ≤ d address chunks of a polynomial-record array via the C-kernel network with phase frames, packed binary basis changes and row splitting among roles, in O(V d^{λ\'}) time for a fixed λ\' < 1 instead of D whole-array passes, with one final truncation.',
 ['phase-frame-interface','packed-selected-bit-addition','guard-width-exactness','power-width-interchange','fixed-tape-recursion-schedule','fft-butterfly'],
 ["Simultaneous normalized butterfly layer",
  "equal-width address chunks, and the cost is $O(Vd^{\\lambda'})$ for a",
  "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D"],
 aliases=['parallel butterfly layer'])

add('synthetic-transform-layout','Transform layout on which parallel layers apply',
 'Places the selected bits of all axes at a common offset of consecutive K-bit chunks using prefix-slot moves and chunk exchanges, so each transform round is one simultaneous butterfly layer; total cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ\'}]).',
 ['synthetic-transform','simultaneous-butterfly-layer','chunk-interchange'],
 ["Transform layout and cost",
  "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right)"])

add('synthetic-convolution','Convolution over the polynomial ring from the retained transform layout',
 'Normalized convolution M_r(f,g) = (f*g)/(rM): two forward synthetic transforms, pointwise ring products by signed packing in the retained stored order, and the opposite transform, with error below √2·M(3ℓ+1)·2^{−p}.',
 ['synthetic-transform-layout','signed-packing'],
 ["\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}",
  "Convolution from the retained transform layout"])

add('parameter-choice','Parameter choice: precision, dimension, axis lengths and prime source lengths',
 'For input length n, take b = ⌈log₂ n⌉, precision p = 6b, dimension d = ⌊b^ε⌋, chunk K = ⌊d^c⌋, power-of-two axis lengths t_i ∈ {r/2, r} with product T ≈ n/b, and distinct odd primes s_i just below t_i with T/2 < S < T so all resampling hypotheses hold.',
 ['multiplication-by-convolution','gaussian-resampling','crt-address-map'],
 ["b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
  "The distinct prime lengths $s_i$ must be close to the powers of two"])

add('precision-exact-recovery','Precision, rounding and carry propagation',
 'Tracks scales (the two factors S and 2^{2b+4}) and disk margins to show the recovered convolution coefficients have error below 1/2, rounds to nearest integers, and propagates radix-2^b carries to output the exact 2n-bit product.',
 ['fixed-point-disk-arithmetic','multiplication-by-convolution'],
 ["Propagate radix-$2^b$ carries in increasing coefficient order.",
  "k_{j+1}=\\left\\lfloor\\frac{c_j+k_j}{Q_0}\\right\\rfloor"])

add('multiplication-algorithm','The multiplication algorithm: digits to transform, pointwise product and back',
 'Convert operands to digit lists on a padded prime-axis box via Φ, apply the source transform (resample, chirp convolution through the twist, resample) to each, multiply pointwise, apply the opposite transform, scale by S and 2^{2b+4}, undo Φ, round and propagate carries.',
 ['crt-address-map','gaussian-resampling','bluestein-chirp','permutation-cancellation','coefficient-twist','synthetic-convolution','parameter-choice','precision-exact-recovery'],
 ["With these streams prepared, perform the following operations.",
  "Integer product\\\\radix-digit convolution"] if False else
 ["With these streams prepared, perform the following operations.",
  "The two occurrences of $S$ in this algorithm undo different"])

add('time-bound-accounting','Time-bound accounting and the exponent κ',
 'Dividing the costs of all stages by Tp = Θ(n) gives a table of normalized costs, each a power of p of at most 1 − 2κ (the minimum margin is 2^{−181} = 2κ with κ = 2^{−182}), so the total is O(n (lg n)^{1−κ}).',
 ['multiplication-algorithm','chunk-interchange','simultaneous-butterfly-layer','synthetic-transform-layout','parameter-choice'],
 ["Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
  "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})",
  "Costs divided by $Tp$; each coefficient"])

add('main-theorem','Power-saving integer multiplication theorem',
 'One deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model; it combines fast address interchange, fast simultaneous butterfly layers, and the resampling–chirp–synthetic-convolution reduction.',
 ['time-bound-accounting','multiplication-algorithm','optimality-conjecture'],
 ["There is one deterministic Turing machine $A$, with a fixed finite",
  "T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right)",
  "We obtain a strict power saving in the"],
 aliases=['Theorem 1'])

bad=0
ids={c['id'] for c in C}
for c in C:
    for r in c['requires']:
        if r not in ids: print('missing req',c['id'],r); bad=1
    for e in c['evidence']:
        if norm(e['quote']) not in S:
            print('BAD QUOTE',c['id'],e['quote']); bad=1
    if not c['known'] and not c['evidence']: print('no evidence',c['id']); bad=1
# cycle check
import collections
state={}
def dfs(u):
    state[u]=1
    for v in next(c for c in C if c['id']==u)['requires']:
        if state.get(v)==1: print('cycle',u,v); return True
        if v not in state and dfs(v): return True
    state[u]=2
for c in C:
    if c['id'] not in state: dfs(c['id'])
out=dict(target='main-theorem',concepts=C)
json.dump(out,open('/home/user/openai-nlogn-wiki/runs/P2/exegenius/tasks/0001-extract.answer.json','w'),ensure_ascii=False,indent=1)
print('done',len(C),'bad' if bad else 'ok')
