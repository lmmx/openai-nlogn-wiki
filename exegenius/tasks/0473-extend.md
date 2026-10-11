# exegenius task 0473-extend

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Extend a prerequisite graph of concepts built from source documents. An audit of the wiki found terms that a specific reader cannot follow and that match no existing concept. For each term, either point it at an existing concept that covers it, or add a new concept.

- Add a new concept only when no existing concept covers the term. Give each new concept an id that is not already used.
- New concepts may require existing concepts or each other; the graph must stay acyclic.
- Mark `known: true` if the reader profile already covers the concept, with `requires: []`.
- `evidence` quotes must be copied from the sources character for character, with their source id. A concept that does not appear in the sources may have no quotes.
- A name with mathematics in it needs a `title` with the mathematics in LaTeX and a binding in `symbols` for every symbol in it, as in the extract task.
- Give a resolution for every term.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `big-o-notation`: Big-O notation (known to the reader): A way of comparing growth rates of functions, ignoring constant factors.
- `polynomials`: Polynomials (known to the reader): Finite sums of powers of a variable with coefficients, multiplied and reduced in the usual way.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with real a and b and imaginary unit i, with i² = −1.
- `turing-machine-tapes`: Turing machines and tapes (known to the reader): A finite-state machine that reads and writes symbols on one or more tapes, each with a movable head.
- `fixed-tape-model`: Fixed-tape machine model: A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input.
- `exact-integer-multiplication`: Exact integer multiplication: Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
- `n-log-n-conjecture`: The n log n optimality conjecture: The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers.
- `established-multiplier`: Established O(n log n) multiplier: The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine.
- `radix-digit-convolution`: Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
- `discrete-fourier-transform`: Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices wrap around modulo the sequence length.
- `gaussian-resampling`: Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- `chinese-remainder-map`: Chinese-remainder map: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
- `bluestein-chirp-identity`: Bluestein's chirp identity: An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients.
- `polynomial-ring-mod-yr-plus-1`: Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign.
- `phase-twist`: Phase twist: A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring.
- `signed-packing`: Signed coefficient packing: Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.
- `polynomial-ring-convolution`: Convolution over the polynomial ring: The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.
- `subspace-labels`: Subspace labels: Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.
- `linear-network-frames`: Linear networks and frames: A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame.
- `subset-intersection-network`: Subset-intersection network: A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
- `address-interchange`: Address-field interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly.
- `address-shear`: Address shear: The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges.
- `rank-saving-recursion`: Rank-saving recursion: The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
- `gaussian-dyadics`: Gaussian dyadics: Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer.
- `complex-phase-network`: Complex phase network: A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time.
- `packed-bit-addition`: Packed selected-bit addition: An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.
- `guard-width-bound`: Guard-width bound: An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices.
- `transform-layout`: Transform layout: A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
- `prime-source-lengths`: Prime source lengths: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.
- `transform-identity`: Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
- `carry-propagation`: Carry propagation: Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
- `recovery-and-error`: Exact coefficient recovery: The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.
- `address-field`: Address field: A contiguous block of address bits of an array, which an address interchange exchanges with another block of the same width.
- `agarwal-cooley-split`: Agarwal and Cooley's split: The reduction, by the Chinese remainder theorem, of one cyclic convolution to a multidimensional cyclic convolution, after Agarwal and Cooley.
- `transform-axis`: Transform axis: One coordinate direction of a multidimensional array or transform, with its own length.
- `linear-algebra-basics`: Linear algebra basics: Vector spaces over a field, linear maps and matrices, and the inverse of an invertible linear operator.
- `bilinear-map`: Bilinear map: A map that is linear in each of two vector arguments separately, such as the product of two polynomials.
- `bilinear-form`: Bilinear form: A bilinear map from a vector space and itself to its scalars; a space with such a form is nondegenerate when the form has no nonzero vector orthogonal to everything, and two vectors are orthogonal when the form vanishes on them.
- `binary-field`: Binary field: The field with two elements 0 and 1, where addition is exclusive or and multiplication is AND.
- `binary-change-of-basis`: Binary change of basis: An invertible change of basis of the selected address bits over the binary field, realised by row additions on bit positions.
- `bit-procedure`: Bit procedure: The first tape procedure, which interchanges two address fields by a shear built from the bit network over the binary field.
- `butterfly`: Butterfly: The two-point map H0(u, v) = ((u + v)/2, (u − v)/2) applied to a pair of values, the elementary step of a Fourier-type transform.
- `congruence-modulo`: Congruence: Two integers are congruent modulo m when their difference is divisible by m; a residue is the class of an integer modulo m.
- `centered-residue`: Centered residue: The representative of a residue class modulo B that lies in the interval from −B/2 to B/2, used to recover a signed coefficient.
- `linear-contraction`: Linear contraction: A linear map that does not increase the maximum modulus of any vector, so that errors pass through it without growing.
- `cyclic-shift`: Cyclic shift: A rotation of the values of a block of positions by an offset taken modulo the block length, where the offset may be set by control bits.
- `convolution`: Convolution: The product of two sequences in which each output index sums the products of pairs of input indices that combine to it.
- `coprime`: Coprime: Two integers are coprime when their greatest common divisor is 1; a set of integers is pairwise coprime when every two of them are coprime.
- `running-time-cost`: Running time cost: The number of machine steps an algorithm takes, as a worst-case function of the input length, on a machine with a fixed alphabet and fixed number of tapes.
- `cost-table`: Cost table: The list of separate running-time terms of an algorithm, each a power of the input size, whose sum bounds the total time.
- `stable-radix-sort`: Stable radix sort: Sorting by successive passes over key digits from least to most significant, each pass stable so that equal keys keep their earlier order.
- `destination-rank`: Destination rank: The position a record takes in the final order after a move, given by its rank among the records in that order.
- `network-route`: Network route: The path that carries one input role of a linear network to an output role, together with the scalar sign that the network attaches to that path.
- `endpoint-operator`: Endpoint operator: The operator that a network realises on each role's array once all intermediate frames have cancelled, so that it depends only on the endpoint frames.
- `network-gate-terminal`: Gate and terminal of a network: A gate combines the values on the wires it touches by a fixed linear map, and a terminal is an input or output end of a wire where the network's values enter or leave.
- `gaussian-integer`: Gaussian integer: A complex number whose real and imaginary parts are both integers.
- `grid-numerator`: Grid numerator: For a fixed precision, a grid value is an integer multiple of a fixed negative power of two, and its numerator is the integer multiplier.
- `ground-set`: Ground set: A finite set from which the subsets under consideration are chosen.
- `indicator-vector`: Indicator vector: The 0-1 vector whose entries mark which elements of a ground set belong to a given subset.
- `modular-inverse`: Modular inverse: An integer a has an inverse modulo q when some integer b makes ab congruent to 1 modulo q; this holds exactly when a and q are coprime.
- `two-point-kernel`: Two-point kernel: The two-by-two operator aI + bX, with X the bit flip, applied along one direction of a binary address; its coefficients are Gaussian dyadics.
- `cyclic-coordinate`: Cyclic coordinate: One of the axes of a multidimensional cyclic convolution, with its own cyclic length.
- `limit-inferior`: Limit inferior: The smallest value that a sequence approaches infinitely often; its limit inferior is zero when it has subsequences that tend to zero.
- `line-spanned-by-vector`: Line spanned by a vector: The set of all scalar multiples of one nonzero vector, a one-dimensional subspace.
- `little-o-notation`: Little-o notation: A function f is o(g) when the ratio f/g tends to zero, a stronger statement than being O(g).
- `middle-transform`: Middle transform: The transform on the target lengths that sits between the two Gaussian resampling maps, which Bluestein's identity turns into a cyclic convolution.
- `mixed-radix-digits`: Mixed-radix digits: The digits of an integer written in a positional system whose place values use a separate length for each place, so that the digit at each place ranges over its own length.
- `multidimensional-transform`: Multidimensional transform: A Fourier transform over several axes at once, computed by transforming along each axis in turn.
- `array-norm`: Array norm: The maximum modulus over all entries of an array of complex values; an array has norm at most one exactly when every entry has modulus at most one.
- `normalized-cyclic-convolution`: Normalized cyclic convolution: A cyclic convolution divided by the transform length, the normalization for which a Fourier transform turns convolution into pointwise product.
- `normalization-scales`: Normalization scales: The known powers of two and transform lengths by which a computed product is multiplied to undo the normalizing factors of the transforms and the digit scaling.
- `numerical-layer`: Numerical layer: A layer of the transform calculation in which a simultaneous butterfly is applied to a chosen set of selected axes.
- `opposite-transform`: Opposite transform: The discrete Fourier transform with the opposite sign in its exponent, which inverts the forward transform up to a normalizing factor.
- `padded-transform-box`: Padded transform box: The full array of transform entries after every axis has been padded to its chosen length, with zero entries outside the valid region.
- `payload`: Payload: The record data carried at each address of an array, as distinct from the address that locates it.
- `phase-factor`: Phase factor: A complex number of modulus one, such as a power of i, multiplied into coefficients; a scalar correction is a fixed constant factor of this kind.
- `polynomial-ring`: Polynomial ring: The ring of polynomials in an indeterminate with complex coefficients, with the usual addition and multiplication, here reduced modulo a fixed polynomial.
- `matrix-rank`: Matrix rank: The number of linearly independent rows or columns of a matrix, taken over the rational numbers in the present context.
- `ring-homomorphism`: Ring homomorphism and isomorphism: A map between rings that preserves addition and multiplication; it is an isomorphism when it is also bijective, so that the two rings have the same structure.
- `schoolbook-multiplication`: Schoolbook multiplication: Multiplication of two integers digit by digit by the grade-school method, which takes quadratic time in the number of digits.
- `scratch-storage`: Scratch storage: Auxiliary storage that a procedure may overwrite during its work but must restore to its starting contents, whatever those contents were.
- `tensor-product`: Tensor product: The Kronecker product of two matrices, whose m-fold power applies one operator to m independent coordinates at once.
- `transform-round`: Transform round: One step of a multidimensional transform in which a butterfly is applied on the participating axes at once, followed by the corresponding twiddle.
- `truncation`: Truncation: Discarding the fractional digits of a value beyond a fixed precision, here toward zero, so that the value stays on a fixed grid.
- `union-bound`: Union bound: The probability that at least one of several events occurs is at most the sum of their probabilities; in counting form, the size of a union is at most the sum of the sizes.
- `xor`: Exclusive or: The bitwise sum modulo 2 of two bits, which is 1 exactly when the bits differ.
- `address`: Address: A label that locates one entry of an array, written as a string of address bits.
- `array`: Array: A finite collection of entries, each stored at an address and carrying a payload.
- `logical-array`: Logical array: The array of values that a role presents to the network, which may differ from the stored array by a frame.
- `logarithm`: Logarithm: The exponent to which a fixed base must be raised to give a positive number; lg n is the logarithm to base 2.
- `base-two-logarithm`: Base-2 logarithm: The logarithm to base 2, written lg n or log₂ n.
- `ceiling-function`: Ceiling function: The least integer that is not less than a given real number, written with brackets ⌈x⌉.
- `bezout-identity`: Bézout's identity: For integers a and b with greatest common divisor d, there are integers x and y with ax + by = d.
- `big-theta-notation`: Big-Theta notation: A function f is Θ(g) when f is both O(g) and bounded below by a constant multiple of g for large inputs.
- `bijection`: Bijection: A map that is one-to-one and onto, so that every element of the target is hit by exactly one element of the source.
- `permutation`: Permutation: A bijection of a finite set onto itself, which rearranges the positions of a sequence.
- `carry`: Carry: The bit passed from one digit position to the next when two digits are added in positional notation.
- `bit-network`: Bit network: A linear network whose wires carry bits over the binary field and which realises a binary change of basis.
- `bit-construction`: Bit construction: The construction of a subset-intersection network whose scalars lie in the binary field, with neighbours chosen by intersection size one.
- `complex-construction`: Complex construction: The construction of a subset-intersection network whose scalars are Gaussian dyadics, with neighbours chosen among distinct triples.
- `chinese-remainder-theorem`: Chinese remainder theorem: For pairwise coprime moduli, a system of congruences has a solution, unique modulo the product of the moduli.
- `cyclic-group`: Cyclic group: A group whose elements are all powers of one fixed element, called a generator.
- `product-of-cyclic-groups`: Product of cyclic groups: The direct product of finitely many cyclic groups, whose elements are tuples with one entry from each factor.
- `order-of-element`: Order of an element: The least positive integer k for which the k-th power of an element of a group is the identity.
- `diagonal-scaling`: Diagonal scaling: A linear operator that multiplies each coordinate by its own fixed scalar.
- `eigenvalue`: Eigenvalue: A scalar λ for which a linear operator maps some nonzero vector v to λv.
- `extended-reals`: Extended real numbers: The real numbers together with two added values, positive infinity and negative infinity.
- `family-parameter`: Family parameter: A parameter that indexes a family of constructions and controls their sizes.
- `frequency-domain`: Frequency domain: The representation of a sequence by the values of its discrete Fourier transform.
- `incidence`: Incidence: The relation that a gate and a wire have when the wire touches the gate.
- `independence`: Independence of events: Two events are independent when the probability that both occur equals the product of their probabilities.
- `mathematical-induction`: Mathematical induction: A proof method that establishes a statement for all integers by proving a base case and that each case implies the next.
- `integer`: Integer: A whole number, positive, negative or zero.
- `prime-number`: Prime number: An integer greater than one whose only positive divisors are one and itself.
- `set-intersection`: Set intersection: The set of elements that belong to both of two given sets.
- `logical-bit-volume`: Logical bit volume: The number of bits in a padded transform box, counting every entry of the box at its record width.
- `triangular-permutation-factorization`: Triangular and permutation factorization: A matrix factored into lower triangular factors and a partial permutation matrix, so that its rank can be read off the pivots.
- `ring`: Ring: A set with addition and multiplication that satisfy the usual axioms, with addition forming a commutative group.
- `multivariate-quotient-ring`: Multivariate quotient ring: The ring of polynomials in several variables taken modulo a fixed set of polynomials.
- `orthogonal-complement`: Orthogonal complement: The set of all vectors that are orthogonal to every vector of a given subspace.
- `pointwise-product`: Pointwise product: The product of two sequences computed entry by entry, with each output entry the product of the two entries at that index.
- `projection-along-subspace`: Projection along a subspace: A linear map that keeps the component of a vector in one subspace and removes its component in a complementary subspace.
- `root-of-unity`: Root of unity: A complex number z for which some positive power of z equals one.
- `stream`: Stream: A sequence of records that a procedure reads or writes in order, one position at a time, on a tape.
- `supremum`: Supremum: The least upper bound of a set of real numbers.
- `tape-procedure`: Tape procedure: A procedure that moves the contents of a Turing machine's tapes, such as the address fields of an array, in a bounded number of passes.
- `telescoping-identity`: Telescoping identity: A sum of differences of consecutive terms equals the difference of its first and last terms.
- `schonhage-strassen`: Schönhage–Strassen multiplication: The fast integer multiplication method of Schönhage and Strassen, which multiplies n-bit integers in O(n log n log log n) time.

