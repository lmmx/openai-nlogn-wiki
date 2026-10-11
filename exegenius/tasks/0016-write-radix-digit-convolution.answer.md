Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer coefficients, which fast convolution methods can evaluate. Splitting each input into radix digits turns the product into a convolution of short coefficients. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>.

Fix a digit width $k$, the number of bits in one digit. The letter $k$ changes meaning here, from the padded length on the earlier page. Let $B = 2^k$ be the radix. Pad both inputs to $d$ digits, where $d$ is a count: the number of digit positions in each input. Here $x$ and $y$ denote the integers that the two input strings represent.

Let $x_j$ and $y_j$ be the $j$th digits of $x$ and $y$, each in $\{0,\dots,B-1\}$, where $j$ is a digit position running over $0,\dots,d-1$. Then
$$x=\sum_{j=0}^{d-1}x_jB^j,\qquad y=\sum_{j=0}^{d-1}y_jB^j.$$
Here $l$ is a second digit position running over $0,\dots,d-1$, and $m$ is a coefficient position running over $0,\dots,2d-2$; the letter $m$ changes meaning here. The product polynomial has coefficient $c_m$ at each position $m$, the convolution of the two digit sequences:
$$c_m=\sum_{j+l=m} x_j y_l,\qquad xy=\sum_m c_m B^m.$$

The convolution is the expensive part, and fast transform methods compute it. The coefficients are short: each term $x_j y_l$ is at most $(B-1)^2 < 2^{2k}$, and $c_m$ has at most $d$ terms, so $c_m < d\,2^{2k}$, about $2k + \lg d$ bits.

Carry propagation recovers the integer from the $c_m$. Take $k=2$, so $B=4$, with $x=11$ and $y=6$. The digits are $x_0=3$, $x_1=2$, $y_0=2$, $y_1=1$, giving $c_0=6$, $c_1=7$, $c_2=2$. From the lowest position, $6=1\cdot 4+2$ writes $2$ and carries $1$; $7+1=8=2\cdot 4$ writes $0$ and carries $2$; $2+2=4=1\cdot 4$ writes $0$ and carries $1$, which is the top digit. The digits $2,0,0,1$ give $66=11\cdot 6$.
