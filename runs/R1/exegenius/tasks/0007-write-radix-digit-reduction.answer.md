Reduction of integer product to digit convolution is the step that rewrites the product of two integers as a convolution of their radix digits, followed by carry propagation. It is what lets the later pages compute the product by fast convolution methods.

Let the inputs $x$ and $y$ be $n$-bit integers, where $n$ is the bit length of each input. Fix a digit width $b$, the number of bits in each radix digit, and let $q=\lceil n/b\rceil$ be the number of radix digits of each input. Write

$$x=\sum_{j=0}^{q-1}x_j\,2^{bj},\qquad y=\sum_{j=0}^{q-1}y_j\,2^{bj}.$$

Here $x_j$ is the $j$th radix digit of $x$, and $y_j$ is the $j$th radix digit of $y$, with $0\le x_j,y_j<2^b$. Splitting the inputs into radix digits reduces the integer product to a [convolution](convolution.md) of short integer coefficients.

Multiplying the two expansions and collecting powers of $2^b$ writes $xy$ as $\sum_k c_k2^{bk}$, where $c_k$ is the sum of $x_i\,y_j$ over all $0\le i,j\le q-1$ with $i+j=k$:

$$xy=\sum_{k=0}^{2q-2}c_k\,2^{bk},\qquad c_k=\sum_{\substack{0\le i,j\le q-1\\ i+j=k}}x_i\,y_j.$$

The sequence $c_0,\ldots,c_{2q-2}$ is the convolution of the digit lists $(x_j)$ and $(y_j)$, and no index wraps because the product has degree $2q-2$. Each $c_k$ is at most $q(2^b-1)^2$, which is below $2^{3b}$ <cite data-source="paper">since $q\le n\le2^b$</cite>.

The $c_k$ may exceed the digit bound $2^b$, so the sum is not yet in radix-$2^b$ form. Carry propagation converts it: here $h_k$ is the carry into position $k$, and $d_k$ is the output digit at position $k$. Set $h_0=0$ and, for $k=0,1,\ldots$, choose integers $d_k$ and $h_{k+1}$ with

$$c_k+h_k=d_k+2^b\,h_{k+1},\qquad 0\le d_k<2^b.$$

Multiplying the $k$th equation by $2^{bk}$ and summing over $k$, the carry terms cancel, so $\sum_k c_k2^{bk}=\sum_k d_k2^{bk}$. Since the carries eventually vanish, $xy=\sum_k d_k2^{bk}$, and the $d_k$ are the radix-$2^b$ digits of the product.

For example, take $b=2$, $x=13$ and $y=7$, so $n=4$ (both inputs padded to four bits) and $q=2$. Then $x_0=1$, $x_1=3$, $y_0=3$, $y_1=1$, and $(c_0,c_1,c_2)=(3,10,3)$. Carries give $3=d_0+4h_1$ with $d_0=3$ and $h_1=0$; $10=2+4\cdot 2$, so $d_1=2$ and $h_2=2$; $3+2=1+4\cdot 1$, so $d_2=1$ and $h_3=1$; and $0+1=1+4\cdot 0$, so $d_3=1$. Thus $91=3+2\cdot4+1\cdot16+1\cdot64=13\cdot7$.
