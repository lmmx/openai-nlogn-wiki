# exegenius task 0220-audit-address-shear

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
- Modular inverse (also: invertible modulo q)
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

- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $D$ (number of axes), bound on `transform-axis`: The number of axes of an array, which is the number of coordinates in each address.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $b$ (input bit), bound on `xor`: The second of the two bits that an XOR combines.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $V$ (logical volume), bound on `cost-table`: The number of logical bits in the padded box, $V = Tp$.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $\tau$ (exchange exponent), bound on `cost-table`: A fixed rational exponent between zero and one in the cost of chunk exchanges.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array being shifted.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set $[h]$.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $\tau$ (bound exponent), bound on `address-interchange`: A fixed number below one, the exponent in the running-time bound.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $W$ (volume divisor), bound on `address-interchange`: The number of equal pieces the volume is cut into at each level.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $h$ (ground-set size), bound on `indicator-vector`: The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $E$ (vector space), bound on `line-spanned-by-vector`: The vector space over K in which the line lies.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $q$ (address before the move), bound on `destination-rank`: The address of a record before the move.
- $h$ (chunk index), bound on `destination-rank`: The index of one of the three address chunks, taking values 1, 2 or 3.
- $M$ (record count), bound on `destination-rank`: The number of records in the stream.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $M$ (change matrix), bound on `binary-change-of-basis`: The invertible m-by-m matrix over the binary field that specifies the change of basis.
- $a$ (numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $b$ (second numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $D$ (axis count), bound on `multidimensional-transform`: The number of transform axes, a positive integer.
- $M$ (entry count), bound on `multidimensional-transform`: The number of entries of the array, the product of the axis lengths.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $h$ (output position), bound on `multidimensional-transform`: A position in the output array, with each coordinate below its axis length.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $h$ (input list), bound on `synthetic-transforms`: The list of $t$ records $(h_0,\dots,h_{t-1})$ that the transform takes as input.
- $Z$ (output list), bound on `synthetic-transforms`: The list of $t$ records $(Z_0,\dots,Z_{t-1})$ that the transform returns.
- $M$ (backward contraction), bound on `gaussian-resampling`: A linear contraction from length-t vectors back to length-s vectors.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $fg$, a polynomial with at most $2r-1$ coefficients $h_j$.
- $M$ (modulus), bound on `centered-residue`: A positive integer, the modulus of the residue with respect to which the centered residue is taken.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $V$ (first input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the first argument of the bilinear map.
- $W$ (second input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the second argument of the bilinear map.
- $M$ (form matrix), bound on `bilinear-form`: The matrix of the bilinear form in the chosen coordinates.
- $E$ (fixed bilinear space), bound on `subspace-labels`: The fixed bilinear space in which every label is a subspace.
- $H$ (Hadamard matrix), bound on `subspace-labels`: The normalized 2 by 2 Hadamard matrix.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $H$ (normalized Hadamard matrix), bound on `complex-phase-network`: The $2\times 2$ matrix with entries $\pm 1/\sqrt{2}$, a symmetric matrix squaring to $I$.
- $M$ (two-point kernel), bound on `complex-phase-network`: The $2\times 2$ matrix $\lambda I+\mu X$ acting on one address bit.
- $D$ (axis count), bound on `simultaneous-butterfly-layer`: The number of axes on which the layer acts, one axis per chunk; it counts the selected bits.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number D of selected axes in one layer, a count of axes.
- $W$ (role count), bound on `numerical-layer`: The number of roles in the network, a count of the wire roles among which rows are distributed.
- $W$ (wire count), bound on `rank-saving-recursion`: The number of wires in the network, which is also the number of roles among which the rows are distributed.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $d$ (axis count), bound on `padded-transform-box`: The number of axes of the transform, the count of coordinate directions along which the data is laid out.
- $d$ (axis bound), bound on `guard-width-bound`: A positive integer bound $d \ge D$ on the number of selected axes.
- $M$ (family size), bound on `coprime`: The number of integers in a family of integers, which counts the members of the family.
- $M$ (modulus), bound on `modular-inverse`: A positive integer, the modulus of the congruence.

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

## Page to audit (`address-shear`)

````markdown
# Address shear

An address shear is the map that adds one address field to another and leaves the second unchanged. Interchanging address chunks on tape reduces to shears, whose cost enters the main bound.

Here $q$ is a fixed odd prime. Here $m$ is the number of fields in each vector. The address fields $H$ and $D$ are vectors of $m$ fields, $H_1, \ldots, H_m$ and $D_1, \ldots, D_m$. Each field is a block of $b$ radix-$q$ digits (digits in base $q$),, so its values form the residue ring $\mathbb{Z}/q^b\mathbb{Z}$.

On a pair of address fields, the shear maps $(H, D)$ to $(H + D, D)$. More generally, a shear is given by a [matrix](linear-algebra-basics.md) $M$, a fixed rational $m \times m$ array: the shear with matrix $M$ sends $(H, D)$ to $(H + MD, D)$. The shear with matrix $M$ is counted by its [rational rank](matrix-rank.md) $a$, the number of independent rows over the rational numbers. The shear is computed with denominators [invertible modulo $q$](modular-inverse.md)..

The shear with matrix $M$. Each interchange costs $O(V u^{\tau})$ by the bound on [Address-field interchange](address-interchange.md), where $u$ is the field width in bits. So an address shear of rank $a$ is implemented by $a$ uses of one [Address-field interchange](address-interchange.md). For fixed $q$, $u$ is a constant multiple of $b$, so the total cost is $O(aVb^{\tau}) + O(V)$.

Why $a$ interchanges suffice: one. Hence $M = E_1\Pi E_2$, with $E_1$ and $E_2$ invertible lower-triangular and $\Pi$ a $0/1$ matrix with exactly $a$ ones. The procedure is transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.

, where $i$ and $j$ are the row and column of that one. That update is one interchange: $D_j \leftarrow D_j + H_i$, swap $H_i$ and $D_j$, then $D_j \leftarrow H_i - D_j$., so the total is $a$ interchanges plus $O(V)$ work.

When $m = 1$, write $h$ and $d$ for the current values of $H$ and $D$. On an initial pair $(h, d)$, For example, with $q = 3$, $b = 2$ (residues modulo $9$), $h = 3$ and $d = 5$: $D \leftarrow D + H$ gives $8$, the swap gives $H = 8$ and $D = 3$, and $D \leftarrow H - D$ gives $5$. So $(3, 5)$ becomes $(8, 5)$.

The shear is computed by the [Linear networks and frames](linear-network-frames.md) of the [bit procedure](bit-procedure.md). On every role, this shear is the [endpoint operator](endpoint-operator.md) of the bit procedure. On each role, this shear is realised as the endpoint operator of the network.

Shears are counted by rank because each costs its rank in interchanges. Each call acts on one, with $W$ the number of wires. times $m$, the comparison is with $Wm$, and Saving means the cost falls below the trivial bound by a power of the chunk width.
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

Write the answer to `exegenius/tasks/0220-audit-address-shear.answer.json`, then run `exegenius submit 0220-audit-address-shear` in the project directory. If submit rejects the answer, fix the answer and submit again.
