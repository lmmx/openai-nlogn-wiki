Truncation is the rounding rule that keeps stored numbers on a fixed grid, so each stored number needs only a fixed number of bits. The multiplication argument rounds a whole layer of computed values only once, and [Exact coefficient recovery](recovery-and-error.md) needs the size of that single rounding error, which this page bounds.

Let $p$ be the number of fractional binary places kept, so the grid spacing is $2^{-p}$. Truncation to precision $p$ replaces each real and imaginary part of a number by the nearest multiple of $2^{-p}$ that lies between it and zero. <cite data-source="paper">toward zero to p fractional bits</cite>

A fractional binary place is a position after the binary point, worth $1/2$, then $1/4$, and so on.

Truncation goes toward zero, not toward minus infinity. With $p = 2$ the grid is the multiples of $1/4$. The real number $0.61$ truncates to $0.5$, and $-0.61$ truncates to $-0.5$. The complex number $0.61 - 0.87i$ truncates to $0.5 - 0.75i$, since each part is truncated separately.

Let $w$ be a finite list of complex numbers, called coefficients. Then $Q_p w$ is the list obtained by truncating each real and imaginary part of each coefficient toward zero onto the grid $2^{-p}\mathbb{Z}$, where $\mathbb{Z}$ is the set of [integers](integer.md). <cite data-source="paper">let Qp truncate each real and imaginary coefficient part toward zero to this grid.</cite>

The error is measured by the [Array norm](array-norm.md) $\|\cdot\|_\infty$, the largest complex modulus of any coefficient, where the modulus of $a+bi$ is $\sqrt{a^2+b^2}$. Two properties of truncation matter here.

First, truncation does not enlarge the list. <cite data-source="paper">truncation cannot increase the absolute value of either component</cite>, so neither part of any coefficient grows in absolute value, and no modulus grows:
$$\|Q_p w\|_\infty \le \|w\|_\infty.$$

Second, each truncation moves each real and imaginary part by less than the grid spacing $2^{-p}$, since the truncated value is the nearest grid point between the value and zero. The modulus of the error in one coefficient is then below $\sqrt{2\cdot 2^{-2p}} = \sqrt{2}\,2^{-p}$.

A layer, written $H$, is one pass over the list. For every pair of entries whose [addresses](address.md) differ in one of several selected bits, with values $s$ and $r$, it replaces the pair by $((s+r)/2,(s-r)/2)$. Truncation is taken over pairs chosen by their [addresses](address.md), with one rounding per layer. The procedure <cite data-source="paper">evaluates the entire layer exactly before this final truncation.</cite> So the only rounding in a layer is $Q_p$ applied to the exact result $Hw$, and the layer's error is $\|Q_p(Hw) - Hw\|_\infty$, one truncation error of the size above. No intermediate step rounds, so no errors add up across steps.

The exact value is held as an integer numerator over a larger power of two. To truncate, the procedure shifts the magnitude of the numerator right, which discards its low bits, and restores the sign. Take $-13/16 = -0.8125$ with two fractional places kept. The magnitude $13$ shifted right by $2$ bits is $3$, and restoring the sign gives $-3/4 = -0.75$, the value toward zero on the grid. The paper does this by shifting its absolute numerator <cite data-source="paper">right by the number of added fractional bits, restore its sign, and write the result in w bits.</cite> Because the magnitude is rounded down and the sign is restored afterwards, the result is truncation toward zero.
