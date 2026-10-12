Exact integer multiplication is the task of multiplying two binary integers and returning every bit of the product, with no rounding or truncation. Here $n$ is the number of bits in each input. The target result lowers the cost of this problem, so this page fixes its exact input and output.

Let $x$ and $y$ be binary strings of length $n$, the two inputs.

For a binary string $x$, $\mathrm{val}(x)$ is its nonnegative integer value, with the leftmost bit most significant. Here $k$ is the number of bits of the padded representation and $z$ is an integer with $0 \le z < 2^k$. Then $\mathrm{bin}_k(z)$ is the binary representation of $z$ padded on the left with zeros to exactly $k$ bits.

On input $x\#y$, where $\#$ separates the two strings, the machine must output $\mathrm{bin}_{2n}(\mathrm{val}(x)\,\mathrm{val}(y))$. The width $2n$ is enough because the product of two $n$-bit values is less than $2^{2n}$. For example, take $n=2$, $x=10$ and $y=11$. Then $\mathrm{val}(x)=2$, $\mathrm{val}(y)=3$, and the output is $\mathrm{bin}_4(6)=0110$.

Schönhage and Strassen proved in 1971 that the problem can be solved in $O(n\log n\log\log n)$ time <cite data-source="paper">two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine</cite>. Harvey and van der Hoeven later reached an $O(n\log n)$ upper bound <cite data-source="paper">unconditional O(n log n) upper bound</cite>. The target result saves a power of the logarithmic factor over this bound, in the same fixed finite-tape model.
