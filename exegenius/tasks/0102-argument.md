# exegenius task 0102-argument

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

`main-theorem`: Integer multiplication in O(n(lg n)^{1-κ}) time: Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

## Pages, in reading order

- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage–Strassen's proposal that n log n is the optimal order of cost for multiplying n-bit integers.
- `convolution`: Convolution: Product of polynomials / combination of coefficient lists where entries sum by index (cyclic if indices wrap).
- `radix-digit-reduction`: Reduction of integer product to digit convolution: Splitting the inputs into radix digits turns the integer product into a convolution of short integer coefficients, followed by carry propagation.
- `poly-ring-y-r`: Polynomial ring modulo $y^r+1$: Complex-coefficient polynomials in y reduced by y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list and powers of y serve as roots of unity.
- `fixed-tape-model`: Fixed-tape machine model and stream operations: Machine with one fixed finite alphabet and a fixed number of one-dimensional tapes; each step touches one cell per tape, so data movement (scans, shifts, permutations) is the cost to minimize.
- `address-fields`: Address fields and array layout on tapes: Arrays stored in tape order with addresses forming a Cartesian product of digit fields; rearranging fields costs time.
- `dft-fft`: Discrete Fourier transform and butterflies: Evaluation of a coefficient list at roots of unity, computed in log-many levels of two-point butterfly operations; turns convolution into pointwise product.
- `ss-hh-background`: Schönhage–Strassen to Harvey–van der Hoeven multiplication: Chain of multitape algorithms from O(n log n log log n) to the unconditional O(n log n) bound, using transforms over rings with cheap roots of unity.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms over the polynomial ring where root multiplications are signed shifts, leaving address rearrangements, shifts and butterflies.
- `linear-network-roles`: Finite linear network with roles and frames: Fixed linear network exchanging two banks of values with prescribed signs and restoring auxiliary values; wires have roles, rows are distributed cyclically among roles, and invertible frame operators cancel along routes leaving an endpoint operator.
- `scratch-restoration`: Restoring auxiliary scratch values: Subtract initial register value, compute, add result, reverse, so the permutation is exact for arbitrary initial auxiliary values.
- `address-shear-factorization`: Address shear and lower-triangular factorization: Endpoint operator (H,D)->(H+D,D) over a residue ring, with rank reduction via a singular-matrix Bruhat factorization into lower-triangular factors.
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: Places the coefficient list on a product of distinct prime cyclic axes by a map preserving convolution, implemented via triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing each Fourier transform of prime-length axes through a multidimensional transform with power-of-two axis lengths.
- `bluestein-chirp`: Bluestein's chirp identity: Rewrites a discrete Fourier transform as a cyclic convolution via chirp phases.
- `phase-twist-convolution`: Last-coordinate phase twist: Twisting the last cyclic coordinate into a polynomial modulo y^r+1 whose negative wrap equals the original cyclic wrap after untwisting.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.
- `signed-packing`: Signed coefficient packing (Kronecker substitution): Packs polynomial coefficients into one integer so polynomial products are done by an ordinary n log n integer multiplier.
- `ring-convolution-retained-order`: Convolution with retained transform order and cancelled permutations: Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it, so retained permutations cancel without separate sorts.
- `tensor-product-of-vector-spaces`: Tensor product of vector spaces: The space built from tuples of vectors whose dimension is the product of the factors' dimensions, so (Q^h)^{⊗3} has dimension h^3.
- `subset-intersection-construction`: Three-element subset intersection construction: Gather/scatter with auxiliary wires cancelling unwanted coefficients, using indicator-vector orthogonality to assign subspaces; gives s<Wm smaller calls.
- `recursive-power-saving`: Recursive power saving from s<Wm: Recursive call at parameter mf uses s calls at parameter f on streams of volume V/W; since s/W<m the volume-normalized cost grows as a power, giving a fixed power saving.
- `fast-address-interchange`: Fast interchange of address fields: Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.
- `main-theorem`: Integer multiplication in O(n(lg n)^{1-κ}) time: Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Multitape Turing machine
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `logarithms-and-floor-ceiling`: Logarithms and floor/ceiling
- `vectors-matrices-and-inverses`: Vectors, matrices and inverses
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences
- `limits-series-and-convergence`: Limits, series and convergence
- `cartesian-product-and-tuples`: Cartesian product and tuples
- `permutations`: Permutations
- `roots-of-unity`: Roots of unity
- `rings-and-basic-algebraic-structures`: Rings and basic algebraic structures
- `fixed-point-and-rounding-arithmetic`: Fixed-point and rounding arithmetic

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Previous plan (revise it: the pages have changed since)

