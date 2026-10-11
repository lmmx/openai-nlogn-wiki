# exegenius task 0436-audit-bluestein-chirp-identity

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
- Exact integer multiplication (also: exact multiplication)
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture, the conjecture)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform, Fourier transform, normalized form, frequency order)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights, Gaussian line map, Gaussian corrections, target)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Gaussian dyadics
- Transform identity with retained permutations (also: target permutation, coordinate permutations)
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Butterfly (also: two-point butterfly map, two-point map, Butterfly operation)
- Congruence (also: congruence modulo B, modulo, modulo arithmetic)
- Centered residue
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Gate and terminal of a network (also: gate applied pointwise, pointwise linear gate, sink)
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set (also: finite set)
- Indicator vector
- Modular inverse (also: invertible modulo q, unit modulo M_i)
- Two-point kernel (also: kernel)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation (also: limit as lambda tends to infinity)
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array, coefficient bound)
- Normalized cyclic convolution
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Tensor product (also: tensor power)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logical array (also: logical array and stored array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Ceiling function
- Bézout's identity (also: Bezout's identity)
- Big-Theta notation
- Bijection
- Permutation
- Bit network (also: the paper's bit network)
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Family parameter
- Frequency domain
- Incidence
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Logical bit volume
- Ring
- Orthogonal complement
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $\lg$ (base-2 logarithm), bound on `base-two-logarithm`: The base-2 logarithm of $n$, the least integer $k$ with $2^k \ge n$, but at least 1.
- $q$ (second prime), bound on `prime-number`: A prime number different from p, used in the coprimality argument.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $\pi$ (permutation), bound on `permutation`: The map from S to S that sends each position to its new position.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $\lg$ (base-2 logarithm), bound on `schoolbook-multiplication`: The base-2 logarithm, applied to the input length n.
- $q$ (level ratio), bound on `mathematical-induction`: The fixed positive real ratio by which one level may multiply a bound.
- $q$ (key), bound on `stable-radix-sort`: The key of a record, a w-bit nonnegative integer written with bits q_{w-1} down to q_0.
- $q$ (address before move), bound on `destination-rank`: The address of a record before the move.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $F$ (field), bound on `linear-algebra-basics`: A set with addition and multiplication in which every nonzero element has a multiplicative inverse, the scalars of the vector space.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $\ell$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $\ell$ (column index), bound on `matrix-rank`: The column of a one in $\Pi$, which is also the index of the field $D_\ell$ it uses.
- $\tau$ (complex number), bound on `phase-factor`: A complex number written as alpha plus beta i.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on, so it counts the entries of a vector.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the output coordinates.
- $F_q$ (discrete Fourier transform), bound on `discrete-fourier-transform`: The map sending a vector of q complex numbers to its normalized discrete Fourier transform, with coordinates given by the weighted sum above.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $\pi$ (circle constant), bound on `multidimensional-transform`: The ratio of a circle's circumference to its diameter.
- $\tau$ (butterfly offset), bound on `synthetic-transforms`: The offset of a butterfly pair within the first half of its block, from $0$ to $\delta-1$.
- $\lg$ (base-2 logarithm), bound on `synthetic-transforms`: The logarithm to base 2.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $\tau$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring whose positive integer power equals 1.
- $\ell$ (halving count), bound on `gaussian-resampling`: The number of halvings of a transform length, so that the length is $2^\ell$.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $\tau$ (common exponent), bound on `gaussian-dyadics`: The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $\chi$ (array), bound on `two-point-kernel`: An array of complex values, with one entry for each address.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $\pi$ (bilinear map), bound on `bilinear-map`: The map sending each pair (e,d) of arguments to a vector pi(e,d) in K, linear in each argument while the other is fixed.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $\tau$ (processed positions), bound on `carry-propagation`: The number of low positions already processed, so that the sums run over $t < \tau$.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $u_j$ (input coefficient), bound on `congruence-modulo`: The input coefficient at position j of the sum being formed.
- $\tau$ (field element), bound on `binary-field`: An arbitrary element of the binary field, so it is $0$ or $1$.
- $\chi$ (source bank), bound on `bit-network`: The source bank, a vector with one bit for each triple.
- $\tau$ (choice of three triples), bound on `line-spanned-by-vector`: A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $\tau$ (centered residue), bound on `centered-residue`: The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\chi$ (number of congruences), bound on `chinese-remainder-theorem`: The number of congruences in the system, a positive integer.
- $\tau$ (solution), bound on `chinese-remainder-theorem`: An unknown integer, which is a solution when it satisfies every congruence of the system.
- $\ast$ (cyclic convolution), bound on `cyclic-convolution`: The operation sending two sequences of length n to their cyclic convolution.
- $\chi_j$ (chirp factor), bound on `cyclic-convolution`: The phase factor e^{pi i j^2/t} of input position j.
- $\tau$ (reflected chirp), bound on `cyclic-convolution`: The function tau(delta) of an integer delta, read as a sequence of length t.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $\tau$ (remainder), bound on `bezout-identity`: The remainder when beta is divided by e, which lies between 0 and e minus 1.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $\tau$ (generator), bound on `cyclic-group`: A fixed element of the group; its powers give every element of the cyclic group $C_\kappa$.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $\tau$ (real number), bound on `extended-reals`: A generic real number, used when the order and arithmetic of the extended reals are stated.
- $\chi$ (sequence term), bound on `limit-inferior`: The $k$-th term of a sequence of real numbers.
- $\lg$ (base-2 logarithm), bound on `fixed-tape-model`: The base-2 logarithm, so that $\lg n$ stands for $\log_2 n$.
- $\tau$ (family parameter), bound on `family-parameter`: The index of a member of the family: a nonnegative integer that selects which construction is built and so fixes its size.
- $\chi$ (modular inverse), bound on `transform-identity`: An integer with $\chi t\equiv 1 \pmod s$, that is, an inverse of $t$ modulo $s$.
- $\chi$ (record width), bound on `logical-bit-volume`: The number of bits in one record of the box.
- $\circledast$ (normalized cyclic convolution), bound on `normalized-cyclic-convolution`: The cyclic convolution of two sequences divided by their common length $s$.
- $\chi$ (chirp phase), bound on `normalized-cyclic-convolution`: The phase $e^{\pi i m^2/q}$ at an integer $m$, which has period $q$ when $q$ is even.

## Pages in the wiki

- [Logarithm](logarithm.md)
- [Base-2 logarithm](base-two-logarithm.md)
- [Integer](integer.md)
- [Ring](ring.md)
- [Root of unity](root-of-unity.md)
- [Stream](stream.md)
- [Prime number](prime-number.md)
- [Pointwise product](pointwise-product.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen multiplication](schonhage-strassen.md)
- [Convolution](convolution.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Bijection](bijection.md)
- [Permutation](permutation.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Mathematical induction](mathematical-induction.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Little-o notation](little-o-notation.md)
- [Coprime](coprime.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Address](address.md)
- [Address field](address-field.md)
- [Cyclic shift](cyclic-shift.md)
- [Array](array.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Logical array](logical-array.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Incidence](incidence.md)
- [Eigenvalue](eigenvalue.md)
- [Indicator vector](indicator-vector.md)
- [Matrix rank](matrix-rank.md)
- [Phase factor](phase-factor.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Gaussian integer](gaussian-integer.md)
- [Two-point kernel](two-point-kernel.md)
- [Tensor product](tensor-product.md)
- [Bilinear map](bilinear-map.md)
- [Ceiling function](ceiling-function.md)
- [Carry propagation](carry-propagation.md)
- [Grid numerator](grid-numerator.md)
- [Congruence](congruence-modulo.md)
- [Binary field](binary-field.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Bit network](bit-network.md)
- [Bilinear form](bilinear-form.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Centered residue](centered-residue.md)
- [Chinese remainder theorem](chinese-remainder-theorem.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bézout's identity](bezout-identity.md)
- [Big-Theta notation](big-theta-notation.md)
- [Cyclic group](cyclic-group.md)
- [Modular inverse](modular-inverse.md)
- [Diagonal scaling](diagonal-scaling.md)
- [Extended real numbers](extended-reals.md)
- [Limit inferior](limit-inferior.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Family parameter](family-parameter.md)
- [Frequency domain](frequency-domain.md)
- [Opposite transform](opposite-transform.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Padded transform box](padded-transform-box.md)
- [Logical bit volume](logical-bit-volume.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Normalization scales](normalization-scales.md)
- [Independence of events](independence.md)
- [Projection along a subspace](projection-along-subspace.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Bit construction](bit-construction.md)
- [Complex phase network](complex-phase-network.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Tape procedure](tape-procedure.md)
- [Exclusive or](xor.md)
- [Bit procedure](bit-procedure.md)
- [Endpoint operator](endpoint-operator.md)
- [Address shear](address-shear.md)
- [Complex construction](complex-construction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Supremum](supremum.md)
- [Linear contraction](linear-contraction.md)
- [Guard-width bound](guard-width-bound.md)
- [Union bound](union-bound.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Telescoping identity](telescoping-identity.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`bluestein-chirp-identity`)

````markdown
# Bluestein's chirp identity

Bluestein's chirp identity rewrites the [Discrete Fourier transform](discrete-fourier-transform.md) $F_q$ as a convolution multiplied by chirp factors. It reduces the transform to a [cyclic convolution](cyclic-convolution.md), so any method that computes that convolution also computes the transform. In the paper, it converts the middle transform into a [normalized cyclic convolution](normalized-cyclic-convolution.md).

The middle transform is the factor QFt in the paper's equation (35). The paper states that QFt is the Fourier transform with its output frequencies relabelled by the paper's target permutation. The paper's statement of the identity is into normalized cyclic convolution. The paper computes convolution in later sections: So a transform rewritten as convolution can be computed by that machinery.

Throughout, $q$ is even, as the identity requires. For sequences of length $q$, $\ast$ and $\circledast$ are cyclic and normalized cyclic convolution, with indices taken modulo $q$. Here $x \bmod q$ denotes the remainder of the integer $x$ on division by $q$, the position in $\{0,\dots,q-1\}$ reached by $x$ on a cycle of $q$ positions.

Here $\tau$ is the integer position of a chirp entry, which may be negative or larger than $q-1$. The chirp is the vector $\chi$ whose entry at each integer $\tau$ is $\chi_\tau = e^{\pi i \tau^2/q}$. So $\chi = (\chi_0,\dots,\chi_{q-1})$, and every entry has modulus $1$, because $\pi\tau^2/q$ is real.

Since $(\tau+q)^2-\tau^2 = q(2\tau+q)$, we get $\chi_{\tau+q}/\chi_\tau = e^{\pi i(2\tau+q)}$. Because $q$ is even, $2\tau+q$ is even, so the ratio is $1$ and $\chi_{\tau+q}=\chi_\tau$. Hence $\chi_\tau$ depends only on $\tau \bmod q$. For odd $q$ the ratio is $-1$, so each wrapped index picks up a sign. The sum below would then be a negacyclic convolution, and the identity would need that sign change.

For integers $j$ and $\ell$, the identity $2j\ell = j^2+\ell^2-(\ell-j)^2$ gives $e^{-2\pi i j\ell/q} = \chi_{\ell-j}/(\chi_j\chi_\ell)$. Here $j$ and $\ell$ are the input and output indices of $F_q$. Write $\hat u = \frac{1}{\chi}\cdot u$, so $\hat u_j = u_j/\chi_j$. Then
$$(F_q u)_\ell = \frac{1}{\chi_\ell}\cdot\frac{1}{q}\sum_{j=0}^{q-1}\hat u_j\,\chi_{\ell-j}.$$
By periodicity $\chi_{\ell-j}=\chi_{(\ell-j)\bmod q}$, so the sum is $(\hat u\ast\chi)_\ell$. Hence
$$F_q u = \frac{1}{\chi}\cdot(\hat u\circledast\chi), \qquad \hat u = \frac{1}{\chi}\cdot u,$$
where $\cdot$ is coordinatewise multiplication. Both chirp multiplications have modulus $1$, so they change phases only. The only convolution is the middle one.

Worked example with $q=2$. Here $\chi_0=1$ and $\chi_1=e^{\pi i/2}=i$. Take $u=(1,3)$. Directly, $(F_2u)_0=(1+3)/2=2$ and $(F_2u)_1=(1-3)/2=-1$. By the identity, $\hat u = (1,\,-3i)$. Then $(\hat u\ast\chi)_0 = 1\cdot 1+(-3i)\cdot i = 4$ and $(\hat u\ast\chi)_1 = 1\cdot i+(-3i)\cdot 1 = -2i$, so $\hat u\circledast\chi = (2,\,-i)$. Multiplying by $\frac{1}{\chi} = (1,\,-i)$ gives $(2,\,-1)$, the same result.

The wrap-around is what makes the convolution cyclic. For $j>\ell$ the index $\ell-j$ is negative, and periodicity replaces $\chi_{\ell-j}$ by $\chi_{(\ell-j)\bmod q}$. The output $\ell$ is written at its own frequency label, with its factor $1/\chi_\ell$ applied there. The identity keeps the target permutation of the [transform identity with retained permutations](transform-identity.md) inside the formula, so that it is never executed as a separate sort. The paper says that

The two chirp multiplications cost $O(q)$ operations, so the transform costs one cyclic convolution of length $q$ plus $O(q)$. The transform's cost bound is stated in terms of the [logarithm](logarithm.md) $\lg$ to base 2, because it is that of the convolution plus $O(q)$.

The paper credits this conversion to, whose reference is
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

Write the answer to `exegenius/tasks/0436-audit-bluestein-chirp-identity.answer.json`, then run `exegenius submit 0436-audit-bluestein-chirp-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
