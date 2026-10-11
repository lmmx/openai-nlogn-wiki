The union bound says that the probability that at least one of several events occurs is at most the sum of their probabilities. The paper uses its counting form to show that the set of exceptional addresses in a packed addition is small, so that the addition is correct at every other address. The [Packed selected-bit addition](packed-bit-addition.md) page builds on that count.

## Statement

Here $\Omega$ is a finite [Ground set](ground-set.md), and the union bound in counting form is applied to subsets of it. Each $E_i$ is one of the subsets of $\Omega$, and $m$ is the number of these subsets, $E_1, \dots, E_m$. The union bound says

$$|E_1 \cup E_2 \cup \cdots \cup E_m| \le |E_1| + |E_2| + \cdots + |E_m|,$$

where $|X|$ is the number of elements of a set $X$. Choose an element of $\Omega$ uniformly at random. The probability that it lies in $E$ is $|E|/|\Omega|$, so dividing by $|\Omega|$ gives the probability form

$$\Pr[E_1 \cup \cdots \cup E_m] \le \Pr[E_1] + \cdots + \Pr[E_m].$$

The bound needs no independence between the events.

**Example.** Let $\Omega = \{0, 1, \dots, 99\}$, $m = 2$, $E_1$ the even numbers in $\Omega$ (50 elements), and $E_2$ the multiples of 5 (20 elements). The union has 60 elements, because the 10 multiples of 10 lie in both sets. The bound gives $60 \le 50 + 20 = 70$. For a uniformly random $x \in \Omega$, the probability that $x$ lies in the union is $0.6$, and the bound gives $0.6 \le 0.5 + 0.2$. The slack of 10 is the overlap, which the bound ignores.

## How the paper uses it

Here $f$ is the number of selected bit positions $j_0, \dots, j_{f-1}$ and $K$ is the width in bits of each segment. Each of the $f-1$ segment pairs carries two guard values, $g$ in $y$ and $h$ in $z$, both in $\{0, \dots, 2^{K-1}-1\}$, so there are $m = 2(f-1)$ guards. The paper notes that <cite data-source="paper">the complete y, z ranges give the same guard distribution at each choice of spectator</cite> coordinates, so a guard value can be treated as uniform on its $2^{K-1}$ values.

A guard is bad when its value falls outside the good range $10 \le g \le 2^{K-1} - 11$, which leaves the 10 smallest and 10 largest values excluded. <cite data-source="paper">There are exactly twenty excluded values for each guard in (23)</cite>. So a uniform guard is bad with probability $20/2^{K-1}$.

An address is exceptional when at least one of its guards is bad, so the exceptional set is the union of the per-guard bad sets. Applying the union bound to these $m = 2(f-1)$ events gives a bad fraction of

$$m \cdot \frac{20}{2^{K-1}} = \frac{80(f-1)}{2^{K}}.$$

<cite data-source="paper">the union bound over the 2(f − 1) guards gives</cite>. The paper caps this at one, since a probability bound above one says nothing: <cite data-source="paper">Put δbad = min{1, 80(f − 1)2−K }.</cite>

**Example.** Take $K = 8$, so each guard has $2^{7} = 128$ values, 20 of them bad, and each guard is bad with probability $20/128 = 5/32$. With $f = 3$ there are $m = 4$ guards, and the bound gives $4 \cdot 5/32 = 5/8$. This equals $80 \cdot 2 / 2^{8} = 5/8$, the paper's formula.
