# exegenius task 0057-audit-packed-bit-addition

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
- Transform layout

## Symbols bound on earlier pages

- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $f$ (packed polynomial), bound on `signed-packing`: A polynomial in y with r integer coefficients, packed as the integer f(B).
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $\tau$ (width exponent), bound on `address-interchange`: A fixed number below one in the cost bound $O(V u^{\tau})$.
- $\oplus$ (bitwise XOR), bound on `address-interchange`: Bitwise exclusive or of two blocks of bits.
- $V$ (stored bit volume), bound on `address-shear`: The number of stored bits in the array.
- $E$ (fixed bilinear space), bound on `subspace-labels`: The fixed bilinear space that contains every label, with bilinear form $\langle\cdot,\cdot\rangle$.
- $V$ (head label), bound on `subspace-labels`: The label at the head of an edge, whose tail label is $U$.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $X$ (source bank), bound on `subset-intersection-network`: One of the two banks of values, with entries $x_a$, that the network exchanges.
- $T$ (neighbouring triple), bound on `subset-intersection-network`: A triple, here the triple whose indicator vector is $t_T$.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $W$ (wire count), bound on `rank-saving-recursion`: The number of wires in the network, which is also the number of roles among which the rows of an array are distributed.
- $V$ (data volume), bound on `rank-saving-recursion`: The number of stored data bits in the array that a call works on.
- $f$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the digits of the field being interchanged or the selected axes of a numerical layer.
- $L$ (lost dimension), bound on `rank-saving-recursion`: The total dimension lost along the decreasing edges of the network.
- $\tau$ (power-saving exponent), bound on `rank-saving-recursion`: The exponent of the power saving, the logarithm to base m of s/W.
- $X$ (bit-flip matrix), bound on `complex-phase-network`: The $2\times 2$ matrix that swaps the two coordinates of a vector.
- $V$ (head label), bound on `complex-phase-network`: The label at the head of an edge.
- $E$ (orthogonal residual), bound on `complex-phase-network`: The orthogonal residual of an edge, the part of $V$ orthogonal to $U$.
- $i$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, from 0 to r-1.
- $f$ (input record), bound on `polynomial-ring-convolution`: The first of the two records whose normalized product is taken, a polynomial in y with complex coefficients of degree less than r.
- $K$ (chunk width), bound on `simultaneous-butterfly-layer`: The number of address bits in each chunk.
- $\rho$ (selected offset), bound on `simultaneous-butterfly-layer`: The position, counted from the least significant end, of the selected bit within each chunk.
- $W$ (wire count), bound on `guard-width-bound`: The number of wires in the complex network.
- $K$ (chunk width), bound on `transform-layout`: The number of address bits in each consecutive chunk, a count of bits.
- $\rho$ (selected offset), bound on `transform-layout`: The position, counted from the least significant bit of a chunk, of the bit selected in every chunk.

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

## Page to audit (`packed-bit-addition`)

````markdown
# Packed selected-bit addition

Packed selected-bit addition supplies the binary basis changes of the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md). The procedure performs this addition for every selected position at once, while a third chunk is restored. Doing the selected bits one pass at a time would multiply the cost of the layer by their number, so packing them is what keeps each layer inside the cost table of the theorem.

Let $X$ and $W$ be two disjoint address chunks, that is, contiguous groups of address bits, of equal width $L$, and let $T$ be a third chunk, whose initial value is arbitrary. Each chunk is cut into $f$ segments of $K$ bits, so $L = fK$. Let $\rho$ be the position of the first selected bit, counting positions from $0$ at the least significant end. The selected bit of segment $i$ is its lowest bit, at position $\rho + iK$ for $0 \le i < f$. The other $K-1$ bits of a segment form its guard, an integer between $0$ and $2^{K-1}-1$.

The row addition is $W \leftarrow W \oplus X$ on the selected bits: for each segment index, the selected bit of $W$ is XORed with the selected bit of $X$ in the same segment. The method treats each segment as an integer. A controlled cyclic shift of the target chunk by $\pm 2^{\rho+iK}$ adds $\pm 1$ to the value of segment $i$, with the sign chosen so that the lowest bit flips. For example, with $K = 3$, the segment value $3 = 011_2$ becomes $2 = 010_2$ under $-1$, and the segment value $4 = 100_2$ becomes $5 = 101_2$ under $+1$. In both cases the guard is unchanged, so the step flips the selected bit and nothing else. The step fires only when the control bit is $1$, so the selected bit is XORed exactly when the control is $1$. Packed selected-bit addition shifts its target chunks by controlled offsets, each applied as an [Address shear](address-shear.md). The paper realizes the flip with eight such controlled updates, which change the target and scratch chunks and return the scratch chunk to its initial value.

Before any update, the target chunk is moved beside its controls. Packed selected-bit addition exchanges its chunks by the [Address-field interchange](address-interchange.md) whenever a target chunk must be moved beside its controls.

All segments are updated in parallel. This is correct when no segment value leaves its own range, because then no $\pm 1$ step carries into a neighbouring segment or borrows from it. The top selected bit is left out of this stage: temporarily, and the stage acts on the first $f-1$ selected bits as $f-1$ independent segment additions. The top bit is XORed in afterwards by a two-bit permutation of the two chunks.

Each guard must lie between $10$ and $2^{K-1}-11$, so that an update of size at most eight stays inside its own segment. Let $E$ be the set of addresses for which some guard lies outside the range from $10$ to $2^{K-1}-11$. Each guard takes each of its $2^{K-1}$ values equally often across the address range, so one guard is excluded from a fraction $20/2^{K-1}$ of addresses. The first $f-1$ segments of each of the two chunks give $2(f-1)$ guards. A union bound over them shows that $E$ contains at most a fraction $80(f-1)/2^K$ of all addresses.

On $E$ the parallel updates may be wrong, so the procedure corrects them. It extracts exactly the records whose addresses lie in $E$, computes for each its destination address, and reinserts it at its destination rank after a stable radix sort of the extracted records. over all payloads.

The movement costs $O(V(L^\tau+1))$, where $\tau$ is the fixed exponent of the [Address-field interchange](address-interchange.md) and $V$ is the number of bits in the stream. in the paper's accounting, and the correction adds a term that is small under the parameter conditions of the family. Each binary basis change in a transform round is paid for at this cost, which is how the cost table keeps every term within the bound of the theorem.
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

Write the answer to `exegenius/tasks/0057-audit-packed-bit-addition.answer.json`, then run `exegenius submit 0057-audit-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
