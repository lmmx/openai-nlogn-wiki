The n log n optimality conjecture concerns the time to multiply two integers, where $n$ is the number of bits in each input. It claims that $n \log n$ is the optimal order of growth of that time. The main theorem of this wiki, [Integer multiplication below n log n](main-theorem.md), refutes it, so this page states exactly what is refuted.

The conjecture bounds the cost of [exact integer multiplication](exact-integer-multiplication.md) from below. Schönhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in <cite data-source="paper">O(n log n log log n)</cite> time on a multitape Turing machine, and they <cite data-source="paper">proposed n log n as the optimal order of growth</cite>. Harvey and van der Hoeven later established an <cite data-source="paper">unconditional O(n log n) bound</cite>, so $n \log n$ is achievable, and the conjecture says that nothing of smaller order is.

A lower bound only makes sense for a fixed machine, so the conjecture is stated for a fixed model. The paper's setting is <cite data-source="paper">one fixed finite-alphabet Turing machine with a fixed finite number</cite> of one-dimensional tapes, where the alphabet and the number of tapes do not grow with the input length.

Let $A$ be one fixed Turing machine that computes exact products. Let $T_A(n)$ be the worst-case running time of $A$ on inputs of two $n$-bit integers, the largest number of steps $A$ takes over all such inputs. Write $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$ for the base-2 logarithm of $n$, rounded up to an integer and never below $1$.

The conjecture says that for every such machine $A$ there are constants $c_A > 0$ and $N_A$ such that the following holds.

$$T_A(n) \ge c_A\, n \lg n \quad \text{for all } n \ge N_A.$$

The paper states this as <cite data-source="paper">an eventual lower bound for every multiplication machine means</cite> the inequality above, for each fixed machine.

The negation of the conjecture is that some one machine $A$ satisfies $\liminf_{n\to\infty} T_A(n)/(n\lg n) = 0$. The growth gap is large. Take $n = 1024$ and $n = 2048$: then $\lg n = 10$ and $\lg n = 11$, so $n \lg n$ grows from $10240$ to $22528$, a factor of $2.2$ when $n$ doubles. Schoolbook multiplication, which takes on the order of $n^2$ steps, grows by a factor of $4$.

The main theorem gives one fixed machine with $T_A(n) = O(n(\lg n)^{1-\kappa})$ for a specific constant $\kappa > 0$. Since $(\lg n)^{-\kappa} \to 0$, this machine has $T_A(n)/(n\lg n) \to 0$, which is the negation above. The paper confirms that this <cite data-source="paper">optimality conjecture of Schönhage and Strassen in this model.</cite>
