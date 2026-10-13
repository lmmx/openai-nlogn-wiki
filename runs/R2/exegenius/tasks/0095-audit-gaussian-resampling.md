# exegenius task 0095-audit-gaussian-resampling

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
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms
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

- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $j$ (rule index), bound on `poly-ring-y-r`: The index of the coefficient that the wrap rule $y^{r+j}=-y^j$ reduces to, ranging over $0\le j<r$.
- $L$ (axis length), bound on `poly-ring-y-r`: The number of entries along one of the remaining transform axes, a divisor of $2r$.
- $p$ (working precision), bound on `fixed-point-precision`: The number of fractional bits in each numerator, $p=6b$ in the source.
- $L$ (log of padded length), bound on `fixed-point-precision`: The base-2 logarithm of $T$.
- $m$ (cell position), bound on `address-fields`: The position of an item in the array, which is also its address written in binary.
- $m$ (frequency index), bound on `dft-fft`: The frequency index of an entry of a transform, $0\le m<n$; it is also the exponent in $\omega^m$.
- $t$ (block offset), bound on `dft-fft`: The offset of an entry within a block.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transformed list, a power of two dividing 2r.
- $m$ (primitivity exponent), bound on `synthetic-transforms`: An exponent used to test that the root has order exactly t.
- $G$ (pointwise gate), bound on `linear-network-roles`: The pointwise linear gate operation that combines input arrays at each address.
- $t$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate.
- $m$ (field count), bound on `address-shear-factorization`: The number of fields in each of the vectors $H$ and $D$.
- $m$ (label dimension), bound on `subset-intersection-construction`: The dimension of the label space $\mathcal F$, which is $h^3$.
- $J$ (all-one matrix), bound on `subset-intersection-construction`: The $h\times h$ matrix with every entry equal to 1.
- $L$ (lost label dimension), bound on `subset-intersection-construction`: The total dimension lost by the label along the decreasing edges of the network.
- $m$ (parameter factor), bound on `recursive-power-saving`: The factor by which a call's parameter is multiplied in the recursive call.
- $t$ (prime count), bound on `crt-address-map`: The number of distinct primes whose product is $N$, which is also the number of axes.

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

## Page to audit (`gaussian-resampling`)

````markdown
# Gaussian resampling

Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution (cited). It lets the fast machinery of the main theorem work only on power-of-two axes.

A standard FFT of length $2m$ splits into two transforms of length $m$, where $m$ is the number of points in each half. A prime-length transform has no such split, so each prime axis would otherwise need its own fast algorithm.

Write $F_L$ for the discrete Fourier transform of a list with $L$ entries, which evaluates the list at the $L$-th roots of unity, and $P_L$ for a fixed reordering of its $L$ coordinates. Here $L$ is the number of entries in the list.

Let $p_j$ be one of the prime axis lengths, and let $t$ be a power of two, the number of points in the power-of-two transform, chosen slightly above $p_j$. The identity is

$$P_{p_j}F_{p_j}=2^{e}\,J\,P_tF_t\,G,$$

where $G$ maps lists of length $p_j$ to lists of length $t$, $J$ maps back, and $e$ is a fixed integer exponent. $G$ and $J$ are linear contractions, maps that do not increase the largest modulus of an entry. Harvey and van der Hoeven prove the identity and the inverse bound (cited).

Why it holds: $G$ and $J$ are sums weighted by Gaussians that move values between the two grids. The Fourier transform maps a Gaussian to a Gaussian, so transforming on one grid agrees with transforming the Gaussian-weighted list on the other. The compensated map from one grid to the other is within less than one half of the identity in norm, so it can be inverted, and $J$ is built from that inverse.

To evaluate $F_{p_j}$ on a list, apply $G$, then $P_tF_t$, then $J$. Multiplying by $2^{e}$ and undoing the permutation $P_{p_j}$ gives the prime transform of the same list.

Gaussian resampling acts on the axes placed by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md), removing the prime-length transform along each one. Gaussian resampling thus computes its transforms by the butterfly layers of [Discrete Fourier transform and butterflies](dft-fft.md), since a transform of length $t$ has $\lg t$ layers, each linear in the array size. So the later butterfly and address-move speedups apply to these transforms.
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

Write the answer to `exegenius/tasks/0095-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0095-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
