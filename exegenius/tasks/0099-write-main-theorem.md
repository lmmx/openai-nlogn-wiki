# exegenius task 0099-write-main-theorem

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
- Packed selected-bit addition
- Guard-width bound
- Transform layout (also: transform layers, selected bits, layouts of the multiplication algorithm)
- Prime source lengths
- Transform identity with retained permutations
- Carry propagation
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

Concept: Integer multiplication below n log n
Gloss: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.
Also called: Theorem 1

## This page in the argument

The step: A deterministic fixed-tape machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, below the $n\lg n$ conjecture in this model.
How: bound the cost of an exact multiplication whose transform layers are made cheap by two tape procedures, then fix parameters so every cost term fits
Why: Each transform level scans $\Theta(n)$ stored bits, so the transform layers alone cost $\Theta(n\log n)$; the savings must come from both address movement and arithmetic. (the sources say so: "transform levels already costs Θ(n log n)." (paper))
Striking feature: the logarithmic factor is reduced by a power, $(\lg n)^{1-\kappa}$, so the bound is strictly below $n\lg n$ through all input lengths (explain why it holds, from the method)

Its sub-steps, in order:

- A simultaneous normalized butterfly layer on $d$ selected chunks of stored volume $V$ costs $O(V d^{\lambda'})$. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- Two disjoint equal address fields of $u$ bits in an array of stored volume $V$ can be interchanged in $O(V u^{\tau})$ time. (on [Address-field interchange](address-interchange.md))
- The exact product of two $n$-bit integers is obtained from the convolution of their radix-digit coefficients, computed by transforms on a fixed tape layout and then recovered and carried. (on [Radix-digit convolution](radix-digit-convolution.md))
- A compatible choice of rational parameters makes every term of the cost table fit the bound of Theorem 1.
- The total cost is $O(n(\lg n)^{1-\kappa})$ for every large input, with $\kappa=2^{-182}$.

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
- $a$ (first input array), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The first array of N records, whose entries a_0, ..., a_{N-1} are multiplied in the convolution.
- $b$ (second input array), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The second array of N records, whose entries b_0, ..., b_{N-1} are multiplied in the convolution.
- $N$ (array length), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The number of records in each array, which is the number of index positions the convolution wraps over.
- $c$ (convolution output), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The array of N records whose k-th entry is the cyclic convolution of a and b, up to a known scalar normalization.
- $F$ (forward transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The forward synthetic transform, applied to an array of N records.
- $G$ (opposite transform), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The opposite transform, applied to an array of N records to recover the convolution from the pointwise product.
- $\odot$ (entrywise ring product), bound on [Convolution over the polynomial ring](polynomial-ring-convolution.md): The operation that multiplies two arrays entry by entry, each entry product taken in the polynomial ring.
- $d$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The largest number of equal-width address chunks in which the same bit position is selected.
- $D$ (layer chunk count), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The number of selected address chunks that the layer acts on, at most $d$.
- $V$ (stored volume), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The logical bit volume of the stored array.
- $\lambda'$ (cost exponent), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A fixed exponent below 1 in the layer's cost bound.
- $H_0$ (two-point map), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The map sending a pair $(u,v)$ to $((u+v)/2, (u-v)/2)$.
- $C$ (complex two-point kernel), bound on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The auxiliary complex two-point kernel, a $2\times 2$ complex matrix.
- $p$ (input precision), bound on [Guard-width bound](guard-width-bound.md): The number of fractional bits in each input coefficient.
- $d$ (size parameter), bound on [Guard-width bound](guard-width-bound.md): The size parameter of the network, which bounds the number of selected address bits.
- $C_0$ (network constant), bound on [Guard-width bound](guard-width-bound.md): A constant fixed by the network construction, scaling the depth bound.
- $C_1$ (depth exponent constant), bound on [Guard-width bound](guard-width-bound.md): A constant fixed by the network construction, used as the exponent of the size parameter in the depth bound.
- $\Delta$ (guard count), bound on [Guard-width bound](guard-width-bound.md): The number of extra bits reserved beyond the input precision, per component, so that every intermediate coefficient is exact.
- $K$ (chunk width), bound on [Transform layout](transform-layout.md): The number of address bits in one chunk.
- $k$ (coefficient index), bound on [Exact coefficient recovery](recovery-and-error.md): The index of a coefficient of the convolution.
- $c_k$ (true coefficient), bound on [Exact coefficient recovery](recovery-and-error.md): The true integer coefficient of the convolution at index k.
- $\hat c_k$ (computed coefficient), bound on [Exact coefficient recovery](recovery-and-error.md): The value the machine computes for the coefficient at index k, which is only approximately an integer.
- $x$ (address chunk x), bound on [Packed selected-bit addition](packed-bit-addition.md): One of the three address chunks of a record, named x.
- $y$ (address chunk y), bound on [Packed selected-bit addition](packed-bit-addition.md): One of the three address chunks of a record, named y.
- $z$ (address chunk z), bound on [Packed selected-bit addition](packed-bit-addition.md): One of the three address chunks of a record, named z; the procedure restores it.
- $L$ (chunk width), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each address chunk, with L = fK.
- $f$ (selected positions per chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of selected bit positions in each address chunk.
- $K$ (selected-position spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bit positions between consecutive selected positions.
- $\rho$ (selected-position offset), bound on [Packed selected-bit addition](packed-bit-addition.md): The offset of the first selected position, with 0 ≤ ρ < K.
- $j_i$ (selected bit position), bound on [Packed selected-bit addition](packed-bit-addition.md): The i-th selected bit position, for 0 ≤ i < f, counted from the least significant bit.
- $R$ (record width), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in each record.
- $N_0,\dots,N_3$ (coordinate range sizes), bound on [Packed selected-bit addition](packed-bit-addition.md): The sizes of the four coordinate ranges of the rectangle that are not chunks.
- $M$ (record count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of records in the rectangle, M = 2^{3L} N_0 N_1 N_2 N_3.
- $V$ (bit volume), bound on [Packed selected-bit addition](packed-bit-addition.md): The total number of bits in the rectangle, V = MR.
- $\tau$ (cost exponent), bound on [Packed selected-bit addition](packed-bit-addition.md): A fixed exponent with 0 < τ < 1 in the time bound.
- $\delta_{\text{bad}}$ (correction factor), bound on [Packed selected-bit addition](packed-bit-addition.md): The factor min{1, 80(f−1)2^{−K}} that scales the correction term in the time bound.
- $s_i$ (prime source length), bound on [Prime source lengths](prime-source-lengths.md): The prime source length on axis i, an odd prime chosen close to t_i.
- $t_i$ (padded axis length), bound on [Prime source lengths](prime-source-lengths.md): The padded length of axis i, a power of two.
- $\eta$ (window width parameter), bound on [Prime source lengths](prime-source-lengths.md): A fixed constant with 0 < eta < 1/4 that sets the width of the window for s_i.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The n log n optimality conjecture](n-log-n-conjecture.md): The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers.
  Shown as: Integer multiplication below n log n *<predicate>* The n log n optimality conjecture
- [Fixed-tape machine model](fixed-tape-model.md): A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input.
  Shown as: Integer multiplication below n log n *<predicate>* Fixed-tape machine model
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Integer multiplication below n log n *<predicate>* Radix-digit convolution
- [Chinese-remainder map](chinese-remainder-map.md): A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
  Shown as: Integer multiplication below n log n *<predicate>* Chinese-remainder map
- [Rank-saving recursion](rank-saving-recursion.md): The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
  Shown as: Integer multiplication below n log n *<predicate>* Rank-saving recursion
- [Transform layout](transform-layout.md): A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
  Shown as: Integer multiplication below n log n *<predicate>* Transform layout
- [Transform identity with retained permutations](transform-identity.md): The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
  Shown as: Integer multiplication below n log n *<predicate>* Transform identity with retained permutations
- [Prime source lengths](prime-source-lengths.md): Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.
  Shown as: Integer multiplication below n log n *<predicate>* Prime source lengths
- [Phase twist](phase-twist.md): A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring.
  Shown as: Integer multiplication below n log n *<predicate>* Phase twist
- [Convolution over the polynomial ring](polynomial-ring-convolution.md): The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.
  Shown as: Integer multiplication below n log n *<predicate>* Convolution over the polynomial ring
- [Packed selected-bit addition](packed-bit-addition.md): An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.
  Shown as: Integer multiplication below n log n *<predicate>* Packed selected-bit addition
- [Exact coefficient recovery](recovery-and-error.md): The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
  Shown as: Integer multiplication below n log n *<predicate>* Exact coefficient recovery
- [Carry propagation](carry-propagation.md): Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
  Shown as: Integer multiplication below n log n *<predicate>* Carry propagation

## Other pages you may link to

- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Tensor product](tensor-product.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine A" (paper)

  > Schönhage and Strassen proved in 1971 that two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine, and proposed n log n as the optimal order of growth [25, Section 1]. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional O(n log n) upper bound [15]. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers. For a binary string x of length n, let val(x) be its nonnegative integer value, with the leftmost bit most significant. For 0 ≤ z < 2k , let bink (z) denote its binary representation padded on the left to length k. We consider exact multiplication: on input x#y, with x, y ∈ {0, 1}n , the output must be bin2n (val(x) val(y)). Write lg n = max{⌈log2 n⌉, 1}. Theorem 1. There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every n ≥ 1 and every pair of n-bit inputs. Its worst-case running time satisfies 


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "A compatible choice of fixed rational parameters makes every term of the cost table fit the bound" (The page never shows the cost table, never gives the parameter values, and does not say what 'compatible' requires. The reader cannot check that every term fits the bound, so the claim that the total is O(n(lg n)^{1-kappa}) is not checkable from the page.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "The factor $(\lg n)^{-\kappa}$ is below $1$ whenever $n\ge 3$, because then $\lg n\ge 2$." (The stated justification fails: lg 3 is about 1.58, which is less than 2. lg n >= 2 holds only for n >= 4. The conclusion (lg n)^{-kappa} < 1 still holds for n >= 3 because lg n > 1 there, but the page's reason does not establish it.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "The savings must come from both movement and arithmetic, so two tape procedures are used." (This is a design claim presented as following ('must', 'so') with no citation and no argument on the page. The reader cannot check why the savings must come from both sources or why exactly two procedures are needed.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.

## Previous version (revise it)

It has 333 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 416 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Write $n$ for the number of bits in each input. The constant $\kappa=2^{-182}$ is a fixed positive number. Integer multiplication below $n\lg n$ is the main theorem: a single deterministic Turing machine that runs in the [fixed-tape machine model](fixed-tape-model.md) multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time.

The bound refutes the [n log n optimality conjecture](n-log-n-conjecture.md) in this model, since $n(\lg n)^{1-\kappa}$ is of strictly smaller order than $n\lg n$. The factor $(\lg n)^{-\kappa}$ is below $1$ whenever $n\ge 3$, because then $\lg n\ge 2$.

The transform layers are the obstacle. <cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> The savings must come from both movement and arithmetic, so two tape procedures are used.

Here $V$ is the stored volume, the number of stored bits in the array. Here $u$ is the width in bits of each address field. The first procedure interchanges two disjoint equal address fields of $u$ bits in an array of stored volume $V$, at cost $O(Vu^{\tau})$, where $\tau$ is a fixed exponent below $1$. <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite>

The second applies a [simultaneous butterfly layer](simultaneous-butterfly-layer.md) to $d$, the number of selected chunks, at cost $O(Vd^{\lambda'})$, where $\lambda'$ is a fixed exponent below $1$.

Multiplication is reduced to the [radix-digit convolution](radix-digit-convolution.md) of the two integers' digit coefficients. On the tapes, it computes its transforms on a [transform layout](transform-layout.md) that places the selected bits of each axis at a common offset. It relabels its axis positions by the [Chinese-remainder map](chinese-remainder-map.md), and its movement is organized by [rank-saving recursion](rank-saving-recursion.md). The transform identity is based on the [transform identity with retained permutations](transform-identity.md), so permutations cancel instead of being sorted. It chooses its source lengths as [prime source lengths](prime-source-lengths.md). It converts the last cyclic coordinate by a [phase twist](phase-twist.md), and its records are multiplied by [convolution over the polynomial ring](polynomial-ring-convolution.md). It adds selected bits with [packed selected-bit addition](packed-bit-addition.md).

It recovers its coefficients by [exact coefficient recovery](recovery-and-error.md), which rounds them to integers. After this, the result ends with [carry propagation](carry-propagation.md).

A compatible choice of fixed rational parameters makes every term of the cost table fit the bound, so the total cost is $O(n(\lg n)^{1-\kappa})$ for every large input.

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

Write the body to `exegenius/tasks/0099-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0099-write-main-theorem.answer.json`, then run `exegenius submit 0099-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
