The ceiling function is the rounding-up operation that the paper's method needs before it can turn recovered integer coefficients into a binary product. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite> The recovered values are then rounded to integers, and carry propagation, which adds each coefficient to the carry from the position below it, writes them as bits. <cite data-source="paper">Known rescalings, rounding, and carry propagation then recover the exact integer product.</cite> The ceiling rounds up recovered coefficients on the way to the binary product of [exact integer multiplication](exact-integer-multiplication.md).

Let $s$ be a real number. The ceiling $\lceil s \rceil$ is the least integer that is not less than $s$. Some values:

$$\lceil 2.3 \rceil = 3, \qquad \lceil 4 \rceil = 4, \qquad \lceil -1.5 \rceil = -1.$$

The symbol $j$ stands for any integer, and an integer is its own ceiling: $\lceil j \rceil = j$. For a real number that is not an integer, the ceiling is the next integer above it. Counting groups is a typical use: $7$ values grouped into pairs need $\lceil 7/2 \rceil = 4$ pairs, the last of which holds a single value.
