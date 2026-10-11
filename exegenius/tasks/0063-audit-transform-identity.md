# exegenius task 0063-audit-transform-identity

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
- Exact coefficient recovery

## Symbols bound on earlier pages

- $A$ (multiplication machine), bound on `n-log-n-conjecture`: A fixed Turing machine that computes exact products.
- $q$ (digits per input), bound on `radix-digit-convolution`: The number of radix-$2^b$ digits in each input.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $j$ (coefficient position), bound on `radix-digit-convolution`: The position of a product coefficient, running from $0$ to $2q-2$.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: A non-negative integer, so that $2^k$ is the denominator.
- $j$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from 0 to r-1.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so every coefficient has magnitude at most 2^p.
- $B$ (block base), bound on `signed-packing`: The base 2^{4p} of the integer encoding, one block of 4p bits per coefficient.
- $A$ (fixed machine), bound on `fixed-tape-model`: A fixed multiplication machine, whose alphabet and tape count do not depend on the input.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $q$ (radix prime), bound on `address-shear`: A fixed odd prime, the base of the digits.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $s$ (smaller call count), bound on `rank-saving-recursion`: The number of smaller calls that one call makes.
- $B$ (residual basis), bound on `complex-phase-network`: An orthonormal basis of the residual $E$ of an edge.
- $v$ (residual basis vector), bound on `complex-phase-network`: A vector of the residual basis $B$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, a positive integer.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ complex numbers, the input to the transform.
- $j$ (input index), bound on `discrete-fourier-transform`: An index of the input coordinates, running from 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: An index of the output coordinates, running from 0 to q-1.
- $F_q$ (Fourier transform), bound on `discrete-fourier-transform`: The discrete Fourier transform of length q, the map sending u to F_q u.
- $q$ (transform length), bound on `gaussian-resampling`: the number of entries of the vector that a transform of length q acts on.
- $F_q$ (normalized transform), bound on `gaussian-resampling`: the normalized discrete Fourier transform of length q.
- $s$ (source length), bound on `gaussian-resampling`: the number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: the power-of-two number of entries in the resampled vector, greater than s.
- $\theta$ (relative gap), bound on `gaussian-resampling`: the relative gap t/s - 1 between the two lengths.
- $\alpha$ (Gaussian width), bound on `gaussian-resampling`: a positive integer parameter that sets the width of the Gaussian weights.
- $p$ (precision), bound on `gaussian-resampling`: a positive integer precision parameter of the approximations.
- $P_s$ (source reordering), bound on `gaussian-resampling`: the permutation of length-s vectors that reorders their entries by multiplying each position by t modulo s.
- $P_t$ (target reordering), bound on `gaussian-resampling`: the permutation of length-t vectors that reorders their entries by multiplying each position by -s modulo t.
- $A$ (forward contraction), bound on `gaussian-resampling`: the linear contraction from length-s vectors to length-t vectors that appears in the identity.
- $B$ (backward contraction), bound on `gaussian-resampling`: the linear contraction from length-t vectors to length-s vectors that appears in the identity.
- $i$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, from 0 to r-1.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing 2r.
- $j$ (output index), bound on `synthetic-transforms`: The index of an entry of the transform, from 0 to t-1.
- $k$ (input index), bound on `synthetic-transforms`: The index of an entry of the input, from 0 to t-1.
- $s$ (shift amount), bound on `polynomial-ring-mod-yr-plus-1`: The number of positions by which the coefficient list moves under multiplication by y^s, with 0 <= s < r.
- $p$ (fractional bits), bound on `polynomial-ring-convolution`: The number of fractional bits of each coefficient, so that every real and imaginary coefficient part of a record is a multiple of 2^{-p}.
- $e$ (imaginary numerator of g), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the imaginary part of g after scaling by 2^{-p}.
- $B_0$ (packing base), bound on `polynomial-ring-convolution`: The power of two at which integer polynomials are evaluated when they are packed into integers, one base-B_0 block per coefficient.
- $u$ (pair value (first)), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair that the two-point map takes as input.
- $v$ (pair value (second)), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair that the two-point map takes as input.
- $p$ (precision), bound on `guard-width-bound`: The number of fractional bits carried by each input coefficient.
- $B$ (per-level growth bound), bound on `guard-width-bound`: A fixed count, s plus 64(W+m+1)^3, that bounds how much the depth grows at each recursive level.
- $s$ (smaller-call count), bound on `guard-width-bound`: The total number of smaller calls made by the network.
- $u$ (first coefficient), bound on `guard-width-bound`: The first of the two coefficients that the two-point map combines.
- $v$ (second coefficient), bound on `guard-width-bound`: The second of the two coefficients that the two-point map combines.
- $s$ (sequence length), bound on `cyclic-convolution`: The number of entries in each of the two input sequences.
- $k$ (output position), bound on `cyclic-convolution`: An index in the range 0 to s-1 naming an entry of the cyclic convolution.
- $j$ (summation index), bound on `cyclic-convolution`: The index running over the entries of f in the cyclic convolution sum.
- $k$ (coefficient index), bound on `chinese-remainder-map`: An ordinary coefficient index in the range $0 \le k < S$.
- $q$ (transform length), bound on `bluestein-chirp-identity`: The number of entries in each input and output vector of the transform.
- $u$ (input vector), bound on `bluestein-chirp-identity`: The input vector of the transform, with entries $u_0$ through $u_{q-1}$.
- $j$ (input position), bound on `bluestein-chirp-identity`: An index into the input vector, an integer from 0 to q-1.
- $k$ (output position), bound on `bluestein-chirp-identity`: An index into the output vector, an integer from 0 to q-1.
- $F_q$ (transform), bound on `bluestein-chirp-identity`: The discrete Fourier transform of length q, normalized by 1/q.
- $\cdot$ (coordinatewise product), bound on `bluestein-chirp-identity`: The product of two vectors of length q taken entry by entry.
- $j$ (coefficient position), bound on `phase-twist`: The position of a coefficient in a record, counted from 0.
- $k$ (first term position), bound on `phase-twist`: The position of the coefficient taken from the first record in a product.
- $p$ (fractional bit count), bound on `recovery-and-error`: The number of binary places kept after the point in each stored value.

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

