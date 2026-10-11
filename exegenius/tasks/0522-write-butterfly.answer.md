The butterfly is an elementary step of the [Discrete Fourier transform](discrete-fourier-transform.md), the two-point map that replaces a pair of values by their half-sum and half-difference. The [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies it to several address bits at once.

Let $\xi$ and $\zeta$ be the two input values, which the paper calls $u$ and $v$. $H_0$ is the two-point map that sends a pair to its half-sum and half-difference: $H_0(\xi,\zeta)=\left(\frac{\xi+\zeta}{2},\frac{\xi-\zeta}{2}\right)$.

For example, $H_0(3,1)=(2,1)$ and $H_0(2,1)=(3,1)/2$. Two applications therefore halve the pair: <cite data-source="paper">H02 = I/2</cite>, that is, $H_0^2=\tfrac12\,\mathrm{id}$.

A transform on $q$ entries, with $q$ a power of two, runs in $\log_2 q$ levels. Write each position as $\log_2 q$ bits, and let $\sigma$ be the index of one bit, counting from $0$ at the least significant end. Level $\sigma$ applies $H_0$ to every pair of positions that differ only in bit $\sigma$. For $q=4$, level 0 pairs positions 00 with 01 and 10 with 11, and level 1 pairs 00 with 10 and 01 with 11.

When each entry is a record, $H_0$ acts <cite data-source="paper">H0 acts coefficientwise</cite>. For each coefficient position $d$, the two output coefficients at $d$ are $H_0$ of the two input coefficients at $d$, one from each record of the pair.

Each pair needs a fixed amount of arithmetic, two additions and halvings. A level touches each of the $q$ entries once, so it costs time linear in $q$, and the $\log_2 q$ levels cost $O(q\log q)$.

The butterfly is followed by a signed [Cyclic shift](cyclic-shift.md) of each record, which rotates the coefficients and negates those that wrap around. The paper's level applies the butterfly, then <cite data-source="paper">one recordwise monomial operation</cite>.
