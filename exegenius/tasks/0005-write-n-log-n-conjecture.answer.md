The n log n optimality conjecture is the claim that exact integer multiplication cannot be done faster, in order of growth, than n log n. It is also called the Schönhage–Strassen conjecture, and the main result is measured against it.

Let $n$ be the number of bits in each of the two input integers. The conjecture bounds the cost of [Exact integer multiplication](exact-integer-multiplication.md), where the input is two $n$-bit binary strings and the output is their $2n$-bit product.

Schoolbook multiplication takes $O(n^2)$ bit operations, so the question is how far below that the best method can go. Schönhage and Strassen gave in 1971 a multitape Turing machine algorithm that runs in $O(n\log n\log\log n)$ time, and <cite data-source="paper">proposed n log n as the optimal order of growth</cite>.

Later algorithms reached $O(n\log n)$ for multiplication, so the conjecture asks whether the extra $\log\log n$ factor, and any other gap, can be closed. Saying $n\log n$ is optimal means no algorithm can do asymptotically better than this order. The conjecture is a claim about the order of growth, so a faster bound in a restricted machine model does not by itself settle it in general.
