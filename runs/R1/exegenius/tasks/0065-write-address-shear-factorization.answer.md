An address shear is a linear update of two vectors of address fields, and a lower-triangular factorization reduces it to interchanges and linear-cost updates. The address shear is the endpoint operator of the bit network, a [Finite linear network with roles and frames](linear-network-roles.md).

Let $m$ be the number of fields in each vector, and let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two vectors of address fields. Here $q$ is a fixed odd prime and $b$ the digits per field; these letters change meaning from earlier pages. Each field is a block of $b$ radix-$q$ digits, so it holds a residue in $\mathbb Z/q^b\mathbb Z$.

For a rational $m\times m$ matrix $M$, the shear by $M$ is $(H,D)\mapsto(H+MD,D)$. A rational entry $u/v$ acts on fields as $u\,v^{-1}$ modulo $q^b$, which exists only if $q$ does not divide $v$. So $q$ is chosen not to divide any denominator or diagonal numerator of the finitely many factors used. Let $\operatorname{rank}_{\mathbb Q}M$ be the number of linearly independent rows of $M$.

Every rational $M$ factors as $M=E_1\Pi E_2$, where $E_1,E_2$ are invertible lower-triangular rational matrices and $\Pi$ is a partial permutation matrix with $\operatorname{rank}_{\mathbb Q}M$ ones, at most one in each row and column. This is Grigor'ev's Bruhat factorization with coordinate order reversed. Elimination proves it: pivot on the topmost nonzero row's rightmost entry, clear its row and column by triangular operations, and repeat.

Example: for $m=2$ and $M=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, $\operatorname{rank}_{\mathbb Q}M=1$, and $M=E_1\Pi E_2$ with $E_1=I$, $\Pi=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $E_2=\begin{pmatrix}1&0\\1&1\end{pmatrix}$.

Let $s$ and $g$ be the row and column indices of $\Pi$. To apply the shear, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$. For each entry $\Pi_{sg}=1$, update $H_s\gets H_s+D_g$. Then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. The result is $H+E_1\Pi E_2D=H+MD$, and $D$ is unchanged.

A lower-triangular transformation costs $O(V)$, where $V$ is the stored bit volume. Update coordinates in descending order: at coordinate $i$, add a fixed combination of coordinates $j<i$. Each $j<i$ is reached only after $i$, so it still holds its original value. Each pass is linear in the stored bits, and $m$ is fixed.

Each update $H_s\gets H_s+D_g$ is one interchange, which swaps the contents of two equal fields, plus two additions: $D_g\gets D_g+H_s$, swap, then $D_g\gets H_s-D_g$. On a pair $(h,d)$ this gives $(h+d,d)$. So the shear needs $\operatorname{rank}_{\mathbb Q}M$ interchanges plus $O(V)$ further work.

Each edge of the bit network carries such a matrix, whose rank is its edge rank. The interchange count of the network is the sum of the edge ranks, which the paper bounds by a rank budget of the network (its motif-residual lemma). That sum is less than the number of wires times $m$, so the recurrence saves a power of the chunk width (the length of each interchanged address chunk). <cite data-source="paper">Because the sum of these ranks is less than the number of wires times</cite>.
