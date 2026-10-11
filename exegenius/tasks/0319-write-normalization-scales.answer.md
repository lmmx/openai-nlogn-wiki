Normalization scales are the known powers of two and transform lengths by which a computed product is multiplied at the end, so that the output is the exact integer convolution of the digit arrays rather than a scaled copy of it. They are the last arithmetic step before rounding in the paper's [integer multiplication algorithm](main-theorem.md).

The normalized transform $F_q$ of length $q$ sends a vector $f=(f_0,\dots,f_{q-1})$ to
$$(F_q f)_k=\frac1q\sum_{j=0}^{q-1} f_j\,e^{-2\pi i jk/q},\qquad 0\le k<q,$$
and $F_q^+$ is the same sum with $e^{+2\pi i jk/q}$ in place of $e^{-2\pi i jk/q}$. Each output is an average of $q$ terms, each an input times a complex number of modulus one, so the transform never increases the largest modulus of its input: <cite data-source="paper">Each normalized Fourier transform above is a contraction</cite>.

For vectors $f$ and $g$ of length $q$, let $f\ast g$ be their cyclic convolution and $\cdot$ the entrywise product. Two rules hold:
$$F_q(f\ast g)=q\,(F_qf)\cdot(F_qg),\qquad F_q^+F_q=\tfrac1q\,I.$$
The paper states them as <cite data-source="paper">The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S.</cite>, with $S$ read as $q$. Both follow by expanding the sums. Substituting $l=j+m$ (indices mod $q$) turns $\frac1q\sum_l (f\ast g)_l e^{-2\pi i lk/q}$ into $\frac1q\sum_{j,m} f_j g_m e^{-2\pi i (j+m)k/q}=q\,(F_qf)_k(F_qg)_k$. For the second rule, $(F_q^+F_qf)_k=\frac1{q^2}\sum_l f_l\sum_j e^{2\pi i j(k-l)/q}$, and the inner sum is $q$ when $l=k$ and $0$ otherwise, since it is a geometric sum with a $q$th root of unity as ratio.

Applying the first rule to the transformed inputs, then the second, gives
$$F_q^+\big((F_qf)\cdot(F_qg)\big)=\frac1q\,F_q^+F_q(f\ast g)=\frac1{q^2}\,(f\ast g).$$
Normalization scales undo the normalization of [normalized cyclic convolution](normalized-cyclic-convolution.md): with $f\circledast g=(f\ast g)/q$, the three transforms leave $\frac1q(f\circledast g)$. <cite data-source="paper">The two occurrences of S in this algorithm undo different normalizations.</cite> The first multiplication by $q$ gives $f\circledast g$, and the second gives $f\ast g$.

Worked example: take $q=4$ and suppose the transforms leave $3/16$, which is $(f\ast g)_k/q^2$ for $(f\ast g)_k=3$. Multiplying by $4$ gives $3/4$, and by $4$ again gives $3$.

The digits carry a second scale. Let $\delta$ and $\delta'$ be the integer digit arrays of the two inputs, with entries from $0$ to $2^b-1$. Each entry is stored as $\sigma$ times the digit, where $\sigma = 2^{-b-2}$ is the digit scale. So the stored arrays are $f=\sigma\delta$ and $g=\sigma\delta'$, and each stored value has modulus below $\frac14$, the bound the source gives its inputs: <cite data-source="paper">Their coefficients are exact p-bit grid values of norm less than 1/4.</cite>

Since $f\ast g=\sigma^2(\delta\ast\delta')$, the product carries $\sigma^2=2^{-2b-4}$, and the algorithm multiplies by $2^{2b+4}$ to remove it: <cite data-source="paper">reverses the two input scales.</cite>

Worked example: take $b=2$, so $\sigma=2^{-4}$. The digit values $3$ and $2$ are stored as $3/16$ and $2/16$. Their product $6/256$, multiplied by $2^{2b+4}=256$, returns $6$.

Each input has $m$ digits, so the ordinary product of the digit polynomials has degree at most $2m-2$. Padding the arrays with zeros to length $q>2m-2$ means no index reaches $q$ and wraps, so the cyclic convolution equals the ordinary one: <cite data-source="paper">Thus convolution modulo xS − 1 has no nonzero wraparound.</cite>

Altogether the algorithm multiplies by $q$, then by $2^{2b+4}q$, and the result is $2^{2b+4}\sigma^2(\delta\ast\delta')=\delta\ast\delta'$. Both multiplications are exact on grid numerators, so they add no rounding: <cite data-source="paper">multiplications act exactly on grid numerators.</cite> The remaining error is bounded by the source, which <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2,</cite> so rounding returns each coefficient exactly.
