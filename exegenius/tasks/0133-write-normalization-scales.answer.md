Normalization scales are the known powers of two and transform lengths by which a computed product is multiplied at the end, so that the result is the exact integer convolution rather than a scaled copy of it. The integer multiplication argument uses them as its last arithmetic step before rounding and carry propagation: [Bluestein's chirp identity](bluestein-chirp-identity.md) turns the middle transform into a [normalized cyclic convolution](normalized-cyclic-convolution.md), and the scales then remove the factors that the transforms and the digit encoding introduced.

The normalized transform $F_q$ of length $q$ averages its inputs: <cite data-source="paper">each output averages inputs multiplied</cite> by complex numbers of modulus one. Its inverse $F_q^+$ is the transform with the opposite sign, and $I$ denotes the identity map. The source writes the transform length as the letter S; here it is $q$, as in the [discrete Fourier transform](discrete-fourier-transform.md). Two rules hold for inputs $u$ and $v$ of length $q$: <cite data-source="paper">The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S.</cite> Read with $q$ for the length, these say $F_q(u \ast v) = q\,(F_q u)\cdot(F_q v)$ and $F_q^+F_q = \frac{1}{q}I$.

Normalization scales undo the normalization of [normalized cyclic convolution](normalized-cyclic-convolution.md): the transforms compute the convolution divided by a power of $q$, and the scales multiply that power back in.

Applying the convolution rule to the transformed inputs and then the inverse gives
$$
F_q^+\big((F_q u)\cdot(F_q v)\big) = \frac{1}{q}\,F_q^+F_q(u \ast v) = \frac{1}{q^2}\,(u \ast v).
$$
So three normalized transforms leave the exact convolution divided by $q^2$. The two normalizations are different, which is why there are two multiplications. <cite data-source="paper">The two occurrences of S in this algorithm undo different normalizations.</cite> The first multiplication by $q$ gives $(u \ast v)/q$. The second multiplication by $q$ gives $u \ast v$.

Worked example: take $q = 4$ and suppose the transforms leave the coefficient $3/16$, whose exact value is $3/16 \cdot 16 = 3$. Multiplying by $q$ gives $3/4$, and multiplying by $q$ again gives $3$.

The digits carry a second scale. Write $\sigma = 2^{-b-2}$ for the digit scale: each radix-$2^b$ digit $a_j$ is stored as the number $\sigma a_j$. For a stored value $a/2^p$ with $a$ an integer, $a$ is its grid numerator. The stored digit has grid numerator $a_j 2^{p-b-2}$, and <cite data-source="paper">the represented value is exactly aj 2−b−2</cite>. A product of two such digit arrays therefore carries the factor $\sigma^2 = 2^{-2b-4}$, and <cite data-source="paper">reverses the two input scales.</cite> The factor $2^{2b+4}$ removes it.

Worked example: take $b = 2$, so $\sigma = 2^{-4}$. The digit $a = 3$ is stored as $3/16$, and the product of the digits $3$ and $2$ is stored as $6/256$. Multiplying by $2^{2b+4} = 256$ returns $6$.

Together, the algorithm multiplies by $q$ once, then by $2^{2b+4} q$, and the result is $2^{2b+4}(u \ast v)$, the integer coefficient convolution of the digit arrays. Both scales act on grid numerators with no rounding: <cite data-source="paper">multiplications act exactly on grid numerators.</cite> Because the scales introduce no rounding, the only error left is in the transforms, and it is bounded separately: the same section <cite data-source="paper">normalizations and digit scales, proves that the recovered coefficient error is strictly below 1/2,</cite> so rounding to the nearest integer recovers each coefficient.
