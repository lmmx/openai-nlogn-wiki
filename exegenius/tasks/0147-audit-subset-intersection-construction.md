# exegenius task 0147-audit-subset-intersection-construction

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

- $A$ (fixed-tape machine), bound on `nlogn-conjecture`: The paper's deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes.
- $s$ (root exponent), bound on `poly-ring-y-r`: The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $V$ (stored bit volume), bound on `address-fields`: The total number of bits the array holds.
- $A$ (transform of a), bound on `dft-fft`: The list of $n$ values $A_m$, the transform of the input list $a$; this letter does not denote the fixed machine.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $h$ (block size), bound on `dft-fft`: The number of entries in a block, a power of two from 2 to $n$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $C$ (transform of c), bound on `dft-fft`: The transform of the convolution list $c$.
- $S$ (padded length), bound on `ss-hh-background`: The number of entries in each zero-padded list, a power of two at least $2q-1$.
- $L$ (transform axis length), bound on `synthetic-transforms`: The number of entries along the transform axis, a power of two dividing $2r$.
- $g$ (output index), bound on `synthetic-transforms`: The index of an entry of the transformed list $Z$, running from $0$ to $L-1$.
- $e$ (power exponent), bound on `synthetic-transforms`: An integer with $0\le e<2r$, the exponent of the power $y^e$ that multiplies a coefficient list.
- $W$ (number of roles), bound on `linear-network-roles`: The number of roles, the wires' fixed places in the network, over which rows are distributed.
- $\alpha$ (edge tail), bound on `linear-network-roles`: The node at which an edge starts.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $\alpha$ (starting scratch value), bound on `scratch-restoration`: The value a scratch wire holds before the procedure runs, which may be any value.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $s$ (row of a one), bound on `address-shear-factorization`: The row index of a 1 in Pi.
- $g$ (column of a one), bound on `address-shear-factorization`: The column index of a 1 in Pi.
- $h$ (first field content), bound on `address-shear-factorization`: The content of the field H_s in a pair (h,d).
- $N$ (source dimension), bound on `address-shear-factorization`: The total source dimension of the bit network.
- $N$ (list length), bound on `crt-address-map`: The number of coefficients in the list, which equals the product of the T distinct primes.
- $T$ (prime count), bound on `crt-address-map`: The number of distinct primes whose product is N, and so the number of axes.
- $e$ (list index), bound on `crt-address-map`: An index of an entry of the list, an integer from 0 to N-1.
- $Q$ (replacing power-of-two length), bound on `gaussian-resampling`: The number of entries in the power-of-two list that replaces a list of length p, chosen slightly above p.
- $\alpha$ (Gaussian width parameter), bound on `gaussian-resampling`: The integer width parameter of the Gaussian weights, satisfying 2 <= alpha < sqrt(p).
- $U$ (forward resampling map), bound on `gaussian-resampling`: The contraction from lists of length p to lists of length Q, equal to half the map S.
- $g$ (scaled input list), bound on `bluestein-chirp`: The list whose k-th entry is a_k times the chirp phase zeta to the power k squared.
- $t$ (chirp index), bound on `bluestein-chirp`: The integer at which the chirp z_t is read.
- $h$ (wrap count), bound on `bluestein-chirp`: The number of multiples of n by which k+l exceeds j, either 0 or 1.
- $h$ (wrap flag), bound on `phase-twist-convolution`: The flag $h\in\{0,1\}$ recording whether the exponent $k+l$ wrapped past $r$.
- $\alpha$ (first entry coefficient), bound on `phase-twist-convolution`: The untwisted coefficient $\alpha_k$ of the first entry at index $k$.
- $T$ (power-of-two length), bound on `fixed-point-precision`: The power of two in [4n/b, 8n/b), the number of points in the power-of-two grid.
- $S$ (cyclic convolution length), bound on `fixed-point-precision`: The length of the cyclic convolution, the number of entries in each transformed list, with T/2 < S < T.
- $L$ (log of T), bound on `fixed-point-precision`: The base-2 logarithm of T, which bounds the number of levels in the error constants.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $h=uv$ in $\mathbb Z[y]$ whose coefficients are recovered from the packed product.
- $t$ (second coefficient position), bound on `signed-packing`: The position of a coefficient $v_t$ of the second input polynomial.
- $e$ (imaginary part e), bound on `signed-packing`: The imaginary component $e\in\mathbb Z[y]$ of the second record $g$.
- $g$ (second record), bound on `signed-packing`: The second polynomial record, multiplied with $f$ in the Gaussian product.
- $F$ (vector space), bound on `tensor-product-of-vector-spaces`: The vector space whose tensor powers are formed, here Q^h in the bit network.
- $t_T$ (triple indicator), bound on `tensor-product-of-vector-spaces`: The vector of F that has entry 1 on the three elements of the triple T and 0 elsewhere.

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

