A projection along a subspace is a linear map that keeps the component of a vector in one subspace and removes its component in a complementary subspace. The paper gives one such map to each label of its network. For nested labels, the rank of the difference of two such maps is the dimension change between the labels, which prices changes of representation on [Subspace labels](subspace-labels.md).

Let $W$ be a finite-dimensional vector space over the field $F$. Let $U$ be a subspace of $W$. A subspace $Y$ is complementary to $U$ when $U \cap Y = \{0\}$ and $U + Y = W$. Every $x \in W$ splits in exactly one way as a sum of a vector of $U$ and a vector of $Y$. Write $x = x_U + x_Y$, where $x_U$ is the component of $x$ in $U$ and $x_Y$ is its component in $Y$. The split is unique since $U \cap Y = \{0\}$. The projection onto $U$ along $Y$ is the map $\Theta$ sending $x$ to $x_U$.

A projection along a subspace is built from [Linear algebra basics](linear-algebra-basics.md) alone. For example, let $W = \mathbb{Q}^2$, $U = \mathrm{span}\{(1,0)\}$ and $Y = \mathrm{span}\{(1,1)\}$. Since $(3,5) = (-2,0) + (5,5)$ with $(-2,0) \in U$ and $(5,5) \in Y$, we get $\Theta(3,5) = (-2,0)$.

$\Theta$ fixes each vector of $U$ and sends each vector of $Y$ to $0$, so $\Theta(\Theta(x)) = \Theta(x)$. The map $I - \Theta$ sends $x$ to $x_Y$, so it is the projection onto $Y$ along $U$.

Let $\langle\cdot,\cdot\rangle$ be a bilinear form on $W$, assumed nondegenerate: only $0$ is orthogonal to every vector of $W$. A subspace $U$ is nondegenerate when no nonzero vector of $U$ is orthogonal to all of $U$. Its orthogonal complement is $U^\perp = \{x : \langle u,x\rangle = 0 \text{ for all } u \in U\}$.

**Lemma 1.** If $U$ is nondegenerate, then $U \cap U^\perp = \{0\}$ and $\dim U^\perp = \dim W - \dim U$. So $U^\perp$ is complementary to $U$, and the projection onto $U$ along $U^\perp$ is defined. Write $\Theta_U$ for it. The paper writes this map as $P_U$: <cite data-source="paper">For a nondegenerate rational subspace U ⊂ F, write PU for the projection onto U along U ⊥ .</cite>

*Proof.* $U \cap U^\perp = \{0\}$ is the definition of nondegeneracy. The map $x \mapsto \langle\cdot,x\rangle$ from $W$ to its dual $W^*$ is injective, hence bijective. Restricting functionals to $U$ is onto $U^*$, with kernel $U^\perp$. Rank plus nullity gives the formula.

**Lemma 2.** Let $U \subset V$ be nondegenerate subspaces. Then $\Theta_V - \Theta_U$ is the projection onto $T = V \cap U^\perp$ along $Z = U + V^\perp$. Its rank is $\dim V - \dim U$.

*Proof.* Since $U \subset V$, $V^\perp \subset U^\perp$. On $T$ the difference is $t - 0 = t$. On $U$ and on $V^\perp$ it is zero, since both maps agree there. Lemma 1, applied inside $V$, gives $\dim T = \dim V - \dim U$. Lemma 1 for $V$ gives $\dim V^\perp = \dim W - \dim V$, and $U \cap V^\perp \subset V \cap V^\perp = \{0\}$, so $\dim Z = \dim U + \dim W - \dim V$. If $t = a + u \in T \cap Z$ with $a \in V^\perp$, $u \in U$, then $a = t - u \in V \cap V^\perp = \{0\}$, so $t = u \in U \cap U^\perp = \{0\}$. Hence $W = T \oplus Z$.

The paper states: <cite data-source="paper">PV − PU is the identity on V ∩ U ⊥ and zero on its orthogonal complement.</cite> <cite data-source="paper">Its rank is dim V − dim U</cite> follows from Lemma 2.

The endpoint identity uses that $I - \Theta_U$ is the projection onto $U^\perp$ along $U$, since it fixes $U^\perp$ and sends $U$ to $0$. Writing $P_{U^\perp} = I - P_U$, the paper's endpoint difference <cite data-source="paper">For an input Xa the endpoint difference is PUa⊥ − (−PUa ) = Im</cite> is $P_{U^\perp} + P_U = I$.
