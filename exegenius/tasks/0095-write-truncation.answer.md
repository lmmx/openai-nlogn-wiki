Truncation is the rounding rule that keeps stored numerical values on a fixed grid. It discards every binary digit beyond a chosen number of fractional places, so a value needs only a fixed number of bits. The error this introduces is small and bounded, which is what lets the multiplication algorithm control the error of its approximate values.

Let $p$ be the number of fractional binary places kept. Truncation to precision $p$ replaces each real and imaginary part of a number by the nearest multiple of $2^{-p}$ that lies between it and zero. <cite data-source="paper">toward zero to p fractional bits</cite>

Truncation goes toward zero, not toward minus infinity. With $p = 2$ the grid is the multiples of $1/4$. The real number $0.61$ truncates to $0.5$, and $-0.61$ truncates to $-0.5$. The complex number $0.61 - 0.87i$ truncates to $0.5 - 0.75i$, because the rule is applied to the real and imaginary parts separately.

For an array $z$ of complex coefficients, $Q_p z$ is the array obtained by truncating each real and imaginary coefficient part to the grid $2^{-p}\mathbb{Z}$, the set of multiples of $2^{-p}$. <cite data-source="paper">let Qp truncate each real and imaginary coefficient part toward zero to this grid.</cite> An array with all parts on this grid is a $p$-bit grid array. <cite data-source="paper">A p-bit grid array has real and imaginary coefficient parts in 2−p Z.</cite>

Two properties of $Q_p$ are used later. The first is that truncation does not enlarge an array. The norm $\|z\|_\infty$ is the maximum absolute value over all coefficient parts of the array, and <cite data-source="paper">truncation cannot increase the absolute value of either component</cite>, so

$$\|Q_p z\|_\infty \le \|z\|_\infty.$$

The second is that the change made by truncation is small. Each part moves by less than $2^{-p}$, and the source gives the bound for the whole array as

$$\|Q_p z - z\|_\infty < 2\sqrt{2}\,2^{-p}$$

<cite data-source="paper">has error less than 2 2−p</cite>

The error bound is per truncation. Because of this, the algorithm does not truncate inside a layer. <cite data-source="paper">The entire layer is evaluated exactly before one final truncation.</cite> The layer's error is therefore one truncation error of the size above, rather than a sum of errors from every intermediate step.

In the implementation, an exact intermediate value is held as an integer numerator over a larger power of two. Truncation shifts the absolute value of that numerator right, which discards the low bits of the magnitude, and then restores the sign. <cite data-source="paper">right by the number of added fractional bits, restore its sign</cite> Removing the low bits of the magnitude and then restoring the sign gives truncation toward zero, because the magnitude is never rounded up.
