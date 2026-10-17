Fast address-chunk interchange exchanges two disjoint fields of $u$ bits in the addresses of an array's entries, on a fixed number of tapes, in time $O(Vu^\tau)$ <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>. Here $V$ is the number of entries of the array (its logical volume), $u$ is the width of each chunk in bits, and $\tau<1$ is a fixed exponent ($\tau=1-2^{-50}$). Intermediate steps form XOR combinations of data, yet the final permutation is exact for arbitrary auxiliary values.

## Reduction to a shear

Take radix-$q$ digits, with $q$ a fixed prime, and let $H$ and $D$ be the values of the two chunks. The interchange is $D\gets D-H$, then $H\gets H+D$, then $D\gets H-D$, componentwise, which sends $(H,D)$ to $(D,H)$. Only the middle shear needs the network below; the other two updates have linear cost.

## Power widths

Let a chunk have $e=m^k$ digits, where $m$ is a fixed number of equal fields per chunk and $k$ is the number of recursion levels. Write each chunk as $m$ consecutive fields of $b=e/m$ digits, giving vectors $H,D$ over $\mathbb Z/q^b\mathbb Z$. Each shear is performed by [Matrix shear by triangular factorization](matrix-shear.md): a rational matrix of rank $a$ costs exactly $a$ interchanges of pairs of $b$-digit fields plus $O(V)$ other work <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite>.

The shears are the edges of a [linear exchange network with restored scratch wires](exchange-network.md) of $W$ wires, whose edge matrices $A_\epsilon$ have total rank $s<Wm$ (see [nested subspace labels and rank deficit](subspace-labels.md)), with $s/W<m^\tau$.

Split whole rows cyclically into $W$ role streams within each prefix; row $r=Wg+(w-1)$ goes to stream $w$ as row $g$. Here a row is a value of the address fields before both chunks, and the prefix is what precedes them. Each stream has logical volume $V/W$ and its row count is divisible by $W^{k-1}$, so the same argument applies one level down. Splitting into streams, merging, and moving digits are done by linear-time scans from [Elementary stream operations](stream-ops.md).

Each wire's array carries a frame ([Frames on wire arrays](array-frames.md)): at a vertex with matrix $M$ it is the address permutation $\Phi_M$, which moves the entry at $(H,D)$ to $(H+MD,D)$, and every edge changes it by $\Phi_{M'-M}$. A common address permutation commutes with every pointwise bit gate, so gates run pointwise at matching addresses. On every circuit edge apply $\Phi_{A_\epsilon}$ to that role stream, implemented by the matrix-shear lemma, recursively interchanging each pivot pair of $b$-digit fields.

Read input $f_w$ as logical array $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$ (no tape operation); the network sends wire $w$ to role $\sigma(w)$. By the endpoint contract, the physical output is $f'_{\sigma(w)}=\Phi_{M_{\mathrm{out}(\sigma(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$. Merging row $g$ of role $\sigma(w)$ back to the original row undoes $\sigma$, and the result is $H\gets H+D$ on every original row, including scratch rows whose initial values were arbitrary.

The recursive calls number exactly the sum of the edge ranks, $s$ <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite>, each on one role stream of volume $V/W$. Splitting, merging, gates, triangular operations and scheduling the calls on the fixed tapes cost $O(V)$ at the node: a fixed number of operations on its own volume, not on its children's. Let $F_k$ be a uniform upper bound on time divided by logical volume at width $m^k$. Then $F_0=O(1)$ (a single-digit operation) and $F_k\le(s/W)F_{k-1}+O(1)$, the factor $s/W$ being $s$ calls times volume fraction $1/W$ each. The interchange gets its power saving from the recurrence of [Recursive power saving](rank-recurrence.md), solved as follows.

Unrolling gives $F_k=O(\sum_{j=0}^k a^j)$ with $a=s/W<m^\tau$. If $a\le1$, every term is at most $1$, so the sum is at most $k+1=O(m^{k\tau})$. If $a>1$, $\sum_{j=0}^k a^j=(a^{k+1}-1)/(a-1)=O(a^k)$ and $a^k<m^{k\tau}$. Hence, since $e=m^k$, $F_k=O(e^\tau)$.

The saving is a power only barely below 1 because the sole source of saving is the rank deficit: $s$ falls just under $Wm$, so each factor $m$ of width multiplies the cost per entry by just under $m$. No arithmetic on the data is involved.

## Arbitrary widths

The address permutation is $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, with prefix $p$, chunks $h,d$, gap $g$ and suffix $z$; one-bit payloads are allowed <cite data-source="paper">In particular, $B=1$ is allowed.</cite>. For chunks of range $[q^e]$ put $k=\lceil\log_m e\rceil$ (a new meaning of $k$, so $m^k<me$). Put $\rho=\lceil k\log W/(2\log q)\rceil$ so that $q^{2\rho}\ge W^k$; for large $e$, $1\le\rho<e$ and $\rho=O(\log(2e))$. Interchange the top $\rho$ digits of the two chunks one pair at a time and join them, so that the two middle field orders have a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks. Pad with zero rows, within each prefix, to $R'=W^k\lceil R/W^k\rceil<2R$ rows, so the padded volume is below $2V$ and the row count is divisible by each needed $W^j$.

Write the remaining width as $e-\rho=\sum_{j=0}^k a_jm^j$ with $0\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case, all using the same row field. The total cost is $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$. The bound $a_j<m$ and $m^k<me$ make this a geometric sum of order $e^\tau$. Then scan away the padding and undo the joins.

For $u$-bit chunks, pad each range from $[2^u]$ to $[q^e]$ with the least $e$ with $q^e\ge2^u$, a fixed factor in volume; as $e=O(u)$, the cost is $O(Vu^\tau)$ <cite data-source="paper">Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.</cite>.
