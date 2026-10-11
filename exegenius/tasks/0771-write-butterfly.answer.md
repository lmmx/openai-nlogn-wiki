The butterfly is the two-point map $H_0$ that replaces a pair of values by their half-sum and half-difference. The butterfly is an elementary step of the [Discrete Fourier transform](discrete-fourier-transform.md). The [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies it to several address bits at once.

Let $u$ be the first input value and $v$ the second, and here these letters do not keep the meanings they have on earlier pages. The map is

$$H_0(u,v)=\left(\frac{u+v}{2},\frac{u-v}{2}\right).$$

For example, $H_0(3,1)=(2,1)$ and $H_0(2,1)=\left(\tfrac32,\tfrac12\right)$. Applying $H_0$ twice halves the pair: $H_0^2=\tfrac12\,\mathrm{id}$ <cite data-source="paper">H02 = I/2</cite>. This is what makes the inverse work: <cite data-source="paper">the reversed level is half the inverse of the corresponding forward level</cite>.

A transform on $q$ entries, with $q$ a power of two, runs in $\log_2 q$ levels. Write each position in binary with $\log_2 q$ bits. Let $\Xi$ be the index of the bit a level acts on, counted from $0$ at the least significant end. A level with index $\Xi$ applies $H_0$ to every pair of positions that differ only in bit $\Xi$. For $q=4$, level $0$ pairs positions $00$ with $01$ and $10$ with $11$, and level $1$ pairs $00$ with $10$ and $01$ with $11$.

When each entry is a record, that is, a polynomial with complex coefficients, <cite data-source="paper">H0 acts coefficientwise</cite>. The two output records take, at each coefficient position, the $H_0$ of the two input coefficients at that position.

Each pair costs two additions and two halvings, a fixed amount of arithmetic. A level touches each of the $q$ entries once, so it costs $O(q)$ operations, and the $\log_2 q$ levels cost $O(q\log_2 q)$ in total.

In the paper, a round applies the butterfly and then <cite data-source="paper">one recordwise monomial operation JE</cite>. This operation multiplies each record by a power of $y$, a monomial in the polynomial variable. <cite data-source="paper">multiplication by such a root is a signed shift of the</cite> coefficient list. The butterfly is followed by a [Cyclic shift](cyclic-shift.md) of each record.
