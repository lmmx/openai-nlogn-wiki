# exegenius task 0015-argument

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

`transform-identity`: Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: discrete mathematics through modular arithmetic, primes, gcds and the Euclidean algorithm, and the binary (radix) representation of integers; a first course in linear algebra over the reals covering vector spaces, bases, dimension, matrices, rank and invertibility; and the basics of complex numbers and roots of unity. They have not studied finite fields beyond GF(2), bilinear forms, tensor products, rings beyond polynomials, or the fast Fourier transform as a specialist topic, so those are explained by the wiki.

## Pages, in reading order

- `exact-integer-multiplication`: Exact integer multiplication: Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
- `radix-digit-convolution`: Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices wrap around modulo the sequence length.
- `discrete-fourier-transform`: Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- `operator-norm`: Operator norm: The norm of a linear map L is the supremum of ‖Lu‖ over vectors u with ‖u‖ ≤ 1, where the vector norm of a complex vector is the largest modulus among its coordinates; a linear contraction is a linear map of norm at most one.
- `gaussian-resampling`: Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- `transform-identity`: Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Turing machines and tapes
- `positional-radix-representation-of-integers`: Positional (radix) representation of integers
- `logarithm`: Logarithm
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `euclidean-algorithm-and-modular-inverses`: Euclidean algorithm and modular inverses
- `prime-numbers`: Prime numbers
- `roots-of-unity`: Roots of unity
- `vector-space-subspace-basis-and-dimension`: Vector space, subspace, basis and dimension
- `matrix-linear-map-rank-and-invertibility`: Matrix, linear map, rank and invertibility
- `dot-product-and-orthogonality`: Dot product and orthogonality
- `field-of-two-elements`: Field of two elements

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Previous plan (revise it: the pages have changed since)

```json
{
  "id": "S0",
  "intention": "show",
  "claim": "The transform identity $P_s F_s = 2^{2\\alpha^2} B_0 P_t F_t A$ holds with linear contractions $A$ and $B_0$, so the source permutation $P_s$ and target permutation $P_t$ stay in the formula instead of being executed as sorts.",
  "from": [
    "radix-digit-convolution",
    "exact-integer-multiplication",
    "discrete-fourier-transform",
    "gaussian-resampling"
  ],
  "method": "invert the Gaussian resampling identity, which keeps both permutations, to a pair of contractions and normalize the constants",
  "motivation": {
    "text": "The usual implementation sorts twice on each coordinate, so the two permutations are kept in the transform formula and that formula is computed directly.",
    "source": "explicit",
    "quote": {
      "source": "paper",
      "quote": "We retain both permutations in the transform formula and compute that formula directly."
    }
  },
  "salient": "the constant in front, $2^{2\\alpha^2}$, is a power of two that depends only on $\\alpha$, not on the coordinate lengths $s$ and $t$",
  "adds": [
    {
      "symbol": "s",
      "name": "source length",
      "meaning": "the source transform length $s$, the number of entries of the source vector, with $\\gcd(s,t)=1$",
      "relation": "count"
    },
    {
      "symbol": "t",
      "name": "target length",
      "meaning": "the target transform length $t$, the number of entries of the target vector, with $s<t$",
      "relation": "count"
    },
    {
      "symbol": "\\alpha",
      "name": "Gaussian width",
      "meaning": "the integer parameter that fixes the width of the Gaussian weights and the size of the constant $2^{2\\alpha^2}$",
      "relation": "direct"
    },
    {
      "symbol": "P_s",
      "name": "source permutation",
      "meaning": "the coordinate permutation $(P_s u)_j = u_{tj}$ of length-$s$ vectors",
      "relation": "direct"
    },
    {
      "symbol": "P_t",
      "name": "target permutation",
      "meaning": "the coordinate permutation $(P_t v)_k = v_{-sk}$ of length-$t$ vectors",
      "relation": "direct"
    }
  ],
  "page": "transform-identity",
  "children": [
    {
      "id": "S0.1",
      "intention": "show",
      "claim": "The Gaussian identity $TP_sF_s = P_tF_tS$ holds, with $S$ and $T$ Gaussian-weighted maps from length-$s$ to length-$t$ vectors, and the near-identity operator $N = CTD$ is invertible.",
      "from": [
        "discrete-fourier-transform",
        "roots-of-unity"
      ],
      "method": "write both transforms through a Gaussian-weighted resampling operator $N=CTD$ whose error from the identity is small",
      "motivation": {
        "text": "The Gaussian weight at the selected coordinate cancels the diagonal factor, so $N$ differs from the identity by a small amount that a Neumann series can invert.",
        "source": "recoverable"
      },
      "adds": [
        {
          "symbol": "S",
          "name": "Gaussian resampling map",
          "meaning": "the Gaussian-weighted map from length-$s$ to length-$t$ vectors, with $(Su)_k = \\frac{1}{\\alpha}\\sum_j e^{-\\pi\\alpha^{-2}(j-sk/t)^2}u_j$",
          "relation": "direct"
        },
        {
          "symbol": "T",
          "name": "dual Gaussian map",
          "meaning": "the Gaussian-weighted map from length-$s$ to length-$t$ vectors that pairs with $S$ through the frequency scaling $t/s$",
          "relation": "direct"
        },
        {
          "symbol": "N",
          "name": "near-identity operator",
          "meaning": "the operator $N=CTD$ on length-$s$ vectors, whose difference from the identity has norm below $1/2$",
          "relation": "direct"
        }
      ],
      "page": "gaussian-resampling",
      "children": [
        {
          "id": "S0.1.1",
          "intention": "infer",
          "claim": "The Gaussian identity $TP_sF_s = P_tF_tS$ holds.",
          "from": [
            "discrete-fourier-transform"
          ],
          "quote": {
            "source": "paper",
            "quote": "TPs Fs = Pt Ft S,"
          }
        },
        {
          "id": "S0.1.2",
          "intention": "infer",
          "claim": "$\\|N-I\\|<1/2$, so $N$ is invertible by the Neumann series.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series."
          }
        }
      ]
    },
    {
      "id": "S0.2",
      "intention": "infer",
      "claim": "The maps $A=S'$ and $B_0=D'J'C$ are linear contractions, since $\\|C\\|=1$ and $\\|S'\\|$, $\\|J'\\|$, $\\|D'\\|$ are below their stated bounds.",
      "from": [
        "discrete-fourier-transform"
      ],
      "quote": {
        "source": "paper",
        "quote": "Because ∥C∥ = 1, both are contractions."
      }
    },
    {
      "id": "S0.3",
      "intention": "infer",
      "claim": "The left inverse $DN^{-1}C$ of $TD^{-1}$ applied to the Gaussian identity gives $DN^{-1}CP_tF_tS = P_sF_s$.",
      "from": [],
      "quote": {
        "source": "paper",
        "quote": "Applying this left inverse to the first identity in (34) gives"
      }
    },
    {
      "id": "S0.4",
      "intention": "infer",
      "claim": "The normalizations $2^{-2\\alpha^2}$ give $B_0P_tF_tA = 2^{-2\\alpha^2}P_sF_s$, which is the transform identity (33) with the power of two $2^{2\\alpha^2}$.",
      "from": [],
      "quote": {
        "source": "paper",
        "quote": "which is (33)."
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

Write the answer to `exegenius/tasks/0015-argument.answer.json`, then run `exegenius submit 0015-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
