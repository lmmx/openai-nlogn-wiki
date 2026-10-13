import json, re, sys
SRC = '/home/user/openai-nlogn-wiki/runs/G5/sources/paper.tex'
src = open(SRC, encoding='utf-8').read()

def ev(q):
    return dict(source='paper', quote=q)

def inf(id, claim, quote, page=None, frm=(), deferred=False, salient=None):
    d = dict(id=id, intention='infer', claim=claim, quote=ev(quote))
    if page: d['page'] = page
    if frm: d['from'] = list(frm)
    if deferred: d['deferred'] = True
    if salient: d['salient'] = salient
    return d

def show(id, claim, method, mot_text, mot_src, children, mot_quote=None, page=None, frm=(), adds=(), salient=None):
    m = dict(text=mot_text, source=mot_src)
    if mot_quote: m['quote'] = ev(mot_quote)
    d = dict(id=id, intention='show', claim=claim, method=method, motivation=m, children=list(children))
    if page: d['page'] = page
    if frm: d['from'] = list(frm)
    if adds: d['adds'] = [dict(symbol=s, name=n, meaning=mn, relation=r) for (s, n, mn, r) in adds]
    if salient: d['salient'] = salient
    return d

# ---------------- Section 3: finite networks ----------------
bank = inf('S1.1.1.1.1.1.1', r'Three stages of the subset gadgets, each adding $x_S$ to $y_S$ whatever the scratch wires hold, send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every scratch wire.',
    'For arbitrary initial values of its auxiliary wires, a forward', page='bank-exchange-network',
    frm=['subset-gadgets', 'binary-arithmetic'],
    salient='Arbitrary initial scratch values leave no trace: they are subtracted off first, the gadgets add the wanted term, and the same values are put back.')
frames = inf('S1.1.1.1.1.1.2', r'Because every gate is pointwise and linear it commutes with a common frame $D_v$ on all of its wires, so the network on arrays realizes $D_{\rm out}\mathsf S D_{\rm in}^{-1}$ and only the endpoint frames matter.',
    'Thus the common frame commutes with the pointwise gate, and', page='frames',
    frm=['bank-exchange-network', 'linear-algebra'])
labels = inf('S1.1.1.1.1.1.3', r'Giving each gate and terminal a nondegenerate subspace label, nested along every edge, makes each edge cost its label-dimension change; the only decreasing edges are the central-wire returns, so the total rank cost is $Wm-2N+2L$.',
    'edges are the central-wire edges from time 3 to time 4; their dimension', page='subspace-labels',
    frm=['frames', 'subset-gadgets', 'linear-algebra'])
bitif = inf('S1.1.1.1.1.1.4', r'With XOR gates and projections $P_U$ as frame matrices, the bit network permutes its roles, the endpoint matrices differ by the identity (a shear $H\leftarrow H+D$), and the sum of edge ranks is $s<Wm$.',
    r'The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates,', page='bit-network-interface',
    frm=['subspace-labels', 'frames', 'binary-arithmetic'])
rankbound = inf('S1.1.1.1.1.1.5', r'The rank deficit is large enough for an explicit exponent: $s/W<m^\tau$ with $\tau=1-2^{-50}$.',
    r'\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,')

rank_saving = show('S1.1.1.1.1.1',
    r'Fixed linear networks exist that exchange two banks of values with prescribed signs, restore every auxiliary wire, and have total edge rank $s$ strictly less than the wire count times $m$, namely $s<Wm$.',
    'Build the bank exchange from three-element-subset gadgets, track the representation of each wire by a common frame, attach nested subspace labels so that every edge costs only its label-dimension change, and add up the ranks',
    'The power saving rests on the number of smaller operations on edges being strictly below the number of wires times the dimension, so the construction must be organised so that this rank count can be read off edge by edge.',
    'explicit', [bank, frames, labels, bitif, rankbound],
    mot_quote='The saving will come from keeping the total dimension lost on decreasing',
    page='rank-saving', frm=['subset-gadgets', 'linear-algebra', 'graphs-directed-acyclic-graphs-and-circuits'],
    adds=[('W', 'wire count', 'The number of wires of the finite network, scratch wires included.', 'count'),
          ('m', 'label dimension', 'The dimension of the fixed space whose subspaces label the gates and terminals.', 'count'),
          ('s', 'rank sum', 'The sum, over all edges of the network, of the ranks of the edge operators.', 'count')],
    salient=r'The inequality $s<Wm$ holds with a relative deficit of only about $10^{-11}$, yet any strict gap gives an exponent below 1.')

# ---------------- Section 4 ----------------
matfact = inf('S1.1.1.1.1.2.1', r'Every rational $m\times m$ matrix of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.',
    r'Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization', page='matrix-factorization', frm=['linear-algebra'])
tri = inf('S1.1.1.1.1.2.2', r'A lower triangular change of the fields $H$ or $D$ costs $O(V)$ because each coordinate is updated, in descending physical order, from earlier coordinates by a controlled shift.',
    'A lower triangular transformation of $H$, or of $D$, costs $O(V)$:')
