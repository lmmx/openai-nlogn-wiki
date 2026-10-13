# Glossary

Short definitions of terms the pages use, outside the reading order.

## Gaussian dyadic numbers { #gaussian-dyadic }

A Gaussian dyadic number is a complex number $z = a + bi$ whose real part $a$ and imaginary part $b$ are both dyadic rationals, that is, rationals $m/2^k$ with $m$ an integer and $k \ge 0$. Write $\mathcal{G}$ for the set of these numbers. They matter because the butterfly layer keeps its values in $\mathcal{G}$.

The butterfly layer applies a map $H_0(u,v) = ((u+v)/2, (u-v)/2)$ to pairs $u, v$ of values. A chunk is one of the equal-width blocks into which the array's addresses are divided; the layer applies $H_0$ to pairs in every chunk at once.

For Gaussian dyadics $u$ and $v$, sums and differences of their parts are dyadic, and halving raises each $k$ by one, so $H_0$ maps Gaussian dyadic pairs to Gaussian dyadic pairs. Take $u = 1 + \tfrac12 i$ and $v = \tfrac14 - i$. Then
$$\frac{u+v}{2} = \frac58 - \frac14 i, \qquad \frac{u-v}{2} = \frac38 + \frac34 i.$$

The layer's inputs are intermediate values, and these lie in $\mathcal{G}$.<cite class="exegenius-ref" data-source="paper" data-locator="§1.1 The two tape operations" data-quote="Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators." title="Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators."> (see §1.1 The two tape operations)</cite> Every output of $H_0$ is again in $\mathcal{G}$, so the layer computes exactly and rounds nothing.

Each stored part is a multiple of $2^{-p}$, where $p$ is the number of fractional bits. A truncation rounds each part toward zero to such a multiple, so it changes a part by less than $2^{-p}$.

The layer is contractive in the maximum norm: each output has size at most that of the larger input, so an error already present does not grow. The paper truncates once.<cite class="exegenius-ref" data-source="paper" data-locator="§1.1 The two tape operations" data-quote="A single truncation follows the completed contractive layer." title="A single truncation follows the completed contractive layer."> (see §1.1 The two tape operations)</cite> Starting with no error, since its inputs are exact, the layer adds none, so the total error is one truncation error.

The letters $m$, $u$ and $v$ mean what is said above only on this page; the later pages that use them give them other meanings.

Used by [Subset-intersection finite network](subset-network.md "A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2]."), [Simultaneous butterfly layer H₀](butterfly-layer.md "The map H₀(u,v) = ((u+v)/2, (u−v)/2) applied at once to a selected coordinate bit of every chunk, a two-point butterfly acting coefficientwise on polynomial records.") and [Exact recovery by rounding and carries](exact-recovery.md "Recovering the exact integer coefficients of a convolution by rounding the computed values, whose error is below one half, and then propagating carries in radix 2^b.").

## Order of an element { #order-of-element }

??? note "Symbols from earlier pages"

    - $x$ — formal variable: The formal variable whose powers index the coefficients of a list. (on [Cyclic convolution](cyclic-convolution.md "The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S."))

The order of an element $\gamma$ of a multiplicative group is the least positive integer $N$ with $\gamma^N=1$, when such $N$ exists. A multiplicative group is a set with an associative product, an identity $1$ and inverses. The argument uses the order of one element to list all of its powers.

For example, in the nonzero residues modulo $7$ under multiplication, $3$ has order $6$: its powers $3,2,6,4,5,1$ are distinct.

If $\gamma$ has order $N$, the powers $1,\gamma,\dots,\gamma^{N-1}$ are distinct. Indeed, if $\gamma^\alpha=\gamma^\beta$ with $0\le\alpha<\beta<N$, then multiplying by the inverse of $\gamma^\alpha$ gives $\gamma^{\beta-\alpha}=1$ with $0<\beta-\alpha<N$, contradicting the minimality of $N$.

Now let $\nu$ be the number of pairwise coprime lengths $s_1,\dots,s_\nu$ of the source, where $s_\eta$ is the $\eta$-th length, and let $S=\prod_\eta s_\eta$. Let $\mu_\eta$ be the inverse of $\prod_{\zeta<\eta}s_\zeta$ modulo $s_\eta$, so $\mu_\eta$ is coprime to $s_\eta$.

