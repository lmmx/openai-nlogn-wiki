The established $O(n\log n)$ multiplier, also called the Harvey–van der Hoeven multiplier, is a known fixed-tape integer multiplier. It solves [exact integer multiplication](exact-integer-multiplication.md). The new algorithm uses it only as a black-box subroutine. Its cost bound contributes a term to the new algorithm's [cost table](cost-table.md).

We write $\log$ for the base-2 logarithm. Here $N$ is the number of bits in each input. The source describes the multiplier as <cite data-source="paper">the fixed-tape integer multiplier of Harvey and van</cite> der Hoeven, with <cite data-source="paper">cost O(N log(2N )) on N -bit inputs</cite>. Since $\log(2N)=\log N+1$ and $\log N\ge 1$ for $N\ge 2$, we get $\log(2N)\le 2\log N$, so the cost is $O(N\log N)$ for $N\ge 2$.

For example, take $N=4$, $u=1011$ (value $11$) and $v=0110$ (value $6$). The product is $66$, so the multiplier outputs the $2N$-bit string $01000010$.

The construction packs the coefficients of each polynomial into one large integer, multiplies two such integers with this multiplier, and unpacks the result (see [signed coefficient packing](signed-packing.md)). The source states this step as <cite data-source="paper">with an established integer multiplier.</cite>

The multiplier is an earlier algorithm, not the new theorem. The source says these calls <cite data-source="paper">are ordinary subroutine calls; they do not invoke the improved theorem recursively.</cite> So the construction does not call itself. Each call is charged its $O(N\log N)$ cost on its own inputs, taken as given. If a call used the new theorem, its cost would refer to the bound being proved.
