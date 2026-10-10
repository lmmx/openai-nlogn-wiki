In 1971 Schönhage and Strassen gave a multiplication algorithm for [exact integer multiplication](exact-integer-multiplication.md) that runs in $O(n \log n \log\log n)$ time on a multitape Turing machine. They proposed $n \log n$ as the optimal order of growth for this problem. This proposal is the Schönhage–Strassen conjecture.

To state it precisely, write $\lg n = \log_2 n$. Say that a fixed machine $M$ that multiplies correctly, with running time $T_M(n)$, satisfies the *eventual $n\lg n$ lower bound* if there are constants $c > 0$ and $N$ such that $T_M(n) \ge c\, n \lg n$ whenever $n \ge N$. This is an eventual lower bound: it constrains the running time for all large $n$, not for a single input length. The conjecture says that every such machine $M$ satisfies the bound.

The conjecture is therefore refuted by one machine $A$ with $\liminf_{n\to\infty} T_A(n)/(n \lg n) = 0$. A machine with running time $O(n(\lg n)^{1-\kappa})$ for a fixed $\kappa > 0$ has this property, since $(\lg n)^{1-\kappa}/\lg n \to 0$. The paper's main theorem uses $\kappa = 2^{-182}$.

Harvey and van der Hoeven later proved an unconditional $O(n \log n)$ upper bound, which matched the conjectured order up to a constant. The conjecture was therefore about whether that $\log n$ factor could be removed, not about whether a faster bound exists at all.
