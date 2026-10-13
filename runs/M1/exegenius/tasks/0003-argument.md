# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/M1` (paths below are relative to it)

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

`main-result`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^-182, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed undergraduate computer science: asymptotic analysis, discrete mathematics (modular arithmetic, primes, basic number theory, finite sets, permutations), linear algebra over the reals and complex numbers (matrices, rank, invertibility, linear maps), and basic algorithm design including recursion, divide and conquer, recurrences, and the standard school and Karatsuba multiplication. They know Turing machines and tapes and probably the FFT as an algorithm, but not abstract algebra beyond basics, finite fields in depth, or any research-level multiplication algorithm.

## Pages, in reading order

- `nlogn-conjecture`: The n log n conjecture and prior multiplication algorithms: Schönhage–Strassen proposed n log n as optimal multiplication time; Harvey and van der Hoeven reached O(n log n).
- `ring-ymr`: Polynomial ring modulo y^r + 1: Complex polynomials modulo y^r+1 with r a power of two, in which multiplying by a power of y is a signed shift of the coefficient list.
- `butterfly`: Two-point butterfly: The map (u,v)↦((u+v)/2,(u−v)/2) applied to a pair of values; the building block of fast transforms.
- `fixed-point-exactness`: Fixed-point precision, exact dyadics and error control: Values are complex numbers on a 2^-p grid; intermediate arithmetic is exact over Gaussian dyadics, with a single truncation, and total error is kept below 1/2 so rounding recovers integers.
- `hh-multiplier`: O(n log n) multiplier as a subroutine: The established Harvey–van der Hoeven fixed-tape integer multiplier, called as an ordinary subroutine on short inputs.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying ring polynomials exactly by packing signed coefficients into one integer, calling the integer multiplier, and unpacking.
- `array-streams`: Arrays on tape, address fields and volume: Arrays are stored in lexicographic order with implicit addresses split into fields; volume V is the number of stored data bits; permutations are realized by scans.
- `linear-networks-frames`: Linear networks, roles and frames: A fixed linear network of gates exchanges two banks of values with signs and restores auxiliary values; roles are wire places and frames are invertible operators giving the stored representation, cancelling so the endpoint operator is the desired one.
- `lower-triangular-shear`: Lower triangular factorization and address shear: Any rational matrix factors as lower-triangular times partial permutation times lower-triangular, so edge operators and address shears (H,D)↦(H+D,D) can be done in tape order at cost scaling with rank.
- `subset-networks`: Finite networks from three-element subsets: Construction using three-element subsets, gather, scatter and scratch wires, with nested subspaces at vertices so that the total number of smaller calls is below the number of roles times m.
- `recursive-saving`: Recursive power saving s < Wm: Using s calls at parameter f on volume V/W each, with s<Wm, makes the cost per volume grow by a factor below m when the parameter is multiplied by m, giving a power rather than linear growth.
- `address-interchange`: Fast address-chunk interchange: Interchanging two disjoint address fields of u bits in an array of volume V in time O(V u^τ) with τ<1, via XOR combinations of intermediate data that finally give an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applying the butterfly on the same bit position of up to d address chunks at once, on complex polynomial records, in time O(V d^λ') with λ'<1, instead of d whole-array passes.
- `dft-convolution`: Discrete Fourier transform and cyclic convolution: The DFT maps a length-q sequence to averages weighted by roots of unity; it turns cyclic convolution into pointwise multiplication.
- `radix-convolution`: Multiplication as convolution of radix digits: Splitting inputs into radix digits turns integer multiplication into convolution of short integer coefficient lists, later carried back to the binary product by carries.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier transforms over the ring modulo y^r+1 using powers of y as roots of unity, so root multiplications are signed shifts, evaluated by butterfly layers with a retained frequency order.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: The coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform, including its target permutation, into a cyclic convolution with pointwise phase multiplications.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform of coprime length through a power-of-two transform, here keeping the two coordinate permutations inside the transform formula.
- `multiplication-algorithm`: Assembly of the integer multiplication algorithm: The pipeline: digits, Chinese-remainder prime axes, Gaussian resampling, chirp convolution, phase twist to the ring modulo y^r+1, synthetic transforms with fast layers, then rescaling, rounding and carries.
- `main-result`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^-182, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `modular-arithmetic-and-residue-rings`: Modular arithmetic and residue rings
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `binary-representation-of-integers`: Binary representation of integers
- `matrices-linear-maps-and-rank`: Matrices, linear maps and rank
- `permutations`: Permutations
- `logarithms-and-exponents`: Logarithms and exponents
- `recurrences-and-divide-and-conquer`: Recurrences and divide and conquer
- `fast-fourier-transform`: Fast Fourier transform
- `karatsuba-and-schoolbook-multiplication`: Karatsuba and schoolbook multiplication
- `floating-point-and-rounding-errors`: Floating-point and rounding errors
- `sets-products-and-tuples`: Sets, products and tuples
- `linear-time-scanning-of-tapes`: Linear-time scanning of tapes
- `asymptotic-constants-and-small-epsilon-exponents`: Asymptotic constants and small epsilon exponents

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
