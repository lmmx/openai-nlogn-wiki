The logical bit volume is the size measure in which the paper states its cost bounds: <cite data-source="paper">We will obtain cost O(V dλ ), with λ′ < 1 and V the logical bit volume</cite>. The [rank-saving recursion](rank-saving-recursion.md) step relies on this count when it shows that each recursive level saves a strict power.

The logical bit volume $\Upsilon$ counts the bits of the [padded transform box](padded-transform-box.md), with every entry at its record width. Here $Q$ is the number of entries in the box and $\chi$ is the record width, the number of bits in one record of the box, so

$$\Upsilon = Q\chi.$$

For example, a box with $Q=4$ entries, each record $\chi=8$ bits wide, has $\Upsilon = 4 \cdot 8 = 32$ bits. An entry that holds only padding zeros still counts at its full width.

The paper writes $V$ for this quantity. For a padded array whose coefficients have fixed-width formats, <cite data-source="paper">so a full padded array has Θ(V ) stored bits.</cite>
