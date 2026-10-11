# exegenius task 0399-audit-radix-digit-convolution

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
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
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
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
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

- $b$ (base), bound on `logarithm`: The fixed number, greater than 1, to which the logarithm is taken.
- $y$ (positive number), bound on `logarithm`: The positive number whose logarithm to base $b$ is taken.
- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $z$ (complex number), bound on `root-of-unity`: A complex number that is tested for being a root of unity.
- $y$ (polynomial variable), bound on `root-of-unity`: The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, which is a root of unity in that ring.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $y$ (indeterminate), bound on `pointwise-product`: The indeterminate of the quotient ring $\mathbb{C}[y]/(y^r+1)$ whose elements are the entries.
- $P$ (normalized pointwise product), bound on `pointwise-product`: The map that sends two entries to their product in the ring divided by $r$.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary input string, of length $n$.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $z$ (padded integer), bound on `exact-integer-multiplication`: A nonnegative integer with $z < 2^k$ that is written in binary.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $z$ (coefficient list), bound on `truncation`: A finite list of complex numbers, called coefficients.
- $y$ (indeterminate), bound on `polynomial-ring`: The formal variable of the polynomials in the ring.
- $y$ (polynomial variable), bound on `array-norm`: The variable of the polynomials in the ring modulo y^r + 1.
- $N$ (family size), bound on `coprime`: The number of integers in the family nu_1 through nu_N.
- $y$ (target indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q'$.
- $N$ (entry count), bound on `address`: The number of entries in an array, which counts every stored entry once.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $y$ (second vector), bound on `linear-algebra-basics`: A vector over $F$, a second arbitrary vector.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $x_i$ (axis coordinate), bound on `transform-axis`: The coordinate of an address along axis $i$, an integer from 0 to $t_i - 1$.
- $y$ (polynomial indeterminate), bound on `transform-axis`: The indeterminate of the polynomial modulo $y^s+1$; its powers serve as roots of unity on the remaining axes.
- $N$ (entry count), bound on `multidimensional-transform`: The number of entries of the array, the product of the axis lengths.
- $y$ (polynomial variable), bound on `multidimensional-transform`: The variable of the polynomial that stores one coordinate of the array.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The variable of the polynomial ring $R_r$, in which $y^r$ is identified with $-1$.
- $N$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $\log_2$ (base-2 logarithm), bound on `synthetic-transforms`: The logarithm to base 2, so $\log_2 N$ is the number of levels of the fast method.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $P$ (ring element), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring $R_r$, given by its representative of degree less than $r$.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.

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

## Page to audit (`radix-digit-convolution`)

````markdown
# Radix-digit convolution

Radix-digit convolution is a reduction of [exact integer multiplication](exact-integer-multiplication.md) that writes each input as a polynomial in a power of two whose coefficients are its digits, so that the product becomes a convolution of short integer coefficients. It is the first step of the argument for [Integer multiplication below n log n](main-theorem.md): the [Chinese-remainder map](chinese-remainder-map.md) and [carry propagation](carry-propagation.md) pages build on the coefficients it produces.

The paper states the reduction in one sentence:

**Digits.** Let $x$ and $y$ be the two binary strings, each of $n$ bits, with $n \ge 2$. The digit width $b$ is the number of bits in each digit. The paper takes, so that $b \ge 1$ and $2^b \ge n$; the second holds because $2^{\lceil \log_2 n\rceil} \ge 2^{\log_2 n} = n$. Cut each input into blocks of $b$ bits, counting from the least significant end and padding the last block with leading zeros. Each block is a digit with value between $0$ and $2^b-1$, and $2^b$ is the radix. Let $N = \lceil n/b\rceil$ be the number of digits in each input. Let $x_i$ be the digit of $x$ at position $i$, for $0 \le i \le N-1$, so that $x = \sum_{i=0}^{N-1} x_i (2^b)^i$. The digits $y_j$ of $y$ are defined the same way, with position $j$.

**Polynomials.** Let $z$ be a formal variable (the letter $z$ changes meaning here). Let $P_x(z) = \sum_{i=0}^{N-1} x_i z^i$ be the polynomial of $x$, and $P_y(z) = \sum_{j=0}^{N-1} y_j z^j$ that of $y$. Substituting $z = 2^b$ returns the inputs: $P_x(2^b) = x$ and $P_y(2^b) = y$. Let $k$ be the position of a product coefficient, running from $0$ to $2N-2$. Let $c_k$ be the integer coefficient of $z^k$ in the product $P_x(z)P_y(z)$. Then
$$c_k = \sum_{i+j=k} x_i\, y_j,$$
with $i$ and $j$ running over $0 \le i, j \le N-1$. This is the convolution of the digit sequences $(x_i)$ and $(y_j)$, so $c_k$ is its $k$-th entry. Substituting $z = 2^b$ gives $xy = \sum_k c_k (2^b)^k$, so the product is recovered from the $c_k$. The $c_k$ are not yet binary digits, since a coefficient can exceed $2^b-1$.

**Coefficient size.** Each $c_k$ is a sum of at most $N$ products $x_i y_j$, and each product is at most $(2^b-1)^2$, so $0 \le c_k \le N(2^b-1)^2$. this bound. Since $N \le n \le 2^b$, we get $c_k \le 2^b \cdot (2^b)^2 = 2^{3b}$, with strict inequality because $(2^b-1)^2 < 2^{2b}$. Each coefficient therefore fits in $3b$ bits. Since $b = \lceil \log_2 n\rceil < \log_2 n + 1$, this is fewer than $3\log_2 n + 3$ bits, which is $O(\log n)$.

**Example.** Take $n = 4$. Then $b = 2$ and $N = 2$. Let $x = 1101$ (value 13) and $y = 1011$ (value 11). Splitting into base-4 digits from the least significant end gives $x_0 = 1$, $x_1 = 3$, $y_0 = 3$ and $y_1 = 2$. The coefficients are $c_0 = x_0 y_0 = 3$, $c_1 = x_0 y_1 + x_1 y_0 = 2 + 9 = 11$ and $c_2 = x_1 y_1 = 6$. Check: $3 + 11 \cdot 4 + 6 \cdot 16 = 143 = 13 \cdot 11$. The coefficient $c_1 = 11$ is larger than a digit, so the sequence is not yet the binary product. [Carry propagation](carry-propagation.md) converts it into one.

**Why the split lowers cost.** Without the split, the digits are single bits ($b = 1$). There are then $2n-1$ coefficients, each at most $n$, so each needs about $\log_2 n$ bits, and the stored volume is $\Theta(n\log n)$ bits. With $b = \lceil\log_2 n\rceil$ there are $2N-1$ coefficients of $3b$ bits, a volume of $(2N-1)\cdot 3b$ bits. Since $N \ge n/b$ and $N \le n/b+1$, this lies between $6n-3b$ and $6n+3b$ bits, which is $\Theta(n)$ because $b = O(\log n)$.

**Where the cost goes.** The convolution is computed with [Fourier transforms](discrete-fourier-transform.md), and each transform level applies [Butterfly](butterfly.md) operations to the whole array. On a tape, a level reads the array in order and writes each entry back at its new address, so the head must visit every stored bit once per level, and its time is proportional to the stored bits. The arithmetic is proportional too: each butterfly acts on one coefficient of $O(\log n)$ bits, so the number of operations is proportional to the number of stored bits, and each operation costs $O(\log n)$ bit steps. A level therefore costs $\Theta(n)$ after the split, and the $\Theta(\log n)$ levels multiply this. The paper's count is that The split alone thus leaves a total of $\Theta(n\log n)$, and
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

Write the answer to `exegenius/tasks/0399-audit-radix-digit-convolution.answer.json`, then run `exegenius submit 0399-audit-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
