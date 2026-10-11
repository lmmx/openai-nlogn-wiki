# exegenius task 0037-argument

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

## Pages, in reading order

- `exact-integer-multiplication`: Exact integer multiplication: Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
- `linear-map`: Linear map: A map between vectors of numbers that preserves addition and scalar multiplication, so that each output coordinate is a fixed weighted sum of the input coordinates.
- `discrete-fourier-transform`: Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices wrap around modulo the sequence length.
- `coprime-integers`: Coprime integers: Two integers are coprime when their greatest common divisor is 1; a family of integers is pairwise coprime when every two of them are coprime.
- `modular-arithmetic`: Modular arithmetic: Arithmetic in which values are reduced to their remainders on division by a fixed modulus q, so that index positions wrap around after q.
- `operator-norm`: Operator norm: For a linear map, the largest factor by which it stretches a vector measured in a fixed norm, taken over all vectors of norm at most one.
- `tensor-product`: Tensor product: The product of two linear maps or arrays acting on separate coordinates, so that applying the product acts on each coordinate in turn.
- `convolution-theorem`: Convolution theorem: The fact that the transform of a convolution of two sequences is the pointwise product of their transforms.
- `gaussian-function`: Gaussian function: The bell-shaped function x ↦ e^(−x²), or a scaled and shifted copy of it, used as a smooth weight that decays rapidly away from its centre.
- `transform`: Transform: A linear map from one array of values to another array of the same kind, each output being a fixed weighted sum of the inputs, such as a discrete Fourier transform.
- `axis-length`: Axis length: The number of positions along one coordinate axis of a multidimensional array; a multidimensional transform is applied along each axis in turn, with its own length.
- `radix-digit-convolution`: Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
- `gaussian-resampling`: Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- `transform-identity`: Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Turing machines and tapes

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Previous plan (revise it: the pages have changed since)

