# exegenius task 0458-audit-cost-table

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
- Tape procedure
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $b$ (base), bound on `logarithm`: The fixed number, greater than 1, to which the logarithm is taken.
- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $\lg$ (base-2 logarithm), bound on `base-two-logarithm`: The base-2 logarithm of $n$, the least integer $k$ with $2^k \ge n$, but at least 1.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $\kappa$ (fixed exponent constant), bound on `running-time-cost`: A fixed constant, equal to $2^{-182}$, that sets the exponent $1-\kappa$ in the running time bound.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $\alpha$ (first paired value), bound on `truncation`: The first of the two values that the layer combines in each pair.
- $\kappa$ (exponent gap), bound on `schoolbook-multiplication`: A fixed constant, $2^{-182}$, which sets the saving in the exponent $1-\kappa$ of the bound.
- $\lg$ (base-2 logarithm), bound on `schoolbook-multiplication`: The base-2 logarithm, applied to the input length n.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $\lambda$ (evaluation point), bound on `little-o-notation`: The real point at which the functions are evaluated, taken to infinity.
- $\kappa$ (saving exponent), bound on `little-o-notation`: The fixed positive constant 2^{-182} in the saving exponent $1-\kappa$.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $\alpha$ (coefficient), bound on `ring-homomorphism`: The complex constant term of an element $\alpha+\delta t$ of $Q$.
- $\delta$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $t$ in an element $\alpha+\delta t$ of $Q$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $\alpha$ (address), bound on `address`: A string of d bits that labels one entry of the array.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array, which the cost bound is linear in.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map from one vector space over $F$ to another.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $K$ (second address chunk), bound on `linear-algebra-basics`: A binary address chunk, the second field of an address pair.
- $\alpha$ (input weight), bound on `linear-network-frames`: The fixed weight with which a gate multiplies its input s, the same at every address.
- $\ell$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $\varepsilon$ (routing sign), bound on `linear-network-frames`: The fixed sign by which the network multiplies the value routed from input role $\ell$.
- $K$ (second address field), bound on `linear-network-frames`: The second of two address fields, written as a vector; not a frame.
- $T$ (three-element subsets), bound on `ground-set`: The set of all three-element subsets of $[h]$.
- $V$ (operator space), bound on `eigenvalue`: The vector space on which the linear operator T acts.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $T$ (triple T), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, whose indicator vector is discussed.
- $\ell$ (column index), bound on `matrix-rank`: The column of a one in $\Pi$, which is also the index of the field $D_\ell$ it uses.
- $\tau$ (complex number), bound on `phase-factor`: A complex number written as alpha plus beta i.
- $\alpha$ (real part), bound on `phase-factor`: The real part of the complex number tau.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the output coordinates.
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
- $\tau$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring whose positive integer power equals 1.
- $\delta$ (first input value), bound on `butterfly`: The first of the two input values of the butterfly.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $\ell$ (halving count), bound on `gaussian-resampling`: The number of halvings of a transform length, so that the length is $2^\ell$.
- $\alpha$ (Gaussian width), bound on `gaussian-resampling`: The integer width of the Gaussian weights.
- $\delta$ (Gaussian integer numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of a Gaussian dyadic $\delta/2^e$.
- $\tau$ (common exponent), bound on `gaussian-dyadics`: The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $K$ (two-point kernel matrix), bound on `two-point-kernel`: The $2\times 2$ matrix $\delta I+\kappa X$ that defines the two-point kernel.
- $\delta$ (diagonal coefficient), bound on `two-point-kernel`: The coefficient of $I$ in $K$, a complex number.
- $\kappa$ (off-diagonal coefficient), bound on `two-point-kernel`: The coefficient of $X$ in $K$, a complex number.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $K$ (output space), bound on `bilinear-map`: The vector space containing the values pi(e,d) of the bilinear map.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\kappa$ (real input), bound on `ceiling-function`: The real number whose ceiling is taken.
- $\tau$ (processed positions), bound on `carry-propagation`: The number of low positions already processed, so that the sums run over $t < \tau$.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $\delta$ (remainder), bound on `congruence-modulo`: The integer in {0,...,B-1} that is the remainder of a residue class.
- $\tau$ (field element), bound on `binary-field`: An arbitrary element of the binary field, so it is $0$ or $1$.
- $K$ (example matrix), bound on `binary-field`: The $2 \times 2$ matrix over the binary field used in the example, with rows $(1, 1)$ and $(0, 1)$.
- $\kappa$ (address), bound on `binary-change-of-basis`: A vector in $\mathbb F_2^m$, one address of the selected bits.
- $K$ (scalar field), bound on `line-spanned-by-vector`: The field of scalars over which the vector space E is taken.
- $\tau$ (choice of three triples), bound on `line-spanned-by-vector`: A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $\kappa$ (modulus), bound on `centered-residue`: A positive integer, the modulus by which residues are taken.
- $\tau$ (centered residue), bound on `centered-residue`: The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\tau$ (solution), bound on `chinese-remainder-theorem`: An unknown integer, which is a solution when it satisfies every congruence of the system.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences of length n whose cyclic convolution is taken.
- $d$ (number of axes), bound on `cyclic-convolution`: The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $\kappa$ (axis index), bound on `cyclic-convolution`: The index of an axis, running from 1 to d.
- $\varepsilon$ (exponent offset), bound on `cyclic-convolution`: The amount by which a reduced exponent exceeds n.
- $\tau$ (reflected chirp), bound on `cyclic-convolution`: The function tau(delta) of an integer delta, read as a sequence of length t.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\kappa$ (last-axis position), bound on `cyclic-coordinate`: An integer from 0 to r-1 giving a position along the last cyclic coordinate.
- $d$ (greatest common divisor), bound on `bezout-identity`: The greatest common divisor of beta and gamma, the largest positive integer dividing both.
- $\kappa$ (integer quotient), bound on `bezout-identity`: The integer quotient when beta is divided by e.
- $\tau$ (remainder), bound on `bezout-identity`: The remainder when beta is divided by e, which lies between 0 and e minus 1.
- $\Theta$ (Big-Theta), bound on `big-theta-notation`: The notation stating that $u$ and $h$ have the same order up to constant factors for large inputs.
- $\kappa$ (saving exponent), bound on `big-theta-notation`: The fixed positive exponent saving in the bound, equal to $2^{-182}$ in the paper.
- $\kappa$ (group order), bound on `cyclic-group`: The number of elements of the cyclic group $C_\kappa$, which is its order.
- $\tau$ (generator), bound on `cyclic-group`: A fixed element of the group; its powers give every element of the cyclic group $C_\kappa$.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $\kappa$ (positive exponent), bound on `modular-inverse`: A positive integer exponent under which the image becomes 1.
- $\tau$ (real number), bound on `extended-reals`: A generic real number, used when the order and arithmetic of the extended reals are stated.
- $\delta$ (sequence position), bound on `extended-reals`: The position of a term in a sequence of extended real numbers, running over 1, 2, 3, and so on.
- $\varepsilon$ (positive tolerance), bound on `limit-inferior`: A positive real number used as a tolerance in a limit criterion.
- $\kappa$ (bound exponent), bound on `limit-inferior`: The fixed exponent $2^{-182}$ in the main time bound.
- $\log$ (base-2 logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm, as used in the expression $n \log n$.
- $\lg n$ (binary logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm of n rounded up to an integer and never below 1.
- $\kappa$ (saving exponent), bound on `n-log-n-conjecture`: The fixed positive constant in the exponent 1 - kappa of the main theorem's running time, equal to 2^{-182}.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers, a count of bits.
- $\lg$ (base-2 logarithm), bound on `fixed-tape-model`: The base-2 logarithm, so that $\lg n$ stands for $\log_2 n$.
- $\tau$ (family parameter), bound on `family-parameter`: The index of a member of the family: a nonnegative integer that selects which construction is built and so fixes its size.
- $g$ (second disk-grid ring array), bound on `opposite-transform`: The second of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $\tau$ (chirp position), bound on `bluestein-chirp-identity`: The integer position of a chirp entry, which may be negative or larger than q-1.
- $\delta$ (first digit array), bound on `normalization-scales`: The integer digit array of the first input, whose entries lie between $0$ and $2^b-1$.
- $\Theta$ (projection along C), bound on `projection-along-subspace`: The map sending each vector $x$ of $X$ to its component $x_U$ in $U$, for the chosen $U$ and $C$.
- $\tau$ (kernel coefficient tau), bound on `subspace-labels`: The first Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $\delta$ (kernel coefficient delta), bound on `subspace-labels`: The second Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $\tau$ (bank index), bound on `subset-intersection-network`: A triple of triples, indexing the entries of a bank.
- $\ell$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, whose central wire is $C_\ell$.
- $\delta$ (vector of E), bound on `subset-intersection-network`: A vector of the ambient space $E=\mathbb Q^h$, an argument of the bit network form.
- $V$ (head label), bound on `complex-phase-network`: The label at the head of an edge, whose frame is applied last along that edge.
- $\delta$ (route step), bound on `complex-phase-network`: The index of a step along the coordinate route, running from one to $m$.
- $c$ (starting central values), bound on `scratch-storage`: The starting values of the central wires $C_\ell$.
- $V$ (copy operator), bound on `scratch-storage`: The operator that adds each control value $x_T$ to the side wire $W_{ST}$ of each neighbouring pair $(S,T)$.
- $T$ (triple), bound on `scratch-storage`: A three-element subset of the ground set, indexing a control value $x_T$.
- $\ell$ (ground element), bound on `scratch-storage`: An element of the ground set, indexing the central wires $C_\ell$.
- $\tau$ (exponent), bound on `address-interchange`: A fixed number in $(0,1)$, the exponent of the bound $O(V u^{\tau})$.
- $\delta$ (first bit), bound on `xor`: A bit, one of the two inputs to the exclusive or.
- $\epsilon$ (second bit), bound on `xor`: A bit, the other input to the exclusive or.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $\delta$ (chunk width), bound on `simultaneous-butterfly-layer`: The number of consecutive address bits in each chunk, one chunk per transform axis.
- $\lambda$ (identity coefficient), bound on `simultaneous-butterfly-layer`: The complex coefficient $(1+i)/2$ of the identity $I$ in $C$.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number $D$ of selected axes in a layer.
- $\lambda'$ (cost exponent), bound on `numerical-layer`: A fixed exponent below one in the layer's cost bound.
- $\delta$ (cost per unit volume), bound on `rank-saving-recursion`: The cost of a call at parameter e divided by its volume.
- $\tau$ (power-saving exponent), bound on `rank-saving-recursion`: The exponent log base m of s/W, so that the cost per unit of data is about e to the power tau.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, one of the $D$ axes.
- $\delta$ (remainder of exponent), bound on `transform-round`: The remainder of $\eta$ on division by $r$, with $0\le\delta<r$.

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

## Page to audit (`cost-table`)

````markdown
# Cost table

The cost table is the last accounting step of the paper, the one that It lists the separate running-time terms of the algorithm, each a power of one size parameter, so that their sum bounds the total time. It shows that the algorithm meets the bound $O(n(\lg n)^{1-\kappa})$ of the [main theorem](main-theorem.md).

## Dividing the cost by a volume

Write $b = \lceil \log_2 n \rceil$ for the rounded-up base-2 logarithm of $n$, the number of bits of $n$. Write $p = 6b$ for the working precision in bits, so $p = \Theta(\log n)$ (). Write $T$ for the number of cells of the padded box, the array the algorithm works on, a power of two chosen with, so $4n/b \le T < 8n/b$.

The cost table splits the [running time cost](running-time-cost.md) of the algorithm into separate terms, one for each kind of work. The cost table divides every term by the [logical bit volume](logical-bit-volume.md) $V = Tp$ of the padded box, so each term becomes a power of one size parameter. Here $V = Tp = \Theta(n)$ ().

The exponents are fixed rationals:. The exponent $\epsilon$ is a fixed positive rational number, not the tolerance $\varepsilon$ of the limit inferior. The exponent $c$ is a fixed positive rational number. The exponent $\delta$ is a fixed rational number. The paper's choice is $\epsilon = 2^{-75}$, $c = 2^{-56}$, $\tau = 1-2^{-50}$, $\lambda' = 1-2^{-54}$ and $\delta = 1/16$. The factor $\alpha$ scales the cost of the line maps, and.

Write $d = \lfloor b^{\epsilon}\rfloor = \Theta(p^{\epsilon})$ for the number of axes of the padded box. Write $K = \lfloor d^{c}\rfloor = \Theta(p^{\epsilon c})$ for the width of the address chunks, which are runs of consecutive address bits, in bits (the letter $K$ changes meaning here). Write $r$ for the largest axis length of the padded box, a power of two (the letter $r$ changes meaning here: it is an axis length, not the record length of the polynomial ring), and $\ell = \log_2 r$.

The construction sets. The construction picks $d\ell - \log_2 T$ of the axis lengths to be $r/2$ and the rest to be $r$ (), so the $d$ axis lengths multiply to $T$ and $d(\ell-1) \le \log_2 T \le d\ell$. Hence $\ell = \lceil \log_2 T / d \rceil$. Since, we get $b/(2d) \le \ell \le b/d + 1$. As $p = 6b$ and $d = \Theta(p^{\epsilon})$, this gives $\ell = \Theta(p^{1-\epsilon})$.

## The table

| Operation | Cost divided by $V$ | Power of $p$ |
| --- | --- | --- |
| [Prefix-slot moves](destination-rank.md) and individual [butterfly rounds](transform-round.md) | $dK$ | $\epsilon(1+c)$ |
| Chunk exchanges for [transform layout](transform-layout.md) | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ |
| Simultaneous [butterfly rounds](transform-round.md) | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ |
| [CRT](chinese-remainder-theorem.md) and axis layouts | $d^2(1+\ell^{\tau})$ | $\tau+\epsilon(2-\tau)$ |
| [Gaussian line maps](gaussian-resampling.md) | $d\,p^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ |
| Chirps, twists and scalar products | $d\,p^{\delta}$ | $\epsilon+\delta$ |
| Packed polynomial products | $\log(rp)$ | $1-\epsilon$ |
| Final scaling and rounding | $p^{\delta}$ | absorbed below |
| Input, padding, carries and output | $1$ | absorbed below |

A packed polynomial product multiplies two records (polynomials with $r$ coefficients of $p$ bits each) by packing each record into one long integer and multiplying the integers, so its cost is the entry $\log(rp)$. Here $\log(rp) = \ell + \log p$, and.

The first row bounds the cost of moves to their [destination rank](destination-rank.md). The second row bounds the cost of the chunk exchanges that produce the [transform layout](transform-layout.md). The third row bounds the cost of each simultaneous [transform round](transform-round.md). The fourth row prices the cost of the [Chinese remainder theorem](chinese-remainder-theorem.md) step. The fifth row prices the line maps of [Gaussian resampling](gaussian-resampling.md).

## Why every term fits

The margin of a power is one minus that power. The margins $g_i$ of the seven dominant powers, in table order, are

$$g_1 = 1-\epsilon(1+c) > \tfrac12, \quad g_2 = \epsilon c(1-\tau) = 2^{-75}\cdot 2^{-56}\cdot 2^{-50} = 2^{-181}, \quad g_3 = \epsilon(1-\lambda') = 2^{-129},$$

$$g_4 = 1-\tau-\epsilon(2-\tau) > 2^{-51}, \quad g_5 = \tfrac14-\delta-\tfrac32\epsilon > \tfrac18, \quad g_6 = 1-\delta-\epsilon > \tfrac12, \quad g_7 = \epsilon = 2^{-75}.$$

For $g_4$, $\epsilon(2-\tau) < 2^{-74}$, so $g_4 > 2^{-50}-2^{-74} > 2^{-51}$. The smallest margin is $g_2 = 2^{-181} = 2\kappa$ with, and Since, each of the seven terms is at most a constant times $p^{1-\kappa}$.

The final scaling row $p^{\delta}$ is at most $d\,p^{\delta}$, the chirp row, since $d \ge 1$, and the input row $1$ is at most $p^{1-\kappa}$. So the table is $O(Vp^{1-\kappa})$, which with $V = \Theta(n)$ and $p = \Theta(\log n)$ is $O(n(\lg n)^{1-\kappa})$, the bound of the [main theorem](main-theorem.md).
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

Write the answer to `exegenius/tasks/0458-audit-cost-table.answer.json`, then run `exegenius submit 0458-audit-cost-table` in the project directory. If submit rejects the answer, fix the answer and submit again.
