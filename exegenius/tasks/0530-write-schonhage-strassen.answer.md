Schönhage–Strassen multiplication is a fast method for [Exact integer multiplication](exact-integer-multiplication.md), and it is the bound that the paper's main theorem sharpens.

<cite data-source="paper">Schönhage and Strassen proved in 1971 that two n-bit integers can be multiplied in O(n log n log log n)</cite> time on a multitape Turing machine. The main theorem improves this to $O(n(\lg n)^{1-\kappa})$ time, with $\kappa = 2^{-182}$, on the same kind of machine: <cite data-source="paper">We obtain a strict power saving in the logarithmic factor</cite>.

Let $\sigma$ be the number of bits in a residue. Schönhage–Strassen multiplication is based on [Congruence](congruence-modulo.md) modulo $2^\sigma+1$, so two integers are congruent when $2^\sigma+1$ divides their difference. The integers modulo $2^\sigma+1$ form a ring, a set with addition and multiplication obeying the usual axioms; it is called Fermat-type because its modulus has the form $2^\sigma+1$.

In this ring $2^\sigma\equiv-1$. For $\sigma=4$ and modulus $17$, $2^4=16\equiv-1$, so $2^8\equiv1$. Schönhage–Strassen multiplication counts its distinct roots of unity by the [Order of an element](order-of-element.md) of $2$, which is $8$ here.

Let $\xi$, with $0\le\xi<\sigma$, be the number of places a multiplication shifts. For a residue $\zeta$, $0\le\zeta<2^\sigma$, let $i$ be a bit position, not the imaginary unit, and let $\zeta_i\in\{0,1\}$ be the bit of $\zeta$ at position $i$. Write $\zeta=\sum_{i=0}^{\sigma-1}\zeta_i2^i$. Then $2^\xi\zeta\equiv\sum_i\zeta_i2^{i+\xi}$. Each term with $i+\xi\ge\sigma$ equals $-\zeta_i2^{i+\xi-\sigma}$, because $2^\sigma\equiv-1$. So multiplying by $2^\xi$ shifts the bits up $\xi$ places, and a bit passing the top returns at the bottom negated.

Take $\sigma=4$, $\zeta=3$, $\xi=3$. Then $2^3\cdot3\equiv7 \pmod{17}$. Bit $\zeta_0=1$ moves to position $3$, giving $8$; bit $\zeta_1=1$ moves to position $4$, which wraps to $-2^0=-1$. The sum is $8-1=7$.
