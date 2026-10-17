# exegenius task 0372-write-chirp

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
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform (also: transform levels)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
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

Concept: Bluestein chirp identity
Gloss: An identity that rewrites a (permuted) Fourier transform as a pointwise chirp phase, a cyclic convolution, and another chirp phase.
Also called: chirp transform

## This page in the argument

The step: For even $t_i$ and the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ one has $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, so the target permutation $Q$ is absorbed into a cyclic convolution of length $T$ and never executed.
How: Expand the coefficient of $u_{\boldsymbol k}$ in the right side using $(j-k)^2=j^2-2jk+k^2$, so that the three chirp phases combine to $\exp(2\pi i\sum s_ij_ik_i/t_i)$, which is the coefficient of $QF_{\boldsymbol t}$ because $Q$ reads frequency $-s_ij_i$.
Why: Bluestein's identity turns a (permuted) discrete Fourier transform into pointwise phases around a convolution; the phases depend on $s_ij_i^2/t_i$ and the permutation $Q$ merely changes which frequency is read, which the identity already includes. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Define $a_{\boldsymbol j}=\exp\left(-\pi i\sum_{i=1}^d s_ij_i^2/t_i\right)$.
- Replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\pi is_i(2j_i+t_i)$, an integral multiple of $2\pi i$ because $t_i$ is even, so $a$ has period $t_i$ in coordinate $i$.
- The coefficient of $u_{\boldsymbol k}$ in the right side is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$.
- This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- The Fourier transforms of pairwise coprime prime lengths $s_i$ that the integer product needs are computed through power-of-two lengths $t_i$ by Gaussian resampling and Bluestein chirps, with the source and target coordinate permutations left inside the transform identities, so that none is executed as a sort.; how: Retain both permutations of Gaussian resampling in the transform formula: the target permutation $Q$ is absorbed by the chirp convolution, and the source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite transform. (on [Retained permutation cancellation](retained-permutations.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.3.1, S4.3.2, S4.3.3, S4.3.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.3.1**: Define $a_{\boldsymbol j}=\exp\left(-\pi i\sum_{i=1}^d s_ij_i^2/t_i\right)$.
Source: "=\exp\left(-\pi i\sum_{i=1}^d\frac{s_i j_i^2}{t_i}\right)." (paper)
> \begin{lemma}[Chirp and permutation cancellation] \label{lem:chirp-permutation} With $R,Q,s_i,t_i$ as in Lemma~\ref{lem:tensor-resampling}, assume every $t_i$ is even. For $\boldsymbol j\in\mathbb Z^d$, define \[ a_{\boldsymbol j} =\exp\left(-\pi i\sum_{i=1}^d\frac{s_i j_i^2}{t_i}\right). \] Then $a$ has period $t_i$ in coordinate $i$, and \begin{equation} QF_{\boldsymbol t}u =\overline a\mathbin{\cdot} \frac{a*(\overline a\mathbin{\cdot}u)}{T}. \label{eq:permuted-chirp} \end{equation} If $S=\prod_i s_i$, then \begin{equation} (RF_{\boldsymbol s}^+) \bigl[(RF_{\boldsymbol s}u)\mathbin{\cdot} (RF_{\boldsymbol s}v)\bigr] =\frac{u*v}{S^2}. \label{eq:source-permutation-cancel} \end{equation} Complex conjugation of the input and output of an algorithm for $RF_{\boldsymbol s}$ gives an algorithm for $RF_{\boldsymbol s}^+$. \end{lemma}

**S4.3.2**: Replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\pi is_i(2j_i+t_i)$, an integral multiple of $2\pi i$ because $t_i$ is even, so $a$ has period $t_i$ in coordinate $i$.
Source: "Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by" (paper)
> \begin{proof} Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\pi i s_i(2j_i+t_i)$, an integral multiple of $2\pi i$. The coefficient of $u_{\boldsymbol k}$ in the right side of \eqref{eq:permuted-chirp} is \[ \frac1T\overline a_{\boldsymbol j} a_{\boldsymbol j-\boldsymbol k} \overline a_{\boldsymbol k} =\frac1T\exp\left(2\pi i\sum_i \frac{s_i j_i k_i}{t_i}\right). \] This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform.

**S4.3.3**: The coefficient of $u_{\boldsymbol k}$ in the right side is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$.
Source: "=\frac1T\exp\left(2\pi i\sum_i" (paper)
> \begin{proof} Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\pi i s_i(2j_i+t_i)$, an integral multiple of $2\pi i$. The coefficient of $u_{\boldsymbol k}$ in the right side of \eqref{eq:permuted-chirp} is \[ \frac1T\overline a_{\boldsymbol j} a_{\boldsymbol j-\boldsymbol k} \overline a_{\boldsymbol k} =\frac1T\exp\left(2\pi i\sum_i \frac{s_i j_i k_i}{t_i}\right). \] This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform.

**S4.3.4**: This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.
Source: "This is precisely the coefficient in $QF_{\boldsymbol t}$, because" (paper)
> \begin{proof} Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\pi i s_i(2j_i+t_i)$, an integral multiple of $2\pi i$. The coefficient of $u_{\boldsymbol k}$ in the right side of \eqref{eq:permuted-chirp} is \[ \frac1T\overline a_{\boldsymbol j} a_{\boldsymbol j-\boldsymbol k} \overline a_{\boldsymbol k} =\frac1T\exp\left(2\pi i\sum_i \frac{s_i j_i k_i}{t_i}\right). \] This is precisely the coefficient in $QF_{\boldsymbol t}$, because $Q$ reads frequency $(-s_i j_i)_i$ from the negative-sign transform.

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
- $f$ (first array), bound on [Phase twist](phase-twist.md): The first complex array being convolved.
- $g$ (second array), bound on [Phase twist](phase-twist.md): The second complex array being convolved with f.
- $d$ (axis count), bound on [Phase twist](phase-twist.md): The number of axes of the arrays.
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis.
- $\mathcal R_r$ (negacyclic ring), bound on [Phase twist](phase-twist.md): The ring of polynomials modulo y^r+1.
- $\zeta$ (twist root), bound on [Phase twist](phase-twist.md): The primitive 2r-th root of unity e^{\pi i/r}, with zeta^r=-1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from the cyclic ring to the negacyclic ring sending x_d to zeta y.
- $k$ (coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient (not an operation count).
- $l$ (second coefficient index), bound on [Phase twist](phase-twist.md): An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on [Phase twist](phase-twist.md): The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on [Phase twist](phase-twist.md): Zero or one according to whether k+l wrapped past r.
- $\iota$ (record reading), bound on [Phase twist](phase-twist.md): The map reading each line along the last axis as a polynomial in R_r.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): The maps multiplying entry k of each line by zeta^{+-k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): Normalized convolution of the first d-1 axes over R_r, including division by T.
- $\mathcal M_{\mathbb C}$ (complex convolution), bound on [Phase twist](phase-twist.md): The normalized complex cyclic convolution of two arrays.
- $\|f\|$ (sup norm), bound on [Phase twist](phase-twist.md): The largest modulus of a scalar coefficient of f.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of entries of a sequence.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to be transformed.
- $\omega$ (primitive root), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2\pi i/q}.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of positions in the sequence being transformed, a power of two.
- $z_k$ (input value), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k of the sequence being transformed.
- $m$ (output index), bound on [Butterflies and the fast transform](butterfly.md): The index of an output of the transform.
- $b$ (lowest bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index m.
- $h$ (remaining index), bound on [Butterflies and the fast transform](butterfly.md): The output index m with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on [Synthetic polynomial transform](synthetic-transform.md): The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of digits stored in the array.
- $\beta$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which rows are dealt.
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values of the array in item 4.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in item 4; here R is not the scalar ring.
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row in item 4.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](dft.md): The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns convolution into pointwise multiplication.
  Shown as: Bluestein chirp identity *<predicate>* Discrete Fourier transform
- [Cyclic convolution](convolution.md): The product of two sequences (or elements of a polynomial quotient ring) where indices wrap around: (f∗g)_k = Σ f_j g_{k−j}.
  Shown as: Bluestein chirp identity *<predicate>* Cyclic convolution

## Pages that build on this one

- Retained permutation cancellation: Leaving the coordinate permutations of resampling inside the transform identity, so the source permutation cancels across the two forward transforms and the opposite one and none is executed as a sort.
- Error tracking and exact recovery: Each normalized transform and product is a contraction with a bounded rounding error, and the total error on the recovered convolution coefficients is below 1/2, so rounding gives exact integers.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
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

- "Bluestein's chirp identity converts the middle transform," (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

- "Chirp and permutation cancellation" (paper)

  > \begin{lemma}[Chirp and permutation cancellation] \label{lem:chirp-permutation} With $R,Q,s_i,t_i$ as in Lemma~\ref{lem:tensor-resampling}, assume every $t_i$ is even. For $\boldsymbol j\in\mathbb Z^d$, define \[ a_{\boldsymbol j} =\exp\left(-\pi i\sum_{i=1}^d\frac{s_i j_i^2}{t_i}\right). \] Then $a$ has period $t_i$ in coordinate $i$, and \begin{equation} QF_{\boldsymbol t}u =\overline a\mathbin{\cdot} \frac{a*(\overline a\mathbin{\cdot}u)}{T}. \label{eq:permuted-chirp} \end{equation} If $S=\prod_i s_i$, then \begin{equation} (RF_{\boldsymbol s}^+) \bigl[(RF_{\boldsymbol s}u)\mathbin{\cdot} (RF_{\boldsymbol s}v)\bigr] =\frac{u*v}{S^2}. \label{eq:source-permutation-cancel} \end{equation} Complex conjugation of the input and output of an algorithm for $RF_{\boldsymbol s}$ gives an algorithm for $RF_{\boldsymbol s}^+$. \end{lemma}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "The permutation needs no separate step: it only changes which frequency is read, and the sign of the cross term $2j_ik_i$ already matches it.": I checked the coefficient algebra line by line, but I could not see why reading frequency (-s_i j_i) from the transform is the right choice, other than that the signs happen to match. I got past this by checking the arithmetic, not by understanding the motivation. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "The permutation needs no separate step: it only changes which frequency is read": The derivation checks out line by line, but the page does not say why absorbing the permutation into a convolution is what the next stage requires. I connected this to the padded length T myself. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "The permutation needs no separate step: it only changes which frequency is read, and the sign of the cross term $2j_ik_i$ already matches it.": I checked the exponent algebra, but I could not see why reading a different frequency makes the permutation free in the transform. (the reader followed the steps but not why they lead where they do: say what this step is for)
- Simulated readers trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" could not work out: Executing the permutations would mean sorting data on a tape, costing about t p log t per line, which would cancel the power saving.. A reader with the stated background should be able to get this from this page and the pages it builds on.

## Previous version (revise it)

It has 315 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 393 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The Bluestein chirp identity rewrites a permuted [Discrete Fourier transform](dft.md) as a pointwise chirp phase, a cyclic convolution, and another chirp phase, so the target permutation of resampling is absorbed into the convolution and never executed as a sort. This is how the middle transform, including its target permutation, becomes a normalized cyclic convolution <cite data-source="paper">Bluestein's chirp identity converts the middle transform,</cite>.

## Setting

Data are arrays indexed by $\boldsymbol j=(j_1,\dots,j_d)$, where $d$ is the number of axes. The tuple $\boldsymbol t=(t_1,\dots,t_d)$ lists the axis lengths, where $t_i$ is the even number of entries along axis $i$, and $s_i$ is an integer coprime to $t_i$. Put $T=\prod_i t_i$, the total number of entries. Indices along axis $i$ are taken modulo $t_i$.

The normalized transform $F_{\boldsymbol t}$ is given by $(F_{\boldsymbol t}u)_{\boldsymbol f}=\frac1T\sum_{\boldsymbol k}u_{\boldsymbol k}\exp(-2\pi i\sum_i k_if_i/t_i)$, where $\boldsymbol k$ runs over input positions and $\boldsymbol f=(f_1,\dots,f_d)$ is the frequency labelling an output entry. The target permutation $Q$ reorders the output so that position $\boldsymbol j$ holds the entry of frequency $(-s_ij_i)_i$. So in $QF_{\boldsymbol t}u$, the coefficient of $u_{\boldsymbol k}$ in output position $\boldsymbol j$ is $\frac1T\exp(2\pi i\sum_i s_ij_ik_i/t_i)$.

## The identity

Define the chirp $a_{\boldsymbol j}=\exp\left(-\pi i\sum_{i=1}^d s_ij_i^2/t_i\right)$, a phase quadratic in the index, and let $\overline a$ be its complex conjugate. When every $t_i$ is even <cite data-source="paper">assume every $t_i$ is even.</cite>,
$$QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T},$$
where the dot is coordinatewise multiplication and $*$ is cyclic convolution. The permuted transform is thus reduced to one [Cyclic convolution](convolution.md) of length $T$ between two pointwise phase multiplications.

## Derivation

The convolution reads $a_{\boldsymbol j-\boldsymbol k}$ at indices taken modulo $t_i$, so $a$ must depend only on residues. Replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\pi i s_i\frac{(j_i+t_i)^2-j_i^2}{t_i}=-\pi i s_i(2j_i+t_i)$, which is an integral multiple of $2\pi i$ because $t_i$ is even, so $a$ has period $t_i$ in coordinate $i$.

In the right side, the coefficient of $u_{\boldsymbol k}$ in output position $\boldsymbol j$ is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}$. Using $(j_i-k_i)^2=j_i^2-2j_ik_i+k_i^2$, the exponent of this product is $\sum_i\frac{\pi i s_i}{t_i}\bigl(j_i^2-(j_i^2-2j_ik_i+k_i^2)+k_i^2\bigr)$, where the squares cancel, so the coefficient is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$.

This is precisely the coefficient of $QF_{\boldsymbol t}$ found above, because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform. The permutation needs no separate step: it only changes which frequency is read, and the sign of the cross term $2j_ik_i$ already matches it.

For $d=1$, $t_1=2$, $s_1=1$: $a_0=1$, $a_1=-i$, and $j=k=1$ gives $\overline a_1a_0\overline a_1=i\cdot1\cdot i=-1=\exp(2\pi i\cdot\tfrac12)$, as required.

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

Write the body to `exegenius/tasks/0372-write-chirp.answer.md` and the JSON to `exegenius/tasks/0372-write-chirp.answer.json`, then run `exegenius submit 0372-write-chirp` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0372-write-chirp`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
