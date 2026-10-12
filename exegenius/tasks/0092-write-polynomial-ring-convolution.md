# exegenius task 0092-write-polynomial-ring-convolution

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
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
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

Concept: Convolution over the polynomial ring
Gloss: The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.

## This page in the argument

The step: Convolution on the remaining axes over $\mathbb{C}[y]/(y^r+1)$ is computed by two forward synthetic transforms, a pointwise product, and an opposite transform.
How: forward synthetic transforms that keep frequency order, with polynomial products by signed packing and an established multiplier
Why: Two forward transforms, a pointwise product and an opposite transform reduce the convolution to one pointwise product in the frequency domain, with polynomial products handled by the established multiplier. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The two forward synthetic transforms keep the same frequency order through their pointwise product.
- The polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine. (on [Signed coefficient packing](signed-packing.md))

It serves these steps, from the main result down:

- A deterministic fixed-tape machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, below the $n\lg n$ conjecture in this model.; how: bound the cost of an exact multiplication whose transform layers are made cheap by two tape procedures, then fix parameters so every cost term fits (on [Integer multiplication below n log n](main-theorem.md))
- The exact product of two $n$-bit integers is obtained from the convolution of their radix-digit coefficients, computed by transforms on a fixed tape layout and then recovered and carried.; how: reduce the convolution by a Chinese-remainder map, Gaussian resampling, Bluestein's identity and a phase twist to a convolution over a polynomial ring, then recover coefficients and propagate carries (on [Radix-digit convolution](radix-digit-convolution.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $a$ (numerator real part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer real part of the numerator a + bi of a Gaussian dyadic.
- $b$ (numerator imaginary part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer imaginary part of the numerator a + bi of a Gaussian dyadic.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): A non-negative integer; the denominator of a Gaussian dyadic is the power of two 2^k.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The common length of the two input strings, counting the bits of each input.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length n.
- $\mathrm{val}$ (value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function mapping a binary string to the nonnegative integer whose binary digits it is.
- $k$ (padded width), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary representation, counting leading zeros.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the k-bit binary representation of a number z, padded with leading zeros.
- $n$ (input length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The number of bits in each of the two input integers.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of bits the array stores.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each address field.
- $\tau$ (cost exponent), bound on [Address-field interchange](address-interchange.md): A fixed exponent less than 1 in the cost bound.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first of the two address fields the shear updates, a vector of residues.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second of the two address fields the shear updates, a vector of residues, left unchanged by the shear.
- $n$ (input length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each of the two binary input strings.
- $w$ (block width), bound on [Signed coefficient packing](signed-packing.md): The number of bits reserved for each coefficient in a packed integer.
- $f$ (packed polynomial), bound on [Signed coefficient packing](signed-packing.md): A polynomial with integer coefficients that is packed into an integer.
- $F$ (packed integer of f), bound on [Signed coefficient packing](signed-packing.md): The integer $f(2^w)$ obtained by packing the coefficients of $f$ into blocks of width $w$.
- $g$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): A second polynomial with integer coefficients, multiplied by $f$.
- $G$ (packed integer of g), bound on [Signed coefficient packing](signed-packing.md): The integer $g(2^w)$ obtained by packing the coefficients of $g$ into blocks of width $w$.
- $h$ (product polynomial), bound on [Signed coefficient packing](signed-packing.md): The product $fg$ of the two packed polynomials, whose coefficients the packed product recovers.
- $F$ (fixed bilinear space), bound on [Subspace labels](subspace-labels.md): The fixed vector space carrying the nondegenerate bilinear form, in which all labels are subspaces.
- $U$ (label), bound on [Subspace labels](subspace-labels.md): A nondegenerate subspace of $F$ attached to a wire or an edge of the network.
- $V$ (larger label), bound on [Subspace labels](subspace-labels.md): The label on the edge that contains the smaller label $U$.
- $R$ (orthogonal residual), bound on [Subspace labels](subspace-labels.md): The orthogonal complement of the smaller label inside the larger one, on an edge.
- $s$ (smaller-call count), bound on [Subset-intersection network](subset-intersection-network.md): The total number of smaller calls made by one call of the recursion.
- $W$ (stream shrink factor), bound on [Subset-intersection network](subset-intersection-network.md): The factor by which the volume of each stream shrinks, so each smaller call receives 1/W of the volume.
- $m$ (label space dimension), bound on [Subset-intersection network](subset-intersection-network.md): The dimension of the fixed space from which the subspace labels are drawn.
- $V$ (stored volume), bound on [Rank-saving recursion](rank-saving-recursion.md): The volume of stored data that one call acts on.
- $f$ (recursion parameter), bound on [Rank-saving recursion](rank-saving-recursion.md): The recursion parameter, counting field digits for address interchange or selected axes for a numerical layer.
- $m$ (fixed dimension), bound on [Rank-saving recursion](rank-saving-recursion.md): The dimension of a fixed space, counting its basis vectors.
- $W$ (stream division factor), bound on [Rank-saving recursion](rank-saving-recursion.md): The factor by which each stream's volume is divided.
- $s$ (smaller call count), bound on [Rank-saving recursion](rank-saving-recursion.md): The number of smaller calls that one call makes.
- $a$ (kernel scalar a), bound on [Complex phase network](complex-phase-network.md): One of the two scalars of a two-point kernel $aI+bX$.
- $b$ (kernel scalar b), bound on [Complex phase network](complex-phase-network.md): The other scalar of a two-point kernel $aI+bX$.
- $I$ (identity on two points), bound on [Complex phase network](complex-phase-network.md): The identity map on the two points of a kernel.
- $X$ (two-point swap), bound on [Complex phase network](complex-phase-network.md): The map that swaps the two points of a kernel.
- $t$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries in each of the two sequences, a positive integer.
- $a$ (first input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first sequence of t complex numbers, indexed from 0 to t-1.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second sequence of t complex numbers, indexed from 0 to t-1.
- $i$ (index into a), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of a, ranging over 0 to t-1.
- $j$ (index into b), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of b, ranging over 0 to t-1.
- $k$ (index into c), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of the output sequence c, ranging over 0 to t-1.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The output sequence a \ast b of length t, whose k-th entry is the sum of a_i b_j over all pairs with i+j congruent to k modulo t.
- $q$ (vector length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of entries in a vector, which is the count the transform acts on.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, whose powers weight the entries of the transform.
- $x$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The vector of $q$ complex numbers that the transform takes as input.
- $X$ (transformed vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The vector of $q$ complex numbers that is the discrete Fourier transform of $x$.
- $j$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index running from $0$ to $q-1$ over the input entries $x_j$.
- $k$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index running from $0$ to $q-1$ over the output entries $X_k$.
- $k$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix digits in each input.
- $x_j$ (input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-2^k digit of the first input x, with x_0 the least significant.
- $y_j$ (input digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th radix-2^k digit of the second input y.
- $t$ (indeterminate), bound on [Radix-digit convolution](radix-digit-convolution.md): The variable of the digit polynomials X(t) and Y(t), evaluated at t = 2^k to recover the inputs.
- $c_j$ (convolution coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th coefficient of the product of the digit polynomials, the sum of x_i y_l over all i+l=j.
- $q$ (source transform length), bound on [Gaussian resampling](gaussian-resampling.md): The number of values in one source Fourier transform, which is the count being resampled.
- $r$ (record length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of complex coefficients in a record; it is a power of two.
- $y$ (ring variable), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The variable of the ring $\mathbb{C}[y]/(y^r+1)$, whose powers serve as roots of unity.
- $q$ (transform length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of values in one transform, counted as the number of terms in each sum.
- $\omega$ (synthetic root of unity), bound on [Synthetic polynomial transforms](synthetic-transforms.md): A primitive $q$-th root of unity in the ring, equal to $y^{2r/q}$.
- $y$ (polynomial variable), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The number of complex coefficients in a polynomial record, a power of two.
- $k$ (axis count), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of cyclic axes, that is, of pairwise coprime lengths.
- $m_i$ (axis length), bound on [Chinese-remainder map](chinese-remainder-map.md): The length of the i-th cyclic axis.
- $N$ (position count), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of coefficient positions, the product of the axis lengths.
- $x$ (position), bound on [Chinese-remainder map](chinese-remainder-map.md): A coefficient position in the sequence, an integer with $0 \le x < N$.
- $x'$ (second position), bound on [Chinese-remainder map](chinese-remainder-map.md): A second coefficient position, added to $x$ in the wrap-around argument.
- $q$ (transform length), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): The number of values the transform takes and returns, so q counts the transform's inputs.
- $\omega$ (primitive root), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): A primitive q-th root of unity, whose powers the transform uses.
- $w$ (chirp root), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): A square root of omega, so that w squared equals omega, used to write the powers of omega as chirps.
- $j$ (input index), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): An integer index from 0 to q-1 on the input values.
- $k$ (output index), bound on [Bluestein's chirp identity](bluestein-chirp-identity.md): An integer index from 0 to q-1 on the output values.
- $j$ (coordinate index), bound on [Phase twist](phase-twist.md): The index of a coordinate in a length-$r$ sequence.
- $\theta$ (twist root), bound on [Phase twist](phase-twist.md): A primitive $2r$-th root of unity, so that $\theta^r=-1$, whose powers are the coordinate factors of the twist.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign.
  Shown as: Convolution over the polynomial ring *<predicate>* Polynomial ring modulo y^r + 1
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients.
  Shown as: Convolution over the polynomial ring *<predicate>* Synthetic polynomial transforms
- [Signed coefficient packing](signed-packing.md): Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.
  Shown as: Convolution over the polynomial ring *<predicate>* Signed coefficient packing
- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices wrap around modulo the sequence length.
  Shown as: Convolution over the polynomial ring *<predicate>* Cyclic convolution

## Pages that build on this one

- Exact coefficient recovery: The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
- Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Other pages you may link to

- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Tensor product](tensor-product.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The two forward synthetic transforms retain the same frequency order" (paper)

  > nts this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section 8 retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts. Next, Bluestein’s chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo y r + 1; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established O(n log n) multiplier as an ordinary subroutine. Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section 9 removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below 1/2, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem 1. Figure 1 summarizes these reductions. Integer product radix-digit convolut


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "up to a known scalar normalization" (The page does not state the scalar or where it comes from. The reader cannot check that c equals the stated product up to it, and the only instance (the factor 1/2 in the N = 2 example) is not generalised on the page.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "A transform turns cyclic convolution into entrywise products only if entry $k$ of $F(a)$ and entry $k$ of $F(b)$ belong to the same frequency" (The page asserts an only-if condition relating cyclic convolution to entrywise products, with no argument. The reader cannot check it, and the term frequency (order) is not explained.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "and $G$ reads that order back" (This claim about G's behaviour is not cited and not shown. The definition of G is not given beyond the N = 2 example, so the reader cannot check that G inverts the ordering of F.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $k$ denotes where it is first used (for a size or count, what it counts): "c_k = \sum_{\substack{0 \le i,j < N" (The formula for c_k is the first use of k; the page never says that k indexes the entries of c. The reader can guess this, but nothing on the page states it.)
- Say what $i$ denotes where it is first used (for a size or count, what it counts): "c_k = \sum_{\substack{0 \le i,j < N" (Summation index in the formula for c_k. The page never says what i denotes or ranges over beyond the inequality.)
- Say what $u$ denotes where it is first used (for a size or count, what it counts): "$G(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$" (Dummy arguments of G in the N = 2 example. The page never says that u and v are the two entries of the argument pair.)
- Say what $v$ denotes where it is first used (for a size or count, what it counts): "$G(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$" (Dummy arguments of G in the N = 2 example. The page never says that u and v are the two entries of the argument pair.)
- "cyclic product (cyclic convolution)" is the concept [Cyclic convolution](cyclic-convolution.md), now a prerequisite: link it where the term is used.
- Explain "opposite transform G" in a sentence where it is first used.

## Previous version (revise it)

It has 308 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 385 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Convolution over the polynomial ring is the cyclic product of two arrays of records, and it is the step that computes convolution on the remaining axes by transforms and one pointwise product. Convolution over the polynomial ring takes its records from the [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md).

Let $a = (a_0, \dots, a_{N-1})$ and $b = (b_0, \dots, b_{N-1})$ be arrays of records, where $N$ is the number of records in each array. The convolution is the array $c$ with
$$c_k = \sum_{\substack{0 \le i,j < N \\ i + j \equiv k \pmod{N}}} a_i\, b_j$$
up to a known scalar normalization. Each product $a_i b_j$ is taken in the ring, where wrap-around in the exponent of $y$ flips a sign, while the index sum wraps modulo $N$. Computing $c$ directly takes $N^2$ record products.

Let $F$ be the forward synthetic transform and $G$ the opposite transform, both acting on arrays of $N$ records. Then
$$c = G\big(F(a) \odot F(b)\big),$$
where $\odot$ multiplies entrywise in the ring, and the normalization is applied at the end. Both inputs must be transformed, because the product needs $F(a)$ and $F(b)$ together. The pointwise product needs only $N$ record products.

A transform turns cyclic convolution into entrywise products only if entry $k$ of $F(a)$ and entry $k$ of $F(b)$ belong to the same frequency, and $G$ reads the product back in that order. Here the two forward transforms keep the same frequency order <cite data-source="paper">through their pointwise product</cite>, and $G$ reads that order back.

Take $N = 2$, with root of unity $-1 = y^r$. Then $F(a) = (a_0 + a_1,\ a_0 - a_1)$, and $F(b)$ is the same with $b$. The pointwise product is $\big((a_0+a_1)(b_0+b_1),\ (a_0-a_1)(b_0-b_1)\big)$. The opposite transform $G(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$ gives $c_0 = a_0 b_0 + a_1 b_1$ and $c_1 = a_0 b_1 + a_1 b_0$, which is the cyclic product for $N = 2$.

Multiplying by a power of $y$ is a signed shift of coefficients, so the transforms are cheap. Convolution over the polynomial ring computes its transforms with [Synthetic polynomial transforms](synthetic-transforms.md), so the transforms need only signed shifts and additions.

The pointwise products are polynomial products. Convolution over the polynomial ring computes its products with [Signed coefficient packing](signed-packing.md), which turns each record product into one integer product. That integer product is computed by the [established $O(n\log n)$ multiplier](established-multiplier.md) as an ordinary subroutine.

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

Write the body to `exegenius/tasks/0092-write-polynomial-ring-convolution.answer.md` and the JSON to `exegenius/tasks/0092-write-polynomial-ring-convolution.answer.json`, then run `exegenius submit 0092-write-polynomial-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
