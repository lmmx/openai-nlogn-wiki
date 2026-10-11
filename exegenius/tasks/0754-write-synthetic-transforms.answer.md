Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable $y$, so multiplying a value by a root only moves its coefficients and changes some signs. They are the transforms that the proof of [Integer multiplication below n log n](main-theorem.md) uses for its convolutions, and their cheap roots keep the cost of each transform to moves and additions.

## Records and signed shifts

Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials in the variable $y$ with complex coefficients, in which $y^r$ is identified with $-1$. This is a [polynomial ring modulo $y^r+1$](polynomial-ring-mod-yr-plus-1.md), a [ring](ring.md) in which sums and products of polynomials are again polynomials of this form. Here $r \ge 2$ is a power of two, and $r$ is the number of complex coefficients in a record.

A record is an element of $R_r$, stored as its $r$ coefficients $c_\varrho$, where $\varrho$, the coefficient position, runs from $0$ to $r-1$ and $c_\varrho$ multiplies $y^\varrho$.

Let $\xi$, with $0 \le \xi < 2r$, be the shift count, the number of places a shift moves each coefficient. For position $\varrho$, let $\mu_\varrho = \lfloor (\varrho+\xi)/r \rfloor$ be the wrap count: the number of times the shift carries the coefficient past position $r-1$, where $\lfloor x \rfloor$ is the largest integer not exceeding $x$. Since $\varrho+\xi = \mu_\varrho r + ((\varrho+\xi) \bmod r)$ and $y^r=-1$, we get $y^{\varrho+\xi} = (-1)^{\mu_\varrho} y^{(\varrho+\xi) \bmod r}$, so

$$y^\xi \sum_{\varrho=0}^{r-1} c_\varrho y^\varrho = \sum_{\varrho=0}^{r-1} (-1)^{\mu_\varrho}\, c_\varrho\, y^{(\varrho+\xi) \bmod r}.$$

Here $(\varrho+\xi) \bmod r$ is the remainder on division by $r$. Since $\varrho \le r-1$ and $\xi < 2r$, each $\mu_\varrho$ is $0$, $1$ or $2$. So multiplying by $y^\xi$ moves each coefficient $\xi$ places along the list, cyclically, and negates those that wrap past the end an odd number of times. No multiplication is needed. For example, take $r=4$ and $\xi=2$: $y^2(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3$, so $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$.

## Roots of unity

Let $N$ be a power of two dividing $2r$, the number of entries in a transform, and let $\upsilon$, running from $0$ to $N-1$, be the entry index that numbers the entries. Write $\omega_N = y^{2r/N}$ for the polynomial root of unity; it is the polynomial counterpart of the complex root $\omega$ of the Fourier transform, and a [root of unity](root-of-unity.md) of order $N$ in $R_r$.

Then $\omega_N^N = y^{2r} = (y^r)^2 = 1$. For $0<\upsilon<N$, write $\omega_N^\upsilon = y^a$ with $a = 2r\upsilon/N$, an integer with $0<a<2r$. If $a<r$, then $y^a$ is a monomial other than $1$, with constant coefficient $0$. If $a=r$, then $y^a=-1$. If $r<a<2r$, then $y^a=-y^{a-r}$ with $1 \le a-r < r$, again with constant coefficient $0$. In every case $\omega_N^\upsilon \ne 1$, so $\omega_N$ is primitive. Each power $\omega_N^\upsilon$ is a shift by $2r\upsilon/N < 2r$ places, so multiplying by it is a signed shift. For example, with $N=4$ and $r=2$, $\omega_4 = y$ and $\omega_4^2 = y^2 = -1$, so multiplying by $\omega_4^2$ negates both coefficients of a record.

## The transform

The input is $P=(P_0,\dots,P_{N-1})$, a list of $N$ records, and $P_\upsilon$ is its $\upsilon$-th entry. The output is $\hat P=(\hat P_0,\dots,\hat P_{N-1})$, the transformed list, where $\zeta$, the output index, runs from $0$ to $N-1$:

$$\hat P_\zeta = \frac{1}{N}\sum_{\upsilon=0}^{N-1} \omega_N^{\upsilon\zeta}\, P_\upsilon.$$

Synthetic polynomial transforms are based on the [Discrete Fourier transform](discrete-fourier-transform.md), with the root $\omega_N$ taken in $R_r$ in place of a complex number. The source says <cite data-source="paper">These are the synthetic polynomial transforms of Nussbaumer and Quandalle</cite>.

## Why the roots make the transform cheap

Every root in the transform is a power of $y$, so every multiplication by a root is a signed shift with no arithmetic. Roots that cost only shifts and signs therefore reduce each transform to address rearrangement and two-point butterflies: the rearrangement moves records, and the arithmetic is a butterfly whose only multiplication is a shift.

Synthetic polynomial transforms start from the order given by [Bit-reversed index order](bit-reversed-order.md): each record is first moved to its bit-reversed position, an address rearrangement with no arithmetic. The transform then runs in $\log_2 N$ levels. The levels run with half-block size $\vartheta$, the number of positions in each half of a block, taking the values $1,2,4,\dots,N/2$. A level groups the records into blocks of $2\vartheta$ consecutive positions. Each butterfly takes a pair of entries, $U$ at the lower position and $W$ at the upper position of the pair. For each block offset $\varpi$ from $0$ to $\vartheta-1$, the pair at positions $\varpi$ and $\varpi+\vartheta$ of the block is replaced by a sum and a difference, where $\theta = \omega_N^{\varpi N/(2\vartheta)}$ is the twiddle of that butterfly, the power of $\omega_N$ that multiplies $W$:

$$(U+\theta W,\ U-\theta W).$$

This replacement is a [two-point butterfly](butterfly.md): a sum and a difference of two entries, one of them first multiplied by the twiddle. Since $\varpi<\vartheta$, the exponent $\varpi N/(2\vartheta)$ is below $N$. Because $(2r/N)\cdot\varpi N/(2\vartheta) = r\varpi/\vartheta$, we have $\theta = y^{r\varpi/\vartheta}$, a signed shift by $r\varpi/\vartheta$ places. This number of places is an integer, since $\vartheta$ is a power of two at most $N/2$ and $N/2$ divides $r$ (because $N$ divides $2r$). So forming $\theta W$ is a shift with no multiplication. The butterfly costs one record addition and one record subtraction, each of $r$ coefficient additions. In a complex transform the same twiddle would be a genuine complex multiplication. The source states the cost as <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> <cite data-source="paper">shifts, and two-point butterfly operations</cite>.

Each level has $N/2$ butterflies and there are $\log_2 N$ levels, so the transform uses $O(Nr\log_2 N)$ coefficient additions and moves. Without the factor $1/N$, the levels produce $N\hat P_\zeta$, so the only multiplication is the single scaling by $1/N$ at the end.
