# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/D5` (paths below are relative to it)

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

`main-theorem`: Integer multiplication below n log n: A deterministic fixed multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it chains CRT map, Gaussian resampling, chirps, twist and synthetic transforms accelerated by the fast interchange and butterfly layers.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science background: asymptotic analysis and recurrences, discrete mathematics (modular arithmetic, primes, gcd, permutations, binary representation), introductory linear algebra (matrices, rank, invertibility, vector spaces), and basic algebra with polynomials and complex numbers. They know algorithms such as schoolbook multiplication, divide and conquer and sorting, and basic Turing machines with tapes. They have not studied the FFT or Schönhage–Strassen in depth, rings and finite fields beyond basics, tensor products, or the specialist multitape-complexity and fast-multiplication literature.

## Pages, in reading order

- `multitape-model`: Fixed multitape Turing machine model: The computation model: one fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step reading/writing one cell per tape and moving each head by at most one cell; time is the number of steps.
- `nlogn-conjecture`: Multiplication history and the n log n conjecture: Schönhage–Strassen's O(n log n log log n) multiplier, their conjecture that n log n is optimal, and the Harvey–van der Hoeven O(n log n) algorithm that the paper beats by a power of log n.
- `convolution-dft`: Convolution and the discrete Fourier transform: Cyclic convolution of coefficient lists, and the DFT that turns it into pointwise multiplication; the inverse transform uses the opposite-sign root and a 1/size normalization.
- `radix-digit-convolution`: Multiplication as convolution of radix digits: Splitting each n-bit operand into short radix-2^b digits turns integer multiplication into a convolution of small integer coefficient lists, followed by rounding and carry propagation to get the exact binary product.
- `multidimensional-transform`: Multidimensional transforms with tensor structure: A transform on an array indexed by several axes is the tensor product of one-dimensional transforms along each axis; the paper uses d axes of power-of-two length.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with multiplication reduced by y^r = −1; powers of y act as roots of unity and multiplying by one is a signed shift of the coefficient list.
- `fft-butterfly`: FFT butterflies: A two-point butterfly combines two values u,v into (u+v)/2 and (u-v)/2; an FFT is built from layers of these acting on address bits, one layer per level, so scanning the array at each level costs n log n.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style Fourier transforms over the negacyclic ring in which roots of unity are powers of y, so multiplications by roots are signed shifts and only butterflies and shifts remain; forward transforms keep the same frequency order and the opposite transform consumes it.
- `fixed-point-precision`: Dyadic fixed-point arithmetic and rounding: Complex coefficients stored as fixed-point Gaussian dyadics with p fractional bits; exact intermediate values, a single truncation after contractive layers, and error tracking so the final coefficient error is below 1/2.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of prime-ish length s through a transform of power-of-two-axis length t via contractive Gaussian maps A and B; the paper keeps the source and target coordinate permutations inside the identity instead of sorting.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's chirp identity rewrites a Fourier transform (with its permutation) as a pointwise chirp multiplication around a cyclic convolution, and permutations cancel across the two forward transforms and the inverse.
- `coefficient-twist`: Phase twist from cyclic to negacyclic: Twisting coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution of length r to the ring modulo y^r+1, whose negative wrap restores the cyclic wrap.
- `signed-packing-products`: Signed packing of polynomial products: Kronecker-substitution style packing of ring elements with Gaussian-integer coefficients into long integers, multiplied by the established O(n log n) multiplier used as an ordinary subroutine.
- `stream-scans`: Array order and elementary stream operations: Arrays are stored in lexicographic order with implicit addresses; splitting by digits, moving a digit, and splitting rows among roles are linear-time scans.
- `linear-network-frames`: Linear networks with frames: A fixed network of pointwise linear gates on wires (roles); giving each vertex an invertible frame operator D_v acting on address-indexed arrays lets gates stay pointwise while edges apply D_v D_u^{-1}, leaving an endpoint operator on every role.
- `subset-subspace-networks`: Finite networks from three-element subsets: Two fixed networks (a bit network over Q and a complex Gaussian-dyadic one over F_2) with nested subspace labels built from triples of [h], whose edge rank changes sum to s < Wm; this strict deficit is the source of the power saving.
- `recursive-saving`: Recursive power saving: A call at parameter mf uses s < Wm calls at parameter f on streams of volume V/W, so the per-volume cost grows by a factor s/W < m when the parameter is multiplied by m, giving cost V·e^τ with τ<1.
- `controlled-shifts`: Controlled shifts and rational scalings: Updating a later address field by an offset computed from earlier control fields, or multiplying it by a rational unit mod q^b, in linear time using whole-block splits and merges.
- `lower-triangular-shear`: Lower triangular factorization and matrix shear: Every rational matrix factors as E1·Π·E2 with E1,E2 lower triangular, so a coordinate change on address fields is a sequence of controlled shifts in tape order and costs O(V) times a rank-dependent number of smaller operations.
- `address-interchange`: Fast address-field interchange: Interchange of two disjoint contiguous address fields of u digits in time O(V u^τ) with a fixed τ<1, via XOR combinations of intermediate streams that finally give an exact permutation for arbitrary auxiliary values.
- `simultaneous-butterfly-layer`: Fast simultaneous butterfly layer: Applying the H_0 butterfly on the same bit position of d address chunks at once, using phase frames, binary changes of basis by chunk moves and the recursive saving, in time O(V d^λ') instead of d whole-array passes.
- `transform-layout-cost`: Synthetic transform layout and convolution cost: Arranging the array so the simultaneous layers apply with frequency order retained, giving a convolution over the ring from two forward transforms, a pointwise product (via signed packing) and an opposite transform at cost O(Tp[dK+pK^{τ-1}+ℓd^{λ'}+log(rp)]).
- `resampling-no-sort`: Resampling without executing the permutations: Lemma stating P_sF_s = 2^{2α²} B_0 P_tF_t A with coordinate permutations kept in the identity and tensored over d axes, so no full sorts are needed.
- `crt-address-map`: Chinese-remainder coefficient address map: Map Φ placing the radix-digit coefficient list on a product of pairwise-coprime cyclic axes by the Chinese remainder theorem so that convolution is preserved, implemented by triangular controlled shifts.
- `parameter-choice-cost`: Parameter choice and total cost accounting: Choosing b=⌈log n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log T/d⌉} and fixed rational exponents with κ=2^{-182}, then summing the normalized cost table, every row of which is a power of p below 1.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it chains CRT map, Gaussian resampling, chirps, twist and synthetic transforms accelerated by the fast interchange and butterfly layers.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `basic-turing-machines`: Turing machines and tapes
- `schoolbook-multiplication-and-divide-and-conquer`: Schoolbook multiplication and divide and conquer
- `recurrences-and-geometric-sums`: Recurrences and geometric sums
- `logarithms-floors-and-ceilings`: Logarithms, floors and ceilings
- `binary-representation-and-bitwise-operations`: Binary representation and bitwise operations
- `modular-arithmetic`: Modular arithmetic
- `divisibility-primes-and-coprimality`: Divisibility, primes and coprimality
- `permutations-and-sorting`: Permutations and sorting
- `linear-algebra-over-a-field`: Linear algebra over a field
- `triangular-matrices-and-elementary-operations`: Triangular matrices and elementary operations
- `the-field-with-two-elements`: The field with two elements
- `rational-numbers-and-dyadic-fractions`: Rational numbers and dyadic fractions
- `rounding-and-approximation-error`: Rounding and approximation error
- `cyclic-groups-and-powers-of-a-generator`: Cyclic groups and powers of a generator
- `array-indexing-by-tuples-and-mixed-radix`: Array indexing by tuples and mixed radix
- `sums-products-and-indicator-notation`: Sums, products and indicator notation
- `basic-complexity-of-tape-computation`: Basic complexity of tape computation
- `euclidean-norm-and-inequalities`: Euclidean norm and inequalities
- `gaussian-integers`: Gaussian integers

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

Keep any other files you make, such as scripts, in `exegenius/tasks/0003-argument`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
