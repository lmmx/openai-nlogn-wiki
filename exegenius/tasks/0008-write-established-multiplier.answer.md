The established $O(n\log n)$ multiplier (also called the Harvey–van der Hoeven multiplier) solves [exact integer multiplication](exact-integer-multiplication.md) on pairs of $N$-bit inputs, where $N$ is the number of bits in each input, in $O(N\log N)$ time. The [main theorem](main-theorem.md) is proved by a construction that calls this multiplier as a subroutine, so its running time enters the new algorithm's cost table.

The source calls it <cite data-source="paper">the fixed-tape integer multiplier of Harvey and van</cite> der Hoeven. A fixed-tape machine is a Turing machine whose alphabet and number of one-dimensional tapes are fixed and do not grow with the input length. Its cost is <cite data-source="paper">with cost O(N log(2N )) on N -bit inputs</cite>, which is $O(N\log N)$ for $N\ge 2$, because $\log(2N)=\log N+1$.

For example, take $N=4$, $x=1011$ (value $11$) and $y=0110$ (value $6$). The product is $66$, so the multiplier outputs the $2N$-bit string $01000010$.

In the construction, polynomial products are computed by packing each polynomial's coefficients into one large integer, multiplying the two integers with this multiplier, and unpacking the result (see [signed coefficient packing](signed-packing.md)). The proof states this step as <cite data-source="paper">with an established integer multiplier.</cite>

The multiplier is not the new algorithm, so the construction never calls itself: <cite data-source="paper">they do not invoke the improved theorem recursively</cite>. Its $O(N\log N)$ cost is taken as given and charged to each call.
