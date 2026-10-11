The n log n optimality conjecture says that $n \log n$ is the optimal order of growth of the time needed to multiply two integers. Here $\log$ is the base-2 logarithm; changing the base multiplies $n \log n$ by a constant, which leaves the order of growth unchanged. The main theorem of this wiki, [Integer multiplication below n log n](main-theorem.md), refutes the conjecture, so this page states exactly what is refuted.

The conjecture bounds the cost of [exact integer multiplication](exact-integer-multiplication.md) from below. Schönhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in <cite data-source="paper">O(n log n log log n)</cite> time on a multitape Turing machine, and they <cite data-source="paper">proposed n log n as the optimal order of growth</cite>. Harvey and van der Hoeven later established an <cite data-source="paper">unconditional O(n log n) bound</cite>, so $n \log n$ is achievable, and the conjecture says that nothing of smaller order is.

The conjecture is stated for a fixed model, because a lower bound on running time must refer to one machine. The model is <cite data-source="paper">one fixed finite-alphabet Turing machine with a fixed finite number</cite> of one-dimensional tapes, so neither the alphabet nor the number of tapes grows with the input length.

Let $A$ be one fixed Turing machine that computes exact products, and let $T_A(n)$ be its worst-case running time: the largest number of steps $A$ takes over all pairs of $n$-bit integers. Write $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$ for the base-2 logarithm of $n$ rounded up to an integer, and never below $1$.

The conjecture says that for every such machine $A$ there are constants $c_A > 0$ and $N_A$ such that the following holds.

$$T_A(n) \ge c_A\, n \lg n \quad \text{for all } n \ge N_A.$$

In the paper, <cite data-source="paper">an eventual lower bound for every multiplication machine means</cite> this inequality for each fixed machine.

The negation of the conjecture is that some machine $A$ has, for every $c > 0$ and every $N$, some $n \ge N$ with $T_A(n) < c\, n \lg n$. The conjecture is negated through the [limit inferior](limit-inferior.md) of $T_A(n)/(n\lg n)$, which must be zero for some machine $A$. The limit inferior, written $\liminf_{n\to\infty}$, is the smallest value a sequence approaches infinitely often. For nonnegative terms it is zero exactly when the sequence falls below every $c > 0$ infinitely often, which is the negation above. The paper writes it as <cite data-source="paper">Its negation requires one machine satisfying</cite> $\liminf_{n\to\infty} T_A(n)/(n\lg n) = 0$.

The gap between these growth rates is large. Take $n = 1024$ and $n = 2048$. Then $\lg n = 10$ and $\lg n = 11$, so $n \lg n$ grows from $10240$ to $22528$, a factor of $2.2$ when $n$ doubles. Schoolbook multiplication, which takes on the order of $n^2$ steps, grows by a factor of $4$.

The main theorem gives one fixed machine with $T_A(n) = O(n(\lg n)^{1-\kappa})$ for a specific constant $\kappa > 0$. Since $(\lg n)^{-\kappa} \to 0$, the ratio $T_A(n)/(n\lg n)$ tends to zero, so its limit inferior is zero, which is the negation above. The paper states that its algorithm <cite data-source="paper">disproves the n log n</cite> optimality conjecture of Schönhage and Strassen in this model.
