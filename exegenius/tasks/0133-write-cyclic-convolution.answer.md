Cyclic convolution is the product of two coefficient lists in which exponents wrap around, so that each exponent is taken modulo the list length. The later pages compute it on power-of-two lengths, where fast transforms make it cheap.

Let $x$ be a formal variable. Let $S$ be the number of coefficients in each list. Let $i$, $j$ and $k$ be indices in $\{0,\dots,S-1\}$. Write the first list as $a(x)=\sum_{i=0}^{S-1} a_i x^i$ and the second as $b(x)=\sum_{j=0}^{S-1} b_j x^j$, with complex coefficients. Let $c=a\ast b$ be the cyclic convolution of $a$ and $b$, a list of $S$ coefficients. On this page the letters $a$, $b$, $c$, $i$, $j$, $k$, $S$ and $x$ take these meanings, not the ones bound on earlier pages.

Their ordinary product has terms up to $x^{2S-2}$. Modulo $x^S-1$, the power $x^S$ is replaced by $1$, so every exponent at least $S$ wraps around to its remainder modulo $S$. The entries of $c$ are the coefficients of this reduced product:

$$c_k=\sum_{\substack{i,j\in\{0,\dots,S-1\}\\ i+j\equiv k \ (\mathrm{mod}\ S)}} a_i\,b_j, \qquad 0\le k\le S-1.$$

For example, let $S=3$, $a(x)=1+2x$ and $b(x)=x+3x^2$. The ordinary product is $x+5x^2+6x^3$, and replacing $x^3$ by $1$ gives $c(x)=6+x+5x^2$, that is, $c=(6,1,5)$.

If the ordinary product has degree below $S$, no term wraps, so the cyclic product equals the ordinary product. <cite data-source="paper">Thus convolution modulo $x^S-1$ has no nonzero wraparound.</cite>
