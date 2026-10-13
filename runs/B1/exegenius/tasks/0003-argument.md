# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/B1` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1−κ)), κ=2^−182: digit convolution, CRT prime axes, Gaussian resampling and chirps, synthetic transforms over the y^r+1 ring, accelerated by fast address interchange and butterfly layers.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has done an undergraduate computer science degree: asymptotic analysis and recurrences, basic algorithms (including schoolbook and Karatsuba multiplication and the idea of the FFT), discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, permutations, bit operations), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know complex numbers, polynomials and basic Turing machines with tapes. They have not studied abstract algebra beyond rings as a name, tensor products, Nussbaumer or Schönhage–Strassen transforms, or any research-level multiplication algorithm.

## Pages, in reading order

- `convolution-reduction`: Multiplication as convolution of digit lists: Splitting inputs into radix digits turns integer multiplication into convolution of short integer coefficient lists, with carries propagated afterwards.
- `polyring-mod`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced modulo y^r+1, so y^r=-1; coefficients stored as a list, with r a power of two.
- `chinese-remainder-map`: Chinese-remainder address map onto prime axes: Places the digit coefficient list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- `multitape-model`: Fixed multitape Turing machine model: Deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes; cost is the number of steps.
- `nlogn-conjecture`: Schönhage–Strassen n log n optimality conjecture: Schönhage and Strassen proposed n log n as optimal growth for multiplying n-bit integers on multitape machines; Harvey–van der Hoeven reached O(n log n).
- `controlled-shifts`: Elementary scans and controlled shifts: Linear-time tape operations: digit moves, splitting rows cyclically into streams, and updating a target field by an offset computed from earlier control fields.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network of gates exchanging banks of values with signs, restoring auxiliary values; each wire is a role and each gate has an invertible frame so intermediate frames cancel.
- `subset-network`: Three-element-subset finite networks: Finite networks built from three-element subsets with nested subspaces at gates; gather/scatter and auxiliary wires cancel unwanted coefficients, giving s<Wm smaller calls.
- `recursive-saving`: Recursive power saving: Recursing at parameter mf with s calls of parameter f on volume V/W adds s/W<m per level, a strict inequality that gives a power saving.
- `scalar-motif-network`: Scratch-restoring exchange network: Eight-row schedule of copy, gather, scatter and side-injection gates adding x_S to y_S for arbitrary initial scratch values; three stages give the exchange (X,Y) → (−Y,X).
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with a ones, so it can be applied in tape order.
- `matrix-shear`: Rational matrix shear of address fields: The frame Φ_M moving the entry at address (H,D) to (H+MD,D); a shear of rank a costs a smaller interchanges.
- `address-interchange`: Fast address-field interchange: Interchanges two disjoint address fields of u bits via pointwise XOR combinations that end as an exact permutation, in O(V u^τ) with τ<1.
- `signed-packing`: Signed packing (Kronecker substitution): Encodes polynomial coefficients, with signs, into one long integer so ring products are computed by one integer multiplication.
- `hvdh-subroutine`: Established O(n log n) multiplier as subroutine: The Harvey–van der Hoeven O(n log n) multiplication used as an ordinary subroutine for polynomial products, not recursively invoking the new theorem.
- `fourier-transform`: Discrete Fourier transform: Evaluation of a sequence at powers of a root of unity; it turns cyclic convolution into pointwise product.
- `multidim-transform`: Multidimensional transform: A Fourier transform on an array with several axes, applied along each axis in turn; here axis lengths are powers of two.
- `synthetic-transform`: Synthetic polynomial transform: Fourier transform over the polynomial ring where powers of y act as roots of unity, so multiplying by a root is a signed shift of the coefficient list (Nussbaumer).
- `butterfly`: Two-point butterfly H₀: The map (u,v) → ((u+v)/2, (u−v)/2), the basic arithmetic step of a transform layer, applied coefficientwise.
- `phase-frames`: Phase frames for the butterfly layer: Using C=HSH=aI+bX with C²=X and H₀=bSCS, a tensor product of butterflies is expressed through smaller groups of selected bits separated by binary changes of basis.
- `fast-butterfly-layer`: Simultaneous butterfly layers: Applies H₀ at the same bit position of up to d address chunks at once on complex fixed-point records, in O(V d^λ′) with λ′<1.
- `exact-recovery`: Fixed-point precision and exact recovery: Intermediate values are exact Gaussian dyadics truncated once; the recovered coefficient error is below 1/2 so rounding and carry propagation give the exact product.
- `synthetic-character-cancellation`: Synthetic character cancellation: In the ring modulo y^r+1, sums of powers of the root ω_t vanish unless t divides the exponent, so forward and opposite transforms invert each other up to 1/t.
- `transform-layout`: Retained frequency order and transform layout: Selected bits of the participating axes are placed at a common offset in K-bit chunks so the simultaneous layers apply, and the frequency order is retained through the pointwise product.
- `normalized-convolution`: Normalized convolution over the ring: Convolution over the polynomial ring computed as two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform, normalized by 1/(rM).
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing each prime-length Fourier transform through a power-of-two tensor transform, with source and target permutations.
- `resampling-lemma`: Resampling without executing permutations: Gaussian resampling identity P_sF_s = 2^{2α²}B₀P_tF_tA relating a length-s transform to a power-of-two-shape transform, with the two coordinate permutations kept inside the formula.
- `tensor-resampling`: Tensor interface for growing dimension: Applies the one-dimensional resampling maps line by line along d axes, using chunk swaps to move axes, giving R F_s = 2^γ B₀ Q F_t A.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform (with its permutation) into a normalized cyclic convolution via multiplication by chirp phases.
- `chirp-permutation-cancellation`: Chirp and permutation cancellation: Chirp identity Q F_t u = ā·(a*(ā·u))/T computes the permuted middle transform as a convolution, and the source permutation R cancels across forward transforms, product and opposite transform.
- `parameter-choice`: Fixed rational parameter choice: The fixed exponents (τ=σ=1−2⁻⁵⁰, λ′=1−2⁻⁵⁴, ε=2⁻⁷⁵, κ=2⁻¹⁸²) and size parameters p=6b, d=⌊b^ε⌋ making all costs fit the theorem.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1−κ)), κ=2^−182: digit convolution, CRT prime axes, Gaussian resampling and chirps, synthetic transforms over the y^r+1 ring, accelerated by fast address interchange and butterfly layers.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-tapes`: Turing machines and tapes
- `logarithms-and-iterated-logarithms`: Logarithms and iterated logarithms
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `fast-fourier-transform-algorithm`: Fast Fourier transform algorithm
- `convolution`: Convolution
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `primes-and-coprimality`: Primes and coprimality
- `chinese-remainder-theorem`: Chinese remainder theorem
- `matrices-rank-and-invertibility`: Matrices, rank and invertibility
- `vector-spaces-and-subspaces`: Vector spaces and subspaces
- `permutations`: Permutations
- `floor-ceiling-and-rounding`: Floor, ceiling and rounding
- `recursion-and-recurrence-relations`: Recursion and recurrence relations
- `fixed-point-and-dyadic-arithmetic`: Fixed-point and dyadic arithmetic
- `complex-conjugate-and-modulus`: Complex conjugate and modulus
- `cartesian-products-and-multi-indexing`: Cartesian products and multi-indexing
- `linear-time-scans-and-tape-sorting`: Linear-time scans and tape sorting
- `deterministic-computation-and-time-complexity-classes`: Deterministic computation and time complexity classes
- `geometric-and-power-of-two-parameter-manipulation`: Geometric and power-of-two parameter manipulation

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
