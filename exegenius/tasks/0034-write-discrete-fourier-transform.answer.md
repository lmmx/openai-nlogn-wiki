The discrete Fourier transform, also called the normalized Fourier transform, is the linear map that sends a list of complex numbers to another list of the same length. Each output entry is a sum of all the input entries weighted by powers of a root of unity, scaled by a normalizing factor. The paper implements these normalized transforms <cite data-source="paper">needed for convolution</cite>.

Let $q$ be the number of entries in the vector. Let $\omega$ be a primitive $q$-th root of unity. It satisfies $\omega^q = 1$, and its powers $\omega^0, \omega^1, \dots, \omega^{q-1}$ are distinct.

Let $a = (a_0, a_1, \dots, a_{q-1})$ be the input vector. Index $j$ runs over the input positions, so $a_j$ is the entry at position $j$. The transform $\hat a = (\hat a_0, \dots, \hat a_{q-1})$ of $a$ has $q$ entries. Index $k$ runs over the output positions, so $\hat a_k$ is the output at position $k$; here $k$ no longer denotes the padded width of earlier pages. The transform is

$$\hat a_k = \frac{1}{q} \sum_{j=0}^{q-1} \omega^{jk} a_j, \qquad k = 0, 1, \dots, q-1.$$

Each output is a linear combination of all the inputs, so the transform is a linear map with a $q \times q$ matrix whose $(k, j)$ entry is $\omega^{jk}/q$. The factor $1/q$ is the normalization; without it the map differs from this one by the factor $q$.

For example, take $q = 2$. Then $\omega = -1$ is a primitive square root of unity, and $\hat a_0 = (a_0 + a_1)/2$ and $\hat a_1 = (a_0 - a_1)/2$. For $a = (3, 1)$ this gives $\hat a = (2, 1)$.
