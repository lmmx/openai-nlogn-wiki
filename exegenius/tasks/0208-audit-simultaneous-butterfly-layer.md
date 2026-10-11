# exegenius task 0208-audit-simultaneous-butterfly-layer

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: a term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set
- Indicator vector
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Opposite transform (also: opposite-sign transform)
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $D$ (number of axes), bound on `transform-axis`: The number of axes of an array, which is the number of coordinates in each address.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $b$ (input bit), bound on `xor`: The second of the two bits that an XOR combines.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The matrix with ones on the diagonal and zeros elsewhere.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $\rho$ (role permutation), bound on `linear-network-frames`: The permutation of roles that the scalar network realises, sending input role $w$ to output role $\rho(w)$.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $\rho$ (role permutation), bound on `endpoint-operator`: The signed permutation of roles realised by the scalar network, sending each input role to an output role.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $K$ (chunk width), bound on `cost-table`: The number of bits in each address chunk.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $K$ (scalar field), bound on `line-spanned-by-vector`: The field of scalars over which the vector space E is taken.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $K$ (segment width), bound on `union-bound`: The number of bits in each segment, so that each guard value takes one of $2^{K-1}$ values.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $a$ (numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $b$ (second numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $D$ (axis count), bound on `multidimensional-transform`: The number of transform axes, a positive integer.
- $X$ (input array), bound on `multidimensional-transform`: The input array, on which the transform acts.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than s.
- $p$ (precision parameter), bound on `gaussian-resampling`: An integer precision parameter of the resampling identity.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $H_0$ (butterfly map), bound on `butterfly`: The two-point map sending a pair of values to their half-sum and half-difference.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $X$ (array of complex values), bound on `array-norm`: A finite array of complex values, the argument of the norm.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $g$ (packed polynomial g), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, the second input that is packed.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so that $|f_j| \le 2^p$.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences, of length s.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $X$ (vector space), bound on `bilinear-form`: The vector space on which the bilinear form is defined.
- $I$ (identity), bound on `subspace-labels`: The identity operator (or matrix).
- $x$ (address), bound on `subspace-labels`: An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $H$ (Hadamard matrix), bound on `subspace-labels`: The normalized 2 by 2 Hadamard matrix.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $X$ (bank X), bound on `subset-intersection-network`: One of the two banks of scalars, indexed by triples of triples.
- $I$ (identity matrix), bound on `subset-intersection-network`: The h by h identity matrix.
- $I$ (identity matrix), bound on `complex-phase-network`: The identity operator, which leaves every vector or function unchanged.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $H$ (normalized Hadamard matrix), bound on `complex-phase-network`: The $2\times 2$ matrix with entries $\pm 1/\sqrt{2}$, a symmetric matrix squaring to $I$.
- $X$ (bit-flip matrix), bound on `complex-phase-network`: The matrix swapping the two coordinates of a vector.
- $\mathrm{diag}$ (diagonal operator), bound on `complex-phase-network`: The operator that multiplies the value at each address by a given factor.
- $\mu$ (constant mu), bound on `complex-phase-network`: The constant $(1-i)/2$.
- $x$ (address), bound on `complex-phase-network`: A binary vector in $\mathbb{F}_2^m$ at which the arrays are evaluated.
- $\rho$ (binary vector), bound on `complex-phase-network`: A second binary vector used in the weight identity.

## Pages in the wiki

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Address field](address-field.md)
- [Exclusive or](xor.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`simultaneous-butterfly-layer`)

````markdown
# Simultaneous butterfly layer

A simultaneous butterfly layer applies the two-point map of a [butterfly](butterfly.md) to several selected address bits at once, and computes the result exactly in a single pass over the stored records. It is the step that lets a transform round apply its butterflies on all participating axes together; the transform layout and packed selected-bit addition pages build on it.

Let $\mu$ and $\nu$ be the two values of a pair. Let $H_0(\mu,\nu) = ((\mu+\nu)/2, (\mu-\nu)/2)$ be the two-point map. As a matrix, $H_0 = \frac{1}{2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.

Let $D$ be the number of axes on which the layer acts. The layer acts on these $D$ [transform axes](transform-axis.md), one per chunk, where a chunk is a run of consecutive address bits. Let $K$ be the number of bits in each chunk. Let $\rho$ be the offset of the selected bit within each chunk, counted from the least significant end, with $0 \le \rho < K$. The sources describe this step as.

The layer applies the length-two case of the [discrete Fourier transform](discrete-fourier-transform.md), $H_0$, to each of the $D$ selected bits independently. This is the [tensor product](tensor-product.md) of $H_0$ over those bits. It acts on each stored coefficient of each record and leaves every other address bit and field unchanged.

Take $D=2$, $K=1$ and $\rho=0$. The two selected bits are then the two bits of a 2-bit address, the first belonging to the first axis. Let the values $1,2,3,4$ sit at addresses $00,01,10,11$. The layer returns $2.5,-0.5,-1,0$ at those addresses. Each output is one quarter of a signed sum of all four inputs; for instance the value at $00$ is $(1+2+3+4)/4 = 2.5$, and the value at $10$ is $(1+2-3-4)/4 = -1$.

Applied one axis at a time, the same numbers come out. Pairing along the first bit, the values at $00$ and $10$ (holding $1$ and $3$) become $2$ and $-1$, and those at $01$ and $11$ (holding $2$ and $4$) become $3$ and $-1$. Pairing along the second bit then replaces the values at $00$ and $01$ by $2.5$ and $-0.5$, and those at $10$ and $11$ by $-1$ and $0$.

The sources give the reason for doing all axes together:. A whole-array pass is one scan that reads and rewrites every stored record. Applying the one-axis factors in turn needs $D$ such scans. The sources instead compute the layer by one tape procedure, a fixed sequence of reads and writes on the machine's tapes, which handles all $D$ axes together.

The procedure rests on three facts. First, the layer expresses its phase frames through the [complex phase network](complex-phase-network.md), as products of two-point kernels $C$ on the selected bits. Here $I$ is the $2\times 2$ identity matrix. Here $H$ is the normalized Hadamard matrix $\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, and $C = H\,\mathrm{diag}(1,i)\,H = \frac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix} = aI+bX$, so $a=(1+i)/2$ and $b=(1-i)/2$. Each of $a$ and $b$ is a Gaussian dyadic, with numerator $1\pm i$ over $2^1$. The layer rests on [Gaussian dyadics](gaussian-dyadics.md) for this reason.

Second, the layer splits bits into smaller groups by [binary changes of basis](binary-change-of-basis.md). Its phase frames express the $C$ tensor product. The layer moves its address chunks by [address-field interchange](address-interchange.md).

Third, the procedure evaluates the whole layer exactly and ends with one final [truncation](truncation.md) of its values. The sources bound the intermediate dyadic values so that this single truncation is enough, and then.
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

Write the answer to `exegenius/tasks/0208-audit-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0208-audit-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
