# exegenius task 0056-audit-transform-layout

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
- Guard-width bound

## Symbols bound on earlier pages

- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $H$ (address field H), bound on `address-shear`: The first of the two address fields, a vector of m fields, which the shear updates.
- $D$ (address field D), bound on `address-shear`: The second of the two address fields, a vector of m fields, which the shear reads and leaves unchanged.
- $L$ (lost dimension), bound on `rank-saving-recursion`: The total dimension lost along the decreasing edges of the network.
- $H$ (Hadamard matrix), bound on `complex-phase-network`: The normalized $2\times 2$ Hadamard matrix.
- $v$ (residual basis vector), bound on `complex-phase-network`: A vector of the residual basis $B$.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ complex numbers, the input to the transform.
- $u$ (pair value (first)), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair that the two-point map takes as input.
- $v$ (pair value (second)), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair that the two-point map takes as input.
- $H_0$ (two-point map), bound on `simultaneous-butterfly-layer`: The map sending a pair of values to their half-sum and half-difference.
- $D$ (axis count), bound on `simultaneous-butterfly-layer`: The number of axes on which the layer acts, which is also the number of address chunks it transforms.
- $K$ (chunk width), bound on `simultaneous-butterfly-layer`: The number of address bits in each chunk.
- $\rho$ (selected offset), bound on `simultaneous-butterfly-layer`: The position, counted from the least significant end, of the selected bit within each chunk.
- $D$ (selected axes), bound on `guard-width-bound`: The number of selected axes in one layer.
- $u$ (first coefficient), bound on `guard-width-bound`: The first of the two coefficients that the two-point map combines.
- $v$ (second coefficient), bound on `guard-width-bound`: The second of the two coefficients that the two-point map combines.

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

## Page to audit (`transform-layout`)

````markdown
# Transform layout

Transform layout is a permutation of address bits that puts the selected bits of several axes at one common offset, in consecutive chunks, so that a single pass can apply a whole transform round. It is the step that lets the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) act on a multi-axis transform, and its cost is part of the bound for [Integer multiplication below n log n](main-theorem.md).

Each entry of a multidimensional array sits at a binary address, and the bits of that address are the *address bits*. Each coordinate of the array is an *axis*. A *transform round* applies one two-point butterfly on each participating axis. The butterfly is $H_0(u,v) = ((u+v)/2, (u-v)/2)$ on a pair of entries that differ in one selected bit.

The shape a round needs is fixed by two numbers. Here $K$ is the number of address bits in each chunk and $D$ is the number of participating axes, each of which contributes one chunk of $K$ consecutive address bits. Here $\rho$ is that common offset, the position of the selected bit within each chunk, counted from the least significant bit.

The simultaneous butterfly layer is defined on exactly this shape. It applies $H_0$ to the selected bit of every chunk in one evaluation, and

Without this shape, a round would need one pass per axis: The layout moves the selected bits of all participating axes into the shape above, so that one pass of the layer serves the whole round. The layout prepares the input for each [simultaneous butterfly layer](simultaneous-butterfly-layer.md) of a transform round.

The layout is an explicit permutation $L$ of record addresses. The coefficients of each record stay together as a contiguous block of its address, the record's

The layout is built from [address-field interchange](address-interchange.md) moves of whole chunks, together with single-bit moves. The construction has two phases. In the first, so the bits that must be selected are gathered into a prefix. In the second, the chunks outside that prefix are reordered: Their order is changed so that the chunks of all $D$ axes at the same chunk index sit next to each other, and the layer is applied to each such group of $D$ consecutive chunks.

Here is a small example of the target shape, not of the procedure's own steps. Take $K = 2$, $D = 2$, $\rho = 1$, and 6-bit addresses with bit positions $0$ to $5$, counted from the least significant bit. The layer then needs the two selected bits at positions $1$ and $3$, which are the second bits of the chunks at positions $\{0,1\}$ and $\{2,3\}$. If the selected bits start at positions $0$ and $5$, exchanging positions $0$ and $1$ and exchanging positions $3$ and $5$ puts them at positions $1$ and $3$.

The layout is charged in full. The forward transform may keep its output order: it can The frequency entries therefore stay in layout order through the pointwise product, and the opposite transform reads them in that order. The layout is applied within each round of the [synthetic polynomial transforms](synthetic-transforms.md).
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

Write the answer to `exegenius/tasks/0056-audit-transform-layout.answer.json`, then run `exegenius submit 0056-audit-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.
