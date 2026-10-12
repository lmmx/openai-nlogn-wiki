Here $n$ is the number of bits in each input integer. The Harvey–van der Hoeven multiplier is a deterministic algorithm that multiplies two such integers in worst-case time $O(n\log n)$ on a multitape Turing machine, a machine with several tapes, each read and written by its own head. The bound counts steps as $n$ grows, and it is the <cite data-source="paper">unconditional $O(n\log n)$ upper bound</cite> for integer multiplication: it needs no unproven hypothesis.

The target result treats this multiplier as an ordinary subroutine with the cost above. Every polynomial product that the target computes is charged at this cost, so the target's running time inherits the bound.

The multiplier matters here as a comparison point. Its $O(n\log n)$ bound matches the order that Schönhage and Strassen conjectured as optimal. The target result beats that order, so the multiplier serves as the baseline the target must improve on, not as the new bound.
