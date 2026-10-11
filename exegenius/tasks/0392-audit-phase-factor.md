# exegenius task 0392-audit-phase-factor

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
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Ground set (also: finite set)
- Indicator vector
- Little-o notation (also: limit as lambda tends to infinity)
- Array norm (also: norm of an array, coefficient bound)
- Payload (also: record)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
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

- $a$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $p$ (prime), bound on `prime-number`: A prime number, an integer greater than one with no positive divisors other than one and itself.
- $a$ (divisor), bound on `prime-number`: A positive integer that divides another integer.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $p$ (precision), bound on `truncation`: The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $\alpha$ (first paired value), bound on `truncation`: The first of the two values that the layer combines in each pair.
- $\beta$ (second paired value), bound on `truncation`: The second of the two values that the layer combines in each pair.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $\alpha$ (coefficient), bound on `ring-homomorphism`: The complex constant term of an element $\alpha+\delta t$ of $Q$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $\alpha$ (address), bound on `address`: A string of d bits that labels one entry of the array.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $\alpha$ (input weight), bound on `linear-network-frames`: The fixed weight with which a gate multiplies its input s, the same at every address.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $a$ (rational rank), bound on `matrix-rank`: The rational rank of $A$, the number of its linearly independent rows, which is also the number of ones in $\Pi$.
- $D$ (second field vector), bound on `matrix-rank`: The vector $(D_1, \ldots, D_m)$ of $m$ address fields, which the shear reads without changing.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.

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

## Page to audit (`phase-factor`)

````markdown
# Phase factor

Phase factors are the twists that this paper's transforms apply to coefficients without changing their sizes. The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) and [Gaussian resampling](gaussian-resampling.md) rely on them.

A phase factor is a complex number $\zeta$ of modulus one, $|\zeta| = 1$, where $|\zeta|$ is the distance from $\zeta$ to $0$ in the complex plane. Write $\tau = \alpha + \beta i$ for a complex number, where $\alpha$ and $\beta$ are real numbers, the real and imaginary parts of $\tau$.

A unit of a [ring](ring.md) is an element whose inverse also lies in the ring. A Gaussian integer is a complex number whose real and imaginary parts are integers. Each phase factor $\zeta$ that is a power of $i$ is a unit of the [ring](ring.md) of Gaussian integers, so multiplying a Gaussian integer by $\zeta$ gives a Gaussian integer.

The phase factors used here are built from the fourth [roots of unity](root-of-unity.md) $1, i, -1, -i$. Multiplying by $i$ gives $i(\alpha+\beta i) = -\beta + \alpha i$. The paper states it:

In a butterfly layer, the phase depends on the address: for an address $s$ in a layer, let $D$ be the number of selected bits, the address bits on which the layer acts, and write $s_1,\dots,s_D$ for them, each 0 or 1. The layer multiplies the value at $s$ by $i^{s_1+\cdots+s_D}$. stored at that address.

A scalar correction is a fixed constant phase factor applied at each [sink](network-gate-terminal.md) of a network, undoing a sign or an exchange of roles. The endpoint operator is what the frames leave on each role array:.

Call $C = \tfrac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix}$ the forward kernel, and $Z = \mathrm{diag}(1,-1)$ the sign matrix. The paper's identity gives $C^{-1} = -iZCZ$, so multiplying by $i$ and conjugating by $Z$ turns $C^{-1}$ into $C$. The corrections at each affected sink

An inverse child on $D$ selected bits is $(C^{-1})^{\otimes D} = (-i)^D Z^{\otimes D} C^{\otimes D} Z^{\otimes D}$, where $\otimes D$ is the tensor product of $D$ copies. Signs and phases multiply each stored coefficient without calling the procedure.
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

Write the answer to `exegenius/tasks/0392-audit-phase-factor.answer.json`, then run `exegenius submit 0392-audit-phase-factor` in the project directory. If submit rejects the answer, fix the answer and submit again.
