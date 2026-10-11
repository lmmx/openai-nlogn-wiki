A ring is a set with addition and multiplication that obey the usual rules of arithmetic, where addition alone already behaves like ordinary addition of integers. The argument needs rings because its arrays hold coefficients that are added and multiplied, and the pages that build on this one, such as the polynomial ring, fix which arithmetic those coefficients follow.

Let $R$ be a ring. Its elements are written $a$, $b$, $c$, and for all of them:

- $a+b=b+a$ and $(a+b)+c=a+(b+c)$.
- There is a zero $0$ with $a+0=a$, and every $a$ has a negative $-a$ with $a+(-a)=0$. Together with the two addition rules, this says that addition forms a commutative group.
- $(ab)c=a(bc)$.
- $a(b+c)=ab+ac$ and $(a+b)c=ac+bc$.

The last two lines say that multiplication distributes over addition. Subtraction is defined as $a-b=a+(-b)$, so $a-b$ needs no separate axiom.

Examples the reader already knows are rings:

- The integers, with ordinary addition and multiplication. Here $-a$ is the usual negative of $a$.
- The complex numbers, with ordinary addition and multiplication.

The natural numbers $0,1,2,\dots$ are not a ring, because $3$ has no negative among them: no $x$ satisfies $3+x=0$.

Rings can behave less like the integers than one might expect. In the integers modulo $6$, which are the remainders after division by $6$, the product $2\cdot 3=6$ equals $0$ although neither factor is $0$. So the rule "a product is zero only if a factor is zero" does not hold in a general ring, and an argument may not divide by a nonzero element.

Rings with a more specific structure appear in the argument. The bit procedure's fields are <cite data-source="paper">H, D over a common residue ring</cite>, and the fast multiplication of Schönhage and Strassen <cite data-source="paper">uses roots of unity in Fermat-type residue rings</cite>, where certain multiplications become shifts.