```json
{
  "id": "S0",
  "intention": "show",
  "claim": "The Gaussian resampling identity $RF_s=2^{2d\\alpha^2}B_0QF_tA$ holds with the permutations $R$ and $Q$ kept in the formula, and the source permutation $R$ cancels across a convolution: $(RF_s^+)((RF_su)\\cdot(RF_sv))=\\frac{u*v}{(\\prod_i s_i)^2}$.",
  "from": [],
  "method": "prove the one-dimensional identity with both permutations kept, lift it to a tensor product, then cancel the source permutation in a convolution",
  "motivation": {
    "text": "Retaining the two permutations in the formula avoids executing each of them as a separate full sort on every coordinate.",
    "source": "explicit",
    "quote": {
      "source": "paper",
      "quote": "Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly."
    }
  },
  "adds": [
    {
      "symbol": "d",
      "name": "axis count",
      "meaning": "the number of coordinate axes in the tensor product",
      "relation": "count"
    },
    {
      "symbol": "s",
      "name": "source length",
      "meaning": "the number of entries in a source transform line",
      "relation": "count"
    },
    {
      "symbol": "t",
      "name": "target length",
      "meaning": "the number of entries in a target transform line, larger than the source length",
      "relation": "count"
    },
    {
      "symbol": "\\alpha",
      "name": "Gaussian parameter",
      "meaning": "a fixed integer parameter that sets the width of the Gaussian weights",
      "relation": "direct"
    },
    {
      "symbol": "P_s",
      "name": "source permutation",
      "meaning": "the coordinate permutation of a source line that places entry t_j at position j",
      "relation": "direct"
    },
    {
      "symbol": "P_t",
      "name": "target permutation",
      "meaning": "the coordinate permutation of a target line that places entry -s k at position k",
      "relation": "direct"
    },
    {
      "symbol": "A",
      "name": "source contraction",
      "meaning": "the linear contraction from source lines to target lines",
      "relation": "direct"
    },
    {
      "symbol": "B_0",
      "name": "target contraction",
      "meaning": "the linear contraction from target lines back to source lines",
      "relation": "direct"
    },
    {
      "symbol": "R",
      "name": "source permutation product",
      "meaning": "the tensor product of the source permutations over all axes",
      "relation": "direct"
    },
    {
      "symbol": "Q",
      "name": "target permutation product",
      "meaning": "the tensor product of the target permutations over all axes",
      "relation": "direct"
    }
  ],
  "page": "transform-identity",
  "children": [
    {
      "id": "S0.1",
      "intention": "show",
      "claim": "For coprime $s<t$ with $\\theta=t/s-1$ large enough, $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$.",
      "from": [
        "operator-norm",
        "linear-map",
        "coprime-integers",
        "discrete-fourier-transform",
        "complex-numbers"
      ],
      "method": "factor the resampling through two Gaussian maps and a near-identity correction, invert the correction by a Neumann series, then normalize",
      "motivation": {
        "text": "The two Gaussian maps relate the two frequency grids, and the correction is close to the identity, so it is invertible and its inverse can be bounded.",
        "source": "recoverable"
      },
      "salient": "the constant $2^{2\\alpha^2}$ is uniform in $p$, $s$, $t$ and $\\alpha$",
      "adds": [
        {
          "symbol": "S",
          "name": "Gaussian source map",
          "meaning": "the Gaussian-weighted map from source lines to target lines",
          "relation": "direct"
        },
        {
          "symbol": "T",
          "name": "Gaussian target map",
          "meaning": "the second Gaussian-weighted map from source lines to target lines",
          "relation": "direct"
        },
        {
          "symbol": "N",
          "name": "near-identity correction",
          "meaning": "the composite CTD on source lines, within one half of the identity",
          "relation": "direct"
        },
        {
          "symbol": "C",
          "name": "coordinate selector",
          "meaning": "the map that selects the target coordinates nearest to t_j over s",
          "relation": "direct"
        },
        {
          "symbol": "D",
          "name": "diagonal factor",
          "meaning": "the diagonal map multiplying each source entry by a Gaussian phase correction",
          "relation": "direct"
        }
      ],
      "page": "gaussian-resampling",
      "children": [
        {
          "id": "S0.1.1",
          "intention": "infer",
          "claim": "$TP_sF_s=P_tF_tS$, the Gaussian identity relating the two resampled transforms.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "TPs Fs = Pt Ft S,"
          }
        },
        {
          "id": "S0.1.2",
          "intention": "infer",
          "claim": "$\\|N-I\\|<1/2$, so the correction $N$ is invertible by a Neumann series.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series."
          }
        },
        {
          "id": "S0.1.3",
          "intention": "infer",
          "claim": "$A=S/2$ and $B_0=2^{-(2\\alpha^2-2)}DN^{-1}C/2$ are set as contractions.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Now set A = S′ and B0 = D′ J′ C."
          }
        },
        {
          "id": "S0.1.4",
          "intention": "infer",
          "claim": "$DN^{-1}CP_tF_tS=P_sF_s$, the left inverse applied to the first identity.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Applying this left inverse to the first identity in (34) gives DN −1 CPt Ft S = Ps Fs"
          }
        },
        {
          "id": "S0.1.5",
          "intention": "infer",
          "claim": "$B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$, which is the one-dimensional identity.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "B0 Pt Ft A = 2−2α DN −1 CPt Ft S = 2−2α Ps Fs"
          }
        }
      ]
    },
    {
      "id": "S0.2",
      "intention": "infer",
      "claim": "$RF_s=2^{2d\\alpha^2}B_0QF_tA$: the one-dimensional identity tensors into the identity with permutations $R$ and $Q$ kept.",
      "from": [
        "tensor-product",
        "axis-length",
        "gaussian-resampling"
      ],
      "quote": {
        "source": "paper",
        "quote": "Tensoring (33) proves (35)."
      }
    },
    {
      "id": "S0.3",
      "intention": "show",
      "claim": "$(RF_s^+)((RF_su)\\cdot(RF_sv))=\\frac{u*v}{(\\prod_i s_i)^2}$, so the source permutation cancels across the convolution.",
      "from": [
        "exact-integer-multiplication",
        "radix-digit-convolution",
        "discrete-fourier-transform"
      ],
      "method": "commute the source permutation through the conjugate transform and the pointwise product, then apply the normalized convolution rule",
      "motivation": {
        "text": "A coordinate permutation commutes with pointwise products and with the conjugated transform, so it can be moved out of the product and cancelled.",
        "source": "recoverable"
      },
      "salient": "the source permutation $R$ drops out of the convolution identity",
      "children": [
        {
          "id": "S0.3.1",
          "intention": "infer",
          "claim": "$F_s^+R=R^{-1}F_s^+$, hence $RF_s^+R=F_s^+$.",
          "from": [
            "modular-arithmetic",
            "coprime-integers"
          ],
          "quote": {
            "source": "paper",
            "quote": "Each ti is a unit modulo si , so tensoring this identity gives Fs+ R = R−1 Fs+ and hence RFs+ R = Fs+ ."
          }
        },
        {
          "id": "S0.3.2",
          "intention": "infer",
          "claim": "$(RF_su)\\cdot(RF_sv)=R(F_su\\cdot F_sv)$, since a coordinate permutation commutes with pointwise products.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Also (RFs u) · (RFs v) = R(Fs u · Fs v), because a coordinate permutation commutes with pointwise"
          }
        },
        {
          "id": "S0.3.3",
          "intention": "infer",
          "claim": "$RF_s^+R(F_su\\cdot F_sv)=F_s^+(F_su\\cdot F_sv)$.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "RFs+ R(Fs u · Fs v) = Fs+ (Fs u · Fs v)."
          }
        },
        {
          "id": "S0.3.4",
          "intention": "infer",
          "claim": "$F_s^+(F_su\\cdot F_sv)=\\frac{u*v}{(\\prod_i s_i)^2}$, by the normalized convolution rule and $F_s^+F_s=I/\\prod_i s_i$.",
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

Write the answer to `exegenius/tasks/0037-argument.answer.json`, then run `exegenius submit 0037-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
