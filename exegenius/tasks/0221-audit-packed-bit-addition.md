# exegenius task 0221-audit-packed-bit-addition

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
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Guard-width bound
- Transform layout
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
- $\oplus$ (exclusive or), bound on `xor`: The XOR operation: $a \oplus b$ is the bitwise sum modulo 2 of the bits $a$ and $b$, which is 1 exactly when they differ.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map between vector spaces over $F$.
- $B$ (candidate inverse matrix), bound on `linear-algebra-basics`: A matrix that is a two-sided inverse of the matrix $A$ when $A$ is invertible.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $\rho$ (role permutation), bound on `linear-network-frames`: The permutation of roles that the scalar network realises, sending input role $w$ to output role $\rho(w)$.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $\rho$ (role permutation), bound on `endpoint-operator`: The signed permutation of roles realised by the scalar network, sending each input role to an output role.
- $n$ (input length), bound on `limit-inferior`: The number of bits in each input, which is the index of the running-time function.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $T$ (padded box size), bound on `cost-table`: The power of two that sets the number of cells in the padded box.
- $V$ (logical volume), bound on `cost-table`: The number of logical bits in the padded box, $V = Tp$.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $\tau$ (exchange exponent), bound on `cost-table`: A fixed rational exponent between zero and one in the cost of chunk exchanges.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array being shifted.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $\tau$ (bound exponent), bound on `address-interchange`: A fixed number below one, the exponent in the running-time bound.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $\oplus$ (XOR operator), bound on `address-interchange`: Bitwise exclusive or.
- $W$ (volume divisor), bound on `address-interchange`: The number of equal pieces the volume is cut into at each level.
- $T$ (triple), bound on `indicator-vector`: A three-element subset of the ground set $[h]$.
- $\lambda$ (scalar multiplier), bound on `line-spanned-by-vector`: A scalar in K, an element of the scalar field, used to scale v.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $\zeta$ (phase factor), bound on `phase-factor`: A complex number of modulus one, the factor multiplied into coefficients.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $a$ (numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $b$ (second numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $l$ (second denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of the second element $b/2^l$.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $X$ (input array), bound on `multidimensional-transform`: The input array, on which the transform acts.
- $T$ (second Gaussian map), bound on `gaussian-resampling`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $\zeta$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: A complex number that some positive integer power of it equals 1.
- $\xi$ (first input value), bound on `butterfly`: The first of the two values that the butterfly takes as input.
- $\eta$ (second input value), bound on `butterfly`: The second of the two values that the butterfly takes as input.
- $R$ (polynomial ring), bound on `polynomial-ring`: The quotient ring of complex polynomials in y modulo the multiples of f.
- $X$ (array of complex values), bound on `array-norm`: A finite array of complex values, the argument of the norm.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between a computed input and the exact input w.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $e$ (integer), bound on `congruence-modulo`: An integer, the other of the two integers compared by congruence.
- $g$ (packed polynomial g), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, the second input that is packed.
- $B$ (block base), bound on `signed-packing`: The base $2^{4p}$ at which the polynomials are evaluated, so that each coefficient occupies a block of $4p$ bits.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences, of length s.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $V$ (first input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the first argument of the bilinear map.
- $W$ (second input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the second argument of the bilinear map.
- $X$ (vector space), bound on `bilinear-form`: The vector space on which the bilinear form is defined.
- $\xi$ (vector), bound on `bilinear-form`: A vector of $X$.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $X$.
- $\oplus$ (direct sum), bound on `subspace-labels`: The direct sum: each vector is uniquely a vector of the first summand plus one of the second.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $X$ (bank X), bound on `subset-intersection-network`: One of the two banks of scalars, indexed by triples of triples.
- $\beta$ (bank index), bound on `subset-intersection-network`: A triple of triples that indexes one entry of a bank.
- $\xi$ (source vector), bound on `subset-intersection-network`: The vector of source-bank entries on one line, indexed by triples.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of target-bank entries on one line, indexed by triples.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $X$ (bit-flip matrix), bound on `complex-phase-network`: The matrix swapping the two coordinates of a vector.
- $\lambda$ (constant lambda), bound on `complex-phase-network`: The constant $(1+i)/2$.
- $\mu$ (constant mu), bound on `complex-phase-network`: The constant $(1-i)/2$.
- $R$ (orthogonal residual), bound on `complex-phase-network`: The subspace by which an edge's two labels differ, orthogonal to the smaller one.
- $\mathcal{B}$ (orthonormal basis), bound on `complex-phase-network`: A basis of the residual whose vectors $v$ satisfy $v\cdot v=1$ and are pairwise orthogonal.
- $\sigma$ (binary vector), bound on `complex-phase-network`: A binary vector used in the weight identity.
- $\rho$ (binary vector), bound on `complex-phase-network`: A second binary vector used in the weight identity.
- $\rho$ (selected offset), bound on `simultaneous-butterfly-layer`: The position of the selected bit within each chunk, counted from the least significant end.
- $\mu$ (first value), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair, the first input of the two-point map.
- $\nu$ (second value), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair, the second input of the two-point map.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number D of selected axes in one layer, a count of axes.
- $W$ (role count), bound on `numerical-layer`: The number of roles in the network, a count of the wire roles among which rows are distributed.
- $W$ (wire count), bound on `rank-saving-recursion`: The number of wires in the network, which is also the number of roles among which the rows are distributed.
- $\mu$ (source dimension sum), bound on `rank-saving-recursion`: The sum of the dimensions of the source labels.
- $\gamma$ (cost per volume), bound on `rank-saving-recursion`: The cost of a call at parameter $\ell$ divided by its volume.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $\eta$ (twiddle exponent), bound on `transform-round`: The exponent of y at an address, an integer taken modulo 2r.
- $\nu$ (axis index), bound on `padded-transform-box`: The index of an axis, running from 1 to d.
- $d$ (axis count), bound on `padded-transform-box`: The number of axes of the transform, the count of coordinate directions along which the data is laid out.
- $\sigma$ (digit scale), bound on `normalization-scales`: The power of two 2^{-b-2} by which each radix-2^b digit is multiplied when it is stored.
- $\lambda$ (limit variable), bound on `little-o-notation`: The real point at which both functions are evaluated, taken to infinity in the limit.
- $d$ (axis bound), bound on `guard-width-bound`: A positive integer bound $d \ge D$ on the number of selected axes.
- $\eta$ (per-level operation count), bound on `guard-width-bound`: The fixed count $64(W+m+1)^3$ of operations that a level adds beyond its $s$ child calls.
- $\beta$ (depth growth bound), bound on `guard-width-bound`: The fixed count $s+\eta$ bounding how much the depth bound grows at each recursive level.
- $\nu$ (power exponent), bound on `guard-width-bound`: The least integer $j \ge 1$ with $m^j \ge \beta$, which satisfies $\beta \le m^\nu$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $\gamma$ (second integer), bound on `coprime`: The second of the two integers whose greatest common divisor is taken, not both zero.
- $\beta$ (integer to invert), bound on `modular-inverse`: The integer whose inverse modulo $M$ is sought.
- $\mu$ (modular inverse), bound on `modular-inverse`: The integer with $\beta\mu$ congruent to $1$ modulo $M$.
- $\nu$ (multiple of the modulus), bound on `modular-inverse`: The integer with $\beta\mu - 1 = \nu M$ in a solution of the congruence.
- $\xi$ (cyclic generator), bound on `modular-inverse`: A generator of a cyclic group of order $S$, which the map sends to $\prod_i \xi_i^{\mu_i}$.
- $b$ (digit count), bound on `address-shear`: The number of radix-$q$ digits in each field, a count; the letter changes meaning from earlier pages.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges that the shear with matrix $M$ needs, equal to the rational rank of $M$.
- $d$ (current value of D), bound on `address-shear`: The value of the single field $D$ when $m = 1$.
- $i$ (row index), bound on `address-shear`: The row of a one in $\Pi$, which names an $H$ field.

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

## Page to audit (`packed-bit-addition`)

````markdown
# Packed selected-bit addition

Packed selected-bit addition adds one selected bit position across several [address chunks](address-field.md) at once, using [cyclic shifts](cyclic-shift.md) and a small deterministic correction for exceptional addresses. Packed selected-bit addition supplies the binary basis changes of the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md). Packed selected-bit addition performs its basis changes in each [transform round](transform-round.md). Packed selected-bit addition contributes one term to the [cost table](cost-table.md) of the theorem.

Packed selected-bit addition acts on two disjoint [address fields](address-field.md) of equal width, the source $\mathcal{X}$ and the target $\mathcal{W}$. Packed selected-bit addition uses its third chunk as [scratch storage](scratch-storage.md), $\mathcal{T}$, whose initial value is arbitrary and must be restored.

Each chunk has width $\lambda$ bits, cut into $\nu$ segments of $\mu$ bits, so $\lambda = \nu\mu$. Let $\rho$ be the position of the first selected bit, counted from $0$ at the least significant end. The selected bit of segment $\sigma$ is its lowest bit, at position $\rho+\sigma\mu$ for $0\le\sigma<\nu$, where $\sigma$ is a segment index. The other $\mu-1$ bits of a segment form its guard, whose value $\gamma$ lies between $0$ and $2^{\mu-1}-1$.

Packed selected-bit addition adds selected bits by [exclusive or](xor.md), so each selected bit of $\mathcal{W}$ is XORed with the selected bit of $\mathcal{X}$ in the same segment. Packed selected-bit addition updates its target chunk by controlled [cyclic shifts](cyclic-shift.md). A segment's value is $2\gamma$ plus its selected bit. For a control bit $\beta\in\{0,1\}$, a cyclic shift of $\mathcal{W}$ by $\pm 2^{\rho+\sigma\mu}$ adds $\pm 1$ to the value of segment $\sigma$, with sign $-1$ when the selected bit is $1$ and $+1$ when it is $0$. For example, with $\mu=3$, $3=011_2$ becomes $2=010_2$.

One shift cannot test the selected bit of $\mathcal{W}$, so the sign depends on it. For a segment of $\mathcal{W}$ with value $\xi$ and the corresponding segment of $\mathcal{T}$ with value $\eta$, the construction uses eight controlled updates. that have the required effect away from a small set of addresses. Here $[P]$ is $1$ when $P$ holds and $0$ otherwise, and the updates run in order (1) to (8):

$$
\begin{aligned}
(1)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 0 \pmod 2], & (2)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 0 \pmod 2],\\
(3)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 0 \pmod 2], & (4)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 0 \pmod 2],\\
(5)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 1 \pmod 2], & (6)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 1 \pmod 2],\\
(7)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 1 \pmod 2], & (8)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 1 \pmod 2].
\end{aligned}
$$

