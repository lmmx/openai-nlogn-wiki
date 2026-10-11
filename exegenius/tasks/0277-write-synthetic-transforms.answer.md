Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable, so that multiplying a value by a root only moves coefficients and changes some signs. They compute the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md). Here $\lg$ is the base-2 logarithm and $\kappa$ is a fixed positive constant. The source's main result is <cite data-source="paper">a deterministic algorithm that multiplies two n-bit integers in</cite> $O(n(\lg n)^{1-\kappa})$ time.

## Records and signed shifts

Let $r \ge 2$ be a power of two, where $r$ is the number of complex coefficients in a record. Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials in the variable $y$ with complex coefficients, in which $y^r$ is identified with $-1$. A record is an element of $R_r$, stored as its $r$ coefficients $c_d$, one for each power $y^d$, where the position $d$ runs from $0$ to $r-1$.

Let $s$, with $0 \le s < 2r$, be the number of places a shift moves each coefficient. For a coefficient at position $d$, let $\nu_d = \lfloor (d+s)/r \rfloor$ be the number of times the shift carries it past position $r-1$, where $\lfloor x \rfloor$ is the largest integer not exceeding $x$. Since $d+s = \nu_d r + ((d+s) \bmod r)$, we get $y^{d+s} = (y^r)^{\nu_d} y^{(d+s) \bmod r} = (-1)^{\nu_d} y^{(d+s) \bmod r}$, and so

$$y^s \sum_{d=0}^{r-1} c_d y^d = \sum_{d=0}^{r-1} (-1)^{\nu_d}\, c_d\, y^{(d+s) \bmod r}.$$

Here $(d+s) \bmod r$ is the remainder of $d+s$ on division by $r$, a position in $\{0,\dots,r-1\}$. Since $d \le r-1$ and $s < 2r$, each $\nu_d$ is $0$, $1$ or $2$. So multiplying by $y^s$ moves each coefficient $s$ places along the list, cyclically, and negates those that wrap past the end an odd number of times. No rounding or multiplication is needed.

For example, take $r = 4$ and $s = 2$. Then $y^2(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3$, so $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$.

## Roots of unity

Let $N$ be a power of two dividing $2r$, the number of entries in the transform. The root $\omega_N = y^{2r/N}$ is a primitive $N$-th root of unity in $R_r$, meaning $\omega_N^N = 1$ and $\omega_N^j \ne 1$ for $0<j<N$. First, $\omega_N^N = (y^r)^2 = 1$. For $0<j<N$, write $\omega_N^j = y^a$ with $a = 2rj/N$, an integer with $0<a<2r$. The monomials $1, y, \dots, y^{r-1}$ are a basis of $R_r$. If $a<r$, then $y^a$ is a basis element other than $1$. If $a=r$, then $\omega_N^j=-1 \ne 1$. If $r<a<2r$, then $y^a=-y^{a-r}$ has coefficient $-1$ on a basis element other than $1$, which has coefficient $0$ there. In every case $\omega_N^j \ne 1$. Each power $\omega_N^j$ with $0 \le j < N$ is thus a shift by $2rj/N < 2r$ places, so multiplying by it is a signed shift.

## The transform

The input is $e = (e_0,\dots,e_{N-1})$, a list of $N$ records, and $e_j$ is its $j$-th entry. The output is $Z = (Z_0,\dots,Z_{N-1})$, the transformed list. With $j$ the input index and $\ell$ the output index, as on the Discrete Fourier transform page,

$$Z_\ell = \frac{1}{N}\sum_{j=0}^{N-1} \omega_N^{j\ell}\, e_j.$$

A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. The source attributes the method: <cite data-source="paper">The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method</cite> of Nussbaumer and Quandalle.

## Why the roots make the transform cheap

The fast method computes $Z$ in $\log_2 N$ levels, where $\log_2 N$ is the base-2 logarithm of $N$. First the records are placed in bit-reversed index order, an address rearrangement. A level has a half-size $\delta$, taking the values $1, 2, \dots, N/2$, and groups the records into blocks of $2\delta$ consecutive positions. In each block, each offset $\tau$ from $0$ to $\delta-1$ gives a pair of entries $U$ and $W$ at positions $\tau$ and $\tau+\delta$. Let $\theta = \omega_N^{\tau N/(2\delta)}$ be the twiddle of that butterfly, a power of $\omega_N$. The pair is replaced by

$$(U+\theta W,\ U-\theta W).$$

This replacement is a two-point butterfly. After the level with $\delta = N/2$, the records hold $Z$ in natural order, up to the scalar $1/N$.

The exponent of $\theta$ is below $N$, so $\theta$ is a signed shift by $2r\cdot\tau N/(2\delta)/N = r\tau/\delta$ places, an integer since $\delta$ divides $r$. Forming $\theta W$ is therefore a signed shift with no multiplication. The butterfly costs one record addition and one record subtraction, each of $r$ coefficient additions. In a complex transform the same twiddle would be a genuine complex multiplication. The source states the cost as <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> shifts and <cite data-source="paper">two-point butterfly operations</cite>. Each level has $N/2$ butterflies, so the transform uses $O(Nr\log_2 N)$ coefficient operations and no coefficient multiplication.
