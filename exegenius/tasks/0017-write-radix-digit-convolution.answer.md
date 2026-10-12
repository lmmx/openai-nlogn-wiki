Radix-digit convolution is the rewriting of two integers as polynomials in a power of two whose coefficients are their digits, so that multiplying the integers becomes multiplying the polynomials. It is the first step of the argument, and the [Transform identity with retained permutations](transform-identity.md) acts on the coefficient lists it produces.

Splitting integers into radix digits reduces [Exact integer multiplication](exact-integer-multiplication.md) to convolution of short integer coefficients. This is the reduction the paper uses at the start of its argument. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>

Let $b$ be the number of bits in one radix digit, so the digit base is $2^b$, and let $m$ be the number of digits in each integer.

Take integers $u$ and $v$ below $2^{bm}$, and let $u_i$ and $v_i$ be their $i$-th digits, for an index $i$ running from $0$ to $m-1$, each in $\{0,\dots,2^b-1\}$. Then
$$u = \sum_{i=0}^{m-1} u_i 2^{bi}, \qquad v = \sum_{i=0}^{m-1} v_i 2^{bi}.$$

Let $z$ be an indeterminate, a symbol that is not a number. Let $U(z)=\sum_{i=0}^{m-1} u_i z^i$ and $V(z)=\sum_{i=0}^{m-1} v_i z^i$ be the polynomials whose coefficient lists are the digits of $u$ and $v$, so that $u=U(2^b)$ and $v=V(2^b)$.

Here $l$ is an index running from $0$ to $m-1$ like $i$, so $v_l$ is the $l$-th digit of $v$. 

Let $W=UV$ be their product, whose coefficient of $z^j$ is $w_j=\sum_{i+l=j} u_i v_l$, where $j$ indexes the coefficients of $W$. This convolution of the digit lists gives $uv=W(2^b)$.

Each $w_j$ is a sum of at most $m$ products of digits, so $w_j \le m(2^b-1)^2$ and $w_j$ has about $2b+\log_2 m$ bits. These are the short integer coefficients of the reduction.

Multiplying the integers is thus replaced by convolving short coefficient lists, followed by carry propagation: each coefficient is rewritten in base $2^b$ by carrying its excess into the next position, because $w_j$ can exceed $2^b-1$.

For $b=2$ and $m=2$, take $u=13$ and $v=6$. Then $U(z)=1+3z$ and $V(z)=2+z$, so $W=2+7z+3z^2$ and $W(4)=78=13\cdot 6$. The coefficient $7$ is larger than any radix-4 digit, so it is carried into the next position, giving the digits $2,3,0,1$ of $78$.
