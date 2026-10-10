A dyadic rational is a number of the form $a / 2^k$ with $a$ an integer and $k \ge 0$. A Gaussian dyadic number is a complex number $x + iy$ whose real part $x$ and imaginary part $y$ are both dyadic rationals. Equivalently, its real and imaginary parts have denominators that are powers of two.

Examples are $\tfrac{1}{2} + \tfrac{3}{4} i$ and $-\tfrac{5}{8}$. Their sums and products are again Gaussian dyadic numbers, because dyadic rationals are closed under addition and multiplication. Division by $2$ keeps a number Gaussian dyadic, which is what the butterfly map $H_0$ uses: it computes $(u+v)/2$ and $(u-v)/2$.

The paper uses these numbers because they are exact. A value of this form has a finite binary expansion, so it can be stored and combined on a tape without rounding. The only rounding in the layer is a single truncation after the whole layer is complete.

This property is why the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) can keep intermediate values exact. The paper describes them as exact Gaussian dyadics whose real and imaginary parts have power-of-two denominators, with a single truncation after the completed layer.
