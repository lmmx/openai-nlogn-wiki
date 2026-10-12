The Harvey–van der Hoeven multiplier is a deterministic algorithm that multiplies two $n$-bit integers in worst-case time $O(n\log n)$ on a multitape Turing machine, a machine with several tapes, each read and written by its own head. It is the <cite data-source="paper">unconditional $O(n\log n)$ upper bound</cite> for integer multiplication, so it needs no unproven hypothesis.

The target result treats this multiplier as an ordinary subroutine, charging each polynomial product it computes at the multiplier's cost. Each product has at most $n$ bits, so its logarithm is at most $\log n$. The sum of the charges is therefore at most a constant times $\log n$ times the total length of the products, which is $O(n\log n)$ when that total length is $O(n)$. The target's analysis is organized this way, so its running time inherits the bound.

The target's bound is $O(n(\lg n)^{1-\kappa})$ for a fixed constant $\kappa>0$. Its value is $2^{-182}$ <cite data-source="paper">$\kappa=2^{-182}$</cite>. Since $(\lg n)^{1-\kappa}/\lg n=(\lg n)^{-\kappa}$ tends to $0$ as $n$ grows, the target's bound grows strictly slower than $n\log n$.

The multiplier matches the $n\log n$ order that [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md) proposed as optimal. It is the baseline the target improves on, not the new bound.
