# exegenius task 0214-audit-normalized-cyclic-convolution

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

- $k$ (output position), bound on `convolution`: The position of an entry of the output sequence c.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $k$ (term index), bound on `limit-inferior`: The position of a term in the sequence $x$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $k$ (offset), bound on `cyclic-shift`: The integer, taken modulo L, by which the cyclic shift rotates the block.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $k$ (level count), bound on `address-interchange`: The number of recursion levels, log base m of the field width.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $f$ (selected position count), bound on `union-bound`: The number of selected bit positions $j_0, \dots, j_{f-1}$ in the packed operation.
- $k$ (key), bound on `stable-radix-sort`: The key of a record, written as a string of $w$ bits.
- $q$ (address before the move), bound on `destination-rank`: The address of a record before the move.
- $k$ (denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of an element of $\mathbb{D}$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $F_q$ (discrete Fourier transform), bound on `discrete-fourier-transform`: The map of length q sending a vector of q complex numbers to its transform.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $k$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a record, running from 0 to r-1.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The fixed monic polynomial with complex coefficients by which the ring is reduced.
- $f$ (packed polynomial f), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, one of the two inputs that are packed.
- $g$ (packed polynomial g), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, the second input that is packed.
- $f_j$ (coefficient of f), bound on `signed-packing`: The integer coefficient of $y^j$ in $f$.
- $f$ (first input sequence), bound on `cyclic-convolution`: The first of the two sequences, of length s.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences, of length s.
- $\ast$ (cyclic convolution), bound on `cyclic-convolution`: The cyclic convolution operation, whose result f \ast g is the sequence with entries (f \ast g)_k.
- $f$ (function of addresses), bound on `subspace-labels`: A function of addresses; the letter changes meaning here.
- $S$ (triple), bound on `subspace-labels`: A second three-element subset, used for inner products.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
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

## Page to audit (`normalized-cyclic-convolution`)

````markdown
# Normalized cyclic convolution

A normalized cyclic convolution is a scaling of the [Cyclic convolution](cyclic-convolution.md) $f \ast g$ by $1/s$. Its purpose is to make a [Discrete Fourier transform](discrete-fourier-transform.md) turn convolution into a pointwise product. On the way to the target, [Bluestein's chirp identity](bluestein-chirp-identity.md) rewrites the middle transform, including its target permutation, as a normalized cyclic convolution.

For sequences $f$ and $g$ of length $s$, the entries of $f \ast g$ are
$$(f \ast g)_k = \sum_{j=0}^{s-1} f_j\, g_{(k-j) \bmod s}, \qquad 0 \le k \le s-1,$$
where $f_j$ is the entry of $f$ at position $j$, and the index $(k-j) \bmod s$ wraps around modulo $s$.

We write $f \circledast g$ for the normalized cyclic convolution of $f$ and $g$, the cyclic convolution $f \ast g$ divided by $s$.
$$f \circledast g = \frac{1}{s}\,(f \ast g).$$

Let $F_s$ be the normalized discrete Fourier transform of length $s$, which is the $F_q$ of the transform page with $q = s$. A normalized cyclic convolution is turned into pointwise products by the [Discrete Fourier transform](discrete-fourier-transform.md) $F_s$, as the rule below states. The source states the rule for the unnormalized product, writing the length as $S$:

With $S = s$, the rule says $F_s(f \ast g) = s\,(F_s f)(F_s g)$. Dividing both sides by $s$ gives the form used here:
$$F_s(f \circledast g)_k = (F_s f)_k\,(F_s g)_k, \qquad 0 \le k \le s-1.$$
That is, the transform of the normalized product is the pointwise product of the transforms of $f$ and $g$, meaning entry $k$ of one multiplied by entry $k$ of the other.

Take $s = 2$, $f = (1, 2)$ and $g = (3, 4)$. Then $(f \ast g)_0 = 1 \cdot 3 + 2 \cdot 4 = 11$ and $(f \ast g)_1 = 1 \cdot 4 + 2 \cdot 3 = 10$, so $f \circledast g = (11/2,\ 5)$. For $s = 2$ the transform is $F_2 u = \left(\frac{u_0 + u_1}{2},\ \frac{u_0 - u_1}{2}\right)$, so $F_2 f = (3/2,\ -1/2)$ and $F_2 g = (7/2,\ -1/2)$, whose entrywise product is $(21/4,\ 1/4)$. Directly, $F_2(f \circledast g) = \left(\frac{11/2 + 5}{2},\ \frac{11/2 - 5}{2}\right) = (21/4,\ 1/4)$, as the rule predicts.

This is the step the source uses. It states that so the transform step reduces to one cyclic convolution and two pointwise phase multiplications.
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

Write the answer to `exegenius/tasks/0214-audit-normalized-cyclic-convolution.answer.json`, then run `exegenius submit 0214-audit-normalized-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
