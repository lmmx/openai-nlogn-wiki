Here $n$ is the number of bits in each of the two integers being multiplied. The $n\log n$ optimality conjecture is Schönhage and Strassen's proposal that $n\log n$ is the optimal order of cost for this multiplication. The conjecture is the benchmark that a faster algorithm must beat.

Costs are running times on a multitape Turing machine with a fixed, finite number of tapes. A cost has order $f(n)$ when it is $O(f(n))$, that is, at most a constant times $f(n)$ for all large $n$. "Optimal" means that no algorithm in this model runs in $o(n\log n)$ time.

Schönhage and Strassen's 1971 algorithm runs in $O(n\log n\log\log n)$ time <cite data-source="paper">two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>. Harvey and van der Hoeven later reached the unconditional $O(n\log n)$ upper bound, so the order $n\log n$ is achievable. The conjecture is posed against the upper bounds of the chain in [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md).

An upper bound shows what is achievable, not what is optimal. The conjecture is therefore a claim about a lower bound: no algorithm does better than $n\log n$.

The conjecture fails in the fixed-tape model used here. The paper obtains a strict power saving in the logarithmic factor in that model. <cite data-source="paper">We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model.</cite>
