Bluestein's chirp identity rewrites a [Discrete Fourier transform](discrete-fourier-transform.md) as a [cyclic convolution](cyclic-convolution.md) multiplied by chirp factors. It reduces the transform to a [cyclic convolution](cyclic-convolution.md), so any method that computes that convolution also computes the transform.

In the argument, this is the step that converts the middle transform, including its target permutation, into a normalized cyclic convolution. The paper states the step as <cite data-source="paper">Bluestein’s chirp identity converts the middle transform, including its target permutation,</cite> into normalized cyclic convolution. A chirp factorisation therefore turns the middle transform into a cyclic convolution, which the earlier steps already compute: <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring.</cite> The paper also says that <cite data-source="paper">The chirp identity below performs the frequency change in Q without applying</cite> the target permutation as a separate permutation of the array, so no separate sort is needed.

Let $q$ be the length of the transform: the number of entries in each input and output vector. Let $u$ be the input vector, with entries $u_0$ through $u_{q-1}$. Let $j$ be an input position and $k$ an output position, each an integer from $0$ to $q-1$. Write $F_q$ for this transform of the input vector. That is,
$$(F_q u)_k = \frac{1}{q}\sum_{j=0}^{q-1} u_j\, e^{-2\pi i jk/q}.$$

The dot $\cdot$ denotes coordinatewise multiplication of two vectors of length $q$. The star $\ast$ denotes cyclic convolution of two vectors $x$ and $y$ of length $q$. That is,
$$(x\ast y)_k = \sum_{j=0}^{q-1} x_j\, y_{(k-j) \bmod q}.$$

The chirp is the vector $a$ whose entry at each integer $m$ is $a_m = e^{\pi i m^2/q}$. Since $q$ is even, $a_{m+q} = a_m$ for every integer $m$. Indeed $(m+q)^2 - m^2 = q(2m+q)$, so $a_{m+q}/a_m = e^{\pi i (2m+q)} = 1$. Thus the index $k-j$ can be read modulo $q$ without changing $a_{k-j}$.

Since $2jk = j^2 + k^2 - (k-j)^2$, the exponential splits as
$$e^{-2\pi i jk/q} = \frac{a_{k-j}}{a_j\, a_k}.$$
Substituting this into the definition gives
$$(F_q u)_k = \frac{1}{q\,a_k}\sum_{j=0}^{q-1} \frac{u_j}{a_j}\, a_{k-j}.$$
The sum is the cyclic convolution of $(1/a)\cdot u$ with $a$, where $1/a$ is the vector with entries $1/a_m$. So the transform is
$$F_q u = \frac{1}{q}\,\Big(\frac{1}{a}\Big)\cdot\Big(\Big(\frac{1}{a}\cdot u\Big)\ast a\Big).$$
Each chirp entry has modulus $1$, so the two pointwise multiplications by $1/a$ do not change the size of any entry. The only convolution is the one in the middle.

Worked example with $q=2$. Here $a_0 = 1$ and $a_1 = e^{\pi i/2} = i$. Take $u = (1,3)$. The definition gives $(F_2 u)_0 = (1+3)/2 = 2$ and $(F_2 u)_1 = (1-3)/2 = -1$. The identity gives the same result. First, $(1/a)\cdot u = (1,\,-3i)$. Its cyclic convolution with $a = (1,i)$ has entries $1\cdot 1 + (-3i)\cdot i = 4$ at $k=0$, and $1\cdot i + (-3i)\cdot 1 = -2i$ at $k=1$. Multiplying by $\frac{1}{2}(1,\,-i)$ gives $(2,\,-1)$.

The wrap-around is essential. The index $k-j$ runs over all of $\{0,\dots,q-1\}$ modulo $q$, and the periodicity of $a$ is what makes the wrapped terms agree with $a_{k-j}$. The identity therefore produces a cyclic convolution, not a linear one. The paper credits this conversion to Bluestein: <cite data-source="paper">Bluestein’s conversion to convolution [4]</cite>.