## Unresolved terms

- "aligned streams"
  - on page `stream`: "transforming aligned streams"
- "axis layouts"
  - on page `cost-table`: "and axis layouts"
- "B-adic blocks"
  - on page `polynomial-ring-convolution`: "holds every coefficient as $B$-adic blocks"
- "bad addresses"
  - on page `bijection`: "which agree outside a set of bad addresses"
- "basis"
  - on page `ring-homomorphism`: "whose powers cover the target basis"
- "Big-Omega notation"
  - on page `fixed-tape-model`: "an eventual $\Omega(n\log n)$ lower bound this model"
- "Binary product"
  - on page `ceiling-function`: "into a binary product"
- "bit case"
  - on page `complex-construction`: "Copy is unchanged from the bit case"
- "bit-reversed index order"
  - on page `synthetic-transforms`: "First the records are placed in bit-reversed index order, an address rearrangement."
- "branch bit"
  - on page `transform-round`: "the branch bit the round writes on axis $i$"
- "butterfly layer"
  - on page `phase-factor`: "In a butterfly layer, the phase depends on the address"
- "chunk interchange"
  - on page `address-shear`: "It is the costly step of the paper's chunk interchange"
- "correction"
  - on page `destination-rank`: "returns each record extracted by the correction to its hole"
- "cyclic axes"
  - on page `prime-number`: "primes serve as the lengths of cyclic axes"
