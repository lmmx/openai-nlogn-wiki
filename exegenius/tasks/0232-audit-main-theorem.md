# exegenius task 0232-audit-main-theorem

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
- Chinese-remainder map (also: Agarwal–Cooley map, coefficient layout, generator)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Convolution over the polynomial ring
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Prime source lengths (also: pairwise coprime source lengths)
- Transform identity with retained permutations (also: target permutation)
- Carry propagation (also: carry scan)
- Exact coefficient recovery
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
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
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
- Modular inverse (also: invertible modulo q)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation
- Mixed-radix digits (also: mixed-radix digit)
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
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map between vector spaces over $F$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m\times m$ matrix with entries in $F$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network in the paper, at which a frame is placed.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.
- $v$ (vertex), bound on `linear-network-frames`: A source, gate or sink of the network.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $n$ (input length), bound on `limit-inferior`: The number of bits in each input, which is the index of the running-time function.
- $A$ (fixed machine), bound on `limit-inferior`: A fixed multiplication machine whose running time is studied.
- $T_A$ (running time), bound on `limit-inferior`: The worst-case running time of machine $A$ on inputs of $n$ bits, as a function of $n$.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $T_A$ (running time), bound on `fixed-tape-model`: The running time of machine A as a function of the input length n.
- $A$ (multiplication machine), bound on `fixed-tape-model`: A fixed Turing machine that multiplies two integers, whose running time is T_A.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $\mathrm{val}$ (binary value), bound on `exact-integer-multiplication`: The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $\#$ (separator), bound on `exact-integer-multiplication`: A separator symbol that marks where the first input ends and the second begins.
- $\kappa$ (exponent saving), bound on `n-log-n-conjecture`: A specific positive constant; the main theorem's time bound has logarithmic exponent $1-\kappa$.
- $T$ (padded box size), bound on `cost-table`: The power of two that sets the number of cells in the padded box.
- $V$ (logical volume), bound on `cost-table`: The number of logical bits in the padded box, $V = Tp$.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array being shifted.
- $v$ (vertex), bound on `network-gate-terminal`: A gate or terminal of the network, which carries the frame $D_v$.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $W$ (volume divisor), bound on `address-interchange`: The number of equal pieces the volume is cut into at each level.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $T$ (triple), bound on `indicator-vector`: A three-element subset of the ground set $[h]$.
- $v$ (generating vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form the line.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $f$ (selected position count), bound on `union-bound`: The number of selected bit positions $j_0, \dots, j_{f-1}$ in the packed operation.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $a$ (numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $l$ (second denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of the second element $b/2^l$.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $s$ (axis index), bound on `multidimensional-transform`: The index of an axis, running from 1 to D.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient of a record, with $0 \le s < 2r$.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, which is the length of the transform being replaced.
- $T$ (second Gaussian map), bound on `gaussian-resampling`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $m$ (power count), bound on `polynomial-ring-mod-yr-plus-1`: A positive integer, the number of factors of a root of unity whose product is 1.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The fixed monic polynomial with complex coefficients by which the ring is reduced.
- $m$ (modulus degree), bound on `polynomial-ring`: The degree of f, which is also the number of coefficients in the representative of each element of R.
- $m$ (input coordinate count), bound on `linear-contraction`: The number of coordinates of the input vectors of a linear map, a positive integer.
- $m$ (modulus), bound on `congruence-modulo`: A positive integer, the modulus by which congruence is taken.
- $f$ (packed polynomial f), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, one of the two inputs that are packed.
- $g$ (packed polynomial g), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, the second input that is packed.
- $m$ (integer), bound on `centered-residue`: An integer whose residue class modulo M is represented by its centered residue.
- $f$ (first input sequence), bound on `cyclic-convolution`: The first of the two sequences, of length s.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences, of length s.
- $V$ (first input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the first argument of the bilinear map.
- $W$ (second input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the second argument of the bilinear map.
- $v$ (first argument), bound on `bilinear-map`: A vector of V, the first argument of the bilinear map.
- $v$ (basis vector), bound on `subspace-labels`: A vector of the orthonormal basis of the residual, the shift used by the kernel.
- $x$ (address), bound on `subspace-labels`: An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $f$ (function of addresses), bound on `subspace-labels`: A function of addresses; the letter changes meaning here.
- $m$ (address length), bound on `subspace-labels`: The number of address bits, so addresses lie in F_2^m.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $x$ (address), bound on `complex-phase-network`: A binary vector in $\mathbb{F}_2^m$ at which the arrays are evaluated.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $v$ (binary vector), bound on `complex-phase-network`: A binary vector; the vectors of the orthonormal basis $\mathcal{B}$ are such vectors.
- $\nu$ (second value), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair, the second input of the two-point map.
- $W$ (role count), bound on `numerical-layer`: The number of roles in the network, a count of the wire roles among which rows are distributed.
- $W$ (wire count), bound on `rank-saving-recursion`: The number of wires in the network, which is also the number of roles among which the rows are distributed.
- $s$ (smaller-call count), bound on `rank-saving-recursion`: The total number of smaller calls that one call makes.
- $\nu$ (axis index), bound on `padded-transform-box`: The index of an axis, running from 1 to d.
- $A$ (depth bound), bound on `guard-width-bound`: A bound $A(e)$ on the number of operations on any chain for a group of $e$ axes.
- $\nu$ (power exponent), bound on `guard-width-bound`: The least integer $j \ge 1$ with $m^j \ge \beta$, which satisfies $\beta \le m^\nu$.
- $\nu$ (multiple of the modulus), bound on `modular-inverse`: The integer with $\beta\mu - 1 = \nu M$ in a solution of the congruence.
- $m$ (field count), bound on `address-shear`: The number of address fields in each vector, a count.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges that the shear with matrix $M$ needs, equal to the rational rank of $M$.
- $\nu$ (segments per chunk), bound on `packed-bit-addition`: The number of segments into which each chunk is cut.
- $T$ (Gaussian map T), bound on `transform-identity`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the source's resampling identity.
- $\cdot$ (entrywise product), bound on `transform-identity`: The product of two vectors of the same length taken entry by entry.
- $m$ (chirp position), bound on `bluestein-chirp-identity`: The integer position at which a chirp entry is taken, which may be negative or exceed q-1.
- $l$ (second record position), bound on `phase-twist`: The position of the coefficient taken from the second record in a product.
- $\nu$ (integer being written), bound on `mixed-radix-digits`: The integer whose mixed-radix expansion is sought, with 0 at most nu less than Lambda.
- $\nu$ (power exponent), bound on `chinese-remainder-map`: A nonnegative integer exponent of $\Phi(x)$.
- $T$ (padded box size), bound on `prime-source-lengths`: The size of the padded box, the product of the padded axis lengths.
- $\Theta$ (forward transform), bound on `polynomial-ring-convolution`: The forward synthetic transform along the remaining axes.
- $\nu$ (record count), bound on `polynomial-ring-convolution`: The number of record positions in the transformed array, the product of the remaining axis lengths.

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

## Page to audit (`main-theorem`)

````markdown
# Integer multiplication below n log n

This page states the main theorem, the target of the whole argument: one fixed deterministic machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ steps. The theorem disproves [The n log n optimality conjecture](n-log-n-conjecture.md) in this model, and each later step exists to establish its bound.

## The statement

For a binary string $x$, $\mathrm{val}(x)$ denotes its nonnegative integer value, with the leftmost bit most significant. The input is $x\#y$, where $x$ and $y$ are binary strings of length $n$, and the output is the $2n$-bit binary form of $\mathrm{val}(x)\cdot\mathrm{val}(y)$. For example, take $n=4$, $x=1011$ and $y=0110$. Then $\mathrm{val}(x)=11$ and $\mathrm{val}(y)=6$, so the output is $66$ written in eight bits, $01000010$.

. The theorem is stated in the [Fixed-tape machine model](fixed-tape-model.md): the alphabet and the number of tapes do not depend on the input. $T_A(n)$ is the worst-case number of steps of $A$ on inputs of length $n$, and the claim is $T_A(n) = O(n(\lg n)^{1-\kappa})$ for every $n \ge 1$., so it is a bit-complexity bound, not a practical algorithm.

## Why the bound is a real improvement

Schönhage and Strassen. For large $n$ the theorem is faster than [Schoolbook multiplication](schoolbook-multiplication.md), which takes quadratic time in the number of digits. The new bound is smaller than $n\lg n$ by the factor $(\lg n)^{-\kappa}$. This factor tends to zero, but it falls below one half only when $\lg n > 2^{2^{182}}$.

## Where the saving comes from

The theorem gets its power saving from the [Rank-saving recursion](rank-saving-recursion.md): a call splits into smaller calls, each working on a stream holding a fraction of the stored bits. Let $g(f)$ be the cost of a call at parameter $f$ divided by its volume. A call at parameter $mf$ makes $s$ smaller calls at parameter $f$, each on a stream of volume $V/W$, so $g(mf) \approx (s/W)\,g(f)$, ignoring overhead. Since $s < Wm$, the factor $s/W$ is below $m$, the factor by which the parameter grew.

After $\nu$ levels of recursion, where $\nu$ counts the levels, the normalized cost is about $(s/W)^\nu = (m^\nu)^{\log_m(s/W)}$ times the base cost. With the parameter of order $\lg n$, this is a power of $\lg n$ with exponent $\log_m(s/W)$, which is below one. The saving holds at every input length because its ingredients are fixed:

## Why the method is needed

 A scan reads every stored bit once in order, so it costs $\Theta(n)$. A level that costs a full scan contributes $\Theta(n)$, and the total falls below $n\lg n$ only if each level costs less than a scan. Address rearrangements and transform layers must therefore be cheaper than a scan.

## How the argument proceeds

1. The first step reduces multiplication to a [Radix-digit convolution](radix-digit-convolution.md) of short integer coefficients, obtained by splitting each input into radix digits, that is, blocks of consecutive bits.
2. One coordinate is stored as a polynomial modulo $y^r+1$., and.
3. The method lays out the transforms by a [Transform layout](transform-layout.md), so that a butterfly layer can act on every transform round..
4. The machine adds selected bits by [Packed selected-bit addition](packed-bit-addition.md).
5. The method places coefficients on distinct axes by a [Chinese-remainder map](chinese-remainder-map.md) that preserves convolution. The theorem chooses its axis lengths by [Prime source lengths](prime-source-lengths.md): distinct odd primes lying just below powers of two..
6. The method keeps permutations inside the [Transform identity with retained permutations](transform-identity.md), so the source and target coordinate permutations need not be executed as sorts. [Bluestein's chirp identity](bluestein-chirp-identity.md) into normalized cyclic convolution.
7. The method turns the last cyclic coordinate into a polynomial by [Phase twist](phase-twist.md)..
8. The method handles the remaining axes by [Convolution over the polynomial ring](polynomial-ring-convolution.md)..
9. The method recovers the coefficients by rounding through [Exact coefficient recovery](recovery-and-error.md), which shows that the error is below one half..
10. The algorithm ends with [Carry propagation](carry-propagation.md), which turns the recovered coefficients into the exact binary product..

Each stage is charged to the stored volume $V$; for example,
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

Write the answer to `exegenius/tasks/0232-audit-main-theorem.answer.json`, then run `exegenius submit 0232-audit-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