pi_ = inf('S1.1.1.1.1.2.3', r'Each one of $\Pi$, in position $(i,j)$, is realized as $H_i\leftarrow H_i+D_j$ by one interchange of $H_i$ and $D_j$ between two controlled updates, so there are exactly $a$ interchanges.',
    r'Each one in position $(i,j)$ of $\Pi$ calls for')
matshear = show('S1.1.1.1.1.2',
    r'The shear $(H,D)\mapsto(H+AD,D)$ of address fields over $\mathbb Z/q^b\mathbb Z$ costs exactly $\operatorname{rank}(A)=a$ interchanges of $b$-digit fields plus $O(V)$ further work.',
    'Factor the matrix as lower triangular, partial permutation, lower triangular; do the triangular parts by controlled shifts and each one of the partial permutation by a single field interchange',
    'Controlled shifts update a later field from earlier fields in linear time, and lower triangular changes of coordinates can be done entirely in that direction, so the only expensive operations are the interchanges, one per rank.',
    'explicit', [matfact, tri, pi_],
    mot_quote='can be performed entirely in this direction.',
    page='matrix-shear', frm=['controlled-shifts', 'stream-scans', 'modular-arithmetic', 'linear-algebra'],
    adds=[('a', 'matrix rank', 'The rank of the shear matrix, which equals the number of ones of the partial permutation.', 'count')])

pw = [
 inf('S1.1.1.1.1.3', r'Splitting whole rows cyclically into the $W$ role streams gives each stream the same address set and volume $V/W$.',
     'Split whole rows cyclically into $W$ role streams within each prefix'),
 inf('S1.1.1.1.1.4', r'On every edge of the circuit apply the shear with the edge matrix to that role stream, recursively interchanging the pivot pairs of narrower fields, and run each gate pointwise on matching addresses.',
     r'$\Phi_{A_e}$ to that role stream; implement it by'),
 inf('S1.1.1.1.1.5', r'By the common-frame identity the endpoint matrices differ by $I_m$, so the circuit applies the shear $H\leftarrow H+D$ to every row, scratch rows included, and two linear updates turn it into the interchange.',
     'The row split supplies the common address set used in the'),
 inf('S1.1.1.1.1.6', r'The $s$ recursive calls on volume $V/W$ give $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$ for the cost per volume at width $e=m^k$, and since $s/W<m^\tau$ this solves to $F_k=O(e^\tau)$.',
     r'F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).',
     salient=r'The cost per volume grows by the factor $s/W$, strictly less than $m$ per multiplication of the width by $m$, so the width exponent is below 1.'),
 inf('S1.1.1.1.1.7', r'The recursive calls can be scheduled on a fixed number of tapes at linear cost per node by parking the inactive role streams on a stack.',
     r'\paragraph{A fixed-tape depth-first schedule.}'),
]
powerwidth = show('S1.1.1.1.1',
    r'For width $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits (with enough rows before them) are interchanged in $O(Ve^\tau)$ time.',
    'Recursion on the width: perform the shear with the finite bit network on its role streams, each edge being a rank-bounded shear on fields $m$ times narrower, and solve the resulting recurrence',
    r'A call at width $mf$ makes $s$ calls at width $f$ on streams of volume $V/W$, so dividing by the volume the cost per volume grows by $s/W<m$ at each level.',
    'explicit', [rank_saving, matshear] + pw,
    mot_quote='A recursive call at parameter $mf$ therefore uses $s$ calls at parameter',
    page='power-width-interchange', frm=['stream-scans', 'mathematical-induction-and-recurrences', 'modular-arithmetic'],
    adds=[('e', 'chunk width', 'The number of radix-q digits in each of the two chunks being interchanged, a power of m.', 'count'),
          ('k', 'recursion depth', 'The exponent with e = m^k, the number of levels of the recursion.', 'count')])

chunk = inf('S1.1.1.1.2', r'Interchanging two chunks of $u$ bits at arbitrary prefix, gap and suffix lengths takes $O(Vu^\tau)$ for a fixed $\tau<1$, by writing $u$ in base $m$, supplying rows from a few high digits and padding.',
    r'There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape')
addrint = show('S1.1.1.1',
    r'Two disjoint contiguous address fields of $u$ bits in an array of volume $V$ with product address set can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, although intermediate steps form XOR combinations of data.',
    'Realize the interchange as a shear computed by a recursive XOR circuit whose edge ranks sum to less than the wire count, first for power widths with enough rows, then for arbitrary widths by splitting the width in base m',
    'The exponent below one comes from the recurrence on the sum of ranks, so the whole argument is arranged to make that recurrence applicable to arbitrary widths.',
    'explicit', [powerwidth, chunk],
    mot_quote='Because the sum of these ranks is less than the number of wires times',
    page='address-interchange', frm=['stream-scans', 'sets-cartesian-products-and-indexed-arrays'],
    adds=[('u', 'chunk width', 'The number of bits in each of the two address fields being interchanged.', 'count'),
          (r'\tau', 'interchange exponent', 'The fixed exponent below 1 in the cost O(V u^tau) of an interchange.', 'direct')],
    salient='Intermediate steps mix data by XOR, yet the final effect is an exact permutation for arbitrary initial auxiliary contents.')

