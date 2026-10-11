A tensor product is built from one [Linear map](linear-map.md) for each coordinate, and it lets a map on a multidimensional array act on each coordinate in turn. The argument uses it to pass from one-dimensional identities to identities for arrays, with their permutations kept.

Here $i$ and $m$ index the output row and column, and $h$ and $g$ index the input row and column. Let $L$ be a linear map on vectors of length $s$ and $M$ a linear map on vectors of length $t$, with entries $L_{ih}$ (row $i$, column $h$) and $M_{mg}$ (row $m$, column $g$). The tensor product $L\otimes M$ is the linear map on arrays $u$ with $s$ rows and $t$ columns, entries $u_{hg}$, whose entry at position $(i,m)$ is

$$(L\otimes M)(u)_{im}=\sum_{h}\sum_{g} L_{ih}\,M_{mg}\,u_{hg}.$$

Applying $L\otimes M$ is the same as applying $M$ to each row of $u$ and then $L$ to each column. <cite data-source="paper">For the tensor product, apply the one-dimensional maps to one coordinate line at a time.</cite>

Take $s=t=2$, $L=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $M=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, and let $u$ have $u_{00}=1$ and all other entries $0$. Only the terms with $h=g=0$ survive, so $(L\otimes M)(u)_{im}=L_{i0}M_{m0}$. This is $1$ at $(i,m)=(0,0)$ and at $(1,0)$, and $0$ elsewhere.
