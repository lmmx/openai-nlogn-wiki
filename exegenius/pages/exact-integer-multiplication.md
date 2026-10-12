Exact integer multiplication is the problem of multiplying two binary integers and returning every bit of the product, with no rounding or truncation. The target result is a faster algorithm for this problem, so this page fixes its exact input and output.

Here $n$ is the number of bits in each input. Let $x$ and $y$ be binary strings of length $n$, the two inputs.

For a binary string $x$, $\mathrm{val}(x)$ is its nonnegative integer value, with the leftmost bit most significant. Here $k$ is the number of bits of the padded representation and $z$ is an integer with $0 \le z < 2^k$. Then $\mathrm{bin}_k(z)$ is the binary representation of $z$ padded on the left with zeros to exactly $k$ bits.

On input $x\#y$, where $\#$ separates the two strings, the machine must output $\mathrm{bin}_{2n}(\mathrm{val}(x)\,\mathrm{val}(y))$. The width $2n$ suffices because each value is at most $2^n-1$, so the product is at most $(2^n-1)^2<2^{2n}$. For example, take $n=2$, $x=10$ and $y=11$. Then $\mathrm{val}(x)=2$, $\mathrm{val}(y)=3$, and the output is $\mathrm{bin}_4(6)=0110$.

Schönhage and Strassen proved in 1971 that the problem can be solved in $O(n\log n\log\log n)$ time <cite data-source="paper">two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine</cite>. Harvey and van der Hoeven later reached the unconditional $O(n\log n)$ upper bound <cite data-source="paper">unconditional O(n log n) upper bound</cite>.

The target result improves the $O(n\log n)$ bound <cite data-source="paper">We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model</cite>. This model is a Turing machine with <cite data-source="paper">a fixed finite alphabet and a fixed finite number of one-dimensional tapes</cite>.
