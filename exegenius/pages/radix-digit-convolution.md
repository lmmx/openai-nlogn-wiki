Radix-digit convolution rewrites an integer product as a polynomial product: it reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short digit vectors.

Fix a radix $B \ge 2$, the base in which the inputs are written. Let $x$ and $y$ be the two integers to multiply, and let $d$ be the number of radix-$B$ digits of each input, so $x=\sum_{i=0}^{d-1}x_iB^i$ and $y=\sum_{j=0}^{d-1}y_jB^j$, where $x_i$ and $y_j$ are the digits. Let $u=(x_0,\dots,x_{d-1})$ and $v=(y_0,\dots,y_{d-1})$ be the digit vectors.

Multiplying the two expansions gives
$$xy=\sum_{m=0}^{2d-2}\Big(\sum_{i+j=m}u_iv_j\Big)B^m.$$
The inner sum, written $(u\ast v)_m$, is the convolution of $u$ and $v$ at index $m$. Each entry is a sum of at most $d$ products of digits, so the entries are small. Evaluating the list $u\ast v$ at $B$ gives $xy$, and carrying its entries yields the radix-$B$ digits of the product.

For example, with $B=10$, $x=12$ and $y=13$, the digit vectors are $u=(2,1)$ and $v=(3,1)$, their convolution is $u\ast v=(6,5,1)$, and $6+5\cdot 10+1\cdot 10^2=156=12\cdot 13$.

The point of the rewriting is that convolution becomes entrywise multiplication after a [discrete Fourier transform](discrete-fourier-transform.md), so the method works with the short convolution instead of the full integers. The source takes this as its starting point. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>.
