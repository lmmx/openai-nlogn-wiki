Little-o notation says that one function is negligible next to another. It is the form in which the integer multiplication result below $n\lg n$ states that its cost falls strictly below $n\lg n$, and so it is what turns the saving into a refutation of the optimality conjecture.

The variable $\lambda$ is the real point at which both functions are evaluated, and it is taken to infinity. The function $\varphi$ is the one being bounded, a map from the positive reals to the positive reals. The function $\psi$ is the comparison function, a map from the positive reals to the positive reals that is positive for all large $\lambda$.

We write $\varphi(\lambda) = o(\psi(\lambda))$ as $\lambda \to \infty$ when the ratio tends to zero:

$$\lim_{\lambda \to \infty} \frac{\varphi(\lambda)}{\psi(\lambda)} = 0.$$

Every function that is $o(\psi)$ is also $O(\psi)$, since a ratio that tends to zero is eventually at most $1$. The converse fails. For example $2\lambda$ is $O(\lambda)$, yet $2\lambda/\lambda = 2$ does not tend to zero, so $2\lambda$ is not $o(\lambda)$. By contrast $\lambda = o(\lambda^2)$, because $\lambda/\lambda^2 = 1/\lambda$ tends to zero.

The bound of the main result has the form $n(\lg n)^{1-\kappa}$ with $\kappa = 2^{-182}$, where $n$ is the input length and $\lg n$ is the binary logarithm. Dividing by $n\lg n$ gives

$$\frac{n(\lg n)^{1-\kappa}}{n\lg n} = (\lg n)^{-\kappa} \longrightarrow 0 \qquad (n \to \infty),$$

because $\kappa > 0$. The saving is therefore a power of the logarithm, and little-o records that this saving eventually falls below every positive constant. Little-o notation bounds the cost of the multiplication machine strictly below $n\lg n$: its running time is $o(n\lg n)$, not merely $O(n\lg n)$.

The optimality conjecture asserts a lower bound $T_A(n) \ge c_A\, n\lg n$ for a positive constant $c_A$ and all large $n$. Dividing by $n\lg n$ shows that a machine whose time is $o(n\lg n)$ has $T_A(n)/(n\lg n) \to 0$, which contradicts $T_A(n)/(n\lg n) \ge c_A > 0$. The paper states the saving as a limit in the same way: <cite data-source="paper">The power saving proved here gives a limit of zero through all input lengths</cite>.

The paper uses the notation in its own estimates to say that a quantity is negligible against a parameter: <cite data-source="paper">γ = o(b). For example b ≥ 224 implies γ ≤ b/4.</cite>
