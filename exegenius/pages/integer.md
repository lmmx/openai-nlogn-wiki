An integer is a whole number, positive, negative or zero. The target result, Theorem 1 of the paper *Integer multiplication below n log n* (OpenAI, 2026), multiplies two integers of $n$ bits each, and its argument first rewrites each integer as a list of digits so that the multiplication can be carried out on short coefficients.

Write $c_1, \dots, c_k$ for the digits of a list, where $k$ is the number of digits and $c_j$ is the digit at position $j$ counted from the left, so $c_1$ is the most significant. In a base $b$ (also called a radix), with $b \ge 2$ an integer, an integer is written as a list of digits, each between $0$ and $b-1$. Its value is

$$\sum_{j=1}^{k} c_j\, b^{k-j}.$$

In base 4 the integer 13 is the digit list $3, 1$, because $13 = 3 \cdot 4 + 1$; in base 2 the same integer is $1101$.

The paper reads a binary string in the same way. Write $x = x_1 x_2 \cdots x_m$ for a binary string, where $m$ is the number of bits and $x_j$ is its bit at position $j$ counted from the left. The paper reads $x$ as an integer by the rule

$$\mathrm{val}(x) = \sum_{j=1}^{m} x_j\, 2^{m-j},$$

which is the nonnegative integer value with the leftmost bit most significant. The paper states this as <cite data-source="paper">let val(x) be its nonnegative integer value</cite>.

A digit list also determines a polynomial. Here $t$ is an indeterminate, a formal variable that is not a number, so $1 + 3t$ is a polynomial with coefficients $1$ and $3$. Read in increasing position order, the digits of 13 in base 4 are $(1, 3)$, and these are the coefficients of $1 + 3t$; evaluating at $t = b = 4$ gives $1 + 3 \cdot 4 = 13$. The convolution of two coefficient lists is the coefficient list of the product of their polynomials.

The paper states the step that uses this as a reduction: <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite> That is, exact multiplication of two integers reduces to a convolution of short integer coefficients, obtained by splitting each input into radix digits. The sources do not say why this helps. Splitting turns the big inputs into short lists of small digits, so the work on the whole integers becomes a convolution whose entries are small, and the carries described below then recover the exact integer.

For example, take $13 \cdot 11$. The coefficient lists in increasing position order, in base 4, are $(1, 3)$ for 13 and $(3, 2)$ for 11, since $11 = 2 \cdot 4 + 3$. The product of $1 + 3t$ and $3 + 2t$ is $3 + 11t + 6t^2$, so the convolution is the list $(3, 11, 6)$. Evaluating at $t = 4$ gives $3 + 11 \cdot 4 + 6 \cdot 16 = 143 = 13 \cdot 11$. But $(3, 11, 6)$ is not yet a digit list, because $11$ is larger than the base.

A carry turns it into one. A carry is the part of a position's value that exceeds the base; it is passed to the next position. Position 0 holds $3$, which is already a digit. Position 1 holds $11 = 2 \cdot 4 + 3$: keep the digit $3$ and pass the carry $2$ to position 2. Position 2 holds $6 + 2 = 8 = 2 \cdot 4 + 0$: keep $0$ and pass $2$ to position 3. Position 3 holds $2$, a digit. The digits, most significant first, are $2, 0, 3, 3$, and $2 \cdot 4^3 + 0 \cdot 4^2 + 3 \cdot 4 + 3 = 143$.

Each base-4 digit is two bits, so the same digits in binary are $10\,00\,11\,11 = 10001111$, which is the binary form of $143$. Carry propagation across the radix digits is this carry step applied to the whole coefficient list, and it converts the integer coefficients into the exact binary product.
