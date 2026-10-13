# exegenius task 0093-audit-fast-butterfly-layers

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
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
- Fast interchange of address fields (also: address interchange and numerical layer, interchange)
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

- $a$ (input list a), bound on `convolution`: The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $p$ (working precision), bound on `fixed-point-precision`: The number of fractional bits in each numerator, $p=6b$ in the source.
- $T$ (padded length), bound on `fixed-point-precision`: A power of two giving the padded length of the box of digit positions, with $4n/b\le T<8n/b$.
- $u$ (scaled digit list u), bound on `fixed-point-precision`: The digit list of the first input, each entry divided by $2^{b+2}$.
- $v$ (scaled digit list v), bound on `fixed-point-precision`: The digit list of the second input, each entry divided by $2^{b+2}$.
- $m$ (cell position), bound on `address-fields`: The position of an item in the array, which is also its address written in binary.
- $u$ (field width), bound on `address-fields`: The number of bits in one address field.
- $V$ (stored bit volume), bound on `address-fields`: The number of bits the array holds in total.
- $m$ (frequency index), bound on `dft-fft`: The frequency index of an entry of a transform, $0\le m<n$; it is also the exponent in $\omega^m$.
- $u$ (butterfly input), bound on `dft-fft`: The first input of a butterfly.
- $v$ (butterfly input), bound on `dft-fft`: The second input of a butterfly.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that a butterfly applies to its second input.
- $O$ (odd-index transform), bound on `dft-fft`: The transform, with root $\omega^2$, of the odd-indexed entries of $a$.
- $C$ (transform of c), bound on `dft-fft`: The transform of the cyclic convolution $c$.
- $d$ (index difference), bound on `dft-fft`: An integer, the difference of two output indices in the inverse sum.
- $g$ (output index), bound on `synthetic-transforms`: A position in the transformed list, running from 0 to t-1.
- $s$ (input index), bound on `synthetic-transforms`: A position in the input list, running from 0 to t-1.
- $m$ (primitivity exponent), bound on `synthetic-transforms`: An exponent used to test that the root has order exactly t.
- $W$ (role count), bound on `linear-network-roles`: The number of roles of the network, the fixed places a wire can occupy.
- $V$ (stored bit volume), bound on `linear-network-roles`: The number of bits stored in the padded array.
- $v$ (node), bound on `linear-network-roles`: A source, gate or sink of the network.
- $u$ (edge tail node), bound on `linear-network-roles`: The node at the start of an edge, a node rather than the address field width.
- $g$ (logical array), bound on `linear-network-roles`: The array the network computes on before the frame is applied.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $m$ (field count), bound on `address-shear-factorization`: The number of fields in each of the vectors $H$ and $D$.
- $H$ (first field vector), bound on `address-shear-factorization`: A vector of $m$ address fields, $H_1,\ldots,H_m$.
- $D$ (second field vector), bound on `address-shear-factorization`: A vector of $m$ address fields, $D_1,\ldots,D_m$.
- $s$ (row index), bound on `address-shear-factorization`: The row index of an entry of $\Pi$.
- $g$ (column index), bound on `address-shear-factorization`: The column index of an entry of $\Pi$.
- $m$ (label dimension), bound on `subset-intersection-construction`: The dimension of the label space $\mathcal F$, which is $h^3$.
- $s$ (smaller call count), bound on `subset-intersection-construction`: The number of smaller calls, the sum over all edges of the rank of the difference of the matrices at its two ends.
- $f$ (call parameter), bound on `recursive-power-saving`: The parameter of a call, counting field digits for address interchange or selected axes for a numerical layer.
- $m$ (parameter factor), bound on `recursive-power-saving`: The factor by which a call's parameter is multiplied in the recursive call.
- $T$ (normalized cost), bound on `recursive-power-saving`: The cost of a call at parameter f divided by the volume it works on.
- $C$ (overhead constant), bound on `recursive-power-saving`: The constant bounding the normalized outside work at a node.
- $\lambda$ (outside-work exponent), bound on `recursive-power-saving`: The exponent, below 1, bounding the normalized outside work at a node of parameter mf.

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

