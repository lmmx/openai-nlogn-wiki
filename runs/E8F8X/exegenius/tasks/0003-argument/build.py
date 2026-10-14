import json, re, sys

ROOTDIR = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F8X'
SRC = open(ROOTDIR + '/sources/paper.tex').read()
cursor = 0
LOG = []


def pat(phrase):
    phrase = phrase.replace('@AP@', "'").replace("\\'", "'")
    toks = phrase.split()
    return r'\s+'.join(re.escape(t) for t in toks)


def Q(start, end=None, defer=False):
    global cursor
    pos = 0 if defer else cursor
    m = re.compile(pat(start)).search(SRC, pos)
    if not m:
        raise Exception('start not found after cursor: %r (cursor line %d)' % (start, SRC.count('\n', 0, cursor) + 1))
    i, j = m.start(), m.end()
    if end is not None:
        m2 = re.compile(pat(end)).search(SRC, j)
        if not m2:
            raise Exception('end not found: %r after %r' % (end, start))
        j = m2.end()
    if not defer:
        cursor = j
    LOG.append((SRC.count('\n', 0, i) + 1, SRC.count('\n', 0, j) + 1, defer, SRC[i:j][:50].replace('\n', ' ')))
    return {'source': 'paper', 'quote': SRC[i:j]}


def QM(start, end=None):
    m = re.compile(pat(start)).search(SRC, 0)
    if not m:
        raise Exception('motivation start not found: %r' % start)
    i, j = m.start(), m.end()
    if end is not None:
        m2 = re.compile(pat(end)).search(SRC, j)
        if not m2:
            raise Exception('motivation end not found: %r' % end)
        j = m2.end()
    return {'source': 'paper', 'quote': SRC[i:j]}


def mot(text, kind, start=None, end=None):
    d = {'text': text, 'source': kind}
    if kind == 'explicit':
        d['quote'] = QM(start, end)
    return d


def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    d = {'id': id, 'intention': 'show', 'claim': claim, 'method': method, 'motivation': motivation,
         'children': children, 'from': frm or []}
    if page:
        d['page'] = page
    if salient:
        d['salient'] = salient
    if adds:
        d['adds'] = adds
    return d


ERRS = []


def infer(id, claim, start, end=None, frm=None, deferred=False, salient=None, page=None):
    try:
        qq = Q(start, end, deferred)
    except Exception as ex:
        ERRS.append((id, str(ex)))
        qq = {'source': 'paper', 'quote': 'MISSING'}
    d = {'id': id, 'intention': 'infer', 'claim': claim, 'quote': qq, 'from': frm or []}
    if deferred:
        d['deferred'] = True
    if salient:
        d['salient'] = salient
    if page:
        d['page'] = page
    return d


def B(symbol, name, meaning, relation='direct'):
    return {'symbol': symbol, 'name': name, 'meaning': meaning, 'relation': relation}


# concept ids
BO = 'big-o-notation'; POLY = 'polynomials'; CX = 'complex-numbers'; TM = 'multitape-turing-machine'
BIN = 'binary-numerals-and-bit-strings'; RADIX = 'positional-notation-in-any-radix'
DIV = 'integer-division-with-remainder-floor-and-ceiling'; MOD = 'modular-arithmetic'
XOR = 'arithmetic-modulo-2-and-xor'; PRIME = 'primes-coprimality-and-gcd'
ROOTS = 'roots-of-unity-and-euler-s-formula'; EXP = 'exponential-logarithm-and-gaussian-function'
ASYM = 'asymptotic-notation-beyond-big-o'; GEO = 'geometric-series-and-sums'
DC = 'divide-and-conquer-and-recurrences'; SCHOOL = 'schoolbook-and-karatsuba-multiplication'
SORT = 'sorting-and-its-cost'; PERM = 'permutations-and-bijections'; SETS = 'sets-subsets-and-cartesian-products'
ARR = 'multidimensional-arrays-and-row-major-order'; MAT = 'matrices-vectors-and-linear-maps'
TRI = 'triangular-and-permutation-matrices'; DOT = 'dot-product-inner-product-and-orthogonality'
DYAD = 'dyadic-rationals-and-fixed-width-numerators'; TRANSP = 'matrix-transposition'
NORM = 'triangle-inequality-and-norms'; INDUCT = 'mathematical-induction-and-proof-by-contradiction'
CYC = 'cyclic-shifts-and-rotations-of-lists'; SUB = 'subroutines-and-composition-of-algorithms'
# pages
P_BARRIER = 'n-log-n-barrier'; P_CONV = 'convolution'; P_NEG = 'negacyclic-ring'; P_TWIST = 'coefficient-twist'
P_PACK = 'signed-packing'; P_ADDR = 'tape-address-model'; P_CSHIFT = 'controlled-cyclic-shift'
P_EXCH = 'scratch-restoring-exchange'; P_FRAME = 'array-frames'; P_RANK = 'rank-and-orthogonal-subspaces'
P_LABEL = 'subset-intersection-labels'; P_SHEAR = 'address-shear-factorization'
P_SAVE = 'rank-saving-recurrence'; P_PWI = 'power-width-interchange'; P_CHUNK = 'address-chunk-interchange'
P_CRT = 'crt-axis-map'; P_PACKED = 'packed-selected-bit-addition'; P_FIXED = 'fixed-point-complex-arithmetic'
P_PHASE = 'phase-frame-network'; P_DFT = 'discrete-fourier-transform'; P_FFT = 'fft-butterflies'
P_SYN = 'synthetic-polynomial-transform'; P_LAYER = 'simultaneous-butterfly-layer'; P_BLU = 'bluestein-chirp'
P_FREQ = 'stored-frequency-order'; P_LAYOUT = 'transform-tape-layout'; P_CONTR = 'contraction-error-propagation'
P_GAUSS = 'gaussian-resampling'; P_PERMC = 'permutation-cancellation'; P_NRC = 'normalized-ring-convolution'
P_PARAM = 'parameter-regime'; P_RADIX = 'radix-digit-reduction'; P_TENS = 'tensor-source-transform'
P_PREC = 'precision-exact-recovery'; P_ALG = 'multiplication-algorithm'; P_COST = 'cost-accounting'
P_MAIN = 'main-theorem'

# ---------------------------------------------------------------------------------------------
# S1: the barrier
# ---------------------------------------------------------------------------------------------
S1 = show(
    'S1',
    r'Multiplication costs $O(n\log n\log\log n)$ by Sch\"onhage--Strassen and $O(n\log n)$ by Harvey--van der Hoeven, and a transform with $\Theta(\log n)$ levels that scans $\Theta(n)$ bits per level costs $\Theta(n\log n)$, so beating $n\log n$ needs savings in data movement and in arithmetic.',
    'Recall the known upper bounds and the conjecture, then identify the scan-per-level cost of a transform as what must be reduced.',
    mot('The conjectured optimum and the best known bound coincide at $n\\log n$, and the transform structure used here has exactly that scanning cost, so any power saving has to attack the per-level scan; this is the framing the later pages rely on.', 'recoverable'),
    [
        infer('S1.1', r'Sch\"onhage and Strassen multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine in 1971 and proposed $n\log n$ as the optimal order of growth.',
              r'Sch\"onhage and Strassen proved in 1971', 'optimal order of growth', frm=[TM, BO, SCHOOL]),
        infer('S1.2', r'Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound, which this paper uses only as a subroutine on short inputs.',
              r'Harvey and van der Hoeven reached the unconditional', r'bound~\cite{HarveyHoeven2021}.', frm=[BO]),
        infer('S1.3', r'In the polynomial-ring transform representation, scanning $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so the address rearrangements and the butterfly arithmetic must both be sped up.',
              r'Scanning an array of $\Theta(n)$ stored bits at each of', r'already costs $\Theta(n\log n)$.', frm=[BO, ASYM]),
    ],
    page=P_BARRIER, frm=[BO, ASYM, SCHOOL, TM],
)

# ---------------------------------------------------------------------------------------------
# S2: the key step: rank saving
# ---------------------------------------------------------------------------------------------
S2_0 = infer(
    'S2.0',
    r'A recursive call at parameter $mf$ uses $s$ calls at parameter $f$, each on a stream of volume $V/W$, so dividing cost by volume multiplies the recursive contribution by $s/W<m$ when the parameter is multiplied by $m$; this strict inequality is the source of the power saving.',
    r'A recursive call at parameter $mf$ therefore uses', r'is the source of the power saving.',
    frm=[DC, GEO], salient=r'The factor by which the normalized cost grows when the parameter is multiplied by $m$ is $s/W$, strictly smaller than $m$, so the saving is a genuine power of the parameter rather than a constant factor.')

S2_1 = show(
    'S2.1',
    r'An array indexed by $[a_1]\times\cdots\times[a_t]$ is stored in lexicographic order with implicit addresses, its logical volume $V$ counts the data bits, and fixed digit permutations, digit moves, splits on a digit and cyclic row splits into $W$ streams of volume $V/W$ each cost $O(V)$ on a fixed number of tapes.',
    'State the storage convention, then realize each elementary operation by splitting into streams according to the specified digit values, scanning aligned streams, and merging.',
    mot('A split on a digit gives streams with the same remaining address set in the same order, so one aligned scan applies any pointwise change; this is what keeps every elementary operation linear in the volume.', 'recoverable'),
    [
        infer('S2.1.1', r'An array is stored in lexicographic order with the first coordinate most significant, and an address is implicit in an entry position.',
              r'An array with address set $[a_1]\times\cdots\times[a_t]$ is stored in', r'first coordinate most significant.', frm=[ARR, TM]),
        infer('S2.1.2', r'The logical volume $V$ is the number of stored data bits; work tapes and duplicate streams are charged in time but do not increase $V$ in recurrences.',
              r'The \emph{logical volume} $V$ is the number of stored data bits.', r'in recurrences.', frm=[BO]),
        infer('S2.1.3', r'For a fixed radix $q$, permuting two digit values, moving a digit, splitting on a digit with a pointwise map, and cyclic row splits each take $O(V)$ steps on a fixed number of one-dimensional tapes.',
              r'Fix a radix $q\ge2$. Each of the following operations on an array of', r'one-dimensional tapes:', frm=[RADIX, TM]),
        infer('S2.1.4', r'Writing the row number as $r=Wg+w$ and sending the whole row to stream $w$ splits the rows cyclically into $W$ streams of equal shape, each of volume $V/W$ (when $W$ divides the row count).',
              r'For the fourth, write $r=Wg+w$', r'each has volume $V/W$.', frm=[DIV, ARR],
              salient=r'The row split costs only $O(V)$ yet divides the volume of each stream by exactly $W$, which is what later makes the recursive calls cheap.'),
    ],
    page=P_ADDR, frm=[TM, ARR, RADIX, BO, SUB],
)

S2_2 = show(
    'S2.2',
    r'Adding to a target field $y\in[Q]$, $Q=q^b$, an offset computed from earlier control fields modulo $Q$ costs $O(V)$ when the offset is prepared in $b^{O(1)}$ time, by splitting each fiber at $Q-a$ and merging the two pieces in the opposite order.',
    'Realize the cyclic shift as a split into two consecutive ranges followed by a merge in reversed order, and absorb the offset computation into the size of the fiber.',
    mot('Because the target field follows its controls, one pass per fiber can compute the offset once and rotate the fiber; the polynomial-in-$b$ offset work is dominated by the $q^b$ blocks of the fiber.', 'recoverable'),
    [
        infer('S2.2.1', r'An update $y\mapsto y+a(\text{controls})\pmod Q$ of a target field following its controls costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time.',
              r'Suppose a target field $y\in[Q]$ follows its control fields', r'fixed number of control values.', frm=[MOD, CYC]),
        infer('S2.2.2', r'Splitting the $Q$ blocks of each fiber at $Q-a$ and merging the second piece before the first realizes the rotation by $a$.',
              r'For an offset $a\in[Q]$, split these blocks at $Q-a$.', r'of the new target coordinate.', frm=[CYC]),
        infer('S2.2.3', r'The offset work $b^C$ is $O(q^b)=O(Q)$ for each fixed $C$, so it is absorbed by the $QB\ge Q$ bits of the fiber.',
              r'b^C=O(q^b)=O(Q)', r'fiber.', frm=[BO, ASYM]),
    ],
    page=P_CSHIFT, frm=[MOD, CYC, BO, P_ADDR],
)

S2_3 = show(
    'S2.3',
    r'A fixed linear network of copy, side-injection, gather and scatter gates swaps two banks of values, $(X_a,Y_a)\mapsto(-Y_a,X_a)$, in three stages while returning every scratch wire to its arbitrary initial value.',
    'Write each stage as eight gate rows that first subtract the effect of the old scratch values, then add the source into the target through the scratch wires, then restore the scratch; show the net map on the target is independent of the scratch values; compose three stages.',
    mot('The scratch roles will later hold arbitrary data of the array, so the network must cancel unknown initial values; subtracting and re-adding them around the computation does this.', 'recoverable'),
    [
        infer('S2.3.1', r'There are three stages, and at each stage $j$ the $v$ values of each bank varying in coordinate $j$ are processed by $v^2$ separate invocations, each with its own scratch wires, whose initial values may be arbitrary.',
              r'There are three stages. At stage $j$, fix the other two coordinates and', r'separate invocations at each stage.', frm=[SETS]),
        infer('S2.3.2', r'In the bit construction scalars lie in $\mathbb F_2$ and gates copy, side-inject, gather and scatter along triples with $|S\cap T|=1$; in the complex construction scalars lie in $\mathbb Z[i,1/2]$, neighbors have even intersection, and the side injection and scatter carry the coefficients $-(|S\cap T|-1)/2$ and $(\sum_{i\in S}C_i-C_\ast)/2$.',
              r'In the bit construction, scalars lie in $\mathbb F_2$, and', r'$(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$.', frm=[XOR, SETS, DYAD]),
        infer('S2.3.3', r'The first two rows of the eight-row schedule remove the effect of the old scratch values, the next four add the source values and their effect to the target, and the last two restore the scratch values.',
              r'Each update leaves its control wires unchanged.', r'the last two restore the scratch values.', frm=[XOR]),
        show('S2.3.4',
             r'For arbitrary initial scratch values a forward invocation changes $y_S$ to $y_S+x_S$ and leaves everything else unchanged.',
             'Compute the net target change of the eight rows as a sum of two linear maps applied to the source, and check its coefficients on each pair of triples.',
             mot('The scratch contributions cancel between rows, leaving a fixed matrix whose entries depend only on the intersection sizes of the triples.', 'recoverable'),
             [
                 infer('S2.3.4a', r'A forward invocation changes $y_S$ to $y_S+x_S$ for arbitrary initial auxiliary wires.',
                       r'For arbitrary initial values of its auxiliary wires, a forward', r'unchanged.', frm=[]),
                 infer('S2.3.4b', r'With initial side and central vectors $a,c$, the net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$, because rows 0-1 subtract $\mathcal Ja+\mathcal Rc$, rows 2-5 add $\mathcal J(a+\mathcal Vx)+\mathcal R(c+\mathcal Gx)$ and rows 6-7 restore $a,c$.',
                       r'If the initial side and central vectors are $a,c$, the first two rows', r'$a,c$.', frm=[MAT]),
                 infer('S2.3.4c', r'In the bit case the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$ and the side injection cancels exactly the intersection-one cases, while distinct triples of intersection zero or two already have coefficient zero and the self coefficient is one.',
                       r'In the bit case, the central coefficient from $x_T$ to $y_S$ is', r'the self coefficient is one.', frm=[XOR, SETS]),
                 infer('S2.3.4d', r'In the complex case the central coefficient is $(|S\cap T|-1)/2$; the side injection cancels it for distinct triples of intersection zero or two, intersection one contributes zero, and the self coefficient is one.',
                       r'In the complex case, the central coefficient is $(|S\cap T|-1)/2$.', r'the self coefficient is one.', frm=[SETS]),
             ]),
        infer('S2.3.5', r'Running the forward schedule from $X$ to $Y$ at stage 1, the inverse schedule from $Y$ to $X$ at stage 2 and the forward schedule again at stage 3 sends $(x,y)$ to $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$, restoring every auxiliary value.',
              r'The inverse schedule with logical source $Y$ and target $X$ effects', r'then $(-y,x)$.', frm=[]),
        infer('S2.3.6', r'The wire counts $W_{\rm b}$ and $W_{\rm c}$ of the bit and complex networks are fixed numbers independent of the input length.',
              r'All these numbers are fixed, independently of any eventual input length.', frm=[]),
    ],
    page=P_EXCH, frm=[XOR, SETS, MAT, DYAD],
)

S2_4 = show(
    'S2.4',
    r'If every scalar wire is replaced by an array stored as $D_vg$ for an invertible operator $D_v$ (a frame) and all incidences of a gate share one frame, then each pointwise linear gate commutes with its frame and the implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so only the endpoint frames matter.',
    'Maintain the invariant that the stored array equals the frame applied to the logical array, and check it at the sources, along each edge and across each pointwise linear gate.',
    mot('Once the scalar routing is fixed, the endpoint frames determine the array operator on each route, and the intermediate frames are free to be chosen so that every edge is cheap.', 'explicit',
        r'Once the scalar routing is fixed,', r'make each edge change inexpensive.'),
    [
        infer('S2.4.1', r'Every source, gate and sink $v$ gets an invertible operator $D_v$ on the array space; all incidences of one gate use the same $D_v$, and an edge from $u$ to $v$ applies $D_vD_u^{-1}$.',
              r'assign an invertible $R$-linear operator', r"$D_vD_u^{-1}$ to that wire's array.", frm=[MAT]),
        show('S2.4.2',
             r'The stored array at every vertex equals the frame applied to the logical array there.',
             'Induct along the network: the invariant holds at sources by definition, is preserved by each edge operator, and is preserved by gates by linearity.',
             mot('A gate combines wire values at fixed addresses while a frame mixes addresses, so linearity lets the common frame be pulled out.', 'recoverable'),
             [
                 infer('S2.4.2a', r'The logical interpretation of the supplied input is defined as $g=D_{\rm in}^{-1}f$, so the invariant holds at the sources by definition and needs no preprocessing.',
                       r'For a supplied physical input $f$, define its logical interpretation to be', r'It holds at the sources by definition.', frm=[MAT]),
                 infer('S2.4.2b', r'On an edge whose logical array is $\varphi$ the edge operator changes $D_u\varphi$ to $D_v\varphi$.',
                       r'On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$', r'to $D_v\varphi$.', frm=[]),
                 infer('S2.4.2c', r'At a gate with logical inputs $\varphi_j$, $R$-linearity gives $\sum_jc_jD_v\varphi_j=D_v\sum_jc_j\varphi_j$, so the common frame commutes with the pointwise gate and the invariant continues to the sinks.',
                       r'At a gate with logical input arrays $\varphi_j$,', r'the invariant continues to the sinks.', frm=[MAT]),
             ]),
        infer('S2.4.3', r'The implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$.',
              r'The implemented operator is therefore', r'D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}.', frm=[MAT]),
        infer('S2.4.4', r'For a signed role permutation sending input role $w$ to output role $\rho(w)$ with sign $\varepsilon_w$, the route applies $\varepsilon_wD_{{\rm sink}(\rho(w))}D_{{\rm source}(w)}^{-1}$ to its input array, for auxiliary roles as well.',
              r'In particular, if the scalar network is a signed role permutation that', r'enter this identity.', frm=[PERM, MAT],
              salient=r'The array operator on each route depends only on the frames at its two ends, so all the intermediate frames cancel.'),
    ],
    page=P_FRAME, frm=[MAT, PERM, P_EXCH, P_ADDR],
    adds=[B('D_v', 'frame', 'the invertible operator on the common array space attached to a source, gate or sink $v$, in which the array there is stored'),],
)

