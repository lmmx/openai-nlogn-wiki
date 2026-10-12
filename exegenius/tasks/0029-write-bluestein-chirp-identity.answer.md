Bluestein's chirp identity rewrites a [Discrete Fourier transform](discrete-fourier-transform.md) so that it can be computed with convolution. It computes its transforms by a [Cyclic convolution](cyclic-convolution.md) multiplied by chirp factors.

Let $q$ be the number of values the transform takes and returns. Let $\omega = e^{2\pi i/q}$ be the primitive $q$-th root of unity whose powers the transform uses. Let $w = e^{\pi i/q}$, so that $w^2 = \omega$. The indices $j$ and $k$ are integers in $\{0,\ldots,q-1\}$, with $j$ the input index and $k$ the output index.

The identity is
$$\omega^{jk} = w^{j^2}\, w^{k^2}\, w^{-(k-j)^2}.$$

It holds because $j^2 + k^2 - (k-j)^2 = 2jk$, so the right side equals $w^{2jk} = \omega^{jk}$. Each term of the transform's sum thus splits into a factor in $j$, a factor in $k$, and a chirp $w^{-(k-j)^2}$ that depends only on the difference $k-j$. Because the chirp depends only on $k-j$, the sum over $j$ has the form of a convolution. The factors $w^{j^2}$ and $w^{-(k-j)^2}$ are quadratic phases, which is why they are called chirps.

For example, take $q=2$, $\omega=-1$ and $w=i$. For $j=k=1$ the right side is $i\cdot i\cdot 1=-1=\omega^{1}$, as the identity requires.

In the paper's reduction, the middle transform, including its target permutation, is turned into normalized cyclic convolution by this identity. The permutation stays inside the transform identity <cite data-source="paper">so they need not be executed as separate full sorts</cite>.
