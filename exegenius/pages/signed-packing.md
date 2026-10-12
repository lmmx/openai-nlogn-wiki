Signed coefficient packing is an encoding that turns the coefficients of a polynomial, some of them negative, into one integer, so that multiplying polynomials becomes multiplying integers. It is also called Kronecker substitution. <cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite>

Fix a block width $w$, the number of bits given to each coefficient. For a polynomial $f$ with integer coefficients, write $F = f(2^w)$ for its packed integer. A negative coefficient simply subtracts from its block.

Packing respects products. If $g$ is a second polynomial with packed integer $G = g(2^w)$ and $h = fg$, then $FG = h(2^w)$ exactly. One integer multiplication thus gives $FG$, and the coefficients of $h$ are read back from it, provided each is below $2^{w-1}$ in absolute value.

Recovery reads the blocks from the bottom as balanced digits in $[-2^{w-1}, 2^{w-1})$, carrying remainders upward. Such a digit string is unique for its value: if two had equal values, their lowest differing block would leave a difference that is a multiple of $2^w$ yet smaller than $2^w$ in absolute value, so it is zero. The coefficients of $h$ form such a string, so they are the recovered digits.

Worked example: take $f = 1-2x$, $g = 3+x$ and $w = 4$, where $x$ is the polynomial variable, not the input string. Then $F = 1-32 = -31$, $G = 3+16 = 19$, and $FG = -589$. The balanced base-16 digits of $-589$ are $3$, $-5$, $-2$, the coefficients of $fg = 3-5x-2x^2$.

The product of the two packed integers is computed by the [Established O(n log n) multiplier](established-multiplier.md), used as a black box. <cite data-source="paper">Calls to the established O(n log n) multiplier are ordinary subroutine calls; they do not invoke the improved theorem recursively.</cite>