# ---- labels and bit rank budget
S2_5 = show(
    'S2.5',
    r'Attaching nested nondegenerate subspaces of $F^{\otimes3}$, built from indicator vectors of three-element subsets, to the gates and terminals makes the total edge rank satisfy $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$ for the bit network, with $L_{\rm b}/N=100/539<1/2$.',
    'Choose labels so that dimension never decreases except on one central edge per central wire, count signed and absolute dimension changes, and convert dimension changes to ranks, treating the $N$ negative source projections as the one exception.',
    mot('Each unit of rank on an edge costs one smaller call, so what matters is the total rank; keeping the dimension lost on decreasing edges small relative to $N$ makes this total smaller than $Wm$.', 'explicit',
        r'A label is a nondegenerate subspace of a fixed bilinear space.', r'edges small relative to $N$.'),
    [
        show('S2.5.1',
             r'Triple indicator vectors $t_T$ are nondegenerate, with $\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$ and $t_T\cdot t_T=1$ over $\mathbb F_2$, so neighboring triple lines are orthogonal.',
             'Pick a bilinear form on $\mathbb Q^h$ (and the dot product on $\mathbb F_2^h$) whose values on indicators are the intersection formulas of Alon and Frankl--Wilson.',
             mot('Neighboring triples (intersection one for the bit network, even intersection for the complex network) must be orthogonal so that nested labels exist on the side wires.', 'recoverable'),
             [
                 infer('S2.5.1a', r'On $F=\mathbb Q^h$ the form $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate.',
                       r'For the bit network, let $F=\mathbb Q^h$ with bilinear form', r'so it is nondegenerate.', frm=[MAT, DOT]),
                 infer('S2.5.1b', r'For a triple $T$ with indicator $t_T$, $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$.',
                       r'For a triple $T$ let $t_T$ be', r'\langle t_T,t_T\rangle=2.', frm=[SETS, DOT]),
                 infer('S2.5.1c', r'For the complex network take $F=\mathbb F_2^h$ with the ordinary dot product, where $t_T\cdot t_T=1$.',
                       r'For the complex network, take instead $F=\mathbb F_2^h$ with the', r'here $t_T\cdot t_T=1$.', frm=[XOR, DOT]),
                 infer('S2.5.1d', r'Every triple line is nondegenerate and neighboring triple lines are orthogonal in the label field of either construction.',
                       r'Thus every triple line is nondegenerate, and neighboring triple lines', r'either construction.', frm=[DOT]),
             ]),
        show('S2.5.2',
             r'The terminal labels give source dimensions summing to $N$ and sink dimensions summing to $Wm-N$, so signed dimension changes sum to $Wm-2N$ and absolute changes to $Wm-2N+2L$.',
             'Prescribe terminal labels $U_a$, $0$ and the full space on the data and scratch roles, and use that signed changes telescope at every gate.',
             mot('The gates contribute no net change, so only the terminals fix the signed total; absolute changes then differ from it by twice the dimension lost on decreasing edges.', 'recoverable'),
             [
                 infer('S2.5.2a', r'The label space is $\mathcal F=F^{\otimes3}$ of dimension $m$ with $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$ and $U_a=\langle u_a\rangle$.',
                       r'The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor', r'U_a=\langle u_a\rangle.', frm=[MAT, P_RANK]),
                 infer('S2.5.2b', r'The sources have total dimension $N$ and the sinks $Wm-N$, so signed dimension changes sum to $Wm-2N$ and absolute changes to $Wm-2N+2L$ when the decreasing edges lose $L$ in total, with $L<N/2$ to be obtained.',
                       r'Write $W$ for the wire count in the construction under consideration.', r'saving in both constructions.', frm=[]),
             ]),
        show('S2.5.3',
             r'The data wires pass through stage transitions that expose one tensor factor at a time, and the labels at consecutive stages fit together.',
             'Write the previous-factor space as $A=B\perp P$ and track the incoming and outgoing labels of $X$ and $Y$ wires through the table of transitions.',
             mot('Exposing one tensor factor per stage makes the outgoing labels of stage $j$ equal the incoming labels of stage $j+1$, so no extra cost arises between stages.', 'recoverable'),
             [
                 infer('S2.5.3a', r'At stage $j$ put $A=F^{\otimes(j-1)}$, $P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$, $B=P^\perp$ and $Q=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$, so $A=B\perp P$.',
                       r'At stage $j$, fix an invocation. Put', r'$A=B\mathbin{\perp}P$.', frm=[P_RANK]),
                 infer('S2.5.3b', r'The outgoing labels of stage $j$ are exactly the incoming labels of stage $j+1$, with $A\'=A\otimes F$, $P\'=P\otimes\langle t\rangle$ and $B\'=(P\')^\perp_{A\'}$.',
                       r'These transitions expose one tensor factor at each stage.', r'the next incoming labels.', frm=[P_RANK]),
             ]),
        show('S2.5.4',
             r'Gate labels are assigned in the order of the eight times so that all decreases are confined to the central-wire edge from time 3 to time 4.',
             'Decompose $A\otimes F=(B\otimes F)\perp(P\otimes F)$ and give each time a label from the table, using $t_X\perp t_Y$ on side wires.',
             mot('Making the label grow along every edge except one return of each central wire is what keeps the total loss small.', 'recoverable'),
             [
                 infer('S2.5.4a', r'The labels use the decomposition $A\otimes F=(B\otimes F)\perp(P\otimes F)$, with common summand $B\otimes F$ and remaining summand $P\otimes F$ of dimension $h$.',
                       r'The gate labels are organized by the decomposition', r'of dimension $h$.', frm=[P_RANK]),
                 infer('S2.5.4b', r'A central wire returns once from the label $A\otimes F$ to $B\otimes F$, losing exactly $P\otimes F$, and the gate order confines all decreases to this return.',
                       r'For the central gates we assign $A\otimes F$ on the physical $X$', r'prescribed stage transitions.', frm=[]),
                 infer('S2.5.4c', r'The common gate labels at times 0 to 7 are $B\otimes\langle t\rangle$, $B\otimes F$, $(B\otimes F)\perp(P\otimes\langle t\rangle)$, $A\otimes F$, $B\otimes F$, $(B\otimes F)\perp(P\otimes t^\perp)$, $A\otimes F$ and $A\otimes F$.',
                       r'\text{time}&\text{physical wires}&\text{common gate label}', r'7&X,\ \text{its side wires}&A\otimes F.', frm=[]),
             ]),
        show('S2.5.5',
             r'Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to time 4 of loss $h$, so $L=Ich$ and the absolute dimension changes sum to $Wm-2N+2L$.',
             'Tabulate the orthogonal residual and its dimension on every edge, observe that dimension is nondecreasing except on center $3\\to4$, and use the telescoping identity at gates to turn signed into absolute changes.',
             mot('The orthogonal residual of an edge is the complement of the smaller label in the larger one, so its dimension is the number of smaller operations needed on that edge.', 'recoverable'),
             [
                 infer('S2.5.5a', r'Every edge joins comparable nondegenerate labels and the only decreasing edges are the central-wire edges from time 3 to time 4, each of dimension loss $h$.',
                       r'Every edge joins comparable nondegenerate labels. The only decreasing', r'loss is $h$.', frm=[P_RANK]),
                 infer('S2.5.5b', r'The orthogonal residual of each edge and its dimension are tabulated, for example $(a-1)(h-1)$ on the first $X$ edge, $h$ on each central edge, $h-2$ on the side edge $2\to5$, and $ah(f-1)$ on the scratch edges into the sinks.',
                       r'\text{wire and edge}&\text{orthogonal residual}&\text{dimension}', r'&ah(f-1).', frm=[P_RANK]),
                 infer('S2.5.5d', r'The side edge $2\to5$ is an inclusion because $t_X\perp t_Y$ gives $\langle t_X\rangle\subset t_Y^\perp$, and its residual has dimension $h-2$.',
                       r'The side edge $2\to5$ uses the neighbor relation', r'gives the residual in the table.', frm=[P_RANK, DOT]),
                 infer('S2.5.5c', r'Label dimension is nondecreasing along every edge except center $3\to4$, which removes $P\otimes F\otimes Q$; the initial and final data labels match their terminals so no other changes occur.',
                       r'Label dimension is nondecreasing along every edge except center $3\to4$, which removes', r'so no other dimension changes occur.', frm=[]),
                 infer('S2.5.5e', r'The signed dimension changes telescope at every gate, sum to $Wm-2N$, and the $Ic$ decreasing edges of loss $h$ make the absolute sum $Wm-2N+2L$ with $L=Ich$.',
                       r'The signed sum of dimension changes telescopes at every gate: each', r'adds $2L$.', frm=[],
                       salient=r'$L/N$ equals $100/539$ for the bit network and $101/539$ for the complex network, both below $1/2$, because decreases occur only once per central wire.'),
                 infer('S2.5.5f', r'Over $\mathbb F_2$ every nonzero orthogonal residual is nondegenerate and nonalternating, hence has an orthonormal basis.',
                       r'Now work over $\mathbb F_2$. A nondegenerate symmetric bilinear space', r'absorbs every alternating plane.', frm=[P_RANK, XOR]),
                 infer('S2.5.5g', r'The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.',
                       r'The loss ratios have the exact values', r'both are smaller than $1/2$.', frm=[]),
             ]),
        show('S2.5.6',
             r'For the bit network the edge matrices $M_v$ are rational projections $P_U$, the endpoint difference is $I_m$ on every input role, and the sum of edge ranks is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.',
             'Assign projection matrices to labels, show the rank of an edge difference equals the dimension change, and add the $N$ extra ranks coming from the negative source projections.',
             mot('Rank of $P_V-P_U$ equals $\\dim V-\\dim U$, so rank sums copy the dimension accounting except where the source matrix breaks the pattern.', 'recoverable'),
             [
                 infer('S2.5.6a', r'The projection $P_U$ onto $U$ along $U^\perp$ is assigned to each gate or sink with label $U$, the source matrix $-P_{U_a}$ to $X_a$, and zero to every other source.',
                       r'For a nondegenerate rational subspace $U\subset\mathcal F$, write', r'every other source.', frm=[MAT, P_RANK]),
                 infer('S2.5.6b', r'The frame $\Phi_M$ moves the entry at address $(H,D)$ to $(H+MD,D)$ modulo a common range, and $\Phi_{M\'}\Phi_M=\Phi_{M\'+M}$.',
                       r'In the tape application, two address chunks are written as vectors $H,D$', r'$\Phi_{M\'}\Phi_M=\Phi_{M\'+M}$.', frm=[MOD, PERM, P_FRAME]),
                 infer('S2.5.6c', r'The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, sends its input to the permutation $\rho$, has endpoint difference $I_m$ on every input role, and total rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.',
                       r'The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates,', r'<W_{\rm b}m.', frm=[XOR]),
                 infer('S2.5.6d', r'For nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its complement, so its rank is $\dim V-\dim U$ and reversing the edge does not change it.',
                       r'For $U\subset V$ nondegenerate,', r'reversing the edge negates the matrix without changing its rank.', frm=[P_RANK, MAT]),
                 infer('S2.5.6e', r'The only exceptions are the $N$ negative source projections: the first edge matrix on $X_a$ at stage 1 is $2P_{U_a}$ of rank one although the dimension change was zero, giving the deficit $N-2L_{\rm b}>0$ from $W_{\rm b}m$.',
                       r'The only exceptions are the $N$ negative source projections.', r'Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.', frm=[],
                       salient=r'In the bit network the rank sum exceeds the dimension accounting by exactly $N$ because of the negative source projection, but since $L_{\rm b}<N/2$ the total is still below $W_{\rm b}m$.'),
                 infer('S2.5.6f', r'For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has zero source matrix and identity sink matrix.',
                       r'For an input $X_a$ the endpoint difference is', r'This proves the interface.', frm=[MAT]),
             ]),
    ],
    page=P_LABEL, frm=[P_RANK, P_FRAME, P_EXCH, SETS, DOT, MAT, XOR],
    adds=[
        B('h', 'ground-set size', 'the number of points ($h=100$) from which three-element subsets are drawn', 'count'),
        B('m', 'label dimension', 'the dimension $m=h^3$ of the label space $\\mathcal F$, equal to the number of coordinate fields in the address shear', 'count'),
        B('N', 'source dimension total', 'the sum of the dimensions of all source labels', 'count'),
        B('L', 'lost dimension', 'the total dimension lost on decreasing edges', 'count'),
        B('s', 'total edge rank', 'the sum over all edges of the rank of the edge difference, equal to the number of smaller calls', 'count'),
        B('W', 'wire count', 'the number of wires of the network, scratch wires included', 'count'),
    ],
)

# ---- phase network (second variant)
S2_6 = show(
    'S2.6',
    r'In the complex network with binary labels each edge frame change is a product of one two-point kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual, the total count is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and the endpoint operator is $C^{\otimes m}$ on every role.',
    'Define phase frames from the Hamming weight modulo four, show weight is additive across orthogonal sums so each residual basis vector adds one kernel, count kernels as the edge ranks, and repair the one asymmetric pair with $Z$-conjugation.',
    mot('Weight modulo four turns orthogonal direct sums into additive phases, and a norm-one vector has odd weight, so each basis vector contributes exactly one fourth-root phase that is one two-point kernel; this makes arithmetic exact over Gaussian dyadics.', 'recoverable'),
    [
        infer('S2.6.1', r'For a binary label $U$ let $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$, with $P_U$ the projection over $\mathbb F_2$.',
              r'Use the complex scalar network and binary labels.', r'The projection here is over $\mathbb F_2$.', frm=[XOR]),
        infer('S2.6.2', r'With $H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, the kernel is $C=H\,\mathrm{diag}(1,i)\,H=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$, and $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$ has entries that are Gaussian integers divided by $2^m$.',
              r'H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad', r'preserve arrays over $\mathbb Z[i,1/2]$.', frm=[CX, MAT, DYAD]),
        infer('S2.6.3', r'The frame at a vertex with label $U$ is $\mathcal C_U$, and on $k$ columns every frame and edge operator is the $k$-fold tensor power of its one-column version.',
              r'To apply the scalar network to these functions, replace the scalar on', r'to the vector of values on the roles it touches.', frm=[P_FRAME]),
        infer('S2.6.4', r'Each edge frame change $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$ or its inverse per vector of an orthonormal basis of the edge residual, summing to $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and the telescoped endpoint operator is $C^{\otimes m}$ on every role.',
              r'For each edge of the complex network, write $U,V$ for its tail and', r'<W_{\rm c}m.', frm=[P_LABEL]),
        infer('S2.6.5', r'For binary $z,w$, $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$, so weight is additive modulo four when $z\cdot w=0$.',
              r'For binary vectors $z,w$,', r'additive modulo four.', frm=[XOR, SETS]),
        infer('S2.6.6', r'If $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$ then $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$.',
              r'If $V=U\mathbin{\perp}E$ and $\mathcal B$', r'[v\cdot x]\pmod4.', frm=[DOT]),
        infer('S2.6.7', r'A norm-one vector has odd weight, so its phase coefficient is $\varepsilon=\pm1$ modulo four, and $i^{\varepsilon[v\cdot x]}=\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$ becomes $aI+bX_v$ (or its inverse) because $H\operatorname{diag}(1,-1)H=X$.',
              r'Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd.', r'becomes $aI+bX_v$ or its inverse.', frm=[XOR, ROOTS, MAT]),
        infer('S2.6.8', r'Nonzero residuals have orthonormal bases by the residual lemma, zero residuals use the empty basis, so the kernel count is the edge rank sum $s_{\rm c}$ with deficit $2N-2L_{\rm c}>0$, unlike the bit network where $N$ extra source ranks appear.',
              r'The nonzero residuals have such', r'The deficit is $2N-2L_{\rm c}>0$.', frm=[P_LABEL],
              salient=r'Here the deficit is $2N-2L_{\rm c}$, twice as large as in the bit network, because no negative source projection adds ranks.'),
        infer('S2.6.9', r'On $k$ columns each residual vector contributes one factor $K_{e,v}^{\otimes k}$ acting on all columns, so there are $s_{\rm c}$ such factors over the network.',
              r'For an edge $e$, write $\mathcal B_e$ for its residual basis and', r'such factors over the network.', frm=[MAT]),
        infer('S2.6.10', r'By the scalar exchange lemma the pointwise network sends $X_a$ to $Y_a$ with sign $+1$, $Y_a$ to $X_a$ with sign $-1$ and each scratch input to itself with sign $+1$, with route operator the $k$th tensor power of the displayed address operator.',
              r'Let $\rho$ denote the underlying permutation of the complex roles: it', r'multiplied by its scalar route sign once.', frm=[P_EXCH, P_FRAME]),
        infer('S2.6.11', r'The zero label has frame $I$ and the full label has frame $C^{\otimes m}$ since $q_{\mathcal F}(x)=\operatorname{wt}(x)$; for $X_a\to Y_a$ the phase difference is $\operatorname{wt}(x)+2[u\cdot x]$ modulo four because $u_a$ has weight $27$, giving $C^{-1}$ on the 27 support coordinates and $C$ elsewhere.',
              r'The zero label has frame $I$, while the full label has frame', r'and $C$ elsewhere.', frm=[XOR]),
        infer('S2.6.12', r'With $Z=\operatorname{diag}(1,-1)$ one has $C=iZC^{-1}Z$, so applying $Z_{a,k}$ before and $i^{27k}Z_{a,k}$ after the network turns each of the $27k$ inverse factors into $C$ and gives $C^{\otimes mk}$ on this pair as well.',
              r'Put $Z=\operatorname{diag}(1,-1)$. Direct multiplication gives', r'$C^{\otimes mk}$ as well.', frm=[MAT, CX]),
        infer('S2.6.13', r'Negating the physical $X$ outputs and sending output role $\rho(w)$ back to role $w$ leaves the forward tensor product $C^{\otimes m}$ on every role, scratch roles included.',
              r'Only the physical $X$ outputs still carry the minus sign of the', r'required forward tensor product.', frm=[]),
        show('S2.6.14',
             r'With the fixed exponent $\tau=\sigma=1-2^{-50}$ one has $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $0<\tau=\sigma<1$.',
             'Compute the relative rank deficits $\\eta_{\\rm b},\\eta_{\\rm c}$ exactly, show they exceed $20\\cdot2^{-50}$, and compare with $m^{1-2^{-50}}=m\\exp(-2^{-50}\\log m)$.',
             mot('The recursion needs a rational exponent strictly between the ratio $s/W$ measured in powers of $m$ and one; a bound on the deficit gives it with an explicit exponent.', 'recoverable'),
             [
                 infer('S2.6.14a', r'The relative rank deficits are $\eta_{\rm b}=339/22587335000000$ and $\eta_{\rm c}=73/19906842167500$.',
                       r'The relative rank deficits are', r'\frac{73}{19906842167500}.', frm=[]),
                 infer('S2.6.14b', r'The exponent $\tau=\sigma=1-2^{-50}$ may be used for both recurrences because both exact deficits exceed $20\cdot2^{-50}$.',
                       r'For both recurrences we may use the fixed rational exponent', r'greater than $20\cdot2^{-50}$.', frm=[]),
                 infer('S2.6.14c', r'Since $m<2^{20}$ and $\log2<1$, $\log m<20$, hence $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta)$ for $\eta=\eta_{\rm b}$ or $\eta_{\rm c}$.',
                       r'Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence', r'for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$.', frm=[EXP]),
                 infer('S2.6.14d', r'Consequently $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$ with $0<\tau=\sigma<1$.',
                       r'Consequently', r'0<\tau=\sigma<1.', frm=[]),
             ]),
    ],
    page=P_PHASE, frm=[P_EXCH, P_FRAME, P_RANK, P_LABEL, XOR, DOT, CX, MAT, DYAD],
    adds=[B('C', 'two-point kernel', 'the $2\\times2$ matrix $C=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$ whose tensor powers are the endpoint operators of the complex network')],
)

# ---- shear factorization
S2_8 = show(
    'S2.8',
    r'The address shear $(H,D)\mapsto(H+AD,D)$ for a rational matrix $A$ of rank $a$ is performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work, after factoring $A=E_1\Pi E_2$ into lower-triangular factors and a partial permutation matrix.',
    'Factor $A$ by elimination into lower-triangular factors and a partial permutation, perform the triangular parts as controlled shifts in linear time, and reduce each pivot of $\\Pi$ to one interchange by three updates.',
    mot('Controlled shifts update a later field from earlier fields in linear time, so any lower-triangular change of coordinates is cheap and only the rank-$a$ partial permutation needs interchanges.', 'explicit',
        r'Lemma~\ref{lem:ordered-affine-streams} updates a later field using', r'entirely in this direction.'),
    [
        infer('S2.8.1', r'Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ having exactly $a$ ones, at most one in each row and column.',
              r'Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization', r'all remaining entries zero.', frm=[TRI, MAT]),
        infer('S2.8.2', r'Choosing the topmost nonzero row and its rightmost nonzero entry, clearing to its left by right multiplication and below by left multiplication with lower triangular elementary matrices, and scaling the pivot to one isolates one pivot.',
              r'Otherwise choose the topmost', r'scale the pivot to one.', frm=[TRI]),
        infer('S2.8.3', r'Repeating on the active indices keeps all operations lower triangular, and the final partial permutation has exactly $a$ ones.',
              r'Delete the pivot row and column from the active index sets', r'exactly $a$ ones.', frm=[INDUCT]),
        infer('S2.8.4', r'For $A$ in a finite collection of rational matrices of rank $a$ there is a fixed odd prime $q$ such that $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ uses exactly $a$ interchanges of $b$-digit fields between an $H$ field and a $D$ field and $O(V)$ further work.',
              r'For $A\in\mathcal A$ of rational rank $a$, the', r'Every interchange is between an $H$ field and a $D$ field.', frm=[MOD, PRIME]),
        infer('S2.8.5', r'A lower triangular transformation of $H$ or of $D$ costs $O(V)$ by updating coordinates in descending physical order, each by its diagonal unit and a fixed linear combination of earlier coordinates; inverses are also lower triangular.',
              r'A lower triangular transformation of $H$, or of $D$, costs $O(V)$:', r'Inverses are also lower triangular.', frm=[P_CSHIFT, TRI]),
        infer('S2.8.6', r'For $A=E_1\Pi E_2$ transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$; each one at position $(i,j)$ of $\Pi$ calls for $H_i\leftarrow H_i+D_j$.',
              r'For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,', r'$H_i\leftarrow H_i+D_j$.', frm=[TRI]),
        infer('S2.8.7', r'$H_i\leftarrow H_i+D_j$ is realized by $D_j\leftarrow D_j+H_i$, an interchange $(H_i,D_j)\leftarrow(D_j,H_i)$, and $D_j\leftarrow H_i-D_j$, yielding $(h,d)\mapsto(h+d,d)$ with just one interchange, the first and last updates targeting a later field controlled by an earlier one.',
              r'Implement it by', r'It uses just one interchange.', frm=[P_CSHIFT]),
        infer('S2.8.8', r'With $a$ ones in $\Pi$ the number of recursive calls equals the rational rank $a$, and temporary tapes for other operations do not multiply that count.',
              r'There are $a$ ones, which proves the', r'that count.', frm=[],
              salient=r'The count of smaller interchanges is exactly the rank $a$ of the matrix, not its size $m$, which is why rank sums measure the cost.'),
    ],
    page=P_SHEAR, frm=[TRI, MAT, MOD, PRIME, P_CSHIFT, P_ADDR, P_LABEL],
)

