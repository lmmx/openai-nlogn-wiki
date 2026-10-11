# exegenius task 0409-audit-congruence-modulo

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
- Exact integer multiplication (also: exact multiplication)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights, Gaussian line map, Gaussian corrections, target)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Gaussian dyadics
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set (also: finite set)
- Indicator vector
- Two-point kernel (also: kernel)
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Tensor product (also: tensor power)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Ceiling function
- Bijection
- Permutation
- Eigenvalue
- Incidence
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $B$ (target set), bound on `bijection`: The target set, whose elements are the outputs of the map f.
- $f$ (map), bound on `bijection`: The map from the source set A to the target set B, which is a bijection when it is one-to-one and onto.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $B$ (exceptional addresses), bound on `destination-rank`: The set of exceptional addresses, whose records the correction extracts.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The monic complex polynomial whose multiples count as zero.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $\gamma$ (second integer), bound on `coprime`: The other integer whose greatest common divisor with beta is taken, not both zero with it.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $\mathbb{Z}$ (integers), bound on `coprime`: The set of all integers.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $\delta$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $t$ in an element $\alpha+\delta t$ of $Q$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $B$ (inverse candidate), bound on `linear-algebra-basics`: A matrix that may serve as the inverse of $A$.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $Z$ (sign matrix), bound on `phase-factor`: The diagonal matrix diag(1,-1), which negates the entry whose bit is 1.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $\nu$ (second input index), bound on `discrete-fourier-transform`: A second integer index from 0 to q-1 that numbers the input coordinates in the inverse identity.
- $\nu$ (input position), bound on `multidimensional-transform`: A position in the input array, a tuple of D coordinates with the s-th coordinate between 0 and t_s minus 1.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $Z$ (transformed list), bound on `synthetic-transforms`: The output list of records produced by the transform.
- $\delta$ (half block size), bound on `synthetic-transforms`: The number of positions in half of a block at a level, taking the values $1, 2, \dots, N/2$.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\nu$ (exponent), bound on `polynomial-ring-mod-yr-plus-1`: The positive integer power to which a root of unity is raised to give 1, counting the factors of the product.
- $\delta$ (first input value), bound on `butterfly`: The first of the two input values of the butterfly.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $\delta$ (Gaussian integer numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of a Gaussian dyadic $\delta/2^e$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\nu$ (second numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of the second Gaussian dyadic $\nu/2^{e'}$.
- $e'$ (second denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of the second Gaussian dyadic.
- $\delta$ (diagonal coefficient), bound on `two-point-kernel`: The coefficient of $I$ in $K$, a complex number.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $\nu$ (address), bound on `two-point-kernel`: An integer whose binary form with $d$ bits is one address of an array.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $f$ (function on addresses), bound on `tensor-product`: A function on addresses of m coordinates, the input that the operator transforms.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\mathbb{Z}$ (integers), bound on `grid-numerator`: The set of integers, whose elements are the whole numbers, which may be negative.

## Pages in the wiki

- [Logarithm](logarithm.md)
- [Base-2 logarithm](base-two-logarithm.md)
- [Integer](integer.md)
- [Ring](ring.md)
- [Root of unity](root-of-unity.md)
- [Stream](stream.md)
- [Prime number](prime-number.md)
- [Pointwise product](pointwise-product.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen multiplication](schonhage-strassen.md)
- [Convolution](convolution.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Bijection](bijection.md)
- [Permutation](permutation.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Mathematical induction](mathematical-induction.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Little-o notation](little-o-notation.md)
- [Coprime](coprime.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Address](address.md)
- [Address field](address-field.md)
- [Cyclic shift](cyclic-shift.md)
- [Array](array.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Logical array](logical-array.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Incidence](incidence.md)
- [Eigenvalue](eigenvalue.md)
- [Indicator vector](indicator-vector.md)
- [Matrix rank](matrix-rank.md)
- [Phase factor](phase-factor.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Gaussian integer](gaussian-integer.md)
- [Two-point kernel](two-point-kernel.md)
- [Tensor product](tensor-product.md)
- [Bilinear map](bilinear-map.md)
- [Ceiling function](ceiling-function.md)
- [Carry propagation](carry-propagation.md)
- [Grid numerator](grid-numerator.md)
- [Congruence](congruence-modulo.md)
- [Binary field](binary-field.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Bit network](bit-network.md)
- [Bilinear form](bilinear-form.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Centered residue](centered-residue.md)
- [Chinese remainder theorem](chinese-remainder-theorem.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bézout's identity](bezout-identity.md)
- [Big-Theta notation](big-theta-notation.md)
- [Cyclic group](cyclic-group.md)
- [Modular inverse](modular-inverse.md)
- [Diagonal scaling](diagonal-scaling.md)
- [Extended real numbers](extended-reals.md)
- [Limit inferior](limit-inferior.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Family parameter](family-parameter.md)
- [Frequency domain](frequency-domain.md)
- [Opposite transform](opposite-transform.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Padded transform box](padded-transform-box.md)
- [Logical bit volume](logical-bit-volume.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Normalization scales](normalization-scales.md)
- [Independence of events](independence.md)
- [Projection along a subspace](projection-along-subspace.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Bit construction](bit-construction.md)
- [Complex phase network](complex-phase-network.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Tape procedure](tape-procedure.md)
- [Exclusive or](xor.md)
- [Bit procedure](bit-procedure.md)
- [Endpoint operator](endpoint-operator.md)
- [Address shear](address-shear.md)
- [Complex construction](complex-construction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Supremum](supremum.md)
- [Linear contraction](linear-contraction.md)
- [Guard-width bound](guard-width-bound.md)
- [Union bound](union-bound.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Telescoping identity](telescoping-identity.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`congruence-modulo`)

````markdown
# Congruence

Congruence is defined on pairs of [Integer](integer.md) values: two of them are congruent when they leave the same remainder on division by a fixed positive integer. It is the arithmetic behind the [Chinese-remainder map](chinese-remainder-map.md), which places coefficients on distinct prime cyclic axes, and behind the [centered residue](centered-residue.md), which recovers a signed coefficient from its remainder.

## Definition

Let $B$ be a positive integer, the modulus, and let $d$ and $e$ be integers. Then $d$ and $e$ are congruent modulo $B$, written $d \equiv e \pmod B$, when $B$ divides $d-e$. The set of all integers is written $\mathbb{Z}$.

Congruence is an equivalence relation: $d \equiv d$; $d \equiv e$ implies $e \equiv d$; and $d \equiv e$ with $e \equiv f$ implies $d \equiv f$, since $d-f = (d-e)+(e-f)$. So each integer lies in exactly one residue class. Here $\nu$ is an integer in the class of $d$, and the residue class of $d$ is

$$\{\, \nu \in \mathbb{Z} : \nu \equiv d \pmod B \,\}.$$

Each class contains exactly one integer $\delta$ in $\{0,\dots,B-1\}$, its remainder. Such a $\delta$ exists because $d$ differs from a multiple of $B$ by $\delta$. It is unique because two integers in $\{0,\dots,B-1\}$ differ by less than $B$. So there are $B$ classes.

For example, with $B = 7$: $23 \equiv 2 \pmod 7$, since $23 - 2 = 3 \cdot 7$, and $-5 \equiv 2 \pmod 7$, since $-5 + 7 = 2$.

Congruence respects sums and products. Let $d'$ be an integer congruent to $d$ modulo $B$, and let $e'$ be an integer congruent to $e$ modulo $B$. Then $d'+e' \equiv d+e$ and $d'e' \equiv de \pmod B$.

## Use in the paper

Congruence is applied in [Carry propagation](carry-propagation.md): each output digit is the residue of the input coefficient plus the incoming carry. The paper says to, with. Here $u_j$ is the input coefficient at position $j$, $\gamma_j$ is the carry into it, and $B$ stands for the paper's $B_0$:

$$d_j \equiv u_j + \gamma_j \pmod B, \qquad \gamma_{j+1} = \frac{u_j + \gamma_j - d_j}{B}.$$

For $B = 10$, $u_j = 27$ and $\gamma_j = 0$, the digit is $7$ and the carry is $(27-7)/10 = 2$.

The paper recovers each signed coefficient as the. The interval $[-B/2, B/2)$ holds exactly one integer from each class, so a coefficient of either sign is determined by its residue.
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

Write the answer to `exegenius/tasks/0409-audit-congruence-modulo.answer.json`, then run `exegenius submit 0409-audit-congruence-modulo` in the project directory. If submit rejects the answer, fix the answer and submit again.
