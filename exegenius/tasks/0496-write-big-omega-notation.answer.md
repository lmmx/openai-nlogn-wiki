Big-Omega notation says that one function is at least a constant multiple of another once the input is large, and it is the lower half of [Big-Theta notation](big-theta-notation.md). The optimality conjecture for integer multiplication is stated in this notation, and the main theorem refutes it.

Let $u$ and $h$ be functions from input sizes to nonnegative real numbers, as on the Big-Theta page, with $N$ the input size and $C_1$ and $N_0$ as there. The notation $\Omega(h)$ denotes the set of functions $u$ for which there are a constant $C_1>0$ and a threshold $N_0$ such that

$$u(N)\ge C_1\,h(N)\qquad\text{for all } N\ge N_0.$$

We write $u(N)=\Omega(h(N))$ when $u$ lies in this set. The letter $\Omega$ changes meaning here: on the [Supremum](supremum.md) page it names an upper bound of a set. Only this lower inequality is required. The upper bound $u(N)=O(h(N))$ says nothing about it, and $u(N)=\Theta(h(N))$ holds exactly when both bounds hold.

Worked example. Let $u(N)=3N^2+5N$ and $h(N)=N^2$. For $N\ge 1$ we have $3N^2\le 3N^2+5N$, so $u(N)=\Omega(N^2)$ with $C_1=3$ and $N_0=1$. The term $3N^2$ supplies the lower bound, and the linear term only adds to it. The same pattern gives $n\lg n=\Omega(n)$: since $\lg n\ge 1$ for $n\ge 1$, we have $n\lg n\ge n$ for all $n\ge 1$, so $C_1=1$ and $N_0=1$ work.

The converse fails. The function $N$ is not $\Omega(N^2)$: for any $C_1>0$, the inequality $N\ge C_1N^2$ fails once $N>1/C_1$, so no constant can work.

Schönhage and Strassen conjectured $n\log n$ as the optimal order of multiplication cost. <cite data-source="paper">Schönhage and Strassen conjectured n log n as the optimal order of multiplication cost</cite>. For a multiplication machine $A$ with running time $T_A(n)$ on inputs of length $n$, the conjecture for $A$ says that $T_A(n)=\Omega(n\lg n)$: there is a constant $c_A>0$ and a threshold such that $T_A(n)\ge c_A\,n\lg n$ for all large $n$. The conjecture asks for this for every such machine.

The main theorem bounds the running time of one fixed machine $A$ by $O(n(\lg n)^{1-\kappa})$, so $T_A(n)/(n\lg n)\le C(\lg n)^{-\kappa}$ for all large $n$. This ratio tends to zero. A function whose ratio to $n\lg n$ tends to zero cannot be $\Omega(n\lg n)$, because the ratio would have to stay at least $c_A$ for large $n$ (the [little-o notation](little-o-notation.md) page develops this comparison). The paper states the limit directly: <cite data-source="paper">The power saving proved here gives a limit of zero through all input lengths</cite>.

The lower bound is stated for machines of the [fixed-tape machine model](fixed-tape-model.md), where each machine has one fixed number of tapes. The paper's setting for the lower bound is given by this sentence: <cite data-source="paper">In the present fixed-tape model, an eventual lower bound for every multiplication machine means</cite>. Because one machine $A$ fails the lower bound, the conjecture as a whole is refuted.
