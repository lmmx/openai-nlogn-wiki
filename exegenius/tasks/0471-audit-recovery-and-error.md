# exegenius task 0471-audit-recovery-and-error

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
- Chinese-remainder map (also: Agarwal–Cooley map, coefficient layout, generator)
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
- Packed selected-bit addition (also: exceptional addresses, selected bit)
- Guard-width bound (also: segment)
- Transform layout (also: transform layout and packed selected-bit addition)
- Prime source lengths (also: pairwise coprime source lengths)
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
- Mixed-radix digits (also: mixed-radix digit)
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
- Telescoping identity
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $b$ (base), bound on `logarithm`: The fixed number, greater than 1, to which the logarithm is taken.
- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $w$ (pointwise product), bound on `pointwise-product`: The sequence of length $m$ whose entry at each index is the product of the entries of $u$ and $v$ at that index.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $Q_p$ (truncation map), bound on `truncation`: The map that truncates each real and imaginary part of each coefficient of a list toward zero to the grid $2^{-p}\mathbb{Z}$.
- $\alpha$ (first paired value), bound on `truncation`: The first of the two values that the layer combines in each pair.
- $f$ (map), bound on `bijection`: The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $w$ (target element), bound on `bijection`: An element of the target set B, which the onto condition requires to be hit by some element of A.
- $E$ (subset of source), bound on `bijection`: A subset of the source set A, whose image under a bijection is compared with the image of its complement.
- $S$ (position set), bound on `permutation`: A finite set of positions, the set whose elements a permutation rearranges.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in a record's key, which is also the number of passes.
- $h$ (chunk index), bound on `destination-rank`: The index of a chunk of an address, taking the value 1, 2 or 3.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The monic complex polynomial whose multiples count as zero.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $\gamma$ (second integer), bound on `coprime`: The other integer whose greatest common divisor with beta is taken, not both zero with it.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $S$ (combined axis length), bound on `coprime`: The product s_1 through s_d, which is the length of the combined cyclic axis.
- $Q$ (quotient ring), bound on `ring-homomorphism`: The ring of complex polynomials in $t$ in which $t^2=1$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\alpha$ (coefficient), bound on `ring-homomorphism`: The complex constant term of an element $\alpha+\delta t$ of $Q$.
- $S$ (cycle length), bound on `ring-homomorphism`: A positive integer by which the paper's cyclic ring is reduced.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $\alpha$ (address), bound on `address`: A string of d bits that labels one entry of the array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $L$ (block length), bound on `cyclic-shift`: The number of positions in the block, a count of positions.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map from one vector space over $F$ to another.
- $S$ (inverse map), bound on `linear-algebra-basics`: A linear map that serves as the inverse of a linear operator $T$ when $ST=TS=\mathrm{id}$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $\alpha$ (input weight), bound on `linear-network-frames`: The fixed weight with which a gate multiplies its input s, the same at every address.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set, so it counts those elements.
- $T$ (three-element subsets), bound on `ground-set`: The set of all three-element subsets of $[h]$.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $S$ (triple S), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, paired with T as a candidate neighbor.
- $T$ (triple T), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, whose indicator vector is discussed.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $\alpha$ (real part), bound on `phase-factor`: The real part of the complex number tau.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $C$ (forward kernel), bound on `phase-factor`: The 2 by 2 matrix called the forward kernel.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $r$ (record length), bound on `synthetic-transforms`: A power of two, the number of complex coefficients in a record.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $\log_2$ (base-2 logarithm), bound on `synthetic-transforms`: The logarithm to base 2, so $\log_2 N$ is the number of levels of the fast method.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $\alpha$ (Gaussian width), bound on `gaussian-resampling`: The integer width of the Gaussian weights.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on `gaussian-resampling`: A generic vector of length $t$, on which $P_t$ acts.
- $E$ (map into length t), bound on `gaussian-resampling`: A linear contraction from length-$s$ vectors to length-$t$ vectors, in the identity.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $Q$ (second matrix), bound on `tensor-product`: A second matrix, the right factor in the tensor product P\otimes Q.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $m$ (tensor power count), bound on `tensor-product`: The number of factors in a tensor power, which counts the coordinates the operator acts on.
- $f$ (function on addresses), bound on `tensor-product`: A function on addresses of m coordinates, the input that the operator transforms.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $E$ (first argument space), bound on `bilinear-map`: The vector space containing the first argument e of the bilinear map.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $E$ (vector space), bound on `bilinear-form`: A vector space over the field $F$ of scalars, on which the bilinear form is defined.
- $E$ (vector space), bound on `line-spanned-by-vector`: A vector space over K, containing the nonzero vector v.
- $v$ (nonzero vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $f$ (first input sequence), bound on `cyclic-convolution`: The first of the two sequences of length n whose cyclic convolution is taken.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences of length n whose cyclic convolution is taken.
- $w$ (formal variable), bound on `cyclic-convolution`: The variable whose powers index the entries of the polynomial that represents a sequence.
- $d$ (number of axes), bound on `cyclic-convolution`: The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $d$ (greatest common divisor), bound on `bezout-identity`: The greatest common divisor of beta and gamma, the largest positive integer dividing both.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $h$ (comparison function), bound on `big-theta-notation`: A second function of the same kind as $u$, against which the growth of $u$ is measured.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $S$ (product of lengths), bound on `modular-inverse`: The product of all the axis lengths M_i.
- $C$ (set of extended reals), bound on `extended-reals`: An arbitrary set of extended real numbers, whose infimum and supremum are taken.
- $m$ (tail start position), bound on `limit-inferior`: The position from which the tail of a sequence starts.
- $C$ (bound constant), bound on `limit-inferior`: A constant in the big-O time bound of the main result.
- $\log$ (base-2 logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm, as used in the expression $n \log n$.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers, a count of bits.
- $f$ (disk-grid ring array), bound on `opposite-transform`: One of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $g$ (second disk-grid ring array), bound on `opposite-transform`: The second of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $w$ (complex vector), bound on `transform-identity`: A complex vector, the argument of the permutation $P_t$ in this page's notation.
- $E$ (entry count), bound on `padded-transform-box`: The number of entries of the box, counting valid and zero entries alike.
- $s$ (sequence length), bound on `normalized-cyclic-convolution`: The number of entries in each input sequence, which is also the length of the transform.
- $\mathcal{C}$ (first event), bound on `independence`: An event, that is, a subset of the sample space.
- $C$ (complementary subspace), bound on `projection-along-subspace`: A subspace of $X$ that meets $U$ only in zero and whose sum with $U$ is all of $X$.
- $v$ (shift vector), bound on `subspace-labels`: A vector in $\mathbb F_2^m$ by which a translation shifts addresses (this letter changes meaning on this page).
- $f$ (function of addresses), bound on `subspace-labels`: A function from addresses in $\mathbb F_2^m$ to values, which a translation shifts (this letter changes meaning on this page).
- $x$ (control vector), bound on `scratch-storage`: The vector of control values, with one entry $x_T$ for each triple $T$.
- $a$ (starting side values), bound on `scratch-storage`: The starting values of the side wires $W_{ST}$.
- $S$ (triple), bound on `scratch-storage`: A three-element subset of the ground set, indexing a target value $y_S$.
- $T$ (triple), bound on `scratch-storage`: A three-element subset of the ground set, indexing a control value $x_T$.
- $x$ (first field), bound on `address-interchange`: One of the two disjoint address fields being interchanged, read as a block of bits.
- $m$ (integer base), bound on `address-interchange`: A fixed integer at least 2, the base in which the field width is written as a power.
- $s$ (call count), bound on `address-interchange`: The number of smaller calls that one call makes.
- $m$ (field count), bound on `address-shear`: The number of fields in each address vector, which is also the size of the square matrix M.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $a$ (rational rank), bound on `address-shear`: The number of linearly independent rows of M over the rational numbers.
- $o$ (selected offset), bound on `simultaneous-butterfly-layer`: The position of the selected bit within its chunk, counted from the least significant end, with $0\le o<\delta$.
- $C$ (two-point kernel), bound on `simultaneous-butterfly-layer`: The $2\times2$ matrix $\mathcal{H}\Delta\mathcal{H}=\lambda I+\mu X$ acting on one selected bit.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number $D$ of selected axes in a layer.
- $s$ (smaller-call count), bound on `numerical-layer`: The number of smaller calls that one call makes.
- $m$ (division factor), bound on `numerical-layer`: The fixed integer by which each call divides its number of axes.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, one of the $D$ axes.
- $b$ (bit length of n), bound on `cost-table`: The rounded-up base-2 logarithm of n, which is the number of bits of n.
- $p$ (working precision), bound on `cost-table`: The working precision in bits, p = 6b, so that p = Theta(log n).
- $T$ (padded box cell count), bound on `cost-table`: The number of cells of the padded box, a power of two with 4n/b <= T < 8n/b.
- $\alpha$ (line-map factor), bound on `cost-table`: The factor of the Gaussian line-map cost, with alpha = Theta(p^{1/4+epsilon/2}).
- $r$ (largest axis length), bound on `cost-table`: The largest axis length of the padded box, a power of two, whose base-two logarithm is ell.
- $\log$ (base-2 logarithm), bound on `established-multiplier`: The base-2 logarithm, the power to which 2 must be raised to give the argument.
- $f$ (first polynomial), bound on `signed-packing`: The first input, an integer polynomial whose coefficients are the $f_j$.
- $g$ (second polynomial), bound on `signed-packing`: The second input, an integer polynomial whose coefficients are the $g_j$.
- $p$ (magnitude exponent), bound on `signed-packing`: The number of bits in the magnitude bound on a coefficient, so each coefficient has magnitude at most $2^p$.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $fg$, a polynomial whose coefficients are the $h_j$.
- $i$ (summation index), bound on `signed-packing`: The index of the sum that gives $h_j$, running over the positions $0$ to $r-1$ of $f$.
- $u$ (first input value), bound on `guard-width-bound`: The first of the two complex input values of the two-point map.
- $v$ (second input value), bound on `guard-width-bound`: The second of the two complex input values of the two-point map.
- $m$ (division factor), bound on `guard-width-bound`: The factor by which a call of the complex phase network divides the number of axes.
- $m$ (event count), bound on `union-bound`: The number of events E_1 through E_m, which here also counts the guards.
- $f$ (selected bit count), bound on `union-bound`: The number of selected bit positions, which fixes the number of guards 2(f-1).
- $L$ (field width), bound on `packed-bit-addition`: The number of address bits in each field, L = fK.
- $i$ (segment index), bound on `packed-bit-addition`: The index of a segment, whose selected position is rho + iK.
- $\gamma$ (guard value), bound on `packed-bit-addition`: The value of the K-1 bits above the selected bit of a segment.
- $o$ (last index), bound on `telescoping-identity`: The index of the last term of the sequence, so the sequence has o+1 terms.
- $i$ (summation index), bound on `mixed-radix-digits`: A place index ranging over the places below a given place $j$.
- $x$ (indeterminate), bound on `chinese-remainder-map`: The indeterminate of the one-dimensional ring, whose powers index positions.
- $u$ (longest axis length), bound on `prime-source-lengths`: The power of two $2^\ell$ that is the common length of the longest axes of the padded box.
- $w$ (axes at half length), bound on `prime-source-lengths`: The number of axes whose padded length is $u/2$, a count with $0\le w<d$.
- $\alpha$ (resampling parameter), bound on `prime-source-lengths`: The real number $(12d^2b)^{1/4}$, a parameter of the source's resampling argument.

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

## Page to audit (`recovery-and-error`)

````markdown
# Exact coefficient recovery

Exact coefficient recovery is the error analysis showing that each convolution coefficient, computed through approximate transforms, lies strictly within one half of its true integer, so rounding returns it exactly. It is the last step of the argument for exact integer multiplication.

## Why rounding recovers the integer

 Distinct integers are at least $1$ apart, so if a computed value $x$ satisfies $|x-m|<1/2$ for an integer $m$, then $m$ is the unique nearest integer and rounding returns $m$. So it suffices to bound each coefficient's total error strictly below $1/2$.

## Units and error sources

Each stored value keeps $p$ fractional bits. Write $h_p = 2^{-p}$ for the size of one unit in the last place; an error of $a$ units is an absolute error below $a\,h_p$. The source sets $b = \lceil\log_2 n\rceil$ and so $h_p = 2^{-6b}$.

This analysis takes its guard widths from the [Guard-width bound](guard-width-bound.md), so every intermediate value is exact. Errors come only from the transforms and the truncations $Q_p$.

## Errors add across stages

 For a bilinear map $\mathcal{C}$ that is a contraction, $\|\mathcal{C}(f,g)\|\le\|f\|\,\|g\|$, and bilinearity gives $\mathcal{C}(f',g')-\mathcal{C}(f,g)=\mathcal{C}(f'-f,g')+\mathcal{C}(f,g'-g)$. Products of approximate operands are [Bilinear map](bilinear-map.md)s, and this analysis bounds the error of each product by $\|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|$: each operand error is weighted by the norm of the other operand. This analysis bounds every operand in the [Array norm](array-norm.md) by one, so each lies in the disk.

## The polynomial-ring stage

Here $T$ counts the entries of the [Padded transform box](padded-transform-box.md). Write $L=\log_2 T$, so $L\le b$; the letter $L$ changes meaning here.

This step bounds the error of the [Convolution over the polynomial ring](polynomial-ring-convolution.md), which is computed from two forward synthetic transforms, a pointwise product and an opposite transform. The stage bound includes the error of the [Opposite transform](opposite-transform.md) and of both forward transforms. Each has error less than $L$ units, and truncating the product adds less than $2$ units: $3L+2$ units of $h_p$. The normalized form scales this by $T/r$, where $r$ is the record length, so the stage error is $E_{\rm ring}=\frac{T}{r}(3L+2)$ units; since $r\ge1$ and $L\ge1$, $E_{\rm ring}<5TL$.

With one operand of norm at most $.7$, the exact output has norm at most $.7$.

The [Phase twist](phase-twist.md) at each end of the ring map adds error too: this analysis bounds the error of the phase twist at each end by $4h_p$. The phase error costs $2\|x\|h_p$, grid truncation adds $2h_p$, and for $\|x\|\le1$. So the complex convolution has error $E_{\rm ring}$ plus three twists:.

## The source transform

Here $\gamma = 2d\alpha^2$ is the construction constant of the source; the letter $\gamma$ changes meaning here. The source transform multiplies grid numerators by $2^\gamma$. Call the source-transform error $E_s$, in units of $h_p$. Multiplying by $2^\gamma$, and using $2dp^2<TL$ for large $n$, gives so $E_s=9\cdot 2^\gamma TL$ units.

The pointwise product adds $2E_s+2$ units and the opposite transform adds $E_s$ more, so the total is $3E_s+2$ units. The first multiplication by $S$, the product of the [Prime source lengths](prime-source-lengths.md), gives the scaled result $\tilde w$, which approximates $w$, the convolution of the digit arrays divided by $S$; call its error $E_w$, in units of $h_p$. Here, and since $S\le T$, $E_w<28\cdot 2^\gamma T^2L$.

## Disk bounds stage by stage

The digit arrays have norm below $1/4$ The scaled source transform is a contraction, so its outputs have norm below $1/4+E_sh_p<.26$, and the truncated product has norm at most $.262<.5$, which the opposite transform accepts. For large $n$, $E_sh_p$, $5TLh_p$ and $E_wh_p$ are all below $10^{-3}$, so $\|\tilde w\|<1/16+10^{-3}<1$.

## Scaling and the final bound

Each scaling is exact on the integer [Grid numerator](grid-numerator.md) of each value, so it adds no error. The final scaling undoes the normalizations of the [Normalization scales](normalization-scales.md): $2^{2b+4}$ reverses the two digit scales, and the factor $S$, the product of the [Prime source lengths](prime-source-lengths.md), reverses the division by $S$ left in $\tilde w$. The result approximates $2^{2b+4}S\,w=2^{2b+4}(u*v)$, with error $2^{2b+4}S\,E_w\,h_p$. Using $E_w<28\cdot 2^\gamma T^2L$ and $h_p=2^{-6b}$,
$$2^{2b+4}S\,E_w\,h_p<2^{2b+4}\cdot S\cdot 28\cdot 2^{\gamma}T^2L\cdot 2^{-6b}=448\,S\,T^2L\,2^{\gamma-4b}.$$
 bound follows: with $S\le T\le 2^b$ and $L\le b$, the right side is at most $448\,b\,2^{\gamma-b}$. The bound uses the growth rule of [Little-o notation](little-o-notation.md) for $\gamma$: $\gamma=o(b)$. Since it is at most $448\,b\,2^{-3b/4}$, which is below $1/2$ for large $n$. Rounding therefore returns each coefficient exactly.
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

Write the answer to `exegenius/tasks/0471-audit-recovery-and-error.answer.json`, then run `exegenius submit 0471-audit-recovery-and-error` in the project directory. If submit rejects the answer, fix the answer and submit again.
