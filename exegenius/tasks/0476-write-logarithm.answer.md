The logarithm is the inverse of exponentiation: it takes a positive number and returns the exponent to which a fixed base must be raised to give that number. The [main theorem](main-theorem.md) states its running time using this function, and the [cost table](cost-table.md) checks that every term is within that bound, so the bound cannot be read without the logarithm.

Here $b$ is the fixed base, a number greater than $1$, and $y$ is the positive number whose logarithm is taken. The logarithm of $y$ to base $b$, written $\log_b y$, is the exponent to which $b$ must be raised to give $y$. For example, $\log_3 81 = 4$, because $3^4 = 81$.

Here $n$ is a positive [integer](integer.md), the number whose base-2 logarithm is taken, and $\lg n$ is defined for every such integer. The paper uses base $2$ and writes $\lg n$ for it; see [Base-2 logarithm](base-two-logarithm.md). Its convention rounds up and never goes below $1$: <cite data-source="paper">Write lg n = max{⌈log2 n⌉, 1}.</cite> The ceiling $\lceil \log_2 n \rceil$ is the smallest integer that is at least $\log_2 n$, which is the same as the least power of two that is at least $n$.

For $n = 5$, $\log_2 5 \approx 2.32$, so $\lceil \log_2 5 \rceil = 3$ and $\lg 5 = 3$, which agrees with $2^2 = 4 < 5 \le 8 = 2^3$. For $n = 8$, $\log_2 8 = 3$ exactly, so $\lg 8 = 3$. For $n = 1$, $\log_2 1 = 0$, but the maximum with $1$ gives $\lg 1 = 1$. <cite data-source="paper">Dimensions equal to one cause no exception, since our convention gives lg 1 = 1.</cite> So $\lg n$ is never $0$.

The paper also writes plain $\log$ in one place, and there it means the natural logarithm, the logarithm to the base $e \approx 2.718$, not base $2$: <cite data-source="paper">Here log is the natural logarithm.</cite>
