# exegenius task 0233-extend

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

## Unresolved terms

- "address"
  - on page `union-bound`: "An address is exceptional when at least one of its guards is bad"
- "address-field interchange procedure"
  - on page `xor`: "The paper's address-field interchange procedure uses this operation"
- "array"
  - on page `linear-algebra-basics`: "an invertible linear operator on arrays"
- "base-2 logarithm"
  - on page `carry-propagation`: "The paper takes $b = \lceil \log_2 n \rceil$ for large $n$"
- "Bezout's identity"
  - on page `modular-inverse`: "Bézout's identity gives integers"
- "Big-Theta notation"
  - on page `guard-width-bound`: "Here $\varepsilon$ is the exponent in $d=\Theta(p^{\varepsilon})$"
- "bijection"
  - on page `transform-identity`: "Both permutations are bijections"
- "bilinear contraction"
  - on page `bilinear-map`: "For a bilinear contraction, distance between the two values"
- "binary addresses"
  - on page `address-field`: "with binary addresses"
- "binary label"
  - on page `subspace-labels`: "for a binary label $U$"
- "bit-complexity bound"
  - on page `main-theorem`: "a bit-complexity bound, not a practical algorithm"
- "bit construction"
  - on page `indicator-vector`: "In the bit construction,, so the indicator vectors lie in $\mathbb{Q}^h$."
  - on page `rank-saving-recursion`: "The bit construction has, giving $s=Wm-\mu+2L$, as states."
- "bit network"
  - on page `xor`: "The bit network of the paper likewise"
  - on page `subspace-labels`: "For the bit network take"
- "butterfly layers"
  - on page `gaussian-integer`: "the butterfly layers and transforms that act on those arrays keep exact values"
- "Butterfly operation"
  - on page `radix-digit-convolution`: "butterfly operations over the whole array"
- "butterfly round"
  - on page `cost-table`: "individual butterfly rounds"
- "carry"
  - on page `xor`: "It is the one-bit sum without a carry"
- "ceiling function"
  - on page `carry-propagation`: "Let $q = \lceil n/b \rceil$ be the number of digits in each input, as on that page."
- "Chinese remainder theorem"
  - on page `cyclic-convolution`: "the Chinese remainder theorem relabels each position by its residues"
- "chirp and twist"
  - on page `cost-table`: "Chirps, twists and scalar products"
- "coefficient bound"
  - on page `bilinear-map`: "a coefficient bound"
- "complex construction"
  - on page `indicator-vector`: "In the complex construction,, so they lie in $\mathbb{F}_2^h$ with the ordinary dot product."
  - on page `rank-saving-recursion`: "The complex construction gives $s=Wm-2\mu+2L$, as states."
- "construction constant of the source"
  - on page `recovery-and-error`: "Here $\gamma$ is the construction constant of the source."
- "coordinate permutations"
  - on page `padded-transform-box`: "its coordinate permutations rearrange entries of the box"
- "copy step"
  - on page `binary-field`: "The coefficient that a copy step places between two sets"
- "CRT"
  - on page `cost-table`: "CRT and axis layouts"
- "current recursive length, level the round processes"
  - on page `transform-round`: "the number of entries that axis holds at the level the round processes"
- "Cyclic group"
  - on page `coprime`: "so the element generates a cyclic group with exactly as many elements as the product of the axes"
- "cyclic group of order S"
  - on page `modular-inverse`: "the generator $\xi$ of a cyclic group of order $S$"
- "der Hoeven"
  - on page `established-multiplier`: "The source calls it der Hoeven."
- "destination key"
  - on page `stable-radix-sort`: "their destination keys are distinct"
- "diagonal scaling"
  - on page `transform-identity`: "let $\Lambda$ be a diagonal scaling"
- "disk array"
  - on page `bilinear-map`: "the other operand is a disk array"
- "Edge change"
  - on page `matrix-rank`: "An edge change given by a matrix of rank $a$ is implemented"
