The tensor product combines two vector spaces into one, and the paper uses it to describe a transform layer that acts on several address bits at once. Write $P$ and $Q$ for the two spaces, over the same ground field.

The tensor product $P \otimes Q$ has as basis all pairs $e \otimes f$, where $e$ runs over a basis of $P$ and $f$ over a basis of $Q$. So the dimension of $P \otimes Q$ is the product of the two dimensions. For example, if $P$ has basis $e_1, e_2$ and $Q$ has basis $f_1, f_2, f_3$, then $P \otimes Q$ has the six basis vectors $e_i \otimes f_j$ and dimension $2 \times 3 = 6$.

A general vector of $P \otimes Q$ is not a single pair $e \otimes f$ but a sum of such pairs, with coefficients from the ground field.

Its defining property is that each [Bilinear form](bilinear-form.md) on $P$ and $Q$ becomes an ordinary linear map on $P \otimes Q$, so the tensor product linearizes it.

A tensor power $P^{\otimes 3}$ is $P \otimes P \otimes P$, with a basis of triples taking one basis vector of $P$ from each copy; it collects three copies of $P$. The paper starts a staged construction from the empty tensor product, which has no factors. <cite data-source="paper">An empty tensor product is the one-dimensional ground field</cite>.

The next page uses this to apply one two-point map to several selected address bits in a single pass.
