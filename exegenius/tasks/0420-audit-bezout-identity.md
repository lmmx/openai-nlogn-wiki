# exegenius task 0420-audit-bezout-identity

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
- Cyclic convolution
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
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic)
- Centered residue
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
- Cyclic coordinate (also: last cyclic coordinate)
- Line spanned by a vector
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
- Bit network (also: the paper's bit network)
- Chinese remainder theorem (also: CRT)
- Eigenvalue
- Incidence
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Orthogonal complement
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $\kappa$ (fixed exponent constant), bound on `running-time-cost`: A fixed constant, equal to $2^{-182}$, that sets the exponent $1-\kappa$ in the running time bound.
- $\beta$ (second paired value), bound on `truncation`: The second of the two values that the layer combines in each pair.
- $\kappa$ (exponent gap), bound on `schoolbook-multiplication`: A fixed constant, $2^{-182}$, which sets the saving in the exponent $1-\kappa$ of the bound.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $\kappa$ (saving exponent), bound on `little-o-notation`: The fixed positive constant 2^{-182} in the saving exponent $1-\kappa$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $\gamma$ (second integer), bound on `coprime`: The other integer whose greatest common divisor with beta is taken, not both zero with it.
- $\gcd$ (greatest common divisor), bound on `coprime`: The function giving the largest positive integer that divides both of two integers.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $d$ (number of source lengths), bound on `coprime`: The number of lengths s_1 through s_d in the split.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $d$ (address length), bound on `address`: The number of bits in each address of an array.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $d$ (second scalar), bound on `linear-algebra-basics`: A scalar in $F$, added to another scalar in the axiom $(c+d)x=cx+dx$.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $d$ (zero-sum vector), bound on `eigenvalue`: A vector in Q^h whose entries sum to zero.
- $\tau$ (complex number), bound on `phase-factor`: A complex number written as alpha plus beta i.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number tau, a real number.
- $\nu$ (second input index), bound on `discrete-fourier-transform`: A second integer index from 0 to q-1 that numbers the input coordinates in the inverse identity.
- $\nu$ (input position), bound on `multidimensional-transform`: A position in the input array, a tuple of D coordinates with the s-th coordinate between 0 and t_s minus 1.
- $\kappa$ (output position), bound on `multidimensional-transform`: A position in the output array, a tuple of D coordinates with the same bounds as a position in the input array.
- $d$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $\tau$ (butterfly offset), bound on `synthetic-transforms`: The offset of a butterfly pair within the first half of its block, from $0$ to $\delta-1$.
- $\kappa$ (running time exponent constant), bound on `synthetic-transforms`: A fixed positive constant in the exponent of the running time bound.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\tau$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring whose positive integer power equals 1.
- $\nu$ (exponent), bound on `polynomial-ring-mod-yr-plus-1`: The positive integer power to which a root of unity is raised to give 1, counting the factors of the product.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than $s$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\nu$ (second numerator), bound on `gaussian-dyadics`: The Gaussian integer numerator of the second Gaussian dyadic $\nu/2^{e'}$.
- $\tau$ (common exponent), bound on `gaussian-dyadics`: The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $\kappa$ (off-diagonal coefficient), bound on `two-point-kernel`: The coefficient of $X$ in $K$, a complex number.
- $d$ (address length), bound on `two-point-kernel`: The number of bits in a binary address, a count.
- $\nu$ (address), bound on `two-point-kernel`: An integer whose binary form with $d$ bits is one address of an array.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $t$ (address bit string), bound on `tensor-product`: A bit string of length m that is an address on m coordinates.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $d$ (second argument), bound on `bilinear-map`: An element of the second argument space H.
- $\kappa$ (real input), bound on `ceiling-function`: The real number whose ceiling is taken.
- $\tau$ (processed positions), bound on `carry-propagation`: The number of low positions already processed, so that the sums run over $t < \tau$.
- $d$ (first integer), bound on `congruence-modulo`: An integer, the first of the two integers compared for congruence.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $\nu$ (class member), bound on `congruence-modulo`: An integer congruent to d modulo B, a member of the residue class of d.
- $\tau$ (field element), bound on `binary-field`: An arbitrary element of the binary field, so it is $0$ or $1$.
- $\nu$ (bit column), bound on `binary-change-of-basis`: The column of values of the selected bits, each an element of $\mathbb F_2$.
- $\kappa$ (address), bound on `binary-change-of-basis`: A vector in $\mathbb F_2^m$, one address of the selected bits.
- $\nu$ (target bank), bound on `bit-network`: The target bank, a vector with one bit for each triple.
- $\tau$ (choice of three triples), bound on `line-spanned-by-vector`: A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $\kappa$ (modulus), bound on `centered-residue`: A positive integer, the modulus by which residues are taken.
- $\nu$ (integer to reduce), bound on `centered-residue`: The integer whose residue modulo $\kappa$ is taken.
- $\tau$ (centered residue), bound on `centered-residue`: The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\nu$ (congruence index), bound on `chinese-remainder-theorem`: An index numbering the congruences, running from 1 to $\chi$.
- $\tau$ (solution), bound on `chinese-remainder-theorem`: An unknown integer, which is a solution when it satisfies every congruence of the system.
- $d$ (number of axes), bound on `cyclic-convolution`: The number of pairwise coprime factors of n, which is the number of axes of the multidimensional cyclic convolution.
- $\kappa$ (axis index), bound on `cyclic-convolution`: The index of an axis, running from 1 to d.
- $\tau$ (reflected chirp), bound on `cyclic-convolution`: The function tau(delta) of an integer delta, read as a sequence of length t.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\nu$ (coordinate index), bound on `cyclic-coordinate`: The index naming one cyclic coordinate, running from 1 to d.
- $\kappa$ (last-axis position), bound on `cyclic-coordinate`: An integer from 0 to r-1 giving a position along the last cyclic coordinate.

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

## Page to audit (`bezout-identity`)

````markdown
# Bézout's identity

Bézout's identity says that the greatest common divisor of two integers is an integer combination of them. It supplies the [modular inverses](modular-inverse.md) that the [Chinese-remainder map](chinese-remainder-map.md) needs when its lengths are coprime.

Let $\beta$ and $\gamma$ be integers, not both zero. Write $d=\gcd(\beta,\gamma)$ for their greatest common divisor, the largest positive integer dividing both. Bézout's identity is stated in terms of the greatest common divisor, which the [Coprime](coprime.md) page defines. The integer $\mu$ is the Bézout coefficient of $\beta$: the integer multiplying $\beta$ in a combination of $\beta$ and $\gamma$ that equals $d$. The integer $\nu$ is the Bézout coefficient of $\gamma$: the integer multiplying $\gamma$ in a combination of $\beta$ and $\gamma$ that equals $d$. The identity says that such integers exist:
$$\beta\mu+\gamma\nu=d.$$

The identity holds for every such pair, and the proof shows how to find $\mu$ and $\nu$. Let $\mu'$ and $\nu'$ be trial integers, which need not yet be the Bézout coefficients. Let $e$ be the least positive integer that can be written as $\beta\mu'+\gamma\nu'$ with $\mu'$ and $\nu'$ integers. The set of such positive values is nonempty because $\beta\beta+\gamma\gamma>0$, so $e$ exists. Divide $\beta$ by $e$: $\beta=\kappa e+\tau$ with $0\le\tau<e$, where $\kappa$ is the integer quotient and $\tau$ the remainder. Then $\tau=\beta(1-\kappa\mu')+\gamma(-\kappa\nu')$ has the same form, and it is smaller than $e$, so minimality forces $\tau=0$. Thus $e$ divides $\beta$, and the same argument shows $e$ divides $\gamma$. Hence $e\le d$. Conversely, $d$ divides $\beta$ and $\gamma$, so $d$ divides $e=\beta\mu'+\gamma\nu'$, giving $d\le e$. So $e=d$, and the trial coefficients $\mu'$ and $\nu'$ are the required $\mu$ and $\nu$.

For $\beta=3$ and $\gamma=5$ we have $d=1$, and $3\cdot 2+5\cdot(-1)=1$, so $\mu=2$ and $\nu=-1$. The coefficients are not unique: $\mu=2+5t$ and $\nu=-1-3t$ also work for every integer $t$, because $3(2+5t)+5(-1-3t)=1$. For $\beta=12$ and $\gamma=18$ we have $d=6$ and $12\cdot(-1)+18\cdot 1=6$, so the combination equals the greatest common divisor rather than $1$.

When $\beta$ and $\gamma$ are coprime, $d=1$ and $\beta\mu\equiv 1 \pmod{\gamma}$, so $\mu$ is an inverse of $\beta$ modulo $\gamma$. For $3$ and $5$ this gives $\mu=2$, since $6\equiv 1 \pmod 5$.

The paper uses the same algorithm to reduce rational coefficients:.
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

Write the answer to `exegenius/tasks/0420-audit-bezout-identity.answer.json`, then run `exegenius submit 0420-audit-bezout-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