## Page to audit (`transform-identity`)

````markdown
# Transform identity with retained permutations

This identity computes its transforms by [Gaussian resampling](gaussian-resampling.md), which replaces a transform of arbitrary length by transforms whose axis lengths are powers of two. The usual implementation of that replacement. The identity instead keeps both coordinate permutations inside the transform formula, so that they can cancel instead of being executed. It is the resampling step of [Integer multiplication below n log n](main-theorem.md).

The permutations are needed because the two sides of the resampling have different shapes. transforms use powers of two, and Gaussian resampling connects these two shapes.

The letters $u$ and $v$ denote complex vectors, and $q$ is the length of such a vector, the number of its entries. The indices $j$ and $k$ run over the entries, taken modulo $q$. $F_q$ is the normalized discrete Fourier transform of length $q$: for $u$ it returns the vector $F_q u$ with entries
$$(F_q u)_k = \frac{1}{q}\sum_{j=0}^{q-1} u_j\, e^{-2\pi i jk/q}.$$
A linear map is a contraction if it does not increase the maximum modulus of a vector. A coordinate permutation $\Pi$ rearranges the entries of a vector.

The integer $s$ is the length of the source axis and $t$ is the length of the target axis, with $s<t$ and $\gcd(s,t)=1$. The permutations $P_s$ and $P_t$ reorder the entries of length-$s$ and length-$t$ vectors by $(P_s u)_j = u_{tj}$ and $(P_t v)_k = v_{-sk}$, and coprimality makes each map a bijection. For example, with $s=3$ and $t=5$, the values $5j \bmod 3$ for $j=0,1,2$ are $0,2,1$, so $(P_3 u)=(u_0,u_2,u_1)$; the values $-3k \bmod 5$ for $k=0,\dots,4$ are $0,2,4,1,3$, so $(P_5 v)=(v_0,v_2,v_4,v_1,v_3)$.

The maps $A$ and $B_0$ are linear contractions, with $A$ taking length-$s$ vectors to length-$t$ vectors and $B_0$ taking length-$t$ vectors to length-$s$ vectors. Here $p$ is the precision, which fixes the grid $2^{-p}$ of stored values, and $\alpha$ is a fixed integer parameter with $2 \le \alpha < p$. The number $\theta = t/s-1$ is the relative gap between $t$ and $s$, and the identity needs $\theta > p/\alpha^4$. The identity is Lemma 19 of the source:
$$P_s F_s = 2^{2\alpha^2}\, B_0\, P_t F_t\, A.$$
Both permutations stay inside this identity, so neither is executed as a sort. The source charges the sorts that the original proof uses for these permutations,

The identity is useful because permutations pass through pointwise products. For a coordinate permutation $\Pi$ and vectors $u$ and $v$ of the same length, $(\Pi u)\cdot(\Pi v)=\Pi(u\cdot v)$, where $\cdot$ is the entrywise product: products. A permutation applied to two transforms before their product can therefore be moved after it, and two such permutations cancel. This is how transforms, their pointwise product, and the opposite-sign transform.
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

Write the answer to `exegenius/tasks/0063-audit-transform-identity.answer.json`, then run `exegenius submit 0063-audit-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
