The tensor product of two vector spaces is a vector space built from all pairs of their basis vectors, and it is the space on which a butterfly can act on one coordinate while leaving the other untouched, which is what the target construction needs.

Let $X$ and $Y$ be vector spaces over the complex numbers. The tensor product $X\otimes Y$ is a vector space whose basis consists of all pairs $\beta\otimes\gamma$, where $\beta$ is a basis vector of $X$ and $\gamma$ is a basis vector of $Y$. Its elements are finite sums of such pairs with complex coefficients, so its dimension is the product of the dimensions of $X$ and $Y$.

Given linear maps $S$ on $X$ and $T$ on $Y$, their tensor product $S\otimes T$ is the linear map on $X\otimes Y$ determined by
$$(S\otimes T)(\beta\otimes\gamma)=S\beta\otimes T\gamma.$$
Thus $S$ changes only the $X$-part of a pair and $T$ changes only the $Y$-part. For a general element, which is a sum of pairs, $S\otimes T$ applies this rule to each pair.

For example, let $X=Y=\mathbb{C}^2$ with the standard basis $(1,0)$, $(0,1)$. The map $H_0\otimes\mathrm{id}$ is built from the butterfly operation $H_0$ and the identity map. It sends $(1,0)\otimes(1,0)$ to $H_0(1,0)\otimes(1,0)=(1/2,1/2)\otimes(1,0)$, and it leaves the second coordinate of every pair unchanged.

A butterfly layer on several address bits applies the tensor product of $H_0$ with itself, one factor for each selected bit, <cite data-source="paper">acting coefficientwise and preserving all other address fields</cite>.
