# exegenius task 0100-write-crt-map

Project directory: `/home/user/e2e-run` (paths below are relative to it)

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
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model (also: multitape Turing machine, fixed-tape model)
- Elementary stream operations
- Controlled shifts and rational scalings
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform (also: transform levels)
- Multidimensional transforms
- Bluestein chirp identity (also: chirp transform)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Two-point kernel C (also: phase network kernel)
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba, O(n^2) multiplication, n^{log_2 3} multiplication)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Binary and radix representation (also: base-b digits, positional notation, binary expansion, bit string, most significant bit, padding with leading zeros, carry propagation)
- Two's complement integers (also: two's-complement, signed binary integers, signed fixed-width addition)
- Bitwise XOR and arithmetic mod 2 (also: XOR, exclusive or, addition in F_2, GF(2), parity, bit flip)
- Logarithms and floors/ceilings (also: lg, log base 2, ceiling, floor, iterated logarithm, log log n)
- Modular arithmetic and primes (also: congruence, residues mod n, gcd, coprime, relatively prime, prime numbers, Z/nZ, modular inverse, units mod n)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n}, Euler's formula)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, basis, span, linear independence, dimension, matrix rank, kernel, linear map, linear operator, direct sum)
- Matrices and linear operators (also: matrix multiplication, invertible matrix, matrix inverse, identity matrix, commuting operators, diagonal matrix, triangular matrix, lower triangular, permutation matrix)
- Gaussian elimination and triangular factorization (also: row reduction, LU decomposition, back substitution)
- Orthogonality and inner products (also: orthonormal basis, dot product, orthogonal complement, bilinear form, nondegenerate form, Euclidean norm)
- Norms and the triangle inequality (also: sup norm, max norm, infinity norm, modulus bounds, absolute value bounds)
- Permutations and bijections (also: permutation of indices, sorting a permutation, bit-reversal permutation, bijective map, inverse permutation)
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape, rectangle, columns)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)
- Contractions and bilinear contractions (also: contraction, bilinear contraction)

## This page

Concept: Chinese-remainder address map
Gloss: An isomorphism that places a cyclic convolution of length S = s₁⋯s_d on pairwise coprime prime axes, implemented as triangular controlled shifts.
Also called: Agarwal–Cooley map

## This page in the argument

The step: The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod_ix_i^{\mu_i}$, is an isomorphism preserving cyclic convolution, and it (with its inverse and padding) is implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^\tau))$ time.
How: Choose the exponents $\mu_i=P_i^{-1}\bmod s_i$ so that the coordinate of a coefficient index in axis $i$ is $a_i+\mu_i\sum_{j<i}a_jP_j$, i.e. it depends only on lower-index digits: a triangular system implemented as prefix-controlled cyclic shifts in descending axis order after reversing the axis order.
Why: A triangular dependence means each target axis is updated from controls that precede it on tape, so each update is a controlled cyclic shift of linear cost (Lemma on controlled shifts); the only expensive part is reordering the axes, which uses the fast chunk interchange. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Let $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\pmod{s_i}$.
- Define $\Phi:x\mapsto\prod_ix_i^{\mu_i}$; it respects $x^S=1$ and so defines an algebra map.
- The image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target monomials exactly once; hence $\Phi$ is an isomorphism preserving cyclic convolution.
- With the mixed-radix expression $k=\sum_ja_jP_j$, the axis-$i$ coordinate of $\Phi(x^k)$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$.
- Terms with $j>i$ vanish modulo $s_i$ (divisible by $s_i$) and $\mu_iP_i=1$ modulo $s_i$, which gives the formula.
- After reordering the padded axes to $(a_1,\dots,a_d)$ update the targets in the order $i=d,d-1,\dots,1$, so lower-index controls have not yet changed; each update is a prefix-controlled cyclic shift of the valid interval $[0,s_i)$ with identity on $[s_i,t_i)$, so zero padding stays zero.
- Reordering uses $O(d^2)$ axis moves, each an equal-width chunk interchange (plus a fixed number of linear passes for a one-bit difference), so the map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$.; how: Reduce the integer product to a cyclic convolution of $S$ short coefficients and compute it through the chain of reductions (digits, CRT address map, Gaussian resampling with chirps, twist to the polynomial ring, synthetic-transform convolution); recover exact integers because the accumulated error is below $1/2$. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.3.1, S5.3.2, S5.3.3, S5.3.4, S5.3.5, S5.3.6, S5.3.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.3.1**: Let $P_i=\prod_{j<i}s_j$ and $\mu_i=P_i^{-1}\pmod{s_i}$.
Source: "P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}." (paper)
> Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.

