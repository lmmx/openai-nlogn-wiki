An address shear is a linear update of two ordered groups of address fields, in which the first group is changed by a matrix applied to the second. The target bound needs it as the endpoint of a tape procedure, and what matters for the bound is how many pairwise interchanges of address fields it takes to carry it out.

Here $H$ and $D$ are the two ordered groups of address fields, viewed as vectors over a common residue ring (the integers with arithmetic taken modulo a fixed number). $A$ is a rational matrix with one row for each field of $H$ and one column for each field of $D$, so that $AD$ has the length of $H$. The shear replaces $H$ by $H+AD$ and leaves $D$ unchanged, so it is the permutation $(H,D)\mapsto(H+AD,D)$.

A pairwise interchange swaps two address fields of the array.

The shear is based on [Lower-triangular factorization](lower-triangular-factorization.md), which writes $A = E_1\Pi E_2$ with $E_1$ and $E_2$ invertible lower-triangular and $\Pi$ a partial permutation matrix with one 1 per pivot. Invertible factors do not change rank, so $\Pi$ has exactly as many 1s as $A$ has rank. Each 1 of $\Pi$ accounts for one pairwise interchange, so the shear uses as many interchanges as the rank of $A$.

The shear is realized in a [Linear network with restored auxiliary values](linear-network-exchange.md), which restores every auxiliary value it uses, so the array holds only the updated fields when the shear ends.

The bit procedure's endpoint operator is a shear of this form. <cite data-source="paper">two fields, written as vectors $H,D$ over a common residue ring, are updated by $(H,D)\mapsto(H+D,D)$</cite>

The count of interchanges is what the later cost bound uses: the shear costs as many interchanges as the rank of $A$, not as many as the size of $A$.
