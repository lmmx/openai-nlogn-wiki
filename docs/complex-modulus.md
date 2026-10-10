# Complex modulus (norm of a coefficient)

The modulus, or absolute value, of a complex number $z = x + iy$ with real $x$ and imaginary $y$ is $|z| = \sqrt{x^2 + y^2}$. It is the distance from $0$ to $z$ in the complex plane, which is the length of $z$ viewed as a vector in $\mathbb{R}^2$. Its square is $|z|^2 = z\bar z$, where $\bar z = x - iy$ is the complex conjugate.

For example, $|3 + 4i| = \sqrt{9 + 16} = 5$, and $|i| = 1$. Multiplying by a number of modulus one, such as $i$ or $e^{\pi i / 4}$, rotates a complex number without changing its modulus.

The paper uses this modulus, which it calls the norm of a coefficient, to bound the size of each complex coefficient. A coefficient of norm less than $\tfrac14$ is a complex number lying within distance $\tfrac14$ of $0$. Bounding the norm of each coefficient is the way the paper keeps the approximations within a fixed range.

The modulus is also the pointwise version of the [sup norm](sup-norm.md): the sup norm of a coefficient array is the largest modulus among its entries. The representation of such values as [disk-grid values](disk-grid-values.md) uses this bound.

## Prerequisites

- Complex numbers (assumed known)

## Used by

- [Disk-grid values](disk-grid-values.md)

## Sources

> Their coefficients are exact p-bit grid values of norm less than 1/4.
>
> — Integer multiplication below n log n (OpenAI, 2026)
