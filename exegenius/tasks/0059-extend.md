# exegenius task 0059-extend

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Extend a prerequisite graph of concepts built from source documents. Audits of the wiki reported terms that they judged a specific reader cannot follow and that match no existing concept. For each term, point it at an existing concept that covers it, add a new concept, or list it under `inline` to be explained in a sentence where it is used.

- Auditors can misjudge what the reader profile covers. A term the profile covers, whether or not it names it, is known to the reader: point it at a known concept, or add one with `known: true`. Known concepts get no page.
- Add a new concept only when no existing concept covers the term and the term needs a page of its own; a term one sentence can explain goes under `inline`. The task gives the most new concepts the reader does not know that this answer may add, and submit rejects more. Give each new concept an id that is not already used.
- New concepts may require existing concepts or each other; the graph must stay acyclic.
- Mark `known: true` if the reader profile already covers the concept, with `requires: []`.
- `evidence` quotes must be copied from the sources character for character, with their source id. A concept that does not appear in the sources may have no quotes.
- A name with mathematics in it needs a `title` with the mathematics in LaTeX and a binding in `symbols` for every symbol in it, as in the extract task.
- Give every term a resolution, or list it under `inline`.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist who has studied discrete mathematics (integers, modular arithmetic, gcd and primes at the basic level, sets, bijections, binomial coefficients), undergraduate linear algebra (vector spaces, matrices, rank, Gaussian elimination, dot products, norms), the single-variable calculus a CS degree requires (limits, convergence of sequences and series, basic integrals, logarithms and exponentials), algorithms and complexity (big-O together with Omega and Theta, recurrences, schoolbook multiplication, worst-case running time of Turing machines), and binary arithmetic with basic complex numbers. This covers the sources' integer, bit, linear-algebra, limit and asymptotic bookkeeping, but not prime-number density results, tensor products, operator norms and contractions, Gaussian integers, or the quotient-ring and Fourier machinery beyond the existing concepts.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `big-o`: Big-O notation (known to the reader): Notation bounding how a function grows asymptotically, up to a constant factor, as its input grows.
- `polynomial`: Polynomials (known to the reader): Expressions sum of constant multiples of powers of a variable, whose coefficients can be listed in order.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + ib with real a and b and imaginary unit i satisfying i² = −1.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with several tapes, each with its own head, that reads and writes at most one cell per tape per step.
- `fixed-tape-model`: Fixed-tape machine model: A multitape Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, the same for every input length.
- `schonhage-strassen-conjecture`: Schonhage-Strassen optimality conjecture: The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers on a multitape Turing machine.
- `power-saving`: Power saving in the logarithmic factor: A bound of the form n times (lg n) raised to the power 1 − κ for a fixed κ > 0, which is smaller than n log n by a polynomial factor in log n.
- `linear-network`: Linear network: A fixed network of wires with gates that apply fixed linear maps to the values on their wires, used here to exchange two banks of values while restoring all auxiliary values.
- `frame`: Frame of a vertex: An invertible linear operator attached to a gate or terminal that sets how the array on each wire there is stored; changing frames along an edge cancels between the two ends of a route.
- `role-streams`: Role streams from a cyclic row split: Splitting the rows of an array cyclically among the W fixed wire roles of a network, so that each role carries an equal share of the volume and gates act pointwise on matching addresses.
- `subset-network`: Subset-intersection finite network: A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2].
- `subspace-labels`: Nested subspace labels: Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge.
- `address-shear`: Address shear: The address permutation that replaces the first of two address fields H by H + D, leaving D fixed, which is the endpoint operator of the bit network on arrays.
- `recursive-saving`: Rank-saving recursion: A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.
- `tape-interchange`: Fast interchange of address chunks: A fixed-tape procedure that swaps two disjoint equal-width address fields of an array in time O(V u^τ) for a fixed τ < 1, where V is the stored volume and u the field width, using XOR combinations of intermediate data.
- `gaussian-dyadic`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are both dyadic rationals, that is, have power-of-two denominators.
- `butterfly-layer`: Simultaneous butterfly layer H₀: The map H₀(u,v) = ((u+v)/2, (u−v)/2) applied at once to a selected coordinate bit of every chunk, a two-point butterfly acting coefficientwise on polynomial records.
- `polynomial-ring`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials of degree less than r, with multiplication reduced modulo y^r + 1; multiplication by a power of y permutes and sign-changes the coefficient list.
- `roots-of-unity`: Root of unity: A number whose some positive integer power equals one; here powers of y in the polynomial ring play this role.
- `synthetic-transform`: Synthetic polynomial transform: A discrete Fourier transform whose roots of unity are powers of y in the polynomial ring, so that each twiddle multiplication is a signed shift and the transform is computed by simultaneous butterfly layers.
- `fourier-transform`: Discrete Fourier transform: The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
- `multidim-transform`: Multidimensional transform with power-of-two axes: A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
- `gaussian-resampling`: Gaussian resampling: A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.
- `bluestein`: Bluestein's chirp identity: An identity writing a Fourier transform as a cyclic convolution sandwiched between pointwise multiplications by chirp sequences exp(−πi s j² / t).
- `crt-axis-map`: Chinese-remainder axis map: The bijection sending a coefficient index written in mixed radix with pairwise coprime lengths to coordinates on a product of cyclic axes, which turns one cyclic convolution into a multidimensional one.
- `radix-digit-convolution`: Radix-digit convolution: Writing each n-bit input as a polynomial in 2^b with about n/b nonnegative digits, so that integer multiplication becomes a convolution whose coefficients are bounded by a fixed power of two.
- `signed-packing`: Signed coefficient packing: Encoding a polynomial with signed integer coefficients as one integer by placing coefficients at fixed bit offsets, so that a polynomial product becomes an integer product.
- `multiplier-subroutine`: Established fast multiplier: The known deterministic O(n log n) multiplication algorithm of Harvey and van der Hoeven, used as a black-box subroutine on shorter integers.
- `exact-recovery`: Exact recovery by rounding and carries: Recovering the exact integer coefficients of a convolution by rounding the computed values, whose error is below one half, and then propagating carries in radix 2^b.
- `fixed-tape-multiplication`: Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Arithmetic on integers in which two integers are identified when a fixed modulus m divides their difference, giving the residue classes Z/mZ, with division with remainder and modular inverses where they exist.
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality (known to the reader): The greatest common divisor of two integers is the largest positive integer dividing both and is computed by the Euclidean algorithm, with two integers coprime when this divisor is one and a family of integers pairwise coprime when every two members are coprime.
- `prime-number`: Prime number (known to the reader): A prime is a positive integer greater than one whose only positive divisors are one and itself, and every integer greater than one factors uniquely into primes.
- `binary-field-and-exclusive-or`: Binary field and exclusive or (known to the reader): The two-element field {0,1} with addition modulo 2, which on bit strings is bitwise exclusive-or, and multiplication equal to bitwise AND.
- `hamming-weight`: Hamming weight (known to the reader): The Hamming weight of a binary vector is its number of coordinates equal to one.
- `two-s-complement-representation`: Two's-complement representation (known to the reader): A signed integer is stored in a fixed number of bits whose leading bit has negative place value, so that negative values are obtained by complementing the bits and adding one.
- `positional-notation-and-binary-representation`: Positional notation and binary representation (known to the reader): An integer is written as a sum of digits times powers of a fixed base b, and in base 2 a binary string of length k represents its value with the leftmost bit most significant, with addition propagating carries.
- `dyadic-rational`: Dyadic rational (known to the reader): A dyadic rational is a rational number whose denominator is a power of two, equivalently a number with a finite binary expansion.
- `floor-and-ceiling-functions`: Floor and ceiling functions (known to the reader): The floor of a real number x, written floor(x), is the greatest integer not exceeding x, and the ceiling, written ceiling(x), is the least integer not less than x.
- `binomial-coefficient`: Binomial coefficient (known to the reader): The binomial coefficient C(n,k) is the number of k-element subsets of an n-element set.
- `finite-sets-subsets-and-intersections`: Finite sets, subsets and intersections (known to the reader): Finite sets with unions, intersections and subsets, where the indicator vector of a subset is the vector with entry one at its elements and zero elsewhere.
- `bijection-and-permutation`: Bijection and permutation (known to the reader): A bijection between two finite sets is a function that is one-to-one and onto, and a permutation of a set is a bijection from the set to itself.
- `cartesian-product`: Cartesian product (known to the reader): The Cartesian product of finite sets is the set of ordered tuples whose i-th entry lies in the i-th set, and it is used to index arrays with several coordinates.
- `lexicographic-order`: Lexicographic order (known to the reader): The lexicographic order on tuples compares entries from the first coordinate onward, so the first coordinate is most significant, and row-major order is the lexicographic order of the row and column indices.
- `logarithm-and-exponential-function`: Logarithm and exponential function (known to the reader): The base-2 logarithm log_2 x, also written lg x, and the natural logarithm ln x are inverse to the powers of 2 and of e, and the exponential function exp(x) = e^x is the inverse of ln.
- `limits`: Limits (known to the reader): The limit of a sequence or of a function is the value its terms or outputs approach as the index or input grows without bound or approaches a given point, written lim.
- `convergence-of-sequences-and-series`: Convergence of sequences and series (known to the reader): A sequence converges to a limit when its terms eventually stay arbitrarily close to it, and an infinite series converges when its sequence of partial sums converges.
- `basic-integrals`: Basic integrals (known to the reader): The definite integral of a continuous function over an interval is the limit of its Riemann sums, and for elementary functions it is computed by finding an antiderivative and applying the fundamental theorem of calculus.
- `geometric-series`: Geometric series (known to the reader): The geometric series a^0 + a^1 + ... + a^k equals (a^(k+1) - 1)/(a - 1) when a is not equal to one.
- `big-omega-big-theta-and-little-o-notation`: Big-Omega, big-Theta and little-o notation (known to the reader): f is Omega(g) when f is at least a constant times g for large inputs, Theta(g) when f is both O(g) and Omega(g), and o(g) when the ratio f/g tends to zero.
- `worst-case-running-time-of-a-turing-machine`: Worst-case running time of a Turing machine (known to the reader): The worst-case running time of a Turing machine on inputs of length n is the maximum, over all inputs of length n, of the number of steps taken before it halts.
- `recurrence-relation`: Recurrence relation (known to the reader): A recurrence relation defines each term of a sequence in terms of earlier terms, such as T(n) = 2T(n/2) + n, and is solved by unrolling it or by substitution.
- `schoolbook-multiplication`: Schoolbook multiplication (known to the reader): Schoolbook multiplication multiplies two n-digit integers by forming all digit products and adding them with carries, using order n squared digit operations.
- `directed-graph`: Directed graph (known to the reader): A directed graph consists of vertices and edges, each edge having a tail vertex and a head vertex, and a network of wires and gates forms such a graph.
- `vector-space-subspace-basis-and-dimension`: Vector space, subspace, basis and dimension (known to the reader): A vector space over a field such as R, C or F_2 is a set closed under addition and scalar multiplication, a subspace is a subset that is itself a vector space, a basis is a linearly independent spanning set, and the dimension is the number of vectors in a basis.
- `linear-map-and-matrix`: Linear map and matrix (known to the reader): A linear map preserves addition and scalar multiplication and is represented by a matrix relative to chosen bases, the matrix being invertible when it has an inverse and its transpose swapping rows and columns.
- `matrix-rank`: Matrix rank (known to the reader): The rank of a matrix is the dimension of its column space, equal to its maximum number of linearly independent columns and to its number of pivots after row reduction.
- `gaussian-elimination-and-triangular-matrices`: Gaussian elimination and triangular matrices (known to the reader): Gaussian elimination reduces a matrix to echelon form by elementary row operations, and a triangular matrix has all entries vanishing on one side of its diagonal.
- `dot-product-and-orthogonal-complement`: Dot product and orthogonal complement (known to the reader): The dot product of two vectors is the sum of products of their corresponding coordinates, and the orthogonal complement of a subspace U is the set of vectors whose dot product with every vector of U is zero.
- `vector-norm-and-maximum-norm`: Vector norm and maximum norm (known to the reader): A norm assigns each vector a nonnegative length satisfying the triangle inequality, and the maximum norm of a vector is the largest absolute value of its coordinates.
- `complex-conjugate-modulus-and-polar-form`: Complex conjugate, modulus and polar form (known to the reader): For a complex number a + ib, its conjugate is a - ib, its modulus is the square root of a^2 + b^2, and Euler's formula writes a number of modulus r and argument theta as r(cos theta + i sin theta) = r e^(i theta).

