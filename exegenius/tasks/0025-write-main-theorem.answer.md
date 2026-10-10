The main theorem says that there is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes the exact product of two $n$-bit integers for every $n \ge 1$. Its worst-case running time $T_A(n)$ satisfies

$$T_A(n) = O\bigl(n(\lg n)^{1-\kappa}\bigr), \qquad \kappa = 2^{-182}.$$

The bound is asymptotic: $T_A(n) \le C\, n(\lg n)^{1-\kappa}$ for some constant $C$ and all sufficiently large $n$. The paper notes that the constants and thresholds in the construction are very large, so the result establishes a bit-complexity bound, not a practical algorithm.

The statement uses the [multitape Turing machine](turing-machine-model.md) model and the exact product from [exact integer multiplication](exact-integer-multiplication.md). Compared with the best known bound $O(n \log n)$, the factor $\log n$ is replaced by $(\log n)^{1-\kappa}$, a strict power saving.

The theorem refutes the [Schönhage–Strassen conjecture](n-log-n-conjecture.md) in this model. An eventual $\Omega(n \log n)$ lower bound for every multiplication machine would require $T_A(n)/(n \lg n)$ to stay bounded below for each fixed machine. The machine $A$ has $T_A(n)/(n \lg n) \to 0$, so the lower bound fails for it.

The proof combines the [multiplication algorithm](multiplication-algorithm.md) with the [cost accounting](cost-accounting.md). The algorithm is exact for every input length, and the cost table shows that all its terms fit the bound, with the smallest margin $2\kappa$ absorbing the logarithmic factors. The [rank-saving recursion](rank-saving-recursion.md) supplies the strict inequality that produces the power saving.
