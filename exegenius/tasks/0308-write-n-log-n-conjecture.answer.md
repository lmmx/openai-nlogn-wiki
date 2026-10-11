Here $\log$ is the base-2 logarithm. The n log n optimality conjecture claims that $n \log n$ is the optimal order of growth of the time needed to multiply two integers, where $n$ is the number of bits in each input. Changing the base multiplies $n \log n$ by a constant, which leaves the order of growth unchanged. The main theorem of this wiki, [Integer multiplication below n log n](main-theorem.md), refutes the conjecture, so this page states exactly what is refuted.

The conjecture bounds the cost of [exact integer multiplication](exact-integer-multiplication.md) from below. Schönhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in <cite data-source="paper">O(n log n log log n)</cite> time on a multitape Turing machine, and they <cite data-source="paper">proposed n log n as the optimal order of growth</cite>. Later, Harvey and van der Hoeven reached an <cite data-source="paper">unconditional O(n log n) bound</cite>, so $n \log n$ is achievable. The conjecture says that nothing of smaller order is.

A lower bound on running time must refer to one machine, so the conjecture is stated for a fixed model. In this model, <cite data-source="paper">A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.</cite> Neither the alphabet nor the number of tapes grows with the input length.

Let $A$ be one fixed Turing machine that computes exact products, and let $T_A(n)$ be its worst-case running time: the largest number of steps $A$ takes over all pairs of $n$-bit integers. Write $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$ for the base-2 logarithm of $n$ rounded up to an integer and never below $1$.

The conjecture says that for every such machine $A$ there are a positive constant $c_A$ and a threshold $N_A$ on the input length such that the following holds.

$$T_A(n) \ge c_A\, n \lg n \quad \text{for all } n \ge N_A.$$

The paper says that <cite data-source="paper">an eventual lower bound for every multiplication machine means</cite> this inequality for each fixed machine. Eventual means that the inequality is required only from $N_A$ on.

The conjecture is negated through the [limit inferior](limit-inferior.md) of the ratio $T_A(n)/(n\lg n)$. The paper states the negation as <cite data-source="paper">Its negation requires one machine satisfying</cite> $\liminf_{n\to\infty} T_A(n)/(n\lg n) = 0$. For nonnegative terms, a limit inferior of zero means that the ratio falls below every $c>0$ infinitely often, which is exactly the negation: some machine $A$ has, for every $c > 0$ and every $N$, some $n \ge N$ with $T_A(n) < c\, n \lg n$.

The gap between these growth rates is large. For $n = 1024$, $\lg n = 10$ and $n \lg n = 10240$. For $n = 2048$, $\lg n = 11$ and $n \lg n = 22528$. Doubling $n$ multiplies $n \lg n$ by $2.2$, while schoolbook multiplication, which takes on the order of $n^2$ steps, multiplies by $4$.

The main theorem gives one fixed machine $A$ with $T_A(n) = O(n(\lg n)^{1-\kappa})$, where $\kappa$ is a fixed positive constant. Its value is <cite data-source="paper">κ = 2−182</cite>. Since $(\lg n)^{-\kappa} \to 0$, the ratio $T_A(n)/(n\lg n)$ tends to zero, so its limit inferior is zero and this machine satisfies the negation above. The paper states that its algorithm <cite data-source="paper">disproves the n log n optimality conjecture of Schönhage and Strassen in this model.</cite>
