# exegenius task 0097-audit-phase-twist-convolution

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
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network)
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
- Fast interchange of address fields (also: address interchange and numerical layer, interchange)
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

- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on `convolution`: A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $y$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $y$ (ring variable), bound on `poly-ring-y-r`: The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element, a power of two.
- $j$ (rule index), bound on `poly-ring-y-r`: The index of the coefficient that the wrap rule $y^{r+j}=-y^j$ reduces to, ranging over $0\le j<r$.
- $k$ (shift exponent), bound on `poly-ring-y-r`: The exponent of the power $y^k$ that acts as a signed shift, with $0\le k<r$.
- $v$ (scaled digit list v), bound on `fixed-point-precision`: The digit list of the second input, each entry divided by $2^{b+2}$.
- $m$ (cell position), bound on `address-fields`: The position of an item in the array, which is also its address written in binary.
- $m$ (frequency index), bound on `dft-fft`: The frequency index of an entry of a transform, $0\le m<n$; it is also the exponent in $\omega^m$.
- $v$ (butterfly input), bound on `dft-fft`: The second input of a butterfly.
- $h$ (block length), bound on `dft-fft`: The number of entries in a block at a level.
- $C$ (transform of c), bound on `dft-fft`: The transform of the cyclic convolution $c$.
- $l$ (paired index), bound on `dft-fft`: The index into $b$ paired with $i$ at output $k$, $l=(k-i)\bmod n$.
- $d$ (index difference), bound on `dft-fft`: An integer, the difference of two output indices in the inverse sum.
- $z$ (input list), bound on `synthetic-transforms`: The list of t ring elements being transformed.
- $m$ (primitivity exponent), bound on `synthetic-transforms`: An exponent used to test that the root has order exactly t.
- $v$ (node), bound on `linear-network-roles`: A source, gate or sink of the network.
- $\alpha$ (initial register value), bound on `scratch-restoration`: The initial value of an auxiliary register, which may be any value.
- $m$ (field count), bound on `address-shear-factorization`: The number of fields in each of the vectors $H$ and $D$.
- $h$ (ground set size), bound on `subset-intersection-construction`: The number of elements of the ground set $[h]$, here 100.
- $\alpha$ (data index), bound on `subset-intersection-construction`: An ordered triple $(T_1,T_2,T_3)$ of triples, indexing one data entry of the network.
- $m$ (label dimension), bound on `subset-intersection-construction`: The dimension of the label space $\mathcal F$, which is $h^3$.
- $m$ (parameter factor), bound on `recursive-power-saving`: The factor by which a call's parameter is multiplied in the recursive call.
- $C$ (overhead constant), bound on `recursive-power-saving`: The constant bounding the normalized outside work at a node.
- $v$ (second record), bound on `fast-butterfly-layers`: The other of the two records paired by the butterfly, at an address that differs from the first only in the selected bit.
- $d$ (chunk count bound), bound on `fast-butterfly-layers`: An upper bound on the number of selected chunks $D$.
- $i$ (imaginary unit), bound on `fast-butterfly-layers`: The imaginary unit $\sqrt{-1}$; on this page the letter no longer denotes an index.
- $C$ (two-point kernel), bound on `fast-butterfly-layers`: The $2\times 2$ matrix $\tfrac12((1+i)I+(1-i)X)$ from which each butterfly is built.
- $e$ (scale exponent), bound on `gaussian-resampling`: A fixed integer exponent giving the power-of-two factor $2^{e}$ in the identity.
- $\zeta$ (chirp root of unity), bound on `bluestein-chirp`: A primitive $2n$th root of unity whose square is $\omega$, the base of the chirp phases.
- $z$ (chirp), bound on `bluestein-chirp`: The chirp sequence $\zeta^{-t^2}$, indexed by every integer $t$.
- $j$ (output index), bound on `bluestein-chirp`: The index of an output $A_j$, ranging over the outputs.
- $k$ (input index), bound on `bluestein-chirp`: The index of an input $a_k$, ranging over the inputs.
- $l$ (twisted chirp index), bound on `bluestein-chirp`: The index of a twisted chirp $\zeta^l z_l$ in the cyclic sum.
- $v$ (twisted cyclic sum), bound on `bluestein-chirp`: The cyclic convolution of the twisted lists $\zeta^k g_k$ and $\zeta^l z_l$ at index $j$.

## Pages in the wiki

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Page to audit (`phase-twist-convolution`)

````markdown
# Last-coordinate phase twist

A last-coordinate phase twist is a coefficientwise rescaling that makes the last cyclic axis of a convolution behave like a product of polynomials. The twist is applied after [Bluestein's chirp identity](bluestein-chirp.md) has turned the middle transform into a cyclic convolution, and it lets the remaining axes be convolved over a polynomial ring.

Let $z$ be the variable of the cyclic ring $\mathbb C[z]/(z^r-1)$, whose exponents wrap modulo $r$. Let $\zeta=e^{\pi \mathrm i/r}$, where $\mathrm i$ is the imaginary unit, so $\zeta^r=-1$. Let $y$ be the variable of $\mathbb C[y]/(y^r+1)$, where $y^r=-1$. The twist is the ring map $z\mapsto \zeta y$, well defined since $(\zeta y)^r=1$. The twist turns the last cyclic coordinate into the [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md).

Let $k$ index a last-axis coefficient, $0\le k<r$. On this page $k$ and $l$ index the last axis, replacing their meanings on the Convolution page. Untwisting multiplies coefficient $k$ by $\zeta^{-k}$.

For $k+l=j+hr$ with $0\le j<r$ and $h\in\{0,1\}$, where $j$ is the cyclic index of the product and $h$ records whether the exponent wrapped (here $h$ is not the carry of the radix-digit page), the cyclic product is $z^{k+l}=z^j$. In the ring, $y^{k+l}=(-1)^h y^j$, while the twist contributes $\zeta^{k+l}=(-1)^h\zeta^j$. The signs cancel, so the twisted term is $\zeta^j y^j$, and untwisting it by $\zeta^{-j}$ gives the cyclic term. Untwisting restores the original cyclic wrap (cited).

For example, if $r=2$ then $(\mathrm iy)(\mathrm iy)=-y^2=1$ modulo $y^2+1$, matching $z\cdot z=1$.

For the other axes, index tuples $v$ with one coordinate per remaining cyclic axis, each wrapping modulo its length. Let $R=\mathbb C[y]/(y^r+1)$, so each entry on those axes is an element of $R$. A convolution over $R$ multiplies entries in $R$ and sums over index pairs with cyclic wrap on the remaining axes. The twist leaves those axes unchanged, so they add no sign. Write $\alpha_k$ and $\beta_l$ for the coefficients of two entries, $\sum_k \alpha_k\zeta^k y^k$ and $\sum_l \beta_l\zeta^l y^l$. Their product in $R$ has $y^j$-coefficient $\zeta^j\sum_{k+l\equiv j \ (\mathrm{mod}\ r)}\alpha_k\beta_l$, so untwisting by $\zeta^{-j}$ gives their cyclic product. Hence the product on the remaining axes is a convolution over $R$. The twist converts the cyclic wrap of [Convolution](convolution.md) on the last axis into a negative wrap in $R$.
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

Write the answer to `exegenius/tasks/0097-audit-phase-twist-convolution.answer.json`, then run `exegenius submit 0097-audit-phase-twist-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