# ---------------- Section 5: butterfly layer ----------------
phase = inf('S1.1.1.2.1', r'On the complex network with binary labels, each edge frame change is a product of translation kernels $aI+bX_v$, one per residual basis vector, and telescoping the frames gives $C^{\otimes m}$ on every role, scratch roles included.',
    'For each edge of the complex network, write $U,V$ for its tail and', page='phase-interface', deferred=True,
    frm=['subspace-labels', 'frames', 'two-point-kernel', 'bank-exchange-network', 'complex-numbers'],
    salient=r'The same tensor power $C^{\otimes m}$ appears on every role, even on the scratch roles that carry arbitrary values.')
edgek = inf('S1.1.1.2.2', r'Moving the residual directions of an edge into coordinate positions by a binary change of basis turns the edge into one child call per direction on the $f$ axes of one slot.',
    'The number of directional kernels is precisely')
h0 = inf('S1.1.1.2.3', r'The normalized butterfly layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, an exact Gaussian-dyadic rescaling and phase change of the layer $C^{\otimes D}$.',
    r'H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.')
pk = [
 inf('S1.1.1.2.4.1', r'The selected-bit rotations by cyclic shifts of whole chunk ranges give the required XORs except at a small explicit set of addresses.',
     'We first construct eight rotations that have the required effect away'),
 inf('S1.1.1.2.4.2', r'The exceptional addresses are extracted, given destination keys, stably radix sorted and reinserted, which repairs them deterministically.',
     'To implement the correction, scan the stream with a record-rank counter.'),
 inf('S1.1.1.2.4.3', r'The movement costs $O(V(L^\tau+1))$ and the repair adds only a small fraction because the bad fraction is at most $80(f-1)2^{-K}$.',
     'The movement costs $O(V(L^\\tau+1))$.',
     salient='The fraction of addresses needing repair is exponentially small in the chunk length, so the repair costs almost nothing.'),
]
packed = show('S1.1.1.2.4',
    r'XORing the selected bit of $f$ chunks of one range into another range, with a third chunk restored to its arbitrary initial value, costs $O(V(L^\tau+1))$ in the family of parameters used.',
    'Use a constant number of cyclic shifts of whole chunk ranges that are correct away from an explicit small exceptional set, then repair that set by sorting',
    'The shifts are cheap whole-range moves but wrong on some addresses; since the wrong addresses depend only on the addresses, they can be listed and fixed in worst-case time whatever the payload.',
    'explicit', pk,
    mot_quote='The correction depends only on addresses, so the time bound is',
    page='packed-selected-bit-addition', frm=['address-interchange', 'controlled-shifts', 'sorting-and-permutation-of-arrays'])
bf = [
 phase, edgek, h0, packed,
 inf('S1.1.1.2.5', r'A fixed binary change of basis on $e$ axis chunks is a fixed number of packed row additions and costs $O(V((eK)^\tau+1))$.',
     'An invertible matrix over $\\mathbb F_2$ of fixed order $m\\ge3$ is a'),
 inf('S1.1.1.2.6', r'Splitting complete rows among the $W$ roles, after padding, makes each child call run on a stream of exactly $1/W$ of the parent volume.',
     r'\paragraph{Where the rows come from.}'),
 inf('S1.1.1.2.7', r'The recursion $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, stopped at $e<d^{\beta}$, unrolls to a cost per volume $O(d^{\lambda\prime})$ with $\lambda\prime<1$.',
     r'F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),',
     salient='The strict inequality s/W below m again makes the recursive contribution grow more slowly than the number of axes.'),
 inf('S1.1.1.2.8', r'Evaluating the whole layer exactly in Gaussian dyadics needs only $o(p)$ guard bits, so every intermediate value fits in $O(p)$ bits.',
     'The accelerated network is evaluated exactly until an entire'),
 inf('S1.1.1.2.9', r'The procedure returns $Q_p(\mathcal H z)$ in $O(Vd^{\lambda\prime})$ time with a single truncation, coefficientwise error below $\sqrt2\,2^{-p}$, and a result still in the unit disk.',
     'The procedure returns $Q_p(\\mathcal H z)$ in the same array,'),
]
butter = show('S1.1.1.2',
    r'The butterfly $H_0$ applied at once to the same bit position of $D\le d$ address chunks of polynomial-record arrays, followed by one truncation, costs $O(Vd^{\lambda\prime})$ for a fixed $\lambda\prime<1$ instead of $D$ passes.',
    'Compute the equivalent tensor power of the two-point kernel with the complex phase network, by the same recursion as the address interchange, performing its binary changes of basis by packed XORs, then convert back to the normalized butterfly and truncate once',
    r'Separate butterfly factors would need $D$ whole-array passes, so the layer is done through a network whose rank saving makes the cost per volume a power of $d$ below 1.',
    'explicit', bf,
    mot_quote='factors would require $D$ whole-array passes.',
    page='simultaneous-butterfly-layer', frm=['fixed-point-disk', 'two-point-kernel', 'polynomial-ring', 'rank-saving', 'complex-numbers'],
    adds=[('D', 'selected chunk count', 'The number of address chunks whose same bit position is butterflied at once, at most d.', 'count'),
          (r"\lambda\prime", 'layer exponent', 'The fixed exponent below 1 in the layer cost O(V d^lambda-prime).', 'direct')],
    salient=r'The cost per volume grows only like $d^{\lambda\prime}$ with $\lambda\prime<1$, while $D$ separate passes would cost a factor $d$.')

