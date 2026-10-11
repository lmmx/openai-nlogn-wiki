The established $O(n\log n)$ multiplier solves [exact integer multiplication](exact-integer-multiplication.md). Here $N$ is the number of bits in each input, and the multiplier runs in $O(N\log N)$ time on two $N$-bit inputs. The [main theorem](main-theorem.md) is proved by a construction that calls this multiplier as a subroutine, so its cost is one term of the new algorithm's [cost table](cost-table.md).

The source calls it <cite data-source="paper">the fixed-tape integer multiplier of Harvey and van</cite> der Hoeven. A fixed-tape machine is a Turing machine whose alphabet and number of tapes do not depend on the input length. Its running time on $N$-bit inputs is <cite data-source="paper">O(N log(2N )) on N -bit inputs</cite>, which is $O(N\log N)$ for $N\ge 2$, because $\log(2N)=\log N+1$.

For example, take $N=4$, $x=1011$ (value $11$) and $y=0110$ (value $6$). The product is $66$, so the multiplier outputs the $2N$-bit string $01000010$.

The construction packs each polynomial's coefficients into one large integer, multiplies two such integers with this multiplier, and unpacks the result (see [signed coefficient packing](signed-packing.md)). The proof states this step as <cite data-source="paper">with an established integer multiplier.</cite>

The multiplier is not the new algorithm, so the construction never calls itself: it makes only ordinary subroutine calls to this multiplier, and <cite data-source="paper">they do not invoke the improved theorem recursively</cite>. Each call is charged the multiplier's $O(N\log N)$ cost on its own inputs, taken as given, and these charges are summed in the cost table.