```json
{
  "id": "S0",
  "intention": "show",
  "claim": "An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\\lg n)^{1-\\kappa})$ time, $\\kappa=2^{-182}$.",
  "from": [
    "nlogn-conjecture",
    "ss-hh-background",
    "fixed-tape-model",
    "big-o",
    "turing-machine-tapes"
  ],
  "method": "reduce multiplication to ring convolution and speed up its address moves and butterfly layers",
  "motivation": {
    "text": "The n log n cost comes from moving data and applying butterflies at every transform level, so faster versions of exactly these operations lower the whole bound.",
    "source": "recoverable"
  },
  "salient": "The logarithmic factor drops by a fixed power $\\kappa$, strictly below the conjectured $n\\log n$.",
  "page": "main-theorem",
  "children": [
    {
      "id": "S2",
      "intention": "infer",
      "claim": "Splitting the inputs into radix digits reduces the integer product to a convolution of short integer coefficients.",
      "from": [
        "convolution"
      ],
      "page": "radix-digit-reduction",
      "quote": {
        "source": "paper",
        "quote": "Splitting the inputs into radix digits reduces multiplication to"
      }
    },
    {
      "id": "S1",
      "intention": "show",
      "claim": "Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\\tau)$ and $O(Vd^{\\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume.",
      "from": [],
      "method": "build both procedures from one finite linear network and a recursion that saves a power",
      "motivation": {
        "text": "Scanning the array at each of the logarithmically many transform levels already costs n log n, so both data movement and arithmetic must be sped up.",
        "source": "explicit",
        "quote": {
          "source": "paper",
          "quote": "We therefore need savings in both movement and arithmetic."
        }
      },
      "adds": [
        {
          "symbol": "V",
          "name": "stored volume",
          "meaning": "The number of stored bits in the array being processed.",
          "relation": "count"
        },
        {
          "symbol": "W",
          "name": "role count",
          "meaning": "The number of roles among which rows are distributed.",
          "relation": "count"
        },
        {
          "symbol": "m",
          "name": "space dimension",
          "meaning": "The dimension of the fixed space whose subspaces label the network.",
          "relation": "count"
        },
        {
          "symbol": "s",
          "name": "smaller calls",
          "meaning": "The number of smaller calls the network uses.",
          "relation": "count"
        }
      ],
      "children": [
        {
          "id": "S1.1",
          "intention": "infer",
          "claim": "Each procedure comes from a fixed linear network that exchanges two banks of values with prescribed signs and restores every auxiliary value; rows are distributed among $W$ roles and frames cancel along routes.",
          "from": [
            "fixed-tape-model",
            "address-fields",
            "vectors-matrices-and-inverses"
          ],
          "page": "linear-network-roles",
          "quote": {
            "source": "paper",
            "quote": "Each procedure arises from its own fixed linear network that exchanges two"
          }
        },
        {
          "id": "S1.2",
          "intention": "show",
          "claim": "Two disjoint contiguous $u$-bit address fields can be interchanged in $O(Vu^\\tau)$ for a fixed $\\tau<1$, although the intermediate steps are XOR combinations.",
          "from": [
            "scratch-restoration",
            "address-fields",
            "linear-network-roles",
            "recursive-power-saving"
          ],
          "method": "take the network's endpoint operator to be an address shear and finish with two linear-cost updates",
          "motivation": {
            "text": "The network only yields the shear (H,D)->(H+D,D); to get a true interchange of fields that shear must be completed by cheap updates.",
            "source": "recoverable"
          },
          "salient": "Its final effect is an exact permutation, even though intermediate steps form XOR combinations of data, and exact for arbitrary initial auxiliary values.",
          "page": "fast-address-interchange",
          "children": [
            {
              "id": "S1.2.1",
              "intention": "infer",
              "claim": "The endpoint operator of the bit network is the address shear $(H,D)\\mapsto(H+D,D)$ over a residue ring, with rank reduced by a lower-triangular factorization.",
              "from": [
                "modular-arithmetic",
                "vectors-matrices-and-inverses",
                "linear-network-roles"
              ],
              "page": "address-shear-factorization",
              "quote": {
                "source": "paper",
                "quote": "For the bit procedure, that endpoint operator is an address shear:"
              }
            },
            {
              "id": "S1.2.2",
              "intention": "infer",
              "claim": "Two further linear-cost address updates complete the interchange.",
              "from": [],
              "quote": {
                "source": "paper",
                "quote": "updated by $(H,D)\\mapsto(H+D,D)$. Two further linear-cost address"
              }
            }
          ]
        },
        {
          "id": "S1.3",
          "intention": "infer",
          "claim": "A simultaneous layer of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on selected address bits of polynomial-valued arrays costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, with a single truncation at the end.",
          "from": [
            "poly-ring-y-r",
            "dft-fft",
            "fixed-point-and-rounding-arithmetic",
            "fast-address-interchange",
            "recursive-power-saving",
            "linear-network-roles"
          ],
          "page": "fast-butterfly-layers",
          "quote": {
            "source": "paper",
            "quote": "endpoint operator becomes the simultaneous $H_0$ layer after diagonal"
          }
        },
        {
          "id": "S1.4",
          "intention": "infer",
          "claim": "The network is built from three-element subsets with gather, scatter and cancelling auxiliary wires, so that the total number $s$ of smaller calls satisfies $s<Wm$.",
          "from": [
            "linear-network-roles",
            "scratch-restoration"
          ],
          "salient": "The number of smaller calls is strictly below the trivial count, $s<Wm$.",
          "page": "subset-intersection-construction",
          "quote": {
            "source": "paper",
            "quote": "number $s$ of smaller calls satisfies $s<Wm$."
          }
        },
        {
          "id": "S1.5",
          "intention": "infer",
          "claim": "A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, so the volume-normalized cost grows as a power, giving a fixed power saving.",
          "from": [
            "subset-intersection-construction",
            "divide-and-conquer-recurrences"
          ],
          "salient": "The strict inequality $s/W<m$ is the source of the power saving.",
          "page": "recursive-power-saving",
          "quote": {
            "source": "paper",
            "quote": "increases the recursive contribution by $s/W<m$. This strict inequality"
          }
        }
      ]
    },
    {
      "id": "S3",
      "intention": "infer",
      "claim": "The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a convolution-preserving Chinese-remainder map.",
      "from": [
        "address-fields",
        "convolution",
        "prime-numbers-and-coprimality",
        "modular-arithmetic",
        "fast-address-interchange"
      ],
      "page": "crt-address-map",
      "quote": {
        "source": "paper",
        "quote": "distinct prime cyclic axes by a Chinese-remainder map that preserves"
      }
    },
    {
      "id": "S4",
      "intention": "infer",
      "claim": "Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.",
      "from": [
        "dft-fft",
        "crt-address-map"
      ],
      "page": "gaussian-resampling",
      "quote": {
        "source": "paper",
        "quote": "resampling then expresses each source Fourier transform through a"
      }
    },
    {
      "id": "S5",
      "intention": "infer",
      "claim": "Bluestein's chirp identity converts the middle transform into normalized cyclic convolution.",
      "from": [
        "dft-fft",
        "convolution"
      ],
      "page": "bluestein-chirp",
      "quote": {
        "source": "paper",
        "quote": "Next, Bluestein's chirp identity converts the middle transform,"
      }
    },
    {
      "id": "S6",
      "intention": "infer",
      "claim": "A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, whose negative wrap gives the original cyclic wrap after untwisting.",
      "from": [
        "poly-ring-y-r",
        "convolution"
      ],
      "page": "phase-twist-convolution",
      "quote": {
        "source": "paper",
        "quote": "A phase twist changes the last cyclic coordinate into a polynomial"
      }
    },
    {
      "id": "S7",
      "intention": "show",
      "claim": "Convolution over $\\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by synthetic transforms and packed polynomial products.",
      "from": [
        "fast-address-interchange",
        "fast-butterfly-layers"
      ],
      "method": "use two forward transforms, a pointwise product and the opposite transform, with retained frequency order",
      "motivation": {
        "text": "Convolution becomes pointwise product after transform; keeping the same frequency order means no separate sorts are needed.",
        "source": "recoverable"
      },
      "page": "ring-convolution-retained-order",
      "children": [
        {
          "id": "S7.1",
          "intention": "infer",
          "claim": "Synthetic transforms over the polynomial ring need only signed shifts, address rearrangements and butterflies.",
          "from": [
            "poly-ring-y-r",
            "dft-fft",
            "convolution"
          ],
          "page": "synthetic-transforms",
          "quote": {
            "source": "paper",
            "quote": "and~\\ref{sec:exact-ring-products} compute convolution on the remaining"
          }
        },
        {
          "id": "S7.2",
          "intention": "infer",
          "claim": "The two forward transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "retain the same frequency order through their pointwise product, and"
          }
        },
        {
          "id": "S7.3",
          "intention": "infer",
          "claim": "Polynomial products use signed packing and the ordinary $O(n\\log n)$ multiplier as a subroutine.",
          "from": [
            "convolution",
            "polynomials"
          ],
          "page": "signed-packing",
          "quote": {
            "source": "paper",
            "quote": "use signed packing and the established $O(n\\log n)$ multiplier as an"
          }
        }
      ]
    },
    {
      "id": "S8",
      "intention": "infer",
      "claim": "Known rescalings and rounding recover the coefficients since the error is below $1/2$, and carry propagation gives the exact product.",
      "from": [
        "fixed-point-and-rounding-arithmetic",
        "radix-digit-reduction"
      ],
      "page": "fixed-point-precision",
      "quote": {
        "source": "paper",
        "quote": "coefficient error is strictly below $1/2$, and propagates carries to"
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

Write the answer to `exegenius/tasks/0102-argument.answer.json`, then run `exegenius submit 0102-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
