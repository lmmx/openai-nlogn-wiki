The discrete Fourier transform (DFT, also called the Fourier transform) sends a sequence to its values at the roots of unity of the same length.

The input sequence is $a = (a_0, \dots, a_{n-1})$, a list of complex numbers, where $n$ is its length. The transform is defined using [Primitive roots of unity](roots-of-unity.md): fix a primitive $n$-th root of unity $\omega$. Here $j$ indexes the input entries and runs from $0$ to $n-1$. Here $k$ indexes the output entries and runs over the same range, not the power index of the roots-of-unity page.

The output sequence is $\hat a = (\hat a_0, \dots, \hat a_{n-1})$, with entries given by the formula below.

$$\hat a_k = \sum_{j=0}^{n-1} a_j\,\omega^{jk}, \qquad k = 0, 1, \dots, n-1.$$

Each entry is a polynomial evaluation. Let $p(x) = \sum_{j=0}^{n-1} a_j x^j$ be the polynomial whose coefficient list is $a$, where $x$ is a formal variable, a placeholder for a number to be substituted, and $a_j$ is the coefficient of $x^j$. Substituting $x = \omega^k$ gives $p(\omega^k) = \sum_{j} a_j\,\omega^{jk} = \hat a_k$.

The output lists $p$ at all $n$-th roots of unity, because the powers $\omega^0,\dots,\omega^{n-1}$ are distinct. If $\omega^j = \omega^k$ with $j < k$, dividing by $\omega^j \neq 0$ gives $\omega^{k-j} = 1$ with $0 < k-j < n$, contradicting primitivity. Each power satisfies $(\omega^k)^n = 1$, and a polynomial of degree $n$ has at most $n$ roots, so these $n$ powers are all the $n$-th roots of unity.

Example. For $n = 2$, $\omega = -1$ is primitive, and $\hat a_0 = a_0 + a_1$, $\hat a_1 = a_0 - a_1$. For $a = (3, 1)$ this gives $\hat a = (4, 2)$.

Term by term, the formula takes about $n^2$ multiplications. When $n$ is a power of two, the fast Fourier transform (Cooley–Tukey) computes the same output in $O(n \log n)$ operations by splitting the even-indexed and odd-indexed entries into two transforms of length $n/2$, with root $\omega^2$, and combining them in $O(n)$ operations.
