A Gaussian dyadic is a complex number whose real and imaginary parts are integers divided by a common power of two. It is the number type in which the integer multiplication algorithm does its transform arithmetic exactly, so that rounding is needed only once, at the end.

Here $a$ and $b$ are the integer real and imaginary parts of the numerator $a + bi$, a Gaussian integer (a complex number with integer real and imaginary parts). The exponent $k$ is a non-negative integer that sets the denominator $2^k$. A Gaussian dyadic has the form

$$\frac{a + bi}{2^k}.$$

Sums and products of Gaussian dyadics are again Gaussian dyadics, since a sum can be written over a common power of two. For example,

$$\frac{1+2i}{2} \cdot \frac{3-i}{4} = \frac{(1+2i)(3-i)}{8} = \frac{5+5i}{8},$$

which has numerator $5+5i$ and exponent $k = 3$.

A butterfly layer applies the two-point map $H_0$ to pairs of coefficients whose indices differ in one selected bit, sending $u$, $v$ to $\left(\frac{u+v}{2}, \frac{u-v}{2}\right)$. If $u$ and $v$ are Gaussian dyadics, so are both outputs, since halving only raises the exponent by one. <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>. So no layer introduces a rounding error, and an error is never carried into a later layer.
