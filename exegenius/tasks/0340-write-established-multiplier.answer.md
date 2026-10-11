The established multiplier is a known fixed-tape integer multiplier, and it solves [exact integer multiplication](exact-integer-multiplication.md). The [main theorem](main-theorem.md) uses it only through its cost bound, which is one term of the new algorithm's [cost table](cost-table.md).

We write $\log$ for the base-2 logarithm. Here $N$ is the number of bits in each input. The source calls the multiplier <cite data-source="paper">the fixed-tape integer multiplier of Harvey and van</cite> der Hoeven, and its cost is <cite data-source="paper">cost O(N log(2N )) on N -bit inputs</cite>. Since $\log(2N)=\log N+1$ and $\log N\ge 1$ for $N\ge 2$, we get $\log(2N)\le 2\log N$, so the cost is $O(N\log N)$ for $N\ge 2$.

For example, take $N=4$, $x=1011$ (value $11$) and $y=0110$ (value $6$). The product is $66$, so the multiplier outputs the $2N$-bit string $01000010$.

The construction packs the coefficients of each polynomial into one large integer, multiplies two such integers with this multiplier, and unpacks the result (see [signed coefficient packing](signed-packing.md)). The source states this step as <cite data-source="paper">with an established integer multiplier.</cite>

The multiplier is Harvey and van der Hoeven's algorithm, not the new theorem. The source says of these calls: <cite data-source="paper">they do not invoke the improved theorem recursively.</cite> So the construction never calls itself. Each call is charged the $O(N\log N)$ cost on its own inputs, taken as given, and these charges are summed in the cost table.
