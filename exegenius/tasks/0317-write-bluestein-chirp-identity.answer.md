Bluestein's chirp identity rewrites the [Discrete Fourier transform](discrete-fourier-transform.md) $F_q$ as a convolution multiplied by chirp factors. It reduces the transform to a [cyclic convolution](cyclic-convolution.md), so any method that computes that convolution also computes the transform. In the paper, it converts the middle transform into a [normalized cyclic convolution](normalized-cyclic-convolution.md).

The middle transform is the factor QFt in the paper's equation (35). The paper states that <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase multiplications.</cite> QFt is the Fourier transform with its output frequencies relabelled by the paper's target permutation. The paper's statement of the identity is <cite data-source="paper">Bluestein’s chirp identity converts the middle transform, including its target permutation,</cite> into normalized cyclic convolution. The paper computes convolution in later sections: <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring.</cite> So a transform rewritten as convolution can be computed by that machinery.

Throughout, $q$ is even, as the identity requires. For sequences of length $q$, $\ast$ and $\circledast$ are cyclic and normalized cyclic convolution, with indices taken modulo $q$. Here $x \bmod q$ denotes the remainder of the integer $x$ on division by $q$, the position in $\{0,\dots,q-1\}$ reached by $x$ on a cycle of $q$ positions.

Here $\tau$ is the integer position of a chirp entry, which may be negative or larger than $q-1$. The chirp is the vector $\chi$ whose entry at each integer $\tau$ is $\chi_\tau = e^{\pi i \tau^2/q}$. So $\chi = (\chi_0,\dots,\chi_{q-1})$, and every entry has modulus $1$, because $\pi\tau^2/q$ is real.

Since $(\tau+q)^2-\tau^2 = q(2\tau+q)$, we get $\chi_{\tau+q}/\chi_\tau = e^{\pi i(2\tau+q)}$. Because $q$ is even, $2\tau+q$ is even, so the ratio is $1$ and $\chi_{\tau+q}=\chi_\tau$. Hence $\chi_\tau$ depends only on $\tau \bmod q$. For odd $q$ the ratio is $-1$, so each wrapped index picks up a sign. The sum below would then be a negacyclic convolution, and the identity would need that sign change.

For integers $j$ and $\ell$, the identity $2j\ell = j^2+\ell^2-(\ell-j)^2$ gives $e^{-2\pi i j\ell/q} = \chi_{\ell-j}/(\chi_j\chi_\ell)$. Here $j$ and $\ell$ are the input and output indices of $F_q$. Write $\hat u = \frac{1}{\chi}\cdot u$, so $\hat u_j = u_j/\chi_j$. Then
$$(F_q u)_\ell = \frac{1}{\chi_\ell}\cdot\frac{1}{q}\sum_{j=0}^{q-1}\hat u_j\,\chi_{\ell-j}.$$
By periodicity $\chi_{\ell-j}=\chi_{(\ell-j)\bmod q}$, so the sum is $(\hat u\ast\chi)_\ell$. Hence
$$F_q u = \frac{1}{\chi}\cdot(\hat u\circledast\chi), \qquad \hat u = \frac{1}{\chi}\cdot u,$$
where $\cdot$ is coordinatewise multiplication. Both chirp multiplications have modulus $1$, so they change phases only. The only convolution is the middle one.

Worked example with $q=2$. Here $\chi_0=1$ and $\chi_1=e^{\pi i/2}=i$. Take $u=(1,3)$. Directly, $(F_2u)_0=(1+3)/2=2$ and $(F_2u)_1=(1-3)/2=-1$. By the identity, $\hat u = (1,\,-3i)$. Then $(\hat u\ast\chi)_0 = 1\cdot 1+(-3i)\cdot i = 4$ and $(\hat u\ast\chi)_1 = 1\cdot i+(-3i)\cdot 1 = -2i$, so $\hat u\circledast\chi = (2,\,-i)$. Multiplying by $\frac{1}{\chi} = (1,\,-i)$ gives $(2,\,-1)$, the same result.

The wrap-around is what makes the convolution cyclic. For $j>\ell$ the index $\ell-j$ is negative, and periodicity replaces $\chi_{\ell-j}$ by $\chi_{(\ell-j)\bmod q}$. The output $\ell$ is written at its own frequency label, with its factor $1/\chi_\ell$ applied there. The identity keeps the target permutation of the [transform identity with retained permutations](transform-identity.md) inside the formula, so that it is never executed as a separate sort. The paper says that <cite data-source="paper">The chirp identity below performs the frequency change in Q without applying Q as a separate permutation of the array.</cite>

The two chirp multiplications cost $O(q)$ operations, so the transform costs one cyclic convolution of length $q$ plus $O(q)$. The transform's cost bound is stated in terms of the [logarithm](logarithm.md) $\lg$ to base 2, because it is that of the convolution plus $O(q)$.

The paper credits this conversion to <cite data-source="paper">Bluestein’s conversion to convolution [4]</cite>, whose reference is <cite data-source="paper">L. I. Bluestein. A linear filtering approach to the computation of discrete Fourier transform.</cite>