Packed selected-bit addition uses updates like the [Address shear](address-shear.md). If $\beta=1$, the parities $(\xi \bmod 2,\ \eta \bmod 2)$ run through the cycle $(00\ 01\ 10)$ under lines (1) to (4) and $(01\ 10\ 11)$ under lines (5) to (8). Together they give $(00\ 10)(01\ 11)$, which flips the parity of $\xi$ alone, and. So $\xi$ becomes $\xi+\beta(1-2(\xi \bmod 2))$..

The top selected bit is left out of this stage: temporarily. A guard with $10\le\gamma\le 2^{\mu-1}-11$ gives a segment value in $[20,\,2^\mu-21]$, so a change of size at most eight stays inside the segment. Let $\mathcal{B}$ be the set of addresses at which some guard of the first $\nu-1$ segments of $\mathcal{W}$ or $\mathcal{T}$ lies outside this range. Off $\mathcal{B}$ it gives exactly the required XORs.

Each guard has exactly twenty excluded values, $0,\dots,9$ and $2^{\mu-1}-10,\dots,2^{\mu-1}-1$:, so each guard takes each of its $2^{\mu-1}$ values equally often, and one is excluded from a fraction $20/2^{\mu-1}$ of addresses. Packed selected-bit addition bounds its exceptional set by a [union bound](union-bound.md) over the $2(\nu-1)$ guards, so $\mathcal{B}$ holds at most a fraction $80(\nu-1)/2^{\mu}$ of all addresses.

