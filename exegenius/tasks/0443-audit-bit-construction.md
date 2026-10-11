# exegenius task 0443-audit-bit-construction

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

- $b$ (base), bound on `logarithm`: The fixed number, greater than 1, to which the logarithm is taken.
- $b$ (ring element), bound on `ring`: An element of the ring $R$, one of the arguments of its addition and multiplication.
- $z$ (complex number), bound on `root-of-unity`: A complex number that is tested for being a root of unity.
- $z$ (padded integer), bound on `exact-integer-multiplication`: A nonnegative integer with $z < 2^k$ that is written in binary.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $z$ (coefficient list), bound on `truncation`: A finite list of complex numbers, called coefficients.
- $S$ (position set), bound on `permutation`: A finite set of positions, the set whose elements a permutation rearranges.
- $t$ (step index), bound on `mathematical-induction`: The number of recursion levels passed, a nonnegative integer.
- $t$ (bit position), bound on `stable-radix-sort`: A bit position of a key, running over 0, 1, ..., w-1, which also numbers the passes.
- $h$ (chunk index), bound on `destination-rank`: The index of a chunk of an address, taking the value 1, 2 or 3.
- $t$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient, running from 0 to $m-1$.
- $X$ (array), bound on `array-norm`: A finite array of complex values.
- $t$ (coefficient index), bound on `array-norm`: The index of a coefficient of a representative, running from 0 to r-1.
- $C$ (constant factor), bound on `little-o-notation`: A constant factor in the big-O bound on $T_A(n)$.
- $t$ (prefix index), bound on `coprime`: The number of leading family members used in a least common multiple L_t.
- $S$ (combined axis length), bound on `coprime`: The product s_1 through s_d, which is the length of the combined cyclic axis.
- $t$ (indeterminate), bound on `ring-homomorphism`: The indeterminate of $Q$, whose square is 1 in $Q$.
- $\xi$ (element), bound on `ring-homomorphism`: An arbitrary element of the domain ring.
- $\eta$ (second element), bound on `ring-homomorphism`: An arbitrary element of the domain ring.
- $S$ (cycle length), bound on `ring-homomorphism`: A positive integer by which the paper's cyclic ring is reduced.
- $t$ (position), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $F$ (field), bound on `linear-algebra-basics`: A set with addition and multiplication in which every nonzero element has a multiplicative inverse, the scalars of the vector space.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map from one vector space over $F$ to another.
- $S$ (inverse map), bound on `linear-algebra-basics`: A linear map that serves as the inverse of a linear operator $T$ when $ST=TS=\mathrm{id}$.
- $K$ (second address chunk), bound on `linear-algebra-basics`: A binary address chunk, the second field of an address pair.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $\ell$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $K$ (second address field), bound on `linear-network-frames`: The second of two address fields, written as a vector; not a frame.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set, so it counts those elements.
- $T$ (three-element subsets), bound on `ground-set`: The set of all three-element subsets of $[h]$.
- $S$ (triple S), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, paired with T as a candidate neighbor.
- $T$ (triple T), bound on `indicator-vector`: A three-element subset of the ground set, called a triple, whose indicator vector is discussed.
- $t_T$ (indicator vector of T), bound on `indicator-vector`: The 0-1 vector with an entry 1 in each position of T and 0 elsewhere.
- $\mathbb{F}_2$ (binary field), bound on `indicator-vector`: The field with two elements, 0 and 1, in which 1+1=0.
- $\ell$ (column index), bound on `matrix-rank`: The column of a one in $\Pi$, which is also the index of the field $D_\ell$ it uses.
- $W$ (wire count), bound on `matrix-rank`: The number of wires in the network, which counts the edges that carry edge changes.
- $C$ (forward kernel), bound on `phase-factor`: The 2 by 2 matrix called the forward kernel.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index from 0 to q-1 that numbers the output coordinates.
- $K$ (linear map on q-vectors), bound on `discrete-fourier-transform`: A linear map from q-vectors to q-vectors, which is tested for being a contraction.
- $Y$ (output array), bound on `multidimensional-transform`: The output array of the transform.
- $b$ (index bit), bound on `butterfly`: The index bit, a binary digit of the position, that the level of the transform processes.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $z$ (formal variable), bound on `radix-digit-convolution`: The indeterminate of the polynomials $P_x$ and $P_y$, which is set to $2^b$ to recover the inputs.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than $s$.
- $\ell$ (halving count), bound on `gaussian-resampling`: The number of halvings of a transform length, so that the length is $2^\ell$.
- $K$ (two-point kernel matrix), bound on `two-point-kernel`: The $2\times 2$ matrix $\delta I+\kappa X$ that defines the two-point kernel.
- $X$ (bit flip), bound on `two-point-kernel`: The $2\times 2$ matrix that interchanges the two entries of a pair.
- $t$ (address bit string), bound on `tensor-product`: A bit string of length m that is an address on m coordinates.
- $K$ (output space), bound on `bilinear-map`: The vector space containing the values pi(e,d) of the bilinear map.
- $\mathbb{F}_2$ (binary field), bound on `binary-field`: The field with the two elements $0$ and $1$, with addition given by exclusive or and multiplication by AND.
- $K$ (example matrix), bound on `binary-field`: The $2 \times 2$ matrix over the binary field used in the example, with rows $(1, 1)$ and $(0, 1)$.
- $\xi$ (vector), bound on `bilinear-form`: A vector of $E$.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $E$.
- $K$ (scalar field), bound on `line-spanned-by-vector`: The field of scalars over which the vector space E is taken.
- $h$ (comparison function), bound on `big-theta-notation`: A second function of the same kind as $u$, against which the growth of $u$ is measured.
- $S$ (product of lengths), bound on `modular-inverse`: The product of all the axis lengths M_i.
- $\xi$ (generator), bound on `modular-inverse`: A generator of a cyclic group of order S, whose powers make up the group.
- $C$ (set of extended reals), bound on `extended-reals`: An arbitrary set of extended real numbers, whose infimum and supremum are taken.
- $C$ (bound constant), bound on `limit-inferior`: A constant in the big-O time bound of the main result.
- $C$ (complementary subspace), bound on `projection-along-subspace`: A subspace of $X$ that meets $U$ only in zero and whose sum with $U$ is all of $X$.
- $X$ (bank X), bound on `subset-intersection-network`: One of the two banks of scalars, with entries $X_\tau$ indexed by triples of triples.
- $Y$ (bank Y), bound on `subset-intersection-network`: The second of the two banks of scalars, with entries $Y_\tau$.
- $\xi$ (source vector), bound on `subset-intersection-network`: The vector of one bank's entries along the varying coordinate, read by a forward invocation.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of the other bank's entries along the varying coordinate, updated by a forward invocation.
- $W_{ST}$ (side wire), bound on `subset-intersection-network`: The scratch wire for an ordered pair of neighbouring triples $(S,T)$.
- $C_\ell$ (central wire), bound on `subset-intersection-network`: The scratch wire attached to an element $\ell$ of the ground set.
- $\ell$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, whose central wire is $C_\ell$.

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