## Unresolved terms

- "active address fields"
  - on page `role-streams`: "A row is the complete ordered suffix of the active address fields, taken at a fixed prefix and row index."
- "address chunks"
  - on page `linear-network`: "the building block for interchanging address chunks"
- "address field"
  - on page `recursive-saving`: "two equal address fields of width $u$"
- "address fields"
  - on page `subspace-labels`: "two equal address fields of width $u$"
- "algebra map"
  - on page `crt-axis-map`: "the algebra map sending"
- "bit network"
  - on page `tape-interchange`: "on a bit network"
- "bit procedure"
  - on page `address-shear`: "It is the endpoint operator of the bit procedure"
- "Chinese remainder theorem"
  - on page `crt-axis-map`: "the Chinese remainder theorem makes the exponents of $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ pairwise distinct"
- "common address set"
  - on page `frame`: "the space of arrays indexed by the common address set"
- "edge matrix"
  - on page `recursive-saving`: "an edge matrix of rank $a$ costs $a$ smaller calls"
  - on page `tape-interchange`: "Each edge matrix of rank $a$"
- "endpoint operator"
  - on page `tape-interchange`: "its endpoint operator"
- "gather and scatter wires"
  - on page `subspace-labels`: "whose gather and scatter wires create coefficients that depend on intersection size"
