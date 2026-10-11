Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer coefficients, a form that fast convolution methods can evaluate. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>

Fix a digit width $k$, the number of bits in one digit. Let $B = 2^k$ be the radix. Pad both inputs to $d$ digits, where $d$ is a count: the number of digit positions in each input.

For integers $x$ and $y$, let $x_j$ and $y_j$ be the $j$th digits of $x$ and $y$, each in $\{0,\dots,B-1\}$. Then
$$x=\sum_{j=0}^{d-1}x_jB^j,\qquad y=\sum_{j=0}^{d-1}y_jB^j.$$
So multiplying the integers is the same as multiplying the polynomials whose coefficient lists are these digits, and then evaluating the product at $B$. The product polynomial has the coefficient $c_m = \sum_{j+l=m} x_j y_l$ at each position $m$, the convolution of the two digit sequences, and $xy = \sum_m c_m B^m$.

The convolution is the expensive part. The sources compute it with Fourier transforms, and later pages replace these by transforms whose lengths are powers of two. The coefficients are short: each term $x_j y_l$ is at most $(B-1)^2 < 2^{2k}$, and $c_m$ has at most $d$ terms, so $c_m < d\,2^{2k}$, about $2k + \lg d$ bits.

The integer is recovered from the $c_m$ by carry propagation. For example, take $k=2$, so $B=4$, with $x=11$ and $y=6$. Their digits are $x_0=3$, $x_1=2$, $y_0=2$, $y_1=1$, giving $c_0=6$, $c_1=7$, $c_2=2$. As a check, $6+7\cdot 4+2\cdot 16=66=11\cdot 6$. Carrying from the lowest position: $6=1\cdot 4+2$ writes $2$ and carries $1$; $7+1=8=2\cdot 4$ writes $0$ and carries $2$; $2+2=4=1\cdot 4$ writes $0$ and carries $1$; the last carry is the top digit $1$. The digits from lowest to highest are $2,0,0,1$, which is $66$.
