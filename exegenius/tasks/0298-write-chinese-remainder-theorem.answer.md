The Chinese remainder theorem says when a system of congruences has a solution, and how many solutions it has. It is the arithmetic fact behind the [Chinese-remainder map](chinese-remainder-map.md), which relabels the positions of a [cyclic convolution](cyclic-convolution.md) so that it becomes a multidimensional one.

The theorem concerns a system of [congruences](congruence-modulo.md) with pairwise coprime moduli. Let $\chi$ be the number of congruences in the system. Here $\nu$ is an index numbering the congruences, running from $1$ to $\chi$. For each $\nu$, let $\kappa_\nu$ be the modulus of the $\nu$-th congruence, a positive integer, and let $\delta_\nu$ be its residue, an integer. The unknown is an integer $\tau$, which is a solution when it satisfies every congruence below:

$$\tau \equiv \delta_\nu \pmod{\kappa_\nu} \qquad \text{for every } \nu=1,\dots,\chi.$$

The theorem requires moduli that are pairwise [coprime](coprime.md). Every two of $\kappa_1,\dots,\kappa_\chi$ have greatest common divisor $1$. Let $\Lambda=\kappa_1\kappa_2\cdots\kappa_\chi$ be the product of the moduli, a positive integer.

The statement is this. If the moduli are pairwise coprime, then the system has a solution, and an integer $\tau'$ is also a solution exactly when $\tau'\equiv\tau \pmod{\Lambda}$. So the solutions form one residue class modulo $\Lambda$.

Coprimality cannot be dropped. Take the two moduli $2$ and $4$ with residues $0$ and $1$. The first congruence says $\tau$ is even and the second says $\tau$ is odd, so no solution exists.

For uniqueness, suppose $\tau$ and $\tau'$ are both solutions. Then every $\kappa_\nu$ divides $\tau-\tau'$. Take a prime $p$ with $p^e$ exactly dividing $\Lambda$. Because the moduli are pairwise coprime, $p$ divides exactly one modulus $\kappa_\nu$, and writing $\Lambda=\kappa_\nu R$ with $p$ not dividing $R$ gives $p^e\mid\kappa_\nu$. Hence $p^e$ divides $\tau-\tau'$. Doing this for every prime in $\Lambda$ shows $\Lambda$ divides $\tau-\tau'$.

For existence, fix $\nu$. No prime divides both $\kappa_\nu$ and another modulus, so $\Lambda/\kappa_\nu$, the product of the other moduli, is coprime to $\kappa_\nu$. Let $\pi_\nu$ be an integer that inverts $\Lambda/\kappa_\nu$ modulo $\kappa_\nu$, so that $\pi_\nu\,\Lambda/\kappa_\nu\equiv 1 \pmod{\kappa_\nu}$; such an integer exists because the two numbers are coprime. Put

$$\tau=\sum_{\nu=1}^{\chi}\delta_\nu\,\pi_\nu\,\frac{\Lambda}{\kappa_\nu}.$$

Fix an index $\nu_0$ and reduce modulo $\kappa_{\nu_0}$. Every term with $\nu\ne\nu_0$ contains the factor $\kappa_{\nu_0}$ inside $\Lambda/\kappa_\nu$, so it vanishes. The term with $\nu=\nu_0$ is congruent to $\delta_{\nu_0}$, because $\pi_{\nu_0}\,\Lambda/\kappa_{\nu_0}\equiv 1$. So $\tau\equiv\delta_{\nu_0} \pmod{\kappa_{\nu_0}}$ for every $\nu_0$.

For example, take $\chi=3$, moduli $3$, $4$, $5$ (pairwise coprime, so $\Lambda=60$), and residues $2$, $3$, $1$. Then $\Lambda/3=20$, $\Lambda/4=15$ and $\Lambda/5=12$. The inverses are $\pi_1=2$, since $2\cdot 20=40\equiv 1 \pmod 3$; $\pi_2=3$, since $3\cdot 15=45\equiv 1 \pmod 4$; and $\pi_3=3$, since $3\cdot 12=36\equiv 1 \pmod 5$. So

$$\tau = 2\cdot 2\cdot 20+3\cdot 3\cdot 15+1\cdot 3\cdot 12 = 80+135+36 = 251.$$

Since $251=4\cdot 60+11$, the solutions are exactly the integers $11+60k$. Checking, $11$ leaves remainder $2$ mod $3$, remainder $3$ mod $4$, and remainder $1$ mod $5$.

The paper relies on this theorem for the same kind of split. <cite data-source="paper">Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite> The moduli play the role of axis lengths, and the residues of a position on each axis determine that position.
