A two-point kernel is the $2\times 2$ operator that acts on the two entries of an array whose addresses differ in one bit. The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) is built from such kernels: in the paper *Integer multiplication below n log n*, its [phase frames](phase-factor.md) are written as a <cite data-source="paper">product of two-point kernels on selected directions</cite>.

Letters on this page have the meanings given here, not those they have on other pages. Let $d$ be the number of bits in a binary address. An address is an integer $\nu$ with $0\le\nu<2^d$, written in binary with $d$ bits. A bit position is an index $e$ with $0\le e<d$, counted from the least significant bit. Write $\oplus$ for bitwise exclusive or, so $\nu\oplus 2^e$ is the address $\nu$ with bit $e$ changed and the other bits kept. Let $\chi$ be an array of complex values, one entry $\chi(\nu)$ for each address $\nu$.

Here $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is the bit flip, which interchanges the two entries of a pair. Let $\delta$ and $\kappa$ be complex numbers, the coefficients of $I$ and of $X$ in the kernel. The two-point kernel is the matrix $K=\delta I+\kappa X$, where $I$ is the $2\times 2$ identity matrix:
$$K=\begin{pmatrix}\delta&\kappa\\ \kappa&\delta\end{pmatrix}.$$
The kernel $K$ is a matrix as defined in [Linear algebra basics](linear-algebra-basics.md).

The kernel along bit $e$ is the operator $K_e$ defined by the formula below:
$$(K_e\chi)(\nu)=\delta\,\chi(\nu)+\kappa\,\chi(\nu\oplus 2^e).$$
Equivalently, for every address $\nu$, the pair of entries at $\nu$ and $\nu\oplus 2^e$ is multiplied by $K$:
$$\begin{pmatrix}(K_e\chi)(\nu)\\ (K_e\chi)(\nu\oplus 2^e)\end{pmatrix}=K\begin{pmatrix}\chi(\nu)\\ \chi(\nu\oplus 2^e)\end{pmatrix}.$$
All other bits of the address are unchanged, so the kernel acts only along bit $e$.

**Example.** Take $d=1$, so the addresses are $0$ and $1$, and take $\delta=\frac{1+i}{2}$ and $\kappa=\frac{1-i}{2}$. For $\chi(0)=1$ and $\chi(1)=0$, the formula gives $(K_0\chi)(0)=\delta\cdot 1+\kappa\cdot 0=\frac{1+i}{2}$ and $(K_0\chi)(1)=\delta\cdot 0+\kappa\cdot 1=\frac{1-i}{2}$. Since $X^2=I$, the square of the kernel is $K^2=(\delta^2+\kappa^2)I+2\delta\kappa X$. Here $\delta^2+\kappa^2=\frac{i}{2}-\frac{i}{2}=0$ and $2\delta\kappa=2\cdot\frac{1}{2}=1$, so $K^2=X$. Applying the kernel twice along the same bit therefore swaps the two entries, which is the bit flip.

The kernel $K$ has coefficients in [Gaussian dyadics](gaussian-dyadics.md) when $\delta$ and $\kappa$ are. Sums and products of Gaussian dyadics are again Gaussian dyadics, so a computation that uses only Gaussian dyadic coefficients is exact and involves no rounding. A kernel is multiplied by a [phase factor](phase-factor.md), such as $i$, and its coefficients remain Gaussian dyadic. The paper uses kernels of this kind, and <cite data-source="paper">kernels implemented below have Gaussian dyadic coefficients</cite>, so the values computed with them stay exact.
