Convolution with retained transform order convolves two arrays over $\mathbb C[y]/(y^r+1)$ by transforming each one, multiplying the transforms entry by entry, and transforming back, without sorting the frequency entries in between. It is the convolution that the fast tape layouts of the main result run on the remaining axes. This convolution computes its transforms by [Synthetic polynomial transforms](synthetic-transforms.md), which need only signed shifts, address rearrangements and butterflies.

Let $\phi$ and $\psi$ be the two input arrays. Let $\ast$ denote their cyclic convolution on one axis of length $t$, with products taken in the ring:

$$(\phi\ast\psi)_k=\sum_{i+j\equiv k \pmod t}\phi_i\psi_j.$$

The forward transform $\mathcal D$ sends an array to $(\mathcal D\phi)_m=\sum_i\omega^{mi}\phi_i$, where $\omega$ is the primitive $t$th root of unity of the ring and $m$ is the frequency index. Let $\mathcal D^{+}$ be the opposite transform. Let $M$ be the known scalar fixed by the normalization of the transforms. Let $\odot$ be the entrywise product of ring elements at the same address.

Expanding the sums gives the first identity up to the normalization: $\sum_k\omega^{mk}(\phi\ast\psi)_k=\sum_{i,j}\omega^{m(i+j)}\phi_i\psi_j=(\mathcal D\phi)_m(\mathcal D\psi)_m$, because $\omega^{mk}$ depends only on $k$ mod $t$. With the normalization of the source,

$$\mathcal{D}(\phi\ast\psi)=M\,(\mathcal{D}\phi)\odot(\mathcal{D}\psi), \qquad \mathcal{D}^{+}\mathcal{D}=\tfrac{1}{M}\,I.$$

The second identity is the inverse relation that the normalization fixes, and the source checks it by expanding the finite sums <cite data-source="paper">To check normalization, expansion of the finite sums gives</cite>.

Let $\chi$ be the permutation of addresses that the layout of the forward transforms fixes: the entry for frequency $m$ is stored at address $\chi(m)$, so the stored arrays are $\chi\mathcal{D}\phi$ and $\chi\mathcal{D}\psi$. The source also composes $\chi$ with a fixed relabelling of frequencies; the argument needs only that both forward transforms use the same $\chi$. Both forward transforms therefore use $\chi$, so the two forward transforms keep the same frequency order through the pointwise product <cite data-source="paper">retain the same frequency order through their pointwise product, and</cite>. Without this, the entry at frequency $m$ of $\mathcal D\phi$ would meet an entry of $\mathcal D\psi$ at a different frequency, and a sort would be needed to align them.

Since $\chi$ moves entries by address and each product entry uses only the two entries at its address, the product of the stored arrays equals $\chi$ applied to the product of the transforms:

$(\chi\mathcal{D}\phi)\odot(\chi\mathcal{D}\psi)=\chi\big((\mathcal{D}\phi)\odot(\mathcal{D}\psi)\big)$.

The opposite transform takes the stored product and first applies $\chi^{-1}$, so the $\chi$ cancels and no sort is run. This is the step the source describes as the <cite data-source="paper">opposite transform consumes that order</cite>:

$\mathcal{D}^{+}\chi^{-1}\big((\chi\mathcal{D}\phi)\odot(\chi\mathcal{D}\psi)\big)=\mathcal{D}^{+}\big((\mathcal{D}\phi)\odot(\mathcal{D}\psi)\big)$.

By the first identity and the second, the right side is $\frac{1}{M^{2}}\,(\phi\ast\psi)$, a known scalar multiple of the convolution. For example, if $\chi$ swaps two records, $\chi^{-1}$ swaps them back before $\mathcal{D}^{+}$ acts.

This convolution computes its products through [Signed coefficient packing (Kronecker substitution)](signed-packing.md): polynomial products are packed into integers and multiplied by the ordinary $O(n\log n)$ multiplier as a subroutine.

This convolution is applied after [Gaussian resampling](gaussian-resampling.md), which writes each source transform through a power-of-two tensor transform. This convolution is taken over the ring from the [Last-coordinate phase twist](phase-twist-convolution.md), in which the negative wrap gives the original cyclic wrap.