- "eigenvalues"
  - on page `bilinear-form`: "The matrix $J$ has eigenvalues $100$ and $0$"
  - on page `subset-intersection-network`: "then $J$ has eigenvalues $h$ and $0$"
- "exact multiplication"
  - on page `convolution`: "It is the computation that exact multiplication is reduced to"
- "exceptional addresses"
  - on page `destination-rank`: "Since the move permutes the exceptional addresses"
- "extended reals"
  - on page `limit-inferior`: "its limit exists in the extended reals"
- "extracted records"
  - on page `destination-rank`: "the extracted records are sorted by"
  - on page `stable-radix-sort`: "the extracted exceptional records"
- "family parameter"
  - on page `packed-bit-addition`: "since $\zeta$ is polynomial in the family parameter"
- "field interchanges"
  - on page `endpoint-operator`: "implemented by a small number of field interchanges"
- "finite set"
  - on page `ground-set`: "is a finite set from which the subsets under consideration are chosen"
- "fixed track"
  - on page `destination-rank`: "on a fixed track of the stream"
- "forward schedule"
  - on page `scratch-storage`: "The forward schedule has eight rows"
- "Fourier transform"
  - on page `transform-axis`: "replaces the Fourier transforms of the convolution"
- "frequency-domain"
  - on page `opposite-transform`: "turns frequency-domain products back into coefficients"
- "frequency order"
  - on page `opposite-transform`: "keep its frequency order, since"
- "gate applied pointwise"
  - on page `xor`: "a gate applied pointwise acts at each address separately"
- "gather and scatter"
  - on page `scratch-storage`: "gather them, scatter them back into the target"
- "Gaussian corrections"
  - on page `gaussian-resampling`: "A map $N$ built from $T$ and Gaussian corrections"
- "Gaussian line map"
  - on page `cost-table`: "the factor in the cost of the Gaussian line maps"
- "Group Z/lambda_1 x ... x Z/lambda_M"
  - on page `coprime`: "In the group $\mathbb{Z}/\lambda_1\times\cdots\times\mathbb{Z}/\lambda_M$"
- "hole"
  - on page `destination-rank`: "marks its hole, the position it returns to"
- "incidence"
  - on page `rank-saving-recursion`: "because all incidences of one gate carry the same label"
- "independence"
  - on page `union-bound`: "The bound needs no independence between the events."
- "induction"
  - on page `stable-radix-sort`: "To see this by induction"
- "integer"
  - on page `congruence-modulo`: "Congruence is the relation between two integers that they leave the same remainder"
- "integer multiplication argument"
  - on page `normalization-scales`: "The integer multiplication argument uses them as its last arithmetic step"
- "integer multiplication result below n lg n"
  - on page `little-o-notation`: "the integer multiplication result below $n\lg n$"
- "intersection"
  - on page `ground-set`: "the size of their intersection is what distinguishes"
- "label-and-sort operations"
  - on page `transform-identity`: "uses two label-and-sort operations"
- "layer"
  - on page `truncation`: "the algorithm does not truncate inside a layer"
- "limit as lambda tends to infinity"
  - on page `little-o-notation`: "\lim_{\lambda \to \infty} \frac{\varphi(\lambda)}{\psi(\lambda)} = 0."
- "linear-cost update"
  - on page `bit-procedure`: "which is the linear-cost direction"
- "linear-readout version"
  - on page `scratch-storage`: "The paper's schedule is the linear-readout version of that construction."
- "logarithm"
  - on page `main-theorem`: "$O(n(\lg n)^{1-\kappa})$"
- "logarithm and ceiling"
  - on page `stable-radix-sort`: "$\lceil \log_2 M \rceil$ bits"
- "logarithm lg"
  - on page `bluestein-chirp-identity`: "runs in $O(n(\lg n)^{1-\kappa})$ time"
- "logical array"
  - on page `endpoint-operator`: "for the logical array $g$"
