# exegenius task 0047-audit-rank-saving-recursion

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
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Gaussian dyadics

## Symbols bound on earlier pages

- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $N$ (input bit length), bound on `established-multiplier`: The number of bits in each of the two binary inputs of the multiplier.
- $f$ (packed polynomial), bound on `signed-packing`: A polynomial in y with r integer coefficients, packed as the integer f(B).
- $g$ (second packed polynomial), bound on `signed-packing`: A second polynomial in y with r integer coefficients, multiplied with f by one integer product.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $\tau$ (width exponent), bound on `address-interchange`: A fixed number below one in the cost bound $O(V u^{\tau})$.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $V$ (stored bit volume), bound on `address-shear`: The number of stored bits in the array.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $V$ (head label), bound on `subspace-labels`: The label at the head of an edge, whose tail label is $U$.

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

## Page to audit (`rank-saving-recursion`)

````markdown
# Rank-saving recursion

Rank-saving recursion is a recursive scheme in which each call splits into several smaller calls, each on a stream holding a fixed fraction of the data, so that the cost per unit of data grows by a strictly smaller factor at each level. It is the step that gives the paper's power saving in the logarithmic factor, and the later estimates of [Integer multiplication below n log n](main-theorem.md) keep it.

Each wire of the network has a fixed place in the network, called its role, and carries a label, a subspace of a fixed ambient space. Let $m$ be the dimension of the ambient label space, a fixed number. Let $W$ be the number of wires in the network, which is also the number of roles among which the rows of the array are distributed. Let $V$ be the number of stored data bits in the array that the call works on. Let $f$ be the parameter of the call, the number of digits in the address field being interchanged, or the number of selected axes in a numerical layer. Let $s$ be the total number of smaller calls that one call makes.

Each call splits into smaller calls to the [address-field interchange](address-interchange.md), each on one role stream of $V/W$ bits. The rows are split into role streams by, so every stream has the same size, and a call at parameter $mf$ therefore reduces to calls at parameter $f$ on streams of volume $V/W$.

Why $s < Wm$. Rank-saving recursion counts its smaller calls on the wires of the [subset-intersection network](subset-intersection-network.md)., so the number of smaller calls is governed by the dimension changes of the labels along the edges. Let $N$ be the sum of the dimensions of the labels at the sources, and let $L$ be the total dimension lost along decreasing edges, where an edge decreases when its label loses dimension. Summing the absolute dimension changes over all edges gives $Wm - 2N + 2L$, since the signed sum plus twice the lost dimension. Depending on the construction, $s$ equals $Wm - N + 2L$ or $Wm - 2N + 2L$, and both are at most $Wm - N + 2L$. The paper shows that, so $2L < N$ and hence $s < Wm$. This is the key inequality:.

Why this gives a power saving. Let $g(f)$ be the cost of a call at parameter $f$ divided by its volume. A call at parameter $mf$ on volume $V$ makes $s$ calls at parameter $f$, each on volume $V/W$, plus work linear in $V$. Ignoring the linear work at each level, $g(mf) \approx (s/W)\, g(f)$. Set $\tau = \log_m(s/W)$, the power-saving exponent. Because $s/W < m$, we have $\tau < 1$, and iterating the relation gives $g(f) \approx f^{\tau}$. The cost of a call is therefore about $V f^{\tau}$, a power of $f$ with exponent below one. If instead $s/W$ equaled $m$, the exponent would be exactly one and no saving would occur.

As a toy example, not the paper's values, take $W = 4$, $s = 6$ and $m = 2$. Then $s < Wm$ because $6 < 8$, and each doubling of the parameter multiplies $g$ by $s/W = 1.5$. So $\tau = \log_2 1.5 \approx 0.585$. With $s = 8$ instead, $s/W = m$, $\tau = 1$, and the saving disappears.

The two steps of the argument are therefore $s < Wm$, from the count above, and then $s/W < m$, from dividing by $W$. The second step gives the power saving.
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

Write the answer to `exegenius/tasks/0047-audit-rank-saving-recursion.answer.json`, then run `exegenius submit 0047-audit-rank-saving-recursion` in the project directory. If submit rejects the answer, fix the answer and submit again.
