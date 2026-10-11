The limit inferior of a sequence of real numbers is the smallest value that the sequence keeps approaching as its index grows. The paper states the negation of its lower bound on multiplication time with it.

Here $k$ and $m$ are position indices on this page. Let $\chi_1, \chi_2, \chi_3, \dots$ be a sequence of real numbers, where $\chi_k$ is the $k$-th term. For each position $m$, let $\tau_m$ be the infimum of the terms from position $m$ on: the largest number that is at most every term $\chi_k$ with $k \ge m$. The infimum over fewer terms never decreases as $m$ grows. The limit inferior takes its values in the [extended real numbers](extended-reals.md), and it is $-\infty$ when the terms are unbounded below. It is the limit of this sequence:
$$\liminf_{k\to\infty} \chi_k = \lim_{m\to\infty} \tau_m.$$

For example, if $\chi_k = (-1)^k + 1/k$, every tail has infimum $-1$, so $\liminf_{k\to\infty} \chi_k = -1$.

**Zero limit inferior for nonnegative sequences.** Suppose every $\chi_k \ge 0$, and let $\varepsilon$ be a positive real tolerance. Then $\liminf_{k\to\infty} \chi_k = 0$ exactly when for every $\varepsilon > 0$ there are infinitely many $k$ with $\chi_k < \varepsilon$. The reason: each $\tau_m$ is nonnegative and nondecreasing, so the limit is $0$ exactly when $\tau_m = 0$ for every $m$. And $\tau_m = 0$ means no positive number is a lower bound of the tail, that is, for each $\varepsilon > 0$ some $k \ge m$ has $\chi_k < \varepsilon$. Requiring this for every $m$ means infinitely many such $k$.

**Use in the paper.** Here $n$ is the input length in bits, and $\lg$ is the [base-2 logarithm](base-two-logarithm.md). For a fixed machine $A$, $\mathcal{T}_A(n)$ is the worst-case running time of $A$ on inputs of $n$ bits. Here $\delta_A > 0$ is a real constant and $\Gamma_A$ is a threshold on input length. The [n log n optimality conjecture](n-log-n-conjecture.md) says that for each fixed machine $A$ there are such constants, with
$$\mathcal{T}_A(n) \ge \delta_A\, n\lg n \quad \text{whenever } n \ge \Gamma_A.$$
The paper states it as <cite data-source="paper">for each fixed machine A, there are constants cA > 0 and NA such that TA (n) ≥ cA n lg n</cite>.

The limit inferior is applied to the ratio of time to the [Schönhage–Strassen bound](schonhage-strassen.md) $n\lg n$, that is, to $\mathcal{T}_A(n)/(n\lg n)$. The negation for $A$ says that for every $\delta > 0$ and every threshold $\Gamma$, some $n \ge \Gamma$ has $\mathcal{T}_A(n) < \delta\, n\lg n$. The ratio is nonnegative for $n \ge 2$, so this says the ratio falls below every $\delta > 0$ infinitely often: $\liminf_{n\to\infty} \mathcal{T}_A(n)/(n\lg n) = 0$. The paper states it as <cite data-source="paper">Its negation requires one machine satisfying lim inf n→∞ TA (n)/(n lg n) = 0.</cite>

The main theorem, on [Integer multiplication below n log n](main-theorem.md), gives one machine $A$ with a time bound. Here $\kappa = 2^{-182}$ is a fixed exponent with $0 < \kappa < 1$, and $C$ is a constant: $\mathcal{T}_A(n) \le C\, n(\lg n)^{1-\kappa}$ for all large $n$. This page uses that bound without proving it: <cite data-source="paper">We give a deterministic algorithm that multiplies two n-bit integers in O(n(lg n)1−κ )</cite>.

Dividing by $n\lg n$ gives $0 \le \mathcal{T}_A(n)/(n\lg n) \le C(\lg n)^{-\kappa}$. Since $\kappa > 0$ and $\lg n \to \infty$, the right side tends to zero, so the ratio's limit, and its limit inferior, is zero. This refutes the conjecture: <cite data-source="paper">The algorithm is exact for every input length and disproves the n log n</cite>.
