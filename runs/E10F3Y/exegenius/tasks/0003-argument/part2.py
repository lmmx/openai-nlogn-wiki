from lib import *

# ---------------------------------------------------------------- S1.5 chunk interchange
s15_1 = show(
    "S1.5.1",
    r"Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones, at most one in each row and column.",
    r"Eliminate pivot by pivot: take the topmost nonzero row and its rightmost nonzero entry, clear the entries to its left by right multiplication and those below by left multiplication with lower triangular elementary matrices, scale the pivot to one, delete that row and column from the active indices and repeat.",
    mot("Lower triangular changes of coordinates are exactly the ones that can be done in linear time because each target field follows its control fields on the tape.", "explicit",
        r"earlier fields in linear time.  Lower triangular changes of coordinates"),
    [
        infer("S1.5.1a",
              r"If $A=0$ take $E_1=E_2=I$ and $\Pi=0$; otherwise pick the topmost nonzero row and its rightmost nonzero entry, use that pivot column to clear entries to its left by lower triangular right multiplications (no nonzero entries lie to its right), clear below the pivot by lower triangular left multiplications and scale the pivot to one.",
              r"If $A=0$, take $E_1=E_2=I$ and $\Pi=0$.  Otherwise choose the topmost"),
        infer("S1.5.1b",
              r"Deleting the pivot row and column and repeating on the active indices keeps all operations lower triangular and leaves earlier pivot rows and columns untouched, so each step isolates one rank-one block and the final partial permutation has exactly $a$ ones; if $LAR=\Pi$ then $E_1=L^{-1}$ and $E_2=R^{-1}$.",
              r"Delete the pivot row and column from the active index sets, retaining"),
    ],
    page="matrix-factorization",
    frm=["gaussian-elimination-and-triangular-matrices", "vector-spaces-subspaces-dimension-and-rank", "matrices-and-linear-maps", "permutations-bijections-and-permutation-matrices"],
    adds=[
        add(r"A", "rational matrix", "A rational $m\\times m$ matrix to be factored (later the edge matrix whose shear is to be performed).", "direct"),
        add(r"a", "matrix rank", "The rank of $A$ over $\\mathbb Q$, which will count the interchanges needed.", "count"),
        add(r"\Pi", "partial permutation", "A $0/1$ matrix with at most one one in each row and column, with exactly $a$ ones.", "direct"),
    ])