# ---- power-width interchange (variant 1 recursion)
S2_9 = show(
    'S2.9',
    r'Two disjoint contiguous address chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time by running the bit network on $W$ role streams, with each edge shear implemented by $\operatorname{rank}$ many smaller interchanges, for any rational $\tau$ with $s/W<m^\tau<m$.',
    'Induct on $k$: split rows into $W$ role streams, apply the shear on every edge recursively through the shear lemma, run the pointwise gates, merge back, interchange via three shears, and solve the recursion $F_k\\le(s/W)F_{k-1}+O(1)$.',
    mot('The frame identity makes the network apply the shear $H\\leftarrow H+D$ to every role, including scratch roles; each edge shear is $a$ smaller interchanges on volume $V/W$ streams, giving a recursion whose ratio $s/W$ is below $m^\\tau$.', 'recoverable'),
    [
        infer('S2.9.1', r'The circuit has $W$ wires and rational $m\times m$ matrices on terminals and gates with edge differences $A_e$, total rank $s$, and satisfies $M_{{\rm out}(\rho(w))}-M_{{\rm in}(w)}=I_m$ for every input role and $s<Wm$.',
              r'The required conditions are', r'\qquad s<Wm.', frm=[P_LABEL]),
        infer('S2.9.2', r'For any rational $\tau\in(0,1)$ with $s/W<m^\tau$, two disjoint address chunks of $e=m^k$ digits, with a row field preceding both of length divisible by $W^k$, are interchanged in $O(Ve^\tau)$ time on a fixed number of tapes, with constant independent of all field lengths and the data.',
              r'Assume the fixed circuit data satisfy', r'The constant is independent of all field lengths and of the data.', frm=[P_SHEAR, P_LABEL]),
        infer('S2.9.3', r'For $k=0$ use the single-digit operation; for $k>0$ write each chunk as $m$ consecutive $b=e/m$ digit fields, giving vectors $H,D$ over $\mathbb Z/q^b\mathbb Z$, and first construct the shear $H\leftarrow H+D$.',
              r'For $k=0$ apply the single-digit operation of', r'the shear $H\leftarrow H+D$.', frm=[P_ADDR]),
        infer('S2.9.4', r'Splitting whole rows cyclically into $W$ role streams gives streams with the same remaining shape, each of logical volume $V/W$ and row count divisible by $W^{k-1}$.',
              r'Split whole rows cyclically into $W$ role streams within each prefix', r'its row count is divisible by $W^{k-1}$.', frm=[P_ADDR]),
        infer('S2.9.5', r'On every circuit edge apply $\Phi_{A_e}$ to that role stream, implemented recursively through the shear lemma by interchanging each pivot pair of $b$-digit fields, and execute each circuit gate pointwise at matching addresses of the role streams.',
              r'For a rational matrix $M$, let $\Phi_M$ act on an array by moving its', r'addresses of its role streams.', frm=[P_SHEAR]),
        infer('S2.9.6', r'Since a common address permutation commutes with every pointwise bit gate, the frame identity gives $f'+"'"+r'_{\rho(w)}=\Phi_{M_{{\rm out}(\rho(w))}}\Phi_{-M_{{\rm in}(w)}}f_w=\Phi_{I_m}f_w$, i.e. the shear $H\leftarrow H+D$ on each role.',
              r'The row split supplies the common address set used in the', r'by~\eqref{eq:finite-shear-contract}.', frm=[P_FRAME],
              salient=r'The shear is applied identically to every role, the scratch roles included, even though the network is a mixture of gates and edge shears whose individual effects differ.'),
        infer('S2.9.7', r'Merging row $g$ of output role $\rho(w)$ back to original row $Wg+(w-1)$ undoes $\rho$ and restores the row order, so $H\leftarrow H+D$ holds on every original row including rows assigned to scratch roles with arbitrary values.',
              r'Merge by returning row $g$ of', r'whose initial values were arbitrary.', frm=[]),
        infer('S2.9.8', r'The updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the circuit and the others target the later group in linear time.',
              r'To interchange the two full chunks, perform', r'sends $(H,D)$ to $(D,H)$.', frm=[P_CSHIFT]),
        show('S2.9.9',
             r'If $F_k$ bounds time divided by volume then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, so $F_k=O(e^\tau)$ because $s/W<m^\tau$.',
             'Count the $s$ recursive calls on streams of volume $V/W$, add the linear node overhead, and sum the geometric series separately for $s/W\\le1$ and $s/W>1$.',
             mot('Every call but the recursion is a fixed number of linear scans, so the recurrence has a constant additive term and its solution is governed by the ratio $s/W$.', 'recoverable'),
             [
                 infer('S2.9.9a', r'The number of recursive calls is the sum of edge ranks, exactly $s$, each acting on one role stream of volume $V/W$ with all other fields as spectators.',
                       r'The number of recursive calls is the sum of the edge ranks, exactly $s$.', r'fields as spectators.', frm=[P_SHEAR]),
                 infer('S2.9.9b', r'Splitting, merging, gates and triangular operations cost $O(V)$ at a node, so with $F_k$ a uniform bound for time divided by volume, $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.',
                       r'merging, gates, and triangular operations have total cost $O(V)$ because', r'F_k\le(s/W)F_{k-1}+O(1).', frm=[DC]),
                 infer('S2.9.9c', r'For $a=s/W<m^\tau$ the sum $\sum_{j=0}^ka^j$ is $O(m^{k\tau})$: it is at most $k+1=O(m^{k\tau})$ if $a\le1$ and $O(a^k)$ if $a>1$; hence $F_k=O(e^\tau)$.',
                       r'For $a=s/W<m^\tau$ the geometric sum', r'Hence $F_k=O(e^\tau)$.', frm=[GEO, ASYM],
                       salient=r'The exponent $\tau$ can be any number below one with $s/W<m^\tau$; the saving in the exponent is only the distance between $\log_m(s/W)$ and $1$, which is tiny but positive.'),
             ]),
        show('S2.9.10',
             r'Scheduling the recursive calls depth first on a fixed set of tapes adds only $O(V)$ at each node, so it does not change the recurrence.',
             'Park the inactive role streams on a stack, copy the active stream to the child I/O area, return afterwards, and bound descriptor work using the volume that remains at depth $j$.',
             mot('Stack operations move only the volume of the current call, and descriptor work is polylogarithmic in the root volume, which is $O(V_j)$ at depth $j$ because the chunk ranges stay present.', 'recoverable'),
             [
                 infer('S2.9.10a', r'Reserve $W$ role tapes, work tapes, a parking stack and a descriptor stack; before a recursive call append the $W-1$ inactive role streams to the parking stack, copy the active stream to the child I/O area, and push the descriptor, so the same tapes serve every depth.',
                       r'Reserve $W$ role tapes, a fixed set of', r'using the same tapes at every depth.', frm=[TM, SUB]),
                 infer('S2.9.10b', r'Each push, pop, copy, positioning or erasure moves $O(V)$ symbols at a parent node and there are only $s$ child calls, giving precisely the additional $O(V)$ term without substituting temporary storage for logical volume in the factor $s/W$.',
                       r'Each push, pop, copy, positioning operation, or erasure moves $O(V)$', r'factor $s/W$.', frm=[]),
                 infer('S2.9.10c', r'At depth $j$ the volume is $V_j=V_0/W^j\ge q^{2e_0}$ and $j\log W\le(\log_me_0)\log W=O(e_0)=O(\log V_j)$, so $\log V_0=\log V_j+j\log W=O(\log(2V_j))$.',
                       r'Both original chunk ranges remain present: digits outside the current', r'$\log V_0=\log V_j+j\log W=O(\log(2V_j))$.', frm=[MOD]),
                 infer('S2.9.10d', r'Descriptor processing of a child costs $(\log(2V_0))^{O(1)}=O(V_j)$, so one finite machine serves every recursion depth and every choice of spectator lengths.',
                       r'Computing products of their lengths, subdividing', r'depth and every choice of spectator lengths.', frm=[]),
             ]),
    ],
    page=P_PWI, frm=[P_LABEL, P_SHEAR, P_FRAME, P_ADDR, P_CSHIFT, P_SAVE, DC, GEO],
    adds=[
        B('e', 'chunk width', 'the number of radix-$q$ digits $e=m^k$ in each of the two chunks being interchanged', 'count'),
        B('k', 'recursion depth', 'the exponent $k$ in $e=m^k$, the number of recursion levels', 'count'),
        B('\\tau', 'interchange exponent', 'a rational number below one with $s/W<m^\\tau$ bounding the normalized cost by $e^\\tau$'),
    ],
)

# ---- arbitrary width
S2_10 = show(
    'S2.10',
    r'Two disjoint contiguous address fields of $u$ bits of an array on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ are interchanged in $O(Vu^\tau)$ time for the fixed $\tau<1$, by reducing arbitrary widths and row counts to power widths with enough rows.',
    'Create the row field from a few high digits, pad the rows to a multiple of $W^k$, split the remaining width in base $m$ into pieces of widths $m^j$ and apply the power-width interchange to each, undo the padding and the high-digit moves, and pad binary ranges to powers of $q$.',
    mot('The power-width procedure needs a row field divisible by $W^k$ and a width $m^k$; both can be supplied by a few extra moves whose cost is lower order.', 'recoverable'),
    [
        infer('S2.10.1', r'For ranges $[q^e]$ put $k=\lceil\log_me\rceil$ and $\rho=\lceil k\log W/(2\log q)\rceil=O(\log(2e))$; bounded remaining widths are handled by $e$ individual digit interchanges.',
              r'First suppose the two ranges are $[q^e]$, where $q$ is the fixed prime', r'absorbs their cost.', frm=[P_PWI]),
        infer('S2.10.2', r'Interchanging the top $\rho$ digits one pair at a time and joining the high parts turns the field order $(h^+,h^-,g,d^+,d^-)$ into $(d^+,h^+,h^-,g,d^-)$, then $(d^+,h^+,d^-,g,h^-)$ after the remaining interchange, then $(d^+,d^-,g,h^+,h^-)$ after separating the high parts.',
              r'Write each chunk as its top $\rho$ digits followed by its remaining', r'after separating the high parts again}.', frm=[P_ADDR]),
        infer('S2.10.3', r'In the middle orders the first two fields form a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks; padding with zero rows to $R\'=W^k\lceil R/W^k\rceil<2R$ at most doubles the volume.',
              r'In the two middle orders, the first two fields form a row field of range', r'The padded logical volume is less than $2V$.', frm=[P_ADDR]),
        show('S2.10.4',
             r'Interchanging the remaining pieces costs $O(Ve^\tau)$.',
             'Write the remaining width $e-\\rho=\\sum_ja_jm^j$ in base $m$ with $a_j<m$, apply the power-width interchange to each of the $a_j$ pieces of width $m^j$, and sum the costs.',
             mot('Writing the width in base $m$ splits it into at most $(m-1)(k+1)$ pieces of widths $m^j$ that the power-width procedure accepts directly.', 'recoverable'),
             [
                 infer('S2.10.4a', r'Writing $e-\rho=\sum_{j=0}^ka_jm^j$ with $0\le a_j<m$ partitions each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$, and the power-width interchange is applied to each corresponding pair.',
                       r'Write the remaining width in base $m$:', r'to each corresponding pair.', frm=[P_PWI, RADIX]),
                 infer('S2.10.4b', r'All calls use the same row field of length $R'+"'"+r'$ divisible by each $W^j$, preserve their row address so padded rows are untouched, and cost $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$ as a geometric sum, using $a_j<m$ and $m^k<me$.',
                       r'All these calls use the same row field of length $R', r'geometric sum of the stated order.', frm=[GEO]),
             ]),
        infer('S2.10.5', r'Scanning away the padded rows and reversing only the moves that joined the high parts leaves the exact interchange of the two full chunks, with remaining movement cost $O(V\log(2e))=O(Ve^\tau)$.',
              r'Scan away the padded rows, then', r'is $O(Ve^\tau)$.', frm=[P_ADDR]),
        infer('S2.10.6', r'For binary chunks pad each range from $[2^u]$ to $[q^e]$ with $q^e\ge2^u$ at fixed factor $q^2$ extra volume, interchange, and scan away the invalid entries, giving $O(Vu^\tau)$ since $e=O(u)$.',
              r'Finally, for binary chunks let $e$ be the least integer with', r'$O(Vu^\tau)$.', frm=[BIN]),
        infer('S2.10.7', r'For widths differing by one bit, move the leading bit of the longer chunk outside, interchange the equal-width parts, and put it back, so every later interchange of bit chunks is an instance of the lemma.',
              r'For widths differing by one bit, choose the leading bit of the longer', r'in the final order.', frm=[P_ADDR]),
    ],
    page=P_CHUNK, frm=[P_PWI, P_ADDR, GEO, RADIX, BIN],
    adds=[B('u', 'chunk bits', 'the number of bits in each of the two address chunks being interchanged', 'count')],
)

# ---- packed selected-bit addition
def mk_S2_11():
    return show(
    'S2.11',
    r'XORing the selected bits $x_{j_i}$ into $y_{j_i}$ at $f$ positions of two $L$-bit chunks takes $O(V(L^\tau+1))$ time, using a constant number of whole-chunk cyclic shifts that are correct off a set $\mathcal B$ of guard-violating addresses of fraction at most $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, which is then repaired deterministically by sorting.',
    'Realize the conditional parity flip of each segment as eight conditional additions that restore an arbitrary auxiliary integer, pack the $f-1$ segments with guard bits so that the additions are simultaneous cyclic shifts, count the few addresses where a guard fails, and fix exactly those by an extraction-sort-reinsertion pass.',
    mot('Packed additions carry into the neighboring segment only when a guard value is within a few units of its range ends, which a union bound shows is a small fraction of addresses, so the fix-up by sorting costs little.', 'recoverable'),
    [
        infer('S2.11.1', r'For parameters $R,K,f,L=fK,\rho$ on a rectangle of $R$-bit records with three chunks $x,y,z$ in any order, the procedure performs $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ for $j_i=\rho+iK$, restores $z$ for every initial value, and its time is $O\bigl(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect})\bigr)$, which is $O(V(L^\tau+1))$ in the fixed family.',
              r'With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is', r'in the fixed family.', frm=[XOR, P_CHUNK]),
        show('S2.11.2',
             r'Eight conditional additions to two integers $u,w$ flip the parity of $u$ exactly when the Boolean control $c$ is $1$ and restore $w$.',
             'Write the eight additions in order, track the parity pair $(u,w)$ through two three-cycles, and compose them.',
             mot('Each addition changes only one parity pair at a time, so two three-cycles on the four parity corners compose to the transposition that flips the parity of $u$ and fixes $w$.', 'recoverable'),
             [
                 infer('S2.11.2a', r'For a Boolean control $c$ the eight additions $u\mp c[w\equiv0],\ w\mp c[u\equiv0],\ \dots$ in the stated order change $u$ and $w$ by at most one each time.',
                       r'For a Boolean control $c$ and arbitrary integers $u,w$, perform the following', r'&(8)', frm=[MOD]),
                 infer('S2.11.2b', r'If $c=1$ the first four operations induce the cycle $(00\ 01\ 10)$ and the last four induce $(01\ 10\ 11)$ on the parity pair in every $2\times2$ square, composing to $(00\ 10)(01\ 11)$, so the output is $(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are preserved, and the auxiliary integer $w$ is restored.',
                       r'If $c=0$, these operations do nothing.', r'auxiliary integer $w$ is restored.', frm=[PERM, MOD]),
             ]),
        infer('S2.11.3', r'Omitting the top selected position, the $f-1$ disjoint $K$-bit segments of $y$ and $z$ are written $u_i=2g_i+a_i$, $w_i=2h_i+b_i$ with guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$, and the control for each pair is the selected bit $c_i=x_{j_i}$.',
              r'Omit the most significant selected position $j_{f-1}$ temporarily.', r'$c_i=x_{j_i}$.', frm=[BIN]),
        infer('S2.11.4', r'Each line of the eight additions applied simultaneously to all segment pairs is the single cyclic shift $y\leftarrow y+\varepsilon\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^L}$, whose offset never depends on its target chunk so each line is a bijection; their composition is $S_0$.',
              r'Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all', r'Let $S_0$ be their composition.', frm=[P_CSHIFT, CYC]),
        infer('S2.11.5', r'Let $\mathcal B$ be the set of addresses where some used guard fails $10\le g\le2^{K-1}-11$; outside $\mathcal B$ every segment stays in $[0,2^K-1]$ even under displacement eight, so no segment carries into or borrows from the next and $S_0$ agrees with the ideal permutation $T_0$ performing the required XORs.',
              r'Let $\mathcal B$ consist of the addresses for which', r'fixes all other address coordinates.', frm=[]),
        infer('S2.11.6', r'Each guard has exactly twenty excluded values among $2^{K-1}$, so the union bound over the $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$, independently of the payload.',
              r'There are exactly twenty excluded values for each guard in', r'No record value enters this count.', frm=[],
              salient=r'The bad fraction $80(f-1)2^{-K}$ depends only on addresses and decays exponentially in $K$, which is why a sorting repair is affordable.'),
        infer('S2.11.7', r'$T_0$ preserves guard values and hence $\mathcal B$; both $T_0$ and $S_0$ are bijections agreeing off $\mathcal B$, so $S_0(\mathcal B)=\mathcal B$ and $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.',
              r'The ideal map $T_0$ preserves all guard values and therefore preserves', r'permutes $\mathcal B$.', frm=[PERM]),
        infer('S2.11.8', r'Each rotation moves its target to the rightmost of the three chunk positions with one chunk swap, collapses the other intervals into a descriptor of $O(A_{\rm rect})$ bits, and costs $O(V)$ by the controlled-shift lemma after a swap costing $O(VL^\tau)$.',
              r'For one rotation, move its target to the rightmost of the three chunk', r'its own padding and cleanup.', frm=[P_CHUNK, P_CSHIFT]),
        infer('S2.11.9', r'With the target after its two controls the offset routine evaluates the cyclic-shift formula in $L^{O(1)}$ time, so $S_0$ uses at most sixteen swaps and eight rotations.',
              r'With the target now after its two controls, collapse', r'There are at most sixteen swaps and eight rotations in $S_0$.', frm=[P_CSHIFT]),
        infer('S2.11.10', r'The correction scans records with a rank counter, extracts the records of $\mathcal B$ with destination keys $q'+"'"+r'=T_0(S_0^{-1}(q))$, sorts them stably by radix sort on the keys, and reinserts them in one forward scan, implementing $T_0$ everywhere.',
              r'To implement the correction, scan the stream with a record-rank counter.', r'This implements $T_0$ everywhere.', frm=[SORT, PERM]),
        infer('S2.11.11', r'The omitted top selected position is handled by a two-bit XOR of Lemma 2.1 at cost $O(V)$, and for $f=1$ this is the entire algorithm.',
              r'Finally apply the two-bit XOR to $x_{j_{f-1}},y_{j_{f-1}}$ by', r'the entire algorithm.', frm=[P_ADDR]),
        infer('S2.11.12', r'The movement costs $O(V(L^\tau+1))$, the record scans $O(MA_{\rm rect}^3+V)$ and the radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; after division by $V$ the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)=O(p^22^{-K}(1+A_{\rm rect}/R))=o(1)$ when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$ and $K/\log p\to\infty$.',
              r'The movement costs $O(V(L^\tau+1))$.', r'This proves the final assertion.', frm=[BO, ASYM]),
        infer('S2.11.13', r'A binary change of basis in $\mathrm{GL}(m,\mathbb F_2)$ is a fixed number of row additions, each applying the lemma to slots $h\'$ (as $x$), $h$ (as $y$) and a third distinct slot (as $z$), so a complete change of basis and its inverse cost $O(V((eK)^\tau+1))$.',
              r"To add row $h'$ to row $h$, use slot $h'$ as $x$,", r'$O(V((eK)^\tau+1))$ on a stream of volume $V$.', frm=[MAT]),
    ],
    page=P_PACKED, frm=[XOR, MOD, PERM, SORT, CYC, BIN, P_CSHIFT, P_CHUNK, P_ADDR],
    adds=[
        B('K', 'chunk width', 'the number of address bits in each chunk, $K=\\lfloor d^c\\rfloor$ in the application', 'count'),
        B('f', 'segment count', 'the number of selected bit positions, equal to the number of $K$-bit chunks in a slot', 'count'),
    ],
)

