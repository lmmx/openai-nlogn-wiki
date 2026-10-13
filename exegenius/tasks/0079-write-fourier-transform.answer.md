The discrete Fourier transform is the linear map that turns a vector into its Fourier coefficients. It matters because it turns [cyclic convolution](cyclic-convolution.md) into entrywise products.

Let $u=(u_0,\dots,u_{q-1})$ be a complex vector of length $q$, its number of entries; here $u$ is not the first input of earlier pages. Let $\omega=\exp(-2\pi i/q)$, the [primitive $q$-th root of unity](roots-of-unity.md), so $\omega^q=1$. Let $\hat u$ be the transform of $u$, whose $k$-th entry $\hat u_k$ is given below, with $j$ and $k$ running over the entries of $u$ and $\hat u$, from $0$ to $q-1$:

$$\hat u_k=\frac1q\sum_{j=0}^{q-1}u_j\,\omega^{jk}.$$

Multiplying two polynomials is a cyclic convolution. Let $a$ and $b$ be coefficient lists of length $q/2$, polynomials of degree below $q/2$. Their product has degree below $q$, so reducing it modulo $x^q-1$ changes nothing, and its coefficients are the cyclic convolution $c$, where $c_l=\sum_{i+j\equiv l \ (\mathrm{mod}\ q)} a_i b_j$.

Without the factor $1/q$, the sum is $q\hat u_k$. Each product $a_ib_j$ lies in $c_l$ for $l\equiv i+j$, and $\omega^{lk}=\omega^{(i+j)k}$ since $\omega^q=1$, so

$$\sum_l c_l\,\omega^{lk}=\sum_{i,j}a_ib_j\,\omega^{(i+j)k}=\Big(\sum_i a_i\omega^{ik}\Big)\Big(\sum_j b_j\omega^{jk}\Big).$$

Hence $\hat c_k=q\,\hat a_k\,\hat b_k$ for the transforms $\hat a$, $\hat b$, $\hat c$ of $a$, $b$, $c$. Up to the factor $q$ from the normalization, the transform turns convolution into entrywise products.

For $q$ a power of two, the Cooley–Tukey fast Fourier transform takes $O(q\log q)$ operations. It splits $u$ into its even- and odd-indexed entries, transforms each at length $q/2$ (normalized results $\alpha$ and $\beta$), and combines them for $0\le k<q/2$, using $\omega^{q/2}=-1$:

$$\hat u_k=\tfrac12(\alpha_k+\omega^k\beta_k),\qquad \hat u_{k+q/2}=\tfrac12(\alpha_k-\omega^k\beta_k).$$

Let $T(q)$ count the operations on length $q$. Each level costs $O(q)$ plus two half-length transforms, so $T(q)=2T(q/2)+O(q)$ gives $O(q\log q)$.
