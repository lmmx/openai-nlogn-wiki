# exegenius task 0450-audit-endpoint-operator

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
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Subspace labels (also: binary label)
- Linear networks and frames (also: roles, frames, network of wires and gates, network, vertex, edge, source and sink vertices, Edge change)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network, side and central wires, gather and scatter, scalar network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks, address-field interchange procedure, field interchanges)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant, orthogonal residual of an edge)
- Transform identity with retained permutations (also: target permutation, coordinate permutations)
- Carry propagation (also: carry scan)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Transform axis (also: axis, remaining axes, reduction axis)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms)
- Bilinear map (also: bilinear product, bilinear contraction)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2, copy step)
- Binary change of basis (also: residual basis of directions)
- Bit procedure
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
- Normalization scales (also: normalizations and known scales)
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload (also: record)
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring (also: polynomial suffix)
- Matrix rank (also: rational rank, rank of a shear, Row reduction and pivots)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Scratch storage (also: scratch values, scratch chunk, scratch wires, forward schedule, linear-readout version)
- Tensor product (also: tensor power)
- Truncation
- Exclusive or (also: XOR)
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
- Bit construction
- Chinese remainder theorem (also: CRT)
- Cyclic group (also: cyclic group of order S)
- Diagonal scaling
- Eigenvalue
- Extended real numbers
- Family parameter
- Frequency domain
- Incidence
- Independence of events
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Logical bit volume
- Ring
- Orthogonal complement
- Pointwise product
- Projection along a subspace
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Tape procedure
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $n$ (integer argument), bound on `logarithm`: The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on `base-two-logarithm`: A positive integer whose base-2 logarithm is taken.
- $c$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $v$ (second input sequence), bound on `pointwise-product`: The second of the two input sequences, of length $m$.
- $w$ (pointwise product), bound on `pointwise-product`: The sequence of length $m$ whose entry at each index is the product of the entries of $u$ and $v$ at that index.
- $r$ (ring size), bound on `pointwise-product`: A power of two that counts the complex coefficients in an entry, since each entry is a polynomial of degree less than $r$.
- $n$ (input length), bound on `running-time-cost`: The number of cells holding an input, that is, the length of the input string.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs $x$ and $y$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $n$ (input length), bound on `schonhage-strassen`: The number of bits in each of the two input integers.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (first input position), bound on `convolution`: The position in a of the input entry that combines to an output entry.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $w$ (target element), bound on `bijection`: An element of the target set B, which the onto condition requires to be hit by some element of A.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in a record's key, which is also the number of passes.
- $r$ (modulus exponent), bound on `polynomial-ring`: The exponent of $y$ in the modulus $y^r+1$, a power of two at least 2.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $e$ (power exponent), bound on `polynomial-ring`: The exponent of $y$ in a power $y^e$ that is reduced when $e \ge m$.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $r$ (coefficient count), bound on `array-norm`: The number of coefficients in each representative of a ring element, equal to the degree of the modulus y^r + 1.
- $g$ (ring element), bound on `array-norm`: An element of the polynomial ring modulo y^r + 1.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $v$ (second family index), bound on `coprime`: A second position in the family, different from u in the coprimality condition.
- $g$ (all-ones tuple), bound on `coprime`: The all-ones tuple (1,...,1), one entry per family member, whose order is the least common multiple of the family.
- $e$ (multiple), bound on `coprime`: The least positive integer with e g = 0, which is the order of the element g.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $v$ (linear coefficient), bound on `ring-homomorphism`: The complex coefficient of $y$ in an element $u+vy$ of $Q'$.
- $\rho$ (reduction map), bound on `ring-homomorphism`: The map from $Q$ to $\mathbb{C}$ sending $\alpha+\delta t$ to $\alpha+\delta$.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar in $F$, multiplying vectors.
- $i$ (output coordinate index), bound on `linear-algebra-basics`: The index of a coordinate of the output $Ax$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the endpoint of an edge.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $D_v$ (frame of vertex v), bound on `linear-algebra-basics`: The frame of vertex $v$, an invertible linear operator on arrays.
- $D_u$ (frame of vertex u), bound on `linear-algebra-basics`: The frame of vertex $u$, an invertible linear operator on arrays.
- $g$ (logical array), bound on `linear-algebra-basics`: The array the computation means, before any change of representation.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $\mathrm{source}$ (source vertex), bound on `linear-network-frames`: The source vertex of an input wire.
- $\mathrm{sink}$ (sink vertex), bound on `linear-network-frames`: The sink vertex of an output role.
- $\rho$ (role permutation), bound on `linear-network-frames`: The permutation of roles that sends each input role to an output role.
- $\varepsilon$ (routing sign), bound on `linear-network-frames`: The fixed sign by which the network multiplies the value routed from input role $\ell$.
- $e$ (eigenvector), bound on `eigenvalue`: A nonzero vector of V that the operator T maps to a multiple of itself.
- $D$ (second field vector), bound on `matrix-rank`: The vector $(D_1, \ldots, D_m)$ of $m$ address fields, which the shear reads without changing.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $D$ (selected bit count), bound on `phase-factor`: The number of selected bits of an address in a layer.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $i$ (imaginary unit), bound on `discrete-fourier-transform`: The imaginary unit, the square root of minus one, used in the complex exponent and coordinates.
- $D$ (axis count), bound on `transform-axis`: The number of axes of the array, which is also the number of coordinates in each address.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $r$ (record length), bound on `synthetic-transforms`: A power of two, the number of complex coefficients in a record.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $e$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a representative, running from 0 to r-1.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $v$ (generic resampled vector), bound on `gaussian-resampling`: A generic vector of length $t$, on which $P_t$ acts.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $e$ (denominator exponent), bound on `gaussian-dyadics`: The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The complex number whose square is $-1$.
- $e$ (bit position), bound on `two-point-kernel`: The index of the address bit along which the kernel acts, counted from the least significant bit.
- $i$ (row index), bound on `tensor-product`: The index of a row of a matrix, here also the index of a block-row and of a coordinate.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $e$ (first argument), bound on `bilinear-map`: An element of the first argument space E.
- $e$ (second integer), bound on `congruence-modulo`: An integer, the second of the two integers compared for congruence.
- $v$ (nonzero vector), bound on `line-spanned-by-vector`: A nonzero vector of E whose scalar multiples form a line; here it is a vector, not a vertex.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences of length n whose cyclic convolution is taken.
- $w$ (formal variable), bound on `cyclic-convolution`: The variable whose powers index the entries of the polynomial that represents a sequence.
- $\varepsilon$ (exponent offset), bound on `cyclic-convolution`: The amount by which a reduced exponent exceeds n.
- $e$ (least positive combination), bound on `bezout-identity`: The least positive integer of the form beta times mu' plus gamma times nu'.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $i$ (axis index), bound on `modular-inverse`: The position of an axis among the axes.
- $k$ (term index), bound on `limit-inferior`: The position of a term in a sequence, an index counting from 1.
- $\varepsilon$ (positive tolerance), bound on `limit-inferior`: A positive real number used as a tolerance in a limit criterion.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers, a count of bits.
- $g$ (second disk-grid ring array), bound on `opposite-transform`: The second of the two disk-grid ring arrays whose convolution the synthetic transforms compute.
- $w$ (complex vector), bound on `transform-identity`: A complex vector, the argument of the permutation $P_t$ in this page's notation.
- $s$ (sequence length), bound on `normalized-cyclic-convolution`: The number of entries in each input sequence, which is also the length of the transform.
- $v$ (shift vector), bound on `subspace-labels`: A vector in $\mathbb F_2^m$ by which a translation shifts addresses (this letter changes meaning on this page).
- $c$ (starting central values), bound on `scratch-storage`: The starting values of the central wires $C_\ell$.
- $k$ (number of levels), bound on `address-interchange`: The number of levels in the recursion on the width, so that a width $u=m^k$ has $k=\log_m u$ levels.
- $s$ (call count), bound on `address-interchange`: The number of smaller calls that one call makes.

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

