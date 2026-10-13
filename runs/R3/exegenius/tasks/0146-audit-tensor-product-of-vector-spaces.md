# exegenius task 0146-audit-tensor-product-of-vector-spaces

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

## Symbols bound on earlier pages

- $s$ (root exponent), bound on `poly-ring-y-r`: The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $h$ (block size), bound on `dft-fft`: The number of entries in a block, a power of two from 2 to $n$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $\nu$ (network node), bound on `linear-network-roles`: A source, gate or sink of the network, which carries one frame.
- $s$ (row of a one), bound on `address-shear-factorization`: The row index of a 1 in Pi.
- $h$ (first field content), bound on `address-shear-factorization`: The content of the field H_s in a pair (h,d).
- $T$ (prime count), bound on `crt-address-map`: The number of distinct primes whose product is N, and so the number of axes.
- $\nu$ (axis index), bound on `crt-address-map`: The index of one prime and of its axis, running from 1 to T.
- $Q$ (replacing power-of-two length), bound on `gaussian-resampling`: The number of entries in the power-of-two list that replaces a list of length p, chosen slightly above p.
- $K$ (backward resampling map), bound on `gaussian-resampling`: The contraction from lists of length Q back to lists of length p, which undoes the resampling.
- $\zeta$ (chirp root of unity), bound on `bluestein-chirp`: A primitive 2n-th root of unity whose square is omega, from which the chirp phases are built.
- $t$ (chirp index), bound on `bluestein-chirp`: The integer at which the chirp z_t is read.
- $h$ (wrap count), bound on `bluestein-chirp`: The number of multiples of n by which k+l exceeds j, either 0 or 1.
- $\zeta$ (twist root), bound on `phase-twist-convolution`: The root of unity $e^{\pi \mathrm i/r}$, whose $r$-th power is $-1$, used to rescale coefficients.
- $h$ (wrap flag), bound on `phase-twist-convolution`: The flag $h\in\{0,1\}$ recording whether the exponent $k+l$ wrapped past $r$.
- $T$ (power-of-two length), bound on `fixed-point-precision`: The power of two in [4n/b, 8n/b), the number of points in the power-of-two grid.
- $\xi$ (scaled digit list x), bound on `fixed-point-precision`: The digit list of x divided by 2^{b+2}, with entries in [0,1/4).
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $h=uv$ in $\mathbb Z[y]$ whose coefficients are recovered from the packed product.
- $t$ (second coefficient position), bound on `signed-packing`: The position of a coefficient $v_t$ of the second input polynomial.
- $\phi$ (first input array), bound on `ring-convolution-retained-order`: The first of the two input arrays of the convolution, indexed by $i$ on each axis.

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

## Page to audit (`tensor-product-of-vector-spaces`)

````markdown
# Tensor product of vector spaces

The tensor product of vector spaces is the construction that combines spaces into one larger space whose vectors are sums of tuples of vectors, one from each factor, so that its dimension is the product of the factors' dimensions. The subset construction uses it to place a label for each triple of subsets in one ambient space, and the dimension of that space is what the later counting bounds.

Let $F$ be a vector space of dimension $\nu$, the number of vectors in a basis of $F$, and let $K\ge1$ be the number of factors. The tensor power $F^{\otimes K}$ is the vector space spanned by the pure tensors $\xi_1\otimes\cdots\otimes\xi_K$, one for each choice of vectors $\xi_1,\dots,\xi_K\in F$. The symbol $\otimes$ is linear in each slot separately:

$$(\xi+\eta)\otimes\zeta=\xi\otimes\zeta+\eta\otimes\zeta,\qquad (\lambda\xi)\otimes\zeta=\lambda(\xi\otimes\zeta),$$

and likewise in every other slot, for scalars $\lambda$. Not every element is a pure tensor. If $\phi_1,\dots,\phi_\nu$ is a basis of $F$, the $\nu^K$ products $\phi_{\mu_1}\otimes\cdots\otimes\phi_{\mu_K}$, one for each tuple $(\mu_1,\dots,\mu_K)$ with $1\le\mu_s\le\nu$, form a basis of $F^{\otimes K}$. Hence $\dim F^{\otimes K}=\nu^K$.

For example, take $\nu=K=2$. Then $F^{\otimes 2}$ has the four basis products $\phi_1\otimes\phi_1$, $\phi_1\otimes\phi_2$, $\phi_2\otimes\phi_1$ and $\phi_2\otimes\phi_2$, so its dimension is 4. The sum $\phi_1\otimes\phi_2+\phi_2\otimes\phi_1$ is not a pure tensor.

In the paper's bit network the field is $F=\mathbb Q^{h}$, where $h$ is the ground-set size (the letter $h$ changes meaning here). The label space is $F^{\otimes 3}$, of dimension $h^3$ (cited), and $h=100$ gives $10^6$.

For each three-element subset $T$ of the ground set, its indicator vector $t_T$ is the vector of $F$ with entry 1 on $T$ and 0 elsewhere. For three such subsets $T_1,T_2,T_3$, the label is the line $\langle t_{T_1}\otimes t_{T_2}\otimes t_{T_3}\rangle$ spanned by one pure tensor, so each label is a single vector in the one space $F^{\otimes 3}$.
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

Write the answer to `exegenius/tasks/0146-audit-tensor-product-of-vector-spaces.answer.json`, then run `exegenius submit 0146-audit-tensor-product-of-vector-spaces` in the project directory. If submit rejects the answer, fix the answer and submit again.
