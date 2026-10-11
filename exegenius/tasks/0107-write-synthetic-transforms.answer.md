Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable, so that multiplying a value by a root only moves coefficients and changes some signs. They compute the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md). The result is <cite data-source="paper">a deterministic algorithm that multiplies two n-bit integers in</cite> $O(n(\lg n)^{1-\kappa})$ time for a fixed constant $\kappa$.

## Records and roots

Let $r \ge 2$ be a power of two, where $r$ is the number of complex coefficients in a record. Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials in the variable $y$ with complex coefficients, in which $y^r$ is identified with $-1$. A record is an element of $R_r$, stored as its $r$ coefficients $c_m$, one for each power $y^m$, with position $m$ running from $0$ to $r-1$.

Since $y^r = -1$, a power of $y$ that runs past position $r-1$ wraps around with a sign change. Let $s$, with $0 \le s < 2r$, be the number of places a shift moves each coefficient. Then

$$y^s \sum_{m=0}^{r-1} c_m y^m = \sum_{m=0}^{r-1} (-1)^{\lfloor (m+s)/r \rfloor}\, c_m\, y^{(m+s) \bmod r}.$$

Here $\lfloor x \rfloor$ is the largest integer not exceeding $x$, and $p \bmod r$ is the remainder of the integer $p$ on division by $r$, a position in $\{0,\dots,r-1\}$. Since $m \le r-1$ and $s < 2r$, the quotient $\lfloor (m+s)/r \rfloor$ is $0$, $1$ or $2$: it counts how many times the shift carries that coefficient past position $r-1$. The identity follows from $y^{m+s} = (y^r)^q y^p = (-1)^q y^p$, where $m+s = qr+p$ with $q = \lfloor (m+s)/r \rfloor$ and $p = (m+s) \bmod r$.

So multiplying by $y^s$ moves every coefficient $s$ places along the coefficient list, cyclically, and negates the coefficients that wrap past the end an odd number of times. This signed shift is exact: it uses no rounding and no multiplication.

Let $t$ be a power of two dividing $2r$, the number of entries in the transform. The root $\omega_t = y^{2r/t}$ is a primitive $t$-th root of unity in $R_r$: its $t$-th power is $1$, and no smaller positive power is $1$. Indeed $\omega_t^t = y^{2r} = 1$ and $\omega_t^{t/2} = y^r = -1$. Each power $\omega_t^j$ with $0 \le j < t$ is $y^{2rj/t}$, a power of $y$ with shift $2rj/t < 2r$, so multiplying by it is a signed shift.

## The transform

The input is $h = (h_0,\dots,h_{t-1})$, a list of $t$ records in $R_r$, and the output is the list $Z = (Z_0,\dots,Z_{t-1})$, whose $k$-th entry is $Z_k$. With $j$ and $k$ as on the Discrete Fourier transform page,

$$Z_k = \frac{1}{t}\sum_{j=0}^{t-1} \omega_t^{jk}\, h_j.$$

A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. <cite data-source="paper">The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method</cite> of Nussbaumer and Quandalle.

## Why the roots make the transform cheap

The fast method computes $Z$ in $\log_2 t$ levels, where $\log_2 t$ is the base-2 logarithm of $t$. At each level, each pair of entries $(u,v)$ is replaced by $(u+\omega v,\ u-\omega v)$, where $\omega$ is a power of $\omega_t$. This operation is a two-point butterfly. In a complex transform, forming $\omega v$ is a genuine multiplication. Here $\omega$ is a power of $y$, so $\omega v$ is a signed shift of the coefficients of $v$, and the butterfly costs only one addition and one subtraction of records. The source states the cost as: <cite data-source="paper">the transform calculation consists of address rearrangements, signed</cite> shifts, and two-point butterfly operations.

For example, take $r = 4$ and $t = 4$. Then $\omega_4 = y^{2}$, the root $\omega_t$ with $t = 4$, since $2r/t = 2$, and $\omega_4^2 = y^4 = -1$. Multiplying by $\omega_4$ gives

$$\omega_4\,(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3,$$

so the coefficient list $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$. Here $s = 2$, and $c_2$ and $c_3$ wrap once and are negated. That is two moves and two negations.
