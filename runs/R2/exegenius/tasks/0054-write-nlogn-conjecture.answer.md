The $n\log n$ optimality conjecture is Schönhage and Strassen's proposal that $n\log n$ is the optimal order of cost for multiplying two integers, where $n$ is the number of bits in each integer. It is the benchmark that a faster algorithm must beat.

Costs are running times on a multitape Turing machine with a fixed, finite number of tapes. A cost has order $f(n)$ when it is $O(f(n))$, that is, at most a constant times $f(n)$ for all large $n$. "Optimal" means that no algorithm in this model runs in $o(n\log n)$ time.

Schönhage and Strassen's 1971 algorithm runs in $O(n\log n\log\log n)$ time <cite data-source="paper">two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>. Harvey and van der Hoeven reached $O(n\log n)$, so that order is achievable. The conjecture is posed against this chain of upper bounds.

The conjecture fails in the fixed-tape model used here. Let $A$ be the paper's deterministic machine, and let $T_A(n)$ be its worst-case running time on pairs of $n$-bit inputs. Here $\kappa=2^{-182}$ is a fixed positive constant. The paper proves <cite data-source="paper">T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)</cite>, so $\lg n$ is replaced by $(\lg n)^{1-\kappa}$, a smaller power of the logarithm.

This is $o(n\log n)$, since
$$\frac{T_A(n)}{n\lg n}=O\big((\lg n)^{-\kappa}\big)\to 0$$
because $\kappa>0$. So $A$ runs in $o(n\log n)$ time, which contradicts the conjecture that no machine in this model runs in $o(n\log n)$ time.
