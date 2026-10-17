# exegenius task 0367-write-radix-digit-reduction

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

Concept: Multiplication as radix-digit convolution
Gloss: Splitting each integer into radix-2^b digits turns the product into a convolution of short integer coefficients, which carry propagation turns back into a binary number.

## This page in the argument

The step: Writing the two inputs in radix $2^b$ with $q=\lceil n/b\rceil$ digits each, the product polynomial has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and every coefficient $c_j\le q(2^b-1)^2<2^{3b}$.
How: Count degrees and bound the coefficients: a product of two polynomials with $q$ digits below $2^b$ has degree $2q-2$ and coefficients that are sums of at most $q$ products.
Why: Splitting an integer into radix digits turns the product into a convolution of short integer coefficients; the cyclic convolution of length $S$ equals the ordinary product as long as the degree stays below $S$, and the coefficient bound shows rounding errors below 1/2 will identify them. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits; their product has degree at most $2q-2$.
- Since $2q-2<2n/b\le T/2<S$, convolution modulo $x^S-1$ has no nonzero wraparound.
- Every product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$, since $q\le n\le2^b$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$.; how: Reduce the integer product to a cyclic convolution of $S$ short coefficients and compute it through the chain of reductions (digits, CRT address map, Gaussian resampling with chirps, twist to the polynomial ring, synthetic-transform convolution); recover exact integers because the accumulated error is below $1/2$. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.2.1, S5.2.2, S5.2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.2.1**: Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits; their product has degree at most $2q-2$.
Source: "$q=\lceil n/b\rceil$ nonnegative digits.  Their product has degree at most" (paper)
> Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits. Their product has degree at most \[ 2q-2<2n/b\le T/2<S. \] Thus convolution modulo $x^S-1$ has no nonzero wraparound. Every product coefficient obeys \begin{equation}\label{eq:capacity} 0\le c_j\le q(2^b-1)^2<2^{3b}, \end{equation} since $q\le n\le2^b$.

**S5.2.2**: Since $2q-2<2n/b\le T/2<S$, convolution modulo $x^S-1$ has no nonzero wraparound.
Source: "2q-2<2n/b\le T/2<S." (paper)
> Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits. Their product has degree at most \[ 2q-2<2n/b\le T/2<S. \] Thus convolution modulo $x^S-1$ has no nonzero wraparound. Every product coefficient obeys \begin{equation}\label{eq:capacity} 0\le c_j\le q(2^b-1)^2<2^{3b}, \end{equation} since $q\le n\le2^b$.

**S5.2.3**: Every product coefficient obeys $0\le c_j\le q(2^b-1)^2<2^{3b}$, since $q\le n\le2^b$.
Source: "0\le c_j\le q(2^b-1)^2<2^{3b}," (paper)
> Write the two inputs as polynomials in $2^b$, each with $q=\lceil n/b\rceil$ nonnegative digits. Their product has degree at most \[ 2q-2<2n/b\le T/2<S. \] Thus convolution modulo $x^S-1$ has no nonzero wraparound. Every product coefficient obeys \begin{equation}\label{eq:capacity} 0\le c_j\le q(2^b-1)^2<2^{3b}, \end{equation} since $q\le n\le2^b$.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](convolution.md): The product of two sequences (or elements of a polynomial quotient ring) where indices wrap around: (f∗g)_k = Σ f_j g_{k−j}.
  Shown as: Multiplication as radix-digit convolution *<predicate>* Cyclic convolution

## Pages that build on this one

- Error tracking and exact recovery: Each normalized transform and product is a contraction with a bounded rounding error, and the total error on the recovered convolution coefficients is below 1/2, so rounding gives exact integers.
- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Phase twist](phase-twist.md)
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

