# exegenius task 0230-audit-polynomial-ring-convolution

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

- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The matrix with ones on the diagonal and zeros elsewhere.
- $B$ (candidate inverse matrix), bound on `linear-algebra-basics`: A matrix that is a two-sided inverse of the matrix $A$ when $A$ is invertible.
- $w$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $w$ (input role), bound on `endpoint-operator`: An input role of the network, whose route starts at its source vertex.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $\delta$ (arithmetic exponent), bound on `cost-table`: A fixed rational exponent in the powers of $p$ that bound the arithmetic costs.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set $[h]$.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $h$ (ground-set size), bound on `indicator-vector`: The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $\lambda$ (scalar multiplier), bound on `line-spanned-by-vector`: A scalar in K, an element of the scalar field, used to scale v.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in each key.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $h$ (chunk index), bound on `destination-rank`: The index of one of the three address chunks, taking values 1, 2 or 3.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $h$ (output position), bound on `multidimensional-transform`: A position in the output array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $R_r$ (record ring), bound on `synthetic-transforms`: The ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$; records are its elements.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $h$ (input list), bound on `synthetic-transforms`: The list of $t$ records $(h_0,\dots,h_{t-1})$ that the transform takes as input.
- $p$ (precision parameter), bound on `gaussian-resampling`: An integer precision parameter of the resampling identity.
- $R$ (polynomial ring), bound on `polynomial-ring`: The quotient ring of complex polynomials in y modulo the multiples of f.
- $w$ (array entry), bound on `array-norm`: A single entry of the array X, which is a complex number.
- $w$ (input vector), bound on `linear-contraction`: A vector in the input space of a linear map, with m complex coordinates.
- $w$ (class member), bound on `congruence-modulo`: An integer in the residue class of d modulo m.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so that $|f_j| \le 2^p$.
- $B$ (block base), bound on `signed-packing`: The base $2^{4p}$ at which the polynomials are evaluated, so that each coefficient occupies a block of $4p$ bits.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $fg$, a polynomial with at most $2r-1$ coefficients $h_j$.
- $w$ (formal variable), bound on `cyclic-convolution`: A formal variable in which a sequence is written as a polynomial, never evaluated.
- $\ast$ (cyclic convolution), bound on `cyclic-convolution`: The cyclic convolution operation, whose result f \ast g is the sequence with entries (f \ast g)_k.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $w$ (second argument), bound on `bilinear-map`: A vector of W, the second argument of the bilinear map.
- $I$ (identity), bound on `subspace-labels`: The identity operator (or matrix).
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set.
- $\beta$ (bank index), bound on `subset-intersection-network`: A triple of triples that indexes one entry of a bank.
- $I$ (identity matrix), bound on `subset-intersection-network`: The h by h identity matrix.
- $I$ (identity matrix), bound on `complex-phase-network`: The identity operator, which leaves every vector or function unchanged.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $\lambda$ (constant lambda), bound on `complex-phase-network`: The constant $(1+i)/2$.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $R$ (orthogonal residual), bound on `complex-phase-network`: The subspace by which an edge's two labels differ, orthogonal to the smaller one.
- $\sigma$ (binary vector), bound on `complex-phase-network`: A binary vector used in the weight identity.
- $\phi$ (function on addresses), bound on `complex-phase-network`: An arbitrary function on binary addresses.
- $\nu$ (second value), bound on `simultaneous-butterfly-layer`: The second of the two values of a pair, the second input of the two-point map.
- $I$ (identity matrix), bound on `simultaneous-butterfly-layer`: The $2\times 2$ identity matrix, with ones on the diagonal and zeros elsewhere.
- $\gamma$ (cost per volume), bound on `rank-saving-recursion`: The cost of a call at parameter $\ell$ divided by its volume.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $\nu$ (axis index), bound on `padded-transform-box`: The index of an axis, running from 1 to d.
- $\sigma$ (digit scale), bound on `normalization-scales`: The power of two 2^{-b-2} by which each radix-2^b digit is multiplied when it is stored.
- $\psi$ (comparison function), bound on `little-o-notation`: A map from the positive reals to the positive reals, positive for all large arguments, against which the function being bounded is compared.
- $\lambda$ (limit variable), bound on `little-o-notation`: The real point at which both functions are evaluated, taken to infinity in the limit.
- $p$ (fractional bit count), bound on `guard-width-bound`: The number of fractional bits each input coefficient carries, so the inputs lie on $2^{-p}\mathbb{Z}[i]$.
- $\beta$ (depth growth bound), bound on `guard-width-bound`: The fixed count $s+\eta$ bounding how much the depth bound grows at each recursive level.
- $\nu$ (power exponent), bound on `guard-width-bound`: The least integer $j \ge 1$ with $m^j \ge \beta$, which satisfies $\beta \le m^\nu$.
- $\beta$ (first integer), bound on `coprime`: One of the two integers whose greatest common divisor is taken, not both zero.
- $\gamma$ (second integer), bound on `coprime`: The second of the two integers whose greatest common divisor is taken, not both zero.
- $\beta$ (integer to invert), bound on `modular-inverse`: The integer whose inverse modulo $M$ is sought.
- $\nu$ (multiple of the modulus), bound on `modular-inverse`: The integer with $\beta\mu - 1 = \nu M$ in a solution of the congruence.
- $h$ (current value of H), bound on `address-shear`: The value of the single field $H$ when $m = 1$.
- $i$ (row index), bound on `address-shear`: The row of a one in $\Pi$, which names an $H$ field.
- $j$ (column index), bound on `address-shear`: The column of a one in $\Pi$, which names a $D$ field.
- $\lambda$ (chunk width), bound on `packed-bit-addition`: The number of address bits in each chunk, equal to the number of segments times the segment width.
- $\nu$ (segments per chunk), bound on `packed-bit-addition`: The number of segments into which each chunk is cut.
- $\sigma$ (segment index), bound on `packed-bit-addition`: The index of a segment within a chunk, running from 0 to nu minus 1.
- $\gamma$ (guard value), bound on `packed-bit-addition`: The integer formed by the non-selected bits of a segment, which lies between 0 and 2 to the power of mu minus 1, minus 1.
- $\beta$ (control bit), bound on `packed-bit-addition`: The bit that decides whether a controlled update is applied.
- $R$ (record length), bound on `packed-bit-addition`: The number of bits in each record, which the cost bounds divide by.
- $w$ (second vector), bound on `transform-identity`: A second complex vector of length q, paired with u in the permutation and product formulas.
- $\cdot$ (entrywise product), bound on `transform-identity`: The product of two vectors of the same length taken entry by entry.
- $R$ (retained source permutation), bound on `transform-identity`: The source permutation that is kept in the formula instead of being executed, and cancels across the convolution.
- $\chi$ (chirp vector), bound on `bluestein-chirp-identity`: The vector of chirp factors, whose entries are unit-modulus phases $\chi_m = e^{\pi i m^2/q}$.
- $w$ (scaled input), bound on `bluestein-chirp-identity`: The input vector u with each entry divided by the corresponding chirp entry.
- $j$ (coefficient position), bound on `phase-twist`: The position of a coefficient in the record, running from 0 to r-1.
- $w$ (indeterminate), bound on `ring-homomorphism`: The variable of the example ring $Q=\mathbb{C}[w]/(w^2-1)$, whose square is $1$.
- $\lambda$ (constant coefficient), bound on `ring-homomorphism`: The complex coefficient of $1$ in an element $\lambda+\mu w$ of $Q$.
- $\psi$ (evaluation at one), bound on `ring-homomorphism`: The ring homomorphism from $Q$ to $\mathbb{C}$ that sends $w$ to $1$, which is not bijective.
- $\beta$ (number of places), bound on `mixed-radix-digits`: The number of places in the system, a positive integer.
- $j$ (place index), bound on `mixed-radix-digits`: An index naming one place of the system, running from 1 to beta; on this page it is not the index of earlier pages.
- $w_j$ (place value), bound on `mixed-radix-digits`: The weight of place j, the product of the lengths of the places below it.
- $\nu$ (integer being written), bound on `mixed-radix-digits`: The integer whose mixed-radix expansion is sought, with 0 at most nu less than Lambda.
- $\nu$ (power exponent), bound on `chinese-remainder-map`: A nonnegative integer exponent of $\Phi(x)$.
- $\beta$ (bit count), bound on `prime-source-lengths`: The number of bits needed to write n, a count.
- $w$ (short axis count), bound on `prime-source-lengths`: The number of axes padded to length u/2, a count.
- $\sigma$ (interval prime), bound on `prime-source-lengths`: A prime lying in the prime interval.
- $h$ (summed position), bound on `carry-propagation`: The position of an already processed coefficient, running over the summation range 0 to j minus 1.

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

