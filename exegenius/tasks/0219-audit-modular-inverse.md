# exegenius task 0219-audit-modular-inverse

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
- Discrete Fourier transform (also: normalized Fourier transform, transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Guard-width bound
- Transform layout
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set
- Indicator vector
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $M$ (record count), bound on `destination-rank`: The number of records in the stream.
- $M$ (change matrix), bound on `binary-change-of-basis`: The invertible m-by-m matrix over the binary field that specifies the change of basis.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $M$ (entry count), bound on `multidimensional-transform`: The number of entries of the array, the product of the axis lengths.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $M$ (backward contraction), bound on `gaussian-resampling`: A linear contraction from length-t vectors back to length-s vectors.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $\xi$ (first input value), bound on `butterfly`: The first of the two values that the butterfly takes as input.
- $M$ (modulus), bound on `centered-residue`: A positive integer, the modulus of the residue with respect to which the centered residue is taken.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $\xi$ (vector), bound on `bilinear-form`: A vector of $X$.
- $M$ (form matrix), bound on `bilinear-form`: The matrix of the bilinear form in the chosen coordinates.
- $\xi_1$ (first coordinate), bound on `bilinear-form`: The first coordinate of a vector $\xi$ in $\mathbb{Q}^2$.
- $\xi_2$ (second coordinate), bound on `bilinear-form`: The second coordinate of a vector $\xi$ in $\mathbb{Q}^2$.
- $S$ (triple), bound on `subspace-labels`: A second three-element subset, used for inner products.
- $\beta$ (bank index), bound on `subset-intersection-network`: A triple of triples that indexes one entry of a bank.
- $\xi$ (source vector), bound on `subset-intersection-network`: The vector of source-bank entries on one line, indexed by triples.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $\mu$ (constant mu), bound on `complex-phase-network`: The constant $(1-i)/2$.
- $M$ (two-point kernel), bound on `complex-phase-network`: The $2\times 2$ matrix $\lambda I+\mu X$ acting on one address bit.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $\mu$ (first value), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair, the first input of the two-point map.
- $\nu$ (second value), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair, the second input of the two-point map.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.
- $\mu$ (source dimension sum), bound on `rank-saving-recursion`: The sum of the dimensions of the source labels.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $\nu$ (axis index), bound on `padded-transform-box`: The index of an axis, running from 1 to d.
- $\beta$ (depth growth bound), bound on `guard-width-bound`: The fixed count $s+\eta$ bounding how much the depth bound grows at each recursive level.
- $\nu$ (power exponent), bound on `guard-width-bound`: The least integer $j \ge 1$ with $m^j \ge \beta$, which satisfies $\beta \le m^\nu$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $M$ (family size), bound on `coprime`: The number of integers in a family of integers, which counts the members of the family.

## Pages in the wiki

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Address field](address-field.md)
- [Exclusive or](xor.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`modular-inverse`)

````markdown
# Modular inverse

A modular inverse of an integer modulo a positive integer is a second integer whose product with the first is congruent to $1$ modulo the positive integer. The argument needs such inverses for the exponents of its Chinese-remainder map, which places the radix-digit coefficients on cyclic axes whose lengths are pairwise coprime.

Here $\beta$ is the integer to be inverted, $M \ge 1$ is the modulus, and $\mu$ is the inverse: an inverse is an integer $\mu$ for which $\beta\mu$ is [congruent](congruence-modulo.md) to $1$ modulo $M$, so the inverse is defined by that congruence.

An inverse of $\beta$ modulo $M$ exists exactly when $\beta$ and $M$ are [coprime](coprime.md). If $\beta\mu \equiv 1 \pmod M$, then $\beta\mu - 1 = \nu M$ for some integer $\nu$, so every common divisor of $\beta$ and $M$ divides $1$. Conversely, if $\beta$ and $M$ are coprime, Bézout's identity gives integers $\mu$ and $\nu$ with $\beta\mu + \nu M = 1$, and this $\mu$ is an inverse. The inverse is unique modulo $M$: if $\mu$ and $\mu'$ both work, then $M$ divides $\beta(\mu - \mu')$, and since $\beta$ and $M$ are coprime, $M$ divides $\mu - \mu'$.

For $M = 5$ and $\beta = 3$, the inverse is $\mu = 2$, since $3 \cdot 2 = 6 \equiv 1 \pmod 5$. For $M = 6$ and $\beta = 2$ there is no inverse: $2\mu$ is even for every $\mu$, and an even number is never congruent to $1$ modulo $6$.

The paper writes its lengths as $s_i$, and they are pairwise coprime:. Here $M_i$ denotes the length of the $i$-th axis, for $i = 1, 2, \dots$, and the letter $i$ indexes them only in this paragraph. Put $S = M_1 M_2 \cdots$ for their product, and $\pi_i = M_1 M_2 \cdots M_{i-1}$ for the product of the earlier lengths, with $\pi_1 = 1$. The paper calls $\pi_i$ an integer prefix product:. Each $\pi_i$ is coprime to $M_i$, so the inverse $\mu_i$ of $\pi_i$ modulo $M_i$ exists.

The paper's map sends the generator $\xi$ of a cyclic group of order $S$ to $\prod_i \xi_i^{\mu_i}$, where $\xi_i$ generates a cyclic group of order $M_i$, so $\xi_i^{M_i} = 1$. The image has order $S$ only because each exponent is a unit modulo $M_i$:. For $M_1 = 3$ and $M_2 = 5$, we have $\pi_2 = 3$ and $\mu_2 = 2$, so the image of $\xi$ is $\xi_1\xi_2^2$. Its $\nu$-th power is $\xi_1^{\nu}\xi_2^{2\nu}$, which equals $1$ exactly when $3 \mid \nu$ and $5 \mid 2\nu$, that is, when $15 \mid \nu$. So the image has order $15 = S$.
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

Write the answer to `exegenius/tasks/0219-audit-modular-inverse.answer.json`, then run `exegenius submit 0219-audit-modular-inverse` in the project directory. If submit rejects the answer, fix the answer and submit again.
