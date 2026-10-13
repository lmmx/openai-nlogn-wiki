# exegenius task 0048-audit-fast-butterfly-layers

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
- Complex numbers
- Multitape Turing machine
- Fixed-tape machine model and stream operations
- Convolution
- Discrete Fourier transform and butterflies
- The n log n optimality conjecture
- Schönhage–Strassen to Harvey–van der Hoeven multiplication
- Reduction of integer product to digit convolution
- Bluestein's chirp identity
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms
- Signed coefficient packing (Kronecker substitution)
- Last-coordinate phase twist
- Address fields and array layout on tapes
- Finite linear network with roles and frames
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
- Fast interchange of address fields
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

- $a$ (input list a), bound on `convolution`: The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element of the ring, a power of two.
- $a$ (coefficient list), bound on `dft-fft`: The list of $n$ complex coefficients $a_0,\dots,a_{n-1}$ being transformed.
- $X$ (output value), bound on `bluestein-chirp`: The $j$th output value of the transform, for $j=0,\dots,n-1$.
- $a$ (premultiplied inputs), bound on `bluestein-chirp`: The sequence $a_k=x_k\zeta^{k^2}$, indexed by $k$.
- $S$ (cyclic convolution length), bound on `fixed-point-precision`: The number of coefficients in the cyclic convolution whose transforms are computed.
- $u$ (packed polynomial), bound on `signed-packing`: A polynomial in $\mathbb Z[y]$ of degree below $r$ whose coefficients have absolute value at most $2^p$; its packed integer is $u(B)$.
- $u$ (address field width), bound on `address-fields`: The number of bits in one address field, a count of bits.
- $V$ (stored bit volume), bound on `address-fields`: The total number of bits the array holds, a count of stored bits.
- $V$ (padded bit volume), bound on `linear-network-roles`: The number of bits stored in the array after padding, which counts the node volume the network handles.
- $a$ (initial auxiliary value), bound on `scratch-restoration`: The initial content of an auxiliary register, which may be any value.
- $H$ (first address vector), bound on `address-shear-factorization`: The vector $(H_1,\ldots,H_m)$ of $m$ address fields.
- $D$ (second address vector), bound on `address-shear-factorization`: The vector $(D_1,\ldots,D_m)$ of $m$ address fields.
- $a$ (rank), bound on `address-shear-factorization`: The rank of $A$ over $\mathbb Q$, the number of linearly independent rows of $A$.
- $V$ (stored volume), bound on `address-shear-factorization`: The stored bit volume, the number of bits held in the array.
- $f$ (call parameter), bound on `recursive-power-saving`: The parameter of a call; it counts field digits for address interchange and selected axes for a numerical layer.
- $V$ (stored bit volume), bound on `recursive-power-saving`: The number of stored bits in the array a call works on.
- $u$ (field width), bound on `fast-address-interchange`: The number of bits in each of the two address fields being interchanged.
- $V$ (stored bit volume), bound on `fast-address-interchange`: The number of bits stored in the array.
- $H$ (first field), bound on `fast-address-interchange`: The first of the two address fields, viewed as a vector of entries over a common residue ring.
- $D$ (second field), bound on `fast-address-interchange`: The second of the two address fields, viewed as a vector of entries over a common residue ring.

## Pages in the wiki

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Page to audit (`fast-butterfly-layers`)

````markdown
# Fast simultaneous butterfly layers

Fast simultaneous butterfly layers is a fixed-tape procedure that applies the butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit position in several address chunks at once. The multiplication algorithm needs it because applying the butterflies one at a time would cost one whole-array pass for each.

## The layer

Let $D$ be the number of selected address chunks. Let $d$ be an upper bound on $D$, so $D\le d$. Let $K$ be the number of bits in each chunk. Let $V$ be the number of stored bits. Let $\lambda'<1$ be a fixed exponent. The address set is the unselected bits together with the $D$ chunks, in lexicographic order. Each address holds a polynomial record with $r$ coefficients, and $H_0$ combines pairs of records coefficientwise, leaving every other address bit unchanged. The cost is $O(Vd^{\lambda'})$.

## Method

Let $X$ be the bit-flip matrix. Let $\mathsf S$ be the diagonal phase matrix $\operatorname{diag}(1,i)$. Let $C=\tfrac12\bigl((1+i)I+(1-i)X\bigr)$ be the two-point kernel. Then $H_0=\tfrac{1-i}{2}\,\mathsf S C\mathsf S$ and $C^2=X$. So each butterfly is the kernel $C$ between two diagonal phases, and $D$ selected bits give $H_0^{\otimes D}$ equal to a scalar times $\mathsf S^{\otimes D}C^{\otimes D}\mathsf S^{\otimes D}$. The phases act on each coefficient with work linear in its width, so the cost lies in computing $C^{\otimes D}$.

The tensor product $C^{\otimes D}$ is computed recursively. The layer moves whole chunks by [Fast interchange of address fields](fast-address-interchange.md) to bring each group of selected bits to a common offset. The smaller products are applied to disjoint halves of the rows, and the moves are then undone. The layer gets its exponent $\lambda'<1$ from [Recursive power saving from s<Wm](recursive-power-saving.md), since each recursive call uses fewer calls on less volume. The layer is built from the root multiplications of [Synthetic polynomial transforms](synthetic-transforms.md), which are signed shifts.

For $D=2$ and records $f_{00},f_{01},f_{10},f_{11}$ indexed by the two selected bits, the output at index $00$ is $(f_{00}+f_{01}+f_{10}+f_{11})/4$.

## Exactness

A Gaussian dyadic is a complex number whose real and imaginary parts have power-of-two denominators. Each factor $H_0$ adds at most one binary digit to the denominators, and the coefficients stay in the unit disk, so every intermediate value is an exact Gaussian dyadic. (cited). (cited) The layer's single truncation is bounded as in [Fixed-point precision and exact recovery](fixed-point-precision.md).
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

Write the answer to `exegenius/tasks/0048-audit-fast-butterfly-layers.answer.json`, then run `exegenius submit 0048-audit-fast-butterfly-layers` in the project directory. If submit rejects the answer, fix the answer and submit again.
