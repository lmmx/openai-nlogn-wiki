# exegenius task 0474-argument

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Reconstruct the plan of the argument the sources make for the target result, as a tree of steps. Writers of the wiki's pages are given their page's step, and readers are shown where each page fits, so the plan says what each page is for.

- The root is the intention to show the target result. Each `show` step names a `method` that splits its claim into sub-steps, and a `motivation`: why that method suits the claim. Its `children` are the sub-steps, in the order the method takes them. An `infer` step is a single step the sources report: give its `quote`, copied exactly, and no children.
- Read the plan top down, as a reader of the sources would: "we show that", "it suffices to", "the key step is" and section structure mark the steps. Go down to the level the pages need: every page below is either the module that presents one step (`page`) or a concept some step relies on (`from`). Deeper steps of a page's own proof can stop at an `infer` step quoting where the sources carry them out.
- The sources report the plan in order: the infer steps' quotes must appear in the sources in the order of a depth-first walk of the tree (submit checks it). Mark an infer step `deferred` if the sources report it out of order.
- `motivation.source`: `explicit` if the sources state why the method is used (quote them), `recoverable` if a reader could work it out from what they say, `reconstructed` if you supply it. Do not mark a motivation explicit unless you can quote it. Writers are told to give readers every reconstructed motivation, since the sources will not.
- `from`: the concepts a step relies on, as ids: known concepts, or pages that come before the step's page in the reading order below. A step's page is its own `page` or the nearest ancestor's.
- `salient`: for a step whose claim has a feature a reader would find striking (a symmetry, a uniformity across cases, a surprising value or bound), that feature. A proof explains a result only relative to such a feature (Lange), so its page is asked to explain why the feature holds. Most steps have none.
- `adds`: symbols a step introduces for its sub-steps, each occurring in the mathematics ($...$) of the claims below it, with a display name, meaning and relation as for concept names.
- The target page presents the root. Give each other page at most one step; a page that presents no step must be in some step's `from`.

## Target

