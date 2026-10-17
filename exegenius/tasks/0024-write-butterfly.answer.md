A butterfly is the two-point step $H_0(u,v)=(\frac{u+v}{2},\frac{u-v}{2})$, the matrix with rows $\frac12(1,1)$ and $\frac12(1,-1)$ applied to a pair of values. Here $t$ is the transform length, a power of two. Repeated over the address bits of an array, with twiddle multiplications between layers, it computes the [Discrete Fourier transform](dft.md) of an array in $\log_2 t$ layers instead of $t^2$ operations. The transforms later on this wiki are built from address rearrangements, signed shifts and these steps <cite data-source="paper">two-point butterfly operations</cite>.

## One layer

Let $z_k$, for positions $0\le k<t$, be the input values, and let $\omega_t=e^{2\pi i/t}$. The transform is $(F_tz)_m=\frac1t\sum_j z_j\omega_t^{-jm}$. The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for $0\le k<t/2$ <cite data-source="paper">the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$</cite>. Split the sum over $j$ into $j=k$ and $j=k+t/2$. Since $\omega_t^{t/2}=-1$, the second part carries the factor $(-1)^m$. Write the output index as $m=2h+b$, where $b\in\{0,1\}$ is its lowest bit and $h$ is the remaining index. Then
$$(F_tz)_{2h+b}=\frac1{t/2}\sum_{k=0}^{t/2-1}(\omega_t^2)^{-hk}\,\omega_t^{-bk}\,\frac{z_k+(-1)^bz_{k+t/2}}{2}.$$
The pair $(z_k,z_{k+t/2})$ enters only through $\frac{z_k+z_{k+t/2}}2$ (for $b=0$) and $\frac{z_k-z_{k+t/2}}2$ (for $b=1$), which are exactly the two outputs of $H_0$. After multiplying the $b=1$ output by the twiddle factor $\omega_t^{-k}$, what remains for each $b$ is the same transform of length $t/2$, because $\omega_t^2$ is the primitive $(t/2)$-th root of unity.

## Recursion

So one layer of $t/2$ butterflies and $t/2$ twiddle multiplications reduces a length-$t$ transform to two independent length-$t/2$ transforms, run on the two halves of the array. After $\log_2 t$ layers every transform has length one, which is the identity. The total is $O(t\log t)$ operations.

For $t=4$: the first layer forms $\frac{z_0\pm z_2}2$ and $\frac{z_1\pm z_3}2$, multiplies the two differences by $1$ and $\omega_4^{-1}=-i$, and the second layer applies $H_0$ to each of the two resulting pairs.

Output index $2h+b$ has its lowest bit $b$ decided in the first layer, which acts on the highest address bit of the array. Each output therefore lands at the bit-reversed position of its index.
