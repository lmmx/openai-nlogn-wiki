# exegenius task 0143-audit-fixed-point-precision

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
- Last-coordinate phase twist
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
- $n$ (list length), bound on `convolution`: The number of entries in each input and output coefficient list.
- $b$ (input list b), bound on `convolution`: The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on `convolution`: The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on `convolution`: A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $x$ (first input integer), bound on `radix-digit-reduction`: The first of the two integers being multiplied, written with n bits.
- $y$ (second input integer), bound on `radix-digit-reduction`: The second of the two integers being multiplied, written with n bits.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in each radix digit.
- $x_j$ (radix digit of x), bound on `radix-digit-reduction`: The j-th radix digit of x, a value in the range 0 to 2^b minus 1.
- $y_j$ (radix digit of y), bound on `radix-digit-reduction`: The j-th radix digit of y, a value in the range 0 to 2^b minus 1.
- $y$ (ring variable), bound on `poly-ring-y-r`: The polynomial variable whose powers act as roots of unity.
- $j$ (reduction offset), bound on `poly-ring-y-r`: The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $s$ (root exponent), bound on `poly-ring-y-r`: The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $\omega$ (primitive root of unity), bound on `dft-fft`: A primitive $n$-th root of unity, with $\omega^n=1$ and no smaller power equal to 1.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $E$ (even-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the even-indexed entries of $a$.
- $h$ (block size), bound on `dft-fft`: The number of entries in a block, a power of two from 2 to $n$.
- $S$ (padded length), bound on `ss-hh-background`: The number of entries in each zero-padded list, a power of two at least $2q-1$.
- $L$ (transform axis length), bound on `synthetic-transforms`: The number of entries along the transform axis, a power of two dividing $2r$.
- $p$ (input index), bound on `synthetic-transforms`: The index of an entry of the input list $z$, running from $0$ to $L-1$.
- $p$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate, counting the arrays it combines.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $\gamma$ (written value), bound on `scratch-restoration`: The value added to a scratch wire, computed from data and not from the wire's starting value.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $b$ (digit count per field), bound on `address-shear-factorization`: The number of radix-q digits in each field.
- $s$ (row of a one), bound on `address-shear-factorization`: The row index of a 1 in Pi.
- $h$ (first field content), bound on `address-shear-factorization`: The content of the field H_s in a pair (h,d).
- $d$ (second field content), bound on `address-shear-factorization`: The content of the field D_g in a pair (h,d).
- $T$ (prime count), bound on `crt-address-map`: The number of distinct primes whose product is N, and so the number of axes.
- $p$ (prime axis length), bound on `gaussian-resampling`: The number of entries in a list on a prime axis.
- $\Phi$ (compensated map), bound on `gaussian-resampling`: The compensated map from lists of length p to lists of length p, close to the identity and hence invertible.
- $j$ (output index), bound on `bluestein-chirp`: The index of an output of the transform, running from 0 to n-1.
- $k$ (input index), bound on `bluestein-chirp`: The index of an input a_k of the transform, running from 0 to n-1.
- $h$ (wrap count), bound on `bluestein-chirp`: The number of multiples of n by which k+l exceeds j, either 0 or 1.
- $k$ (last-axis exponent), bound on `phase-twist-convolution`: An exponent on the last axis, with $0\le k<r$, indexing one coefficient.
- $j$ (cyclic product index), bound on `phase-twist-convolution`: The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
- $h$ (wrap flag), bound on `phase-twist-convolution`: The flag $h\in\{0,1\}$ recording whether the exponent $k+l$ wrapped past $r$.

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

## Page to audit (`fixed-point-precision`)

````markdown
# Fixed-point precision and exact recovery

Fixed-point precision and exact recovery turns approximate transform output into exact integers, and then into the digits of the product. It recovers the integer coefficients produced by the [Reduction of integer product to digit convolution](radix-digit-reduction.md).

Each complex coefficient is stored as a pair of integer numerators $X$ over $2^p$, where $p$ is the working precision in bits; a numerator $X$ represents $X/2^p$. Scalings by known integers and powers of two are exact on numerators, so the only inexact steps are transforms, pointwise products and truncations. The source sets $p=6b$ (cited), where $b=\lceil\log_2 n\rceil$ (cited), so $n\le 2^b$.

Let $T$ be the power of two in $[4n/b,8n/b)$, and $S$ the cyclic convolution length, with $T/2<S<T$. Since $T<8n/b<2^b$ for $b>8$, we have $S<2^b$. Let $L=\log_2 T$ (this letter changes meaning from the Gaussian resampling page), so $L<b$. The digit lists have degree below $T/2<S$, so cyclic convolution has no wraparound. It computes its transforms by the [forward transform of length $S$](dft-fft.md) and its opposite, which run in finite precision.

Let $\xi_j=x_j/2^{b+2}$ and $\psi_j=y_j/2^{b+2}$; each entry lies in $[0,1/4)$. Let $\Phi$ be the forward transform of length $S$, with $(\Phi\xi)_m=\frac1S\sum_k\xi_k\omega^{mk}$, where $\omega$ is a primitive $S$-th root of unity, and let $\Phi^{+}$ be its opposite, with $\omega^{-mk}$ in its place. Two identities hold: $\Phi(\xi*\psi)=S\,\Phi\xi\cdot\Phi\psi$, since powers of $\omega$ multiply by adding exponents mod $S$; and $\Phi^{+}\Phi=I/S$, since $\sum_m\omega^{m(k-k')}$ is $S$ for $k=k'$ and $0$ otherwise. Hence
$$\Phi^{+}(\Phi\xi\cdot\Phi\psi)=\frac1S\,\Phi^{+}\Phi(\xi*\psi)=\frac{\xi*\psi}{S^2}.$$
The source's transforms also carry a coordinate permutation, which cancels from this product (cited), so the identity holds for the transforms written here.

Each computed transform, after the source scale $2^\gamma$, has error below $E_s2^{-p}$ with $E_s=9\cdot 2^\gamma TL$ (cited); here $\gamma$ is the exponent of that scale (this letter changes meaning from the scratch-restoration page). Each factor of the pointwise product contributes $E_s2^{-p}$ and truncation adds $2\cdot2^{-p}$, and the opposite transform adds $E_s2^{-p}$ more, so the computed $\Phi^{+}$ result is within $(3E_s+2)2^{-p}$ of $(\xi*\psi)/S^2$. Multiplying by $S$ multiplies this error by $S$: it is below $S(3E_s+2)2^{-p}<28\cdot2^\gamma T^2L\cdot2^{-p}$, since $3E_s+2=27\cdot2^\gamma TL+2<28\cdot2^\gamma TL$. The second scaling by $2^{2b+4}S$ and $2^{-p}=2^{-6b}$ give a coefficient error below
$$2^{2b+4}S\cdot 28\cdot2^\gamma T^2L\cdot2^{-6b}<448\,b\,2^{-b+\gamma}\le 448\,b\,2^{-3b/4},$$
using $S<T<2^b$, $L<b$, and $\gamma\le b/4$ for large $b$ (cited). For large $b$ this is below $\tfrac12$ (cited). The coefficient $c_j=2^{2b+4}(\xi*\psi)_j$ is an integer, so rounding each computed value returns $c_j$ exactly.

Carry propagation then gives the digits. Let $h_0=0$ and, for $0\le j<S$,
$$d_j=(c_j+h_j)\bmod 2^b,\qquad h_{j+1}=\left\lfloor\frac{c_j+h_j}{2^b}\right\rfloor.$$
Since $c_j+h_j=d_j+2^bh_{j+1}$, induction gives $\sum_{i<j}c_i2^{bi}=\sum_{i<j}d_i2^{bi}+h_j2^{bj}$. With $j=S$, $xy=\sum_{i<S}c_i2^{bi}<2^{2n}\le 2^{bS}$, because $S>T/2\ge2n/b$. The digit sum also lies below $2^{bS}$, so $h_S=0$, and $d_0,\dots,d_{S-1}$ are the radix-$2^b$ digits of $xy$.

Example, radix $10$ for $2^b$ and $c=(12,15,3)$: $d_0=2$, $h_1=1$; $d_1=6$, $h_2=1$; $d_2=4$, $h_3=0$. The digits $4,6,2$ give $462=12+15\cdot10+3\cdot100$.
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

Write the answer to `exegenius/tasks/0143-audit-fixed-point-precision.answer.json`, then run `exegenius submit 0143-audit-fixed-point-precision` in the project directory. If submit rejects the answer, fix the answer and submit again.
