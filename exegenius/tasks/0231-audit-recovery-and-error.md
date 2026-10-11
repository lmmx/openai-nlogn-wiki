# exegenius task 0231-audit-recovery-and-error

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
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Chinese-remainder map (also: Agarwal–Cooley map, coefficient layout, generator)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Convolution over the polynomial ring
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Prime source lengths (also: pairwise coprime source lengths)
- Transform identity with retained permutations (also: target permutation)
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set
- Indicator vector
- Modular inverse (also: invertible modulo q)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation
- Mixed-radix digits (also: mixed-radix digit)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $b$ (input bit), bound on `xor`: The second of the two bits that an XOR combines.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map between vector spaces over $F$.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $w$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $w$ (input role), bound on `endpoint-operator`: An input role of the network, whose route starts at its source vertex.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $n$ (input length), bound on `limit-inferior`: The number of bits in each input, which is the index of the running-time function.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $T$ (padded box size), bound on `cost-table`: The power of two that sets the number of cells in the padded box.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $L$ (block length), bound on `cyclic-shift`: The number of positions in the block that a cyclic shift rotates.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set $[h]$.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $h$ (ground-set size), bound on `indicator-vector`: The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $T$ (triple), bound on `indicator-vector`: A three-element subset of the ground set $[h]$.
- $E$ (vector space), bound on `line-spanned-by-vector`: The vector space over K in which the line lies.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in each key.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $h$ (chunk index), bound on `destination-rank`: The index of one of the three address chunks, taking values 1, 2 or 3.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $a$ (numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $b$ (second numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $L$ (linear map), bound on `discrete-fourier-transform`: A generic linear map from vectors to vectors, tested for the contraction property.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $h$ (output position), bound on `multidimensional-transform`: A position in the output array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $h$ (input list), bound on `synthetic-transforms`: The list of $t$ records $(h_0,\dots,h_{t-1})$ that the transform takes as input.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $p$ (precision parameter), bound on `gaussian-resampling`: An integer precision parameter of the resampling identity.
- $L$ (forward contraction), bound on `gaussian-resampling`: A linear contraction from length-s vectors to length-t vectors.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $T$ (second Gaussian map), bound on `gaussian-resampling`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $w$ (array entry), bound on `array-norm`: A single entry of the array X, which is a complex number.
- $L$ (linear contraction map), bound on `linear-contraction`: A linear map between complex coordinate spaces, the map whose contraction property is studied on this page.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $w$ (input vector), bound on `linear-contraction`: A vector in the input space of a linear map, with m complex coordinates.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $w$ (class member), bound on `congruence-modulo`: An integer in the residue class of d modulo m.
- $g$ (packed polynomial g), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, the second input that is packed.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so that $|f_j| \le 2^p$.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $fg$, a polynomial with at most $2r-1$ coefficients $h_j$.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences, of length s.
- $w$ (formal variable), bound on `cyclic-convolution`: A formal variable in which a sequence is written as a polynomial, never evaluated.
- $w$ (second argument), bound on `bilinear-map`: A vector of W, the second argument of the bilinear map.
- $E$ (fixed bilinear space), bound on `subspace-labels`: The fixed bilinear space in which every label is a subspace.
- $x$ (address), bound on `subspace-labels`: An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $S$ (triple), bound on `subspace-labels`: A second three-element subset, used for inner products.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $x$ (address), bound on `complex-phase-network`: A binary vector in $\mathbb{F}_2^m$ at which the arrays are evaluated.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $L$ (layout permutation), bound on `transform-layout`: The explicit permutation of record addresses that places the selected bits in the required chunks.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.
- $L$ (lost dimension), bound on `rank-saving-recursion`: The total dimension lost along decreasing edges, where the head label is smaller than the tail label.
- $\gamma$ (cost per volume), bound on `rank-saving-recursion`: The cost of a call at parameter $\ell$ divided by its volume.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $p$ (fractional bit count), bound on `guard-width-bound`: The number of fractional bits each input coefficient carries, so the inputs lie on $2^{-p}\mathbb{Z}[i]$.
- $\gamma$ (second integer), bound on `coprime`: The second of the two integers whose greatest common divisor is taken, not both zero.
- $S$ (product of the lengths), bound on `modular-inverse`: The product $M_1 M_2 \cdots$ of all the lengths, the order of the cyclic group.
- $m$ (field count), bound on `address-shear`: The number of address fields in each vector, a count.
- $b$ (digit count), bound on `address-shear`: The number of radix-$q$ digits in each field, a count; the letter changes meaning from earlier pages.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges that the shear with matrix $M$ needs, equal to the rational rank of $M$.
- $h$ (current value of H), bound on `address-shear`: The value of the single field $H$ when $m = 1$.
- $i$ (row index), bound on `address-shear`: The row of a one in $\Pi$, which names an $H$ field.
- $\gamma$ (guard value), bound on `packed-bit-addition`: The integer formed by the non-selected bits of a segment, which lies between 0 and 2 to the power of mu minus 1, minus 1.
- $w$ (second vector), bound on `transform-identity`: A second complex vector of length q, paired with u in the permutation and product formulas.
- $S$ (Gaussian map S), bound on `transform-identity`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the source's resampling identity.
- $T$ (Gaussian map T), bound on `transform-identity`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the source's resampling identity.
- $L$ (left inverse of T), bound on `transform-identity`: The map Lambda N^{-1} Gamma from length-t vectors to length-s vectors, which is a left inverse of T.
- $\cdot$ (entrywise product), bound on `transform-identity`: The product of two vectors of the same length taken entry by entry.
- $m$ (chirp position), bound on `bluestein-chirp-identity`: The integer position at which a chirp entry is taken, which may be negative or exceed q-1.
- $w$ (scaled input), bound on `bluestein-chirp-identity`: The input vector u with each entry divided by the corresponding chirp entry.
- $w$ (indeterminate), bound on `ring-homomorphism`: The variable of the example ring $Q=\mathbb{C}[w]/(w^2-1)$, whose square is $1$.
- $T$ (padded box size), bound on `prime-source-lengths`: The size of the padded box, the product of the padded axis lengths.
- $w$ (short axis count), bound on `prime-source-lengths`: The number of axes padded to length u/2, a count.
- $S$ (total length), bound on `prime-source-lengths`: The product of the prime source lengths, the total number of positions.
- $h$ (summed position), bound on `carry-propagation`: The position of an already processed coefficient, running over the summation range 0 to j minus 1.
- $p$ (precision), bound on `polynomial-ring-convolution`: The number of fractional bits carried by each coefficient of a record.
- $\gamma$ (imaginary numerator of phi), bound on `polynomial-ring-convolution`: The integer polynomial $2^p$ times the imaginary parts of the coefficients of $\phi$.

## Pages in the wiki

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Address field](address-field.md)
- [Exclusive or](xor.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`recovery-and-error`)

````markdown
# Exact coefficient recovery

Exact coefficient recovery is the error analysis showing that each convolution coefficient, computed through approximate transforms, lies within one half of its true integer value, so rounding returns that integer exactly. It is the last step of the argument for exact integer multiplication: it certifies that the approximate computation yields the exact product.

## Why rounding recovers the integer

The true coefficients are integers, and distinct integers are at least $1$ apart. If a computed value $x$ satisfies $|x-m|<1/2$ for an integer $m$, every other integer is farther than $1/2$ from $x$, so $m$ is the unique nearest integer and rounding returns $m$. For example, $7.3$ rounds to $7$, while $7.6$ rounds to $8$. The goal is therefore to bound the total error of each coefficient strictly below $1/2$. unique correct coefficient, and

## Units

Each stored value keeps $p$ fractional bits, so it is a multiple of $2^{-p}$. Write $h_p = 2^{-p}$ for the size of one unit in the last place of a stored value; an error of $a$ units is an absolute error below $a\,h_p$. This analysis takes its guard widths from the [Guard-width bound](guard-width-bound.md), so each stored value is exact and only the stated truncations contribute error. The source sets $b = \lceil\log_2 n\rceil$, the number of bits in each radix digit, and so $h_p = 2^{-6b}$.

## Errors add across stages

Each stage works on values that already carry error. For a [Bilinear map](bilinear-map.md) of two approximate operands, the error of the result sums the errors of the operands, each weighted by the norm of the other. This analysis bounds the norm of every operand by one, where the norm is the [Array norm](array-norm.md), the largest modulus of an entry. An array of norm at most one lies in the unit disk, so the two errors simply add:

The operand bound holds stage by stage. The paper's margin argument then keeps each computed ring output below $0.701$, since it.

## The polynomial-ring stage

This step bounds the error of the [Convolution over the polynomial ring](polynomial-ring-convolution.md), computed from two forward transforms, a pointwise product, and an opposite transform. Here $T$ counts the entries of the [Padded transform box](padded-transform-box.md), a power of two in $[4n/b, 8n/b)$, and $L=\log_2 T$; the letter $L$ changes meaning here. The stage bound includes the error of the [Opposite transform](opposite-transform.md), which inverts the forward transform up to a known factor, and of both forward transforms. $3L+2$ units of $h_p$. The scale $T/r$ is at most $T$ because $r\ge 1$, and $L\ge 1$ gives $3L+2\le 5L$. Call this error $E_{\rm ring}$, in units of $h_p$; so $E_{\rm ring}<5TL$.

Each twist at the ends of the ring map adds an error too. This analysis bounds the error of the [Phase twist](phase-twist.md) at each end of the ring map by $4h_p$, because rounding to the grid adds for an operand of norm at most one. The complex convolution has error $E_{\rm ring}$ plus three such twists:.

## Summing the stage errors

Summing the stage errors, each in units of $h_p$, gives the total error of the coefficient. The source transform contributes an error $E_s$ in units of $h_p$, with and the products and the opposite transform together add $3E_s+2$ units. The first multiplication by $S$ then gives the scaled result with error $E_w$ units, where.

## Scaling and the final bound

Here $\gamma$ is the construction constant of the source. Both scaling multiplications act exactly on the integer [Grid numerator](grid-numerator.md) of each value, so they add no error of their own. The final scaling undoes the normalizations of the [Normalization scales](normalization-scales.md): $S$ reverses the normalization left in the first result, and $2^{2b+4}$ reverses the two input scales. The final bound divides by the product $S$ of the [Prime source lengths](prime-source-lengths.md). The bound uses the growth of $\gamma$ in the [Little-o notation](little-o-notation.md) sense: $\gamma = o(b)$.

 absolute error of each coefficient is $\frac{1}{2^{2b+4}S}\cdot 28\cdot 2^{\gamma}\,T^2L\cdot 2^{-6b}$, where $2^{-6b}=h_p$. Using $T<2^b$ and $L<b$, this is at most $448\,b\,2^{-b+\gamma}$. Since $\gamma\le b/4$ for large $n$, it is at most $448\,b\,2^{-3b/4}$, which is below $1/2$ for large $n$.

With the total error below $1/2$, the computed coefficient lies within $1/2$ of the true integer, and rounding to the nearest integer returns it exactly.
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

Write the answer to `exegenius/tasks/0231-audit-recovery-and-error.answer.json`, then run `exegenius submit 0231-audit-recovery-and-error` in the project directory. If submit rejects the answer, fix the answer and submit again.
