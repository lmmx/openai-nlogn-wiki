# exegenius task 0054-audit-simultaneous-butterfly-layer

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

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $a$ (Gaussian integer numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $r$ (coefficient count), bound on `signed-packing`: The number of coefficients of each polynomial being packed.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so every coefficient has magnitude at most 2^p.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $H$ (address field H), bound on `address-shear`: The first of the two address fields, a vector of m fields, which the shear updates.
- $D$ (address field D), bound on `address-shear`: The second of the two address fields, a vector of m fields, which the shear reads and leaves unchanged.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $a$ (bank index), bound on `subset-intersection-network`: An index $a=(a_1,a_2,a_3)$ of one entry of a bank, a triple of triples.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $m$ (label dimension), bound on `rank-saving-recursion`: The dimension of the fixed ambient space in which the labels are subspaces.
- $H$ (Hadamard matrix), bound on `complex-phase-network`: The normalized $2\times 2$ Hadamard matrix.
- $a$ (kernel coefficient a), bound on `complex-phase-network`: The constant $(1+i)/2$ in the kernel $C = aI + bX$.
- $m$ (address length), bound on `complex-phase-network`: The number of coordinates of a binary address, so that $\mathbb{F}_2^m$ is the address space.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $v$ (residual basis vector), bound on `complex-phase-network`: A vector of the residual basis $B$.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ complex numbers, the input to the transform.
- $t$ (resampled length), bound on `gaussian-resampling`: the power-of-two number of entries in the resampled vector, greater than s.
- $p$ (precision), bound on `gaussian-resampling`: a positive integer precision parameter of the approximations.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $i$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, from 0 to r-1.
- $a$ (shift amount), bound on `synthetic-transforms`: The number of places a signed shift moves each coefficient, an integer with 0 \le a < 2r.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing 2r.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $p$ (fractional bits), bound on `polynomial-ring-convolution`: The number of fractional bits of each coefficient, so that every real and imaginary coefficient part of a record is a multiple of 2^{-p}.
- $a$ (real numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the real part of f after scaling by 2^{-p}.

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

## Page to audit (`simultaneous-butterfly-layer`)

````markdown
# Simultaneous butterfly layer

A simultaneous butterfly layer applies the two-point map to several selected address bits at once, as one tensor product, and computes it exactly in a single pass over the array. The synthetic transforms need this step to run their butterfly rounds on all participating axes together; the transform layout and packed selected-bit addition pages build on it.

Here $u$ and $v$ are the two values of a pair. Let $H_0(u,v) = ((u+v)/2, (u-v)/2)$ be the two-point map. In matrix form, $H_0 = \frac{1}{2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$. The layer applies the length-two case of the [discrete Fourier transform](discrete-fourier-transform.md), $H_0$, to each selected bit.

Let $D$ be the number of axes on which the layer acts, one axis per chunk, where a chunk is a run of consecutive address bits. Let $K$ be the number of bits in each chunk. In every chunk the layer selects one bit, at a common offset. Let $\rho$ be the offset of the selected bit within each chunk, counted from the least significant end, with $0 \le \rho < K$. The layer applies $H_0$ to each of the $D$ selected bits independently, which is the tensor product of $H_0$ over those bits. It acts on each stored coefficient of each record and leaves every other address bit and field unchanged.

Take $D=2$, $K=1$ and $\rho=0$, so the two selected bits are the two bits of a 2-bit address, with the first digit belonging to the first axis. Let the four values $1$, $2$, $3$, $4$ sit at addresses $00$, $01$, $10$, $11$. The layer returns $2.5$, $-0.5$, $-1$, $0$ at those addresses. For instance, the value at $00$ is $(1+2+3+4)/4 = 2.5$, and the value at $10$ is $(1+2-3-4)/4 = -1$. Each output is computed from all four inputs in one step rather than from one axis at a time.

The sources call this step. Applied one axis at a time, the layer would be $D$ separate butterfly factors, and the sources note that. A whole-array pass is one scan that reads and rewrites every stored record. Doing all $D$ axes in one tape procedure avoids those scans.

The method rests on the algebra of the phase frames. The layer expresses its phase frames through the [complex phase network](complex-phase-network.md). The layer rests on [Gaussian dyadics](gaussian-dyadics.md), since its phase identities use only Gaussian dyadic coefficients. The layer moves its address chunks by [address-field interchange](address-interchange.md) to implement its binary changes of basis.

The procedure evaluates the whole layer exactly and truncates only once, at the end:
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

Write the answer to `exegenius/tasks/0054-audit-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0054-audit-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
