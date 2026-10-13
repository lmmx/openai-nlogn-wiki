Fast simultaneous butterfly layers is a fixed-tape procedure that applies $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit position in several address chunks at once. Here $u$ and $v$ are the paired records. The layer performs the butterfly rounds of [Synthetic polynomial transforms](synthetic-transforms.md), which otherwise needs one whole-array pass per butterfly.

## The layer

Let $D$ be the number of selected address chunks, and let $d$ be an upper bound on $D$, so $D\le d$. Each chunk consists of $K$ consecutive address bits, and the selected bit sits at one common offset in every chunk. Each record has complex fixed-point coefficients with $O(p)$ bits per component, where $p$ is the working precision. The layer costs $O(Vd^{\lambda'})$ for a fixed exponent $\lambda'<1$, where $V$ is the stored bit volume.

## Method

Here $i$ is the imaginary unit, so the letter changes meaning here. Let $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ be the bit-flip matrix. Let $\Phi=\operatorname{diag}(1,i)$ be the diagonal phase matrix. Let $C=\tfrac12\bigl((1+i)I+(1-i)X\bigr)$ be the two-point kernel; the letter $C$ changes meaning here. Since $H_0=\tfrac{1-i}{2}\,\Phi C\Phi$ and tensor powers respect products,

$$H_0^{\otimes D}=\left(\tfrac{1-i}{2}\right)^{D}\Phi^{\otimes D}\,C^{\otimes D}\,\Phi^{\otimes D}.$$

Multiplying by $\Phi^{\otimes D}$ only permutes and negates real and imaginary parts, so the work lies in $C^{\otimes D}$.

The layer computes $C^{\otimes D}$ recursively. Group $mf$ selected bits into $m$ slots of $f$ bits. The phase identities for $C$ reduce this group to $s$ child calls, each computing $C^{\otimes f}$ on one slot, with $s<Wm$. The data sits on $W$ roles (wires) of a [Finite linear network with roles and frames](linear-network-roles.md), and splitting the rows evenly gives each child $1/W$ of the volume. The layer moves whole chunks by [Fast interchange of address fields](fast-address-interchange.md) to realize its binary basis changes. With $T(f)$ the normalized cost (time divided by volume), each child costs $(V/W)\,T(f)$, and the node's outside work is $O(VK^{\tau})$ for its chunk exchanges, with $\tau<1$, plus linear copying. Dividing by $V$,

$$T(mf)\le \tfrac{s}{W}\,T(f)+O\bigl((mfK)^{\tau}+1\bigr).$$

The fixed exponent $\sigma=1-2^{-50}$ gives $s/W<m^{\sigma}$, because $s/W$ is $m$ times one minus a tiny fraction. For this network the source computes $\frac{Wm-s}{Wm}=\frac{73}{19906842167500}$, which exceeds $20\cdot2^{-50}$ <cite data-source="paper">Both exact deficits displayed above are greater than $20\cdot2^{-50}$</cite>. Since $m<2^{20}$ gives $\log m<20$,

$$m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m\Bigl(1-\tfrac{73}{19906842167500}\Bigr)=\frac{s}{W}.$$

[Recursive power saving from s<Wm](recursive-power-saving.md) turns such a recursion into a power saving. Unroll it over $\lceil\log_m d\rceil$ levels, stopping at groups of fewer than $\sqrt d$ bits, which apply their kernels one at a time. Internal overheads form a geometric series, summing to $O(d^{\lambda})$ with $\lambda<1$. A leaf after $j$ levels has $u=d/m^j<\sqrt d$ chunks, and its share is at most $(s/W)^j u\le (d/u)^{\sigma}u=d^{\sigma}u^{1-\sigma}\le d^{\sigma+\frac12(1-\sigma)}$. The layer gets its exponent $\lambda'<1$ from [Recursive power saving from s<Wm](recursive-power-saving.md), taking $\lambda'$ above $\sigma+\tfrac12(1-\sigma)$.

## Exactness

A Gaussian dyadic is a complex number whose real and imaginary parts have power-of-two denominators. Each entry of $C$ is $\tfrac{1\pm i}{2}$, so each selected bit adds one binary digit to the denominators. <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>.

A unitary matrix preserves the Euclidean length of every pair of values, and here $C=\sqrt2H_0\,\Phi\,\sqrt2H_0$ is a product of unitary matrices, so $C^{\otimes D}$ preserves the norm of each block of $2^D$ entries. If the inputs have modulus at most 1, the block norm is at most $2^{D/2}$, so intermediate moduli are at most $2^{D/2}\le 2^{d/2}$. The final factor $\bigl(\tfrac{1-i}{2}\bigr)^{D}$ has modulus $2^{-D/2}$, so the outputs stay in the unit disk. These fit the $O(p)$ widths <cite data-source="paper">these widths are $O(p)$</cite>.

The layer evaluates exactly and truncates once, toward zero to multiples of $2^{-p}$, with error below $\sqrt2\,2^{-p}$ in maximum norm. This single truncation keeps error within the bound of [Fixed-point precision and exact recovery](fixed-point-precision.md), which needs error below $1/2$.
