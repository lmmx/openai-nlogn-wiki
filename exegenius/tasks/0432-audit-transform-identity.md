# exegenius task 0432-audit-transform-identity

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
- Exact integer multiplication (also: exact multiplication)
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture, the conjecture)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights, Gaussian line map, Gaussian corrections, target)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Gaussian dyadics
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic)
- Centered residue
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set (also: finite set)
- Indicator vector
- Modular inverse (also: invertible modulo q, unit modulo M_i)
- Two-point kernel (also: kernel)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Opposite transform (also: opposite-sign transform)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Tensor product (also: tensor power)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Ceiling function
- Bézout's identity (also: Bezout's identity)
- Big-Theta notation
- Bijection
- Permutation
- Bit network (also: the paper's bit network)
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Family parameter
- Frequency domain
- Incidence
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Orthogonal complement
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $R$ (ring), bound on `ring`: A set with an addition and a multiplication satisfying the axioms listed on this page.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $z$ (complex number), bound on `root-of-unity`: A complex number that is tested for being a root of unity.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $w$ (pointwise product), bound on `pointwise-product`: The sequence of length $m$ whose entry at each index is the product of the entries of $u$ and $v$ at that index.
- $P$ (normalized pointwise product), bound on `pointwise-product`: The map that sends two entries to their product in the ring divided by $r$.
- $A$ (machine), bound on `running-time-cost`: The single machine whose running time the main theorem bounds.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $z$ (padded integer), bound on `exact-integer-multiplication`: A nonnegative integer with $z < 2^k$ that is written in binary.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $z$ (coefficient list), bound on `truncation`: A finite list of complex numbers, called coefficients.
- $\alpha$ (first paired value), bound on `truncation`: The first of the two values that the layer combines in each pair.
- $A$ (source set), bound on `bijection`: The source set, whose elements are the inputs of the map f.
- $B$ (target set), bound on `bijection`: The target set, whose elements are the outputs of the map f.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $w$ (target element), bound on `bijection`: An element of the target set B, which the onto condition requires to be hit by some element of A.
- $E$ (subset of source), bound on `bijection`: A subset of the source set A, whose image under a bijection is compared with the image of its complement.
- $S$ (position set), bound on `permutation`: A finite set of positions, the set whose elements a permutation rearranges.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $A$ (array), bound on `permutation`: An array of entries stored at addresses, the object that an address permutation moves.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in a record's key, which is also the number of passes.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $B$ (exceptional addresses), bound on `destination-rank`: The set of exceptional addresses, whose records the correction extracts.
- $R$ (payload bits), bound on `destination-rank`: The number of payload bits in a record.
- $R$ (polynomial ring modulo f), bound on `polynomial-ring`: The ring of classes of complex polynomials in $y$, where multiples of $f$ are zero.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $u_t$ (coefficient), bound on `polynomial-ring`: The complex coefficient of $y^t$ in the representative $u$.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $A$ (multiplication machine), bound on `little-o-notation`: The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $\gcd$ (greatest common divisor), bound on `coprime`: The function giving the largest positive integer that divides both of two integers.
- $N$ (family size), bound on `coprime`: The number of integers in the family nu_1 through nu_N.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $S$ (combined axis length), bound on `coprime`: The product s_1 through s_d, which is the length of the combined cyclic axis.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\theta$ (homomorphism), bound on `ring-homomorphism`: A map from one ring to another that preserves both operations.
- $\alpha$ (coefficient), bound on `ring-homomorphism`: The complex constant term of an element $\alpha+\delta t$ of $Q$.
- $S$ (cycle length), bound on `ring-homomorphism`: A positive integer by which the paper's cyclic ring is reduced.
- $N$ (entry count), bound on `address`: The number of entries in an array, which counts every stored entry once.
- $\alpha$ (address), bound on `address`: A string of d bits that labels one entry of the array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $F$ (field), bound on `linear-algebra-basics`: A set with addition and multiplication in which every nonzero element has a multiplicative inverse, the scalars of the vector space.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m	imes m$ matrix with entries in $F$.
- $B$ (inverse candidate), bound on `linear-algebra-basics`: A matrix that may serve as the inverse of $A$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The $m	imes m$ matrix with ones on the diagonal and zeros elsewhere.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map from one vector space over $F$ to another.
- $S$ (inverse map), bound on `linear-algebra-basics`: A linear map that serves as the inverse of a linear operator $T$ when $ST=TS=\mathrm{id}$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $\alpha$ (input weight), bound on `linear-network-frames`: The fixed weight with which a gate multiplies its input s, the same at every address.
- $\theta$ (supplied array), bound on `linear-network-frames`: The physical array supplied on an input wire.
- $T$ (three-element subsets), bound on `ground-set`: The set of all three-element subsets of $[h]$.
- $\theta$ (eigenvalue), bound on `eigenvalue`: A scalar in F for which the operator T maps some nonzero vector e to the multiple θe.
- $S$ (triple S), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, paired with T as a candidate neighbor.
- $T$ (triple T), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, whose indicator vector is discussed.
- $\Pi$ (partial permutation matrix), bound on `matrix-rank`: The matrix in the factorization with at most one 1 in each row and column and zeros elsewhere.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $\alpha$ (real part), bound on `phase-factor`: The real part of the complex number tau.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $N$ (entry count), bound on `multidimensional-transform`: The number of entries of the array, the product of the axis lengths.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $N$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $\theta$ (twiddle factor), bound on `synthetic-transforms`: The power of $\omega_N$ that multiplies one entry of a butterfly.
- $P$ (ring element), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring $R_r$, given by its representative of degree less than $r$.
- $\theta$ (second input value), bound on `butterfly`: The second of the two input values of the butterfly.
- $N$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input.
- $z$ (formal variable), bound on `radix-digit-convolution`: The indeterminate of the polynomials $P_x$ and $P_y$, which is set to $2^b$ to recover the inputs.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than $s$.
- $\alpha$ (Gaussian width), bound on `gaussian-resampling`: The integer width of the Gaussian weights.
- $\theta$ (relative gap), bound on `gaussian-resampling`: The relative gap $t/s-1$ between the two lengths.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on `gaussian-resampling`: A generic vector of length $t$, on which $P_t$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $P_s$ (source permutation), bound on `gaussian-resampling`: The coordinate permutation of length-$s$ vectors defined by $(P_s u)_j = u_{tj \bmod s}$.
- $P_t$ (resampled permutation), bound on `gaussian-resampling`: The coordinate permutation of length-$t$ vectors defined by $(P_t v)_k = v_{-sk \bmod t}$.
- $E$ (map into length t), bound on `gaussian-resampling`: A linear contraction from length-$s$ vectors to length-$t$ vectors, in the identity.
- $\Gamma$ (second resampling map), bound on `gaussian-resampling`: The other of the two maps from length-$s$ to length-$t$ vectors used in the proof.
- $N$ (near-identity map), bound on `gaussian-resampling`: A map built from $\Gamma$ and Gaussian corrections, close to the identity.
- $\chi$ (array), bound on `two-point-kernel`: An array of complex values, with one entry for each address.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}, the matrix whose tensor powers are taken.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $t$ (address bit string), bound on `tensor-product`: A bit string of length m that is an address on m coordinates.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $E$ (first argument space), bound on `bilinear-map`: The vector space containing the first argument e of the bilinear map.
- $B$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus modulo which congruence is taken.
- $\chi$ (source bank), bound on `bit-network`: The source bank, a vector with one bit for each triple.
- $E$ (vector space), bound on `bilinear-form`: A vector space over the field $F$ of scalars, on which the bilinear form is defined.
- $A$ (form matrix), bound on `bilinear-form`: The $m\times m$ matrix of the form in the chosen basis.
- $E$ (vector space), bound on `line-spanned-by-vector`: A vector space over K, containing the nonzero vector v.
- $v$ (nonzero vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $\chi$ (number of congruences), bound on `chinese-remainder-theorem`: The number of congruences in the system, a positive integer.
- $\Lambda$ (product of moduli), bound on `chinese-remainder-theorem`: The product of the moduli $\kappa_1,\dots,\kappa_\chi$, a positive integer.
- $w$ (formal variable), bound on `cyclic-convolution`: The variable whose powers index the entries of the polynomial that represents a sequence.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $N$ (input size), bound on `big-theta-notation`: The number of bits in the input, a count of its bit positions.
- $S$ (product of lengths), bound on `modular-inverse`: The product of all the axis lengths M_i.
- $\chi$ (sequence term), bound on `limit-inferior`: The $k$-th term of a sequence of real numbers.
- $k$ (term index), bound on `limit-inferior`: The position of a term in a sequence, an index counting from 1.

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

## Page to audit (`transform-identity`)

````markdown
# Transform identity with retained permutations

This identity computes its transforms by [Gaussian resampling](gaussian-resampling.md), which replaces a transform of arbitrary length by transforms whose axis lengths are powers of two. It is the resampling step of [Integer multiplication below n log n](main-theorem.md), and it keeps the two coordinate permutations inside the transform formula, so they cancel across a convolution.

The usual implementation of Gaussian resampling This identity keeps both permutations in the formula, so they need not be

The sides differ: transforms have power-of-two lengths. The identity pairs a length-$s$ transform with a length-$t$ one.

Each permutation is defined by [congruence](congruence-modulo.md) of positions: $(P_su)_j=u_{tj}$ and $(P_tw)_k=w_{-sk}$, with indices taken modulo the length, where $u$ and $w$ are complex vectors. For example, with $s=3$ and $t=5$, $P_3$ sends $u$ to $(u_0,u_2,u_1)$.

The identity depends on $s$ and $t$ being [coprime](coprime.md), making both permutations bijections. Let $\gcd(s,t)$ be the greatest common divisor. If $\gcd(s,t)=1$, Bézout's identity gives $\chi$ with $\chi t\equiv 1 \pmod s$, an inverse of $t$ modulo $s$. Then $tj\equiv tj'$ forces $j\equiv j'$, so $j\mapsto tj$ is one-to-one. Each permutation reorders entries by a [bijection](bijection.md) of positions.

The identity is built from two [linear maps](linear-algebra-basics.md): $A$ is a linear contraction from length-$s$ to length-$t$ vectors, and $B_0$ goes back (the lemma's letters). A linear map $\Psi$ is a contraction when $\|\Psi u\|\le\|u\|$, where $\|u\|$ is the largest modulus of an entry of $u$. For example, $u\mapsto(u_0+u_1)/2$ is one. Lemma 19 states:
$$P_sF_s=2^{2\alpha^2}\,B_0\,P_tF_t\,A.$$
The Gaussian identity reads that is, $TP_sF_s=P_tF_tS$. Let $\Gamma$ select the coordinates nearest $tj/s$, and let $N=\Gamma T\Lambda$, a map from length-$s$ vectors to themselves, where $\Lambda$ is a [diagonal scaling](diagonal-scaling.md).

$\|N-I\|$ is the operator norm, the largest $\|(N-I)u\|$ over $\|u\|\le1$; the source gives. $\alpha^2\theta>p/\alpha^2>1$, which is why the lemma needs $\theta>p/\alpha^4$. If $\|E\|<1$, the Neumann series $\sum_{k\ge 0}(-E)^k$ inverts $I+E$.

Put $\Upsilon=\Lambda N^{-1}\Gamma$: the proof builds its left inverse from the [diagonal scaling](diagonal-scaling.md) $\Lambda$. It is a left inverse of $T$, since $\Gamma T=N\Lambda^{-1}$ gives $\Upsilon T=\Lambda N^{-1}N\Lambda^{-1}=I$. Multiplying the Gaussian identity by $\Upsilon$ gives $P_sF_s=\Upsilon P_tF_tS$; with $A=S/2$ and $B_0=2^{-(2\alpha^2-1)}\Upsilon$, this is the identity above.

The original proof uses two [label-and-sort operations](stable-radix-sort.md), one for $P_t$ and one for $P_s^{-1}$, This identity avoids the [label-and-sort operations](stable-radix-sort.md), since $P_s$ and $P_t$ remain in the formula.

Permutations pass through pointwise products: for a coordinate permutation $\Pi$ and entrywise product $\cdot$, $(\Pi u)\cdot(\Pi w)=\Pi(u\cdot w)$, because products. The retained permutation is $R$, with $(R_cz)_j=z_{cj}$ for a unit $c$ modulo $s$ on each axis. The identity cancels its permutations through the [opposite transform](opposite-transform.md) $F_s^+$, the opposite-sign transform.. So
$$RF_s^+\big((RF_su)\cdot(RF_sv)\big)=RF_s^+R\,(F_su\cdot F_sv)=F_s^+(F_su\cdot F_sv),$$
and $R$ disappears.
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

Write the answer to `exegenius/tasks/0432-audit-transform-identity.answer.json`, then run `exegenius submit 0432-audit-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
