Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable $y$, so multiplying a value by a root only moves its coefficients and changes some signs. They are the normalized Fourier transforms that the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md) need, and the sign-and-shift roots make those transforms cost only moves and additions. The source's main result is <cite data-source="paper">a deterministic algorithm that multiplies two n-bit integers in</cite> $O(n(\lg n)^{1-\kappa})$ time, where $\kappa$ is a fixed positive constant.

## Records and signed shifts

Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials in the variable $y$ with complex coefficients, in which $y^r$ is identified with $-1$. Here $r \ge 2$ is a power of two, and $r$ is the number of complex coefficients in a record. This is the [polynomial ring modulo $y^r+1$](polynomial-ring-mod-yr-plus-1.md). A record is an element of $R_r$, stored as its $r$ coefficients $c_\rho$, one for each power $y^\rho$, where the position $\rho$ runs from $0$ to $r-1$.

Let $\sigma$, with $0 \le \sigma < 2r$, be the number of places a shift moves each coefficient. For a coefficient at position $\rho$, let $\mu_\rho = \lfloor (\rho+\sigma)/r \rfloor$ be the number of times the shift carries it past position $r-1$, where $\lfloor x \rfloor$ is the largest integer not exceeding $x$. Since $\rho+\sigma = \mu_\rho r + ((\rho+\sigma) \bmod r)$, we get $y^{\rho+\sigma} = (y^r)^{\mu_\rho} y^{(\rho+\sigma) \bmod r} = (-1)^{\mu_\rho} y^{(\rho+\sigma) \bmod r}$, and so

$$y^\sigma \sum_{\rho=0}^{r-1} c_\rho y^\rho = \sum_{\rho=0}^{r-1} (-1)^{\mu_\rho}\, c_\rho\, y^{(\rho+\sigma) \bmod r}.$$

Here $(\rho+\sigma) \bmod r$ is the remainder of $\rho+\sigma$ on division by $r$, a position in $\{0,\dots,r-1\}$. Since $\rho \le r-1$ and $\sigma < 2r$, each $\mu_\rho$ is $0$, $1$ or $2$. So multiplying by $y^\sigma$ moves each coefficient $\sigma$ places along the list, cyclically, and negates those that wrap past the end an odd number of times. No rounding or multiplication is needed.

For example, take $r = 4$ and $\sigma = 2$. Then $y^2(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3$, so $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$.

## Roots of unity

Let $N$ be a power of two dividing $2r$, the number of entries in the transform. The letter $j$ changes meaning here: it is an index running from $0$ to $N-1$ that numbers the entries, not the coordinate index of earlier pages. The root $\omega_N = y^{2r/N}$ is a primitive $N$-th root of unity in $R_r$, meaning $\omega_N^N = 1$ and $\omega_N^j \ne 1$ for $0<j<N$. The subscript keeps this polynomial root apart from the complex root $\omega$ of the Discrete Fourier transform page. First, $\omega_N^N = y^{2r} = (y^r)^2 = 1$. For $0<j<N$, write $\omega_N^j = y^a$ with $a = 2rj/N$, an integer with $0<a<2r$. If $a<r$, then $y^a$ is a basis element other than $1$, so its constant coefficient is $0$. If $a=r$, then $\omega_N^j=-1 \ne 1$. If $r<a<2r$, then $y^a=-y^{a-r}$, where $1 \le a-r < r$, so again its constant coefficient is $0$. In every case $\omega_N^j \ne 1$. Each power $\omega_N^j$ with $0 \le j < N$ is thus a shift by $2rj/N < 2r$ places, so multiplying by it is a signed shift. For example, with $N=4$ and $r=2$, $\omega_4 = y$ and $\omega_4^2 = y^2 = -1$, so multiplying by $\omega_4^2$ negates both coefficients of a record.

## The transform

The input is $f = (f_0,\dots,f_{N-1})$, a list of $N$ records, and $f_j$ is its $j$-th entry. The output is $Z = (Z_0,\dots,Z_{N-1})$, the transformed list. The letter $\ell$ is the output index, from $0$ to $N-1$.

$$Z_\ell = \frac{1}{N}\sum_{j=0}^{N-1} \omega_N^{j\ell}\, f_j.$$

A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. The source says <cite data-source="paper">These are the synthetic polynomial transforms of Nussbaumer and Quandalle</cite>, and attributes the method: <cite data-source="paper">The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method</cite> of Nussbaumer and Quandalle.

## Why the roots make the transform cheap

Every root in the transform is a power of $y$, so every multiplication by a root is a signed shift with no arithmetic. The fast method computes $Z$ in $\log_2 N$ levels, where $\log_2 N$ is the base-2 logarithm of $N$. The transform first orders the records by [bit-reversed index order](bit-reversed-order.md), an address rearrangement that moves stored records without arithmetic. A level has half-size $\eta$, the number of positions in each half of a block, taking the values $1, 2, 4, \dots, N/2$, and groups the records into blocks of $2\eta$ consecutive positions. In each block, each offset $\gamma$ from $0$ to $\eta-1$ gives a pair of entries $U$ and $W$ at positions $\gamma$ and $\gamma+\eta$ of the block. Let $\theta = \omega_N^{\gamma N/(2\eta)}$ be the twiddle of that butterfly, a power of $\omega_N$. The pair is replaced by

$$(U+\theta W,\ U-\theta W).$$

This replacement is a [two-point butterfly](butterfly.md): it forms the sum and the difference of two entries, after one of them is multiplied by a twiddle. Since $\gamma<\eta$, the exponent $\gamma N/(2\eta)$ is below $N$, so $\theta = y^{r\gamma/\eta}$, because $(2r/N)\cdot\gamma N/(2\eta) = r\gamma/\eta$. Thus $\theta$ is a signed shift by $r\gamma/\eta$ places. This number is an integer because $\eta$ is a power of two at most $N/2$, and $N/2$ divides $r$ since $N$ divides $2r$. Forming $\theta W$ is therefore a signed shift with no multiplication. The butterfly costs one record addition and one record subtraction, each of $r$ coefficient additions. In a complex transform the same twiddle would be a genuine complex multiplication. The source states the cost as <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> <cite data-source="paper">shifts, and two-point butterfly operations</cite>.

Each level has $N/2$ butterflies, and there are $\log_2 N$ levels. The transform therefore uses $O(Nr\log_2 N)$ coefficient additions and moves and no coefficient multiplication. After the level with $\eta = N/2$, the records hold the unnormalized sums, which are $N$ times $Z_\ell$, so the factor $1/N$ is applied last.
