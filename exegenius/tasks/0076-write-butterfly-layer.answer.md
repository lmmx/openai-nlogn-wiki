The simultaneous butterfly layer $H_0$ applies a two-point butterfly to one selected address bit of every chunk in one pass. It is the basic step of the transforms used in the multiplication algorithm, which need many address bits transformed at once.

A butterfly on one bit takes two values $u$ and $v$ at the two addresses that differ only in that bit, and replaces them by $(u+v)/2$ and $(u-v)/2$. An address chunk is a block of consecutive address bits. The layer is the map $H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr)$ applied at once to one selected bit of each of $d$ equal-width chunks, where $d$ is the number of chunks, each with its selected bit at a common offset from the least significant end.

Applying $H_0$ to all $d$ selected bits is the [Tensor product](tensor-product.md) of the $d$ single-bit butterflies, so the result equals applying them one at a time in any order, and the other address bits are unchanged.

The layer acts on arrays stored in the [Frame of a vertex](frame.md) on each wire. Each address holds a polynomial record of $r$ complex coefficients, where $r$ is the number of complex coefficients in a record. $H_0$ acts coefficientwise, so each coefficient of $u$ is combined with the matching coefficient of $v$. For $u=1+i$ and $v=1-i$ the output pair is $(1,\,i)$, since $(u+v)/2=1$ and $(u-v)/2=i$.

Intermediate values in the layer are exact [Gaussian dyadic numbers](gaussian-dyadic.md), whose real and imaginary parts have power-of-two denominators.

The cost model counts tape operations on the fixed-tape machine, with $V$ the stored volume. The arithmetic is pointwise: each pair of coefficients takes a fixed number of exact operations, so it costs $O(V)$ in total. The rest of the cost is moving each selected bit to where it is combined. That address movement is bounded in [Fast interchange of address chunks](tape-interchange.md), and the layer costs $O(Vd^{\lambda'})$ <cite data-source="paper">the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$</cite>, where $\lambda'<1$ is a fixed exponent. Since $d^{\lambda'}<d$, this is cheaper than the $d$ whole-array passes that separate single-bit butterflies would take, each costing $O(V)$.
