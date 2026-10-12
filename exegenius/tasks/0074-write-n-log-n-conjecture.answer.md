The n log n optimality conjecture is the claim that exact integer multiplication cannot be done faster, in order of growth, than $n\log n$. It is also called the Schönhage–Strassen conjecture.

Let $n$ be the number of bits in each of the two input integers. The conjecture bounds the cost of [Exact integer multiplication](exact-integer-multiplication.md), where the input is two $n$-bit binary strings and the output is their $2n$-bit product.

Schoolbook multiplication takes $O(n^2)$ bit operations, so the question is how far below that the best method can go. Schönhage and Strassen gave in 1971 a multitape Turing machine algorithm that runs in $O(n\log n\log\log n)$ time, and <cite data-source="paper">proposed n log n as the optimal order of growth</cite>.

Later, Harvey and van der Hoeven reached an unconditional $O(n\log n)$ upper bound, one that holds without any extra hypothesis <cite data-source="paper">Harvey and van der Hoeven reached the unconditional O(n log n) upper bound</cite>. The conjecture therefore asks whether the extra $\log\log n$ factor, and any other gap, can be closed.

Saying $n\log n$ is optimal means no algorithm can do asymptotically better than this order. A faster method in a restricted model, such as a [fixed-tape machine](fixed-tape-model.md) (a Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes), does not by itself settle the conjecture.