## Page to audit (`bit-construction`)

````markdown
# Bit construction

The bit construction is a specialization of the [Subset-intersection network](subset-intersection-network.md) to scalars in $\mathbb F_2$, in which two triples are neighbours when they share exactly one element. It is the first of the two networks in the paper's Section 3 that exchange two banks of values while restoring every scratch wire, and the [Rank-saving recursion](rank-saving-recursion.md) depends on its wire count.

## The neighbour rule

Let $[h]=\{1,\dots,h\}$ be the ground set, with $h=100$, and let $\mathcal K$ be the set of three-element subsets of $[h]$. For $T\in\mathcal K$, let $t_T$ be its indicator vector. The neighbour rule is stated in terms of [indicator vectors](indicator-vector.md): for $S,T\in\mathcal K$, the intersection size is the dot product $|S\cap T| = t_S\cdot t_T$, so the rule is a condition on that dot product.

An ordered pair $(S,T)$ is a *neighbour pair* when $|S\cap T|=1$. A triple is never its own neighbour, since $|T\cap T|=3$. The bit construction has its scalars in the [Binary field](binary-field.md) $\mathbb{F}_2$, where addition is exclusive or and multiplication is AND, so every scalar is a single bit.

For a fixed triple $T$, let $z_b$ be the number of triples meeting $T$ in exactly one element, which are the neighbours of $T$. Choose the shared element in 3 ways and the other two elements from the 97 elements outside $T$:

