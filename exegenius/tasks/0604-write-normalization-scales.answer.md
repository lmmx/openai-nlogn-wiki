Normalization scales are the known powers of two and transform lengths by which a computed product is multiplied at the end, so that the output is the exact integer convolution of the digit arrays rather than a scaled copy of it. They are the last arithmetic step before rounding in the paper's [integer multiplication algorithm](main-theorem.md).

The normalized transform $F_q$ of length $q$ sends a vector $f=(f_0,\dots,f_{q-1})$ to
$$(F_q f)_\ell=\frac1q\sum_{s=0}^{q-1} f_s\,e^{-2\pi i s\ell/q},\qquad 0\le \ell<q,$$
where $s$ and $\ell$ are the input and output indices. $F_q^+$ is the same sum with $e^{+2\pi i s\ell/q}$ in place of $e^{-2\pi i s\ell/q}$. Each output is an average of $q$ terms, each an input times a complex number of modulus one, so the transform never increases the largest modulus of its input: <cite data-source="paper">normalized Fourier transform above is a contraction</cite>.

For vectors $f$ and $g$ of length $q$, let $f\ast g$ be their cyclic convolution, $(f\ast g)_\ell=\sum_{s+\nu\equiv \ell \pmod q} f_s g_\nu$, where $\nu$ is a second input index from $0$ to $q-1$, and let $f\cdot g$ be their entrywise product. Two rules hold:
$$F_q(f\ast g)=q\,(F_qf)\cdot(F_qg),\qquad F_q^+F_q=\tfrac1q\,I,$$
where $I$ is the identity. The paper states them as <cite data-source="paper">The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S.</cite> with $S$ read as $q$.

Both follow by expanding the sums. The exponential $e^{-2\pi i(s+\nu)\ell/q}$ depends on $s+\nu$ only modulo $q$, and the convolution adds each product $f_s g_\nu$ into the entry $s+\nu$ modulo $q$, so $F_q(f\ast g)_\ell=\frac1q\sum_{s,\nu}f_s g_\nu\, e^{-2\pi i(s+\nu)\ell/q}$. This double sum factors into $\frac1q\bigl(q(F_qf)_\ell\bigr)\bigl(q(F_qg)_\ell\bigr)$, which is the first rule. For the second, $(F_q^+F_qf)_\ell=\frac1{q^2}\sum_s f_s\sum_\nu e^{2\pi i\nu(\ell-s)/q}$. For $s,\ell\in\{0,\dots,q-1\}$ the inner sum over $\nu$ is $q$ when $s=\ell$ and $0$ otherwise, because it is a geometric sum whose ratio $e^{2\pi i(\ell-s)/q}$ is a $q$th root of unity different from $1$ when $s\ne\ell$. Hence $(F_q^+F_qf)_\ell=f_\ell/q$.

Applying the first rule to the transformed inputs, then the second, gives
$$F_q^+\big((F_qf)\cdot(F_qg)\big)=\frac1q\,F_q^+F_q(f\ast g)=\frac1{q^2}\,(f\ast g).$$
These are the algorithm's three transforms: the forward transforms $F_qf$ and $F_qg$, and the transform $F_q^+$ applied to their pointwise product.

Normalization scales undo the normalization of [Normalized cyclic convolution](normalized-cyclic-convolution.md). With $f\circledast g=(f\ast g)/q$, the three transforms leave $\frac1q(f\circledast g)$. Multiplying by $q$ gives $f\circledast g$, and multiplying by $q$ again gives $f\ast g$. <cite data-source="paper">The two occurrences of S in this algorithm undo different normalizations.</cite>

Worked example: take $q=4$ and suppose the three transforms leave $3/16=(f\ast g)_\ell/q^2$ for an entry with $(f\ast g)_\ell=3$. Multiplying by $4$ gives $3/4$, and by $4$ again gives $3$.

The digits carry a second scale. Let $\hat f$ and $\hat g$ be the integer digit arrays of the two inputs, with entries from $0$ to $2^b-1$, where $b$ is the digit width. The algorithm stores each entry as $\sigma$ times its digit, with the digit scale $\sigma=2^{-b-2}$, so the stored arrays are $f=\sigma\hat f$ and $g=\sigma\hat g$. Each stored value then has modulus below $\sigma 2^b=\frac14$. Here $p$ is the precision, with grid spacing $2^{-p}$, and <cite data-source="paper">Their coefficients are exact p-bit grid values of norm less than 1/4.</cite>

Since $f\ast g=\sigma^2(\hat f\ast\hat g)$, the product carries $\sigma^2=2^{-2b-4}$, and the algorithm multiplies by $2^{2b+4}$ to remove it. <cite data-source="paper">reverses the two input scales</cite>.

Worked example: take $b=2$, so $\sigma=2^{-4}$. The digits $3$ and $2$ are stored as $3/16$ and $2/16$, and their product $6/256$ times $2^{2b+4}=256$ returns $6$.

Each input has $m$ digits, so each digit array has $m$ entries (here $m$ counts digits). The ordinary product of two such digit polynomials has degree at most $2m-2$. Padding both arrays with zeros to length $q>2m-2$ means no product index reaches $q$, so the cyclic convolution equals the ordinary one. <cite data-source="paper">has no nonzero wraparound</cite>

Altogether the algorithm multiplies by $q$, then by $2^{2b+4}q$, which turns $\sigma^2(\hat f\ast\hat g)/q^2$ into $2^{2b+4}\sigma^2(\hat f\ast\hat g)=\hat f\ast\hat g$. Both multiplications are exact on grid numerators, so they add no rounding. <cite data-source="paper">multiplications act exactly on grid numerators.</cite> The computed transforms do carry rounding error. The paper bounds the final absolute error by $448b\,2^{-3b/4}$, which is below $\frac12$ for large $b$. <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2</cite>. Since the true coefficients are integers, a computed value within $\frac12$ of one of them rounds to exactly that integer.
