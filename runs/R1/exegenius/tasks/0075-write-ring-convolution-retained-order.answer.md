Convolution with retained transform order convolves two arrays over $\mathbb C[y]/(y^r+1)$ by transforming each one, multiplying the transforms entry by entry, and transforming back, without sorting the frequency entries in between. The main result reduces integer multiplication to this convolution.

This convolution computes its transforms by [Synthetic polynomial transforms](synthetic-transforms.md), which need only signed shifts, address rearrangements and butterflies.

Let $f$ and $g$ be the two input arrays. Let $\mathcal{D}$ be the forward transform applied to each. Let $\mathcal{D}^{+}$ be the opposite transform. Here $M$ is a known scalar, fixed by the normalization of the transforms. With $\odot$ the entrywise product of ring elements at the same address, the first identity below is the convolution theorem with a scalar, and the second says that $\mathcal{D}^{+}$ inverts $\mathcal{D}$ up to $M$:

$$\mathcal{D}(f*g)=M\,(\mathcal{D}f)\odot(\mathcal{D}g), \qquad \mathcal{D}^{+}\mathcal{D}=\tfrac{1}{M}\,I.$$

The second identity is checked by expanding the finite sums of the transform <cite data-source="paper">To check normalization, expansion of the finite sums gives</cite>.

Let $L$ be the permutation of addresses that the forward transform applies to its output, so that the frequency order is the order of those addresses. Let $k$ index the frequency entries, the positions in that order. If the two forward transforms ordered their outputs differently, the entry at position $k$ of $\mathcal{D}f$ would be multiplied by an entry of $\mathcal{D}g$ at a different frequency, and a sort would be needed to align them. Both forward transforms therefore store their outputs in order $L$, so the stored arrays are $L\mathcal{D}f$ and $L\mathcal{D}g$, and the two forward transforms keep the same frequency order through the pointwise product <cite data-source="paper">retain the same frequency order through their pointwise product, and</cite>.

Since $L$ moves entries by address and each product entry uses only the two entries at its address, the product of the stored arrays equals $L$ applied to the product of the transforms:

$$(L\mathcal{D}f)\odot(L\mathcal{D}g)=L\big((\mathcal{D}f)\odot(\mathcal{D}g)\big).$$

The opposite transform applies $L^{-1}$ first, so the $L$ cancels and no sort is run. The opposite transform consumes that order <cite data-source="paper">the opposite transform consumes that order</cite>.

$$\mathcal{D}^{+}L^{-1}\big((L\mathcal{D}f)\odot(L\mathcal{D}g)\big)=\mathcal{D}^{+}\big((\mathcal{D}f)\odot(\mathcal{D}g)\big)$$

By the first identity, the right-hand side is $f*g$ up to a known scalar, because $\mathcal{D}^{+}$ inverts $\mathcal{D}$ up to $M$. For example, if $L$ swaps two records, $L^{-1}$ swaps them back before $\mathcal{D}^{+}$ acts.

This convolution computes its products through [Signed coefficient packing (Kronecker substitution)](signed-packing.md): polynomial products are packed into integers and multiplied by the ordinary $O(n\log n)$ multiplier as a subroutine.

This convolution is applied after [Gaussian resampling](gaussian-resampling.md), which writes each source transform through a power-of-two tensor transform. This convolution is taken over the ring from the [Last-coordinate phase twist](phase-twist-convolution.md), in which the negative wrap gives the original cyclic wrap.
