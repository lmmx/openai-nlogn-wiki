# exegenius task 0469-audit-chinese-remainder-map

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
- Packed selected-bit addition (also: exceptional addresses, selected bit)
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
- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $P$ (normalized pointwise product), bound on `pointwise-product`: The map that sends two entries to their product in the ring divided by $r$.
- $A$ (machine), bound on `running-time-cost`: The single machine whose running time the main theorem bounds.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $A$ (source set), bound on `bijection`: The source set, whose elements are the inputs of the map f.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $\pi$ (permutation), bound on `permutation`: The map from S to S that sends each position to its new position.
- $A$ (array), bound on `permutation`: An array of entries stored at addresses, the object that an address permutation moves.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $\lambda$ (evaluation point), bound on `little-o-notation`: The real point at which the functions are evaluated, taken to infinity.
- $A$ (multiplication machine), bound on `little-o-notation`: The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $\gamma$ (second integer), bound on `coprime`: The other integer whose greatest common divisor with beta is taken, not both zero with it.
- $\operatorname{lcm}$ (least common multiple), bound on `coprime`: The function giving the smallest positive integer divisible by each of its integer arguments.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $s_i$ (source length), bound on `coprime`: The i-th of the pairwise coprime axis lengths.
- $P_i$ (prefix product), bound on `coprime`: The product of the lengths s_1 through s_{i-1}, with P_1 equal to 1.
- $\mu_i$ (inverse of prefix product), bound on `coprime`: An integer with P_i mu_i congruent to 1 modulo s_i, the inverse of P_i modulo s_i.
- $\eta$ (second element), bound on `ring-homomorphism`: An arbitrary element of the domain ring.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m	imes m$ matrix with entries in $F$.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $D$ (second field vector), bound on `matrix-rank`: The vector $(D_1, \ldots, D_m)$ of $m$ address fields, which the shear reads without changing.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $D$ (selected bit count), bound on `phase-factor`: The number of selected bits of an address in a layer.
- $C$ (forward kernel), bound on `phase-factor`: The 2 by 2 matrix called the forward kernel.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $\nu$ (second input index), bound on `discrete-fourier-transform`: A second integer index from 0 to q-1 that numbers the input coordinates in the inverse identity.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $D$ (axis count), bound on `transform-axis`: The number of axes of the array, which is also the number of coordinates in each address.
- $x_i$ (axis coordinate), bound on `transform-axis`: The coordinate of an address along axis $i$, an integer from 0 to $t_i - 1$.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $\nu$ (input position), bound on `multidimensional-transform`: A position in the input array, a tuple of D coordinates with the s-th coordinate between 0 and t_s minus 1.
- $\pi$ (circle constant), bound on `multidimensional-transform`: The ratio of a circle's circumference to its diameter.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $e_j$ (input record), bound on `synthetic-transforms`: The $j$-th record of the input list.
- $P$ (ring element), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring $R_r$, given by its representative of degree less than $r$.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\nu$ (exponent), bound on `polynomial-ring-mod-yr-plus-1`: The positive integer power to which a root of unity is raised to give 1, counting the factors of the product.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $x_i$ (digit of x), bound on `radix-digit-convolution`: The digit of $x$ at position $i$, with weight $(2^b)^i$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\nu$ (second numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of the second Gaussian dyadic $\nu/2^{e'}$.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $\nu$ (address), bound on `two-point-kernel`: An integer whose binary form with $d$ bits is one address of an array.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}, the matrix whose tensor powers are taken.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $m$ (tensor power count), bound on `tensor-product`: The number of factors in a tensor power, which counts the coordinates the operator acts on.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $\pi$ (bilinear map), bound on `bilinear-map`: The map sending each pair (e,d) of arguments to a vector pi(e,d) in K, linear in each argument while the other is fixed.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\nu$ (class member), bound on `congruence-modulo`: An integer congruent to d modulo B, a member of the residue class of d.
- $\nu$ (bit column), bound on `binary-change-of-basis`: The column of values of the selected bits, each an element of $\mathbb F_2$.
- $\nu$ (target bank), bound on `bit-network`: The target bank, a vector with one bit for each triple.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $E$.
- $\eta_1$ (first coordinate), bound on `bilinear-form`: The first coordinate of the vector $\eta$ in $\mathbb{Q}^2$.
- $e_i$ (basis vector), bound on `bilinear-form`: The $i$-th vector of the fixed basis of $E$.
- $A$ (form matrix), bound on `bilinear-form`: The $m\times m$ matrix of the form in the chosen basis.
- $\nu$ (integer to reduce), bound on `centered-residue`: The integer whose residue modulo $\kappa$ is taken.
- $\nu$ (congruence index), bound on `chinese-remainder-theorem`: An index numbering the congruences, running from 1 to $\chi$.
- $\Lambda$ (product of moduli), bound on `chinese-remainder-theorem`: The product of the moduli $\kappa_1,\dots,\kappa_\chi$, a positive integer.
- $\Phi$ (coefficient layout map), bound on `cyclic-convolution`: The map sending the cyclic ring to the multidimensional ring, which places each coefficient at an array position.
- $\nu$ (coordinate index), bound on `cyclic-coordinate`: The index naming one cyclic coordinate, running from 1 to d.
- $\mu$ (Bézout coefficient of beta), bound on `bezout-identity`: The integer multiplying beta in the Bézout combination.
- $\nu$ (Bézout coefficient of gamma), bound on `bezout-identity`: The integer multiplying gamma in the Bézout combination.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $\nu$ (exponent), bound on `cyclic-group`: An integer exponent saying which power of the generator $\tau$ is meant.
- $\mu$ (inverse), bound on `modular-inverse`: An integer whose product with beta is congruent to 1 modulo M.
- $\nu$ (quotient integer), bound on `modular-inverse`: The integer with beta mu - 1 = nu M, the quotient (beta mu - 1)/M.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $\pi_i$ (prefix product), bound on `modular-inverse`: The product of the lengths of the axes before axis i.
- $\mu_i$ (inverse of prefix product), bound on `modular-inverse`: The inverse of pi_i modulo M_i.
- $C$ (set of extended reals), bound on `extended-reals`: An arbitrary set of extended real numbers, whose infimum and supremum are taken.
- $m$ (tail start position), bound on `limit-inferior`: The position from which the tail of a sequence starts.
- $C$ (bound constant), bound on `limit-inferior`: A constant in the big-O time bound of the main result.
- $\Lambda$ (diagonal scaling), bound on `transform-identity`: The diagonal scaling on length-$s$ vectors that multiplies each entry by its own nonzero factor.
- $A$ (forward contraction), bound on `transform-identity`: A linear contraction from length-$s$ vectors to length-$t$ vectors.
- $s$ (sequence length), bound on `normalized-cyclic-convolution`: The number of entries in each input sequence, which is also the length of the transform.
- $j$ (record position), bound on `phase-twist`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $C$ (complementary subspace), bound on `projection-along-subspace`: A subspace of $X$ that meets $U$ only in zero and whose sum with $U$ is all of $X$.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of the other bank's entries along the varying coordinate, updated by a forward invocation.
- $x$ (control vector), bound on `scratch-storage`: The vector of control values, with one entry $x_T$ for each triple $T$.
- $a$ (starting side values), bound on `scratch-storage`: The starting values of the side wires $W_{ST}$.
- $c$ (starting central values), bound on `scratch-storage`: The starting values of the central wires $C_\ell$.
- $x$ (first field), bound on `address-interchange`: One of the two disjoint address fields being interchanged, read as a block of bits.
- $m$ (integer base), bound on `address-interchange`: A fixed integer at least 2, the base in which the field width is written as a power.
- $s$ (call count), bound on `address-interchange`: The number of smaller calls that one call makes.
- $j$ (recursion depth), bound on `address-interchange`: The number of levels below the top call, counting from 0 at the top.
- $m$ (field count), bound on `address-shear`: The number of fields in each address vector, which is also the size of the square matrix M.
- $D$ (second address vector), bound on `address-shear`: The vector of m address fields that the shear leaves unchanged.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $a$ (rational rank), bound on `address-shear`: The number of linearly independent rows of M over the rational numbers.
- $e$ (chunk digit count), bound on `address-shear`: The number of radix-q digits in each interchanged chunk, which is m^k at recursion depth k.
- $C$ (two-point kernel), bound on `simultaneous-butterfly-layer`: The $2\times2$ matrix $\mathcal{H}\Delta\mathcal{H}=\lambda I+\mu X$ acting on one selected bit.
- $\lambda$ (identity coefficient), bound on `simultaneous-butterfly-layer`: The complex coefficient $(1+i)/2$ of the identity $I$ in $C$.
- $\mu$ (bit-flip coefficient), bound on `simultaneous-butterfly-layer`: The complex coefficient $(1-i)/2$ of the bit flip $X$ in $C$.
- $e$ (axes per call), bound on `numerical-layer`: The number of selected axes that a call acts on.
- $s$ (smaller-call count), bound on `numerical-layer`: The number of smaller calls that one call makes.
- $m$ (division factor), bound on `numerical-layer`: The fixed integer by which each call divides its number of axes.
- $\mu$ (source dimension total), bound on `rank-saving-recursion`: The sum of the dimensions of the source labels of the network.
- $e$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the selected axes of a numerical layer or the digits of an address field.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, one of the $D$ axes.
- $\eta$ (twiddle exponent), bound on `transform-round`: The exponent of the twiddle at an address, an integer taken modulo $2r$.
- $e$ (quotient of exponent), bound on `transform-round`: The integer quotient of $\eta$ by $r$, which counts the whole multiples of $r$ in $\eta$.
- $b$ (bit length of n), bound on `cost-table`: The rounded-up base-2 logarithm of n, which is the number of bits of n.
- $c$ (chunk exponent), bound on `cost-table`: A fixed positive rational exponent, 2^{-56} in the paper's choice, with K = Theta(p^{epsilon c}).
- $j$ (coefficient position), bound on `signed-packing`: The position of a coefficient in a record, running from 0 to r-1.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
- $i$ (summation index), bound on `signed-packing`: The index of the sum that gives $h_j$, running over the positions $0$ to $r-1$ of $f$.
- $\nu$ (record count), bound on `polynomial-ring-convolution`: The number of records in the array along the remaining axes, which counts the product of the remaining axis lengths.
- $j$ (position index), bound on `polynomial-ring-convolution`: A frequency address of a transform entry, or a coefficient position in the reduction step, a nonnegative integer index.
- $e$ (wrap exponent), bound on `polynomial-ring-convolution`: An integer exponent of y, which may be at least r, so that y^e wraps around with a sign flip.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between the computed input and the exact input $x$, so that the computed input is $x + \eta$.
- $e$ (group size), bound on `guard-width-bound`: The number of selected axes in a group that the recursion splits.
- $A$ (operation bound), bound on `guard-width-bound`: An upper bound on the number of operations on any chain within a group of e axes.
- $m$ (division factor), bound on `guard-width-bound`: The factor by which a call of the complex phase network divides the number of axes.
- $\eta$ (gate constant), bound on `guard-width-bound`: The constant $64(W+m+1)^3$ bounding the operations for gates and corrections at one node.
- $\nu$ (exponent of the factor), bound on `guard-width-bound`: The least integer $j\ge1$ with $m^j\ge\beta$.
- $m$ (event count), bound on `union-bound`: The number of events E_1 through E_m, which here also counts the guards.
- $i$ (segment index), bound on `packed-bit-addition`: The index of a segment, whose selected position is rho + iK.
- $\gamma$ (guard value), bound on `packed-bit-addition`: The value of the K-1 bits above the selected bit of a segment.
- $\eta$ (scratch segment value), bound on `packed-bit-addition`: The integer value of the corresponding segment of the scratch field.
- $e_1$ (source selected bit), bound on `packed-bit-addition`: The top selected bit of the source field in the final two-bit step.
- $e_2$ (target selected bit), bound on `packed-bit-addition`: The top selected bit of the target field in the final two-bit step.
- $\lambda_j$ (place length), bound on `mixed-radix-digits`: The number of values the digit at place $j$ can take.
- $j$ (place index), bound on `mixed-radix-digits`: A position among the places, running from 1 to the number of places.
- $\Lambda$ (product of lengths), bound on `mixed-radix-digits`: The product of all the place lengths, the number of distinct digit strings the system can write.
- $\nu$ (integer being written), bound on `mixed-radix-digits`: A nonnegative integer less than $\Lambda$, whose expansion is sought.
- $e_j$ (digit), bound on `mixed-radix-digits`: The digit of an expansion at place $j$, an integer from $0$ to $\lambda_j-1$.
- $i$ (summation index), bound on `mixed-radix-digits`: A place index ranging over the places below a given place $j$.

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

## Page to audit (`chinese-remainder-map`)

````markdown
# Chinese-remainder map

The Chinese-remainder map is a relabeling of coefficient positions. It is applied to a [cyclic convolution](cyclic-convolution.md) of length $\Lambda$ and turns it into a multidimensional cyclic convolution whose axes have pairwise coprime lengths. It is the step of the [exact multiplication algorithm](main-theorem.md) that places the coefficients of a [radix-digit convolution](radix-digit-convolution.md) on distinct prime cyclic axes, so that later steps can transform each axis separately. It is also called the Agarwal–Cooley map, after cyclic convolution.

There are $D$ cyclic axes, and axis $i$ has $\lambda_i$ positions. The lengths are pairwise coprime: any two have greatest common divisor $1$. Let $\Lambda=\lambda_1\cdots\lambda_D$ be the total number of positions.

Let $x$ be an indeterminate, a formal symbol that is never evaluated, whose powers index positions. (This letter changes meaning from the first input of earlier pages.) The one-dimensional ring is $\mathbb{C}[x]/(x^\Lambda-1)$, and multiplying polynomials here reduces exponents modulo $\Lambda$, which is exactly cyclic convolution of their coefficient lists. The target is the multidimensional ring $\mathbb{C}[x_1,\dots,x_D]/(x_1^{\lambda_1}-1,\dots,x_D^{\lambda_D}-1)$, where $x_i$ is the indeterminate of axis $i$. Its monomials $x_1^{\eta_1}\cdots x_D^{\eta_D}$ have $\eta_i$ as the exponent of $x_i$ (the letter $\eta_i$ changes meaning from earlier pages). The monomials with $0\le\eta_i<\lambda_i$ for every $i$ form a basis of $\Lambda$ elements, since each exponent is chosen from $\lambda_i$ values.

For axis $i$, let $\pi_i=\lambda_1\cdots\lambda_{i-1}$ (so $\pi_1=1$), and let $\mu_i$ be an inverse of $\pi_i$ modulo $\lambda_i$, so $\mu_i\pi_i\equiv 1 \pmod{\lambda_i}$. It exists because each $\lambda_j$ with $j<i$ is coprime to $\lambda_i$, so $\pi_i$ is too.

Define $\Phi$ on the generator $x$ by $\Phi(x)=\prod_{i=1}^D x_i^{\mu_i}$; it is extended to polynomials as a [ring homomorphism](ring-homomorphism.md), which is well defined because $\Phi(x)^\Lambda=\prod_i x_i^{\mu_i\Lambda}$ and each $\lambda_i$ divides $\Lambda$, so every factor is $1$.

For an integer $\nu\ge 0$ (an exponent; the letter changes meaning from earlier pages), $\Phi(x)^\nu=\prod_i x_i^{\mu_i\nu}$ equals $1$ exactly when $\lambda_i\mid\nu$ for every $i$, because each $\mu_i$ is invertible modulo $\lambda_i$. That holds exactly when $\operatorname{lcm}(\lambda_1,\dots,\lambda_D)\mid\nu$, and for pairwise coprime lengths the lcm is $\Lambda$. So $\Phi(x)$ has order $\Lambda$. Let $e$ be an ordinary coefficient index, $0\le e<\Lambda$. The powers $\Phi(x)^e$ are distinct, since $\Phi(x)^a=\Phi(x)^b$ with $0\le a<b<\Lambda$ would give $\Lambda\mid b-a$. Each is a basis monomial once its exponents are reduced modulo the $\lambda_i$. These $\Lambda$ distinct monomials exhaust the basis, so the powers

Hence $\Phi$ maps the basis $1,x,\dots,x^{\Lambda-1}$ bijectively onto the monomial basis of the target, so $\Phi$ is a [ring isomorphism](ring-homomorphism.md). The product of two coefficient polynomials maps to the product of their images, a multidimensional cyclic convolution on the axes $\lambda_1,\dots,\lambda_D$.

Each index $e$ has [mixed-radix digits](mixed-radix-digits.md) $e_1,\dots,e_D$, where $e_j$ is the digit on axis $j$ and $0\le e_j<\lambda_j$. They satisfy $e=\sum_{j=1}^D e_j\pi_j$. The Chinese-remainder map computes its coordinates from the [mixed-radix digits](mixed-radix-digits.md) of $e$. Let $\gamma_i\in[0,\lambda_i)$ be the coordinate of $e$ on axis $i$, the exponent of $x_i$ in $\Phi(x^e)$ reduced modulo $\lambda_i$ (the letter $\gamma_i$ changes meaning from earlier pages).

Since $\Phi(x^e)=\prod_i x_i^{\mu_i e}$, $\gamma_i$ is $\mu_i e$ reduced modulo $\lambda_i$. Substituting the digits gives
$$\mu_i e=\mu_i e_i\pi_i+\mu_i\sum_{j<i}e_j\pi_j+\sum_{j>i}\mu_i e_j\pi_j.$$
For $j>i$, $\pi_j$ contains the factor $\lambda_i$, so the last sum vanishes modulo $\lambda_i$. (the source writes $s_i$ and $P_i$ for $\lambda_i$ and $\pi_i$). The first term is $e_i(\mu_i\pi_i)\equiv e_i$, so
$$\gamma_i\equiv e_i+\mu_i\sum_{j<i}e_j\pi_j \pmod{\lambda_i}.$$

Take $D=2$, $\lambda_1=3$, $\lambda_2=5$, so $\Lambda=15$. Then $\pi_2=3$, $\mu_1=1$, and $\mu_2=2$ because $3\cdot 2=6\equiv 1 \pmod 5$. So $\Phi(x)=x_1x_2^2$. The index $e=7$ has digits $e_1=1$ and $e_2=2$, since $7=1+3\cdot 2$. Its coordinates are $\gamma_1=1$ and $\gamma_2\equiv 2+2\cdot 1\cdot 1=4 \pmod 5$. Directly, $\Phi(x)^7=x_1^7x_2^{14}=x_1x_2^4$, since $7\equiv 1 \pmod 3$ and $14\equiv 4 \pmod 5$. So index $7$ sits at address $(1,4)$ on the $3\times 5$ grid.

The map only moves coefficients: each keeps its value and changes its address. Evaluating $x_i$ at the $\lambda_i$-th roots of unity is a ring isomorphism from $\mathbb{C}[x_i]/(x_i^{\lambda_i}-1)$ onto $\mathbb{C}^{\lambda_i}$, the [discrete Fourier transform](discrete-fourier-transform.md) of length $\lambda_i$. Doing this on every axis gives an isomorphism onto $\mathbb{C}^{\Lambda}$ whose matrix is the [tensor product](tensor-product.md) of the one-axis transforms. A tensor product $A_1\otimes\cdots\otimes A_D$ applies $A_i$ along axis $i$ alone, so a transform on the product ring is a transform on each axis separately, and each axis is a shorter cyclic convolution. Pairwise coprimality keeps $\Phi$ injective: shared factors would make the lcm smaller than $\Lambda$, and two powers of $\Phi(x)$ would coincide. Distinct primes are pairwise coprime, so the construction applies to distinct prime axis lengths.
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

Write the answer to `exegenius/tasks/0469-audit-chinese-remainder-map.answer.json`, then run `exegenius submit 0469-audit-chinese-remainder-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
