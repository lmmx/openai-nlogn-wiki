# exegenius task 0444-audit-complex-phase-network

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
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Subspace labels (also: binary label)
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network, side and central wires, gather and scatter, scalar network)
- Gaussian dyadics
- Transform identity with retained permutations (also: target permutation, coordinate permutations)
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
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Opposite transform (also: opposite-sign transform)
- Padded transform box
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
- Bit construction
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Family parameter
- Frequency domain
- Incidence
- Independence of events
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Logical bit volume
- Ring
- Orthogonal complement
- Pointwise product
- Projection along a subspace
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $b$ (base), bound on `logarithm`: The fixed number, greater than 1, to which the logarithm is taken.
- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $z$ (complex number), bound on `root-of-unity`: A complex number that is tested for being a root of unity.
- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $q$ (second prime), bound on `prime-number`: A prime number different from p, used in the coprimality argument.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $w$ (pointwise product), bound on `pointwise-product`: The sequence of length $m$ whose entry at each index is the product of the entries of $u$ and $v$ at that index.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $P$ (normalized pointwise product), bound on `pointwise-product`: The map that sends two entries to their product in the ring divided by $r$.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $A$ (machine), bound on `running-time-cost`: The single machine whose running time the main theorem bounds.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $z$ (padded integer), bound on `exact-integer-multiplication`: A nonnegative integer with $z < 2^k$ that is written in binary.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $z$ (coefficient list), bound on `truncation`: A finite list of complex numbers, called coefficients.
- $H$ (layer), bound on `truncation`: The operation that applies a two-point map to each pair of entries whose addresses differ in one of several selected bits, in one pass.
- $A$ (source set), bound on `bijection`: The source set, whose elements are the inputs of the map f.
- $B$ (target set), bound on `bijection`: The target set, whose elements are the outputs of the map f.
- $f$ (map), bound on `bijection`: The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $w$ (target element), bound on `bijection`: An element of the target set B, which the onto condition requires to be hit by some element of A.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $A$ (array), bound on `permutation`: An array of entries stored at addresses, the object that an address permutation moves.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $q$ (level ratio), bound on `mathematical-induction`: The fixed positive real ratio by which one level may multiply a bound.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in a record's key, which is also the number of passes.
- $q$ (key), bound on `stable-radix-sort`: The key of a record, a w-bit nonnegative integer written with bits q_{w-1} down to q_0.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $q$ (address before move), bound on `destination-rank`: The address of a record before the move.
- $B$ (exceptional addresses), bound on `destination-rank`: The set of exceptional addresses, whose records the correction extracts.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The monic complex polynomial whose multiples count as zero.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $X$ (array), bound on `array-norm`: A finite array of complex values.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $A$ (multiplication machine), bound on `little-o-notation`: The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\delta$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $t$ in an element $\alpha+\delta t$ of $Q$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array, which the cost bound is linear in.
- $F$ (field), bound on `linear-algebra-basics`: A set with addition and multiplication in which every nonzero element has a multiplicative inverse, the scalars of the vector space.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m	imes m$ matrix with entries in $F$.
- $B$ (inverse candidate), bound on `linear-algebra-basics`: A matrix that may serve as the inverse of $A$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The $m	imes m$ matrix with ones on the diagonal and zeros elsewhere.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $H$ (address chunk), bound on `linear-algebra-basics`: A binary address chunk, one of the two fields of an address pair.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $\varepsilon$ (routing sign), bound on `linear-network-frames`: The fixed sign by which the network multiplies the value routed from input role $\ell$.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $H$ (first address field), bound on `linear-network-frames`: The first of two address fields, written as a vector.
- $V$ (operator space), bound on `eigenvalue`: The vector space on which the linear operator T acts.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $\mathbb{F}_2$ (binary field), bound on `indicator-vector`: The field with two elements, 0 and 1, in which 1+1=0.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $H$ (first field vector), bound on `matrix-rank`: The vector $(H_1, \ldots, H_m)$ of $m$ address fields that the shear updates.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $W$ (wire count), bound on `matrix-rank`: The number of wires in the network, which counts the edges that carry edge changes.
- $\tau$ (complex number), bound on `phase-factor`: A complex number written as alpha plus beta i.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $C$ (forward kernel), bound on `phase-factor`: The 2 by 2 matrix called the forward kernel.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, so it counts the entries of a vector.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $r$ (record length), bound on `synthetic-transforms`: A power of two, the number of complex coefficients in a record.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $\delta$ (half block size), bound on `synthetic-transforms`: The number of positions in half of a block at a level, taking the values $1, 2, \dots, N/2$.
- $\tau$ (butterfly offset), bound on `synthetic-transforms`: The offset of a butterfly pair within the first half of its block, from $0$ to $\delta-1$.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $P$ (ring element), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring $R_r$, given by its representative of degree less than $r$.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\tau$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring whose positive integer power equals 1.
- $\delta$ (first input value), bound on `butterfly`: The first of the two input values of the butterfly.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $z$ (formal variable), bound on `radix-digit-convolution`: The indeterminate of the polynomials $P_x$ and $P_y$, which is set to $2^b$ to recover the inputs.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than $s$.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on `gaussian-resampling`: A generic vector of length $t$, on which $P_t$ acts.
- $U$ (map back to s), bound on `gaussian-resampling`: A linear contraction from length-$t$ vectors to length-$s$ vectors, in the identity.
- $\delta$ (Gaussian integer numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of a Gaussian dyadic $\delta/2^e$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\tau$ (common exponent), bound on `gaussian-dyadics`: The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $\delta$ (diagonal coefficient), bound on `two-point-kernel`: The coefficient of $I$ in $K$, a complex number.
- $X$ (bit flip), bound on `two-point-kernel`: The $2\times 2$ matrix that interchanges the two entries of a pair.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}, the matrix whose tensor powers are taken.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $m$ (tensor power count), bound on `tensor-product`: The number of factors in a tensor power, which counts the coordinates the operator acts on.
- $t$ (address bit string), bound on `tensor-product`: A bit string of length m that is an address on m coordinates.
- $f$ (function on addresses), bound on `tensor-product`: A function on addresses of m coordinates, the input that the operator transforms.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $H$ (second argument space), bound on `bilinear-map`: The vector space containing the second argument d of the bilinear map.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\tau$ (processed positions), bound on `carry-propagation`: The number of low positions already processed, so that the sums run over $t < \tau$.
- $B$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus modulo which congruence is taken.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\delta$ (remainder), bound on `congruence-modulo`: The integer in {0,...,B-1} that is the remainder of a residue class.
- $\mathbb{F}_2$ (binary field), bound on `binary-field`: The field with the two elements $0$ and $1$, with addition given by exclusive or and multiplication by AND.
- $\tau$ (field element), bound on `binary-field`: An arbitrary element of the binary field, so it is $0$ or $1$.
- $U$ (subspace), bound on `bilinear-form`: A subspace of $E$, whose orthogonal complement is taken.
- $U^\perp$ (orthogonal complement), bound on `bilinear-form`: The set of vectors of $E$ orthogonal to every vector of $U$.
- $A$ (form matrix), bound on `bilinear-form`: The $m\times m$ matrix of the form in the chosen basis.
- $v$ (nonzero vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $\tau$ (choice of three triples), bound on `line-spanned-by-vector`: A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $\tau$ (centered residue), bound on `centered-residue`: The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\tau$ (solution), bound on `chinese-remainder-theorem`: An unknown integer, which is a solution when it satisfies every congruence of the system.
- $f$ (first input sequence), bound on `cyclic-convolution`: The first of the two sequences of length n whose cyclic convolution is taken.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences of length n whose cyclic convolution is taken.
- $w$ (formal variable), bound on `cyclic-convolution`: The variable whose powers index the entries of the polynomial that represents a sequence.
- $d$ (number of axes), bound on `cyclic-convolution`: The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $\varepsilon$ (exponent offset), bound on `cyclic-convolution`: The amount by which a reduced exponent exceeds n.
- $\tau$ (reflected chirp), bound on `cyclic-convolution`: The function tau(delta) of an integer delta, read as a sequence of length t.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $d$ (greatest common divisor), bound on `bezout-identity`: The greatest common divisor of beta and gamma, the largest positive integer dividing both.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $\tau$ (remainder), bound on `bezout-identity`: The remainder when beta is divided by e, which lies between 0 and e minus 1.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $\Theta$ (Big-Theta), bound on `big-theta-notation`: The notation stating that $u$ and $h$ have the same order up to constant factors for large inputs.
- $\tau$ (generator), bound on `cyclic-group`: A fixed element of the group; its powers give every element of the cyclic group $C_\kappa$.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $\tau$ (real number), bound on `extended-reals`: A generic real number, used when the order and arithmetic of the extended reals are stated.
- $C$ (set of extended reals), bound on `extended-reals`: An arbitrary set of extended real numbers, whose infimum and supremum are taken.
- $\delta$ (sequence position), bound on `extended-reals`: The position of a term in a sequence of extended real numbers, running over 1, 2, 3, and so on.
- $m$ (tail start position), bound on `limit-inferior`: The position from which the tail of a sequence starts.
- $\varepsilon$ (positive tolerance), bound on `limit-inferior`: A positive real number used as a tolerance in a limit criterion.
- $C$ (bound constant), bound on `limit-inferior`: A constant in the big-O time bound of the main result.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers, a count of bits.
- $\tau$ (family parameter), bound on `family-parameter`: The index of a member of the family: a nonnegative integer that selects which construction is built and so fixes its size.
- $f$ (disk-grid ring array), bound on `opposite-transform`: One of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $g$ (second disk-grid ring array), bound on `opposite-transform`: The second of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $A$ (forward contraction), bound on `transform-identity`: A linear contraction from length-$s$ vectors to length-$t$ vectors.
- $w$ (complex vector), bound on `transform-identity`: A complex vector, the argument of the permutation $P_t$ in this page's notation.
- $s$ (sequence length), bound on `normalized-cyclic-convolution`: The number of entries in each input sequence, which is also the length of the transform.
- $\tau$ (chirp position), bound on `bluestein-chirp-identity`: The integer position of a chirp entry, which may be negative or larger than q-1.
- $\bmod$ (remainder modulo q), bound on `bluestein-chirp-identity`: x mod q is the remainder of the integer x on division by q, a position in {0,...,q-1}.
- $\delta$ (first digit array), bound on `normalization-scales`: The integer digit array of the first input, whose entries lie between $0$ and $2^b-1$.
- $\Theta$ (projection along C), bound on `projection-along-subspace`: The map sending each vector $x$ of $X$ to its component $x_U$ in $U$, for the chosen $U$ and $C$.
- $C$ (complementary subspace), bound on `projection-along-subspace`: A subspace of $X$ that meets $U$ only in zero and whose sum with $U$ is all of $X$.
- $C_U$ (frame of a label), bound on `subspace-labels`: The invertible operator on arrays attached to a vertex whose label is $U$, the change of representation at that vertex.
- $P_U$ (label projection), bound on `subspace-labels`: The projection onto the binary label $U$ along $U^\perp$, computed over $\mathbb F_2$.
- $\mathrm{wt}$ (Hamming weight), bound on `subspace-labels`: The number of ones in a binary vector, computed as an integer.
- $H$ (Hadamard matrix), bound on `subspace-labels`: The $2\times 2$ matrix with entries $\pm 1/\sqrt2$ that defines the frame $C_U$ through its tensor powers.
- $\tau$ (kernel coefficient tau), bound on `subspace-labels`: The first Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $\delta$ (kernel coefficient delta), bound on `subspace-labels`: The second Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $X_v$ (translation operator), bound on `subspace-labels`: The operator that shifts a function of addresses by the vector $v$, so that $(X_vf)(x)=f(x+v)$.
- $v$ (shift vector), bound on `subspace-labels`: A vector in $\mathbb F_2^m$ by which a translation shifts addresses (this letter changes meaning on this page).
- $f$ (function of addresses), bound on `subspace-labels`: A function from addresses in $\mathbb F_2^m$ to values, which a translation shifts (this letter changes meaning on this page).
- $X$ (bank X), bound on `subset-intersection-network`: One of the two banks of scalars, with entries $X_\tau$ indexed by triples of triples.
- $\tau$ (bank index), bound on `subset-intersection-network`: A triple of triples, indexing the entries of a bank.
- $\delta$ (vector of E), bound on `subset-intersection-network`: A vector of the ambient space $E=\mathbb Q^h$, an argument of the bit network form.

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

## Page to audit (`complex-phase-network`)

````markdown
# Complex phase network

The complex phase network is built on the [subset-intersection network](subset-intersection-network.md). Each wire carries an array of complex values in place of a scalar,. Its edges change the frames of these arrays by products of two-point kernels, and this identity is what the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) uses to apply a butterfly on several address bits at once, one step toward the [main theorem](main-theorem.md).

