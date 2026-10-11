A projection along a subspace is a linear map that keeps the component of a vector in one subspace and removes its component in a complementary subspace. The paper's labels are subspaces of this kind: <cite data-source="paper">A label is a nondegenerate subspace</cite> of a bilinear space, and the projection onto each label is the map used to change representation at that label. Comparing two projections on nested labels gives a rank equal to the dimension change between them.

A projection along a subspace is built from [Linear algebra basics](linear-algebra-basics.md) alone: it needs only vector spaces, subspaces and linear maps.

Let $\Psi$ be a finite-dimensional vector space over the field $F$, and let $\Xi$ be a subspace of $\Psi$. A subspace $\Upsilon$ is *complementary* to $\Xi$ when $\Xi \cap \Upsilon = \{0\}$ and $\Xi + \Upsilon = \Psi$. Then every $x \in \Psi$ splits in exactly one way as $x = x_\Xi + x_\Upsilon$ with $x_\Xi \in \Xi$ and $x_\Upsilon \in \Upsilon$: the split is unique because $\Xi \cap \Upsilon = \{0\}$. The projection onto $\Xi$ along $\Upsilon$ is the linear map $\Theta$ with $\Theta(x) = x_\Xi$.

For example, take $\Psi = \mathbb{Q}^2$, $\Xi = \mathrm{span}\{(1,0)\}$ and $\Upsilon = \mathrm{span}\{(1,1)\}$. Since $(3,5) = (-2,0) + (5,5)$ with $(-2,0) \in \Xi$ and $(5,5) = 5(1,1) \in \Upsilon$, we get $\Theta(3,5) = (-2,0)$.

$\Theta$ fixes each vector of $\Xi$ and sends each vector of $\Upsilon$ to $0$, so $\Theta(\Theta(x)) = \Theta(x)$. The map $I - \Theta$ sends $x$ to $x_\Upsilon$, so it is the projection onto $\Upsilon$ along $\Xi$.

Let $\langle\cdot,\cdot\rangle$ be a bilinear form on $\Psi$, a map linear in each argument. Assume it is nondegenerate: only $0$ is orthogonal to every vector of $\Psi$. A subspace $\Xi$ is nondegenerate when no nonzero vector of $\Xi$ is orthogonal to all of $\Xi$. Its orthogonal complement is $\Xi^\perp = \{x : \langle u,x\rangle = 0 \text{ for all } u \in \Xi\}$.

**Lemma 1.** If $\Xi$ is nondegenerate, then $\Xi \cap \Xi^\perp = \{0\}$ and $\dim \Xi^\perp = \dim \Psi - \dim \Xi$. So $\Xi^\perp$ is complementary to $\Xi$, and the projection onto $\Xi$ along $\Xi^\perp$ exists; write $\Theta_\Xi$ for it. The paper writes this map as $P_U$: <cite data-source="paper">For a nondegenerate rational subspace U ⊂ F, write PU for the projection onto U along U ⊥ .</cite>

*Proof.* $\Xi \cap \Xi^\perp = \{0\}$ is the definition of nondegeneracy. The map $x \mapsto \langle\cdot,x\rangle$ from $\Psi$ to its dual $\Psi^*$, the linear functionals on $\Psi$, is injective, so it is bijective. Restricting functionals to $\Xi$ gives a map $\Psi^* \to \Xi^*$ that is onto, and under the bijection its kernel is exactly $\Xi^\perp$. Rank plus nullity gives the dimension formula, and the dimensions then add to $\dim \Psi$ with trivial intersection, so the sum is $\Psi$. The same proof applies to any nondegenerate subspace.

**Lemma 2.** Let $\Xi \subset \Xi'$ be nondegenerate subspaces. Then $\Theta_{\Xi'} - \Theta_\Xi$ is the projection onto $T = \Xi' \cap \Xi^\perp$ along $Z = \Xi + \Xi'^\perp$, and its rank is $\dim \Xi' - \dim \Xi$.

*Proof.* Since $\Xi \subset \Xi'$, we have $\Xi'^\perp \subset \Xi^\perp$. For $t \in T$, the difference is $t - 0 = t$. For $u \in \Xi$ and for $a \in \Xi'^\perp$, both maps agree, so the difference is $0$. Thus the difference is the identity on $T$ and zero on $Z$. Lemma 1 inside $\Xi'$ gives $\dim T = \dim \Xi' - \dim \Xi$. Lemma 1 for $\Psi$ gives $\dim \Xi'^\perp = \dim \Psi - \dim \Xi'$, and $\Xi \cap \Xi'^\perp \subset \Xi' \cap \Xi'^\perp = \{0\}$, so $\dim Z = \dim \Xi + \dim \Psi - \dim \Xi'$. These dimensions sum to $\dim \Psi$. If $t = a + u \in T \cap Z$ with $a \in \Xi'^\perp$ and $u \in \Xi$, then $a = t - u \in \Xi'$, so $a \in \Xi' \cap \Xi'^\perp = \{0\}$ and $t = u \in \Xi \cap \Xi^\perp = \{0\}$. Hence $\Psi = T \oplus Z$. $\square$

The paper's letters $U$ and $V$ are $\Xi$ and $\Xi'$ here. The paper states the rank claim as: <cite data-source="paper">PV − PU is the identity on V ∩ U ⊥ and zero on its orthogonal complement.</cite> <cite data-source="paper">Its rank is dim V − dim U</cite>, which is Lemma 2.

The endpoint identity uses that $I - \Theta_\Xi$ is the projection onto $\Xi^\perp$ along $\Xi$, written $\Theta_{\Xi^\perp}$, since it fixes $\Xi^\perp$ and sends $\Xi$ to $0$. The paper's endpoint difference is <cite data-source="paper">For an input Xa the endpoint difference is PUa⊥ − (−PUa ) = Im</cite>, which is $\Theta_{\Xi^\perp} + \Theta_\Xi = I$.