## Page to audit (`fast-butterfly-layers`)

````markdown
# Fast simultaneous butterfly layers

Fast simultaneous butterfly layers is a fixed-tape procedure that applies $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit position in several address chunks at once, where $u$ and $v$ are the two records at addresses that differ only in the selected bit and $H_0$ combines them coefficientwise. Applied one at a time, the butterflies would cost one whole-array pass each. The layer performs the butterfly rounds of [Synthetic polynomial transforms](synthetic-transforms.md).

## The layer

Let $D$ be the number of selected address chunks, and let $d$ be an upper bound on $D$, so $D\le d$. Each chunk has $K$ bits, and the selected bit has one common offset. The width of a coefficient is its number of stored bits, $O(p)$ per real or imaginary component. The layer leaves the other address bits unchanged and costs $O(Vd^{\lambda'})$ for a fixed exponent $\lambda'<1$.

## Method

Let $X$ be the bit-flip matrix. Here $i$ is the imaginary unit, so the letter changes meaning here. Let $\Phi=\operatorname{diag}(1,i)$ be the diagonal phase matrix. Let $C=\tfrac12\bigl((1+i)I+(1-i)X\bigr)$ be the two-point kernel. Direct multiplication gives

$$H_0=\tfrac{1-i}{2}\,\Phi C\Phi.$$

So each butterfly is the kernel $C$ between two phases. Multiplying by a power of $i$ only swaps and negates real and imaginary parts, at cost linear in the coefficient width. The tensor product of matrices, written $\otimes$, replaces each entry of the first matrix by that entry times the second matrix, so $C^{\otimes D}$ is a $2^D\times 2^D$ matrix on the $D$ selected bits. Applying the identity to each selected bit gives

$$H_0^{\otimes D}=\left(\tfrac{1-i}{2}\right)^{D}\Phi^{\otimes D}\,C^{\otimes D}\,\Phi^{\otimes D},$$

so the cost lies in computing $C^{\otimes D}$.

The layer computes $C^{\otimes D}$ recursively. A group of $mf$ selected bits is split into $m$ slots of $f$ bits, and the layer moves whole chunks by [Fast interchange of address fields](fast-address-interchange.md) to realize its binary basis changes. A network of these changes turns $C^{\otimes mf}$ into $s$ child calls, each computing $C^{\otimes f}$ on one slot. Splitting the rows among the network's $W$ wires gives each child $1/W$ of the volume. Writing $T(f)$ for normalized cost at parameter $f$, $T(mf)\le (s/W)\,T(f)+O(1)$. The network satisfies $s/W<m^{\sigma}$ for a fixed exponent $\sigma=1-2^{-50}$. (cited). Unrolling over the $\log_m d$ levels, $T(d)$ grows no faster than $d^{\sigma}$. The layer gets its exponent $\lambda'<1$ from [Recursive power saving from s<Wm](recursive-power-saving.md), taking $\lambda'$ above $\sigma+\tfrac12(1-\sigma)$.

## Exactness

A Gaussian dyadic is a complex number whose real and imaginary parts have power-of-two denominators. Each entry of $C$ is $\tfrac{1\pm i}{2}$, so each selected bit adds one binary digit to the denominators. (cited). Because $C$ is unitary, a coefficient can exceed modulus 1 mid-computation, so the procedure carries $O(p)$ extra fractional bits. The final values stay in the unit disk, because one butterfly maps moduli at most 1 to $(|u|+|v|)/2\le 1$.

 (cited) This truncation keeps error within the bound of [Fixed-point precision and exact recovery](fixed-point-precision.md).
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

Write the answer to `exegenius/tasks/0093-audit-fast-butterfly-layers.answer.json`, then run `exegenius submit 0093-audit-fast-butterfly-layers` in the project directory. If submit rejects the answer, fix the answer and submit again.
