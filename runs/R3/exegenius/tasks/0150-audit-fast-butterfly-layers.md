# exegenius task 0150-audit-fast-butterfly-layers

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
- Three-element subset intersection construction
- Recursive power saving from s<Wm
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values (also: scratch (auxiliary) roles)
- Fast interchange of address fields (also: address interchange and numerical layer, interchange, address interchange)
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
- Tensor product of vector spaces (also: tensor power)

## Symbols bound on earlier pages

- $a$ (input list a), bound on `convolution`: The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $i$ (index i), bound on `convolution`: An index into the entries of the input list $a$.
- $j$ (index j), bound on `convolution`: An index into the entries of the input list $b$.
- $x$ (first input integer), bound on `radix-digit-reduction`: The first of the two integers being multiplied, written with n bits.
- $r$ (ring degree), bound on `poly-ring-y-r`: The number of complex coefficients in each element of the ring, a power of two.
- $j$ (reduction offset), bound on `poly-ring-y-r`: The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
- $s$ (root exponent), bound on `poly-ring-y-r`: The exponent of a power of $y$ used as a root, reduced to $0\le s<2r$.
- $m$ (tape position), bound on `address-fields`: The position of an item in tape order, which is also the item's address written in binary.
- $u$ (field width), bound on `address-fields`: The number of bits in one address field.
- $V$ (stored bit volume), bound on `address-fields`: The total number of bits the array holds.
- $m$ (frequency index), bound on `dft-fft`: The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
- $u$ (butterfly input u), bound on `dft-fft`: The first input of a butterfly; this letter does not denote the field width.
- $v$ (butterfly input v), bound on `dft-fft`: The second input of a butterfly.
- $s$ (butterfly exponent), bound on `dft-fft`: The exponent of the power $\omega^s$ that multiplies the second input of a butterfly.
- $O$ (odd-index transform), bound on `dft-fft`: The transform with root $\omega^2$ of the odd-indexed entries of $a$.
- $t$ (block offset), bound on `dft-fft`: The position of an entry within the first half of a block.
- $C$ (transform of c), bound on `dft-fft`: The transform of the convolution list $c$.
- $p$ (input index), bound on `synthetic-transforms`: The index of an entry of the input list $z$, running from $0$ to $L-1$.
- $g$ (output index), bound on `synthetic-transforms`: The index of an entry of the transformed list $Z$, running from $0$ to $L-1$.
- $W$ (number of roles), bound on `linear-network-roles`: The number of roles, the wires' fixed places in the network, over which rows are distributed.
- $f$ (logical array), bound on `linear-network-roles`: The logical array that a node stores in the form D_nu f.
- $p$ (gate input count), bound on `linear-network-roles`: The number of input arrays of a gate, counting the arrays it combines.
- $I$ (identity operator), bound on `linear-network-roles`: The identity operator, which leaves every array unchanged.
- $m$ (field count), bound on `address-shear-factorization`: The number of address fields in each vector.
- $H$ (first field vector), bound on `address-shear-factorization`: The vector of m address fields $(H_1,\ldots,H_m)$ that the shear updates.
- $D$ (second field vector), bound on `address-shear-factorization`: The vector of m address fields $(D_1,\ldots,D_m)$ that the shear reads.
- $u$ (numerator), bound on `address-shear-factorization`: The integer numerator of a rational entry u/v.
- $v$ (denominator), bound on `address-shear-factorization`: The integer denominator of a rational entry u/v, not divisible by q.
- $s$ (row of a one), bound on `address-shear-factorization`: The row index of a 1 in Pi.
- $g$ (column of a one), bound on `address-shear-factorization`: The column index of a 1 in Pi.
- $d$ (second field content), bound on `address-shear-factorization`: The content of the field D_g in a pair (h,d).
- $T$ (prime count), bound on `crt-address-map`: The number of distinct primes whose product is N, and so the number of axes.
- $p$ (prime axis length), bound on `gaussian-resampling`: The number of entries in a list on a prime axis.
- $K$ (backward resampling map), bound on `gaussian-resampling`: The contraction from lists of length Q back to lists of length p, which undoes the resampling.
- $\Phi$ (compensated map), bound on `gaussian-resampling`: The compensated map from lists of length p to lists of length p, close to the identity and hence invertible.
- $g$ (scaled input list), bound on `bluestein-chirp`: The list whose k-th entry is a_k times the chirp phase zeta to the power k squared.
- $v$ (twisted convolution), bound on `bluestein-chirp`: The cyclic convolution of the twisted lists, whose entry at output j is v_j.
- $j$ (output index), bound on `bluestein-chirp`: The index of an output of the transform, running from 0 to n-1.
- $t$ (chirp index), bound on `bluestein-chirp`: The integer at which the chirp z_t is read.
- $j$ (cyclic product index), bound on `phase-twist-convolution`: The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
- $v$ (remaining-axis index), bound on `phase-twist-convolution`: An index tuple with one coordinate per remaining cyclic axis, each wrapping modulo its length.
- $X$ (integer numerator), bound on `fixed-point-precision`: An integer numerator storing a complex coefficient; it represents the value X/2^p.
- $p$ (working precision), bound on `fixed-point-precision`: The number of bits of precision, the power of two 2^p in each numerator's denominator.
- $T$ (power-of-two length), bound on `fixed-point-precision`: The power of two in [4n/b, 8n/b), the number of points in the power-of-two grid.
- $\Phi$ (forward transform), bound on `fixed-point-precision`: The forward transform of length S, whose entries are the normalized sums (1/S) times the sum of xi_k omega^{mk}.
- $u$ (packed polynomial), bound on `signed-packing`: A polynomial in $\mathbb Z[y]$ with coefficients of absolute value at most $2^p$, whose packed integer is $u(B)$.
- $v$ (second packed polynomial), bound on `signed-packing`: The second input polynomial in $\mathbb Z[y]$, with coefficients $v_t$ of absolute value at most $2^p$.
- $j$ (coefficient position), bound on `signed-packing`: The position of a coefficient $u_j$ of a packed polynomial, which is also its block exponent.
- $t$ (second coefficient position), bound on `signed-packing`: The position of a coefficient $v_t$ of the second input polynomial.
- $d$ (block digit), bound on `signed-packing`: The digit $d_j$ stored in block $j$ of a packed integer, with $0\le d_j<B$.
- $a$ (real part a), bound on `signed-packing`: The real component $a\in\mathbb Z[y]$ of a record, whose coefficients are $2^p$ times the real parts of the record's coefficients.
- $f$ (first record), bound on `signed-packing`: The first polynomial record, a polynomial of degree less than $r$ with complex fixed-point coefficients.
- $g$ (second record), bound on `signed-packing`: The second polynomial record, multiplied with $f$ in the Gaussian product.
- $\sigma$ (layout permutation), bound on `ring-convolution-retained-order`: The permutation of addresses fixed by the layout, which moves the entry for frequency $m$ to address $\sigma(m)$.
- $K$ (number of factors), bound on `tensor-product-of-vector-spaces`: The number of factors in the tensor power F^{\otimes K}, a count of how many vectors each pure tensor has.
- $\lambda$ (scalar), bound on `tensor-product-of-vector-spaces`: A scalar of the field over which F is a vector space.
- $T$ (triple), bound on `subset-intersection-construction`: A three-element subset of $[h]$, one of the elements of $\mathcal T$.
- $m$ (label space dimension), bound on `subset-intersection-construction`: The dimension of $\mathcal F$, which counts the coordinates of a label space.
- $s$ (smaller-call count), bound on `subset-intersection-construction`: The number of smaller calls, the total rank over all edges.
- $f$ (call parameter), bound on `recursive-power-saving`: The parameter of a call, counting field digits for an address interchange or selected axes for a numerical layer.
- $m$ (growth factor), bound on `recursive-power-saving`: The factor by which the parameter grows in one recursive call.
- $\Phi$ (normalized cost), bound on `recursive-power-saving`: The cost of a call at parameter f divided by the volume V it works on.
- $C$ (outside-work constant), bound on `recursive-power-saving`: A constant bounding the outside work at a node of parameter mf.
- $\lambda$ (power exponent), bound on `recursive-power-saving`: The fixed exponent below 1 of the power that bounds the cost per stored bit.
- $\tau$ (interchange exponent), bound on `recursive-power-saving`: The fixed exponent below 1 in the cost O(V u^tau) of an address interchange.
- $K$ (chunk bit count), bound on `recursive-power-saving`: The number of address bits in one axis chunk.
- $d$ (axis-count parameter), bound on `recursive-power-saving`: The paper's parameter giving the number of axes, which sets the chunk width and the threshold d^beta.
- $\sigma$ (leaf exponent), bound on `recursive-power-saving`: A fixed exponent with max{0, log_m(s/W)} at most sigma below lambda, used to bound the leaf costs.
- $\tau$ (cost exponent), bound on `fast-address-interchange`: A fixed exponent below 1 in the interchange cost $O(Vu^\tau)$, chosen so that $s/W<m^\tau$.

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