# ---- simultaneous butterfly layer (variant 2 recursion)
S2_12 = show(
    'S2.12',
    r'Applying $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ to the same bit position in each of $D\le d$ address chunks of $K$ bits, on polynomial records with $r$ complex fixed-point coefficients in the unit disk, costs $O(Vd^{\lambda@AP@})$ for a fixed $\lambda@AP@<1$, with one final truncation of error below $\sqrt2\,2^{-p}$.',
    'Express $H_0^{\\otimes D}$ through $C^{\\otimes D}$ and diagonal phases, evaluate $C^{\\otimes e}$ by the phase network recursively with binary changes of basis done by packed selected-bit addition, split rows among the wire roles so each child has volume $V/W$, unroll the recursion, and bound the guard widths so that the evaluation is exact.',
    mot('Separate butterfly factors would need one whole-array pass per axis; the recursive network saves a power of $d$ because the number of children is below the number of roles times the dimension.', 'explicit',
        r'whereas separate butterfly', r'would require $D$ whole-array passes.'),
    [
        infer('S2.12.1', r'The layer acts on $[P]\times[2^K]^D\times[S]$ with parameters $d=\Theta(p^\epsilon)$, $K=\lfloor d^c\rfloor$ and $r=2^{\Theta(p/d)}$, so that $r$ exceeds every fixed power of $p$ and $K/\log p\to\infty$.',
              r'The parameters will satisfy', r'to repair by sorting.', frm=[P_FIXED]),
        infer('S2.12.2', r'With $H=\sqrt2H_0$, $\mathsf S=\operatorname{diag}(1,i)$ and $Z=\operatorname{diag}(1,-1)$, one has $C=H\mathsf SH=aI+bX$, $H_0=b\mathsf SC\mathsf S$, $C^2=X$, $C^4=I$ and $C^{-1}=bI+aX=-iZCZ$.',
              r'Direct multiplication gives', r'C^{-1}=bI+aX=-iZCZ.', frm=[CX, MAT]),
        infer('S2.12.3', r'The frame change on an edge from label $U_-$ to $U_+$ is $\prod_{j=1}^{\rho_{\rm edge}}(aI+bX_{v_j})^{\epsilon_j}$ for an orthonormal basis $v_j$ of the residual, $\epsilon_j\in\{1,-1\}$.',
              r'Consider an edge from label $U_-$ to label $U_+$, and choose an', r'\epsilon_j\in\{1,-1\}.', frm=[P_PHASE]),
        show('S2.12.4',
             r'An arbitrary residual basis is implemented by a change of coordinates $\mathcal P_M$ with $M\in\mathrm{GL}(m,\mathbb F_2)$, one child call per basis vector on one slot of $f$ axes, and at most $m(m-1)+3m$ row additions.',
             'Conjugate the product of kernels in the first residual directions by the address permutation $\\mathcal P_M$ carrying the basis to standard vectors, lay the group out in $m$ slots, and express $\\mathcal P_M$ by elementary row additions.',
             mot('The conjugation identity needs only invertibility of $M$, and row additions of whole slots can be done by the packed operation, so no general transpose is required.', 'recoverable'),
             [
                 infer('S2.12.4a', r'The address permutation $\mathcal P_M$ with $(\mathcal P_Mf)(x)=f(M^{-1}x)$ satisfies $\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}$, and taking the residual basis as the first columns of an invertible $M$ turns the edge identity into $\mathcal P_M\bigl(\prod_jC_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$, using only invertibility of $M$.',
                       r'For $M\in\operatorname{GL}(m,\mathbb F_2)$, let $\mathcal P_M$ be the', r'uses its invertibility.', frm=[MAT, PERM]),
                 infer('S2.12.4b', r'A group of $e=mf$ consecutive axis chunks is divided into $m$ slots of $f$ chunks, column $j$ is the vector $(x_{1,j},\dots,x_{m,j})$ of selected bits, and a frame on the group is the same phase frame on these $f$ columns.',
                       r'For the array layout used below, take a group of $e=mf$ consecutive', r'$f$ columns.', frm=[P_PHASE]),
                 infer('S2.12.4c', r'The edge is implemented by applying $\mathcal P_M^{-1}$ to each column, then $(C^{\epsilon_h})^{\otimes f}$ on the $f$ bits $x_{h,0},\dots,x_{h,f-1}$ of slot $h$ for each $h\le\rho_{\rm edge}$ (one child operation on $f$ axes), then $\mathcal P_M$.',
                       r'To implement \eqref{eq:phase-edge-coordinate} on the group, first apply', r'in slot $h$.', frm=[]),
                 infer('S2.12.4d', r'A negative directional kernel still needs only one forward child because $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$, and the wrappers are address signs and fourth-root phases.',
                       r'A negative directional kernel still requires only one', r'so they add no recursive calls.', frm=[P_PHASE]),
                 infer('S2.12.4e', r'Gaussian elimination writes $M$ as at most $m(m-1)+3m$ elementary row additions (each row swap is three), and adding row $h'+"'"+r'$ to row $h$ in every column applies $x_{h,j}\leftarrow x_{h,j}\oplus x_{h'+"'"+r',j}$ for all $j$ at once by the packed operation.',
                       r'Gaussian elimination expresses any $M\in\operatorname{GL}(m,\mathbb F_2)$', r'performs all of these XORs together.', frm=[XOR, MAT]),
             ]),
        infer('S2.12.5', r'Applying the finite network with these column frames to $e=mf$ selected axes gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, with $C^{\otimes e}$ on every role, scratch roles included, and only a fixed number of row additions and coefficientwise scalar operations besides.',
              r'Apply the finite network with these column frames to a group of', r'coefficientwise scalar operations.', frm=[P_PHASE]),
        infer('S2.12.6', r'Multiplying the value at an address by $i^{x_1+\cdots+x_D}$ defines the diagonal operator $\mathcal S_D$, and $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $b^D$ a binary shift and fourth-root phase times at most one factor $b$.',
              r'The diagonal operator $\mathcal S_D$ multiplies the value stored at', r'b^D\mathcal S_D C^{\otimes D}\mathcal S_D.', frm=[CX]),
        mk_S2_11(),
        show('S2.12.7',
             r'The recursive network evaluation on fixed tapes costs $O(V((eK)^\tau+1))$ at a node of $e$ chunks, and unrolling $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ with $F(e)=O(e)$ for $e<d^\beta$ gives $O(d^{\lambda@AP@})$ per volume.',
             'Provide rows by individually transforming the first $q_0$ chunks, split rows into the $W$ roles, count the node overhead from the packed operation, then unroll the recurrence and sum over a base-$m$ partition of the chunks.',
             mot('The roles need $W^{k_0}$ rows to be split at every depth; a logarithmic number of chunks supplies them, and the recurrence has the same shape as the one for the interchange but with an overhead $e^{\\lambda}$.', 'recoverable'),
             [
                 infer('S2.12.7a', r'At a node of $e=m^k$ active chunks the phase construction makes exactly $s$ recursive calls on slots, and the binary changes of basis, scalar gates, endpoint corrections and reassembly cost $O(V((eK)^\tau+1))$ at this node.',
                       r'First consider an internal node containing \(e=m^k\) consecutive', r'at this node.', frm=[P_PACKED]),
                 show('S2.12.7b',
                      r'Rows are supplied by transforming the first $q_0$ chunks individually, padded to a multiple of $W^{k_0}$, and each recursive edge call acts on one role stream of exactly $1/W$ of its parent volume.',
                      'Treat the concatenated bits of the first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks as a row index, pad rows within each prefix, and assign row $Wg+w$ to role $w$.',
                      mot('The network needs the row count divisible by $W^{k_0}$ at depth zero, and each recursion divides it by $W$.', 'recoverable'),
                      [
                          infer('S2.12.7b1', r'If $D\le q_0$ individual $C$ kernels cost $O(V\log d)$; otherwise $C$ is applied individually to the first $q_0$ chunks, whose bits form a row index of range $2^{q_0K}\ge W^{k_0}$, padded to the next multiple of $W^{k_0}$ with volume growing by at most a factor two, so that at depth $j$ the row count is divisible by $W^{k_0-j}$.',
                                r'If \(D\le q_0\), use individual \(C\) kernels, at cost \(O(V\log d)\).', r'the volume grows by a factor at most two.', frm=[P_ADDR]),
                          infer('S2.12.7b2', r'A row index is written $u=Wg+w$ and the entire row goes to physical wire role $w$, so every role stream has the same remaining address shape and each recursive edge call acts on one role stream of volume exactly $1/W$ of its parent.',
                                r'At a node, write a row index as \(u=Wg+w\), with \(0\le w<W\),', r'parent@AP@s logical volume.', frm=[P_ADDR]),
                          infer('S2.12.7b3', r'Splitting the row index removes no address within a row, so every role stream retains the complete suffix and, with the spectator intervals collapsed, each child is a rectangle to which the packed lemma applies with its guard count and deterministic repair.',
                                r'Splitting the row index removes no address within a row.', r'deterministic repair apply to every child.', frm=[P_PACKED]),
                          infer('S2.12.7b4', r'The $W$ role streams are managed on a fixed number of tapes by a LIFO stack so that pushing, popping, copying and clearing cost the node volume times a constant, and there are only $d^{O(1)}$ nodes with descriptor setup dominated by $r$.',
                                r'The \(W\) role streams use a fixed number of tapes.', r'dominated by \(r\).', frm=[P_PWI]),
                          infer('S2.12.7b5', r'Each completed network invocation applies $C^{\otimes e}$ to each input row on chunks disjoint from the earlier preprocessing, so the two commute on genuine rows, and padded zero rows are again zero and can be deleted afterwards.',
                                r'Every completed network invocation applies \(C^{\otimes e}\)', r'Intermediate scratch values may be arbitrary.', frm=[]),
                      ]),
                 show('S2.12.7c',
                      r'With $F(e)$ the time divided by the current volume, $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ for $e<d^\beta$ imply total cost $O(d^{\lambda@AP@})$ per volume.',
                      'Fix $\\beta=1/2$ and exponents $\\tau,\\sigma<\\lambda<\\lambda\'$; sum the internal-node costs as a geometric series with ratio $a/m^\\lambda<1$ for $a=s/W\\le m^\\sigma$, bound the leaves separately, and add the base-$m$ pieces.',
                      mot('Internal nodes have $K\\le e^{c/\\beta}$ so their overhead is $O(e^\\lambda)$; the leaves, below $d^\\beta$ chunks, contribute $O(e^\\sigma d^{\\beta(1-\\sigma)})$, and both are bounded by a power of $d$ below one.', 'recoverable'),
                      [
                          infer('S2.12.7c1', r'Fix $\beta=1/2$ and rational exponents with $0<\tau<1$, $\max\{0,\log_m(s/W)\}\le\sigma<1$, $\max\{\tau,\sigma\}<\lambda<1$ and $\tau(1+c/\beta)<\lambda$.',
                                r'Fix \(\beta=1/2\), and choose real exponents satisfying', r'\tau(1+c/\beta)<\lambda.', frm=[]),
                          infer('S2.12.7c2', r'Stopping the recursion when $e<d^\beta$ and applying the $e$ kernels individually gives $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ and $F(e)=O(e)$ for $e<d^\beta$.',
                                r'Stop recursion when', r'F(e)=O(e)\quad(e<d^\beta).', frm=[DC]),
                          infer('S2.12.7c3', r'The $s$ child calls run on streams of volume $V/W$, so their total cost is $s(V/W)F(e/m)$ and dividing by $V$ gives the factor $s/W$.',
                                r'Indeed, the \(s\) child calls are executed on streams of volume', r'factor \(s/W\).', frm=[]),
                          infer('S2.12.7c4', r'At an internal node $e\ge d^\beta$, so $K\le d^c\le e^{c/\beta}$ and the overhead is $O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)$.',
                                r'At an internal node \(e\ge d^\beta\), hence', r'\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\).', frm=[]),
                          infer('S2.12.7c5', r'Since $a=s/W\le m^\sigma<m^\lambda$, the internal costs sum to at most $Ce^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda)$.',
                                r'Put \(a=s/W\).  Since \(a\le m^\sigma<m^\lambda\), the internal', r'=O(e^\lambda).', frm=[GEO]),
                          infer('S2.12.7c6', r'The leaves after $j$ levels, each with $u=e/m^j<d^\beta$ active chunks, contribute at most $O(a^ju)\le O(e^\sigma u^{1-\sigma})\le O(e^\sigma d^{\beta(1-\sigma)})$ using $a^j\le m^{j\sigma}=(e/u)^\sigma$.',
                                r'If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\)', r'by taking \(\sigma\ge0\).', frm=[]),
                          infer('S2.12.7c7', r'Writing $D-q_0=\sum_ja_jm^j$ in base $m$ gives at most $(m-1)(1+\lfloor\log_md\rfloor)$ pieces, and adding their costs and the row preprocessing gives $O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda@AP@})$ for any fixed $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda@AP@<1$.',
                                r'Write \(D-q_0=\sum_j a_jm^j\) in base \(m\)', r'\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda@AP@<1.', frm=[RADIX]),
                      ]),
             ]),
        show('S2.12.8',
             r'All intermediate values within one layer are Gaussian dyadics whose denominator and magnitude growth is at most $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, so the exact evaluation uses $O(p)$ bits per coefficient.',
             'Bound the arithmetic dependency depth $A(e)$ by a recurrence $A(e)\\le sA(e/m)+E$, convert depth into growth since each operation at most doubles the modulus and adds at most one denominator bit, and choose $\\epsilon C_1<1$.',
             mot('The accelerated network is evaluated exactly until the entire layer is complete and its intermediate operators need not be contractions, so explicit growth bounds are needed to size the registers.', 'explicit',
                 r'The accelerated network is evaluated exactly until an entire', r'need not be contractions.'),
             [
                 infer('S2.12.8a', r'With $E=64(W+m+1)^3$, $B=s+E$, $\nu=\min\{j\ge1:m^j\ge B\}$, $C_1=\max\{20,\nu+3\}$, $C_0=128mB^2$ and $\Delta=\lceil C_0d^{C_1}\rceil$, the construction has $m^{10}<B<m^{11}$ so $\nu=11$ and $C_1=20$.',
                       r'E=64(W+m+1)^3,\qquad B=s+E,', r'\Delta=\lceil C_0d^{C_1}\rceil.', frm=[]),
                 infer('S2.12.8b', r'A data wire occurs in at most twelve scalar gates, there are at most $12W$ gates and one gate evaluation takes at most $2W^2$ operations, so a network invocation costs at most $24W^3+4s+4W+4<E$ coefficient operations at an interface.',
                       r'The scalar schedule \eqref{eq:motif-schedule} touches a data wire', r'\(E=64(W+m+1)^3\).', frm=[P_EXCH]),
                 infer('S2.12.8c', r'The depth $A(e)$ of operations on any chain satisfies $A(e)\le sA(e/m)+E$ at an internal node and $A(e)\le8e$ at a leaf; the depth estimate concatenates the $s$ calls and so uses $s$, whereas the earlier time recurrence used $s/W$ because the calls act on smaller stream volumes.',
                       r'The paired evaluation in \eqref{eq:individual-C-pair} uses at most', r'smaller stream volumes.', frm=[]),
                 infer('S2.12.8d', r'With $k\le\lceil\log_md\rceil$ internal levels, $sx+E\le(s+E)x=Bx$ for $x\ge1$ and $B^{k+1}\le B^{\log_md+2}=B^2d^{\log_mB}\le B^2d^\nu$ give $A(e)\le8dB^{k+1}\le8B^2d^{\nu+1}$.',
                       r'There are at most \(k\le\lceil\log_m d\rceil\) internal levels.', r'8B^2d^{\nu+1}.', frm=[GEO]),
                 infer('S2.12.8e', r'Concatenating the at most $md$ pieces and the at most $d$ individual kernels gives total depth below $128mB^2d^{\nu+3}\le C_0d^{C_1}$ in either preprocessing branch.',
                       r'For the sufficiently large sizes under consideration, the earlier', r'\(C_1\ge\nu+3\).', frm=[]),
                 infer('S2.12.8f', r'A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell$ by induction, since addition at most doubles the modulus and halving adds one denominator bit, so $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represent every intermediate coefficient exactly.',
                       r'To see how this count controls numerical size, start with disk-valued', r'prevents overflow.', frm=[INDUCT, DYAD]),
                 infer('S2.12.8g', r'Choosing $\epsilon C_1<1$ with $d=\Theta(p^\epsilon)$ makes $\Delta=o(p)$, so the coefficient width stays $O(p)$.',
                       r'Choose \(\epsilon C_1<1\).', r'required in the time analysis.', frm=[]),
             ]),
        infer('S2.12.9', r'The procedure returns $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda@AP@})$ time, every returned coefficient lies in the unit disk and $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$.',
              r'The procedure returns $Q_p(\mathcal H z)$ in the same array,', r'<\sqrt2\,2^{-p}.', frm=[P_FIXED]),
        show('S2.12.10',
             r'The proof of the layer proposition combines the phase-frame reduction to $s_{\rm c}$ children, the packed procedure at one common time constant uniformly in the bands for $d$ and $r$, and the final truncation.',
             'Check that the guarded record width stays within $12rp$, that the packed width parameter obeys $A_*\\le C_Ap$, and that both packed-lemma extra terms tend to zero uniformly.',
             mot('The lemma\'s explicit time bound has two extra terms that vanish only under the family hypotheses, so these must be verified uniformly.', 'recoverable'),
             [
                 infer('S2.12.10a', r'The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ selected bits, the row split gives each child $1/W_{\rm c}$ of the volume, and the packed procedure supplies the binary basis changes.',
                       r'The phase-frame construction reduces a group of $e$ selected bits to', r'uniform over the displayed bands for $d,r$.', frm=[P_PHASE]),
                 infer('S2.12.10b', r'Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, $\Delta\le p$, the guarded record width is $R_{\rm g}=2r(p+2\Delta+3)\le12rp$ and $R_{\rm g}\ge2rp$, and the packed width parameter is $A_*\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap$ with $C_A=C_M+b_r+7$.',
                       r'Put $\Delta=\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$', r'$\log_2p\le p$.', frm=[]),
                 infer('S2.12.10c', r'For large $p$, $f\le d\le p$, $K\ge\frac12a_d^cp^{\epsilon c}$ and $r\ge2^{(a_r/b_d)p^{1-\epsilon}}$, so $K\ge6$, $K/\log p\to\infty$ and the two additional normalized terms $A_*^3/R_{\rm g}\le C_A^3p^2/(2r)$ and $80(f-1)2^{-K}A_*(1+A_*/R_{\rm g})\le80C_Ap^22^{-K}(1+C_A/(2r))$ tend to zero uniformly.',
                       r'Uniformly for large $p$, the bands give', r'with one common time constant.', frm=[]),
                 infer('S2.12.10d', r'The row construction and the recurrence analysis give total time $O(Vd^{\lambda@AP@})$ on fixed tapes including all padded and auxiliary streams, and the phase-butterfly identity converts the exact $C$-layer to $\mathcal H$.',
                       r'The row construction and the recurrence analysis', r'converts the resulting exact $C$-layer to $\mathcal H$.', frm=[]),
                 infer('S2.12.10e', r'Every row of $\mathcal H$ has absolute row sum one so $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation toward zero keeps the disk and changes each component by less than $2^{-p}$, giving error less than $\sqrt2\,2^{-p}$.',
                       r'Finally, every row of $\mathcal H$ has', r'so the supplied component width can hold them.', frm=[NORM]),
             ]),
    ],
    page=P_LAYER, frm=[P_PHASE, P_PACKED, P_FIXED, P_CHUNK, P_PWI, P_SAVE, P_FFT, P_NEG, DC, GEO, CX, DYAD],
    adds=[
        B('d', 'axis bound', 'the maximum number of axes whose selected bits are butterflied together, $d=\\Theta(p^\\epsilon)$', 'count'),
        B('D', 'selected axes', 'the number of address chunks, at most $d$, whose bit at a common offset is transformed', 'count'),
        B('r', 'record length', 'the number of complex coefficients in a polynomial record, a power of two', 'count'),
        B('p', 'precision', 'the number of fractional bits of the fixed-point grid $2^{-p}\\mathbb Z[i]$', 'count'),
        B('\\lambda\'', 'layer exponent', 'a fixed rational number below one bounding the normalized layer cost by $d^{\\lambda\'}$'),
    ],
)

S2 = show(
    'S2',
    r'Both fast tape procedures, interchanging two address chunks of $u$ bits in $O(Vu^\tau)$ time and applying $H_0$ simultaneously to the same bit of $D\le d$ chunks in $O(Vd^{\lambda@AP@})$ time, have exponents below one because each comes from a fixed linear network of $W$ wires whose total number $s$ of smaller calls satisfies $s<Wm$.',
    'Replace the scalar values of a fixed exchange network by arrays under frames, label every gate with a nested subspace so that each edge costs as many smaller calls as its rank, show the total rank $s$ is below $Wm$, split rows among the $W$ roles so each call has volume $V/W$, and solve the resulting recursion; do this once with the bit network for the address interchange and once with the complex phase network for the butterfly layer.',
    mot('The strict inequality of the total number of smaller calls below the number of wires times the dimension makes the cost per volume grow by a factor less than the parameter multiplier at each level.', 'explicit',
        r'The decisive property is that the total', r'$s<Wm$.'),
    [
        S2_0, S2_1, S2_2, S2_3, S2_4, S2_5, S2_6, S2_8, S2_9, S2_10, S2_12,
    ],
    page=P_SAVE, frm=[DC, GEO, ASYM, BO],
    salient=r'One strict inequality $s<Wm$ between two fixed finite numbers, checked from a rank count, is the entire source of the power saving, and it holds in the same form for both the bit network and the complex network.',
    adds=[
        B('W', 'wire count', 'the number of wires of the fixed network, scratch wires included', 'count'),
        B('m', 'label dimension', 'the dimension of the label space, equal to the number of fields or slots into which a parameter is divided at each recursive level', 'count'),
        B('s', 'call count', 'the total rank of the edge differences, equal to the number of smaller calls made by one invocation of the network', 'count'),
    ],
)

