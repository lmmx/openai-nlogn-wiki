A simultaneous butterfly layer applies the [butterfly operation](butterfly-operation.md) to one selected address bit of every record at once. The transform layers of the multiplication algorithm are built from such layers, and their tape cost is what saves a power in the target result.

An address chunk is a block of consecutive address bits. Here $d$ is the largest number of equal-width address chunks a layer acts on, and $D \le d$ is the number used in one layer; the layer selects the same bit position in each of those $D$ chunks.

Each record is a polynomial with complex fixed-point coefficients, meaning each coefficient is stored with a fixed number of binary places. The layer is the tensor product of the [butterfly operation](butterfly-operation.md) on the $D$ selected bits, acting on each coefficient separately and leaving the other address bits unchanged. Applying the factors one at a time would need one pass over the whole array per selected bit.

Its cost is $O(Vd^{\lambda'})$ for a fixed exponent $\lambda'<1$, where $V$ is the logical volume, the number of stored data bits. <cite data-source="paper">the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$</cite>

The bound comes from how the layer is evaluated. The tensor product is written using smaller groups of selected bits, joined by binary changes of basis, and each change of basis is performed by moving whole address chunks. The layer computes its chunk moves by the [linear network with restored auxiliary values](linear-network-exchange.md), which exchanges banks of values with prescribed signs. Splitting complete rows among the network's roles reduces the volume each recursive call handles, which gives the power saving.

Intermediate values are exact Gaussian dyadics: complex numbers whose real and imaginary parts are dyadic rationals. Because the butterfly divides by two, the coefficients need these exact denominators rather than rounding at each step. A single truncation, discarding binary digits beyond the fixed precision, follows the completed layer.