- "logical array and stored array"
  - on page `linear-algebra-basics`: "When the logical array is $g$, the stored array is $D_v g$"
- "logical bit volume"
  - on page `cost-table`: "for the logical bit volume of the padded box"
- "Lower triangular factors and partial permutation matrix"
  - on page `matrix-rank`: "factorization into lower triangular factors and a partial permutation matrix"
- "main bound"
  - on page `address-shear`: "whose cost enters the main bound."
- "Matrix shear"
  - on page `matrix-rank`: "The paper uses it to count the interchanges needed to apply one matrix shear on address fields"
- "modulo arithmetic"
  - on page `binary-field`: "Addition modulo $2$ on integers gives the same table"
- "move"
  - on page `destination-rank`: "Let $q$ be the address of a record before the move"
- "multivariate quotient ring"
  - on page `ring-homomorphism`: "from a cyclic quotient ring into a multivariate quotient ring"
- "network of wires and gates"
  - on page `ground-set`: "the wires and gates of the network that the later pages build"
- "network, vertex, edge"
  - on page `linear-algebra-basics`: "each vertex $v$ of the network carries a frame $D_v$"
- "normalized form"
  - on page `discrete-fourier-transform`: "The argument uses its normalized form:."
- "Order of an element"
  - on page `coprime`: "has order $\operatorname{lcm}(\lambda_1,\dots,\lambda_M)$"
- "orthogonal complement"
  - on page `line-spanned-by-vector`: "the sink role carries the orthogonal complement of the line"
- "orthogonal residual of an edge"
  - on page `complex-phase-network`: "where $R$ is the orthogonal residual of the edge."
- "packed polynomial product"
  - on page `cost-table`: "Packed polynomial products"
- "permutation"
  - on page `address-field`: "so an interchange is a permutation of addresses"
  - on page `xor`: "Its final effect is an exact permutation"
  - on page `transform-layout`: "is an explicit permutation $L$ of record addresses"
- "pointwise linear gate"
  - on page `network-gate-terminal`: "A pointwise linear gate commutes with its frame"
- "pointwise product"
  - on page `opposite-transform`: "the forward transforms of two inputs are multiplied pointwise"
- "polynomial suffix"
  - on page `transform-layout`: "preserves each record's polynomial suffix"
- "prefix-slot move"
  - on page `cost-table`: "Prefix-slot moves and individual butterfly rounds"
- "prime"
  - on page `prime-source-lengths`: "distinct odd primes $s_1,\dots,s_d$"
- "projection along a subspace"
  - on page `subspace-labels`: "let $P_U$ project onto $U$ along $U^\perp$"
- "rank of a shear"
  - on page `bit-procedure`: "carried out by one interchange per unit of rank"
- "record"
  - on page `numerical-layer`: "that is, a polynomial with $r$ complex coefficients stored as its coefficient list"
- "rectangular routine"
  - on page `destination-rank`: "the integers the rectangular routine handles"
- "reduction axis"
  - on page `multidimensional-transform`: "the reduction axis lengths are powers of two"
- "residual basis of directions"
  - on page `binary-change-of-basis`: "puts a residual basis of directions into coordinate positions"
- "ring"
  - on page `phase-factor`: "A unit of a ring is an element whose inverse also lies in the ring."
  - on page `polynomial-ring`: "is the ring of complex polynomials in $y$"
  - on page `polynomial-ring-mod-yr-plus-1`: "The polynomial ring modulo $y^r+1$ is the set of polynomials with complex coefficients"
- "role stream"
  - on page `rank-saving-recursion`: "each on one role stream of $V/W$ bits"
- "roots of unity"
  - on page `transform-axis`: "the remaining axes take powers of $y$ as their roots of unity"
  - on page `phase-factor`: "the fourth roots of unity $1, i, -1, -i$"