# ---------------------------------------------------------------------------------------------
# S3: synthetic transforms and layout
# ---------------------------------------------------------------------------------------------
S3_1 = show(
    'S3.1',
    r'Over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the powers of $\omega_t=y^{2r/t}$ act as signed coefficient shifts (isometries), the transforms $F_t^\pm$ are contractions, and $F_t^+F_t^-=t^{-1}I$ although the ring has zero divisors.',
    'Define the ring, its sup norm and the roots $\\omega_t$, note contraction from averaging isometries, and prove character cancellation by a direct pairing argument instead of dividing by $\\omega_t^j-1$.',
    mot('The ring has zero divisors, so the usual geometric-sum argument for character cancellation fails and a direct argument is needed.', 'explicit',
        r'The ring has zero divisors, so we verify character cancellation', r'dividing by $\omega_t^j-1$.'),
    [
        infer('S3.1.1', r'For a power of two $r\ge2$ the ring is $\mathcal R_r=\mathbb C[y]/(y^r+1)$ with coefficient sup norm $\|\sum_kz_ky^k\|_\infty=\max_k|z_k|$.',
              r'For an integer $r\geq 2$ that is a power of two, put', r'=\max_{0\leq k<r}|z_k|.', frm=[P_NEG, POLY]),
        infer('S3.1.2', r'Multiplication by $y^a$ permutes the coefficients and changes some signs, so it is an isometry for this norm.',
              r'We always use representatives of degree less than $r$. Multiplication', r'it is an isometry for this norm.', frm=[P_NEG]),
        infer('S3.1.3', r'For a power of two $t$ dividing $2r$ put $\omega_t=y^{2r/t}$ and $(F_t^\mp z)_j=\frac1t\sum_k\omega_t^{\mp jk}z_k$; each output averages $t$ isometric images so both transforms are contractions.',
              r'For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$.', r'Thus both transforms are contractions.', frm=[P_DFT, ROOTS]),
        infer('S3.1.4', r'The ring has zero divisors, so character cancellation is verified directly rather than by dividing by $\omega_t^j-1$.',
              r'The ring has zero divisors, so we verify character cancellation', r'dividing by $\omega_t^j-1$.', frm=[]),
        infer('S3.1.5', r'For an integer $j$, $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise, and $F_t^+F_t^-=t^{-1}I$.',
              r'If $j$ is an integer, then', r'F_t^+F_t^-=t^{-1}I.', frm=[]),
        infer('S3.1.6', r'Writing $j=2^vj_0$ with $j_0$ odd, replacing $k$ by $k+t/2^{v+1}$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$, so the sum is zero since the additive group of $\mathcal R_r$ has no two-torsion.',
              r'Only the second case needs proof.', r'has no two-torsion.', frm=[PERM, ROOTS],
              salient=r'The cancellation in a ring with zero divisors holds because a half-period shift multiplies the sum by $-1$.'),
    ],
    page=P_SYN, frm=[P_NEG, P_DFT, ROOTS, POLY, PERM, CX],
)

S3_2 = show(
    'S3.2',
    r'The forward procedure computes $B_tF_t^-$ by decimation in frequency and writes outputs directly in bit-reversed order $B_t$, the reverse procedure computes $F_t^+B_t^{-1}$ from that order, and for several axes one round is a parallel butterfly $\mathcal H$ followed by one recordwise monomial $y^E$.',
    'Run the two-point butterfly and twiddle level by level, track which address bit holds which frequency bit, and traverse the same recursion in reverse for the opposite transform so the permutation is never executed.',
    mot('Because the forward transform writes frequency bits where the recursion leaves them, the pointwise product and the reverse procedure use the same order and no permutation of whole records is needed.', 'recoverable'),
    [
        infer('S3.2.1', r'For $t\ge2$ the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, writes the $H_0$ outputs to the same slots, multiplies the $b=1$ output by $\omega_t^{-k}$ and recurses on the two branches.',
              r'decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$', r'separately within the two branches.', frm=[P_FFT]),
        infer('S3.2.2', r'This computes $F_t^-$ because $(F_t^-z)_{2h+b}=\frac1{t/2}\sum_{k=0}^{t/2-1}(\omega_t^2)^{-hk}\omega_t^{-bk}\frac{z_k+(-1)^bz_{k+t/2}}2$.',
              r'This computes', r'z_{k+t/2}}2.', frm=[P_DFT]),
        infer('S3.2.3', r'After all $a$ rounds the named slots from high to low contain the frequency bits from low to high, so the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$; the recursion writes its outputs directly in this order.',
              r'After all $a$ rounds, the named slots from high to low therefore', r'it does not move whole frequency indices.', frm=[BIN]),
        infer('S3.2.4', r'The reverse procedure processes the smaller branches first, applies the inverse monomial to the second branch and then $H_0$; since $H_0^2=I/2$ each reversed level is half the inverse of the forward level, so the composite with $B_tF_t^-$ is $2^{-a}I=I/t$ and the two procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.',
              r'The procedure consuming this stored order traverses the recursion in', r'respectively.', frm=[P_SYN, MAT]),
        infer('S3.2.5', r'For several axes the twiddles of different axes commute with the other axes\' butterflies, so a round is a parallel butterfly $\mathcal H$ followed by one monomial $J_E$ with exponent $E=-\sum_i\frac{2r}{u_i}b_ik_i\pmod{2r}$, the opposite round is $\mathcal HJ_E^{-1}$, and every completed round is a contraction.',
              r'For $D$ axes of lengths $t_1,\ldots,t_D$, put', r'so every completed round is a contraction.', frm=[P_SYN]),
    ],
    page=P_FREQ, frm=[P_SYN, P_FFT, P_DFT, BIN, MAT, PERM],
)

S3 = show(
    'S3',
    r'With the selected bit of each axis placed at a common offset in consecutive $K$-bit chunks, a forward synthetic transform and its opposite on $M$ polynomial records cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\'}])$ with error below $\sqrt2\,\ell\,2^{-p}$, and the frequency order is retained between them.'.replace("\\'", "@AP@"),
    'Build the layout permutation from bit moves and chunk interchanges, run each round as one simultaneous butterfly layer followed by a monomial, truncate once per round, and show that the exact counterpart is $LBF^-$ with opposite $F^+B^{-1}L^{-1}$.',
    mot('The fast butterfly layer only applies when the participating bits sit at a common offset in consecutive chunks of an array, so the arrays must first be rearranged by cheap movements.', 'recoverable'),
    [
        S3_1,
        S3_2,
        infer('S3.3', r'To apply the simultaneous layer in a transform round the selected bits of the participating axes must be placed at a common offset in consecutive $K$-bit chunks while each polynomial keeps a contiguous suffix; the layout uses the single-bit moves and the chunk interchanges, charged in the transform cost.',
              r'To apply Proposition~\ref{prop:simultaneous-layer} in a transform round,', r'keeping each polynomial\'s coefficients in a contiguous suffix.'.replace("\\'", "@AP@"), frm=[P_LAYER]),
        infer('S3.4', r'For $p,d,r=2^\ell$ in the bands with $d\ell\le C_\ell p$, $1\le K\le\ell-1$ and axes $t_i\in\{2^{\ell-1},2^\ell\}$, $T=rM$, the forward procedure has exact counterpart $LBF_{\boldsymbol t}^-$ and the opposite $F_{\boldsymbol t}^+B^{-1}L^{-1}$, each with error below $\sqrt2\,\ell\,2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\'}])$.'.replace("\\'", "@AP@"),
              r'Each procedure has error less than', r'\label{eq:synthetic-transform-cost}', frm=[P_LAYER, P_CHUNK]),
        infer('S3.5', r'With $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$, the $O(dK)$ listed slots (the top slot of each long axis and the $b$ lowest slots of each axis) are moved to a prefix at cost $O(TpdK)$, leaving $q$ consecutive $K$-bit chunks per axis.',
              r'Put $D=d-1$ and write $a_i=\log_2t_i$.', r'so the moves cost $O(TpdK)$.', frm=[P_ADDR]),
        infer('S3.6', r'Reordering the chunks from axis-major to chunk-index-major takes at most $Dq-1$ exchanges of width-$K$ chunks, each costing $O(TpK^\tau)$, so the total is $O(Tp\,DqK^\tau)=O(Tp\,pK^{\tau-1})$ because $Dq=O(p/K)$.',
              r'Number the axes by $i$ and their chunks, from high to low, by $j$.', r'=O\bigl(Tp\,pK^{\tau-1}\bigr).', frm=[P_CHUNK],
              salient=r'The chunk exchanges number $O(p/K)$ rather than $O(p)$ because only $dq\approx d\ell/K$ chunks must be moved, and each costs $K^\tau$ per volume, giving the term $pK^{\tau-1}$ with exponent below $1$ only because $\tau<1$.'),
        infer('S3.7', r'For a position $h$ in the remaining chunks, the selected bit has offset $(h-b)\bmod K$ in each of the $D$ consecutive chunks of the same index, every combination of the other address bits occurs, and the layer sees the complete address set $[P]\times[2^K]^D\times[S]$ with $\log_2(2M)\le(C_\ell+1)p=C_Mp$.',
              r'For a position $h$ in the remaining chunks, the selected bit has', r'$\log_2(2M)\leq(C_\ell+1)p=C_Mp$.', frm=[P_LAYER]),
        infer('S3.8', r'The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda\'})$ per round and $O(Tp\ell d^{\lambda\'})$ in total.'.replace("\\'", "@AP@"),
              r'The simultaneous-layer procedure therefore applies at cost', r'in total.', frm=[]),
        infer('S3.9', r'The at most $b+1\le K$ rounds on prefix slots process their participating bits individually with exact dyadic coefficients on $p+D+O(1)$ bits, at cost $O(Tp)$ per round and $O(TpdK)$ in total.',
              r'In a round on prefix slots, process the participating bits individually.', r'giving cost $O(TpdK)$.', frm=[]),
        infer('S3.10', r'Multiplication by the monomial $y^E$ with $E=er+s$ splits the coefficient list before position $r-s$, puts the tail before the head, negates the moved tail and applies the sign $(-1)^e$, at cost $O(rp)$ per record and without any sort.',
              r'To implement the monomial, write $E=er+s$ with $0\leq s<r$.', r'no coefficient sort is required.', frm=[P_NEG, CYC]),
        infer('S3.11', r'Truncation toward zero is odd, so $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$; each round adds one truncation of error less than $\sqrt2\,2^{-p}$ to the previous error because a contraction does not increase the difference, and with at most $\ell$ rounds, the layout isometries adding nothing, the error is below $\sqrt2\,\ell\,2^{-p}$.',
              r'For a forward round on a group of $D$ chunks, the layer call returns', r'are isometries and add no numerical error.', frm=[NORM]),
        infer('S3.12', r'Executing the operations on named slots after $L$ conjugates them by $L$, giving full exact operators $LBF_{\boldsymbol t}^-$ and $F_{\boldsymbol t}^+B^{-1}L^{-1}$, and the forward entry with frequency address $j$ is stored at $L(Bj)$.',
              r'It remains to identify the order of the full procedures.', r'restores axis-major physical order.', frm=[P_FREQ]),
    ],
    page=P_LAYOUT, frm=[P_SYN, P_FREQ, P_LAYER, P_CHUNK, P_ADDR, NORM, CYC],
    adds=[
        B('T', 'box size', 'the number of entries $T=rM$ of the padded box, the product of all axis lengths including $r$', 'count'),
        B('\\ell', 'record exponent', 'the exponent $\\ell=\\log_2r$ of the record length', 'count'),
    ],
)

# ---------------------------------------------------------------------------------------------
# S4: normalized ring convolution (with signed packing)
# ---------------------------------------------------------------------------------------------
S4_1 = show(
    'S4.1',
    r'Two disk-grid polynomials $f,g\in\mathcal R_r$ can be multiplied exactly and the normalized product $Q_p(fg/r)$ returned with error below $\sqrt2\,2^{-p}$ in time $O(rp\log(rp))$, by signed Kronecker substitution at $B_0=2^{4p}$ with four integer products by the $O(n\log n)$ multiplier.',
    'Evaluate the integer coefficient polynomials at $B_0=2^{4p}$ with signed carries, multiply the four pairs of evaluation integers, recover the coefficients of the ordinary product by centered residues, reduce modulo $y^r+1$, and truncate after dividing by $r$.',
    mot('Every coefficient of an ordinary polynomial product is below $B_0/2$ in magnitude, so after removing the lower coefficients the next one is identified by its centered residue modulo $B_0$.', 'explicit',
        r'After the lower coefficients have been removed from an evaluation,', r'residue modulo $B_0$.'),
    [
        infer('S4.1.1', r'The fixed-tape integer multiplier of Harvey and van der Hoeven with cost $O(N\log(2N))$ on $N$-bit inputs is used as an independent subroutine, on inputs of $O(rp)$ bits, with conversions charged.',
              r'To multiply the polynomial records, we use the fixed-tape integer', r'This is an independent subroutine.', frm=[P_BARRIER, SUB]),
        infer('S4.1.2', r'Writing $f=2^{-p}(a+ib)$ and $g=2^{-p}(c+ie)$ with integer coefficient polynomials of coefficients at most $2^p$, the evaluation integers $A_u=u(B_0)$ at $B_0=2^{4p}$ satisfy $|A_u|<B_0^r/2$ and fit in $4pr$ bits.',
              r'Set $B_0=2^{4p}$', r'fits in $4pr$ bits.', frm=[RADIX]),
        infer('S4.1.3', r'The four products $A_aA_c$, $A_bA_e$, $A_aA_e$, $A_bA_c$ equal $(ac)(B_0)$ and so on, and every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$.',
              r'Multiply the four', r'<B_0/2.', frm=[POLY]),
        infer('S4.1.4', r'After the lower coefficients have been removed, this strict bound identifies the next coefficient by its centered residue modulo $B_0$.',
              r'After the lower coefficients have been removed from an evaluation,', r'residue modulo $B_0$.', frm=[MOD]),
        infer('S4.1.5', r'Forming $A_u$ with carries $\gamma_j\in\{-1,0\}$ from $d_j\equiv u_j+\gamma_j\pmod{B_0}$ gives blocks forming a fixed-width two\'s-complement encoding of $A_u$ with $\gamma_r=-1$ exactly when $A_u<0$, in $O(rp)$ time.'.replace("\\'", "@AP@"),
              r'To form $A_u$, start with carry $\gamma_0=0$ and write', r'so a constant number of scans costs $O(rp)$.', frm=[BIN]),
        infer('S4.1.6', r'For a product integer $Z=h(B_0)$ with $J=2r$ blocks, at block $j$ let $\widehat h_j$ be the centered representative of $q_j+\rho_j$ modulo $B_0$ and $\rho_{j+1}=(q_j+\rho_j-\widehat h_j)/B_0\in\{0,1\}$.',
              r'Put $\rho_0=0$.  At block $j$, let', r'or subtracts $B_0$.', frm=[MOD]),
        infer('S4.1.7', r'The residual identity $\sum_{k\ge j}h_kB_0^{k-j}=\sum_{k\ge j}q_kB_0^{k-j}+\rho_j+\varepsilon B_0^{J-j}$ shows by induction on $j$ that $\widehat h_j=h_j$, with final carry canceling the sign extension, so extraction costs $O(rp)$.',
              r'The meaning of the carry is the following residual identity, after', r'so extraction costs $O(rp)$.', frm=[INDUCT]),
        infer('S4.1.8', r'Reducing modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$, so each Gaussian integer coefficient $H_j$ is a sum of exactly $r$ signed products and $|H_j|\le r2^{2p}$.',
              r'The real and imaginary numerator streams are respectively', r'|H_j|\leq r2^{2p}.', frm=[P_NEG]),
        infer('S4.1.9', r'The same triangle inequality gives $\|fg/r\|_\infty\le\|f\|_\infty\|g\|_\infty$, so the normalized product of disk polynomials lies in the disk.',
              r'The same triangle inequality before imposing the disk bound gives', r'lies in the disk.', frm=[NORM]),
        infer('S4.1.10', r'The $p$-bit numerator of the normalized product is $\operatorname{trunc}_0(\Re H_j/2^{p+\ell})+i\operatorname{trunc}_0(\Im H_j/2^{p+\ell})$, computed by shifting magnitudes right by $p+\ell$ bits at $O(p)$ per coefficient.',
              r'Finally the $p$-bit grid numerator of the normalized product is', r'used by the opposite transform.', frm=[DYAD]),
        infer('S4.1.11', r'Four exact integer products dominate the linear packing, extraction, combination, wrapping and truncation costs, giving $O(rp\log(rp))$.',
              r'Four exact integer products dominate the linear', r'truncation costs.', frm=[BO]),
    ],
    page=P_PACK, frm=[P_BARRIER, P_NEG, DYAD, POLY, RADIX, MOD, BIN, NORM, INDUCT, SUB, BO],
    adds=[B('B_0', 'evaluation base', 'the large power of two $2^{4p}$ at which polynomials are evaluated to become integers')],
)

S4 = show(
    'S4',
    r'The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is computed from two forward synthetic transforms, a pointwise polynomial product divided by $r$ and one opposite transform in their retained order, with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda@AP@}+\log(rp)])$.',
    'Transform both operands, multiply the records pointwise by signed packing, apply the opposite transform to that order, scale by $M$ exactly, and bound the error by inserting exact maps at the computed inputs.',
    mot('The convolution theorem turns convolution into pointwise products, and keeping the transform output in its stored order lets the pointwise product and the opposite transform use that order without ever permuting.', 'recoverable'),
    [
        S4_1,
        infer('S4.2', r'For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with values in $\mathcal R_r$, $\mathcal M_r(f,g)=(f*g)/(rM)=(f*g)/T$ averages $rM$ signed scalar products per coefficient and is a bilinear contraction, so $\|\mathcal M_r(f,g)\|_\infty\le\|f\|_\infty\|g\|_\infty$.',
              r'For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with values in', r'norm distance between its two values.', frm=[P_CONV, P_NEG, NORM]),
        infer('S4.3', r'Under the hypotheses of the layout lemma $\mathcal M_r$ on disk grid operands has an approximation of error less than $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda@AP@}+\log(rp)])$, with output of width $w_M=w+m_M$, and a disk array if one operand has norm $\le\rho<1$ and the bound is at most $1-\rho$.',
              r'$\mathcal M_r$ on disk grid operands has an approximation with error', r'component boundary from this width and the retained shape parameters.', frm=[P_LAYOUT]),
        infer('S4.4', r'Perform both forward transforms retaining their common $LB$ order, form the pointwise polynomial products in that order by signed packing, apply the opposite procedure to that order, and multiply exactly by $M=T/r$.',
              r'Perform both forward transforms and retain their common $LB$ order.', r'multiply its result exactly by $M=T/r$.', frm=[P_LAYOUT, P_PACK]),
        infer('S4.5', r'Expansion of the finite sums gives $F_{\boldsymbol t}^-(f*g)=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)$ and with $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$ one gets $MF_{\boldsymbol t}^+\bigl(\frac{(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)}r\bigr)=\frac{f*g}{rM}$.',
              r'To check normalization, expansion of the finite sums gives', r'\frac{f*g}{rM}.', frm=[P_DFT, P_SYN]),
        infer('S4.6', r'Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$ for the pointwise product $P(u,v)=uv/r$, so $\mathcal T_+=F_{\boldsymbol t}^+B^{-1}L^{-1}$ applied to the pointwise product of the stored outputs equals $F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$.',
              r'Let $P(u,v)$ denote the exact pointwise product $uv/r$, and put', r'with $\mathcal M_r(f,g)$.', frm=[P_FREQ, PERM],
              salient=r'The stored frequency order, though a nontrivial permutation, never needs to be undone because pointwise multiplication commutes with permuting both operands.'),
        show('S4.7',
             r'The returned convolution has error below $\sqrt2\,M(3\ell+1)2^{-p}$.',
             'Insert exact maps at the computed inputs: forward errors $\\delta=\\sqrt2\\ell2^{-p}$ propagate through the bilinear contraction $P$ to $2\\delta$, one truncation adds $\\eta=\\sqrt2\\,2^{-p}$, the opposite contraction adds nothing but its own $\\delta$, and the exact scaling by $M$ multiplies by $M$.',
             mot('Contractions do not increase differences and truncations add a fixed amount, so the errors add: $2\\delta+\\eta$ before the opposite transform and $3\\delta+\\eta$ after it.', 'recoverable'),
             [
                 infer('S4.7.1', r'With $\delta=\sqrt2\ell2^{-p}$ and $\eta=\sqrt2\,2^{-p}$, the bilinear contraction $P$ gives $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$ using the disk bounds on $\widetilde v$ and $u$.',
                       r'For the error estimate, put', r'the second uses it on $u$.', frm=[P_CONTR]),
                 infer('S4.7.2', r'With $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$, $\widetilde z$ is a disk grid array with $\|\widetilde z-z_*\|_\infty<2\delta+\eta$.',
                       r'Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$.', r'$\|\widetilde z-z_*\|_\infty<2\delta+\eta$.', frm=[]),
                 infer('S4.7.3', r'Since $\mathcal T_+$ is a contraction, $\|\widetilde h-\mathcal T_+z_*\|_\infty<3\delta+\eta$, and the exact multiplication by $M$ gives error below $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.',
                       r'If $\widetilde h$ is the returned opposite output, its approximation', r'as claimed.', frm=[NORM]),
             ]),
        infer('S4.8', r'Scaling by $M=2^{m_M}$ preserves the $p$-bit grid by appending exactly $m_M$ zero bits to each numerator, giving width $w_M=w+m_M=O(p)$, and the procedure writes $\Gamma(w_M)$ on the output descriptor tape.',
              r'Every computed output before the final scaling is a disk grid array.', r'Writing $\Gamma(w_M)$ takes $O(p)$ time.', frm=[DYAD, BIN]),
        infer('S4.9', r'The $M=T/r$ pointwise polynomial products cost $O(Tp\log(rp))$ in total, the three transforms cost as stated, and the last exact scaling is linear in $Tp$.',
              r'There are $M=T/r$ pointwise polynomial products.', r'layout restoration.', frm=[P_PACK]),
    ],
    page=P_NRC, frm=[P_CONV, P_NEG, P_SYN, P_FREQ, P_LAYOUT, P_PACK, P_CONTR, P_DFT, NORM, PERM, DYAD, BIN],
    adds=[B('M', 'transform records', 'the number $M=T/r$ of polynomial records on the first $d-1$ axes', 'count')],
)