# ---------------- Section 6 ----------------
syn = show('S1.1.1.3',
    r'Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with $\omega_t=y^{2r/t}$, the normalized transforms $F_t^\mp$ satisfy $F_t^+F_t^-=t^{-1}I$ and are computed by $\log_2 t$ levels of butterflies and signed shifts, so twiddle multiplications are exact.',
    'Take powers of the ring variable as roots of unity, check character cancellation directly, and run the decimation-in-frequency recursion with butterflies and monomial multiplications',
    'Multiplying by a power of $y$ only permutes and negates coefficients, so with such roots of unity the twiddle factors cost nothing and only the butterflies need arithmetic.',
    'explicit',
    [inf('S1.1.1.3.1', r'Because $\mathcal R_r$ has zero divisors, $\sum_{k}\omega_t^{jk}$ is shown directly to be $t$ if $t\mid j$ and $0$ otherwise, so $F_t^+F_t^-=t^{-1}I$.',
         'The ring has zero divisors, so we verify character cancellation',
         salient='The character sums vanish although the ring has zero divisors: shifting k by t/2^(v+1) multiplies the sum by -1.'),
     inf('S1.1.1.3.2', r'The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$ and a twiddle $\omega_t^{-k}$ to one output, and recurses on both halves.',
         'decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for')],
    mot_quote='where the required roots of unity act by exact signed permutations',
    page='synthetic-transform', frm=['polynomial-ring', 'fft-butterfly', 'multidimensional-transform', 'dft', 'roots-of-unity'],
    adds=[('t', 'transform length', 'The power-of-two length of one transform axis.', 'count'),
          (r'\omega_t', 'synthetic root', 'The power y^(2r/t) of the ring variable that plays the role of a primitive t-th root of unity.', 'direct')])

stored = inf('S1.1.1.4', r'The forward transform writes frequency $j$ into slot $\operatorname{rev}(j)$ and the opposite transform consumes exactly that bit-reversed order, so no reordering sort is needed between them.',
    'After all $a$ rounds, the named slots from high to low therefore', page='stored-frequency-order', frm=['synthetic-transform'],
    salient='The bit-reversed order that the forward recursion produces for free is exactly the order the opposite recursion needs, so nothing is sorted.')

tl = [
 butter,
]
layout_children = [
 addrint, butter, syn, stored,
 inf('S1.1.1.5', r'On several axes a round applies one butterfly on each axis, followed by one recordwise monomial multiplication, so each round is a parallel butterfly layer.',
     'Consequently the individual axis steps may be grouped as a parallel'),
 inf('S1.1.1.6', r'A positional layout permutation $L$ puts the selected bits of all axes at a common offset in consecutive $K$-bit chunks while each polynomial keeps its contiguous coefficient suffix.',
     'The procedure constructs an explicit positional'),
 inf('S1.1.1.7', r'Moving the at most $d(b+1)=O(dK)$ listed bit slots into a prefix costs $O(TpdK)$.',
     'listed slots, so the moves cost $O(TpdK)$.'),
 inf('S1.1.1.8', r'The $O(p/K)$ exchanges of width-$K$ chunks needed to reach the layout cost $O(Tp\cdot pK^{\tau-1})$ in total.',
     'exchanges of width-$K$ address chunks, even when the chunks are'),
]
tlayout = show('S1.1.1',
    r'A forward synthetic transform of $M$ polynomial records, with error below $\sqrt2\,\ell 2^{-p}$, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}])$ and leaves its output in a retained layout order that the opposite transform consumes.',
    'Use address interchanges to put the selected bits of all axes at a common offset in consecutive $K$-bit chunks so that each of the $\\ell$ rounds is one simultaneous butterfly layer, and add the movement, exchange and layer costs'.replace('$\\ell$', r'$\ell$'),
    'The layer procedure only applies to the same bit position in equal-width chunks, so the bits that each round needs must first be moved there by the fast chunk exchanges.',
    'explicit', layout_children,
    mot_quote='we must place the selected bits of the participating axes at a common',
    page='transform-layout', frm=['polynomial-ring', 'multidimensional-transform', 'fixed-point-disk', 'sorting-and-permutation-of-arrays'],
    adds=[('K', 'chunk length', 'The number of address bits in each chunk, K = floor(d^c).', 'count'),
          (r'\ell', 'log record length', 'The base-2 logarithm of the record length r, which is also the number of rounds of one transform.', 'count')])