The network takes its addresses from the [binary field](binary-field.md). Let $m$ be the number of coordinates of an address, so addresses are the vectors $x\in\mathbb F_2^m$ and each array has $2^m$ entries. For a binary vector $z$, $\mathrm{supp}(z)$ is the set of coordinates at which $z$ is $1$, and $\mathrm{wt}(z)=|\mathrm{supp}(z)|$ is its Hamming weight, read as an integer. For binary vectors $u,v$, the dot product $u\cdot v$ is the parity of $|\mathrm{supp}(u)\cap\mathrm{supp}(v)|$. For $b\in\mathbb F_2$, $[b]\in\{0,1\}$ is its integer representative.

The complex phase network is indexed by [subspace labels](subspace-labels.md): each vertex carries one label $U$, a subspace with $U\cap U^\perp=0$. For a nondegenerate subspace $W$, $P_W$ is the projection onto $W$ along $W^\perp$. For a function $f$ on addresses, $\mathrm{diag}_x(f(x))$ is the diagonal operator that multiplies the value at each address $x$ by $f(x)$. The phase exponent of an address is $q_U(x)=\mathrm{wt}(P_Ux)\bmod 4$, and the frame at a vertex with label $U$ is
$$C_U = H^{\otimes m}\,\mathrm{diag}_x\big(i^{q_U(x)}\big)\,H^{\otimes m},$$
where $H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ is the normalized Hadamard matrix.

