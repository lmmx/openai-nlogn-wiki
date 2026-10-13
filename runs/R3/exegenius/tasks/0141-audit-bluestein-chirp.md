# exegenius task 0141-audit-bluestein-chirp

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
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms (also: fast transform and transform axes)
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network, source and sink nodes of a route)
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values (also: scratch (auxiliary) roles)
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

- $n$ (integer length), bound on `nlogn-conjecture`: The number of bits in each of the two integers being multiplied.
- $A$ (fixed-tape machine), bound on `nlogn-conjecture`: The paper's deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes.
- $n$ (list length), bound on `convolution`: The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on `convolution`: The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $j$ (reduction offset), bound on `poly-ring-y-r`: The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $\omega$ (primitive root of unity), bound on `dft-fft`: A primitive $n$-th root of unity, with $\omega^n=1$ and no smaller power equal to 1.
- $A$ (transform of a), bound on `dft-fft`: The list of $n$ values $A_m$, the transform of the input list $a$; this letter does not denote the fixed machine.
- $v$ (butterfly input v), bound on `dft-fft`: The second input of a butterfly.
- $h$ (block size), bound on `dft-fft`: The number of entries in a block, a power of two from 2 to $n$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $l$ (paired index), bound on `dft-fft`: The index into $b$ paired with the index $i$ at output $k$, namely $(k-i)\bmod n$.
- $z$ (input list), bound on `synthetic-transforms`: The list of ring elements that the transform acts on, with entries $z_0,\dots,z_{L-1}$.
- $g$ (output index), bound on `synthetic-transforms`: The index of an entry of the transformed list $Z$, running from $0$ to $L-1$.
- $v$ (denominator), bound on `address-shear-factorization`: The integer denominator of a rational entry u/v, not divisible by q.
- $g$ (column of a one), bound on `address-shear-factorization`: The column index of a 1 in Pi.
- $h$ (first field content), bound on `address-shear-factorization`: The content of the field H_s in a pair (h,d).
- $z_j$ (nearest grid index), bound on `gaussian-resampling`: The integer nearest to Q j/p, the grid point of the power-of-two list paired with entry j.

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

## Page to audit (`bluestein-chirp`)

````markdown
# Bluestein's chirp identity

Bluestein's chirp identity rewrites a [discrete Fourier transform](dft-fft.md) as a cyclic [Convolution](convolution.md), so that later convolution machinery can compute it.

Let $\zeta$ be a primitive $2n$th root of unity with $\zeta^2=\omega$. Here $j$ indexes outputs and $k$ indexes inputs, both in $\{0,\dots,n-1\}$. The transform of $a_0,\dots,a_{n-1}$ is
$$A_j=\sum_{k=0}^{n-1}a_k\,\omega^{jk}.$$

Since $2jk=j^2+k^2-(j-k)^2$, the power splits:
$$\omega^{jk}=\zeta^{j^2}\,\zeta^{k^2}\,\zeta^{-(j-k)^2}.$$
Define $g_k=a_k\zeta^{k^2}$ and $z_t=\zeta^{-t^2}$, the chirp at integer index $t$. Then
$$A_j=\zeta^{j^2}\sum_{k=0}^{n-1}g_k\,z_{j-k}.$$

Reading $z$ at $j-k$ modulo $n$ makes the sum cyclic, but the wrap carries a sign. Since $\zeta^n$ squares to $\omega^n=1$ and is not $1$, $\zeta^n=-1$. Expanding $(t+n)^2=t^2+2tn+n^2$ gives $z_{t+n}=(-1)^n z_t$, using $\omega^{tn}=1$. For odd $n$, $z_{t+n}=-z_t$, and the phase twist below turns this wrap into the original cyclic wrap (cited).

Multiply each $g_k$ by $\zeta^k$ and each $z_l$ by $\zeta^l$, for $k,l\in\{0,\dots,n-1\}$. Let $v_j$ be the cyclic convolution of these twisted lists at output $j$, for $j\in\{0,\dots,n-1\}$:
$$v_j=\sum_{k+l\equiv j \pmod n}\left(\zeta^k g_k\right)\left(\zeta^l z_l\right).$$

Since $k$, $l$ and $j$ lie in $\{0,\dots,n-1\}$, $k+l-j$ lies between $-(n-1)$ and $2n-2$, whose only multiples of $n$ are $0$ and $n$, so $k+l=j+hn$ with $h\in\{0,1\}$. Then $\zeta^{k+l}=\zeta^j(-1)^h$. If $h=1$, then $l=(j-k)+n$ and $z_l=-z_{j-k}$, so $(-1)^h z_l=z_{j-k}$. If $h=0$, then $l=j-k$. Either way it contributes $\zeta^j g_k z_{j-k}$. Each $k$ gives one pair, so $v_j=\zeta^j\sum_k g_k z_{j-k}$ and $A_j=\zeta^{j^2-j}v_j$.

So the identity computes its transform by a cyclic [Convolution](convolution.md), with the phase $\zeta^{j^2-j}$ applied to each output.

For $n=2$, take $\zeta=i$, so $\omega=-1$. Then $A_1=i\,(-i\,a_0+i\,a_1)=a_0-a_1$. For even $n$, $z_{t+n}=z_t$ and no twist is needed.
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

Write the answer to `exegenius/tasks/0141-audit-bluestein-chirp.answer.json`, then run `exegenius submit 0141-audit-bluestein-chirp` in the project directory. If submit rejects the answer, fix the answer and submit again.