- "cyclic axes of the proof"
  - on page `cyclic-group`: "the structure behind the cyclic axes of the proof"
- "data banks X_τ and Y_τ"
  - on page `line-spanned-by-vector`: "The two data banks $X_\tau$ and $Y_\tau$ carry it:"
- "decreasing edge"
  - on page `subset-intersection-network`: "The construction needs the loss on decreasing edges to stay small: edges."
- "destination map"
  - on page `stable-radix-sort`: "Since the destination map permutes the exceptional set"
- "digit"
  - on page `stream`: "splitting an array on a digit"
- "directed graph (vertices)"
  - on page `linear-algebra-basics`: "The paper's network is a directed graph"
- "disk"
  - on page `recovery-and-error`: "so each lies in the disk"
- "disk-grid ring array"
  - on page `opposite-transform`: "two disk-grid ring arrays"
- "dual space U^*"
  - on page `subset-intersection-network`: "the form identifies $U'$ with its dual"
- "exceptional set"
  - on page `stable-radix-sort`: "the records whose addresses lie in the exceptional set"
- "exclusive or and AND"
  - on page `bit-construction`: "where addition is exclusive or and multiplication is AND"
- "Fermat-type residue ring"
  - on page `schonhage-strassen`: "The residue ring of integers modulo $2^m+1$ is a Fermat-type residue ring."
