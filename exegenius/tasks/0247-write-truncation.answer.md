Truncation is the rounding rule that keeps stored numbers on a fixed grid, so each stored number needs only a fixed number of bits. The multiplication algorithm truncates only once per layer of exact arithmetic, and the bound on that one error is what lets the final rounding recover the exact integer coefficients.

Let $p$ be the number of fractional binary places kept, so the grid spacing is $2^{-p}$. Truncation to precision $p$ replaces each real and imaginary part of a number by the nearest multiple of $2^{-p}$ that lies between it and zero. <cite data-source="paper">toward zero to p fractional bits</cite>

Truncation goes toward zero, not toward minus infinity. With $p = 2$ the grid is the multiples of $1/4$. The real number $0.61$ truncates to $0.5$, and $-0.61$ truncates to $-0.5$. The complex number $0.61 - 0.87i$ truncates to $0.5 - 0.75i$, because the rule is applied to the real and imaginary parts separately.

Let $z$ be a finite list of complex numbers, called coefficients. Then $Q_p z$ is the list obtained by truncating each real and imaginary part of each coefficient toward zero to the grid $2^{-p}\mathbb{Z}$. <cite data-source="paper">let Qp truncate each real and imaginary coefficient part toward zero to this grid.</cite> Truncation to precision $p$ is built from the [Integer](integer.md) $\mathbb{Z}$, the set of integers, because its grid $2^{-p}\mathbb{Z}$ consists of the multiples of $2^{-p}$. A list whose parts all lie on this grid is a $p$-bit grid array. <cite data-source="paper">A p-bit grid array has real and imaginary coefficient parts in 2−p Z.</cite>

The error of truncation is measured by the [Array norm](array-norm.md) $\|\cdot\|_\infty$, the largest complex modulus of any coefficient. Two properties of truncation matter for the error argument.

First, truncation does not enlarge the list. <cite data-source="paper">truncation cannot increase the absolute value of either component</cite>, so no coefficient's modulus grows, and
$$\|Q_p z\|_\infty \le \|z\|_\infty.$$

Second, each truncation changes a coefficient only a little. <cite data-source="paper">changes each by less than 2−p</cite>, so the real and imaginary parts of the error of one coefficient are each below $2^{-p}$ in absolute value. Its modulus is then below $\sqrt{2\cdot 2^{-2p}} = \sqrt{2}\,2^{-p}$. The paper states the weaker bound <cite data-source="paper">has error less than 2 2−p</cite>, namely
$$\|Q_p z - z\|_\infty < 2\sqrt{2}\,2^{-p}.$$

A layer, written $H$, is one pass that replaces each pair of values $(\alpha,\beta)$ by $((\alpha+\beta)/2,(\alpha-\beta)/2)$, for every pair of entries whose addresses differ in one of several selected bits. <cite data-source="paper">The entire layer is evaluated exactly before one final truncation.</cite> Since <cite data-source="paper">every intermediate coefficient is represented exactly</cite>, the only rounding in a layer is $Q_p$ applied to the exact result $Hz$. The layer's error is therefore $\|Q_p(Hz) - Hz\|_\infty$, one truncation error of the size above. It is not a sum over intermediate steps, because none of them rounds.

In the implementation, an exact intermediate value is held as an integer numerator over a larger power of two. The paper's procedure is to <cite data-source="paper">shift its absolute numerator right by the number of added fractional bits, restore its sign</cite>. Shifting the magnitude right discards its low bits, so the magnitude is rounded down, never up, and restoring the sign gives truncation toward zero.
