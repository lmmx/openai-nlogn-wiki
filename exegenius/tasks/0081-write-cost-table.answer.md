A cost table lists the separate running-time terms of an algorithm, each a power of a size parameter, so that the sum of the terms bounds the total time. In this paper it is the final accounting step: <cite data-source="paper">makes all terms in its cost table fit Theorem 1.</cite> The parameters are chosen so that every term fits the bound $O(n(\lg n)^{1-\kappa})$ of the [main theorem](main-theorem.md), and the table is where that fit is checked.

## Splitting the cost and dividing by a volume

The cost table splits the [running time cost](running-time-cost.md) of the algorithm into separate terms, one for each kind of work. Each term is first divided by one common volume, so that every term becomes a power of one size parameter and the terms can be compared directly.

Write $b = \lceil \log_2 n \rceil$ for the rounded-up base-2 logarithm of $n$. Write $p = 6b$ for the working precision, the parameter that sets the coefficient width up to a constant factor, so $p = \Theta(\log n)$. Write $T$ for the power of two that sets the number of cells in the padded box (the array the algorithm works on), with $4n/b \le T < 8n/b$. Write $V = Tp$ for the logical bit volume of the padded box, so $V = \Theta(n)$.

The exponents are fixed numbers, chosen once for the whole construction. The exponent $\epsilon$ is a fixed positive rational number. The exponent $c$ is a fixed positive rational number. The exponent $\tau$ is a fixed rational number between zero and one. The exponent $\lambda'$ is a fixed rational number below one. The exponent $\delta$ is a fixed rational number. <cite data-source="paper">The exponents can all be chosen rational</cite>. The factor $\alpha = \Theta(p^{1/4+\epsilon/2})$ is the factor in the cost of the Gaussian line maps.

Four more symbols appear in the table. Write $d$ for the number of axes of the padded box, with $d = \lfloor b^{\epsilon} \rfloor = \Theta(p^{\epsilon})$. Write $K = \lfloor d^{c} \rfloor = \Theta(p^{\epsilon c})$ for the width of the address chunks, in bits. Write $r$ for the largest axis length of the padded box, a power of two. Write $\ell = \log_2 r = \Theta(p^{1-\epsilon})$ for its base-2 logarithm.

## The table

<cite data-source="paper">Table 1 lists costs after division by V</cite>. The table below restates its rows with the symbols above. Each row gives one operation, its cost divided by $V$, and the power of $p$ that bounds that cost.

| Operation | Cost divided by $V$ | Power of $p$ |
| --- | --- | --- |
| Prefix-slot moves and individual butterfly rounds | $dK$ | $\epsilon(1+c)$ |
| Chunk exchanges for transform layout | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ |
| Simultaneous butterfly rounds | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ |
| CRT and axis layouts | $d^2(1+\ell^{\tau})$ | $\tau+\epsilon(2-\tau)$ |
| Gaussian line maps | $d\,p^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ |
| Chirps, twists and scalar products | $d\,p^{\delta}$ | $\epsilon+\delta$ |
| Packed polynomial products | $\log(rp)$ | $1-\epsilon$ |
| Final scaling and rounding | $p^{\delta}$ | absorbed in the constant |
| Input, padding, carries and output | $1$ | absorbed in the constant |

Each power follows from substituting the sizes above. For example, the first row is $dK = \Theta(p^{\epsilon})\,\Theta(p^{\epsilon c}) = \Theta(p^{\epsilon(1+c)})$.

A table is a finite sum of such terms. Suppose a table had only the terms $p^{0.5}$, $p^{0.9}$ and $3$ after division by $V$. For $p \ge 1$ each term is at most $3p^{0.9}$, so the total is at most $5p^{0.9}$, and the cost is $O(V p^{0.9})$. The largest power decides the bound, so the question for the real table is whether every power stays below one by a fixed margin.

## Why every term fits

The margin of a power is one minus that power. <cite data-source="paper">Each of the seven displayed powers is at most 1 − 2κ by (45).</cite> So each term is at most a constant times $p^{1-\kappa}$, after multiplying by any fixed power of $\log p$, because a fixed power of $\log p$ is at most $p^{\kappa}$ for large $p$. The smallest margin is exactly $2\kappa$: <cite data-source="paper">Thus mini gi = 2−181 = 2κ.</cite>

Multiplying by $V$ and using $V = \Theta(n)$ and $p = \Theta(\log n)$ gives $O(V p^{1-\kappa}) = O(n(\lg n)^{1-\kappa})$. Every row of the table is therefore within the bound of the theorem, and so is their sum.
