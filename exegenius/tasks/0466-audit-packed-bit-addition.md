# exegenius task 0466-audit-packed-bit-addition

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
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier, der Hoeven)
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
- Signed coefficient packing (also: Kronecker substitution, packed polynomial product)
- Convolution over the polynomial ring
- Subspace labels (also: binary label)
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network, side and central wires, gather and scatter, scalar network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks, address-field interchange procedure, field interchanges)
- Address shear (also: shear of address pairs, Matrix shear)
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant, orthogonal residual of an edge)
- Simultaneous butterfly layer (also: selected bits, two-point operator on selected bits)
- Guard-width bound (also: segment)
- Transform layout (also: transform layout and packed selected-bit addition)
- Transform identity with retained permutations (also: target permutation, coordinate permutations)
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Bit procedure
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Cost table (also: chirp and twist)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Endpoint operator
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
- Numerical layer (also: butterfly layers, layer)
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Scratch storage (also: scratch values, scratch chunk, scratch wires, forward schedule, linear-readout version)
- Tensor product (also: tensor power)
- Transform round (also: butterfly round, current recursive length, level the round processes)
- Truncation
- Union bound
- Exclusive or (also: XOR)
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
- Complex construction
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
- Supremum
- Tape procedure
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $\lg$ (base-2 logarithm), bound on `base-two-logarithm`: The base-2 logarithm of $n$, the least integer $k$ with $2^k \ge n$, but at least 1.
- $R$ (ring), bound on `ring`: A set with an addition and a multiplication satisfying the axioms listed on this page.
- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $q$ (second prime), bound on `prime-number`: A prime number different from p, used in the coprimality argument.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $P$ (normalized pointwise product), bound on `pointwise-product`: The map that sends two entries to their product in the ring divided by $r$.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $A$ (machine), bound on `running-time-cost`: The single machine whose running time the main theorem bounds.
- $\kappa$ (fixed exponent constant), bound on `running-time-cost`: A fixed constant, equal to $2^{-182}$, that sets the exponent $1-\kappa$ in the running time bound.
- $M$ (scanning machine), bound on `running-time-cost`: The example machine that reads cells from left to right and halts at the first cell holding 1 or at the last cell.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $\beta$ (second paired value), bound on `truncation`: The second of the two values that the layer combines in each pair.
- $A$ (source set), bound on `bijection`: The source set, whose elements are the inputs of the map f.
- $f$ (map), bound on `bijection`: The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $E$ (subset of source), bound on `bijection`: A subset of the source set A, whose image under a bijection is compared with the image of its complement.
- $A$ (array), bound on `permutation`: An array of entries stored at addresses, the object that an address permutation moves.
- $\kappa$ (exponent gap), bound on `schoolbook-multiplication`: A fixed constant, $2^{-182}$, which sets the saving in the exponent $1-\kappa$ of the bound.
- $\lg$ (base-2 logarithm), bound on `schoolbook-multiplication`: The base-2 logarithm, applied to the input length n.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $q$ (level ratio), bound on `mathematical-induction`: The fixed positive real ratio by which one level may multiply a bound.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $q$ (key), bound on `stable-radix-sort`: The key of a record, a w-bit nonnegative integer written with bits q_{w-1} down to q_0.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $A_{\mathrm{rect}}$ (integer bit bound), bound on `stable-radix-sort`: The source's bound on the number of bits in its integers, which the padded destination key width may not exceed.
- $q$ (address before move), bound on `destination-rank`: The address of a record before the move.
- $q'$ (address after move), bound on `destination-rank`: The address of the same record after the move.
- $h$ (chunk index), bound on `destination-rank`: The index of a chunk of an address, taking the value 1, 2 or 3.
- $q_h$ (current chunk value), bound on `destination-rank`: The value of chunk $h$ in the address $q$ before the move.
- $q'_h$ (destination chunk value), bound on `destination-rank`: The value of chunk $h$ in the address $q'$ after the move.
- $\sigma_h$ (record stride), bound on `destination-rank`: The amount by which the rank changes when chunk $h$ rises by one with the other two chunks fixed.
- $A_{\mathrm{rect}}$ (rectangular bit bound), bound on `destination-rank`: A bound on the number of bits in each integer the rectangular routine handles.
- $R$ (payload bits), bound on `destination-rank`: The number of payload bits in a record.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The monic complex polynomial whose multiples count as zero.
- $R$ (polynomial ring modulo f), bound on `polynomial-ring`: The ring of classes of complex polynomials in $y$, where multiples of $f$ are zero.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $X$ (array), bound on `array-norm`: A finite array of complex values.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $A$ (multiplication machine), bound on `little-o-notation`: The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $\kappa$ (saving exponent), bound on `little-o-notation`: The fixed positive constant 2^{-182} in the saving exponent $1-\kappa$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $\gamma$ (second integer), bound on `coprime`: The other integer whose greatest common divisor with beta is taken, not both zero with it.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $\xi$ (element), bound on `ring-homomorphism`: An arbitrary element of the domain ring.
- $\eta$ (second element), bound on `ring-homomorphism`: An arbitrary element of the domain ring.
- $\delta$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $t$ in an element $\alpha+\delta t$ of $Q$.
- $\rho$ (reduction map), bound on `ring-homomorphism`: The map from $Q$ to $\mathbb{C}$ sending $\alpha+\delta t$ to $\alpha+\delta$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $L$ (block length), bound on `cyclic-shift`: The number of positions in the block, a count of positions.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array, which the cost bound is linear in.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m	imes m$ matrix with entries in $F$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map from one vector space over $F$ to another.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $M$ (matrix), bound on `linear-algebra-basics`: A matrix from which the shear frame $\Phi_M$ is built.
- $K$ (second address chunk), bound on `linear-algebra-basics`: A binary address chunk, the second field of an address pair.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $\rho$ (role permutation), bound on `linear-network-frames`: The permutation of roles that sends each input role to an output role.
- $K$ (second address field), bound on `linear-network-frames`: The second of two address fields, written as a vector; not a frame.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set, so it counts those elements.
- $T$ (three-element subsets), bound on `ground-set`: The set of all three-element subsets of $[h]$.
- $V$ (operator space), bound on `eigenvalue`: The vector space on which the linear operator T acts.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $T$ (triple T), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, whose indicator vector is discussed.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $W$ (wire count), bound on `matrix-rank`: The number of wires in the network, which counts the edges that carry edge changes.
- $\tau$ (complex number), bound on `phase-factor`: A complex number written as alpha plus beta i.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number tau, a real number.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, so it counts the entries of a vector.
- $K$ (linear map on q-vectors), bound on `discrete-fourier-transform`: A linear map from q-vectors to q-vectors, which is tested for being a contraction.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $\kappa$ (output position), bound on `multidimensional-transform`: A position in the output array, a tuple of D coordinates with the same bounds as a position in the input array.
- $r$ (record length), bound on `synthetic-transforms`: A power of two, the number of complex coefficients in a record.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $\delta$ (half block size), bound on `synthetic-transforms`: The number of positions in half of a block at a level, taking the values $1, 2, \dots, N/2$.
- $\tau$ (butterfly offset), bound on `synthetic-transforms`: The offset of a butterfly pair within the first half of its block, from $0$ to $\delta-1$.
- $\log_2$ (base-2 logarithm), bound on `synthetic-transforms`: The logarithm to base 2, so $\log_2 N$ is the number of levels of the fast method.
- $\lg$ (base-2 logarithm), bound on `synthetic-transforms`: The logarithm to base 2.
- $\kappa$ (running time exponent constant), bound on `synthetic-transforms`: A fixed positive constant in the exponent of the running time bound.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $P$ (ring element), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring $R_r$, given by its representative of degree less than $r$.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\tau$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring whose positive integer power equals 1.
- $\delta$ (first input value), bound on `butterfly`: The first of the two input values of the butterfly.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than $s$.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $E$ (map into length t), bound on `gaussian-resampling`: A linear contraction from length-$s$ vectors to length-$t$ vectors, in the identity.
- $\delta$ (Gaussian integer numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of a Gaussian dyadic $\delta/2^e$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\tau$ (common exponent), bound on `gaussian-dyadics`: The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $K$ (two-point kernel matrix), bound on `two-point-kernel`: The $2\times 2$ matrix $\delta I+\kappa X$ that defines the two-point kernel.
- $\delta$ (diagonal coefficient), bound on `two-point-kernel`: The coefficient of $I$ in $K$, a complex number.
- $\kappa$ (off-diagonal coefficient), bound on `two-point-kernel`: The coefficient of $X$ in $K$, a complex number.
- $X$ (bit flip), bound on `two-point-kernel`: The $2\times 2$ matrix that interchanges the two entries of a pair.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $\oplus$ (bitwise exclusive or), bound on `two-point-kernel`: The operation giving the bitwise exclusive or of two addresses.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}, the matrix whose tensor powers are taken.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $t$ (address bit string), bound on `tensor-product`: A bit string of length m that is an address on m coordinates.
- $f$ (function on addresses), bound on `tensor-product`: A function on addresses of m coordinates, the input that the operator transforms.
- $E$ (first argument space), bound on `bilinear-map`: The vector space containing the first argument e of the bilinear map.
- $K$ (output space), bound on `bilinear-map`: The vector space containing the values pi(e,d) of the bilinear map.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\kappa$ (real input), bound on `ceiling-function`: The real number whose ceiling is taken.
- $\tau$ (processed positions), bound on `carry-propagation`: The number of low positions already processed, so that the sums run over $t < \tau$.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\delta$ (remainder), bound on `congruence-modulo`: The integer in {0,...,B-1} that is the remainder of a residue class.
- $\oplus$ (exclusive or), bound on `binary-field`: The addition of the binary field, which gives $1$ exactly when its two bits differ.
- $\tau$ (field element), bound on `binary-field`: An arbitrary element of the binary field, so it is $0$ or $1$.
- $K$ (example matrix), bound on `binary-field`: The $2 \times 2$ matrix over the binary field used in the example, with rows $(1, 1)$ and $(0, 1)$.
- $M$ (change-of-basis matrix), bound on `binary-change-of-basis`: An invertible $m\times m$ matrix over $\mathbb F_2$ that specifies the change of basis.
- $\kappa$ (address), bound on `binary-change-of-basis`: A vector in $\mathbb F_2^m$, one address of the selected bits.
- $E$ (vector space), bound on `bilinear-form`: A vector space over the field $F$ of scalars, on which the bilinear form is defined.
- $\xi$ (vector), bound on `bilinear-form`: A vector of $E$.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $E$.
- $A$ (form matrix), bound on `bilinear-form`: The $m\times m$ matrix of the form in the chosen basis.
- $K$ (scalar field), bound on `line-spanned-by-vector`: The field of scalars over which the vector space E is taken.
- $E$ (vector space), bound on `line-spanned-by-vector`: A vector space over K, containing the nonzero vector v.
- $\tau$ (choice of three triples), bound on `line-spanned-by-vector`: A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $\kappa$ (modulus), bound on `centered-residue`: A positive integer, the modulus by which residues are taken.
- $\tau$ (centered residue), bound on `centered-residue`: The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\tau$ (solution), bound on `chinese-remainder-theorem`: An unknown integer, which is a solution when it satisfies every congruence of the system.
- $f$ (first input sequence), bound on `cyclic-convolution`: The first of the two sequences of length n whose cyclic convolution is taken.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences of length n whose cyclic convolution is taken.
- $d$ (number of axes), bound on `cyclic-convolution`: The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $\kappa$ (axis index), bound on `cyclic-convolution`: The index of an axis, running from 1 to d.
- $\tau$ (reflected chirp), bound on `cyclic-convolution`: The function tau(delta) of an integer delta, read as a sequence of length t.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\kappa$ (last-axis position), bound on `cyclic-coordinate`: An integer from 0 to r-1 giving a position along the last cyclic coordinate.
- $d$ (greatest common divisor), bound on `bezout-identity`: The greatest common divisor of beta and gamma, the largest positive integer dividing both.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $\kappa$ (integer quotient), bound on `bezout-identity`: The integer quotient when beta is divided by e.
- $\tau$ (remainder), bound on `bezout-identity`: The remainder when beta is divided by e, which lies between 0 and e minus 1.
- $h$ (comparison function), bound on `big-theta-notation`: A second function of the same kind as $u$, against which the growth of $u$ is measured.
- $\kappa$ (saving exponent), bound on `big-theta-notation`: The fixed positive exponent saving in the bound, equal to $2^{-182}$ in the paper.
- $\kappa$ (group order), bound on `cyclic-group`: The number of elements of the cyclic group $C_\kappa$, which is its order.
- $\tau$ (generator), bound on `cyclic-group`: A fixed element of the group; its powers give every element of the cyclic group $C_\kappa$.
- $\beta$ (integer to invert), bound on `modular-inverse`: The integer whose inverse modulo M is sought.
- $M$ (modulus), bound on `modular-inverse`: A positive integer, the modulus of the inverse.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $\xi$ (generator), bound on `modular-inverse`: A generator of a cyclic group of order S, whose powers make up the group.
- $\kappa$ (positive exponent), bound on `modular-inverse`: A positive integer exponent under which the image becomes 1.
- $\tau$ (real number), bound on `extended-reals`: A generic real number, used when the order and arithmetic of the extended reals are stated.
- $\delta$ (sequence position), bound on `extended-reals`: The position of a term in a sequence of extended real numbers, running over 1, 2, 3, and so on.
- $k$ (term index), bound on `limit-inferior`: The position of a term in a sequence, an index counting from 1.
- $\kappa$ (bound exponent), bound on `limit-inferior`: The fixed exponent $2^{-182}$ in the main time bound.
- $\log$ (base-2 logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm, as used in the expression $n \log n$.
- $\lg n$ (binary logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm of n rounded up to an integer and never below 1.
- $\kappa$ (saving exponent), bound on `n-log-n-conjecture`: The fixed positive constant in the exponent 1 - kappa of the main theorem's running time, equal to 2^{-182}.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers, a count of bits.
- $\lg$ (base-2 logarithm), bound on `fixed-tape-model`: The base-2 logarithm, so that $\lg n$ stands for $\log_2 n$.
- $\tau$ (family parameter), bound on `family-parameter`: The index of a member of the family: a nonnegative integer that selects which construction is built and so fixes its size.
- $f$ (disk-grid ring array), bound on `opposite-transform`: One of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $g$ (second disk-grid ring array), bound on `opposite-transform`: The second of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $M$ (pointwise product count), bound on `opposite-transform`: The number of pointwise polynomial products, a count that is not the record count of earlier pages.
- $R$ (retained permutation), bound on `transform-identity`: The coordinate permutation $(R_cz)_j=z_{cj}$ for a unit $c$ modulo $s$, applied on each axis, which the identity keeps.
- $A$ (forward contraction), bound on `transform-identity`: A linear contraction from length-$s$ vectors to length-$t$ vectors.
- $E$ (entry count), bound on `padded-transform-box`: The number of entries of the box, counting valid and zero entries alike.
- $\tau$ (chirp position), bound on `bluestein-chirp-identity`: The integer position of a chirp entry, which may be negative or larger than q-1.
- $\bmod$ (remainder modulo q), bound on `bluestein-chirp-identity`: x mod q is the remainder of the integer x on division by q, a position in {0,...,q-1}.
- $\sigma$ (digit scale), bound on `normalization-scales`: The power of two $2^{-b-2}$ by which each radix-$2^b$ digit is multiplied when it is stored.
- $\delta$ (first digit array), bound on `normalization-scales`: The integer digit array of the first input, whose entries lie between $0$ and $2^b-1$.
- $\oplus$ (direct sum), bound on `subspace-labels`: The sum of two subspaces that meet only in zero, so that each vector of the sum is uniquely a vector of one plus a vector of the other.
- $\tau$ (kernel coefficient tau), bound on `subspace-labels`: The first Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $\delta$ (kernel coefficient delta), bound on `subspace-labels`: The second Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $f$ (function of addresses), bound on `subspace-labels`: A function from addresses in $\mathbb F_2^m$ to values, which a translation shifts (this letter changes meaning on this page).
- $\mathcal T$ (set of triples), bound on `subset-intersection-network`: The set of all three-element subsets of the ground set $[h]$.
- $X$ (bank X), bound on `subset-intersection-network`: One of the two banks of scalars, with entries $X_\tau$ indexed by triples of triples.
- $\tau$ (bank index), bound on `subset-intersection-network`: A triple of triples, indexing the entries of a bank.
- $\xi$ (source vector), bound on `subset-intersection-network`: The vector of one bank's entries along the varying coordinate, read by a forward invocation.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of the other bank's entries along the varying coordinate, updated by a forward invocation.
- $\delta$ (vector of E), bound on `subset-intersection-network`: A vector of the ambient space $E=\mathbb Q^h$, an argument of the bit network form.
- $V$ (head label), bound on `complex-phase-network`: The label at the head of an edge, whose frame is applied last along that edge.
- $\delta$ (route step), bound on `complex-phase-network`: The index of a step along the coordinate route, running from one to $m$.
- $a$ (starting side values), bound on `scratch-storage`: The starting values of the side wires $W_{ST}$.
- $c$ (starting central values), bound on `scratch-storage`: The starting values of the central wires $C_\ell$.
- $V$ (copy operator), bound on `scratch-storage`: The operator that adds each control value $x_T$ to the side wire $W_{ST}$ of each neighbouring pair $(S,T)$.
- $R$ (scatter operator), bound on `scratch-storage`: The operator that adds to $y_S$ the central wires $C_\ell$ summed over the elements $\ell$ of $S$.
- $T$ (triple), bound on `scratch-storage`: A three-element subset of the ground set, indexing a control value $x_T$.
- $\oplus$ (exclusive or), bound on `address-interchange`: Bitwise exclusive or: the sum modulo 2 of two bits, taken position by position.
- $k$ (number of levels), bound on `address-interchange`: The number of levels in the recursion on the width, so that a width $u=m^k$ has $k=\log_m u$ levels.
- $W$ (piece count), bound on `address-interchange`: The number of equal pieces the volume is cut into at each call, at least 2.
- $\tau$ (exponent), bound on `address-interchange`: A fixed number in $(0,1)$, the exponent of the bound $O(V u^{\tau})$.
- $\delta$ (first bit), bound on `xor`: A bit, one of the two inputs to the exclusive or.
- $\oplus$ (XOR operation), bound on `xor`: The exclusive-or operation, the bitwise sum modulo 2 of two bits, applied at each position to bit strings of equal length.
- $q$ (radix), bound on `address-shear`: A fixed odd prime, the base in which the digits of each field are written.
- $M$ (shear matrix), bound on `address-shear`: A fixed m by m matrix with rational entries, which determines the shear.
- $a$ (rational rank), bound on `address-shear`: The number of linearly independent rows of M over the rational numbers.
- $e$ (chunk digit count), bound on `address-shear`: The number of radix-q digits in each interchanged chunk, which is m^k at recursion depth k.
- $\delta$ (chunk width), bound on `simultaneous-butterfly-layer`: The number of consecutive address bits in each chunk, one chunk per transform axis.
- $X$ (bit-flip matrix), bound on `simultaneous-butterfly-layer`: The $2\times2$ matrix swapping the two coordinates of a bit.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number $D$ of selected axes in a layer.
- $e$ (axes per call), bound on `numerical-layer`: The number of selected axes that a call acts on.
- $W$ (role count), bound on `numerical-layer`: The number of roles among which rows are distributed.
- $e$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the selected axes of a numerical layer or the digits of an address field.
- $\delta$ (cost per unit volume), bound on `rank-saving-recursion`: The cost of a call at parameter e divided by its volume.
- $\tau$ (power-saving exponent), bound on `rank-saving-recursion`: The exponent log base m of s/W, so that the cost per unit of data is about e to the power tau.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, one of the $D$ axes.
- $\eta$ (twiddle exponent), bound on `transform-round`: The exponent of the twiddle at an address, an integer taken modulo $2r$.
- $e$ (quotient of exponent), bound on `transform-round`: The integer quotient of $\eta$ by $r$, which counts the whole multiples of $r$ in $\eta$.
- $\delta$ (remainder of exponent), bound on `transform-round`: The remainder of $\eta$ on division by $r$, with $0\le\delta<r$.
- $T$ (padded box cell count), bound on `cost-table`: The number of cells of the padded box, a power of two with 4n/b <= T < 8n/b.
- $V$ (logical bit volume), bound on `cost-table`: The logical bit volume V = Tp of the padded box, which is Theta(n) bits.
- $c$ (chunk exponent), bound on `cost-table`: A fixed positive rational exponent, 2^{-56} in the paper's choice, with K = Theta(p^{epsilon c}).
- $\delta$ (resampling exponent), bound on `cost-table`: A fixed rational exponent, 1/16 in the paper's choice, in the powers of the Gaussian and chirp rows.
- $K$ (chunk width), bound on `cost-table`: The width of the address chunks, in bits, K = floor(d^c) = Theta(p^{epsilon c}).
- $r$ (largest axis length), bound on `cost-table`: The largest axis length of the padded box, a power of two, whose base-two logarithm is ell.
- $\log$ (base-2 logarithm), bound on `established-multiplier`: The base-2 logarithm, the power to which 2 must be raised to give the argument.
- $f$ (first polynomial), bound on `signed-packing`: The first input, an integer polynomial whose coefficients are the $f_j$.
- $g$ (second polynomial), bound on `signed-packing`: The second input, an integer polynomial whose coefficients are the $g_j$.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $fg$, a polynomial whose coefficients are the $h_j$.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
- $i$ (summation index), bound on `signed-packing`: The index of the sum that gives $h_j$, running over the positions $0$ to $r-1$ of $f$.
- $e$ (wrap exponent), bound on `polynomial-ring-convolution`: An integer exponent of y, which may be at least r, so that y^e wraps around with a sign flip.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between the computed input and the exact input $x$, so that the computed input is $x + \eta$.
- $e$ (group size), bound on `guard-width-bound`: The number of selected axes in a group that the recursion splits.
- $A$ (operation bound), bound on `guard-width-bound`: An upper bound on the number of operations on any chain within a group of e axes.
- $\eta$ (gate constant), bound on `guard-width-bound`: The constant $64(W+m+1)^3$ bounding the operations for gates and corrections at one node.
- $\beta$ (operation growth factor), bound on `guard-width-bound`: The constant $s+\eta$ by which each recursion level multiplies a bound.
- $f$ (selected bit count), bound on `union-bound`: The number of selected bit positions, which fixes the number of guards 2(f-1).
- $K$ (segment width), bound on `union-bound`: The number of bits in each segment.

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

## Page to audit (`packed-bit-addition`)

````markdown
# Packed selected-bit addition

Packed selected-bit addition acts on two disjoint [address fields](address-field.md) of equal width, the source $\mathcal{X}$ and the target $\mathcal{W}$. It XORs selected bits of $\mathcal{X}$ into the same bits of $\mathcal{W}$ at every address, and it supplies the binary basis changes of the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md). It contributes one term to the [cost table](cost-table.md) of the main theorem, which bounds exact multiplication of $n$-bit integers by $O(n(\lg n)^{1-\kappa})$ for a fixed $\kappa>0$. Packed selected-bit addition performs its basis changes in each [transform round](transform-round.md).

Packed selected-bit addition uses its third field as [scratch storage](scratch-storage.md), $\mathcal{T}$, whose initial value is arbitrary and must be restored. Each field has $L=fK$ address bits.

Let $\rho$ be the position of the first selected bit, counted from $0$ at the least significant end. Let $i$ index the $f-1$ segments, $0\le i<f-1$, so segment $i$ starts at the selected position $\rho+iK$ and occupies $K$ bits, where $K$ is the segment width. The lowest bit of a segment is its selected bit, and the other $K-1$ bits form its guard, whose value $\gamma$ lies between $0$ and $2^{K-1}-1$. As an integer, a segment has value $2\gamma$ plus its selected bit.

Packed selected-bit addition adds selected bits by [exclusive or](xor.md), so each selected bit of $\mathcal{W}$ is XORed with the selected bit of $\mathcal{X}$ in the same segment. A shift adds its offset to the field's integer value. Packed selected-bit addition updates its target field by controlled [cyclic shifts](cyclic-shift.md)., so a shift cannot test the selected bit of the field it changes.

Shifting $\mathcal{W}$ by $2^{\rho+iK}$ adds $1$ to the value $2\gamma+a$ of segment $i$, where $a$ is its selected bit. The carry stays inside the segment while the value stays in $[0,2^K-1]$. Adding $+1$ flips a selected bit $0$ to $1$, but flipping a $1$ to $0$ needs $-1$. The eight updates below supply that sign.

For a segment of $\mathcal{W}$ with value $\xi$ and the corresponding segment of $\mathcal{T}$ with value $\eta$, the procedure applies eight controlled updates. Each is controlled by a bit $\beta\in\{0,1\}$, the selected bit of $\mathcal{X}$ in that segment. Here $[P]$ is $1$ when $P$ holds and $0$ otherwise, and the updates run in order (1) to (8):

$$
\begin{aligned}
(1)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 0 \pmod 2], & (2)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 0 \pmod 2],\\
(3)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 0 \pmod 2], & (4)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 0 \pmod 2],\\
(5)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 1 \pmod 2], & (6)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 1 \pmod 2],\\
(7)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 1 \pmod 2], & (8)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 1 \pmod 2].
\end{aligned}
$$