- "isomorphism"
  - on page `crt-axis-map`: "Hence $\Phi$ is an isomorphism."
- "linear-cost address update"
  - on page `address-shear`: "one of the linear-cost address updates that interchange two address fields"
- "local address set"
  - on page `role-streams`: "All role streams have the same local address set."
- "network"
  - on page `recursive-saving`: "each edge of a network is paid for by a few smaller calls"
- "Neumann series"
  - on page `gaussian-resampling`: "a Neumann series"
- "node"
  - on page `role-streams`: "the number of bits the node holds once its rows are padded"
- "phase twist"
  - on page `bluestein`: "with a phase twist"
- "pointwise linear gate"
  - on page `frame`: "A pointwise linear gate commutes with its common frame"
- "recursive scheme"
  - on page `subspace-labels`: "This is what lets a recursive scheme pay less per edge when its parameter shrinks"
- "target permutation"
  - on page `bluestein`: "including its target permutation"
- "tensor product"
  - on page `butterfly-layer`: "This is the tensor product of the single-bit butterflies"
  - on page `multidim-transform`: "The whole transform is a tensor product of one"
- "twiddle multiplication"
  - on page `polynomial-ring`: "so each twiddle multiplication is a signed shift of the $r$ coefficients rather than a complex multiplication."
- "twiddle step"
  - on page `roots-of-unity`: "A discrete Fourier transform multiplies by a root of unity at each twiddle step"
- "volume"
  - on page `subspace-labels`: "costs less than linear in $u$ per unit volume"
  - on page `recursive-saving`: "so each role carries an equal share of the volume"
- "wires"
  - on page `tape-interchange`: "over the wires"
- "Z[i,1/2] (Gaussian dyadic numbers)"
  - on page `subset-network`: "In the complex version, scalars lie in $\mathbb Z[i,1/2]$"
- "zero padding"
  - on page `radix-digit-convolution`: "with zero padding"

## New pages

New concepts the reader does not know: at most 13, and submit rejects more. Resolve the other terms to existing or known concepts, or list them under `inline`.

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
    "inline": {
      "default": [],
      "description": "Unresolved terms to explain in a sentence where they are used, instead of on a page.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "resolutions": {
      "description": "For every unresolved term not under `inline`, the id of the concept (existing or\nnew) that covers it.",
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

Write the answer to `exegenius/tasks/0059-extend.answer.json`, then run `exegenius submit 0059-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
