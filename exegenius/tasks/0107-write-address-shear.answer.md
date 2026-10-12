An address shear is a rearrangement of two ordered groups of address fields in which one group is changed by a matrix applied to the other. It is the endpoint operator of a tape procedure in the target bound. Here $H$ is the first group, a vector over a common residue ring (the integers with arithmetic taken modulo a fixed number), with one entry for each row of $A$. $D$ is the second group, with one entry for each column of $A$. The shear is $(H,D)\mapsto(H+AD,D)$, which replaces $H$ by $H+AD$ and leaves $D$ unchanged.

The shear is based on [Lower-triangular factorization](lower-triangular-factorization.md), which writes $A = E_1\Pi E_2$ with $E_1$ and $E_2$ invertible lower-triangular and $\Pi$ a partial permutation matrix with one 1 per pivot. Invertible factors do not change rank, so $\Pi$ has exactly as many 1s as $A$ has rank.

The shear runs in four steps. First transform $D$ by $E_2$ and $H$ by $E_1^{-1}$. Then add $\Pi D$, computed from the transformed $D$, to $H$. Finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. The result is $H+E_1\Pi E_2D=H+AD$, and $D$ is restored. Only the addition moves values between the two groups, so only it needs interchanges.

On this page $s$ and $t$ take new meanings: $s$ indexes the fields of $H$ and $t$ the fields of $D$, and a 1 in row $s$ and column $t$ of $\Pi$ calls for $H_s\leftarrow H_s+D_t$. Three updates achieve this with one swap:

$$D_t\leftarrow D_t+H_s,\qquad (H_s,D_t)\leftarrow(D_t,H_s),\qquad D_t\leftarrow H_s-D_t.$$

The first update puts $H_s+D_t$ into $D_t$. The swap moves that sum into $H_s$ and puts the old $H_s$ into $D_t$. The last update subtracts the old $H_s$ from $D_t$, which restores $D_t$. Only the swap moves fields, so each 1 of $\Pi$ costs exactly one interchange. The shear therefore uses as many interchanges as the rank of $A$, not one for each entry of $A$.

The shear is realized in a [Linear network with restored auxiliary values](linear-network-exchange.md), which restores every auxiliary value it uses, so the array holds only the updated fields when the shear ends.

The bit procedure, which interchanges two equal address chunks on tape using a fixed bit network, has an endpoint operator that is a shear of this form. <cite data-source="paper">two fields, written as vectors $H,D$ over a common residue ring, are updated by $(H,D)\mapsto(H+D,D)$</cite>.
