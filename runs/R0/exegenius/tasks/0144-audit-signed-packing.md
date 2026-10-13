# exegenius task 0144-audit-signed-packing

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

- $n$ (integer length), bound on `nlogn-conjecture`: The number of bits in each of the two integers being multiplied.
- $n$ (list length), bound on `convolution`: The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on `convolution`: The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on `convolution`: The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on `convolution`: The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on `convolution`: A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $y$ (second input integer), bound on `radix-digit-reduction`: The second of the two integers being multiplied, written with n bits.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in each radix digit.
- $h_k$ (carry), bound on `radix-digit-reduction`: The carry into radix position k during carry propagation.
- $y$ (ring variable), bound on `poly-ring-y-r`: The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element of the ring, a power of two.
- $j$ (reduction offset), bound on `poly-ring-y-r`: The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $u$ (field width), bound on `address-fields`: The number of bits in one address field.
- $u$ (butterfly input u), bound on `dft-fft`: The first input of a butterfly; this letter does not denote the field width.
- $v$ (butterfly input v), bound on `dft-fft`: The second input of a butterfly.
- $O$ (odd-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the odd-indexed entries of $a$.
- $h$ (block size), bound on `dft-fft`: The number of entries in a block, a power of two from 2 to $n$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $B$ (transform of b), bound on `dft-fft`: The transform of the input list $b$.
- $Z$ (transformed list), bound on `synthetic-transforms`: The list of $L$ ring elements that the transform produces from the input list $z$.
- $p$ (input index), bound on `synthetic-transforms`: The index of an entry of the input list $z$, running from $0$ to $L-1$.
- $g$ (output index), bound on `synthetic-transforms`: The index of an entry of the transformed list $Z$, running from $0$ to $L-1$.
- $e$ (power exponent), bound on `synthetic-transforms`: An integer with $0\le e<2r$, the exponent of the power $y^e$ that multiplies a coefficient list.
- $f$ (logical array), bound on `linear-network-roles`: The logical array that a node stores in the form D_nu f.
- $p$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate, counting the arrays it combines.
- $\gamma$ (written value), bound on `scratch-restoration`: The value added to a scratch wire, computed from data and not from the wire's starting value.
- $b$ (digit count per field), bound on `address-shear-factorization`: The number of radix-q digits in each field.
- $u$ (numerator), bound on `address-shear-factorization`: The integer numerator of a rational entry u/v.
- $v$ (denominator), bound on `address-shear-factorization`: The integer denominator of a rational entry u/v, not divisible by q.
- $g$ (column of a one), bound on `address-shear-factorization`: The column index of a 1 in Pi.
- $h$ (first field content), bound on `address-shear-factorization`: The content of the field H_s in a pair (h,d).
- $d$ (second field content), bound on `address-shear-factorization`: The content of the field D_g in a pair (h,d).
- $T$ (prime count), bound on `crt-address-map`: The number of distinct primes whose product is N, and so the number of axes.
- $e$ (list index), bound on `crt-address-map`: An index of an entry of the list, an integer from 0 to N-1.
- $p$ (prime axis length), bound on `gaussian-resampling`: The number of entries in a list on a prime axis.
- $g$ (scaled input list), bound on `bluestein-chirp`: The list whose k-th entry is a_k times the chirp phase zeta to the power k squared.
- $v$ (twisted convolution), bound on `bluestein-chirp`: The cyclic convolution of the twisted lists, whose entry at output j is v_j.
- $j$ (output index), bound on `bluestein-chirp`: The index of an output of the transform, running from 0 to n-1.
- $k$ (input index), bound on `bluestein-chirp`: The index of an input a_k of the transform, running from 0 to n-1.
- $t$ (chirp index), bound on `bluestein-chirp`: The integer at which the chirp z_t is read.
- $h$ (wrap count), bound on `bluestein-chirp`: The number of multiples of n by which k+l exceeds j, either 0 or 1.
- $k$ (last-axis exponent), bound on `phase-twist-convolution`: An exponent on the last axis, with $0\le k<r$, indexing one coefficient.
- $j$ (cyclic product index), bound on `phase-twist-convolution`: The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
- $h$ (wrap flag), bound on `phase-twist-convolution`: The flag $h\in\{0,1\}$ recording whether the exponent $k+l$ wrapped past $r$.
- $v$ (remaining-axis index), bound on `phase-twist-convolution`: An index tuple with one coordinate per remaining cyclic axis, each wrapping modulo its length.
- $p$ (working precision), bound on `fixed-point-precision`: The number of bits of precision, the power of two 2^p in each numerator's denominator.
- $T$ (power-of-two length), bound on `fixed-point-precision`: The power of two in [4n/b, 8n/b), the number of points in the power-of-two grid.
- $\gamma$ (source scale exponent), bound on `fixed-point-precision`: The exponent of the source scale 2^gamma applied to each computed transform.

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

## Page to audit (`signed-packing`)

````markdown
# Signed coefficient packing (Kronecker substitution)

Signed coefficient packing (Kronecker substitution) encodes a polynomial with integer coefficients of either sign as one integer, so that a polynomial product becomes an integer product, which an ordinary $O(n\log n)$ multiplier computes.

Let $p$ be the working precision of the fixed-point page, so each coefficient of an input polynomial is an integer of absolute value at most $2^p$. Let $B=2^{4p}$ be the block base. Let $u=\sum_{j=0}^{r-1}u_j y^j$ denote a polynomial in $\mathbb Z[y]$ with $|u_j|\le 2^p$; its packed integer is
$$u(B)=\sum_{j=0}^{r-1}u_jB^j.$$
Here $j$ and $t$ are coefficient positions; the sum may be negative.

On tapes, a carry $\gamma_j$ and a block digit $d_j$ satisfy $\gamma_0=0$, $0\le d_j<B$, $d_j\equiv u_j+\gamma_j \pmod B$, and $\gamma_{j+1}=(u_j+\gamma_j-d_j)/B$. Each $\gamma_j$ stays in $\{-1,0\}$, since $u_j+\gamma_j$ lies in $(-B,B)$. Telescoping gives $u(B)=\sum_j d_jB^j+\gamma_rB^r$. So the blocks are nonnegative digits, and the sign is the final carry $\gamma_r$. Each block is $4p$ bits wide (cited).

Evaluation respects products: let $v=\sum_{t=0}^{r-1}v_t y^t$ denote a second input polynomial with $|v_t|\le 2^p$. Then $u(B)\,v(B)=(uv)(B)$ exactly, where $uv$ is the ordinary product in $\mathbb Z[y]$. Signed coefficient packing computes its integer products by the [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md), an ordinary subroutine call that costs $O(n\log n)$.

Recovering the coefficients. Write $h=uv$, and $h_k$ for its coefficient of $y^k$, with $k$ running over $0,\dots,2r-2$. Each $h_k$ sums at most $r$ products $u_jv_t$, so $|h_k|\le r2^{2p}$. Recovery needs $|h_k|<B/2$, which holds because $r<2^p$: the ring degree is at most the padded length, $r\le T$ (cited), and $T<2^p$ for sufficiently large inputs by the choice of $p$ on the fixed-point page. Hence $|h_k|\le r2^{2p}<2^{3p}<B/2$. Since every $h_kB^k$ with $k\ge1$ is a multiple of $B$, $h(B)\equiv h_0 \pmod B$. As $|h_0|<B/2$, $h_0$ is the unique integer in $[-B/2,B/2)$ congruent to $h(B)$ modulo $B$. Subtracting it and dividing by $B$ leaves the same form for $h_1,h_2,\dots$.

Example with $B=12$. For $u=2-y$ and $v=1+3y$, $u(12)=-10$ and $v(12)=37$, so the packed product is $-370$. Recovery gives $h_0=2$, $h_1=5$, $h_2=-3$, so $uv=2+5y-3y^2$.

Gaussian products. A record is a polynomial of degree less than $r$ with complex fixed-point coefficients. A record $f=2^{-p}(a+\sqrt{-1}\,b)$ has real and imaginary components $a,b\in\mathbb Z[y]$. Records have norm at most one, so their parts lie in $[-1,1]$ (cited). Truncation puts each part on the grid $2^{-p}\mathbb Z$, so $2^p$ times each part is an integer, and its coefficients are at most $2^p$ in absolute value (cited). The second record $g=2^{-p}(c+\sqrt{-1}\,e)$ has components $c,e\in\mathbb Z[y]$, and the product is
$$(a+\sqrt{-1}\,b)(c+\sqrt{-1}\,e)=(ac-be)+\sqrt{-1}\,(ae+bc).$$
The four ordinary products $ac$, $be$, $ae$, $bc$ are each one packed product. Each is unpacked to exact coefficients before subtraction or addition, so the bound $|h_k|<B/2$ holds for each product, not for the sums.
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

Write the answer to `exegenius/tasks/0144-audit-signed-packing.answer.json`, then run `exegenius submit 0144-audit-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.
