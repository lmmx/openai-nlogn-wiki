# Glossary

Short definitions of terms the pages use, outside the reading order.

## Gaussian dyadics { #gaussian-dyadics }

A Gaussian dyadic is a complex number whose real and imaginary parts are integers divided by a common power of two. It is the number type in which the integer multiplication algorithm does its transform arithmetic exactly, so that rounding is needed only once, at the end.

Here $a$ and $b$ are the integer real and imaginary parts of the numerator $a + bi$, a Gaussian integer (a complex number with integer real and imaginary parts). The exponent $k$ is a non-negative integer that sets the denominator $2^k$. A Gaussian dyadic has the form

$$\frac{a + bi}{2^k}.$$

Sums and products of Gaussian dyadics are again Gaussian dyadics, since a sum can be written over a common power of two. For example,

$$\frac{1+2i}{2} \cdot \frac{3-i}{4} = \frac{(1+2i)(3-i)}{8} = \frac{5+5i}{8},$$

which has numerator $5+5i$ and exponent $k = 3$.

A butterfly layer applies the two-point map $H_0$ to pairs of coefficients whose indices differ in one selected bit, sending $u$, $v$ to $\left(\frac{u+v}{2}, \frac{u-v}{2}\right)$. If $u$ and $v$ are Gaussian dyadics, so are both outputs, since halving only raises the exponent by one.<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 3" data-quote="Intermediate values are exact Gaussian dyadics" title="Intermediate values are exact Gaussian dyadics"> (see §11 A consequence for matrix transposition, p. 3)</cite>. So no layer introduces a rounding error, and an error is never carried into a later layer.

Used by [Complex phase network](complex-phase-network.md "A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values."), [Simultaneous butterfly layer](simultaneous-butterfly-layer.md "The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time.") and [Guard-width bound](guard-width-bound.md "An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices.").

## Established O(n log n) multiplier { #established-multiplier }

The established multiplier, also called the Harvey–van der Hoeven multiplier, is a known algorithm for [exact integer multiplication](exact-integer-multiplication.md "Given binary strings x and y of length n, output the 2n-bit binary representation of their product."): it takes two binary strings and outputs their product. Here $n$ is the number of bits in each input string, so the product has $2n$ bits. The algorithm runs in $O(n\log n)$ time on a [fixed-tape machine](fixed-tape-model.md "A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input."), a Turing machine whose number of tapes does not grow with the input.

The argument needs it only as a fast product that can be treated as a black box. Its internals are not opened: the polynomial products of [signed coefficient packing](signed-packing.md "Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.") call it as an ordinary subroutine. The paper therefore does not apply its improved result to the multiplier itself, since<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 6" data-quote="they do not invoke the improved theorem recursively" title="they do not invoke the improved theorem recursively"> (see §11 A consequence for matrix transposition, p. 6)</cite>.

Used by [Signed coefficient packing](signed-packing.md "Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.").

## Bilinear form { #bilinear-form }

