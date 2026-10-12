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

For these sources: The reader has completed an undergraduate computer science degree, so they know big-O and related asymptotic notation, polynomials, complex numbers (roots of unity, polar form), and Turing machines with tapes. They also know the discrete mathematics and first linear algebra that every such degree teaches: modular arithmetic, gcd and primes, sets, permutations, binary and radix notation, XOR over GF(2), induction, recurrences and geometric sums, and vector spaces, matrices and Gaussian elimination over a field, with basic sorting. They have not met the Chinese remainder theorem, the FFT, tensor products, bilinear forms, Gaussian integers, prime-number estimates, or operator norms and Neumann series.

## Pages, in reading order

- `exact-integer-multiplication`: Exact integer multiplication: Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
- `radix-digit-convolution`: Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
- `discrete-fourier-transform`: Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- `gaussian-resampling`: Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices wrap around modulo the sequence length.
- `transform-identity`: Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Turing machines and tapes
- `big-theta-big-omega-and-little-o-notation`: Big-Theta, big-Omega and little-o notation
- `logarithms`: Logarithms
- `floor-and-ceiling`: Floor and ceiling
- `mathematical-induction`: Mathematical induction
- `recurrence-relations`: Recurrence relations
- `geometric-series`: Geometric series
- `sets-intersections-and-indicator-vectors`: Sets, intersections and indicator vectors
- `permutations`: Permutations
- `lexicographic-order`: Lexicographic order
- `positional-radix-notation`: Positional (radix) notation
- `hamming-weight`: Hamming weight
- `two-s-complement-and-signed-binary`: Two's complement and signed binary
- `fixed-point-binary-numbers`: Fixed-point binary numbers
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `prime-numbers`: Prime numbers
- `binary-field-gf-2-and-xor`: Binary field GF(2) and XOR
- `roots-of-unity`: Roots of unity
- `polar-form-and-euler-s-formula`: Polar form and Euler's formula
- `vector-spaces-over-a-field`: Vector spaces over a field
- `matrices-rank-and-invertibility`: Matrices, rank and invertibility
- `gaussian-elimination-and-triangular-factorization`: Gaussian elimination and triangular factorization
- `eigenvalues-and-eigenvectors`: Eigenvalues and eigenvectors
- `newton-s-method`: Newton's method
- `stable-sorting-and-radix-sort`: Stable sorting and radix sort

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Previous plan (revise it: the pages have changed since)