# ---------------------------------------------------------------------------------------------
# S5: resampling, chirp, permutation cancellation
# ---------------------------------------------------------------------------------------------
S5_1 = infer('S5.1', r'The vector norm is the maximum modulus, operator norms are induced, the normalized Fourier transforms are contractions since each output averages inputs times unit complex numbers, and coordinate permutations preserve the norm.',
              r'For an integer $q\geq 1$, write', r'Coordinate permutations preserve the norm.', frm=[P_DFT, NORM])
S5_2 = infer('S5.2', r'Grid values lie in $\mathbb D_p=\{2^{-p}(a+ib):a^2+b^2\le2^{2p}\}$ stored as $(p+2)$-bit signed words; an approximation $\widetilde L$ of a linear contraction $L$ has error $E$ if $2^p\|\widetilde Lu-Lu\|<E$, and composing approximations adds their errors by inserting the exact map at the computed input and using its contraction bound.',
              r'For an integer precision $p\geq1$, put', r'on the accumulated input error.', frm=[P_CONTR, DYAD])
S5_3 = infer('S5.3', r'The established $O(N\log N)$ integer multiplier and the Harvey--van der Hoeven routine for $e^{2\pi ij/k}$ to within $2^{-p}\cdot2$ in time $O(\max(p,\log k)^{1+\delta})$ are used as black boxes.',
              r'We use the established $O(N\log N)$ integer multiplier of', r'$O(\max(p,\log k)^{1+\delta})$, for every fixed $0<\delta<1/8$.', frm=[P_BARRIER, EXP])

S5_D = show(
    'S5.4',
    r'For coprime $2\le s<t<2^p$ with $\theta=t/s-1>p/\alpha^4$ there are contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, and fixed multitape approximations of error below $p^2$ and time $O(tp^{3/2+\delta}\alpha)$, without executing the permutations $P_s,P_t$.',
    'Use the Gaussian resampling identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ with $N=C\\mathsf T\\mathsf D$ close to the identity, invert $N$ by a Neumann series, normalize by powers of two to make $A$ and $B_0$ contractions, and implement them with the ordered Harvey--van der Hoeven maps.',
    mot('Gaussian weights make the resampling error $\\|N-I\\|$ exponentially small in $\\alpha^2\\theta$, so the inverse exists, while the normalizations by powers of two cost only the exact scale $2^{2\\alpha^2}$.', 'recoverable'),
    [
        infer('S5.4.1', r'There are linear contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, and fixed multitape approximations $\widetilde A,\widetilde B_0$ with error less than $p^2$ and time $O(tp^{3/2+\delta}\alpha)$ uniformly in $p,s,t,\alpha$.',
              r'There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and', r'occur in increasing coordinate order.', frm=[P_DFT]),
        infer('S5.4.2', r'The Gaussian maps $\mathsf S,\mathsf T:\mathbb C^s\to\mathbb C^t$ are $(\mathsf Su)_k=\alpha^{-1}\sum_je^{-\pi\alpha^{-2}(j-sk/t)^2}u_j$ and $(\mathsf Tu)_k=\sum_je^{-\pi\alpha^2(tj/s-k)^2}u_j$; with the nearest-index selector $C$ and the diagonal $\mathsf D$, $N=C\mathsf T\mathsf D$ has the summand $u_j$ exactly plus the rest $(N-I)u$.',
              r'The Gaussian resampling argument uses two maps', r'form $((N-I)u)_j$.', frm=[EXP]),
        infer('S5.4.3', r'The identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ and the estimate $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$ are the exact Gaussian facts of Harvey and van der Hoeven.',
              r'The exact Gaussian identity and inverse estimate proved in', r'<2^{-\alpha^2\theta}.', frm=[EXP, P_CONTR]),
        infer('S5.4.4', r'Since $\alpha^2<p$ and $\theta>p/\alpha^4$, $\alpha^2\theta>p/\alpha^2>1$ and $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series.',
              r'Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have', r'by the Neumann series.', frm=[GEO, NORM]),
        infer('S5.4.5', r'Put $\mathsf S\'=\mathsf S/2$, $\mathsf J\'=N^{-1}/2$ and $\mathsf D\'=2^{-(2\alpha^2-2)}\mathsf D$; then $\|\mathsf S\'\|<3/4$, $\|\mathsf J\'\|<7/8$ and $\|\mathsf D\'\|<1$.'.replace("\\'", "@AP@"),
              r"\mathsf S@AP@=\mathsf S/2,", r"\|\mathsf D@AP@\|<1.", frm=[NORM]),
        infer('S5.4.6', r'With $A=\mathsf S\'$ and $B_0=\mathsf D\'\mathsf J\'C$ both contractions, the left inverse $\mathsf DN^{-1}C$ of $\mathsf T$ applied to $\mathsf TP_sF_s=P_tF_t\mathsf S$ gives $\mathsf DN^{-1}CP_tF_t\mathsf S=P_sF_s$, and the normalizations multiply to $2^{-(2\alpha^2-2)}\cdot\frac12\cdot\frac12=2^{-2\alpha^2}$, which proves the identity.'.replace("\\'", "@AP@"),
              r"Now set $A=\mathsf S@AP@$ and $B_0=\mathsf D@AP@\mathsf J@AP@C$.", r"which is \eqref{eq:no-sort-one-dimensional}.", frm=[MAT],
              salient=r'The permutations $P_s$ and $P_t$ stay inside the identity and are never executed, which saves the two sorts per coordinate of the usual implementation.'),
        infer('S5.4.7', r'The ordered numerical maps $\widetilde{\mathsf S}\'$, $\widetilde{\mathsf J}\'$, $\widetilde{\mathsf D}\'$ of Harvey and van der Hoeven have errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$.'.replace("\\'", "@AP@"),
              r'Lemmas~4.8, 4.9 and 4.12 of', r'&O(tp^{1+\delta}).', frm=[P_CONTR]),
        infer('S5.4.8', r'The selector $C$ picks the ordered subsequence $q_0=0<q_1<\cdots<q_{s-1}<t$ with $q_j=\lfloor tj/s+1/2\rfloor$, generated in order with $O(p)$ work per index by carrying counters $tj=sf_j+e_j$, so $C$ takes $O(tp)$ time with zero numerical error.',
              r'For $C$, observe that $q_0=0$, $q_{s-1}<t$, and $q_{j+1}>q_j$,', r'with zero numerical error.', frm=[DIV]),
        infer('S5.4.9', r'Taking $\widetilde A=\widetilde{\mathsf S}\'$ and $\widetilde B_0=\widetilde{\mathsf D}\'\widetilde{\mathsf J}\'C$, contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$, and the costs add to the claimed bound.'.replace("\\'", "@AP@"),
              r'Consequently we may take', r'The costs add to the claimed bound.', frm=[P_CONTR]),
        infer('S5.4.10', r'The original proof implemented $B=P_s^{-1}\mathsf D\'\mathsf J\'CP_t$ with two label-and-sort operations of cost $O(tp\log t)$ each; here these permutations remain in the transform identity and $A,B_0$ use only $C$ and the three arithmetic maps.'.replace("\\'", "@AP@"),
              r'The original proof of Proposition~4.7(ii) implements', r'with all their original truncations.', frm=[SORT]),
        infer('S5.4.11', r'The Neumann evaluation with $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$ terms keeps every iterate $\widetilde v^{(j)}=\widetilde E\widetilde v^{(j-1)}$ in $\mathbb D_p^s$ since $\|\widetilde Ez\|<0.42\|z\|+(p/3)2^{-p}<1$.',
              r'Put $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$.', r'$\mathbb D_p^s$.', frm=[GEO]),
        infer('S5.4.12', r'The $k-1$ calls of $\widetilde E$ with window radius $m=\lceil\sqrt p/(2\alpha)\rceil$ spend $O((\alpha^2+1)tp(1+\sqrt p/\alpha))=O(tp\sqrt p\alpha)$ on scans and additions using $2\le\alpha<\sqrt p$, and outer accumulation $O(tp\alpha^2)$ is within that bound.',
              r'The window of radius $m$ in one $\widetilde E$ call has tape movement', r'within $O(tp\sqrt p\alpha)$.', frm=[BO]),
    ],
)

S5_T = show(
    'S5.5',
    r'For $d$ coordinate lines the tensor product gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, linewise contractions of error less than $dp^2$ and time $O(dTp^{3/2+\delta}\alpha)$ on the padded box, plus $O(Tp\,d^2(1+\ell^\tau))$ for exposing and restoring the lines.',
    'Tensor the one-dimensional identity, apply the one-dimensional maps axis by axis on the zero-padded power-of-two box, charge each axis its lines, and expose each axis by adjacent chunk interchanges.',
    mot('The padded power-of-two box has full size $T$ at every stage, so the axis maps act independently on lines and costs sum over axes; the movement uses the fast interchange.', 'recoverable'),
    [
        infer('S5.5.1', r'If each pair $(s_i,t_i)$ satisfies the one-dimensional lemma, then with $R=\bigotimes P_{s_i}$, $Q=\bigotimes P_{t_i}$, $\mathcal A=\bigotimes A_i$, $\mathcal B_0=\bigotimes B_{0,i}$ and $\gamma=2d\alpha^2$: $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, the maps are contractions, linewise implementations have error below $dp^2$ and total time $O(dTp^{3/2+\delta}\alpha)$.',
              r'Suppose every pair $(s_i,t_i)$, $1\leq i\leq d$, satisfies', r'with a constant independent of $d$.', frm=[]),
        infer('S5.5.2', r'If each $t_i\in\{r/2,r\}$ and the array is kept in the full padded box of $T$ entries of $O(p)$ bits, exposing and restoring all lines costs $O(Tp\,d^2(1+\ell^\tau))$ using the chunk interchange bound.',
              r'If each $t_i\in\{r/2,r\}$ with $r=2^\ell$, the array is kept in the', r'd^2(1+\ell^\tau)\bigr)', frm=[P_CHUNK]),
        infer('S5.5.3', r'To expand axes one at a time, the input is embedded in the padded box with zeros outside $\prod_i[0,s_i)$; after axes $I$ are expanded the valid entries have ranges $[0,t_i)$ for $i\in I$ and $[0,s_i)$ otherwise, and for compression each line invalid on another coordinate is already zero and written as a zero line.',
              r'Tensoring \eqref{eq:no-sort-one-dimensional} proves', r'valid set is the one for $J\cup\{i\}$.', frm=[ARR]),
        infer('S5.5.4', r'Each axis map acts independently on valid lines and is zero elsewhere, so it is a contraction with error below $p^2$; composing $d$ axes gives error below $dp^2$, and at most $T/t_i$ lines call the one-dimensional algorithm so the cost is $\sum_i\frac T{t_i}O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.',
              r'For a fixed axis, the exact map acts independently on its valid lines', r'Both are within the same bound.', frm=[NORM, P_CONTR]),
        infer('S5.5.5', r'To move an axis past its neighbor interchange their $\ell$-bit or $(\ell-1)$-bit fields, unequal widths by peeling the leading bit, so each adjacent interchange costs $O(Tp(1+\ell^\tau))$ and exposing and restoring one axis needs $O(d)$ of them, hence $O(d^2)$ for all axes, exact permutations of the padded box.',
              r'The descriptor records which coordinate each physical address field', r'hence all axes need $O(d^2)$.', frm=[P_CHUNK]),
        infer('S5.5.6', r'Since $t_i\ge r/2$ each tensor map invokes at most $2dT/r$ lines, so $O(p^c)$ setup per line totals $O(dTp^c/r)=o(Tp)$ when $r$ exceeds every fixed power of $p$.',
              r'Since $t_i\geq r/2$, each tensor map invokes at most', r'preparing line boundaries.', frm=[BO]),
    ],
)

S5_BLU = show(
    'S5.6',
    r'For even $t_i$ and chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}T$, i.e. the middle transform with its frequency permutation is a cyclic convolution with the chirp between pointwise chirp phases.',
    'Check that the chirp has period $t_i$, expand the coefficient of $u_{\\boldsymbol k}$ on the right as $\\frac1T\\overline a_{\\boldsymbol j}a_{\\boldsymbol j-\\boldsymbol k}\\overline a_{\\boldsymbol k}$, and recognize the Fourier kernel with the permuted frequency.',
    mot('Writing $jk$ as a combination of squares $j^2,k^2,(j-k)^2$ turns the Fourier kernel into a convolution kernel; the extra permutation $Q$ is absorbed by the choice of the chirp exponent with $s_i$.', 'recoverable'),
    [
        infer('S5.6.1', r'Assuming every $t_i$ is even, define $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$; then $a$ has period $t_i$ in coordinate $i$ and $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}T$.',
              r'assume every $t_i$ is even.', r'{T}.', frm=[P_DFT, ROOTS, P_CONV]),
        infer('S5.6.2', r'Replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\pi is_i(2j_i+t_i)$, an integral multiple of $2\pi i$, and the coefficient of $u_{\boldsymbol k}$ on the right is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, which is the coefficient in $QF_{\boldsymbol t}$ because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.',
              r'Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by', r'from the negative-sign transform.', frm=[ROOTS, MOD]),
    ],
    page=P_BLU, 
)
S5_BLU['page'] = P_BLU
S5_BLU['from'] = [P_DFT, P_CONV, ROOTS, MOD]

S5_PC = show(
    'S5.7',
    r'With $R$ the source permutation and $S=\prod s_i$, $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, so the source permutation cancels between the two forward transforms, the pointwise product and the opposite-sign transform.',
    'Show that a dilation $R_c$ by a unit commutes with the Fourier transform up to inverting $c$, so $RF^+R=F^+$; factor the pointwise product through $R$; and apply the convolution rule $F(u*v)=S\\,Fu\\cdot Fv$.',
    mot('Because the same permutation $R$ acts on both forward transforms and the opposite one undoes it, no sort is ever needed; the proof makes this precise using that each $t_i$ is a unit modulo $s_i$.', 'recoverable'),
    [
        infer('S5.7.1', r'For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ gives $F_q^+R_cz=R_c^{-1}F_q^+z$; since each $t_i$ is a unit modulo $s_i$, tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.',
              r'For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.', r'$RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.', frm=[PRIME, MOD, PERM]),
        infer('S5.7.2', r'A coordinate permutation commutes with pointwise products, so $RF_{\boldsymbol s}^+[R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)]=F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=\frac1SF_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)=\frac{u*v}{S^2}$ using $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$.',
              r'Also $(RF_{\boldsymbol s}u)\mathbin{\cdot}(RF_{\boldsymbol s}v)', r'proving \eqref{eq:source-permutation-cancel}.', frm=[P_DFT, P_BLU],
              salient=r'The permutation $R$ appears twice in the forward transforms and once undoing them, so it cancels exactly rather than approximately.'),
        infer('S5.7.3', r'Complex conjugation of input and output of an algorithm for $RF_{\boldsymbol s}$ gives one for $RF_{\boldsymbol s}^+$, since it commutes with the real permutation $R$ and preserves the disk grid and the norm.',
              r'Finally, conjugation', r'bound.', frm=[CX, NORM]),
    ],
    page=P_PERMC,
)
S5_PC['from'] = [P_DFT, P_BLU, P_GAUSS, PRIME, MOD, PERM, CX, NORM] if False else [P_DFT, P_BLU, PRIME, MOD, PERM, CX, NORM]

S5 = show(
    'S5',
    r'The source Fourier transform $RF_{\boldsymbol s}$ on pairwise coprime prime lengths $s_i$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ on the padded power-of-two box, where the middle transform with its permutation is a chirp convolution, and the source permutation cancels in the convolution without any executed sort.',
    'Use Gaussian resampling to trade the prime-length transform for a power-of-two transform composed with linewise contractions, keep both coordinate permutations inside the transform identity, evaluate the middle factor by a chirp convolution, and show the source permutation cancels between the two forward transforms and the opposite one.',
    mot('Harvey and van der Hoeven sort twice on each coordinate; keeping both permutations in the identity avoids the sorts, which would cost $O(Tp\\log T)$ and thus exactly the $n\\log n$ the paper is trying to beat.', 'explicit',
        r'Its usual implementation sorts twice on each', r'compute that formula directly.'),
    [
        S5_1, S5_2, S5_3,
        S5_D,
        S5_T,
        S5_BLU,
        S5_PC,
    ],
    page=P_GAUSS, frm=[P_DFT, P_CONTR, P_CHUNK, P_BARRIER, EXP, NORM, DYAD, P_CONV],
    adds=[
        B('\\alpha', 'Gaussian width', 'the integer parameter $2\\le\\alpha<\\sqrt p$ controlling the width of the Gaussian weights'),
        B('s_i', 'source length', 'the prime length of the $i$th source axis', 'count'),
        B('t_i', 'padded length', 'the power-of-two length of the $i$th axis of the padded box, slightly larger than $s_i$', 'count'),
    ],
)

# ---------------------------------------------------------------------------------------------
# S6: assembly
# ---------------------------------------------------------------------------------------------
S6_1 = show(
    'S6.1',
    r'Choose precision $p=6b$ with $b=\lceil\log_2n\rceil$, dimension $d=\lfloor b^\epsilon\rfloor$, chunk width $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, record length $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$, and distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, so that $Tp=\Theta(n)$ and every hypothesis of the layer, layout and resampling lemmas holds.',
    'Fix rational exponents satisfying the layer conditions, define the sizes from $n$, verify the comparison bands with explicit constants, choose $\\alpha,\\gamma,\\eta$, and show that enough primes exist near $t_i$ to give $T/2<S<T$ and $\\alpha^4\\theta_i>p$.',
    mot('The resampling lemma needs coprime source lengths just below the powers of two with ratio separation $\\theta_i>p/\\alpha^4$, while the transform lemma needs power-of-two axes of nearly equal size; the explicit choices make all bands hold at once.', 'recoverable'),
    [
        infer('S6.1.1', r'The fixed rational parameters are $\tau=\sigma=1-2^{-50}$, $\beta=\frac12$, $\delta=\frac1{16}$, $\lambda=1-2^{-52}$, $c=2^{-56}$, $\lambda\'=1-2^{-54}$, $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$.'.replace("\\'", "@AP@"),
              r'\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},', r'\kappa=2^{-182}.', frm=[]),
        infer('S6.1.2', r'The layer conditions hold: $\tau(1+c/\beta)<1-31\cdot2^{-55}<\lambda$, $\sigma+\beta(1-\sigma)=1-2^{-51}<\lambda<\lambda\'<1$, and $\epsilon<\frac1{12}$, $\epsilon C_1<1$, $\epsilon(2-\tau)<1-\tau$, $\frac34+\delta+\frac32\epsilon<1$, $\epsilon(1+c)<1$, $\epsilon+\delta<1$.'.replace("\\'", "@AP@"),
              r'The layer conditions hold with room to spare:', r'\epsilon+\delta<1.', frm=[P_LAYER]),
        infer('S6.1.3', r'For large $n$ put $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, take a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, $\ell=\log_2r$, and make $d\ell-\log_2T$ of the axes of length $r/2$ and the others $r$, with the last axis of length $r$.',
              r'large $n$, put', r'choose it as the last axis.', frm=[BIN, DIV]),
        infer('S6.1.4', r'These definitions give $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $r=2^{\Theta(p^{1-\epsilon})}$.',
              r'Tp=\Theta(n),\quad d=\Theta(p^\epsilon),', r'r=2^{\Theta(p^{1-\epsilon})}.', frm=[ASYM]),
        infer('S6.1.5', r'Since $b/2\le\log_2T\le b$, the comparison constants can be fixed at $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$ and $C_\ell=1$, so $r$ exceeds every fixed power of $p$, $K/\log p\to\infty$ and $\ell/K\to\infty$.',
              r'The comparison constants can be fixed for every input length at once.', r'in the layer and transform interfaces.', frm=[]),
        infer('S6.1.6', r'Set $\alpha=\lceil(12d^2b)^{1/4}\rceil$, $\gamma=2d\alpha^2$ and $\eta=1/(4d)$.',
              r'\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,', r'\eta=\frac1{4d}.', frm=[]),
        infer('S6.1.7', r'Then $\alpha\le2(12d^2b)^{1/4}$ and $\gamma<28d^2\sqrt b\le28b^{2/3}$, so $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$; for example $b\ge2^{24}$ implies $\gamma\le b/4$.',
              r'It follows that $2\le\alpha<\sqrt p$ eventually and $\gamma=o(b)$.', r'implies $\gamma\le b/4$.', frm=[]),
        show('S6.1.8',
             r'Distinct odd primes $s_i$ exist with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, they satisfy $T/2<S<T$ and $\alpha^4\theta_i>p$, and all of them together with their search cost $n^{o(1)}$ are generated by the machine.',
             'Quote the prime-interval estimate of Rosser and Schoenfeld in the form of Harvey and van der Hoeven, check it applies to $x=r/2$ and $x=r$, bound the product of the lower bounds by Bernoulli\'s inequality, and search deterministically by trial division.',
             mot('The count $\\eta x/(2\\log x)$ of primes in $(1-2\\eta)x<q\\le(1-\\eta)x$ exceeds $d$ since $x$ is superpolynomially large compared to $d$, which gives enough distinct primes in two disjoint intervals.', 'recoverable'),
             [
                 infer('S6.1.8a', r'For $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes.',
                       r'The prime-interval result', r'contains at least $\eta x/(2\log x)$ primes.', frm=[PRIME]),
                 infer('S6.1.8b', r'Both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$, and the number of primes $x/(8d\log x)$ exceeds $d$ since $\log(8d^2\log x)=O(\log p)=o(\log x)$ so $x>8d^2\log x$ eventually.',
                       r'Thus both $x=r/2$ and $x=r$ satisfy $\log x>8d=2/\eta$.', r'so $x>8d^2\log x$ eventually.', frm=[ASYM]),
                 infer('S6.1.8c', r'The two intervals are disjoint because $(1-\eta)r/2<(1-2\eta)r$ for $\eta<1/4$ and lie above $2$, so distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ and $\gcd(s_i,t_i)=1$ exist.',
                       r'The two intervals are disjoint because', r'(1-2\eta)t_i<s_i\leq(1-\eta)t_i.', frm=[PRIME]),
                 infer('S6.1.8d', r'Multiplying the lower bounds on $s_i$ and applying the strict Bernoulli inequality gives $S/T>(1-\frac1{2d})^d>\frac12$, so with $s_i<t_i$ we get $T/2<S<T$.',
                       r'Put $S=\prod_i s_i$. Multiplying the lower bounds on $s_i$ and', r'$T/2<S<T$.', frm=[],
                       salient=r'The product $S$ of the prime lengths is at least half of the box size $T$, so padding wastes only a constant factor.'),
                 infer('S6.1.8e', r'With $\theta_i=t_i/s_i-1\ge\eta/(1-\eta)>\eta$ one gets $\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\ge6b=p$.',
                       r'Writing $\theta_i=t_i/s_i-1$, the upper bound on $s_i$ gives', r'\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p.', frm=[]),
                 infer('S6.1.8f', r'Every hypothesis of the one-dimensional resampling lemma holds for all sufficiently large input lengths, since also $t_i\le r\le T<8n/b<2^{6b}=2^p$.',
                       r'Thus every hypothesis of Lemma~\ref{lem:no-sort-resampling} holds for', r'all sufficiently large input lengths.', frm=[P_GAUSS]),
                 infer('S6.1.8g', r'The machine finds the primes by scanning the two intervals and trial division through the square root in time $O(dr^{3/2}\operatorname{poly}(p))=n^{o(1)}=o(n)$, and all other scalar setup is polynomial in $p$.',
                       r'The machine finds these primes by scanning the two intervals', r'$n^{o(1)}=o(n)$ time.', frm=[PRIME, SORT]),
             ]),
    ],
    page=P_PARAM, frm=[P_LAYER, P_GAUSS, P_LAYOUT, PRIME, ASYM, BIN, DIV, EXP],
    adds=[
        B('n', 'input length', 'the number of bits of each operand', 'count'),
        B('b', 'digit length', 'the number $b=\\lceil\\log_2n\\rceil$ of bits in each radix digit', 'count'),
        B('T', 'box size', 'the power of two $T\\in[4n/b,8n/b)$ equal to the product of the axis lengths $t_i$', 'count'),
        B('S', 'source size', 'the product $S=\\prod_is_i$ of the prime source lengths', 'count'),
        B('\\epsilon', 'dimension exponent', 'the exponent $2^{-75}$ with $d=\\lfloor b^\\epsilon\\rfloor$'),
    ],
)

