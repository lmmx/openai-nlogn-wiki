The address shear is the map that replaces one address field by its sum with a second field and leaves the second field unchanged. It is the endpoint operator of the bit procedure, and it is one of the linear-cost address updates that interchange two address fields.

Write $H$ and $D$ for the two address fields, each a vector whose entries lie in a common residue ring, that is, in the integers modulo some fixed modulus. The shear is the map

$$(H,D)\mapsto(H+D,\,D),$$

which adds $D$ entrywise to $H$ and leaves $D$ fixed. It is linear in the pair $(H,D)$, and it is invertible: applying $(H,D)\mapsto(H-D,\,D)$ returns the original pair.

Worked example, with modulus $10$: take $H=(3,7)$ and $D=(5,5)$. The shear gives $H+D=(8,2)$, since $7+5=12\equiv 2$, so the pair becomes $((8,2),(5,5))$. The inverse map recovers $(3,7)$.

A single shear does not swap $H$ and $D$. Interchanging the two fields takes three linear-cost address updates in all, of which the shear is one. The two further linear-cost updates <cite data-source="paper">complete their interchange.</cite>

The shear is applied in the [linear network](linear-network.md) of the bit procedure, at its endpoint. It acts on fields stored in the [frame of a vertex](frame.md) at that terminal.
