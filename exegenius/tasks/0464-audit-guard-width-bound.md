# exegenius task 0464-audit-guard-width-bound

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

- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $A$ (machine), bound on `running-time-cost`: The single machine whose running time the main theorem bounds.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $Q_p$ (truncation map), bound on `truncation`: The map that truncates each real and imaginary part of each coefficient of a list toward zero to the grid $2^{-p}\mathbb{Z}$.
- $\beta$ (second paired value), bound on `truncation`: The second of the two values that the layer combines in each pair.
- $A$ (source set), bound on `bijection`: The source set, whose elements are the inputs of the map f.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $E$ (subset of source), bound on `bijection`: A subset of the source set A, whose image under a bijection is compared with the image of its complement.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $A$ (array), bound on `permutation`: An array of entries stored at addresses, the object that an address permutation moves.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $A$ (multiplication machine), bound on `little-o-notation`: The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $\mathbb{Z}$ (integers), bound on `coprime`: The set of all integers.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $Q$ (quotient ring), bound on `ring-homomorphism`: The ring of complex polynomials in $t$ in which $t^2=1$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\eta$ (second element), bound on `ring-homomorphism`: An arbitrary element of the domain ring.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m	imes m$ matrix with entries in $F$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $\ell$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $\varepsilon$ (routing sign), bound on `linear-network-frames`: The fixed sign by which the network multiplies the value routed from input role $\ell$.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $D$ (second field vector), bound on `matrix-rank`: The vector $(D_1, \ldots, D_m)$ of $m$ address fields, which the shear reads without changing.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $\ell$ (column index), bound on `matrix-rank`: The column of a one in $\Pi$, which is also the index of the field $D_\ell$ it uses.
- $W$ (wire count), bound on `matrix-rank`: The number of wires in the network, which counts the edges that carry edge changes.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number tau, a real number.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $D$ (selected bit count), bound on `phase-factor`: The number of selected bits of an address in a layer.
- $C$ (forward kernel), bound on `phase-factor`: The 2 by 2 matrix called the forward kernel.
- $Z$ (sign matrix), bound on `phase-factor`: The diagonal matrix diag(1,-1), which negates the entry whose bit is 1.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the output coordinates.
- $\nu$ (second input index), bound on `discrete-fourier-transform`: A second integer index from 0 to q-1 that numbers the input coordinates in the inverse identity.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $D$ (axis count), bound on `transform-axis`: The number of axes of the array, which is also the number of coordinates in each address.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $\nu$ (input position), bound on `multidimensional-transform`: A position in the input array, a tuple of D coordinates with the s-th coordinate between 0 and t_s minus 1.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $Z$ (transformed list), bound on `synthetic-transforms`: The output list of records produced by the transform.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\nu$ (exponent), bound on `polynomial-ring-mod-yr-plus-1`: The positive integer power to which a root of unity is raised to give 1, counting the factors of the product.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $\ell$ (halving count), bound on `gaussian-resampling`: The number of halvings of a transform length, so that the length is $2^\ell$.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on `gaussian-resampling`: A generic vector of length $t$, on which $P_t$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $E$ (map into length t), bound on `gaussian-resampling`: A linear contraction from length-$s$ vectors to length-$t$ vectors, in the identity.
- $\mathbb{Z}[i]$ (Gaussian integers), bound on `gaussian-dyadics`: The set of complex numbers whose real and imaginary parts are integers.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\nu$ (second numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of the second Gaussian dyadic $\nu/2^{e'}$.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $\mathbb{Z}[i]$ (Gaussian integers), bound on `gaussian-integer`: The set of all Gaussian integers.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $\nu$ (address), bound on `two-point-kernel`: An integer whose binary form with $d$ bits is one address of an array.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $Q$ (second matrix), bound on `tensor-product`: A second matrix, the right factor in the tensor product P\otimes Q.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $m$ (tensor power count), bound on `tensor-product`: The number of factors in a tensor power, which counts the coordinates the operator acts on.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $E$ (first argument space), bound on `bilinear-map`: The vector space containing the first argument e of the bilinear map.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\mathbb{Z}$ (integers), bound on `grid-numerator`: The set of integers, whose elements are the whole numbers, which may be negative.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\mathbb{Z}$ (integers), bound on `congruence-modulo`: The set of all integers.
- $\nu$ (class member), bound on `congruence-modulo`: An integer congruent to d modulo B, a member of the residue class of d.
- $\nu$ (bit column), bound on `binary-change-of-basis`: The column of values of the selected bits, each an element of $\mathbb F_2$.
- $\nu$ (target bank), bound on `bit-network`: The target bank, a vector with one bit for each triple.
- $E$ (vector space), bound on `bilinear-form`: A vector space over the field $F$ of scalars, on which the bilinear form is defined.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $E$.
- $A$ (form matrix), bound on `bilinear-form`: The $m\times m$ matrix of the form in the chosen basis.
- $E$ (vector space), bound on `line-spanned-by-vector`: A vector space over K, containing the nonzero vector v.
- $v$ (nonzero vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $\nu$ (integer to reduce), bound on `centered-residue`: The integer whose residue modulo $\kappa$ is taken.
- $\nu$ (congruence index), bound on `chinese-remainder-theorem`: An index numbering the congruences, running from 1 to $\chi$.
- $d$ (number of axes), bound on `cyclic-convolution`: The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $\varepsilon$ (exponent offset), bound on `cyclic-convolution`: The amount by which a reduced exponent exceeds n.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\nu$ (coordinate index), bound on `cyclic-coordinate`: The index naming one cyclic coordinate, running from 1 to d.
- $d$ (greatest common divisor), bound on `bezout-identity`: The greatest common divisor of beta and gamma, the largest positive integer dividing both.
- $\nu$ (Bézout coefficient of gamma), bound on `bezout-identity`: The integer multiplying gamma in the Bézout combination.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $\Theta$ (Big-Theta), bound on `big-theta-notation`: The notation stating that $u$ and $h$ have the same order up to constant factors for large inputs.
- $C_1$ (lower factor), bound on `big-theta-notation`: A positive real constant multiplying $h$ in the lower bound.
- $\nu$ (exponent), bound on `cyclic-group`: An integer exponent saying which power of the generator $\tau$ is meant.
- $\beta$ (integer to invert), bound on `modular-inverse`: The integer whose inverse modulo M is sought.
- $\nu$ (quotient integer), bound on `modular-inverse`: The integer with beta mu - 1 = nu M, the quotient (beta mu - 1)/M.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $C$ (set of extended reals), bound on `extended-reals`: An arbitrary set of extended real numbers, whose infimum and supremum are taken.
- $m$ (tail start position), bound on `limit-inferior`: The position from which the tail of a sequence starts.
- $\varepsilon$ (positive tolerance), bound on `limit-inferior`: A positive real number used as a tolerance in a limit criterion.
- $C$ (bound constant), bound on `limit-inferior`: A constant in the big-O time bound of the main result.
- $\log$ (base-2 logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm, as used in the expression $n \log n$.
- $A$ (forward contraction), bound on `transform-identity`: A linear contraction from length-$s$ vectors to length-$t$ vectors.
- $E$ (entry count), bound on `padded-transform-box`: The number of entries of the box, counting valid and zero entries alike.
- $s$ (sequence length), bound on `normalized-cyclic-convolution`: The number of entries in each input sequence, which is also the length of the transform.
- $j$ (record position), bound on `phase-twist`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $\Theta$ (projection along C), bound on `projection-along-subspace`: The map sending each vector $x$ of $X$ to its component $x_U$ in $U$, for the chosen $U$ and $C$.
- $C$ (complementary subspace), bound on `projection-along-subspace`: A subspace of $X$ that meets $U$ only in zero and whose sum with $U$ is all of $X$.
- $v$ (shift vector), bound on `subspace-labels`: A vector in $\mathbb F_2^m$ by which a translation shifts addresses (this letter changes meaning on this page).
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of the other bank's entries along the varying coordinate, updated by a forward invocation.
- $\ell$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, whose central wire is $C_\ell$.
- $\Delta$ (orthogonal residual), bound on `complex-phase-network`: The orthogonal residual of an edge, the orthogonal complement of its smaller label inside its larger label.
- $x$ (control vector), bound on `scratch-storage`: The vector of control values, with one entry $x_T$ for each triple $T$.
- $\ell$ (ground element), bound on `scratch-storage`: An element of the ground set, indexing the central wires $C_\ell$.
- $x$ (first field), bound on `address-interchange`: One of the two disjoint address fields being interchanged, read as a block of bits.
- $m$ (integer base), bound on `address-interchange`: A fixed integer at least 2, the base in which the field width is written as a power.
- $W$ (piece count), bound on `address-interchange`: The number of equal pieces the volume is cut into at each call, at least 2.
- $s$ (call count), bound on `address-interchange`: The number of smaller calls that one call makes.
- $j$ (recursion depth), bound on `address-interchange`: The number of levels below the top call, counting from 0 at the top.
- $m$ (field count), bound on `address-shear`: The number of fields in each address vector, which is also the size of the square matrix M.
- $D$ (second address vector), bound on `address-shear`: The vector of m address fields that the shear leaves unchanged.
- $\mathbb{Z}$ (integers), bound on `address-shear`: The set of all integers.
- $e$ (chunk digit count), bound on `address-shear`: The number of radix-q digits in each interchanged chunk, which is m^k at recursion depth k.
- $o$ (selected offset), bound on `simultaneous-butterfly-layer`: The position of the selected bit within its chunk, counted from the least significant end, with $0\le o<\delta$.
- $\Delta$ (diagonal phase matrix), bound on `simultaneous-butterfly-layer`: The diagonal $2\times2$ matrix $\mathrm{diag}(1,i)$ that multiplies one basis entry by $i$.
- $C$ (two-point kernel), bound on `simultaneous-butterfly-layer`: The $2\times2$ matrix $\mathcal{H}\Delta\mathcal{H}=\lambda I+\mu X$ acting on one selected bit.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number $D$ of selected axes in a layer.
- $e$ (axes per call), bound on `numerical-layer`: The number of selected axes that a call acts on.
- $s$ (smaller-call count), bound on `numerical-layer`: The number of smaller calls that one call makes.
- $W$ (role count), bound on `numerical-layer`: The number of roles among which rows are distributed.
- $m$ (division factor), bound on `numerical-layer`: The fixed integer by which each call divides its number of axes.
- $\Delta$ (signed dimension change), bound on `rank-saving-recursion`: The change in label dimension along an edge from tail label U to head label U', negative on a decreasing edge.
- $e$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the selected axes of a numerical layer or the digits of an address field.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, one of the $D$ axes.
- $\eta$ (twiddle exponent), bound on `transform-round`: The exponent of the twiddle at an address, an integer taken modulo $2r$.
- $e$ (quotient of exponent), bound on `transform-round`: The integer quotient of $\eta$ by $r$, which counts the whole multiples of $r$ in $\eta$.
- $p$ (working precision), bound on `cost-table`: The working precision in bits, p = 6b, so that p = Theta(log n).
- $\log$ (base-2 logarithm), bound on `established-multiplier`: The base-2 logarithm, the power to which 2 must be raised to give the argument.
- $j$ (coefficient position), bound on `signed-packing`: The position of a coefficient in a record, running from 0 to r-1.
- $p$ (magnitude exponent), bound on `signed-packing`: The number of bits in the magnitude bound on a coefficient, so each coefficient has magnitude at most $2^p$.
- $i$ (summation index), bound on `signed-packing`: The index of the sum that gives $h_j$, running over the positions $0$ to $r-1$ of $f$.
- $\Theta$ (forward transform), bound on `polynomial-ring-convolution`: The forward transform along the remaining axes, normalized by 1/t on each axis of length t.
- $\nu$ (record count), bound on `polynomial-ring-convolution`: The number of records in the array along the remaining axes, which counts the product of the remaining axis lengths.
- $j$ (position index), bound on `polynomial-ring-convolution`: A frequency address of a transform entry, or a coefficient position in the reduction step, a nonnegative integer index.
- $e$ (wrap exponent), bound on `polynomial-ring-convolution`: An integer exponent of y, which may be at least r, so that y^e wraps around with a sign flip.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between the computed input and the exact input $x$, so that the computed input is $x + \eta$.

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

## Page to audit (`guard-width-bound`)

````markdown
# Guard-width bound

The guard-width bound makes every intermediate coefficient of one [simultaneous butterfly layer](simultaneous-butterfly-layer.md) exact, by reserving an explicit count $\Delta$ of extra fractional and integer bits per real component, so that a single final truncation suffices.

The two-point map sends two complex input values $u,v$ (these letters change meaning here) to $((u+v)/2,\ (u-v)/2)$. The layer applies it on $D$ selected axes, and $d\ge D$ bounds $D$. The bound applies to the output of the [tensor product](tensor-product.md) of $D$ copies of the map. Its entries are $\pm\tfrac12$, so each output is $2^{-D}$ times a signed sum of inputs.

The bound must allow for operators that are not [linear contractions](linear-contraction.md), meaning linear maps that can increase the largest modulus of a vector. Rounding after each stage would be unsafe, since errors need not shrink.

Intermediate values are exact [Gaussian dyadics](gaussian-dyadics.md), so the bound must limit the denominators of the values. Inputs lie in $2^{-p}\mathbb{Z}[i]$ with modulus at most $1$, where $p$ is the fractional precision.

Let $\ell$ be the depth of a value, the number of operations on a chain that follows an operand from an input into it. A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb{Z}[i]$ with modulus at most $2^\ell$. By induction on $\ell$, operands of depth $\ell-1$ lie in $2^{-(p+\ell)}\mathbb{Z}[i]$ with modulus at most $2^{\ell-1}$, so a sum has modulus at most $2^\ell$. A halving adds one denominator bit.

The recursion is that of the [complex phase network](complex-phase-network.md): a group of $e$ selected axes splits into $s$ calls on groups of $e/m$ axes, where $W$ is the wire count, $s$ the smaller-call count, and $m$ the factor by which a call divides the axis count (the letter $m$ changes meaning here). Let $A(e)$ bound the operations on any chain within such a group. A chain is charged for all $s$ calls, plus at most $\eta=64(W+m+1)^3$ operations for the gates at the node (, the paper's $E$). Hence at an internal node, and $A(e)\le8e$ at a leaf.

Each level divides the axis count by $m$, so there are at most $\lceil\log_m d\rceil$ internal levels. Put $\beta=s+\eta$. For $x\ge1$, $sx+\eta\le\beta x$, so each level multiplies a bound of at least $1$ by $\beta$. From the leaf bound $8d\le8d\beta$, we get $A(e)\le8d\beta^{\lceil\log_m d\rceil+1}$. Let $\nu$ be the least $j\ge1$ with $m^j\ge\beta$, so $\log_m\beta\le\nu$ (the letters $\beta,\nu$ change meaning here). Then $\beta^{\lceil\log_m d\rceil+1}\le\beta^2d^{\log_m\beta}\le\beta^2d^\nu$, so $A(e)\le8\beta^2d^{\nu+1}$.

Preprocessing adds at most $md$ earlier pieces of depth $8\beta^2d^{\nu+1}$ each, and at most $d$ kernels add $8d$. The shift by $\lfloor D/2\rfloor$ is charged as that many halvings, and phases add at most $9$. Since $\lfloor D/2\rfloor+9\le10d$, the depth is at most $26m\beta^2d^{\nu+2}$, which is below $128m\beta^2d^{\nu+3}$, where $128$ rounds $26$ up. Let $C_0=128m\beta^2$ and $C_1=\max\{20,\nu+3\}$, so every value has $\ell\le C_0d^{C_1}$.

Let $\Delta=\lceil C_0d^{C_1}\rceil$. Every value lies in $2^{-(p+\Delta)}\mathbb{Z}[i]$ with modulus at most $2^\Delta$, so $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits suffice.

The growth of $d$ is stated with [Big-Theta notation](big-theta-notation.md): $d=\Theta(p^{\varepsilon})$ means $d$ lies between two constant multiples of $p^{\varepsilon}$ for large $p$. Since $W$, $m$ and $s$ are fixed, so are $\beta$, $\nu$, $C_0$ and $C_1$, and $\Delta=O(p^{\varepsilon C_1})$. The bound states growth in the sense of [little-o notation](little-o-notation.md): $\Delta=o(p)$ means $\Delta/p\to0$, which holds since $\varepsilon C_1<1$.

Truncation $Q_p$ moves a real component $x$ to the last multiple of $2^{-p}$ before $x$ towards $0$. $2^{-p}$, because the next multiple of $2^{-p}$ away from $0$ lies beyond $x$.
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

Write the answer to `exegenius/tasks/0464-audit-guard-width-bound.answer.json`, then run `exegenius submit 0464-audit-guard-width-bound` in the project directory. If submit rejects the answer, fix the answer and submit again.
