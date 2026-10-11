# exegenius task 0034-audit-tensor-product

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

## Symbols bound on earlier pages

- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $m$ (input length), bound on `linear-map`: The number of input coordinates of a linear map.
- $L$ (linear map), bound on `linear-map`: The rule sending a vector of m complex numbers to a vector of k complex numbers.
- $u$ (input vector), bound on `linear-map`: The vector of m complex numbers that a linear map takes as input.
- $m$ (exponent), bound on `discrete-fourier-transform`: An integer exponent of $\omega$, with $0<m<q$.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ values.
- $a$ (digit list of x), bound on `radix-digit-convolution`: The coefficient list of x, the vector of its d radix digits a_0 through a_{d-1}.
- $L$ (linear map), bound on `operator-norm`: The linear map whose stretching of vectors the operator norm measures.
- $u$ (test vector), bound on `operator-norm`: A vector whose length matches the input length of the map, over which the supremum is taken.
- $s$ (source length), bound on `gaussian-resampling`: The number of coordinates of the source vector, a count.
- $t$ (target length), bound on `gaussian-resampling`: The number of coordinates of the target vector, a count.
- $u$ (source vector), bound on `gaussian-resampling`: A vector of $s$ coordinates.
- $p$ (precision), bound on `gaussian-resampling`: The integer precision of the numerical approximation.

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

## Page to audit (`tensor-product`)

````markdown
# Tensor product

A tensor product is built from one [Linear map](linear-map.md) for each coordinate, and it lets a map on a multidimensional array act on each coordinate in turn. The argument uses it to pass from one-dimensional identities to identities for arrays, with their permutations kept.

Here $i$ and $m$ index the output row and column, and $h$ and $g$ index the input row and column. Let $L$ be a linear map on vectors of length $s$ and $M$ a linear map on vectors of length $t$, with entries $L_{ih}$ (row $i$, column $h$) and $M_{mg}$ (row $m$, column $g$). The tensor product $L\otimes M$ is the linear map on arrays $u$ with $s$ rows and $t$ columns, entries $u_{hg}$, whose entry at position $(i,m)$ is

$$(L\otimes M)(u)_{im}=\sum_{h}\sum_{g} L_{ih}\,M_{mg}\,u_{hg}.$$

Applying $L\otimes M$ is the same as applying $M$ to each row of $u$ and then $L$ to each column. (cited)

Take $s=t=2$, $L=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $M=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, and let $u$ have $u_{00}=1$ and all other entries $0$. Only the terms with $h=g=0$ survive, so $(L\otimes M)(u)_{im}=L_{i0}M_{m0}$. This is $1$ at $(i,m)=(0,0)$ and at $(1,0)$, and $0$ elsewhere.
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

Write the answer to `exegenius/tasks/0034-audit-tensor-product.answer.json`, then run `exegenius submit 0034-audit-tensor-product` in the project directory. If submit rejects the answer, fix the answer and submit again.