The complex phase network computes its frames by the [tensor power](tensor-product.md) $H^{\otimes m}$ of $H$, where $\otimes$ is the Kronecker product. The complex phase network has coefficients in [Gaussian dyadics](gaussian-dyadics.md): each entry of $C_U$ and of $C_U^{-1}$ is a Gaussian integer divided by $2^m$. This holds because each entry of $H^{\otimes m}$ is $\pm 2^{-m/2}$, so each entry of $C_U$ is $2^{-m}$ times a sum of terms $\pm i^{q_U(x)}$, and each such sum is a Gaussian integer.

Set $\tau_0=\frac{1+i}{2}$ and $\tau_1=\frac{1-i}{2}$. Then $\tau_0^2+\tau_1^2=0$ and $2\tau_0\tau_1=1$. For a binary vector $v$, $X_v$ is the translation by $v$ on functions of addresses: Since $X_v^2=I$, the operator $\Theta_v=\tau_0 I+\tau_1 X_v$ has inverse $\tau_1 I+\tau_0 X_v$, because $(\tau_0 I+\tau_1X_v)(\tau_1 I+\tau_0X_v)=2\tau_0\tau_1 I+(\tau_0^2+\tau_1^2)X_v=I$.

An edge runs from a tail label $U$ to a head label $V$, and its frame change is $C_VC_U^{-1}$. Write $A\perp B$ when every vector of $A$ is orthogonal to every vector of $B$ and $A\cap B=0$, so $A+B$ is their orthogonal sum. The orthogonal residual $\Delta$ of an edge is the orthogonal complement of the smaller label inside the larger one. An increasing edge has $V=U\perp\Delta$, and a decreasing edge has $U=V\perp\Delta$. Let $\mathcal{O}$ be an orthonormal basis of $\Delta$: a set of vectors $v$ with $v\cdot v=1$ and $v\cdot v'=0$ for distinct $v,v'\in\mathcal O$.

