Congruence is defined on pairs of [Integer](integer.md) values, and it groups them by their remainder after division by a fixed positive integer. It is the arithmetic behind the [Chinese-remainder map](chinese-remainder-map.md), which places coefficients on distinct prime cyclic axes, and behind the [centered residue](centered-residue.md), which recovers a signed coefficient from its remainder.

Fix a positive integer $\mu$, the modulus. For integers $\varrho$ and $\varsigma$, we write $\varrho \equiv \varsigma \pmod{\mu}$, read "$\varrho$ is congruent to $\varsigma$ modulo $\mu$", when $\mu$ divides $\varrho-\varsigma$, that is, when $\varrho-\varsigma=\vartheta\mu$ for some integer $\vartheta$, the number of copies of $\mu$ in the difference.

Congruence is an equivalence relation. $\mu$ divides $0$, so $\varrho \equiv \varrho$. $\mu$ divides $\varrho-\varsigma$ exactly when it divides $\varsigma-\varrho$, so the relation is symmetric. If $\varrho \equiv \varsigma$ and $\varsigma \equiv \varkappa$ for a third integer $\varkappa$, then $\varrho-\varkappa=(\varrho-\varsigma)+(\varsigma-\varkappa)$ is a sum of two multiples of $\mu$, so it is transitive. The class of $\varrho$ is the set of integers $\varpi$ with $\varpi \equiv \varrho \pmod{\mu}$; the classes partition the integers, so each integer lies in exactly one class.

Each class contains exactly one integer in $\{0,\dots,\mu-1\}$, its remainder. Write $\mathrm{rem}(\varrho)$ for the remainder of $\varrho$. To find it, take the largest multiple $\vartheta\mu$ of $\mu$ with $\vartheta\mu \le \varrho$; then $\mathrm{rem}(\varrho)=\varrho-\vartheta\mu$ lies in $\{0,\dots,\mu-1\}$. It is the only such integer, because two integers in $\{0,\dots,\mu-1\}$ differ by less than $\mu$, so their difference is not a nonzero multiple of $\mu$. For $\mu=10$ and $\varrho=27$, the largest multiple of $10$ not above $27$ is $20$, so $\mathrm{rem}(27)=7$. For $\varrho=-3$ the largest such multiple is $-10$, so $\mathrm{rem}(-3)=7$, and $-3 \equiv 7 \pmod{10}$.

Congruence respects sums and products. Let $\varrho' \equiv \varrho$ and $\varsigma' \equiv \varsigma$ modulo $\mu$, where $\varrho'$ and $\varsigma'$ are integers, with $\varrho'-\varrho=\vartheta\mu$ and $\varsigma'-\varsigma=\vartheta'\mu$, where $\vartheta'$ is the number of copies of $\mu$ in $\varsigma'-\varsigma$. Then $(\varrho'+\varsigma')-(\varrho+\varsigma)=(\vartheta+\vartheta')\mu$. Since $\varrho'\varsigma'-\varrho\varsigma=\varrho'(\varsigma'-\varsigma)+\varsigma(\varrho'-\varrho)$,

$$\varrho'\varsigma'-\varrho\varsigma=(\varrho'\vartheta'+\varsigma\vartheta)\mu.$$

So a sum or product may be reduced modulo $\mu$ at any step.

Congruence is applied in [Carry propagation](carry-propagation.md): each output digit is the residue of the input coefficient plus the incoming carry. Let $u_j$ be the input coefficient at position $j$ and $\gamma_j$ the carry into position $j$; here $\gamma_j$ is not the scalar of the linear algebra page. Here $c_j$ is the output digit at position $j$, the paper's $d_j$, and $\mu$ is the paper's $B_0$. The paper says to <cite data-source="paper">start with carry γ0 = 0</cite> and write <cite data-source="paper">dj ≡ uj + γj</cite> modulo $\mu$, with $0 \le c_j < \mu$:

$$c_j \equiv u_j+\gamma_j \pmod{\mu}, \qquad \gamma_{j+1}=\frac{u_j+\gamma_j-c_j}{\mu}.$$

The congruence says $\mu$ divides $u_j+\gamma_j-c_j$, so the carry $\gamma_{j+1}$ is an integer. For $\mu=10$, $u_j=27$ and $\gamma_j=0$, the digit is $c_j=7$ and the carry is $\gamma_{j+1}=(27-7)/10=2$.

The paper recovers each signed coefficient as the <cite data-source="paper">unique integer in [−B0 /2, B0 /2) congruent to qj + ρj</cite> modulo $\mu$, a [centered residue](centered-residue.md). The interval $[-\mu/2,\mu/2)$ holds exactly $\mu$ consecutive integers, and any two of them differ by less than $\mu$, so they lie in different classes and meet every class once. For $\mu=10$ the interval is $\{-5,\dots,4\}$, so the remainder $7$ is read back as $-3$.
