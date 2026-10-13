# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/C3` (paths below are relative to it)

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

`main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine multiplies two n-bit integers in O(n(lg n)^{1-κ}) time with κ = 2^{-182}, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science degree: algorithm analysis with big-O and recurrences, discrete mathematics (sets, modular arithmetic, primes, induction, permutations), and the linear algebra and complex numbers of the first years (matrices, rank, invertibility, subspaces, norms). They know basic Turing machines with tapes and binary and two's-complement number representation. They have not studied Fourier transforms over rings, FFT-based multiplication, algebraic complexity, or the history of fast multiplication, and have not seen finite-field linear algebra beyond XOR as a bitwise operation.

## Pages, in reading order

- `convolution`: Convolution: The product of two coefficient lists as polynomials, cyclic when indices wrap around; integer multiplication is convolution of digits followed by carries.
- `tape-streams`: Fixed-tape machine model and tape streams: A machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, where arrays are stored in address order and processed by sequential scans, so moving data costs time.
- `nlogn-conjecture`: The n log n conjecture and history of multiplication: Schönhage and Strassen proposed n log n as the optimal order for multiplying n-bit integers; the history runs from Karatsuba and Toom through Schönhage–Strassen and Fürer to Harvey–van der Hoeven's O(n log n).
- `address-fields`: Array addresses, fields and chunks: Arrays on tape are indexed by lexicographic address fields; chunks are contiguous groups of address digits, and rearranging them costs a pass over the data.
- `fixed-point-dyadics`: Fixed-point complex values and Gaussian dyadics: Complex numbers stored as pairs of two's-complement integers over a power-of-two denominator 2^p, truncated toward zero, with contractive (norm ≤ 1) linear maps and error accumulation.
- `linear-network`: Linear exchange network with roles and frames: A fixed network of linear gates on wires (roles) that exchanges two banks of values while restoring auxiliary values; with a common invertible frame at each gate, arrays flow through pointwise and only endpoint frame operators remain.
- `subset-network`: Three-element-subset network with rank saving: A finite construction using three-element subsets, gather/scatter and auxiliary wires, with nested subspaces attached to gates so the total number s of smaller calls is below W·m.
- `recursive-power-saving`: Recursive power saving from s < Wm: A recursive call at parameter mf uses s calls on streams of volume V/W, so the cost per volume grows by s/W < m per factor m in the parameter, giving a power saving.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier as subroutine: The established O(N log N) integer multiplier, used as an ordinary subroutine for short integer products rather than recursively.
- `shear-factorization`: Lower triangular factorization of address shears: Bruhat-type factorization into lower triangular matrices, letting a rational matrix shear (H,D)→(H+D,D) on address fields be done with linear-time scans and rank-many smaller interchanges.
- `fast-interchange`: Fast interchange of address chunks: Interchanges two equal address chunks of u digits in time O(V u^τ) for a fixed τ < 1 via XOR-like linear combinations, ending in an exact permutation.
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution, implemented by controlled shifts and axis moves.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree less than r with y^r = -1, so multiplying by a power of y is a signed cyclic shift of the coefficient list; powers of y act as roots of unity.
- `signed-packing`: Signed packing (Kronecker substitution): Polynomial products over the ring are done by packing coefficients into signed integers and calling the integer multiplier, then unpacking.
- `dft`: Discrete Fourier transform: Evaluation of a coefficient list at powers of a root of unity, in normalized form (1/q)Σ u_j ω^{jk}; it turns convolution into pointwise product, and the opposite-sign transform inverts it.
- `gaussian-resampling`: Gaussian resampling: Expresses a Fourier transform of coprime length as a power-of-two-length tensor transform with permutations, via Gaussian weights, with contraction and error bounds.
- `bluestein`: Bluestein's chirp identity: Rewrites a Fourier transform as a convolution using chirp factors.
- `phase-twist`: Phase twist to the negacyclic last coordinate: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1; its negative wrap yields the original cyclic wrap once the twist is removed.
- `synthetic-transform`: Synthetic polynomial transform: The Fourier transform over the polynomial ring using ω_t = y^{2r/t}, whose root multiplications are signed shifts and whose layers consist of two-point butterflies.
- `butterfly`: Two-point butterfly H₀: The map H_0(u,v) = ((u+v)/2, (u-v)/2) on a pair of values, the basic step of radix-two transforms.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applies H₀ on the same bit position in each of d address chunks of arrays of complex polynomial records in time O(V d^λ') with λ' < 1, evaluated exactly with one final truncation.
- `transform-layout`: Synthetic transform on a retained-order layout: Transforms on several axes are computed by simultaneous butterfly layers on a tape layout, with the frequency order kept through the pointwise product so the opposite transform consumes it.
- `ring-convolution`: Normalized convolution over the polynomial ring: Convolution on power-of-two axes over the polynomial ring via forward synthetic transforms, pointwise ring products and an opposite transform.
- `retained-permutations`: Resampling with permutations left in the transform: The source and target coordinate permutations of resampling are kept inside the transform identity and cancel across the two forward transforms, product and inverse, so no separate sorts are run.
- `radix-digit-reduction`: Reduction of integer multiplication to digit convolution: Split each operand into radix-2^b digits, take the convolution of the digit lists with scaled fixed-point values, round the coefficients and propagate carries.
- `precision-recovery`: Precision and exact recovery: Parameters are chosen so accumulated error in the recovered coefficients is below 1/2, so rounding returns the exact integer convolution, and carries yield the product.
- `multiplication-algorithm`: The multiplication algorithm and its cost: Digits are mapped by the CRT address map, transformed by two source transforms, multiplied pointwise, inverse transformed, scaled, rounded and carried; the cost table totals O(n(lg n)^{1-κ}) for a fixed rational parameter choice.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine multiplies two n-bit integers in O(n(lg n)^{1-κ}) time with κ = 2^{-182}, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Turing machines and tapes
- `linear-algebra-over-the-reals-and-complex-numbers`: Linear algebra over the reals and complex numbers
- `linear-algebra-over-gf-2`: Linear algebra over GF(2)
- `triangular-matrices-and-gaussian-elimination`: Triangular matrices and Gaussian elimination
- `modular-arithmetic-and-prime-numbers`: Modular arithmetic and prime numbers
- `binary-and-two-s-complement-representation`: Binary and two's-complement representation
- `floor-ceiling-rounding-and-logarithms`: Floor, ceiling, rounding and logarithms
- `permutations-and-sorting`: Permutations and sorting
- `cartesian-products-and-mixed-radix-indexing`: Cartesian products and mixed-radix indexing
- `vector-norms-and-inequalities`: Vector norms and inequalities
- `geometric-series-and-recurrences`: Geometric series and recurrences
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `roots-of-unity-and-euler-s-formula`: Roots of unity and Euler's formula
- `asymptotic-conventions`: Asymptotic conventions
- `finite-state-and-constant-size-alphabets`: Finite-state and constant-size alphabets

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
