# exegenius task 0015-extend

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

For these sources: The reader has an undergraduate computer science education at introductory depth: discrete mathematics (integers, divisibility, modular arithmetic, gcd and primes, binomial coefficients, induction, the field of two elements with XOR), algorithms (the big-O family, divide-and-conquer recurrences, the RAM and multitape Turing models), calculus (limits, convergence of sequences and series, geometric series, basic integrals), elementary linear algebra over the reals and F_2 (vector spaces, linear maps, rank, dot products, matrix products), and complex numbers with modulus and polar form. The reader has not reached specialist algebra, tensor products, bilinear forms, eigen-theory beyond the basics, analysis (liminf and limsup), or numerical analysis, so the main theorem's proof and its network and transform machinery must be explained.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `big-o-notation`: Big-O notation (known to the reader): A way of stating that a function grows no faster than a constant multiple of another function, beyond some input size.
- `complex-numbers`: Complex numbers (known to the reader): Numbers of the form a + bi with real a and b and imaginary unit i, with the usual addition and multiplication.
- `polynomials`: Polynomials (known to the reader): Finite sums of constant multiples of powers of a variable, with coefficients drawn from a number system.
- `turing-machine`: Multitape Turing machine (known to the reader): An abstract machine with a finite control and a fixed number of tapes, each with its own head that reads and writes one cell per step.
- `linear-algebra`: Linear algebra over a field: The theory of vector spaces, linear maps, invertible operators, subspaces, and the rank of a linear map.
- `conjecture-n-log-n`: Schönhage–Strassen optimality conjecture: The conjecture of Schönhage and Strassen that n log n is the optimal order of growth of the cost of multiplying two n-bit integers on a multitape Turing machine.
- `integer-multiplication-problem`: Exact integer multiplication: The task of computing the exact 2n-bit binary representation of the product of two n-bit binary integers given as input.
- `fixed-tape-machine`: Fixed-tape machine model: A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, where a step moves each head by at most one cell.
- `fast-multiplier`: Established fast multiplier: The known deterministic multitape algorithm that multiplies two n-bit integers in O(n log n) time, used here as a black-box subroutine.
- `radix-convolution`: Multiplication as digit convolution: The reduction of integer multiplication to the convolution of the coefficient lists of the integers written in a fixed radix.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient sequences in which indices wrap around modulo a fixed length.
- `roots-of-unity`: Roots of unity: Complex numbers z with z^m = 1 for some positive integer m, whose powers cycle through a finite set.
- `dft`: Discrete Fourier transform: The linear map that sends a sequence of n complex numbers to its values at the n-th roots of unity, weighted by powers of a root of unity.
- `gaussian-dyadic`: Gaussian dyadic number: A complex number whose real and imaginary parts are both dyadic rationals, meaning fractions with power-of-two denominators.
- `butterfly`: Two-point butterfly: The map (u, v) to ((u+v)/2, (u-v)/2) applied to a pair of values, the basic step of a radix-two Fourier transform.
- `multidim-transform`: Multidimensional power-of-two transform: A Fourier-type transform over an array whose axis lengths are all powers of two, which replaces a one-dimensional transform of other lengths.
- `gaussian-resampling`: Gaussian resampling: The identity of Harvey and van der Hoeven that rewrites a Fourier transform of one length as a transform over power-of-two axes, with Gaussian weights.
- `negacyclic-ring`: Negacyclic polynomial ring: The ring of polynomials with complex coefficients reduced modulo y^r + 1, where y^r is identified with -1.
- `synthetic-transform`: Synthetic polynomial transform: A transform whose roots of unity are powers of a polynomial variable, so that multiplying by a root is a signed cyclic shift of a coefficient list.
- `chirp`: Bluestein chirp identity: Bluestein's identity that turns a Fourier transform into a convolution by multiplying with chirp factors before and after.
- `phase-twist`: Last-coordinate phase twist: A multiplication of the last cyclic coordinate by a root-of-unity phase, which turns the cyclic wrap into the negacyclic wrap of the polynomial ring.
- `signed-packing`: Signed coefficient packing: The encoding of a polynomial with signed coefficients as a single integer by evaluating it at a large power of two, so that polynomial products become integer products.
- `crt-map`: Chinese-remainder address map: The map that places a coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
- `linear-network`: Linear network that restores auxiliary values: A fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state.
- `frame`: Frame of a network vertex: An invertible linear operator attached to a vertex of a linear network that changes how the array stored on each wire is represented.
- `scratch-restoration`: Scratch-register restoration: The technique of subtracting an initial register value, computing, adding the result, and reversing the computation so that scratch registers return to their arbitrary starting contents.
- `subset-network`: Subset-intersection network: A linear network whose subspace labels come from intersection sizes of three-element subsets, so that the total number of smaller calls is less than the number of wires times the dimension.
- `address-interchange`: Fast address interchange: A tape procedure that swaps two equal-width address fields in an array by computing XOR combinations of intermediate data, at cost proportional to the volume times a power of the field width.
- `rank-saving`: Rank-saving recursion: The recursive construction in which the number of smaller calls is less than the wire count times the parameter, which gives a strict power saving in each level of the recursion.
- `cost-recurrence`: Volume-normalized cost recurrence: The recurrence obtained by dividing a procedure's cost by its stored volume, which shows that the recursive contribution shrinks by a fixed factor at each level.
- `butterfly-layer`: Simultaneous butterfly layer: A single tape procedure that applies the two-point butterfly to the same selected bit position in several equal-width address chunks at once, at cost sublinear in the number of chunks.
- `exact-recovery`: Exact recovery by rounding: The step that rounds the approximate convolution coefficients to integers, after the known normalizations are removed, and shows that each error is below one half.
- `main-theorem`: Deterministic fixed-tape sub-quasilinear multiplication: A deterministic fixed-tape multitape Turing machine that multiplies two n-bit integers exactly in O(n (lg n)^(1-kappa)) time with kappa = 2^(-182), which disproves the n log n optimality conjecture in this model.
- `logarithms-and-exponentials`: Logarithms and exponentials (known to the reader): The logarithm log_b x is the exponent to which the base b must be raised to give x, and exp is its inverse, so that log(xy) = log x + log y and b^(log_b x) = x.
- `floor-and-ceiling-functions`: Floor and ceiling functions (known to the reader): The floor of x is the largest integer not exceeding x, and the ceiling of x is the smallest integer not less than x.
- `positional-radix-representation`: Positional (radix) representation (known to the reader): A nonnegative integer written in base b is a finite string of digits, each between 0 and b-1, whose value is the sum of each digit times the corresponding power of b.
- `field-of-two-elements`: Field of two elements (known to the reader): The field F_2 has the two elements 0 and 1, with addition given by XOR and multiplication given by AND.
- `bitwise-xor`: Bitwise XOR (known to the reader): XOR of two bits is 1 exactly when the bits differ, and bitwise XOR of two equal-length bit strings applies this to each position.
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences (known to the reader): Two integers are congruent modulo m when they differ by a multiple of m, and addition and multiplication of residue classes modulo m are well defined by working with representatives.
- `greatest-common-divisor-and-the-euclidean-algorithm`: Greatest common divisor and the Euclidean algorithm (known to the reader): The gcd of two integers is the largest integer dividing both, two integers are coprime when their gcd is 1, and the Euclidean algorithm computes the gcd by repeated division with remainder.
- `prime-numbers`: Prime numbers (known to the reader): A prime is an integer greater than 1 whose only positive divisors are 1 and itself, and every integer greater than 1 factors uniquely into primes.
- `binomial-coefficients-and-counting-subsets`: Binomial coefficients and counting subsets (known to the reader): The binomial coefficient binom(n,k) counts the k-element subsets of an n-element set and equals n!/(k!(n-k)!).
- `mathematical-induction`: Mathematical induction (known to the reader): Induction proves a statement for all natural numbers by proving a base case and showing that the statement for n+1 follows from the statement for n, or from all smaller values in strong induction.
- `divide-and-conquer-recurrence`: Divide-and-conquer recurrence (known to the reader): A divide-and-conquer recurrence expresses the cost on an input of size n in terms of the costs on smaller subproblems plus the cost of combining them, and its solution is found by unrolling the recursion.
- `random-access-machine-model`: Random-access machine model (known to the reader): The random-access machine has a finite program and memory cells addressed by integers, so that any cell can be read or written in one step.
- `limits-and-convergence-of-sequences`: Limits and convergence of sequences (known to the reader): A sequence converges to L when its terms eventually stay arbitrarily close to L, and the limit of a ratio is the ratio of the limits when both converge.
- `convergence-of-series`: Convergence of series (known to the reader): An infinite series converges when its sequence of partial sums converges, and its sum is the limit of those partial sums.
- `geometric-series`: Geometric series (known to the reader): A geometric series is a sum of the form a + ar + ar^2 + ... + ar^k, which equals a(1 - r^(k+1))/(1 - r) for r not equal to 1 and is bounded by a/(1 - r) when |r| < 1.
- `big-omega-big-theta-and-little-o-notation`: Big-Omega, big-Theta and little-o notation (known to the reader): Omega(f) bounds a function below by a constant multiple of f for large inputs, Theta(f) bounds it both above and below, and o(f) means the ratio to f tends to zero.
- `dot-product-and-orthogonal-vectors`: Dot product and orthogonal vectors (known to the reader): The dot product of two vectors of the same length is the sum of the products of their corresponding entries, and two vectors are orthogonal when this sum is zero.
- `matrix-product-transpose-and-special-matrices`: Matrix product, transpose, and special matrices (known to the reader): The product of an m-by-k and a k-by-n matrix is the m-by-n matrix of dot products of rows and columns, the transpose swaps rows and columns, and a diagonal, triangular, or permutation matrix has the stated zero pattern.
- `complex-modulus-conjugate-and-polar-form`: Complex modulus, conjugate and polar form (known to the reader): The modulus |a+bi| of a complex number is sqrt(a^2+b^2), its conjugate is a-bi, and every nonzero complex number can be written as r e^(i theta) with r > 0 and a real angle theta.
- `fixed-point-arithmetic`: Fixed-point arithmetic (known to the reader): A fixed-point number is an integer scaled by a fixed power of two, so that arithmetic on such numbers is integer arithmetic with a fixed binary point.

## Unresolved terms

- "bit construction"
  - on page `subset-network`: "the bit construction has indicator vectors"
- "common address set"
  - on page `frame`: "the space of arrays indexed by the common address set"
- "indicator vector"
  - on page `subset-network`: "indicator vectors"
- "input role and output role"
  - on page `frame`: "On a route from an input role $w$ to the output role $\rho(w)$ assigned to it"
- "network"
  - on page `linear-algebra`: "The network uses invertible linear operators to change how each array is stored from one gate to the next"
- "pointwise linear gate"
  - on page `frame`: "Pointwise linear gates are what make the frames cancel."
- "scan"
  - on page `fixed-tape-machine`: "Moving one digit in a fixed radix takes a bounded number of scans"
- "tracks"
  - on page `fixed-tape-machine`: "Fixed tracks and finitely many work tapes are harmless for this count."

## New pages

New concepts the reader does not know: at most 2, and submit rejects more. Resolve the other terms to existing or known concepts, or list them under `inline`.

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

Write the answer to `exegenius/tasks/0015-extend.answer.json`, then run `exegenius submit 0015-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
