The discrete Fourier transform (DFT, also called the Fourier transform) is the map that sends a sequence to its values at the roots of unity of the same length. Let $n$ be the length of the input sequence, the number of its entries, so the roots are the $n$-th roots of unity. Later pages rewrite this transform in other forms, so its exact definition matters here.

The input sequence is $a = (a_0, \dots, a_{n-1})$, a list of complex numbers. The transform is defined using [Primitive roots of unity](roots-of-unity.md): fix a primitive $n$-th root of unity $\omega$. Here $j$ indexes the input entries and runs from $0$ to $n-1$. Here $k$ indexes the output entries and runs over the same range.

The output sequence is $\hat a = (\hat a_0, \dots, \hat a_{n-1})$, with entries given by the formula below.

$$\hat a_k = \sum_{j=0}^{n-1} a_j\,\omega^{jk}, \qquad k = 0, 1, \dots, n-1.$$

Each $\hat a_k$ is the value at $\omega^k$ of the polynomial whose coefficient list is $a$. As $k$ runs over $0,\dots,n-1$, the powers $\omega^0,\dots,\omega^{n-1}$ are $n$ distinct $n$-th roots of unity, so the output lists the polynomial's values at all of them.

Example. For $n = 2$, $\omega = -1$ is primitive, and the formula reads $\hat a_0 = a_0 + a_1$ and $\hat a_1 = a_0 - a_1$. For $a = (3, 1)$ this gives $\hat a = (4, 2)$.

Evaluated term by term, the formula takes about $n^2$ multiplications, since every pair $(j,k)$ contributes one. Fast algorithms compute the same output in $O(n \log n)$ operations.