## Page to audit (`endpoint-operator`)

````markdown
# Endpoint operator

The endpoint operator is realised by a [linear network](linear-network-frames.md) on each role array once all intermediate frames have cancelled, so it depends only on the frames at the two ends of a route. The recursion in [rank-saving recursion](rank-saving-recursion.md) uses it to count the smaller calls on each edge.

The endpoint operator is instantiated by the [bit procedure](bit-procedure.md) as an [address shear](address-shear.md): a map that adds one address field to the other and leaves the second unchanged.. That shear is implemented by a small number of [field interchanges](address-interchange.md).

The frame at a vertex $v$ is the invertible operator $D_v$ on arrays, and the stored array at $v$ is $D_v g$ when the [logical array](logical-array.md) is $g$. Take a path of three vertices $v_0$, $v_1$, $v_2$, and write $D_{v_0}$, $D_{v_1}$, $D_{v_2}$ for the frames at them. $D_v D_u^{-1}$ changes the stored array from $D_u g$ to $D_v g$. So the stored array changes from $D_{v_0} g$ to $D_{v_1} g$ on the first edge and from $D_{v_1} g$ to $D_{v_2} g$ on the second. The two edge changes compose to
$$(D_{v_2} D_{v_1}^{-1})(D_{v_1} D_{v_0}^{-1}) = D_{v_2} D_{v_0}^{-1},$$
because $D_{v_1}^{-1} D_{v_1}$ is the identity. The frame at the middle vertex cancels, and only the frames at the ends remain.

A route through the whole network composes in the same way. Each edge contributes its change, and a pointwise linear gate passes a common frame through unchanged:. Write $\rho$ for the signed role permutation that the [scalar network](subset-intersection-network.md) realises, so input role $w$ goes to output role $\rho(w)$, and $\varepsilon_w$ for the sign that the route carries. Then the route applies
$$\varepsilon_w\, D_{\mathrm{sink}(\rho(w))}\, D_{\mathrm{source}(w)}^{-1}$$
to the input array, where $D_{\mathrm{source}(w)}$ is the frame at the vertex where input role $w$ starts and $D_{\mathrm{sink}(\rho(w))}$ the frame at the vertex where output role $\rho(w)$ ends. The endpoint operator maps the stored form of the [logical array](logical-array.md) $g$ at the start of the route to its stored form at the end.

The route also exchanges roles, so output role $\rho(w)$ holds what input role $w$ held. To undo this, move each output role back to the role it came from, which applies the inverse of $\rho$, and multiply by $\varepsilon_w$ again. A sign squares to $1$, so this removes the sign. Each role $w$ then holds $D_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ applied to its array. The endpoint operator holds on every role of the [scalar network](subset-intersection-network.md), including the roles that carry auxiliary scalar values.

The frames are chosen for this purpose:
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

Write the answer to `exegenius/tasks/0450-audit-endpoint-operator.answer.json`, then run `exegenius submit 0450-audit-endpoint-operator` in the project directory. If submit rejects the answer, fix the answer and submit again.