spack = inf('S1.1.2', r'Two disk-grid polynomials of the ring can be multiplied exactly, by signed Kronecker packing at $B_0=2^{4p}$ and four integer products of the established multiplier, in $O(rp\log(rp))$ time, returning $Q_p(fg/r)$.',
    'Let $r=2^\\ell<2^p$ with integers $\\ell\\geq1$ and $p\\geq2$, and fix $C_w>1$.', page='signed-packing',
    frm=['nlogn-multiplier', 'polynomial-ring', 'binary-arithmetic'])
ringconv = show('S1.1',
    r'The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}+\log(rp)])$ time.',
    'Take two forward synthetic transforms, multiply pointwise in the retained order using signed packing, apply the opposite transform to that same order, and rescale by $M$'.replace('$M$', '$M$'),
    'The pointwise product commutes with the common record permutation, so the retained order can be passed from the forward transforms through the product to the opposite transform with no reordering.',
    'explicit',
    [tlayout,
     inf('S1.1.2a', r'Pointwise multiplication commutes with the common record permutation $LB$, so the forward outputs can be multiplied in their retained order.',
         'Pointwise multiplication commutes with applying the same record'),
     spack,
     inf('S1.1.3', r'The three transforms, the $T/r$ pointwise products and the exact scaling by $M=T/r$ give $(f*g)/T$ with the stated error and cost, and the output is a disk array when the error margin permits.',
         'Perform both forward transforms and retain their common $LB$ order.')],
    mot_quote='forward outputs in their retained order and pass that order directly',
    page='ring-convolution', frm=['convolution', 'fixed-point-disk', 'polynomial-ring'],
    adds=[('M', 'record count', 'The number T/r of polynomial records, equal to the product of the lengths of the first d-1 axes.', 'count')])

# ---------------- Section 8 ----------------
retained = show('S1.2',
    r'The source transform $RF_{\boldsymbol s}$ on pairwise coprime axis lengths $s_i$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ on power-of-two lengths $t_i$ with both permutations $R,Q$ left inside the formula, the middle transform $QF_{\boldsymbol t}$ is a chirp convolution, and $R$ cancels in a convolution.',
    'Apply Gaussian resampling on each axis line by line, keep both coordinate permutations in the formula instead of executing them as sorts, compute the middle transform by the chirp identity, and cancel the source permutation across the transforms',
    'Gaussian resampling normally needs two sorts per coordinate, which would cost a full pass per axis; leaving the permutations inside the formula avoids the sorts altogether.',
    'explicit',
    [inf('S1.2.1', r'There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$.',
         'There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and', page='gaussian-resampling',
         frm=['dft', 'multidimensional-transform', 'complex-numbers']),
     inf('S1.2.2', r'Tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, applied line by line in the padded box at cost $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tp\,d^2(1+\ell^\tau))$ for exposing the lines.',
         'Suppose every pair $(s_i,t_i)$, $1\\leq i\\leq d$, satisfies'),
     inf('S1.2.3', r'For even $t_i$, the chirp array $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ gives $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$, a cyclic convolution between two pointwise phase products.',
         'assume every $t_i$ is even. For $\\boldsymbol j\\in\\mathbb Z^d$, define', page='chirp-identity',
         frm=['dft', 'convolution', 'multidimensional-transform']),
     inf('S1.2.4', r'Because each $t_i$ is a unit modulo $s_i$ the source permutation satisfies $RF^+_{\boldsymbol s}R=F^+_{\boldsymbol s}$, so $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.',
         'For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.',
         salient='The source permutation $R$ is never executed: it cancels between the two forward transforms and the opposite one.')],
    mot_quote='coordinate. We retain both permutations in the transform formula and',
    page='retained-permutations', frm=['dft', 'multidimensional-transform', 'convolution'],
    adds=[(r'\gamma', 'scale exponent', 'The exponent 2 d alpha^2 of the power of two by which the resampled transform is rescaled.', 'direct')],
    salient='The permutation of the source axes cancels across the forward transforms, the pointwise product and the opposite transform.')

