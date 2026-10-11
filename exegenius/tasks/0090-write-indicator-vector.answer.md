An indicator vector is the 0-1 vector that marks which elements of a [Ground set](ground-set.md) belong to a given subset. The [subset-intersection network](subset-intersection-network.md) builds its subspace assignments from the indicator vectors of three-element subsets, and the orthogonality of those vectors is what permits the assignments.

Let $h$ be the number of elements in the ground set, so that the ground set is $[h] = \{1, \dots, h\}$; the construction uses $h = 100$. Let $T$ be a three-element subset of $[h]$, called a triple. <cite data-source="paper">For a triple T let tT be its indicator vector.</cite> Its indicator vector $t_T$ has an entry $1$ in each position $i \in T$ and $0$ in every other position. Each indicator vector has one entry per element of the ground set.

For example, in the ground set $\{1, \dots, 6\}$ with $T = \{1, 2, 4\}$, the indicator vector is $t_T = (1, 1, 0, 1, 0, 0)$.

The entries lie in the scalar field of each construction. In the bit construction, <cite data-source="paper">For the bit network, let F = Qh with bilinear form</cite>, so the indicator vectors lie in $\mathbb{Q}^h$. In the complex construction, <cite data-source="paper">take instead F = Fh2 with the ordinary dot product</cite>, so they lie in $\mathbb{F}_2^h$ with the ordinary dot product.

Over $\mathbb{F}_2$, the dot product of two indicator vectors is $|S \cap T| \bmod 2$, so two triples $S$ and $T$ with no common element are orthogonal. For $T = \{1, 2, 3\}$ and $S = \{4, 5, 6\}$, $t_S \cdot t_T = 0$, while $t_T \cdot t_T = 3 = 1$ in $\mathbb{F}_2$. The network needs such orthogonality between neighboring triples: <cite data-source="paper">of the corresponding indicator vectors permits the subspace assignments.</cite>
