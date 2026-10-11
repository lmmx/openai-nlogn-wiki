The polynomial ring modulo a fixed polynomial is the set of complex polynomials in which every multiple of that polynomial counts as zero, and it satisfies the axioms of a [Ring](ring.md). The argument needs it because its convolution on the remaining axes is computed over this ring: <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring.</cite>

Here $y$ is the indeterminate. Let $f$ be a monic polynomial with complex coefficients, that is, one whose leading coefficient is $1$. Let $m$ be the degree of $f$, the number of coefficients in each representative below. Write $R = \mathbb{C}[y]/(f)$ for the ring of classes of polynomials $g(y)$ with complex coefficients, where $g$ and $\hat g$ are identified when $g - \hat g$ is a multiple of $f$.

Here $r$ is the exponent of $y$ in the modulus $y^r+1$. The paper takes <cite data-source="paper">an integer r ≥ 2 that is a power of two</cite>, and for this modulus it writes the ring as <cite data-source="paper">Rr = C[y]/(y r + 1),</cite> which it calls $R_r$.

Each class contains exactly one polynomial $u$ of degree less than $m$, its representative. Existence and uniqueness follow from division with remainder by $f$. Here $u_t$ is the complex coefficient of $y^t$, and $t$ is its index, running from $0$ to $m-1$, so $u = \sum_{t=0}^{m-1} u_t y^t$. The list $(u_0, \dots, u_{m-1})$ is the coefficient list of $u$.

Addition is coefficientwise. Multiplication is ordinary polynomial multiplication followed by reduction: each power $y^e$ with $e \ge m$ that appears, where $e$ is the exponent of $y$, is replaced by its remainder on division by $f$.

Take $f = y^4+1$, so $m = 4$, and let $u = 1 + 2y + 3y^2$, with coefficient list $(1, 2, 3, 0)$. Then $y^3 u = y^3 + 2y^4 + 3y^5$. Since $y^4 = -1$ and $y^5 = -y$, we get $y^3 u = -2 - 3y + y^3$, with coefficient list $(-2, -3, 0, 1)$. Coefficients moved past the top re-enter at the bottom with reversed sign.

The paper states the general form: <cite data-source="paper">Multiplication by y a , for any integer a, permutes the coefficients and changes some signs</cite>. Here $s$ is the integer exponent, written $a$ in the paper, so the example has $s = 3$. Multiplication by a power of $y$ is what the paper calls <cite data-source="paper">multiplication by such a root is a signed shift of the</cite> coefficient list.
