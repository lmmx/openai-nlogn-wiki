Cyclic convolution is the product of two coefficient lists in which exponents wrap around, so that the exponent of each term is taken modulo the list length. It is the operation that later pages compute on power-of-two lengths.

Let $x$ be a formal variable and $S$ be the number of coefficients in each list. Here $i$, $j$ and $k$ are indices, each in $\{0,\dots,S-1\}$. Write the first list as $a(x)=\sum_{i=0}^{S-1} a_i x^i$ and the second as $b(x)=\sum_{j=0}^{S-1} b_j x^j$, with complex coefficients. Their ordinary product has terms up to $x^{2S-2}$. Modulo $x^S-1$, the power $x^S$ is replaced by $1$, so every exponent at least $S$ wraps around to its remainder modulo $S$. The cyclic convolution $c=a\ast b$ is the list of coefficients of the reduced product. Its entries are

$$c_k=\sum_{\substack{i,j\in\{0,\dots,S-1\}\\ i+j\equiv k \ (\mathrm{mod}\ S)}} a_i\,b_j, \qquad 0\le k\le S-1.$$

For example, let $S=3$, $a(x)=1+2x$ and $b(x)=x+3x^2$. The ordinary product is $x+5x^2+6x^3$, and $x^3$ is replaced by $1$, so $c(x)=6+x+5x^2$, that is, $c=(6,1,5)$.

If the ordinary product has degree below $S$, no term wraps, and the cyclic product equals the ordinary product. <cite data-source="paper">Thus convolution modulo $x^S-1$ has no nonzero wraparound.</cite>

This gives integer multiplication. Write each integer as a polynomial in $2^b$ whose coefficients are its digits. Choosing $S$ above the product degree makes the cyclic product equal the ordinary product of these polynomials. Evaluating that product at $2^b$ gives the integer product. Its coefficients stay bounded, so carrying them in base $2^b$ reads the integer off.