# ---------------- Section 9 ----------------
param = show('S1.3',
    r'All sizes are tied to $b=\lceil\log_2 n\rceil$: $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a padded size $T$ in $[4n/b,8n/b)$ and $r=2^{\lceil\log_2 T/d\rceil}$, so that $Tp=\Theta(n)$ and $r$ exceeds every fixed power of $p$.',
    'Fix the rational exponents, then derive every size from b and verify the comparison constants that the layer and transform interfaces need',
    'The interfaces proved earlier hold only inside bands of $d$ and $r$ relative to $p$, so one choice of sizes must put every pair $(d,r)$ inside them for all input lengths at once.',
    'reconstructed',
    [inf('S1.3.1', r'The exponents are fixed rationals, for example $\tau=1-2^{-50}$, $\lambda\prime=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$, which satisfy every layer condition with room to spare.',
         'Take the following fixed rational numbers:'),
     inf('S1.3.2', r'Put $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$, with $T$ and $r$ derived, so $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$ and $r=2^{\Theta(p^{1-\epsilon})}$.',
         'b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,'),
     inf('S1.3.3', r'The band constants can be fixed for every input length at once, giving $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac{p}{12d}\le\ell\le\frac{p}{3d}$.',
         'Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\\ell=1$')],
    page='parameter-regime', frm=['logarithms-floors-and-ceilings', 'fixed-point-disk', 'multidimensional-transform'])

primes = show('S1.4',
    r'Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ and $\eta=1/(4d)$ are found deterministically, so $S=\prod_i s_i$ lies in $(T/2,T)$ and each ratio $t_i/s_i$ leaves enough separation for Gaussian resampling.',
    'Show by a prime-counting bound that each interval contains enough primes, choose them, bound their product, check the resampling hypotheses, and find them by trial division',
    'The primes must be close to the powers of two so that their product fills a fixed fraction of the padded box, yet far enough below them that resampling is possible.',
    'explicit',
    [inf('S1.4.1', r'Each of the intervals $(1-2\eta)x<q\le(1-\eta)x$, for $x=r/2$ and $x=r$, contains more than $d$ primes, so distinct odd primes $s_i$ can be chosen.',
         'We may therefore choose distinct odd primes satisfying'),
     inf('S1.4.2', r'Multiplying the lower bounds gives $S/T>(1-1/(2d))^d>1/2$, hence $T/2<S<T$.',
         'Together with $s_i<t_i$, this gives $T/2<S<T$.'),
     inf('S1.4.3', r'With $\alpha=\lceil(12d^2b)^{1/4}\rceil$ every hypothesis of the one-dimensional resampling lemma holds, since $\alpha^4\theta_i>p$.',
         'Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for'),
     inf('S1.4.4', r'Scanning the two intervals and testing candidates by trial division finds the primes in time $n^{o(1)}=o(n)$.',
         'The machine finds these primes by scanning the two intervals')],
    mot_quote='The distinct prime lengths $s_i$ must be close to the powers of two',
    page='prime-lengths', frm=['primes-and-trial-division', 'gaussian-resampling', 'parameter-regime'],
    adds=[(r'\eta', 'prime gap fraction', 'The relative gap 1/(4d) that separates the prime lengths s_i from the powers of two t_i.', 'direct')])

radix = inf('S1.5', r'Writing each integer as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits turns the product into a convolution of digit lists; since the degree is below $S$, convolution modulo $x^S-1$ has no wraparound and each coefficient is below $2^{3b}$.',
    'Write the two inputs as polynomials in $2^b$, each with', page='radix-digit-reduction', frm=['convolution', 'binary-arithmetic'])

crt = show('S1.6',
    r'A ring isomorphism sends the length-$S$ cyclic convolution to a cyclic convolution on the pairwise coprime axes $s_i$, and on tape it is a sequence of triangular controlled shifts costing $O(Tp\,d^2(1+\ell^\tau))$.',
    'Use the Chinese remainder map x to the product of x_i^(mu_i), whose coordinates are triangular in the mixed-radix digits, and implement each triangular update as a controlled cyclic shift',
    'The coordinates of the map depend only on lower-index digits, so with the axes reordered each coordinate is a shift controlled by fields that precede it, which is the linear-time case of controlled shifts.',
    'explicit',
    [inf('S1.6.1', r'The assignment $x\mapsto\prod_i x_i^{\mu_i}$, with $\mu_i=P_i^{-1}\bmod s_i$, is an isomorphism that preserves cyclic convolution.',
         '$\\Phi$ is an isomorphism and preserves cyclic convolution.'),
     inf('S1.6.2', r'In mixed-radix digits $a_j$ the coordinate on axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j \pmod{s_i}$, which depends only on lower digits.',
         'Indeed terms with $j>i$ are divisible by $s_i$, and $\\mu_iP_i=1$ modulo'),
     inf('S1.6.3', r'Each triangular update is a prefix-controlled cyclic shift of the valid target interval, so padding stays zero and the map and its inverse cost $O(Tp\,d^2(1+\ell^\tau))$ with the axis reordering.',
         'Each triangular update is a prefix-controlled cyclic shift.')],
    mot_quote='sequence of controlled cyclic shifts.',
    page='crt-prime-axes', frm=['controlled-shifts', 'modular-arithmetic', 'multidimensional-transform', 'radix-digit-reduction'])

