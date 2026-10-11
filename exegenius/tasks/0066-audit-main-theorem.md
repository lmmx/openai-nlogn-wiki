# exegenius task 0066-audit-main-theorem

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
- Carry propagation
- Exact coefficient recovery

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $y$ (second input string), bound on `exact-integer-multiplication`: A binary string of length n, the second input to the product.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each input string.
- $n$ (input length), bound on `n-log-n-conjecture`: The number of bits in each of the two input integers.
- $A$ (multiplication machine), bound on `n-log-n-conjecture`: A fixed Turing machine that computes exact products.
- $T_A$ (running time), bound on `n-log-n-conjecture`: The worst-case running time of A on inputs of two n-bit integers, as a number of steps.
- $\lg n$ (binary logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm of n, rounded up to an integer and never below 1.
- $\kappa$ (saving exponent), bound on `n-log-n-conjecture`: The specific positive constant by which the main theorem's running time falls below n lg n.
- $n$ (input length), bound on `radix-digit-convolution`: The number of bits in each input.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $y$ (second input), bound on `radix-digit-convolution`: The second input, a binary string of $n$ bits.
- $a$ (Gaussian integer numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $y$ (indeterminate), bound on `signed-packing`: The indeterminate of the polynomial ring, the variable in which the packed polynomials are written.
- $r$ (coefficient count), bound on `signed-packing`: The number of coefficients of each polynomial being packed.
- $n$ (input length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $A$ (fixed machine), bound on `fixed-tape-model`: A fixed multiplication machine, whose alphabet and tape count do not depend on the input.
- $T_A$ (running time), bound on `fixed-tape-model`: The worst-case running time of machine A as a function of the input length n.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $y$ (second field), bound on `address-interchange`: The value of the second field, a block of bits at matching positions.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $a$ (bank index), bound on `subset-intersection-network`: An index $a=(a_1,a_2,a_3)$ of one entry of a bank, a triple of triples.
- $T$ (neighbouring triple), bound on `subset-intersection-network`: A triple, here the triple whose indicator vector is $t_T$.
- $a$ (kernel coefficient a), bound on `complex-phase-network`: The constant $(1+i)/2$ in the kernel $C = aI + bX$.
- $x$ (binary address), bound on `complex-phase-network`: A binary address, a vector in $\mathbb{F}_2^m$.
- $v$ (residual basis vector), bound on `complex-phase-network`: A vector of the residual basis $B$.
- $A$ (forward contraction), bound on `gaussian-resampling`: the linear contraction from length-s vectors to length-t vectors that appears in the identity.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The polynomial variable whose powers serve as the roots of unity.
- $a$ (shift amount), bound on `synthetic-transforms`: The number of places a signed shift moves each coefficient, an integer with 0 \le a < 2r.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $a$ (real numerator of f), bound on `polynomial-ring-convolution`: The integer polynomial whose coefficients give the real part of f after scaling by 2^{-p}.
- $v$ (pair value (second)), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair that the two-point map takes as input.
- $v$ (second coefficient), bound on `guard-width-bound`: The second of the two coefficients that the two-point map combines.
- $T$ (scratch chunk), bound on `packed-bit-addition`: The third address chunk, whose initial value is arbitrary and which is used as temporary space.
- $x$ (formal variable), bound on `cyclic-convolution`: The indeterminate of the polynomial associated with a sequence, whose power x^j stands for position j.
- $x$ (one-dimensional indeterminate), bound on `chinese-remainder-map`: The indeterminate of the one-dimensional cyclic polynomial ring.
- $x$ (first operand), bound on `bluestein-chirp-identity`: The first of the two vectors of length q in the cyclic convolution.
- $y$ (second operand), bound on `bluestein-chirp-identity`: The second of the two vectors of length q in the cyclic convolution.
- $a$ (chirp), bound on `bluestein-chirp-identity`: The chirp vector, whose entry at each integer m is e^{\pi i m^2/q}.
- $l$ (second term position), bound on `phase-twist`: The position of the coefficient taken from the second record in a product.
- $x$ (computed value), bound on `recovery-and-error`: A computed approximation of a true integer coefficient.
- $T$ (padded transform size), bound on `recovery-and-error`: The number of entries in the padded transform box, a power of two.
- $v$ (second vector), bound on `transform-identity`: A complex vector whose length is set by the transform applied to it.
- $A$ (source map), bound on `transform-identity`: A linear contraction from length-s vectors to length-t vectors.
- $T$ (padded box size), bound on `prime-source-lengths`: The size of the padded box, the number of positions in it.
- $n$ (input bit length), bound on `prime-source-lengths`: The number of bits in each input integer.
- $x$ (interval scale), bound on `prime-source-lengths`: The real number that sets the scale of the prime interval.
- $n$ (input bit length), bound on `carry-propagation`: The number of bits in each input.

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

## Page to audit (`main-theorem`)

````markdown
# Integer multiplication below n log n

The main theorem of the argument is a single deterministic machine that multiplies two binary integers exactly, in a number of steps that is the input length times a power of its logarithm, with an exponent just below one. Every step of the argument exists to establish this bound, and the steps below show how each one contributes to it.

## The statement

Let $n$ be the number of bits in each of the two input integers. Let $\kappa = 2^{-182}$, a fixed positive constant. Write $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$ for the base-two logarithm of $n$, rounded up and at least 1. The inputs are $x$ and $y$, two binary strings of length $n$, written as $x\#y$. For a binary string $x$, $\mathrm{val}(x)$ denotes its nonnegative integer value, with the leftmost bit most significant.

 finite number of one-dimensional tapes that computes the exact product. The theorem is stated for the [fixed-tape machine model](fixed-tape-model.md): one machine with a fixed finite alphabet and a fixed finite number of tapes. Call this machine $A$, and let $T_A(n)$ be its worst-case number of steps on inputs of length $n$.

The output must be the $2n$-bit binary representation of $\mathrm{val}(x)\,\mathrm{val}(y)$. For example, take $n = 4$, $x = 1011$ and $y = 0110$. Then $\mathrm{val}(x) = 11$ and $\mathrm{val}(y) = 6$, so the product is $66$, and the output is the eight-bit string $01000010$. The theorem says that $T_A(n) = O(n(\lg n)^{1-\kappa})$ for every $n \ge 1$.

; the algorithm is intended to establish a bit-complexity bound.

## Why the bound is a real improvement

Schönhage and Strassen. It refutes the [n log n optimality conjecture](n-log-n-conjecture.md) in this model.

The new bound is smaller than $n\lg n$ by the factor $(\lg n)^{-\kappa}$, which tends to zero as $n$ grows. Since $\kappa$ is so small, this factor is below one half only when $\lg n > 2^{2^{182}}$. The saving is therefore real but appears only at input lengths far beyond any practical size.

The theorem is stated for every input length, not only for large ones. Inputs below a fixed cutoff are multiplied by schoolbook multiplication, and the cutoff is absorbed into the constant.

The saving is strict because of the recursion. The machine splits each recursive call into smaller calls on streams of a fraction of the volume, and each level of recursion increases the cost by a factor smaller than the factor by which the parameter grows. The power saving comes from the [rank-saving recursion](rank-saving-recursion.md), in which each call splits into smaller calls on streams of a fraction of the volume.

## Why the method is needed

 Address rearrangements and transform layers must therefore be cheaper than a scan.

## How the argument proceeds

Each step is developed on the linked page.

1. The first step reduces multiplication to a [radix-digit convolution](radix-digit-convolution.md) of short integer coefficients, obtained by splitting each input into radix digits.
2. [Gaussian resampling](gaussian-resampling.md).
3. One coordinate is stored as the coefficient list of a [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md)., and.
4. The transforms are [synthetic transforms](synthetic-transforms.md)..
5. An [address-field interchange](address-interchange.md) exchanges two address fields.
6. A [simultaneous butterfly layer](simultaneous-butterfly-layer.md) acts at once..
7. Each procedure is a [linear network](linear-network-frames.md)..
8. The transforms are laid out by a [transform layout](transform-layout.md) that places the selected bits of all axes at a common offset, so that the butterfly layer applies to each transform round.
9. The machine adds the selected bits of the address chunks by [packed selected-bit addition](packed-bit-addition.md), which uses cyclic shifts of whole chunks and a deterministic correction.
10. The radix-digit coefficients are placed on distinct prime cyclic axes by a [Chinese-remainder map](chinese-remainder-map.md) that preserves convolution. It uses [prime source lengths](prime-source-lengths.md): distinct odd primes chosen close to the powers of two..
11. The method keeps the source and target coordinate permutations inside the [transform identity with retained permutations](transform-identity.md), so they need not be executed as sorts.
12. [Bluestein's chirp identity](bluestein-chirp-identity.md) into normalized cyclic convolution.
13. The last cyclic coordinate is converted by a [phase twist](phase-twist.md) into a coordinate of a polynomial ring. ring.
14. The remaining axes are handled by [convolution over the polynomial ring](polynomial-ring-convolution.md), which computes the convolution with two forward synthetic transforms, a pointwise product and an opposite transform.
15. The algorithm recovers the coefficients by rounding, which is justified by [exact coefficient recovery](recovery-and-error.md): the error is below one half..
16. [Carry propagation](carry-propagation.md) turns the recovered coefficients into the exact binary product.

The parameters are chosen so that each term of the cost table fits the bound. $O(n(\log n)^{1-\kappa})$.
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

Write the answer to `exegenius/tasks/0066-audit-main-theorem.answer.json`, then run `exegenius submit 0066-audit-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
