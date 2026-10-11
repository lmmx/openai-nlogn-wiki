Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable, so that multiplying a value by a root only moves coefficients and changes some signs. They are the transforms that compute the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md). The result is <cite data-source="paper">a deterministic algorithm that multiplies two n-bit integers in</cite> $O(n(\lg n)^{1-\kappa})$ time for a fixed constant $\kappa$, where $n$ is the bit length of the integers.

## Records and roots

Let $r \ge 2$ be a power of two, where $r$ is the number of complex coefficients in a record. Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$, where $y$ is the polynomial variable. A record is an element of $R_r$, stored as its $r$ coefficients.

Since $y^r = -1$, a power of $y$ that runs past position $r-1$ wraps around with a sign change. The rule below uses three symbols. In it, $c_i$ is the coefficient of $y^i$ in the record, $i$ is its position, and $a$ is the number of places the shift moves each coefficient, with $0 \le a < 2r$:

$$y^a \sum_{i=0}^{r-1} c_i y^i = \sum_{i=0}^{r-1} (-1)^{\lfloor (i+a)/r \rfloor}\, c_i\, y^{(i+a) \bmod r}.$$

So multiplying by $y^a$ moves every coefficient $a$ places along the coefficient list, cyclically, and negates each coefficient that wraps past the end. This is a signed shift of the coefficient list, and it is exact: it involves no rounding and no multiplication.

Let $t$ be a power of two dividing $2r$, the number of entries in the transform. The root $\omega_t = y^{2r/t}$ is a primitive $t$-th root of unity in $R_r$. Indeed, $\omega_t^t = y^{2r} = 1$, and $\omega_t^{t/2} = y^r = -1$. Every power of $\omega_t$ is a power of $y$, so multiplying by any power of $\omega_t$ is a signed shift.

## The transform

<cite data-source="paper">We now implement the normalized Fourier transforms needed for convolution.</cite> The input $z=(z_0,\dots,z_{t-1})$ is a list of $t$ records in $R_r$.

Here $j$ and $k$ are indices running from $0$ to $t-1$, and $Z_j$ is the $j$-th entry of the transform $Z=(Z_0,\dots,Z_{t-1})$ of $z$, given by

$$Z_j = \frac{1}{t}\sum_{k=0}^{t-1} \omega_t^{jk}\, z_k.$$

A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. <cite data-source="paper">The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method</cite> of Nussbaumer and Quandalle.

## Why the roots make the transform cheap

A radix-two transform of length $t$ has $\log_2 t$ levels. Each level pairs up entries and applies a two-point butterfly: one entry of the pair is multiplied by a power of $\omega_t$, and the pair is replaced by its sum and its difference. Because a power of $\omega_t$ is a signed shift, the multiplication inside each butterfly is only a rearrangement of coefficients with sign changes, and the butterfly costs one addition and one subtraction of records. Between levels, the entries are moved to new addresses, which is also a rearrangement. In the source's words, <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> shifts, and two-point butterfly operations.

For example, take $r = 4$ and $t = 4$. Then $\omega_4 = y^2$, and $\omega_4^2 = y^4 = -1$. Multiplying a record by $\omega_4$ gives

$$\omega_4\,(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3,$$

so the coefficient list $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$. This is two moves and two negations, with no multiplication.
