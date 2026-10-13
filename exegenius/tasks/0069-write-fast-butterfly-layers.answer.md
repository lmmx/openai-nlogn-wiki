Fast simultaneous butterfly layers is a fixed-tape procedure that applies $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit position in several address chunks at once, where $u$ and $v$ are the two records at addresses that differ only in the selected bit and $H_0$ combines them coefficientwise. Applied one at a time, the butterflies would cost one whole-array pass each. The layer performs the butterfly rounds of [Synthetic polynomial transforms](synthetic-transforms.md).

## The layer

Let $D$ be the number of selected address chunks, and let $d$ be an upper bound on $D$, so $D\le d$. Each chunk has $K$ bits, and the selected bit has one common offset. The width of a coefficient is its number of stored bits, $O(p)$ per real or imaginary component. The layer leaves the other address bits unchanged and costs $O(Vd^{\lambda'})$ for a fixed exponent $\lambda'<1$.

## Method

Let $X$ be the bit-flip matrix. Here $i$ is the imaginary unit, so the letter changes meaning here. Let $\Phi=\operatorname{diag}(1,i)$ be the diagonal phase matrix. Let $C=\tfrac12\bigl((1+i)I+(1-i)X\bigr)$ be the two-point kernel. Direct multiplication gives

$$H_0=\tfrac{1-i}{2}\,\Phi C\Phi.$$

So each butterfly is the kernel $C$ between two phases. Multiplying by a power of $i$ only swaps and negates real and imaginary parts, at cost linear in the coefficient width. The tensor product of matrices, written $\otimes$, replaces each entry of the first matrix by that entry times the second matrix, so $C^{\otimes D}$ is a $2^D\times 2^D$ matrix on the $D$ selected bits. Applying the identity to each selected bit gives

$$H_0^{\otimes D}=\left(\tfrac{1-i}{2}\right)^{D}\Phi^{\otimes D}\,C^{\otimes D}\,\Phi^{\otimes D},$$

so the cost lies in computing $C^{\otimes D}$.

The layer computes $C^{\otimes D}$ recursively. A group of $mf$ selected bits is split into $m$ slots of $f$ bits, and the layer moves whole chunks by [Fast interchange of address fields](fast-address-interchange.md) to realize its binary basis changes. A network of these changes turns $C^{\otimes mf}$ into $s$ child calls, each computing $C^{\otimes f}$ on one slot. Splitting the rows among the network's $W$ wires gives each child $1/W$ of the volume. Writing $T(f)$ for normalized cost at parameter $f$, $T(mf)\le (s/W)\,T(f)+O(1)$. The network satisfies $s/W<m^{\sigma}$ for a fixed exponent $\sigma=1-2^{-50}$. <cite data-source="paper">For both recurrences we may use the fixed rational exponent</cite>. Unrolling over the $\log_m d$ levels, $T(d)$ grows no faster than $d^{\sigma}$. The layer gets its exponent $\lambda'<1$ from [Recursive power saving from s<Wm](recursive-power-saving.md), taking $\lambda'$ above $\sigma+\tfrac12(1-\sigma)$.

## Exactness

A Gaussian dyadic is a complex number whose real and imaginary parts have power-of-two denominators. Each entry of $C$ is $\tfrac{1\pm i}{2}$, so each selected bit adds one binary digit to the denominators. <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>. Because $C$ is unitary, a coefficient can exceed modulus 1 mid-computation, so the procedure carries $O(p)$ extra fractional bits. The final values stay in the unit disk, because one butterfly maps moduli at most 1 to $(|u|+|v|)/2\le 1$.

<cite data-source="paper">A single truncation follows the completed contractive layer.</cite> This truncation keeps error within the bound of [Fixed-point precision and exact recovery](fixed-point-precision.md).
