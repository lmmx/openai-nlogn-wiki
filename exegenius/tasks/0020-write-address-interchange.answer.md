Fast address interchange is a tape procedure that swaps two disjoint contiguous address fields of an array, and its cost bound is what lets the recursion in [Recursive power saving](recursive-power-saving.md) save a power. An address field is a block of consecutive address bits.

$V$ is the stored bit volume: the number of data bits the array holds. $u$ is the width of each field: the number of address bits in one field. $\tau$ is a fixed exponent with $0<\tau<1$. For example, with $u=2$, an address whose two fields hold $01$ and $10$ becomes one whose fields hold $10$ and $01$.

Swapping two fields of width $u$ in an array of volume $V$ costs $O(Vu^\tau)$ time. <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>

The procedure is applied to each [Address shear](address-shear.md) that a layer produces, and each shear takes as many interchanges as its rank. It runs the [Linear network with restored auxiliary values](linear-network-exchange.md), whose gates act on the stored array and restore every auxiliary value. Its intermediate steps are pointwise XOR combinations of data. The result does not depend on the values held in auxiliary storage when the procedure starts. <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

The claim is shown by writing the interchange as a linear network whose XOR intermediate values cancel, so its tape cost follows from the recurrence that the network yields.
