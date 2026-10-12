# Radix-digit convolution

!!! info "Before this page"

    Radix-digit convolution *reduces* [Exact integer multiplication](exact-integer-multiplication.md "Splitting integers into radix digits reduces Exact integer multiplication to convolution of short integer coefficients, which is where the paper starts."). Assumed known: Polynomials.

!!! abstract "Where this fits"

    - Relied on to show: The transform identity $P_s F_s = 2^{2\alpha^2} B_0 P_t F_t A$ holds with linear contractions $A$ and $B_0$, so the source permutation $P_s$ and target permutation $P_t$ stay in the formula instead of being executed as sorts. ([Transform identity with retained permutations](transform-identity.md "The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts."))

Radix-digit convolution is the rewriting of two integers as polynomials in a power of two whose coefficients are their digits, so that multiplying the integers becomes multiplying the polynomials. It is the first step of the argument, and the [Transform identity with retained permutations](transform-identity.md "The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.") acts on the coefficient lists it produces.

Splitting integers into radix digits reduces [Exact integer multiplication](exact-integer-multiplication.md "Given binary strings x and y of length n, output the 2n-bit binary representation of their product.") to convolution of short integer coefficients, which is where the paper starts.<cite class="exegenius-ref" data-source="paper" data-locator="§11 A consequence for matrix transposition, p. 3" data-quote="Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients" title="Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients"> (see §11 A consequence for matrix transposition, p. 3)</cite>

Let $b$ be the number of bits in one radix digit, so the digit base is $2^b$, and let $m$ be the number of digits in each integer. Take integers $p$ and $q$ below $2^{bm}$, and for an index $i$ from $0$ to $m-1$ let $p_i$ and $q_i$ be the $i$-th digits of $p$ and $q$, each in $\{0,\dots,2^b-1\}$. Then
$$p = \sum_{i=0}^{m-1} p_i 2^{bi}, \qquad q = \sum_{i=0}^{m-1} q_i 2^{bi}.$$

Let $X$ be an indeterminate, a symbol that is not a number. Let $P(X)$ and $Q(X)$ be the polynomials whose coefficient lists are the digits of $p$ and $q$, so that $p=P(2^b)$ and $q=Q(2^b)$.

Let $W = PQ$ be their product. Let $w_j$ be the coefficient of $X^j$ in $W$, so $w_j=\sum_i p_i q_{j-i}$, with $i$ and $j-i$ ranging over $0,\dots,m-1$. Evaluation at $2^b$ preserves products, so $pq=W(2^b)$: the integer product is the value at $2^b$ of a polynomial whose coefficients are convolutions of the digit lists.

Each $w_j$ is a sum of at most $m$ products of digits, so $w_j \le m(2^b-1)^2$ and $w_j$ has about $2b+\log_2 m$ bits. These are the short integer coefficients of the reduction.

Multiplication is thus replaced by convolving short coefficient lists, followed by carry propagation: because $w_j$ can exceed $2^b-1$, each coefficient is rewritten in base $2^b$ by carrying its excess into the next position.

For $b=2$ and $m=2$, take $p=13$ and $q=6$. Then $P(X)=1+3X$ and $Q(X)=2+X$, so $W=2+7X+3X^2$ and $W(4)=78=13\cdot 6$. The coefficient $7$ exceeds every radix-4 digit, so it is carried into the next position, giving the digits $2,3,0,1$ of $78$ from the lowest position up.

## Connections

```mermaid
flowchart LR
  n0["Exact integer multiplication"]
  click n0 href "../exact-integer-multiplication/" "Given binary strings x and y of length n, output the 2n-bit binary representation of their product."
  n1["Radix-digit convolution"]
  class n1 current
  n2["Gaussian resampling"]
  click n2 href "../gaussian-resampling/" "A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies."
  n0 --> n1
  n1 --> n2
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Gaussian resampling](gaussian-resampling.md "It replaces the transforms for the radix-digit convolution of two integers by such transforms.") *replaces the transforms for* Radix-digit convolution

??? quote "From the sources"

    > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients
    >
    > — Integer multiplication below n log n (OpenAI, 2026)
