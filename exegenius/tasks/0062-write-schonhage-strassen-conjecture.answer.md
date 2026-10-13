The Schönhage–Strassen optimality conjecture is a claim about the fastest possible multiplication of two integers on a multitape Turing machine, and it is the yardstick for the target result.

Here $n$ is the number of bits in each of the two integers being multiplied. The time is the worst-case number of steps over inputs of that length, and the conjecture says that $n\log n$ is the best possible order of growth for it.

In 1971 Schönhage and Strassen gave an algorithm running in $O(n\log n\log\log n)$ time <cite data-source="paper">Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>, and they proposed $n\log n$ as the optimal order of growth <cite data-source="paper">proposed $n\log n$ as the optimal order of growth</cite>. Harvey and van der Hoeven later reached an unconditional $O(n\log n)$ upper bound <cite data-source="paper">Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound</cite>.

Since an $O(n\log n)$ algorithm exists, the open part of the conjecture is the matching lower bound: every multitape machine needs $\Omega(n\log n)$ worst-case time to multiply $n$-bit integers.

The conjecture is posed for multitape machines and is contrasted with the [fixed-tape machine model](fixed-tape-model.md), in which the target result is measured. The target result, [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md), computes the integer product exactly on one fixed-tape machine. Here $\kappa>0$ is a fixed constant. Its worst-case time is $O(n(\lg n)^{1-\kappa})$, whose exponent $1-\kappa$ on $\lg n$ is less than 1.

The target's bound is smaller than $n\log n$ by the factor $(\lg n)^{\kappa}$, because $n\log n = n(\lg n)^{1-\kappa}\cdot(\lg n)^{\kappa}$ and $(\lg n)^{\kappa}\to\infty$ as $n\to\infty$. That strict power saving <cite data-source="paper">We obtain a strict power saving in the logarithmic factor</cite> is why the conjecture is the comparison point.
