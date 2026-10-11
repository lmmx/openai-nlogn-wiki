# exegenius task 0384-audit-linear-network-frames

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
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Little-o notation (also: limit as lambda tends to infinity)
- Array norm (also: norm of an array, coefficient bound)
- Payload (also: record)
- Polynomial ring (also: polynomial suffix)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Bijection
- Permutation
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $H$ (layer), bound on `truncation`: The operation that applies a two-point map to each pair of entries whose addresses differ in one of several selected bits, in one pass.
- $\alpha$ (first paired value), bound on `truncation`: The first of the two values that the layer combines in each pair.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $g_t$ (level bound), bound on `mathematical-induction`: A bound on the cost after t levels.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\theta$ (homomorphism), bound on `ring-homomorphism`: A map from one ring to another that preserves both operations.
- $\alpha$ (coefficient), bound on `ring-homomorphism`: The complex constant term of an element $\alpha+\delta t$ of $Q$.
- $\rho$ (reduction map), bound on `ring-homomorphism`: The map from $Q$ to $\mathbb{C}$ sending $\alpha+\delta t$ to $\alpha+\delta$.
- $\alpha$ (address), bound on `address`: A string of d bits that labels one entry of the array.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $D_v$ (frame of vertex v), bound on `linear-algebra-basics`: The frame of vertex $v$, an invertible linear operator on arrays.
- $D_u$ (frame of vertex u), bound on `linear-algebra-basics`: The frame of vertex $u$, an invertible linear operator on arrays.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $H$ (address chunk), bound on `linear-algebra-basics`: A binary address chunk, one of the two fields of an address pair.
- $K$ (second address chunk), bound on `linear-algebra-basics`: A binary address chunk, the second field of an address pair.

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

## Page to audit (`linear-network-frames`)

````markdown
# Linear networks and frames

A linear network with frames realises each tape procedure on arrays: a fixed wiring of linear gates that exchanges two banks of values and restores its auxiliary (scratch) values. It is the step that lets the main result count the cost of each procedure.

A bank is a set of wires indexed by a common index set, so exchanging two banks swaps the values at matching indices., and it.

A gate is a fixed linear map on some wires, and..

Each scalar becomes an array indexed by a common set of addresses, and each gate acts separately at each address. The logical array $g$ is the array a wire is meant to represent. Each vertex $v$ carries an invertible linear operator $D_v$, its frame, so the stored array there is $D_v g$. Frames are built from invertible linear operators, as defined in [Linear algebra basics](linear-algebra-basics.md).

Let an edge go from $u$ to $v$, where $u$ is the earlier vertex.: the edge operator $D_v D_u^{-1}$ takes $D_u g$ to $D_v g$, while $g$ does not change.

Let $G$ be a pointwise linear gate with $t$ inputs, where $t$ is the number of input arrays it takes. Its inputs are logical arrays $g_1,\dots,g_t$, and each input $s$ has a fixed weight $\alpha_s$, the same at every address.

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

This is why frames sit on the wires. A gate adds its inputs entrywise, so inputs in different frames would not add to the stored form of the sum. With one frame $D_v$ on every input and on the output, the gate computes the logical sum in stored form, and the representation is unchanged. For example, take $t = 2$, $G(g_1, g_2) = g_1 + g_2$, and let $D_v$ have rows $(1, 1)$ and $(0, 1)$. For $g_1 = (1, 0)$ and $g_2 = (0, 1)$, the stored inputs $(1, 0)$ and $(1, 1)$ sum to $(2, 1)$, which is $D_v(1, 1)$.

Inputs must share one frame, and.. Write $\ell$ for an input wire, $\theta_\ell$ for its supplied physical array, and $\mathrm{source}(\ell)$ for its source vertex. Its logical array is $g_\ell = D_{\mathrm{source}(\ell)}^{-1}\theta_\ell$.

A permutation $\rho$ of roles sends each input role $\ell$ to an output role $\rho(\ell)$, multiplying by a fixed sign $\varepsilon_\ell$. Write $\mathrm{sink}(r)$ for the sink vertex of output role $r$. Along a route through vertices $x_0,\dots,x_k$, where $x_0=\mathrm{source}(\ell)$ and $x_k=\mathrm{sink}(\rho(\ell))$, each inner pair $D_{x_i}^{-1}D_{x_i}$ cancels, so the edge operators telescope to $D_{x_k}D_{x_0}^{-1}$., leaving the endpoint operator

$$\varepsilon_\ell\, D_{\mathrm{sink}(\rho(\ell))}\, D_{\mathrm{source}(\ell)}^{-1}\,\theta_\ell.$$

 The bit procedure is realised by the bit network, a linear network on bits, which. Its frames act on the [Address field](address-field.md) blocks of each array, with $H$ the first field and $K$ the second, not a frame.:. Over bits $H+K$ is a bitwise XOR, so the shear is a pointwise XOR of the two fields, which is why an XOR network with frames on the address fields realises it., the XOR swap $H\leftarrow H+K$, $K\leftarrow K+H$, $H\leftarrow H+K$.

The claim is that each tape procedure is such a network. The scalar network (the wiring on single values) The endpoint formula then gives each route's operator.
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

Write the answer to `exegenius/tasks/0384-audit-linear-network-frames.answer.json`, then run `exegenius submit 0384-audit-linear-network-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.
