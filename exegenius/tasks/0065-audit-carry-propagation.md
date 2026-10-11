# exegenius task 0065-audit-carry-propagation

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
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Chinese-remainder map (also: Agarwal–Cooley map)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
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
- Prime source lengths
- Transform identity with retained permutations
- Exact coefficient recovery

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each input string.
- $n$ (input length), bound on `n-log-n-conjecture`: The number of bits in each of the two input integers.
- $n$ (input length), bound on `radix-digit-convolution`: The number of bits in each input.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit.
- $q$ (digits per input), bound on `radix-digit-convolution`: The number of radix-$2^b$ digits in each input.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $j$ (coefficient position), bound on `radix-digit-convolution`: The position of a product coefficient, running from $0$ to $2q-2$.
- $c_j$ (product coefficient), bound on `radix-digit-convolution`: The integer coefficient of $z^j$ in the product of the two digit polynomials.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: A non-negative integer, so that $2^k$ is the denominator.
- $j$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from 0 to r-1.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary polynomial product fg, whose coefficients are read back from the integer product.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in [-B/2, B/2) congruent to f(B)g(B) modulo B, which is the next coefficient of h.
- $n$ (input length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $q$ (radix prime), bound on `address-shear`: A fixed odd prime, the base of the digits.
- $h$ (value of H), bound on `address-shear`: The current value of H when m = 1.
- $d$ (value of D), bound on `address-shear`: The current value of D when m = 1.
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set on which triples are taken.
- $h$ (ground set size), bound on `subset-intersection-network`: The number of elements in the ground set $[h]$, from which the triples are drawn.
- $b$ (kernel coefficient b), bound on `complex-phase-network`: The constant $(1-i)/2$ in the kernel $C = aI + bX$.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, a positive integer.
- $j$ (input index), bound on `discrete-fourier-transform`: An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: An index of the output coordinates, running from 0 to q-1.
- $q$ (transform length), bound on `gaussian-resampling`: the number of entries of the vector that a transform of length q acts on.
- $j$ (output index), bound on `synthetic-transforms`: The index of an entry of the transform, from 0 to t-1.
- $k$ (input index), bound on `synthetic-transforms`: The index of an entry of the input, from 0 to t-1.
- $b$ (imaginary numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the imaginary part of f after scaling by 2^{-p}.
- $c$ (real numerator of g), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the real part of g after scaling by 2^{-p}.
- $d$ (axis bound), bound on `guard-width-bound`: An upper bound on the number D of selected axes in one layer.
- $k$ (output position), bound on `cyclic-convolution`: An index in the range 0 to s-1 naming an entry of the cyclic convolution.
- $j$ (summation index), bound on `cyclic-convolution`: The index running over the entries of f in the cyclic convolution sum.
- $x$ (formal variable), bound on `cyclic-convolution`: The indeterminate of the polynomial associated with a sequence, whose power x^j stands for position j.
- $d$ (axis count), bound on `chinese-remainder-map`: The number of cyclic axes, a count.
- $x$ (one-dimensional indeterminate), bound on `chinese-remainder-map`: The indeterminate of the one-dimensional cyclic polynomial ring.
- $k$ (coefficient index), bound on `chinese-remainder-map`: An ordinary coefficient index in the range $0 \le k < S$.
- $q$ (transform length), bound on `bluestein-chirp-identity`: The number of entries in each input and output vector of the transform.
- $j$ (input position), bound on `bluestein-chirp-identity`: An index into the input vector, an integer from 0 to q-1.
- $k$ (output position), bound on `bluestein-chirp-identity`: An index into the output vector, an integer from 0 to q-1.
- $\cdot$ (coordinatewise product), bound on `bluestein-chirp-identity`: The product of two vectors of length q taken entry by entry.
- $x$ (first operand), bound on `bluestein-chirp-identity`: The first of the two vectors of length q in the cyclic convolution.
- $j$ (coefficient position), bound on `phase-twist`: The position of a coefficient in a record, counted from 0.
- $k$ (first term position), bound on `phase-twist`: The position of the coefficient taken from the first record in a product.
- $b$ (digit width), bound on `recovery-and-error`: The number of bits in each radix digit, where $b = \lceil \log_2 n \rceil$.
- $x$ (computed value), bound on `recovery-and-error`: A computed approximation of a true integer coefficient.
- $q$ (vector length), bound on `transform-identity`: The number of entries of a vector to which the normalized transform F_q applies.
- $j$ (entry index), bound on `transform-identity`: An index of an entry of a vector, running from 0 to q-1 in the sum defining F_q.
- $k$ (output index), bound on `transform-identity`: An index of an entry of a transformed vector, taken modulo q.
- $d$ (number of axes), bound on `prime-source-lengths`: The number of axes of the box, which is also the number of prime lengths.
- $n$ (input bit length), bound on `prime-source-lengths`: The number of bits in each input integer.
- $b$ (bit length of n), bound on `prime-source-lengths`: The number of bits needed to write $n$, that is, $\lceil\log_2 n\rceil$.
- $x$ (interval scale), bound on `prime-source-lengths`: The real number that sets the scale of the prime interval.
- $q$ (prime in interval), bound on `prime-source-lengths`: A prime lying in the interval $((1-2\eta)x, (1-\eta)x]$.

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

## Page to audit (`carry-propagation`)

````markdown
# Carry propagation

Carry propagation is the final arithmetic step that turns integer coefficients into the exact binary product, so it is what gives the output of [Integer multiplication below n log n](main-theorem.md) its value.

Carry propagation takes its input from [Radix-digit convolution](radix-digit-convolution.md): the output is the list of integer coefficients $c_0, c_1, \dots$ of the product of the two digit polynomials.

Let $n$ be the bit length of each input. Let $b$ be the number of bits in one radix digit, and let $q = \lceil n/b \rceil$ be the number of digits in each input. The radix is $Q_0 = 2^b$, the base in which each digit is written. Each input is then a polynomial in $Q_0$ with $q$ digit coefficients. The index $j$ runs over the positions of the coefficient list, from $0$ upward. The integer coefficient $c_j$ is the coefficient of $Q_0^j$ in the product of the two digit polynomials. Each product coefficient obeys $0 \le c_j \le q(Q_0-1)^2 < Q_0^3$.

The digit $d_j$ is the $j$th base-$Q_0$ digit of the output, so $0 \le d_j < Q_0$. The sum $\sum_j c_j Q_0^j$ is the product, but the $c_j$ are not digits, because they can exceed $Q_0 - 1$. Carry propagation rewrites the same sum with digits $d_j$. The carry $k_j$ is the amount carried into position $j$ from the lower positions. These are defined by

$$k_0 = 0, \qquad d_j = (c_j + k_j) \bmod Q_0, \qquad k_{j+1} = \left\lfloor \frac{c_j + k_j}{Q_0} \right\rfloor,$$

where $x \bmod Q_0$ is the remainder of $x$ on division by $Q_0$, and $\lfloor x \rfloor$ is the largest integer not above $x$. At each position, the number $c_j + k_j$ is split into its remainder $d_j$, which stays at position $j$, and its quotient $k_{j+1}$, which moves to position $j+1$. Hence

$$c_j + k_j = d_j + Q_0 k_{j+1}.$$

Summing this relation over the positions shows what the carries do. For every $j$,

$$\sum_{h<j} c_h Q_0^h = \sum_{h<j} d_h Q_0^h + k_j Q_0^j.$$

This holds at $j = 0$, where both sides are $0$ because $k_0 = 0$. If it holds at $j$, add $c_j Q_0^j$ to the left side and $d_j Q_0^j + k_{j+1} Q_0^{j+1}$ to the right side. Multiplying the split relation by $Q_0^j$ gives $c_j Q_0^j + k_j Q_0^j = d_j Q_0^j + k_{j+1} Q_0^{j+1}$, so the identity holds at $j+1$. The carry $k_j$ is therefore exactly the value that the lower positions pass upward:

Once all coefficients are processed, the leftover carry is written out the same way, one digit at a time, until it is zero:. Taking $j$ past the last coefficient, where every $c_h$ and the remaining carry are zero, the identity gives $\sum_j c_j Q_0^j = \sum_j d_j Q_0^j$. Each $d_j$ is a block of $b$ bits, and the digits are base-$Q_0$ digits, so the digit string written from the top digit down is the binary representation of the product.

The recurrence reads $c_j$ only after $k_j$ is known, so the positions must be processed from least significant to most significant. The carries also stay small. If $0 \le k_j \le q(Q_0-1)$, then $c_j + k_j \le q(Q_0-1)^2 + q(Q_0-1) = qQ_0(Q_0-1)$, so $k_{j+1} \le q(Q_0-1)$ as well.

For $Q_0 = 4$ (so $b = 2$) and coefficients $(c_0, c_1, c_2) = (5, 3, 7)$:

- $j=0$: $c_0 + k_0 = 5$, so $d_0 = 1$ and $k_1 = 1$.
- $j=1$: $c_1 + k_1 = 4$, so $d_1 = 0$ and $k_2 = 1$.
- $j=2$: $c_2 + k_2 = 8$, so $d_2 = 0$ and $k_3 = 2$.
- The leftover carry $2 < 4$ becomes $d_3 = 2$, with $k_4 = 0$.

The digits $(d_3, d_2, d_1, d_0) = (2, 0, 0, 1)$ give $2 \cdot 64 + 0 \cdot 16 + 0 \cdot 4 + 1 = 129$, which equals $5 + 3 \cdot 4 + 7 \cdot 16 = 129$. Written in binary, each digit takes two bits: $10\,00\,00\,01$.
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

Write the answer to `exegenius/tasks/0065-audit-carry-propagation.answer.json`, then run `exegenius submit 0065-audit-carry-propagation` in the project directory. If submit rejects the answer, fix the answer and submit again.