twist = show('S1.7',
    r'Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ turns convolution modulo $x^r-1$ into convolution modulo $y^r+1$ on the last axis, so the complex cyclic convolution is the synthetic one conjugated by phase twists at cost $O(Tp^{1+\delta})$.',
    'Define the twist as the diagonal ring isomorphism x_d to zeta y, check that the negacyclic wrap exactly compensates the twist, and compute the twists with grid phases',
    'The synthetic transforms need the last axis to be negacyclic, while the convolution to be computed is cyclic, so a diagonal phase change that converts one wrap into the other is needed.',
    'explicit',
    [inf('S1.7.1', r'The map $x_d\mapsto\zeta y$ is well defined because $(\zeta y)^r=(-1)(-1)=1$, and it is an isomorphism that multiplies coefficient $k$ by $\zeta^k$.',
         'is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.'),
     inf('S1.7.2', r'If $k+l=j+hr$ then a product term acquires $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.',
         'For an explicit check on the wrap, write $k+l=j+hr$, where'),
     inf('S1.7.3', r'The computed complex convolution twists both operands, applies the ring convolution and untwists, with every phase product rounded by $Q_p$.',
         'with the twist arrays repeated on every last-coordinate line:')],
    mot_quote='The power-of-two complex convolution used in the chirp identity is',
    page='coefficient-twist', frm=['polynomial-ring', 'convolution', 'roots-of-unity'],
    adds=[(r'\zeta', 'twist root', 'The complex number e^(pi i / r), a primitive 2r-th root of unity.', 'direct')])

chirpproc = inf('S1.8', r'The middle factor $QF_{\boldsymbol t}$ is computed by multiplying by the conjugate chirp, taking the complex convolution with the chirp, and multiplying by the conjugate chirp again, at cost $O(Tdp^{1+\delta})$ for the chirps.',
    'We next use the complex convolution to evaluate the middle factor')
srcproc = inf('S1.9', r'The source transform expands each axis by $\mathcal A$, applies the chirp transform, compresses by $\mathcal B_0$ and scales by $2^\gamma$, exactly realizing $RF_{\boldsymbol s}$; the opposite-sign transform is obtained by conjugation.',
    'For a source disk-grid tensor of norm at most $.5$, write')
algo = inf('S1.10', r'The algorithm reads radix-$2^b$ digits, places them by $\Phi$, transforms both operands, multiplies pointwise, applies the opposite transform, scales, rounds and propagates carries to give the $2n$-bit product.',
    'With these streams prepared, perform the following operations.')
snorm = inf('S1.11', r'The two scalings by $S$ undo different normalizations: after the three transforms the exact result is $(u*v)/S^2$, and the scalings by $S$ and $2^{2b+4}$ restore the integer coefficient convolution.',
    'The two occurrences of $S$ in this algorithm undo different')

prec = show('S1.12',
    r'Every call returns disk-grid values with the stated error and norm margins, the final coefficient error is below $1/2$, so rounding gives the exact integer coefficients and carries give the product.',
    'Track the norm and the error through each stage using that every transform is a contraction and every pointwise product is bilinear, undo the known scales, and round',
    'Contractions do not enlarge errors, so the total error is a sum of per-stage truncation errors, which a large enough precision $p$ drives below one half.',
    'recoverable',
    [inf('S1.12.1', r'If one operand has norm at most $.7$, the normalized ring convolution stays within norm $.7$, so computed outputs remain in the disk and every call is defined.',
         'If one operand has norm at most $.7$, bilinear contraction gives'),
     inf('S1.12.2', r'The final absolute error of the recovered integer coefficients is below $448b\,2^{-3b/4}<1/2$.',
         'Since $S\\le T<2^b$ and $L<b$ eventually, the final absolute error is less than',
         salient='The scales $2^{2b+4}S$ are absorbed because the error budget $2^{-6b}$ from $p=6b$ leaves exponentially small slack.'),
     inf('S1.12.3', r'The carries satisfy $0\le k_j<Q_0^2$, and the recurrence for $d_j$ and $k_{j+1}$ gives the first $j$ radix digits of the product exactly, hence exactly $2n$ output bits.',
         'To propagate carries, let $Q_0=2^b$.')],
    page='precision-recovery', frm=['fixed-point-disk', 'vector-norms-and-the-triangle-inequality', 'rounding-rational-numbers-and-fixed-point-numbers'])

mult = show('S1',
    r'The algorithm, with digits placed on prime axes by the Chinese-remainder map, transformed by Gaussian resampling, chirp convolution and polynomial-ring convolution, multiplied pointwise, transformed back, rescaled, rounded and carry-propagated, outputs the exact $2n$-bit product.',
    'Reduce the product to a cyclic convolution of digit lists and evaluate it with Fourier transforms, building from the fastest inner primitive (convolution over a polynomial ring) outward through the resampling, prime-axis and twist reductions, then bound the error so that rounding is exact',
    'Splitting into digits turns multiplication into convolution, and convolutions are cheap through transforms, but each transform has the wrong shape for the one below, so each reduction is added around the innermost primitive.',
    'recoverable',
    [ringconv, retained, param, primes, radix, crt, twist, chirpproc, srcproc, algo, snorm, prec],
    page='multiplication-algorithm', frm=['convolution', 'dft', 'binary-arithmetic'],
    adds=[('b', 'digit width', 'The number of bits in one radix digit, b = ceil(log2 n).', 'count'),
          ('p', 'precision', 'The number of fractional bits of the disk-grid values, p = 6b.', 'count'),
          ('d', 'axis count', 'The number of transform axes, d = floor(b^epsilon).', 'count'),
          ('T', 'padded size', 'The number of entries of the padded power-of-two box, about n/b.', 'count'),
          ('r', 'record length', 'The number of complex coefficients of one polynomial record, a power of two.', 'count'),
          ('S', 'prime product', 'The product of the prime source lengths s_i, lying between T/2 and T.', 'direct'),
          ('s_i', 'source length', 'The pairwise coprime odd prime length of the source axis i.', 'direct'),
          ('t_i', 'padded length', 'The power-of-two length of axis i of the padded box, equal to r/2 or r.', 'direct')])

