Bluestein's chirp identity rewrites a Fourier transform as a convolution, and so converts the middle transform into a [normalized cyclic convolution](cyclic-convolution.md) on the way to the target.

The identity is applied to the middle transform produced by [Gaussian resampling](gaussian-resampling.md), and it keeps the target permutation.

Let $N$ be the number of points in the transform, and let $\omega$ be a primitive $N$-th root of unity. Let $j$ and $k$ be the input and output indices, each running from $0$ to $N-1$. The input is the sequence $x_0,\dots,x_{N-1}$ and its transform is $X_k=\sum_{j=0}^{N-1} x_j\,\omega^{jk}$ for $k=0,\dots,N-1$. 

Choose $\zeta$, a square root of $\omega$, as the chirp base; for $\omega=e^{2\pi i/N}$, $\zeta=e^{\pi i/N}$ works. Since $2jk=j^2+k^2-(k-j)^2$, we have $\omega^{jk}=\zeta^{j^2}\zeta^{k^2}\zeta^{-(k-j)^2}$, and therefore
$$X_k=\zeta^{k^2}\sum_{j=0}^{N-1}\bigl(\zeta^{j^2}x_j\bigr)\,\zeta^{-(k-j)^2}.$$

The factors $\zeta^{j^2}$ before the sum and $\zeta^{k^2}$ after it are chirps, factors whose exponents are quadratic in an index. The sum is a convolution: each term pairs the sequence $\zeta^{j^2}x_j$ with the chirp $\zeta^{-(k-j)^2}$ at offset $k-j$. So the transform is computed by multiplying by chirps, convolving, and multiplying again. For $N=2$, $\omega=-1$ and $\zeta=i$, the formula at $k=1$ gives $X_1=x_0-x_1$, as the definition does.

The cyclic form matters because of the polynomial ring. Multiplying polynomials modulo $y^r+1$ convolves their coefficient lists, but a term that wraps past the top coefficient picks up a minus sign, since $y^r=-1$. A phase twist turns the last cyclic coordinate into such a polynomial, and the ring's negative wrap reproduces the cyclic wrap <cite data-source="paper">its negative wrap gives precisely the original cyclic wrap after the twist is removed</cite>. So a cyclic convolution is the form the ring convolution can compute, and that is why the argument needs it in this form.
