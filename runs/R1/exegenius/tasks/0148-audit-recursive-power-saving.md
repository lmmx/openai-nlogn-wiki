# exegenius task 0148-audit-recursive-power-saving

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
- $\nu$ (network node), bound on `linear-network-roles`: A source, gate or sink of the network, which carries one frame.
- $\beta$ (edge head), bound on `linear-network-roles`: The node at which an edge ends.
- $f$ (logical array), bound on `linear-network-roles`: The logical array that a node stores in the form D_nu f.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $u$ (numerator), bound on `address-shear-factorization`: The integer numerator of a rational entry u/v.
- $s$ (row of a one), bound on `address-shear-factorization`: The row index of a 1 in Pi.
- $d$ (second field content), bound on `address-shear-factorization`: The content of the field D_g in a pair (h,d).
- $\nu$ (axis index), bound on `crt-address-map`: The index of one prime and of its axis, running from 1 to T.
- $K$ (backward resampling map), bound on `gaussian-resampling`: The contraction from lists of length Q back to lists of length p, which undoes the resampling.
- $\Phi$ (compensated map), bound on `gaussian-resampling`: The compensated map from lists of length p to lists of length p, close to the identity and hence invertible.
- $\beta$ (second entry coefficient), bound on `phase-twist-convolution`: The untwisted coefficient $\beta_l$ of the second entry at index $l$.
- $\Phi$ (forward transform), bound on `fixed-point-precision`: The forward transform of length S, whose entries are the normalized sums (1/S) times the sum of xi_k omega^{mk}.
- $u$ (packed polynomial), bound on `signed-packing`: A polynomial in $\mathbb Z[y]$ with coefficients of absolute value at most $2^p$, whose packed integer is $u(B)$.
- $d$ (block digit), bound on `signed-packing`: The digit $d_j$ stored in block $j$ of a packed integer, with $0\le d_j<B$.
- $f$ (first record), bound on `signed-packing`: The first polynomial record, a polynomial of degree less than $r$ with complex fixed-point coefficients.
- $\sigma$ (layout permutation), bound on `ring-convolution-retained-order`: The permutation of addresses fixed by the layout, which moves the entry for frequency $m$ to address $\sigma(m)$.
- $\nu$ (field dimension), bound on `tensor-product-of-vector-spaces`: The number of vectors in a basis of F, which counts the coordinates of each factor.
- $K$ (number of factors), bound on `tensor-product-of-vector-spaces`: The number of factors in the tensor power F^{\otimes K}, a count of how many vectors each pure tensor has.
- $\lambda$ (scalar), bound on `tensor-product-of-vector-spaces`: A scalar of the field over which F is a vector space.
- $m$ (label space dimension), bound on `subset-intersection-construction`: The dimension of $\mathcal F$, which counts the coordinates of a label space.
- $s$ (smaller-call count), bound on `subset-intersection-construction`: The number of smaller calls, the total rank over all edges.

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

## Page to audit (`recursive-power-saving`)

````markdown
# Recursive power saving from s<Wm

Recursive power saving is the argument that a recursion's cost per stored bit can grow as a fixed power of its parameter, with exponent $\lambda<1$, which the main theorem needs.

Let $f$ be the parameter of a call: the number of field digits for an address interchange (exchanging two disjoint address fields of $u$ bits), or the number of selected axes for a numerical layer (a butterfly layer on chosen axes of a polynomial-valued array). Here $m$ is the factor by which the parameter grows; this letter changes meaning from the subspace dimension of the prerequisite. A recursive call at parameter $mf$ makes $s$ subcalls at parameter $f$, each on a stream of volume $V/W$. The recursion is built on the [Three-element subset intersection construction](subset-intersection-construction.md), which gives $s<Wm$ smaller calls.

Let $\Phi(f)$ be the cost of a call divided by the volume $V$ it works on. The subcalls contribute $\frac{s}{W}\Phi(f)$. Let $C$ be a constant such that the call's own outside work is at most $C(mf)^\lambda$, so

$$\Phi(mf)\le\frac{s}{W}\Phi(f)+C(mf)^\lambda.$$

The outside work is a fixed number of address-field row additions. An address interchange of $u$-bit fields costs $O(Vu^\tau)$, where $\tau<1$ is fixed. (cited) Here $K$ is the bit count of one axis chunk, $d$ is the paper's axis-count parameter (this letter changes meaning from the DFT page), and $\eta>0$ is fixed, with $K\le d^\eta$. A row addition on fields of $u=fK$ bits costs $O(V(u^\tau+1))$. Since $\beta=\tfrac12$ and $f\ge d^\beta$ at an internal node, $d\le f^{1/\beta}$, so the outside work divided by $V$ is $O((fK)^\tau+1)\le O(f^{\tau(1+\eta/\beta)}+1)$, which is $O(f^\lambda)$ when $\lambda>\tau(1+\eta/\beta)$.

Let $\nu$ count the levels of unrolling, which stop once $f/m^\nu<d^\beta$. Each leaf is handled by one kernel per chunk, at cost $O(f/m^\nu)$. After $\nu$ levels the weight is $(s/W)^\nu$, so the internal costs sum to

$$C f^\lambda\sum_{\nu\ge0}\Big(\frac{s/W}{m^\lambda}\Big)^\nu.$$

The saving exists because $s/W<m$. (cited) Taking $\lambda$ with $\log_m(s/W)<\lambda<1$ makes the ratio below 1, so the internal sum is at most a constant times $f^\lambda$.

The leaves at depth $\nu$ have $u=f/m^\nu<d^\beta$ chunks and total weight $(s/W)^\nu$, so they cost $O((s/W)^\nu u)$. Choose $\sigma$ with $\max\{0,\log_m(s/W)\}\le\sigma<\lambda$. Then $(s/W)^\nu\le m^{\nu\sigma}=(f/u)^\sigma$, and the leaves cost $O(f^\sigma d^{\beta(1-\sigma)})\le O(f^\lambda)$.

For example, with $m=2$, $s=3$, $W=2$, we have $s/W=\tfrac32$ and $\log_2(3/2)\approx0.585$. For $\lambda=0.8$ the ratio is $\tfrac{3/2}{2^{0.8}}\approx0.86$.
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

Write the answer to `exegenius/tasks/0148-audit-recursive-power-saving.answer.json`, then run `exegenius submit 0148-audit-recursive-power-saving` in the project directory. If submit rejects the answer, fix the answer and submit again.
