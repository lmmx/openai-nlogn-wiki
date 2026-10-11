# exegenius task 0418-audit-cyclic-convolution

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
- Two-point kernel (also: kernel)
- Line spanned by a vector
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
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
- Bijection
- Permutation
- Bit network (also: the paper's bit network)
- Chinese remainder theorem (also: CRT)
- Eigenvalue
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

- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $w$ (pointwise product), bound on `pointwise-product`: The sequence of length $m$ whose entry at each index is the product of the entries of $u$ and $v$ at that index.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $\kappa$ (fixed exponent constant), bound on `running-time-cost`: A fixed constant, equal to $2^{-182}$, that sets the exponent $1-\kappa$ in the running time bound.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $f$ (map), bound on `bijection`: The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $w$ (target element), bound on `bijection`: An element of the target set B, which the onto condition requires to be hit by some element of A.
- $\pi$ (permutation), bound on `permutation`: The map from S to S that sends each position to its new position.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $\kappa$ (exponent gap), bound on `schoolbook-multiplication`: A fixed constant, $2^{-182}$, which sets the saving in the exponent $1-\kappa$ of the bound.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in a record's key, which is also the number of passes.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The monic complex polynomial whose multiples count as zero.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $\kappa$ (saving exponent), bound on `little-o-notation`: The fixed positive constant 2^{-182} in the saving exponent $1-\kappa$.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $Q$ (quotient ring), bound on `ring-homomorphism`: The ring of complex polynomials in $t$ in which $t^2=1$.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $\delta$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $t$ in an element $\alpha+\delta t$ of $Q$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $F$ (field), bound on `linear-algebra-basics`: A set with addition and multiplication in which every nonzero element has a multiplicative inverse, the scalars of the vector space.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $\varepsilon$ (routing sign), bound on `linear-network-frames`: The fixed sign by which the network multiplies the value routed from input role $\ell$.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $\tau$ (complex number), bound on `phase-factor`: A complex number written as alpha plus beta i.
- $C$ (forward kernel), bound on `phase-factor`: The 2 by 2 matrix called the forward kernel.
- $\omega$ (primitive root of unity), bound on `discrete-fourier-transform`: The primitive q-th root of unity $e^{-2\pi i/q}$, a complex number whose q-th power is 1.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $\nu$ (second input index), bound on `discrete-fourier-transform`: A second integer index from 0 to q-1 that numbers the input coordinates in the inverse identity.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $\nu$ (input position), bound on `multidimensional-transform`: A position in the input array, a tuple of D coordinates with the s-th coordinate between 0 and t_s minus 1.
- $\kappa$ (output position), bound on `multidimensional-transform`: A position in the output array, a tuple of D coordinates with the same bounds as a position in the input array.
- $\pi$ (circle constant), bound on `multidimensional-transform`: The ratio of a circle's circumference to its diameter.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $\nu_d$ (wrap count), bound on `synthetic-transforms`: The number of times a shift carries the coefficient at position $d$ past position $r-1$.
- $\delta$ (half block size), bound on `synthetic-transforms`: The number of positions in half of a block at a level, taking the values $1, 2, \dots, N/2$.
- $\tau$ (butterfly offset), bound on `synthetic-transforms`: The offset of a butterfly pair within the first half of its block, from $0$ to $\delta-1$.
- $\kappa$ (running time exponent constant), bound on `synthetic-transforms`: A fixed positive constant in the exponent of the running time bound.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\tau$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring whose positive integer power equals 1.
- $\nu$ (exponent), bound on `polynomial-ring-mod-yr-plus-1`: The positive integer power to which a root of unity is raised to give 1, counting the factors of the product.
- $\delta$ (first input value), bound on `butterfly`: The first of the two input values of the butterfly.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than $s$.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $\delta$ (Gaussian integer numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of a Gaussian dyadic $\delta/2^e$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\nu$ (second numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of the second Gaussian dyadic $\nu/2^{e'}$.
- $\tau$ (common exponent), bound on `gaussian-dyadics`: The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $\delta$ (diagonal coefficient), bound on `two-point-kernel`: The coefficient of $I$ in $K$, a complex number.
- $\kappa$ (off-diagonal coefficient), bound on `two-point-kernel`: The coefficient of $X$ in $K$, a complex number.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $\nu$ (address), bound on `two-point-kernel`: An integer whose binary form with $d$ bits is one address of an array.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $\chi$ (array), bound on `two-point-kernel`: An array of complex values, with one entry for each address.
- $Q$ (second matrix), bound on `tensor-product`: A second matrix, the right factor in the tensor product P\otimes Q.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $t$ (address bit string), bound on `tensor-product`: A bit string of length m that is an address on m coordinates.
- $f$ (function on addresses), bound on `tensor-product`: A function on addresses of m coordinates, the input that the operator transforms.
- $\pi$ (bilinear map), bound on `bilinear-map`: The map sending each pair (e,d) of arguments to a vector pi(e,d) in K, linear in each argument while the other is fixed.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\kappa$ (real input), bound on `ceiling-function`: The real number whose ceiling is taken.
- $\tau$ (processed positions), bound on `carry-propagation`: The number of low positions already processed, so that the sums run over $t < \tau$.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\nu$ (class member), bound on `congruence-modulo`: An integer congruent to d modulo B, a member of the residue class of d.
- $\delta$ (remainder), bound on `congruence-modulo`: The integer in {0,...,B-1} that is the remainder of a residue class.
- $u_j$ (input coefficient), bound on `congruence-modulo`: The input coefficient at position j of the sum being formed.
- $\tau$ (field element), bound on `binary-field`: An arbitrary element of the binary field, so it is $0$ or $1$.
- $\nu$ (bit column), bound on `binary-change-of-basis`: The column of values of the selected bits, each an element of $\mathbb F_2$.
- $\kappa$ (address), bound on `binary-change-of-basis`: A vector in $\mathbb F_2^m$, one address of the selected bits.
- $\chi$ (source bank), bound on `bit-network`: The source bank, a vector with one bit for each triple.
- $\nu$ (target bank), bound on `bit-network`: The target bank, a vector with one bit for each triple.
- $\tau$ (choice of three triples), bound on `line-spanned-by-vector`: A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $\kappa$ (modulus), bound on `centered-residue`: A positive integer, the modulus by which residues are taken.
- $\nu$ (integer to reduce), bound on `centered-residue`: The integer whose residue modulo $\kappa$ is taken.
- $\tau$ (centered residue), bound on `centered-residue`: The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\chi$ (number of congruences), bound on `chinese-remainder-theorem`: The number of congruences in the system, a positive integer.
- $\nu$ (congruence index), bound on `chinese-remainder-theorem`: An index numbering the congruences, running from 1 to $\chi$.
- $\tau$ (solution), bound on `chinese-remainder-theorem`: An unknown integer, which is a solution when it satisfies every congruence of the system.

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

## Page to audit (`cyclic-convolution`)

````markdown
# Cyclic convolution

Cyclic convolution is the product of two sequences of equal length in which an index that runs past the end wraps around to the start. The paper's algorithm for [Integer multiplication below n log n](main-theorem.md) needs it because its coefficient layout and middle transform both become cyclic convolutions.

For sequences $f = (f_0, \dots, f_{n-1})$ and $g = (g_0, \dots, g_{n-1})$, indices are read modulo $n$, so $g_{-1}$ means $g_{n-1}$. The cyclic convolution $f \ast g$ has entries

$$(f \ast g)_k = \sum_{j=0}^{n-1} f_j \, g_{(k-j) \bmod n}, \qquad 0 \le k < n,$$

where $k$ is the output position and $j$ is the position in $f$ of each summand. An index that reaches $n$ wraps back to the start. [Ordinary (linear) convolution](convolution.md), by contrast, has output length $2n-1$.

Identify $f$ with $f(w) = \sum_{j=0}^{n-1} f_j w^j$, where $w$ is a formal variable of this page. Let $\varepsilon$ be the offset of an exponent past $n$, with $0 \le \varepsilon \le n-2$. Then $f \ast g$ is the product in the [polynomial ring](polynomial-ring.md) $\mathbb{C}[w]/(w^n - 1)$: form $f(w)g(w)$, replace each power $w^{n+\varepsilon}$ by $w^\varepsilon$, and read off the coefficients. This works because $w^n = 1$ in the quotient.

Take $n = 4$, $f = (1, 2, 3, 4)$ and $g = (1, 1, 0, 0)$. Their ordinary product is $1 + 3w + 5w^2 + 7w^3 + 4w^4$. Replacing $w^4$ by $1$ gives $f \ast g = (5, 3, 5, 7)$.

The first step is the coefficient layout, which the paper motivates as:. Its model is Agarwal and Cooley's split. A cyclic convolution of length $n$ is split by the [Chinese remainder theorem](chinese-remainder-theorem.md) when $n = n_1 \cdots n_d$ with pairwise coprime $n_1, \dots, n_d$ (no common factor above 1), giving a $d$-dimensional cyclic convolution with axis $\kappa$, $1 \le \kappa \le d$, of length $n_\kappa$. The paper notes that cyclic convolution.

Pick integers $\mu_\kappa$, each invertible modulo $n_\kappa$, and let $\Phi$ send $w$ to $\prod_\kappa \nu_\kappa^{\mu_\kappa}$, where $\nu_\kappa$ is the variable of axis $\kappa$, in $\mathbb{C}[\nu_1,\dots,\nu_d]/(\nu_\kappa^{n_\kappa}-1)$. This is well defined because $(\prod_\kappa \nu_\kappa^{\mu_\kappa})^n = 1$. Then $\Phi(w^k)$ puts the coefficient at index $k$ at the array position with coordinates $\mu_\kappa k \bmod n_\kappa$. These positions are distinct for $0 \le k < n$ by the Chinese remainder theorem. The paper concludes: convolution. A ring isomorphism sends products to products, so $\Phi(f \ast g) = \Phi(f)\Phi(g)$, a product on the array, which is a cyclic convolution on each axis.

The second step is the middle transform, the factor $QFt$ in the paper's equation (35), a Fourier-type transform. The paper states that. Let $t$ be even, $\omega = e^{2\pi i/t}$, and let $F_t u$ have entries $\sum_j \omega^{jk} u_j$. From $2jk = j^2 + k^2 - (k-j)^2$ we get $\omega^{jk} = \chi_j \chi_k \tau(k-j)$, where $\chi_j = e^{\pi i j^2/t}$ and $\tau(\delta) = e^{-\pi i \delta^2/t}$. Since $t$ is even, $\tau(\delta + t) = \tau(\delta)$, so $\tau$ is a sequence of length $t$ read modulo $t$. With $\cdot$ the coordinatewise product, $F_t u = \chi \cdot \big((\chi \cdot u) \ast \tau\big)$: two pointwise phase multiplications around one cyclic convolution.
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

Write the answer to `exegenius/tasks/0418-audit-cyclic-convolution.answer.json`, then run `exegenius submit 0418-audit-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