```json
{
  "id": "S0",
  "intention": "show",
  "claim": "With both coordinate permutations kept in the formula, $P_sF_s = 2^{2\\alpha^2}B_0P_tF_tA$, and the retained source permutation cancels across a convolution.",
  "from": [
    "exact-integer-multiplication"
  ],
  "method": "keep the permutations in the Gaussian resampling identity, then cancel the source permutation through the convolution",
  "motivation": {
    "text": "Keeping the permutations in the formula lets the two sorts disappear instead of being executed as full passes over each coordinate.",
    "source": "explicit",
    "quote": {
      "source": "paper",
      "quote": "the source and target coordinate permutations in the transform identity, so they need not be"
    }
  },
  "adds": [
    {
      "symbol": "s",
      "name": "source axis length",
      "meaning": "The number of coordinates of the source transform axis, coprime to t.",
      "relation": "count"
    },
    {
      "symbol": "t",
      "name": "target axis length",
      "meaning": "The number of coordinates of the target transform axis, with s < t.",
      "relation": "count"
    },
    {
      "symbol": "\\alpha",
      "name": "Gaussian width parameter",
      "meaning": "The integer width parameter of the Gaussian weights, with 2 <= alpha < p.",
      "relation": "direct"
    }
  ],
  "page": "transform-identity",
  "children": [
    {
      "id": "S0.1",
      "intention": "show",
      "claim": "The one-dimensional Gaussian resampling identity $P_sF_s = 2^{2\\alpha^2}B_0P_tF_tA$ holds with contractions $A$ and $B_0$.",
      "from": [
        "discrete-fourier-transform",
        "roots-of-unity"
      ],
      "method": "resample Fourier transform through Gaussian weights onto the other length, invert the near-identity factor by a Neumann series, and absorb the normalizations",
      "motivation": {
        "text": "The source transform length and the target length are coprime, so the Fourier transform of one length must be moved onto the power-of-two frequencies of the other; Gaussian weights move between the two sets of frequencies.",
        "source": "explicit",
        "quote": {
          "source": "paper",
          "quote": "Gaussian resampling connects these two shapes."
        }
      },
      "adds": [
        {
          "symbol": "N",
          "name": "near-identity factor",
          "meaning": "The map $N=CTD$, which is the identity up to a Gaussian error of norm below one half.",
          "relation": "direct"
        },
        {
          "symbol": "C",
          "name": "coordinate selection",
          "meaning": "The map that selects the coordinates $q_j$ nearest to $tj/s$ from a vector of length $t$.",
          "relation": "direct"
        },
        {
          "symbol": "D",
          "name": "Gaussian phase",
          "meaning": "The diagonal map that multiplies coordinate $j$ by $e^{\\pi\\alpha^2\\beta_j^2}$ to cancel the Gaussian factor at the selected coordinate.",
          "relation": "direct"
        }
      ],
      "page": "gaussian-resampling",
      "children": [
        {
          "id": "S0.1.1",
          "intention": "infer",
          "claim": "$TP_sF_s = P_tF_tS$, the Gaussian resampling identity before normalization.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "TPs Fs = Pt Ft S,"
          }
        },
        {
          "id": "S0.1.2",
          "intention": "infer",
          "claim": "$\\|N-I\\|<1/2$, so $N$ is invertible.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series."
          }
        },
        {
          "id": "S0.1.3",
          "intention": "infer",
          "claim": "$DN^{-1}CP_tF_tS = P_sF_s$, using the left inverse of $CT$.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Applying this left inverse to the first identity in (34) gives DN −1 CPt Ft S = Ps Fs ."
          }
        },
        {
          "id": "S0.1.4",
          "intention": "infer",
          "claim": "$B_0P_tF_tA = 2^{-2\\alpha^2}P_sF_s$, after the normalizations of $A$, $B_0$ are absorbed.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "B0 Pt Ft A = 2−2α DN −1 CPt Ft S = 2−2α Ps Fs ,"
          }
        }
      ]
    },
    {
      "id": "S0.2",
      "intention": "show",
      "claim": "The retained source permutation cancels: $RF_s^{+}R(F_su\\cdot F_sv)=(u\\ast v)/S^2$ with $S=\\prod_i s_i$.",
      "from": [
        "radix-digit-convolution",
        "discrete-fourier-transform"
      ],
      "method": "commute the permutation through pointwise products, use that it is its own inverse against the opposite transform, then apply the normalized convolution rule",
      "motivation": {
        "text": "A coordinate permutation commutes with pointwise products, and the normalized convolution rule turns the product of transforms into a convolution.",
        "source": "recoverable"
      },
      "salient": "the permutation $R$ disappears exactly, leaving no residual reordering of the convolution",
      "children": [
        {
          "id": "S0.2.1",
          "intention": "infer",
          "claim": "$F_s^{+}R=R^{-1}F_s^{+}$, hence $RF_s^{+}R=F_s^{+}$.",
          "from": [
            "modular-arithmetic",
            "greatest-common-divisor-and-coprimality"
          ],
          "quote": {
            "source": "paper",
            "quote": "Each ti is a unit modulo si , so tensoring this identity gives Fs+ R = R−1 Fs+ and hence RFs+ R = Fs+ ."
          }
        },
        {
          "id": "S0.2.2",
          "intention": "infer",
          "claim": "$(RF_su)\\cdot(RF_sv)=R(F_su\\cdot F_sv)$, since a permutation commutes with pointwise products.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Also (RFs u) · (RFs v) = R(Fs u · Fs v), because a coordinate permutation commutes with pointwise"
          }
        },
        {
          "id": "S0.2.3",
          "intention": "infer",
          "claim": "$F_s(u\\ast v)=S(F_su)\\cdot(F_sv)$ and $F_s^{+}F_s=I/S$, the normalized convolution rule.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S."
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

Write the answer to `exegenius/tasks/0015-argument.answer.json`, then run `exegenius submit 0015-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
