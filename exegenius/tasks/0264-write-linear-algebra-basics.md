# exegenius task 0264-write-linear-algebra-basics

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Open with one or two sentences that say what the concept is and what it is for on the way to the target (the step of the argument it presents, and the pages that build on it, are listed below), so a reader arriving from a link knows at once why the page matters.
- If the page presents a step of the argument, explain how its method shows its claim. Give the reader every motivation the task marks as not stated by the sources: the sources will not.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, say in a sentence what this page uses it for, and give that sentence as a relation: the prerequisite's id, a predicate, and the sentence copied exactly. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject and the prerequisite as object: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". If the sentence says "the transforms are reduced by X", the predicate is "reduces its transforms by", not "are reduced to". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"); the sentence must link or name the prerequisite. Pick the predicate that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources: read the parts you need (search for the evidence quotes). State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Back each specific claim taken from a source (a result, a constant, a construction step) with the source text it rests on, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them. Submit rejects text not found in the named source. Do not cite common background.
- Be concrete and specific. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication (also: exact multiplication)
- Address field (also: address chunk, chunk, target chunk, selected address bits)
- Cyclic shift (also: controlled cyclic shift, signed shifts)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Destination rank (also: prefix-slot move, move, extracted records, rectangular routine, hole, destination key)
- Little-o notation (also: limit as lambda tends to infinity)
- Array norm (also: norm of an array, coefficient bound)
- Payload (also: record)
- Polynomial ring (also: polynomial suffix)
- Ring homomorphism and isomorphism (also: ring homomorphism and ring isomorphism)
- Schoolbook multiplication (also: the paper's construction)
- Truncation
- Address (also: binary addresses)
- Array (also: disk array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Bijection
- Permutation
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## This page

Concept: Linear algebra basics
Gloss: Vector spaces over a field, linear maps and matrices, and the inverse of an invertible linear operator.
Also called: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map, usual axioms

## Where the argument relies on this page

- Each tape procedure is a fixed linear network that exchanges two banks of values and restores its scratch values. (on [Linear networks and frames](linear-network-frames.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first input, a binary string of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second input, a binary string of length n.
- $\mathrm{val}$ (binary value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to a fixed length k.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $z$ (integer to encode), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than $2^k$, which is written in binary by the padded representation.
- $\#$ (separator), bound on [Exact integer multiplication](exact-integer-multiplication.md): A separator symbol that marks where the first input ends and the second begins.
- $a$ (first input sequence), bound on [Convolution](convolution.md): The first input sequence, of length n.
- $b$ (second input sequence), bound on [Convolution](convolution.md): The second input sequence, of length n.
- $n$ (sequence length), bound on [Convolution](convolution.md): The number of entries in each input sequence.
- $k$ (output position), bound on [Convolution](convolution.md): The position of an entry of the output sequence c.
- $i$ (input position in a), bound on [Convolution](convolution.md): The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on [Convolution](convolution.md): The position of an entry of b in a product a_i b_j.
- $c$ (convolution), bound on [Convolution](convolution.md): The convolution of a and b, a sequence of length 2n-1.
- $p$ (fractional precision), bound on [Truncation](truncation.md): The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $Q_p$ (truncation to precision p), bound on [Truncation](truncation.md): The operator that truncates each real and imaginary coefficient part of an array toward zero to the grid $2^{-p}\mathbb{Z}$.
- $z$ (input array), bound on [Truncation](truncation.md): An array of complex coefficients that is truncated by $Q_p$.
- $w$ (key width), bound on [Stable radix sort](stable-radix-sort.md): The number of bits in each key.
- $M$ (record count), bound on [Stable radix sort](stable-radix-sort.md): The number of records being sorted.
- $k$ (key), bound on [Stable radix sort](stable-radix-sort.md): The key of a record, written as a string of $w$ bits.
- $i$ (bit index), bound on [Stable radix sort](stable-radix-sort.md): The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $q$ (address before the move), bound on [Destination rank](destination-rank.md): The address of a record before the move.
- $q'$ (address after the move), bound on [Destination rank](destination-rank.md): The address of the same record after the move.
- $\operatorname{rank}$ (stream rank), bound on [Destination rank](destination-rank.md): The position of a record among the records in stream order, written as a function of its address.
- $h$ (chunk index), bound on [Destination rank](destination-rank.md): The index of one of the three address chunks, taking values 1, 2 or 3.
- $q_h$ (current chunk value), bound on [Destination rank](destination-rank.md): The current value of chunk h of the address q.
- $q'_h$ (destination chunk value), bound on [Destination rank](destination-rank.md): The value that chunk h of the address takes after the move.
- $\sigma_h$ (record stride), bound on [Destination rank](destination-rank.md): The amount by which the rank changes when chunk h rises by one with the other chunks fixed.
- $M$ (record count), bound on [Destination rank](destination-rank.md): The number of records in the stream.
- $A_{\mathrm{rect}}$ (integer bit bound), bound on [Destination rank](destination-rank.md): A bit-size bound for the integers the rectangular routine handles.
- $R$ (polynomial ring), bound on [Polynomial ring](polynomial-ring.md): The quotient ring of complex polynomials in y modulo the multiples of f.
- $f$ (modulus polynomial), bound on [Polynomial ring](polynomial-ring.md): The fixed monic polynomial with complex coefficients by which the ring is reduced.
- $m$ (modulus degree), bound on [Polynomial ring](polynomial-ring.md): The degree of f, which is also the number of coefficients in the representative of each element of R.
- $X$ (array of complex values), bound on [Array norm](array-norm.md): A finite array of complex values, the argument of the norm.
- $w$ (array entry), bound on [Array norm](array-norm.md): A single entry of the array X, which is a complex number.
- $\|X\|$ (array norm), bound on [Array norm](array-norm.md): The largest modulus of the entries of the array X, a nonnegative real number.
- $\varphi$ (function being bounded), bound on [Little-o notation](little-o-notation.md): A map from the positive reals to the positive reals, the function that the little-o statement bounds.
- $\psi$ (comparison function), bound on [Little-o notation](little-o-notation.md): A map from the positive reals to the positive reals, positive for all large arguments, against which the function being bounded is compared.
- $\lambda$ (limit variable), bound on [Little-o notation](little-o-notation.md): The real point at which both functions are evaluated, taken to infinity in the limit.
- $\beta$ (first integer), bound on [Coprime](coprime.md): One of the two integers whose greatest common divisor is taken, not both zero.
- $\gamma$ (second integer), bound on [Coprime](coprime.md): The second of the two integers whose greatest common divisor is taken, not both zero.
- $M$ (family size), bound on [Coprime](coprime.md): The number of integers in a family of integers, which counts the members of the family.
- $\lambda_i$ (family member), bound on [Coprime](coprime.md): The i-th integer of a family of integers, for an index i from 1 to M.
- $Q$ (source ring), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring from which the ring homomorphism $\varphi$ starts.
- $Q'$ (target ring), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring into which the ring homomorphism $\varphi$ sends elements of $Q$.
- $\varphi$ (ring homomorphism), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): A map from the ring $Q$ to the ring $Q'$ that preserves sums, products and the identity.
- $\xi$ (ring element), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): An arbitrary element of the source ring $Q$.
- $\eta$ (ring element), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): A second arbitrary element of the source ring $Q$.
- $w$ (indeterminate), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The variable of the example ring $Q=\mathbb{C}[w]/(w^2-1)$, whose square is $1$.
- $\lambda$ (constant coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex coefficient of $1$ in an element $\lambda+\mu w$ of $Q$.
- $\mu$ (linear coefficient), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The complex coefficient of $w$ in an element $\lambda+\mu w$ of $Q$.
- $\psi$ (evaluation at one), bound on [Ring homomorphism and isomorphism](ring-homomorphism.md): The ring homomorphism from $Q$ to $\mathbb{C}$ that sends $w$ to $1$, which is not bijective.
- $u$ (field width), bound on [Address field](address-field.md): The number of address bits in each of the two fields being interchanged, a count.
- $L$ (block length), bound on [Cyclic shift](cyclic-shift.md): The number of positions in the block that a cyclic shift rotates.
- $i$ (position index), bound on [Cyclic shift](cyclic-shift.md): A position in the block, numbered from 0 to L-1.
- $k$ (offset), bound on [Cyclic shift](cyclic-shift.md): The integer, taken modulo L, by which the cyclic shift rotates the block.
- $V$ (stored bit volume), bound on [Cyclic shift](cyclic-shift.md): The number of bits held in the array being shifted.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Array](array.md): A finite collection of entries, each stored at an address and carrying a payload.
  Shown as: Linear algebra basics *<predicate>* Array

## Pages that build on this one

- Linear networks and frames: A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame.
- Eigenvalue: A scalar λ for which a linear operator maps some nonzero vector v to λv.
- Matrix rank: The number of linearly independent rows or columns of a matrix, taken over the rational numbers in the present context.
- Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- Two-point kernel: The two-by-two operator aI + bX, with X the bit flip, applied along one direction of a binary address; its coefficients are Gaussian dyadics.
- Tensor product: The Kronecker product of two matrices, whose m-fold power applies one operator to m independent coordinates at once.
- Bilinear map: A map that is linear in each of two vector arguments separately, such as the product of two polynomials.
- Binary change of basis: An invertible change of basis of the selected address bits over the binary field, realised by row additions on bit positions.
- Bilinear form: A bilinear map from a vector space and itself to its scalars; a space with such a form is nondegenerate when the form has no nonzero vector orthogonal to everything, and two vectors are orthogonal when the form vanishes on them.
- Line spanned by a vector: The set of all scalar multiples of one nonzero vector, a one-dimensional subspace.
- Diagonal scaling: A linear operator that multiplies each coordinate by its own fixed scalar.
- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
- Projection along a subspace: A linear map that keeps the component of a vector in one subspace and removes its component in a complementary subspace.
- Address shear: The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges.
- Linear contraction: A linear map that does not increase the maximum modulus of any vector, so that errors pass through it without growing.

## Other pages you may link to

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

## Evidence from the sources

- "choose an invertible linear operator Dv on the space of arrays indexed by the common address set." (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "the change of representation is the composite operator $D_vD_u^{-1}$" (The page does not define change of representation or show why it equals D_v D_u^{-1}; the reader cannot check the claim from the page.)
- The reader cannot follow this step: "so each such frame has an inverse, as the definition of a frame requires" (The page does not show that a shear of address pairs is invertible, so the reader cannot check that each such frame has an inverse.)
- The reader cannot follow this step: "Such an $S$ is unique" (The page asserts that the inverse is unique but gives no argument, and the reader cannot check it from what is given.)
- Say what $d$ denotes where it is first used (for a size or count, what it counts): "$(c+d)x=cx+dx$" (The page never says what d denotes; it appears only in the axiom (c+d)x=cx+dx, with no sentence introducing it as a scalar.)
- Say what $m$ denotes where it is first used: the page uses it before saying so in "where $m$ is the number of coordinates in each vector."
- Say what $i$ denotes where it is first used (for a size or count, what it counts): "$(Ax)_i=\sum_j A_{ij}x_j$" (Used as an index of the entries of Ax; the page never says what i indexes. The convolution page binds i to a different meaning (input position in a), which does not apply here.)
- Say what $j$ denotes where it is first used (for a size or count, what it counts): "$(Ax)_i=\sum_j A_{ij}x_j$" (Used as a summation index; the page never says what j indexes. The convolution page binds j to a different meaning (input position in b), which does not apply here.)
- Say what $x_j$ denotes where it is first used (for a size or count, what it counts): "$(Ax)_i=\sum_j A_{ij}x_j$" (Subscripted coordinate of x; the page says F^m is the set of m-tuples but never says x_j is the j-th entry of x.)
- Say what $x_1$ denotes where it is first used (for a size or count, what it counts): "$A$ sends $(x_1,x_2)$ to" (Coordinates of the vector (x_1,x_2) in the example; the page never says x_1 denotes the first entry of x.)
- Say what $x_2$ denotes where it is first used (for a size or count, what it counts): "$A$ sends $(x_1,x_2)$ to" (Coordinates of the vector (x_1,x_2) in the example; the page never says x_2 denotes the second entry of x.)
- Say what $\mathrm{id}$ denotes where it is first used: the page uses it before saying so in "where $\mathrm{id}$ sends every vector to itself"
- Say what $D_u$ denotes where it is first used (for a size or count, what it counts): "composite operator $D_vD_u^{-1}$" (By analogy with D_v this should be the frame of vertex u, but the page never says so.)
- Say what $u$ denotes where it is first used (for a size or count, what it counts): "on an edge from $u$ to $v$" (The page never says what u denotes. The address-field page binds u to a field width, which does not fit a vertex here, so that binding does not tell the reader anything about this use.)
- "array" is the concept [Array](array.md), now a prerequisite: link it where the term is used.
- Explain "network, vertex, edge" inline: its concept depends on this page, so it cannot be a prerequisite.
- Explain "logical array and stored array" inline: its concept depends on this page, so it cannot be a prerequisite.
- Explain "shear of address pairs" inline: its concept depends on this page, so it cannot be a prerequisite.

## Previous version (revise it)

It has 463 words. Fix the problems by restructuring rather than appending: keep the rewrite within 578 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

The paper describes its tape procedures with linear algebra: each step applies an invertible linear operator to an array of values, and that operator can be undone exactly. This page defines the vector spaces, linear maps, matrices and inverses that this description uses.

Fix a field $F$, a set with addition and multiplication in which every nonzero element has a multiplicative inverse. Examples are the rational numbers $\mathbb{Q}$, the complex numbers, and the two-element field $\mathbb{F}_2$ of integers modulo 2, whose elements are $0$ and $1$ with $1+1=0$.

A vector space over $F$ is a set of vectors with an addition of vectors and a multiplication of vectors by scalars from $F$, satisfying the usual axioms. Write $x$ and $y$ for vectors and $c$ for a scalar in $F$. The axioms include $c(x+y)=cx+cy$, $(c+d)x=cx+dx$ and $1x=x$. The standard example is $F^m$, the set of $m$-tuples of elements of $F$ with componentwise addition and scalar multiplication, where $m$ is the number of coordinates in each vector.

## Linear maps and matrices

A linear map $T$ from one vector space over $F$ to another satisfies $T(x+y)=Tx+Ty$ and $T(cx)=cT(x)$ for all vectors $x,y$ and scalars $c$. A linear map from a vector space to itself is called an operator.

An $m\times m$ matrix $A$ with entries in $F$ determines a linear map from $F^m$ to itself, sending $x$ to $Ax$, where $(Ax)_i=\sum_j A_{ij}x_j$. Here $I$ is the identity matrix, with ones on the diagonal and zeros elsewhere.

A matrix $A$ is invertible when some matrix $B$ satisfies $AB=BA=I$. For example, over $\mathbb{Q}$ take
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$
$A$ sends $(x_1,x_2)$ to $(x_1+x_2,\,x_2)$, and $AB=BA=I$, so $A$ is invertible with inverse $B$. Over $\mathbb{F}_2$ we have $-1=1$, so the same $A$ satisfies $B=A$ and $A^2=I$. Whether a matrix is invertible depends on the field.

## Invertible operators and inverses

A linear operator $T$ is invertible when some linear map $S$ satisfies $ST=TS=\mathrm{id}$, where $\mathrm{id}$ sends every vector to itself. Such an $S$ is unique and is called the inverse of $T$, written $T^{-1}$. If $T$ is invertible, applying $T$ and then $T^{-1}$ returns every vector to where it started, so no information is lost.

## Use in the paper

In the paper, each vertex $v$ of the network carries a frame $D_v$, an invertible linear operator on arrays. <cite data-source="paper">choose an invertible linear operator Dv on the space of arrays indexed by the common address set.</cite> When the logical array is $g$, the stored array is $D_v g$, and on an edge from $u$ to $v$ the change of representation is the composite operator $D_vD_u^{-1}$. <cite data-source="paper">the operator Dv Du−1 changes the stored array</cite>

Frames can also come from matrices. For a matrix $M$, the frame $\Phi_M$ acts on array entries by a shear of their address pairs. <cite data-source="paper">Hence ΦM is an invertible F2 -linear permutation of array entries</cite>, so each such frame has an inverse, as the definition of a frame requires. The network built from these frames is the subject of [Linear networks and frames](linear-network-frames.md).

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Edge": {
      "additionalProperties": false,
      "description": "What this page uses one prerequisite page for.",
      "properties": {
        "predicate": {
          "description": "A short predicate built from the sentence's own words, such that \"<this page's\nconcept> <predicate> <prerequisite>\" is a true sentence: \"is reduced to\", \"computes\nits transforms by\", \"is based on\".",
          "type": "string"
        },
        "prerequisite": {
          "description": "Id of the prerequisite page.",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on this page that states it, copied exactly. It must link or name the\nprerequisite and contain the predicate's words.",
          "type": "string"
        }
      },
      "required": [
        "prerequisite",
        "predicate",
        "quote"
      ],
      "type": "object"
    },
    "PageBinding": {
      "additionalProperties": false,
      "description": "What a symbol a page introduces denotes, and where the page says so.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on the page that says what the symbol denotes, copied exactly. A use\nin an example (\"take $r = 4$\") does not say what a symbol denotes.",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation",
        "quote"
      ],
      "type": "object"
    },
    "Relation": {
      "oneOf": [
        {
          "const": "direct",
          "description": "The symbol denotes a thing: \"ω, a primitive root of unity\".",
          "type": "string"
        },
        {
          "const": "count",
          "description": "The symbol is the number of instances of something: \"r, the number of complex\ncoefficients in a record\".",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "description": "The structured part of a write answer; the body is the markdown answer file.",
  "properties": {
    "relations": {
      "description": "One relation for each prerequisite page: what this page uses it for. Empty if the\npage has no prerequisite pages.",
      "items": {
        "$ref": "#/$defs/Edge"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol the page binds: each symbol it introduces and says what it denotes.\nLeave out symbols listed as already bound, unless the page gives them a new meaning.\nEmpty if the page introduces no symbols.",
      "items": {
        "$ref": "#/$defs/PageBinding"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "relations"
  ],
  "title": "WriteAnswer",
  "type": "object"
}
```

Write the body to `exegenius/tasks/0264-write-linear-algebra-basics.answer.md` and the JSON to `exegenius/tasks/0264-write-linear-algebra-basics.answer.json`, then run `exegenius submit 0264-write-linear-algebra-basics` in the project directory. If submit rejects the answer, fix the answer and submit again.
