# exegenius task 0467-audit-telescoping-identity

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
- Exact integer multiplication (also: exact multiplication)
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture, the conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier, der Hoeven)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights, Gaussian line map, Gaussian corrections, target)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution, packed polynomial product)
- Convolution over the polynomial ring
- Subspace labels (also: binary label)
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network, side and central wires, gather and scatter, scalar network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks, address-field interchange procedure, field interchanges)
- Address shear (also: shear of address pairs, Matrix shear)
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant, orthogonal residual of an edge)
- Simultaneous butterfly layer (also: selected bits, two-point operator on selected bits)
- Packed selected-bit addition (also: exceptional addresses, selected bit)
- Guard-width bound (also: segment)
- Transform layout (also: transform layout and packed selected-bit addition)
- Transform identity with retained permutations (also: target permutation, coordinate permutations)
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Bit procedure
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Cost table (also: chirp and twist)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Endpoint operator
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set (also: finite set)
- Indicator vector
- Modular inverse (also: invertible modulo q, unit modulo M_i)
- Two-point kernel (also: kernel)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer (also: butterfly layers, layer)
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Scratch storage (also: scratch values, scratch chunk, scratch wires, forward schedule, linear-readout version)
- Tensor product (also: tensor power)
- Transform round (also: butterfly round, current recursive length, level the round processes)
- Truncation
- Union bound
- Exclusive or (also: XOR)
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Ceiling function
- Bézout's identity (also: Bezout's identity)
- Big-Theta notation
- Bijection
- Permutation
- Bit network (also: the paper's bit network)
- Bit construction
- Complex construction
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Family parameter
- Frequency domain
- Incidence
- Independence of events
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Logical bit volume
- Ring
- Orthogonal complement
- Pointwise product
- Projection along a subspace
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Supremum
- Tape procedure
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $b$ (base), bound on `logarithm`: The fixed number, greater than 1, to which the logarithm is taken.
- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $\iota$ (coordinate label), bound on `diagonal-scaling`: An element of the label set $\mathcal{I}$, naming one coordinate of a vector.
- $k$ (term index), bound on `limit-inferior`: The position of a term in a sequence, an index counting from 1.
- $x$ (control vector), bound on `scratch-storage`: The vector of control values, with one entry $x_T$ for each triple $T$.
- $a$ (starting side values), bound on `scratch-storage`: The starting values of the side wires $W_{ST}$.
- $x$ (first field), bound on `address-interchange`: One of the two disjoint address fields being interchanged, read as a block of bits.
- $k$ (number of levels), bound on `address-interchange`: The number of levels in the recursion on the width, so that a width $u=m^k$ has $k=\log_m u$ levels.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $a$ (rational rank), bound on `address-shear`: The number of linearly independent rows of M over the rational numbers.
- $o$ (selected offset), bound on `simultaneous-butterfly-layer`: The position of the selected bit within its chunk, counted from the least significant end, with $0\le o<\delta$.
- $b$ (bit length of n), bound on `cost-table`: The rounded-up base-2 logarithm of n, which is the number of bits of n.

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

## Page to audit (`telescoping-identity`)

````markdown
# Telescoping identity

The telescoping identity says that a sum of differences of consecutive terms of a sequence equals the difference of its last and first terms. The argument uses it to add up a chain of small changes, one per stage, and keep only the two endpoints; the [Exact coefficient recovery](recovery-and-error.md) bound and the [Cost table](cost-table.md) both depend on this collapse.

A sequence is an ordered list of numbers. Let $o$ be the index of the last term of a sequence of real or complex numbers, so the sequence has $o+1$ terms. The index $k$ is the position of a term, running from $0$ to $o$; the letter $k$ changes meaning here. The term $\iota_k$ is the number at position $k$, so the sequence is $\iota_0,\iota_1,\dots,\iota_o$. The sum $\sum_{k=a}^{b} x_k$ stands for $x_a+x_{a+1}+\dots+x_b$, and it is $0$ when $b<a$.

For every such sequence,
$$\sum_{k=0}^{o-1}\left(\iota_{k+1}-\iota_k\right)=\iota_o-\iota_0.$$

To prove it, split the sum into two sums and shift the index of the first one:
$$\sum_{k=0}^{o-1}\iota_{k+1}-\sum_{k=0}^{o-1}\iota_k=\sum_{k=1}^{o}\iota_k-\sum_{k=0}^{o-1}\iota_k.$$
Each term $\iota_k$ with $1\le k\le o-1$ appears once in each sum, with opposite signs, so it cancels. What remains is $\iota_o$ from the first sum and $-\iota_0$ from the second, which gives $\iota_o-\iota_0$. When $o=0$ both sides are $0$.

For example, take $\iota_k=k^2$ and $o=4$. The differences $\iota_{k+1}-\iota_k$ for $k=0,1,2,3$ are $1-0$, $4-1$, $9-4$ and $16-9$, that is $1,3,5,7$. Their sum is $16=\iota_4-\iota_0$.

The identity turns a sum over many stages into a difference of two numbers. If stage $k$ changes a quantity from $\iota_k$ to $\iota_{k+1}$, the total change over all stages is the final value minus the initial value, whatever the intermediate values are. The paper applies the same collapse to signed dimension changes:, which leaves only the source and sink dimensions.
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

Write the answer to `exegenius/tasks/0467-audit-telescoping-identity.answer.json`, then run `exegenius submit 0467-audit-telescoping-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