- "Row reduction and pivots"
  - on page `matrix-rank`: "Row reduction computes it: each pivot that elimination finds is one independent row, and the number of pivots is the rank."
- "scalar network"
  - on page `endpoint-operator`: "the signed role permutation realised by the scalar network"
- "scan"
  - on page `stable-radix-sort`: "Each pass is one scan of the extracted records and keys"
- "Schönhage and Strassen"
  - on page `fixed-tape-model`: "Schönhage and Strassen."
- "Schönhage–Strassen bound"
  - on page `limit-inferior`: "to the Schönhage–Strassen bound, as defined below"
- "segment"
  - on page `union-bound`: "Each of the $f-1$ segment pairs carries two guard values"
- "selected address bits"
  - on page `binary-change-of-basis`: "on a block of selected address bits"
- "selected bit"
  - on page `transform-layout`: "It places the selected bits of all participating axes at one common offset"
- "selected bits"
  - on page `phase-factor`: "the selected bits of that address"
- "shear of address pairs"
  - on page `linear-algebra-basics`: "acts on array entries by a shear of their address pairs"
- "side and central wires"
  - on page `scratch-storage`: "the side and central wires that carry intermediate sums"
- "signed shifts"
  - on page `multidimensional-transform`: "makes the roots of unity signed shifts"
  - on page `butterfly`: "sit alongside address rearrangements and signed shifts"
- "sink"
  - on page `phase-factor`: "at each affected sink"
- "source and sink vertices"
  - on page `linear-network-frames`: "(a source, gate or sink)"
- "stream"
  - on page `destination-rank`: "A counter that moves through the stream computes it"
- "stream position"
  - on page `packed-bit-addition`: "counts the bits of a stream position"
- "supremum"
  - on page `linear-contraction`: "$\|L\| = \sup_{\|w\| \le 1} \|Lw\|$"
- "tape procedure"
  - on page `bit-procedure`: "the first of the two tape procedures that move address fields in an array"
- "target"
  - on page `normalized-cyclic-convolution`: "On the way to the target"
- "telescoping identity"
  - on page `mixed-radix-digits`: "The proof uses the telescoping identity"
- "the conjecture"
  - on page `fixed-tape-model`: "the conjecture is a claim about each machine separately"
- "The map that splits the length-S axis"
  - on page `coprime`: "The map that splits the length-$S$ axis into the axes of lengths $s_1,\dots,s_d$ then relies on"
- "the multiplication algorithm"
  - on page `address-field`: "the operation the multiplication algorithm uses"
- "the paper's bit network"
  - on page `bilinear-form`: "The paper's bit network uses a larger example., and the ground-set size is."
- "the paper's construction"
  - on page `schoolbook-multiplication`: "the paper's construction falls back on for small inputs"
- "The paper's factorization lemma"
  - on page `matrix-rank`: "The paper's factorization lemma applies to every such matrix"
- "the theorem"
  - on page `packed-bit-addition`: "contributes one term to the [cost table](cost-table.md) of the theorem."
- "the theorem's bound"
  - on page `schoolbook-multiplication`: "which fits the bound of the theorem"
- "transform layout and packed selected-bit addition"
  - on page `simultaneous-butterfly-layer`: "the transform layout and packed selected-bit addition pages build on it"
- "two-point butterfly map"
  - on page `tensor-product`: "Its intended operation is the two-point butterfly map on each selected bit"
- "two-point map"
  - on page `gaussian-dyadics`: "The simultaneous butterfly layer applies a two-point map to several selected address bits in one pass."
- "two-point operator on selected bits"
  - on page `tensor-product`: "apply one two-point operator to several selected bits in a single pass"
- "unit modulo M_i"
  - on page `modular-inverse`: "each exponent is a unit modulo $M_i$"
- "usual axioms"
  - on page `linear-algebra-basics`: "satisfying the usual axioms"

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

Write the answer to `exegenius/tasks/0233-extend.answer.json`, then run `exegenius submit 0233-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
