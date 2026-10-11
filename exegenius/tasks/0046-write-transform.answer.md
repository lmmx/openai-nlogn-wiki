A transform is a [Linear map](linear-map.md) from one array of values to another array of the same kind, each output being a fixed weighted sum of the inputs. It is the object that the identities on the next pages rewrite: each one expresses a transform of one length in terms of a transform of another length, and treating transforms as linear maps lets such rewritings be checked as compositions.

Take input coordinates $u_1, \dots, u_m$ and output coordinates $v_1, \dots, v_k$. A transform has the form

$$v_i = \sum_{j=1}^{m} a_{ij}\, u_j \qquad (1 \le i \le k),$$

where each weight $a_{ij}$ is a fixed complex number that does not depend on the input. The weights form a $k \times m$ array, and this array determines the transform.

For example, the normalized [Discrete Fourier transform](discrete-fourier-transform.md) of length $2$ has $k=m=2$ and weights $\frac{1}{\sqrt 2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, taking $\omega=-1$. Applied to $u=(1,0)$ it returns $v=\left(\frac{1}{\sqrt 2}, \frac{1}{\sqrt 2}\right)$, the first column of the weight array.
