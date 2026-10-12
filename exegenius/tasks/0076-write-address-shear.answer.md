Address shear is the map that sends two address fields $H$ and $D$, which are vectors of residues, to $H + D$ and $D$. It is the endpoint update of the bit procedure, the paper's version of the construction for binary integers rather than complex numbers.

Entries are residues modulo a common integer, so $H + D$ is computed entry by entry modulo that integer. For example, with modulus 5, $H = (1, 2)$ and $D = (3, 4)$ give $H + D = (4, 1)$, while $D$ is unchanged.

The map is invertible: subtracting $D$ from its first field recovers $H$, so the inverse is the same kind of update with a minus sign.

An endpoint operator relates the stored array at the start of a route through a network to the stored array at its end. For the bit procedure, the address shear is the endpoint operator of a route through a [Linear networks and frames](linear-network-frames.md). <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors H, D over a common residue ring, are updated by (H, D) 7→ (H + D, D).</cite>

Address shear is the first of three address updates in an [Address-field interchange](address-interchange.md). <cite data-source="paper">Two further linear-cost address updates complete their interchange.</cite> The shear alone does not swap $H$ and $D$.