**S5.3.2**: Define $\Phi:x\mapsto\prod_ix_i^{\mu_i}$; it respects $x^S=1$ and so defines an algebra map.
Source: "\qquad x\longmapsto\prod_i x_i^{\mu_i}" (paper)
> Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.

**S5.3.3**: The image of $x$ has order $S$ because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime, so its powers run through all target monomials exactly once; hence $\Phi$ is an isomorphism preserving cyclic convolution.
Source: "group has size $S$, and the image of $x$ has order $S$, because each" (paper)
> Let $s_1,\ldots,s_d$ be the pairwise coprime source lengths, let $S=\prod_i s_i$, and put \[ P_i=\prod_{j<i}s_j,\qquad \mu_i=P_i^{-1}\pmod{s_i}. \] Here $P_i$ denotes an integer prefix product, not a Fourier-coordinate permutation. The assignment \[ \Phi:\mathbb C[x]/(x^S-1)\longrightarrow \mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1), \qquad x\longmapsto\prod_i x_i^{\mu_i} \] respects $x^S=1$, so it defines an algebra map. The target monomial group has size $S$, and the image of $x$ has order $S$, because each $\mu_i$ is a unit and the $s_i$ are pairwise coprime. Its powers therefore run through all target basis monomials exactly once. Hence $\Phi$ is an isomorphism and preserves cyclic convolution.

**S5.3.4**: With the mixed-radix expression $k=\sum_ja_jP_j$, the axis-$i$ coordinate of $\Phi(x^k)$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$.
Source: "b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}." (paper)
> Every ordinary coefficient index has a unique mixed-radix expression \[ k=\sum_{j=1}^d a_jP_j,\qquad 0\le a_j<s_j. \] The coordinate of $\Phi(x^k)$ in axis $i$ is \begin{equation}\label{eq:triangular-crt} b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}. \end{equation} Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo $s_i$. Numerical order of $k$ is lexicographic order of $(a_d,\ldots,a_1)$. Insert the padding in one nested scan of the full box $\prod_i[0,t_i)$ in this lexicographic order, with $a_d$ the outermost counter and $a_1$ the innermost. At an address satisfying $a_i<s_i$ for every $i$, copy the next original coefficient record; at every other address, write a zero record. The valid addresses occur in the original coefficient order, so each record is copied to its intended mixed-radix address. To delete the padding after the inverse axis reorder, use the same enumeration, copying the record at each valid address and skipping the record at each invalid address.

**S5.3.5**: Terms with $j>i$ vanish modulo $s_i$ (divisible by $s_i$) and $\mu_iP_i=1$ modulo $s_i$, which gives the formula.
Source: "Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo" (paper)
> Every ordinary coefficient index has a unique mixed-radix expression \[ k=\sum_{j=1}^d a_jP_j,\qquad 0\le a_j<s_j. \] The coordinate of $\Phi(x^k)$ in axis $i$ is \begin{equation}\label{eq:triangular-crt} b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}. \end{equation} Indeed terms with $j>i$ are divisible by $s_i$, and $\mu_iP_i=1$ modulo $s_i$. Numerical order of $k$ is lexicographic order of $(a_d,\ldots,a_1)$. Insert the padding in one nested scan of the full box $\prod_i[0,t_i)$ in this lexicographic order, with $a_d$ the outermost counter and $a_1$ the innermost. At an address satisfying $a_i<s_i$ for every $i$, copy the next original coefficient record; at every other address, write a zero record. The valid addresses occur in the original coefficient order, so each record is copied to its intended mixed-radix address. To delete the padding after the inverse axis reorder, use the same enumeration, copying the record at each valid address and skipping the record at each invalid address.

**S5.3.6**: After reordering the padded axes to $(a_1,\dots,a_d)$ update the targets in the order $i=d,d-1,\dots,1$, so lower-index controls have not yet changed; each update is a prefix-controlled cyclic shift of the valid interval $[0,s_i)$ with identity on $[s_i,t_i)$, so zero padding stays zero.
Source: "order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}.  When target" (paper)
> Now reorder the complete padded axes to $(a_1,\ldots,a_d)$. In this physical order, the coordinates with indices below $i$ precede coordinate $i$. Update the targets in the order $i=d,d-1,\ldots,1$ using \eqref{eq:triangular-crt}. When target $i$ is updated, none of its lower-index controls has yet changed, so the offset is computed from the original digits $a_j$ required by the formula.