- "fields of the bit procedure"
  - on page `ring`: "The bit procedure's fields are,"
- "floor function"
  - on page `bijection`: "$g(s)=\lfloor s/2\rfloor$"
- "forward procedure"
  - on page `transform-layout`: "The forward procedure may keep its output order."
- "forward transform"
  - on page `pointwise-product`: "inverts the forward transform up to a normalizing factor"
- "frame of a gate"
  - on page `incidence`: "the frame of the gate is shared by all of them"
- "Gram matrix"
  - on page `complex-phase-network`: "Each $U_\delta$ is nondegenerate, since the Gram matrix of $e_1,\dots,e_\delta$ is the identity"
- "highest unprocessed bit"
  - on page `transform-round`: "the highest unprocessed bit $h$"
- "Integer multiplication below n log n (the paper)"
  - on page `discrete-fourier-transform`: "The paper *Integer multiplication below n log n* uses the same sign"
- "inverse child"
  - on page `phase-factor`: "An inverse child on $D$ selected bits is"
- "inverse schedule"
  - on page `bit-construction`: "followed by the inverse schedule from $Y$ to $X$"
- "invertible modulo n"
  - on page `cyclic-convolution`: "Pick integers $\mu_\kappa$, each invertible modulo $n_\kappa$"
- "Iverson bracket"
  - on page `bit-construction`: "|S\cap T| + [\,|S\cap T|=1\,] \pmod 2"
