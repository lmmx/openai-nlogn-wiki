A ring is a set with an addition and a multiplication that obey the usual rules of arithmetic, and the argument needs one because a ring gives the arithmetic of the [arrays](array.md) used here, whose entries are added and multiplied. A later step stores one coordinate as a polynomial modulo $y^r+1$, a ring in which $y^r$ is identified with $-1$, so the rules below fix that arithmetic.

Let $R$ be a ring, with elements written $\vartheta$, $\varpi$, $\varsigma$. For all of them:

- $\vartheta+\varpi=\varpi+\vartheta$ and $(\vartheta+\varpi)+\varsigma=\vartheta+(\varpi+\varsigma)$.
- There is a zero $0$ with $\vartheta+0=\vartheta$, and every $\vartheta$ has a negative $-\vartheta$ with $\vartheta+(-\vartheta)=0$. Together with the two addition rules, this says that addition forms a commutative group: an associative, commutative operation with a zero and negatives.
- $(\vartheta\varpi)\varsigma=\vartheta(\varpi\varsigma)$.
- $\vartheta(\varpi+\varsigma)=\vartheta\varpi+\vartheta\varsigma$ and $(\vartheta+\varpi)\varsigma=\vartheta\varsigma+\varpi\varsigma$.

The last two lines say that multiplication distributes over addition. Subtraction is defined as $\vartheta-\varpi=\vartheta+(-\varpi)$, so it needs no separate axiom.

The integers and the complex numbers, with ordinary addition and multiplication, are rings. The natural numbers $0,1,2,\dots$ are not, because no natural number added to $3$ gives $0$.

Rings can break a rule of ordinary arithmetic. In the integers modulo $6$, where addition and multiplication leave remainders after division by $6$, the product $2\cdot 3=6$ equals $0$ although neither factor is $0$. Since $2\cdot 3=2\cdot 0$ while $3\neq 0$, a common factor cannot always be cancelled from both sides of an equation, and "a product is zero only if a factor is zero" fails.

Rings with more specific structure appear in the argument. A residue ring is the set of integers modulo a fixed positive integer, and a Fermat-type residue ring takes that integer to be one more than a power of two. Residue rings are the arithmetic of the [fast multiplication of Schönhage and Strassen](schonhage-strassen.md). The paper states that Schönhage–Strassen multiplication <cite data-source="paper">uses roots of unity in Fermat-type residue rings</cite>.
