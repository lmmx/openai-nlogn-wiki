A linear contraction is a linear map $A$ between normed spaces that does not increase the size of its inputs: $\|Ax\| \le \|x\|$ for every input $x$. The norm is a measure of size, and for coefficient arrays the paper uses the maximum absolute value of the coefficients, the [sup norm](sup-norm.md).

A contraction keeps errors from growing. If a computed input differs from the exact input by $\varepsilon$ in norm, then its image under a contraction differs by at most $\varepsilon$. This is why the paper can chain several resampling maps without losing control of the error.

As an example, the map $x \mapsto x/2$ is a contraction on any normed space, since $\|x/2\| = \|x\|/2 \le \|x\|$. The paper's Gaussian resampling maps are contractions of this kind, in the sense that they do not amplify the sup norm of their inputs.

The [Gaussian resampling](gaussian-resampling.md) step uses a pair of such maps, one in each direction between a length-$s$ grid and a length-$t$ grid. Their contraction property is what allows the approximate resampling to be analysed with fixed precision.
