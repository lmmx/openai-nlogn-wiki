The discrete Fourier transform (DFT, also called the Fourier transform) is the map that sends a sequence to its values at the roots of unity of the same length. The multiplication argument needs it for convolution. Gaussian resampling replaces these transforms by multidimensional transforms whose axis lengths are powers of two. <cite data-source="paper">it replaces the Fourier transforms needed for</cite>

The input sequence is $a = (a_0, \dots, a_{n-1})$, a list of complex numbers, where $n$ is its length. The transform is defined using [Primitive roots of unity](roots-of-unity.md): fix a primitive $n$-th root of unity $\omega$. Here $j$ is the input position, running from $0$ to $n-1$, and $k$ is the output position, running over the same range. On this page $j$ and $k$ are these positions; on the roots-of-unity page they are power exponents, so the meanings differ.

The output sequence is $\hat a = (\hat a_0, \dots, \hat a_{n-1})$, the transform of $a$, with entries given by the formula below.

$$\hat a_k = \sum_{j=0}^{n-1} a_j\,\omega^{jk}, \qquad k = 0, 1, \dots, n-1.$$

Each entry is a polynomial evaluation. Let $p(x) = \sum_{j=0}^{n-1} a_j x^j$ be the polynomial with coefficient list $a$, where $x$ is a formal variable, a placeholder for a number to be substituted. Substituting $x = \omega^k$ gives $p(\omega^k) = \hat a_k$.

Since $\omega$ is primitive, its powers $\omega^0,\dots,\omega^{n-1}$ are distinct, so they are all $n$ roots of $x^n = 1$. Hence $\hat a$ lists $p$ at every $n$-th root of unity.

Example. For $n = 2$, $\omega = -1$ is primitive, and $\hat a_0 = a_0 + a_1$, $\hat a_1 = a_0 - a_1$. For $a = (3, 1)$ this gives $\hat a = (4, 2)$.

Computed term by term, the formula takes about $n^2$ multiplications, since each of the $n$ entries is a sum of $n$ products.
