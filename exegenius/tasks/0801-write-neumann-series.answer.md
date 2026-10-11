The Neumann series is the infinite sum of the powers of a linear operator, with alternating signs. The paper uses it to show that its own operator is invertible, and to apply the inverse with a fixed number of terms.

## Definition

The Neumann series is defined over the linear operators of [Linear algebra basics](linear-algebra-basics.md). Let $J$ be a linear operator on a finite-dimensional complex vector space, and let $I$ be the identity operator on that space. The index $\xi$ numbers the terms of the series, and $\xi$ ranges over the nonnegative integers. The series is

$$\sum_{\xi\ge 0}(-1)^\xi J^\xi,$$

where $J^\xi$ is the composition of $J$ with itself $\xi$ times, with $J^0=I$.

Convergence is measured by the [array norm](array-norm.md), and $\|\cdot\|$ denotes the operator norm induced by it. For a vector, the array norm is the largest modulus of its coordinates. The operator norm of $J$ is $\|J\|=\sup_{\|\upsilon\|\le 1}\|J\upsilon\|$, where $\upsilon$ ranges over the vectors of the space. Operator norms are submultiplicative, meaning $\|AB\|\le\|A\|\,\|B\|$, so $\|J^\xi\|\le\|J\|^\xi$.

The series converges when $\|J\|<1$, because its $\xi$-th term has norm at most $\|J\|^\xi$, a geometric bound. The question is whether its value is the inverse of $I+J$.

## Partial sums and the telescoping identity

For a number $\Xi\ge 1$ of terms, write $\sum_{\xi=0}^{\Xi-1}(-J)^\xi$ for the partial sum of the first $\Xi$ terms. Multiplying it by $I+J$ leaves only two terms, because $J(-J)^\xi=-(-J)^{\xi+1}$ makes each term cancel its neighbour:

$$(I+J)\sum_{\xi=0}^{\Xi-1}(-J)^\xi=\sum_{\xi=0}^{\Xi-1}(-J)^\xi-\sum_{\xi=1}^{\Xi}(-J)^\xi=I-(-J)^\Xi.$$

If $\|J\|<1$, then $\|(-J)^\Xi\|\le\|J\|^\Xi$ tends to zero as $\Xi$ grows. So the partial sums converge to an operator $W$ with $(I+J)W=I$. In finite dimensions a right inverse is also a left inverse, so $W=(I+J)^{-1}$, and the series equals the inverse of $I+J$.

The same identity gives the error after $\Xi$ terms. Multiplying it on the left by $(I+J)^{-1}$ gives $(I+J)^{-1}-\sum_{\xi=0}^{\Xi-1}(-J)^\xi=(I+J)^{-1}(-J)^\Xi$, so

$$\Big\|(I+J)^{-1}-\sum_{\xi=0}^{\Xi-1}(-J)^\xi\Big\|\le\|(I+J)^{-1}\|\,\|J\|^\Xi.$$

Worked example. Take $J=\tfrac12$ acting on $\mathbb{C}$, where $\|J\|=\tfrac12$. The inverse of $1+\tfrac12$ is $\tfrac23$. The four-term partial sum is $1-\tfrac12+\tfrac14-\tfrac18=\tfrac58$, and $(1+\tfrac12)\cdot\tfrac58=\tfrac{15}{16}=1-(-\tfrac12)^4$, as the identity predicts. The error $\tfrac23-\tfrac58=\tfrac1{24}$ equals the bound $\tfrac23\cdot(\tfrac12)^4$.

## The paper's use

The paper's operator is $N$, not the entry count $N$ of [Address](address.md). It sets $J=N-I$, so that $I+J=N$. Its proof of invertibility is a norm bound followed by this series: <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite>

Here $\alpha$ and $\theta$ are parameters of the paper's construction, not the address string $\alpha$ of [Address](address.md). The paper bounds the norm of $J$ by a power of two: <cite data-source="paper">∥N − I∥ < 2.01e−πα θ/2 < 2−α θ</cite>. Its parameters satisfy <cite data-source="paper">α2 θ > p/α2 > 1</cite>. Writing $\sigma=\alpha^2\theta$ for the exponent, we get $\|J\|<2^{-\sigma}$ with $\sigma>1$. So $\|J\|<\tfrac12$, and summing $\|J\|^\xi$ over $\xi$ gives $\|N^{-1}\|\le 1/(1-\|J\|)<2$.

The paper uses $\Xi=\lceil p/\sigma\rceil$ terms. It writes this number as <cite data-source="paper">k = ⌈p/(α2 θ)⌉</cite>, but $k$ is the padded length on earlier pages, so this page uses $\Xi$. Since $\Xi\sigma\ge p$,

$$\|J^\Xi\|\le\|J\|^\Xi<2^{-\sigma\Xi}\le 2^{-p},$$

and the error bound gives $\|N^{-1}-\sum_{\xi<\Xi}(-J)^\xi\|\le\|N^{-1}\|\,2^{-p}<2\cdot 2^{-p}$. The truncated series therefore approximates the inverse to within twice $2^{-p}$, where $p$ is the precision of the records.

The paper applies the truncated series to rounded records. Each iterate is obtained by applying the operator to the previous rounded iterate, and the bound below one makes the iterates shrink. Rounding each iterate to precision $p$ keeps them bounded: <cite data-source="paper">keeps every iterate in Dsp</cite>.
