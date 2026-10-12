Address shear is the map that sends two address fields $H$ and $D$, which are vectors of residues, to $H + D$ and $D$; it is the form the bit procedure's endpoint operator takes. <cite data-source="paper">two fields, written as vectors H, D over a common residue ring, are updated by (H, D) 7→ (H + D, D)</cite>

Entries are residues modulo a common integer, so $H + D$ is computed entry by entry modulo that integer. For example, with modulus 5, $H = (1, 2)$ and $D = (3, 4)$ give $H + D = (4, 1)$, while $D$ is unchanged.

The map is additive and invertible: subtracting $D$ from its first field recovers $H$, so the inverse is the same kind of update with a minus sign.

Address shear is implemented by a small number of [Address-field interchange](address-interchange.md) steps. The shear alone does not swap $H$ and $D$. <cite data-source="paper">Two further linear-cost address updates complete their interchange.</cite>

An endpoint operator relates the stored array at the start of a route through a network to the stored array at its end. For the bit procedure, the endpoint operator of a route through a [Linear networks and frames](linear-network-frames.md) is an address shear.
