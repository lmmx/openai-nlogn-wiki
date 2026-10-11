# exegenius task 0446-audit-address-interchange

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
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## Symbols bound on earlier pages

- $y$ (positive number), bound on `logarithm`: The positive number whose logarithm to base $b$ is taken.
- $m$ (order), bound on `root-of-unity`: The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $y$ (polynomial variable), bound on `root-of-unity`: The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, which is a root of unity in that ring.
- $m$ (dividend), bound on `prime-number`: An integer that a divisor a divides.
- $k$ (cofactor), bound on `prime-number`: An integer with m equal to a times k.
- $m$ (sequence length), bound on `pointwise-product`: The number of entries in each sequence, so $m$ counts the entries.
- $u$ (first input sequence), bound on `pointwise-product`: The first of the two input sequences, of length $m$.
- $j$ (entry index), bound on `pointwise-product`: An index naming one position in each sequence, with $0 \le j < m$.
- $y$ (indeterminate), bound on `pointwise-product`: The indeterminate of the quotient ring $\mathbb{C}[y]/(y^r+1)$ whose elements are the entries.
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary input string, of length $n$.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $m$ (modulus exponent), bound on `schonhage-strassen`: The positive integer exponent that defines the modulus $2^m+1$ of the Fermat-type residue ring.
- $m$ (output position), bound on `convolution`: The position of an output entry of the convolution.
- $j$ (second input position), bound on `convolution`: The position in b of the input entry that combines to an output entry.
- $s$ (source element), bound on `bijection`: An element of the source set A, the input to the map f.
- $u$ (address), bound on `permutation`: The position of one entry in an array.
- $y$ (indeterminate), bound on `polynomial-ring`: The formal variable of the polynomials in the ring.
- $m$ (modulus degree), bound on `polynomial-ring`: The number of coefficients in each representative, which is the degree of $f$.
- $u$ (representative), bound on `polynomial-ring`: The unique polynomial of degree less than $m$ in a class.
- $s$ (shift exponent), bound on `polynomial-ring`: The integer exponent in a shift $y^s$ by which a coefficient list is moved.
- $u$ (array entry), bound on `array-norm`: An entry of the array X, a complex number.
- $y$ (polynomial variable), bound on `array-norm`: The variable of the polynomials in the ring modulo y^r + 1.
- $u$ (family index), bound on `coprime`: A position in the family, taking values from 1 to N.
- $y$ (target indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q'$.
- $u$ (constant coefficient), bound on `ring-homomorphism`: The complex constant term of an element $u+vy$ of $Q'$.
- $u$ (field width), bound on `address-field`: The number of bits in each of the two fields being interchanged.
- $s$ (offset), bound on `cyclic-shift`: An integer taken modulo L that gives the amount of rotation.
- $V$ (stored bit volume), bound on `cyclic-shift`: The number of bits held in the array, which the cost bound is linear in.
- $x$ (vector), bound on `linear-algebra-basics`: A vector over $F$; the letter stands for an arbitrary vector.
- $y$ (second vector), bound on `linear-algebra-basics`: A vector over $F$, a second arbitrary vector.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, so the length of the tuples.
- $j$ (coordinate index), bound on `linear-algebra-basics`: The index that runs from 1 to $m$ and labels the coordinates $x_j$ of a vector.
- $u$ (vertex), bound on `linear-algebra-basics`: A vertex of the network, the starting point of an edge.
- $u$ (earlier vertex), bound on `linear-network-frames`: The earlier of the two vertices joined by an edge, the vertex the edge leaves.
- $s$ (input index), bound on `linear-network-frames`: The position of an input of a gate, running from 1 to t.
- $x$ (route vertex), bound on `linear-network-frames`: A vertex on a route, numbered in order from the source to the sink.
- $V$ (operator space), bound on `eigenvalue`: The vector space on which the linear operator T acts.
- $s$ (row index), bound on `matrix-rank`: The row of a one in $\Pi$, which is also the index of the field $H_s$ it updates.
- $W$ (wire count), bound on `matrix-rank`: The number of wires in the network, which counts the edges that carry edge changes.
- $\tau$ (complex number), bound on `phase-factor`: A complex number written as alpha plus beta i.
- $s$ (address), bound on `phase-factor`: An address in a butterfly layer, whose selected bits determine the phase applied to its value.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the argument of the transform.
- $s$ (input index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the input coordinates.
- $s$ (modulus exponent), bound on `transform-axis`: The power of two $s$ in the modulus $y^s+1$ of the polynomial that stores one coordinate.
- $y$ (polynomial indeterminate), bound on `transform-axis`: The indeterminate of the polynomial modulo $y^s+1$; its powers serve as roots of unity on the remaining axes.
- $s$ (axis index), bound on `multidimensional-transform`: The index of one axis, running from 1 to D.
- $y$ (polynomial variable), bound on `multidimensional-transform`: The variable of the polynomial that stores one coordinate of the array.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The variable of the polynomial ring $R_r$, in which $y^r$ is identified with $-1$.
- $s$ (shift amount), bound on `synthetic-transforms`: The number of places a shift moves each coefficient, with $0 \le s < 2r$.
- $\tau$ (butterfly offset), bound on `synthetic-transforms`: The offset of a butterfly pair within the first half of its block, from $0$ to $\delta-1$.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $\tau$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: An element of the ring whose positive integer power equals 1.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in the source vector, the length of the transform being replaced.
- $u$ (generic source vector), bound on `gaussian-resampling`: A generic vector of length $s$, on which $P_s$ acts.
- $j$ (source position), bound on `gaussian-resampling`: An index position of a length-$s$ vector, running from $0$ to $s-1$ in the permutation.
- $k$ (resampled position), bound on `gaussian-resampling`: An index position of a length-$t$ vector in the permutation $P_t$.
- $\tau$ (common exponent), bound on `gaussian-dyadics`: The larger of the two denominator exponents, which gives the power of two in a common denominator.
- $\oplus$ (bitwise exclusive or), bound on `two-point-kernel`: The operation giving the bitwise exclusive or of two addresses.
- $j$ (column index), bound on `tensor-product`: The index of a column of a matrix, here also the index of a block-column.
- $m$ (tensor power count), bound on `tensor-product`: The number of factors in a tensor power, which counts the coordinates the operator acts on.
- $s$ (output address), bound on `tensor-product`: An output address of m coordinates, a bit string whose bit at coordinate i is s_i.
- $\tau$ (processed positions), bound on `carry-propagation`: The number of low positions already processed, so that the sums run over $t < \tau$.
- $\oplus$ (exclusive or), bound on `binary-field`: The addition of the binary field, which gives $1$ exactly when its two bits differ.
- $\tau$ (field element), bound on `binary-field`: An arbitrary element of the binary field, so it is $0$ or $1$.
- $\tau$ (choice of three triples), bound on `line-spanned-by-vector`: A triple (tau_1, tau_2, tau_3) of three-element subsets of the ground set, selecting one label.
- $\tau$ (centered residue), bound on `centered-residue`: The integer in $[-\kappa/2, \kappa/2)$ that is congruent to $\nu$ modulo $\kappa$.
- $\tau$ (solution), bound on `chinese-remainder-theorem`: An unknown integer, which is a solution when it satisfies every congruence of the system.
- $\tau$ (reflected chirp), bound on `cyclic-convolution`: The function tau(delta) of an integer delta, read as a sequence of length t.
- $\tau$ (remainder), bound on `bezout-identity`: The remainder when beta is divided by e, which lies between 0 and e minus 1.
- $u$ (function), bound on `big-theta-notation`: A function from input sizes to nonnegative real numbers, whose growth is being compared with that of $h$.
- $\tau$ (generator), bound on `cyclic-group`: A fixed element of the group; its powers give every element of the cyclic group $C_\kappa$.
- $\tau$ (real number), bound on `extended-reals`: A generic real number, used when the order and arithmetic of the extended reals are stated.
- $k$ (term index), bound on `limit-inferior`: The position of a term in a sequence, an index counting from 1.
- $m$ (tail start position), bound on `limit-inferior`: The position from which the tail of a sequence starts.
- $\log$ (base-2 logarithm), bound on `n-log-n-conjecture`: The base-2 logarithm, as used in the expression $n \log n$.
- $\tau$ (family parameter), bound on `family-parameter`: The index of a member of the family: a nonnegative integer that selects which construction is built and so fixes its size.
- $s$ (sequence length), bound on `normalized-cyclic-convolution`: The number of entries in each input sequence, which is also the length of the transform.
- $\tau$ (chirp position), bound on `bluestein-chirp-identity`: The integer position of a chirp entry, which may be negative or larger than q-1.
- $j$ (record position), bound on `phase-twist`: The position of a coefficient in a record, running from $0$ to $r-1$.
- $\oplus$ (direct sum), bound on `subspace-labels`: The sum of two subspaces that meet only in zero, so that each vector of the sum is uniquely a vector of one plus a vector of the other.
- $\tau$ (kernel coefficient tau), bound on `subspace-labels`: The first Gaussian dyadic coefficient of the translation kernel $\tau I+\delta X_v$.
- $\tau$ (bank index), bound on `subset-intersection-network`: A triple of triples, indexing the entries of a bank.
- $V$ (head label), bound on `complex-phase-network`: The label at the head of an edge, whose frame is applied last along that edge.
- $x$ (control vector), bound on `scratch-storage`: The vector of control values, with one entry $x_T$ for each triple $T$.
- $y$ (target vector), bound on `scratch-storage`: The vector of target values, with one entry $y_S$ for each triple $S$.
- $V$ (copy operator), bound on `scratch-storage`: The operator that adds each control value $x_T$ to the side wire $W_{ST}$ of each neighbouring pair $(S,T)$.

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

## Page to audit (`address-interchange`)

````markdown
# Address-field interchange

Address-field interchange is a tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width. [Integer multiplication below n log n](main-theorem.md) uses it to organize the layouts of its transforms.

A tape procedure moves tape contents in a bounded number of passes. The procedure runs on the [Fixed-tape machine model](fixed-tape-model.md) with a fixed number of one-dimensional tapes.

Let $u$ be the bits per field and $V$ the stored bit volume, the number of bits held in the array. Let $\tau<1$ be a fixed number, the exponent in the bound $O(V u^{\tau})$.

The method is not a direct copy., although its final effect is a permutation. Write $x$ and $y$ for the two fields, read as blocks of bits at matching positions; these letters change meaning here. Let $\oplus$ denote bitwise exclusive or (XOR), which adds bits modulo 2. Three XOR steps swap the fields:
$$(x,y)\to(x,\;x\oplus y)\to(y,\;x\oplus y)\to(y,\;x).$$
The second step replaces $x$ by $x\oplus(x\oplus y)=y$, since a block XORed with itself is zero. For example, $x=10$, $y=01$ give $(10,01)\to(10,11)\to(01,11)\to(01,10)$.

The source uses signs: Over bits, $-y=y$ and $y+x=x\oplus y$, so the signs vanish and leave the chain above.

Each XOR step acts on all matching addresses at once. The interchange is carried out by a [Linear networks and frames](linear-network-frames.md) network, which restores its [scratch storage](scratch-storage.md) to its starting contents, whatever they were. Per the source, The network is fixed and So the data changes do not depend on the scratch starting values:

The cost bound comes from a recursion on the width. Let $m\ge 2$ be a fixed integer base; the letter $m$ changes meaning here. A width $u=m^k$ has $k=\log_m u$ levels; the letter $k$ changes meaning here too. Let $W\ge 2$ be the number of equal pieces the volume is cut into at each call, and let $s$ be the number of smaller calls one call makes. Each child works on $V/W$ bits, since

Let $j$ count levels below the top call; the letter $j$ changes meaning here. Level $j$ has $s^j$ calls, each on volume $V/W^j$, so its work is proportional to $V(s/W)^j$. The source's counting gives Hence $s/W<m$. The source then chooses Such $\tau$ exists since $m^{\tau}\to m$ as $\tau\to 1$.

The recursion stops after $k$ levels, since The levels sum to $V\sum_{j=0}^{k}(s/W)^j$. If $s/W\le 1$ this is at most $(k+1)V$, and $k+1=O((m^{\tau})^k)$ because $m^{\tau}>1$. If $s/W>1$ it is $O(V(s/W)^k)$, and $(s/W)^k<(m^{\tau})^k$. Either way the work is $O(V(m^{\tau})^k)=O(Vu^{\tau})$, since $(m^{\tau})^k=(m^k)^{\tau}=u^{\tau}$.
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

Write the answer to `exegenius/tasks/0446-audit-address-interchange.answer.json`, then run `exegenius submit 0446-audit-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
