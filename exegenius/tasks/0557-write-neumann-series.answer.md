The Neumann series is the infinite sum of the powers of a linear operator, with alternating signs. For a small operator it equals the inverse of the identity plus that operator, which is how the paper shows that its operator is invertible and applies the inverse with a fixed number of steps.

## Definition

The Neumann series is defined over the linear operators of [Linear algebra basics](linear-algebra-basics.md). Let $J$ be a linear operator on a finite-dimensional complex vector space, and let $I$ be the identity operator on that space. The index $\xi$ numbers the terms of the series, and $\xi$ ranges over the nonnegative integers. The series is

$$\sum_{\xi\ge 0}(-1)^\xi J^\xi,$$

where $J^\xi$ is the composition of $J$ with itself $\xi$ times, with $J^0=I$.

Convergence is measured by the [array norm](array-norm.md), and $\|\cdot\|$ denotes the operator norm induced by it. The array norm of a vector is the largest modulus of its coordinates, and the operator norm of $J$ is $\|J\| = \sup_{\|\upsilon\|\le 1}\|J\upsilon\|$. Operator norms are submultiplicative, so $\|J^\xi\|\le\|J\|^\xi$.

The series converges when $\|J\|<1$, because its $\xi$-th term has norm at most $\|J\|^\xi$, a geometric bound. The question is whether its value is the inverse of $I+J$.

## Partial sums and the telescoping identity

For a number $\Xi\ge 1$ of terms, write $\sum_{\xi=0}^{\Xi-1}(-J)^\xi$ for the partial sum of the first $\Xi$ terms. Multiplying the partial sum by $I+J$ makes all but two terms cancel, because $J(-J)^\xi=-(-J)^{\xi+1}$:

$$(I+J)\sum_{\xi=0}^{\Xi-1}(-J)^\xi=\sum_{\xi=0}^{\Xi-1}(-J)^\xi-\sum_{\xi=1}^{\Xi}(-J)^\xi=I-(-J)^\Xi.$$

If $\|J\|<1$, then $\|(-J)^\Xi\|\le\|J\|^\Xi$ tends to zero as $\Xi$ grows. So the partial sums converge to an operator $W$ with $(I+J)W=I$. In finite dimensions a one-sided inverse is two-sided, so $W=(I+J)^{-1}$. The series therefore equals the inverse of $I+J$.

The same identity gives the error after $\Xi$ terms. Since $(I+J)^{-1}\big(I-(I+J)\Psi\big)=(I+J)^{-1}(-J)^\Xi$ for any partial sum $\Psi$ with $\Xi$ terms,

$$\Big\|(I+J)^{-1}-\sum_{\xi=0}^{\Xi-1}(-J)^\xi\Big\|\le\|(I+J)^{-1}\|\,\|J\|^\Xi.$$

Worked example. Take $J=\tfrac12$ acting on $\mathbb{C}$, where $\|J\|=\tfrac12$. The inverse of $1+\tfrac12$ is $\tfrac23$. The four-term partial sum is $1-\tfrac12+\tfrac14-\tfrac18=\tfrac58$, and $(1+\tfrac12)\cdot\tfrac58=\tfrac{15}{16}=1-(-\tfrac12)^4$, as the identity predicts. The error $\tfrac23-\tfrac58=\tfrac1{24}$ equals the bound $\tfrac23\cdot(\tfrac12)^4$.

## The paper's use

Here the letter $N$ denotes the paper's operator, which changes its meaning from the earlier pages. The paper takes $J=N-I$, so that $I+J=N$. Its proof of invertibility is a norm bound followed by this series: <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite> The bound below one gives convergence, and the identity above shows that the limit inverts $N$.

Here $\alpha$ and $\theta$ are parameters of the paper's construction, and the letter $\alpha$ changes meaning here. The paper's exponent is $\sigma=\alpha^2\theta$. The paper bounds the norm of $J$ by a power of two, <cite data-source="paper">∥N − I∥ < 2.01e−πα θ/2 < 2−α θ</cite>. Its parameters satisfy <cite data-source="paper">α2 θ > p/α2 > 1</cite>. So $\|J\|<2^{-\sigma}$, with $\sigma>1$.

The paper uses $\Xi=\lceil p/\sigma\rceil$ terms. It writes this number as $k$, but $k$ is the padded length on earlier pages, so this page uses $\Xi$. Since $\Xi\sigma\ge p$,

$$\|J^\Xi\|\le\|J\|^\Xi<2^{-\sigma\Xi}\le 2^{-p},$$

and the error bound above gives $\|N^{-1}-\sum_{\xi<\Xi}(-J)^\xi\|\le\|N^{-1}\|\,2^{-p}$. The truncated series therefore approximates the inverse to within a fixed multiple of $2^{-p}$, where $p$ is the precision of the records.

The paper applies the truncated series to rounded records. Each application of $J$ multiplies the size of an iterate by at most $\|J\|$, which is less than one, so the iterates shrink. Rounding each iterate to precision $p$ keeps the records bounded: <cite data-source="paper">keeps every iterate in Dsp</cite>.
