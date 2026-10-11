A Gaussian integer is a complex number whose real and imaginary parts are both integers. The paper's arrays hold exact values in this number system, which its later [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) step needs.

Here $i$ is the imaginary unit, the number with $i^2=-1$. Write $\mathbb{Z}[i]$ for the set of all Gaussian integers.

Every integer is one, with imaginary part $0$: $5=5+0i$. The number $3+4i$ is one, but $\tfrac12+i$ is not, since $\tfrac12$ is not an integer.

Sums and products of Gaussian integers are again Gaussian integers, because $i^2=-1$ is an integer. For example, $(1+2i)(3-i) = 3 - i + 6i - 2i^2 = 5+5i$.

Gaussian integers keep exact the outputs of a [Discrete Fourier transform](discrete-fourier-transform.md) of length $4$, which is normalized by $1/4$. Its weights are $1$, $i$, $-1$ and $-i$, and dividing by $4=2^2$ leaves each output a Gaussian integer divided by a power of two.

The paper's arrays take entries in $\mathbb{Z}[i,1/2]$, the Gaussian integers divided by powers of two. Each entry of its kernels and their inverses is a <cite data-source="paper">Gaussian integer divided by 2m , so both preserve arrays over Z[i, 1/2].</cite>

The reduction step gives <cite data-source="paper">Gaussian integer coefficient Hj is a sum of exactly r signed products of Gaussian integer input</cite>, where a signed product is a product multiplied by $+1$ or $-1$. A sum of products of Gaussian integers is a Gaussian integer, so each coefficient is exact.