- "label"
  - on page `orthogonal-complement`: "to split one label into a part that is kept and a part that is removed"
- "least significant end"
  - on page `transform-layout`: "one common offset $\rho$, counted from the least significant end"
- "line"
  - on page `padded-transform-box`: "Expanding axis $s$ transforms each line whose other coordinates are valid"
- "linear functionals"
  - on page `subspace-labels`: "to the linear functionals on $U'$"
- "linear tape time"
  - on page `cyclic-shift`: "in linear tape time"
- "main result"
  - on page `linear-network-frames`: "It is the step that lets the main result count the cost of each procedure."
- "modulo (mod 4)"
  - on page `bijection`: "$f(s)=s+1 \bmod 4$"
- "multiplicative order"
  - on page `schonhage-strassen`: "so $2$ has multiplicative order $8$ modulo $17$"
- "natural logarithm"
  - on page `logarithm`: "there it means the natural logarithm, not base $2$"
- "near-linear time"
  - on page `stream`: "a procedure that is to run in near-linear time"
- "negacyclic convolution"
  - on page `bluestein-chirp-identity`: "The sum below would then be a negacyclic convolution"
- "neighbors"
  - on page `subspace-labels`: "and for neighbors $\langle t_{T'},t_T\rangle=0$, so their lines are orthogonal"
- "network"
  - on page `stream`: "Each procedure is a fixed network whose wires each carry one stream"
- "Neumann series"
  - on page `transform-identity`: "If $\|E\|<1$, the Neumann series $\sum_{k\ge 0}(-E)^k$ inverts $I+E$."
- "nondegenerate space"
  - on page `rank-saving-recursion`: "a fixed nondegenerate space of dimension $m$"
