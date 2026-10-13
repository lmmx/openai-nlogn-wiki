Convolution with retained transform order convolves two arrays over $\mathbb C[y]/(y^r+1)$ by transforming each one, multiplying the transforms entry by entry, and transforming back, without sorting the frequency entries in between.

This convolution computes its transforms by [Synthetic polynomial transforms](synthetic-transforms.md), which need only signed shifts, address rearrangements and butterflies.

Let $u$ and $v$ be two input arrays. Let $\mathcal{D}$ be the forward transform applied to each, and $\mathcal{D}^{+}$ the opposite transform, which inverts $\mathcal{D}$ up to a known scalar. The convolution theorem says that after the transform a convolution becomes a pointwise product: $\mathcal{D}(u*v)$ equals $(\mathcal{D}u)\odot(\mathcal{D}v)$ up to a known scalar, where $\odot$ multiplies the ring elements at the same address and $u*v$ is the convolution of $u$ and $v$.

Let $L$ be the permutation of addresses that the forward transform applies to its output, so that the frequency order is the order of those addresses. If the two forward transforms ordered their outputs differently, the product would pair frequency $k$ of $u$ with a different frequency of $v$, and a sort would be needed to align them. Both forward transforms therefore store their entries in the same order, so the stored arrays are $L\mathcal{D}u$ and $L\mathcal{D}v$, and the two forward transforms keep the same frequency order through the pointwise product <cite data-source="paper">retain the same frequency order through their pointwise product, and</cite>.

Since $L$ moves entries by address and each product entry uses only the two entries at its address, the stored product equals $L$ applied to the product of the transforms.

$$(L\mathcal{D}u)\odot(L\mathcal{D}v)=L\big((\mathcal{D}u)\odot(\mathcal{D}v)\big)$$

The opposite transform applies $L^{-1}$ first, so the $L$ cancels and no sort is run. The opposite transform consumes that order <cite data-source="paper">the opposite transform consumes that order</cite>.

$$\mathcal{D}^{+}L^{-1}\big((L\mathcal{D}u)\odot(L\mathcal{D}v)\big)=\mathcal{D}^{+}\big((\mathcal{D}u)\odot(\mathcal{D}v)\big)$$

The right-hand side is $u*v$ up to the known scalar, because $\mathcal{D}^{+}$ undoes $\mathcal{D}$ up to that scalar. For example, if $L$ swaps two records, both stored arrays are swapped, their product is swapped the same way, and $L^{-1}$ swaps it back before $\mathcal{D}^{+}$ acts.

This convolution computes its products through [Signed coefficient packing (Kronecker substitution)](signed-packing.md): polynomial products are packed into integers and multiplied by the ordinary $O(n\log n)$ multiplier as a subroutine.

This convolution is applied after [Gaussian resampling](gaussian-resampling.md), which writes each source transform through a power-of-two tensor transform. This convolution is taken over the ring from the [Last-coordinate phase twist](phase-twist-convolution.md), in which the negative wrap gives the original cyclic wrap.
