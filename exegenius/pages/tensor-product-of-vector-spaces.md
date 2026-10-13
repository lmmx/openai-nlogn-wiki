The tensor product of vector spaces is the construction that combines spaces into one larger space whose vectors are sums of tuples of vectors, one from each factor, so that its dimension is the product of the factors' dimensions. The subset construction uses it to place a label for each triple of subsets in one ambient space, and the dimension of that space is what the later counting bounds.

Let $F$ be a vector space of dimension $\nu$, the number of vectors in a basis of $F$, and let $K\ge1$ be the number of factors. The tensor power $F^{\otimes K}$ is the vector space spanned by the pure tensors $\xi_1\otimes\cdots\otimes\xi_K$, one for each choice of vectors $\xi_1,\dots,\xi_K\in F$. The symbol $\otimes$ is linear in each slot separately:

$$(\xi+\eta)\otimes\zeta=\xi\otimes\zeta+\eta\otimes\zeta,\qquad (\lambda\xi)\otimes\zeta=\lambda(\xi\otimes\zeta),$$

and likewise in every other slot, for scalars $\lambda$. Not every element is a pure tensor. If $\phi_1,\dots,\phi_\nu$ is a basis of $F$, the $\nu^K$ products $\phi_{\mu_1}\otimes\cdots\otimes\phi_{\mu_K}$, one for each tuple $(\mu_1,\dots,\mu_K)$ with $1\le\mu_s\le\nu$, form a basis of $F^{\otimes K}$. Hence $\dim F^{\otimes K}=\nu^K$.

For example, take $\nu=K=2$. Then $F^{\otimes 2}$ has the four basis products $\phi_1\otimes\phi_1$, $\phi_1\otimes\phi_2$, $\phi_2\otimes\phi_1$ and $\phi_2\otimes\phi_2$, so its dimension is 4. The sum $\phi_1\otimes\phi_2+\phi_2\otimes\phi_1$ is not a pure tensor.

In the paper's bit network the field is $F=\mathbb Q^{h}$, where $h$ is the ground-set size (the letter $h$ changes meaning here). The label space is $F^{\otimes 3}$, of dimension $h^3$ <cite data-source="paper">m=h^3=1000000</cite>, and $h=100$ gives $10^6$.

For each three-element subset $T$ of the ground set, its indicator vector $t_T$ is the vector of $F$ with entry 1 on $T$ and 0 elsewhere. For three such subsets $T_1,T_2,T_3$, the label is the line $\langle t_{T_1}\otimes t_{T_2}\otimes t_{T_3}\rangle$ spanned by one pure tensor, so each label is a single vector in the one space $F^{\otimes 3}$.