S6_2 = show(
    'S6.2',
    r'Writing each input as a polynomial in $2^b$ with $q=\lceil n/b\rceil$ digits makes the integer product the convolution of the digit lists modulo $x^S-1$ with no wraparound, with every coefficient below $2^{3b}$, followed by carry propagation.',
    'Split each operand into $b$-bit digits, observe that the degree of the digit product is below $S$ so the cyclic wrap is vacuous, and bound the coefficients by $q(2^b-1)^2$.',
    mot('Short coefficients make it possible to recover them from an approximate convolution by rounding, since only an error below $1/2$ is required.', 'recoverable'),
    [
        infer('S6.2.1', r'Writing the inputs as polynomials in $2^b$ with $q=\lceil n/b\rceil$ nonnegative digits, their product has degree at most $2q-2<2n/b\le T/2<S$.',
              r'Write the two inputs as polynomials in $2^b$, each with', r'2q-2<2n/b\le T/2<S.', frm=[RADIX, POLY, DIV]),
        infer('S6.2.2', r'So convolution modulo $x^S-1$ has no nonzero wraparound, and every product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$ since $q\le n\le2^b$.',
              r'Thus convolution modulo $x^S-1$ has no nonzero wraparound.', r'since $q\le n\le2^b$.', frm=[P_CONV, SCHOOL]),
    ],
    page=P_RADIX, frm=[RADIX, POLY, DIV, P_CONV, SCHOOL],
)

S6_3 = show(
    'S6.3',
    r'The assignment $\Phi:x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ and $P_i=\prod_{j<i}s_j$ is an algebra isomorphism from $\mathbb C[x]/(x^S-1)$ onto $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$ preserving convolution, and $\Phi$, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$ through triangular controlled shifts and axis reorderings.',
    'Show $\\Phi$ is a well-defined algebra map whose image of $x$ has order $S$ by the Chinese remainder theorem, express its action on mixed-radix indices in a triangular form, and implement the triangular updates as prefix-controlled cyclic shifts after reordering the padded axes with fast chunk interchanges.',
    mot('Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into a multidimensional one; with coordinate powers $\\mu_i$ the change of order is a sequence of controlled cyclic shifts, which are cheap on tape.', 'explicit',
        r'The following map uses that', r'sequence of controlled cyclic shifts.'),
    [
        infer('S6.3.1', r'The assignment $x\mapsto\prod_ix_i^{\mu_i}$ respects $x^S=1$ so it defines an algebra map; the image of $x$ has order $S$ since each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target basis monomials exactly once, hence $\Phi$ is an isomorphism and preserves cyclic convolution.',
              r'Let $s_1,\ldots,s_d$ be the pairwise coprime', r'preserves cyclic convolution.', frm=[PRIME, MOD, P_CONV]),
        infer('S6.3.2', r'Every index $k=\sum_ja_jP_j$ with $0\le a_j<s_j$ maps to axis coordinates $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$ because terms with $j>i$ are divisible by $s_i$ and $\mu_iP_i=1$ modulo $s_i$.',
              r'Every ordinary coefficient index has a unique mixed-radix expression', r'and $\mu_iP_i=1$ modulo $s_i$.', frm=[RADIX, MOD]),
        infer('S6.3.3', r'Numerical order of $k$ is lexicographic order of $(a_d,\dots,a_1)$, so one nested scan of the full box $\prod_i[0,t_i)$ copies the next original record at each valid address ($a_i<s_i$ for all $i$) and writes a zero record elsewhere; deleting the padding uses the same enumeration.',
              r'Numerical order of $k$ is lexicographic order of', r'skipping the record at each invalid address.', frm=[ARR]),
        infer('S6.3.4', r'After reordering the padded axes to $(a_1,\dots,a_d)$, the targets are updated in the order $i=d,d-1,\dots,1$ using the triangular formula, so when target $i$ is updated none of its lower-index controls has yet changed.',
              r'Now reorder the complete padded axes to $(a_1,\ldots,a_d)$.', r'required by the formula.', frm=[]),
        infer('S6.3.5', r'On a fixed control prefix, rotating the valid target interval $[0,s_i)$ by the offset and fixing $[s_i,t_i)$ is a bijection of the padded set that preserves the valid set and its complement, so zero padding remains zero; the inverse subtracts the same expression from the recovered lower coordinates.',
              r'To specify the action on padded addresses, let', r'zero padding remains zero after every step.', frm=[PERM, P_CSHIFT]),
        infer('S6.3.6', r'Each triangular update is a prefix-controlled cyclic shift: prepare the offset, split the valid target interval into two pieces and merge in the opposite order; offsets for the at most $T/t_i$ control prefixes cost $O(dTp^C/r)=o(Tp)$ since $t_i\ge r/2$ and $r$ exceeds every fixed power of $p$.',
              r'Each triangular update is a prefix-controlled cyclic shift.', r'every fixed power of $p$.', frm=[P_CSHIFT]),
        infer('S6.3.7', r'Axes have widths $\ell$ or $\ell-1$; exchanging two adjacent axes of unequal width peels the leading bit and uses the equal-width chunk swap, and reversing all axes takes $O(d^2)$ moves, so $\Phi$, its inverse and padding cost $O(Tp\,d^2(1+\ell^\tau))$.',
              r'The axis widths are $\ell$ or $\ell-1$.', r'O\bigl(Tp\,d^2(1+\ell^\tau)\bigr).', frm=[P_CHUNK]),
    ],
    page=P_CRT, frm=[PRIME, MOD, RADIX, ARR, PERM, P_CONV, P_CSHIFT, P_CHUNK],
)

S6_4 = show(
    'S6.4',
    r'With $\zeta=e^{\pi i/r}$, multiplying coefficient $k$ by $\zeta^k$ maps cyclic convolution on the last axis (modulo $x_d^r-1$) onto convolution modulo $y^r+1$, untwisting recovers the cyclic result, and the normalized complex cyclic convolution $\mathcal M_{\mathbb C}(f,g)=(f*g)/T$ is computed from $\mathcal M_r$ with error below $6TL\,2^{-p}$.',
    'Define the diagonal isomorphism $x_d\\mapsto\\zeta y$, check that the wrap sign $(-1)^h$ cancels against $\\zeta^{rh}=(-1)^h$, identify the last coordinate with the polynomial suffix so no payload is moved, and conjugate $\\mathcal M_r$ by the twists.',
    mot('The synthetic transforms apply to the negacyclic ring while the chirp identity needs ordinary cyclic convolution on every axis; a phase twist of the coefficients converts one to the other at the cost of one pointwise multiplication per line.', 'recoverable'),
    [
        infer('S6.4.1', r'The map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R$, $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ is well defined since $(\zeta y)^r=(-1)(-1)=1$; on the bases $(x_d^k)$ and $(y^k)$ it multiplies coefficient $k$ by $\zeta^k$, so it is an isomorphism with inverse multiplying by $\zeta^{-k}$, and both preserve the coefficient sup norm.',
              r'Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and', r'$\zeta^{-k}$.', frm=[P_NEG, ROOTS]),
        infer('S6.4.2', r'For $k+l=j+hr$ with $h\in\{0,1\}$, a product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.',
              r'For an explicit check on the wrap, write $k+l=j+hr$, where', r'with the correct sign.', frm=[ROOTS],
              salient=r'The sign $(-1)^h$ picked up by the negacyclic wrap is cancelled exactly by $\zeta^{rh}=(-1)^h$ because $\zeta^r=-1$.'),
        infer('S6.4.3', r'Identifying an array with $M=T/r$ records in $\mathcal R$ by $\iota$ and writing $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$, normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=\frac{f*g}T$.',
              r'Consequently, with $\mathcal M_r$ from', r'=\frac{f*g}{T}.', frm=[P_NRC] if False else []),
        infer('S6.4.4', r'Since $D_\pm$ and $\iota^{\pm1}$ are isometries, $\mathcal M_{\mathbb C}$ is also a bilinear contraction.',
              r'Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$,', r'is also a bilinear contraction.', frm=[NORM]),
        infer('S6.4.5', r'With $w_{\rm c}=p+2\le2p$ the scalar and synthetic component formats coincide and the last coordinate is already the contiguous polynomial suffix, so $\iota$ and $\iota^{-1}$ change only the shape descriptor.',
              r'For the tape representation, use the scalar format of', r'require no payload movement when these component formats agree.', frm=[DYAD]),
        infer('S6.4.6', r'The computed complex convolution forms $f\'=Q_p(\widetilde\theta^+\cdot f)$, $g\'=Q_p(\widetilde\theta^+\cdot g)$, $h\'=\widetilde{\mathcal M}_r(\iota f\',\iota g\')$ and returns $Q_p(\widetilde\theta^-\cdot\iota^{-1}h\')$, with twist factors approximating $\zeta^{\pm k}$ to within $2\cdot2^{-p}$ in time $O(p^{1+\delta})$ each.'.replace("\\'", "@AP@"),
              r'For $0\le k<r$, obtain disk-grid approximations', r'\iota^{-1}h@AP@\right).', frm=[EXP]),
        infer('S6.4.7', r'Each phase product is computed exactly as a dyadic product on $O(p)$-bit numerators and truncated, costing $O(p^{1+\delta})$ per coefficient and $O(Tp^{1+\delta})$ in total even when every factor is generated anew.',
              r'Each phase product is computed exactly as a dyadic product before', r'twist cost $O(Tp^{1+\delta})$.', frm=[DYAD]),
    ],
    page=P_TWIST, frm=[P_NEG, P_CONV, ROOTS, NORM, EXP, DYAD],
)

S6_5 = show(
    'S6.5',
    r'The approximate source transform $\widetilde{\mathscr F}$ applies linewise $\widetilde{\mathcal A}$, the computed chirp transform $\widetilde{\mathscr C}$ (a chirp convolution of length $T$ on the padded power-of-two box), linewise $\widetilde{\mathcal B}_0$ and an exact scaling by $2^\gamma$, and its exact counterpart is $RF_{\boldsymbol s}$ on the prime-length source.',
    'Evaluate the middle factor $QF_{\\boldsymbol t}$ through the chirp identity and the computed complex convolution, with exact multiplication by the unit-modulus phases, then compose with the Gaussian maps and the exact scaling.',
    mot('Replacing every numerical routine by the exact map it approximates identifies the exact counterpart as $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$ by the resampling identity.', 'recoverable'),
    [
        infer('S6.5.1', r'The chirp numerator at tensor address $\boldsymbol j$ is computed modulo $2r$ as $-\sum_is_ij_i^2(r/t_i)$ with $r/t_i\in\{1,2\}$ and $O(p)$-bit integers.',
              r'We next use the complex convolution to evaluate the middle factor', r'-\sum_i s_i j_i^2(r/t_i)\pmod{2r}.', frm=[P_BLU]),
        infer('S6.5.2', r'Chirp construction costs $O(Tdp^{1+\delta})$ in total, since squares and products use the integer multiplier, exponentials cost $O(p^{1+\delta})$, and the cost includes the scan of the axis descriptors at every coefficient.',
              r'All integers have $O(p)$ bits and $r/t_i\in\{1,2\}$.', r'costs $O(Td p^{1+\delta})$ in total.', frm=[P_BARRIER]),
        infer('S6.5.3', r'With the disk-grid array $\widetilde a$ approximating the chirp, a target tensor $x$ of norm at most $.6$ gives $x_0=Q_p(\overline{\widetilde a}\cdot x)$, $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$ and $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$.',
              r'Let $\widetilde a$ be the resulting disk-grid array, so', r'after the first endpoint phase.', frm=[P_TWIST]),
        infer('S6.5.4', r'Replacing the approximations by exact phases and exact convolution gives $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$, and $\|x\|_\infty\le.6$ implies $\|x_0\|_\infty\le.6$, supplying the smaller operand required by the computed convolution.',
              r'Replacing the approximations', r'required by the computed convolution.', frm=[P_BLU]),
        infer('S6.5.5', r'For a source disk-grid tensor of norm at most $.5$, $\widetilde{\mathscr F}$ applies linewise $\mathcal A$, the computed chirp transform, linewise $\mathcal B_0$ and multiplies the grid numerators exactly by $2^\gamma$, with exact counterpart $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.',
              r'For a source disk-grid tensor of norm at most $.5$, write', r'=RF_{\boldsymbol s}.', frm=[P_GAUSS]),
        infer('S6.5.6', r'The source arrays sit in the padded box with zeros outside the valid coordinates; appending $\gamma$ zero bits scales a numerator exactly and, since the scaled coordinates stay in $\mathbb D_p$, a scan removes only sign extension at cost $O(T(w_{\rm c}+\gamma))=O(Tp)$.',
              r'stored in the padded power-of-two box, with zeros outside the valid', r'leaves the padded zero records zero.', frm=[DYAD]),
        infer('S6.5.7', r'The opposite-sign procedure is $\widetilde{\mathscr F}^+(z)=\overline{\widetilde{\mathscr F}(\overline z)}$ with exact counterpart $RF_{\boldsymbol s}^+$ by the chirp and permutation lemma.',
              r'Define the opposite-sign procedure by', r'Lemma~\ref{lem:chirp-permutation}.', frm=[P_PERMC]),
    ],
    page=P_TENS, frm=[P_GAUSS, P_BLU, P_PERMC, P_TWIST, P_NRC, P_PARAM, DYAD],
)

S6_ALG = show(
    'S6.6',
    r'The multiplication algorithm converts the digits to the grid, applies $\Phi$, computes two forward source transforms, a rounded pointwise product, one opposite transform with scaling by $S$, a second scaling by $2^{2b+4}S$, rounds, applies $\Phi^{-1}$ and propagates carries to output the $2n$-bit product.',
    'List the algorithm step by step, with each exact scaling undoing a specific normalization, so that the exact counterpart of the result is the integer coefficient convolution.',
    mot('The three source transforms and the exact scalings by $S$ and $2^{2b+4}$ undo the normalizations $S^{-2}$ of the transform pair and the digit scale $2^{-b-2}$ twice.', 'recoverable'),
    [
        infer('S6.6.1', r'Each operand is read backward from its least significant end in groups of $b$ bits to give the radix-$2^b$ digits $a_j$, each written as the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word followed by a zero imaginary word, and $S-q$ zero records are appended; input conversion costs $O(n+Sp)=O(Tp)$.',
              r'Read each stored operand backward from its least significant end in groups', r'$O(n+Sp)=O(Tp)$;', frm=[P_RADIX, P_FIXED]),
        infer('S6.6.2', r'Step 1 applies the coefficient-address map $\Phi$ with its padded layout, giving source arrays $u,v$ with exact $p$-bit grid coefficients of norm less than $1/4$.',
              r'\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain', r'of norm less than $1/4$.', frm=[P_CRT]),
        infer('S6.6.3', r'Step 2 computes $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.',
              r'\item Compute $\widetilde{\mathscr F}(u)$ and', r'$\widetilde{\mathscr F}(v)$.', frm=[P_TENS]),
        infer('S6.6.4', r'Step 3 multiplies corresponding complex coefficients exactly and truncates each real and imaginary part toward zero to $p$ fractional bits, giving the source array $z$.',
              r'\item Multiply corresponding complex coefficients exactly and truncate', r'Denote the resulting source array by $z$.', frm=[P_FIXED]),
        infer('S6.6.5', r'Step 4 computes $\widetilde{\mathscr F}^+(z)$ and multiplies its grid numerators exactly by $S$, denoting the represented array by $\widetilde w$ in signed width $w_{\rm c}+b$.',
              r'\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid', r'dyadic array by $\widetilde w$.', frm=[P_TENS]),
        infer('S6.6.6', r'Step 5 multiplies by $2^{2b+4}S$, rounds the real values to the nearest integers, writes each rounded coefficient in a $(3b+1)$-bit word (zero at padded addresses) and applies $\Phi^{-1}$ with removal of padding.',
              r'\item Multiply the grid numerators of $\widetilde w$ exactly by', r'to restore the ordinary coefficient order.', frm=[P_CRT]),
        infer('S6.6.7', r'Step 6 propagates radix-$2^b$ carries in increasing coefficient order, writes the bits from least to most significant on a work tape and reverses that stream to output exactly $2n$ bits.',
              r'\item Propagate radix-$2^b$ carries in increasing coefficient order.', r'most-significant-first order.', frm=[P_RADIX]),
        infer('S6.6.8', r'The two occurrences of $S$ undo different normalizations: the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$ whose inverse image under $\Phi$ is the original integer coefficient convolution.',
              r'The two occurrences of $S$ in this algorithm undo different', r'integer coefficient convolution.', frm=[P_PERMC, P_CRT]),
    ],
)

