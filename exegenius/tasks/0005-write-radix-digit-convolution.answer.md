Radix-digit convolution is the rewriting of two integers as polynomials in a power of two whose coefficients are their digits, so that multiplying the integers becomes multiplying the polynomials. It is the first step of the argument, and the [Transform identity with retained permutations](transform-identity.md) acts on the coefficient lists it produces.

Splitting integers into radix digits reduces [Exact integer multiplication](exact-integer-multiplication.md) to convolution of short integer coefficients. The paper states this reduction at the start of its argument.<cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>

Let $k$ be the number of bits in one radix digit, so the digit base is $2^k$, and let $m$ be the number of digits in each integer.

Take integers $u$ and $v$ below $2^{km}$, whose $i$-th digits are $u_i$ and $v_i$, each in $\{0,\dots,2^k-1\}$. Then
$$u = \sum_{i=0}^{m-1} u_i 2^{ki}, \qquad v = \sum_{i=0}^{m-1} v_i 2^{ki}.$$

Let $z$ be an indeterminate and let $U(z)=\sum_{i=0}^{m-1} u_i z^i$ and $V(z)=\sum_{i=0}^{m-1} v_i z^i$ be the polynomials whose coefficient lists are the digits of $u$ and $v$, so that $u=U(2^k)$ and $v=V(2^k)$.

Let $W=UV$ be their product, whose coefficient of $z^j$ is $w_j=\sum_{i+l=j} u_i v_l$; this convolution of the digit lists gives $uv=W(2^k)$.

Each $w_j$ is a sum of at most $m$ products of digits, so $w_j \le m(2^k-1)^2$ and $w_j$ has about $2k+\log_2 m$ bits. These are the short integer coefficients of the reduction.

Multiplying the integers is thus replaced by convolving short coefficient lists, followed by carry propagation, because $w_j$ can exceed $2^k-1$.

For $k=2$ and $m=2$, take $u=13$ and $v=6$. Then $U(z)=1+3z$ and $V(z)=2+z$, so $W=2+7z+3z^2$ and $W(4)=78=13\cdot 6$. The coefficient $7$ is larger than any radix-4 digit, so it is carried into the next position, giving the digits $2,3,0,1$ of $78$.
