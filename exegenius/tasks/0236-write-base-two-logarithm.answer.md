The base-2 logarithm is a special case of the [Logarithm](logarithm.md), with the base fixed at 2. It is the function in which the paper's main running-time bound is stated, so that bound's logarithmic factor is measured on this scale.

Throughout, $n$ is a positive integer, the argument of the logarithm. The base-2 logarithm of $n$ is the exponent $x$ with $2^x = n$; that exponent is an integer only when $n$ is a power of 2, and for other $n$ it is a real number strictly between two consecutive integers. The ceiling $\lceil x \rceil$ of a real number $x$ is the smallest integer that is at least $x$.

Writing $\lg n$ for the base-2 logarithm of $n$, this means $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$: the least integer $k$ with $2^k \ge n$, or 1 if that is smaller. The paper fixes this as <cite data-source="paper">Write lg n = max{⌈log2 n⌉, 1}.</cite> The $\max$ changes the value only at $n = 1$, where $\lceil \log_2 1\rceil = 0$.

Worked values:

- $n = 8$: $2^3 = 8$, so $\lg 8 = 3$.
- $n = 10$: $2^3 = 8 < 10 \le 16 = 2^4$, so $\lceil \log_2 10\rceil = 4$ and $\lg 10 = 4$.
- $n = 1$: the formula gives 0, and the $\max$ replaces it by 1. <cite data-source="paper">Dimensions equal to one cause no exception, since our convention gives lg 1 = 1.</cite>

So $\lg n \ge 1$ for every $n \ge 1$.
