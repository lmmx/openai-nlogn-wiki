Exact integer multiplication is the task of computing the complete product of two binary integers, with no rounding and no bits lost. It is the problem that the main result bounds ([Integer multiplication below n log n](main-theorem.md)). That result's method first splits each input into digits, which turns the product into a convolution ([radix-digit convolution](radix-digit-convolution.md)). <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>

Let $x$ and $y$ be binary strings, each of length $n$, where $n$ is the number of bits in each input. $\mathrm{val}(x)$ is the nonnegative integer value of $x$, with the leftmost bit most significant. <cite data-source="paper">For a binary string x of length n, let val(x) be its nonnegative integer value, with the leftmost</cite>

Let $k$ be the number of bits in a padded binary string. For an integer $z$ with $0 \le z < 2^k$, $\mathrm{bin}_k(z)$ is the binary representation of $z$ padded on the left with zeros to length $k$. <cite data-source="paper">denote its binary representation padded on the left</cite>

The input is $x$, then a separator symbol $\#$, then $y$, written $x\#y$; the separator marks where $x$ ends and $y$ begins. <cite data-source="paper">We consider exact multiplication: on input x#y</cite> The output must be $\mathrm{bin}_{2n}(\mathrm{val}(x)\cdot\mathrm{val}(y))$, the $2n$-bit representation of the product. Each value is at most $2^n-1$, so the product is below $2^{2n}$ and fits in $2n$ bits.

For example, take $n = 2$, $x = 10$ and $y = 11$. Then $\mathrm{val}(x) = 2$ and $\mathrm{val}(y) = 3$, so the product is $6$, and the required output is $\mathrm{bin}_4(6) = 0110$.

Exactness must hold for every input length, not only for large $n$. <cite data-source="paper">The algorithm is exact for every input length</cite>

Exact integer multiplication is measured by [running time cost](running-time-cost.md), counted on a machine whose alphabet and number of tapes are fixed in advance. <cite data-source="paper">A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.</cite> The classical question is how fast this product can be computed. <cite data-source="paper">Schönhage and Strassen conjectured n log n as the optimal order of multiplication cost</cite> (see [the n log n optimality conjecture](n-log-n-conjecture.md)).
