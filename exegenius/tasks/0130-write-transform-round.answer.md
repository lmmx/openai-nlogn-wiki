A transform round is one stage of the [multidimensional transform](multidimensional-transform.md) on a set of participating axes. In it, every participating axis takes one butterfly step at the same time, and the twiddles those steps need are applied afterwards as one operation on each record. It is the basic step of the transforms used for convolution over the polynomial ring.

A *butterfly* on one axis replaces each pair of entries that differ only in one address bit by the pair's half-sum and half-difference. A *twiddle* is a power of $y$ by which a record is multiplied after a butterfly.

Consider a round on the $D$ participating axes. Here $i$ indexes the participating axes, and the letter changes meaning from its use for digit positions. Here $\ell_i$ is the current recursive length of axis $i$, the number of entries that axis holds at the level the round processes. Here $\beta_i$ is the branch bit that the round writes on axis $i$, the bit recording which output of the butterfly the entry is. Here $\nu_i$ is the index of the twiddle on axis $i$, with $0 \le \nu_i < \ell_i/2$, encoded by the address bits not yet processed. <cite data-source="paper">A round applies one current H0 on each participating axis.</cite>

The twiddle on axis $i$ is determined by that axis alone. <cite data-source="paper">The twiddle for axis i depends only on</cite> that axis’s address bits. <cite data-source="paper">The two entries paired by another axis’s butterfly have the same axis-i</cite> <cite data-source="paper">address, so that twiddle commutes with the other butterfly.</cite> Because each twiddle commutes with the butterflies on the other axes, the axis steps can be reordered: <cite data-source="paper">may be grouped as a parallel butterfly H, followed by one recordwise monomial operation JE</cite>.

The parallel butterfly $\Lambda$ is the tensor product of $H_0$ over the participating axes. A transform round computes its butterfly by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which applies $\Lambda$ to the selected bits in one pass. Here $\eta$ is the twiddle exponent at each address, an integer taken modulo $2r$, given by

$$
\eta = -\sum_{i} \frac{2r}{\ell_i}\,\beta_i\,\nu_i \pmod{2r},
$$

where the sum runs over the $D$ participating axes. The recordwise twiddle $\Gamma_\eta$ multiplies each record at its address by $y^\eta$. <cite data-source="paper">Here ui is that axis’s current recursive length, bi its newly written branch bit,</cite> <cite data-source="paper">The exponent depends on the address, not on</cite> coefficient values.

Multiplication by $y^\eta$ modulo $y^r+1$ rearranges coefficients without arithmetic on their values. Write $\eta = er + s$ with $0 \le s < r$. Since $y^r = -1$, multiplying by $y^\eta$ is multiplying by $y^s$ and then applying the sign $(-1)^e$, and multiplying by $y^s$ moves each coefficient up $s$ places and negates the coefficients that pass the top.

As a small example, take $r = 4$, $D = 2$, $\ell_1 = \ell_2 = 4$, $\beta_1 = 1$, $\nu_1 = 1$, $\beta_2 = 0$, and $\nu_2 = 1$. Then $\eta = -(2\cdot 1\cdot 1 + 2\cdot 0\cdot 1) \bmod 8 = 6$. Modulo $y^4+1$ we have $y^6 = -y^2$, so the record $c_0 + c_1 y + c_2 y^2 + c_3 y^3$ becomes $c_2 + c_3 y - c_0 y^2 - c_1 y^3$. Its coefficient list $(c_0, c_1, c_2, c_3)$ becomes $(c_2, c_3, -c_0, -c_1)$.

A contraction is a linear map that does not increase the norm of an array, and an isometry is one that preserves it. <cite data-source="paper">Each H is a contraction and each JE is an isometry</cite>, so the round as a whole does not increase the norm.