Take an increasing edge and an address $x$. First, $P_\Delta x=\sum_{v\in\mathcal O}(v\cdot x)\,v$: the sum lies in $\Delta$, and $x$ minus the sum is orthogonal to every $v\in\mathcal O$, hence to $\Delta$. Second, $P_Vx=P_Ux+P_\Delta x$. The right side lies in $V$. The vector $x-P_Ux-P_\Delta x$ is orthogonal to $U$, because $x-P_Ux\in U^\perp$ and $P_\Delta x\in\Delta\perp U$. It is also orthogonal to $\Delta$, because $x-P_\Delta x\in\Delta^\perp$ and $P_Ux\in U\perp\Delta$. So it lies in $(U+\Delta)^\perp=V^\perp$.

For binary vectors $z,w$ (letters local to this argument), a coordinate in both supports is counted twice in $\mathrm{wt}(z)+\mathrm{wt}(w)$ and not at all in $\mathrm{wt}(z+w)$, so $\mathrm{wt}(z+w)=\mathrm{wt}(z)+\mathrm{wt}(w)-2|\mathrm{supp}(z)\cap\mathrm{supp}(w)|$. Hence $\mathrm{wt}(z+w)\equiv\mathrm{wt}(z)+\mathrm{wt}(w)\pmod 4$ whenever $z\cdot w=0$.

