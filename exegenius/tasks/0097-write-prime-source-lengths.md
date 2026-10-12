# exegenius task 0097-write-prime-source-lengths

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
- Transform identity with retained permutations
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

Concept: Prime source lengths
Gloss: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.

## Where the argument relies on this page

- A compatible choice of rational parameters makes every term of the cost table fit the bound of Theorem 1.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder map](chinese-remainder-map.md): A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
  Shown as: Prime source lengths *<predicate>* Chinese-remainder map
- [Gaussian resampling](gaussian-resampling.md): A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
  Shown as: Prime source lengths *<predicate>* Gaussian resampling

## Pages that build on this one

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
- [Signed coefficient packing](signed-packing.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Tensor product](tensor-product.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The distinct prime lengths si must be close to the powers of two ti" (paper)

  > The distinct prime lengths si must be close to the powers of two ti : their product must occupy a fixed fraction of the padded box, while each ratio ti /si must leave enough separation for resampling. We verify both requirements for the parameters just chosen. The prime-interval result [15, Lemma 5.1], based on explicit estimates of Rosser and Schoenfeld [23], gives the following bound: for 0 < η < 1/4 and x > e2/η , the interval (1 − 2η)x < q ≤ (1 − η)x contains at least ηx/(2 log x) primes. Here log is the natural logarithm. The size bounds in (39) give d = Θ(pϵ ) and log r = Θ(p/d). For large n we have d ≥ 2, so 0 < η < 1/4, and log(r/2) = Θ(p1−2ϵ ) −→ ∞. d Thus both x = r/2 and x = r satisfy log x > 8d = 2/η. For either choice, the stated lower bound for the number of primes is x/(8d log x) and exceeds d: indeed, log x = Θ(p1−ϵ ), whereas log(8d2 log x) = O(log p) = o(log x), so x > 8d2 log x eventually. The two intervals are disjoint because (1 − η)r/2 < (1 − 2η)r for η < 1/4, and both intervals lie above 2. We may therefore choose distinct odd primes satisfying (1 − 2η)ti < si ≤ (1 − η)ti . Every gcd(si , ti ) equals one because ti is a power of two. Put S = bounds on si and applying strict Bernoulli inequality gives S 1 > 1− T 2d 


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Such windows contain primes." (The page states that every window of this shape contains a prime, but the only support given is the cited Rosser and Schoenfeld estimate, which the page describes as applying for large t. The reader cannot check from the page that the claim holds for all t, including small ones.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $t$ denotes where it is first used (for a size or count, what it counts): "for large $t$" (The page uses bare t only in the cited estimate and in the example t=16; it never says what t denotes. The earlier bindings of t (indeterminate, sequence length) are not the padded axis length or any clearly matching quantity.)
- Say what $s$ denotes where it is first used (for a size or count, what it counts): "The window is $9.6 < s \le 12.8$" (Bare s appears only in the worked example, where it stands for a candidate prime. The page never says it denotes s_i or any general quantity, so the reader must guess its role.)

## Previous version (revise it)

It has 199 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 249 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Prime source lengths are distinct odd primes, each chosen just below a power of two, so that their product fills a fixed fraction of the padded box. Here $s_i$ is the $i$-th prime source length, an odd prime, and $t_i$ is the $i$-th padded axis length, a power of two. The padded box is the box whose axis lengths are the $t_i$.

Two requirements fix how close $s_i$ must be to $t_i$. First, their product must occupy a fixed fraction of the padded box <cite data-source="paper">their product must occupy a fixed fraction of the padded box</cite>. Second, each ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md), which moves between transforms of length $s_i$ and of length $t_i$.

We use the window
$$(1-2\eta)\,t_i < s_i \le (1-\eta)\,t_i,$$
where $\eta$ is a fixed constant with $0<\eta<1/4$ that sets the window width. Such windows contain primes. A prime-interval estimate due to Rosser and Schoenfeld says that for large $t$ a window of this shape contains many primes <cite data-source="paper">contains at least ηx/(2 log x) primes</cite>. We choose distinct primes from these windows, one per axis.

For example, take $t=16$ and $\eta=1/5$. The window is $9.6 < s \le 12.8$, which contains exactly one prime, $s=11$, and $\gcd(11,16)=1$ because $11$ is odd.

Since the $s_i$ are distinct primes, they are pairwise coprime. Distinct primes give pairwise coprime lengths for the [Chinese-remainder map](chinese-remainder-map.md), which turns one cyclic convolution into a multidimensional one.

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

Write the body to `exegenius/tasks/0097-write-prime-source-lengths.answer.md` and the JSON to `exegenius/tasks/0097-write-prime-source-lengths.answer.json`, then run `exegenius submit 0097-write-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
