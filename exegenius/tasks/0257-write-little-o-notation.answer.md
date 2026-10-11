Little-o notation says that one function is negligible next to another. It states the integer multiplication result below $n\lg n$ as a strict saving, and so turns that saving into a refutation of the optimality conjecture.

The variable $\lambda$ is the real point at which both functions are evaluated, and it is taken to infinity. The function $\varphi$ is the one being bounded, and $\psi$ is the comparison function, positive for all large $\lambda$; both map the positive reals to the positive reals.

We write $\varphi(\lambda) = o(\psi(\lambda))$ as $\lambda \to \infty$ when the ratio tends to zero:

$$\lim_{\lambda \to \infty} \frac{\varphi(\lambda)}{\psi(\lambda)} = 0.$$

That is, for every positive number the ratio is below it for all sufficiently large $\lambda$. Taking that number to be $1$ shows that every $o(\psi)$ function is also $O(\psi)$: the ratio is eventually at most $1$, and since $\psi(\lambda) > 0$, $\varphi(\lambda) \le \psi(\lambda)$ for large $\lambda$. The converse fails. For example $2\lambda$ is $O(\lambda)$, yet $2\lambda/\lambda = 2$ never drops below $1$, so $2\lambda$ is not $o(\lambda)$.
The machine $A$ is one deterministic Turing machine with a fixed number of tapes that multiplies two $n$-bit integers exactly, where $n$ is the number of bits in each input. Here $\kappa = 2^{-182}$ is a fixed positive constant, and $\lg n$ is the [logarithm](logarithm.md) to base 2. The main result says that $A$ <cite data-source="paper">multiplies two n-bit integers in O(n(lg n)1−κ ) worstcase time, with κ = 2−182</cite>, so its time is $O(n(\lg n)^{1-\kappa})$.

Let $T_A(n)$ be the running time of $A$ on inputs of length $n$. The big-O bound gives a constant factor $C$ with $T_A(n) \le C\,n(\lg n)^{1-\kappa}$ for all sufficiently large $n$. Dividing by $n\lg n$ gives

$$\frac{T_A(n)}{n\lg n} \le C\,(\lg n)^{-\kappa} \qquad \text{for all sufficiently large } n.$$

Little-o notation bounds the cost of the [exact integer multiplication](exact-integer-multiplication.md) machine $A$ strictly below $n\lg n$: its running time is $o(n\lg n)$, not merely $O(n\lg n)$. As $n$ grows, $\lg n$ grows without bound. Then $(\lg n)^{\kappa}$ also grows without bound, since $\kappa > 0$, so $(\lg n)^{-\kappa} = 1/(\lg n)^{\kappa}$ tends to zero, and so does the ratio.

The optimality conjecture asserts that every exact multiplication machine $A$ satisfies $T_A(n) \ge c_A\, n\lg n$ for all sufficiently large $n$, for a positive constant $c_A$ depending on $A$. Dividing by $n\lg n$ keeps the ratio $T_A(n)/(n\lg n)$ at least $c_A$, yet that ratio tends to zero and is eventually below $c_A/2$, a contradiction. The conjecture fails for machine $A$. The paper states the saving as a limit too: <cite data-source="paper">The power saving proved here gives a limit of zero through all input lengths</cite>.
