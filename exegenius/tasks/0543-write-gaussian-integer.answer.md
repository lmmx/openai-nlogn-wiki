A Gaussian integer is a complex number whose real and imaginary parts are both integers. The set of them is $\mathbb{Z}[i]$, where $i$ is the imaginary unit, $i^2=-1$. The paper's arrays hold exact values in this system, which its later [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) step works on.

Sums and products stay in $\mathbb{Z}[i]$, because $i^2=-1$ is an integer: $(1+2i)(3-i)=3-i+6i-2i^2=5+5i$.

Gaussian integers keep exact the outputs of a [Discrete Fourier transform](discrete-fourier-transform.md) of length $4$, which is normalized by $1/4$. Its weights are $(-i)^0,\dots,(-i)^3$, namely $1,-i,-1,i$. Dividing by $4=2^2$ leaves each output a Gaussian dyadic, a Gaussian integer divided by a power of two.

Each entry of the paper's frame and of its inverse is a Gaussian integer divided by a power of two, <cite data-source="paper">so both preserve arrays over Z[i, 1/2].</cite> Gaussian integers keep exact the entries of the paper's [kernels](two-point-kernel.md) and their inverses: <cite data-source="paper">The kernels implemented below have Gaussian dyadic coefficients.</cite>

Reduction modulo $y^r+1$ subtracts, for each position $j$ from $0$ to $r-1$, the coefficient at $j+r$ from the coefficient at $j$. The paper states that <cite data-source="paper">Gaussian integer coefficient Hj is a sum of exactly r signed products of Gaussian integer input</cite> coefficients, where a signed product is a product multiplied by $+1$ or $-1$. So each reduced coefficient is a Gaussian integer.

Take $r=2$ and $(1+iy)(2+y)=2+(1+2i)y+iy^2$. Reduction gives $2-i$ at position $0$ and $1+2i$ at position $1$. Each is a sum of two signed products: $2-i=1\cdot 2-i\cdot 1$ and $1+2i=1\cdot 1+i\cdot 2$.
