# exegenius task 0472-audit-main-theorem

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
- Exact coefficient recovery (also: construction constant of the source)
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
- $y$ (positive number), bound on `logarithm`: The positive number whose logarithm to base $b$ is taken.
- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $\lg$ (base-2 logarithm), bound on `base-two-logarithm`: The base-2 logarithm of $n$, the least integer $k$ with $2^k \ge n$, but at least 1.
- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $y$ (polynomial variable), bound on `root-of-unity`: The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, which is a root of unity in that ring.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $y$ (indeterminate), bound on `pointwise-product`: The indeterminate of the quotient ring $\mathbb{C}[y]/(y^r+1)$ whose elements are the entries.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $A$ (machine), bound on `running-time-cost`: The single machine whose running time the main theorem bounds.
- $\kappa$ (fixed exponent constant), bound on `running-time-cost`: A fixed constant, equal to $2^{-182}$, that sets the exponent $1-\kappa$ in the running time bound.
- $T_A$ (running time cost), bound on `running-time-cost`: The running time cost of machine A as a function of the input length n: the largest number of steps A takes on any input of that length.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary input string, of length $n$.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $\mathrm{val}$ (value function), bound on `exact-integer-multiplication`: $\mathrm{val}(x)$ is the nonnegative integer value of a binary string $x$, with the leftmost bit most significant.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $\#$ (separator), bound on `exact-integer-multiplication`: A separator symbol placed between $x$ and $y$ in the input, marking where $x$ ends and $y$ begins.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $A$ (source set), bound on `bijection`: The source set, whose elements are the inputs of the map f.
- $f$ (map), bound on `bijection`: The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $A$ (array), bound on `permutation`: An array of entries stored at addresses, the object that an address permutation moves.
- $\kappa$ (exponent gap), bound on `schoolbook-multiplication`: A fixed constant, $2^{-182}$, which sets the saving in the exponent $1-\kappa$ of the bound.
- $\lg$ (base-2 logarithm), bound on `schoolbook-multiplication`: The base-2 logarithm, applied to the input length n.
- $y$ (indeterminate), bound on `polynomial-ring`: The formal variable of the polynomials in the ring.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The monic complex polynomial whose multiples count as zero.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $y$ (polynomial variable), bound on `array-norm`: The variable of the polynomials in the ring modulo y^r + 1.
- $A$ (multiplication machine), bound on `little-o-notation`: The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $\kappa$ (saving exponent), bound on `little-o-notation`: The fixed positive constant 2^{-182} in the saving exponent $1-\kappa$.
- $T_A$ (running time), bound on `little-o-notation`: The running time of machine A on inputs of length n.
- $\gamma$ (second integer), bound on `coprime`: The other integer whose greatest common divisor with beta is taken, not both zero with it.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $y$ (target indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q'$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array, which the cost bound is linear in.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $y$ (second vector), bound on `linear-algebra-basics`: A vector over $F$, a second arbitrary vector.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m	imes m$ matrix with entries in $F$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map from one vector space over $F$ to another.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $\ell$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $T$ (three-element subsets), bound on `ground-set`: The set of all three-element subsets of $[h]$.
- $V$ (operator space), bound on `eigenvalue`: The vector space on which the linear operator T acts.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $T$ (triple T), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, whose indicator vector is discussed.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $\ell$ (column index), bound on `matrix-rank`: The column of a one in $\Pi$, which is also the index of the field $D_\ell$ it uses.
- $W$ (wire count), bound on `matrix-rank`: The number of wires in the network, which counts the edges that carry edge changes.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the output coordinates.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $y$ (polynomial indeterminate), bound on `transform-axis`: The indeterminate of the polynomial modulo $y^s+1$; its powers serve as roots of unity on the remaining axes.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $\kappa$ (output position), bound on `multidimensional-transform`: A position in the output array, a tuple of D coordinates with the same bounds as a position in the input array.
- $y$ (polynomial variable), bound on `multidimensional-transform`: The variable of the polynomial that stores one coordinate of the array.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The variable of the polynomial ring $R_r$, in which $y^r$ is identified with $-1$.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $\log_2$ (base-2 logarithm), bound on `synthetic-transforms`: The logarithm to base 2, so $\log_2 N$ is the number of levels of the fast method.
- $\lg$ (base-2 logarithm), bound on `synthetic-transforms`: The logarithm to base 2.
- $\kappa$ (running time exponent constant), bound on `synthetic-transforms`: A fixed positive constant in the exponent of the running time bound.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $\ell$ (halving count), bound on `gaussian-resampling`: The number of halvings of a transform length, so that the length is $2^\ell$.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on `gaussian-resampling`: A generic vector of length $t$, on which $P_t$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\kappa$ (off-diagonal coefficient), bound on `two-point-kernel`: The coefficient of $X$ in $K$, a complex number.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $m$ (tensor power count), bound on `tensor-product`: The number of factors in a tensor power, which counts the coordinates the operator acts on.
- $f$ (function on addresses), bound on `tensor-product`: A function on addresses of m coordinates, the input that the operator transforms.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\kappa$ (real input), bound on `ceiling-function`: The real number whose ceiling is taken.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\kappa$ (address), bound on `binary-change-of-basis`: A vector in $\mathbb F_2^m$, one address of the selected bits.
- $A$ (form matrix), bound on `bilinear-form`: The $m\times m$ matrix of the form in the chosen basis.
- $v$ (nonzero vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $\kappa$ (modulus), bound on `centered-residue`: A positive integer, the modulus by which residues are taken.
- $f$ (first input sequence), bound on `cyclic-convolution`: The first of the two sequences of length n whose cyclic convolution is taken.
- $d$ (number of axes), bound on `cyclic-convolution`: The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $\kappa$ (axis index), bound on `cyclic-convolution`: The index of an axis, running from 1 to d.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\kappa$ (last-axis position), bound on `cyclic-coordinate`: An integer from 0 to r-1 giving a position along the last cyclic coordinate.
- $d$ (greatest common divisor), bound on `bezout-identity`: The greatest common divisor of beta and gamma, the largest positive integer dividing both.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $\kappa$ (integer quotient), bound on `bezout-identity`: The integer quotient when beta is divided by e.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $\Theta$ (Big-Theta), bound on `big-theta-notation`: The notation stating that $u$ and $h$ have the same order up to constant factors for large inputs.
- $\kappa$ (saving exponent), bound on `big-theta-notation`: The fixed positive exponent saving in the bound, equal to $2^{-182}$ in the paper.
- $\kappa$ (group order), bound on `cyclic-group`: The number of elements of the cyclic group $C_\kappa$, which is its order.
- $\kappa$ (positive exponent), bound on `modular-inverse`: A positive integer exponent under which the image becomes 1.
- $k$ (term index), bound on `limit-inferior`: The position of a term in a sequence, an index counting from 1.
- $m$ (tail start position), bound on `limit-inferior`: The position from which the tail of a sequence starts.
- $\kappa$ (bound exponent), bound on `limit-inferior`: The fixed exponent $2^{-182}$ in the main time bound.
- $\log$ (base-2 logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm, as used in the expression $n \log n$.
- $\lg n$ (binary logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm of n rounded up to an integer and never below 1.
- $\kappa$ (saving exponent), bound on `n-log-n-conjecture`: The fixed positive constant in the exponent 1 - kappa of the main theorem's running time, equal to 2^{-182}.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers, a count of bits.
- $\lg$ (base-2 logarithm), bound on `fixed-tape-model`: The base-2 logarithm, so that $\lg n$ stands for $\log_2 n$.
- $f$ (disk-grid ring array), bound on `opposite-transform`: One of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $A$ (forward contraction), bound on `transform-identity`: A linear contraction from length-$s$ vectors to length-$t$ vectors.
- $s$ (sequence length), bound on `normalized-cyclic-convolution`: The number of entries in each input sequence, which is also the length of the transform.
- $j$ (record position), bound on `phase-twist`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $\Theta$ (projection along C), bound on `projection-along-subspace`: The map sending each vector $x$ of $X$ to its component $x_U$ in $U$, for the chosen $U$ and $C$.
- $v$ (shift vector), bound on `subspace-labels`: A vector in $\mathbb F_2^m$ by which a translation shifts addresses (this letter changes meaning on this page).
- $f$ (function of addresses), bound on `subspace-labels`: A function from addresses in $\mathbb F_2^m$ to values, which a translation shifts (this letter changes meaning on this page).
- $\ell$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, whose central wire is $C_\ell$.
- $V$ (head label), bound on `complex-phase-network`: The label at the head of an edge, whose frame is applied last along that edge.
- $x$ (control vector), bound on `scratch-storage`: The vector of control values, with one entry $x_T$ for each triple $T$.
- $y$ (target vector), bound on `scratch-storage`: The vector of target values, with one entry $y_S$ for each triple $S$.
- $a$ (starting side values), bound on `scratch-storage`: The starting values of the side wires $W_{ST}$.
- $V$ (copy operator), bound on `scratch-storage`: The operator that adds each control value $x_T$ to the side wire $W_{ST}$ of each neighbouring pair $(S,T)$.
- $T$ (triple), bound on `scratch-storage`: A three-element subset of the ground set, indexing a control value $x_T$.
- $\ell$ (ground element), bound on `scratch-storage`: An element of the ground set, indexing the central wires $C_\ell$.
- $x$ (first field), bound on `address-interchange`: One of the two disjoint address fields being interchanged, read as a block of bits.
- $y$ (second field), bound on `address-interchange`: The other of the two disjoint address fields being interchanged, read as a block of bits.
- $m$ (integer base), bound on `address-interchange`: A fixed integer at least 2, the base in which the field width is written as a power.
- $k$ (number of levels), bound on `address-interchange`: The number of levels in the recursion on the width, so that a width $u=m^k$ has $k=\log_m u$ levels.
- $W$ (piece count), bound on `address-interchange`: The number of equal pieces the volume is cut into at each call, at least 2.
- $s$ (call count), bound on `address-interchange`: The number of smaller calls that one call makes.
- $j$ (recursion depth), bound on `address-interchange`: The number of levels below the top call, counting from 0 at the top.
- $\epsilon$ (second bit), bound on `xor`: A bit, the other input to the exclusive or.
- $m$ (field count), bound on `address-shear`: The number of fields in each address vector, which is also the size of the square matrix M.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $a$ (rational rank), bound on `address-shear`: The number of linearly independent rows of M over the rational numbers.
- $e$ (chunk digit count), bound on `address-shear`: The number of radix-q digits in each interchanged chunk, which is m^k at recursion depth k.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number $D$ of selected axes in a layer.
- $e$ (axes per call), bound on `numerical-layer`: The number of selected axes that a call acts on.
- $s$ (smaller-call count), bound on `numerical-layer`: The number of smaller calls that one call makes.
- $W$ (role count), bound on `numerical-layer`: The number of roles among which rows are distributed.
- $m$ (division factor), bound on `numerical-layer`: The fixed integer by which each call divides its number of axes.
- $e$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the selected axes of a numerical layer or the digits of an address field.
- $e$ (quotient of exponent), bound on `transform-round`: The integer quotient of $\eta$ by $r$, which counts the whole multiples of $r$ in $\eta$.
- $b$ (bit length of n), bound on `cost-table`: The rounded-up base-2 logarithm of n, which is the number of bits of n.
- $p$ (working precision), bound on `cost-table`: The working precision in bits, p = 6b, so that p = Theta(log n).
- $T$ (padded box cell count), bound on `cost-table`: The number of cells of the padded box, a power of two with 4n/b <= T < 8n/b.
- $V$ (logical bit volume), bound on `cost-table`: The logical bit volume V = Tp of the padded box, which is Theta(n) bits.
- $\epsilon$ (size exponent), bound on `cost-table`: A fixed positive rational exponent, 2^{-75} in the paper's choice, with d = Theta(p^epsilon).
- $\log$ (base-2 logarithm), bound on `established-multiplier`: The base-2 logarithm, the power to which 2 must be raised to give the argument.
- $f$ (first polynomial), bound on `signed-packing`: The first input, an integer polynomial whose coefficients are the $f_j$.
- $j$ (coefficient position), bound on `signed-packing`: The position of a coefficient in a record, running from 0 to r-1.
- $p$ (magnitude exponent), bound on `signed-packing`: The number of bits in the magnitude bound on a coefficient, so each coefficient has magnitude at most $2^p$.
- $\Theta$ (forward transform), bound on `polynomial-ring-convolution`: The forward transform along the remaining axes, normalized by 1/t on each axis of length t.
- $j$ (position index), bound on `polynomial-ring-convolution`: A frequency address of a transform entry, or a coefficient position in the reduction step, a nonnegative integer index.
- $e$ (wrap exponent), bound on `polynomial-ring-convolution`: An integer exponent of y, which may be at least r, so that y^e wraps around with a sign flip.
- $u$ (first input value), bound on `guard-width-bound`: The first of the two complex input values of the two-point map.
- $v$ (second input value), bound on `guard-width-bound`: The second of the two complex input values of the two-point map.
- $\ell$ (value depth), bound on `guard-width-bound`: The number of arithmetic operations on a chain computing a value from an input.
- $e$ (group size), bound on `guard-width-bound`: The number of selected axes in a group that the recursion splits.
- $A$ (operation bound), bound on `guard-width-bound`: An upper bound on the number of operations on any chain within a group of e axes.
- $m$ (division factor), bound on `guard-width-bound`: The factor by which a call of the complex phase network divides the number of axes.
- $m$ (event count), bound on `union-bound`: The number of events E_1 through E_m, which here also counts the guards.
- $f$ (selected bit count), bound on `union-bound`: The number of selected bit positions, which fixes the number of guards 2(f-1).
- $y$ (address chunk y), bound on `union-bound`: One of the two address chunks, which holds the segment that gives each guard g_i.
- $\gamma$ (guard value), bound on `packed-bit-addition`: The value of the K-1 bits above the selected bit of a segment.
- $k$ (term index), bound on `telescoping-identity`: The position of a term in the sequence, running from 0 to o.
- $j$ (place index), bound on `mixed-radix-digits`: A position among the places, running from 1 to the number of places.
- $x$ (indeterminate), bound on `chinese-remainder-map`: The indeterminate of the one-dimensional ring, whose powers index positions.
- $e$ (coefficient index), bound on `chinese-remainder-map`: An ordinary coefficient index, an integer from 0 to Lambda minus 1.
- $u$ (longest axis length), bound on `prime-source-lengths`: The power of two $2^\ell$ that is the common length of the longest axes of the padded box.
- $\gamma$ (construction constant), bound on `recovery-and-error`: The integer $2d\alpha^2$ fixed by the source's construction, which grows more slowly than $b$.

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

## Page to audit (`main-theorem`)

````markdown
# Integer multiplication below n log n

This page states the main theorem, the target of the whole argument: one fixed deterministic machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ steps, where $\lg n = \max\{\lceil\log_2 n\rceil, 1\}$ is the base-two logarithm of $n$, rounded up and at least 1. It disproves [The n log n optimality conjecture](n-log-n-conjecture.md) in this model, and each later page establishes one step of the argument for this bound.

## The statement

For a binary string $x$, $\mathrm{val}(x)$ denotes its nonnegative integer value, with the leftmost bit most significant. The input is $x\#y$, with $x$ and $y$ binary strings of length $n$, and the output is the $2n$-bit binary form of $\mathrm{val}(x)\cdot\mathrm{val}(y)$. For example, take $n=4$, $x=1011$ and $y=0110$. Here $\mathrm{val}(x)=11$ and $\mathrm{val}(y)=6$, and the output is $01000010$, the eight-bit form of $66$.

. The theorem is stated in the [Fixed-tape machine model](fixed-tape-model.md): the alphabet and the number of tapes do not depend on the input. The machine's time is measured by the [Running time cost](running-time-cost.md) $T_A(n)$, the worst-case number of steps of $A$ on inputs of length $n$. The claim is $T_A(n) = O(n(\lg n)^{1-\kappa})$ for every $n \ge 1$, with $\kappa = 2^{-182}$.

The bound is stated with the [Logarithm](logarithm.md) to base two., so it bounds machine steps, not the speed of a practical multiplier.

## Why the bound is an improvement

Schönhage and Strassen. For large $n$ the theorem is faster than [Schoolbook multiplication](schoolbook-multiplication.md), which takes quadratic time in the number of digits. The bound is $n\lg n$ times $(\lg n)^{-\kappa}$. This factor is below one half exactly when $(\lg n)^{\kappa}>2$, that is, when $\lg n > 2^{1/\kappa} = 2^{2^{182}}$.

## Where the saving comes from

The theorem gets its power saving from the [Rank-saving recursion](rank-saving-recursion.md): a call splits into smaller calls, each working on a stream holding a fraction of the stored bits. Let $V$ be the number of stored bits a call works on. A call at parameter $m\ell$ makes $s$ child calls at parameter $\ell$, each on a stream of volume $V/W$. Here $m$ is the parameter's growth factor and $W$ the number of pieces..

Let $\gamma(\ell)$ be the cost of a call at parameter $\ell$ divided by its volume. The child calls run one after another, so their costs add to $s\cdot(V/W)\cdot\gamma(\ell)$. Dividing by $V$ gives $\gamma(m\ell)\approx (s/W)\,\gamma(\ell)$. The approximation omits the node's own work:, and these costs enter the same sum over levels.

After $k$ levels the cost per volume is multiplied by $(s/W)^k = (m^k)^{\log_m(s/W)}$, where $\log_m x$ is the number $e$ with $m^e = x$. Since $s<Wm$, $\log_m(s/W)<1$. The cost thus grows as a power of the parameter with exponent below one.

The parameter is tied to $n$. The working precision is $p = 6b$ with, so $p=\Theta(\lg n)$, where $\Theta(f(n))$ denotes a quantity lying between two positive constant multiples of $f(n)$ for all large $n$. The layer uses so $d=\Theta(p^{\epsilon})$ for a fixed $\epsilon$ with $0<\epsilon<1$., so $m^k\le md$. The cost is therefore at most a constant times $d^{\log_m(s/W)}=\Theta(p^{\epsilon\log_m(s/W)})$, a power of $\lg n$ with exponent below one.

The saving holds at every input length because its ingredients are fixed. Small inputs are covered by multiplication below it.

## Why the method is needed

 A scan reads each stored bit once, so it costs $\Theta(n)$. A full scan per level gives the conjectured cost and no better. The levels must together cost less than $n\lg n$. The recursion achieves this: the work at depth $j$ is $V(s/W)^j$, and $s/W<m$ keeps this below the parameter's growth.

## How the argument proceeds

1. The first step reduces multiplication to a [Radix-digit convolution](radix-digit-convolution.md) of short integer coefficients, obtained by splitting each input into radix digits (blocks of consecutive bits).
2. The Fourier transforms are replaced by multidimensional transforms whose axis lengths are powers of two..
3. Then, and.
4. The method lays out the transforms by a [Transform layout](transform-layout.md), so that a butterfly layer can act on every transform round..
5. The machine adds selected bits by [Packed selected-bit addition](packed-bit-addition.md).
6. The method places coefficients on distinct axes by a [Chinese-remainder map](chinese-remainder-map.md) that preserves convolution.. The theorem chooses its axis lengths by [Prime source lengths](prime-source-lengths.md): distinct odd primes close to powers of two..
7. The method keeps permutations inside the [Transform identity with retained permutations](transform-identity.md), so the source and target coordinate permutations need not be executed as sorts. [Bluestein's chirp identity](bluestein-chirp-identity.md) into a normalized cyclic convolution.
8. The method turns the last cyclic coordinate into a polynomial by [Phase twist](phase-twist.md)..
9. The method handles the remaining axes by [Convolution over the polynomial ring](polynomial-ring-convolution.md)..
10. The method recovers the coefficients by rounding through [Exact coefficient recovery](recovery-and-error.md), which shows that the error is below one half..
11. The algorithm ends with [Carry propagation](carry-propagation.md), which turns the recovered coefficients into the exact binary product..

Each stage is charged to the stored volume $V$: its cost is $V$ times a power of its parameter. For example, the first tape procedure interchanges two address fields of $u$ bits.
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

Write the answer to `exegenius/tasks/0472-audit-main-theorem.answer.json`, then run `exegenius submit 0472-audit-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
