# exegenius task 0368-write-phase-twist

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
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Cyclic convolution
- Multiplication as radix-digit convolution
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
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

## This page

Concept: Phase twist
Gloss: Multiplying coefficient k by e^{πik/r}, which converts the cyclic coordinate modulo x^r − 1 into the negacyclic ring modulo y^r + 1 and is removed afterwards.

## This page in the argument

The step: With $\zeta=e^{\pi i/r}$ the map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$, is an isomorphism multiplying coefficient $k$ by $\zeta^k$; hence normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$.
How: Twist the last cyclic coordinate by powers of $\zeta$, so that the negative wrap of $y^r=-1$ cancels against the factor $\zeta^r=-1$; untwist afterwards.
Why: The last cyclic axis of length $r$ must become the polynomial coordinate of $\mathbb C[y]/(y^r+1)$; since $(\zeta y)^r=(-1)(-1)=1$, a diagonal change of basis turns the cyclic wrap into a negative wrap, and the factor $\zeta^{k+l}$ undoes the sign. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Put $\mathcal R=\mathcal R_r$ and $\zeta=e^{\pi i/r}$; the map $\Theta$ sends $x_d$ to $\zeta y$.
- $\Theta$ is well defined since $(\zeta y)^r=(-1)(-1)=1$; it is diagonal on the bases $(x_d^k)$ and $(y^k)$, multiplying coefficient $k$ by $\zeta^k\ne0$, so it is an isomorphism with inverse multiplying by $\zeta^{-k}$, and both maps preserve the sup norm.
- For a product term with $k+l=j+hr$, $h\in\{0,1\}$, the factor after twisting and negacyclic reduction is $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.
- Hence $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$ is a bilinear contraction ($\iota$ identifies the scalar tensor with $M$ records, $D_\pm$ multiply by $\zeta^{\pm k}$).

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$.; how: Reduce the integer product to a cyclic convolution of $S$ short coefficients and compute it through the chain of reductions (digits, CRT address map, Gaussian resampling with chirps, twist to the polynomial ring, synthetic-transform convolution); recover exact integers because the accumulated error is below $1/2$. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.4.1, S5.4.2, S5.4.3, S5.4.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.4.1**: Put $\mathcal R=\mathcal R_r$ and $\zeta=e^{\pi i/r}$; the map $\Theta$ sends $x_d$ to $\zeta y$.
Source: "$\zeta=e^{\pi i/r}$.  The map" (paper)
> The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise

**S5.4.2**: $\Theta$ is well defined since $(\zeta y)^r=(-1)(-1)=1$; it is diagonal on the bases $(x_d^k)$ and $(y^k)$, multiplying coefficient $k$ by $\zeta^k\ne0$, so it is an isomorphism with inverse multiplying by $\zeta^{-k}$, and both maps preserve the sup norm.
Source: "is well defined, since $(\zeta y)^r=(-1)(-1)=1$." (paper)
> The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z

**S5.4.3**: For a product term with $k+l=j+hr$, $h\in\{0,1\}$, the factor after twisting and negacyclic reduction is $\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.
Source: "\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j." (paper)
> ity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequentl

**S5.4.4**: Hence $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$ is a bilinear contraction ($\iota$ identifies the scalar tensor with $M$ records, $D_\pm$ multiply by $\zeta^{\pm k}$).
Source: "\mathcal M_r(\iota D_+f,\iota D_+g)" (paper)
> Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequently, with $\mathcal M_r$ from Section~\ref{sec:exact-ring-products}, normalized complex cyclic convolution is \[ \mathcal M_{\mathbb C}(f,g) :=D_-\iota^{-1} \mathcal M_r(\iota D_+f,\iota D_+g) =\frac{f*g}{T}. \] Here $\mathcal M_r$ convolves the first $d-1$ axes over $\mathcal R$, whereas $*$ on the right convolves all $d$ scalar axes. The division by $T$ is already part of $\mathcal M_r$. The maps $D_\pm$ and $\iota^{\pm1}$ are isometries, so $\mathcal M_{\mathbb C}$ is also a bilinear contraction.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant, the amount by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $X$ (first data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): One of the two data banks, with entries X_a.
- $Y$ (second data bank), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The other data bank, with entries Y_a.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A triple of three-element subsets of [h] indexing the entries of the banks.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the banks.
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of values in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used on later pages.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations over all three stages.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network acting on all the wire arrays together, each gate applied at every address separately.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to the source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of the gate G.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role w to its output role rho(w) in a signed role permutation.
- $\varepsilon_w$ (role sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign carried by the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two n-bit integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two n-bit integers being multiplied (not the number of triples).
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The padded length, a power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, with T/2<S<T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of digits in each input, not the sequence length of the convolution page.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The indeterminate of the digit polynomials, evaluated at 2^b to recover the integers.
- $c_j$ (product coefficient), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The coefficient of x^j in the product of the two digit polynomials.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](ring-y.md): Polynomials of degree below r over the complex numbers with y^r = −1, so multiplying by a power of y is a signed shift of the coefficient list.
  Shown as: Phase twist *<predicate>* Polynomial ring modulo y^r + 1
- [Cyclic convolution](convolution.md): The product of two sequences (or elements of a polynomial quotient ring) where indices wrap around: (f∗g)_k = Σ f_j g_{k−j}.
  Shown as: Phase twist *<predicate>* Cyclic convolution