S6_PREC = show(
    'S6.7',
    r'The recovered convolution coefficients have error below $448b\,2^{-3b/4}<1/2$ and lie in $[0,2^{3b})$, so rounding and carry propagation give the exact $2n$-bit product.',
    'Propagate disk margins and errors stage by stage through twist, ring convolution, chirp transform and source transform by contraction and bilinear-contraction estimates, combine them through the product and the opposite transform, scale by the known normalizations and bound the final error.',
    mot('Each exact map is a contraction and each computed map differs from it by a bounded multiple of $2^{-p}$, so the errors add stage by stage; the precision $p=6b$ is chosen so that the amplification by $2^\\gamma T^2$ and the output scale $2^{2b+4}S$ still leaves less than $1/2$.', 'recoverable'),
    [
        infer('S6.7.1', r'With $h_p=2^{-p}$ an error of $a$ means absolute error less than $ah_p$; a linear contraction propagates input error without increase, and for a bilinear contraction $\|\mathcal M(f\',g\')-\mathcal M(f,g)\|\le\|f\'-f\|\|g\'\|+\|f\|\|g\'-g\|$, so the two errors add when all four operands are in the disk.'.replace("\\'", "@AP@"),
              r'Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this', r'their two errors therefore add.', frm=[P_CONTR, NORM]),
        infer('S6.7.2', r'For a unit phase $e$ with disk-grid approximation $|\widetilde e-e|<2h_p$ and a disk operand $x$, $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$ and $\|Q_p(\widetilde ex)\|\le\|x\|$, which preserves smaller operand norms through twists and endpoint phases.',
              r'We also need the norm as well as the error of a computed phase product.', r'coordinatewise for arrays of phases.', frm=[NORM]),
        infer('S6.7.3', r'Two normalized synthetic forwards, pointwise product divided by $r$ and the normalized opposite give $(f*g)/(rM^2)$; the three transform errors and the product truncation total less than $3L+2$, so the returned normalized convolution has error $E_{\rm ring}:=M(3L+2)<5TL$, and for an operand of norm at most $.7$ the output has norm below $.7+5TLh_p<.701$.',
              r'For disk-grid ring arrays $f,g$, put $M=T/r$.', r'without clipping the output.', frm=[P_NRC]),
        infer('S6.7.4', r'The twisted complex convolution inherits the input twist errors (each below $4$), the ring error $E_{\rm ring}$ and the output untwist (below $4$): $\|\widetilde{\mathcal M}_{\mathbb C}(f,g)-\mathcal M_{\mathbb C}(f,g)\|<(E_{\rm ring}+4+4+4)h_p<6TLh_p$, and the result is a disk grid array.',
              r'Consider now $\widetilde{\mathcal M}_{\mathbb C}(f,g)$ for disk grid', r'<6TLh_p.', frm=[P_TWIST]),
        infer('S6.7.5', r'For a chirp input $x$ with $\|x\|\le.6$ the kernel approximation contributes less than $2$, the first endpoint phase less than $4$, the computed convolution less than $6TL$ and the last endpoint phase less than $4$, so $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p$ and $\|\widetilde{\mathscr C}(x)\|<.701$.',
              r'For a disk-grid chirp input $x$ with $\|x\|\le.6$, the previously', r'<8TLh_p.', frm=[P_TENS]),
        infer('S6.7.6', r'For a source input of norm at most $.5$ the computed expansion has error below $dp^2$ and norm below $.51$, and inserting the exact contractions $\mathcal A$, $QF_{\boldsymbol t}$, $\mathcal B_0$ gives error below $2dp^2+8TL$ before the scale and, after multiplying by $2^\gamma$, below $E_sh_p$ with $E_s=9\cdot2^\gamma TL$ since $2dp^2<TL$ eventually.',
              r'Finally let the input to a source transform have norm at most $.5$.', r'because $2dp^2<TL$ eventually.', frm=[P_GAUSS]),
        infer('S6.7.7', r'The exact source transform is a contraction, so the scaled approximation has norm at most $.5+E_sh_p<.501$ and its exact numerator scaling leaves a disk-grid output without clipping; conjugation gives the same for the opposite procedure, and one fixed cutoff, for example $b\ge2^{24}$, makes all these margins smaller than $10^{-3}$.',
              r'The exact source transform', r'smaller than $10^{-3}$.', frm=[P_PERMC]),
        infer('S6.7.8', r'The scaled radix digits in $u,v$ have norm less than $1/4$, so the exact transforms $U=RF_{\boldsymbol s}u$, $V_1=RF_{\boldsymbol s}v$ have norm less than $1/4$ and the computed ones less than $.26$; hence $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm at most $.26^2<.5$.',
              r'The scaled radix digits in $u,v$ are exact $p$-bit grid values of norm', r'norm at most $.26^2<.5$.', frm=[P_TENS]),
        infer('S6.7.9', r'From $\widetilde U\widetilde V_1-UV_1=(\widetilde U-U)\widetilde V_1+U(\widetilde V_1-V_1)$ with $\widetilde V_1,U$ in the disk, the product has error below $2E_sh_p$ and truncation adds less than $2h_p$, so $\|z-U\cdot V_1\|<(2E_s+2)h_p$.',
              r'To estimate its error, write', r'$\|z-U\cdot V_1\|<(2E_s+2)h_p$.', frm=[]),
        infer('S6.7.10', r'With $G=RF_{\boldsymbol s}^+$ the exact opposite contraction, $G(U\cdot V_1)=(u*v)/S^2$ by the permutation cancellation, and inserting $G$ at the computed input gives $\|\widetilde{\mathscr F}^+(z)-G(U\cdot V_1)\|\le\|\widetilde{\mathscr F}^+(z)-Gz\|+\|G(z-U\cdot V_1)\|<(3E_s+2)h_p$.',
              r'Let $G:=RF_{\boldsymbol s}^+$ be the exact opposite contraction.', r'<(3E_s+2)h_p.', frm=[P_PERMC]),
        infer('S6.7.11', r'The first exact multiplication by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$ with error below $E_wh_p$, $E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L$, and each coefficient of $w$ is an average of $S$ products so $\|w\|<1/16$ and $\|\widetilde w\|<1/16+E_wh_p<1/16+10^{-3}<1$.',
              r'The first exact numerator multiplication by $S$ gives', r'<1/16+10^{-3}<1.', frm=[]),
        infer('S6.7.12', r'In tensor order the unscaled integer coefficient array is $2^{2b+4}Sw$, where $S$ reverses the normalization still present in $w$ and $2^{2b+4}$ reverses the two input scales.',
              r'In tensor order, the unscaled integer coefficient array is', r'$2^{2b+4}S w$.', frm=[]),
        infer('S6.7.13', r'Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\frac12$, using $\gamma\le b/4$.',
              r'Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than', r'<\frac12.', frm=[ASYM],
              salient=r'Only $2^{-b}$ of precision is left after the amplification by $2^{\gamma}T^2S\,2^{2b+4}$ against $2^{-6b}$, because $p=6b$ was chosen exactly to absorb $T^3\approx2^{3b}$ and the digit scale $2^{4b}$; and $\gamma=o(b)$ is what allows Gaussian resampling to be paid for.'),
        infer('S6.7.14', r'The true coefficients are integers, so with error below $1/2$ the nearest integer to $H_j/2^p$ is the unique correct coefficient, and by the capacity bound it lies in $[0,2^{3b})$ and fits a signed $(3b+1)$-bit word.',
              r'The true coefficients are real integers.', r'that value the unique correct coefficient.', frm=[DIV]),
        infer('S6.7.15', r'To round $H_j/2^p$ recover the real magnitude, inspect its low $p$ bits and apply the rounding carry with the sign restored; serialization of the rounded coefficients costs $O(Tp)$ in total.',
              r'The established integer multiplier performs the two products by $S$ in', r'This serialization costs $O(Tp)$ in total.', frm=[P_BARRIER, BIN]),
        infer('S6.7.16', r'With $Q_0=2^b$ and $k_0=0$, $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$, the carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$ since $c_j+k_j\le qQ_0(Q_0-1)$, and the invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ fixes the first $j$ radix digits of the product.',
              r'To propagate carries, let $Q_0=2^b$.', r'the remaining positions.', frm=[DIV, RADIX, INDUCT]),
        infer('S6.7.17', r'After $\Phi^{-1}$ the coefficients occur in increasing index, so the carry scan proceeds from least to most significant with $O(b)$ bits and steps per coefficient; the stream has length $O(Sb)=O(Tp)$, a charged linear reversal gives most-significant-first order, and all bits above position $2n-1$ are zero since the product is less than $2^{2n}$.',
              r'After $\Phi^{-1}$ the coefficients occur in increasing ordinary index,', r'output rule.', frm=[BIN]),
    ],
    page=P_PREC, frm=[P_CONTR, NORM, P_NRC, P_TWIST, P_TENS, P_PERMC, P_RADIX, P_CRT, ASYM, DIV, INDUCT, BIN, RADIX, P_BARRIER],
    adds=[
        B('h_p', 'grid step', 'the grid spacing $h_p=2^{-p}$ in which errors are measured'),
        B('L', 'log box size', 'the integer $L=\\log_2T$', 'count'),
    ],
)

S6_COST = show(
    'S6.8',
    r'Dividing every cost by $V=Tp$ gives seven dominant normalized costs, each at most $p^{1-2\kappa}$, the smallest margin $2^{-181}=2\kappa$ coming from the chunk-exchange term $pK^{\tau-1}$, so the total time is $O(Tp\cdot p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ with $\kappa=2^{-182}$.',
    'Tabulate the cost of each operation relative to $V=Tp$, convert every row to a power of $p$ using $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$, $\\alpha=\\Theta(p^{1/4+\\epsilon/2})$, compare each exponent with $1$ to obtain margins $g_i$, charge setup and the exceptional streams, and absorb any fixed power of $\\log p$ by the slack.',
    mot('A power saving needs each row of the cost table to be at most $p^{1-\\text{margin}}$ for a positive margin; the smallest margin $g_2=\\epsilon c(1-\\tau)$ is a product of three tiny exponents and fixes $\\kappa=g_{\\min}/2$.', 'recoverable'),
    [
        infer('S6.8.1', r'With $V=Tp=\Theta(n)$ a full padded array has $\Theta(V)$ stored bits, and the table lists costs after division by $V$ with a fixed number of repeated transforms and convolutions included in its constants.',
              r'For the cost calculation put $V=Tp=\Theta(n)$.', r'is included in its constants.', frm=[P_PARAM]),
        infer('S6.8.2', r'Normalized costs are $dK$ (power $\epsilon(1+c)$) for prefix moves and individual rounds, $pK^{\tau-1}$ (power $1-\epsilon c(1-\tau)$) for chunk exchanges, $\ell d^{\lambda@AP@}$ (power $1-\epsilon(1-\lambda@AP@)$) for butterfly rounds, $d^2(1+\ell^\tau)$ (power $\tau+\epsilon(2-\tau)$) for CRT and axis layouts, $dp^{1/2+\delta}\alpha$ (power $3/4+\delta+3\epsilon/2$) for Gaussian line maps, $dp^\delta$ (power $\epsilon+\delta$) for chirps and twists, and $\log(rp)$ (power $1-\epsilon$) for packed polynomial products; the remaining rows are absorbed.',
              r'Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\', r'Input, padding, carries and output & $1$ & absorbed above\\', frm=[P_LAYOUT, P_LAYER, P_CRT, P_GAUSS, P_TENS, P_NRC]),
        infer('S6.8.3', r'The margins below one are $g_1=1-\epsilon(1+c)$, $g_2=\epsilon c(1-\tau)$, $g_3=\epsilon(1-\lambda@AP@)$, $g_4=1-\tau-\epsilon(2-\tau)$, $g_5=1/4-\delta-3\epsilon/2$, $g_6=1-\delta-\epsilon$ and $g_7=\epsilon$.',
              r'The seven dominant powers in Table~\ref{tab:costs} have the following', r'g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon.', frm=[P_PARAM]),
        infer('S6.8.4', r'Direct substitution gives $g_1>\frac12$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>\frac18$, $g_6>\frac12$ and $g_7=2^{-75}$.',
              r'Direct substitution gives', r'g_7=2^{-75}.', frm=[]),
        infer('S6.8.5', r'Thus $\min_ig_i=2^{-181}=2\kappa$ and this explicit slack covers any remaining fixed power of $\log p$.',
              r'Thus $\min_i g_i=2^{-181}=2\kappa$.', r'any remaining fixed power of $\log p$.', frm=[],
              salient=r'The smallest margin is $g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}$, so $\kappa=2^{-182}$ is determined by the chunk exchange term $pK^{\tau-1}$ through the three tiny exponents $\epsilon$, $c$ and $1-\tau$.'),
        infer('S6.8.6', r'The term $d^2$ is absorbed by $d^2\ell^\tau$ and $\log(rp)=O(p^{1-\epsilon}+\log p)=O(p^{1-\epsilon})$.',
              r'Here $d^2$ is absorbed by $d^2\ell^\tau$, and', r'$\log(rp)=O(p^{1-\epsilon}+\log p)=O(p^{1-\epsilon})$.', frm=[ASYM]),
        infer('S6.8.7', r'The first three rows are the terms of the transform cost; the layout uses $O(p/K)$ exchanges of width-$K$ chunks because $d\ell=O(p)$, each costing $O(VK^\tau)$, so the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$, a power $1-\epsilon c(1-\tau)$ of $p$ since $K=\Theta(p^{\epsilon c})$.',
              r'The first three rows are the terms in', r'O(p/K)\,K^\tau=O(pK^{\tau-1}).', frm=[P_LAYOUT, P_CHUNK]),
        infer('S6.8.8', r'The at most $\ell$ simultaneous rounds each cost $O(Vd^{\lambda@AP@})$, already including the binary basis changes, deterministic repair, row padding and removal, all base-$m$ groups and fixed-tape cleanup, giving $\ell d^{\lambda@AP@}$ with power $1-\epsilon(1-\lambda@AP@)$.',
              r'For the at most $\ell$ simultaneous rounds,', r'fixed-tape cleanup.', frm=[P_LAYER]),
        infer('S6.8.9', r'Axis exposure and restoration take $O(d^2)$ adjacent axis moves, each $O(V(1+\ell^\tau))$ by peeling a single excess bit, exchanging equal-width parts and restoring the bit; the $d$ CRT rotations copy intervals in $O(dV)$ with offset setup $o(Tp)$.',
              r'Axis exposure and restoration require $O(d^2)$ adjacent axis moves.', r'using at most $T/t_i$ control prefixes for target $i$.', frm=[P_CRT, P_CHUNK]),
        infer('S6.8.10', r'Axis $i$ has at most $T/t_i$ processed lines, so Gaussian line maps cost $\sum_i\frac T{t_i}O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$ and, divided by $V=Tp$ with $\alpha=\Theta(p^{1/4+\epsilon/2})$, give $dp^{1/2+\delta}\alpha$ of power $3/4+\delta+3\epsilon/2$.',
              r'For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines.', r'explains its displayed power of $p$.', frm=[P_GAUSS]),
        infer('S6.8.11', r'Chirp numerators have $O(p)$ bits computed modulo $2r$ as sums of $d$ terms, using the integer multiplier for squares and products and then exponentials, in $O(dp^{1+\delta})$ per entry; the smaller twist and scalar products fit the same row and the two final products by $S$ cost $O(p\log p)$ per entry, listed separately.',
              r'Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as', r'as listed separately.', frm=[P_TENS, P_BARRIER]),
        infer('S6.8.12', r'There are $T/r$ polynomial records in each pointwise ring product, and four integer products on $O(rp)$ bits per record cost $O(Tp\log(rp))$ in total using the earlier multiplier on records of length $O(rp)=o(n)$, not the improved algorithm being constructed.',
              r'polynomial records in each pointwise ring product.', r'being constructed.', frm=[P_PACK, P_BARRIER]),
        show('S6.8.13',
             r'Setup at recursion nodes, descriptor work per record and line, and the sorting of exceptional streams all cost $o(Tp)$, so they do not affect the power of $p$.',
             'Charge setup at each visit of the layer and layout recursions, which number at most $p^A$, descriptor work per polynomial record against the $\\Theta(rp)$ bits of the record, setup per Gaussian line against $2dT/r$ lines, and bound the exceptional stream by its bad fraction.',
             mot('Because $r$ exceeds every fixed power of $p$ each polynomial record or Gaussian line absorbs any fixed polynomial setup cost, and the bad-address fraction decays like $2^{-K}$ with $K\\to\\infty$.', 'recoverable'),
             [
                 infer('S6.8.13a', r'The layer and layout recursions have constant branching and depth $O(\log p)$ and polynomially many rounds and groups, so their total visits are at most $p^A$; descriptor setup of $p^C$ per visit costs $p^{A+C}=o(Tp)$.',
                       r'We next separate setup at recursion nodes from work repeated for every', r'$p^{A+C}=o(Tp)$.', frm=[P_LAYER, P_LAYOUT]),
                 infer('S6.8.13b', r'At a visit processing polynomial records there are $O(T/r)$ records, so $O(p^C)$ work per record costs $O(Tp^{A+C}/r)=o(Tp)$, and setup before each Gaussian line costs $O(dTp^C/r)=o(Tp)$ since there are at most $2dT/r$ lines per tensor map.',
                       r'At a layer or synthetic-transform visit that processes polynomial', r'that $r$ exceeds every fixed power of $p$.', frm=[P_GAUSS]),
                 infer('S6.8.13c', r'For one packed change of basis the bad-address fraction is $O(d2^{-K})$, independent of the payload, so the compact exceptional stream has length $O(V_{\rm call}d2^{-K})$, stable bit sorting makes $O(p)$ scans of it costing $O(V_{\rm call}dp2^{-K})$ per call, and over at most $p^A$ visits the total is $O(Vp^{A\'}2^{-K})=o(V)$ since $K=\Theta(p^{\epsilon c})$; this is a deterministic worst-case bound.'.replace("\\'", "@AP@"),
                       r'For one packed change of basis, let $V_{\rm call}$ be its current', r'a deterministic worst-case bound.', frm=[P_PACKED, SORT],
                       salient=r'The exceptional addresses are rare, a fraction $d2^{-K}$ of all addresses, and independent of the data, so the repair by sorting is worst-case cheap.'),
                 infer('S6.8.13d', r'All role, arithmetic and stack tapes form fixed finite families, a child parks and restores only its parent\'s streams, so no operation rescans parked ancestors; global setup and prime search cost $o(V)$.'.replace("\\'", "@AP@"),
                       r'Finally, all role, arithmetic, and stack tapes form fixed finite', r'proved earlier.', frm=[P_PWI, TM]),
             ]),
        infer('S6.8.14', r'Each of the seven displayed powers is at most $1-2\kappa$ and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.',
              r'Each of the seven displayed powers is at most $1-2\kappa$ by', r'O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).', frm=[ASYM, BO]),
        infer('S6.8.15', r'Below a fixed cutoff beyond all size, precision, margin and layout conditions schoolbook multiplication is used; the finitely many smaller lengths are included by enlarging the constant, giving one fixed-alphabet fixed-tape deterministic machine of worst-case time $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.',
              r'Fix one cutoff beyond all the size, precision, margin and layout', r'the required $2n$-bit product.', frm=[SCHOOL, TM]),
    ],
    page=P_COST, frm=[P_PARAM, P_LAYOUT, P_LAYER, P_CHUNK, P_CRT, P_GAUSS, P_TENS, P_NRC, P_PACK, P_PACKED, P_PWI, P_BARRIER, ASYM, BO, SORT, SCHOOL, TM],
)

S6 = show(
    'S6',
    r'Combining digit conversion, the Chinese-remainder map $\Phi$, two forward source transforms, a pointwise product, one opposite transform, exact rescalings, rounding, $\Phi^{-1}$ and carry propagation computes the exact $2n$-bit product with all errors below $1/2$, in total time $O(n(\lg n)^{1-\kappa})$.',
    'Choose parameters so that the padded box has $Tp=\Theta(n)$ and all hypotheses hold, express the product as a cyclic convolution, convert it with the Chinese remainder theorem to a convolution on distinct prime axes, compute it by source transforms built from resampling and chirp convolutions, show the recovered coefficients round to the exact integers, and add the costs.',
    mot('Each preceding page supplies one piece of this reduction (Figure 1 of the paper), and the proof of exactness and the cost table require explicit parameters fixed first.', 'recoverable'),
    [
        S6_1, S6_2, S6_3, S6_4, S6_5, S6_ALG, S6_PREC, S6_COST,
    ],
    page=P_ALG, frm=[P_RADIX, P_CRT, P_TWIST, P_TENS, P_NRC, P_PREC, P_PARAM, SUB],
)

# ---------------------------------------------------------------------------------------------
# ROOT
# ---------------------------------------------------------------------------------------------
ROOT = show(
    'S0',
    r'There is a deterministic multitape Turing machine multiplying two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, which disproves the $n\log n$ optimality conjecture in this model.',
    'Build the multiplier bottom up: locate the $n\\log n$ barrier, obtain two tape procedures with power savings from one rank-saving network recursion, use them to evaluate synthetic transforms and ring convolutions, turn the integer product into such convolutions by Chinese remaindering, Gaussian resampling and chirps, then assemble the algorithm, prove exact recovery and total the cost.',
    mot('Plain transform levels over $\\Theta(n)$ stored bits cost $\\Theta(n\\log n)$ by scanning, so a power saving needs savings in both movement and arithmetic, and each later page supplies one saving or accounts for a change of representation.', 'explicit',
        r'We therefore need savings in both movement and arithmetic.'),
    [S1, S2, S3, S4, S5, S6],
    page=P_MAIN, frm=[TM, BO, SUB, ASYM],
    adds=[B('V', 'logical volume', 'the number of stored data bits of the array an operation acts on', 'count')],
)


def fix(o):
    if isinstance(o, str):
        return o.replace('@AP@', "'").replace("\\'", "'")
    if isinstance(o, list):
        return [fix(x) for x in o]
    if isinstance(o, dict):
        return {k: fix(v) for k, v in o.items()}
    return o


if __name__ == '__main__':
    tree = fix(ROOT)
    out = ROOTDIR + '/exegenius/tasks/0003-argument.answer.json'
    json.dump({'root': tree}, open(out, 'w'), indent=1, ensure_ascii=False)
    cnt = [0]
    def walk(n):
        cnt[0] += 1
        for c in n.get('children', []):
            walk(c)
    walk(tree)
    print('nodes', cnt[0])
    for e in ERRS:
        print('ERR', e)
    if len(sys.argv) > 1:
        for l in LOG:
            print(l)
