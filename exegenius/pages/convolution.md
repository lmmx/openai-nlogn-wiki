Cyclic convolution is the product of two sequences whose indices wrap around; the multiplication algorithm reduces integer multiplication to it, because it is the operation that Fourier-type transforms turn into pointwise multiplication (see [Discrete Fourier transform](dft.md)).

For two sequences $f,g$ indexed by $\mathbb Z/q\mathbb Z$, where $q$ is the number of entries in each sequence, the cyclic convolution is
$$(f*g)_k=\sum_{j\in\mathbb Z/q\mathbb Z} f_j\,g_{k-j},$$
with $k-j$ taken modulo $q$. Equivalently, $f*g$ is the product of the polynomials $\sum_j f_jx^j$ and $\sum_j g_jx^j$ reduced modulo $x^q-1$: since $x^q=1$, a term $x^m$ with $m\ge q$ lands on index $m-q$.

Take $q=3$, $f=1+2x+3x^2$ and $g=1+x$. The ordinary product is $1+3x+5x^2+3x^3$, and the wrapped term $3x^3$ becomes $3$, giving $4+3x+5x^2$. The formula agrees: $(f*g)_0=f_0g_0+f_1g_2+f_2g_1=1+0+3=4$. If the ordinary product has degree below $q$, nothing wraps and $f*g$ is the ordinary product.

## Several axes and the negacyclic ring

The algorithm uses arrays with $d$ axes, where $t_i$ is the length of axis $i$, so the index is a tuple in $\prod_i\mathbb Z/t_i\mathbb Z$. Convolution sums over all index tuples, and the index wraps independently on each axis. On the last axis, $t_d=r$, each entry is a polynomial in the ring of [Polynomial ring modulo y^r + 1](ring-y.md), and the product of entries there is the ring product, where wrapping past $y^r$ flips the sign (this is what "negacyclic" means).

Let $M=\prod_{i<d}t_i$ be the number of cyclic addresses on the first $d-1$ axes, and $T=rM$ the total number of complex coefficients in an array. The normalized convolution of arrays over the ring is
$$\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}.$$

Division by $T$ keeps values bounded. A fixed output coefficient is a sum of exactly $rM$ signed scalar products, so it is their average <cite data-source="paper">Thus that coefficient averages $rM$ signed scalar products, and $\mathcal M_r$ is a bilinear contraction</cite>. An average of products of numbers of size at most $\|f\|_\infty$ and $\|g\|_\infty$ has size at most $\|f\|_\infty\|g\|_\infty$, where $\|\cdot\|_\infty$ is the largest modulus of a coefficient. Fixed-point arithmetic therefore needs no extra bits for growth, and rounding errors in the operands change the output by at most the size of the change.
