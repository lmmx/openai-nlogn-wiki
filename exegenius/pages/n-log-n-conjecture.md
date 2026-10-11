The n log n optimality conjecture says that no method of multiplying two integers can take asymptotically less time than $n \log n$, where $\log$ is the base-2 logarithm and $n$ is the number of bits in each input. It matters because the main theorem of this wiki, [Integer multiplication below n log n](main-theorem.md), refutes it, so this page states exactly what is refuted.

The conjecture bounds the cost of [exact integer multiplication](exact-integer-multiplication.md) from below. Changing the base would multiply $n \log n$ by a constant, which leaves the order of growth unchanged.

<cite data-source="paper">In the multitape Turing model, Schönhage and Strassen proved the bound O(n log n log log n)</cite> in 1971, and they <cite data-source="paper">proposed n log n as the optimal order of growth</cite>. Later, Harvey and van der Hoeven proved an <cite data-source="paper">unconditional O(n log n) bound</cite>, an upper bound showing that $n \log n$ is achievable. The conjecture asserts that nothing of smaller order is.

A lower bound on running time must refer to one machine, so the conjecture is stated for a fixed model. In the paper's model, <cite data-source="paper">A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.</cite> Neither the alphabet nor the number of tapes grows with the input length. This is the [fixed-tape machine model](fixed-tape-model.md).

Let $A$ be one fixed Turing machine that computes exact products, and let $T_A(n)$ be its worst-case running time: the largest number of steps $A$ takes over all pairs of $n$-bit integers. Write $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$ for the base-2 logarithm of $n$ rounded up to an integer and never below $1$.

The conjecture says that for every such machine $A$ there are a positive constant $c_A$ and a threshold $N_A$ on the input length such that the following holds.

$$T_A(n) \ge c_A\, n \lg n \quad \text{for all } n \ge N_A.$$

In the paper's wording, <cite data-source="paper">an eventual lower bound for every multiplication machine means</cite> this inequality for each fixed machine $A$, with its own $c_A$ and $N_A$. "Eventual" means that the inequality is required only from $N_A$ on, not at every input length.

The conjecture is negated through the [limit inferior](limit-inferior.md) of the ratio $T_A(n)/(n\lg n)$. The paper states the negation as <cite data-source="paper">Its negation requires one machine satisfying</cite> $\liminf_{n\to\infty} T_A(n)/(n\lg n) = 0$. For nonnegative terms, a limit inferior of zero means that for every positive $\varepsilon$ the ratio falls below $\varepsilon$ infinitely often. So the negation asks for one machine $A$ with this property: for every positive $\varepsilon$ and every threshold $n_0$ on the input length, there is some $n \ge n_0$ with $T_A(n) < \varepsilon\, n \lg n$.

For example, $n = 1024$ gives $\lg n = 10$ and $n \lg n = 10240$, while $n = 2048$ gives $\lg n = 11$ and $n \lg n = 22528$. Doubling $n$ multiplies $n \lg n$ by $2.2$ here.

The main theorem gives one fixed machine $A$ with $T_A(n) = O(n(\lg n)^{1-\kappa})$, where $\kappa$ is a fixed positive constant, the saving exponent. The paper gives its value as <cite data-source="paper">κ = 2−182</cite>. Since $(\lg n)^{-\kappa} \to 0$, the ratio $T_A(n)/(n\lg n)$ is $O((\lg n)^{-\kappa})$ and tends to zero. Its limit inferior is therefore zero, so this machine satisfies the negation above. The paper states that its algorithm <cite data-source="paper">disproves the n log n</cite> optimality conjecture of Schönhage and Strassen in this model.