## Page to audit (`fast-butterfly-layers`)

````markdown
# Fast simultaneous butterfly layers

Fast simultaneous butterfly layers is a fixed-tape procedure that applies $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit position in several address chunks at once. Here $u$ and $v$ are the paired records. The layer performs the butterfly rounds of [Synthetic polynomial transforms](synthetic-transforms.md), which otherwise needs one whole-array pass per butterfly.

## The layer

Let $D$ be the number of selected address chunks, and let $d$ be an upper bound on $D$, so $D\le d$. Each chunk consists of $K$ consecutive address bits, and the selected bit sits at one common offset in every chunk. Each record has complex fixed-point coefficients with $O(p)$ bits per component, where $p$ is the working precision. The layer costs $O(Vd^{\lambda'})$ for a fixed exponent $\lambda'<1$, where $V$ is the stored bit volume.

## Method

Here $i$ is the imaginary unit, so the letter changes meaning here. Let $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ be the bit-flip matrix. Let $\Phi=\operatorname{diag}(1,i)$ be the diagonal phase matrix. Let $C=\tfrac12\bigl((1+i)I+(1-i)X\bigr)$ be the two-point kernel; the letter $C$ changes meaning here. Since $H_0=\tfrac{1-i}{2}\,\Phi C\Phi$ and tensor powers respect products,

$$H_0^{\otimes D}=\left(\tfrac{1-i}{2}\right)^{D}\Phi^{\otimes D}\,C^{\otimes D}\,\Phi^{\otimes D}.$$

Multiplying by $\Phi^{\otimes D}$ only permutes and negates real and imaginary parts, so the work lies in $C^{\otimes D}$.

The layer computes $C^{\otimes D}$ recursively. Group $mf$ selected bits into $m$ slots of $f$ bits. The phase identities for $C$ reduce this group to $s$ child calls, each computing $C^{\otimes f}$ on one slot, with $s<Wm$. The data sits on $W$ roles (wires) of a [Finite linear network with roles and frames](linear-network-roles.md), and splitting the rows evenly gives each child $1/W$ of the volume. The layer moves whole chunks by [Fast interchange of address fields](fast-address-interchange.md) to realize its binary basis changes. With $T(f)$ the normalized cost (time divided by volume), each child costs $(V/W)\,T(f)$, and the node's outside work is $O(VK^{\tau})$ for its chunk exchanges, with $\tau<1$, plus linear copying. Dividing by $V$,

$$T(mf)\le \tfrac{s}{W}\,T(f)+O\bigl((mfK)^{\tau}+1\bigr).$$

The fixed exponent $\sigma=1-2^{-50}$ gives $s/W<m^{\sigma}$, because $s/W$ is $m$ times one minus a tiny fraction. For this network the source computes $\frac{Wm-s}{Wm}=\frac{73}{19906842167500}$, which exceeds $20\cdot2^{-50}$ (cited). Since $m<2^{20}$ gives $\log m<20$,

$$m^{1-2^{-50}}=m\exp(-2^{-50}\log m)>m(1-20\cdot2^{-50})>m\Bigl(1-\tfrac{73}{19906842167500}\Bigr)=\frac{s}{W}.$$

[Recursive power saving from s<Wm](recursive-power-saving.md) turns such a recursion into a power saving. Unroll it over $\lceil\log_m d\rceil$ levels, stopping at groups of fewer than $\sqrt d$ bits, which apply their kernels one at a time. Internal overheads form a geometric series, summing to $O(d^{\lambda})$ with $\lambda<1$. A leaf after $j$ levels has $u=d/m^j<\sqrt d$ chunks, and its share is at most $(s/W)^j u\le (d/u)^{\sigma}u=d^{\sigma}u^{1-\sigma}\le d^{\sigma+\frac12(1-\sigma)}$. The layer gets its exponent $\lambda'<1$ from [Recursive power saving from s<Wm](recursive-power-saving.md), taking $\lambda'$ above $\sigma+\tfrac12(1-\sigma)$.

## Exactness

A Gaussian dyadic is a complex number whose real and imaginary parts have power-of-two denominators. Each entry of $C$ is $\tfrac{1\pm i}{2}$, so each selected bit adds one binary digit to the denominators. (cited).

A unitary matrix preserves the Euclidean length of every pair of values, and here $C=\sqrt2H_0\,\Phi\,\sqrt2H_0$ is a product of unitary matrices, so $C^{\otimes D}$ preserves the norm of each block of $2^D$ entries. If the inputs have modulus at most 1, the block norm is at most $2^{D/2}$, so intermediate moduli are at most $2^{D/2}\le 2^{d/2}$. The final factor $\bigl(\tfrac{1-i}{2}\bigr)^{D}$ has modulus $2^{-D/2}$, so the outputs stay in the unit disk. These fit the $O(p)$ widths (cited).

The layer evaluates exactly and truncates once, toward zero to multiples of $2^{-p}$, with error below $\sqrt2\,2^{-p}$ in maximum norm. This single truncation keeps error within the bound of [Fixed-point precision and exact recovery](fixed-point-precision.md), which needs error below $1/2$.
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

Write the answer to `exegenius/tasks/0150-audit-fast-butterfly-layers.answer.json`, then run `exegenius submit 0150-audit-fast-butterfly-layers` in the project directory. If submit rejects the answer, fix the answer and submit again.
