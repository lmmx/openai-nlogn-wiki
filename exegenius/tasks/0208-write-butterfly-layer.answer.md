The simultaneous butterfly layer is the map that applies a two-point butterfly to one selected address bit of every chunk in one pass. Here $d$ is the number of chunks, not the number of axes used on the transform page, and the layer is written $B_d$. It is the basic step of the transforms, which need many address bits transformed at once.

The two-point butterfly is $H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr)$. It takes two values $u$ and $v$ at the two addresses that differ only in the selected bit. An address chunk is a block of consecutive address bits. Each chunk has the same width, and the selected bits sit at a common offset from the least significant end. The layer applies $H_0$ to all $d$ selected bits at once.

Applying $B_d$ to all $d$ selected bits is built by the [Tensor product](tensor-product.md) of the $d$ single-bit butterflies, so applying them one at a time in any order gives the same result.

The layer acts on arrays stored in the [Frame of a vertex](frame.md) on each wire. Each address holds a polynomial record of $M$ complex coefficients; $M$ is the number of complex coefficients in a record. $B_d$ acts on each record coefficientwise. For $u=1+i$ and $v=1-i$ the output pair is $(1,\,i)$, since $(u+v)/2=1$ and $(u-v)/2=i$.

The layer computes exactly in [Gaussian dyadic numbers](gaussian-dyadic.md), whose real and imaginary parts have power-of-two denominators, each part stored with $p$ bits after the binary point.

The cost counts tape operations on the stored volume $V$. The exponent $\lambda'<1$ is a fixed constant. The pointwise arithmetic costs $O(V)$, since each pair of coefficients takes a fixed number of exact operations. The rest is address movement by [Fast interchange of address chunks](tape-interchange.md), which moves a group of equal-width chunks by one swap. The layer costs $O(Vd^{\lambda'})$ tape operations, <cite data-source="paper">the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$</cite>.

The proof, in the paper's section on fast butterfly layers, splits the chunks into groups of power-of-base sizes, moves each group with swaps, and sums the costs over $O(\log d)$ levels. The sum is $O(d^{\lambda'})$ for any $\lambda'$ above the swap exponents and below 1. Since $d^{\lambda'}<d$ for $d\ge 2$, this beats the $d$ whole-array passes that separate single-bit butterflies would take, each costing $O(V)$.
