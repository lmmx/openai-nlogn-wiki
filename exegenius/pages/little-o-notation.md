Little-o notation says that one function is negligible next to another, a strictly stronger statement than big-O. It is used here to state the [Integer multiplication below $n\lg n$](main-theorem.md) result as a strict saving below $n\lg n$, which refutes the optimality conjecture.

Here $\lambda$ is the real point at which both functions are evaluated, and it is taken to infinity. The function $\varphi$ is the one being bounded, and $\psi$ is the comparison function, positive for all large $\lambda$; both map the positive reals to the positive reals.

We write $\varphi(\lambda) = o(\psi(\lambda))$ as $\lambda \to \infty$ when the ratio tends to zero:

$$\lim_{\lambda \to \infty} \frac{\varphi(\lambda)}{\psi(\lambda)} = 0.$$

That is, for every positive number the ratio is below it for all sufficiently large $\lambda$. Taking that number to be $1$ shows that every $o(\psi)$ function is also $O(\psi)$: the ratio is eventually at most $1$, and since $\psi(\lambda) > 0$, $\varphi(\lambda) \le \psi(\lambda)$ for large $\lambda$. The converse fails. For example $2\lambda$ is $O(\lambda)$, yet $2\lambda/\lambda = 2$ never drops below $1$, so $2\lambda$ is not $o(\lambda)$.

Machine $A$ is the single deterministic Turing machine, with a fixed number of tapes, that multiplies two $n$-bit integers exactly, where $n$ is the number of bits in each input. Little-o notation is applied to the [running time cost](running-time-cost.md) $T_A$ of $A$, the largest number of steps $A$ takes on any input of length $n$. The paper's abstract says that $A$ <cite data-source="paper">multiplies two n-bit integers in O(n(lg n)1−κ ) worstcase time, with κ = 2−182</cite>, where $\kappa = 2^{-182}$ is a fixed constant. So $T_A(n) = O(n(\lg n)^{1-\kappa})$. Let $C$ be a constant with $T_A(n) \le C\,n(\lg n)^{1-\kappa}$ for all sufficiently large $n$. Dividing by $n\lg n$ gives

$$\frac{T_A(n)}{n\lg n} \le C\,(\lg n)^{-\kappa} \qquad \text{for all sufficiently large } n.$$

Little-o notation bounds the cost of the [exact integer multiplication](exact-integer-multiplication.md) machine $A$ strictly below $n\lg n$. The comparison uses the growth of $\lg n$, the [base-2 logarithm](base-two-logarithm.md) of $n$, which grows without bound as $n$ grows. Since $\kappa > 0$, $(\lg n)^{\kappa}$ also grows without bound, so $(\lg n)^{-\kappa} = 1/(\lg n)^{\kappa}$ tends to zero. The ratio is nonnegative and at most $C(\lg n)^{-\kappa}$, so it tends to zero too. That is $T_A(n) = o(n\lg n)$, a strictly stronger statement than $O(n\lg n)$.

The [optimality conjecture](n-log-n-conjecture.md) asserts that each exact multiplication machine $A$ has a positive constant $c_A$, depending on $A$, with $T_A(n) \ge c_A\,n\lg n$ for all sufficiently large $n$. Dividing by $n\lg n$ keeps the ratio at least $c_A$, yet the ratio tends to zero and is eventually below $c_A/2$. This is a contradiction, so the conjecture fails for $A$. The paper states the saving as a limit too: $\lim_{n\to\infty} T_A(n)/(n\lg n) = 0$. <cite data-source="paper">The power saving proved here gives a limit of zero through all input lengths</cite>.
