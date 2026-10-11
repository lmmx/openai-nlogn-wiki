# exegenius task 0206-audit-subset-intersection-network

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
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
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

- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $b$ (input bit), bound on `xor`: The second of the two bits that an XOR combines.
- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $T$ (linear map), bound on `linear-algebra-basics`: A linear map between vector spaces over $F$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The matrix with ones on the diagonal and zeros elsewhere.
- $S$ (candidate inverse), bound on `linear-algebra-basics`: A linear map that is a two-sided inverse of the operator $T$ when $T$ is invertible.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $n$ (input length), bound on `limit-inferior`: The number of bits in each input, which is the index of the running-time function.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $T$ (padded box size), bound on `cost-table`: The power of two that sets the number of cells in the padded box.
- $K$ (chunk width), bound on `cost-table`: The number of bits in each address chunk.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $\ell$ (log axis length), bound on `cost-table`: The base-2 logarithm of $r$.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set $[h]$.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $W$ (volume divisor), bound on `address-interchange`: The number of equal pieces the volume is cut into at each level.
- $\mathbb{F}_2$ (binary field), bound on `binary-field`: The field with the two elements 0 and 1, where addition is exclusive or and multiplication is AND.
- $h$ (ground-set size), bound on `indicator-vector`: The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $T$ (triple), bound on `indicator-vector`: A three-element subset of the ground set $[h]$.
- $t_T$ (triple indicator vector), bound on `indicator-vector`: The indicator vector of the triple $T$: the 0-1 vector with entry 1 exactly at the positions of the elements of $T$.
- $K$ (scalar field), bound on `line-spanned-by-vector`: The field of scalars over which the vector space E is taken.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $Q$ (second matrix), bound on `tensor-product`: A second matrix, which is copied once for each entry of P in the tensor product P \otimes Q.
- $\mathbb{Q}$ (rational numbers), bound on `matrix-rank`: The field of rational numbers, the fractions p/q with integers p and q nonzero.
- $f$ (selected position count), bound on `union-bound`: The number of selected bit positions $j_0, \dots, j_{f-1}$ in the packed operation.
- $K$ (segment width), bound on `union-bound`: The number of bits in each segment, so that each guard value takes one of $2^{K-1}$ values.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $h$ (chunk index), bound on `destination-rank`: The index of one of the three address chunks, taking values 1, 2 or 3.
- $\beta$ (imaginary part), bound on `phase-factor`: The imaginary part of the complex number z.
- $b$ (second numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a second element $b/2^l$ of $\mathbb{D}$.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $\ell$ (output index), bound on `discrete-fourier-transform`: An integer index of output coordinates, running from 0 to q-1.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit, a positive integer.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.
- $X$ (input array), bound on `multidimensional-transform`: The input array, on which the transform acts.
- $Y$ (output array), bound on `multidimensional-transform`: The output array, the transformed array.
- $h$ (output position), bound on `multidimensional-transform`: A position in the output array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $t$ (transform length), bound on `synthetic-transforms`: The number of entries in the transform, a power of two dividing $2r$.
- $h$ (input list), bound on `synthetic-transforms`: The list of $t$ records $(h_0,\dots,h_{t-1})$ that the transform takes as input.
- $t$ (resampled length), bound on `gaussian-resampling`: The number of entries in the resampled vector, a power of two greater than s.
- $S$ (first Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $T$ (second Gaussian map), bound on `gaussian-resampling`: A second Gaussian-weighted map from length-s vectors to length-t vectors, used in the proof.
- $\xi$ (first input value), bound on `butterfly`: The first of the two values that the butterfly takes as input.
- $\eta$ (second input value), bound on `butterfly`: The second of the two values that the butterfly takes as input.
- $f$ (modulus polynomial), bound on `polynomial-ring`: The fixed monic polynomial with complex coefficients by which the ring is reduced.
- $X$ (array of complex values), bound on `array-norm`: A finite array of complex values, the argument of the norm.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between a computed input and the exact input w.
- $e$ (integer), bound on `congruence-modulo`: An integer, the other of the two integers compared by congruence.
- $f$ (packed polynomial f), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, one of the two inputs that are packed.
- $g$ (packed polynomial g), bound on `signed-packing`: A polynomial in $y$ with $r$ integer coefficients, the second input that is packed.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary product $fg$, a polynomial with at most $2r-1$ coefficients $h_j$.
- $f$ (first input sequence), bound on `cyclic-convolution`: The first of the two sequences, of length s.
- $g$ (second input sequence), bound on `cyclic-convolution`: The second of the two sequences, of length s.
- $\ell$ (coordinate index), bound on `cyclic-coordinate`: The index naming one cyclic coordinate, running from 1 to d.
- $\beta$ (bilinear map), bound on `bilinear-map`: A map sending each pair of vectors, one from V and one from W, to a vector in U.
- $W$ (second input space), bound on `bilinear-map`: A vector space over the scalars, whose vectors form the second argument of the bilinear map.
- $X$ (vector space), bound on `bilinear-form`: The vector space on which the bilinear form is defined.
- $\xi$ (vector), bound on `bilinear-form`: A vector of $X$.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $X$.
- $J$ (all-one matrix), bound on `bilinear-form`: The matrix all of whose entries are 1.
- $t_T$ (triple indicator vector), bound on `bilinear-form`: The indicator vector of the triple $T$, with entries 1 at the positions of $T$ and 0 elsewhere.
- $\cap$ (intersection), bound on `subspace-labels`: The vectors lying in both subspaces.
- $I$ (identity), bound on `subspace-labels`: The identity operator (or matrix).
- $x$ (address), bound on `subspace-labels`: An address, a binary point at which array entries are indexed; the letter changes meaning here.
- $f$ (function of addresses), bound on `subspace-labels`: A function of addresses; the letter changes meaning here.
- $\mathbb{Q}$ (rationals), bound on `subspace-labels`: The field of rational numbers.
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set.
- $J$ (all-ones matrix), bound on `subspace-labels`: The h by h matrix with every entry 1.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $t_T$ (indicator vector), bound on `subspace-labels`: The 0-1 vector with entry 1 on the triple T.
- $S$ (triple), bound on `subspace-labels`: A second three-element subset, used for inner products.
- $t_S$ (indicator vector), bound on `subspace-labels`: The 0-1 vector of the triple S.

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

## Page to audit (`subset-intersection-network`)

````markdown
# Subset-intersection network

A *subset-intersection network* is a fixed linear network whose wires carry single scalars and whose gates combine them according to how much two three-element subsets overlap. It exchanges two banks of values while restoring every scratch wire. It is the finite exchange step on which the main result, [Integer multiplication below n log n](main-theorem.md), builds: the exchange is used to change the representation of data at small cost.

## Banks, wires and the two vectors

Fix $h$, the number of elements of the ground set $[h]=\{1,\dots,h\}$. A *triple* is a three-element subset of $[h]$, and $\mathcal K$ is the set of all triples. The letters $S$ and $T$ denote triples.

A *bank* is a family of scalars indexed by $\beta=(\beta_1,\beta_2,\beta_3)\in\mathcal K^3$. The network has two banks, $X$ and $Y$, with entries $x_\beta$ and $y_\beta$. On this page $x$ and $y$ do not mean the input strings of earlier pages: the letters change meaning here, and $X$ and $Y$ name banks.

Each wire carries one scalar. A gate is a fixed linear map on a chosen set of wires, and wires it does not touch keep their values. A *scratch wire* is an auxiliary wire whose initial value may be arbitrary, and the network must return it to that value.

The network changes one coordinate of $\beta$ at a time. Fix the other two coordinates. The entries of a bank along the varying coordinate then form a vector indexed by $\mathcal K$. Call these two vectors $\xi$ (the source) and $\eta$ (the target), so that $\xi_T$ is the source entry at triple $T$ and $\eta_S$ is the target entry at triple $S$.

## The bit construction

All arithmetic is mod 2: the scalars lie in the binary field $\mathbb F_2=\{0,1\}$, where $-1=1$, so signs vanish. Distinct triples $S$ and $T$ are *neighbours* when they share exactly one element:

For each ordered neighbouring pair $(S,T)$ there is a side wire $W_{ST}$. For each element $\ell\in[h]$ there is a central wire $C_\ell$. Four gates act on these wires:

- copy: adds $\xi_T$ to $W_{ST}$ for each neighbouring pair $(S,T)$;
- side injection: adds $\sum_{T\text{ neighbour of }S} W_{ST}$ to $\eta_S$;
- gather: adds $\sum_{T\ni \ell}\xi_T$ to $C_\ell$ for each $\ell\in[h]$;
- scatter: adds $\sum_{\ell\in S}C_\ell$ to $\eta_S$.

A *forward invocation* from $\xi$ to $\eta$ runs the following eight rows in order. Each row is one gate on the wires named in its grouping.

| row | operation | gate grouping |
|---|---|---|
| 0 | subtract side injection | one gate per target |
| 1 | subtract scatter | one gate on targets and centre |
| 2 | copy | one gate per source |
| 3 | gather | one gate on sources and centre |
| 4 | scatter | one gate on targets and centre |
| 5 | side injection | one gate per target |
| 6 | undo gather | one gate on sources and centre |
| 7 | undo copy | one gate per source |

Rows 0 and 1 remove the effect of whatever the scratch wires already hold: Rows 2 to 5 load the source values and add their effect to the target, and rows 6 and 7 restore the scratch wires. The net change to the target is the sum of two routes, copy then side injection and gather then scatter, and it does not depend on the scratch values.

**Worked check.** Take $h\ge 5$ and $S=\{1,2,3\}$, and find the coefficient of each $\xi_T$ in the final $\eta_S$. The gather-then-scatter route contributes $|S\cap T| \bmod 2$, because each shared element is counted once. The side route contributes $1$ exactly when $T$ is a neighbour of $S$. Three cases cover all $T$:

- $T=S$: the central route gives $|S\cap S| \bmod 2=1$, and $S$ is not its own neighbour, so the coefficient is $1$.
- $T=\{1,4,5\}$, so $|S\cap T|=1$: the central route gives $1$ and the side route gives $1$, so the total is $1+1=0$.
- $|S\cap T|\in\{0,2\}$: the central route gives $0$, and $T$ is not a neighbour, so the total is $0$.

So the net change is $\eta_S\leftarrow\eta_S+\xi_S$, and every other entry of $\eta$ is unchanged. The side wires exist to cancel the intersection-one terms:

## Exchanging the banks

Over $\mathbb F_2$ a forward invocation adds its source into its target, and the inverse schedule, with source $Y$ and target $X$, adds $Y$ into $X$. The construction runs three stages, one per coordinate of $\beta$, each on the vectors of one line with the other coordinates fixed. On one line, with $\xi$ the $X$-entries and $\eta$ the $Y$-entries, the stages act as follows:

1. Stage 1, a forward invocation from $X$ to $Y$: $(\xi,\eta)\mapsto(\xi,\ \xi+\eta)$.
2. Stage 2, the inverse schedule from $Y$ to $X$: $(\xi,\ \xi+\eta)\mapsto(\eta,\ \xi+\eta)$, since $\xi+(\xi+\eta)=\eta$.
3. Stage 3, a forward invocation from $X$ to $Y$: $(\eta,\ \xi+\eta)\mapsto(\eta,\ \xi)$, since $(\xi+\eta)+\eta=\xi$.

The paper states the outcome over the integers with signs, as and every auxiliary wire restored. Over $\mathbb F_2$ the signs disappear, so the three invocations exchange the two banks on every line.

## Labels and the cost of a change of representation

The sources do not define the cost of a change of representation. The reading used here is the one the paper's count implies: so the cost on an edge is governed by its dimension change.

Each gate and terminal is labelled by [Subspace labels](subspace-labels.md): a nondegenerate subspace of a fixed bilinear space. Nondegenerate means the form restricts to a nonsingular form on the subspace, so the whole space splits as the subspace plus its orthogonal complement. The orthogonal residual of an edge is the part of the larger label orthogonal to the smaller one, and its dimension is the absolute change in label dimension. The paper's only decreasing edges are

Orthogonality and nondegeneracy are tested with the form of [Bilinear form](bilinear-form.md). For the bit network take $\mathbb Q^h$ with the form $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$, where $I$ is the $h\times h$ identity matrix and $J$ is the all-one matrix. Let $t_T$ be the $0/1$ indicator vector of $T$. Since $t_S^{\mathsf T}t_T=|S\cap T|$ and $t_S^{\mathsf T}Jt_T=9$,

$$\langle t_S,t_T\rangle=|S\cap T|-1,$$

so $\langle t_T,t_T\rangle=2$, and two neighbours $S,T$ satisfy $\langle t_S,t_T\rangle=0$. The paper takes $h=100$, and then $J$ has eigenvalues $h$ and $0$, so the form has eigenvalues $1$ and $1-h/9$. Hence field of the bit network.

The orthogonality of neighbours is what makes the nesting work. On a side wire joining neighbours $X$ and $Y$, the paper needs the line $\langle t_X\rangle$ to sit inside $t_Y^{\perp}$, and The gate labels are tensor products built from these lines, and the paper's Lemma 6 checks every edge; this page does not reproduce that table.

The complex variant keeps the same schedule and changes the scalars and the neighbour rule: even intersection.

The network is built within the framework of [Linear networks and frames](linear-network-frames.md): every wire is a role and every gate carries a frame, so the same scalar gates can act on arrays.
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

Write the answer to `exegenius/tasks/0206-audit-subset-intersection-network.answer.json`, then run `exegenius submit 0206-audit-subset-intersection-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
