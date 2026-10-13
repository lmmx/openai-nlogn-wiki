The discrete Fourier transform is the linear map that turns a vector into its Fourier coefficients. It matters because it turns [cyclic convolution](cyclic-convolution.md) into entrywise products.

Let $u=(u_0,\dots,u_{q-1})$ be a complex vector of length $q$, where $q$ is the number of entries of $u$. Let $\omega=\exp(-2\pi i/q)$ be a [primitive $q$-th root of unity](roots-of-unity.md), so $\omega^q=1$ and no smaller positive power of $\omega$ equals $1$.

The transform of $u$, written $\hat u$, has entries $\hat u_k$, where $j$ indexes the entries of $u$ and $k$ indexes those of $\hat u$, each from $0$ to $q-1$, given by

$$\hat u_k=\frac1q\sum_{j=0}^{q-1}u_j\,\omega^{jk},$$

Let $a$ and $b$ be vectors of length $q$. Let $c$ be their cyclic convolution, $c_l=\sum_{j+r\equiv l\ (\mathrm{mod}\ q)}a_j b_r$, where $r$ indexes the entries of $b$ and $l$ indexes the entries of $c$. Each product $a_jb_r$ appears in $c_l$ for $l\equiv j+r$, and $\omega^{lk}=\omega^{(j+r)k}$ because $\omega^q=1$. Hence

$$\sum_{l=0}^{q-1}c_l\,\omega^{lk}=\sum_{j,r}a_jb_r\,\omega^{(j+r)k}=\Big(\sum_j a_j\omega^{jk}\Big)\Big(\sum_r b_r\omega^{rk}\Big).$$

Here $\hat a$, $\hat b$ and $\hat c$ are the transforms of $a$, $b$ and $c$, each defined by the formula above. Each bracket on the right is $q$ times a transform, and $\hat c_k=\frac1q\sum_l c_l\,\omega^{lk}$, so $\hat c_k=q\,\hat a_k\,\hat b_k$. The transform turns cyclic convolution into entrywise products, up to the factor $q$.

For $q$ a power of two, the fast Fourier transform (FFT) of Cooley and Tukey computes $\hat u$ in $O(q\log q)$ operations: it splits $u$ into its even- and odd-indexed entries and transforms each half at length $q/2$. Let $N(q)$ count the operations on length $q$; splitting gives $N(q)=2N(q/2)+O(q)$, which solves to $O(q\log q)$.