`main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Pages, in reading order

- `integer`: Integer: A whole number, positive, negative or zero.
- `logarithm`: Logarithm: The exponent to which a fixed base must be raised to give a positive number; lg n is the logarithm to base 2.
- `base-two-logarithm`: Base-2 logarithm: The logarithm to base 2, written lg n or log₂ n.
- `root-of-unity`: Root of unity: A complex number z for which some positive power of z equals one.
- `running-time-cost`: Running time cost: The number of machine steps an algorithm takes, as a worst-case function of the input length, on a machine with a fixed alphabet and fixed number of tapes.
- `exact-integer-multiplication`: Exact integer multiplication: Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
- `convolution`: Convolution: The product of two sequences in which each output index sums the products of pairs of input indices that combine to it.
- `payload`: Payload: The record data carried at each address of an array, as distinct from the address that locates it.
- `mathematical-induction`: Mathematical induction: A proof method that establishes a statement for all integers by proving a base case and that each case implies the next.
- `little-o-notation`: Little-o notation: A function f is o(g) when the ratio f/g tends to zero, a stronger statement than being O(g).
- `address`: Address: A label that locates one entry of an array, written as a string of address bits.
- `truncation`: Truncation: Discarding the fractional digits of a value beyond a fixed precision, here toward zero, so that the value stays on a fixed grid.
- `array`: Array: A finite collection of entries, each stored at an address and carrying a payload.
- `array-norm`: Array norm: The maximum modulus over all entries of an array of complex values; an array has norm at most one exactly when every entry has modulus at most one.
- `ceiling-function`: Ceiling function: The least integer that is not less than a given real number, written with brackets ⌈x⌉.
- `big-theta-notation`: Big-Theta notation: A function f is Θ(g) when f is both O(g) and bounded below by a constant multiple of g for large inputs.
- `extended-reals`: Extended real numbers: The real numbers together with two added values, positive infinity and negative infinity.
- `supremum`: Supremum: The least upper bound of a set of real numbers.
- `telescoping-identity`: Telescoping identity: A sum of differences of consecutive terms equals the difference of its first and last terms.
- `mixed-radix-digits`: Mixed-radix digits: The digits of an integer written in a positional system whose place values use a separate length for each place, so that the digit at each place ranges over its own length.
- `fixed-width-digit-blocks`: Fixed-width digit blocks: A coefficient stored as a block of a fixed number of digits in a positional system with base B, padded with leading zeros.
- `exceptional-set`: Exceptional set: The set of addresses at which a generic formula must be replaced by a special rule; the generic formula is correct everywhere outside it.
- `big-omega-notation`: Big-Omega notation: A function f is Ω(g) when f is bounded below by a positive constant times g for all sufficiently large inputs.
- `bit-reversed-order`: Bit-reversed index order: The order of array positions obtained by reversing the binary digits of each index.
- `directed-graph`: Directed graph: A set of vertices together with a set of ordered pairs of vertices, called directed edges.
- `linear-algebra-basics`: Linear algebra basics: Vector spaces over a field, linear maps and matrices, and the inverse of an invertible linear operator.
- `discrete-fourier-transform`: Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- `transform-axis`: Transform axis: One coordinate direction of a multidimensional array or transform, with its own length.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients.
- `linear-contraction`: Linear contraction: A linear map that does not increase the maximum modulus of any vector, so that errors pass through it without growing.
- `bilinear-map`: Bilinear map: A map that is linear in each of two vector arguments separately, such as the product of two polynomials.
- `coprime`: Coprime: Two integers are coprime when their greatest common divisor is 1; a set of integers is pairwise coprime when every two of them are coprime.
- `bezout-identity`: Bézout's identity: For integers a and b with greatest common divisor d, there are integers x and y with ax + by = d.
- `cyclic-group`: Cyclic group: A group whose elements are all powers of one fixed element, called a generator.
- `order-of-element`: Order of an element: The least positive integer k for which the k-th power of an element of a group is the identity.
- `diagonal-scaling`: Diagonal scaling: A linear operator that multiplies each coordinate by its own fixed scalar.
- `frequency-domain`: Frequency domain: The representation of a sequence by the values of its discrete Fourier transform.
- `projection-along-subspace`: Projection along a subspace: A linear map that keeps the component of a vector in one subspace and removes its component in a complementary subspace.
- `complex-disk`: Closed disk in the complex plane: The set of complex numbers whose distance from a fixed center is at most a fixed radius.
- `linear-functional`: Linear functional: A linear map from a vector space to its field of scalars.
- `dual-space`: Dual space: The vector space of all linear functionals on a given vector space.
- `floor-function`: Floor function: The greatest integer that is not greater than a given real number.
- `bijection`: Bijection: A map that is one-to-one and onto, so that every element of the target is hit by exactly one element of the source.
- `permutation`: Permutation: A bijection of a finite set onto itself, which rearranges the positions of a sequence.
- `address-field`: Address field: A contiguous block of address bits of an array, which an address interchange exchanges with another block of the same width.
- `linear-network-frames`: Linear networks and frames: A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame.
- `logical-array`: Logical array: The array of values that a role presents to the network, which may differ from the stored array by a frame.
- `cyclic-shift`: Cyclic shift: A rotation of the values of a block of positions by an offset taken modulo the block length, where the offset may be set by control bits.
- `butterfly`: Butterfly: The two-point map H0(u, v) = ((u + v)/2, (u − v)/2) applied to a pair of values, the elementary step of a Fourier-type transform.
- `radix-digit-convolution`: Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
- `ground-set`: Ground set: A finite set from which the subsets under consideration are chosen.
- `network-gate-terminal`: Gate and terminal of a network: A gate combines the values on the wires it touches by a fixed linear map, and a terminal is an input or output end of a wire where the network's values enter or leave.
- `incidence`: Incidence: The relation that a gate and a wire have when the wire touches the gate.
- `tensor-product`: Tensor product: The Kronecker product of two matrices, whose m-fold power applies one operator to m independent coordinates at once.
- `carry-propagation`: Carry propagation: Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
- `congruence-modulo`: Congruence: Two integers are congruent modulo m when their difference is divisible by m; a residue is the class of an integer modulo m.
- `schonhage-strassen`: Schönhage–Strassen multiplication: The fast integer multiplication method of Schönhage and Strassen, which multiplies n-bit integers in O(n log n log log n) time.
- `ring`: Ring: A set with addition and multiplication that satisfy the usual axioms, with addition forming a commutative group.
- `polynomial-ring-mod-yr-plus-1`: Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign.
- `limit-inferior`: Limit inferior: The smallest value that a sequence approaches infinitely often; its limit inferior is zero when it has subsequences that tend to zero.
- `n-log-n-conjecture`: The n log n optimality conjecture: The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers.
- `fixed-tape-model`: Fixed-tape machine model: A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input.
- `binary-field`: Binary field: The field with two elements 0 and 1, where addition is exclusive or and multiplication is AND.
- `modular-inverse`: Modular inverse: An integer a has an inverse modulo q when some integer b makes ab congruent to 1 modulo q; this holds exactly when a and q are coprime.
- `binary-change-of-basis`: Binary change of basis: An invertible change of basis of the selected address bits over the binary field, realised by row additions on bit positions.
- `bit-network`: Bit network: A linear network whose wires carry bits over the binary field and which realises a binary change of basis.
- `phase-factor`: Phase factor: A complex number of modulus one, such as a power of i, multiplied into coefficients; a scalar correction is a fixed constant factor of this kind.
- `gaussian-dyadics`: Gaussian dyadics: Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer.
- `two-point-kernel`: Two-point kernel: The two-by-two operator aI + bX, with X the bit flip, applied along one direction of a binary address; its coefficients are Gaussian dyadics.
- `gaussian-integer`: Gaussian integer: A complex number whose real and imaginary parts are both integers.
- `polynomial-ring`: Polynomial ring: The ring of polynomials in an indeterminate with complex coefficients, with the usual addition and multiplication, here reduced modulo a fixed polynomial.
- `grid-numerator`: Grid numerator: For a fixed precision, a grid value is an integer multiple of a fixed negative power of two, and its numerator is the integer multiplier.
- `chinese-remainder-theorem`: Chinese remainder theorem: For pairwise coprime moduli, a system of congruences has a solution, unique modulo the product of the moduli.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices wrap around modulo the sequence length.
- `ring-homomorphism`: Ring homomorphism and isomorphism: A map between rings that preserves addition and multiplication; it is an isomorphism when it is also bijective, so that the two rings have the same structure.
- `chinese-remainder-map`: Chinese-remainder map: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
- `forward-transform`: Forward transform: The discrete Fourier transform with the standard sign in its exponent, applied first in a convolution.
- `pointwise-product`: Pointwise product: The product of two sequences computed entry by entry, with each output entry the product of the two entries at that index.
- `opposite-transform`: Opposite transform: The discrete Fourier transform with the opposite sign in its exponent, which inverts the forward transform up to a normalizing factor.
- `iverson-bracket`: Iverson bracket: The value 1 when a stated condition is true and 0 when it is false.
- `axis-line`: Axis line: The set of entries of a multidimensional array that vary along one chosen axis while all other coordinates stay fixed.
- `near-linear-time`: Near-linear time: A running time of the form n times a polylogarithmic factor in n, such as n log n or n (log n) squared.
- `negacyclic-convolution`: Negacyclic convolution: A convolution in which indices that wrap around the sequence length pick up a minus sign.
- `neumann-series`: Neumann series: The series of powers of an operator with alternating signs, which inverts I plus a small operator when that operator has norm below one.
- `probability`: Probability: A number between 0 and 1 assigned to each event, additive over disjoint events, with 1 for the certain event.
- `independence`: Independence of events: Two events are independent when the probability that both occur equals the product of their probabilities.
- `radix-two-factorization`: Radix-two factorization: The factorization of a Fourier transform of length 2 to the power k into k levels of butterflies.
- `multidimensional-transform`: Multidimensional transform: A Fourier transform over several axes at once, computed by transforming along each axis in turn.
- `gaussian-resampling`: Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- `standard-basis-vector`: Standard basis vector: A vector with entry 1 in one fixed coordinate and 0 in every other coordinate.
- `matrix-rank`: Matrix rank: The number of linearly independent rows or columns of a matrix, taken over the rational numbers in the present context.
- `symmetric-matrix`: Symmetric matrix: A square matrix equal to its own transpose.
- `eigenvalue`: Eigenvalue: A scalar λ for which a linear operator maps some nonzero vector v to λv.
- `bilinear-form`: Bilinear form: A bilinear map from a vector space and itself to its scalars; a space with such a form is nondegenerate when the form has no nonzero vector orthogonal to everything, and two vectors are orthogonal when the form vanishes on them.
- `orthogonal-complement`: Orthogonal complement: The set of all vectors that are orthogonal to every vector of a given subspace.
- `indicator-vector`: Indicator vector: The 0-1 vector whose entries mark which elements of a ground set belong to a given subset.
- `line-spanned-by-vector`: Line spanned by a vector: The set of all scalar multiples of one nonzero vector, a one-dimensional subspace.
- `subspace-labels`: Subspace labels: Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.
- `subset-intersection-network`: Subset-intersection network: A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
- `scratch-storage`: Scratch storage: Auxiliary storage that a procedure may overwrite during its work but must restore to its starting contents, whatever those contents were.
- `address-interchange`: Address-field interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly.
- `xor`: Exclusive or: The bitwise sum modulo 2 of two bits, which is 1 exactly when the bits differ.
- `gram-matrix`: Gram matrix: The matrix whose entries are the values of a bilinear form on all pairs of a list of vectors.
- `complex-phase-network`: Complex phase network: A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time.
- `guard-width-bound`: Guard-width bound: An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices.
- `numerical-layer`: Numerical layer: A layer of the transform calculation in which a simultaneous butterfly is applied to a chosen set of selected axes.
- `union-bound`: Union bound: The probability that at least one of several events occurs is at most the sum of their probabilities; in counting form, the size of a union is at most the sum of the sizes.
- `transform-round`: Transform round: One step of a multidimensional transform in which a butterfly is applied on the participating axes at once, followed by the corresponding twiddle.
- `tape-procedure`: Tape procedure: A procedure that moves the contents of a Turing machine's tapes, such as the address fields of an array, in a bounded number of passes.
- `stream`: Stream: A sequence of records that a procedure reads or writes in order, one position at a time, on a tape.
- `bit-procedure`: Bit procedure: The first tape procedure, which interchanges two address fields by a shear built from the bit network over the binary field.
- `endpoint-operator`: Endpoint operator: The operator that a network realises on each role's array once all intermediate frames have cancelled, so that it depends only on the endpoint frames.
- `address-shear`: Address shear: The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges.
- `stable-radix-sort`: Stable radix sort: Sorting by successive passes over key digits from least to most significant, each pass stable so that equal keys keep their earlier order.
- `destination-rank`: Destination rank: The position a record takes in the final order after a move, given by its rank among the records in that order.
- `transform-identity`: Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
- `transform-layout`: Transform layout: A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
- `padded-transform-box`: Padded transform box: The full array of transform entries after every axis has been padded to its chosen length, with zero entries outside the valid region.
- `cyclic-coordinate`: Cyclic coordinate: One of the axes of a multidimensional cyclic convolution, with its own cyclic length.
- `prime-number`: Prime number: An integer greater than one whose only positive divisors are one and itself.
- `logical-bit-volume`: Logical bit volume: The number of bits in a padded transform box, counting every entry of the box at its record width.
- `cost-table`: Cost table: The list of separate running-time terms of an algorithm, each a power of the input size, whose sum bounds the total time.
- `established-multiplier`: Established O(n log n) multiplier: The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine.
- `signed-packing`: Signed coefficient packing: Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.
- `schoolbook-multiplication`: Schoolbook multiplication: Multiplication of two integers digit by digit by the grade-school method, which takes quadratic time in the number of digits.
- `centered-residue`: Centered residue: The representative of a residue class modulo B that lies in the interval from −B/2 to B/2, used to recover a signed coefficient.
- `polynomial-ring-convolution`: Convolution over the polynomial ring: The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.
- `normalized-cyclic-convolution`: Normalized cyclic convolution: A cyclic convolution divided by the transform length, the normalization for which a Fourier transform turns convolution into pointwise product.
- `bluestein-chirp-identity`: Bluestein's chirp identity: An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution.
- `normalization-scales`: Normalization scales: The known powers of two and transform lengths by which a computed product is multiplied to undo the normalizing factors of the transforms and the digit scaling.
- `middle-transform`: Middle transform: The transform on the target lengths that sits between the two Gaussian resampling maps, which Bluestein's identity turns into a cyclic convolution.
- `phase-twist`: Phase twist: A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring.
- `prime-source-lengths`: Prime source lengths: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.
- `recovery-and-error`: Exact coefficient recovery: The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
- `schedule`: Schedule: An ordered sequence of tape procedures applied one after another; the inverse schedule applies the inverses in reverse order.
- `bit-construction`: Bit construction: The construction of a subset-intersection network whose scalars lie in the binary field, with neighbours chosen by intersection size one.
- `complex-construction`: Complex construction: The construction of a subset-intersection network whose scalars are Gaussian dyadics, with neighbours chosen among distinct triples.
- `rank-saving-recursion`: Rank-saving recursion: The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
- `family-parameter`: Family parameter: A parameter that indexes a family of constructions and controls their sizes.
- `packed-bit-addition`: Packed selected-bit addition: An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Turing machines and tapes
- `real-numbers`: Real numbers

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Previous plan (revise it: the pages have changed since)

```json
{
  "id": "S0",
  "intention": "show",
  "claim": "Exact multiplication of two $n$-bit integers runs in $O(n(\\lg n)^{1-\\kappa})$ time on one deterministic fixed-tape machine, with $\\kappa = 2^{-182}$.",
  "from": [
    "n-log-n-conjecture",
    "exact-integer-multiplication",
    "fixed-tape-model",
    "running-time-cost",
    "schonhage-strassen",
    "logarithm",
    "base-two-logarithm",
    "big-o-notation",
    "little-o-notation"
  ],
  "method": "reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and recover the exact product",
  "motivation": {
    "text": "Linear combinations of intermediate data cut the cost of both address rearrangement and transform layers, which the fixed-tape bound needs.",
    "source": "explicit",
    "quote": {
      "source": "paper",
      "quote": "The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers"
    }
  },
  "salient": "A strict power saving in the logarithmic factor, valid for every input length.",
  "adds": [
    {
      "symbol": "n",
      "name": "input width",
      "meaning": "The number of bits in each of the two input integers.",
      "relation": "count"
    },
    {
      "symbol": "\\kappa",
      "name": "saving exponent",
      "meaning": "The fixed constant $2^{-182}$ that makes the logarithmic factor a power below $\\lg n$.",
      "relation": "direct"
    }
  ],
  "page": "main-theorem",
  "children": [
    {
      "id": "S1",
      "intention": "show",
      "claim": "Exact multiplication of two $n$-bit integers reduces to a convolution of short integer coefficients obtained by splitting each input into radix digits.",
      "from": [
        "exact-integer-multiplication",
        "integer",
        "convolution",
        "polynomials"
      ],
      "method": "split each input into radix digits and convolve",
      "motivation": {
        "text": "Short coefficients keep each convolution cheap, so the cost comes from the transforms rather than from the digits.",
        "source": "recoverable"
      },
      "page": "radix-digit-convolution",
      "children": [
        {
          "id": "S1.1",
          "intention": "infer",
          "claim": "Exact multiplication of $n$-bit integers reduces to convolution of short integer coefficients.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients"
          }
        }
      ]
    },
    {
      "id": "S2",
      "intention": "show",
      "claim": "The Fourier transforms of this convolution are replaced by multidimensional transforms whose axis lengths are powers of two.",
      "from": [
        "discrete-fourier-transform",
        "transform-axis",
        "multidimensional-transform",
        "radix-digit-convolution",
        "root-of-unity",
        "phase-factor"
      ],
      "method": "resample Gaussian weights onto power-of-two axes",
      "motivation": {
        "text": "Power-of-two axis lengths let the later steps use butterfly layers and polynomial transforms.",
        "source": "recoverable"
      },
      "page": "gaussian-resampling",
      "children": [
        {
          "id": "S2.1",
          "intention": "infer",
          "claim": "The Fourier transforms needed for the convolution become multidimensional transforms with power-of-two axes.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose"
          }
        }
      ]
    },
    {
      "id": "S3",
      "intention": "show",
      "claim": "After a further conversion to convolution, one coordinate of the array is stored as the coefficient list of a polynomial modulo $y^r + 1$, with $r$ a power of two.",
      "from": [
        "ring",
        "polynomial-ring",
        "root-of-unity",
        "polynomials",
        "complex-numbers"
      ],
      "method": "store one coordinate as polynomial coefficients whose powers of $y$ serve as roots of unity",
      "motivation": {
        "text": "Powers of $y$ serve as roots of unity, so multiplying by such a root is only a signed shift of the coefficient list.",
        "source": "recoverable"
      },
      "adds": [
        {
          "symbol": "y",
          "name": "polynomial variable",
          "meaning": "The indeterminate of the polynomial ring, whose powers act as roots of unity.",
          "relation": "direct"
        },
        {
          "symbol": "r",
          "name": "record length",
          "meaning": "The number of complex coefficients in a polynomial record, a power of two.",
          "relation": "count"
        }
      ],
      "page": "polynomial-ring-mod-yr-plus-1",
      "children": [
        {
          "id": "S3.1",
          "intention": "infer",
          "claim": "One coordinate is stored as the coefficient list of a polynomial modulo $y^r + 1$, with $r$ a power of two.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "one coordinate is stored as the coefficient list of a polynomial modulo y r + 1"
          }
        },
        {
          "id": "S3.2",
          "intention": "infer",
          "claim": "Powers of $y$ serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list"
          }
        }
      ]
    },
    {
      "id": "S4",
      "intention": "show",
      "claim": "The transforms are synthetic polynomial transforms whose roots of unity are powers of $y$.",
      "from": [
        "discrete-fourier-transform",
        "polynomial-ring",
        "pointwise-product",
        "root-of-unity",
        "polynomials"
      ],
      "method": "evaluate the transforms with polynomial roots of unity",
      "motivation": {
        "text": "Roots of unity that are powers of the variable cost only shifts and signs, so each transform reduces to address rearrangement and two-point butterflies.",
        "source": "recoverable"
      },
      "page": "synthetic-transforms",
      "children": [
        {
          "id": "S4.1",
          "intention": "infer",
          "claim": "The transforms are the synthetic polynomial transforms of Nussbaumer and Quandalle.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "These are the synthetic polynomial transforms of Nussbaumer and Quandalle and"
          }
        }
      ]
    },
    {
      "id": "S5",
      "intention": "show",
      "claim": "Two disjoint contiguous address fields of $u$ bits in an array can be interchanged in $O(V u^{\\tau})$ time for a fixed $\\tau<1$, where $V$ is the stored bit volume.",
      "from": [
        "fixed-tape-model",
        "address",
        "address-field",
        "array",
        "permutation",
        "bijection",
        "stream",
        "linear-network-frames"
      ],
      "method": "build the interchange from XOR combinations of intermediate data in a linear network",
      "motivation": {
        "text": "A permutation of fields can be built from XOR combinations, which a linear network carries out while restoring its scratch values.",
        "source": "recoverable"
      },
      "adds": [
        {
          "symbol": "u",
          "name": "field width",
          "meaning": "The number of bits in each of the two interchanged address fields.",
          "relation": "count"
        },
        {
          "symbol": "V",
          "name": "stored bit volume",
          "meaning": "The number of stored bits in the array, including every address field.",
          "relation": "count"
        }
      ],
      "page": "address-interchange",
      "children": [
        {
          "id": "S5.1",
          "intention": "infer",
          "claim": "Two disjoint contiguous address fields of $u$ bits are interchanged by the first procedure.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "The first procedure interchanges two disjoint contiguous address fields of u bits in an array whose addresses form a complete Cartesian product"
          }
        },
        {
          "id": "S5.2",
          "intention": "infer",
          "claim": "The interchange costs $O(V u^{\\tau})$ for a fixed $\\tau<1$, where $V$ is the stored bit volume.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Its cost is O(V uτ ) for a fixed τ < 1."
          }
        },
        {
          "id": "S5.3",
          "intention": "infer",
          "claim": "Its intermediate steps form pointwise XOR combinations of data, and the final permutation is exact for arbitrary initial auxiliary values.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values."
          }
        }
      ]
    },
    {
      "id": "S6",
      "intention": "show",
      "claim": "A butterfly layer on the selected coordinate bits of several axes is applied at once, in a single tape procedure.",
      "from": [
        "butterfly",
        "gaussian-dyadics",
        "gaussian-integer",
        "two-point-kernel",
        "tensor-product",
        "diagonal-scaling",
        "eigenvalue",
        "discrete-fourier-transform",
        "phase-factor",
        "complex-phase-network",
        "address-interchange"
      ],
      "method": "apply the layer to all selected bits together in one tape procedure",
      "motivation": {
        "text": "A single pass avoids the whole-array scans that separate butterfly factors would need.",
        "source": "explicit",
        "quote": {
          "source": "paper",
          "quote": "whereas separate butterfly factors would require D whole-array passes"
        }
      },
      "page": "simultaneous-butterfly-layer",
      "children": [
        {
          "id": "S6.1",
          "intention": "infer",
          "claim": "The second procedure applies the two-point map $H_0$ to selected coordinate bits simultaneously.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "simultaneously on selected coordinate bits of the numerical arrays"
          }
        }
      ]
    },
    {
      "id": "S7",
      "intention": "show",
      "claim": "Each tape procedure is a fixed linear network that exchanges two banks of values and restores its scratch values.",
      "from": [
        "linear-algebra-basics",
        "stream",
        "array",
        "address",
        "address-field",
        "bijection",
        "permutation"
      ],
      "method": "realise each procedure as a fixed linear network with frames on its wires",
      "motivation": {
        "text": "Frames on the wires let a pointwise gate act on arrays without disturbing their representation.",
        "source": "recoverable"
      },
      "page": "linear-network-frames",
      "children": [
        {
          "id": "S7.1",
          "intention": "infer",
          "claim": "Each procedure arises from its own fixed linear network that exchanges two banks of values.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Each procedure arises from its own fixed linear network that exchanges two banks of values"
          }
        },
        {
          "id": "S7.2",
          "intention": "infer",
          "claim": "Each vertex carries an invertible operator called its frame, and the stored array is $D_v g$ when the logical array is $g$.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "We call Dv its frame: the stored array is Dv g when the logical array is g."
          }
        }
      ]
    },
    {
      "id": "S8",
      "intention": "show",
      "claim": "A linear network on the three-element subsets of a ground set exchanges two banks of values and restores its scratch wires.",
      "from": [
        "ground-set",
        "indicator-vector",
        "logical-array",
        "network-gate-terminal",
        "incidence",
        "matrix-rank",
        "binary-field",
        "bilinear-map",
        "bilinear-form",
        "orthogonal-complement",
        "line-spanned-by-vector",
        "projection-along-subspace",
        "subspace-labels",
        "bit-network",
        "linear-network-frames"
      ],
      "method": "label the triples by subspaces whose inclusions bound the change of frame",
      "motivation": {
        "text": "Orthogonality of the indicator vectors gives subspace assignments with the nesting that the change of frame needs.",
        "source": "recoverable"
      },
      "page": "subset-intersection-network",
      "children": [
        {
          "id": "S8.1",
          "intention": "infer",
          "claim": "The subspaces at adjacent vertices are nested.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "The subspaces at adjacent vertices are nested."
          }
        },
        {
          "id": "S8.2",
          "intention": "infer",
          "claim": "The construction uses three-element subsets, with gather and scatter creating coefficients by intersection size.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "The construction uses three-element subsets: gather and scatter create coefficients"
          }
        },
        {
          "id": "S8.3",
          "intention": "infer",
          "claim": "Orthogonality of the corresponding indicator vectors permits the subspace assignments.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Orthogonality of the corresponding indicator vectors permits the subspace assignments."
          }
        }
      ]
    },
    {
      "id": "S9",
      "intention": "show",
      "claim": "The total number $s$ of smaller calls satisfies $s < Wm$, so each recursive level saves a strict power.",
      "from": [
        "subset-intersection-network",
        "address-interchange",
        "xor",
        "tape-procedure",
        "bit-procedure",
        "complex-phase-network",
        "complex-construction",
        "bit-construction",
        "endpoint-operator",
        "address-shear",
        "scratch-storage",
        "binary-change-of-basis",
        "numerical-layer",
        "cyclic-shift",
        "stream",
        "payload",
        "mathematical-induction",
        "logical-bit-volume",
        "family-parameter"
      ],
      "method": "count the smaller calls against the wire count and the label dimension",
      "motivation": {
        "text": "A recursion whose branching factor $s/W$ is strictly below $m$ shrinks the cost by a strict power at each level.",
        "source": "recoverable"
      },
      "adds": [
        {
          "symbol": "s",
          "name": "smaller call count",
          "meaning": "The number of smaller calls made on each edge of one network invocation.",
          "relation": "count"
        },
        {
          "symbol": "W",
          "name": "wire count",
          "meaning": "The number of wires in the network.",
          "relation": "count"
        },
        {
          "symbol": "m",
          "name": "label dimension",
          "meaning": "The number of coordinates of each vector in the label space.",
          "relation": "count"
        }
      ],
      "page": "rank-saving-recursion",
      "children": [
        {
          "id": "S9.1",
          "intention": "infer",
          "claim": "The total number $s$ of smaller calls satisfies $s < Wm$.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "the total number s of smaller calls satisfies s < W m"
          }
        },
        {
          "id": "S9.2",
          "intention": "infer",
          "claim": "The strict inequality $s/W < m$ is the source of the power saving.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "This strict inequality is the source of the power saving"
          }
        }
      ]
    },
    {
      "id": "S10",
      "intention": "show",
      "claim": "The radix-digit coefficients are placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.",
      "from": [
        "cyclic-convolution",
        "cyclic-coordinate",
        "cyclic-group",
        "radix-digit-convolution",
        "mixed-radix-digits",
        "coprime",
        "modular-inverse",
        "congruence-modulo",
        "chinese-remainder-theorem",
        "bezout-identity",
        "prime-number",
        "padded-transform-box"
      ],
      "method": "relabel the coefficients by mixed-radix digits for the coprime axis lengths",
      "motivation": {
        "text": "Mixed-radix relabelling turns one cyclic convolution into a multidimensional one whose axis lengths are pairwise coprime.",
        "source": "recoverable"
      },
      "page": "chinese-remainder-map",
      "children": [
        {
          "id": "S10.1",
          "intention": "infer",
          "claim": "The radix-digit coefficient list is placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution."
          }
        }
      ]
    },
    {
      "id": "S11",
      "intention": "show",
      "claim": "Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform, with the source and target coordinate permutations kept in the transform identity.",
      "from": [
        "discrete-fourier-transform",
        "multidimensional-transform",
        "transform-axis",
        "tensor-product",
        "gaussian-resampling",
        "stable-radix-sort",
        "destination-rank",
        "cyclic-convolution",
        "frequency-domain",
        "opposite-transform",
        "permutation"
      ],
      "method": "keep both permutations in the transform formula",
      "motivation": {
        "text": "Keeping the permutations in the formula means they cancel across the convolution instead of being executed as separate sorts.",
        "source": "explicit",
        "quote": {
          "source": "paper",
          "quote": "so they need not be executed as separate full sorts"
        }
      },
      "page": "transform-identity",
      "children": [
        {
          "id": "S11.1",
          "intention": "infer",
          "claim": "Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform."
          }
        },
        {
          "id": "S11.2",
          "intention": "infer",
          "claim": "The source and target coordinate permutations are retained in the transform identity.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Section 8 retains the source and target coordinate permutations in the transform identity"
          }
        }
      ]
    },
    {
      "id": "S12",
      "intention": "show",
      "claim": "The middle transform, including its target permutation, becomes a normalized cyclic convolution.",
      "from": [
        "cyclic-convolution",
        "cyclic-coordinate",
        "normalized-cyclic-convolution",
        "discrete-fourier-transform",
        "transform-identity",
        "frequency-domain",
        "opposite-transform",
        "phase-factor"
      ],
      "method": "rewrite the transform as a cyclic convolution multiplied by chirp factors",
      "motivation": {
        "text": "A chirp factorisation turns the middle transform into a cyclic convolution, which the earlier steps already compute.",
        "source": "recoverable"
      },
      "page": "bluestein-chirp-identity",
      "children": [
        {
          "id": "S12.1",
          "intention": "infer",
          "claim": "Bluestein’s chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Bluestein’s chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution."
          }
        }
      ]
    },
    {
      "id": "S13",
      "intention": "show",
      "claim": "A phase twist turns the last cyclic coordinate into a coordinate of the polynomial ring modulo $y^r + 1$.",
      "from": [
        "polynomial-ring",
        "polynomial-ring-mod-yr-plus-1",
        "ring-homomorphism",
        "root-of-unity",
        "phase-factor",
        "cyclic-coordinate",
        "cyclic-convolution",
        "bluestein-chirp-identity"
      ],
      "method": "multiply the coefficients by roots of unity",
      "motivation": {
        "text": "The twist makes the wrap-around of the cyclic convolution match the negative wrap of the polynomial ring.",
        "source": "recoverable"
      },
      "page": "phase-twist",
      "children": [
        {
          "id": "S13.1",
          "intention": "infer",
          "claim": "A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r + 1$.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "A phase twist changes the last cyclic coordinate into a polynomial modulo y r + 1"
          }
        },
        {
          "id": "S13.2",
          "intention": "infer",
          "claim": "Its negative wrap gives precisely the original cyclic wrap after the twist is removed.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "its negative wrap gives precisely the original cyclic wrap after the twist is removed."
          }
        }
      ]
    },
    {
      "id": "S14",
      "intention": "show",
      "claim": "Convolution on the remaining axes over the polynomial ring is computed by two forward synthetic transforms, a pointwise product, an opposite transform, and packed integer products.",
      "from": [
        "polynomial-ring",
        "polynomial-ring-mod-yr-plus-1",
        "synthetic-transforms",
        "opposite-transform",
        "signed-packing",
        "established-multiplier",
        "ring-homomorphism",
        "phase-twist",
        "simultaneous-butterfly-layer",
        "transform-round",
        "transform-layout",
        "numerical-layer",
        "array-norm",
        "bilinear-map",
        "convolution",
        "cyclic-convolution",
        "normalized-cyclic-convolution",
        "tape-procedure"
      ],
      "method": "pack the coefficients into integers, multiply them, and unpack",
      "motivation": {
        "text": "Packing turns each polynomial product into an integer product that the established multiplier can compute.",
        "source": "recoverable"
      },
      "page": "polynomial-ring-convolution",
      "children": [
        {
          "id": "S14.1",
          "intention": "infer",
          "claim": "Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring."
          }
        },
        {
          "id": "S14.2",
          "intention": "infer",
          "claim": "The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order."
          }
        },
        {
          "id": "S14.3",
          "intention": "infer",
          "claim": "Their polynomial products use signed packing and the established $O(n \\log n)$ multiplier as an ordinary subroutine.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Their polynomial products use signed packing and the established O(n log n) multiplier as an ordinary subroutine"
          }
        }
      ]
    },
    {
      "id": "S15",
      "intention": "show",
      "claim": "The recovered coefficient error is strictly below $1/2$, so rounding returns the exact integer coefficients.",
      "from": [
        "polynomial-ring-convolution",
        "guard-width-bound",
        "phase-twist",
        "array-norm",
        "grid-numerator",
        "linear-contraction",
        "truncation",
        "centered-residue",
        "union-bound",
        "independence",
        "supremum",
        "telescoping-identity",
        "signed-packing",
        "normalization-scales"
      ],
      "method": "bound the error accumulated through each stage",
      "motivation": {
        "text": "Once the total error is below one half, rounding to the nearest integer returns the true coefficient.",
        "source": "recoverable"
      },
      "page": "recovery-and-error",
      "children": [
        {
          "id": "S15.1",
          "intention": "infer",
          "claim": "The recovered coefficient error is strictly below $1/2$.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Section 9 removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below 1/2"
          }
        }
      ]
    },
    {
      "id": "S16",
      "intention": "show",
      "claim": "Carries across the radix digits turn the recovered integer coefficients into the exact binary product.",
      "from": [
        "radix-digit-convolution",
        "exact-integer-multiplication",
        "integer",
        "ceiling-function"
      ],
      "method": "propagate carries through the coefficients in increasing order",
      "motivation": {
        "text": "Carry propagation converts the integer coefficient vector into a binary string with the same value.",
        "source": "recoverable"
      },
      "page": "carry-propagation",
      "children": [
        {
          "id": "S16.1",
          "intention": "infer",
          "claim": "Carries are propagated to obtain the exact binary product.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "propagates carries to obtain the exact binary product"
          }
        }
      ]
    },
    {
      "id": "S17",
      "intention": "infer",
      "claim": "The parameters can be chosen so that every term in the cost table is $O(n(\\lg n)^{1-\\kappa})$ for $\\kappa = 2^{-182}$, which gives the bound of the theorem.",
      "from": [
        "cost-table",
        "prime-source-lengths",
        "packed-bit-addition",
        "limit-inferior",
        "extended-reals",
        "little-o-notation",
        "big-theta-notation",
        "logarithm",
        "base-two-logarithm",
        "schoolbook-multiplication",
        "running-time-cost",
        "established-multiplier",
        "guard-width-bound",
        "subspace-labels",
        "gaussian-dyadics",
        "transform-layout",
        "address-shear",
        "cyclic-shift",
        "telescoping-identity"
      ],
      "quote": {
        "source": "paper",
        "quote": "A compatible choice of rational parameters makes all terms in its cost table fit Theorem 1"
      }
    }
  ]
}
```

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
    "Intention": {
      "oneOf": [
        {
          "const": "show",
          "description": "Show a claim by a method that splits it into sub-steps.",
          "type": "string"
        },
        {
          "const": "infer",
          "description": "Infer one claim in a single step the sources report.",
          "type": "string"
        }
      ]
    },
    "Motivation": {
      "additionalProperties": false,
      "description": "Why a method suits the claim it shows.",
      "properties": {
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an explicit motivation, the sources' words, copied exactly."
        },
        "source": {
          "$ref": "#/$defs/Provenance",
          "description": "Whether the sources state the reason, leave it to be worked out, or neither."
        },
        "text": {
          "description": "The reason, in one or two sentences.",
          "type": "string"
        }
      },
      "required": [
        "text",
        "source"
      ],
      "type": "object"
    },
    "Node": {
      "additionalProperties": false,
      "description": "One step of the argument.",
      "properties": {
        "adds": {
          "description": "Symbols the step introduces, in force in its sub-steps.",
          "items": {
            "$ref": "#/$defs/Binding"
          },
          "type": "array"
        },
        "children": {
          "description": "For a show step: its sub-steps, in the order the method takes them.",
          "items": {
            "$ref": "#/$defs/Node"
          },
          "type": "array"
        },
        "claim": {
          "description": "What the step shows or infers, in one sentence, with mathematics in LaTeX ($...$).",
          "type": "string"
        },
        "deferred": {
          "description": "For an infer step the sources report out of order, before or after the steps around\nit.",
          "type": "boolean"
        },
        "from": {
          "default": [],
          "description": "Ids of the concepts the step relies on: known concepts, or pages before the step's\npage.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "id": {
          "description": "A short label, unique in the tree, such as \"S0\" or \"S2.1\".",
          "type": "string"
        },
        "intention": {
          "$ref": "#/$defs/Intention"
        },
        "method": {
          "description": "For a show step: how the claim is shown, in a phrase (\"reduce to a cyclic\nconvolution and bound its cost\").",
          "type": [
            "string",
            "null"
          ]
        },
        "motivation": {
          "anyOf": [
            {
              "$ref": "#/$defs/Motivation"
            },
            {
              "type": "null"
            }
          ],
          "description": "For a show step: why that method suits the claim."
        },
        "page": {
          "description": "Id of the page that presents this step and its sub-steps, if one does.",
          "type": [
            "string",
            "null"
          ]
        },
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an infer step: the step as the sources report it, copied exactly."
        },
        "salient": {
          "description": "For a step whose claim has a feature a reader would find striking (a symmetry, a\nuniformity across cases, a surprising value or bound): that feature. The page should\nexplain why it holds, from a matching feature of the method.",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "required": [
        "id",
        "intention",
        "claim"
      ],
      "type": "object"
    },
    "Provenance": {
      "oneOf": [
        {
          "const": "explicit",
          "description": "The sources state the reason; quote them.",
          "type": "string"
        },
        {
          "const": "recoverable",
          "description": "The sources do not state it, but a reader can work it out from what they say.",
          "type": "string"
        },
        {
          "const": "reconstructed",
          "description": "The sources neither state it nor make it recoverable: you supply it.",
          "type": "string"
        }
      ]
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
    }
  },
  "additionalProperties": false,
  "properties": {
    "root": {
      "$ref": "#/$defs/Node",
      "description": "The main step: to show the target result."
    }
  },
  "required": [
    "root"
  ],
  "title": "ArgumentAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0474-argument.answer.json`, then run `exegenius submit 0474-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
