# Glossary

Short definitions of terms the pages use, outside the reading order.

## Primitive roots of unity { #roots-of-unity }

Let $n$ be a positive integer, the order of the root. Here $n$ has this meaning, not the bit length used on earlier pages.

A complex number $\omega$ is a primitive $n$-th root of unity if $\omega^n = 1$ and $\omega^k \neq 1$ for every integer exponent $k$ with $1 \le k < n$. Its successive powers $\omega, \omega^2, \dots$ are therefore all different until the first return to $1$, at $\omega^n$. This lets $\omega$ label the positions of a transform of length $n$: a map that combines a sequence of $n$ values by weighting each value with a power of $\omega$. The choice of root decides which values are combined.

The condition on $k$ is what separates a primitive root from an ordinary one. For $n = 4$, $i$ is primitive: $i^4 = 1$, while $i$, $i^2 = -1$ and $i^3 = -i$ are not $1$. The number $-1$ is a fourth root of unity but not a primitive one, since $(-1)^2 = 1$ already.

The condition also makes the powers distinct. Suppose $\omega^j = \omega^k$ for integer exponents $j$ and $k$ with $0 \le j < k < n$; here $j$ and $k$ are positions in the list of powers. Multiplying by $\omega^{-j}$ gives $\omega^{k-j} = 1$ with $0 < k-j < n$, which contradicts primitivity. So $1, \omega, \dots, \omega^{n-1}$ are pairwise different, and a transform of length $n$ never repeats a weight.

Used by [Discrete Fourier transform](fourier-transform.md "The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity.") and [Synthetic polynomial transform](synthetic-transform.md "A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions.").

## Matrix rank { #matrix-rank }

The rank of a matrix is the largest number of linearly independent rows, which also equals the largest number of independent columns and the number of nonzero pivots found by Gaussian elimination. The [lower-triangular factorization](lower-triangular-factorization.md "The factorization A = E₁ΠE₂ of a rational matrix into invertible lower-triangular factors and a partial permutation matrix with one 1 per pivot.") uses rank to count the ones of a partial permutation matrix, a 0-1 matrix with at most one 1 in each row and each column.

Let $A$ be a real matrix. Its rows are linearly independent when no nontrivial combination of them is the zero row, and $\operatorname{rank} A$ is the largest number of such rows. For example, the rows $(1,2)$ and $(2,4)$ have rank 1, because the second row is twice the first.

Elimination computes rank because invertible row and column operations preserve it. Reorder the rows and columns so that a nonzero entry, the pivot, sits in the top-left corner. Clearing the entries below it and to its right leaves the pivot alone, together with the smaller matrix left after deleting the pivot's row and column. Every remaining row has zero in the pivot's column, so the pivot row is independent of them and the rank drops by exactly one. Each pivot therefore lowers the remaining rank by one.<cite class="exegenius-ref" data-source="paper" data-locator="§4.1 A matrix decomposition adapted to tape order" data-quote="Each step isolates a rank-one block and leaves the remaining rank in the active submatrix" title="Each step isolates a rank-one block and leaves the remaining rank in the active submatrix"> (see §4.1 A matrix decomposition adapted to tape order)</cite>. Repeating the step until no nonzero entry is left gives $\operatorname{rank} A$ equal to the number of pivots.

Used by [Linear network with restored auxiliary values](linear-network-exchange.md "A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges.") and [Lower-triangular factorization](lower-triangular-factorization.md "The factorization A = E₁ΠE₂ of a rational matrix into invertible lower-triangular factors and a partial permutation matrix with one 1 per pivot.").

## Tensor product { #tensor-product }

??? note "Symbols from earlier pages"

    - $H_0$ — butterfly map: The two-point map sending a pair of values to its half-sum and half-difference. (on [Butterfly operation](butterfly-operation.md "The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform."))
    - $u$ — first input value: The first of the two input values that the butterfly maps. (on [Butterfly operation](butterfly-operation.md "The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform."))
    - $v$ — second input value: The second of the two input values that the butterfly maps. (on [Butterfly operation](butterfly-operation.md "The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform."))

The tensor product builds, from two vector spaces, a space on which a linear map can act on one factor alone. It lets one butterfly act on one address bit while the rest of the address is untouched.

Let $X$ and $Y$ be vector spaces over the complex numbers. The tensor product $X\otimes Y$ is a vector space whose basis consists of all pairs $\beta\otimes\gamma$, where $\beta$ is a basis vector of $X$ and $\gamma$ is a basis vector of $Y$.

Given linear maps $S$ on $X$ and $T$ on $Y$, their tensor product $S\otimes T$ is the linear map on $X\otimes Y$ determined by
$$(S\otimes T)(\beta\otimes\gamma)=S\beta\otimes T\gamma.$$
Here $S$ is a map, not the matrix bound earlier. So $S$ changes only the $X$-part of a pair.

For example, let $X=Y=\mathbb{C}^2$ with standard basis $(1,0)$, $(0,1)$. The map $H_0\otimes\mathrm{id}$ combines the [butterfly operation](butterfly-operation.md "The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform.") $H_0$ with the identity map. It sends $(1,0)\otimes(1,0)$ to $(1/2,1/2)\otimes(1,0)$, since $H_0(1,0)=(1/2,1/2)$, and leaves the second factor unchanged.

An address bit is one binary digit of an address, so it takes the value 0 or 1. An array indexed by one bit is a pair of values $(u,v)$, a vector of $\mathbb{C}^2$ as in the example, and $H_0$ acts on that pair. Let $D$ be the number of selected chunks, each contributing one selected address bit. The address set is a product of index sets, and an array on a product is the tensor product of arrays on its factors. Each selected bit therefore contributes one factor $\mathbb{C}^2$, so the layer is $H_0\otimes\cdots\otimes H_0\otimes\mathrm{id}$ with $D$ copies of $H_0$, and $\mathrm{id}$ on all other address fields, as the source's layer keeps them,<cite class="exegenius-ref" data-source="paper" data-locator="§5 Fast simultaneous synthetic butterfly layers" data-quote="preserving all other address fields" title="preserving all other address fields"> (see §5 Fast simultaneous synthetic butterfly layers)</cite>.

Used by [Simultaneous butterfly layer](simultaneous-butterfly-layer.md "A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.") and [Gaussian resampling](gaussian-resampling.md "An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.").
