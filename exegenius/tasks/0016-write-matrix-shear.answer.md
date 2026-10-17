Matrix shear by triangular factorization applies $(H,D)\mapsto(H+AD,D)$ for a fixed rational matrix $A$ with only as many field interchanges as $A$ has rank.

Here $A$ is a rational $m\times m$ matrix of rank $a$, and $m$ is the number of fields in each group $H=(H_1,\dots,H_m)$ and $D=(D_1,\dots,D_m)$, every $H_i$ lying before every $D_j$. Each field holds a residue modulo $q^b$, where $q$ is a fixed odd prime and $b$ is the number of base-$q$ digits per field; $V$ is the volume of data. For $A$ in a fixed finite set, the shear can be performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work <cite data-source="paper">can be performed with exactly $a$ interchanges of pairs of $b$-digit</cite>.

Every such $A$ factors as $A=E_1\Pi E_2$, where $E_1,E_2$ are invertible lower triangular and $\Pi$ has exactly $a$ ones, at most one per row and column <cite data-source="paper">Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization</cite>. By elimination, take the topmost nonzero row and its rightmost nonzero entry, the pivot. Right multiplication by lower triangular elementary matrices clears the row left of the pivot, and left multiplication by such matrices clears the column below it; scaling makes the pivot one. Delete the pivot row and column and repeat. Rank is preserved, so there are $a$ pivots; they form $\Pi$.

Fix these factorizations once, and choose an odd prime $q$ avoiding every denominator in the table and every numerator of a diagonal entry of an invertible factor. The identities then specialise to $\mathbb Z/q^b\mathbb Z$ and the triangular factors remain invertible.

A lower triangular transformation of $H$ or of $D$ is carried out by [controlled shifts and rational scalings](controlled-shifts.md): update coordinates in descending physical order, each by a unit scaling and a fixed combination of earlier coordinates, which still hold original values. This costs $O(V)$ for fixed $m$.

To shear, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Then $H$ becomes $E_1(E_1^{-1}H+\Pi E_2D)=H+AD$ and $D$ is restored.

Each one of $\Pi$, in row $i$ and column $j$, calls for $H_i\gets H_i+D_j$. Do it by $D_j\gets D_j+H_i$, then interchange $(H_i,D_j)$, then $D_j\gets H_i-D_j$. The first and last steps target a later field controlled by an earlier one. If $H_i=h$ and $D_j=d$ initially, the pair becomes $(h,d+h)$, then $(d+h,h)$, then $(h+d,d)$.

This uses one interchange per one of $\Pi$, and there are $a$ ones, so exactly $a$ interchanges are used; temporary tapes do not multiply that count.
