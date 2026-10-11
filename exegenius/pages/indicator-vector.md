An indicator vector is the 0-1 vector that marks which elements of a [Ground set](ground-set.md) belong to a given subset. The [subset-intersection network](subset-intersection-network.md) gives each triple a subspace label, and its construction needs the indicator vectors of neighboring triples to be orthogonal.

A *triple* is a three-element subset of $[h]$; $\mathfrak a$ and $\mathfrak b$ denote triples. The indicator vector $t_{\mathfrak a}$ has entry $1$ at each position $p \in \mathfrak a$, where $p$ is an element of $[h]$, and entry $0$ elsewhere. For $[h]=\{1,\dots,6\}$ and $\mathfrak a=\{1,2,4\}$, $t_{\mathfrak a}=(1,1,0,1,0,0)$.

Triples $\mathfrak a$ and $\mathfrak b$ are *neighbors* when the construction links them. In the bit construction, <cite data-source="paper">S, T are neighbors when |S ∩ T | = 1</cite>, so $|\mathfrak a\cap\mathfrak b|=1$. In the complex construction, <cite data-source="paper">neighbors are distinct triples with</cite> <cite data-source="paper">even intersection</cite>.

Indicator vectors are tested for orthogonality by the [bilinear form](bilinear-form.md) of each construction. Let $\mathbf 1\mathbf 1^{\top}$ denote the $h\times h$ all-ones matrix. In the bit construction, <cite data-source="paper">let F = Qh with bilinear form</cite> $\langle x,y\rangle = x^{\top}(I-\tfrac19\mathbf 1\mathbf 1^{\top})y$. Since $t_{\mathfrak a}^{\top}t_{\mathfrak b}=|\mathfrak a\cap\mathfrak b|$ and $t_{\mathfrak a}^{\top}\mathbf 1\mathbf 1^{\top}t_{\mathfrak b}=3\cdot 3=9$, the form gives $\langle t_{\mathfrak a},t_{\mathfrak b}\rangle=|\mathfrak a\cap\mathfrak b|-1$, which is $0$ for neighbors.

In the complex construction, <cite data-source="paper">take instead F = Fh2 with the ordinary dot product</cite>. So $t_{\mathfrak a}\cdot t_{\mathfrak b}=|\mathfrak a\cap\mathfrak b| \bmod 2$, which is $0$ for neighbors because their intersection is even.

Thus <cite data-source="paper">neighboring triple lines are orthogonal</cite>. Orthogonality <cite data-source="paper">of the corresponding indicator vectors permits the subspace assignments.</cite>
