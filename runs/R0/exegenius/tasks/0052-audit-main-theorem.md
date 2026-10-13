# exegenius task 0052-audit-main-theorem

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
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms
- Signed coefficient packing (Kronecker substitution)
- Last-coordinate phase twist
- Convolution with retained transform order and cancelled permutations
- Address fields and array layout on tapes
- Finite linear network with roles and frames
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
- Fast interchange of address fields
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

- $n$ (input length), bound on `nlogn-conjecture`: The number of bits in each of the two integers being multiplied.
- $n$ (list length), bound on `convolution`: The number of entries in each input and output coefficient list.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on `convolution`: A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $n$ (input bit length), bound on `radix-digit-reduction`: The bit length of each input, the number of bits in each of the two integers.
- $y$ (second input), bound on `radix-digit-reduction`: The second $n$-bit input integer.
- $y$ (ring variable), bound on `poly-ring-y-r`: The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element of the ring, a power of two.
- $n$ (list length), bound on `dft-fft`: The number of coefficients in the list $a$, a power of two.
- $n$ (integer length), bound on `ss-hh-background`: The number of bits in each integer being multiplied.
- $n$ (transform length), bound on `bluestein-chirp`: The number of points in the transform.
- $j$ (output index), bound on `bluestein-chirp`: The index of an output of the transform, running from $0$ to $n-1$.
- $k$ (input index), bound on `bluestein-chirp`: The index of an input of the transform, running from $0$ to $n-1$.
- $m$ (chirp index), bound on `bluestein-chirp`: The index of the chirp sequence $b$.
- $k$ (coefficient index), bound on `phase-twist-convolution`: The index of a coefficient on the last cyclic axis, with 0 <= k < r.
- $j$ (cyclic product index), bound on `phase-twist-convolution`: The cyclic index of a product term, the residue of k+l modulo r, with 0 <= j < r.
- $u$ (packed polynomial), bound on `signed-packing`: A polynomial in $\mathbb Z[y]$ of degree below $r$ whose coefficients have absolute value at most $2^p$; its packed integer is $u(B)$.
- $u$ (address field width), bound on `address-fields`: The number of bits in one address field, a count of bits.
- $V$ (stored bit volume), bound on `address-fields`: The total number of bits the array holds, a count of stored bits.
- $n$ (input size), bound on `address-fields`: The size of the input, so that the array holds $\Theta(n)$ bits.
- $W$ (role count), bound on `linear-network-roles`: The number of roles of the network, which counts the fixed places its wires occupy.
- $V$ (padded bit volume), bound on `linear-network-roles`: The number of bits stored in the array after padding, which counts the node volume the network handles.
- $m$ (fields per vector), bound on `address-shear-factorization`: The number of address fields in each of the vectors $H$ and $D$.
- $V$ (stored volume), bound on `address-shear-factorization`: The stored bit volume, the number of bits held in the array.
- $s$ (smaller call count), bound on `subset-intersection-construction`: The total number of smaller calls, found by summing over the network's edges the rank of the difference between the matrices at the edge's two ends.
- $W$ (wire count), bound on `subset-intersection-construction`: The number of wires of the network.
- $m$ (subspace dimension), bound on `subset-intersection-construction`: The dimension of the fixed space that the subspaces lie in.
- $V$ (stored bit volume), bound on `recursive-power-saving`: The number of stored bits in the array a call works on.
- $m$ (parameter multiplier), bound on `recursive-power-saving`: The factor by which a recursive call multiplies the parameter.
- $s$ (subcall count), bound on `recursive-power-saving`: The number of subcalls a recursive call makes.
- $W$ (volume divisor), bound on `recursive-power-saving`: The divisor by which each subcall reduces the stream volume from $V$ to $V/W$.
- $u$ (field width), bound on `fast-address-interchange`: The number of bits in each of the two address fields being interchanged.
- $V$ (stored bit volume), bound on `fast-address-interchange`: The number of bits stored in the array.
- $\tau$ (cost exponent), bound on `fast-address-interchange`: A fixed exponent below 1 in the cost bound $O(Vu^\tau)$.
- $d$ (chunk bound), bound on `fast-butterfly-layers`: An upper bound on the number of selected chunks $D$; a count.
- $V$ (stored bit volume), bound on `fast-butterfly-layers`: The number of stored bits in the array; a count.
- $\lambda'$ (cost exponent), bound on `fast-butterfly-layers`: A fixed exponent below 1 in the layer's cost $O(Vd^{\lambda'})$.
- $C$ (two-point kernel), bound on `fast-butterfly-layers`: The two-by-two kernel $\tfrac12((1+i)I+(1-i)X)$ from which each butterfly is built.
- $u$ (first input array), bound on `ring-convolution-retained-order`: One of the two input arrays whose convolution is computed.

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

## Page to audit (`main-theorem`)

````markdown
# Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time, the main theorem of this wiki, is that a fixed deterministic machine multiplies $n$-bit integers within this bound, where $n$ is the number of bits in each input integer and $\kappa=2^{-182}$ is the fixed saving exponent in the logarithmic factor. It disproves the [n log n optimality conjecture](nlogn-conjecture.md).

One deterministic Turing machine computes the exact product for every $n\ge1$, (cited).

Radix-digit splitting [reduces the integer product to a convolution](radix-digit-reduction.md) of short coefficients. The machine places the coefficient list by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md) onto prime cyclic axes. Gaussian resampling, Bluestein's chirp and a phase twist then give a convolution over $\mathbb C[y]/(y^r+1)$. The machine computes its convolution by [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md). It recovers its coefficients by [Fixed-point precision and exact recovery](fixed-point-precision.md).

The machine performs its address moves by [Fast interchange of address fields](fast-address-interchange.md). It performs its butterfly layers by [Fast simultaneous butterfly layers](fast-butterfly-layers.md).

Let $V$ be the stored bit volume, $u$ the width of each address field, $d$ the number of equal-width address chunks in which one bit position is selected, and $\tau,\lambda'<1$ fixed exponents. Two tape procedures cost $O(Vu^\tau)$ for an address interchange of two $u$-bit fields and $O(Vd^{\lambda'})$ for a simultaneous butterfly layer.

Both procedures come from fixed linear networks. Let $W$ be the number of roles of each network, $s$ the total number of its smaller calls and $m$ the dimension of the space whose subspaces label its gates, so that $s<Wm$. Let $k$ be the recursion level and $F_k$ the time divided by volume at level $k$, so that $u=m^k$. A call at level $k$ makes $s$ calls at level $k-1$, each on a stream of volume $V/W$, so $F_k\le (s/W)F_{k-1}+O(1)$ with $F_0=O(1)$. Since $s/W<m$, choose a rational $\tau\in(0,1)$ with $s/W<m^\tau$. Then the sum of $(s/W)^j$ over $j\le k$ is $O(m^{k\tau})$, so $F_k=O(u^\tau)$ and the interchange costs $O(Vu^\tau)$. The butterfly layer follows the same recursion.

The $n\log n$ cost comes from scanning all stored bits at each of the $\Theta(\log n)$ transform levels. Faster versions of these operations lower the whole bound. The factor drops by $\kappa$ because $s<Wm$ is strict: the cost per unit volume grows as $m^{k\tau}$ with $\tau<1$, not linearly in the levels.
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

Write the answer to `exegenius/tasks/0052-audit-main-theorem.answer.json`, then run `exegenius submit 0052-audit-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