## Pages that build on this one

- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

## Other pages you may link to

- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
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

- "A phase twist changes the last cyclic coordinate into a polynomial" (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

- "x_d\longmapsto\zeta y" (paper)

  > The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "so that Cyclic convolution can be computed by ring convolution, and that is undone afterwards.": The page shows the twist maps cyclic wrap to negacyclic wrap, but does not say why convolution in the negacyclic ring is what the next stage needs. The link to the synthetic transform only appears on page kur. I followed the steps without seeing why the twist is needed. (the reader followed the steps but not why they lead where they do: say what this step is for)

## Previous version (revise it)

It has 411 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 513 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The phase twist is a diagonal change of basis that turns the last cyclic axis of a complex array into the coordinate of a negacyclic polynomial ring, so that cyclic convolution can be computed by ring convolution, and that is undone afterwards.

Let $f$ and $g$ be two complex arrays with $d$ axes, the last of length $r$, and $T$ entries in all. Convolution along the last axis is multiplication in $\mathbb C[x_d]/(x_d^r-1)$, where $x_d$ is the variable of that axis. The twist converts the last cyclic axis into the coordinate of the [Polynomial ring modulo y^r + 1](ring-y.md), written $\mathcal R_r$, where $y^r=-1$ instead.

## The map

Let $\zeta=e^{\pi i/r}$, so $\zeta^r=-1$. Define the ring map $\Theta$ from $\mathbb C[x_d]/(x_d^r-1)$ to $\mathcal R_r$ by $x_d\mapsto\zeta y$. It is well defined because $(\zeta y)^r=(-1)(-1)=1$.

Here $k$ and $l$ index coefficients, not operations. Since $\Theta(x_d^k)=\zeta^k y^k$, $\Theta$ is diagonal on the bases $(x_d^k)$ and $(y^k)$, multiplying coefficient $k$ by $\zeta^k\ne0$. It is therefore an isomorphism, with inverse multiplying by $\zeta^{-k}$. Both maps preserve the coefficient sup norm, since $|\zeta^{\pm k}|=1$ <cite data-source="paper">Both exact maps preserve the coefficient sup norm.</cite>

## The wrap

Take $k,l<r$ and write $k+l=j+hr$, with $j<r$ the resulting position and $h\in\{0,1\}$ the wrap indicator. After twisting, the term carries $\zeta^{k+l}$, and negacyclic reduction contributes $(-1)^h$, so the factor is
$$\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j.$$
The coefficient of $y^j$ is thus $\zeta^j$ times the cyclic coefficient; untwisting by $\zeta^{-j}$ restores it with the correct sign. The twist reproduces [Cyclic convolution](convolution.md) on that axis.

For $r=2$, $\zeta=i$. Twisting $(f_0,f_1)$ and $(g_0,g_1)$ gives $(f_0,if_1)$ and $(g_0,ig_1)$. Their product has $f_0g_0+f_1g_1$ and $i(f_0g_1+f_1g_0)$. Multiplying the second by $\zeta^{-1}=-i$ gives the cyclic result.

## Whole arrays

Then $M=T/r$ is the number of lines along the last axis, and $\iota$ reads each line $(f_{\boldsymbol j,k})_k$ as the polynomial $\sum_k f_{\boldsymbol j,k}y^k$, giving an array of $M$ records in $\mathcal R_r$. Let $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$ multiply entry $k$ of each line by $\zeta^{\pm k}$. Then $\iota D_+$ applies $\Theta$ to every line, with inverse $D_-\iota^{-1}$.

Let $\mathcal M_r$ be the ring convolution of [Convolution from the retained transform layout](ring-convolution.md): it convolves the first $d-1$ axes over $\mathcal R_r$, dividing by $T$. The composite $\mathcal M_{\mathbb C}$, the normalized complex cyclic convolution, is
$$\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=\frac{f*g}{T}.$$
Here $*$ is cyclic convolution over all $d$ axes.

## Contraction

Write $\|f\|$ for the sup norm of an array $f$: the largest modulus of a scalar coefficient. A bilinear map is a bilinear contraction if its value has norm at most the product of the norms of its arguments ([Contractions and bilinear contractions](contraction-maps.md)). $\mathcal M_r$ is one: a fixed output coefficient averages $rM$ signed scalar products of coefficients, each at most $\|f\|\|g\|$ in modulus, so $\|\mathcal M_r(f,g)\|\le\|f\|\|g\|$ <cite data-source="paper">$rM$ signed scalar products, and $\mathcal M_r$ is a bilinear</cite>.

The maps $\iota^{\pm1}$ only regroup scalars, and $D_\pm$ multiplies by numbers of modulus $1$, so all are linear and keep the sup norm. Hence
$$\|\mathcal M_{\mathbb C}(f,g)\|=\|\mathcal M_r(\iota D_+f,\iota D_+g)\|\le\|\iota D_+f\|\,\|\iota D_+g\|=\|f\|\,\|g\|,$$
so $\mathcal M_{\mathbb C}$, a bilinear map composed with linear ones, is a bilinear contraction.

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

Write the body to `exegenius/tasks/0368-write-phase-twist.answer.md` and the JSON to `exegenius/tasks/0368-write-phase-twist.answer.json`, then run `exegenius submit 0368-write-phase-twist` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0368-write-phase-twist`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
