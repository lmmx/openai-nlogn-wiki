The Harvey–van der Hoeven multiplier is a deterministic algorithm that multiplies two $n$-bit integers in worst-case time $O(n\log n)$ on a multitape Turing machine, a machine with several tapes, each read and written by its own head. It is the <cite data-source="paper">unconditional $O(n\log n)$ upper bound</cite> for integer multiplication, so it needs no unproven hypothesis.

It matches the $n\log n$ order proposed as optimal by [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md). It is the baseline the target improves on, not the new bound.

The target's bound is $O(n(\lg n)^{1-\kappa})$ for a fixed constant $\kappa>0$. Its value is $2^{-182}$ <cite data-source="paper">$\kappa=2^{-182}$</cite>. Since $(\lg n)^{1-\kappa}/\lg n=(\lg n)^{-\kappa}$ tends to $0$ as $n\to\infty$, the target's bound grows strictly slower than $n\log n$.
