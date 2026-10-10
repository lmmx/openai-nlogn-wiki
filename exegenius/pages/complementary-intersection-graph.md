Let $\mathcal{F}$ be a family of finite sets, and let $\Sigma$ be a set of integers. The intersection graph of $\mathcal{F}$ with respect to $\Sigma$ has the members of $\mathcal{F}$ as vertices, and it joins two distinct members $A$ and $B$ exactly when the size of their intersection lies in $\Sigma$, that is, when $|A \cap B| \in \Sigma$.

Its complementary intersection graph joins two distinct members exactly when $|A \cap B| \notin \Sigma$. Every pair of distinct members is an edge of exactly one of the two graphs, so each graph is the complement of the other.

For example, let $\mathcal{F} = \{\{1,2\}, \{1,3\}, \{2,3\}, \{1,4\}\}$ and $\Sigma = \{1\}$. The pairs $\{1,2\}, \{1,3\}$ and $\{1,2\}, \{2,3\}$ and $\{1,3\}, \{2,3\}$ and $\{1,2\}, \{1,4\}$ and $\{1,3\}, \{1,4\}$ all share exactly one element, so they are edges of the intersection graph. The remaining pair $\{2,3\}, \{1,4\}$ shares no element, so it is an edge of the complementary intersection graph.

The paper uses these graphs through Alon's presentation of the [Frankl–Wilson construction](frankl-wilson-construction.md), which gives low-degree polynomial representations of complementary intersection graphs over fields. The paper's subsets have three elements, and the intersection sizes it uses are $0$, $1$, $2$, and $3$.
