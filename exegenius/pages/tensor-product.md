The tensor product of two vector spaces is the space spanned by pairs of basis vectors, one from each factor, and it turns a linear map on each factor into one linear map on the product.

Let $E$ and $F$ be vector spaces over $\mathbb{C}$. Every $e\in E$ is a general vector of $E$, and every $f\in F$ a general vector of $F$. Let $e_1,\dots,e_n$ be a basis of $E$ and $f_1,\dots,f_q$ a basis of $F$, where $n$ is the number of basis vectors of $E$ (the letter changes meaning from the input length of earlier pages) and $q$ is the number of basis vectors of $F$. Here $e_i$ is the $i$th basis vector of $E$, $f_j$ the $j$th of $F$, and $1\le i\le n$, $1\le j\le q$.

A concrete model of $E\otimes F$ is the space of $n\times q$ complex arrays, tables with $n$ rows and $q$ columns, where $e_i\otimes f_j$ has a single $1$ in row $i$, column $j$ and zeros elsewhere. These $nq$ arrays form a basis. Each $e$ is a unique combination of the $e_i$, and each $f$ of the $f_j$, so $e\otimes f$ has entry $(i,j)$ equal to the coefficient of $e$ on $e_i$ times the coefficient of $f$ on $f_j$. This product is bilinear, meaning it is linear in each factor separately.

Let $L$ be a linear map of $E$ and $T$ of $F$; the letters $L$ and $T$ change meaning here. Define $L\otimes T$ on the basis by $(L\otimes T)(e_i\otimes f_j)=Le_i\otimes Tf_j$. A linear map is fixed by its values on a basis, so this defines exactly one map. Bilinearity then gives $(L\otimes T)(e\otimes f)=Le\otimes Tf$ for all $e\in E$ and $f\in F$.

For example, take $E=F=\mathbb{C}^2$ with standard bases $e_1,e_2$, and let $L=T$ satisfy $Le_1=e_1+e_2$ and $Le_2=e_1-e_2$. Then
$$(L\otimes T)(e_1\otimes e_2)=(e_1+e_2)\otimes(e_1-e_2)=e_1\otimes e_1-e_1\otimes e_2+e_2\otimes e_1-e_2\otimes e_2,$$
where the last step uses bilinearity. Two maps on two-dimensional spaces are now one map on a four-dimensional space.

Here $D$ counts the selected bits, not the address field $D$. The butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ is the $2\times 2$ matrix $\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ acting on $\begin{pmatrix}u\\v\end{pmatrix}$, and with the other bits fixed, each selected bit carries such a pair. Applying $H_0$ to every selected bit at once is the single linear map $H_0\otimes\cdots\otimes H_0$ with $D$ factors, rather than $D$ separate passes. <cite data-source="paper">The intended operation is the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits</cite>.

The tensor product of one-dimensional transforms is built from one [Discrete Fourier transform](fourier-transform.md) per axis. [Gaussian resampling](gaussian-resampling.md) uses this to express each source Fourier transform as a power-of-two tensor transform.
