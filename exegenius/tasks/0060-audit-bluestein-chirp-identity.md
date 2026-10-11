# exegenius task 0060-audit-bluestein-chirp-identity

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
- $y$ (second input string), bound on `exact-integer-multiplication`: A binary string of length n, the second input to the product.
- $q$ (digits per input), bound on `radix-digit-convolution`: The number of radix-$2^b$ digits in each input.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $y$ (second input), bound on `radix-digit-convolution`: The second input, a binary string of $n$ bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $j$ (coefficient position), bound on `radix-digit-convolution`: The position of a product coefficient, running from $0$ to $2q-2$.
- $a$ (Gaussian integer numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: A non-negative integer, so that $2^k$ is the denominator.
- $y$ (indeterminate), bound on `signed-packing`: The indeterminate of the polynomial ring, the variable in which the packed polynomials are written.
- $j$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from 0 to r-1.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $y$ (second field), bound on `address-interchange`: The value of the second field, a block of bits at matching positions.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $q$ (radix prime), bound on `address-shear`: A fixed odd prime, the base of the digits.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $a$ (bank index), bound on `subset-intersection-network`: An index $a=(a_1,a_2,a_3)$ of one entry of a bank, a triple of triples.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $m$ (label dimension), bound on `rank-saving-recursion`: The dimension of the fixed ambient space in which the labels are subspaces.
- $a$ (kernel coefficient a), bound on `complex-phase-network`: The constant $(1+i)/2$ in the kernel $C = aI + bX$.
- $m$ (address length), bound on `complex-phase-network`: The number of coordinates of a binary address, so that $\mathbb{F}_2^m$ is the address space.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, a positive integer.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ complex numbers, the input to the transform.
- $j$ (input index), bound on `discrete-fourier-transform`: An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: An index of the output coordinates, running from 0 to q-1.
- $F_q$ (Fourier transform), bound on `discrete-fourier-transform`: The discrete Fourier transform of length q, the map sending u to F_q u.
- $q$ (transform length), bound on `gaussian-resampling`: the number of entries of the vector that a transform of length q acts on.
- $F_q$ (normalized transform), bound on `gaussian-resampling`: the normalized discrete Fourier transform of length q.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The polynomial variable whose powers serve as the roots of unity.
- $i$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, from 0 to r-1.
- $a$ (shift amount), bound on `synthetic-transforms`: The number of places a signed shift moves each coefficient, an integer with 0 \le a < 2r.
- $j$ (output index), bound on `synthetic-transforms`: The index of an entry of the transform, from 0 to t-1.
- $k$ (input index), bound on `synthetic-transforms`: The index of an entry of the input, from 0 to t-1.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $a$ (real numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the real part of f after scaling by 2^{-p}.
- $e$ (imaginary numerator of g), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the imaginary part of g after scaling by 2^{-p}.
- $u$ (pair value (first)), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair that the two-point map takes as input.
- $m$ (label dimension), bound on `guard-width-bound`: The dimension of the label space of the complex network.
- $u$ (first coefficient), bound on `guard-width-bound`: The first of the two coefficients that the two-point map combines.
- $\ast$ (cyclic convolution), bound on `cyclic-convolution`: The operation that maps two length-s sequences to their cyclic convolution, a sequence of length s.
- $k$ (output position), bound on `cyclic-convolution`: An index in the range 0 to s-1 naming an entry of the cyclic convolution.
- $j$ (summation index), bound on `cyclic-convolution`: The index running over the entries of f in the cyclic convolution sum.
- $x$ (formal variable), bound on `cyclic-convolution`: The indeterminate of the polynomial associated with a sequence, whose power x^j stands for position j.
- $x$ (one-dimensional indeterminate), bound on `chinese-remainder-map`: The indeterminate of the one-dimensional cyclic polynomial ring.
- $k$ (coefficient index), bound on `chinese-remainder-map`: An ordinary coefficient index in the range $0 \le k < S$.
- $a_j$ (mixed-radix digit), bound on `chinese-remainder-map`: The digit of $k$ on axis $j$, with $0 \le a_j < s_j$.

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

## Page to audit (`bluestein-chirp-identity`)

````markdown
# Bluestein's chirp identity

Bluestein's chirp identity rewrites a [Discrete Fourier transform](discrete-fourier-transform.md) as a [cyclic convolution](cyclic-convolution.md) multiplied by chirp factors. It reduces the transform to a [cyclic convolution](cyclic-convolution.md), so any method that computes that convolution also computes the transform.

In the argument, this is the step that converts the middle transform, including its target permutation, into a normalized cyclic convolution. The paper states the step as into normalized cyclic convolution. A chirp factorisation therefore turns the middle transform into a cyclic convolution, which the earlier steps already compute: The paper also says that the target permutation as a separate permutation of the array, so no separate sort is needed.

Let $q$ be the length of the transform: the number of entries in each input and output vector. Let $u$ be the input vector, with entries $u_0$ through $u_{q-1}$. Let $j$ be an input position and $k$ an output position, each an integer from $0$ to $q-1$. Write $F_q$ for this transform of the input vector. That is,
$$(F_q u)_k = \frac{1}{q}\sum_{j=0}^{q-1} u_j\, e^{-2\pi i jk/q}.$$

The dot $\cdot$ denotes coordinatewise multiplication of two vectors of length $q$. The star $\ast$ denotes cyclic convolution of two vectors $x$ and $y$ of length $q$. That is,
$$(x\ast y)_k = \sum_{j=0}^{q-1} x_j\, y_{(k-j) \bmod q}.$$

The chirp is the vector $a$ whose entry at each integer $m$ is $a_m = e^{\pi i m^2/q}$. Since $q$ is even, $a_{m+q} = a_m$ for every integer $m$. Indeed $(m+q)^2 - m^2 = q(2m+q)$, so $a_{m+q}/a_m = e^{\pi i (2m+q)} = 1$. Thus the index $k-j$ can be read modulo $q$ without changing $a_{k-j}$.

Since $2jk = j^2 + k^2 - (k-j)^2$, the exponential splits as
$$e^{-2\pi i jk/q} = \frac{a_{k-j}}{a_j\, a_k}.$$
Substituting this into the definition gives
$$(F_q u)_k = \frac{1}{q\,a_k}\sum_{j=0}^{q-1} \frac{u_j}{a_j}\, a_{k-j}.$$
The sum is the cyclic convolution of $(1/a)\cdot u$ with $a$, where $1/a$ is the vector with entries $1/a_m$. So the transform is
$$F_q u = \frac{1}{q}\,\Big(\frac{1}{a}\Big)\cdot\Big(\Big(\frac{1}{a}\cdot u\Big)\ast a\Big).$$
Each chirp entry has modulus $1$, so the two pointwise multiplications by $1/a$ do not change the size of any entry. The only convolution is the one in the middle.

Worked example with $q=2$. Here $a_0 = 1$ and $a_1 = e^{\pi i/2} = i$. Take $u = (1,3)$. The definition gives $(F_2 u)_0 = (1+3)/2 = 2$ and $(F_2 u)_1 = (1-3)/2 = -1$. The identity gives the same result. First, $(1/a)\cdot u = (1,\,-3i)$. Its cyclic convolution with $a = (1,i)$ has entries $1\cdot 1 + (-3i)\cdot i = 4$ at $k=0$, and $1\cdot i + (-3i)\cdot 1 = -2i$ at $k=1$. Multiplying by $\frac{1}{2}(1,\,-i)$ gives $(2,\,-1)$.

The wrap-around is essential. The index $k-j$ runs over all of $\{0,\dots,q-1\}$ modulo $q$, and the periodicity of $a$ is what makes the wrapped terms agree with $a_{k-j}$. The identity therefore produces a cyclic convolution, not a linear one. The paper credits this conversion to Bluestein:.
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

Write the answer to `exegenius/tasks/0060-audit-bluestein-chirp-identity.answer.json`, then run `exegenius submit 0060-audit-bluestein-chirp-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
