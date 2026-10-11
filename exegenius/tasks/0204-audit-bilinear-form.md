# exegenius task 0204-audit-bilinear-form

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
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
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

- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map between vector spaces over $F$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The matrix with ones on the diagonal and zeros elsewhere.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $T$ (padded box size), bound on `cost-table`: The power of two that sets the number of cells in the padded box.
- $K$ (chunk width), bound on `cost-table`: The number of bits in each address chunk.
- $\mathbb{F}_2$ (binary field), bound on `binary-field`: The field with the two elements 0 and 1, where addition is exclusive or and multiplication is AND.
- $T$ (triple), bound on `indicator-vector`: A three-element subset of the ground set $[h]$.
- $t_T$ (triple indicator vector), bound on `indicator-vector`: The indicator vector of the triple $T$: the 0-1 vector with entry 1 exactly at the positions of the elements of $T$.
- $K$ (scalar field), bound on `line-spanned-by-vector`: The field of scalars over which the vector space E is taken.
- $Q$ (second matrix), bound on `tensor-product`: A second matrix, which is copied once for each entry of P in the tensor product P \otimes Q.
- $\mathbb{Q}$ (rational numbers), bound on `matrix-rank`: The field of rational numbers, the fractions p/q with integers p and q nonzero.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $K$ (segment width), bound on `union-bound`: The number of bits in each segment, so that each guard value takes one of $2^{K-1}$ values.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $M$ (record count), bound on `destination-rank`: The number of records in the stream.
- $M$ (change matrix), bound on `binary-change-of-basis`: The invertible m-by-m matrix over the binary field that specifies the change of basis.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $M$ (entry count), bound on `multidimensional-transform`: The number of entries of the array, the product of the axis lengths.
- $X$ (input array), bound on `multidimensional-transform`: The input array, on which the transform acts.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than s.
- $M$ (backward contraction), bound on `gaussian-resampling`: A linear contraction from length-t vectors back to length-s vectors.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $T$ (second Gaussian map), bound on `gaussian-resampling`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $\xi$ (first input value), bound on `butterfly`: The first of the two values that the butterfly takes as input.
- $\eta$ (second input value), bound on `butterfly`: The second of the two values that the butterfly takes as input.
- $X$ (array of complex values), bound on `array-norm`: A finite array of complex values, the argument of the norm.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between a computed input and the exact input w.
- $M$ (modulus), bound on `centered-residue`: A positive integer, the modulus of the residue with respect to which the centered residue is taken.
- $U$ (output space), bound on `bilinear-map`: A vector space over the scalars, containing the outputs of the bilinear map.

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

## Page to audit (`bilinear-form`)

````markdown
# Bilinear form

A bilinear form is the structure that decides when two vectors are orthogonal. In the finite network, the [subspace labels](subspace-labels.md) are subspaces of one fixed bilinear space: space, and the [subset-intersection network](subset-intersection-network.md) carries these labels on its wires and gates.

Let $X$ be a vector space over a field $\mathbb{K}$ of scalars, such as $\mathbb{Q}$, $\mathbb{F}_2$ or $\mathbb{C}$. A bilinear form on $X$ is a special case of a [bilinear map](bilinear-map.md): it takes two vectors of $X$ and returns one scalar, and it is linear in each argument when the other is held fixed. The letters $\xi$ and $\eta$ stand for vectors of $X$. The form is written $\langle \cdot,\cdot\rangle$, and $\langle \xi,\eta\rangle$ is the scalar it assigns to the pair.

Two vectors $\xi$ and $\eta$ are *orthogonal* when $\langle \xi,\eta\rangle = 0$. Let $U$ be a subspace of $X$. Its orthogonal complement $U^\perp$ is the set of vectors $\xi$ in $X$ with $\langle \xi,\eta\rangle = 0$ for every $\eta$ in $U$. The form is *nondegenerate* when $X^\perp = 0$, that is, when the only vector orthogonal to every vector of $X$ is $0$.

Here $M$ is the matrix of the form in the chosen coordinates. In coordinates, a bilinear form is given by the matrices of [linear algebra basics](linear-algebra-basics.md): $\langle \xi,\eta\rangle = \xi^{\mathsf T} M \eta$, and the form is nondegenerate exactly when $M$ is invertible.

For example, take $X = \mathbb{Q}^2$, and write $\xi_1$ and $\xi_2$ for the first and second coordinates of $\xi$. The form $\langle \xi,\eta\rangle = \xi_1\eta_1 + \xi_2\eta_2$ is nondegenerate, since $\langle \xi,(1,0)\rangle = \xi_1$ and $\langle \xi,(0,1)\rangle = \xi_2$ both vanish only when $\xi = 0$. The form $\langle \xi,\eta\rangle = \xi_1\eta_1$ is degenerate: the vector $(0,1)$ satisfies $\langle (0,1),\eta\rangle = 0$ for every $\eta$, so it lies in $X^\perp$.

The paper's bit network uses a larger example., and the ground-set size is. Here $J$ is the all-one matrix, and the form is $\langle \xi,\eta\rangle = \xi^{\mathsf T}(I - J/9)\eta$, so $M = I - J/9$. The matrix $J$ has eigenvalues $100$ and $0$, so $M$ has eigenvalues $1$ and $1 - 100/9 = -91/9$, and neither is zero. For a triple $T$ of positions, let $t_T$ be its indicator vector. Then $t_T^{\mathsf T} t_T = 3$ and $t_T^{\mathsf T} J t_T = 9$, so $\langle t_T,t_T\rangle = 3 - 9/9 = 2$, as the paper records: The same computation gives $\langle t_S,t_T\rangle = |S\cap T| - 1$ for two triples $S$ and $T$.
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

Write the answer to `exegenius/tasks/0204-audit-bilinear-form.answer.json`, then run `exegenius submit 0204-audit-bilinear-form` in the project directory. If submit rejects the answer, fix the answer and submit again.
