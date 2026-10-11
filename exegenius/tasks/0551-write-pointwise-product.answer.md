The pointwise product of two sequences multiplies them entry by entry. On the way to fast integer multiplication, the pointwise product is applied to the outputs of two [forward transforms](forward-transform.md), and its result feeds the [Opposite transform](opposite-transform.md).

The reason for multiplying transforms is the [convolution theorem](convolution.md): the pointwise product of transforms gives the transform of a convolution. So a convolution can be computed by transforming both inputs, multiplying entry by entry, and transforming back.

Let $a$ and $b$ be sequences of length $n$. Their pointwise product, written $a \odot b$, is the sequence whose entry at each position $j$, $0 \le j < n$, is $(a\odot b)_j = a_j b_j$. For example, with $n=3$, $a=(2,\,1+i,\,-i)$ and $b=(1,\,3,\,2i)$, we get $a\odot b=(2,\,3+3i,\,2)$, since $(1+i)\cdot 3=3+3i$ and $(-i)(2i)=2$.

In the [Synthetic polynomial transforms](synthetic-transforms.md), each entry is a polynomial rather than a number, and the product of two entries is taken in the [quotient ring](polynomial-ring-mod-yr-plus-1.md) $\mathbb{C}[y]/(y^r+1)$, where $y^r=-1$. The paper divides that product by $r$: it writes <cite data-source="paper">Let P (u, v) denote the exact pointwise product uv/r</cite>. The paper's normalized product is $P(a_j,b_j)=a_jb_j/r$, the product in the ring divided by $r$. Here $P$ names this map; the letter means something else on the polynomial ring page.

For $r=2$ the ring is $\mathbb{C}[y]/(y^2+1)$, where $y^2=-1$. Take $a_j=1+y$ and $b_j=1-y$. Then $a_jb_j=1-y^2=2$, so $P(a_j,b_j)=2/2=1$.

The two forward transforms are multiplied without reordering their entries: <cite data-source="paper">We may therefore multiply the forward outputs in their retained order</cite>. The [Opposite transform](opposite-transform.md) inverts the forward transform up to a normalizing factor, and it reads the product in that same order: the paper says the opposite transform <cite data-source="paper">consumes that same order after a pointwise product.</cite>
