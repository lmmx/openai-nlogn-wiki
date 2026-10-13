# exegenius task 0149-audit-fast-address-interchange

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
- Discrete Fourier transform and butterflies (also: transform (the DFT/FFT the layout is for), twiddle factor, bit-reversed input, forward transform of length S)
- The n log n optimality conjecture
- Schönhage–Strassen to Harvey–van der Hoeven multiplication
- Reduction of integer product to digit convolution
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling (also: Gaussian (weighting function))
- Bluestein's chirp identity
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms (also: fast transform and transform axes)
- Signed coefficient packing (Kronecker substitution)
- Last-coordinate phase twist
- Convolution with retained transform order and cancelled permutations
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network, source and sink nodes of a route)
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values (also: scratch (auxiliary) roles)
- Fixed-point precision and exact recovery (also: source scale 2^gamma)
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map, norm)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)
- Tensor product of vector spaces (also: tensor power)

## Symbols bound on earlier pages

- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $j$ (reduction offset), bound on `poly-ring-y-r`: The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $s$ (root exponent), bound on `poly-ring-y-r`: The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $u$ (field width), bound on `address-fields`: The number of bits in one address field.
- $V$ (stored bit volume), bound on `address-fields`: The total number of bits the array holds.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $u$ (butterfly input u), bound on `dft-fft`: The first input of a butterfly; this letter does not denote the field width.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $O$ (odd-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the odd-indexed entries of $a$.
- $C$ (transform of c), bound on `dft-fft`: The transform of the convolution list $c$.
- $W$ (number of roles), bound on `linear-network-roles`: The number of roles, the wires' fixed places in the network, over which rows are distributed.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $H$ (first field vector), bound on `address-shear-factorization`: The vector of m address fields $(H_1,\ldots,H_m)$ that the shear updates.
- $D$ (second field vector), bound on `address-shear-factorization`: The vector of m address fields $(D_1,\ldots,D_m)$ that the shear reads.
- $u$ (numerator), bound on `address-shear-factorization`: The integer numerator of a rational entry u/v.
- $s$ (row of a one), bound on `address-shear-factorization`: The row index of a 1 in Pi.
- $Q$ (replacing power-of-two length), bound on `gaussian-resampling`: The number of entries in the power-of-two list that replaces a list of length p, chosen slightly above p.
- $j$ (output index), bound on `bluestein-chirp`: The index of an output of the transform, running from 0 to n-1.
- $k$ (input index), bound on `bluestein-chirp`: The index of an input a_k of the transform, running from 0 to n-1.
- $k$ (last-axis exponent), bound on `phase-twist-convolution`: An exponent on the last axis, with $0\le k<r$, indexing one coefficient.
- $j$ (cyclic product index), bound on `phase-twist-convolution`: The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
- $u$ (packed polynomial), bound on `signed-packing`: A polynomial in $\mathbb Z[y]$ with coefficients of absolute value at most $2^p$, whose packed integer is $u(B)$.
- $k$ (product coefficient index), bound on `signed-packing`: The exponent $k$ of a coefficient $h_k$ of the product polynomial, running over $0,\dots,2r-2$.
- $j$ (coefficient position), bound on `signed-packing`: The position of a coefficient $u_j$ of a packed polynomial, which is also its block exponent.
- $F$ (vector space), bound on `tensor-product-of-vector-spaces`: The vector space whose tensor powers are formed, here Q^h in the bit network.
- $m$ (label space dimension), bound on `subset-intersection-construction`: The dimension of $\mathcal F$, which counts the coordinates of a label space.
- $s$ (smaller-call count), bound on `subset-intersection-construction`: The number of smaller calls, the total rank over all edges.
- $m$ (growth factor), bound on `recursive-power-saving`: The factor by which the parameter grows in one recursive call.
- $C$ (outside-work constant), bound on `recursive-power-saving`: A constant bounding the outside work at a node of parameter mf.
- $\tau$ (interchange exponent), bound on `recursive-power-saving`: The fixed exponent below 1 in the cost O(V u^tau) of an address interchange.

## Pages in the wiki

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Page to audit (`fast-address-interchange`)

````markdown
# Fast interchange of address fields

Fast interchange of address fields is a fixed-tape procedure that swaps two disjoint contiguous address fields of an array, and the multiplication construction uses it to speed up its address moves. The procedure acts on fields of arrays laid out as in [Address fields and array layout on tapes](address-fields.md), so each field is a block of $u$ contiguous bits. Write $H$ and $D$ for the two fields, each viewed as a vector of entries over a common residue ring; for the bit procedure this ring is $\mathbb F_2$, where subtraction and addition coincide. Here $\tau$, the fixed exponent below 1 in the cost, is the exponent in $O(Vu^\tau)$ (cited).

Swapping takes three updates, applied componentwise:

$$D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D.$$

Starting from $(H,D)$ they give $(H,D-H)$, then $(D,D-H)$, then $(D,H)$, since $H+(D-H)=D$ and $D-(D-H)=H$. For example, with $(H,D)=(1,0)$ over $\mathbb F_2$ the states are $(1,1)$, $(0,1)$, $(0,1)$, which is $(D,H)$.

The network performs only the middle update, which is the costly one. The procedure is built from the [Address shear and lower-triangular factorization](address-shear-factorization.md): the network's endpoint operator is the shear $(H,D)\mapsto(H+D,D)$ over $\mathbb F_2$, with rank reduced by a lower-triangular factorization. Two further linear-cost address updates complete the interchange. Both change only $D$, each combining $D$ with the earlier field $H$ in linear time.

The cost bound follows from [Recursive power saving from s<Wm](recursive-power-saving.md). The network has $W$ roles, and each of its $s$ smaller calls acts on one role stream of volume $V/W$, where $s$ is the sum of the edge ranks. For the bit network, $s<Wm$ (cited); the paper's proof computes $s$ as $Wm$ minus a positive constant fixed by the construction. Hence $s/W<m$. Since $m^\tau\to m$ as $\tau\to1$, fix $\tau<1$ with $s/W<m^\tau$.

Let $Q_k$ bound the time per unit of volume for interchanging fields of $m^k$ bits, where $k$ is the recursion level. A level-$k$ call makes $s$ calls at level $k-1$, each on volume $V/W$, plus $O(V)$ outside work whose normalized cost is at most $C$. Hence
$$Q_0=O(1),\qquad Q_k\le \frac{s}{W}\,Q_{k-1}+C.$$
Unrolling gives $Q_k\le (s/W)^k Q_0+C\sum_{j<k}(s/W)^j$. The first term is $O(m^{k\tau})$ because $s/W<m^\tau$. The geometric sum is also $O(m^{k\tau})$: if $s/W\le1$ it is at most $k$, and if $s/W>1$ it is $O((s/W)^k)$. Both are $O(m^{k\tau})$, since $m\ge2$. A field of $u=m^k$ bits therefore has $Q_k=O(u^\tau)$, and the interchange costs $O(Vu^\tau)$.

The final effect is an exact permutation, although the network uses only pointwise XOR gates, so its intermediate values are XOR combinations of data. Over $\mathbb F_2$ each update is a pointwise XOR, since addition and subtraction are the same operation; after the first update $D$ holds the XOR of $D$ and $H$. The shear is applied to every row, including scratch rows with arbitrary contents. Exactness is secured by the [Restoring auxiliary scratch values](scratch-restoration.md) schedule, which subtracts the initial register value, computes, adds the result back, and reverses; the initial contents cancel, so the final permutation does not depend on them. (cited).
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

Write the answer to `exegenius/tasks/0149-audit-fast-address-interchange.answer.json`, then run `exegenius submit 0149-audit-fast-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
