from lib import *
from t_s1 import *

# ---------------------------------------------------------------- explicit tau (K.2)
def explicit_tau():
    return infer(
        'K.2',
        r"""For the bit network the exact relative deficit $\eta_{\rm b}$ exceeds $20\cdot2^{-50}$ and $\log m<20$ because $m<2^{20}$, so $\exp(-x)>1-x$ gives $m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m(1-\eta_{\rm b})$, hence $s/W<m^\tau$ with $\tau=1-2^{-50}$.""",
        Q(r"For both recurrences we may use the fixed rational exponent", r"0<\tau=\sigma<1."),
        frm=['logarithms-and-exponentials', 'exponential-function-and-gaussian-function', 'bit-network', 'rank-saving'])

# ---------------------------------------------------------------- lower triangular + matrix shear (K.3)
def lower_triangular():
    return show(
        'K.3.1',
        r"""Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones, at most one in each row and column.""",
        r"""Eliminate pivot by pivot, taking the topmost nonzero row and its rightmost nonzero entry, so that every elementary operation is lower triangular in the original order.""",
        r"""Lower triangular changes of coordinates update a later field from earlier ones, which is the direction in which tape scans can do them in linear time; this is the Bruhat factorization with the coordinate order reversed.""",
        'explicit',
        mot_quote=Q(r"The required factorization is the Bruhat factorization", r"elementary elimination proof in this order."),
        page='lower-triangular',
        frm=['matrix-basics', 'vectors-matrices-and-linear-maps'],
        children=[
            infer('K.3.1.1',
                  r"""If $A\ne0$, take the topmost nonzero row and its rightmost nonzero entry as pivot, clear the entries to its left by right multiplication by lower triangular elementary matrices (nothing lies to its right), clear the entries below by left multiplication, and scale the pivot to one.""",
                  Q(r"If $A=0$, take $E_1=E_2=I$ and $\Pi=0$.", r"were zero in the still active columns.")),
            infer('K.3.1.2',
                  r"""Deleting the pivot row and column and repeating, the later operations stay lower triangular in the original order and leave earlier pivots untouched, so each step isolates a rank-one block, $\Pi$ ends with exactly $a$ ones, and $E_1=L^{-1}$, $E_2=R^{-1}$ if $LAR=\Pi$.""",
                  Q(r"Delete the pivot row and column from the active index sets", r"have the required form.")),
        ])

