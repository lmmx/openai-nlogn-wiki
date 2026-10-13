# exegenius task 0140-audit-gaussian-resampling

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

- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $k$ (output index), bound on `convolution`: An index into the entries of the output list $c$.
- $j$ (reduction offset), bound on `poly-ring-y-r`: The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $S$ (padded length), bound on `ss-hh-background`: The number of entries in each zero-padded list, a power of two at least $2q-1$.
- $z$ (input list), bound on `synthetic-transforms`: The list of ring elements that the transform acts on, with entries $z_0,\dots,z_{L-1}$.
- $Z$ (transformed list), bound on `synthetic-transforms`: The list of $L$ ring elements that the transform produces from the input list $z$.
- $p$ (input index), bound on `synthetic-transforms`: The index of an entry of the input list $z$, running from $0$ to $L-1$.
- $e$ (power exponent), bound on `synthetic-transforms`: An integer with $0\le e<2r$, the exponent of the power $y^e$ that multiplies a coefficient list.
- $\nu$ (network node), bound on `linear-network-roles`: A source, gate or sink of the network, which carries one frame.
- $\alpha$ (edge tail), bound on `linear-network-roles`: The node at which an edge starts.
- $\beta$ (edge head), bound on `linear-network-roles`: The node at which an edge ends.
- $f$ (logical array), bound on `linear-network-roles`: The logical array that a node stores in the form D_nu f.
- $p$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate, counting the arrays it combines.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $\alpha$ (starting scratch value), bound on `scratch-restoration`: The value a scratch wire holds before the procedure runs, which may be any value.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $T$ (prime count), bound on `crt-address-map`: The number of distinct primes whose product is N, and so the number of axes.
- $\nu$ (axis index), bound on `crt-address-map`: The index of one prime and of its axis, running from 1 to T.
- $e$ (list index), bound on `crt-address-map`: An index of an entry of the list, an integer from 0 to N-1.

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

## Page to audit (`gaussian-resampling`)

````markdown
# Gaussian resampling

Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution (cited). A standard FFT of length $2m$ splits into two transforms of length $m$. A prime-length transform has no such split.

Let $p$ be the length of a prime axis, the number of entries in a list on that axis, and let $Q$ be a power of two, the number of entries in the list that replaces it, chosen slightly above $p$. Let $F_p$ and $F_Q$ be the normalized discrete Fourier transforms, $(F_p f)_k=\frac1p\sum_{j=0}^{p-1}f_j e^{-2\pi i jk/p}$ and likewise $F_Q$. Let $\pi_p$ and $\pi_Q$ be the coordinate reorderings used in the paper's identity. A contraction is a linear map that does not increase the largest modulus of an entry. Each normalized transform is a contraction (cited).

For an integer $\alpha$ with $2\le\alpha<\sqrt p$, the identity is
$$\pi_pF_p=2^{2\alpha^2}\,K\,\pi_QF_Q\,U,$$
where $U$ maps lists of length $p$ to lists of length $Q$, $K$ maps back, and $\alpha$ is the width parameter of the Gaussian weights below.

Both $U$ and $K$ are built from two Gaussian-weighted sums $\mathsf S$ and $\mathsf T$, each mapping lists of length $p$ to lists of length $Q$:
$$(\mathsf S f)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-pk/Q)^2}f_j,\qquad(\mathsf T f)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(Qj/p-k)^2}f_j,$$
where entries $f_j$ are read modulo $p$, and $j$ and $k$ are entry indices. Each weight is a Gaussian centred on a point of the other grid. Harvey and van der Hoeven prove the Gaussian identity
$$\mathsf T\pi_pF_p=\pi_QF_Q\mathsf S$$
(their Theorem 4.2). It holds because the Fourier transform maps a Gaussian to a Gaussian.

$\mathsf T$ alone is not invertible, so we compensate. Put $\theta=Q/p-1$, which is assumed to satisfy $\theta>p/\alpha^4$. Let $z_j$ be the integer nearest $Qj/p$ and $\beta_j=Qj/p-z_j$. Let $R$ read the entries $z_j$ from a list of length $Q$, let $\Lambda$ multiply entry $j$ by $e^{\pi\alpha^2\beta_j^2}$, and set $\Phi=R\,\mathsf T\,\Lambda$, a map from length $p$ to length $p$. Entry $j$ of $\Phi f$ contains $f_j$ exactly, since $\Lambda$ cancels the Gaussian weight at $z_j$. The paper's Lemma 4.6 gives $\|\Phi-I\|<2^{-\alpha^2\theta}$. Since $\alpha^2\theta>p/\alpha^2>1$, we have $\|\Phi-I\|<1/2$, so $\Phi$ is invertible by the Neumann series $\Phi^{-1}=\sum_{\nu\ge0}(I-\Phi)^\nu$.

Since $R\mathsf T=\Phi\Lambda^{-1}$, the map $\Lambda\Phi^{-1}R$ is a left inverse of $\mathsf T$. Applying it to the Gaussian identity gives $\Lambda\Phi^{-1}R\,\pi_QF_Q\mathsf S=\pi_pF_p$. Set $U=\frac12\mathsf S$ and $K=2^{1-2\alpha^2}\Lambda\Phi^{-1}R$. Then $2^{2\alpha^2}K\pi_QF_QU=\pi_pF_p$, which is the identity.

The paper's Proposition 4.7(i) bounds $\|U\|<3/4$, $\|\tfrac12\Phi^{-1}\|<7/8$ and $\|2^{2-2\alpha^2}\Lambda\|<1$. Since $\|R\|=1$, $U$ and $K$ are contractions. Contractions keep composed approximation errors from growing.

To evaluate $F_p$ on a list $f$, apply $U$, then $\pi_QF_Q$, then $K$, multiply by $2^{2\alpha^2}$, and undo $\pi_p$.

Gaussian resampling acts on the axes placed by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md). Gaussian resampling thus computes its transforms by the butterfly layers of [Discrete Fourier transform and butterflies](dft-fft.md), since a transform of length $Q$ has $\lg Q$ layers, each linear in the array size. The speedups of [Fast simultaneous butterfly layers](fast-butterfly-layers.md) and [Fast interchange of address fields](fast-address-interchange.md) therefore apply to these transforms.
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

Write the answer to `exegenius/tasks/0140-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0140-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
