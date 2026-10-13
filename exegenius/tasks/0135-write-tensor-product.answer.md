The tensor product of two vector spaces is spanned by pairs of basis vectors, one from each factor. It turns one operation per factor into one linear map.

Let $E$ and $F$ be vector spaces over $\mathbb{C}$. Every $e\in E$ is a general vector of $E$, and every $f\in F$ a general vector of $F$. Let $e_1,\dots,e_p$ be a basis of $E$ and $f_1,\dots,f_q$ a basis of $F$, where $e_i$ is the $i$th basis vector of $E$, $f_j$ the $j$th of $F$, $p$ and $q$ are the numbers of basis vectors, and $1\le i\le p$, $1\le j\le q$.

A concrete model of $E\otimes F$ is the space of $p\times q$ complex arrays, where $e_i\otimes f_j$ has a single $1$ in row $i$, column $j$. These $pq$ arrays form a basis. Every $e$ is a unique combination of the $e_i$, and every $f$ of the $f_j$, so $e\otimes f$ has entry $(i,j)$ equal to $e$'s coefficient on $e_i$ times $f$'s on $f_j$. This is bilinear (linear in each factor).

Let $S$ be a linear map of $E$ and $T$ of $F$. Define $S\otimes T$ on the basis by $(S\otimes T)(e_i\otimes f_j)=Se_i\otimes Tf_j$. A linear map is fixed by its values on a basis, so this defines one map; bilinearity gives $(S\otimes T)(e\otimes f)=Se\otimes Tf$ for all $e\in E$ and $f\in F$.

For example, take $E=F=\mathbb{C}^2$, with standard bases $e_1,e_2$, and let $S=T$ satisfy $Se_1=e_1+e_2$ and $Se_2=e_1-e_2$. Then
$$(S\otimes T)(e_1\otimes e_2)=(e_1+e_2)\otimes(e_1-e_2)=e_1\otimes e_1-e_1\otimes e_2+e_2\otimes e_1-e_2\otimes e_2,$$
where the last step uses bilinearity. Two maps on two-dimensional spaces are now one map on a four-dimensional space.

Here $D$ counts the selected bits, not the address field $D$. With other bits fixed, a selected bit carries a pair $(u,v)$ in $\mathbb{C}^2$. The butterfly $H_0$ is the $2\times 2$ matrix $\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ acting on column vectors $\begin{pmatrix}u\\v\end{pmatrix}$. Applying $H_0$ to each selected bit is $H_0\otimes\cdots\otimes H_0$ with $D$ factors, one linear map rather than $D$ passes. <cite data-source="paper">The intended operation is the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits</cite>.

The tensor product of one-dimensional transforms is built from one [Discrete Fourier transform](fourier-transform.md) per axis. [Gaussian resampling](gaussian-resampling.md) uses this to express each source Fourier transform as a power-of-two tensor transform.
