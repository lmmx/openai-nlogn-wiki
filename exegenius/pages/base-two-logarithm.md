The base-2 logarithm, written $\lg n$, is a special case of the [Logarithm](logarithm.md) with the base fixed at 2. It is the scale on which the paper's main running-time bound is stated. The constant $\kappa$ is the fixed value $2^{-182}$ in that bound, which says that exact multiplication of two $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time.

The real number $\log_2 n$ is the exponent to which 2 must be raised to give $n$. It is an integer only when $n$ is a power of 2; otherwise it lies strictly between two consecutive integers. The ceiling $\lceil x\rceil$ of a real number $x$ is the smallest integer that is at least $x$.

The paper fixes the definition as <cite data-source="paper">Write lg n = max{⌈log2 n⌉, 1}.</cite> Here $\lceil \log_2 n\rceil$ is the least integer $m$ with $2^m \ge n$. For $n \ge 2$, $\log_2 n > 0$, so its ceiling is at least 1 and the $\max$ changes nothing. The $\max$ matters only at $n = 1$, where $\lceil \log_2 1\rceil = 0$ and the formula alone would give 0. <cite data-source="paper">Dimensions equal to one cause no exception, since our convention gives lg 1 = 1.</cite>

Worked values:

- $n = 8$: $2^3 = 8$, so $\lg 8 = 3$.
- $n = 10$: $2^3 < 10 \le 2^4$, so $\lceil \log_2 10\rceil = 4$ and $\lg 10 = 4$.
- $n = 1$: the $\max$ raises the value 0 to 1, so $\lg 1 = 1$.

Hence $\lg n \ge 1$ for every positive integer $n$.
