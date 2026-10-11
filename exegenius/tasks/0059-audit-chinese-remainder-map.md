# exegenius task 0059-audit-chinese-remainder-map

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
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $x_i$ (digit of x), bound on `radix-digit-convolution`: The digit of $x$ at position $i$, of weight $(2^b)^i$.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $j$ (coefficient position), bound on `radix-digit-convolution`: The position of a product coefficient, running from $0$ to $2q-2$.
- $a$ (Gaussian integer numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: A non-negative integer, so that $2^k$ is the denominator.
- $j$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from 0 to r-1.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $d$ (value of D), bound on `address-shear`: The current value of D when m = 1.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $S$ (other triple), bound on `subspace-labels`: Another triple of the ground set, compared with $T$ through the form.
- $a$ (bank index), bound on `subset-intersection-network`: An index $a=(a_1,a_2,a_3)$ of one entry of a bank, a triple of triples.
- $S$ (neighbouring triple), bound on `subset-intersection-network`: A triple that is a neighbour of the other triple $T$ when they share exactly one element.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $s$ (smaller call count), bound on `rank-saving-recursion`: The number of smaller calls that one call makes.
- $m$ (label dimension), bound on `rank-saving-recursion`: The dimension of the fixed ambient space in which the labels are subspaces.
- $C$ (two-point kernel), bound on `complex-phase-network`: The two-point kernel $H\,\mathrm{diag}(1, i)\,H$, which equals $aI + bX$.
- $a$ (kernel coefficient a), bound on `complex-phase-network`: The constant $(1+i)/2$ in the kernel $C = aI + bX$.
- $b$ (kernel coefficient b), bound on `complex-phase-network`: The constant $(1-i)/2$ in the kernel $C = aI + bX$.
- $m$ (address length), bound on `complex-phase-network`: The number of coordinates of a binary address, so that $\mathbb{F}_2^m$ is the address space.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $j$ (input index), bound on `discrete-fourier-transform`: An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: An index of the output coordinates, running from 0 to q-1.
- $s$ (source length), bound on `gaussian-resampling`: the number of entries in the source vector, which is the length of the transform being replaced.
- $i$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, from 0 to r-1.
- $a$ (shift amount), bound on `synthetic-transforms`: The number of places a signed shift moves each coefficient, an integer with 0 \le a < 2r.
- $j$ (output index), bound on `synthetic-transforms`: The index of an entry of the transform, from 0 to t-1.
- $k$ (input index), bound on `synthetic-transforms`: The index of an entry of the input, from 0 to t-1.
- $s$ (shift amount), bound on `polynomial-ring-mod-yr-plus-1`: The number of positions by which the coefficient list moves under multiplication by y^s, with 0 <= s < r.
- $a$ (real numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the real part of f after scaling by 2^{-p}.
- $b$ (imaginary numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the imaginary part of f after scaling by 2^{-p}.
- $d$ (axis bound), bound on `guard-width-bound`: An upper bound on the number D of selected axes in one layer.
- $m$ (label dimension), bound on `guard-width-bound`: The dimension of the label space of the complex network.
- $s$ (smaller-call count), bound on `guard-width-bound`: The total number of smaller calls made by the network.
- $s$ (sequence length), bound on `cyclic-convolution`: The number of entries in each of the two input sequences.
- $k$ (output position), bound on `cyclic-convolution`: An index in the range 0 to s-1 naming an entry of the cyclic convolution.
- $j$ (summation index), bound on `cyclic-convolution`: The index running over the entries of f in the cyclic convolution sum.
- $x$ (formal variable), bound on `cyclic-convolution`: The indeterminate of the polynomial associated with a sequence, whose power x^j stands for position j.

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

## Page to audit (`chinese-remainder-map`)

````markdown
# Chinese-remainder map

The Chinese-remainder map is a relabeling of coefficient positions that turns one [cyclic convolution](cyclic-convolution.md) into a multidimensional cyclic convolution. In the main argument it is the step that places the coefficients of a [radix-digit convolution](radix-digit-convolution.md) on distinct prime cyclic axes, so that each axis can be transformed separately. It is also called the Agarwal–Cooley map.

Let $d$ be the number of cyclic axes. Where $s_i$ is the number of positions on axis $i$, the lengths $s_1, \dots, s_d$ are pairwise coprime, meaning any two of them have greatest common divisor $1$. Let $S = s_1 s_2 \cdots s_d$ be the total number of positions, which is the length of the one-dimensional cyclic convolution being replaced.

A cyclic convolution of length $S$ indexes its positions by the integers modulo $S$. The Chinese remainder theorem says that when $S$ factors into pairwise coprime lengths, an integer modulo $S$ is determined by its residue modulo each factor. The map below is that splitting, written out with explicit coordinates.

For each axis $i$, let $P_i = s_1 s_2 \cdots s_{i-1}$ be the product of the lengths before it, with $P_1 = 1$ as an empty product. Let $\mu_i$ be an inverse of $P_i$ modulo $s_i$, so that $\mu_i P_i \equiv 1 \pmod{s_i}$. It exists because $P_i$ is a product of lengths coprime to $s_i$.

Write $x$ for the indeterminate of the one-dimensional ring, so that $\mathbb{C}[x]/(x^S-1)$ is the ring of polynomials in which $x^S$ is replaced by $1$. Multiplying two such polynomials wraps exponents modulo $S$, which is exactly cyclic convolution of their coefficient lists. The target is the multidimensional ring $\mathbb{C}[x_1,\dots,x_d]/(x_1^{s_1}-1,\dots,x_d^{s_d}-1)$, where $x_i$ is the indeterminate of axis $i$ and $x_i^{s_i}$ is replaced by $1$. A multidimensional cyclic convolution is the product in this ring, where the exponent on each axis wraps modulo that axis's length.

Define $\Phi$ on the generator by $\Phi(x) = \prod_{i=1}^d x_i^{\mu_i}$, and extend it to polynomials as a ring homomorphism. This is well defined: the exponent of $x_i$ in $\Phi(x)^S$ is $\mu_i S$, which is divisible by $s_i$, so $\Phi(x)^S = 1$ in the target. The power $\Phi(x)^m$ equals $1$ exactly when $s_i \mid m$ for every $i$, because each $\mu_i$ is invertible modulo $s_i$. Since the $s_i$ are pairwise coprime, this happens exactly when $S \mid m$. So $\Phi(x)$ has order $S$, its powers are $S$ distinct monomials, and these are all $S$ monomial basis elements of the target. Because $\Phi$ is a ring isomorphism, the map preserves [cyclic convolution](cyclic-convolution.md) of length $S$: the product of two coefficient polynomials maps to the product of their images, which is a multidimensional cyclic convolution on the axes $s_1, \dots, s_d$.

Let $k$ be an ordinary coefficient index, with $0 \le k < S$. Let $a_j$ be the mixed-radix digit of $k$ on axis $j$, with $0 \le a_j < s_j$., $k = \sum_{j=1}^{d} a_j P_j$.

Let $b_i$ be the coordinate of $\Phi(x^k)$ on axis $i$, so $\Phi(x^k) = \prod_i x_i^{b_i}$. Then $b_i = a_i + \mu_i \sum_{j<i} a_j P_j \pmod{s_i}$. Terms with $j > i$ vanish modulo $s_i$ because $P_j$ contains the factor $s_i$. The $j = i$ term gives $\mu_i P_i a_i \equiv a_i$, and the terms with $j < i$ remain.

So the coefficient at index $k$ is stored at the address $(b_1, \dots, b_d)$ on the axes.

Take $d = 2$, $s_1 = 3$, $s_2 = 5$, so $S = 15$. Then $P_1 = 1$, $P_2 = 3$, $\mu_1 = 1$, and $\mu_2 = 2$ because $3 \cdot 2 = 6 \equiv 1 \pmod 5$. So $\Phi(x) = x_1 x_2^2$. The index $k = 7$ has digits $a_1 = 1$ and $a_2 = 2$, since $7 = 1 + 3 \cdot 2$. Its coordinates are $b_1 = a_1 = 1$ and $b_2 = a_2 + \mu_2 a_1 P_1 = 2 + 2 \cdot 1 \cdot 1 \equiv 4 \pmod 5$. Directly, $\Phi(x)^7 = x_1^7 x_2^{14} = x_1 x_2^4$, since $7 \equiv 1 \pmod 3$ and $14 \equiv 4 \pmod 5$. So index $7$ is stored at address $(1, 4)$ on the $3 \times 5$ grid.

In the main argument the axis lengths are distinct primes, which are pairwise coprime, so this construction applies. prime cyclic axes.
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

Write the answer to `exegenius/tasks/0059-audit-chinese-remainder-map.answer.json`, then run `exegenius submit 0059-audit-chinese-remainder-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
