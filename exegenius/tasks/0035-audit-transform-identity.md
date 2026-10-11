# exegenius task 0035-audit-transform-identity

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows the concepts listed as known, and everything the reader profile covers: what anyone with that background has been taught, whether or not the profile names it (a profile of undergraduate computer science covers logarithms and proof by induction without naming them). Anything outside that, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source, which the reader can consult: it is followable by reference, so do not report it as a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, Fourier transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Axis length
- Coprime integers (also: coprime)
- Linear map
- Modular arithmetic (also: modular indices)
- Operator norm (also: norm of a linear map)
- Tensor product

## Symbols bound on earlier pages

- $u$ (input vector), bound on `linear-map`: The vector of m complex numbers that a linear map takes as input.
- $v$ (output vector), bound on `linear-map`: The vector of k complex numbers that a linear map returns.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ values.
- $v$ (second vector), bound on `discrete-fourier-transform`: A second vector of $q$ values, for forming a convolution.
- $B$ (radix), bound on `radix-digit-convolution`: The base in which each integer is written, equal to 2^k.
- $d$ (digit count), bound on `radix-digit-convolution`: The number of radix digits of each input.
- $u$ (test vector), bound on `operator-norm`: A vector whose length matches the input length of the map, over which the supremum is taken.
- $s$ (source length), bound on `gaussian-resampling`: The number of coordinates of the source vector, a count.
- $t$ (target length), bound on `gaussian-resampling`: The number of coordinates of the target vector, a count.
- $\theta$ (relative excess), bound on `gaussian-resampling`: The relative excess $t/s-1$ of the target length over the source length.
- $u$ (source vector), bound on `gaussian-resampling`: A vector of $s$ coordinates.
- $v$ (target vector), bound on `gaussian-resampling`: A vector of $t$ coordinates.
- $P_s$ (source permutation), bound on `gaussian-resampling`: The coordinate permutation on length-$s$ vectors with $(P_s u)_j = u_{tj}$.
- $P_t$ (target permutation), bound on `gaussian-resampling`: The coordinate permutation on length-$t$ vectors with $(P_t v)_k = v_{-sk}$.
- $\alpha$ (Gaussian width), bound on `gaussian-resampling`: An integer at least 2 setting the width of the Gaussian weights.
- $A$ (first contraction), bound on `gaussian-resampling`: The contraction $S/2$, from length-$s$ to length-$t$ vectors.
- $B_0$ (second contraction), bound on `gaussian-resampling`: The contraction $2^{-(2\alpha^2-2)}DN^{-1}C/2$, from length-$t$ to length-$s$ vectors.
- $\otimes$ (tensor product), bound on `tensor-product`: The operator that combines $L$ and $M$ into a linear map on arrays with $s$ rows and $t$ columns.
- $u$ (array), bound on `tensor-product`: An array with $s$ rows and $t$ columns, whose entries are $u_{hg}$.
- $i$ (output row index), bound on `tensor-product`: The index of an output row, which is the first coordinate of an output position.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Axis length](axis-length.md)
- [Linear map](linear-map.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Coprime integers](coprime-integers.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor product](tensor-product.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`transform-identity`)

````markdown
# Transform identity with retained permutations

Transform identity with retained permutations is the form of the Gaussian resampling identity in which the source and target coordinate permutations stay in the formula, so that they cancel across a convolution instead of being executed as sorts.

The one-dimensional identity is derived from [Gaussian resampling](gaussian-resampling.md) and holds for [coprime](coprime-integers.md) $s<t$ with $\theta=t/s-1$ large enough: $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with contractions $A$ and $B_0$.

Here $d$ is the number of coordinates, not the digit count, and $s_i$ is the number of entries along coordinate $i$. Here $R$ permutes the source coordinates, and $Q$ permutes the target coordinates. The identity is lifted to $d$ coordinates by a [tensor product](tensor-product.md) of the $d$ one-dimensional identities. Since $(X_1\otimes\cdots\otimes X_d)(Y_1\otimes\cdots\otimes Y_d)=(X_1Y_1)\otimes\cdots\otimes(X_dY_d)$, multiplying the identities gives $RF_s$ on the left and $B_0QF_tA$ on the right, where $R=\bigotimes_i P_{s_i}$ and $Q=\bigotimes_i P_{t_i}$. Each coordinate contributes a factor $2^{2\alpha^2}$, so the factors multiply to $2^{2d\alpha^2}$:
$$RF_s=2^{2d\alpha^2}B_0QF_tA.$$

Let $R^+$ be the inverse of $R$, so $RF_s^+=F_s^+R^+$ with $F_s^+$ the opposite transform. Here $u$ is the first input array, with one entry for each point of the source grid of shape $s_1\times\cdots\times s_d$, and $v$ is the second. A permutation commutes with the pointwise product $\cdot$, so $(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$. Applying $RF_s^+=F_s^+R^+$ and $R^+R$ = identity removes $R$, leaving $F_s^+\big((F_su)\cdot(F_sv)\big)$. By the convolution theorem, the transform of $u*v$ is a pointwise product of transforms, so this equals $u*v$ up to scale:
$$(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}.$$
The source permutation $R$ is never executed. Sorting is avoided because the usual implementation sorts twice on each coordinate, while this formula is computed directly. (cited).
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0035-audit-transform-identity.answer.json`, then run `exegenius submit 0035-audit-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
