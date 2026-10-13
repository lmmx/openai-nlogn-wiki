# exegenius task 0138-audit-address-shear-factorization

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
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms (also: fast transform and transform axes)
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network, source and sink nodes of a route)
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
- $a$ (input list a), bound on `convolution`: The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on `convolution`: The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $x$ (first input integer), bound on `radix-digit-reduction`: The first of the two integers being multiplied, written with n bits.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in each radix digit.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix digits of each input, q = ceil(n/b).
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element of the ring, a power of two.
- $s$ (root exponent), bound on `poly-ring-y-r`: The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $u$ (field width), bound on `address-fields`: The number of bits in one address field.
- $V$ (stored bit volume), bound on `address-fields`: The total number of bits the array holds.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $u$ (butterfly input u), bound on `dft-fft`: The first input of a butterfly; this letter does not denote the field width.
- $v$ (butterfly input v), bound on `dft-fft`: The second input of a butterfly.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $E$ (even-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the even-indexed entries of $a$.
- $O$ (odd-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the odd-indexed entries of $a$.
- $h$ (block size), bound on `dft-fft`: The number of entries in a block, a power of two from 2 to $n$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $L$ (transform axis length), bound on `synthetic-transforms`: The number of entries along the transform axis, a power of two dividing $2r$.
- $Z$ (transformed list), bound on `synthetic-transforms`: The list of $L$ ring elements that the transform produces from the input list $z$.
- $p$ (input index), bound on `synthetic-transforms`: The index of an entry of the input list $z$, running from $0$ to $L-1$.
- $g$ (output index), bound on `synthetic-transforms`: The index of an entry of the transformed list $Z$, running from $0$ to $L-1$.
- $W$ (number of roles), bound on `linear-network-roles`: The number of roles, the wires' fixed places in the network, over which rows are distributed.
- $p$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate, counting the arrays it combines.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.

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

## Page to audit (`address-shear-factorization`)

````markdown
# Address shear and lower-triangular factorization

An address shear is a linear update of two vectors of address fields, and a lower-triangular factorization reduces it to interchanges and linear-cost updates. The address shear is the endpoint operator of the bit network, a [Finite linear network with roles and frames](linear-network-roles.md).

Let $m$ be the number of fields in each vector, and let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two vectors of address fields. Here $q$ is a fixed odd prime, the radix of the digits, and $b$ is the number of radix-$q$ digits in each field, so a field holds a residue in $\mathbb Z/q^b\mathbb Z$. Several letters here change meaning from earlier pages.

For a rational $m\times m$ matrix $M$, the shear by $M$ is $(H,D)\mapsto(H+MD,D)$. A rational entry is written $u/v$, where $u$ is its integer numerator and $v$ its integer denominator, and $q$ must not divide $v$. It acts on fields as $u\,v^{-1}$ modulo $q^b$. So $q$ divides no numerator or denominator of the finitely many matrices used. Let $\operatorname{rank}_{\mathbb Q}M$ be the number of linearly independent rows of $M$.

A matrix is lower triangular when all its entries above the diagonal are zero. A partial permutation matrix $\Pi$ is a 0-1 matrix with at most one 1 in each row and column, and it has $\operatorname{rank}_{\mathbb Q}M$ ones. Every rational $M$ factors as $M=E_1\Pi E_2$, where $E_1$ and $E_2$ are invertible lower-triangular rational matrices. Elimination proves this: pivot on the topmost nonzero row's rightmost entry, clear its left and lower entries by lower-triangular operations, and repeat on what remains.

Example: for $m=2$ and $M=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, $\operatorname{rank}_{\mathbb Q}M=1$, and $M=E_1\Pi E_2$ with $E_1=I$, $\Pi=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $E_2=\begin{pmatrix}1&0\\1&1\end{pmatrix}$.

For each 1 in $\Pi$, let $s$ be its row and $g$ its column. To apply the shear, replace $D$ by $E_2D$ and $H$ by $E_1^{-1}H$. For each 1 in $\Pi$, update $H_s\gets H_s+D_g$, using the transformed $D$. Finally replace $H$ by $E_1H$ and $D$ by $E_2^{-1}D$. The result is $H+E_1\Pi E_2D=H+MD$, and $D$ is unchanged.

A lower-triangular transformation costs $O(V)$, where $V$ is the stored bit volume (cited). Update coordinates from last to first, so each becomes a fixed combination of earlier, still unchanged, coordinates. The coefficients come from the finitely many matrices, not from $V$, and the paper's lemma states that such an update of a later field takes linear time in the stored bits. So each pass is linear, and $m$ is fixed.

Each update $H_s\gets H_s+D_g$ takes one interchange of two equal fields and two additions: set $D_g\gets D_g+H_s$, swap the contents of $H_s$ and $D_g$, then set $D_g\gets H_s-D_g$. Let $h$ be the content of $H_s$ and $d$ that of $D_g$. Then the pair $(h,d)$ becomes $(h+d,d)$. So the shear needs $\operatorname{rank}_{\mathbb Q}M$ interchanges plus $O(V)$ further work.

Each edge of the bit network carries such a matrix. The interchange count of the network is $s_{\rm b}$, the sum of their ranks. The network's rank budget, which counts dimension changes along its edges (its motif-residual lemma), gives $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, where $W_{\rm b}$ is the number of wires, $N$ the total source dimension and $L_{\rm b}$ the total dimension lost on decreasing edges. The paper shows $N>2L_{\rm b}$, so $s_{\rm b}<W_{\rm b}m$ (cited). Per wire, the interchanges are fewer than $m$, which the recurrence turns into a saving of a power of the chunk width (the chunk length).
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

Write the answer to `exegenius/tasks/0138-audit-address-shear-factorization.answer.json`, then run `exegenius submit 0138-audit-address-shear-factorization` in the project directory. If submit rejects the answer, fix the answer and submit again.
