# exegenius task 0210-audit-numerical-layer

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

- $D$ (number of axes), bound on `transform-axis`: The number of axes of an array, which is the number of coordinates in each address.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network in the paper, at which a frame is placed.
- $v$ (vertex), bound on `linear-network-frames`: A source, gate or sink of the network.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $V$ (logical volume), bound on `cost-table`: The number of logical bits in the padded box, $V = Tp$.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $K$ (chunk width), bound on `cost-table`: The number of bits in each address chunk.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $\lambda'$ (butterfly exponent), bound on `cost-table`: A fixed rational exponent below one in the cost of a simultaneous butterfly round.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array being shifted.
- $v$ (vertex), bound on `network-gate-terminal`: A gate or terminal of the network, which carries the frame $D_v$.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $W$ (volume divisor), bound on `address-interchange`: The number of equal pieces the volume is cut into at each level.
- $K$ (scalar field), bound on `line-spanned-by-vector`: The field of scalars over which the vector space E is taken.
- $v$ (generating vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form the line.
- $\lambda$ (scalar multiplier), bound on `line-spanned-by-vector`: A scalar in K, an element of the scalar field, used to scale v.
- $\otimes$ (tensor product), bound on `tensor-product`: The operation that forms the block matrix P \otimes Q, also called the Kronecker product.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $K$ (segment width), bound on `union-bound`: The number of bits in each segment, so that each guard value takes one of $2^{K-1}$ values.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $\mathbb{D}$ (Gaussian dyadics), bound on `gaussian-dyadics`: The set of Gaussian dyadics.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $D$ (axis count), bound on `multidimensional-transform`: The number of transform axes, a positive integer.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $H_0$ (butterfly map), bound on `butterfly`: The two-point map sending a pair of values to their half-sum and half-difference.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $V$ (first input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the first argument of the bilinear map.
- $W$ (second input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the second argument of the bilinear map.
- $v$ (first argument), bound on `bilinear-map`: A vector of V, the first argument of the bilinear map.
- $v$ (basis vector), bound on `subspace-labels`: A vector of the orthonormal basis of the residual, the shift used by the kernel.
- $H$ (Hadamard matrix), bound on `subspace-labels`: The normalized 2 by 2 Hadamard matrix.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $H$ (normalized Hadamard matrix), bound on `complex-phase-network`: The $2\times 2$ matrix with entries $\pm 1/\sqrt{2}$, a symmetric matrix squaring to $I$.
- $\lambda$ (constant lambda), bound on `complex-phase-network`: The constant $(1+i)/2$.
- $\otimes$ (Kronecker product), bound on `complex-phase-network`: The Kronecker (tensor) product of matrices, so $H^{\otimes m}$ is the $m$-fold tensor power of $H$.
- $v$ (binary vector), bound on `complex-phase-network`: A binary vector; the vectors of the orthonormal basis $\mathcal{B}$ are such vectors.
- $D$ (axis count), bound on `simultaneous-butterfly-layer`: The number of axes on which the layer acts, one axis per chunk; it counts the selected bits.
- $K$ (chunk width), bound on `simultaneous-butterfly-layer`: The number of bits in each chunk, where a chunk is a run of consecutive address bits.
- $H_0$ (two-point map), bound on `simultaneous-butterfly-layer`: The map sending a pair of values to their half-sum and half-difference.

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

## Page to audit (`numerical-layer`)

````markdown
# Numerical layer

A numerical layer is one stage of the transform calculation, in which a simultaneous butterfly is applied to a chosen set of selected axes of the array. The numerical layer computes the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) on its selected bits, in one pass rather than one axis at a time.

Each address of the array is written as $D$ consecutive chunks of $K$ address bits, where $K$ is the number of address bits in each chunk., that is, a polynomial with $r$ complex coefficients stored as its coefficient list. In every chunk one bit is selected, all at one offset:. So the $D$ selected bits sit at the same position within their chunks.

Applying the two-point map $H_0(u,v) = ((u+v)/2, (u-v)/2)$ to one selected bit combines each pair of records whose addresses differ only in that bit. Applying it to all $D$ selected bits at once is the tensor product $H_0^{\otimes D}$, which combines each group of $2^D$ records that agree outside the selected bits. The map acts on each coefficient separately and fixes every other address bit.

For example, take $D = 2$ and four records whose first coefficients, at the settings $(0,0)$, $(0,1)$, $(1,0)$ and $(1,1)$ of the two selected bits, are $1, 3, 5, 7$. Then $H_0^{\otimes 2}$ gives the first coefficients $4, -1, -2, 0$ at the same four settings. At the setting $(0,1)$ the value is $(1-3+5-7)/4 = -1$.

Doing the same work one axis at a time is more expensive:, each of which reads every stored bit. The layer does all $D$ selected bits in one pass.

Here $d$ is an upper bound on the number $D$ of selected axes in a layer. Here $\lambda'$ is a fixed exponent below one, so that the cost is $O(V d^{\lambda'})$.. Since $\lambda' < 1$, the cost grows more slowly than linearly in $d$.

The layer is computed exactly. Its intermediate values are Gaussian dyadics $\mathbb{D}$, and

This is what the argument needs from the layer. The argument needs each recursive call to make fewer than $Wm$ smaller calls, where $W$ is the number of roles in the network.. The recursive contribution then grows by the factor, so each recursive level saves a power.
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

Write the answer to `exegenius/tasks/0210-audit-numerical-layer.answer.json`, then run `exegenius submit 0210-audit-numerical-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
