# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/A3` (paths below are relative to it)

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

`main-result`: Integer multiplication below n log n: A fixed deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^(1−κ)) worst-case time with κ = 2^−182, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science background: asymptotic analysis, discrete mathematics (binary numbers, modular arithmetic, primes, XOR, subsets), introductory linear algebra (matrices, invertibility, vector subspaces, dimension), and basic complex numbers and polynomials. They know basic Turing machines with tapes, and have seen the standard FFT idea at most as an algorithm, not the Nussbaumer, Bluestein or Harvey-van der Hoeven machinery. They have not studied algebraic number theory, advanced algebra such as Bruhat factorization, or numerical error analysis in depth.

## Pages, in reading order

- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen multiplied n-bit integers in O(n log n log log n) on a multitape machine and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `convolution-dft`: Convolution and the discrete Fourier transform: Convolution of coefficient lists is computed by transforming, multiplying pointwise, and transforming back using roots of unity.
- `radix-digit-reduction`: Multiplication as digit convolution: Splitting the inputs into radix digits turns integer multiplication into convolution of short integer coefficients, followed by carry propagation.
- `poly-ring-mod-yr1`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients reduced using y^r = −1; powers of y act as roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Gaussian dyadic intermediates with a single truncation after a contractive layer; the recovered coefficient error is kept below 1/2 so rounding and carries give the exact integer product.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform (with its target permutation) into a cyclic convolution via multiplication by chirp phases.
- `phase-twist`: Last-coordinate phase twist: A phase twist turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap once the twist is removed.
- `signed-packing`: Signed coefficient packing (Kronecker substitution): Packing polynomial coefficients into one long integer so a polynomial product becomes an integer product.
- `hh-nlogn-multiplier`: Established O(n log n) multiplier as subroutine: The Harvey–van der Hoeven O(n log n) algorithm, called as an ordinary subroutine for small polynomial products without recursively invoking the new theorem.
- `stream-operations`: Elementary stream operations on tapes: Array order, scans, controlled shifts and rational scalings that a fixed-tape machine performs in linear time.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring where powers of y serve as roots of unity, built from address rearrangements, signed shifts and two-point butterflies (Nussbaumer).
- `linear-networks-frames`: Linear networks, roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; roles are wire positions and invertible frames D_v change the stored representation so intermediate frames cancel and only an endpoint operator remains.
- `restoring-auxiliary`: Restoring auxiliary values: Scratch registers with arbitrary initial contents are subtracted, used, re-added and the computation reversed so the final effect is exact for any initial auxiliary values.
- `address-shear`: Address shear and triangular factorization: Fields updated by (H,D) -> (H+D,D) over a residue ring; rational matrix shears are factored into lower-triangular pieces (Bruhat factorization) so they can be implemented cheaply in tape order.
- `subset-network-construction`: Finite network from three-element subsets: Subspaces of a fixed m-dimensional space attached to gates, built from three-element subsets with gather/scatter and auxiliary wires, giving a total number of smaller calls s less than W·m.
- `recursive-saving`: Recursive power saving s < Wm: Recursing at parameter m·f uses s calls at parameter f on volume V/W each; since s/W < m the volume-normalized cost grows by less than a factor m per level, giving a power of the parameter below the first power.
- `address-interchange`: Fast interchange of address fields: Exchanging two disjoint contiguous u-bit address fields of an array with volume V in O(V u^τ) time for fixed τ<1, using XOR combinations of intermediate data though the final effect is an exact permutation.
- `butterfly-layer`: Simultaneous butterfly layer H₀: Applying H_0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on selected address bits of numerical arrays of complex fixed-point polynomial records, via the recursive network, in O(V d^λ') time.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the coefficient list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing a Fourier transform on prime-length axes through a multidimensional transform with power-of-two axis lengths; the coordinate permutations are retained in the identity.
- `exact-ring-products`: Exact normalized polynomial products: Convolution over the ring using the forward synthetic transforms, pointwise polynomial products via signed packing and the O(n log n) multiplier, and the opposite transform.
- `transform-layout`: Transform layout with retained frequency order and permutations: Tape layout on which the parallel layers apply; permutations from resampling and chirps are kept inside the transform and cancel across forward, pointwise product and opposite transforms rather than being sorted.
- `main-algorithm`: Multiplication algorithm and its cost: Chain the reductions: digits, prime axes, Gaussian resampling and chirps, phase twist, ring convolution with fast interchanges and butterfly layers, then rescaling, rounding and carries; the cost table fits n(lg n)^(1−κ).
- `main-result`: Integer multiplication below n log n: A fixed deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^(1−κ)) worst-case time with κ = 2^−182, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `logarithms-and-ceiling-floor`: Logarithms and ceiling/floor
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `bitwise-xor`: Bitwise XOR
- `matrices-and-linear-maps`: Matrices and linear maps
- `vector-subspaces-and-dimension`: Vector subspaces and dimension
- `cartesian-product-and-index-sets`: Cartesian product and index sets
- `permutations`: Permutations
- `fixed-point-and-rounding`: Fixed-point and rounding
- `absolute-value-modulus-and-sup-norm`: Absolute value, modulus and sup norm
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `divide-and-conquer-recursion`: Divide and conquer recursion
- `induction-and-proof-by-contradiction`: Induction and proof by contradiction
- `linear-time-scanning-of-tape-data`: Linear-time scanning of tape data
- `euclidean-division-and-floor-division`: Euclidean division and floor division
- `geometric-series-and-exponent-rules`: Geometric series and exponent rules

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
