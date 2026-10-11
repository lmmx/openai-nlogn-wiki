A ring is a set with addition and multiplication that obey the usual rules of arithmetic. The argument needs rings because a ring gives the arithmetic of the [arrays](array.md) used here: their entries are coefficients that are added and multiplied. A later step stores one coordinate as a polynomial modulo $y^r+1$, a polynomial ring in which $y^r$ is identified with $-1$, so the rules below fix that arithmetic.

Let $R$ be a ring, with elements written $\xi$, $\zeta$, $\vartheta$. For all of them:

- $\xi+\zeta=\zeta+\xi$ and $(\xi+\zeta)+\vartheta=\xi+(\zeta+\vartheta)$.
- There is a zero $0$ with $\xi+0=\xi$, and every $\xi$ has a negative $-\xi$ with $\xi+(-\xi)=0$. Together with the two addition rules, this says that addition forms a commutative group: an associative, commutative operation with a zero and negatives.
- $(\xi\zeta)\vartheta=\xi(\zeta\vartheta)$.
- $\xi(\zeta+\vartheta)=\xi\zeta+\xi\vartheta$ and $(\xi+\zeta)\vartheta=\xi\vartheta+\zeta\vartheta$.

The last two lines say that multiplication distributes over addition. Subtraction is defined as $\xi-\zeta=\xi+(-\zeta)$, so it needs no separate axiom.

The integers and the complex numbers, with ordinary addition and multiplication, are rings. The natural numbers $0,1,2,\dots$ are not, because no natural number added to $3$ gives $0$.

Rings can break a rule of ordinary arithmetic. In the integers modulo $6$, the remainders after division by $6$, the product $2\cdot 3=6$ equals $0$ although neither factor is $0$. So "a product is zero only if a factor is zero" fails in a general ring, and an argument may not divide by a nonzero element.

Rings with more specific structure appear in the argument. Residue rings appear in the [fast multiplication of Schönhage and Strassen](schonhage-strassen.md), where certain multiplications become shifts. A residue ring is the set of integers modulo a fixed number, and a Fermat-type residue ring takes a number one more than a power of two. The fast multiplication <cite data-source="paper">uses roots of unity in Fermat-type residue rings</cite>. In the bit procedure, the two address fields are <cite data-source="paper">H, D over a common residue ring</cite>, so its update adds one field to the other inside that ring.