**S5.3.7**: Reordering uses $O(d^2)$ axis moves, each an equal-width chunk interchange (plus a fixed number of linear passes for a one-bit difference), so the map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$.
Source: "O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)." (paper)
> The axis widths are $\ell$ or $\ell-1$. To exchange two adjacent axes of unequal width, move the longer axis's leading bit outside their equal-width pair, swap that pair by the proved chunk-swap procedure, and put the leading bit at its new position. This adds a fixed number of linear passes to the equal-width swap cost. Reversing all axes uses $O(d^2)$ such moves. Therefore the map $\Phi$, its inverse, and their padding operations cost \[ O\bigl(Tp\,d^2(1+\ell^\tau)\bigr). \] This construction describes payload movement from address $a$ to its new address. It is distinct from the operator convention $(R_cz)_j=z_{cj}$ used for Fourier dilations, which moves a payload from address $j$ to $c^{-1}j$.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials, satisfying y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm in the running time is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations applied since the layer began.
- $\Delta$ (extra reserved bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the number of operations charged to the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set $[h]$ whose three-element subsets index the banks.
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of $[h]$.
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every wire's array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network obtained by applying every scalar gate pointwise at each address, acting on all wire arrays together.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): An invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $D_{\rm in}$ (input frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the source frames over the input roles.
- $D_{\rm out}$ (output frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the sink frames over the output roles.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role to its output role in a signed role permutation.
- $\varepsilon_w$ (route sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign of the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of axis i of the array.
- $M$ (cyclic addresses), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses on the first d-1 axes, the product of t_i for i<d.
- $T$ (total coefficients), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array, rM.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $n$ (input bit length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in each input.
- $b$ (digit width), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of radix-2^b digits in each input.
- $u_i$ (digit of u), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The i-th radix-2^b digit of u, an integer below 2^b.
- $v_k$ (digit of v), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The k-th radix-2^b digit of v, an integer below 2^b.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the digit polynomials.
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis, with x_d^r = 1.
- $\zeta$ (twist phase), bound on [Phase twist](phase-twist.md): The number e^{\pi i/r}, a primitive 2r-th root of unity with \zeta^r = -1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from C[x_d]/(x_d^r-1) to the negacyclic ring sending x_d to \zeta y.
- $d$ (number of axes), bound on [Phase twist](phase-twist.md): The number of axes of the array f.
- $T$ (total entries), bound on [Phase twist](phase-twist.md): The number of entries of the array f in all.
- $M$ (number of records), bound on [Phase twist](phase-twist.md): The number of lines along the last axis, T/r.
- $\iota$ (record identification), bound on [Phase twist](phase-twist.md): Reads each line along the last axis as a polynomial in the negacyclic ring.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): Multiplies entry k of each line by \zeta^{\pm k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): The ring convolution that convolves the first d-1 axes over the negacyclic ring and includes the division by T.
- $\mathcal M_{\mathbb C}$ (normalized cyclic convolution), bound on [Phase twist](phase-twist.md): The composite D_-\iota^{-1}\mathcal M_r(\iota D_+ f,\iota D_+ g), equal to f*g/T.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of complex entries in the sequences the transform acts on.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to which the transform is applied.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2 pi i/q} whose powers are the transform weights.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of values in the transform, a power of two.
- $z_k$ (input values), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k, for 0 <= k < t.
- $k$ (input position), bound on [Butterflies and the fast transform](butterfly.md): The position of an input value, 0 <= k < t.
- $\omega_t$ (root of unity), bound on [Butterflies and the fast transform](butterfly.md): The primitive t-th root of unity e^{2 pi i/t}.
- $b$ (lowest output bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index, 0 or 1.
- $h$ (remaining output index), bound on [Butterflies and the fast transform](butterfly.md): The output index with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $\omega_t$ (ring root of unity), bound on [Synthetic polynomial transform](synthetic-transform.md): The power y^{2r/t} of the ring variable, used as the root of unity of the length-t synthetic transform.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits stored in the array.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (number of streams), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which whole rows are dealt cyclically.
- $d$ (number of axes), bound on [Bluestein chirp identity](chirp.md): The number of axes (coordinates) of an index.
- $t_i$ (axis length), bound on [Bluestein chirp identity](chirp.md): The even number of entries along axis i.
- $s_i$ (coprime integer), bound on [Bluestein chirp identity](chirp.md): An integer coprime to t_i, scaling the frequency read along axis i.
- $T$ (total entries), bound on [Bluestein chirp identity](chirp.md): The total number of entries, the product of the t_i.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The target permutation, reading frequency (-s_i j_i)_i at output position j.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i).
- $t$ (transform length), bound on [Retained frequency order](frequency-order.md): The number of ring elements transformed along one axis, a power of two dividing 2r.
- $a$ (number of rounds), bound on [Retained frequency order](frequency-order.md): The number log_2 t of rounds of the fast algorithm.
- $\omega_t$ (root of unity), bound on [Retained frequency order](frequency-order.md): The power y^{2r/t} of the ring variable used as the t-th root of unity.
- $H_0$ (two-point butterfly), bound on [Retained frequency order](frequency-order.md): The 2x2 matrix (1/2)[[1,1],[1,-1]] applied to each pair of entries.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation of records moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The butterfly layer applying H_0 on every participating axis at once.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The operation multiplying the record at each address by y^E.
- $u_i$ (current length), bound on [Retained frequency order](frequency-order.md): The current recursive length of axis i.
- $b_i$ (branch bit), bound on [Retained frequency order](frequency-order.md): The newly written branch bit of axis i.
- $k_i$ (encoded index), bound on [Retained frequency order](frequency-order.md): The index encoded by the still unprocessed slots of axis i.
- $N$ (bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers being multiplied.
- $p$ (precision bits), bound on [Signed packing](signed-packing.md): The number of fractional bits in each coefficient component.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The power of two $2^{4p}$ at which the polynomials are evaluated.
- $A_u$ (evaluation integer), bound on [Signed packing](signed-packing.md): The signed integer obtained by evaluating the polynomial u at B_0.
- $H_j$ (numerator coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The prime base of the field arithmetic.
- $b$ (field digits), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-$q$ digits of a field.
- $Q$ (field size), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can hold, Q = q^b.
- $V$ (array volume), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of stored data bits in the array.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of bits following the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the target is multiplied.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): The fixed rational m by m matrix whose action AD is added to H.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $H$ (H group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields H_1..H_m that receives the update.
- $D$ (D group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields D_1..D_m that is added into H.
- $q$ (base prime), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime; fields are residues modulo q^b.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in a field.
- $V$ (data volume), bound on [Matrix shear by triangular factorization](matrix-shear.md): The volume of data being processed.
- $E_1$ (left factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $E_2$ (right factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $\Pi$ (partial permutation), bound on [Matrix shear by triangular factorization](matrix-shear.md): A matrix with exactly a ones, at most one per row and column, and zeros elsewhere.
- $i$ (row index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The row of a one of Pi.
- $j$ (column index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The column of a one of Pi.
- $h$ (value of H_i), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field H_i.
- $d$ (value of D_j), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field D_j.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2x2 matrix that swaps the two entries of a pair.
- $a$ (kernel coefficient a), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, the coefficient of I in C.
- $b$ (kernel coefficient b), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, the coefficient of X in C.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The matrix aI + bX, a square root of the bit flip.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1, i) that multiplies the second entry of a pair by i.
- $H_0$ (butterfly matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix of the averaging and differencing step (u,v) -> ((u+v)/2, (u-v)/2).
- $d$ (number of axes), bound on [Multidimensional transforms](multidim-transform.md): The number of axes (coordinates) of the array.
- $q_i$ (axis length), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $N$ (number of entries), bound on [Multidimensional transforms](multidim-transform.md): The number of entries of the array, the product of the axis lengths.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](convolution.md): The product of two sequences (or elements of a polynomial quotient ring) where indices wrap around: (f∗g)_k = Σ f_j g_{k−j}.
  Shown as: Chinese-remainder address map *<predicate>* Cyclic convolution
- [Multidimensional transforms](multidim-transform.md): A transform over several axes at once, the tensor product of one-dimensional transforms, applied to an array one axis at a time.
  Shown as: Chinese-remainder address map *<predicate>* Multidimensional transforms
- [Controlled shifts and rational scalings](controlled-shifts.md): Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume.
  Shown as: Chinese-remainder address map *<predicate>* Controlled shifts and rational scalings

## Pages that build on this one

- Parameter and prime-length choice: Fixed rational exponents and sizes (precision p = 6b, d axes, K = d^c, T and r powers of two, prime lengths s_i just below t_i) making every hypothesis of the lemmas hold.
- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "by a Chinese-remainder map that preserves" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.

- "Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution" (paper)

  > To use the source tensor, we first place the ordinary coefficient stream in its tensor order. Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution~\cite{AgarwalCooley1977}. The following map uses that algebraic split, with coordinate powers that make the change of order a sequence of controlled cyclic shifts.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Reorder the padded axes to $(a_1,\dots,a_d)$, so controls precede their target." (The page never says how the coefficient stream is laid out as a padded array nor in which axis order it starts (the paper, line 4231, says numerical order of k is lexicographic in (a_d,...,a_1), with padding inserted by a nested scan, lines 4232-4247). Without this the reader cannot see why a reordering, or why a reversal of all axes, is needed, nor that the padding scan costs O(Tp).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "cost $O(Tp\,d^2(1+\ell^\tau))$ (cited)" (The page does not say what one equal-width chunk interchange costs (O(Tp ell^tau)), nor how the O(d^2) swaps, the linear passes, the shifts and the padding scans combine into the stated bound; the reader cannot check the formula from the page. It also omits the paper's hypotheses for the shift offsets to cost o(Tp) (t_i >= r/2 and r exceeding every fixed power of p, paper lines 4278-4281).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $i$ denotes where it is first used: the page uses it before saying so in "be the product of the lengths before axis $i$"

## Previous version (revise it)

It has 348 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 435 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The Chinese-remainder address map rewrites a cyclic convolution of length $S=s_1\cdots s_d$, where the axis lengths $s_i$, $1\le i\le d$, are pairwise coprime and $d$ is the number of axes, as a multidimensional one, using only controlled shifts on tape. The split is due to Agarwal and Cooley <cite data-source="paper">Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution</cite>; the exponents here make the data movement triangular.

Let $P_i=\prod_{j<i}s_j$ be the product of the lengths before axis $i$, and $\mu_i=P_i^{-1}\pmod{s_i}$. Map $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, with one variable $x_i$ per axis $i$, by $\Phi:x\mapsto\prod_i x_i^{\mu_i}$. It respects $x^S=1$, because $s_i\mid S$ makes every $x_i^{\mu_iS}=1$, so it defines an algebra map.

Now $\Phi(x^k)=1$ exactly when $s_i\mid\mu_ik$ for every $i$; as $\mu_i$ is a unit modulo $s_i$ this means $s_i\mid k$ for every $i$, and as the $s_i$ are pairwise coprime, $S\mid k$. So the image of $x$ has order $S$ and its $S$ powers are distinct; the target has exactly $S$ monomials, so the powers run through all of them exactly once. Hence $\Phi$ is an isomorphism and preserves [Cyclic convolution](convolution.md), because multiplication in each ring is cyclic convolution of coefficients. This prepares [Multidimensional transforms](multidim-transform.md).

Write $k=\sum_ja_jP_j$ in mixed radix, with digits $0\le a_j<s_j$. The axis-$i$ coordinate $b_i$ of $\Phi(x^k)$ is $\mu_ik\bmod s_i=\mu_i\sum_ja_jP_j\bmod s_i$. Terms with $j>i$ vanish modulo $s_i$, since $s_i$ divides $P_j$, and $\mu_iP_i\equiv1$ modulo $s_i$. Hence $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$.

So $b_i$ depends only on lower-index digits. Pad axis $i$ with zero records to a length $t_i\ge s_i$, a power of two of $\ell$ or $\ell-1$ bits, where $\ell$ is the bit width of the widest axis. Let $T=\prod_it_i$ be the number of records in the padded array, each of $O(p)$ bits, where $p$ is the number of bits of precision per record.

Reorder the padded axes to $(a_1,\dots,a_d)$, so controls precede their target. Update targets in the order $i=d,d-1,\dots,1$, so no lower-index control has yet changed when axis $i$ is updated. Each update is a prefix-controlled cyclic shift of the valid interval $[0,s_i)$ and the identity on $[s_i,t_i)$, so zero padding stays zero. The map is implemented by these shifts, each of linear cost by [Controlled shifts and rational scalings](controlled-shifts.md).

Reversing all axes takes $O(d^2)$ adjacent swaps. Each swap is an equal-width [chunk interchange](address-interchange.md) of cost governed by a fixed exponent $\tau\in(0,1)$, plus a fixed number of linear passes if widths differ, so the map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$ <cite data-source="paper">O\bigl(Tp\,d^2(1+\ell^\tau)\bigr).</cite>

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
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
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
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

Write the body to `exegenius/tasks/0100-write-crt-map.answer.md` and the JSON to `exegenius/tasks/0100-write-crt-map.answer.json`, then run `exegenius submit 0100-write-crt-map` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0100-write-crt-map`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
