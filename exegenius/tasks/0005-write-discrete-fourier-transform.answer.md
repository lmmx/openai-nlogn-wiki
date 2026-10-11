The discrete Fourier transform is a linear map that sends a vector of complex numbers to another vector of the same length. It is the tool that makes convolution cheap: the transform reduces [radix-digit convolution](radix-digit-convolution.md) to pointwise products of transformed vectors, and an opposite transform brings the product back.

Here $q$ is the number of values in the vector. Here $\omega$ is a primitive $q$-th root of unity: $\omega^q=1$, and $\omega^m\neq 1$ for $0<m<q$. The input position $j$ runs from $0$ to $q-1$. The output position $k$ runs from $0$ to $q-1$. We write $F_q$ for the transform map. For a vector $u=(u_0,\dots,u_{q-1})$,

$$(F_q u)_k=\frac{1}{q}\sum_{j=0}^{q-1}\omega^{jk}u_j.$$

The opposite transform $F_q^+$ uses $\omega^{-1}$ in place of $\omega$.

For $q=2$ we have $\omega=-1$, so $F_2(3,1)=\left(\tfrac{3+1}{2},\tfrac{3-1}{2}\right)=(2,1)$.

Transforming two vectors, multiplying the results entrywise, and applying the opposite transform gives their convolution up to a fixed scalar. The paper also fixes where each transformed entry is stored, because the opposite transform reads the entries in that same order after the pointwise product.
