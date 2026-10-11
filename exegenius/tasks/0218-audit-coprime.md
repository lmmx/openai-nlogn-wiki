# exegenius task 0218-audit-coprime

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
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $t_i$ (axis length), bound on `transform-axis`: The length of axis $i$: the number of values that coordinate of an address takes.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar, an element of the field $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $c$ (path end vertex), bound on `endpoint-operator`: The last of three vertices on a path through the network.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $c$ (positive constant), bound on `limit-inferior`: A positive real constant in the lower bound and its negation.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $c$ (chunk exponent), bound on `cost-table`: A fixed positive rational exponent that sets $K$ relative to $d$.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $\lambda$ (scalar multiplier), bound on `line-spanned-by-vector`: A scalar in K, an element of the scalar field, used to scale v.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $M$ (record count), bound on `destination-rank`: The number of records in the stream.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $M$ (change matrix), bound on `binary-change-of-basis`: The invertible m-by-m matrix over the binary field that specifies the change of basis.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $l$ (second denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of the second element $b/2^l$.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $M$ (entry count), bound on `multidimensional-transform`: The number of entries of the array, the product of the axis lengths.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $Z$ (output list), bound on `synthetic-transforms`: The list of $t$ records $(Z_0,\dots,Z_{t-1})$ that the transform returns.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than s.
- $M$ (backward contraction), bound on `gaussian-resampling`: A linear contraction from length-t vectors back to length-s vectors.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $c$ (centered residue), bound on `signed-packing`: The unique integer in $[-B/2, B/2)$ that is congruent to $f(B)\,g(B)$ modulo $B$.
- $M$ (modulus), bound on `centered-residue`: A positive integer, the modulus of the residue with respect to which the centered residue is taken.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $M$ (form matrix), bound on `bilinear-form`: The matrix of the bilinear form in the chosen coordinates.
- $\lambda_1$ (kernel coefficient), bound on `subspace-labels`: A Gaussian dyadic coefficient of the translation kernel.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $S$ (triple), bound on `subspace-labels`: A second three-element subset, used for inner products.
- $\beta$ (bank index), bound on `subset-intersection-network`: A triple of triples that indexes one entry of a bank.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $\lambda$ (constant lambda), bound on `complex-phase-network`: The constant $(1+i)/2$.
- $M$ (two-point kernel), bound on `complex-phase-network`: The $2\times 2$ matrix $\lambda I+\mu X$ acting on one address bit.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number D of selected axes in one layer, a count of axes.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.
- $\gamma$ (cost per volume), bound on `rank-saving-recursion`: The cost of a call at parameter $\ell$ divided by its volume.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $d$ (axis count), bound on `padded-transform-box`: The number of axes of the transform, the count of coordinate directions along which the data is laid out.
- $\lambda$ (limit variable), bound on `little-o-notation`: The real point at which both functions are evaluated, taken to infinity in the limit.
- $d$ (axis bound), bound on `guard-width-bound`: A positive integer bound $d \ge D$ on the number of selected axes.
- $\beta$ (depth growth bound), bound on `guard-width-bound`: The fixed count $s+\eta$ bounding how much the depth bound grows at each recursive level.

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

## Page to audit (`coprime`)

````markdown
# Coprime

Two integers are coprime when their greatest common divisor is $1$, that is, when no integer greater than $1$ divides both of them. The concept matters because the argument needs several cyclic axes whose lengths are pairwise coprime, so that they can be combined into one axis of the product length; the [Chinese-remainder map](chinese-remainder-map.md) rests on that fact.

For integers $\beta$ and $\gamma$, not both zero, write $\gcd(\beta,\gamma)$ for their greatest common divisor, the largest positive integer dividing both. The integers $\beta$ and $\gamma$ are coprime when $\gcd(\beta,\gamma)=1$.

For a family of $M$ integers $\lambda_1,\dots,\lambda_M$, where $M$ is the number of integers in the family, the family is pairwise coprime when $\gcd(\lambda_i,\lambda_j)=1$ for every two indices $i\neq j$. Pairwise coprimality is stronger than the family having overall greatest common divisor $1$: the family $4,6,35$ has no common divisor above $1$, yet $\gcd(4,6)=2$, so it is not pairwise coprime.

Examples. $\gcd(6,35)=1$, so $6$ and $35$ are coprime, while $\gcd(6,9)=3$, so $6$ and $9$ are not. The family $3,4,35$ is pairwise coprime, since $\gcd(3,4)=\gcd(3,35)=\gcd(4,35)=1$.

Coprimality is what makes the least common multiple equal to the product. The least common multiple $\operatorname{lcm}(\lambda_1,\dots,\lambda_M)$ is the smallest positive integer divisible by every $\lambda_i$. For the pairwise coprime family above, $\operatorname{lcm}(3,4,35)=420=3\cdot 4\cdot 35$. Without coprimality the product overcounts: $\operatorname{lcm}(4,6)=12$, while $4\cdot 6=24$.

This is the fact the transform argument uses. In the group $\mathbb{Z}/\lambda_1\times\cdots\times\mathbb{Z}/\lambda_M$, the element $(1,1,\dots,1)$ has order $\operatorname{lcm}(\lambda_1,\dots,\lambda_M)$. When the $\lambda_i$ are pairwise coprime, that order is the product $\lambda_1\cdots\lambda_M$, so the element generates a cyclic group with exactly as many elements as the product of the axes. The paper states the requirement for its integer product directly:. Its lengths are chosen to meet it. Each length is an odd prime near a power of two $t_i$, and The map that splits the length-$S$ axis into the axes of lengths $s_1,\dots,s_d$ then relies on to show that its image has order $S$.
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

Write the answer to `exegenius/tasks/0218-audit-coprime.answer.json`, then run `exegenius submit 0218-audit-coprime` in the project directory. If submit rejects the answer, fix the answer and submit again.
