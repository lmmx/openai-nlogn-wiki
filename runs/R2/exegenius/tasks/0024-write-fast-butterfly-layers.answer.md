Fast simultaneous butterfly layers is a fixed-tape procedure that applies the butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit position in several address chunks at once. The multiplication algorithm needs it because applying the butterflies one at a time would cost one whole-array pass for each.

## The layer

Let $D$ be the number of selected address chunks. Let $d$ be an upper bound on $D$, so $D\le d$. Let $K$ be the number of bits in each chunk. Let $V$ be the number of stored bits. Let $\lambda'<1$ be a fixed exponent. The address set is the unselected bits together with the $D$ chunks, in lexicographic order. Each address holds a polynomial record with $r$ coefficients, and $H_0$ combines pairs of records coefficientwise, leaving every other address bit unchanged. The cost is $O(Vd^{\lambda'})$.

## Method

Let $X$ be the bit-flip matrix. Let $\mathsf S$ be the diagonal phase matrix $\operatorname{diag}(1,i)$. Let $C=\tfrac12\bigl((1+i)I+(1-i)X\bigr)$ be the two-point kernel. Then $H_0=\tfrac{1-i}{2}\,\mathsf S C\mathsf S$ and $C^2=X$. So each butterfly is the kernel $C$ between two diagonal phases, and $D$ selected bits give $H_0^{\otimes D}$ equal to a scalar times $\mathsf S^{\otimes D}C^{\otimes D}\mathsf S^{\otimes D}$. The phases act on each coefficient with work linear in its width, so the cost lies in computing $C^{\otimes D}$.

The tensor product $C^{\otimes D}$ is computed recursively. The layer moves whole chunks by [Fast interchange of address fields](fast-address-interchange.md) to bring each group of selected bits to a common offset. The smaller products are applied to disjoint halves of the rows, and the moves are then undone. The layer gets its exponent $\lambda'<1$ from [Recursive power saving from s<Wm](recursive-power-saving.md), since each recursive call uses fewer calls on less volume. The layer is built from the root multiplications of [Synthetic polynomial transforms](synthetic-transforms.md), which are signed shifts.

For $D=2$ and records $f_{00},f_{01},f_{10},f_{11}$ indexed by the two selected bits, the output at index $00$ is $(f_{00}+f_{01}+f_{10}+f_{11})/4$.

## Exactness

A Gaussian dyadic is a complex number whose real and imaginary parts have power-of-two denominators. Each factor $H_0$ adds at most one binary digit to the denominators, and the coefficients stay in the unit disk, so every intermediate value is an exact Gaussian dyadic. <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>. <cite data-source="paper">The procedure evaluates the entire layer exactly before this final truncation.</cite> The layer's single truncation is bounded as in [Fixed-point precision and exact recovery](fixed-point-precision.md).
