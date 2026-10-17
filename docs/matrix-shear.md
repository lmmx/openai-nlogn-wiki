# Matrix shear by triangular factorization

!!! info "Before this page"

    Matrix shear by triangular factorization *is carried out by* [Controlled shifts and rational scalings](controlled-shifts.md "Each lower triangular transformation of $H$ or of $D$ is carried out by Controlled shifts and rational scalings.").

!!! abstract "Where this fits"

    1. A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. — how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. ([Power-saving integer multiplication](main-result.md "A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model."))
    2. Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter. — how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). ([Recursive power saving](rank-recurrence.md "Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving."))
    3. Bit variant: two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$, although the intermediate steps form XOR combinations of data. — how: Run the bit network on the digits of the chunks: an edge whose matrix has rank $a$ costs $a$ interchanges of fields of $1/m$ the width (matrix shear), the $W$ role streams carry $1/W$ of the volume each, so the cost per unit volume satisfies $F_k\le(s/W)F_{k-1}+O(1)$; then remove the restrictions on width and rows. ([Fast address-chunk interchange](address-interchange.md "The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data."))
    4. **This page:** For a rational $m\times m$ matrix $A$ of rank $a$ and fields over $\mathbb Z/q^b\mathbb Z$, the shear $(H,D)\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.

??? note "Symbols from earlier pages"

    - $V$ — volume: The number of digits an array stores. (on [Elementary stream operations](stream-ops.md "Linear-time scans on arrays stored in lexicographic order: swapping two digits, moving a digit, splitting into streams, applying a pointwise map and merging back."))

Matrix shear by triangular factorization adds a fixed rational matrix times one group of fields to another group while spending only as many field interchanges as the matrix has rank.

Let $H=(H_1,\dots,H_m)$ and $D=(D_1,\dots,D_m)$ be two groups of fields, $H$ before $D$, where $m$ is the number of fields in each group ($m$ counts fields here; it is not an output index). Let $A$ be a rational $m\times m$ matrix. Here $q$ is a fixed odd prime, the base of the digits, not a sequence length. Here $b$ is the number of base-$q$ digits in one field, not the lowest bit of an index. Each field is a residue modulo $q^b$. Here $a$ is the rank of $A$, not an offset added to a field. The shear is $(H,D)\mapsto(H+AD,D)$. For $A$ in a fixed finite set, it can be performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work<cite class="exegenius-ref" data-source="paper" data-locator="§4.1 A matrix decomposition adapted to tape order" data-quote="can be performed with exactly $a$ interchanges of pairs of $b$-digit" title="can be performed with exactly $a$ interchanges of pairs of $b$-digit"> (see §4.1 A matrix decomposition adapted to tape order)</cite>. Lower triangular changes of coordinates are cheap, so all the rank of $A$ is pushed into a partial permutation.

## Factoring

Every such $A$ factors as $A=E_1\Pi E_2$, where $E_1,E_2$ are invertible lower triangular and $\Pi$ has exactly $a$ ones, at most one per row and column<cite class="exegenius-ref" data-source="paper" data-locator="§4.1 A matrix decomposition adapted to tape order" data-quote="Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization" title="Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"> (see §4.1 A matrix decomposition adapted to tape order)</cite>. Elimination finds it. Take the topmost nonzero row and its rightmost nonzero entry, the pivot. Right multiplication by lower triangular elementary matrices clears the row to the left of the pivot, and left multiplication by such matrices clears the column below it; scaling makes the pivot one. Delete the pivot row and column and repeat. The pivots become the ones of $\Pi$, and their number is the rank of $A$, because $E_1,E_2$ are invertible and so do not change rank.

## Reducing modulo $q^b$

Choose the factorization of every matrix in the finite set once and for all, and list the factors and the inverses of $E_1$ and $E_2$ in one finite table of rational numbers. A fraction whose denominator is not divisible by $q$ is meaningful modulo $q^b$, since that denominator is a unit there. If $q$ avoids every denominator in the table, every entry reduces modulo $q^b$, and identities such as $A=E_1\Pi E_2$ still hold, since reduction preserves sums and products. A triangular matrix is invertible exactly when its diagonal entries are units, and a fraction is a unit modulo $q^b$ when $q$ divides neither its numerator nor its denominator. Hence choose $q$ to avoid every denominator in the table and every numerator of a diagonal entry of an invertible factor, so that the identities specialise to $\mathbb Z/q^b\mathbb Z$ and the triangular factors remain invertible. Any prime larger than all nonzero numerators and denominators in the table works.

## Triangular parts

Each lower triangular transformation of $H$ or of $D$ is carried out by [Controlled shifts and rational scalings](controlled-shifts.md "Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume."). Update coordinates in descending physical order. Coordinate $i$ becomes its diagonal unit times itself plus a fixed combination of earlier coordinates, which still hold their original values. With $m$ fixed, this costs $O(V)$. Inverses are also lower triangular.

## Shearing

Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. The net effect on $H$ is $E_1(E_1^{-1}H+\Pi E_2D)=H+AD$, and $D$ is restored.

Each one of $\Pi$, in row $i$ and column $j$, calls for $H_i\gets H_i+D_j$. Do it by $D_j\gets D_j+H_i$, then interchange $(H_i,D_j)$, then $D_j\gets H_i-D_j$. The first and last updates target a later field controlled by an earlier one, so they are controlled shifts. For example, if $H_i=5$ and $D_j=3$, the pair becomes $(5,8)$, then $(8,5)$ after the interchange, then $(8,3)$.

This uses one interchange per one of $\Pi$, and $\Pi$ has $a$ ones, so exactly $a$ interchanges are used. Everything else lies within the $O(V)$ further work, so temporary tapes do not multiply the count.

## Connections

```mermaid
flowchart LR
  n0["Controlled shifts and rational scalings"]
  click n0 href "../controlled-shifts/" "Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume."
  n1["Matrix shear by triangular factorization"]
  class n1 current
  n2["Fast address-chunk interchange"]
  click n2 href "../address-interchange/" "The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data."
  n0 --> n1
  n1 --> n2
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Fast address-chunk interchange](address-interchange.md "The interchange performs each edge shear by Matrix shear by triangular factorization") *performs each edge shear by* Matrix shear by triangular factorization

??? quote "From the sources"

    > The cost of a rational matrix shear
    >
    > — [Integer multiplication below n log n (OpenAI, 2026)](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integer-multiplication-below-n-log-n-September-23-2026)

    > Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization
    >
    > — [Integer multiplication below n log n (OpenAI, 2026)](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integer-multiplication-below-n-log-n-September-23-2026)
