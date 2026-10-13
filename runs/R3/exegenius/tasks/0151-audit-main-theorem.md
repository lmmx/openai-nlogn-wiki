# exegenius task 0151-audit-main-theorem

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
- Fast interchange of address fields (also: address interchange and numerical layer, interchange, address interchange)
- Fast simultaneous butterfly layers
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

- $n$ (integer length), bound on `nlogn-conjecture`: The number of bits in each of the two integers being multiplied.
- $\kappa$ (logarithm exponent gap), bound on `nlogn-conjecture`: A fixed positive constant, equal to 2^{-182}.
- $n$ (list length), bound on `convolution`: The number of entries in each input and output coefficient list.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix digits of each input, q = ceil(n/b).
- $s$ (root exponent), bound on `poly-ring-y-r`: The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $u$ (field width), bound on `address-fields`: The number of bits in one address field.
- $V$ (stored bit volume), bound on `address-fields`: The total number of bits the array holds.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $u$ (butterfly input u), bound on `dft-fft`: The first input of a butterfly; this letter does not denote the field width.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $O$ (odd-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the odd-indexed entries of $a$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $L$ (transform axis length), bound on `synthetic-transforms`: The number of entries along the transform axis, a power of two dividing $2r$.
- $p$ (input index), bound on `synthetic-transforms`: The index of an entry of the input list $z$, running from $0$ to $L-1$.
- $e$ (power exponent), bound on `synthetic-transforms`: An integer with $0\le e<2r$, the exponent of the power $y^e$ that multiplies a coefficient list.
- $W$ (number of roles), bound on `linear-network-roles`: The number of roles, the wires' fixed places in the network, over which rows are distributed.
- $\rho$ (role permutation), bound on `linear-network-roles`: The permutation of roles that the scalar network applies, sending input role w to output role rho(w).
- $p$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate, counting the arrays it combines.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $q$ (radix), bound on `address-shear-factorization`: The fixed odd prime that is the radix of the digits of each field.
- $u$ (numerator), bound on `address-shear-factorization`: The integer numerator of a rational entry u/v.
- $s$ (row of a one), bound on `address-shear-factorization`: The row index of a 1 in Pi.
- $d$ (second field content), bound on `address-shear-factorization`: The content of the field D_g in a pair (h,d).
- $N$ (source dimension), bound on `address-shear-factorization`: The total source dimension of the bit network.
- $N$ (list length), bound on `crt-address-map`: The number of coefficients in the list, which equals the product of the T distinct primes.
- $e$ (list index), bound on `crt-address-map`: An index of an entry of the list, an integer from 0 to N-1.
- $p$ (prime axis length), bound on `gaussian-resampling`: The number of entries in a list on a prime axis.
- $U$ (forward resampling map), bound on `gaussian-resampling`: The contraction from lists of length p to lists of length Q, equal to half the map S.
- $t$ (chirp index), bound on `bluestein-chirp`: The integer at which the chirp z_t is read.
- $p$ (working precision), bound on `fixed-point-precision`: The number of bits of precision, the power of two 2^p in each numerator's denominator.
- $L$ (log of T), bound on `fixed-point-precision`: The base-2 logarithm of T, which bounds the number of levels in the error constants.
- $u$ (packed polynomial), bound on `signed-packing`: A polynomial in $\mathbb Z[y]$ with coefficients of absolute value at most $2^p$, whose packed integer is $u(B)$.
- $t$ (second coefficient position), bound on `signed-packing`: The position of a coefficient $v_t$ of the second input polynomial.
- $d$ (block digit), bound on `signed-packing`: The digit $d_j$ stored in block $j$ of a packed integer, with $0\le d_j<B$.
- $e$ (imaginary part e), bound on `signed-packing`: The imaginary component $e\in\mathbb Z[y]$ of the second record $g$.
- $\sigma$ (layout permutation), bound on `ring-convolution-retained-order`: The permutation of addresses fixed by the layout, which moves the entry for frequency $m$ to address $\sigma(m)$.
- $F$ (vector space), bound on `tensor-product-of-vector-spaces`: The vector space whose tensor powers are formed, here Q^h in the bit network.
- $\lambda$ (scalar), bound on `tensor-product-of-vector-spaces`: A scalar of the field over which F is a vector space.
- $e$ (element), bound on `subset-intersection-construction`: An element of the ground set $[h]$.
- $m$ (label space dimension), bound on `subset-intersection-construction`: The dimension of $\mathcal F$, which counts the coordinates of a label space.
- $U$ (label), bound on `subset-intersection-construction`: A label, a nondegenerate subspace of $\mathcal F$; $U_\alpha$ is the label of index $\alpha$.
- $P_U$ (label projection), bound on `subset-intersection-construction`: The projection onto $U$ along $U^\perp$.
- $s$ (smaller-call count), bound on `subset-intersection-construction`: The number of smaller calls, the total rank over all edges.
- $N$ (index count), bound on `subset-intersection-construction`: The number of indices $\alpha$, which is $\binom h3^3$.
- $L$ (decreasing loss), bound on `subset-intersection-construction`: The total dimension lost on decreasing edges.
- $m$ (growth factor), bound on `recursive-power-saving`: The factor by which the parameter grows in one recursive call.
- $\lambda$ (power exponent), bound on `recursive-power-saving`: The fixed exponent below 1 of the power that bounds the cost per stored bit.
- $\tau$ (interchange exponent), bound on `recursive-power-saving`: The fixed exponent below 1 in the cost O(V u^tau) of an address interchange.
- $d$ (axis-count parameter), bound on `recursive-power-saving`: The paper's parameter giving the number of axes, which sets the chunk width and the threshold d^beta.
- $\sigma$ (leaf exponent), bound on `recursive-power-saving`: A fixed exponent with max{0, log_m(s/W)} at most sigma below lambda, used to bound the leaf costs.
- $\tau$ (cost exponent), bound on `fast-address-interchange`: A fixed exponent below 1 in the interchange cost $O(Vu^\tau)$, chosen so that $s/W<m^\tau$.
- $d$ (chunk-count bound), bound on `fast-butterfly-layers`: An upper bound on D, the number of selected address chunks.
- $\sigma$ (recursion exponent), bound on `fast-butterfly-layers`: The fixed exponent 1 minus 2^{-50}, below 1, with s/W < m^sigma.
- $\lambda'$ (layer exponent), bound on `fast-butterfly-layers`: The fixed exponent below 1 in the layer's cost O(V d^{lambda'}).

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

## Page to audit (`main-theorem`)

````markdown
# Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The main theorem is that one fixed deterministic Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time, where $n$ is the number of bits in each input and $\kappa=2^{-182}$ is a fixed saving exponent. It disproves the [n log n optimality conjecture](nlogn-conjecture.md) for this model.

The machine uses a fixed finite alphabet and a fixed number of one-dimensional tapes, and computes the exact product for every $n\ge1$ (cited).

[Reduction of integer product to digit convolution](radix-digit-reduction.md) turns the product into a convolution of short coefficients. The machine places its coefficient list by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md). The machine computes its convolution by [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md). The machine recovers its coefficients by [Fixed-point precision and exact recovery](fixed-point-precision.md).

The machine performs its address moves by [Fast interchange of address fields](fast-address-interchange.md). It performs its butterfly layers by [Fast simultaneous butterfly layers](fast-butterfly-layers.md). These cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$, where $V$ is the stored bit volume, $u$ the field width, $d$ the number of selected chunks, and $\tau,\lambda'<1$ fixed exponents. Here $u$ and $d$ are powers of $\lg n$ with exponents below one.

The $n\log n$ cost scans all $V$ stored bits at each of the $\Theta(\log n)$ transform levels, so cheaper moves and layers lower the whole bound.

The logarithmic factor drops by the fixed power $\kappa$ because $\kappa$ is set by the smallest margin in the sources' cost table. Each row of that table is a power $p$ with exponent one minus a margin, where $p=6\lceil\lg n\rceil$. The smallest margin is $2^{-181}$ (cited), which is $2\kappa$, so the largest power is $p^{1-2\kappa}$. A fixed power of $\log p$ is at most $p^{\kappa}$ for large $p$, so $p^{1-2\kappa}$ times it is $O(p^{1-\kappa})=O((\lg n)^{1-\kappa})$.

Both procedures come from one fixed linear network with $W$ roles and $s$ child calls. For the bit network, $s$ equals $Wm$ minus $N$, the number of negative source projections, plus twice the lost label dimension $L$ (cited), so $s<Wm$ needs $N>2L$. A negative source projection is a source operator $-P_U$, where $P_U$ projects onto a label subspace along its orthogonal complement.

Let $e=m^t$ be the number of radix-$q$ digits in a chunk at recursion level $t$, where $m$ is the number of fields per chunk and $q$ is a fixed prime. Let $F(e)$ be the time divided by $V$ at that level. Here $e$, $t$ and $F$ change meaning. Each chunk is cut into $m$ fields of $e/m$ digits. A call makes $s$ child calls on streams of volume $V/W$, and its own splitting, gates and reassembly cost $O(1)$ per unit volume (cited). Hence $F(e)\le (s/W)F(e/m)+O(e^\tau+1)$ with $F(1)=O(1)$, since the children cost $s(V/W)F(e/m)$ and dividing by $V$ gives $s/W$.

Put $\rho=(s/W)/m^\tau$, not the role permutation of earlier pages. Since $s/W<m$, some rational $\tau<1$ gives $\rho<1$; this is where $s<Wm$ is used. Dividing by $m^{t\tau}$ gives $m^{-t\tau}F(m^t)\le\rho\,m^{-(t-1)\tau}F(m^{t-1})+O(1)$, since $e^\tau+1\le 2e^\tau$. Unrolling gives a geometric sum with ratio $\rho<1$, so $F(m^t)=O(m^{t\tau})$. A field of $e$ radix-$q$ digits has $\Theta(e)$ bits, because $q$ is fixed, so $e$ is proportional to $u$ and the interchange costs $O(Vu^\tau)$. The butterfly layer uses a second fixed network, also with $s<Wm$, and runs the same recursion on the $d$ selected chunks, so it costs $O(Vd^{\lambda'})$ once $\lambda'$ exceeds two exponents.

Nodes with at least $\sqrt d$ active chunks have node overhead of $O(e^\lambda)$ per unit volume, with $e\le d$ and $\lambda=1-2^{-52}$. Smaller nodes, the small-level leaves, cost $O(d^{\sigma+(1-\sigma)/2})$ with $\sigma=1-2^{-50}$. So $\lambda'$ must exceed $\lambda$ and $\sigma+(1-\sigma)/2$, and $\lambda'=1-2^{-54}$ does.
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

Write the answer to `exegenius/tasks/0151-audit-main-theorem.answer.json`, then run `exegenius submit 0151-audit-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
