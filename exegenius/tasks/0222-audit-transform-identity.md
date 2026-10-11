# exegenius task 0222-audit-transform-identity

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
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Packed selected-bit addition
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

- $k$ (output position), bound on `convolution`: The position of an entry of the output sequence c.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map between vector spaces over $F$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m\times m$ matrix with entries in $F$.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $B$ (candidate inverse matrix), bound on `linear-algebra-basics`: A matrix that is a two-sided inverse of the matrix $A$ when $A$ is invertible.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $w$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $w$ (input role), bound on `endpoint-operator`: An input role of the network, whose route starts at its source vertex.
- $k$ (term index), bound on `limit-inferior`: The position of a term in the sequence $x$.
- $A$ (fixed machine), bound on `limit-inferior`: A fixed multiplication machine whose running time is studied.
- $N$ (input length threshold), bound on `limit-inferior`: A threshold on input length, below which the bound is not required.
- $A$ (multiplication machine), bound on `fixed-tape-model`: A fixed Turing machine that multiplies two integers, whose running time is T_A.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $T$ (padded box size), bound on `cost-table`: The power of two that sets the number of cells in the padded box.
- $\alpha$ (line cost factor), bound on `cost-table`: The factor, of order $p^{1/4+\epsilon/2}$, in the cost of the Gaussian line maps.
- $N$ (input length), bound on `established-multiplier`: The number of bits in each of the two input integers of a multiplication.
- $L$ (block length), bound on `cyclic-shift`: The number of positions in the block that a cyclic shift rotates.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $k$ (offset), bound on `cyclic-shift`: The integer, taken modulo L, by which the cyclic shift rotates the block.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $k$ (level count), bound on `address-interchange`: The number of recursion levels, log base m of the field width.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $T$ (triple), bound on `indicator-vector`: A three-element subset of the ground set $[h]$.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in each key.
- $k$ (key), bound on `stable-radix-sort`: The key of a record, written as a string of $w$ bits.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $q$ (address before the move), bound on `destination-rank`: The address of a record before the move.
- $\alpha$ (real part), bound on `phase-factor`: The real part of the complex number z.
- $k$ (denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of an element of $\mathbb{D}$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $F_q$ (discrete Fourier transform), bound on `discrete-fourier-transform`: The map of length q sending a vector of q complex numbers to its transform.
- $L$ (linear map), bound on `discrete-fourier-transform`: A generic linear map from vectors to vectors, tested for the contraction property.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than s.
- $\theta$ (relative gap), bound on `gaussian-resampling`: The relative gap t/s - 1 between the two lengths.
- $\alpha$ (width parameter), bound on `gaussian-resampling`: An integer that sets how wide the Gaussian weights are.
- $p$ (precision parameter), bound on `gaussian-resampling`: An integer precision parameter of the resampling identity.
- $P_s$ (length-s permutation), bound on `gaussian-resampling`: The permutation of length-s vectors that sends each position m to the position tm mod s.
- $P_t$ (length-t permutation), bound on `gaussian-resampling`: The permutation of length-t vectors defined by sending each position m to the position -sm mod t.
- $L$ (forward contraction), bound on `gaussian-resampling`: A linear contraction from length-s vectors to length-t vectors.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $T$ (second Gaussian map), bound on `gaussian-resampling`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $N$ (near-identity map), bound on `gaussian-resampling`: A map built from T and Gaussian corrections that lies within 1/2 of the identity.
- $k$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a record, running from 0 to r-1.
- $R$ (polynomial ring), bound on `polynomial-ring`: The quotient ring of complex polynomials in y modulo the multiples of f.
- $w$ (array entry), bound on `array-norm`: A single entry of the array X, which is a complex number.
- $L$ (linear contraction map), bound on `linear-contraction`: A linear map between complex coordinate spaces, the map whose contraction property is studied on this page.
- $w$ (input vector), bound on `linear-contraction`: A vector in the input space of a linear map, with m complex coordinates.
- $e$ (integer), bound on `congruence-modulo`: An integer, the other of the two integers compared by congruence.
- $w$ (class member), bound on `congruence-modulo`: An integer in the residue class of d modulo m.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so that $|f_j| \le 2^p$.
- $B$ (block base), bound on `signed-packing`: The base $2^{4p}$ at which the polynomials are evaluated, so that each coefficient occupies a block of $4p$ bits.
- $w$ (formal variable), bound on `cyclic-convolution`: A formal variable in which a sequence is written as a polynomial, never evaluated.
- $w$ (second argument), bound on `bilinear-map`: A vector of W, the second argument of the bilinear map.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $S$ (triple), bound on `subspace-labels`: A second three-element subset, used for inner products.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $R$ (orthogonal residual), bound on `complex-phase-network`: The subspace by which an edge's two labels differ, orthogonal to the smaller one.
- $L$ (layout permutation), bound on `transform-layout`: The explicit permutation of record addresses that places the selected bits in the required chunks.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.
- $L$ (lost dimension), bound on `rank-saving-recursion`: The total dimension lost along decreasing edges, where the head label is smaller than the tail label.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $\Lambda$ (parallel butterfly), bound on `transform-round`: The tensor product of the two-point map over all participating axes, applied to the selected bits in one pass.
- $p$ (fractional bit count), bound on `guard-width-bound`: The number of fractional bits each input coefficient carries, so the inputs lie on $2^{-p}\mathbb{Z}[i]$.
- $A$ (depth bound), bound on `guard-width-bound`: A bound $A(e)$ on the number of operations on any chain for a group of $e$ axes.
- $S$ (product of the lengths), bound on `modular-inverse`: The product $M_1 M_2 \cdots$ of all the lengths, the order of the cyclic group.
- $q$ (prime modulus), bound on `address-shear`: A fixed odd prime, the base of the digits; the letter changes meaning from the transform length.
- $\Pi$ (partial permutation matrix), bound on `address-shear`: A $0/1$ matrix with exactly $a$ ones, at most one in each row and column, in the factorization of $M$.
- $i$ (row index), bound on `address-shear`: The row of a one in $\Pi$, which names an $H$ field.
- $j$ (column index), bound on `address-shear`: The column of a one in $\Pi$, which names a $D$ field.
- $R$ (record length), bound on `packed-bit-addition`: The number of bits in each record, which the cost bounds divide by.

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

## Page to audit (`transform-identity`)

````markdown
# Transform identity with retained permutations

This identity computes its transforms by [Gaussian resampling](gaussian-resampling.md), which replaces a transform of arbitrary length by transforms whose axis lengths are powers of two. It keeps the two coordinate permutations of that method inside the transform formula, so that they cancel across a convolution. It is the resampling step of [Integer multiplication below n log n](main-theorem.md).

The usual implementation of Gaussian resampling This identity keeps both permutations in the formula, so they need not be

The two sides have different shapes. transforms use powers of two. The identity pairs a transform of length $s$ with one of length $t$, so the permutations $P_s$ and $P_t$ reorder entries to let the two sides be matched.

The letters $u$ and $w$ denote complex vectors of length $q$, with indices taken [modulo](congruence-modulo.md) $q$. A linear map $\Psi$ is a contraction when $\|\Psi u\|\le\|u\|$ for every $u$, where $\|u\|$ is the largest modulus of an entry of $u$. $F_q$ is the normalized discrete Fourier transform, $(F_q u)_k=\frac{1}{q}\sum_{j=0}^{q-1}u_j\,e^{-2\pi i jk/q}$. $F_s$ and $F_t$ are $F_q$ at $q=s$ and $q=t$.

Each permutation is defined by [congruence](congruence-modulo.md) of positions: $(P_s u)_j=u_{tj}$ and $(P_t w)_k=w_{-sk}$. Both permutations are bijections, which depends on $s$ and $t$ being [coprime](coprime.md). An integer $t$ has an inverse modulo $s$ exactly when $\gcd(s,t)=1$, so $j\mapsto tj$ is one-to-one on positions. For example, with $s=3$ and $t=5$, $(P_3 u)=(u_0,u_2,u_1)$.

The identity is built from two [linear maps](linear-algebra-basics.md): $A$ is a linear contraction from length-$s$ vectors to length-$t$ vectors, and $B_0$ one from length-$t$ to length-$s$. The source's states:
$$P_s F_s = 2^{2\alpha^2}\, B_0\, P_t F_t\, A.$$
The source derives this from its Gaussian resampling identity, which uses two Gaussian-weighted maps $S$ and $T$ from length-$s$ to length-$t$ vectors; these letters are the source's, not those bound elsewhere. The identity reads and the proof uses it as follows. Let $\Gamma$ select the coordinates nearest $tj/s$, let $\Lambda$ be a diagonal scaling, and let $N=\Gamma T\Lambda$, a map from length-$s$ vectors to themselves. $\alpha^2\theta>p/\alpha^2>1$, and this is why the lemma needs $\theta>p/\alpha^4$. Put $L=\Lambda N^{-1}\Gamma$, a left inverse of $T$. Multiplying the Gaussian identity by $L$ gives $P_sF_s=LP_tF_tS$. With $A=S/2$ and $B_0=2^{-(2\alpha^2-1)}L$, this is the identity above.

The original proof uses two label-and-sort operations, one for $P_t$ and one for $P_s^{-1}$, No sort is run.

Permutations pass through pointwise products. $\Pi$ is a coordinate permutation, which rearranges the entries of a vector, and $\cdot$ is the entrywise product. Then $(\Pi u)\cdot(\Pi w)=\Pi(u\cdot w)$, because products. The retained source permutation $R$ cancels across the two forward transforms, their pointwise product, and the [opposite-sign transform](opposite-transform.md) $F_s^+$, the sum with $+$ in the exponent. The source shows this with.
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

Write the answer to `exegenius/tasks/0222-audit-transform-identity.answer.json`, then run `exegenius submit 0222-audit-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
