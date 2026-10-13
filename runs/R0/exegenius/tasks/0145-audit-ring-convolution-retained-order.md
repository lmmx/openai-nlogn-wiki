# exegenius task 0145-audit-ring-convolution-retained-order

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
- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on `convolution`: A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $y$ (second input integer), bound on `radix-digit-reduction`: The second of the two integers being multiplied, written with n bits.
- $y$ (ring variable), bound on `poly-ring-y-r`: The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element of the ring, a power of two.
- $j$ (reduction offset), bound on `poly-ring-y-r`: The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $\omega$ (primitive root of unity), bound on `dft-fft`: A primitive $n$-th root of unity, with $\omega^n=1$ and no smaller power equal to 1.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $O$ (odd-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the odd-indexed entries of $a$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $C$ (transform of c), bound on `dft-fft`: The transform of the convolution list $c$.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $D$ (second field vector), bound on `address-shear-factorization`: The vector of m address fields $(D_1,\ldots,D_m)$ that the shear reads.
- $M$ (rational shear matrix), bound on `address-shear-factorization`: A rational m-by-m matrix whose shear is (H,D) mapped to (H+MD,D).
- $j$ (output index), bound on `bluestein-chirp`: The index of an output of the transform, running from 0 to n-1.
- $k$ (input index), bound on `bluestein-chirp`: The index of an input a_k of the transform, running from 0 to n-1.
- $t$ (chirp index), bound on `bluestein-chirp`: The integer at which the chirp z_t is read.
- $k$ (last-axis exponent), bound on `phase-twist-convolution`: An exponent on the last axis, with $0\le k<r$, indexing one coefficient.
- $j$ (cyclic product index), bound on `phase-twist-convolution`: The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
- $\psi$ (scaled digit list y), bound on `fixed-point-precision`: The digit list of y divided by 2^{b+2}, with entries in [0,1/4).
- $k$ (product coefficient index), bound on `signed-packing`: The exponent $k$ of a coefficient $h_k$ of the product polynomial, running over $0,\dots,2r-2$.
- $j$ (coefficient position), bound on `signed-packing`: The position of a coefficient $u_j$ of a packed polynomial, which is also its block exponent.
- $t$ (second coefficient position), bound on `signed-packing`: The position of a coefficient $v_t$ of the second input polynomial.

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

## Page to audit (`ring-convolution-retained-order`)

````markdown
# Convolution with retained transform order and cancelled permutations

Convolution with retained transform order convolves two arrays over $\mathbb C[y]/(y^r+1)$ by transforming each one, multiplying the transforms entry by entry, and transforming back, without sorting the frequency entries in between. It is the convolution that the fast tape layouts of the main result run on the remaining axes. This convolution computes its transforms by [Synthetic polynomial transforms](synthetic-transforms.md), which need only signed shifts, address rearrangements and butterflies.

Let $\phi$ and $\psi$ be the two input arrays. Let $\ast$ denote their cyclic convolution on one axis of length $t$, with products taken in the ring:

$$(\phi\ast\psi)_k=\sum_{i+j\equiv k \pmod t}\phi_i\psi_j.$$

The forward transform $\mathcal D$ sends an array to $(\mathcal D\phi)_m=\sum_i\omega^{mi}\phi_i$, where $\omega$ is the primitive $t$th root of unity of the ring and $m$ is the frequency index. Let $\mathcal D^{+}$ be the opposite transform. Let $M$ be the known scalar fixed by the normalization of the transforms. Let $\odot$ be the entrywise product of ring elements at the same address.

Expanding the sums gives the first identity up to the normalization: $\sum_k\omega^{mk}(\phi\ast\psi)_k=\sum_{i,j}\omega^{m(i+j)}\phi_i\psi_j=(\mathcal D\phi)_m(\mathcal D\psi)_m$, because $\omega^{mk}$ depends only on $k$ mod $t$. With the normalization of the source,

$$\mathcal{D}(\phi\ast\psi)=M\,(\mathcal{D}\phi)\odot(\mathcal{D}\psi), \qquad \mathcal{D}^{+}\mathcal{D}=\tfrac{1}{M}\,I.$$

The second identity is the inverse relation that the normalization fixes, and the source checks it by expanding the finite sums (cited).

Let $\sigma$ be the permutation of addresses that the layout of the forward transforms fixes: the entry for frequency $m$ is stored at address $\sigma(m)$, so the stored arrays are $\sigma\mathcal{D}\phi$ and $\sigma\mathcal{D}\psi$. The source also composes $\sigma$ with a fixed relabelling of frequencies; the argument needs only that both forward transforms use the same $\sigma$. Both forward transforms therefore use $\sigma$, so the two forward transforms keep the same frequency order through the pointwise product (cited). Without this, the entry at frequency $m$ of $\mathcal D\phi$ would meet an entry of $\mathcal D\psi$ at a different frequency, and a sort would be needed to align them.

Since $\sigma$ moves entries by address and each product entry uses only the two entries at its address, the product of the stored arrays equals $\sigma$ applied to the product of the transforms:

$$(\sigma\mathcal{D}\phi)\odot(\sigma\mathcal{D}\psi)=\sigma\big((\mathcal{D}\phi)\odot(\mathcal{D}\psi)\big).$$

The opposite transform takes the stored product and first applies $\sigma^{-1}$, so the $\sigma$ cancels and no sort is run. This is the step the source describes as the (cited):

$$\mathcal{D}^{+}\sigma^{-1}\big((\sigma\mathcal{D}\phi)\odot(\sigma\mathcal{D}\psi)\big)=\mathcal{D}^{+}\big((\mathcal{D}\phi)\odot(\mathcal{D}\psi)\big).$$

By the first identity and the second, the right side is $\frac{1}{M^{2}}\,(\phi\ast\psi)$, a known scalar multiple of the convolution. For example, if $\sigma$ swaps two records, $\sigma^{-1}$ swaps them back before $\mathcal{D}^{+}$ acts.

This convolution computes its products through [Signed coefficient packing (Kronecker substitution)](signed-packing.md): polynomial products are packed into integers and multiplied by the ordinary $O(n\log n)$ multiplier as a subroutine.

This convolution is applied after [Gaussian resampling](gaussian-resampling.md), which writes each source transform through a power-of-two tensor transform. This convolution is taken over the ring from the [Last-coordinate phase twist](phase-twist-convolution.md), in which the negative wrap gives the original cyclic wrap.
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

Write the answer to `exegenius/tasks/0145-audit-ring-convolution-retained-order.answer.json`, then run `exegenius submit 0145-audit-ring-convolution-retained-order` in the project directory. If submit rejects the answer, fix the answer and submit again.