s15_2 = show(
    "S1.5.2",
    r"For a fixed finite set of rational matrices there is a fixed odd prime $q$ such that, for $A$ of rank $a$, the permutation $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ of two groups of $m$ fields each ranging over $[q^b]$ costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ further work.",
    r"Factor $A=E_1\Pi E_2$, do the triangular parts by controlled shifts in linear time (transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$), and realize each one of $\Pi$ by $D_j\leftarrow D_j+H_i$, $(H_i,D_j)\leftarrow(D_j,H_i)$, $D_j\leftarrow H_i-D_j$, which uses one interchange.",
    mot("The first and last of the three updates target a later field controlled by an earlier one, so they are linear-time controlled shifts; only the middle swap is a genuine interchange.", "explicit",
        r"The first and last updates target a later field controlled by an earlier"),
    [
        infer("S1.5.2a",
              r"Choose the factorizations of the finitely many matrices and an odd prime $q$ avoiding all denominators and diagonal numerators in a finite rational table; the identities then specialize to $\mathbb Z/q^b\mathbb Z$ with the triangular factors still invertible.",
              r"Choose the factorizations of Lemma~\ref{lem:lower-lower} for all matrices"),
        infer("S1.5.2b",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$: update coordinates in descending physical order, multiplying by the diagonal unit and adding a fixed combination of earlier coordinates that still hold their original values.",
              r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
        infer("S1.5.2c",
              r"For $A=E_1\Pi E_2$ the sequence above gives $(h,d)\mapsto(h+d,d)$ at each one of $\Pi$ using one interchange, and since $\Pi$ has $a$ ones the number of recursive calls is the rational rank $a$.",
              r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
    ],
    page="matrix-shear",
    frm=["matrix-factorization", "controlled-shift", "modular-arithmetic", "tape-stream-operations", "primes-coprimality-and-the-extended-euclidean-algorithm"],
    adds=[
        add(r"H", "high field group", "The earlier group of $m$ fields $H=(H_1,\\ldots,H_m)$, each ranging over $[q^b]$.", "direct"),
        add(r"D", "low field group", "The later group of $m$ fields $D=(D_1,\\ldots,D_m)$, each ranging over $[q^b]$.", "direct"),
        add(r"b", "field digits", "The number of radix-$q$ digits of each field.", "count"),
    ])

s15_3_5 = show(
    "S1.5.3.5",
    r"With $F_k$ a uniform bound on time divided by logical volume, $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, hence $F_k=O(e^{\tau})$ for $e=m^k$.",
    r"Count the $s$ recursive calls, each on a role stream of volume $V/W$; show that scheduling them depth-first on a fixed set of tapes adds only $O(V)$ at each node; sum the geometric series with ratio $s/W<m^\tau$.",
    mot("Dividing a call's cost by the volume turns the $s$ children of volume $V/W$ into the single factor $s/W$, which the strict rank deficit keeps below $m^\\tau$.", "recoverable"),
    [
        infer("S1.5.3.5a",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$, because each edge shear $\Phi_{A_e}$ needs $\mathrm{rank}(A_e)$ pivot interchanges (Lemma matrix-shear), and each acts on one role stream of volume $V/W$ with all other fields spectators.",
              r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        infer("S1.5.3.5d",
              r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^ka^j$ is $O(m^{k\tau})$: if $a\le1$ it is at most $k+1=O(m^{k\tau})$, and if $a>1$ it is $O(a^k)\subseteq O(m^{k\tau})$; hence $F_k=O(e^\tau)$.",
              r"For $a=s/W<m^\tau$ the geometric sum"),
        infer("S1.5.3.5b",
              r"A depth-first schedule reserves $W$ role tapes, a parking stack for the $W-1$ inactive streams and a descriptor stack; each push, pop, copy, positioning or erasure moves $O(V)$ symbols at a parent node and there are only $s$ child calls, so the node overhead is an additive $O(V)$ and temporary storage is not substituted for logical volume in the factor $s/W$.",
              r"Each push, pop, copy, positioning operation, or erasure moves $O(V)$"),
        infer("S1.5.3.5c",
              r"Descriptor work also fits: both original chunk ranges stay present in every child, so $V_j\ge q^{2e_0}$ and $j\log W=O(e_0)=O(\log V_j)$, hence $\log V_0=O(\log(2V_j))$ and polylogarithmic descriptor processing is $O(V_j)$ at depth $j$.",
              r"For completeness, descriptor processing also fits this term when the"),
    ])

s15_3 = show(
    "S1.5.3",
    r"If a row field preceding both chunks has length divisible by $W^k$, two disjoint chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^{\tau})$ time, preserving every other address field.",
    r"Split rows cyclically into the $W$ role streams, run the bit network on them with the frame $\Phi_{M_v}$ at each vertex and $\Phi_{A_e}$ on each edge (each implemented by the matrix-shear lemma with one recursive interchange per unit of rank), so the net effect is the shear $H\leftarrow H+D$ on every row; then interchange by $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$.",
    mot("Because the sum of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", "explicit",
        r"$m$, the resulting recurrence saves a power of the chunk width."),
    [
        infer("S1.5.3.1",
              r"Split whole rows cyclically into $W$ role streams within each prefix: row $r=Wg+(w-1)$ goes to stream $w$ as row $g$, so each stream has volume $V/W$, the same remaining shape and a row count divisible by $W^{k-1}$.",
              r"Split whole rows cyclically into $W$ role streams within each prefix"),
        infer("S1.5.3.2",
              r"On every circuit edge apply the address permutation $\Phi_{A_e}$ to that role stream, recursively interchanging each pivot pair of $b$-digit fields, and execute each bit gate pointwise at matching addresses; a common address permutation commutes with every pointwise bit gate, so the frame identity applies.",
              r"On every circuit edge apply"),
        infer("S1.5.3.3",
              r"The physical output satisfies $f'_{\rho(w)}=\Phi_{M_{{\rm out}(\rho(w))}}\Phi_{-M_{{\rm in}(w)}}f_w=\Phi_{I_m}f_w$ by the endpoint condition, and merging row $g$ of role $\rho(w)$ back to row $Wg+(w-1)$ undoes $\rho$, giving the shear $H\leftarrow H+D$ on every original row, scratch rows included.",
              r"=\Phi_{I_m}f_w,"),
        infer("S1.5.3.4",
              r"The three updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the circuit and the other two target the later group, so they cost $O(V)$.",
              r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,"),
        s15_3_5,
    ],
    page="power-width-interchange",
    frm=["matrix-shear", "rank-saving", "frames", "exchange-network", "subspace-labels", "tape-stream-operations", "recurrences-and-geometric-sums", "multitape-turing-machine"],
    adds=[
        add(r"k", "recursion depth", "The exponent in the chunk width $e=m^k$, equal to the depth of the recursion.", "count"),
        add(r"F_k", "normalized cost", "A uniform upper bound for the time of an interchange of $m^k$-digit chunks divided by its logical volume.", "direct"),
    ],
    salient=r"The exponent $\tau$ in the cost $O(Ve^\tau)$ does not depend on how huge $W$ and $s$ are, only on the ratio $s/W$ being strictly below $m$: the geometric series $\sum a^j$ is dominated by the last level, giving $m^{k\tau}=e^\tau$ rather than $km^k$.")

s15_4 = show(
    "S1.5.4",
    r"Arbitrary-width interchange: for positive $P,G,B$ and $u\ge1$ the address permutation $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ on $[P]\times[2^u]\times[G]\times[2^u]\times[B]$ costs $O(Vu^\tau)$ for the fixed $\tau=1-2^{-50}$, with $B=1$ allowed.",
    r"Supply the missing rows from the top $\rho$ digits of the chunks, pad the row count to a multiple of $W^k$, split the remaining width in base $m$ into pieces of widths $m^j$ and interchange each by the power-width procedure, then pad binary chunks to radix $q$.",
    mot("Rows for a general array can be supplied by a few of its own high digits.", "explicit",
        r"Rows for a general array can be supplied by a few of its own high digits."),
    [
        infer("S1.5.4a",
              r"Take $k=\lceil\log_me\rceil$ and $\rho=\lceil k\log W/(2\log q)\rceil$ (so $1\le\rho<e$ and $\rho=O(\log(2e))$ for large $e$); exchange the top $\rho$ digits $h^+,d^+$ digit by digit and join them, costing $O(V\rho)$, so that the first two fields form a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks.",
              r"Write each chunk as its top $\rho$ digits followed by its remaining"),
        infer("S1.5.4b",
              r"Append zero rows within each prefix until the row count is $R'=W^k\lceil R/W^k\rceil<2R$, so the padded volume is below $2V$ and $R'$ is divisible by every $W^j$ needed; completed calls preserve each row address, so padded rows neither mix with genuine rows nor affect them.",
              r"Append zero rows, separately within"),
        infer("S1.5.4c",
              r"Write the remaining width $e-\rho=\sum_{j=0}^ka_jm^j$ in base $m$ with $0\le a_j<m$ and interchange the $a_j$ pieces of width $m^j$ by the power-width procedure; the cost is $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$ because $a_j<m$ and $m^k<me$ make it a geometric sum, and the remaining movement $O(V\log(2e))$ is $O(Ve^\tau)$.",
              r"Write the remaining width in base $m$:"),
        infer("S1.5.4d",
              r"For binary chunks take the least $e$ with $q^e\ge2^u$ and pad each range from $[2^u]$ to $[q^e]$ by zeros, increasing the volume by less than the fixed factor $q^2$; padding preserves order, the interchange preserves the valid set, and $e=O(u)$ gives $O(Vu^\tau)$.",
              r"Finally, for binary chunks let $e$ be the least integer with"),
        infer("S1.5.4e",
              r"For widths differing by one bit the extra leading bit $h_0$ (or $d_0$) is moved outside the equal-width pair: $(h_0,H,g,D)\mapsto(h_0,D,g,H)\mapsto(D,g,h_0,H)$ or $(H,g,d_0,D)\mapsto(d_0,H,g,D)\mapsto(d_0,D,g,H)$, costing one single-bit move $O(V)$ beyond the equal-width interchange.",
              r"For widths differing by one bit, choose the leading bit of the longer"),
    ])

s15 = show(
    "S1.5",
    r"Two disjoint equal-width bit chunks of an address array can be interchanged in $O(Vu^{\tau})$ steps for the fixed $\tau=1-2^{-50}$, even though the intermediate steps form XOR combinations of data and only the final effect is a permutation.",
    r"Run the bit network of the exchange construction recursively on the address fields: factor each edge matrix and charge one smaller interchange per unit of rank (matrix factorization and shear), solve the resulting recurrence for power widths with enough rows, and then remove the width and row restrictions.",
    mot("An edge matrix of rank $a$ requires $a$ smaller interchanges, and because the ranks add to less than the number of wires times $m$ the recursion saves a power of the chunk width.", "explicit",
        r"Because the sum of these ranks is less than the number of wires times"),
    [s15_1, s15_2, s15_3, s15_4],
    page="chunk-interchange",
    frm=["power-width-interchange", "matrix-shear", "rank-saving", "tape-stream-operations", "controlled-shift", "bitwise-operations-and-xor"],
    adds=[
        add(r"q", "radix prime", "The fixed odd prime radix of the address digits chosen so that all denominators of the finite rational table are units.", "direct"),
        add(r"e", "chunk width", "The width of a chunk in radix-$q$ digits (for power widths $e=m^k$).", "count"),
        add(r"\rho", "high digits", "The number of top digits of each chunk that are exchanged first and used as the row field.", "count"),
    ],
    salient=r"The interchange is an exact permutation in the end, yet it is computed through XOR combinations of intermediate data and arbitrary scratch rows; its cost exponent $\tau<1$ is the same fixed number $1-2^{-50}$ for all widths.")
