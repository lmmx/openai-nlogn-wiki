# exegenius task 0179-write-packed-bit-addition

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Write for this reader's next uncertainty: at each point, give what they need to follow, and no more. The task lists the step of the argument this page presents, its motivations, and the pages around it. They are material for deciding what to say, not a list to cover: explain the transitions this reader would find hard, and leave familiar ones to ordinary sentences.
- Open with a sentence that says what the concept is and what it is for on the way to the target.
- If the page presents a step of the argument, say how its method shows its claim, and give its main motivation in a sentence. Add another motivation only if the reader would be stuck without it.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, give a relation: the prerequisite's id, a predicate, and the sentence that links or names it, copied exactly. Use the sentence where the page relies on it; do not add a sentence for the purpose. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"), and pick one that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources. The paragraphs around the evidence are given below; read further in the sources only if they are not enough. State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Cite the results and constants a reader may want to check, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them, so the sentence must read complete without the quoted words: write "the cost is $O(n \log n)$ <cite …>…</cite>", not "the paper states the cost as <cite …>…</cite>". Submit rejects a citation right after "that", "as", "states", "says", "is", "gives", "reads" or a colon, and text not found in the named source. Do not cite common background.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: big-O analysis, polynomials and complex numbers, and Turing machines with tapes, plus the discrete mathematics and first linear algebra course that such a degree requires. For the paper this means modular arithmetic, gcd and primes, roots of unity, binary arithmetic over F2 with Hamming weight, and basic vector-space and matrix facts (subspaces, rank, projections, dot product, eigenvalues) at first-course depth. Bilinear forms, tensor products, finite-field and ring theory, the Chinese remainder theorem, Newton iteration and the Fourier and convolution machinery beyond the basics are treated as not known.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model, fixed-tape machine)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transforms)
- Cyclic convolution (also: convolution, normalized cyclic convolution, cyclic product (cyclic convolution))
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Chinese-remainder map (also: Agarwal–Cooley map)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Convolution over the polynomial ring
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
- Simultaneous butterfly layer (also: butterfly layers)
- Guard-width bound
- Transform layout (also: transform layers, selected bits, layouts of the multiplication algorithm)
- Exact coefficient recovery
- Mathematical induction (also: induction, proof by induction, inductive proof)
- Logarithms and floor and ceiling functions (also: floor function, ceiling function, integer part, log base 2, lg)
- Binary representation of integers (also: binary string, bit string, base-2 representation, binary digits, bits)
- Dyadic rationals (also: binary fractions, dyadic numbers)
- Modular arithmetic (also: congruence modulo m, residues modulo m, integers modulo m, remainder arithmetic)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, Euclidean algorithm)
- Prime numbers (also: primes, primality, prime factorization)
- Roots of unity (also: n-th roots of unity, primitive root of unity, unit roots, powers of a root of unity)
- Binary field F2 and XOR arithmetic (also: GF(2), field of two elements, mod-2 arithmetic, exclusive or, XOR, Boolean addition)
- Hamming weight (also: popcount, number of ones, weight of a binary vector, wt(x))
- Vector spaces and subspaces (also: linear subspace, span, basis, linear independence, dimension)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, transpose, identity matrix, linear transformation)
- Matrix rank (also: rank, rank of a linear map, column rank, row rank)
- Projection onto a subspace (also: projection matrix, idempotent linear map, orthogonal projection)
- Dot product and orthogonality (also: inner product, scalar product, orthogonal vectors, perpendicular vectors, orthogonal complement)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, spectrum, characteristic polynomial)
- Bilinear form (also: bilinear space, nondegenerate form)
- Tensor product (also: tensor product of spaces)

## This page

Concept: Packed selected-bit addition
Gloss: An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.

## Where the argument relies on this page

