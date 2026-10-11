# exegenius task 0058-audit-cyclic-convolution

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
- Discrete Fourier transform (also: normalized Fourier transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed coefficient packing (also: Kronecker substitution)
- Convolution over the polynomial ring
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $j$ (coefficient position), bound on `radix-digit-convolution`: The position of a product coefficient, running from $0$ to $2q-2$.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: A non-negative integer, so that $2^k$ is the denominator.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $j$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from 0 to r-1.
- $f$ (packed polynomial), bound on `signed-packing`: A polynomial in y with r integer coefficients, packed as the integer f(B).
- $g$ (second packed polynomial), bound on `signed-packing`: A second polynomial in y with r integer coefficients, multiplied with f by one integer product.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $s$ (smaller call count), bound on `rank-saving-recursion`: The number of smaller calls that one call makes.
- $f$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the digits of the field being interchanged or the selected axes of a numerical layer.
- $g$ (normalized cost), bound on `rank-saving-recursion`: The function giving the cost of a call at parameter f divided by its volume.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $j$ (input index), bound on `discrete-fourier-transform`: An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: An index of the output coordinates, running from 0 to q-1.
- $s$ (source length), bound on `gaussian-resampling`: the number of entries in the source vector, which is the length of the transform being replaced.
- $j$ (output index), bound on `synthetic-transforms`: The index of an entry of the transform, from 0 to t-1.
- $k$ (input index), bound on `synthetic-transforms`: The index of an entry of the input, from 0 to t-1.
- $s$ (shift amount), bound on `polynomial-ring-mod-yr-plus-1`: The number of positions by which the coefficient list moves under multiplication by y^s, with 0 <= s < r.
- $f$ (input record), bound on `polynomial-ring-convolution`: The first of the two records whose normalized product is taken, a polynomial in y with complex coefficients of degree less than r.
- $g$ (input record), bound on `polynomial-ring-convolution`: The second of the two records whose normalized product is taken, a polynomial in y with complex coefficients of degree less than r.
- $s$ (smaller-call count), bound on `guard-width-bound`: The total number of smaller calls made by the network.
- $f$ (segments per chunk), bound on `packed-bit-addition`: The number of $K$-bit segments into which each chunk is cut, so that each segment holds one selected bit.

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

## Page to audit (`cyclic-convolution`)

````markdown
# Cyclic convolution

Cyclic convolution is the product of two sequences of the same length in which an index that runs past the end wraps around to the start. The paper needs it because its coefficient layout and its middle transform both become cyclic convolutions, which is how the multiplication algorithm of [Integer multiplication below n log n](main-theorem.md) reduces to a product it can compute.

Let $s$ be the number of entries in each sequence. Let $f = (f_0, \dots, f_{s-1})$ and $g = (g_0, \dots, g_{s-1})$ be two sequences of the same length $s$. Indices are read modulo $s$, so $g_{-1}$ means $g_{s-1}$. Here $k$ is an output position, and $j$ runs over the entries of $f$. The cyclic convolution $f \ast g$ is the sequence with entries

$$(f \ast g)_k = \sum_{j=0}^{s-1} f_j \, g_{(k-j) \bmod s}, \qquad 0 \le k < s.$$

Each product $f_j g_l$ lands at output position $(j+l) \bmod s$. A product whose index sum reaches $s$ wraps back to the start instead of extending the sequence. This differs from ordinary (linear) convolution, whose output has length $2s-1$.

Identify $f$ with the polynomial $f(x) = \sum_{j=0}^{s-1} f_j x^j$, where $x$ is a formal variable. The entries of $f \ast g$ are then the coefficients of $f(x)g(x)$ reduced modulo $x^s - 1$, because $x^s = 1$ in that quotient. This is the reason the operation is called cyclic: multiplying by $x$ rotates the entries of a sequence by one position.

Take $s = 4$, $f = (1, 2, 3, 4)$ and $g = (1, 1, 0, 0)$. The ordinary product of the two polynomials is $(1, 3, 5, 7, 4)$, which has length $5$. Reducing modulo $x^4 - 1$ sends the last entry $4$ to position $0$, so $f \ast g = (1+4, 3, 5, 7) = (5, 3, 5, 7)$. The same result follows from the formula: $(f \ast g)_0 = f_0 g_0 + f_3 g_1 = 1 + 4 = 5$.

The paper uses this operation on the product of several coordinate groups. Agarwal and Cooley's split is the model:. The map $\Phi$ of the paper's Section 9.3 takes the cyclic convolution on one coordinate to a multidimensional one, and the paper states that convolution. The paper also states that, which is how the middle transform becomes a cyclic convolution.
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

Write the answer to `exegenius/tasks/0058-audit-cyclic-convolution.answer.json`, then run `exegenius submit 0058-audit-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
