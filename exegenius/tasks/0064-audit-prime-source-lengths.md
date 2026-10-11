# exegenius task 0064-audit-prime-source-lengths

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
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $n$ (input length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $q$ (radix prime), bound on `address-shear`: A fixed odd prime, the base of the digits.
- $d$ (value of D), bound on `address-shear`: The current value of D when m = 1.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $S$ (other triple), bound on `subspace-labels`: Another triple of the ground set, compared with $T$ through the form.
- $S$ (neighbouring triple), bound on `subset-intersection-network`: A triple that is a neighbour of the other triple $T$ when they share exactly one element.
- $T$ (neighbouring triple), bound on `subset-intersection-network`: A triple, here the triple whose indicator vector is $t_T$.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $s$ (smaller call count), bound on `rank-saving-recursion`: The number of smaller calls that one call makes.
- $b$ (kernel coefficient b), bound on `complex-phase-network`: The constant $(1-i)/2$ in the kernel $C = aI + bX$.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, a positive integer.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ complex numbers, the input to the transform.
- $q$ (transform length), bound on `gaussian-resampling`: the number of entries of the vector that a transform of length q acts on.
- $s$ (source length), bound on `gaussian-resampling`: the number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: the power-of-two number of entries in the resampled vector, greater than s.
- $\theta$ (relative gap), bound on `gaussian-resampling`: the relative gap t/s - 1 between the two lengths.
- $i$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, from 0 to r-1.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing 2r.
- $s$ (shift amount), bound on `polynomial-ring-mod-yr-plus-1`: The number of positions by which the coefficient list moves under multiplication by y^s, with 0 <= s < r.
- $b$ (imaginary numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the imaginary part of f after scaling by 2^{-p}.
- $e$ (imaginary numerator of g), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the imaginary part of g after scaling by 2^{-p}.
- $u$ (pair value (first)), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair that the two-point map takes as input.
- $d$ (axis bound), bound on `guard-width-bound`: An upper bound on the number D of selected axes in one layer.
- $s$ (smaller-call count), bound on `guard-width-bound`: The total number of smaller calls made by the network.
- $u$ (first coefficient), bound on `guard-width-bound`: The first of the two coefficients that the two-point map combines.
- $T$ (scratch chunk), bound on `packed-bit-addition`: The third address chunk, whose initial value is arbitrary and which is used as temporary space.
- $s$ (sequence length), bound on `cyclic-convolution`: The number of entries in each of the two input sequences.
- $x$ (formal variable), bound on `cyclic-convolution`: The indeterminate of the polynomial associated with a sequence, whose power x^j stands for position j.
- $d$ (axis count), bound on `chinese-remainder-map`: The number of cyclic axes, a count.
- $s_i$ (axis length), bound on `chinese-remainder-map`: The number of positions on axis $i$, a count.
- $S$ (total length), bound on `chinese-remainder-map`: The total number of positions, the product of the axis lengths, a count.
- $x$ (one-dimensional indeterminate), bound on `chinese-remainder-map`: The indeterminate of the one-dimensional cyclic polynomial ring.
- $q$ (transform length), bound on `bluestein-chirp-identity`: The number of entries in each input and output vector of the transform.
- $u$ (input vector), bound on `bluestein-chirp-identity`: The input vector of the transform, with entries $u_0$ through $u_{q-1}$.
- $x$ (first operand), bound on `bluestein-chirp-identity`: The first of the two vectors of length q in the cyclic convolution.
- $b$ (digit width), bound on `recovery-and-error`: The number of bits in each radix digit, where $b = \lceil \log_2 n \rceil$.
- $x$ (computed value), bound on `recovery-and-error`: A computed approximation of a true integer coefficient.
- $T$ (padded transform size), bound on `recovery-and-error`: The number of entries in the padded transform box, a power of two.
- $S$ (source-length product), bound on `recovery-and-error`: The product of the pairwise coprime source lengths.
- $q$ (vector length), bound on `transform-identity`: The number of entries of a vector to which the normalized transform F_q applies.
- $u$ (input vector), bound on `transform-identity`: A complex vector whose length is set by the transform applied to it.
- $s$ (source length), bound on `transform-identity`: The number of entries of the source vectors, the length of the source axis.
- $t$ (target length), bound on `transform-identity`: The number of entries of the target vectors, the length of the target axis.
- $\theta$ (relative gap), bound on `transform-identity`: The ratio t/s minus one, which measures how far apart the two lengths are.

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

## Page to audit (`prime-source-lengths`)

````markdown
# Prime source lengths

Prime source lengths are distinct odd primes, one for each axis of a multidimensional transform. They are chosen so that their product fills a fixed fraction of the padded box (defined below), which lets the [integer multiplication below n log n](main-theorem.md) algorithm fit every term in its cost table within the bound of the theorem.

Let $d$ be the number of axes, and for $i=1,\dots,d$ let $s_i$ be the prime source length of axis $i$. An *axis* is one coordinate direction of a multidimensional array. Axis $i$ is padded to the power of two $t_i$, so the padded array is a box with sides $t_1,\dots,t_d$.

### What the primes must satisfy

Two requirements fix how close each $s_i$ must be to $t_i$. The first is coprimality. The distinct primes supply pairwise coprime lengths to the [Chinese-remainder map](chinese-remainder-map.md), which relabels coefficient positions by mixed-radix digits. Distinct primes are pairwise coprime, and each $s_i$ is coprime to $t_i$.

The second is separation. Each ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md).: the product must be a large fraction of the box, and each ratio must be large enough for the resampling step.

### Finding the primes

Here $n$ is the bit length of each input, and $b=\lceil\log_2 n\rceil$ is the number of bits needed to write $n$. The padded box has size $T$, a power of two with $4n/b \le T < 8n/b$.. Thus the padded axis lengths take the two values $u/2$ and $u$, where $u$ is a power of two and the longer of the two lengths.

The counting tool is a prime-interval result. Here $x$ is a real number that sets the scale of the interval, $q$ is a prime in it, and $\eta$ is a slack fraction with $0<\eta<1/4$. For $x>e^{2/\eta}$, the interval $(1-2\eta)x < q \le (1-\eta)x$ contains at least $\eta x/(2\log x)$ primes, where $\log$ is the natural logarithm. The slack fraction is $\eta = 1/(4d)$, so $\eta x/(2\log x) = x/(8d\log x)$.

Apply this with $x = u/2$ and with $x = u$. The two intervals are disjoint, because $(1-\eta)u/2 < (1-2\eta)u$ for $\eta < 1/4$. Each interval contains more primes than there are axes:. So distinct odd primes can be chosen, one per axis, with
$$(1-2\eta)\,t_i < s_i \le (1-\eta)\,t_i.$$

The search is deterministic. The source bounds the total search time:.

### Product and separation

Multiplying the lower bounds on the $s_i$ gives a product $S = s_1 s_2\cdots s_d$ that fills most of the box. The source derives this from the $S/T > (1-1/(2d))^d > 1/2$ for $d \ge 2$, since $2\eta = 1/(2d)$. Because each $s_i < t_i$,.

For the separation, write $\theta_i = t_i/s_i - 1$. Since $s_i \le (1-\eta)t_i$ gives $t_i/s_i \ge 1/(1-\eta)$, we get $\theta_i \ge \eta/(1-\eta) > \eta$. This is the separation that the resampling step needs to be large.

### Worked example

Take $d = 2$, so $\eta = 1/8$, and $u = 16$, so the padded lengths are $t_1 = 16$ and $t_2 = 8$, and $T = 128$. For $t_1$, the interval $(12, 14]$ contains only $13$. For $t_2$, the interval $(6, 7]$ contains only $7$. So $s_1 = 13$ and $s_2 = 7$, with $S = 91$ and $64 < 91 < 128$. The ratio is $\theta_1 = 16/13 - 1 = 3/13 \approx 0.23$, which exceeds $\eta/(1-\eta) = 1/7 \approx 0.14$. At this size the counting lemma does not apply, so the example picks the primes by hand.
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

Write the answer to `exegenius/tasks/0064-audit-prime-source-lengths.answer.json`, then run `exegenius submit 0064-audit-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