timeb = show('S2',
    r'Dividing the costs of all stages by $Tp$, the seven dominant normalized terms have exponents of $p$ at most $1-2\kappa$, which gives $O(n(\log n)^{1-\kappa})$.',
    'Tabulate each stage cost divided by the volume, take the exponent of p for each of the seven dominant rows, compare with 1 minus 2 kappa, and absorb setup costs',
    'Each stage has already been bounded in terms of the same volume, so dividing by it exposes the exponent of $p$ per stage and the largest decides the total.',
    'recoverable',
    [inf('S2.1', r'The cost table normalized by $V=Tp$ lists seven dominant terms whose margins below one are $g_1,\dots,g_7$.',
         'The seven dominant powers in Table~\\ref{tab:costs} have the following'),
     inf('S2.2', r'Direct substitution gives margins $g_2=2^{-181}$ as the smallest, so $\min_i g_i=2^{-181}=2\kappa$.',
         'Thus $\\min_i g_i=2^{-181}=2\\kappa$.',
         salient=r'The smallest margin is exactly $2\kappa$ with $\kappa=2^{-182}$, and comes from the chunk exchanges of the layout.'),
     inf('S2.3', r'Per-node setup, exceptional streams and tape management cost $o(V)$ in total because $r$ exceeds every fixed power of $p$.',
         r'\paragraph{Setup and exceptional streams across all calls.}'),
     inf('S2.4', r'Each of the seven powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$, so the bound is $O(n(\log n)^{1-\kappa})$ for large $n$, and schoolbook multiplication handles small $n$.',
         'Each of the seven displayed powers is at most $1-2\\kappa$ by')],
    page='time-bound', frm=['logarithms-floors-and-ceilings', 'worst-case-time-analysis-of-deterministic-algorithms'])

root = show('S0',
    r'One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.',
    'Give the multiplication algorithm and show its output is exact, then total its cost stage by stage',
    'Plain transforms already cost $\\Theta(n\\log n)$ because each of $\\Theta(\\log n)$ levels scans $\\Theta(n)$ bits, so the proof needs components that save on both movement and arithmetic, and the exactness and the cost are best argued separately.'.replace('\\\\','\\'),
    'explicit',
    [mult, timeb],
    mot_quote='We therefore need savings in both movement and arithmetic.',
    page='main-theorem', frm=['nlogn-conjecture', 'fixed-tape-model', 'big-o', 'worst-case-time-analysis-of-deterministic-algorithms'],
    adds=[('V', 'stored volume', 'The number of stored data bits in the array being processed.', 'count')],
    salient=r'The saving exponent $\kappa=2^{-182}$ is astronomically small yet positive, so the gain is a genuine power of the logarithm.')

ans = dict(root=root)
json.dump(ans, open('/home/user/openai-nlogn-wiki/runs/G5/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)

# ------------- checks -------------
norm = lambda s: re.sub(r'\s+', ' ', s)
problems = []
infers = []
def walk(n, path=()):
    if n['intention'] == 'infer':
        infers.append(n)
    for c in n.get('children', []):
        walk(c)
walk(root)
last = -1
for n in infers:
    q = n['quote']['quote']
    cnt = src.count(q)
    if cnt != 1:
        problems.append(('count', n['id'], cnt, q))
        continue
    if '\n' in q: problems.append(('newline', n['id']))
    pos = src.index(q)
    n['_pos'] = pos
    if n.get('deferred'):
        continue
    if pos <= last:
        problems.append(('order', n['id'], pos, last, q))
    last = pos
# motivations
def walk2(n):
    if n['intention']=='show':
        m = n['motivation']
        if m.get('quote'):
            q = m['quote']['quote']
            if src.count(q) < 1: problems.append(('mot', n['id'], q))
        for c in n['children']: walk2(c)
walk2(root)
ids = []
def walk3(n):
    ids.append(n['id'])
    for c in n.get('children', []): walk3(c)
walk3(root)
dup = {i for i in ids if ids.count(i) > 1}
if dup: problems.append(('dup ids', dup))
print('infers', len(infers), 'problems', len(problems))
for p in problems: print(p)