- A compatible choice of rational parameters makes every term of the cost table fit the bound of Theorem 1.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $a$ (real numerator part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer real part of the numerator $a + bi$ of a Gaussian dyadic.
- $b$ (imaginary numerator part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer imaginary part of the numerator $a + bi$ of a Gaussian dyadic.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The non-negative integer exponent that sets the common denominator $2^k$.
- $H_0$ (two-point map), bound on [Gaussian dyadics](gaussian-dyadics.md): The map that sends a pair of coefficients $u$, $v$ to their halved sum and halved difference.
- $u$ (first coefficient), bound on [Gaussian dyadics](gaussian-dyadics.md): The first coefficient of a pair on which the two-point map $H_0$ acts.
- $v$ (second coefficient), bound on [Gaussian dyadics](gaussian-dyadics.md): The second coefficient of a pair on which the two-point map $H_0$ acts.
- $u$ (field size), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of cells in each of two disjoint fields, which counts the cells of a field.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two inputs, the common length of x and y.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary string input, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary string input, of length n.
- $\mathrm{val}$ (binary value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function mapping a binary string to the nonnegative integer whose binary digits it is, leftmost bit most significant.
- $z$ (integer to encode), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than 2^{2n} whose binary representation is taken.
- $\mathrm{bin}$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to a fixed number of bits.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of bits the array stores.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each address field.
- $\tau$ (cost exponent), bound on [Address-field interchange](address-interchange.md): A fixed constant less than 1 in the cost bound $O(V u^{\tau})$.
- $H$ (first address field), bound on [Address shear](address-shear.md): One of the two address fields, a vector of residues that the shear updates.
- $D$ (second address field), bound on [Address shear](address-shear.md): The other address field, a vector of residues that the shear leaves unchanged.
- $n$ (input length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each of the two binary input strings.
- $w$ (block width), bound on [Signed coefficient packing](signed-packing.md): The number of bits given to each coefficient in a packed integer.
- $f$ (polynomial), bound on [Signed coefficient packing](signed-packing.md): A polynomial with integer coefficients, packed into the integer $F$.
- $F$ (packed integer of f), bound on [Signed coefficient packing](signed-packing.md): The integer $f(2^w)$ obtained by packing the coefficients of $f$ into blocks of width $w$.
- $g$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): A second polynomial with integer coefficients, packed into the integer $G$.
- $G$ (packed integer of g), bound on [Signed coefficient packing](signed-packing.md): The integer $g(2^w)$ obtained by packing the coefficients of $g$ into blocks of width $w$.
- $h$ (product polynomial), bound on [Signed coefficient packing](signed-packing.md): The product $fg$ of the two polynomials, whose coefficients are recovered from the product $FG$.
- $U$ (ambient vector space), bound on [Bilinear form](bilinear-form.md): The vector space over F2 on which the bilinear form is defined.
- $B$ (bilinear form), bound on [Bilinear form](bilinear-form.md): The function that takes two vectors of U and returns a scalar, linear in each argument.
- $u$ (first vector), bound on [Bilinear form](bilinear-form.md): A vector of U, the first argument of the form.
- $v$ (second vector), bound on [Bilinear form](bilinear-form.md): A vector of U, the second argument of the form.
- $W$ (subspace), bound on [Bilinear form](bilinear-form.md): A subspace of U whose restricted form is tested for nondegeneracy.
- $u_1$ (first coordinate of u), bound on [Bilinear form](bilinear-form.md): The first coordinate of the vector u in the example.
- $u_2$ (second coordinate of u), bound on [Bilinear form](bilinear-form.md): The second coordinate of the vector u in the example.
- $v_1$ (first coordinate of v), bound on [Bilinear form](bilinear-form.md): The first coordinate of the vector v in the example.
- $v_2$ (second coordinate of v), bound on [Bilinear form](bilinear-form.md): The second coordinate of the vector v in the example.
- $F$ (fixed bilinear space), bound on [Subspace labels](subspace-labels.md): The fixed vector space on which the bilinear form is defined and on which all labels lie.
- $p$ (first vector), bound on [Subspace labels](subspace-labels.md): A vector of F, the first argument of the bilinear form.
- $q$ (second vector), bound on [Subspace labels](subspace-labels.md): A vector of F, the second argument of the bilinear form.
- $L$ (smaller label), bound on [Subspace labels](subspace-labels.md): A nondegenerate subspace of F attached to a wire; on an edge, the label contained in the other.
- $M$ (larger label), bound on [Subspace labels](subspace-labels.md): On an edge, the label that contains the smaller label L.
- $R$ (orthogonal residual), bound on [Subspace labels](subspace-labels.md): On an edge, the subspace of the larger label M orthogonal to the smaller label L.
- $c$ (component in L), bound on [Subspace labels](subspace-labels.md): The part of a vector p in M that lies in the smaller label L.
- $r$ (component in residual), bound on [Subspace labels](subspace-labels.md): The part of a vector p in M that lies in L^perp, and hence in the residual R.
- $m$ (label dimension), bound on [Subset-intersection network](subset-intersection-network.md): The dimension of the fixed space from which the subspace labels are drawn, which counts the vectors in a basis of that space.
- $s$ (smaller-call count), bound on [Subset-intersection network](subset-intersection-network.md): The total number of smaller calls made by one call, which counts the calls on streams of smaller volume.
- $q$ (volume shrink factor), bound on [Subset-intersection network](subset-intersection-network.md): The factor by which the stream volume shrinks in each smaller call.
- $f$ (recursion parameter), bound on [Rank-saving recursion](rank-saving-recursion.md): The recursion parameter: the number of field digits for address interchange, or of selected axes for a numerical layer.
- $P$ (first space), bound on [Tensor product](tensor-product.md): A vector space, the first factor of the tensor product.
- $Q$ (second space), bound on [Tensor product](tensor-product.md): A vector space, the second factor of the tensor product.
- $e$ (basis vector of P), bound on [Tensor product](tensor-product.md): A basis vector of the first factor P, paired with a basis vector f of Q to form a basis vector of the tensor product.
- $f$ (basis vector of Q), bound on [Tensor product](tensor-product.md): A basis vector of the second factor Q, paired with a basis vector e of P to form a basis vector of the tensor product.
- $a$ (kernel scalar a), bound on [Complex phase network](complex-phase-network.md): The first scalar of the two-point kernel $aI+bX$, not the real numerator part of a Gaussian dyadic.
- $b$ (kernel scalar b), bound on [Complex phase network](complex-phase-network.md): The second scalar of the two-point kernel $aI+bX$, not the imaginary numerator part of a Gaussian dyadic.
- $I$ (two-point identity), bound on [Complex phase network](complex-phase-network.md): The identity map on two points, the identity part of the kernel.
- $X$ (two-point swap), bound on [Complex phase network](complex-phase-network.md): The map that swaps the two points, the swap part of the kernel.
- $t$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries in each of the two sequences, a positive integer.
- $a$ (first input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first sequence of t complex numbers, indexed from 0 to t-1.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second sequence of t complex numbers, indexed from 0 to t-1.
- $i$ (index into a), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of a, ranging over 0 to t-1.
- $j$ (index into b), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of b, ranging over 0 to t-1.
- $k$ (index into c), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of the output sequence c, ranging over 0 to t-1.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The output sequence a \ast b of length t, whose k-th entry is the sum of a_i b_j over all pairs with i+j congruent to k modulo t.
- $q$ (vector length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of entries in each vector, a count.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive q-th root of unity, a complex number whose powers are all different from 1 below q.
- $x$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The input vector of q complex numbers, indexed from 0 to q-1.
- $X$ (transform vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform of x, the vector of q outputs computed from x.
- $j$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an input entry, ranging over 0 to q-1.
- $k$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an output entry, ranging over 0 to q-1.
- $i$ (second input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A second index of an input entry, used when the sums are exchanged.
- $m$ (integer exponent), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer whose divisibility by q decides whether the root-of-unity sum vanishes.
- $d$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each digit.
- $L$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each input.
- $x$ (integer x), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer val(x) whose radix-2^d digits are the coefficients x_j.
- $y$ (integer y), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer val(y) whose radix-2^d digits are the coefficients y_j.
- $x_j$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-2^d digit of x, an integer in [0, 2^d).
- $y_j$ (digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-2^d digit of y, an integer in [0, 2^d).
- $j$ (digit index), bound on [Radix-digit convolution](radix-digit-convolution.md): The index of a digit, ranging over 0 to L-1 on this page.
- $i$ (digit index i), bound on [Radix-digit convolution](radix-digit-convolution.md): A digit index used in the convolution sum for the coefficients e_j.
- $l$ (digit index l), bound on [Radix-digit convolution](radix-digit-convolution.md): A digit index used in the convolution sum for the coefficients e_j.
- $T$ (indeterminate), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal variable in which the digit polynomials P and Q are written.
- $P$ (digit polynomial of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in T whose coefficients are the digits of x, so that P(2^d) = x.
- $Q$ (digit polynomial of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in T whose coefficients are the digits of y, so that Q(2^d) = y.
- $e_j$ (convolution coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th coefficient of the product P(T)Q(T), the sum of x_i y_l over i+l=j.
- $r$ (record length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of complex coefficients in a record, a power of two.
- $y$ (ring variable), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The variable of the polynomial ring in which y^r is identified with -1.
- $p$ (input records), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The vector of q records that a transform takes as input.
- $\hat{p}$ (transformed records), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The vector of transformed records, whose entry k is the transform of the input at frequency index k.
- $y$ (polynomial variable), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of complex coefficients in a polynomial record, a power of two.
- $p$ (power exponent), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): A non-negative integer exponent of a power y^p of the indeterminate.
- $K$ (axis count), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of cyclic axes, a count of the axes of the box.
- $M_\nu$ (axis length), bound on [Chinese-remainder map](chinese-remainder-map.md): The length of axis nu, a count of the positions along that axis.
- $\nu$ (axis index), bound on [Chinese-remainder map](chinese-remainder-map.md): The index of an axis, ranging from 1 to K.
- $N$ (position count), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of coefficient positions, the product of the axis lengths.
- $p$ (position), bound on [Chinese-remainder map](chinese-remainder-map.md): A coefficient position, an integer from 0 to N-1.
- $p'$ (second position), bound on [Chinese-remainder map](chinese-remainder-map.md): A second coefficient position, paired with p in a sum.
- $\ell$ (target position), bound on [Chinese-remainder map](chinese-remainder-map.md): The target position of a convolution entry, an integer from 0 to N-1.
- $w$ (half root of unity), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): A complex number whose square is ω.
- $\ell$ (reduced index), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The reduced index (k-j) mod q, an integer from 0 to q-1.
- $p$ (index shift), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): An arbitrary integer shift of the index, used to show the chirp is periodic in q.
- $\theta$ (twist root), bound on [Phase twist](phase-twist.md): A primitive $2r$-th root of unity whose powers are the coordinate factors of the twist.
- $A$ (twisted first input), bound on [Phase twist](phase-twist.md): The polynomial in $y$ obtained from the sequence $a$ by multiplying its $j$-th entry by $\theta^j$.
- $B$ (twisted second input), bound on [Phase twist](phase-twist.md): The polynomial in $y$ obtained from the sequence $b$ by multiplying its $j$-th entry by $\theta^j$.
- $\rho$ (synthetic root of unity), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The root of unity $\rho = y^{2r/q}$ of order $q$, whose powers index the transforms.
- $T$ (forward transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The forward synthetic transform, which maps an array of records to its frequency entries.
- $S$ (opposite transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The opposite synthetic transform, which uses the inverse root and divides by $q$, mapping frequency entries back to records.
- $\ell$ (frequency index), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The index of a frequency, running from 0 to q-1, that labels an entry of a transform.
- $\odot$ (pointwise product), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The entrywise product of two arrays of records in the ring.
- $p$ (index offset), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The offset $i+j-k$ of a pair of indices $(i,j)$ from the target index $k$.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of selected address chunks the layer acts on, at most d, a count.
- $z_0$ (first pair input), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The first input of the pair of coefficients on which the two-point map acts.
- $z_1$ (second pair input), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The second input of the pair of coefficients on which the two-point map acts.
- $z_{00}$ (value at bits 00), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The value at the address whose two selected bits are 00; the other three values are indexed the same way.
- $C$ (two-point kernel), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The complex two-point kernel, a 2 by 2 complex matrix of the form aI + bX.
- $S$ (phase matrix), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal 2 by 2 matrix with diagonal entries 1 and i.
- $S_D$ (address phase map), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal map multiplying the value at each address by i raised to the number of selected bits equal to 1.
- $\beta_D$ (layer scalar), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The scalar factor in the identity between H_0 on D bits and the phased kernel, a power of 1/2 times a fourth root of unity.
- $\lambda'$ (cost exponent), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A fixed exponent below 1 in the layer's cost bound O(V d^{\lambda'}).
- $\ell$ (depth), bound on [Guard-width bound](guard-width-bound.md): The number of elementary operations on the longest chain ending at an intermediate coefficient, a count.
- $C_0$ (first guard constant), bound on [Guard-width bound](guard-width-bound.md): A constant fixed by the network construction, which scales the guard count.
- $C_1$ (guard exponent), bound on [Guard-width bound](guard-width-bound.md): A constant fixed by the network construction, used as the exponent of the chunk count in the guard count.
- $\Delta$ (guard count), bound on [Guard-width bound](guard-width-bound.md): The number of extra guard bits, the ceiling of C_0 d^{C_1}, that bounds every depth.
- $p$ (input fractional bits), bound on [Guard-width bound](guard-width-bound.md): The number of fractional bits in each input coefficient, a count.
- $\alpha$ (first example input), bound on [Guard-width bound](guard-width-bound.md): The first of two example input coefficients, of depth 0.
- $\beta$ (second example input), bound on [Guard-width bound](guard-width-bound.md): The second of two example input coefficients, of depth 0.
- $K$ (chunk width), bound on [Transform layout](transform-layout.md): The number of address bits in one chunk.
- $\nu$ (coefficient index), bound on [Exact coefficient recovery](recovery-and-error.md): The index of a coefficient of the convolution, a position in its output.
- $c_\nu$ (true coefficient), bound on [Exact coefficient recovery](recovery-and-error.md): The true integer value of the convolution coefficient at index nu.
- $\hat c_\nu$ (computed coefficient), bound on [Exact coefficient recovery](recovery-and-error.md): The value the machine computes for the coefficient at index nu, which is only approximately an integer.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time.
  Shown as: Packed selected-bit addition *<predicate>* Simultaneous butterfly layer
- [Address-field interchange](address-interchange.md): A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly.
  Shown as: Packed selected-bit addition *<predicate>* Address-field interchange
- [Address shear](address-shear.md): The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges.
  Shown as: Packed selected-bit addition *<predicate>* Address shear

## Pages that build on this one

- Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Other pages you may link to

- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Tensor product](tensor-product.md)
- [Complex phase network](complex-phase-network.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Packed selected-bit addition on one rectangle" (paper)

  > ess positions in O(V ) time. Each operation uses a fixed number of one-dimensional tapes and restores the order of all spectator fields. The asymptotic simplification in the following lemma describes a fixed family of parameters as p → ∞, after the exponents and comparison constants have been fixed. The statement that R exceeds every fixed polynomial in p means that R/pC → ∞ for each fixed C. Implied constants and eventual cutoffs may depend on the fixed choices and on when the family’s asserted bounds begin to hold. In particular, each explicit bound is uniform over all of its declared inputs; its asymptotic simplification is uniform over the allowed row counts and payloads within a fixed family. Lemma 13 (Packed selected-bit addition on one rectangle). Let R ≥ 1, K ≥ 6, f ≥ 1, L = f K, and 0 ≤ ρ < K. Let N0 , N1 , N2 , N3 be positive integers, and let (χ1 , χ2 , χ3 ) be a permutation of (x, y, z). Consider R-bit records in lexicographic order on [N0 ] × [2L ]χ1 × [N1 ] × [2L ]χ2 × [N2 ] × [2L ]χ3 × [N3 ].


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "So $|Z| \le \delta M$" cites "|B| ≤ δbad M": The quotation bounds |B| by δbad M, a different set (B) with a different fraction (δbad). It says nothing about the exceptional set Z or the fraction δ, so it does not establish |Z| ≤ δM. Say only what the source supports, or cite the passage that supports the claim.
- The quotation does not support the claim it is attached to (unsupported): "The exact map $T$ preserves $Z$" cites "The ideal map T0 preserves all guard values and therefore preserves B": The quotation says the ideal map T0 preserves guard values and therefore B. It does not address the exact map T preserving Z. Say only what the source supports, or cite the passage that supports the claim.
- $L$ means chunk width here, but smaller label on [Subspace labels](subspace-labels.md), which this page builds on: subspace-labels should not use L for a subspace label; L on packed-bit-addition is the chunk width, a bit count equal to mu times K. Use another letter such as W for the label.
- $M$ means record count here, but larger label on [Subspace labels](subspace-labels.md), which this page builds on: subspace-labels should not use M for the larger label; M on packed-bit-addition is the record count. Use another letter such as N for the label.

## Previous version (revise it)

It has 478 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 597 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Packed selected-bit addition is a fixed multitape procedure that performs many binary row additions in one pass, and it supplies the binary basis changes for the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), whose exact computation needs them. Its time bound is one term of the cost table, and a compatible choice of rational parameters makes every term fit the bound of Theorem 1.

A binary row addition XORs one address chunk into another. Here only the selected bit positions change, and the procedure performs all the XORs of one such addition together rather than one bit position at a time.

The record's address is split into three chunks. The procedure XORs selected bits of the source chunk $\xi$ into the target chunk $\eta$, leaving $\zeta$ as it is. Here $\mu$ is the number of selected positions in each chunk, and $\nu$ indexes them. The letter $K$ is the spacing between selected positions here, not the chunk width of the transform layout page. Each chunk has $L$ bits, the chunk width, and $L = \mu K$. The first selected position is at offset $\rho$, with $0 \le \rho < K$, and the $\nu$-th one is $\rho + \nu K$ for $0 \le \nu < \mu$, counted from the least significant bit. The procedure computes

$$\eta_{\rho+\nu K} \leftarrow \eta_{\rho+\nu K} \oplus \xi_{\rho+\nu K} \qquad (0 \le \nu < \mu),$$

where $\eta_{\rho+\nu K}$ and $\xi_{\rho+\nu K}$ are the bits at that position, and $\oplus$ is exclusive or.

For example, take $\mu=2$, $K=6$, $L=12$ and $\rho=1$, so the selected positions are $1$ and $7$. If the $\xi$ bits there are $1$ and $0$, and the $\eta$ bits are $1$ and $1$, the procedure leaves the $\eta$ bits as $0$ and $1$.

Packed selected-bit addition is built from three streaming operations, fixed multitape procedures whose time grows with the volume they process: an [address-field interchange](address-interchange.md) of equal-width chunks, cyclic shifts of chunk ranges, and a fixed permutation of two-bit values. A coordinate range is the finite set of values one address coordinate takes, and a cyclic shift of a chunk range adds an offset, set by the other chunks, to that chunk's value modulo $2^L$. Packed selected-bit addition is a restricted form of the [address shear](address-shear.md) that changes only the selected positions.

Each record has $E$ bits, a count of the bits in one record. Let $\lambda_0,\dots,\lambda_3$ be the sizes of the four other coordinate ranges. Write $M = 2^{3L}\lambda_0\lambda_1\lambda_2\lambda_3$ for the number of records, since each of the three chunks takes $2^L$ values. $V = ME$ is the total number of bits.

The construction first applies a constant number of cyclic shifts, whose composition is $\sigma$. Let $T$ be the exact map that performs the XORs on every record, and let $Z$ be the set of exceptional addresses, where $\sigma$ and $T$ disagree. The fraction $\delta = \min\{1, 80(\mu-1)2^{-K}\}$ is small when $K$ is large. So $|Z| \le \delta M$ <cite data-source="paper">|B| ≤ δbad M</cite>.

The exact map $T$ preserves $Z$ <cite data-source="paper">The ideal map T0 preserves all guard values and therefore preserves B</cite>. Since $T$ preserves $Z$, it also maps addresses outside $Z$ to addresses outside $Z$. As $\sigma$ and $T$ agree outside $Z$ and both are bijections, the correction $T\sigma^{-1}$ fixes every address outside $Z$ and permutes $Z$. Applying the correction after the shifts therefore gives $T$ exactly.

Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$ <cite data-source="paper">When Arect = O(p), R exceeds every fixed polynomial in p, f ≤ d ≤ p, and K/ log p → ∞, this is O(V (Lτ + 1))</cite>, where $\tau$ is the cost exponent of the field interchange.

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

Write the body to `exegenius/tasks/0179-write-packed-bit-addition.answer.md` and the JSON to `exegenius/tasks/0179-write-packed-bit-addition.answer.json`, then run `exegenius submit 0179-write-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
