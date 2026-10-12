A Gaussian dyadic is a complex number whose real and imaginary parts are integers divided by a common power of two. It is the number type in which the integer multiplication algorithm does its transform arithmetic exactly, so that rounding is needed only once, at the end.

Here $a$ and $b$ are the integer real and imaginary parts of the numerator $a + bi$, which is therefore a Gaussian integer. The exponent $k$ is a non-negative integer that sets the denominator $2^k$. A Gaussian dyadic has the form

$$\frac{a + bi}{2^k}.$$

Sums and products of Gaussian dyadics are again Gaussian dyadics, since a product of powers of two is again a power of two. For example,

$$\frac{1+2i}{2} \cdot \frac{3-i}{4} = \frac{(1+2i)(3-i)}{8} = \frac{5+5i}{8},$$

which has numerator $5+5i$ and exponent $k = 3$.

The butterfly layers keep every value in this form, so a layer introduces no rounding error. <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>. Exactness matters because a rounding error made in one layer would otherwise be carried into every later layer.