def matrix_shear():
    return show(
        'K.3',
        r"""For each rational $m\times m$ matrix $A$ of a fixed finite collection, of rank $a$, the shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ is performed by exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.""",
        r"""Factor $A=E_1\Pi E_2$; the lower triangular factors are applied by controlled shifts in linear time, and each one of the partial permutation $\Pi$ calls for $H_i\leftarrow H_i+D_j$, which one interchange between two linear updates achieves.""",
        r"""Controlled shifts update a later field from earlier fields in linear time and lower triangular changes of coordinates can be done entirely in that direction, so the factors are taken lower triangular and only the partial permutation needs interchanges.""",
        'explicit',
        mot_quote=Q(r"Lemma~\ref{lem:ordered-affine-streams} updates a later field", r"performed entirely in this direction."),
        page='matrix-shear',
        frm=['lower-triangular', 'controlled-shifts', 'stream-ops', 'matrix-basics', 'modular-arithmetic', 'primes-coprimality-and-gcd'],
        adds=adds_(
            (r'A', 'shear matrix', r'The rational $m\times m$ matrix whose product with $D$ is added to $H$.', 'direct'),
            (r'a', 'matrix rank', r'The rational rank of $A$, which is the number of interchanges the shear needs.', 'count'),
            (r'\Pi', 'partial permutation', r'The matrix with exactly $a$ ones, at most one per row and column, in the factorization $A=E_1\Pi E_2$.', 'direct'),
            (r'E_1', 'left factor', r'The invertible lower triangular matrix on the left of $\Pi$.', 'direct'),
            (r'E_2', 'right factor', r'The invertible lower triangular matrix on the right of $\Pi$.', 'direct'),
        ),
        salient=r"""The number of recursive calls is the rank $a$ of $A$, not its dimension $m$: an addition $H_i\leftarrow H_i+D_j$ costs one interchange between two linear updates, since $(x,y)\mapsto(x,y+x)\mapsto(y+x,x)\mapsto(y+x,y)$.""",
        children=[
            lower_triangular(),
            infer('K.3.2',
                  r"""A fixed odd prime $q$ avoiding all denominators and all numerators of diagonal entries of the invertible factors is found by a finite computation independent of $b$, so every rational identity specializes to $\mathbb Z/q^b\mathbb Z$ with the triangular factors still invertible.""",
                  Q(r"Choose the factorizations of Lemma~\ref{lem:lower-lower} for all matrices", r"the triangular factors remain invertible there.")),
            infer('K.3.3',
                  r"""A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update the coordinates in descending physical order, multiplying by a diagonal unit and adding a fixed combination of earlier coordinates that still hold their original values.""",
                  Q(r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:", r"Inverses are also lower triangular.")),
            infer('K.3.4',
                  r"""Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, and transform back; each one of $\Pi$ needs $D_j\leftarrow D_j+H_i$, then $(H_i,D_j)\leftarrow(D_j,H_i)$, then $D_j\leftarrow H_i-D_j$, which sends $(x,y)$ to $(x+y,y)$ with just one interchange, so there are $a$ interchanges.""",
                  Q(r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$", r"do not multiply that count.")),
        ])

# ---------------------------------------------------------------- construction on role streams (K.4)
def shear_construction():
    return show(
        'K.4',
        r"""Running the network on $W$ role streams, with $\Phi_{A_e}$ on every edge $e$ and gates pointwise, gives $H\leftarrow H+D$ on every original row including scratch rows, and the three shears $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ interchange the two chunks.""",
        r"""Split rows cyclically into $W$ role streams, apply the shear $\Phi_{A_e}$ on each edge by the matrix-shear lemma, run each gate pointwise, merge the rows back, and compose three shears into the swap.""",
        r"""The row split gives all roles one common address set, which is what the frame identity needs for the gates to commute with the frames.""",
        'explicit',
        mot_quote=Q(r"The row split supplies the common address set used in the frame identity", r"frame identity~\eqref{eq:common-frame-identity}."),
        frm=['bit-network', 'matrix-shear', 'stream-ops', 'frames', 'array-order'],
        adds=adds_(
            (r'\Phi_M', 'address shear', r'The permutation of array entries moving the entry at address $(H,D)$ to $(H+MD,D)$ for a rational matrix $M$.', 'direct'),
            (r'A_e', 'edge difference', r'The difference of the matrices at the head and the tail of edge $e$, whose rank counts the interchanges that edge needs.', 'direct'),
        ),
        children=[
            infer('K.4.1',
                  r"""For $k>0$ each chunk is $m$ fields of $b=e/m$ digits, and whole rows are split cyclically into $W$ role streams, row number $Wg+(w-1)$ becoming row $g$ of stream $w$, each of volume $V/W$ with the same remaining shape and a row count divisible by $W^{k-1}$.""",
                  Q(r"For $k=0$ apply the single-digit operation of", r"its row count is divisible by $W^{k-1}$.")),
            infer('K.4.2',
                  r"""On every circuit edge $e$ the stream is moved by $\Phi_{A_e}$, implemented by the matrix-shear lemma with one recursive interchange of $b$-digit fields per pivot, and every gate runs pointwise at matching addresses of its role streams.""",
                  Q(r"For a rational matrix $M$, let $\Phi_M$ act on an array", r"at matching addresses of its role streams.")),
            infer('K.4.3',
                  r"""The frame at a vertex with matrix $M$ is $\Phi_M$, a common address permutation that commutes with every pointwise bit gate, so the output at role $\rho(w)$ is $\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$, and merging the rows back gives $H\leftarrow H+D$ on every original row, scratch rows included.""",
                  Q(r"The row split supplies the common address set used in the frame identity", r"whose initial values were arbitrary.")),
            infer('K.4.4',
                  r"""Performing $D\leftarrow D-H$, then $H\leftarrow H+D$, then $D\leftarrow H-D$ sends $(H,D)$ to $(D,H)$; only the middle shear uses the circuit and the other two target the later group at linear cost.""",
                  Q(r"To interchange the two full chunks, perform", r"sends $(H,D)$ to $(D,H)$.")),
        ])

# ---------------------------------------------------------------- recurrence (K.5)
def recurrence():
    return show(
        'K.5',
        r"""The $s$ smaller calls of one node each work on a stream of volume $V/W$, so the normalized cost satisfies $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, and for $a=s/W<m^\tau$ it solves to $F_k=O(e^\tau)$.""",
        r"""Count the child calls (exactly the edge-rank sum), divide their cost by the parent's volume to get the factor $s/W$, unroll the recurrence into a geometric sum, and bound the sum separately for $a\le1$ and for $a>1$.""",
        r"""Each child works on a stream of volume $V/W$, so dividing the total cost $s(V/W)F_{k-1}$ by the current volume $V$ gives the factor $s/W$ in front of $F_{k-1}$.""",
        'explicit',
        mot_quote=Q(r"Indeed, the \(s\) child calls are executed on streams of volume", r"gives the factor \(s/W\)."),
        page='power-saving-recurrence',
        frm=['rank-saving', 'bit-network', 'proof-by-induction-and-recursion', 'big-o', 'logarithms-and-exponentials'],
        children=[
            infer('K.5.1',
                  r"""The number of recursive calls is the sum of the edge ranks, exactly $s$, each acting on one role stream of volume $V/W$, and the splitting, merging, gates and triangular operations cost $O(V)$ at the node, so $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.""",
                  Q(r"The number of recursive calls is the sum of the edge ranks, exactly $s$.", r"F_k\le(s/W)F_{k-1}+O(1).")),
            infer('K.5.2',
                  r"""For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^ka^j$ is $O(m^{k\tau})$: at most $k+1=O(m^{k\tau})$ if $a\le1$ and $O(a^k)$ if $a>1$, so $F_k=O(e^\tau)$ since $e=m^k$.""",
                  Q(r"For $a=s/W<m^\tau$ the geometric sum", r"Hence $F_k=O(e^\tau)$.")),
        ])

def schedule():
    return infer(
        'K.6',
        r"""The recursive calls are scheduled depth-first on a fixed number of tapes by parking the inactive role streams on a stack, copying the active stream to the child's input area and restoring on return, each push, pop, copy and erasure moving only $O(V)$ symbols at the parent, so temporary storage is never counted as logical volume in the factor $s/W$.""",
        Q(r"Before a recursive call, append the $W-1$ inactive role streams", r"in the factor $s/W$."),
        frm=['stream-ops', 'tape-machines'])

def descriptors():
    return infer(
        'K.7',
        r"""Even when the payload is one bit, descriptor processing fits the $O(V)$ node term: both original chunk ranges stay present in every child, so $V_j\ge q^{2e_0}$ and $j\log W=O(\log V_j)$ for a depth-$j$ child, giving $\log V_0=O(\log(2V_j))$ and descriptor work $(\log 2V_0)^{O(1)}=O(V_j)$.""",
        Q(r"For completeness, descriptor processing also fits this term when the", r"every choice of spectator lengths."),
        frm=['stream-ops', 'logarithms-and-exponentials'])

# ---------------------------------------------------------------- KEY step (K)
def key_step():
    return show(
        'K',
        r"""Key step: for $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits, with a row field of length divisible by $W^k$ before them, can be interchanged in $O(Ve^\tau)$ time, because the fixed bit network turns each recursion level into only $s<W m$ smaller interchanges, each on a stream of volume $V/W$.""",
        r"""Run the fixed bit network on $W$ role streams to get the shear $H\leftarrow H+D$ on every row, each edge being a matrix shear done by interchanges of chunks of $e/m$ digits, compose three shears into the swap, and solve $F_k\le(s/W)F_{k-1}+O(1)$.""",
        r"""Multiplying the parameter by $m$ multiplies the work by only $s/W<m$ per unit volume, and this strict inequality is the source of the power saving.""",
        'explicit',
        mot_quote=Q(r"After dividing cost by volume", r"is the source of the power saving."),
        page='power-interchange',
        frm=['bit-network', 'matrix-shear', 'power-saving-recurrence', 'stream-ops', 'controlled-shifts', 'array-order', 'modular-arithmetic', 'binary-field-f2-and-xor'],
        adds=adds_(
            (r'F_k', 'normalized cost', r'An upper bound on the running time divided by the logical volume for chunks of $m^k$ digits.', 'direct'),
        ),
        salient=r"""The exponent $\tau=1-2^{-50}$ lies below one by a minuscule margin, since the network saves a relative amount of only about $1.5\cdot10^{-11}$ of its edge ranks and needs $W\approx1.8\cdot10^{20}$ roles, yet the recursion compounds that per-level gain over $\log_m e$ levels into a genuine power of $e$.""",
        children=[bit_network(), explicit_tau(), matrix_shear(), shear_construction(), recurrence(), schedule(), descriptors()])

# ---------------------------------------------------------------- S1.4 removal of restrictions
def removal():
    return show(
        'S1.4',
        r"""For arbitrary widths $u$ and arbitrary prefix, gap and suffix, the $W^k$ rows needed are supplied by $\rho=O(\log e)$ high digits of the chunks, the row count is padded to a multiple of $W^k$, the remaining width is split in base $m$, and binary chunks are padded to radix-$q$ ranges, for a total of $O(Vu^\tau)$.""",
        r"""Interchange and join $\rho$ high digits of the two chunks into a row field, apply the power-width interchange to the base-$m$ pieces of the rest with the same padded row field, undo the joins, and for binary chunks pad to $[q^e]$.""",
        r"""The power-width interchange needs at least $W^k$ rows and a power-of-$m$ width, but a general array has neither, so the rows are taken from a few of the array's own high digits and the width is decomposed in base $m$.""",
        'explicit',
        mot_quote=Q(r"We have proved the fast operation for power widths", r"less than the final bound."),
        frm=['power-interchange', 'stream-ops', 'floor-ceiling-and-rounding', 'logarithms-and-exponentials', 'positional-number-representation-and-carries'],
        adds=adds_(
            (r'\rho', 'row digits', r'The number $\lceil k\log W/(2\log q)\rceil$ of top digits of each chunk that are moved into a joint row field.', 'count'),
            (r'a_j', 'base-$m$ digit', r'The digit of the remaining width $e-\rho$ in base $m$, giving the number of pieces of width $m^j$.', 'count'),
            (r'R', 'row field range', r'The range $q^{2\rho}\ge W^k$ of the joint row field.', 'count'),
        ),
        children=[
            infer('S1.4.1',
                  r"""For large $e$, with $k=\lceil\log_me\rceil$ and $\rho=\lceil k\log W/(2\log q)\rceil=O(\log(2e))$ (the bounded set of small widths being done digit by digit), the top $\rho$ digits of both chunks are interchanged pairwise and the high digits of the first chunk are moved next to those of the second, at cost $O(V\rho)$.""",
                  Q(r"First suppose the two ranges are $[q^e]$, where $q$ is the fixed prime", r"immediately after $d^+$.")),
            infer('S1.4.2',
                  r"""In the two middle field orders the first two fields form a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks.""",
                  Q(r"In the two middle orders, the first two fields form a row field of range", r"before both remaining chunks.")),
            infer('S1.4.3',
                  r"""Appending zero rows within each prefix raises the row count to $R'=W^k\lceil R/W^k\rceil<2R$, so the padded volume is below $2V$.""",
                  Q(r"Append zero rows, separately within each preceding prefix", r"The padded logical volume is less than $2V$.")),
            infer('S1.4.4',
                  r"""Writing $e-\rho=\sum_{j=0}^ka_jm^j$ with $0\le a_j<m$, the remaining chunks split into $a_j$ pieces of width $m^j$, each pair interchanged by the power-width proposition with the same row field, for total cost $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$.""",
                  Q(r"Write the remaining width in base $m$:", r"=O(Ve^\tau).")),
            infer('S1.4.5',
                  r"""Since $a_j<m$ and $m^k<me$ the sum is geometric of order $e^\tau$, and scanning away the padded rows and reversing the joins costs $O(V\log(2e))=O(Ve^\tau)$.""",
                  Q(r"The fixed bound $a_j<m$ and the inequality", r"is $O(Ve^\tau)$.")),
            infer('S1.4.6',
                  r"""Binary chunks of $u$ bits are padded numerically to the radix-$q$ ranges $[q^e]$ with $q^e\ge2^u$, a volume increase below $q^2$, interchanged, and the padding is scanned away; since $e=O(u)$ the bound is $O(Vu^\tau)$.""",
                  Q(r"Finally, for binary chunks let $e$ be the least integer with $q^e\ge2^u$.", r"the bound is $O(Vu^\tau)$.")),
            infer('S1.4.7',
                  r"""For chunks whose widths differ by one bit, the leading bit of the longer chunk is moved by a single-bit move costing $O(V)$ and the equal-width parts are interchanged, so no unrestricted transpose is used.""",
                  Q(r"For widths differing by one bit, choose the leading bit", r"in these operations.")),
        ])

def chunk_interchange():
    return show(
        'S1',
        r"""Two disjoint address chunks of $u$ bits, anywhere in an array whose addresses form a complete Cartesian product, can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$, although the intermediate steps form XOR combinations of the data.""",
        r"""Use linear-time stream tools together with the key step, a recursive interchange of chunks of $m^k$ digits driven by a fixed rank-saving bit network, and then remove its restrictions on width and row count.""",
        r"""An edge matrix of rank $a$ needs $a$ smaller interchanges and the ranks sum to less than the number of wires times $m$, so the resulting recurrence saves a power of the chunk width.""",
        'explicit',
        mot_quote=Q(r"We use the bit network to interchange", r"saves a power of the chunk width."),
        page='chunk-interchange',
        frm=['power-interchange', 'stream-ops', 'controlled-shifts', 'array-order', 'fixed-tape-model', 'binary-field-f2-and-xor'],
        adds=adds_(
            (r'u', 'chunk width', r'The number of bits in each of the two address chunks being interchanged.', 'count'),
            (r'W', 'wire count', r'The number of wires (roles) of the fixed bit network; each role stream carries $V/W$ of the volume.', 'count'),
            (r'm', 'label dimension', r'The dimension of the fixed label space; one recursion level divides the chunk width by $m$.', 'count'),
            (r's', 'total edge rank', r'The sum over all edges of the network of the rank of the matrix difference across the edge, which is the number of smaller interchanges one level makes.', 'count'),
            (r'e', 'chunk width in digits', r'The number of radix-$q$ digits in each of the two chunks, $e=m^k$.', 'count'),
            (r'k', 'recursion depth', r'The number of recursion levels, $k=\log_m e$.', 'count'),
            (r'q', 'digit radix', r'The fixed odd prime that is the radix of the address digits.', 'direct'),
        ),
        salient=r"""The final effect is an exact permutation of the stored bits even though the intermediate steps form XOR combinations of data, and it is exact for arbitrary initial values of the auxiliary rows.""",
        children=[stream_ops(), controlled_shifts(), key_step(), removal()])
