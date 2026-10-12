The discrete Fourier transform is the map that sends a vector of complex numbers to another vector of the same length, and it is the frequency step through which the paper computes convolutions. The paper needs exactly this normalized transform for convolution <cite data-source="paper">We now implement the normalized Fourier transforms needed for convolution</cite>.

Let $q$ be the number of entries in a vector. Let $\omega$ be a primitive $q$-th root of unity, a complex number with $\omega^q = 1$ whose powers $\omega^1, \dots, \omega^{q-1}$ are all different from $1$. For a vector $x = (x_0, \dots, x_{q-1})$ of complex numbers, its discrete Fourier transform is the vector $X = (X_0, \dots, X_{q-1})$ with

$$X_k = \frac{1}{q} \sum_{j=0}^{q-1} x_j\, \omega^{jk}, \qquad k = 0, \dots, q-1.$$

Here $j$ indexes the input entries and $k$ indexes the output entries. Each output is a weighted sum of all the inputs, where the weight $\omega^{jk}$ is a power of $\omega$. The factor $1/q$ is the normalization.

The map is invertible, and its inverse has no extra factor. For an integer $m$, the sum $\sum_{k=0}^{q-1} \omega^{mk}$ equals $q$ when $q$ divides $m$ and $0$ otherwise. Substituting the formula for $X_k$ into $\sum_{k} X_k\, \omega^{-jk}$ and using this fact gives

$$x_j = \sum_{k=0}^{q-1} X_k\, \omega^{-jk}, \qquad j = 0, \dots, q-1.$$

For $q = 2$, the root is $\omega = -1$, so $X_0 = (x_0 + x_1)/2$ and $X_1 = (x_0 - x_1)/2$. The inverse recovers $x_0 = X_0 + X_1$ and $x_1 = X_0 - X_1$.

The point of the transform for what follows is that a cyclic convolution of two vectors becomes entrywise multiplication of their transforms, up to a constant factor from the normalization. A convolution can therefore be computed by transforming both inputs, multiplying entrywise, and inverting.
