Schoolbook multiplication is the grade-school method for multiplying two integers: each digit of one factor multiplies the other factor, the results are shifted into place, and the shifted partial products are added. It is the base case that the paper's construction falls back on for small inputs, so it matters for the final step of the argument.

For two $n$-bit binary strings, the method forms $n$ partial products of at most about $n$ bits each and adds them, which takes $O(n^2)$ steps, quadratic in the number of digits. <cite data-source="paper">so schoolbook arithmetic, descriptor copying,</cite> appears in the paper where its cost is bounded for integers of a given size.

Worked example: $3 \times 5$ in binary is $11 \times 101$. The partial products are $11 \cdot 1 = 11$, then $11 \cdot 0$ shifted one place to the left, which is $000$, then $11 \cdot 1$ shifted two places to the left, which is $1100$. Adding them aligned gives $0011 + 0000 + 1100 = 1111$, which is $15$.

Schoolbook multiplication is a method for [Exact integer multiplication](exact-integer-multiplication.md): it outputs the full product of two $n$-bit inputs, and it is exact for every input.

The argument uses it as follows. The parameters are chosen so that every term in the cost table is $O(n(\lg n)^{1-\kappa})$ for $\kappa = 2^{-182}$, which fits the bound of the theorem. Once the large-input bound holds, the paper fixes a cutoff and uses schoolbook multiplication for every input length below it. <cite data-source="paper">multiplication below it. The finitely many smaller lengths are included by enlarging the implicit</cite> The small cases therefore cost only a constant factor more, and the theorem's $O(n(\lg n)^{1-\kappa})$ bound holds for every input length.