- "Splitting the inputs into radix digits reduces multiplication to" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "Propagate radix-$2^b$ carries in increasing coefficient order." (paper)

  > exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \end{enumerate}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "Here $S$, $T$ and $v$ also differ from their meanings on earlier pages.": Symbols are reused with new meanings (S, T, v, q). I had to re-track what each one means on this page, which made the digit-count step harder to follow. (stuck at the symbol level)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "a product of distinct odd primes with $T/2<S<T$.": I can check the inequalities, but I could not see why S must be a product of distinct odd primes rather than simply T. The parameter page (fef) that would justify this was not opened. (the reader followed the steps but not why they lead where they do: say what this step is for)

## Previous version (revise it)

It has 374 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 467 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Splitting each input into digits in a large power-of-two radix turns the integer product into a convolution of short integer sequences, and the sizes chosen here make a [Cyclic convolution](convolution.md) agree exactly with the ordinary product.

Call the two inputs $u$ and $v$. Let $n$ be the number of bits in each input, and let $b=\lceil\log_2 n\rceil$ be the number of bits in one digit, so $n\le 2^b$. Two more lengths come from [parameter choice](parameter-choice.md). $T$ is the padded length, a power of two with $4n/b\le T<8n/b$. $S$ is the length of the cyclic convolution, a product of distinct odd primes with $T/2<S<T$.

Let $q=\lceil n/b\rceil$ be the number of digits in each input, padding with leading zeros; on this page $q$ is the digit count, not the length of the sequences being convolved as on the convolution page. Here $S$, $T$ and $v$ also differ from their meanings on earlier pages. Write $u=\sum_{i=0}^{q-1}u_i2^{bi}$ and $v=\sum_{k=0}^{q-1}v_k2^{bk}$, where the digits $u_i$ and $v_k$ are integers with $0\le u_i,v_k<2^b$. Let $x$ be a polynomial variable, and form the polynomials in $x$ with the $u_i$ and with the $v_k$ as coefficients. Evaluating them at $x=2^b$ returns $u$ and $v$, so $uv$ is the value at $2^b$ of their product. Let $c_j=\sum_{i+k=j}u_iv_k$ be the coefficient of $x^j$ in that product. The $c_j$ can exceed $2^b$, so the last step is to evaluate at $2^b$ with carries, which gives the binary number.

## No wraparound

Each digit polynomial has degree at most $q-1$, so the product polynomial has degree at most $2q-2$. Since a ceiling is less than its argument plus 1, $q<n/b+1$ and so $2q-2<2n/b$. Also $2n/b\le T/2$ because $T\ge 4n/b$, and $T/2<S$. Hence $2q-2<2n/b\le T/2<S$ <cite data-source="paper">2q-2<2n/b\le T/2<S.</cite>

The cyclic convolution of length $S$ is the product modulo $x^S-1$, where $x^S=1$ folds the term $x^j$ onto $x^{j \bmod S}$. Every exponent $j$ is at most $2q-2<S$, so nothing folds. The cyclic convolution of the two zero-padded digit sequences therefore equals $c_0,\dots,c_{S-1}$, with zeros after $c_{2q-2}$. For example, with $q=3$ the product has degree 4. Length $S=5$ is safe, but $S=4$ would fold $c_4$ onto $c_0$.

## Size of the coefficients

Each $c_j$ is a sum of at most $q$ products $u_iv_k$, each between $0$ and $(2^b-1)^2$. Hence $0\le c_j\le q(2^b-1)^2$. Since $q\le n\le 2^b$, this is below $2^b\cdot 2^{2b}=2^{3b}$ <cite data-source="paper">0\le c_j\le q(2^b-1)^2<2^{3b},</cite>.

So every coefficient is a nonnegative integer of at most $3b$ bits. Any approximation of $c_j$ with error below $1/2$ rounds to $c_j$, which is how [error tracking](precision-recovery.md) recovers exact integers after the approximate transforms.

Multiplication therefore reduces to a [Cyclic convolution](convolution.md) of length $S$ on short integer coefficients.

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

Write the body to `exegenius/tasks/0367-write-radix-digit-reduction.answer.md` and the JSON to `exegenius/tasks/0367-write-radix-digit-reduction.answer.json`, then run `exegenius submit 0367-write-radix-digit-reduction` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0367-write-radix-digit-reduction`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
