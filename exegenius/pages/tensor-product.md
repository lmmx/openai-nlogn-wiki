The tensor product builds, from two vector spaces, a space on which a linear map can act on one factor alone. It lets one butterfly act on one address bit while the rest of the address is untouched.

Let $X$ and $Y$ be vector spaces over the complex numbers. The tensor product $X\otimes Y$ is a vector space whose basis consists of all pairs $\beta\otimes\gamma$, where $\beta$ is a basis vector of $X$ and $\gamma$ is a basis vector of $Y$.

Given linear maps $S$ on $X$ and $T$ on $Y$, their tensor product $S\otimes T$ is the linear map on $X\otimes Y$ determined by
$$(S\otimes T)(\beta\otimes\gamma)=S\beta\otimes T\gamma.$$
Here $S$ is a map, not the matrix bound earlier. So $S$ changes only the $X$-part of a pair.

For example, let $X=Y=\mathbb{C}^2$ with standard basis $(1,0)$, $(0,1)$. The map $H_0\otimes\mathrm{id}$ combines the butterfly operation $H_0$ with the identity map. It sends $(1,0)\otimes(1,0)$ to $(1/2,1/2)\otimes(1,0)$, since $H_0(1,0)=(1/2,1/2)$, and leaves the second factor unchanged.

An address bit is one binary digit of an address, so it takes the value 0 or 1. An array indexed by one bit is a pair of values $(u,v)$, a vector of $\mathbb{C}^2$ as in the example, and $H_0$ acts on that pair. Let $D$ be the number of selected chunks, each contributing one selected address bit. The address set is a product of index sets, and an array on a product is the tensor product of arrays on its factors. Each selected bit therefore contributes one factor $\mathbb{C}^2$, so the layer is $H_0\otimes\cdots\otimes H_0\otimes\mathrm{id}$ with $D$ copies of $H_0$, and $\mathrm{id}$ on all other address fields, as the source's layer keeps them, <cite data-source="paper">preserving all other address fields</cite>.
