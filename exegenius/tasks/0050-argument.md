# exegenius task 0050-argument

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

`integer-multiplication-target`: Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science degree: big-O notation and worst-case time of Turing machines, polynomials and complex numbers, and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). The same degree is taken to include introductory discrete mathematics (modular arithmetic, primes, induction, sets, graphs, recurrences) and a first course in linear algebra over the reals (vectors, subspaces, matrices, elimination, dot products), each at introductory depth. Fields in the abstract sense, tensor products, bilinear forms over general fields, Gaussian integers and the Chinese remainder theorem are not assumed.

## Pages, in reading order

- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture: The conjecture of Schönhage and Strassen that n log n is the optimal order of growth of the time to multiply two n-bit integers on a multitape Turing machine.
- `harvey-hoeven-multiplier`: Harvey–van der Hoeven O(n log n) multiplication: The unconditional O(n log n) multiplication algorithm on a multitape Turing machine, used in this result as an ordinary subroutine.
- `roots-of-unity`: Primitive roots of unity: A complex number ω is a primitive n-th root of unity when ω^n = 1 and no smaller positive power equals 1.
- `fourier-transform`: Discrete Fourier transform: The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity.
- `butterfly-operation`: Butterfly operation: The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices are taken modulo a fixed length, so each coefficient of the result is a sum of products over residues.
- `convolution-reduction`: Multiplication as convolution of digits: Writing each integer in radix 2^b digits so that the integer product becomes a convolution of the digit sequences, which is then carried back to binary.
- `polynomial-ring-y`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials in y reduced modulo y^r + 1, where multiplying by a power of y is a signed cyclic shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions.
- `kronecker-packing`: Signed Kronecker packing: Encoding a polynomial with bounded signed coefficients as an integer by evaluating it at a large power of two, so that polynomial products become integer products.
- `matrix-rank`: Matrix rank: The rank of a matrix is the maximum number of linearly independent rows or columns; the number of nonzero pivots in elimination.
- `linear-network-exchange`: Linear network with restored auxiliary values: A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges.
- `lower-triangular-factorization`: Lower-triangular factorization: The factorization A = E₁ΠE₂ of a rational matrix into invertible lower-triangular factors and a partial permutation matrix with one 1 per pivot.
- `address-shear`: Address shear: The permutation (H, D) ↦ (H + AD, D) on two ordered groups of address fields, which is performed with as many pairwise interchanges as the rank of A.
- `address-interchange`: Fast address interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time O(V u^τ) for width u, computed through XOR combinations of intermediate data.
- `chinese-remainder-address-map`: Chinese-remainder address map: A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges.
- `gaussian-resampling`: Gaussian resampling: An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.
- `bluestein-chirp`: Bluestein's chirp identity: The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.
- `tensor-product`: Tensor product: The tensor product V ⊗ W of two vector spaces, whose basis consists of all pairs of basis vectors of V and W, together with the tensor product A ⊗ B of linear maps, which acts on each coordinate separately.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.
- `recursive-power-saving`: Recursive power saving: The mechanism in which a network with s smaller calls on W roles and parameter m gives a recursion with cost ratio s/W < m, so that repeated recursion saves a power of the parameter.
- `rounding-recovery`: Exact recovery by rounding: The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.
- `integer-multiplication-target`: Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `multitape-tm`: Multitape Turing machine
- `complex-numbers`: Complex numbers
- `polynomials`: Polynomials
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-greatest-common-divisors`: Prime numbers and greatest common divisors
- `arithmetic-modulo-2-and-xor`: Arithmetic modulo 2 and XOR
- `dyadic-rationals`: Dyadic rationals
- `vector-spaces-subspaces-bases-and-dimension`: Vector spaces, subspaces, bases and dimension
- `linear-maps-matrix-operations-and-invertibility`: Linear maps, matrix operations and invertibility
- `gaussian-elimination`: Gaussian elimination
- `triangular-matrices`: Triangular matrices
- `dot-product-and-orthogonality-in-r-n`: Dot product and orthogonality in R^n
- `permutations-of-a-finite-set`: Permutations of a finite set
- `finite-sets-subsets-and-intersections`: Finite sets, subsets and intersections
- `graphs`: Graphs
- `mathematical-induction`: Mathematical induction
- `recurrence-relations-and-divide-and-conquer-recursion`: Recurrence relations and divide-and-conquer recursion
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `logarithms-base-2`: Logarithms base 2
- `big-omega-and-big-theta-notation`: Big-Omega and big-Theta notation
- `limits-and-convergence-of-sequences-and-series`: Limits and convergence of sequences and series
- `geometric-series`: Geometric series
- `newton-s-method`: Newton's method
- `worst-case-time-complexity-of-a-turing-machine`: Worst-case time complexity of a Turing machine

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Previous plan (revise it: the pages have changed since)

```json
{
  "id": "S0",
  "intention": "show",
  "claim": "Two $n$-bit integers can be multiplied exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time on a deterministic multitape Turing machine, for a fixed $\\kappa=2^{-182}$.",
  "from": [
    "nlogn-conjecture"
  ],
  "method": "reduce the product to a digit convolution, compute that convolution through transform layers whose tape cost saves a power, and recover the exact product by rounding",
  "motivation": {
    "text": "Each transform level scans $\\Theta(n)$ bits, so only savings in both movement and arithmetic beat $n\\log n$.",
    "source": "explicit",
    "quote": {
      "source": "paper",
      "quote": "We therefore need savings in both movement and arithmetic."
    }
  },
  "page": "integer-multiplication-target",
  "children": [
    {
      "id": "S1",
      "intention": "show",
      "claim": "The integer product is the carried convolution of the radix-$2^b$ digit sequences of the two inputs.",
      "from": [],
      "method": "write each input in radix digits, convolve the digit sequences, and carry the result back to binary",
      "motivation": {
        "text": "Short digit coefficients let the transform machinery act on fixed-width records.",
        "source": "recoverable"
      },
      "page": "convolution-reduction",
      "children": [
        {
          "id": "S1.1",
          "intention": "infer",
          "claim": "Multiplication reduces to convolution of short integer coefficients.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Splitting the inputs into radix digits reduces multiplication to"
          }
        }
      ]
    },
    {
      "id": "S2",
      "intention": "show",
      "claim": "Both tape procedures cost $O(V)$ times a power of their parameter whose exponent is strictly below one.",
      "from": [
        "matrix-rank",
        "lower-triangular-factorization",
        "address-shear",
        "linear-network-exchange"
      ],
      "method": "give each procedure a fixed linear network with fewer smaller calls than roles, and iterate the resulting recursion",
      "motivation": {
        "text": "If the number of smaller calls per role is below the parameter multiplier, repeated recursion compounds into a power saving.",
        "source": "recoverable"
      },
      "salient": "the saving is a fixed power of the parameter, with exponent strictly below one, uniform over all widths and volumes",
      "page": "recursive-power-saving",
      "children": [
        {
          "id": "S2.1",
          "intention": "infer",
          "claim": "The address interchange of $u$-bit fields costs $O(Vu^\\tau)$ for a fixed $\\tau<1$.",
          "from": [
            "arithmetic-modulo-2-and-xor"
          ],
          "page": "address-interchange",
          "quote": {
            "source": "paper",
            "quote": "Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."
          }
        },
        {
          "id": "S2.2",
          "intention": "infer",
          "claim": "A simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$.",
          "from": [
            "butterfly-operation",
            "dyadic-rationals"
          ],
          "page": "simultaneous-butterfly-layer",
          "quote": {
            "source": "paper",
            "quote": "the cost is $O(Vd^{\\lambda'})$ for a"
          }
        },
        {
          "id": "S2.3",
          "intention": "infer",
          "claim": "Each tape procedure is a fixed linear network that exchanges two banks of values and restores every auxiliary value.",
          "from": [
            "linear-maps-matrix-operations-and-invertibility"
          ],
          "page": "linear-network-exchange",
          "quote": {
            "source": "paper",
            "quote": "Each procedure arises from its own fixed linear network that exchanges two"
          }
        },
        {
          "id": "S2.4",
          "intention": "infer",
          "claim": "The network has $W$ roles and $s$ smaller calls with $s<Wm$.",
          "from": [
            "matrix-rank"
          ],
          "quote": {
            "source": "paper",
            "quote": "number $s$ of smaller calls satisfies $s<Wm$."
          }
        },
        {
          "id": "S2.5",
          "intention": "infer",
          "claim": "Multiplying the parameter by $m$ multiplies the recursive cost ratio by $s/W<m$, which is a strict power saving.",
          "from": [
            "recurrence-relations-and-divide-and-conquer-recursion"
          ],
          "quote": {
            "source": "paper",
            "quote": "increases the recursive contribution by $s/W<m$."
          }
        }
      ]
    },
    {
      "id": "S3",
      "intention": "show",
      "claim": "The radix-digit coefficient list is placed on a product of distinct prime cyclic axes, preserving convolution.",
      "from": [
        "cyclic-convolution",
        "modular-arithmetic",
        "prime-numbers-and-greatest-common-divisors"
      ],
      "method": "apply a Chinese-remainder split of the cyclic index, realized by controlled cyclic shifts and address interchanges",
      "motivation": {
        "text": "The Chinese-remainder split turns one cyclic convolution into a multidimensional one, and controlled shifts make the reordering cheap.",
        "source": "explicit",
        "quote": {
          "source": "paper",
          "quote": "with coordinate powers that make the change of order a"
        }
      },
      "page": "chinese-remainder-address-map",
      "children": [
        {
          "id": "S3.1",
          "intention": "infer",
          "claim": "The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "First, the radix-digit coefficient list is placed on a product of"
          }
        }
      ]
    },
    {
      "id": "S4",
      "intention": "show",
      "claim": "A Fourier transform of prime length is a multidimensional transform whose axis lengths are powers of two.",
      "from": [
        "roots-of-unity",
        "fourier-transform"
      ],
      "method": "apply Gaussian resampling and keep the source and target permutations inside the transform identity",
      "motivation": {
        "text": "Power-of-two axes can be evaluated with polynomial roots of unity, which become signed shifts.",
        "source": "recoverable"
      },
      "page": "gaussian-resampling",
      "children": [
        {
          "id": "S4.1",
          "intention": "infer",
          "claim": "Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "resampling then expresses each source Fourier transform through a"
          }
        }
      ]
    },
    {
      "id": "S5",
      "intention": "show",
      "claim": "The middle transform, with its target permutation, becomes normalized cyclic convolution.",
      "from": [
        "cyclic-convolution",
        "fourier-transform"
      ],
      "method": "Bluestein's chirp identity with chirp factors before and after the transform",
      "motivation": {
        "text": "A cyclic convolution is the form that the polynomial-ring convolution can compute.",
        "source": "recoverable"
      },
      "page": "bluestein-chirp",
      "children": [
        {
          "id": "S5.1",
          "intention": "infer",
          "claim": "Bluestein's chirp identity converts the middle transform into a normalized cyclic convolution.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Next, Bluestein's chirp identity converts the middle transform,"
          }
        }
      ]
    },
    {
      "id": "S6",
      "intention": "show",
      "claim": "The last cyclic coordinate becomes a polynomial modulo $y^r+1$, so that its wrap is a signed shift.",
      "from": [
        "polynomials",
        "roots-of-unity"
      ],
      "method": "apply a phase twist to the last cyclic coordinate",
      "motivation": {
        "text": "Multiplying by a power of $y$ is a signed cyclic shift, so the twisted coordinate needs no general multiplication.",
        "source": "recoverable"
      },
      "page": "polynomial-ring-y",
      "children": [
        {
          "id": "S6.1",
          "intention": "infer",
          "claim": "A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "A phase twist changes the last cyclic coordinate into a polynomial"
          }
        }
      ]
    },
    {
      "id": "S7",
      "intention": "show",
      "claim": "The two forward synthetic transforms keep the same frequency order through their pointwise product, and the opposite transform consumes that order.",
      "from": [
        "polynomial-ring-y"
      ],
      "method": "run synthetic transforms whose roots of unity are powers of $y$ and whose layers use signed shifts and butterflies",
      "motivation": {
        "text": "Powers of $y$ as roots of unity make each transform stage a signed shift plus butterfly additions.",
        "source": "recoverable"
      },
      "page": "synthetic-transform",
      "children": [
        {
          "id": "S7.1",
          "intention": "infer",
          "claim": "The two forward synthetic transforms keep the same frequency order through their pointwise product.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "The two forward synthetic transforms"
          }
        }
      ]
    },
    {
      "id": "S8",
      "intention": "show",
      "claim": "Polynomial products over the ring are computed by signed packing and the $O(n\\log n)$ multiplier.",
      "from": [
        "harvey-hoeven-multiplier",
        "polynomials"
      ],
      "method": "signed Kronecker packing of the coefficients, followed by the established multiplier as a subroutine",
      "motivation": {
        "text": "Evaluating a polynomial at a large power of two turns its product into an integer product.",
        "source": "recoverable"
      },
      "page": "kronecker-packing",
      "children": [
        {
          "id": "S8.1",
          "intention": "infer",
          "claim": "Polynomial products use signed packing and the established $O(n\\log n)$ multiplier as an ordinary subroutine.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "use signed packing and the established $O(n\\log n)$ multiplier as an"
          }
        }
      ]
    },
    {
      "id": "S9",
      "intention": "show",
      "claim": "The exact product is recovered: the source permutation cancels, and the coefficient error is below $1/2$, so rounding and carries give the binary product.",
      "from": [
        "gaussian-resampling",
        "dyadic-rationals"
      ],
      "method": "cancel the retained source permutation, then round the approximate coefficients and propagate carries",
      "motivation": {
        "text": "Rounding recovers the integer coefficients only once the error is strictly below one half.",
        "source": "recoverable"
      },
      "page": "rounding-recovery",
      "children": [
        {
          "id": "S9.1",
          "intention": "infer",
          "claim": "The source permutation retained during resampling cancels across the forward transforms, their product, and the opposite transform.",
          "from": [
            "gaussian-resampling"
          ],
          "quote": {
            "source": "paper",
            "quote": "Finally, the source permutation retained during resampling cancels"
          }
        },
        {
          "id": "S9.2",
          "intention": "infer",
          "claim": "The recovered coefficient error is strictly below $1/2$, and carries are propagated to give the exact binary product.",
          "from": [
            "dyadic-rationals"
          ],
          "quote": {
            "source": "paper",
            "quote": "coefficient error is strictly below $1/2$, and propagates carries to"
          }
        }
      ]
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

Write the answer to `exegenius/tasks/0050-argument.answer.json`, then run `exegenius submit 0050-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
