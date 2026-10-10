In 1971 Schönhage and Strassen gave a multiplication algorithm for [exact integer multiplication](exact-integer-multiplication.md) that runs in $O(n \log n \log\log n)$ time on a multitape Turing machine. They proposed $n \log n$ as the optimal order of growth for this problem. This proposal is the Schönhage–Strassen conjecture.

To state it precisely, call a machine $A$ with running time $T_A(n)$ *optimal at $n \log n$* if, for every fixed machine $A$ that multiplies correctly, there are constants $c_A > 0$ and $N_A$ such that $T_A(n) \ge c_A\, n \lg n$ whenever $n \ge N_A$. This is an eventual lower bound: it constrains the running time for all large $n$, not for a single input length.

The conjecture is therefore refuted by one machine $A$ with $\liminf_{n\to\infty} T_A(n)/(n \lg n) = 0$. A machine with running time $O(n(\lg n)^{1-\kappa})$ has this property, since $(\lg n)^{1-\kappa}/\lg n \to 0$. The paper's main theorem supplies such a machine, and it does so with a limit of zero rather than just a smaller constant factor.

Harvey and van der Hoeven later proved an unconditional $O(n \log n)$ upper bound, which matched the conjectured order up to a constant. The conjecture was therefore about whether that $\log n$ factor could be removed, not about whether a faster bound exists at all.
