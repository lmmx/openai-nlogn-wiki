# exegenius task 0229-audit-carry-propagation

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
- Chinese-remainder map (also: Agarwal–Cooley map, coefficient layout, generator)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
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
- Prime source lengths (also: pairwise coprime source lengths)
- Transform identity with retained permutations (also: target permutation)
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
- Mixed-radix digits (also: mixed-radix digit)
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
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $b$ (input bit), bound on `xor`: The second of the two bits that an XOR combines.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar, an element of the field $F$.
- $c_j$ (input weight), bound on `linear-network-frames`: The fixed weight of input j in a gate, the same at every address.
- $w$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $c$ (path end vertex), bound on `endpoint-operator`: The last of three vertices on a path through the network.
- $w$ (input role), bound on `endpoint-operator`: An input role of the network, whose route starts at its source vertex.
- $n$ (input length), bound on `limit-inferior`: The number of bits in each input, which is the index of the running-time function.
- $c$ (positive constant), bound on `limit-inferior`: A positive real constant in the lower bound and its negation.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $c$ (chunk exponent), bound on `cost-table`: A fixed positive rational exponent that sets $K$ relative to $d$.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set $[h]$.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $h$ (ground-set size), bound on `indicator-vector`: The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $Q$ (second matrix), bound on `tensor-product`: A second matrix, which is copied once for each entry of P in the tensor product P \otimes Q.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in each key.
- $q$ (address before the move), bound on `destination-rank`: The address of a record before the move.
- $h$ (chunk index), bound on `destination-rank`: The index of one of the three address chunks, taking values 1, 2 or 3.
- $b$ (second numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $h$ (output position), bound on `multidimensional-transform`: A position in the output array, with each coordinate below its axis length.
- $h$ (input list), bound on `synthetic-transforms`: The list of $t$ records $(h_0,\dots,h_{t-1})$ that the transform takes as input.
- $w$ (array entry), bound on `array-norm`: A single entry of the array X, which is a complex number.
- $w$ (input vector), bound on `linear-contraction`: A vector in the input space of a linear map, with m complex coordinates.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $w$ (class member), bound on `congruence-modulo`: An integer in the residue class of d modulo m.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $fg$, a polynomial with at most $2r-1$ coefficients $h_j$.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in $[-B/2, B/2)$ that is congruent to $f(B)\,g(B)$ modulo $B$.
- $w$ (formal variable), bound on `cyclic-convolution`: A formal variable in which a sequence is written as a polynomial, never evaluated.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $w$ (second argument), bound on `bilinear-map`: A vector of W, the second argument of the bilinear map.
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number D of selected axes in one layer, a count of axes.
- $\gamma$ (cost per volume), bound on `rank-saving-recursion`: The cost of a call at parameter $\ell$ divided by its volume.
- $d$ (axis count), bound on `padded-transform-box`: The number of axes of the transform, the count of coordinate directions along which the data is laid out.
- $Q$ (box size), bound on `padded-transform-box`: The number of entries of the padded transform box, the product of the padded lengths of all axes.
- $d$ (axis bound), bound on `guard-width-bound`: A positive integer bound $d \ge D$ on the number of selected axes.
- $\gamma$ (second integer), bound on `coprime`: The second of the two integers whose greatest common divisor is taken, not both zero.
- $b$ (digit count), bound on `address-shear`: The number of radix-$q$ digits in each field, a count; the letter changes meaning from earlier pages.
- $q$ (prime modulus), bound on `address-shear`: A fixed odd prime, the base of the digits; the letter changes meaning from the transform length.
- $h$ (current value of H), bound on `address-shear`: The value of the single field $H$ when $m = 1$.
- $d$ (current value of D), bound on `address-shear`: The value of the single field $D$ when $m = 1$.
- $j$ (column index), bound on `address-shear`: The column of a one in $\Pi$, which names a $D$ field.
- $\gamma$ (guard value), bound on `packed-bit-addition`: The integer formed by the non-selected bits of a segment, which lies between 0 and 2 to the power of mu minus 1, minus 1.
- $w$ (second vector), bound on `transform-identity`: A second complex vector of length q, paired with u in the permutation and product formulas.
- $\cdot$ (entrywise product), bound on `transform-identity`: The product of two vectors of the same length taken entry by entry.
- $w$ (scaled input), bound on `bluestein-chirp-identity`: The input vector u with each entry divided by the corresponding chirp entry.
- $j$ (coefficient position), bound on `phase-twist`: The position of a coefficient in the record, running from 0 to r-1.
- $Q$ (source ring), bound on `ring-homomorphism`: The ring from which the ring homomorphism $\varphi$ starts.
- $w$ (indeterminate), bound on `ring-homomorphism`: The variable of the example ring $Q=\mathbb{C}[w]/(w^2-1)$, whose square is $1$.
- $j$ (place index), bound on `mixed-radix-digits`: An index naming one place of the system, running from 1 to beta; on this page it is not the index of earlier pages.
- $d$ (axis count), bound on `prime-source-lengths`: The number of axes of the multidimensional transform, a count.
- $w$ (short axis count), bound on `prime-source-lengths`: The number of axes padded to length u/2, a count.

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

## Page to audit (`carry-propagation`)

````markdown
# Carry propagation

Carry propagation is the final arithmetic step that turns a list of integer coefficients into the binary digits of their value. It is what gives the output of [Integer multiplication below n log n](main-theorem.md) its exact binary form.

Carry propagation takes its input from [Radix-digit convolution](radix-digit-convolution.md): the output is the list of integer coefficients $c_0, c_1, \dots$ of the product of the two digit polynomials. Let $q = \lceil n/b \rceil$ be the number of digits in each input, as on that page. The radix is $Q_0 = 2^b$, the number of values a digit can take, which is the base in which each digit is written. The index $j$ runs over the positions $0, 1, \dots$ of the coefficient list, so $\sum_j c_j Q_0^j$ is the product.

The $c_j$ are not digits. Each $c_j$ is a sum of at most $q$ products of two digits, each at most $(Q_0-1)^2$, so $0 \le c_j \le q(Q_0-1)^2 < Q_0^3$. The paper takes $b = \lceil \log_2 n \rceil$ for large $n$, so $Q_0 \ge n \ge q$, and then $q(Q_0-1)^2 < qQ_0^2 \le Q_0^3$. 
Carry propagation rewrites the same sum with digits. The digit $d_j$ is the $j$th base-$Q_0$ digit of the output, so $0 \le d_j < Q_0$. The carry $\gamma_j$ is the amount carried into position $j$ from the lower positions. Set $\gamma_0 = 0$ and, for $j \ge 0$,

$$d_j = (c_j + \gamma_j) \bmod Q_0, \qquad \gamma_{j+1} = \left\lfloor \frac{c_j + \gamma_j}{Q_0} \right\rfloor,$$

where $w \bmod Q_0$ is the remainder of $w$ on division by $Q_0$, and $\lfloor w \rfloor$ is the largest integer not above $w$. Division with remainder gives, at every position,

$$c_j + \gamma_j = d_j + Q_0\,\gamma_{j+1}.$$

Why this keeps the value: here $h$ is a summation index, the position of an already processed coefficient, running over $0 \le h < j$. For every $j \ge 0$,

$$\sum_{h<j} c_h Q_0^h = \sum_{h<j} d_h Q_0^h + \gamma_j Q_0^j.$$

The identity says that the processed coefficients have the same value as the processed digits plus the carry, which is still owed to the higher positions. It holds at $j=0$, where both sides are $0$. If it holds at $j$, add $c_j Q_0^j$ to the left side, which gives $\sum_{h<j} c_h Q_0^h + c_j Q_0^j$. Substituting $\sum_{h<j} d_h Q_0^h + \gamma_j Q_0^j$ for the first sum, and then multiplying the split relation by $Q_0^j$ to get $c_j Q_0^j + \gamma_j Q_0^j = d_j Q_0^j + \gamma_{j+1} Q_0^{j+1}$, the left side equals $\sum_{h<j+1} d_h Q_0^h + \gamma_{j+1} Q_0^{j+1}$. So the identity holds at $j+1$.

The recurrence reads $c_j$ only after $\gamma_j$ is known, so the positions must be processed from $0$ upward. The carries also stay small. If $0 \le \gamma_j \le q(Q_0-1)$, then $c_j + \gamma_j \le q(Q_0-1)^2 + q(Q_0-1) = qQ_0(Q_0-1)$, so $\gamma_{j+1} \le q(Q_0-1)$. Since $\gamma_0 = 0$, every carry obeys this bound, and fits in $2b$ bits.

Coefficients vanish past the end. The product of two polynomials of degree $q-1$ has degree at most $2q-2$, so $c_j = 0$ for $j \ge 2q-1$. For such $j$, $\gamma_{j+1} = \lfloor \gamma_j / Q_0 \rfloor$. The carry $\gamma_{2q-1}$ is below $Q_0^2$, so $\gamma_{2q} \le Q_0 - 1$ and $\gamma_{2q+1} = 0$. The leftover carry is written out the same way, one digit at a time:. Its digits are $d_j = \gamma_j \bmod Q_0$ for $2q-1 \le j \le 2q$, and $d_j = 0$ beyond. Taking $j = 2q+1$ in the identity, with $\gamma_{2q+1} = 0$ and every $c_h = 0$ for $h \ge 2q+1$, gives $\sum_j c_j Q_0^j = \sum_j d_j Q_0^j$. Each $d_j$ is a $b$-bit block, so the product is the binary string formed by writing $d_{2q}, \dots, d_0$ from the top down, each in $b$ bits.

For $Q_0 = 4$ (so $b = 2$) and three coefficients $(c_0, c_1, c_2) = (5, 3, 7)$:

- $j=0$: $c_0 + \gamma_0 = 5$, so $d_0 = 1$ and $\gamma_1 = 1$.
- $j=1$: $c_1 + \gamma_1 = 4$, so $d_1 = 0$ and $\gamma_2 = 1$.
- $j=2$: $c_2 + \gamma_2 = 8$, so $d_2 = 0$ and $\gamma_3 = 2$.
- The leftover carry $\gamma_3 = 2 < 4$ gives $d_3 = 2$ and $\gamma_4 = 0$.

The digits $(d_3, d_2, d_1, d_0) = (2, 0, 0, 1)$ give $2 \cdot 64 + 0 \cdot 16 + 0 \cdot 4 + 1 = 129 = 5 + 3 \cdot 4 + 7 \cdot 16$. Written in binary, each digit takes two bits: $10\,00\,00\,01$.
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

Write the answer to `exegenius/tasks/0229-audit-carry-propagation.answer.json`, then run `exegenius submit 0229-audit-carry-propagation` in the project directory. If submit rejects the answer, fix the answer and submit again.