$$z_b = 3\binom{97}{2} = 3\cdot 4656 = 13968.$$

## Wires and updates

One invocation works on a source bank with entries $\xi_T$ and a target bank with entries $\eta_S$, both indexed by triples. A bank is simply a family of scalars with one entry per triple. The invocation also has scratch wires: a side wire $W_{ST}$ for each neighbour pair $(S,T)$, and a central wire $C_\ell$ for each ground element $\ell\in[h]$. Scratch wires start at arbitrary values, so the construction has to cancel their contents.

Four linear updates, all over $\mathbb F_2$, act on these wires:

- *Copy* sets $W_{ST} \leftarrow W_{ST} + \xi_T$ for every neighbour pair. The paper states it as
- *Gather* sets $C_\ell \leftarrow C_\ell + \sum_{T\ni \ell}\xi_T$. The paper states it as.
- *Side injection* sets $\eta_S \leftarrow \eta_S + \sum_{T:\,|S\cap T|=1} W_{ST}$. The paper states it as.
- *Scatter* sets $\eta_S \leftarrow \eta_S + \sum_{\ell\in S} C_\ell$, where the paper's form is.

## What one invocation computes

Follow a value $\xi_T$ to $\eta_S$ by two routes. Along gather and then scatter, $\xi_T$ is added to $C_\ell$ for each $\ell\in T$, and each $C_\ell$ with $\ell\in S$ is added to $\eta_S$. The number of such paths is $|S\cap T|$. Along copy and then side injection, $\xi_T$ reaches $\eta_S$ only when $(S,T)$ is a neighbour pair. Over $\mathbb F_2$, the coefficient of $\xi_T$ in $\eta_S$ is therefore

$$|S\cap T| + [\,|S\cap T|=1\,] \pmod 2.$$

Checking the cases:

- If $|S\cap T|=1$, the two routes give $1+1\equiv 0$.
- If $|S\cap T|\in\{0,2\}$, the central route gives an even count and there is no side route, so the coefficient is $0$.
- If $S=T$, the central route gives $|S\cap S|=3\equiv 1$ and there is no side route, so the coefficient is $1$.

Hence one invocation adds $\xi_S$ to $\eta_S$ and changes nothing else, once the scratch wires are cleared. The paper states the same computation:, so the side wires must follow intersection size one. The central term is odd for intersection one and for the diagonal $S=T$. The side route must cancel the first case and leave the diagonal, which is wanted, so the neighbour rule excludes $S=T$.

For a small example, let the ground elements be $1,\dots,5$ and compare three pairs. For $S=\{1,2,3\}$ and $T=\{3,4,5\}$, the intersection is $\{3\}$, the central route contributes $1$ through $C_3$, and the side route contributes $1$ through $W_{ST}$, so the total is $0$. For $S=\{1,2,3\}$ and $T=\{2,3,4\}$, the intersection has two elements, the central route contributes $2\equiv 0$, and the pair is not a neighbour pair, so the total is $0$. For $S=T=\{1,2,3\}$, the central route contributes $3\equiv 1$, which is the diagonal term.

## Exchanging the banks

The scratch wires are cleared by the schedule rather than assumed zero. A forward invocation first subtracts whatever the side and central wires hold, then loads $\xi$ into them with copy and gather, adds their effect to $\eta$ with scatter and side injection, and finally unloads them. The effect on the target does not depend on the starting scratch values, which is why yS + xS.

Three invocations in sequence then exchange the banks. A forward invocation from $X$ to $Y$, followed by the inverse schedule from $Y$ to $X$, followed by a forward invocation from $X$ to $Y$, sends $(X,Y)$ to $(-Y,X)$ and restores every scratch wire. Over $\mathbb F_2$ we have $-1=1$, so the sign disappears and the result is the exchange $(X,Y)\mapsto(Y,X)$. The paper states this as and Ya.
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

Write the answer to `exegenius/tasks/0443-audit-bit-construction.answer.json`, then run `exegenius submit 0443-audit-bit-construction` in the project directory. If submit rejects the answer, fix the answer and submit again.