Now $P_Ux\cdot P_\Delta x=0$, since $P_\Delta x\in\Delta\perp U$. So $\mathrm{wt}(P_Vx)\equiv\mathrm{wt}(P_Ux)+\mathrm{wt}(P_\Delta x)$ modulo 4. The summands $(v\cdot x)\,v$ are pairwise orthogonal. Any partial sum of the earlier summands is a combination of earlier vectors $v$, so it is orthogonal to the next summand. Adding the summands one at a time gives $\mathrm{wt}(P_\Delta x)\equiv\sum_{v\in\mathcal O}[v\cdot x]\,\mathrm{wt}(v)$ modulo 4. Since $q_V(x)$ and $q_U(x)$ are these weights modulo 4,
$$q_V(x)-q_U(x)\equiv\sum_{v\in\mathcal O}\mathrm{wt}(v)\,[v\cdot x]\pmod 4.$$
On a decreasing edge the roles of $U$ and $V$ swap, so the right side is negated.

 Let $\varepsilon_v\in\{1,-1\}$ with $\varepsilon_v\equiv\mathrm{wt}(v)\pmod 4$ on an increasing edge and $\varepsilon_v\equiv-\mathrm{wt}(v)\pmod 4$ on a decreasing edge. Then $i^{q_V(x)-q_U(x)}=\prod_{v\in\mathcal O}i^{\varepsilon_v[v\cdot x]}$.

