# exegenius task 0045-audit-subspace-labels

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: a term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Signed coefficient packing (also: Kronecker substitution)
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange)
- Address shear
- Gaussian dyadics

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $y$ (second input string), bound on `exact-integer-multiplication`: A binary string of length n, the second input to the product.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $y$ (second input), bound on `radix-digit-convolution`: The second input, a binary string of $n$ bits.
- $y$ (indeterminate), bound on `signed-packing`: The indeterminate of the polynomial ring, the variable in which the packed polynomials are written.
- $f$ (packed polynomial), bound on `signed-packing`: A polynomial in y with r integer coefficients, packed as the integer f(B).
- $h$ (product polynomial), bound on `signed-packing`: The ordinary polynomial product fg, whose coefficients are read back from the integer product.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $y$ (second field), bound on `address-interchange`: The value of the second field, a block of bits at matching positions.
- $\oplus$ (bitwise XOR), bound on `address-interchange`: Bitwise exclusive or of two blocks of bits.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $V$ (stored bit volume), bound on `address-shear`: The number of stored bits in the array.
- $h$ (value of H), bound on `address-shear`: The current value of H when m = 1.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`subspace-labels`)

````markdown
# Subspace labels

A subspace label is a nondegenerate subspace of a fixed bilinear space, attached to each gate and terminal of a network. Labels fix how much work each change of representation costs, and the subset-intersection network and the complex phase network that follow are built from them.

Let $E$ denote the fixed bilinear space, with bilinear form $\langle\cdot,\cdot\rangle$, and let its dimension be $m$, the number of coordinates of a vector of $E$. Assume $E$ is nondegenerate. A label is a nondegenerate subspace $U$ of $E$. A subspace $W$ is nondegenerate when no nonzero vector of $W$ is orthogonal to every vector of $W$. The orthogonal complement $W^\perp$ is the set of vectors of $E$ orthogonal to every vector of $W$.

The construction attaches to its gates. The labels are chosen, so the page's question is which subspaces make a change of frame cheap.

Subspace labels are built on [linear networks and frames](linear-network-frames.md). A vertex whose label is $U$ has frame $C_U$, the operator that turns the logical array into the stored array there. In the complex network, each label $U$ gives a frame $C_U$ whose entries lie in [Gaussian dyadics](gaussian-dyadics.md). Each entry of $C_U$ and its inverse is a Gaussian integer divided by $2^m$.

On an edge, $U$ and $V$ are its tail and head labels.. Say $V \subseteq U$. The orthogonal residual of the edge is $U\cap V^\perp$,. Since $V$ is nondegenerate, $E = V \oplus V^\perp$, and intersecting with $U \supseteq V$ gives $U = V \oplus (U\cap V^\perp)$. So the residual has dimension $\dim U - \dim V$, the absolute change in label dimension. That dimension counts. edges small.

Across the edge from $U$ to $V$, the frame changes by $C_V C_U^{-1}$. The source writes this change as a product of translation kernels: vector of an orthonormal basis of the residual. Here $(X_v f)(x) = f(x+v)$.

Let $h$ be the size of a ground set, and let $J$ be the all-one $h\times h$ matrix. For the bit construction, $\langle x,y\rangle = x^{\top}(I-J/9)y$ on $\mathbb{Q}^h$. A triple $T$ is a three-element subset of the ground set, with indicator vector $t_T\in\mathbb{Q}^h$. Then $\langle t_T,t_T\rangle = 3 - 9/9 = 2$, so the line spanned by $t_T$ is nondegenerate. For another triple $S$, $\langle t_S,t_T\rangle = |S\cap T| - 1$, so triples sharing exactly one element give orthogonal lines. field.
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

Write the answer to `exegenius/tasks/0045-audit-subspace-labels.answer.json`, then run `exegenius submit 0045-audit-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.
