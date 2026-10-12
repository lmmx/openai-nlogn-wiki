Signed coefficient packing is an encoding that turns the coefficients of a polynomial, some of them negative, into one integer, so that multiplying polynomials becomes multiplying integers. It is also called Kronecker substitution. <cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite> The proof uses it to treat its polynomial products as ordinary integer products.

Fix a block width $w$, the number of bits given to each coefficient. For a polynomial $f$ with integer coefficients, write $F = f(2^w)$ for its packed integer. A negative coefficient needs no special case: it simply subtracts from its block, and $F$ is still an ordinary integer.

Packing respects products. If $g$ is a second polynomial with packed integer $G = g(2^w)$ and $h = fg$, then $FG = h(2^w)$ exactly. One integer multiplication therefore yields all coefficients of $h$ at once, provided every coefficient of $h$ is below $2^{w-1}$ in absolute value, so that the blocks do not overlap.

Recovery reads the blocks from the bottom as balanced digits: each block is reduced to a value in $[-2^{w-1}, 2^{w-1})$, and the remainder is carried upward, exactly as in ordinary carry propagation.

Worked example: take $f = 1-2x$, $g = 3+x$ and $w = 4$. Then $F = 1-32 = -31$, $G = 3+16 = 19$, and $FG = -589$. The balanced base-16 digits of $-589$ are $3$, $-5$, $-2$, which are the coefficients of $fg = 3-5x-2x^2$. All have absolute value below $8$, as required.

The product of the two packed integers is computed by the [Established O(n log n) multiplier](established-multiplier.md), used as a black box. <cite data-source="paper">Calls to the established O(n log n) multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively.</cite>
