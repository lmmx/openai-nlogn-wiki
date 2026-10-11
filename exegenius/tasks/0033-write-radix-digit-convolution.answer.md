Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer coefficients, which fast convolution methods can evaluate. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>.

Fix a digit width $w$, the number of bits in one digit, and let $B = 2^w$ be the radix. Pad both inputs to $d$ digits, where $d$ is the number of digit positions in each input. Here $l$ is a second digit position over $0,\dots,d-1$, and $p$, running over $0,\dots,2d-2$, is a coefficient position. Let $x$ and $y$ be the input strings, and write $\mathrm{val}(x)$ and $\mathrm{val}(y)$ for the integers they represent.

Let $x_j$ and $y_j$ be the $j$th base-$B$ digits of $\mathrm{val}(x)$ and $\mathrm{val}(y)$, each in $\{0,\dots,B-1\}$, where $j$ runs over the digit positions $0,\dots,d-1$. Then
$$\mathrm{val}(x)=\sum_{j=0}^{d-1}x_jB^j,\qquad \mathrm{val}(y)=\sum_{j=0}^{d-1}y_jB^j.$$
The coefficient $c_p$ at position $p$ is the convolution of the two digit sequences:
$$c_p=\sum_{j+l=p} x_j y_l,\qquad \mathrm{val}(x)\,\mathrm{val}(y)=\sum_p c_p B^p.$$

Fast transform methods compute this convolution. The coefficients are short: each term $x_j y_l$ is at most $(B-1)^2 < 2^{2w}$, and $c_p$ has at most $d$ terms, so $c_p < d\,2^{2w}$, about $2w + \lg d$ bits.

Carry propagation then recovers the product from the $c_p$. Take $w=2$, so $B=4$, with $\mathrm{val}(x)=11$ and $\mathrm{val}(y)=6$, and $d=2$. The digits are $x_0=3$, $x_1=2$, $y_0=2$, $y_1=1$, giving $c_0=6$, $c_1=7$, $c_2=2$. From the lowest position, $6=1\cdot 4+2$ writes $2$ and carries $1$; $7+1=8=2\cdot 4$ writes $0$ and carries $2$; $2+2=4=1\cdot 4$ writes $0$ and carries $1$, which is the top digit. The digits $2,0,0,1$ give $66=11\cdot 6$.
