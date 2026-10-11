# exegenius task 0051-audit-synthetic-transforms

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
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)

## Symbols bound on earlier pages

- $y$ (second input string), bound on `exact-integer-multiplication`: A binary string of length n, the second input to the product.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each input string.
- $n$ (input length), bound on `n-log-n-conjecture`: The number of bits in each of the two input integers.
- $\lg n$ (binary logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm of n, rounded up to an integer and never below 1.
- $\kappa$ (saving exponent), bound on `n-log-n-conjecture`: The specific positive constant by which the main theorem's running time falls below n lg n.
- $n$ (input length), bound on `radix-digit-convolution`: The number of bits in each input.
- $y$ (second input), bound on `radix-digit-convolution`: The second input, a binary string of $n$ bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $j$ (coefficient position), bound on `radix-digit-convolution`: The position of a product coefficient, running from $0$ to $2q-2$.
- $z$ (formal variable), bound on `radix-digit-convolution`: A formal variable in which each input is written as a polynomial whose coefficients are its digits.
- $a$ (Gaussian integer numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: A non-negative integer, so that $2^k$ is the denominator.
- $y$ (indeterminate), bound on `signed-packing`: The indeterminate of the polynomial ring, the variable in which the packed polynomials are written.
- $r$ (coefficient count), bound on `signed-packing`: The number of coefficients of each polynomial being packed.
- $j$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from 0 to r-1.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in [-B/2, B/2) congruent to f(B)g(B) modulo B, which is the next coefficient of h.
- $n$ (input length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $y$ (second field), bound on `address-interchange`: The value of the second field, a block of bits at matching positions.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $a$ (bank index), bound on `subset-intersection-network`: An index $a=(a_1,a_2,a_3)$ of one entry of a bank, a triple of triples.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $C$ (two-point kernel), bound on `complex-phase-network`: The two-point kernel $H\,\mathrm{diag}(1, i)\,H$, which equals $aI + bX$.
- $a$ (kernel coefficient a), bound on `complex-phase-network`: The constant $(1+i)/2$ in the kernel $C = aI + bX$.
- $\omega$ (primitive root of unity), bound on `discrete-fourier-transform`: The complex number $e^{-2\pi i/q}$, a primitive $q$-th root of unity.
- $j$ (input index), bound on `discrete-fourier-transform`: An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: An index of the output coordinates, running from 0 to q-1.
- $t$ (resampled length), bound on `gaussian-resampling`: the power-of-two number of entries in the resampled vector, greater than s.

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

## Page to audit (`synthetic-transforms`)

````markdown
# Synthetic polynomial transforms

Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable, so that multiplying a value by a root only moves coefficients and changes some signs. They are the transforms that compute the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md). The result is $O(n(\lg n)^{1-\kappa})$ time for a fixed constant $\kappa$, where $n$ is the bit length of the integers.

## Records and roots

Let $r \ge 2$ be a power of two, where $r$ is the number of complex coefficients in a record. Write $R_r = \mathbb{C}[y]/(y^r+1)$ for the ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$, where $y$ is the polynomial variable. A record is an element of $R_r$, stored as its $r$ coefficients.

Since $y^r = -1$, a power of $y$ that runs past position $r-1$ wraps around with a sign change. The rule below uses three symbols. In it, $c_i$ is the coefficient of $y^i$ in the record, $i$ is its position, and $a$ is the number of places the shift moves each coefficient, with $0 \le a < 2r$:

$$y^a \sum_{i=0}^{r-1} c_i y^i = \sum_{i=0}^{r-1} (-1)^{\lfloor (i+a)/r \rfloor}\, c_i\, y^{(i+a) \bmod r}.$$

So multiplying by $y^a$ moves every coefficient $a$ places along the coefficient list, cyclically, and negates each coefficient that wraps past the end. This is a signed shift of the coefficient list, and it is exact: it involves no rounding and no multiplication.

Let $t$ be a power of two dividing $2r$, the number of entries in the transform. The root $\omega_t = y^{2r/t}$ is a primitive $t$-th root of unity in $R_r$. Indeed, $\omega_t^t = y^{2r} = 1$, and $\omega_t^{t/2} = y^r = -1$. Every power of $\omega_t$ is a power of $y$, so multiplying by any power of $\omega_t$ is a signed shift.

## The transform

 The input $z=(z_0,\dots,z_{t-1})$ is a list of $t$ records in $R_r$.

Here $j$ and $k$ are indices running from $0$ to $t-1$, and $Z_j$ is the $j$-th entry of the transform $Z=(Z_0,\dots,Z_{t-1})$ of $z$, given by

$$Z_j = \frac{1}{t}\sum_{k=0}^{t-1} \omega_t^{jk}\, z_k.$$

A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. of Nussbaumer and Quandalle.

## Why the roots make the transform cheap

A radix-two transform of length $t$ has $\log_2 t$ levels. Each level pairs up entries and applies a two-point butterfly: one entry of the pair is multiplied by a power of $\omega_t$, and the pair is replaced by its sum and its difference. Because a power of $\omega_t$ is a signed shift, the multiplication inside each butterfly is only a rearrangement of coefficients with sign changes, and the butterfly costs one addition and one subtraction of records. Between levels, the entries are moved to new addresses, which is also a rearrangement. In the source's words, shifts, and two-point butterfly operations.

For example, take $r = 4$ and $t = 4$. Then $\omega_4 = y^2$, and $\omega_4^2 = y^4 = -1$. Multiplying a record by $\omega_4$ gives

$$\omega_4\,(c_0 + c_1 y + c_2 y^2 + c_3 y^3) = -c_2 - c_3 y + c_0 y^2 + c_1 y^3,$$

so the coefficient list $(c_0, c_1, c_2, c_3)$ becomes $(-c_2, -c_3, c_0, c_1)$. This is two moves and two negations, with no multiplication.
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

Write the answer to `exegenius/tasks/0051-audit-synthetic-transforms.answer.json`, then run `exegenius submit 0051-audit-synthetic-transforms` in the project directory. If submit rejects the answer, fix the answer and submit again.
