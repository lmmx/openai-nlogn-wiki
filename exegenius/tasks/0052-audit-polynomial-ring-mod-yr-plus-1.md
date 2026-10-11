# exegenius task 0052-audit-polynomial-ring-mod-yr-plus-1

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
- $y$ (second input), bound on `radix-digit-convolution`: The second input, a binary string of $n$ bits.
- $z$ (formal variable), bound on `radix-digit-convolution`: A formal variable in which each input is written as a polynomial whose coefficients are its digits.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: A non-negative integer, so that $2^k$ is the denominator.
- $y$ (indeterminate), bound on `signed-packing`: The indeterminate of the polynomial ring, the variable in which the packed polynomials are written.
- $r$ (coefficient count), bound on `signed-packing`: The number of coefficients of each polynomial being packed.
- $y$ (second field), bound on `address-interchange`: The value of the second field, a block of bits at matching positions.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $s$ (smaller call count), bound on `rank-saving-recursion`: The number of smaller calls that one call makes.
- $m$ (label dimension), bound on `rank-saving-recursion`: The dimension of the fixed ambient space in which the labels are subspaces.
- $C$ (two-point kernel), bound on `complex-phase-network`: The two-point kernel $H\,\mathrm{diag}(1, i)\,H$, which equals $aI + bX$.
- $m$ (address length), bound on `complex-phase-network`: The number of coordinates of a binary address, so that $\mathbb{F}_2^m$ is the address space.
- $\omega$ (primitive root of unity), bound on `discrete-fourier-transform`: The complex number $e^{-2\pi i/q}$, a primitive $q$-th root of unity.
- $k$ (output index), bound on `discrete-fourier-transform`: An index of the output coordinates, running from 0 to q-1.
- $s$ (source length), bound on `gaussian-resampling`: the number of entries in the source vector, which is the length of the transform being replaced.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $R_r$ (record ring), bound on `synthetic-transforms`: The ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The polynomial variable whose powers serve as the roots of unity.
- $z$ (transform input), bound on `synthetic-transforms`: The input list of t records to be transformed.
- $k$ (input index), bound on `synthetic-transforms`: The index of an entry of the input, from 0 to t-1.

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

## Page to audit (`polynomial-ring-mod-yr-plus-1`)

````markdown
# Polynomial ring modulo $y^r + 1$

Here $y$ is the polynomial variable, an indeterminate (a symbol with no numeric value) whose powers act as roots of unity. Here $r$ is the record length, the number of complex coefficients in a polynomial record, which is a power of two.

The polynomial ring modulo $y^r + 1$ is the ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$, so that $y$ has order $2r$ and wrap-around flips a sign. The argument stores one coordinate of its array in this ring, and the [convolution over this ring](polynomial-ring-convolution.md) is the next step built on that storage.

Write $R_r$ for this ring, where $R_r = \mathbb{C}[y]/(y^r+1)$, the polynomials over $\mathbb{C}$ with two polynomials identified when they differ by a multiple of $y^r+1$.

In the argument, one coordinate of the array is stored. Each element of $R_r$ is a polynomial $z$ with complex coefficients, and a polynomial of any degree is reduced by replacing each power $y^m$ with $m \ge r$ by $-y^{m-r}$. So every element has a unique representative $z = \sum_{k=0}^{r-1} z_k y^k$ of degree less than $r$, where $z_k$ is the $k$-th coefficient of $z$ for $0 \le k < r$, and the list $(z_0, \dots, z_{r-1})$ is the coefficient list of $z$. Addition is coefficientwise.

A root of unity is a number $\omega$ with $\omega^m = 1$ for some positive integer $m$, and the order of $\omega$ is the least such $m$. Since $y^r = -1$, we get $y^{2r} = (-1)^2 = 1$. No smaller positive power of $y$ equals $1$: for $0 < k < r$, $y^k$ is a representative of degree less than $r$ other than $1$, and for $r \le k < 2r$, $y^k = -y^{k-r}$, which is not $1$. So $y$ has order $2r$.

Take $r = 4$. Then $y^4 = -1$, and $z = 1 + 2y$ has coefficient list $(1, 2, 0, 0)$. Multiplying by $y^3$ gives $z\,y^3 = y^3 + 2y^4 = y^3 - 2$, with coefficient list $(-2, 0, 0, 1)$. The coefficient $1$ at position $0$ moves to position $3$, and the coefficient $2$ at position $1$ would move to position $4$, which wraps to position $0$ with its sign reversed.

Here $s$ is the shift amount, the number of positions by which the coefficient list moves, with $0 \le s < r$. Multiplying by $y^s$ therefore moves the coefficient $z_k$ to position $k+s$ when $k+s<r$, and otherwise to position $k+s-r$ with its sign reversed. Powers of $y$ serve as roots of unity here, and coefficient list.

The reason for this representation is that the transforms need roots of unity, and powers of $y$ supply them: $y^k$ for $0 \le k < 2r$ are roots of unity of order dividing $2r$. Multiplying a record by one of them moves coefficients and changes some signs, so it costs data movement rather than complex multiplications. The ring is also called the negacyclic polynomial ring, since its wrap-around reverses sign where a cyclic wrap-around would not.

This ring gives the arithmetic for the [synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$.
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

Write the answer to `exegenius/tasks/0052-audit-polynomial-ring-mod-yr-plus-1.answer.json`, then run `exegenius submit 0052-audit-polynomial-ring-mod-yr-plus-1` in the project directory. If submit rejects the answer, fix the answer and submit again.
