Let $m$ be the number of input coordinates and $k$ the number of output coordinates. A linear map is a rule $L$ that takes a vector $u$ of $m$ complex numbers and returns a vector $v$ of $k$ complex numbers, written $L:\mathbb{C}^m\to\mathbb{C}^k$.

The rule is linear: for vectors $u, u'$ and a number $c$, $L(u+u')=L(u)+L(u')$ and $L(cu)=cL(u)$. Equivalently, each output coordinate is a fixed weighted sum of the input coordinates. Here $u_j$ is the $j$-th input coordinate, $v_i$ the $i$-th output coordinate, and $a_{ij}$ the weight that output $i$ gives to input $j$.

That is,

$$v_i=\sum_{j=1}^{m} a_{ij}\,u_j \qquad (i=1,\dots,k).$$

The weights do not depend on $u$. The table of all $a_{ij}$ is the matrix of $L$, and any choice of weights defines a linear map in this way.

For example, take $m=k=2$ with weights $a_{11}=1$, $a_{12}=2$, $a_{21}=3$, $a_{22}=-1$. Then $L(u)=(u_1+2u_2,\ 3u_1-u_2)$, and for $u=(1,1)$ the output is $v=(3,2)$.

Composing two linear maps gives another linear map, whose matrix is the matrix product of the two matrices. So a chain of linear maps can be replaced by a single one, which is how the argument below combines its steps.
