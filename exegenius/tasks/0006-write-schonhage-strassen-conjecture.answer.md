The Schönhage–Strassen optimality conjecture is a claim about how fast two integers can be multiplied on a multitape Turing machine, and it is the yardstick against which the target result is measured.

Here $n$ is the number of bits in each of the two integers being multiplied, and the time is the worst-case number of steps over inputs of that length. The conjecture says that $n\log n$ is the best possible order of growth for this time.

In 1971 Schönhage and Strassen gave a multiplication algorithm running in $O(n\log n\log\log n)$ time <cite data-source="paper">Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>, and they proposed $n\log n$ as the optimal order of growth <cite data-source="paper">proposed $n\log n$ as the optimal order of growth</cite>. Harvey and van der Hoeven later reached an unconditional $O(n\log n)$ upper bound <cite data-source="paper">Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound</cite>.

Since an $O(n\log n)$ algorithm exists, the open part of the conjecture is the matching lower bound: every multitape machine needs $\Omega(n\log n)$ worst-case time to multiply $n$-bit integers.

The conjecture is posed for multitape machines and is contrasted with the [fixed-tape machine model](fixed-tape-model.md), in which the target result is measured. The target result, [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md), has a smaller power of $\lg n$ in its logarithmic factor than $n\log n$ has, so this conjecture is the comparison point for it.
