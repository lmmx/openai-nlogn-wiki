# exegenius task 0090-audit-subset-intersection-construction

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
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network)
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
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

- $L$ (axis length), bound on `poly-ring-y-r`: The number of entries along one of the remaining transform axes, a divisor of $2r$.
- $T$ (padded length), bound on `fixed-point-precision`: A power of two giving the padded length of the box of digit positions, with $4n/b\le T<8n/b$.
- $L$ (log of padded length), bound on `fixed-point-precision`: The base-2 logarithm of $T$.
- $\mathcal F$ (forward transform), bound on `fixed-point-precision`: The forward transform of length $S$ applied to digit lists.
- $m$ (cell position), bound on `address-fields`: The position of an item in the array, which is also its address written in binary.
- $m$ (frequency index), bound on `dft-fft`: The frequency index of an entry of a transform, $0\le m<n$; it is also the exponent in $\omega^m$.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that a butterfly applies to its second input.
- $h$ (block length), bound on `dft-fft`: The number of entries in a block at a level.
- $t$ (block offset), bound on `dft-fft`: The offset of an entry within a block.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transformed list, a power of two dividing 2r.
- $g$ (output index), bound on `synthetic-transforms`: A position in the transformed list, running from 0 to t-1.
- $s$ (input index), bound on `synthetic-transforms`: A position in the input list, running from 0 to t-1.
- $m$ (primitivity exponent), bound on `synthetic-transforms`: An exponent used to test that the root has order exactly t.
- $W$ (role count), bound on `linear-network-roles`: The number of roles of the network, the fixed places a wire can occupy.
- $g$ (logical array), bound on `linear-network-roles`: The array the network computes on before the frame is applied.
- $t$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $\alpha$ (initial register value), bound on `scratch-restoration`: The initial value of an auxiliary register, which may be any value.
- $m$ (field count), bound on `address-shear-factorization`: The number of fields in each of the vectors $H$ and $D$.
- $s$ (row index), bound on `address-shear-factorization`: The row index of an entry of $\Pi$.
- $g$ (column index), bound on `address-shear-factorization`: The column index of an entry of $\Pi$.

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

## Page to audit (`subset-intersection-construction`)

````markdown
# Three-element subset intersection construction

The three-element subset intersection construction is a fixed network of gather, scatter and auxiliary wires that makes few enough smaller calls for the recursion to save a power. It is built inside a [Finite linear network with roles and frames](linear-network-roles.md).

Let $[h]=\{1,\dots,h\}$ be the ground set, with $h=100$, and let $\mathcal T$ be its set of three-element subsets. For $T\in\mathcal T$, let $t_T$ be its indicator vector. Call $T,T'$ *neighbors* when $|T\cap T'|=1$. Each triple $T$ carries a value $g_T$.

**Coefficients.** Gather sums the values $g_T$ of all triples containing an element $e\in[h]$ onto one central wire per element, and scatter adds the central wires of the elements of $T'$ to the target $T'$. An element of $T\cap T'$ is counted once, so $g_T$ reaches $T'$ with coefficient $|T\cap T'|$ modulo $2$. That is $1$ exactly for neighbors. A copy onto a side wire for each neighbor pair, injected back into the target, cancels those terms, leaving $g_{T'}$ alone since $|T'\cap T'|=3$ is odd. Scratch values are removed and restored, so their initial values do not matter.

**Labels.** Over $\mathbb Q$, the bilinear form with matrix $I-J/9$ gives $\langle t_T,t_{T'}\rangle=|T\cap T'|-1$, zero exactly for neighbors, where $J$ is the all-one matrix. Let $\mathcal F=(\mathbb Q^h)^{\otimes 3}$, of dimension $m=h^3$ (the letter $m$ changes meaning here). Each index $\alpha=(T_1,T_2,T_3)$ gets the line $U_\alpha$ spanned by $t_{T_1}\otimes t_{T_2}\otimes t_{T_3}$. Because neighbors are orthogonal, a label containing $t_T$ can grow by the complement of $t_{T'}$ along a side wire.

**Counting.** Give each gate or sink with label $U$ the projection $P_U$ onto $U$ along $U^\perp$, each source of index $\alpha$ the matrix $-P_{U_\alpha}$, and other sources zero. Let $s$, the number of smaller calls, be the sum of the ranks of the edge differences over all edges. Each edge's rank is its absolute label change, and each unit of rank costs one smaller call (cited). Signed changes telescope to $Wm-2N$, where $N$ counts the indices $\alpha$. Decreasing edges lose a total $L$, adding $2L$; the $N$ source edges add $N$. So
$$s=Wm-N+2L,$$
and $L/N=100/539$ (cited) gives $2L<N$, hence $s<Wm$.

The network meets the count needed for the recursion. (cited) The recursion in [Recursive power saving from s<Wm](recursive-power-saving.md) uses this inequality to save a fixed power.
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

Write the answer to `exegenius/tasks/0090-audit-subset-intersection-construction.answer.json`, then run `exegenius submit 0090-audit-subset-intersection-construction` in the project directory. If submit rejects the answer, fix the answer and submit again.
