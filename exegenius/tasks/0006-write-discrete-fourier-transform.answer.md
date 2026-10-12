The discrete Fourier transform is the linear map that sends a vector of complex values to a vector of the same length, each entry a weighted sum of the inputs with powers of a root of unity as weights, divided by the length. It is the tool behind the [radix-digit convolution](radix-digit-convolution.md) step of the paper's integer multiplication.

Let $q$ be the number of entries in each vector. Here $j$ indexes the output entries and $k$ the input entries, both running from $0$ to $q-1$. Let $\omega$ be a primitive $q$-th root of unity, so $\omega^q = 1$ and $\omega^j \neq 1$ for $0 < j < q$. The transform $F_q$ sends a vector $x = (x_0, \dots, x_{q-1})$ to $y = F_q x$, where

$$y_j = \frac{1}{q}\sum_{k=0}^{q-1} \omega^{jk} x_k.$$

For $q = 2$ take $\omega = -1$; then $y_0 = (x_0 + x_1)/2$ and $y_1 = (x_0 - x_1)/2$.

The map is invertible. Its inverse is $x_l = \sum_{j=0}^{q-1} \omega^{-jl} y_j$, where $l$ indexes the entries, with no factor $1/q$. The inverse has the same form as the transform with $\omega^{-1}$ in place of $\omega$. The reason is that $\sum_{j=0}^{q-1} \omega^{j(k-l)}$ equals $q$ when $k = l$ and $0$ otherwise, a geometric sum over powers of $\omega$.

This matters because the convolution of two vectors becomes a pointwise (entry by entry) product of their transforms, up to the factor $q$ that the normalization introduces. Transforming, multiplying pointwise, and inverting therefore computes the convolution.
