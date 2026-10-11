The Chinese remainder theorem says when a system of congruences has a solution, and how many solutions it has. It is the arithmetic fact behind the [Chinese-remainder map](chinese-remainder-map.md), which relabels the positions of a [cyclic convolution](cyclic-convolution.md) so that it becomes a multidimensional one.

The theorem concerns a system of [congruences](congruence-modulo.md) with pairwise coprime moduli. Let $J$ be the number of congruences. Index them by $\sigma=1,\dots,J$. For each $\sigma$, let $W_\sigma$ be the modulus, a positive integer, and $\varrho_\sigma$ the residue, an integer. The unknown is an integer $Y$, and $Y$ is a solution when

$$Y \equiv \varrho_\sigma \pmod{W_\sigma} \qquad \text{for every } \sigma=1,\dots,J.$$

The theorem requires moduli that are pairwise [coprime](coprime.md): any two of $W_1,\dots,W_J$ have greatest common divisor $1$. Let $\Gamma = W_1W_2\cdots W_J$ be the product of all the moduli, a positive integer.

The statement is this. If the moduli are pairwise coprime, then the system has a solution, and an integer $Y'$ is also a solution exactly when $Y' \equiv Y \pmod{\Gamma}$. So the solutions form one residue class modulo $\Gamma$. Read as a map, this says that an integer modulo $\Gamma$ is determined by its residues modulo $W_1,\dots,W_J$, and that every tuple of such residues occurs.

Coprimality cannot be dropped. Take the moduli $2$ and $4$ with residues $0$ and $1$. The first congruence says $Y$ is even and the second says $Y$ is odd, so no solution exists.

Uniqueness. Suppose $Y$ and $Y'$ are both solutions, and let $D=Y'-Y$. Then every $W_\sigma$ divides $D$. We show by induction on $\sigma$ that $W_1W_2\cdots W_\sigma$ divides $D$. The case $\sigma=1$ holds. Suppose $D=W_1\cdots W_\sigma\,\Delta$ for an integer $\Delta$. The integer $W_{\sigma+1}$ shares no prime factor with $W_1\cdots W_\sigma$: a prime dividing both would divide some $W_{\sigma'}$ with $\sigma'\le\sigma$, since a prime dividing a product divides one of its factors, and that contradicts pairwise coprimality. Since $W_{\sigma+1}$ divides $D=W_1\cdots W_\sigma\,\Delta$ and is coprime to $W_1\cdots W_\sigma$, Euclid's lemma gives $W_{\sigma+1}\mid\Delta$. Hence $W_1\cdots W_{\sigma+1}$ divides $D$. Taking $\sigma=J$ gives $\Gamma\mid D$, so $Y'\equiv Y \pmod{\Gamma}$.

Existence. Fix $\sigma$. The integer $\Gamma/W_\sigma$ is the product of the other moduli. The argument above shows that $\Gamma/W_\sigma$ and $W_\sigma$ share no prime factor, so their greatest common divisor is $1$. By Bézout's identity there are integers $\varpi_\sigma$ and $\Xi_\sigma$ with $\varpi_\sigma\,\Gamma/W_\sigma+\Xi_\sigma\,W_\sigma=1$. Reducing modulo $W_\sigma$ gives $\varpi_\sigma\,\Gamma/W_\sigma\equiv 1 \pmod{W_\sigma}$. Put

$$Y=\sum_{\sigma=1}^{J}\varrho_\sigma\,\varpi_\sigma\,\frac{\Gamma}{W_\sigma}.$$

Fix $\sigma_0$ and reduce modulo $W_{\sigma_0}$. For $\sigma\ne\sigma_0$, the factor $\Gamma/W_\sigma$ contains $W_{\sigma_0}$, so that term is divisible by $W_{\sigma_0}$. The $\sigma_0$ term is congruent to $\varrho_{\sigma_0}$, because $\varpi_{\sigma_0}\,\Gamma/W_{\sigma_0}\equiv 1$. So $Y\equiv\varrho_{\sigma_0} \pmod{W_{\sigma_0}}$ for every $\sigma_0$.

For example, take $J=3$, moduli $3$, $4$, $5$ (pairwise coprime, so $\Gamma=60$), and residues $2$, $3$, $1$. Then $\Gamma/3=20$, $\Gamma/4=15$ and $\Gamma/5=12$. The inverses are $\varpi_1=2$, since $2\cdot 20=40\equiv 1 \pmod 3$; $\varpi_2=3$, since $3\cdot 15=45\equiv 1 \pmod 4$; and $\varpi_3=3$, since $3\cdot 12=36\equiv 1 \pmod 5$. So

$$Y = 2\cdot 2\cdot 20+3\cdot 3\cdot 15+1\cdot 3\cdot 12 = 80+135+36 = 251.$$

Since $251=4\cdot 60+11$, the solutions are exactly the integers $11+60k$ for integers $k$. Check: $11$ leaves remainder $2$ mod $3$, remainder $3$ mod $4$, and remainder $1$ mod $5$.

The paper uses the same kind of split. Agarwal and Cooley <cite data-source="paper">used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite> cyclic convolution. The paper's map then places its coefficient list on distinct prime cyclic axes <cite data-source="paper">by a Chinese-remainder map that preserves convolution</cite>.
