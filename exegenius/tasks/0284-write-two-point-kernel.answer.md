A two-point kernel is the $2\times 2$ operator that acts on the two entries of an array whose addresses differ in one bit. The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) uses such kernels: its phase frames are written as a <cite data-source="paper">product of two-point kernels on selected directions</cite>.

Let $d$ be the number of bits in a binary address. An address is an integer $\nu$ with $0\le\nu<2^d$, whose binary form has $d$ bits. A bit position is an index $e$ with $0\le e<d$, counted from the least significant bit. Write $\oplus$ for bitwise exclusive or, so $\nu\oplus 2^e$ is the address $\nu$ with bit $e$ changed and the other bits kept. Let $\chi$ be an array of complex values, with one entry $\chi(\nu)$ for each address $\nu$.

Here the letter $X$ changes meaning: it is the bit flip $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which interchanges the two entries of a pair. Let $\delta$ and $\kappa$ be complex numbers, the coefficients of $I$ and of $X$ in a $2\times 2$ matrix.

We write $K=\delta I+\kappa X$ for the matrix of the two-point kernel. The kernel $K$ is a matrix as defined in [Linear algebra basics](linear-algebra-basics.md). Explicitly,
$$K=\begin{pmatrix}\delta&\kappa\\ \kappa&\delta\end{pmatrix}.$$

The kernel along bit $e$ is the operator $K_e$ that replaces $\chi$ by $K_e\chi$, where
$$(K_e\chi)(\nu)=\delta\,\chi(\nu)+\kappa\,\chi(\nu\oplus 2^e).$$
Equivalently, for every address $\nu$, the pair of entries at $\nu$ and $\nu\oplus 2^e$ is multiplied by $K$:
$$\begin{pmatrix}(K_e\chi)(\nu)\\ (K_e\chi)(\nu\oplus 2^e)\end{pmatrix}=\begin{pmatrix}\delta&\kappa\\ \kappa&\delta\end{pmatrix}\begin{pmatrix}\chi(\nu)\\ \chi(\nu\oplus 2^e)\end{pmatrix}.$$
All other bits of the address are unchanged, so the kernel acts only along bit $e$.

**Example.** Take $d=1$, so the addresses are $0$ and $1$, and take $\delta=\frac{1+i}{2}$ and $\kappa=\frac{1-i}{2}$. For $\chi(0)=1$ and $\chi(1)=0$, the formula gives $(K_0\chi)(0)=\delta\cdot 1+\kappa\cdot 0=\frac{1+i}{2}$ and $(K_0\chi)(1)=\delta\cdot 0+\kappa\cdot 1=\frac{1-i}{2}$. Applying the kernel twice along the same bit gives $K^2=(\delta^2+\kappa^2)I+2\delta\kappa X$, because $X^2=I$. Here $\delta^2+\kappa^2=\frac{i}{2}-\frac{i}{2}=0$ and $2\delta\kappa=2\cdot\frac{1}{2}=1$, so $K^2=X$. Two applications therefore swap the two entries, which is the bit flip. Check: applying $K$ to $(\delta,\kappa)$ gives $(\delta^2+\kappa^2,\,2\delta\kappa)=(0,1)$, which is $X$ applied to $(1,0)$.

The kernel $K$ has coefficients that are [Gaussian dyadics](gaussian-dyadics.md) when $\delta$ and $\kappa$ are. The kernels used in the paper <cite data-source="paper">have Gaussian dyadic coefficients</cite>, so the values computed with them stay exact.