The records on $\mathcal{B}$ are corrected. over all payloads. Packed selected-bit addition is correct for every [payload](payload.md) it carries. Packed selected-bit addition computes the [destination rank](destination-rank.md) of each extracted record, its position in the final order after the move. Packed selected-bit addition sorts the extracted records by a [stable radix sort](stable-radix-sort.md) on these ranks, and reinserts each at its rank.

The top selected bit is XORed in afterwards by a two-bit permutation of the two chunks. On the pair of top selected bits, one from $\mathcal{X}$ and one from $\mathcal{W}$, the map $(a,b)\mapsto(a,\,a\oplus b)$ fixes $00$ and $01$ and swaps $10$ and $11$, so it XORs the first bit into the second. positions in $O(V)$ time.

Packed selected-bit addition exchanges its chunks by the [Address-field interchange](address-interchange.md) to bring a target chunk beside its controls. Each exchange costs $O(V\lambda^\tau)$, with $\tau$ the width exponent of the interchange, and each shift costs $O(V)$. in total.

Here $R$ is the number of bits in each record, and $\zeta=\lceil\log_2(2V)\rceil$ counts the bits of a stream position. The extra time is small relative to $V$ under, since $\zeta$ is polynomial in the family parameter, $R$ outgrows every polynomial, and $\mu$ outgrows its logarithm.
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

Write the answer to `exegenius/tasks/0221-audit-packed-bit-addition.answer.json`, then run `exegenius submit 0221-audit-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
