# Exact integer multiplication

Exact integer multiplication takes two binary strings of length $n$ and returns the full binary representation of their product. For $x \in \{0,1\}^n$, let $\mathrm{val}(x)$ be its nonnegative integer value, with the leftmost bit most significant. On input $x\#y$, the machine must output the $2n$-bit string representing $\mathrm{val}(x)\cdot\mathrm{val}(y)$, padded with leading zeroes.

"Exact" means there is no rounding and no error: the output is the true product for every pair of inputs, not an approximation with a bounded error. Any product of two $n$-bit numbers fits in $2n$ bits, so the output length is fixed in advance.

For example, with $n = 3$, take $x = 101$ (so $\mathrm{val}(x) = 5$) and $y = 011$ (so $\mathrm{val}(y) = 3$). The product is $15$, which is $001111$ in six bits, so the machine must output `001111`.

The problem is a computation on a [multitape Turing machine](turing-machine-model.md), and the cost of an algorithm is measured as a function of $n$. The paper attributes to Harvey and van der Hoeven an unconditional $O(n \log n)$ algorithm for this problem, which was the best upper bound known before the paper. Whether $n \log n$ can be beaten is the question of the [Schönhage–Strassen conjecture](n-log-n-conjecture.md).

The paper's main theorem is an exact algorithm in this same model whose worst-case time is $O(n(\lg n)^{1-\kappa})$ for a fixed $\kappa = 2^{-182}$. Here $\lg n = \log_2 n$ denotes the base-2 logarithm.

## Used by

- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Radix-digit convolution](radix-digit-convolution.md)

## Sources

> We consider exact multiplication
>
> — Integer multiplication below n log n (OpenAI, 2026)
