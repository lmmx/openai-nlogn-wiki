# exegenius task 0404-audit-tensor-product

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: a term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication (also: exact multiplication)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights, Gaussian line map, Gaussian corrections, target)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Gaussian dyadics
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Ground set (also: finite set)
- Indicator vector
- Two-point kernel (also: kernel)
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Bijection
- Permutation
- Eigenvalue
- Incidence
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $b$ (base), bound on `logarithm`: The fixed number, greater than 1, to which the logarithm is taken.
- $y$ (positive number), bound on `logarithm`: The positive number whose logarithm to base $b$ is taken.
- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $y$ (polynomial variable), bound on `root-of-unity`: The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, which is a root of unity in that ring.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $q$ (second prime), bound on `prime-number`: A prime number different from p, used in the coprimality argument.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $y$ (indeterminate), bound on `pointwise-product`: The indeterminate of the quotient ring $\mathbb{C}[y]/(y^r+1)$ whose elements are the entries.
- $P$ (normalized pointwise product), bound on `pointwise-product`: The map that sends two entries to their product in the ring divided by $r$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary input string, of length $n$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $H$ (layer), bound on `truncation`: The operation that applies a two-point map to each pair of entries whose addresses differ in one of several selected bits, in one pass.
- $f$ (map), bound on `bijection`: The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $q$ (level ratio), bound on `mathematical-induction`: The fixed positive real ratio by which one level may multiply a bound.
- $q$ (key), bound on `stable-radix-sort`: The key of a record, a w-bit nonnegative integer written with bits q_{w-1} down to q_0.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $q$ (address before move), bound on `destination-rank`: The address of a record before the move.
- $q'$ (address after move), bound on `destination-rank`: The address of the same record after the move.
- $y$ (indeterminate), bound on `polynomial-ring`: The formal variable of the polynomials in the ring.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The monic complex polynomial whose multiples count as zero.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $y$ (polynomial variable), bound on `array-norm`: The variable of the polynomials in the ring modulo y^r + 1.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $s_i$ (source length), bound on `coprime`: The i-th of the pairwise coprime axis lengths.
- $Q$ (quotient ring), bound on `ring-homomorphism`: The ring of complex polynomials in $t$ in which $t^2=1$.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $Q'$ (target ring), bound on `ring-homomorphism`: The ring of complex polynomials in $y$ in which $y^2=-1$.
- $y$ (target indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q'$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $y$ (second vector), bound on `linear-algebra-basics`: A vector over $F$, a second arbitrary vector.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The $m	imes m$ matrix with ones on the diagonal and zeros elsewhere.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $H$ (address chunk), bound on `linear-algebra-basics`: A binary address chunk, one of the two fields of an address pair.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $H$ (first address field), bound on `linear-network-frames`: The first of two address fields, written as a vector.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $H$ (first field vector), bound on `matrix-rank`: The vector $(H_1, \ldots, H_m)$ of $m$ address fields that the shear updates.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, so it counts the entries of a vector.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $t_i$ (axis length), bound on `transform-axis`: The length of axis $i$, the number of values its coordinate takes.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $y$ (polynomial indeterminate), bound on `transform-axis`: The indeterminate of the polynomial modulo $y^s+1$; its powers serve as roots of unity on the remaining axes.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $y$ (polynomial variable), bound on `multidimensional-transform`: The variable of the polynomial that stores one coordinate of the array.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The variable of the polynomial ring $R_r$, in which $y^r$ is identified with $-1$.
- $r$ (record length), bound on `synthetic-transforms`: A power of two, the number of complex coefficients in a record.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $P$ (ring element), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring $R_r$, given by its representative of degree less than $r$.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $H_0$ (butterfly map), bound on `butterfly`: The two-point map sending a pair of values to its half-sum and half-difference.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than $s$.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.

## Pages in the wiki

- [Logarithm](logarithm.md)
- [Base-2 logarithm](base-two-logarithm.md)
- [Integer](integer.md)
- [Ring](ring.md)
- [Root of unity](root-of-unity.md)
- [Stream](stream.md)
- [Prime number](prime-number.md)
- [Pointwise product](pointwise-product.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen multiplication](schonhage-strassen.md)
- [Convolution](convolution.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Bijection](bijection.md)
- [Permutation](permutation.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Mathematical induction](mathematical-induction.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Little-o notation](little-o-notation.md)
- [Coprime](coprime.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Address](address.md)
- [Address field](address-field.md)
- [Cyclic shift](cyclic-shift.md)
- [Array](array.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Logical array](logical-array.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Incidence](incidence.md)
- [Eigenvalue](eigenvalue.md)
- [Indicator vector](indicator-vector.md)
- [Matrix rank](matrix-rank.md)
- [Phase factor](phase-factor.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Gaussian integer](gaussian-integer.md)
- [Two-point kernel](two-point-kernel.md)
- [Tensor product](tensor-product.md)
- [Bilinear map](bilinear-map.md)
- [Ceiling function](ceiling-function.md)
- [Carry propagation](carry-propagation.md)
- [Grid numerator](grid-numerator.md)
- [Congruence](congruence-modulo.md)
- [Binary field](binary-field.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Bit network](bit-network.md)
- [Bilinear form](bilinear-form.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Centered residue](centered-residue.md)
- [Chinese remainder theorem](chinese-remainder-theorem.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bézout's identity](bezout-identity.md)
- [Big-Theta notation](big-theta-notation.md)
- [Cyclic group](cyclic-group.md)
- [Modular inverse](modular-inverse.md)
- [Diagonal scaling](diagonal-scaling.md)
- [Extended real numbers](extended-reals.md)
- [Limit inferior](limit-inferior.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Family parameter](family-parameter.md)
- [Frequency domain](frequency-domain.md)
- [Opposite transform](opposite-transform.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Padded transform box](padded-transform-box.md)
- [Logical bit volume](logical-bit-volume.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Normalization scales](normalization-scales.md)
- [Independence of events](independence.md)
- [Projection along a subspace](projection-along-subspace.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Bit construction](bit-construction.md)
- [Complex phase network](complex-phase-network.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Tape procedure](tape-procedure.md)
- [Exclusive or](xor.md)
- [Bit procedure](bit-procedure.md)
- [Endpoint operator](endpoint-operator.md)
- [Address shear](address-shear.md)
- [Complex construction](complex-construction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Supremum](supremum.md)
- [Linear contraction](linear-contraction.md)
- [Guard-width bound](guard-width-bound.md)
- [Union bound](union-bound.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Telescoping identity](telescoping-identity.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`tensor-product`)

````markdown
# Tensor product

The tensor product of two matrices is the block matrix formed by scaling copies of one by the entries of the other. It lets one operator act on several address coordinates at once, which is the step the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) relies on.

The tensor product is built from matrices, the basic objects of [Linear algebra basics](linear-algebra-basics.md). Let $P=(p_{ij})$ be a matrix, with $p_{ij}$ its entry in row $i$ and column $j$, where $i$ and $j$ index rows and columns here. Let $Q$ be a second matrix (here $Q$ is a matrix, not the ring of other pages). The tensor product $P\otimes Q$, also called the Kronecker product, is the block matrix whose block in block-row $i$ and block-column $j$ is $p_{ij}Q$. Each entry of $P$ scales a full copy of $Q$.

For example, take $P=\begin{array}{rr}1&1\\1&-1\end{array}$. Then

$$P\otimes P=\begin{array}{rrrr}1&1&1&1\\1&-1&1&-1\\1&1&-1&-1\\1&-1&-1&1\end{array}.$$

Here $m$ is the number of factors in a tensor power, which is also the number of coordinates the operator acts on. The power is defined by $P^{\otimes 1}=P$ and $P^{\otimes m}=P\otimes P^{\otimes(m-1)}$. An address on $m$ coordinates is a bit string $t=(t_1,\dots,t_m)\in\{0,1\}^m$, where $t_i$ is the bit at coordinate $i$. For a function $f$ on such addresses (here $f$ is not the modulus polynomial), $P^{\otimes m}$ maps $f$ to the function whose value at an output address $s=(s_1,\dots,s_m)\in\{0,1\}^m$, with bit $s_i$ at coordinate $i$, is

$$(P^{\otimes m}f)(s)=\sum_{t\in\{0,1\}^m}\Big(\prod_{i=1}^{m}p_{s_i t_i}\Big)f(t).$$

Each factor $p_{s_i t_i}$ involves only coordinate $i$, so $P^{\otimes m}$ transforms each coordinate by $P$ independently.

The mixed-product rule turns this into a sequence of single-coordinate steps. For matrices of compatible sizes,

$$(P\otimes Q)(P'\otimes Q')=(PP')\otimes(QQ').$$

To check it, the entry in row $(a,b)$ and column $(c,d)$ of the left side is $\sum_e\sum_g p_{ae}q_{bg}\,p'_{ec}q'_{gd}=\big(\sum_e p_{ae}p'_{ec}\big)\big(\sum_g q_{bg}q'_{gd}\big)$, where $e$ and $g$ are summation indices. This is the entry of the right side. If $P$ and $Q$ are invertible, taking $P'=P^{-1}$ and $Q'=Q^{-1}$ gives $(P\otimes Q)(P^{-1}\otimes Q^{-1})=I\otimes I=I$, so $(P\otimes Q)^{-1}=P^{-1}\otimes Q^{-1}$.

Let $P_{(i)}$ apply $P$ to coordinate $i$ and the identity to the others. Repeated use of the rule gives $P_{(1)}P_{(2)}\cdots P_{(m)}=P^{\otimes m}$. So $P^{\otimes m}$ is the same as applying $P$ to coordinate 1, then to coordinate 2, and so on, one coordinate at a time.

The paper uses the same construction. On $k$ columns (its $k$ counts the columns), each frame and edge operator is It states the product rule as.

The tensor product takes its one-coordinate factor from the [two-point butterfly map](butterfly.md) $H_0$, whose matrix is $\tfrac12 P$. So a two-point operator on a selected bit is $\tfrac12 P$ acting on that bit, with the other bits left fixed. The paper states the layer as this operator on each selected bit. The whole layer is therefore the single operator $(\tfrac12 P)^{\otimes m}$, applied in one pass rather than one bit at a time.
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0404-audit-tensor-product.answer.json`, then run `exegenius submit 0404-audit-tensor-product` in the project directory. If submit rejects the answer, fix the answer and submit again.
