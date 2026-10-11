A linear contraction is a linear map that acts on the vector spaces of [Linear algebra basics](linear-algebra-basics.md) and never increases the maximum modulus of a vector. It keeps errors from growing as they pass through a computation, which the exact-recovery step needs ([Exact coefficient recovery](recovery-and-error.md)).

Let $L\colon \mathbb{C}^m \to \mathbb{C}^{m'}$ be a linear map, where $m$ is the number of coordinates of its input vectors and $m'$ is the number of coordinates of its output vectors. For $x \in \mathbb{C}^m$, $\|x\|$ is its largest coordinate modulus. <cite data-source="paper">The vector norm is the maximum modulus of its coordinates.</cite>

$L$ is a linear contraction when $\|Lx\| \le \|x\|$ for every $x \in \mathbb{C}^m$. Its operator norm $\|L\|$ is defined through the [supremum](supremum.md) of $\|Lx\|$ over all $x$ with $\|x\| \le 1$. Thus $L$ is a contraction exactly when $\|L\| \le 1$.

Suppose the computed input is $x + \eta$ where $x$ is the exact input and $\eta$ is the error vector. By linearity, $L(x+\eta) - Lx = L\eta$, so $\|L(x+\eta) - Lx\| \le \|\eta\|$. <cite data-source="paper">A linear contraction propagates an input error without increasing it.</cite> In a chain of contractions, earlier errors do not grow; only the errors introduced at each step accumulate, and the recovery step needs their total below $1/2$.

The normalized transform $F_q$ of length $q$ has entries $\omega^{jk}/q$, where $\omega$ is a $q$-th root of unity, so $|\omega^{jk}| = 1$. Each output is $\frac{1}{q}\sum_j \omega^{jk} u_j$, so $|(F_q u)_k| \le \frac{1}{q}\sum_j |u_j| \le \|u\|$ and $\|F_q u\| \le \|u\|$. <cite data-source="paper">Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one.</cite>

For example, take $q = 2$ and $u = (1, i)$. The outputs are $\frac{1+i}{2}$ and $\frac{1-i}{2}$, each of modulus $\frac{\sqrt{2}}{2} \approx 0.71 \le 1 = \|u\|$. Unnormalized sums $(1+i, 1-i)$ have norm $\sqrt{2} > 1$, so the division by $q$ matters.
