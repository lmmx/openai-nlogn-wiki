# exegenius task 0212-audit-transform-round

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
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $D$ (number of axes), bound on `transform-axis`: The number of axes of an array, which is the number of coordinates in each address.
- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar, an element of the field $F$.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $c$ (path end vertex), bound on `endpoint-operator`: The last of three vertices on a path through the network.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $c$ (positive constant), bound on `limit-inferior`: A positive real constant in the lower bound and its negation.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $\ell$ (log axis length), bound on `cost-table`: The base-2 logarithm of $r$.
- $c$ (chunk exponent), bound on `cost-table`: A fixed positive rational exponent that sets $K$ relative to $d$.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index of output coordinates, running from 0 to q-1.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $D$ (axis count), bound on `multidimensional-transform`: The number of transform axes, a positive integer.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $H_0$ (butterfly map), bound on `butterfly`: The two-point map sending a pair of values to their half-sum and half-difference.
- $\eta$ (second input value), bound on `butterfly`: The second of the two values that the butterfly takes as input.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between a computed input and the exact input w.
- $e$ (integer), bound on `congruence-modulo`: An integer, the other of the two integers compared by congruence.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in $[-B/2, B/2)$ that is congruent to $f(B)\,g(B)$ modulo $B$.
- $\ell$ (coordinate index), bound on `cyclic-coordinate`: The index naming one cyclic coordinate, running from 1 to d.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $X$.
- $H$ (Hadamard matrix), bound on `subspace-labels`: The normalized 2 by 2 Hadamard matrix.
- $\beta$ (bank index), bound on `subset-intersection-network`: A triple of triples that indexes one entry of a bank.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of target-bank entries on one line, indexed by triples.
- $\ell$ (ground element), bound on `subset-intersection-network`: An element of the ground set, indexing a central wire.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $H$ (normalized Hadamard matrix), bound on `complex-phase-network`: The $2\times 2$ matrix with entries $\pm 1/\sqrt{2}$, a symmetric matrix squaring to $I$.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $D$ (axis count), bound on `simultaneous-butterfly-layer`: The number of axes on which the layer acts, one axis per chunk; it counts the selected bits.
- $\nu$ (second value), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair, the second input of the two-point map.
- $H_0$ (two-point map), bound on `simultaneous-butterfly-layer`: The map sending a pair of values to their half-sum and half-difference.
- $\ell$ (log record length), bound on `transform-layout`: The base-two logarithm of $r$, which is the number of address bits in a long axis.
- $\ell$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, counting the selected axes of a numerical layer or the digits of an address field.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.

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

## Page to audit (`transform-round`)

````markdown
# Transform round

A transform round is one stage of the [multidimensional transform](multidimensional-transform.md) on a set of participating axes. In it, every participating axis takes one butterfly step at the same time, and the twiddles those steps need are applied afterwards as one operation on each record. It is the basic step of the transforms used for convolution over the polynomial ring.

A *butterfly* on one axis replaces each pair of entries that differ only in one address bit by the pair's half-sum and half-difference. A *twiddle* is a power of $y$ by which a record is multiplied after a butterfly.

Consider a round on the $D$ participating axes. Here $i$ indexes the participating axes, and the letter changes meaning from its use for digit positions. Here $\ell_i$ is the current recursive length of axis $i$, the number of entries that axis holds at the level the round processes. Here $\beta_i$ is the branch bit that the round writes on axis $i$, the bit recording which output of the butterfly the entry is. Here $\nu_i$ is the index of the twiddle on axis $i$, with $0 \le \nu_i < \ell_i/2$, encoded by the address bits not yet processed.

The twiddle on axis $i$ is determined by that axis alone. that axis’s address bits. Because each twiddle commutes with the butterflies on the other axes, the axis steps can be reordered:.

The parallel butterfly $\Lambda$ is the tensor product of $H_0$ over the participating axes. A transform round computes its butterfly by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which applies $\Lambda$ to the selected bits in one pass. Here $\eta$ is the twiddle exponent at each address, an integer taken modulo $2r$, given by

$$
\eta = -\sum_{i} \frac{2r}{\ell_i}\,\beta_i\,\nu_i \pmod{2r},
$$

where the sum runs over the $D$ participating axes. The recordwise twiddle $\Gamma_\eta$ multiplies each record at its address by $y^\eta$. coefficient values.

Multiplication by $y^\eta$ modulo $y^r+1$ rearranges coefficients without arithmetic on their values. Write $\eta = er + s$ with $0 \le s < r$. Since $y^r = -1$, multiplying by $y^\eta$ is multiplying by $y^s$ and then applying the sign $(-1)^e$, and multiplying by $y^s$ moves each coefficient up $s$ places and negates the coefficients that pass the top.

As a small example, take $r = 4$, $D = 2$, $\ell_1 = \ell_2 = 4$, $\beta_1 = 1$, $\nu_1 = 1$, $\beta_2 = 0$, and $\nu_2 = 1$. Then $\eta = -(2\cdot 1\cdot 1 + 2\cdot 0\cdot 1) \bmod 8 = 6$. Modulo $y^4+1$ we have $y^6 = -y^2$, so the record $c_0 + c_1 y + c_2 y^2 + c_3 y^3$ becomes $c_2 + c_3 y - c_0 y^2 - c_1 y^3$. Its coefficient list $(c_0, c_1, c_2, c_3)$ becomes $(c_2, c_3, -c_0, -c_1)$.

A contraction is a linear map that does not increase the norm of an array, and an isometry is one that preserves it., so the round as a whole does not increase the norm.
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

Write the answer to `exegenius/tasks/0212-audit-transform-round.answer.json`, then run `exegenius submit 0212-audit-transform-round` in the project directory. If submit rejects the answer, fix the answer and submit again.