- "norm of a vector"
  - on page `gaussian-resampling`: "over vectors with $\|u\|\le 1$"
  - on page `supremum`: "vectors of norm at most one"
- "orthogonal"
  - on page `eigenvalue`: "no nonzero vector is orthogonal to every vector"
  - on page `indicator-vector`: "the orthogonality of those vectors is what permits the assignments"
- "padded address set"
  - on page `bijection`: "a bijection on the padded address set"
- "padded box"
  - on page `cyclic-coordinate`: "The construction is the padded box of the paper's Section 9.2.1"
- "paper's main running-time bound"
  - on page `base-two-logarithm`: "the paper's main running-time bound is stated"
- "participating axis"
  - on page `transform-layout`: "applies one such butterfly on each participating axis"
- "phase frames"
  - on page `two-point-kernel`: "its phase frames are written as a."
- "primitive root of unity"
  - on page `normalized-cyclic-convolution`: "where $\omega$ is the primitive $s$-th root of unity, so $\omega^s = 1$"
- "probability in general"
  - on page `independence`: "Two events are independent when the probability that both occur equals the product of their probabilities."
- "product of groups"
  - on page `cyclic-group`: "Then $C_\kappa$ is the product $C_{\kappa_1}\times C_{\kappa_2}$"
- "QFt"
  - on page `bluestein-chirp-identity`: "The middle transform is the factor QFt in the paper's equation (35)."
- "quotient ring"
  - on page `pointwise-product`: "the indeterminate of the quotient ring"
- "radix-digit coefficients"
  - on page `prime-number`: "the radix-digit coefficients are placed on distinct prime cyclic axes"
  - on page `padded-transform-box`: "the radix-digit coefficients are placed on distinct prime cyclic axes inside it"
  - on page `modular-inverse`: "places the radix-digit coefficients on cyclic axes"
- "radix-two factorization"
  - on page `multidimensional-transform`: "the standard radix-two factorization writes the one-dimensional transform as $k$ levels of such butterflies"
- "rank counter"
  - on page `packed-bit-addition`: "scans the [stream](stream.md) of all $M$ records with a rank counter"
- "rank-saving argument"
  - on page `complex-construction`: "the rank-saving argument compares this count with $m$"
- "Real number"
  - on page `ceiling-function`: "the real number being rounded up"
- "real numbers"
  - on page `big-theta-notation`: "from input sizes to nonnegative real numbers"
  - on page `limit-inferior`: "a sequence of real numbers"
  - on page `telescoping-identity`: "a sequence of real or complex numbers"
- "residue"
  - on page `schonhage-strassen`: "Multiplying a residue by $2^j$"
- "residue class"
  - on page `centered-residue`: "representative of a residue class"
- "retained order"
  - on page `transform-layout`: "feeds its retained order to the"
- "role"
  - on page `linear-network-frames`: "A permutation $\rho$ of roles sends each input role $\ell$ to an output role $\rho(\ell)$"
- "role array"
  - on page `endpoint-operator`: "on each role array"
- "Row reduction and pivot"
  - on page `matrix-rank`: "Row reduction computes it, since each pivot is one independent row."
- "sets"
  - on page `bijection`: "Let $A$ and $B$ be sets"
- "shear"
  - on page `linear-network-frames`: "so the shear is a pointwise XOR of the two fields"
- "signed dimension changes"
  - on page `telescoping-identity`: "The paper applies the same collapse to signed dimension changes"
- "source and sink dimensions"
  - on page `telescoping-identity`: "which leaves only the source and sink dimensions"
- "Standard basis vector"
  - on page `matrix-rank`: "the rows of $\Pi$ holding a one are distinct standard basis vectors."
- "symmetric matrix"
  - on page `eigenvalue`: "For a symmetric matrix $A$"
- "tape lemmas"
  - on page `stream`: "The tape lemmas rely on splitting an array on a digit"
- "tape step"
  - on page `bit-network`: "the tape step that interchanges two equal address chunks"
- "target monomial group"
  - on page `cyclic-group`: "The paper uses this split for its target monomial group."
- "target result"
  - on page `integer`: "The target result multiplies integers"
- "the multiplication method"
  - on page `butterfly`: "the basic step of the transforms in the multiplication method"
