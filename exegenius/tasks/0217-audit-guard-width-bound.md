# exegenius task 0217-audit-guard-width-bound

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
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Transform layout
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
- Little-o notation
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $D$ (number of axes), bound on `transform-axis`: The number of axes of an array, which is the number of coordinates in each address.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m\times m$ matrix with entries in $F$.
- $B$ (candidate inverse matrix), bound on `linear-algebra-basics`: A matrix that is a two-sided inverse of the matrix $A$ when $A$ is invertible.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network in the paper, at which a frame is placed.
- $v$ (vertex), bound on `linear-network-frames`: A source, gate or sink of the network.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $\varepsilon$ (tolerance), bound on `limit-inferior`: A positive real number used as a threshold for how small a term must be.
- $A$ (fixed machine), bound on `limit-inferior`: A fixed multiplication machine whose running time is studied.
- $A$ (multiplication machine), bound on `fixed-tape-model`: A fixed Turing machine that multiplies two integers, whose running time is T_A.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $d$ (axis count), bound on `cost-table`: The number of axes of the padded box.
- $\ell$ (log axis length), bound on `cost-table`: The base-2 logarithm of $r$.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $v$ (vertex), bound on `network-gate-terminal`: A gate or terminal of the network, which carries the frame $D_v$.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $W$ (volume divisor), bound on `address-interchange`: The number of equal pieces the volume is cut into at each level.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $E$ (vector space), bound on `line-spanned-by-vector`: The vector space over K in which the line lies.
- $v$ (generating vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form the line.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $\mathbb{Z}[i]$ (Gaussian integers), bound on `gaussian-integer`: The set of all Gaussian integers.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index of output coordinates, running from 0 to q-1.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $D$ (axis count), bound on `multidimensional-transform`: The number of transform axes, a positive integer.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $Z$ (output list), bound on `synthetic-transforms`: The list of $t$ records $(Z_0,\dots,Z_{t-1})$ that the transform returns.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $p$ (precision parameter), bound on `gaussian-resampling`: An integer precision parameter of the resampling identity.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $\eta$ (second input value), bound on `butterfly`: The second of the two values that the butterfly takes as input.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between a computed input and the exact input w.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $d$ (integer), bound on `congruence-modulo`: An integer, one of the two integers compared by congruence.
- $e$ (integer), bound on `congruence-modulo`: An integer, the other of the two integers compared by congruence.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so that $|f_j| \le 2^p$.
- $B$ (block base), bound on `signed-packing`: The base $2^{4p}$ at which the polynomials are evaluated, so that each coefficient occupies a block of $4p$ bits.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $d$ (number of cyclic coordinates), bound on `cyclic-coordinate`: The number of cyclic coordinates of an array, a positive integer.
- $\ell$ (coordinate index), bound on `cyclic-coordinate`: The index naming one cyclic coordinate, running from 1 to d.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $W$ (second input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the second argument of the bilinear map.
- $v$ (first argument), bound on `bilinear-map`: A vector of V, the first argument of the bilinear map.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $X$.
- $E$ (fixed bilinear space), bound on `subspace-labels`: The fixed bilinear space in which every label is a subspace.
- $\subseteq$ (inclusion), bound on `subspace-labels`: V is contained in U: every vector of V lies in U.
- $v$ (basis vector), bound on `subspace-labels`: A vector of the orthonormal basis of the residual, the shift used by the kernel.
- $x$ (address), bound on `subspace-labels`: An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $\beta$ (bank index), bound on `subset-intersection-network`: A triple of triples that indexes one entry of a bank.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of target-bank entries on one line, indexed by triples.
- $\ell$ (ground element), bound on `subset-intersection-network`: An element of the ground set, indexing a central wire.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $x$ (address), bound on `complex-phase-network`: A binary vector in $\mathbb{F}_2^m$ at which the arrays are evaluated.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $v$ (binary vector), bound on `complex-phase-network`: A binary vector; the vectors of the orthonormal basis $\mathcal{B}$ are such vectors.
- $\varepsilon$ (edge sign), bound on `complex-phase-network`: The sign in $\{1,-1\}$ that encodes each basis vector's weight and the edge direction.
- $D$ (axis count), bound on `simultaneous-butterfly-layer`: The number of axes on which the layer acts, one axis per chunk; it counts the selected bits.
- $\nu$ (second value), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair, the second input of the two-point map.
- $\ell$ (log record length), bound on `transform-layout`: The base-two logarithm of $r$, which is the number of address bits in a long axis.
- $d$ (axis bound), bound on `numerical-layer`: An upper bound on the number D of selected axes in one layer, a count of axes.
- $W$ (role count), bound on `numerical-layer`: The number of roles in the network, a count of the wire roles among which rows are distributed.
- $W$ (wire count), bound on `rank-saving-recursion`: The number of wires in the network, which is also the number of roles among which the rows are distributed.
- $\ell$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, counting the selected axes of a numerical layer or the digits of an address field.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $\eta$ (twiddle exponent), bound on `transform-round`: The exponent of y at an address, an integer taken modulo 2r.
- $\nu$ (axis index), bound on `padded-transform-box`: The index of an axis, running from 1 to d.
- $d$ (axis count), bound on `padded-transform-box`: The number of axes of the transform, the count of coordinate directions along which the data is laid out.

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

## Page to audit (`guard-width-bound`)

````markdown
# Guard-width bound

The guard-width bound is an explicit number of extra fractional and integer bits that makes every intermediate coefficient of one [simultaneous butterfly layer](simultaneous-butterfly-layer.md) exact, so that a single final truncation suffices. It lets the layer's output enter the exact multiplication algorithm, whose coefficients are recovered by rounding ([exact coefficient recovery](recovery-and-error.md)).

The two-point map sends $u, v$ to $((u+v)/2,\ (u-v)/2)$. The layer applies it on $D$ selected axes, and $d\ge D$ is a positive integer bound on $D$. The guard-width bound applies to output coefficients computed by the [tensor product](tensor-product.md) of the two-point map, so each output is $2^{-D}$ times a signed sum of input coefficients. Its entries are $\pm\tfrac12$, so each entry of the $D$-fold tensor product is $\pm2^{-D}$.

The bound must allow for operators that need not be [contractions](linear-contraction.md), meaning linear maps that can increase the largest modulus of a vector. Rounding after each stage would be unsafe, since errors need not shrink. The layer is evaluated exactly, and only its result is truncated.

Intermediate values are exact [Gaussian dyadics](gaussian-dyadics.md), so the bound reserves bits for them.

Here $p$ is the number of fractional bits each input carries, and $\mathbb{Z}[i]$ is the set of Gaussian integers. Inputs are disk-valued, meaning of modulus at most $1$:

Let $\ell$ be the depth of a value, the number of arithmetic operations on a chain computing it from an input. A value at depth $\ell$ lies in $2^{-(p+\ell)}\mathbb{Z}[i]$ with modulus at most $2^\ell$. We induct on $\ell$. An operand of depth at most $\ell-1$ lies in $2^{-(p+\ell-1)}\mathbb{Z}[i]\subseteq2^{-(p+\ell)}\mathbb{Z}[i]$ with modulus at most $2^{\ell-1}$. A sum or difference has modulus at most $2\cdot2^{\ell-1}=2^\ell$. A halving lies in $2^{-(p+\ell)}\mathbb{Z}[i]$ with modulus at most $2^{\ell-1}$. Sign changes and multiplications by $i$ keep both bounds.

Write $\eta=64(W+m+1)^3$ (the paper's $E$) and $\beta=s+\eta$ (the paper's $B$), where $s$ is the number of smaller calls, and $W$ and $m$ are the wire count and label dimension of the [complex phase network](complex-phase-network.md). For a group of $e$ axes, $A(e)$ bounds the number of operations on any chain, with $A(e)\le sA(e/m)+\eta$ when the group splits into $s$ calls on groups of $e/m$ axes, and $A(e)\le8e$ otherwise. Since $sx+\eta\le\beta x$ for $x\ge1$, each of at most $\lceil\log_m d\rceil$ levels multiplies the bound by $\beta$, so $A(e)\le8d\beta^{\lceil\log_m d\rceil+1}$. Let $\nu$ be the least integer $j\ge1$ with $m^j\ge\beta$. Since $\beta\le m^\nu$, $\beta^{\lceil\log_m d\rceil+1}\le\beta^2d^\nu$, so $A(e)\le8\beta^2d^{\nu+1}$.

Put $C_0=128m\beta^2$ and $C_1=\max\{20,\nu+3\}$. Including its final shift, total depth is at most $128m\beta^2d^{\nu+3}\le C_0d^{C_1}$, since $C_1\ge\nu+3$. Hence $\ell\le C_0d^{C_1}$ for every value.

Let $\Delta=\lceil C_0d^{C_1}\rceil$ be the number of extra fractional bits that the layer reserves. Every intermediate value has $\ell\le\Delta$, so it lies in $2^{-(p+\Delta)}\mathbb{Z}[i]$ with modulus at most $2^\Delta$. A real component then needs $p+\Delta$ fractional bits and $\Delta+2$ integer and sign bits. The layer reserves $\Delta+3$.

Here $\varepsilon$ is the exponent in $d=\Theta(p^{\varepsilon})$, chosen so that $\varepsilon C_1<1$; the letter changes meaning here. Then $\Delta=O(p^{\varepsilon C_1})$. The guard-width bound states growth in the sense of [little-o notation](little-o-notation.md): $\Delta=o(p)$ means $\Delta/p\to0$ as $p$ grows. So each component has width $p+2\Delta+3=O(p)$. Scanning a component's bits takes time linear in its width, so addition, signed shifts, copying and phase changes each take $O(p)$ bit operations per coefficient.

Truncation toward zero onto $2^{-p}\mathbb{Z}[i]$ changes each component by less than $2^{-p}$, because $2^{-p}$.
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

Write the answer to `exegenius/tasks/0217-audit-guard-width-bound.answer.json`, then run `exegenius submit 0217-audit-guard-width-bound` in the project directory. If submit rejects the answer, fix the answer and submit again.
