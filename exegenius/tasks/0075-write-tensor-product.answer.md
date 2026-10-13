The tensor product of two vector spaces is the space spanned by all pairs of basis vectors, one from each factor. It lets an operation acting on each factor separately combine into one operation on the product space.

Let $E$ and $F$ be vector spaces over the same field, with bases $e_1,\dots,e_p$ and $f_1,\dots,f_q$, where $p$ is the number of basis vectors of $E$ and $q$ is the number of basis vectors of $F$. Write $e_i$ for the $i$th basis vector of $E$ and $f_j$ for the $j$th basis vector of $F$. Their tensor product $E\otimes F$ has basis $e_i\otimes f_j$ for $1\le i\le p$ and $1\le j\le q$, so its dimension is $pq$.

Let $S$ and $T$ be linear maps of $E$ and $F$ respectively. Their tensor product $S\otimes T$ is the linear map on $E\otimes F$ determined by
$$(S\otimes T)(e\otimes f)=Se\otimes Tf \quad (e\in E,\ f\in F).$$
It applies $S$ to the first factor and $T$ to the second, independently of each other.

For example, take $E=F=\mathbb{C}^2$, with $e_1,e_2$ the standard basis of each, and let $S=T$ satisfy $Se_1=e_1+e_2$ and $Se_2=e_1-e_2$. Then
$$(S\otimes T)(e_1\otimes e_2)=(e_1+e_2)\otimes(e_1-e_2)=e_1\otimes e_1-e_1\otimes e_2+e_2\otimes e_1-e_2\otimes e_2.$$
One pair of one-dimensional operations has become one linear map on a four-dimensional space.

Here the letter $D$ counts the selected bits, not the second address field. A two-point butterfly $H_0$ sends a pair $(u,v)$ to $((u+v)/2,(u-v)/2)$. Applied to $D$ selected address bits at once, the layer is a tensor product of $D$ copies of $H_0$. The point is that $D$ separate passes over single coordinates become one linear map, which can be analysed once. <cite data-source="paper">The intended operation is the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits</cite>.

Gaussian resampling uses this form to express each source Fourier transform through a power-of-two tensor transform.
