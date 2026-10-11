# exegenius task 0055-audit-guard-width-bound

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

## Symbols bound on earlier pages

- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so every coefficient has magnitude at most 2^p.
- $B$ (block base), bound on `signed-packing`: The base 2^{4p} of the integer encoding, one block of 4p bits per coefficient.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $D$ (address field D), bound on `address-shear`: The second of the two address fields, a vector of m fields, which the shear reads and leaves unchanged.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $d$ (value of D), bound on `address-shear`: The current value of D when m = 1.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $s$ (smaller call count), bound on `rank-saving-recursion`: The number of smaller calls that one call makes.
- $W$ (wire count), bound on `rank-saving-recursion`: The number of wires in the network, which is also the number of roles among which the rows of an array are distributed.
- $m$ (label dimension), bound on `rank-saving-recursion`: The dimension of the fixed ambient space in which the labels are subspaces.
- $C$ (two-point kernel), bound on `complex-phase-network`: The two-point kernel $H\,\mathrm{diag}(1, i)\,H$, which equals $aI + bX$.
- $m$ (address length), bound on `complex-phase-network`: The number of coordinates of a binary address, so that $\mathbb{F}_2^m$ is the address space.
- $B$ (residual basis), bound on `complex-phase-network`: An orthonormal basis of the residual $E$ of an edge.
- $v$ (residual basis vector), bound on `complex-phase-network`: A vector of the residual basis $B$.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ complex numbers, the input to the transform.
- $s$ (source length), bound on `gaussian-resampling`: the number of entries in the source vector, which is the length of the transform being replaced.
- $p$ (precision), bound on `gaussian-resampling`: a positive integer precision parameter of the approximations.
- $B$ (backward contraction), bound on `gaussian-resampling`: the linear contraction from length-t vectors to length-s vectors that appears in the identity.
- $i$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, from 0 to r-1.
- $Z$ (transform output), bound on `synthetic-transforms`: The transform of the input z, a list of t entries.
- $s$ (shift amount), bound on `polynomial-ring-mod-yr-plus-1`: The number of positions by which the coefficient list moves under multiplication by y^s, with 0 <= s < r.
- $p$ (fractional bits), bound on `polynomial-ring-convolution`: The number of fractional bits of each coefficient, so that every real and imaginary coefficient part of a record is a multiple of 2^{-p}.
- $u$ (pair value (first)), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair that the two-point map takes as input.
- $v$ (pair value (second)), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair that the two-point map takes as input.
- $D$ (axis count), bound on `simultaneous-butterfly-layer`: The number of axes on which the layer acts, which is also the number of address chunks it transforms.

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

## Page to audit (`guard-width-bound`)

````markdown
# Guard-width bound

This page gives the guard widths for the intermediate coefficients of one [simultaneous butterfly layer](simultaneous-butterfly-layer.md), so that a single truncation at the end suffices. The guard-width bound is an explicit number of extra fractional and integer bits that makes every intermediate coefficient exact. It is the step that lets the layer's output enter the exact multiplication algorithm, whose final coefficients are recovered by rounding.

Here $u$ and $v$ are the two coefficients that the map combines. The two-point map sends them to $((u+v)/2,\ (u-v)/2)$. A layer applies this map to selected address bits, acting on each coefficient of each record. The layer acts on $D$ selected axes. The number $d$ is an upper bound on $D$. By the definition of the tensor product, each output coefficient is $2^{-D}$ times a signed sum of input coefficients. Intermediate values are exact Gaussian dyadics. A Gaussian dyadic is a complex number whose real and imaginary parts are integers divided by powers of two. The guard-width bound reserves fractional and integer bits for [Gaussian dyadics](gaussian-dyadics.md) of this kind.

Rounding after each stage would therefore be unsafe, because the intermediate operators need not be contractions. An error made at one stage is then not guaranteed to shrink later. The layer is evaluated exactly instead, and only its result is truncated.

Let $\ell$ be the depth of a value, the number of arithmetic operations on a chain that computes it from an input coefficient. Addition and subtraction can at most double the maximum modulus of their operands. Halving adds at most one denominator bit. Each input coefficient lies on the grid $2^{-p}\mathbb{Z}[i]$, so $p$ is the number of fractional bits it carries. Take $p = 8$ and two such coefficients $u, v$ with $|u| \le 1$ and $|v| \le 1$. Then $(u+v)/2$ lies on $2^{-9}\mathbb{Z}[i]$ and has modulus at most $1$, since $|u+v| \le 2$. Iterating these two rules along a chain, a value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb{Z}[i]$ and has modulus at most $2^{\ell}$.

The constants come from the [complex phase network](complex-phase-network.md), which the layer uses. The complex network has $W$ wires in total. Its label space has dimension $m$. The network makes $s$ smaller calls in total. Put $B = s+64(W+m+1)^3$, a fixed count that bounds how much the depth grows at each recursive level. Put $C_0 = 128\,m\,B^2$, a fixed constant of the network. For the stated construction, where $m = 10^6$, the exponent is $C_1 = 20$.

Let $\Delta = \lceil C_0 d^{C_1}\rceil$ be the number of extra fractional bits that the layer reserves. The layer therefore reserves $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component. Every intermediate coefficient is then exact, because the shifts discard no bits.

Since $d$ grows as a fixed power of $p$ whose exponent times $C_1$ is below one, $\Delta$ is $o(p)$, so the stored width of each component is $O(p)$. Addition, signed shifts and phase changes then cost $O(p)$ bit operations per coefficient.

The one final truncation, toward zero onto $2^{-p}\mathbb{Z}[i]$, changes each real and imaginary component by less than $2^{-p}$.
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

Write the answer to `exegenius/tasks/0055-audit-guard-width-bound.answer.json`, then run `exegenius submit 0055-audit-guard-width-bound` in the project directory. If submit rejects the answer, fix the answer and submit again.