??? note "Symbols from earlier pages"

    - $a$ — real numerator part: The integer real part of the numerator $a + bi$ of a Gaussian dyadic. (on [Gaussian dyadics](glossary.md#gaussian-dyadics "Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer."))
    - $b$ — imaginary numerator part: The integer imaginary part of the numerator $a + bi$ of a Gaussian dyadic. (on [Gaussian dyadics](glossary.md#gaussian-dyadics "Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer."))

A bilinear form is a function of two vectors that is linear in each argument, and it is the structure on which the argument's labels are defined. Throughout, $U$ is a vector space over $\mathbb{F}_2$, so the only scalars are $0$ and $1$.

A bilinear form on $U$ is a function $B$ that takes two vectors $u, v$ of $U$ and returns a scalar $B(u,v)$, linear in each argument. Over $\mathbb{F}_2$ the scalar condition is automatic, so linearity reduces to

$$B(u+u',v)=B(u,v)+B(u',v), \qquad B(u,v+v')=B(u,v)+B(u,v').$$

The form is symmetric when $B(u,v)=B(v,u)$ for all $u$ and $v$. Two vectors are orthogonal when $B(u,v)=0$. The form is nondegenerate when no nonzero vector of $U$ is orthogonal to every vector of $U$. A subspace $W$ of $U$ is nondegenerate when no nonzero vector of $W$ is orthogonal to every vector of $W$.

For example, let $U=\mathbb{F}_2^2$ and write $u=(u_1,u_2)$ and $v=(v_1,v_2)$ for its vectors. Take $B(u,v)=u_1v_1+u_2v_2$, the dot product. A vector $(a,b)$ is orthogonal to $(1,0)$ only if $a=0$, and to $(0,1)$ only if $b=0$, so the only vector orthogonal to both is $(0,0)$ and $B$ is nondegenerate. Now take $B'(u,v)=u_1v_1$. Then $B'((0,1),v)=0$ for every $v$, so $(0,1)$ is a nonzero vector orthogonal to everything and $B'$ is degenerate.

The argument's intermediate labels are nondegenerate subspaces of one fixed bilinear space.<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 13" data-quote="A label is a nondegenerate subspace of a fixed bilinear space" title="A label is a nondegenerate subspace of a fixed bilinear space"> (see §11 A consequence for matrix transposition, p. 13)</cite>. The labels are then chosen so that changes of frame are inexpensive, as the [Subspace labels](subspace-labels.md "Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.") page explains.

Used by [Subspace labels](subspace-labels.md "Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.") and [Tensor product](glossary.md#tensor-product "The product of vector spaces, whose basis is formed by pairing basis vectors of the factors, so that a tensor power of a space collects several copies of it.").

## Tensor product { #tensor-product }

The tensor product combines two vector spaces into one, and the paper uses it to describe a transform layer that acts on several address bits at once. Write $P$ and $Q$ for the two spaces, over the same ground field.

The tensor product $P \otimes Q$ has as basis all pairs $e \otimes f$, where $e$ runs over a basis of $P$ and $f$ over a basis of $Q$. So the dimension of $P \otimes Q$ is the product of the two dimensions. For example, if $P$ has basis $e_1, e_2$ and $Q$ has basis $f_1, f_2, f_3$, then $P \otimes Q$ has the six basis vectors $e_i \otimes f_j$ and dimension $2 \times 3 = 6$.

A general vector of $P \otimes Q$ is not a single pair $e \otimes f$ but a sum of such pairs, with coefficients from the ground field.

Its defining property is that each [Bilinear form](glossary.md#bilinear-form "A function of two vectors that is linear in each argument; a form is nondegenerate when no nonzero vector is orthogonal to every vector of the space.") on $P$ and $Q$ becomes an ordinary linear map on $P \otimes Q$, so the tensor product linearizes it.

A tensor power $P^{\otimes 3}$ is $P \otimes P \otimes P$, with a basis of triples taking one basis vector of $P$ from each copy; it collects three copies of $P$. The paper starts a staged construction from the empty tensor product, which has no factors.<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 15" data-quote="An empty tensor product is the one-dimensional ground field" title="An empty tensor product is the one-dimensional ground field"> (see §11 A consequence for matrix transposition, p. 15)</cite>.

The next page uses this to apply one two-point map to several selected address bits in a single pass.

Used by [Complex phase network](complex-phase-network.md "A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values.") and [Simultaneous butterfly layer](simultaneous-butterfly-layer.md "The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time.").

## Cyclic convolution { #cyclic-convolution }

Cyclic convolution is the product of two sequences of the same length in which indices wrap around modulo that length. The argument later computes this product with transforms, so the reader needs its exact definition and a small example.

Let $a = (a_0, \dots, a_{t-1})$ and $b = (b_0,\dots,b_{t-1})$ be two sequences of complex numbers of length $t$, a positive integer. Their cyclic convolution $c = a \ast b$ is the sequence of length $t$ given by the rule below. Here $i$ and $j$ index the entries of $a$ and $b$, and $k$ indexes the entries of $c$.

$$c_k = \sum_{\substack{0 \le i,\, j \le t-1 \\ i+j \equiv k \pmod{t}}} a_i\, b_j, \qquad 0 \le k \le t-1.$$

The condition $i+j \equiv k \pmod{t}$ means that $i+j$ and $k$ leave the same remainder on division by $t$. An index sum that runs past $t-1$ therefore wraps around to the start. In ordinary (linear) convolution the term $a_i b_j$ would sit at position $i+j$, which can reach $2t-2$. In cyclic convolution it is folded back onto a position between $0$ and $t-1$.

Example: take $t=3$, $a=(1,2,3)$ and $b=(4,5,6)$. The pairs with $i+j \equiv 0 \pmod 3$ are $(0,0)$, $(1,2)$ and $(2,1)$, so $c_0 = 4 + 12 + 15 = 31$. Similarly $c_1 = 5 + 8 + 18 = 31$ and $c_2 = 6 + 10 + 12 = 28$.

The paper uses the symbol $\ast$ for this product<cite class="exegenius-ref" data-source="paper" data-locator="§1 X 2 -hk -bk zk + (-1)b zk+t/2, p. 46" data-quote="denote cyclic convolution in the displayed axes" title="denote cyclic convolution in the displayed axes"> (see §1 X 2 -hk -bk zk + (-1)b zk+t/2, p. 46)</cite>.

Used by [Discrete Fourier transform](discrete-fourier-transform.md "The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q."), [Synthetic polynomial transforms](synthetic-transforms.md "Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients."), [Bluestein's chirp identity](bluestein-chirp-identity.md "An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution."), [Transform identity with retained permutations](transform-identity.md "The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts."), [Chinese-remainder map](chinese-remainder-map.md "A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.") and [Convolution over the polynomial ring](polynomial-ring-convolution.md "The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.").
