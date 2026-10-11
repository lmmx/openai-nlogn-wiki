A two-point kernel is a $2\times 2$ operator that acts on the two entries of an array whose addresses differ in one bit. It is the building block of the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md), which applies a butterfly to several selected bits at once: the paper writes the phase identities for such a layer as a <cite data-source="paper">product of two-point kernels on selected directions</cite>.

Let $d$ be the number of bits in an address. An address is an integer $\nu$ with $0\le\nu<2^d$, written in binary with $d$ bits. A bit position is an index $\ell$ with $0\le\ell<d$, counted from the least significant bit as $0$. Write $\oplus$ for bitwise exclusive or, so $\nu\oplus 2^\ell$ is the address $\nu$ with bit $\ell$ changed. Let $\chi$ be an array of complex values, one entry $\chi(\nu)$ for each address $\nu$.

Let $X=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ be the bit flip, which interchanges the two entries of a pair. Let $I$ be the $2\times 2$ identity matrix. Let $p$ and $q$ be complex numbers, the coefficients of $I$ and of $X$. The two-point kernel $A$ is a matrix as defined in [Linear algebra basics](linear-algebra-basics.md), here of size $2\times 2$:
$$A=pI+qX=\begin{pmatrix}p&q\\ q&p\end{pmatrix}.$$

The kernel along bit $\ell$ is the operator $A_\ell$ on arrays defined by
$$(A_\ell\chi)(\nu)=p\,\chi(\nu)+q\,\chi(\nu\oplus 2^\ell).$$
Equivalently, for every address $\nu$, the pair of entries at $\nu$ and $\nu\oplus 2^\ell$ is multiplied by $A$:
$$\begin{pmatrix}(A_\ell\chi)(\nu)\\ (A_\ell\chi)(\nu\oplus 2^\ell)\end{pmatrix}=A\begin{pmatrix}\chi(\nu)\\ \chi(\nu\oplus 2^\ell)\end{pmatrix}.$$
All other bits of the address are unchanged, so the kernel acts only along bit $\ell$.

**Example.** Take $d=1$, so the addresses are $0$ and $1$, and let $p=\frac{1+i}{2}$ and $q=\frac{1-i}{2}$. For $\chi(0)=1$ and $\chi(1)=0$, the formula gives $(A_0\chi)(0)=p\cdot 1+q\cdot 0=\frac{1+i}{2}$ and $(A_0\chi)(1)=p\cdot 0+q\cdot 1=\frac{1-i}{2}$. Since $X^2=I$, we have $A^2=(p^2+q^2)I+2pqX$. Here $p^2+q^2=\frac{i}{2}-\frac{i}{2}=0$ and $2pq=1$, so $A^2=X$. Applying the kernel twice along the same bit therefore interchanges the two entries, which is the bit flip.

The kernel $A$ has coefficients in [Gaussian dyadics](gaussian-dyadics.md) when $p$ and $q$ are. Sums and products of Gaussian dyadics are again Gaussian dyadic, so a computation that uses only such coefficients is exact and involves no rounding. A two-point kernel is scaled by a [Phase factor](phase-factor.md), such as $i$, and its coefficients remain Gaussian dyadic. The paper's kernels are of this kind: the kernels it implements <cite data-source="paper">below have Gaussian dyadic coefficients</cite>, so the values computed with them stay exact.
