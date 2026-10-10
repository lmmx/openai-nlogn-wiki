Index coding is a setting in which a sender broadcasts values that receivers already partly know, and decoding means a receiver recovers the value it wants. Linear index-code decoding uses linear combinations for this recovery.

Suppose a receiver wants a coordinate $x_1$ and holds side information about its neighbours. The sender transmits a low-rank linear summary of several coordinates. This summary contains $x_1$ together with contributions from neighbouring coordinates $x_2, x_3, \dots$. The receiver already knows those neighbouring coordinates, so it can compute their contributions and subtract them. What remains is the wanted coordinate.

As a small example over the rationals, let the summary be $z = x_1 + x_2$, and suppose the receiver knows $x_2 = 3$. Subtracting the known contribution gives $x_1 = z - 3$.

The paper says that the gather and scatter operations, together with the [side wires](side-wire.md), have this form. A low-rank linear summary of the coordinates is formed, and the contributions of known neighbouring coordinates are subtracted, so the wanted coordinate is recovered from its neighbours. This is the decoding structure behind the [gather and scatter operations](gather-scatter.md).