Let $G$ be the set of monomials $y_1^{\theta_1}\cdots y_\nu^{\theta_\nu}$ with $0\le\theta_\eta<s_\eta$ in the ring $\mathbb C[y_1,\dots,y_\nu]/(y_1^{s_1}-1,\dots,y_\nu^{s_\nu}-1)$. Multiplying monomials adds the exponents of each $y_\eta$ modulo $s_\eta$, so $G$ is a multiplicative group with $S$ elements. Put $\gamma=\prod_\eta y_\eta^{\mu_\eta}$.

Let $\rho$ be a positive integer. Then $\gamma^\rho=\prod_\eta y_\eta^{\mu_\eta\rho}$ equals $1$ exactly when $s_\eta\mid\mu_\eta\rho$ for every $\eta$. Since each $\mu_\eta$ is coprime to $s_\eta$, this means $s_\eta\mid\rho$ for every $\eta$, and since the lengths are pairwise coprime, $S\mid\rho$. So $\gamma$ has order $S$<cite class="exegenius-ref" data-source="paper" data-locator="§9.3 An explicit cyclic-convolution layout" data-quote="the image of $x$ has order $S$" title="the image of $x$ has order $S$"> (see §9.3 An explicit cyclic-convolution layout)</cite>.

Hence $\gamma^0,\dots,\gamma^{S-1}$ are $S$ distinct elements of $G$, so they list every monomial of $G$ exactly once.

The order is applied to [Cyclic convolution](cyclic-convolution.md "The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.") by sending $x^\rho$ to $\gamma^\rho$ for $0\le\rho<S$. The powers $1,x,\dots,x^{S-1}$ form a basis of $\mathbb C[x]/(x^S-1)$, so this map is a bijection between the two monomial bases.

Used by [Root of unity](roots-of-unity.md "A number whose some positive integer power equals one; here powers of y in the polynomial ring play this role.").

## Operator norm of a linear map { #operator-norm }

The operator norm of a linear map is the largest factor by which the map can stretch a vector, measured in a chosen vector norm. The argument uses it to bound how far a transform can grow its input. Because such bounds multiply along a chain of maps, the size of a composite can be controlled one stage at a time.

Let $\Phi$ be a linear map from one finite-dimensional complex vector space to another, each with a chosen vector norm $\|\cdot\|$. Write $\xi$ for a vector in the domain of $\Phi$. The operator norm of $\Phi$ is

$$\|\Phi\| = \sup\{\, \|\Phi\xi\| : \|\xi\| \le 1 \,\}.$$

So $\|\Phi\|$ is the largest value that $\|\Phi\xi\|$ takes on the unit ball $\{\xi : \|\xi\| \le 1\}$. In finite dimensions the unit ball is compact, so the supremum is attained and is a maximum.

Two facts follow from the definition. First, $\|\Phi\xi\| \le \|\Phi\|\,\|\xi\|$ for every vector $\xi$: for $\xi \ne 0$, apply the definition to $\xi/\|\xi\|$. Second, $\|\Phi\|$ is the smallest constant $c$ with $\|\Phi\xi\| \le c\|\xi\|$ for all $\xi$, so it is the sharpest bound of this form. Consequently, if $\Psi$ is a second linear map whose output can be fed into $\Phi$, then

$$\|\Phi\Psi\| \le \|\Phi\|\,\|\Psi\|,$$

since $\|\Phi\Psi\xi\| \le \|\Phi\|\,\|\Psi\xi\| \le \|\Phi\|\,\|\Psi\|\,\|\xi\|$. This is why a chain of stages can be bounded one stage at a time.

Example. Let $\Phi(\xi_1,\xi_2) = (\xi_1+\xi_2,\,0)$ on $\mathbb{C}^2$, with the maximum norm $\|\xi\| = \max_j |\xi_j|$. If $\|\xi\| \le 1$ then $|\xi_1+\xi_2| \le 2$, and $\xi=(1,1)$ attains the value 2. So $\|\Phi\| = 2$.

Used by [Gaussian resampling](gaussian-resampling.md "A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.").
