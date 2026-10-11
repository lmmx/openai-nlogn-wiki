# exegenius task 0062-audit-recovery-and-error

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

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each input string.
- $n$ (input length), bound on `n-log-n-conjecture`: The number of bits in each of the two input integers.
- $n$ (input length), bound on `radix-digit-convolution`: The number of bits in each input.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so every coefficient has magnitude at most 2^p.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary polynomial product fg, whose coefficients are read back from the integer product.
- $n$ (input length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $h$ (value of H), bound on `address-shear`: The current value of H when m = 1.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set on which triples are taken.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $S$ (other triple), bound on `subspace-labels`: Another triple of the ground set, compared with $T$ through the form.
- $h$ (ground set size), bound on `subset-intersection-network`: The number of elements in the ground set $[h]$, from which the triples are drawn.
- $S$ (neighbouring triple), bound on `subset-intersection-network`: A triple that is a neighbour of the other triple $T$ when they share exactly one element.
- $T$ (neighbouring triple), bound on `subset-intersection-network`: A triple, here the triple whose indicator vector is $t_T$.
- $m$ (label dimension), bound on `rank-saving-recursion`: The dimension of the fixed ambient space in which the labels are subspaces.
- $L$ (lost dimension), bound on `rank-saving-recursion`: The total dimension lost along the decreasing edges of the network.
- $b$ (kernel coefficient b), bound on `complex-phase-network`: The constant $(1-i)/2$ in the kernel $C = aI + bX$.
- $m$ (address length), bound on `complex-phase-network`: The number of coordinates of a binary address, so that $\mathbb{F}_2^m$ is the address space.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $p$ (precision), bound on `gaussian-resampling`: a positive integer precision parameter of the approximations.
- $p$ (fractional bits), bound on `polynomial-ring-convolution`: The number of fractional bits of each coefficient, so that every real and imaginary coefficient part of a record is a multiple of 2^{-p}.
- $b$ (imaginary numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the imaginary part of f after scaling by 2^{-p}.
- $p$ (precision), bound on `guard-width-bound`: The number of fractional bits carried by each input coefficient.
- $m$ (label dimension), bound on `guard-width-bound`: The dimension of the label space of the complex network.
- $T$ (scratch chunk), bound on `packed-bit-addition`: The third address chunk, whose initial value is arbitrary and which is used as temporary space.
- $L$ (chunk width), bound on `packed-bit-addition`: The number of address bits in each of the chunks $X$ and $W$.
- $x$ (formal variable), bound on `cyclic-convolution`: The indeterminate of the polynomial associated with a sequence, whose power x^j stands for position j.
- $S$ (total length), bound on `chinese-remainder-map`: The total number of positions, the product of the axis lengths, a count.
- $x$ (one-dimensional indeterminate), bound on `chinese-remainder-map`: The indeterminate of the one-dimensional cyclic polynomial ring.
- $\cdot$ (coordinatewise product), bound on `bluestein-chirp-identity`: The product of two vectors of length q taken entry by entry.
- $x$ (first operand), bound on `bluestein-chirp-identity`: The first of the two vectors of length q in the cyclic convolution.
- $m$ (integer argument), bound on `bluestein-chirp-identity`: The integer at which the chirp entry a_m is evaluated.

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

## Page to audit (`recovery-and-error`)

````markdown
# Exact coefficient recovery

Exact coefficient recovery is the error analysis that makes the final rounding return the true integer convolution coefficients. It is the last step of the argument for exact integer multiplication: the convolution is computed through approximate transforms, and this page shows that the accumulated error stays below one half, so rounding gives exactly the integers the product needs.

## Why rounding recovers the integer

The true coefficients are integers, and distinct integers are at least $1$ apart. If a computed value $x$ satisfies $|x - m| < 1/2$ for an integer $m$, then every other integer is farther than $1/2$ from $x$, so $m$ is the unique nearest integer and rounding returns $m$. For example, if the true coefficient is $7$, a computed value $7.3$ (error $0.3$) rounds to $7$, while a computed value $7.6$ (error $0.6$) rounds to $8$. The goal is therefore to bound the total error of each coefficient by a quantity strictly below $1/2$. unique correct coefficient, and

## Units

Each stored value keeps $p$ fractional bits, the number of binary places after the point. Write $h_p = 2^{-p}$ for the size of one unit in the last place of a stored value, so an error measured in units of $h_p$ is an absolute error below that multiple of $h_p$. It takes its guard widths from the [guard-width bound](guard-width-bound.md), so each stored value is exact and only the stated truncations contribute error. The source sets $b = \lceil \log_2 n\rceil$, the number of bits in each radix digit, and $p = 6b$, so $h_p = 2^{-6b}$.

## Errors add across stages

Each stage works on values that already carry error from the stages before it. A linear map never increases an input error. For a bilinear product of two approximate operands, the operand errors add: the error of the product is at most the error of the first operand times the norm of the second, plus the norm of the first times the error of the second. Here the operands lie in the unit disk, arrays of norm at most one, so every norm is at most one and the two errors simply add. Summing the stage errors, each measured in units of $h_p$, gives the total error of the coefficient.

## The polynomial-ring stage

The convolution over the polynomial ring is computed from two forward transforms, a pointwise product, and an opposite transform, with one truncation in the product. Here $T$ is the number of entries in the padded transform box, a power of two chosen in $[4n/b, 8n/b)$, and $L = \log_2 T$. This step bounds the error of [Convolution over the polynomial ring](polynomial-ring-convolution.md) by $5TL\,h_p$. Before the exact scale, $3L+2$ units of $h_p$. $5TL\,h_p$.

The twists at the two ends of the ring map also carry error. It counts the error of the [phase twist](phase-twist.md) at each end, each below $4h_p$, so these errors enter the same sum.

## Scaling and the final bound

Two exact multiplications by known scales undo the normalizations. Each acts exactly on grid numerators, so it adds no error of its own and only rescales the error already present. Here $S$ is the product of the pairwise coprime source lengths, and $\gamma$ is a construction constant with $\gamma = o(b)$. absolute error of each coefficient is bounded by $\frac{1}{2^{2b+4}S}\cdot 28\sqrt{2}\,\gamma\,T^2 L\cdot 2^{-6b}$. This is at most $448\,b\,2^{-b+\gamma} \le 448\,b\,2^{-3b/4}$, which is less than $1/2$ for large $n$. The last factor $2^{-6b}$ is $h_p$, one unit of the stored precision.

With the error below $1/2$, the computed coefficient lies within $1/2$ of the true integer, and rounding to the nearest integer returns it exactly.
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

Write the answer to `exegenius/tasks/0062-audit-recovery-and-error.answer.json`, then run `exegenius submit 0062-audit-recovery-and-error` in the project directory. If submit rejects the answer, fix the answer and submit again.
