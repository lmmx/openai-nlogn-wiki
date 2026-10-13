The address shear is the permutation of array entries that replaces one address field by its sum with a second field and leaves the second field unchanged. It is the endpoint operator of the bit procedure, the version of the construction that works on single bits through XOR gates, and it is one of the linear-cost address updates that interchange two address fields.

Write $H$ for the first address field and $D$ for the second, each a vector whose entries lie in a common residue ring $\mathbb{Z}/q\mathbb{Z}$, the integers modulo a fixed modulus $q$. The shear is

$$(H,D)\mapsto(H+D,\,D),$$

which adds $D$ entrywise to $H$ and leaves $D$ fixed. It is linear and invertible: $(H,D)\mapsto(H-D,\,D)$ undoes it.

Worked example, with $q=10$: take $H=(3,7)$ and $D=(5,5)$. Then $H+D=(8,2)$, since $7+5=12\equiv 2$, so the pair becomes $((8,2),(5,5))$. Applying the inverse recovers $(3,7)$.

A single shear does not swap $H$ and $D$. The swap uses three updates in order: $D\leftarrow D-H$, then the shear $H\leftarrow H+D$, then $D\leftarrow H-D$. Starting from $(H,D)$ these give $(H,\,D-H)$, then $(D,\,D-H)$, then $(D,\,H)$.

Only the middle shear moves entries between addresses. The network performs it by splitting rows into role streams, applying its gates pointwise at matching addresses, and merging the rows back. The two outer updates only change $D$ by a subtraction, and they cost linear time per unit volume. <cite data-source="paper">The other two updates target the later group and have linear cost.</cite>

The shear is applied in the [linear network](linear-network.md) of the bit procedure, at its endpoint. It acts on fields stored in the [frame of a vertex](frame.md) at that terminal, so the $H$ and $D$ it updates are the address fields as they are stored there.
