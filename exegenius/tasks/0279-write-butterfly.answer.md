The butterfly is the two-point map $H_0$, the basic step of the transforms in the multiplication method.

Let $\delta$ and $\theta$ be the two input values; the sources call them $u$ and $v$, but $u$ already denotes a field width. The butterfly is $H_0(\delta,\theta)=\left(\frac{\delta+\theta}{2},\frac{\delta-\theta}{2}\right)$, which replaces a pair by its half-sum and half-difference.

For example, $H_0(3,1)=(2,1)$ and $H_0(2,1)=(3,1)/2$. Two applications halve the input, as the paper records: <cite data-source="paper">H02 = I/2</cite>.

The butterfly is an elementary step of the [discrete Fourier transform](discrete-fourier-transform.md). A transform on $q$ entries, with $q$ a power of two, has $\log_2 q$ levels, one for each index bit of the position. At the level for bit $b$, it acts on pairs of entries whose positions differ only in that digit. The butterfly is combined with [signed shifts](cyclic-shift.md), which rotate a record's coefficient list and change the sign of entries that wrap around.

Cheap means a fixed amount of arithmetic per butterfly: two additions and a halving. One level on all $q$ entries therefore costs time linear in $q$, and the $\log_2 q$ levels cost $O(q\log q)$. The sources' concern is data movement, since scanning stored bits at every level <cite data-source="paper">already costs Θ(n log n)</cite>.

Records are polynomials with complex coefficients, and <cite data-source="paper">H0 acts coefficientwise</cite>: at each coefficient position, the two output coefficients are $H_0$ of the two input coefficients there.

The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies this step to several address bits at once.