- "the paper's representation"
  - on page `multidimensional-transform`: "In the paper's representation those root multiplications become cheap."
- "the paper's transform and middle transform"
  - on page `normalized-cyclic-convolution`: "rewrite the middle transform (the Fourier-type factor of the paper's transform) as one such convolution"
- "the source"
  - on page `address-interchange`: "The source uses signs:"
- "the target"
  - on page `mathematical-induction`: "The method matters for the target because"
- "transform level"
  - on page `tape-procedure`: "a full scan at every transform level is too costly"
- "transform levels"
  - on page `big-theta-notation`: "at each of $\Theta(\log n)$ transform levels"
- "update line and rectangle"
  - on page `bijection`: "each update line is checked to be a bijection of the rectangle"
- "working grid"
  - on page `simultaneous-butterfly-layer`: "times the working grid"

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Binding": {
      "additionalProperties": false,
      "description": "What a symbol in a concept's name denotes.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the title's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation"
      ],
      "type": "object"
    },
    "Concept": {
      "additionalProperties": false,
      "description": "One concept. This is also the shape of a concept in an extract answer, so the field\ndocs double as instructions in the task file.",
      "properties": {
        "aliases": {
          "description": "Other names and abbreviations the sources use for this concept.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "evidence": {
          "description": "Short quotes copied exactly from the sources that state or use this concept.",
          "items": {
            "$ref": "#/$defs/Evidence"
          },
          "type": "array"
        },
        "gloss": {
          "description": "One precise sentence saying what the concept is, in plain text with Unicode symbols\n(it is shown as a tooltip on links to the concept).",
          "type": "string"
        },
        "id": {
          "description": "Lowercase slug, unique across the graph, e.g. \"chirp-identity\".",
          "type": "string"
        },
        "known": {
          "description": "True if the reader profile already covers this concept.",
          "type": "boolean"
        },
        "name": {
          "description": "Display name in plain text, e.g. \"Chirp identity\". Write symbols in Unicode (κ, ω,\n≤, n log n), not LaTeX or spelled-out Greek: names appear in the navigation, which\ndoes not render mathematics.",
          "type": "string"
        },
        "requires": {
          "description": "Ids of the concepts a reader must understand before this one.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "symbols": {
          "description": "What each symbol in the title's mathematics denotes, one binding per symbol. A reader\nwho knows the concept is shown these, so give every symbol, however minor.",
          "items": {
            "$ref": "#/$defs/Binding"
          },
          "type": "array"
        },
        "title": {
          "description": "Only for a name with mathematics in it: the name with the mathematics in LaTeX, e.g.\n\"Polynomial ring modulo $y^r + 1$\". It is the heading of the concept's page.",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "required": [
        "id",
        "name",
        "aliases",
        "gloss",
        "requires",
        "known",
        "evidence"
      ],
      "type": "object"
    },
    "Evidence": {
      "additionalProperties": false,
      "properties": {
        "quote": {
          "description": "Text copied character for character from that source.",
          "type": "string"
        },
        "source": {
          "description": "Id of the source the quote comes from.",
          "type": "string"
        }
      },
      "required": [
        "source",
        "quote"
      ],
      "type": "object"
    },
    "Relation": {
      "oneOf": [
        {
          "const": "direct",
          "description": "The symbol denotes a thing: \"ω, a primitive root of unity\".",
          "type": "string"
        },
        {
          "const": "count",
          "description": "The symbol is the number of instances of something: \"r, the number of complex\ncoefficients in a record\".",
          "type": "string"
        }
      ]
    },
    "Resolution": {
      "additionalProperties": false,
      "properties": {
        "concept": {
          "description": "Id of the concept that covers it.",
          "type": "string"
        },
        "term": {
          "description": "The unresolved term, exactly as given.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "concept"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "concepts": {
      "description": "New concepts only; existing concepts must not be repeated.",
      "items": {
        "$ref": "#/$defs/Concept"
      },
      "type": "array"
    },
    "resolutions": {
      "description": "For every unresolved term, the id of the concept (existing or new) that covers it.",
      "items": {
        "$ref": "#/$defs/Resolution"
      },
      "type": "array"
    }
  },
  "required": [
    "concepts",
    "resolutions"
  ],
  "title": "ExtendAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0473-extend.answer.json`, then run `exegenius submit 0473-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