For $b\in\{0,1\}$ and $\varepsilon\in\{1,-1\}$, $i^{\varepsilon b}=\frac{1+i\varepsilon}{2}+\frac{1-i\varepsilon}{2}(-1)^b$, since both sides equal $1$ at $b=0$ and $i\varepsilon$ at $b=1$. With $b=[v\cdot x]$, $\mathrm{diag}_x\big(i^{\varepsilon_v[v\cdot x]}\big)=\frac{1+i\varepsilon_v}{2}I+\frac{1-i\varepsilon_v}{2}\,\mathrm{diag}_x\big((-1)^{[v\cdot x]}\big)$. The matrix $H\,\mathrm{diag}(1,-1)\,H$ is the bit flip $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, and it turns the sign $(-1)^{[v\cdot x]}$, a product of one-coordinate signs over $\mathrm{supp}(v)$, into $X_v$. So conjugating by $H^{\otimes m}$ gives $\frac{1+i\varepsilon_v}{2}I+\frac{1-i\varepsilon_v}{2}X_v$. For $\varepsilon_v=1$ this is $\Theta_v$, and for $\varepsilon_v=-1$ it is $\tau_1 I+\tau_0X_v=\Theta_v^{-1}$. Thus $H^{\otimes m}\,\mathrm{diag}_x\big(i^{\varepsilon_v[v\cdot x]}\big)\,H^{\otimes m}=\Theta_v^{\varepsilon_v}$.

Since $(H^{\otimes m})^2=I$ and diagonal operators multiply pointwise, $C_VC_U^{-1}=H^{\otimes m}\,\mathrm{diag}_x\big(i^{q_V(x)-q_U(x)}\big)\,H^{\otimes m}$. Therefore $C_VC_U^{-1}=\prod_{v\in\mathcal O}\Theta_v^{\varepsilon_v}$: the edge change is one two-point kernel per basis vector, so it costs $\dim\Delta$ kernels. The intermediate labels are chosen.

For $m=1$, take the labels $\{0\}$ and $\mathbb F_2$. Here $C_{\{0\}}=I$, since $q_{\{0\}}=0$, and $P_{\mathbb F_2}$ is the identity, so $C_{\mathbb F_2}=H\,\mathrm{diag}(1,i)\,H=\tau_0I+\tau_1X_1$, the matrix $\frac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix}$. The edge is increasing with $\Delta=\mathbb F_2$, $\mathcal O=\{1\}$, and $\mathrm{wt}(1)=1$ gives $\varepsilon_1=1$, so the formula gives the same kernel $\Theta_1=C_{\mathbb F_2}$.

For general $m$, take the route $U_0=\{0\}$ and $U_\delta=\mathrm{span}(e_1,\dots,e_\delta)$ for $1\le\delta\le m$, where $e_1,\dots,e_m$ is the standard basis and $e_\delta$ has a single $1$ at position $\delta$. Each $U_\delta$ is nondegenerate, since the Gram matrix of $e_1,\dots,e_\delta$ is the identity. The edge from $U_{\delta-1}$ to $U_\delta$ is increasing with $\Delta=\mathrm{span}(e_\delta)$, $\mathcal O=\{e_\delta\}$ and $\varepsilon_{e_\delta}=1$. So its exponent difference is $[e_\delta\cdot x]=x_\delta$, the $\delta$-th coordinate of $x$. The intermediate frames cancel in the product, so $(C_{U_1}C_{U_0}^{-1})\cdots(C_{U_m}C_{U_{m-1}}^{-1})=C_{U_m}C_{U_0}^{-1}$. The exponents telescope to $q_{\mathbb F_2^m}(x)-q_{\{0\}}(x)\equiv\sum_\delta x_\delta=\mathrm{wt}(x)\pmod 4$, since $P_{\mathbb F_2^m}$ is the identity. Hence $C_{U_m}C_{U_0}^{-1}=H^{\otimes m}\,\mathrm{diag}_x\big(i^{\mathrm{wt}(x)}\big)\,H^{\otimes m}$. The diagonal entry at $x$ is a product of single-coordinate factors $i^{x_\delta}$, so $\mathrm{diag}_x(i^{\mathrm{wt}(x)})$ is the $m$-fold tensor power of $\mathrm{diag}(1,i)$. Writing $C=C_{\mathbb F_2}$, the mixed-product rule gives $C_{U_m}C_{U_0}^{-1}=C^{\otimes m}$. This is the frame that the paper's telescoping gives:.
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

Write the answer to `exegenius/tasks/0444-audit-complex-phase-network.answer.json`, then run `exegenius submit 0444-audit-complex-phase-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
