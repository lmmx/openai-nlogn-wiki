The Chinese remainder theorem says when a system of [congruences](congruence-modulo.md) has a solution, and how many solutions it has. It is the arithmetic fact behind the [Chinese-remainder map](chinese-remainder-map.md), which relabels the positions of a [cyclic convolution](cyclic-convolution.md) so that it becomes multidimensional.

Let $\Xi$ be the number of congruences in the system. Index them by $\mathcal{L}=1,\dots,\Xi$. For each $\mathcal{L}$, let $M_\mathcal{L}$ be the modulus, a positive integer, and $\varrho_\mathcal{L}$ the residue, an integer. The unknown is an integer $\mathcal{Y}$, and $\mathcal{Y}'$ denotes a second integer to be compared with it. Call $\mathcal{Y}$ a solution when

$$\mathcal{Y} \equiv \varrho_\mathcal{L} \pmod{M_\mathcal{L}} \qquad \text{for every } \mathcal{L}=1,\dots,\Xi.$$

The theorem requires moduli that are pairwise [coprime](coprime.md). That is, any two of $M_1,\dots,M_\Xi$ have greatest common divisor $1$. Let $\mathcal{N}=M_1M_2\cdots M_\Xi$ be the product of all the moduli, a positive integer.

The statement is this. If the moduli are pairwise coprime, then a solution exists, and an integer $\mathcal{Y}'$ is also a solution exactly when $\mathcal{Y}'\equiv\mathcal{Y}\pmod{\mathcal{N}}$. So the solutions form one residue class modulo $\mathcal{N}$. Read as a map, this says that an integer modulo $\mathcal{N}$ is determined by its residues modulo $M_1,\dots,M_\Xi$, and every tuple of such residues occurs.

Coprimality cannot be dropped. Take the moduli $2$ and $4$ with residues $0$ and $1$. The first congruence says $\mathcal{Y}$ is even and the second says it is odd, so no solution exists.

Uniqueness. Let $\mathcal{Y}$ and $\mathcal{Y}'$ be solutions, and put $\mathcal{E}=\mathcal{Y}'-\mathcal{Y}$. Every $M_\mathcal{L}$ divides $\mathcal{E}$. We show by induction on $\mathcal{L}$ that $M_1\cdots M_\mathcal{L}$ divides $\mathcal{E}$. The case $\mathcal{L}=1$ holds. Suppose $\mathcal{E}=M_1\cdots M_\mathcal{L}\,\Delta$, where $\Delta$ is an integer cofactor. A prime dividing both $M_{\mathcal{L}+1}$ and $M_1\cdots M_\mathcal{L}$ would divide some $M_{\mathcal{L}'}$ with $\mathcal{L}'\le\mathcal{L}$, since a prime dividing a product divides one of its factors. That contradicts pairwise coprimality. So $M_{\mathcal{L}+1}$ shares no prime factor with $M_1\cdots M_\mathcal{L}$. Euclid's lemma (an integer that divides a product and shares no prime factor with one factor divides the other factor) gives $M_{\mathcal{L}+1}\mid\Delta$, so $M_1\cdots M_{\mathcal{L}+1}$ divides $\mathcal{E}$. Taking $\mathcal{L}=\Xi$ gives $\mathcal{N}\mid\mathcal{E}$, that is, $\mathcal{Y}'\equiv\mathcal{Y}\pmod{\mathcal{N}}$.

Existence. Fix $\mathcal{L}$. The integer $\mathcal{N}/M_\mathcal{L}$ is the product of the other moduli. A prime dividing both $M_\mathcal{L}$ and $\mathcal{N}/M_\mathcal{L}$ would divide some other modulus, which is impossible, so the two are coprime. Since they are coprime, [Bézout's identity](bezout-identity.md) gives integers $\varpi_\mathcal{L}$ and $\varsigma_\mathcal{L}$ with $\varpi_\mathcal{L}\,\mathcal{N}/M_\mathcal{L}+\varsigma_\mathcal{L}\,M_\mathcal{L}=1$. Reducing modulo $M_\mathcal{L}$ gives $\varpi_\mathcal{L}\,\mathcal{N}/M_\mathcal{L}\equiv 1 \pmod{M_\mathcal{L}}$. Put

$$\mathcal{Y}=\sum_{\mathcal{L}=1}^{\Xi}\varrho_\mathcal{L}\,\varpi_\mathcal{L}\,\frac{\mathcal{N}}{M_\mathcal{L}}.$$

Fix $\mathcal{L}_0$ and reduce modulo $M_{\mathcal{L}_0}$. For $\mathcal{L}\ne\mathcal{L}_0$, the factor $\mathcal{N}/M_\mathcal{L}$ contains $M_{\mathcal{L}_0}$, so that term is divisible by $M_{\mathcal{L}_0}$. The $\mathcal{L}_0$ term is congruent to $\varrho_{\mathcal{L}_0}$, because $\varpi_{\mathcal{L}_0}\,\mathcal{N}/M_{\mathcal{L}_0}\equiv 1$. So $\mathcal{Y}\equiv\varrho_{\mathcal{L}_0} \pmod{M_{\mathcal{L}_0}}$ for every $\mathcal{L}_0$, and $\mathcal{Y}$ is a solution.

For example, take $\Xi=3$, moduli $3$, $4$, $5$ (pairwise coprime, so $\mathcal{N}=60$), and residues $2$, $3$, $1$. Then $\mathcal{N}/3=20$, $\mathcal{N}/4=15$ and $\mathcal{N}/5=12$. The inverses are $\varpi_1=2$, since $2\cdot 20=40\equiv 1 \pmod 3$; $\varpi_2=3$, since $3\cdot 15=45\equiv 1 \pmod 4$; and $\varpi_3=3$, since $3\cdot 12=36\equiv 1 \pmod 5$. So

$$\mathcal{Y} = 2\cdot 2\cdot 20+3\cdot 3\cdot 15+1\cdot 3\cdot 12 = 80+135+36 = 251.$$

Since $251=4\cdot 60+11$, the solutions are exactly the integers $11+60k$ for integers $k$. Check: $11$ leaves remainder $2$ mod $3$, remainder $3$ mod $4$, and remainder $1$ mod $5$.

The paper uses the same kind of split. <cite data-source="paper">The following map uses that algebraic split</cite>. Agarwal and Cooley <cite data-source="paper">used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite> cyclic convolution. The paper's map then places the radix-digit coefficients on distinct prime cyclic axes <cite data-source="paper">by a Chinese-remainder map that preserves convolution</cite>.