Each line changes one value by $\pm\beta$ and tests the parity of the other value, its selected bit, so it is one controlled shift. Packed selected-bit addition uses updates like the [Address shear](address-shear.md).

If $\beta=1$, the parity pairs $(\xi \bmod 2,\ \eta \bmod 2)$ cycle through $(00\ 01\ 10)$ under lines (1) to (4) and through $(01\ 10\ 11)$ under lines (5) to (8). Together these give $(00\ 10)(01\ 11)$, which flips the parity of $\xi$ alone. Both quotients by two are preserved, and $\eta$ returns to its start:. So $\xi\mapsto\xi+\beta(1-2(\xi \bmod 2))$. The selected bit of $\mathcal{W}$ flips exactly when $\beta=1$, and the guard is unchanged, which is the XOR..

Let $\mathcal{E}$ be the set of addresses at which some guard of the $f-1$ segments of $\mathcal{W}$ or of $\mathcal{T}$ lies outside $[10,\,2^{K-1}-11]$. Off $\mathcal{E}$, each segment value lies in $[20,\,2^K-21]$, so a displacement of at most eight keeps it in $[0,\,2^K-1]$. No carry crosses a segment, and the stage gives exactly the required XORs.

Each guard takes each of its $2^{K-1}$ values equally often over the addresses, and exactly twenty values are excluded, so the excluded fraction is $20/2^{K-1}$. The procedure bounds its exceptional set by a [union bound](union-bound.md) over the $2(f-1)$ guards, giving $|\mathcal{E}|\le 80(f-1)2^{-K}M$, where $M$ counts the records.

 over all payloads. Packed selected-bit addition is correct for every [payload](payload.md) it carries. The procedure scans the [stream](stream.md) of all $M$ records with a rank counter to find the records at addresses in $\mathcal{E}$. For a record at address $q$, reverse the eight updates with negated offsets and apply the XORs to find $q'$.

