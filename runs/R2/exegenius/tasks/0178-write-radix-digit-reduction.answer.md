Reduction of integer product to digit convolution is the step that rewrites the product of two integers as a convolution of their radix digits, followed by carry propagation. It lets the later pages compute the product by fast convolution methods.

Let the two integers being multiplied be $x$ and $y$, where $y$ denotes an integer, not the indeterminate of the convolution page. Each is written with $n$ bits, where $n$ is their common bit length: a shorter input is padded with leading zeros. Fix a digit width $b$, the number of bits in each radix digit, and let $q=\lceil n/b\rceil$, the number of radix digits of each input. The letter $b$ denotes the digit width here, not the input list $b$ of the convolution page. Choose $b$ with $n\le 2^b$. Write

$$x=\sum_{j=0}^{q-1}x_j\,2^{bj},\qquad y=\sum_{j=0}^{q-1}y_j\,2^{bj}.$$

Here $x_j$ is the $j$th radix digit of $x$, and $y_j$ is the $j$th radix digit of $y$, with $0\le x_j,y_j<2^b$. Splitting the inputs into radix digits reduces the integer product to a [convolution](convolution.md) of short integer coefficients.

Multiplying the two expansions and collecting powers of $2^b$ writes $xy$ as $\sum_k c_k2^{bk}$, where $c_k$ is the sum of $x_i\,y_j$ over all $0\le i,j\le q-1$ with $i+j=k$:

$$xy=\sum_{k=0}^{2q-2}c_k\,2^{bk},\qquad c_k=\sum_{\substack{0\le i,j\le q-1\\ i+j=k}}x_i\,y_j.$$

The sequence $c_0,\ldots,c_{2q-2}$ is the convolution of the digit lists $(x_j)$ and $(y_j)$, and no index wraps because the product has degree $2q-2$. Each $c_k$ is a sum of at most $q$ products, each at most $(2^b-1)^2$, so $c_k\le q(2^b-1)^2$ <cite data-source="paper">0\le c_j\le q(2^b-1)^2<2^{3b}</cite>. Since $(2^b-1)^2<2^{2b}$ and $q\le 2^b$, this is below $2^{3b}$. The condition $q\le 2^b$ holds because $q=\lceil n/b\rceil\le n\le 2^b$.

The $c_k$ may exceed $2^b$, so the sum is not yet in radix-$2^b$ form. Carry propagation converts it. Let $h_k$ be the carry into position $k$, with $h_0=0$, and let $d_k$ be the output digit at position $k$. For $k=0,1,\ldots$, $d_k$ is the remainder and $h_{k+1}$ the quotient of $c_k+h_k$ divided by $2^b$, so that

$$c_k+h_k=d_k+2^b\,h_{k+1},\qquad 0\le d_k<2^b.$$

The bound on $c_k$ keeps the carries from growing. If $h_k<2^{2b+1}$, then $h_{k+1}\le(c_k+h_k)/2^b<2^{2b}+2^{b+1}\le 2^{2b+1}$, so by induction every carry is below $2^{2b+1}$.

The carries also vanish. Since $c_k=0$ for $k>2q-2$, we have $h_{k+1}=\lfloor h_k/2^b\rfloor$ for $k\ge 2q-1$. This is smaller than $h_k$ whenever $h_k>0$, so the carries reach $0$ after finitely many steps and stay $0$. Multiply the $k$th equation by $2^{bk}$ and sum over all $k$. Each carry term $h_{k}2^{bk}$ appears once on each side, except $h_0=0$, so the carries cancel and only finitely many terms are nonzero, leaving

$$\sum_{k} c_k2^{bk}=\sum_{k} d_k2^{bk}.$$

The left side is $xy$, so $xy=\sum_k d_k2^{bk}$, and the $d_k$ are the radix-$2^b$ digits of the product.

For example, take $b=2$, $x=13=1101_2$ and $y=7=0111_2$ written with the same $4$ bits, so $n=4$ and $q=2$. Then $x_0=01_2=1$, $x_1=11_2=3$, $y_0=3$, $y_1=1$, and $(c_0,c_1,c_2)=(3,10,3)$. The carries are $h_1=0$, $h_2=2$, $h_3=1$, $h_4=0$, giving digits $(d_0,d_1,d_2,d_3)=(3,2,1,1)$. Thus $91=3+2\cdot4+1\cdot16+1\cdot64=13\cdot7$.