## Page to audit (`polynomial-ring-convolution`)

````markdown
# Convolution over the polynomial ring

Convolution over the polynomial ring is computed along the [remaining axes](transform-axis.md) after the earlier reductions. It is the normalized product of two arrays of records: it transforms both arrays, multiplies the transforms entry by entry, and transforms the product back, which reduces the exact product in [Integer multiplication below n log n](main-theorem.md) to integer products.

Convolution over the polynomial ring takes its products in the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md), $R_r$, where $y^r = -1$, so a power $y^j$ with $j \ge r$ wraps around with a sign flip. Let $\phi$ and $\psi$ be the two input records, each a polynomial in $y$ of degree less than $r$ with complex coefficients. Their normalized product is $\phi\psi/r$: the ordinary product, reduced in $R_r$ and divided by $r$.

Convolution over the polynomial ring computes its transforms by [synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$. Let $\Theta$ be the forward transform along the remaining axes, $\Theta^{+}$ its opposite, and $\nu$ the number of record positions in the array, the product of the remaining axis lengths. The one-axis identity gives $\Theta^{+}\Theta = I/\nu$ over all axes.

Write $\ast$ for cyclic convolution over the remaining axes, and $\phi\star\psi=\phi\ast\psi/(r\nu)$ for the normalized convolution. $\Theta(\phi\ast\psi)=\nu\,(\Theta\phi)(\Theta\psi)$, with the product taken in $R_r$. Here $\odot$ is the normalized entrywise product, so $\Theta\phi\odot\Theta\psi$ means $(\Theta\phi)(\Theta\psi)/r$ taken entry by entry. Then $\Theta(\phi\star\psi)=\Theta\phi\odot\Theta\psi$. Applying $\Theta^{+}$ and using $\Theta^{+}\Theta=I/\nu$ gives $\phi\star\psi=\nu\,\Theta^{+}(\Theta\phi\odot\Theta\psi)$. The division by $r$ makes this exact, with no extra factor.

The two forward transforms list their entries in the same frequency order, so equal positions in the two lists hold the same frequency., and; the opposite transform consumes that order. to both operands, so the product is formed on the stored records, in that order.

Convolution over the polynomial ring computes its record products by [signed coefficient packing](signed-packing.md), which turns each polynomial product into an integer product. Let $p$ be the number of fractional bits of each coefficient, so each real and imaginary coefficient part of a record is a multiple of $2^{-p}$. The inputs have: each coefficient lies in the unit disk, so its real and imaginary parts lie in $[-1,1]$, and multiplying by $2^p$ gives integers of absolute value at most $2^p$. Hence $\phi = 2^{-p}(\beta+i\gamma)$ and $\psi = 2^{-p}(\delta+i\lambda)$, where $\beta,\gamma,\delta,\lambda$ are integer polynomials of degree less than $r$ with coefficients of absolute value at most $2^p$.

Let $h=\beta\delta$ be the ordinary integer product, and let $B=2^{4p}$ be the packing base (). Evaluation at $B$ turns the product into one integer product, $\beta(B)\,\delta(B)=h(B)$. Its base-$B$ blocks are the coefficients of $h$ if each coefficient is below $B/2$ in absolute value. Each $h_j$ is a sum of at most $r$ products of two integers bounded by $2^p$, so $|h_j|\le r\,2^{2p}$. Since $r<2^p$ (), $|h_j|<2^{3p}<2^{4p-1}=B/2$. polynomial product satisfies this bound. Convolution over the polynomial ring reads each coefficient as the [centered residue](centered-residue.md) of its block modulo $B$. Convolution over the polynomial ring extracts its blocks by a [carry scan](carry-propagation.md).

Signs are restored after multiplying magnitudes:, the [established O(n log n) multiplier](established-multiplier.md) run as an ordinary subroutine. (evaluation at a large power of two).

Write $\sigma=\beta\delta-\gamma\lambda$ and $\chi=\beta\lambda+\gamma\delta$ for the real and imaginary numerators, which are the real and imaginary parts of $(\beta+i\gamma)(\delta+i\lambda)$. these two sums. Four integer products suffice: $\beta\delta$, $\gamma\lambda$, $\beta\lambda$ and $\gamma\delta$.

The numerators have degree at most $2r-2$ and must be reduced modulo $y^r+1$. Since $y^r=-1$, the coefficient at $j+r$ wraps to position $j$ with a minus sign, so for $0 \le j < r$, treating coefficients of degree above $2r-2$ as zero. Write $\sigma_j$ for the coefficient of $y^j$ in $\sigma$, and $w_j$ for the reduced coefficient of $y^j$. Then $w_j=\sigma_j-\sigma_{j+r}$, with $\sigma_{j+r}=0$ when $j+r>2r-2$.

Worked example, with $r=2$, $\beta=1+2y$, $\delta=3+y$, and the toy base $B=100$ (not a power of two). Then $\beta(100)=201$, $\delta(100)=103$, and $201\cdot103=20703$. Its base-100 blocks, from the least significant end, are $03$, $07$, $02$, so $\beta\delta=3+7y+2y^2$ with every coefficient below $B/2=50$. The reduction gives $w_0=3-2=1$ and $w_1=7$, so $1+7y$, which agrees with $(1+2y)(3+y)$ at $y^2=-1$.
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

Write the answer to `exegenius/tasks/0230-audit-polynomial-ring-convolution.answer.json`, then run `exegenius submit 0230-audit-polynomial-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