The procedure computes the [destination rank](destination-rank.md) of each extracted record. Its value is $\operatorname{rank}(q')=\operatorname{rank}(q)+\sum_h (q'_h-q_h)\sigma_h$, summed over $h\in\{\mathcal{X},\mathcal{W},\mathcal{T}\}$, where $\sigma_h$ is the record stride of field $h$. The procedure sorts the extracted records by a [stable radix sort](stable-radix-sort.md) on these ranks. The map sends $\mathcal{E}$ onto itself, so the ranks are distinct and are exactly the holes left by the extraction. One forward scan then reinserts each record at its rank.

The top selected bit is XORed in last. On two bits, $e_1$ from $\mathcal{X}$ and $e_2$ from $\mathcal{W}$, the map $(e_1,e_2)\mapsto(e_1,\,e_1\oplus e_2)$ fixes $00$ and $01$ and swaps $10$ and $11$, so it XORs the first bit into the second. positions in $O(V)$ time.

The procedure exchanges its fields by the [Address-field interchange](address-interchange.md)., with $\tau$ the fixed exponent of the interchange. It uses at most sixteen exchanges and eight shifts, each shift costing $O(V)$. in total.

Each address holds a record of $R$ bits, so $V=MR$. The correction adds $O(MA_{\mathrm{rect}}^3+\delta MA_{\mathrm{rect}}(R+A_{\mathrm{rect}}))$ time, where $A_{\mathrm{rect}}=\lceil\log_2(2V)\rceil$ bounds the bit size of every integer involved, and $\delta=80(f-1)2^{-K}$. The total time is

$$
O\bigl(V(L^{\tau}+1)+MA_{\mathrm{rect}}^3+\delta\,MA_{\mathrm{rect}}(R+A_{\mathrm{rect}})\bigr).
$$

The bound is stated along a [family parameter](family-parameter.md) that tends to infinity. Along that family $A_{\mathrm{rect}}$ grows at most linearly, $R$ outgrows every polynomial, and $K$ outgrows the logarithm, so the extra terms, which are $A_{\mathrm{rect}}^3/R$ and $\delta A_{\mathrm{rect}}(1+A_{\mathrm{rect}}/R)$ after dividing by $V=MR$, tend to zero. So the time is $O(V(L^{\tau}+1))$.
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

Write the answer to `exegenius/tasks/0466-audit-packed-bit-addition.answer.json`, then run `exegenius submit 0466-audit-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
