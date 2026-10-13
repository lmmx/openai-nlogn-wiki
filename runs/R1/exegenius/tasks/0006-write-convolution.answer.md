Convolution combines two coefficient lists into one by summing products into entries indexed by the sum of their positions, with indices past the end wrapping around. A coefficient list is a list of numbers, one per power of a variable. The target needs this operation because integer multiplication reduces to it. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>

Let $n$ be the length of the lists, the number of entries in each coefficient list. Let $a=(a_0,\dots,a_{n-1})$ and $b=(b_0,\dots,b_{n-1})$ be the two input coefficient lists. The cyclic convolution of $a$ and $b$ is the list $c$ with entries

$$c_k=\sum_{\substack{0\le i,j\le n-1\\ i+j\equiv k \pmod n}} a_i b_j,\qquad 0\le k\le n-1.$$

Here $i$ and $j$ index the entries of $a$ and $b$, and $k$ indexes the entries of $c$. Each product $a_ib_j$ is added into the entry $c_k$ where $k$ is $i+j$ reduced modulo $n$, so the $n^2$ products are distributed over the $n$ entries of $c$.

Equivalently, let $y$ be an indeterminate, a symbol with no value, and let $A(y)=\sum_i a_i y^i$ and $B(y)=\sum_j b_j y^j$. Working modulo $y^n-1$ sets $y^n=1$, so the term $a_ib_jy^{i+j}$ becomes $a_ib_jy^{i+j-n}$ when $i+j\ge n$. Hence $c$ is the coefficient list of $A(y)B(y)$ reduced modulo $y^n-1$.

Without the wrap, the product $A(y)B(y)$ has $2n-1$ coefficients. Cyclic convolution folds the entries at indices $n$ to $2n-2$ back onto indices $0$ to $n-2$.

For example, take $n=2$, $a=(1,2)$ and $b=(3,4)$. Then $c_0=a_0b_0+a_1b_1=11$ and $c_1=a_0b_1+a_1b_0=10$. Check: $(1+2y)(3+4y)=3+10y+8y^2$, and $y^2=1$ turns $8y^2$ into $8$, giving $11+10y$.