## Page to audit (`subset-intersection-construction`)

````markdown
# Three-element subset intersection construction

The three-element subset intersection construction is a fixed network of gather, scatter and auxiliary wires that makes few enough smaller calls for the recursion to save a power. It is built inside a [Finite linear network with roles and frames](linear-network-roles.md).

Let $[h]=\{1,\dots,h\}$ be the ground set, with $h=100$. For a three-element subset $T$ of $[h]$, called a triple, $t_T$ is its indicator vector, and $\mathcal T$ is the set of all triples. Call two triples $T,S$ *neighbors* when $|T\cap S|=1$. Each triple $T$ carries a value $g_T$.

**Coefficients.** Over $\mathbb F_2$, gather puts the sum of the $g_T$ with $T\ni e$ on a central wire $C_e$ for each element $e$, and scatter adds $\sum_{e\in S}C_e$ to the target $S$. So $g_T$ reaches $S$ with coefficient $|S\cap T|$ mod $2$. A copy of $g_T$ on an auxiliary wire $A_{ST}$ for each neighbor pair, injected back into $S$, adds $1$ exactly when $|S\cap T|=1$. The net coefficient $|S\cap T|+[|S\cap T|=1]$ mod $2$ is $0$ for sizes $0,1,2$ and $1$ for $T=S$, so only $g_S$ remains.

**Labels.** Over $\mathbb Q$, the bilinear form with matrix $I-J/9$, where $J$ is the all-one matrix, gives $\langle t_T,t_S\rangle=|T\cap S|-1$; neighbors are orthogonal. Let $\mathcal F=(\mathbb Q^h)^{\otimes 3}$, a space built from the [tensor product of vector spaces](tensor-product-of-vector-spaces.md) of three copies of $\mathbb Q^h$, of dimension $m=h^3$ (the letter $m$ changes meaning here). A label $U$ is a nondegenerate subspace of $\mathcal F$. For an index $\alpha=(T_1,T_2,T_3)\in\mathcal T^3$, the label $U_\alpha$ is the line spanned by $t_{T_1}\otimes t_{T_2}\otimes t_{T_3}$. Along a side wire, a label containing $t_T$ may grow to $t_S^\perp$, since $t_T\perp t_S$, adding $h-2$ dimensions.

**Counting.** Give each gate or sink with label $U$ the projection $P_U$ onto $U$ along $U^\perp$, and the source of index $\alpha$ the matrix $-P_{U_\alpha}$. If $U\subseteq V$, then $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on $U\oplus V^\perp$, so its rank is $\dim V-\dim U$. Let $s$, the total rank over all edges, change meaning here. Each unit of rank costs one smaller call (cited)

Let $N=\binom h3^3$, the number of indices $\alpha$ (the letter $N$ changes meaning here). Signed label changes telescope along each wire, and gate labels cancel. Sources have dimension $1$, summing to $N$; sinks have dimension $m$, except the $N$ sinks that receive the sources, which have label $U_\alpha^\perp$ and dimension $m-1$. So the signed total is $Wm-2N$.

Let $L$ be the total dimension lost on decreasing edges (the letter $L$ changes meaning here). Each of the $3\binom h3^2$ invocations has $h$ central wires, each losing $h$ on a decreasing edge, so $L=3\binom h3^2h^2$. Absolute values add $2L$. The first edge out of each source has matrix $2P_{U_\alpha}$, rank one, with no label change; these $N$ ranks give
$$s=Wm-2N+2L+N=Wm-N+2L.$$

Now $L/N=3h^2/\binom h3=100/539$ (cited), so $2L<N$ and $s<Wm$. The recursion in [Recursive power saving from s<Wm](recursive-power-saving.md) needs $s/W<m$, which is $s<Wm$; this is the decisive property (cited).
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

Write the answer to `exegenius/tasks/0147-audit-subset-intersection-construction.answer.json`, then run `exegenius submit 0147-audit-subset-intersection-construction` in the project directory. If submit rejects the answer, fix the answer and submit again.
