A bijection is a map that can be undone: it sends different inputs to different outputs and misses no output, so rearranging data by a bijection moves every value and loses or duplicates none. The paper relies on this in its address-field interchange and in its tape procedures, where each step is shown to be a bijection so that the stored bits are only moved.

Let $A$ and $B$ be sets, the source set $A$ and the target set $B$, and let $f\colon A\to B$ be a map that sends each element $s$ of $A$ to an element $f(s)$ of $B$. The map $f$ is a bijection when it is one-to-one and onto:

- one-to-one: if $f(s)=f(s')$ for $s,s'\in A$, then $s=s'$, so no two elements of the source go to the same target;
- onto: for every $w\in B$ there is some $s\in A$ with $f(s)=w$, so every target is hit.

Together these say that for each $w\in B$ there is exactly one $s\in A$ with $f(s)=w$. Then $f$ has an inverse $f^{-1}\colon B\to A$, which sends $w$ to that unique $s$, and $f^{-1}(f(s))=s$ for every $s\in A$.

**Example.** Take $A=B=\{0,1,2,3\}$ and $f(s)=s+1 \bmod 4$. The map sends $0\mapsto 1$, $1\mapsto 2$, $2\mapsto 3$, $3\mapsto 0$, so each target is hit exactly once and $f$ is a bijection. Its inverse subtracts $1$ modulo $4$. The map $g(s)=\lfloor s/2\rfloor$ on the same sets is not a bijection: $g(0)=g(1)=0$, so the target $0$ is hit twice, and the targets $2$ and $3$ are never hit. It has no inverse.

For finite sets, a bijection preserves complements. If $E\subseteq A$ and $f$ is a bijection, then $f(A\setminus E)=B\setminus f(E)$. This is the property the paper uses when it compares two bijections: if two bijections agree outside a set $E$, the image of $E$ is the same for both, and so each bijection maps $E$ onto itself when the other one does.

The paper applies this in two places. In the address-field interchange, each update line is checked to be a bijection of the rectangle: <cite data-source="paper">so each line is a bijection of the rectangle</cite>. Its argument then compares two such bijections, which agree outside a set of bad addresses, and uses complements to conclude that the bad set is mapped onto itself: <cite data-source="paper">Taking complements in the finite rectangle gives</cite>. In the tape procedure the map is a bijection on the padded address set, and the paper gives its inverse explicitly: <cite data-source="paper">bijection of P: for fixed controls and spectators it is a cyclic permutation of the valid target interval</cite>, and <cite data-source="paper">An inverse is explicit</cite>. Having an explicit inverse is what lets each step be undone, so that the stored data can be recovered after the step.
