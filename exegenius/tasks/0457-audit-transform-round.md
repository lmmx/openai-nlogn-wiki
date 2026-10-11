# exegenius task 0457-audit-transform-round

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
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks, address-field interchange procedure, field interchanges)
- Address shear (also: shear of address pairs, Matrix shear)
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant, orthogonal residual of an edge)
- Simultaneous butterfly layer (also: selected bits, two-point operator on selected bits)
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
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
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
- Truncation
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
- Tape procedure
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $y$ (positive number), bound on `logarithm`: The positive number whose logarithm to base $b$ is taken.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $y$ (polynomial variable), bound on `root-of-unity`: The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, which is a root of unity in that ring.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $y$ (indeterminate), bound on `pointwise-product`: The indeterminate of the quotient ring $\mathbb{C}[y]/(y^r+1)$ whose elements are the entries.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary input string, of length $n$.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $H$ (layer), bound on `truncation`: The operation that applies a two-point map to each pair of entries whose addresses differ in one of several selected bits, in one pass.
- $\beta$ (second paired value), bound on `truncation`: The second of the two values that the layer combines in each pair.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $h$ (chunk index), bound on `destination-rank`: The index of a chunk of an address, taking the value 1, 2 or 3.
- $y$ (indeterminate), bound on `polynomial-ring`: The formal variable of the polynomials in the ring.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $X$ (array), bound on `array-norm`: A finite array of complex values.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $\|X\|$ (array norm), bound on `array-norm`: The largest modulus |u| over all entries u of the array X.
- $y$ (polynomial variable), bound on `array-norm`: The variable of the polynomials in the ring modulo y^r + 1.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $y$ (target indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q'$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\eta$ (second element), bound on `ring-homomorphism`: An arbitrary element of the domain ring.
- $\delta$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $t$ in an element $\alpha+\delta t$ of $Q$.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $y$ (second vector), bound on `linear-algebra-basics`: A vector over $F$, a second arbitrary vector.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $H$ (address chunk), bound on `linear-algebra-basics`: A binary address chunk, one of the two fields of an address pair.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $\ell$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $H$ (first address field), bound on `linear-network-frames`: The first of two address fields, written as a vector.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set, so it counts those elements.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $J$ (all-one matrix), bound on `eigenvalue`: The h by h matrix with every entry equal to 1.
- $J$ (all-ones matrix), bound on `indicator-vector`: The h by h matrix with every entry equal to 1.
- $H$ (first field vector), bound on `matrix-rank`: The vector $(H_1, \ldots, H_m)$ of $m$ address fields that the shear updates.
- $D$ (second field vector), bound on `matrix-rank`: The vector $(D_1, \ldots, D_m)$ of $m$ address fields, which the shear reads without changing.
- $\ell$ (column index), bound on `matrix-rank`: The column of a one in $\Pi$, which is also the index of the field $D_\ell$ it uses.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number tau, a real number.
- $D$ (selected bit count), bound on `phase-factor`: The number of selected bits of an address in a layer.
- $C$ (forward kernel), bound on `phase-factor`: The 2 by 2 matrix called the forward kernel.
- $\omega$ (primitive root of unity), bound on `discrete-fourier-transform`: The primitive q-th root of unity $e^{-2\pi i/q}$, a complex number whose q-th power is 1.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the output coordinates.
- $\nu$ (second input index), bound on `discrete-fourier-transform`: A second integer index from 0 to q-1 that numbers the input coordinates in the inverse identity.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $D$ (axis count), bound on `transform-axis`: The number of axes of the array, which is also the number of coordinates in each address.
- $y$ (polynomial indeterminate), bound on `transform-axis`: The indeterminate of the polynomial modulo $y^s+1$; its powers serve as roots of unity on the remaining axes.
- $\nu$ (input position), bound on `multidimensional-transform`: A position in the input array, a tuple of D coordinates with the s-th coordinate between 0 and t_s minus 1.
- $y$ (polynomial variable), bound on `multidimensional-transform`: The variable of the polynomial that stores one coordinate of the array.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The variable of the polynomial ring $R_r$, in which $y^r$ is identified with $-1$.
- $r$ (record length), bound on `synthetic-transforms`: A power of two, the number of complex coefficients in a record.
- $\delta$ (half block size), bound on `synthetic-transforms`: The number of positions in half of a block at a level, taking the values $1, 2, \dots, N/2$.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\nu$ (exponent), bound on `polynomial-ring-mod-yr-plus-1`: The positive integer power to which a root of unity is raised to give 1, counting the factors of the product.
- $H_0$ (butterfly map), bound on `butterfly`: The two-point map sending a pair of values to its half-sum and half-difference.
- $\delta$ (first input value), bound on `butterfly`: The first of the two input values of the butterfly.
- $\ell$ (halving count), bound on `gaussian-resampling`: The number of halvings of a transform length, so that the length is $2^\ell$.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on `gaussian-resampling`: A generic vector of length $t$, on which $P_t$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $\delta$ (Gaussian integer numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of a Gaussian dyadic $\delta/2^e$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\nu$ (second numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of the second Gaussian dyadic $\nu/2^{e'}$.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $\delta$ (diagonal coefficient), bound on `two-point-kernel`: The coefficient of $I$ in $K$, a complex number.
- $X$ (bit flip), bound on `two-point-kernel`: The $2\times 2$ matrix that interchanges the two entries of a pair.
- $\nu$ (address), bound on `two-point-kernel`: An integer whose binary form with $d$ bits is one address of an array.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $H$ (second argument space), bound on `bilinear-map`: The vector space containing the second argument d of the bilinear map.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\nu$ (class member), bound on `congruence-modulo`: An integer congruent to d modulo B, a member of the residue class of d.
- $\delta$ (remainder), bound on `congruence-modulo`: The integer in {0,...,B-1} that is the remainder of a residue class.
- $\nu$ (bit column), bound on `binary-change-of-basis`: The column of values of the selected bits, each an element of $\mathbb F_2$.
- $\nu$ (target bank), bound on `bit-network`: The target bank, a vector with one bit for each triple.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $E$.
- $J$ (all-one matrix), bound on `bilinear-form`: The $h\times h$ matrix whose entries are all $1$.
- $v$ (nonzero vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $\nu$ (integer to reduce), bound on `centered-residue`: The integer whose residue modulo $\kappa$ is taken.
- $\nu$ (congruence index), bound on `chinese-remainder-theorem`: An index numbering the congruences, running from 1 to $\chi$.
- $\nu$ (coordinate index), bound on `cyclic-coordinate`: The index naming one cyclic coordinate, running from 1 to d.
- $\nu$ (Bézout coefficient of gamma), bound on `bezout-identity`: The integer multiplying gamma in the Bézout combination.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $h$ (comparison function), bound on `big-theta-notation`: A second function of the same kind as $u$, against which the growth of $u$ is measured.
- $\nu$ (exponent), bound on `cyclic-group`: An integer exponent saying which power of the generator $\tau$ is meant.
- $\beta$ (integer to invert), bound on `modular-inverse`: The integer whose inverse modulo M is sought.
- $\nu$ (quotient integer), bound on `modular-inverse`: The integer with beta mu - 1 = nu M, the quotient (beta mu - 1)/M.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $C$ (set of extended reals), bound on `extended-reals`: An arbitrary set of extended real numbers, whose infimum and supremum are taken.
- $\delta$ (sequence position), bound on `extended-reals`: The position of a term in a sequence of extended real numbers, running over 1, 2, 3, and so on.
- $C$ (bound constant), bound on `limit-inferior`: A constant in the big-O time bound of the main result.
- $\bmod$ (remainder modulo q), bound on `bluestein-chirp-identity`: x mod q is the remainder of the integer x on division by q, a position in {0,...,q-1}.
- $j$ (record position), bound on `phase-twist`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $\delta$ (first digit array), bound on `normalization-scales`: The integer digit array of the first input, whose entries lie between $0$ and $2^b-1$.
- $C$ (complementary subspace), bound on `projection-along-subspace`: A subspace of $X$ that meets $U$ only in zero and whose sum with $U$ is all of $X$.
- $H$ (Hadamard matrix), bound on `subspace-labels`: The $2\times 2$ matrix with entries $\pm 1/\sqrt2$ that defines the frame $C_U$ through its tensor powers.
- $\delta$ (kernel coefficient delta), bound on `subspace-labels`: The second Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $v$ (shift vector), bound on `subspace-labels`: A vector in $\mathbb F_2^m$ by which a translation shifts addresses (this letter changes meaning on this page).
- $X$ (bank X), bound on `subset-intersection-network`: One of the two banks of scalars, with entries $X_\tau$ indexed by triples of triples.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of the other bank's entries along the varying coordinate, updated by a forward invocation.
- $\ell$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, whose central wire is $C_\ell$.
- $\delta$ (vector of E), bound on `subset-intersection-network`: A vector of the ambient space $E=\mathbb Q^h$, an argument of the bit network form.
- $\delta$ (route step), bound on `complex-phase-network`: The index of a step along the coordinate route, running from one to $m$.
- $x$ (control vector), bound on `scratch-storage`: The vector of control values, with one entry $x_T$ for each triple $T$.
- $y$ (target vector), bound on `scratch-storage`: The vector of target values, with one entry $y_S$ for each triple $S$.
- $c$ (starting central values), bound on `scratch-storage`: The starting values of the central wires $C_\ell$.
- $J$ (side injection), bound on `scratch-storage`: The operator that adds to $y_S$ the side wires $W_{ST}$ summed over the neighbours $T$ of $S$.
- $\ell$ (ground element), bound on `scratch-storage`: An element of the ground set, indexing the central wires $C_\ell$.
- $x$ (first field), bound on `address-interchange`: One of the two disjoint address fields being interchanged, read as a block of bits.
- $y$ (second field), bound on `address-interchange`: The other of the two disjoint address fields being interchanged, read as a block of bits.
- $j$ (recursion depth), bound on `address-interchange`: The number of levels below the top call, counting from 0 at the top.
- $\delta$ (first bit), bound on `xor`: A bit, one of the two inputs to the exclusive or.
- $H$ (first address vector), bound on `address-shear`: The vector of m address fields that the shear changes.
- $D$ (second address vector), bound on `address-shear`: The vector of m address fields that the shear leaves unchanged.
- $e$ (chunk digit count), bound on `address-shear`: The number of radix-q digits in each interchanged chunk, which is m^k at recursion depth k.
- $\delta$ (chunk width), bound on `simultaneous-butterfly-layer`: The number of consecutive address bits in each chunk, one chunk per transform axis.
- $\mathcal{H}$ (normalized Hadamard matrix), bound on `simultaneous-butterfly-layer`: The $2\times2$ matrix $\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, equal to $\sqrt2\,H_0$.
- $X$ (bit-flip matrix), bound on `simultaneous-butterfly-layer`: The $2\times2$ matrix swapping the two coordinates of a bit.
- $C$ (two-point kernel), bound on `simultaneous-butterfly-layer`: The $2\times2$ matrix $\mathcal{H}\Delta\mathcal{H}=\lambda I+\mu X$ acting on one selected bit.
- $e$ (axes per call), bound on `numerical-layer`: The number of selected axes that a call acts on.
- $e$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the selected axes of a numerical layer or the digits of an address field.
- $\delta$ (cost per unit volume), bound on `rank-saving-recursion`: The cost of a call at parameter e divided by its volume.

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

## Page to audit (`transform-round`)

````markdown
# Transform round

A transform round is one stage of the [multidimensional transform](multidimensional-transform.md): every participating axis takes one butterfly step at once, then the twiddles are applied. It is the basic step of the transforms behind [convolution over the polynomial ring](polynomial-ring-convolution.md). Its claim is that the round is a contraction in the array norm $\|X\|$ of an array $X$, the largest modulus of its entries.

A *butterfly* on one axis takes each pair of entries $u,v$ that differ only in one address bit to $\left(\frac{u+v}{2},\frac{u-v}{2}\right)$, their half-sum and half-difference, the two-point map $H_0$. A *twiddle* is a power of $y$ by which a record is multiplied after a butterfly.

Let $D$ be the number of participating axes, and let $i$ index them (the letter changes meaning here). Let $\ell_i$ be the current recursive length of axis $i$, the entries it holds at the level processed. Let $\beta_i\in\{0,1\}$ be the branch bit the round writes on axis $i$. Let $\nu_i$ be the index of the twiddle on axis $i$, with $0\le\nu_i<\ell_i/2$.

Address bits are processed The bit receiving $\beta_i$ is the highest unprocessed bit $h$. $\nu_i=\sum_{v=0}^{h-1}2^v x_v$, where $x_v$ is the bit at position $v$.

At current length $\ell$, the branch-1 output is multiplied by $\omega_\ell^{-\nu}$, where $\omega_\ell=y^{2r/\ell}$ is a primitive $\ell$-th root of unity in $\mathbb{C}[y]/(y^r+1)$.. So axis $i$ contributes $y^{-(2r/\ell_i)\beta_i\nu_i}$ at each address.

 Since $H_0(cu,cv)=c\,H_0(u,v)$, a factor common to the pair moves past the butterfly. Hence the individual axis steps.

The parallel butterfly $\mathcal{H}$ applies $H_0$ on every participating axis. A transform round computes its butterfly by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which applies $\mathcal{H}$ in one pass. The letter $\eta$ changes meaning here: it is the twiddle exponent at each address, an integer taken modulo $2r$, given by

$$
\eta = -\sum_{i} \frac{2r}{\ell_i}\,\beta_i\,\nu_i \pmod{2r},
$$

summed over the $D$ participating axes. The monomial operation $\mathcal{J}_\eta$ multiplies each record by $y^\eta$ at its address.

Write $\eta=er+\delta$ with $0\le\delta<r$, where $e$ is the integer quotient of $\eta$ by $r$, the number of whole multiples of $r$ in $\eta$ (the letter $e$ changes meaning here), and $\delta$ is the remainder. Since $y^r=-1$, $y^\eta=(-1)^e\,y^\delta$. Multiplying by $y^\delta$ shifts coefficients up $\delta$ places, negating those that pass the top. The source does this by.

Take $r=4$, $D=2$, $\ell_1=\ell_2=4$, $\beta_1=1$, $\nu_1=1$, $\beta_2=0$, $\nu_2=1$. Then $\eta=-(2\cdot1\cdot1+2\cdot0\cdot1)\bmod 8=6$, and $y^6=-y^2$ modulo $y^4+1$. With the record $c_0+c_1y+c_2y^2+c_3y^3$, where $c_j$ is the coefficient of $y^j$, the coefficient list $(c_0,c_1,c_2,c_3)$ becomes $(c_2,c_3,-c_0,-c_1)$.

A *contraction* is a linear map that does not increase the array norm, and an *isometry* preserves it. A single $H_0$ sends $(u,v)$ to values of modulus at most $\max(|u|,|v|)$, so $H_0$, and hence $\mathcal{H}$, is a contraction. Multiplying by $y^\eta$ only moves coefficients and changes signs, so $\mathcal{J}_\eta$ is an isometry., so the round is a contraction.
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

Write the answer to `exegenius/tasks/0457-audit-transform-round.answer.json`, then run `exegenius submit 0457-audit-transform-round` in the project directory. If submit rejects the answer, fix the answer and submit again.
