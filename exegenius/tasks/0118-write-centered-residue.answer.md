The centered residue of an integer is the representative of its residue class that lies in a window centered at zero, so a small negative integer keeps its sign. The paper uses it to read a signed product coefficient back from a residue, which is the step that makes [Exact coefficient recovery](recovery-and-error.md) return exact integers.

Let $M$ be a positive integer, the modulus, and let $m$ be an integer whose residue is taken. The centered residue of $m$ modulo $M$ is defined by [Congruence](congruence-modulo.md): it is the unique integer $c$ in $[-M/2, M/2)$ that is congruent to $m$ modulo $M$.

The interval $[-M/2, M/2)$ contains exactly $M$ integers, one from each residue class modulo $M$, so the centered residue is well defined. For example, take $M = 10$. The interval $[-5, 5)$ contains the integers $-5, \dots, 4$. Hence $7 \equiv -3$ gives centered residue $-3$, $12 \equiv 2$ gives centered residue $2$, and $-6 \equiv 4$ gives centered residue $4$.

Any integer $m$ with $|m| < M/2$ is its own centered residue. So if every coefficient of a product lies strictly within $M/2$ of zero, reading the residue of the product modulo $M$ returns each coefficient exactly. The paper's signed packing has this property, since it bounds each coefficient by half the modulus: <cite data-source="paper">identifies the next coefficient by its centered residue modulo B0</cite>
