A linear map is a rule $L$ with two fixed sizes: $m$, the number of input coordinates, and $k$, the number of output coordinates. It takes a vector $u$ of $m$ complex numbers and returns a vector $v$ of $k$ complex numbers, written $L:\mathbb{C}^m\to\mathbb{C}^k$. It is the form of each step that the argument chains together.

The rule is linear: for vectors $u, u'$ and a number $c$, $L(u+u')=L(u)+L(u')$ and $L(cu)=cL(u)$. Equivalently, each output coordinate is a fixed weighted sum of the input coordinates. Write $u_j$ for the $j$-th input coordinate of $u$, $v_i$ for the $i$-th output coordinate of $v$, and $a_{ij}$ for the weight that output $i$ gives to input $j$. Then

$$v_i=\sum_{j=1}^{m} a_{ij}\,u_j \qquad (i=1,\dots,k).$$

The weights do not depend on $u$. The table of all $a_{ij}$ is the matrix of $L$.

For example, take $m=k=2$, and write $u_1$ and $u_2$ for the first and second coordinates of $u$. Let $a_{11}=1$, $a_{12}=2$, $a_{21}=3$ and $a_{22}=-1$ be the weights. Then $L(u)=(u_1+2u_2,\ 3u_1-u_2)$, and for $u=(1,1)$ the output is $v=(3,2)$.

Composing two linear maps gives another linear map. Its matrix is the matrix product, in which each entry is a sum of products of one row of the first matrix with one column of the second. So a chain of linear maps can be replaced by one map.
