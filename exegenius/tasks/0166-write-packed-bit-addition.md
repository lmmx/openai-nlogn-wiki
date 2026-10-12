# exegenius task 0166-write-packed-bit-addition

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
- $F$ (fixed bilinear space), bound on [Subspace labels](subspace-labels.md): The fixed bilinear space on which all subspace labels are based.
- $x$ (first argument), bound on [Subspace labels](subspace-labels.md): A vector of F, the first argument of the bilinear form.
- $y$ (second argument), bound on [Subspace labels](subspace-labels.md): A vector of F, the second argument of the bilinear form.
- $U$ (label), bound on [Subspace labels](subspace-labels.md): A nondegenerate subspace of F, the label attached to a wire.
- $U^{\perp}$ (orthogonal complement), bound on [Subspace labels](subspace-labels.md): The set of vectors of F orthogonal to every vector of U.
- $V$ (larger label), bound on [Subspace labels](subspace-labels.md): The larger of the two labels on an edge, containing the smaller label U.
- $R$ (orthogonal residual), bound on [Subspace labels](subspace-labels.md): The orthogonal residual of an edge, the orthogonal complement of the smaller label inside the larger one.
- $m$ (label space dimension), bound on [Subset-intersection network](subset-intersection-network.md): The dimension of the fixed space from which the subspace labels are drawn, a count of its basis vectors.
- $s$ (smaller call count), bound on [Subset-intersection network](subset-intersection-network.md): The total number of smaller calls made by one call, a count.
- $W$ (volume shrink factor), bound on [Subset-intersection network](subset-intersection-network.md): The factor by which the stream volume shrinks, so each smaller call works on a stream of 1/W of the volume.
- $f$ (recursion parameter), bound on [Rank-saving recursion](rank-saving-recursion.md): The recursion parameter: the number of field digits for address interchange, or of selected axes for a numerical layer.
- $P$ (first space), bound on [Tensor product](tensor-product.md): A vector space, the first factor of the tensor product.
- $Q$ (second space), bound on [Tensor product](tensor-product.md): A vector space, the second factor of the tensor product.
- $e$ (basis vector of P), bound on [Tensor product](tensor-product.md): A basis vector of the first factor P, paired with a basis vector f of Q to form a basis vector of the tensor product.
- $f$ (basis vector of Q), bound on [Tensor product](tensor-product.md): A basis vector of the second factor Q, paired with a basis vector e of P to form a basis vector of the tensor product.
- $I$ (two-point identity), bound on [Complex phase network](complex-phase-network.md): The identity map on two points, a 2 by 2 identity matrix.
- $X$ (two-point swap), bound on [Complex phase network](complex-phase-network.md): The swap of the two points, a 2 by 2 swap matrix.
- $a$ (kernel scalar a), bound on [Complex phase network](complex-phase-network.md): The coefficient of the identity in a two-point kernel $aI+bX$.
- $b$ (kernel scalar b), bound on [Complex phase network](complex-phase-network.md): The coefficient of the swap in a two-point kernel $aI+bX$.
- $i$ (imaginary unit), bound on [Complex phase network](complex-phase-network.md): The imaginary unit, with i squared equal to -1.
- $H_0$ (two-point map), bound on [Complex phase network](complex-phase-network.md): The map sending two inputs to their average and half their difference, applied to selected address bits.
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
- $d$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each radix-2^d digit.
- $L$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix-2^d digits in each input.
- $x_j$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-2^d digit of x, an integer in [0, 2^d), with index 0 the least significant.
- $y_j$ (digit of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-2^d digit of y, defined in the same way as the digits of x.
- $t$ (indeterminate), bound on [Radix-digit convolution](radix-digit-convolution.md): The indeterminate of the digit polynomials P(t) and Q(t).
- $P$ (digit polynomial of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in t whose coefficients are the digits x_j of x.
- $Q$ (digit polynomial of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in t whose coefficients are the digits y_j of y.
- $e_j$ (convolution coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th coefficient of the product P(t)Q(t), the convolution of the two digit lists.
- $r$ (record length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of complex coefficients in a record, a power of two.
- $y$ (ring variable), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The variable of the ring C[y]/(y^r+1), where y^r equals -1; the letter changes meaning from the multiplication page's second input.
- $a$ (input records), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The input vector of q records a_0 through a_{q-1}; the letter changes meaning from the cyclic convolution page.
- $\hat a$ (transformed record), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The transformed record at frequency index j, the output of the transform.
- $y$ (polynomial variable), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of complex coefficients in a polynomial record, a power of two.
- $k$ (power exponent), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The exponent of a power y^k, a non-negative integer.
- $d$ (number of axes), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of cyclic axes, a count of the lengths m_i.
- $m_i$ (axis length), bound on [Chinese-remainder map](chinese-remainder-map.md): The length of the i-th cyclic axis, a count of the positions along that axis.
- $N$ (number of positions), bound on [Chinese-remainder map](chinese-remainder-map.md): The product of the axis lengths, counting the coefficient positions.
- $x$ (position), bound on [Chinese-remainder map](chinese-remainder-map.md): A coefficient position, an integer from 0 to N-1.
- $x'$ (second position), bound on [Chinese-remainder map](chinese-remainder-map.md): A second coefficient position, added to x.
- $z$ (target position), bound on [Chinese-remainder map](chinese-remainder-map.md): The position of the convolution output whose sum is being formed.
- $w$ (half-angle root of unity), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The complex number $e^{\pi i/q}$, whose square is the root of unity $\omega$.
- $t$ (reduced index), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The index $(k-j) \bmod q$ in $\{0,\ldots,q-1\}$ at which the chirp sequence $b$ is evaluated.
- $\theta$ (twist root), bound on [Phase twist](phase-twist.md): A primitive $2r$-th root of unity whose powers are the coordinate factors of the twist.
- $A$ (twisted first input), bound on [Phase twist](phase-twist.md): The polynomial in $y$ obtained from the sequence $a$ by multiplying its $j$-th entry by $\theta^j$.
- $B$ (twisted second input), bound on [Phase twist](phase-twist.md): The polynomial in $y$ obtained from the sequence $b$ by multiplying its $j$-th entry by $\theta^j$.
- $N$ (record count), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The number of records in each of the two arrays, so each array has N entries.
- $F$ (forward transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The forward synthetic transform, whose entry m is the sum of a_j omega^{jm} over the input records.
- $G$ (opposite transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The opposite transform, which uses the inverse root omega^{-1} in place of omega and divides by N.
- $\odot$ (entrywise ring product), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The product that multiplies two arrays of records entry by entry in the ring.
- $d$ (chunk count bound), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The maximum number of equal-width address chunks that carry the selected bit position.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of selected address chunks the layer acts on, with $1 \le D \le d$.
- $H_0$ (two-point map), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The normalized two-point map sending a pair $(u,v)$ to $((u+v)/2, (u-v)/2)$.
- $u$ (first input), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The first value of the pair that the two-point map takes as input.
- $v$ (second input), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The second value of the pair that the two-point map takes as input.
- $C$ (complex two-point kernel), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The $2\times 2$ complex matrix $aI + bX$ whose tensor powers the phase network realizes.
- $S$ (diagonal phase), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal $2\times 2$ matrix with diagonal entries $1$ and $i$, a phase.
- $S_D$ (selected-bit phase), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The diagonal phase on the $D$ selected bits, multiplying the value at an address by $i$ raised to its number of selected bits equal to 1.
- $\beta_D$ (dyadic scale), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The scalar in the identity for the $D$-bit layer, a power of one half times a fourth root of unity, with at most one further factor $b$.
- $\lambda'$ (cost exponent), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A fixed exponent below 1 in the layer's cost bound.
- $z$ (example values), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The stored values in the $D=2$ example, indexed by the two selected bits.
- $p$ (fractional bit count), bound on [Guard-width bound](guard-width-bound.md): The number of fractional bits in each input coefficient.
- $\ell$ (depth), bound on [Guard-width bound](guard-width-bound.md): The depth of a value, the number of operations on its longest chain from an input coefficient.
- $C_0$ (network constant C0), bound on [Guard-width bound](guard-width-bound.md): A constant fixed by the network construction, multiplying the power of d in the guard count.
- $C_1$ (network exponent C1), bound on [Guard-width bound](guard-width-bound.md): A constant fixed by the network construction, used as the exponent of d in the guard count.
- $\Delta$ (guard count), bound on [Guard-width bound](guard-width-bound.md): The guard count, the number of extra bits, which bounds the depth of every intermediate coefficient.
- $u$ (first example input), bound on [Guard-width bound](guard-width-bound.md): The first of two input coefficients in the worked example, with depth 0.
- $v$ (second example input), bound on [Guard-width bound](guard-width-bound.md): The second of two input coefficients in the worked example, with depth 0.
- $K$ (chunk width), bound on [Transform layout](transform-layout.md): The number of address bits in one chunk.
- $k$ (coefficient index), bound on [Exact coefficient recovery](recovery-and-error.md): The index of a coefficient of the convolution.
- $c_k$ (true coefficient), bound on [Exact coefficient recovery](recovery-and-error.md): The true integer coefficient of the convolution at index k.
- $\hat c_k$ (computed coefficient), bound on [Exact coefficient recovery](recovery-and-error.md): The value the machine computes for the coefficient at index k, which is only approximately an integer.

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

- $x$ means source chunk here, but input vector on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Discrete-Fourier-transform page: x is an input vector of complex numbers, whereas on the packed-bit-addition page x is an address chunk. Use another letter for the chunk.
- $x$ means source chunk here, but first argument on [Subspace labels](subspace-labels.md), which this page builds on: Subspace-labels page: x is a vector of F, whereas on the packed-bit-addition page x is an address chunk. Use another letter for the chunk.
- $y$ means target chunk here, but second argument on [Subspace labels](subspace-labels.md), which this page builds on: Subspace-labels page: y is a vector of F, whereas on the packed-bit-addition page y is an address chunk. Use another letter for the chunk.
- $z$ means temporary chunk here, but example values on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md), which this page builds on: Simultaneous-butterfly page: z is a list of stored values, whereas on the packed-bit-addition page z is an address chunk. Use another letter for the chunk.
- $f$ means selected count here, but basis vector of Q on [Tensor product](tensor-product.md), which this page builds on: Tensor-product page: f is a basis vector of Q, whereas on the packed-bit-addition page f is a count of selected positions. Use another letter for the count.
- $i$ means selected index here, but second input index on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Discrete-Fourier-transform page: i indexes input entries, whereas on the packed-bit-addition page i indexes selected bit positions. Use another letter (for example s) for the selected index.
- $i$ means selected index here, but index into a on [Cyclic convolution](cyclic-convolution.md), which this page builds on: Cyclic-convolution page: i indexes entries of a, whereas on the packed-bit-addition page i indexes selected bit positions. Use another letter (for example s) for the selected index.
- $i$ means selected index here, but imaginary unit on [Complex phase network](complex-phase-network.md), which this page builds on: Complex-phase page: i is the imaginary unit, whereas on the packed-bit-addition page i is a selected index. Use another letter (for example s) for the selected index.
- $R$ means record bit count here, but orthogonal residual on [Subspace labels](subspace-labels.md), which this page builds on: Subspace-labels page: R is an orthogonal residual, whereas on the packed-bit-addition page R is a record bit count. Use another letter for the bit count.
- $B$ means exceptional set here, but bilinear form on [Bilinear form](bilinear-form.md), which this page builds on: Bilinear-form page: B is a bilinear form function, whereas on the packed-bit-addition page B is an exceptional address set. Use another letter for the set.

## Previous version (revise it)

It has 437 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 546 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Packed selected-bit addition is a fixed multitape procedure that performs many binary row additions in one pass. Packed selected-bit addition supplies the binary basis changes for the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), whose exact computation needs them.

A binary row addition adds one row of a matrix into another in every column, so it changes the selected bits of two whole address chunks at once. The procedure performs all the XORs of one such addition together rather than one bit position at a time.

The record's address is split into three chunks named $x$, $y$, and $z$; here these letters name chunks, so $y$ no longer means the polynomial variable. Here $f$ is the number of selected positions in each chunk. $K$ is the spacing between them, not the chunk width used on the transform layout page. Each chunk has $L$ bits, the chunk width, with $L = fK$.

The selected positions start at offset $\rho$, with $0 \le \rho < K$. Here $i$ indexes selected positions, not the convolution indices of earlier pages. The $i$-th selected position is $j_i = \rho + iK$ for $0 \le i < f$, counted from the least significant bit. The procedure computes

$$y_{j_i} \leftarrow y_{j_i} \oplus x_{j_i} \qquad (0 \le i < f),$$

so the selected bits of $x$ are XORed into the same positions of $y$, where $\oplus$ is exclusive or.

For example, take $f=2$, $K=6$, $L=12$ and $\rho=1$, so $j_0=1$ and $j_1=7$. If the $x$ bits there are $1$ and $0$, and the $y$ bits are $1$ and $1$, the procedure leaves the $y$ bits as $0$ and $1$.

Packed selected-bit addition is built from three streaming operations: an [address-field interchange](address-interchange.md) of equal-width chunks, cyclic shifts of chunk ranges, and a fixed permutation of two-bit values. A streaming operation is a fixed multitape procedure whose time grows with the volume it processes. A coordinate range is the finite set of values one address coordinate takes, and a cyclic shift of a chunk range adds an offset, set by the other chunks, to that chunk's value modulo $2^L$. Packed selected-bit addition is a restricted form of the [address shear](address-shear.md) that changes only the selected positions.

Each record has $R$ bits, a bit count, not the orthogonal residual $R$ of earlier pages. Let $N_0,\dots,N_3$ be the sizes of the four other coordinate ranges, so $M = 2^{3L}N_0N_1N_2N_3$ counts the records, and $V = MR$ is the total number of bits.

The construction first applies a constant number of cyclic shifts, whose composition is $S_0$. Outside a set $B$ of exceptional addresses, $S_0$ agrees with the exact map $T_0$ that performs the XORs. The fraction $\delta_{\text{bad}} = \min\{1, 80(f-1)2^{-K}\}$ is small when $K$ is large. The exceptions are few: $|B| \le \delta_{\text{bad}} M$ <cite data-source="paper">|B| ≤ δbad M</cite>.

The exact map $T_0$ preserves $B$ <cite data-source="paper">The ideal map T0 preserves all guard values and therefore preserves B</cite>. Since $S_0$ and $T_0$ agree outside $B$ and both are bijections, $T_0S_0^{-1}$ fixes every address outside $B$ and permutes $B$. Applying this correction after the shifts therefore gives $T_0$ exactly.

Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$ <cite data-source="paper">When Arect = O(p), R exceeds every fixed polynomial in p, f ≤ d ≤ p, and K/ log p → ∞, this is O(V (Lτ + 1))</cite>.

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

Write the body to `exegenius/tasks/0166-write-packed-bit-addition.answer.md` and the JSON to `exegenius/tasks/0166-write-packed-bit-addition.answer.json`, then run `exegenius submit 0166-write-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
