# exegenius task 0099-audit-ring-convolution-retained-order

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows the concepts listed as known, and everything the reader profile covers: what anyone with that background has been taught, whether or not the profile names it (a profile of undergraduate computer science covers logarithms and proof by induction without naming them). Anything outside that, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source. A citation lets the reader check a result, not follow an argument: a cited result the page uses is followable if the page says what it states and why it applies where it is used, and its proof can be left to the source. A cited claim that stands in for how the page's own concept works, or whose content or role the page does not say, is a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives. A claim about an identity, construction or definition that the page never states is a step.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers (also: Gaussian integer)
- Multitape Turing machine
- Fixed-tape machine model and stream operations (also: fixed-tape machine)
- Convolution
- Discrete Fourier transform and butterflies
- The n log n optimality conjecture
- Schönhage–Strassen to Harvey–van der Hoeven multiplication
- Reduction of integer product to digit convolution
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms
- Signed coefficient packing (Kronecker substitution)
- Last-coordinate phase twist
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network)
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
- Fast interchange of address fields (also: address interchange and numerical layer, interchange)
- Fast simultaneous butterfly layers
- Fixed-point precision and exact recovery
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)

## Symbols bound on earlier pages

- $n$ (input bit length), bound on `nlogn-conjecture`: The number of bits in each of the two integers being multiplied.
- $n$ (list length), bound on `convolution`: The number of entries in each input and output coefficient list.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on `convolution`: A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $y$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $y$ (ring variable), bound on `poly-ring-y-r`: The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element, a power of two.
- $k$ (shift exponent), bound on `poly-ring-y-r`: The exponent of the power $y^k$ that acts as a signed shift, with $0\le k<r$.
- $L$ (axis length), bound on `poly-ring-y-r`: The number of entries along one of the remaining transform axes, a divisor of $2r$.
- $L$ (log of padded length), bound on `fixed-point-precision`: The base-2 logarithm of $T$.
- $O$ (odd-index transform), bound on `dft-fft`: The transform, with root $\omega^2$, of the odd-indexed entries of $a$.
- $C$ (transform of c), bound on `dft-fft`: The transform of the cyclic convolution $c$.
- $g$ (output index), bound on `synthetic-transforms`: A position in the transformed list, running from 0 to t-1.
- $g$ (logical array), bound on `linear-network-roles`: The array the network computes on before the frame is applied.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $D$ (second field vector), bound on `address-shear-factorization`: A vector of $m$ address fields, $D_1,\ldots,D_m$.
- $M$ (rational matrix), bound on `address-shear-factorization`: A rational $m\times m$ matrix whose shear $(H,D)\mapsto(H+MD,D)$ is taken.
- $g$ (column index), bound on `address-shear-factorization`: The column index of an entry of $\Pi$.
- $L$ (lost label dimension), bound on `subset-intersection-construction`: The total dimension lost by the label along the decreasing edges of the network.
- $f$ (call parameter), bound on `recursive-power-saving`: The parameter of a call, counting field digits for address interchange or selected axes for a numerical layer.
- $C$ (overhead constant), bound on `recursive-power-saving`: The constant bounding the normalized outside work at a node.
- $D$ (selected chunk count), bound on `fast-butterfly-layers`: The number of selected address chunks, which counts the chunks carrying the selected bit.
- $C$ (two-point kernel), bound on `fast-butterfly-layers`: The $2\times 2$ matrix $\tfrac12((1+i)I+(1-i)X)$ from which each butterfly is built.
- $L$ (list length), bound on `gaussian-resampling`: The number of entries in a list to which a transform or reordering applies.
- $g$ (premultiplied input), bound on `bluestein-chirp`: The $k$th input $a_k$ multiplied by the chirp phase $\zeta^{k^2}$.
- $k$ (input index), bound on `bluestein-chirp`: The index of an input $a_k$, ranging over the inputs.
- $k$ (last-axis index), bound on `phase-twist-convolution`: An index of a coefficient on the last axis, with $0\le k<r$.
- $k$ (product coefficient index), bound on `signed-packing`: The index of a coefficient of the ordinary product $h$, so that $h_k$ is the coefficient of $y^k$.

## Pages in the wiki

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Page to audit (`ring-convolution-retained-order`)

````markdown
# Convolution with retained transform order and cancelled permutations

Convolution with retained transform order convolves two arrays over $\mathbb C[y]/(y^r+1)$ by transforming each one, multiplying the transforms entry by entry, and transforming back, without sorting the frequency entries in between. The main result reduces integer multiplication to this convolution.

This convolution computes its transforms by [Synthetic polynomial transforms](synthetic-transforms.md), which need only signed shifts, address rearrangements and butterflies.

Let $f$ and $g$ be the two input arrays. Let $\mathcal{D}$ be the forward transform applied to each. Let $\mathcal{D}^{+}$ be the opposite transform. Here $M$ is a known scalar, fixed by the normalization of the transforms. With $\odot$ the entrywise product of ring elements at the same address, the first identity below is the convolution theorem with a scalar, and the second says that $\mathcal{D}^{+}$ inverts $\mathcal{D}$ up to $M$:

$$\mathcal{D}(f*g)=M\,(\mathcal{D}f)\odot(\mathcal{D}g), \qquad \mathcal{D}^{+}\mathcal{D}=\tfrac{1}{M}\,I.$$

The second identity is checked by expanding the finite sums of the transform (cited).

Let $L$ be the permutation of addresses that the forward transform applies to its output, so that the frequency order is the order of those addresses. Let $k$ index the frequency entries, the positions in that order. If the two forward transforms ordered their outputs differently, the entry at position $k$ of $\mathcal{D}f$ would be multiplied by an entry of $\mathcal{D}g$ at a different frequency, and a sort would be needed to align them. Both forward transforms therefore store their outputs in order $L$, so the stored arrays are $L\mathcal{D}f$ and $L\mathcal{D}g$, and the two forward transforms keep the same frequency order through the pointwise product (cited).

Since $L$ moves entries by address and each product entry uses only the two entries at its address, the product of the stored arrays equals $L$ applied to the product of the transforms:

$$(L\mathcal{D}f)\odot(L\mathcal{D}g)=L\big((\mathcal{D}f)\odot(\mathcal{D}g)\big).$$

The opposite transform applies $L^{-1}$ first, so the $L$ cancels and no sort is run. The opposite transform consumes that order (cited).

$$\mathcal{D}^{+}L^{-1}\big((L\mathcal{D}f)\odot(L\mathcal{D}g)\big)=\mathcal{D}^{+}\big((\mathcal{D}f)\odot(\mathcal{D}g)\big)$$

By the first identity, the right-hand side is $f*g$ up to a known scalar, because $\mathcal{D}^{+}$ inverts $\mathcal{D}$ up to $M$. For example, if $L$ swaps two records, $L^{-1}$ swaps them back before $\mathcal{D}^{+}$ acts.

This convolution computes its products through [Signed coefficient packing (Kronecker substitution)](signed-packing.md): polynomial products are packed into integers and multiplied by the ordinary $O(n\log n)$ multiplier as a subroutine.

This convolution is applied after [Gaussian resampling](gaussian-resampling.md), which writes each source transform through a power-of-two tensor transform. This convolution is taken over the ring from the [Last-coordinate phase twist](phase-twist-convolution.md), in which the negative wrap gives the original cyclic wrap.
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

Write the answer to `exegenius/tasks/0099-audit-ring-convolution-retained-order.answer.json`, then run `exegenius submit 0099-audit-ring-convolution-retained-order` in the project directory. If submit rejects the answer, fix the answer and submit again.
