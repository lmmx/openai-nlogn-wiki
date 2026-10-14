# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/K1` (paths below are relative to it)

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

`sub-linearithmic-integer-multiplication`: Sub-linearithmic integer multiplication on a fixed tape machine: A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, with κ = 2^−182, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has the standard undergraduate computer science core: discrete mathematics (Cartesian products, permutations, induction, binomial coefficients, graphs, modular arithmetic, gcd, primes and division with remainder), linear algebra over the real and rational numbers (vector spaces, bases, matrices, eigenvalues, dot products, Gaussian elimination), calculus-level analysis (logarithms, exponentials, limits, geometric sums, roots of unity and Euler's formula), and algorithms and computer organization (Omega, Theta and little-o notation, recurrences, positional notation, two's-complement words). Not assumed are fields other than F_2, tensor products, bilinear forms, Gaussian integers, rings and groups, the integer Chinese remainder theorem, limit inferior and Newton iteration.

## Pages, in reading order

- `integer-multiplication-problem`: Exact integer multiplication: The task of reading two n-bit binary strings x and y after a separator # and writing the 2n-bit binary representation of their product exactly, for every n.
- `polynomial-ring-mod`: Polynomial ring modulo y^r + 1: The ring of complex polynomials in y reduced modulo y^r + 1, so that y^r equals −1 and products that overflow degree r wrap around with a sign.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are dyadic rationals with power-of-two denominators, so that they are stored exactly in binary.
- `harvey-hoeven-multiplier`: Harvey–van der Hoeven multiplier: The known unconditional O(n log n) bit-complexity algorithm for multiplying integers, which the construction calls as an ordinary subroutine.
- `signed-kronecker-packing`: Signed Kronecker packing: Encoding a polynomial with signed integer coefficients as a single integer by placing the coefficients at fixed bit spacing, so that one integer product computes the polynomial product.
- `fixed-tape-model`: Fixed-tape machine model: A Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, where each step moves every head by at most one cell.
- `sch-conjecture`: Schönhage–Strassen optimality conjecture: The proposal that n log n is the optimal order of growth for multiplying integers, which the target result refutes in the fixed-tape model.
- `stream-scans`: Linear-time tape stream operations: Scans that permute, split, merge, or shift the entries of an array with V stored data bits in O(V) steps, where addresses are implicit in the position of each entry.
- `linear-subspaces`: Subspaces, rank and orthogonal complement: Subspaces of a vector space over a field, their dimensions, the rank of a linear map, and the orthogonal complement of a subspace with respect to a bilinear form.
- `bank-exchange-network`: Bank-exchange network: A fixed linear network of wires with pointwise gates and scratch wires that exchanges two banks of values with prescribed signs and restores every scratch value.
- `frames`: Frame change for linear gates: An invertible operator D_v attached to each gate, source and sink, so that a wire's stored array is D_v applied to its logical array and a pointwise linear gate commutes with a common frame.
- `address-shear`: Address shear: The update that replaces an address field H by H + D, with D another field, and which is the endpoint operator the bit network applies to every role.
- `three-element-subsets`: Three-element subset construction: The set of three-element subsets of a fixed ground set together with the intersection-size relation that decides which triples are joined by a wire.
- `complex-phase-network`: Complex phase network: The fixed linear network over Gaussian dyadic values and binary subspaces that exchanges complex coefficients while restoring every scratch value.
- `scratch-restoring-exchange`: Scratch-restoring exchange: A three-stage gate schedule built from copy, gather, side-injection and scatter gates that adds one bank into another and exchanges two banks with a sign, leaving any initial scratch values unchanged.
- `rank-saving-recursion`: Rank-saving recursion: The fact that the total rank s of the edge changes is less than W times m, so that multiplying the recursion parameter by m multiplies the recursive cost by s/W < m, a strict power saving.
- `bruhat-factorization`: Bruhat factorization for shears: The factorization of a singular matrix into lower-triangular factors after reversing the coordinate order, so that a shear becomes a sequence of updates of later fields from earlier ones.
- `fast-address-interchange`: Fast address-chunk interchange: A tape procedure that swaps two disjoint equal-width address chunks of u bits in a stored array of volume V in O(V u^τ) time for a fixed τ < 1, by recursive calls to the bit network.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient arrays indexed by Z/tZ in which indices wrap around modulo the length t.
- `radix-digit-convolution`: Radix-digit convolution: The reduction of an integer product to the cyclic convolution of its base-2^b digit sequences, whose coefficients are short integers before carries are propagated.
- `approximate-contraction`: Approximate contraction: A map between arrays whose norm in the maximum-coefficient norm is at most one, computed with a stated error bound so that the errors of composed approximate steps add.
- `truncation`: Truncation to a fixed-point grid: Rounding each real and imaginary coefficient part toward zero onto a grid of spacing 2^−p, which does not increase the maximum-coefficient norm.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The operation that applies the two-point butterfly H_0(u, v) = ((u + v)/2, (u − v)/2) to D selected address bits at once on arrays of complex polynomial records, at cost O(V d^λ′) with λ′ < 1.
- `fourier-transform`: Normalized discrete Fourier transform: The map on length-q vectors whose k-th output is (1/q) times the sum over j of u_j e^(−2πijk/q), which is a contraction in the maximum-modulus norm.
- `synthetic-polynomial-transform`: Synthetic polynomial transform: A transform over the polynomial ring in which the roots of unity are powers of y, so that multiplying by a root is a signed shift of a coefficient list, computed with radix-two butterflies.
- `bluestein-chirp`: Bluestein's chirp identity: The identity that writes a transform with quadratic phase factors (chirps) as a pointwise multiplication by a chirp, a cyclic convolution, and a second pointwise multiplication by the conjugate chirp.
- `phase-twist`: Phase twist to negacyclic wrap: A phase multiplication of the last cyclic coordinate that turns the cyclic wrap-around into the negative wrap of the polynomial ring, so that the original cyclic product is recovered once the twist is removed.
- `normalized-ring-convolution`: Normalized convolution over the polynomial ring: The bilinear map sending arrays f and g of ring elements to (f * g)/T, computed from the retained transform layout and bounded in the maximum-coefficient norm.
- `chinese-remainder-axes`: Chinese remainder axis layout: The algebra isomorphism that places a cyclic convolution of pairwise coprime length S on a product of cyclic axes, so that the change of coefficient order is a sequence of controlled shifts.
- `gaussian-resampling`: Gaussian resampling: The identity that expresses a Fourier transform of a length that is not a power of two through a tensor transform with power-of-two axis lengths, using Gaussian-weighted resampling.
- `sort-free-resampling`: Sort-free Gaussian resampling: Gaussian resampling in which the source and target coordinate permutations remain inside the transform formula, so they are never executed as separate full sorts.
- `permutation-cancellation`: Permutation cancellation: The identity that the retained source permutation cancels across the two forward transforms, their pointwise product and the inverse transform, leaving a plain cyclic convolution.
- `rounding-carry-recovery`: Rounding and carry recovery: The step that removes the known normalizations and digit scales, rounds each recovered coefficient (with error below 1/2), and propagates carries to obtain the exact binary product.
- `multiplication-pipeline`: Transform pipeline for integer product: The sequence of reductions (digit packing, Chinese remainder layout, sort-free Gaussian resampling, chirps, phase twist, normalized ring convolution, cancellation and carry recovery) that computes the exact product of two integers.
- `parameter-choice-cost`: Parameter choice and cost accounting: The fixing of rational exponents, including τ = σ = 1 − 2^−50 and κ = 2^−182, so that every term of the cost table is within the bound O(n(lg n)^(1−κ)) after division by the stored volume V.
- `sub-linearithmic-integer-multiplication`: Sub-linearithmic integer multiplication on a fixed tape machine: A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, with κ = 2^−182, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Turing machines and tapes
- `logarithms-and-exponentials`: Logarithms and exponentials
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `geometric-series`: Geometric series
- `mathematical-induction`: Mathematical induction
- `recurrence-relations-for-running-times`: Recurrence relations for running times
- `cartesian-product-of-sets`: Cartesian product of sets
- `permutation-of-a-finite-set`: Permutation of a finite set
- `binomial-coefficients`: Binomial coefficients
- `lexicographic-order`: Lexicographic order
- `graphs-vertices-and-edges`: Graphs, vertices and edges
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `greatest-common-divisor-and-coprime-integers`: Greatest common divisor and coprime integers
- `prime-numbers`: Prime numbers
- `division-with-remainder`: Division with remainder
- `limits-of-sequences-and-functions`: Limits of sequences and functions
- `nth-roots-of-unity-and-polar-form`: Nth roots of unity and polar form
- `vector-spaces-bases-and-linear-maps`: Vector spaces, bases and linear maps
- `matrices-inverses-and-triangular-matrices`: Matrices, inverses and triangular matrices
- `eigenvalues-and-eigenvectors`: Eigenvalues and eigenvectors
- `gaussian-elimination-and-elementary-row-operations`: Gaussian elimination and elementary row operations
- `dot-product-and-orthogonality`: Dot product and orthogonality
- `indicator-vector-of-a-subset`: Indicator vector of a subset
- `arithmetic-modulo-2-and-xor`: Arithmetic modulo 2 and XOR
- `dyadic-rational-numbers`: Dyadic rational numbers
- `positional-radix-notation`: Positional (radix) notation
- `two-s-complement-integers`: Two's-complement integers

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

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

Write the answer to `exegenius/tasks/0003-argument.answer.json`, then run `exegenius submit 0003-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0003-argument`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
