# exegenius task 0313-write-multiplication-algorithm

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
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity (also: chirp transform)
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Error tracking and exact recovery (also: synthetic transform error, source transform error)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange, costly recursive primitive)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition (also: exceptional addresses)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout for synthetic transforms
- Convolution from the retained transform layout
- Parameter and prime-length choice
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
- Tensor products of subspaces (also: tensor product of subspaces, tensor product)

## This page

Concept: The multiplication algorithm
Gloss: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

## This page in the argument

The step: The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$.
How: Reduce the integer product to a cyclic convolution of $S$ short coefficients and compute it through the chain of reductions (digits, CRT address map, Gaussian resampling with chirps, twist to the polynomial ring, synthetic-transform convolution); recover exact integers because the accumulated error is below $1/2$.
Why: Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. (the sources say so: "Splitting the inputs into radix digits reduces multiplication to" (paper))

Its sub-steps, in order:

- Fixed rational exponents and sizes make every hypothesis of the lemmas hold: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$, $t_d=r$, and distinct odd primes $s_i\in((1-2\eta)t_i,(1-\eta)t_i]$. (on [Parameter and prime-length choice](parameter-choice.md))
- Writing the two inputs in radix $2^b$ with $q=\lceil n/b\rceil$ digits each, the product polynomial has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and every coefficient $c_j\le q(2^b-1)^2<2^{3b}$. (on [Multiplication as radix-digit convolution](radix-digit-reduction.md))
- The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod_ix_i^{\mu_i}$, is an isomorphism preserving cyclic convolution, and it (with its inverse and padding) is implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^\tau))$ time. (on [Chinese-remainder address map](crt-map.md))
- With $\zeta=e^{\pi i/r}$ the map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$, is an isomorphism multiplying coefficient $k$ by $\zeta^k$; hence normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$. (on [Phase twist](phase-twist.md))
- The computed chirp transform $\widetilde{\mathscr C}$ and the source transform $\widetilde{\mathscr F}$ (apply $\mathcal A$, the chirp transform, $\mathcal B_0$, then multiply by $2^\gamma$) have exact counterparts $QF_{\boldsymbol t}$ and $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.
- The algorithm: read radix digits, apply $\Phi$, compute the source transforms $\widetilde{\mathscr F}(u)$, $\widetilde{\mathscr F}(v)$, multiply pointwise, apply the opposite transform, rescale by $S$ and $2^{2b+4}S$, round, undo $\Phi$ and propagate carries to output exactly $2n$ bits.
- The error on the recovered integer coefficients is below $1/2$, so rounding gives the exact integer coefficients, and carry propagation yields the exact binary product. (on [Error tracking and exact recovery](precision-recovery.md))

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.5, S5.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.5**: The computed chirp transform $\widetilde{\mathscr C}$ and the source transform $\widetilde{\mathscr F}$ (apply $\mathcal A$, the chirp transform, $\mathcal B_0$, then multiply by $2^\gamma$) have exact counterparts $QF_{\boldsymbol t}$ and $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.
How: Evaluate $QF_{\boldsymbol t}$ by the chirp identity: pointwise phase, complex convolution with the chirp, pointwise phase; compose with the Gaussian maps and the exact scale $2^\gamma$.
- S5.5.1: The data operand after the first endpoint phase is $x_0=Q_p(\overline{\widetilde a}\cdot x)$.
  Source: "x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\" (paper)
  > Let $\widetilde a$ be the resulting disk-grid array, so $\|\widetilde a-a\|_\infty<2\,2^{-p}$. For a disk-grid target tensor $x$ of norm at most $.6$, the computed chirp transform forms the arrays \[ \begin{aligned} x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\ y_0&=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0),\\ \widetilde{\mathscr C}(x) &=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0). \end{aligned} \] Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data operand after the first endpoint phase. Replacing the approximations by exact phases and exact convolution gives $\overline a\mathbin{\cdot}\mathcal M_{\mathbb C} (a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by \eqref{eq:permuted-chirp}. Below we show that $\|x\|_\infty\le.6$ implies $\|x_0\|_\infty\le.6$, which supplies the smaller operand required by the computed convolution.
- S5.5.2: The computed chirp transform is $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$ with $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$.
  Source: "Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0)" (paper)
  > Let $\widetilde a$ be the resulting disk-grid array, so $\|\widetilde a-a\|_\infty<2\,2^{-p}$. For a disk-grid target tensor $x$ of norm at most $.6$, the computed chirp transform forms the arrays \[ \begin{aligned} x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),\\ y_0&=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0),\\ \widetilde{\mathscr C}(x) &=Q_p(\overline{\widetilde a}\mathbin{\cdot}y_0). \end{aligned} \] Thus $\widetilde a$ is the convolution kernel and $x_0$ is the data operand after the first endpoint phase. Replacing the approximations by exact phases and exact convolution gives $\overline a\mathbin{\cdot}\mathcal M_{\mathbb C} (a,\overline a\mathbin{\cdot}x)=QF_{\boldsymbol t}x$ by \eqref{eq:permuted-chirp}. Below we show that $\|x\|_\infty\le.6$ implies $\|x_0\|_\infty\le.6$, which supplies the smaller operand required by the computed convolution.
- S5.5.3: The exact counterpart of the source transform is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.
  Source: "\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A" (paper)
  > For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**S5.6**: The algorithm: read radix digits, apply $\Phi$, compute the source transforms $\widetilde{\mathscr F}(u)$, $\widetilde{\mathscr F}(v)$, multiply pointwise, apply the opposite transform, rescale by $S$ and $2^{2b+4}S$, round, undo $\Phi$ and propagate carries to output exactly $2n$ bits.
How: Write each radix digit $a_j$ as the exact grid value $a_j2^{-b-2}$ so inputs have norm below $1/4$, and run six explicit operations whose exact counterpart is $(u*v)/S^2$ scaled back to the integer coefficient convolution.
- S5.6.1: For digit $a_j$ write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word followed by a zero imaginary word, represented value $a_j2^{-b-2}$ (nonnegative exponent because $p=6b$); append $S-q$ zero records.
  Source: "$a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero" (paper)
  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.
- S5.6.2: Step 1: apply the coefficient-address map $\Phi$ with its padded layout to obtain source arrays $u,v$ of exact $p$-bit grid values of norm less than $1/4$.
  Source: "\item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)
  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$
- S5.6.3: Step 2: compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
  Source: "\item Compute $\widetilde{\mathscr F}(u)$ and" (paper)
  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to
- S5.6.4: Step 3: multiply corresponding complex coefficients exactly and truncate each part toward zero to $p$ fractional bits, obtaining $z$.
  Source: "\item Multiply corresponding complex coefficients exactly and truncate" (paper)
  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed
- S5.6.5: Step 4: compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, obtaining $\widetilde w$.
  Source: "\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid" (paper)
  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficien
- S5.6.6: Step 5: multiply by $2^{2b+4}S$, round the real values to the nearest integers, write each as a signed $(3b+1)$-bit word (zero at padded addresses), and apply $\Phi^{-1}$ with padding removal.
  Source: "\item Multiply the grid numerators of $\widetilde w$ exactly by" (paper)
  > ficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \
- S5.6.7: Step 6: propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.
  Source: "\item Propagate radix-$2^b$ carries in increasing coefficient order." (paper)
  > rs exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \end{enumerate}
- S5.6.8: The two occurrences of $S$ undo different normalizations: the exact counterpart after three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$.
  Source: "The two occurrences of $S$ in this algorithm undo different" (paper)
  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S5.1 (on [Parameter and prime-length choice](parameter-choice.md)): Fixed rational exponents and sizes make every hypothesis of the lemmas hold: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a power of two $T\in[4n/b,8n/b)$, $r=2^{\lceil(\log_2T)/d\rceil}$, axis lengths $t_i\in\{r/2,r\}$ with $\prod t_i=T$, $t_d=r$, and distinct odd primes $s_i\in((1-2\eta)t_i,(1-\eta)t_i]$.
- S5.2 (on [Multiplication as radix-digit convolution](radix-digit-reduction.md)): Writing the two inputs in radix $2^b$ with $q=\lceil n/b\rceil$ digits each, the product polynomial has degree at most $2q-2<2n/b\le T/2<S$, so convolution modulo $x^S-1$ has no wraparound, and every coefficient $c_j\le q(2^b-1)^2<2^{3b}$.
- S5.3 (on [Chinese-remainder address map](crt-map.md)): The Chinese-remainder map $\Phi:\mathbb C[x]/(x^S-1)\to\mathbb C[x_1,\dots,x_d]/(x_i^{s_i}-1)$, $x\mapsto\prod_ix_i^{\mu_i}$, is an isomorphism preserving cyclic convolution, and it (with its inverse and padding) is implemented by triangular controlled shifts in $O(Tp\,d^2(1+\ell^\tau))$ time.
- S5.4 (on [Phase twist](phase-twist.md)): With $\zeta=e^{\pi i/r}$ the map $\Theta:\mathbb C[x_d]/(x_d^r-1)\to\mathcal R_r$, $x_d\mapsto\zeta y$, is an isomorphism multiplying coefficient $k$ by $\zeta^k$; hence normalized complex cyclic convolution is $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$.
- S5.7 (on [Error tracking and exact recovery](precision-recovery.md)): The error on the recovered integer coefficients is below $1/2$, so rounding gives the exact integer coefficients, and carry propagation yields the exact binary product.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Bluestein chirp identity](chirp.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)

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
- $\mathsf S_\Omega$ (array network), bound on [Frames on wire arrays](array-frames.md): The network obtained by applying every gate pointwise on arrays over the address set, acting on all wire arrays together.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $t$ (gate fan-in), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of a gate.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (address count), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): A power of two with 4n/b <= T < 8n/b, the padded length from parameter choice.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of digits in each input.
- $u_i$ (digit of u), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The digit of u of weight 2^{bi}, an integer below 2^b.
- $v_k$ (digit of v), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The digit of v of weight 2^{bk}, an integer below 2^b.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The indeterminate of the digit polynomials.
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
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The radix: the number of values one digit can take (not a sequence length here).
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values in the array indexed by [P]x[R]x[B].
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in each prefix (not the scalar ring).
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which rows are dealt.
- $j$ (digit value), bound on [Elementary stream operations](stream-ops.md): A value of the chosen digit in the splitting example.
- $\boldsymbol j$ (index tuple), bound on [Bluestein chirp identity](chirp.md): The tuple of indices (j_1,...,j_d), one per axis, locating an entry of an array.
- $\boldsymbol t$ (axis lengths), bound on [Bluestein chirp identity](chirp.md): The tuple (t_1,...,t_d) of axis lengths, where t_i is the even number of entries along axis i.
- $s_i$ (coprime multiplier), bound on [Bluestein chirp identity](chirp.md): An integer coprime to the axis length t_i.
- $F_{\boldsymbol t}$ (normalized transform), bound on [Bluestein chirp identity](chirp.md): The normalized multidimensional discrete Fourier transform with axis lengths t.
- $\boldsymbol k$ (input position), bound on [Bluestein chirp identity](chirp.md): The index tuple of an input entry.
- $\boldsymbol f$ (frequency), bound on [Bluestein chirp identity](chirp.md): The tuple of frequencies labelling an output entry of the transform.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a phase quadratic in the index.
- $N$ (factor bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers given to the established multiplier.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The base 2^{4p} at which the polynomials are evaluated.
- $A_u$ (signed evaluation integer), bound on [Signed packing](signed-packing.md): The integer obtained by evaluating the integer-coefficient polynomial u at B_0.
- $\gamma_j$ (carry), bound on [Signed packing](signed-packing.md): The carry, in {-1,0}, into block j when forming A_u.
- $d_j$ (block), bound on [Signed packing](signed-packing.md): The residue of u_j plus the carry modulo B_0, the j-th block of 4p bits of A_u.
- $h_j$ (product coefficient), bound on [Signed packing](signed-packing.md): The coefficient of y^j in the ordinary product h=ac of integer polynomials.
- $\rho_j$ (extraction carry), bound on [Signed packing](signed-packing.md): The carry into block j during extraction, in {0,1}.
- $H_j$ (reduced coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime radix), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The prime radix of the stored digits.
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-q digits of a field.
- $Q$ (field size), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take, q^b.
- $y$ (field value), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The value of the target field, between 0 and Q-1.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of digits that follow the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q, by which the field is multiplied.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of times cy wraps past Q.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank of A), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the rational matrix A.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in each field.
- $q$ (fixed odd prime), bound on [Matrix shear by triangular factorization](matrix-shear.md): The fixed odd prime modulus base of the fields.
- $H$ (target group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The first group of m fields, which receives AD.
- $D$ (source group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The second group of m fields, which is left unchanged.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rational m by m matrix whose shear is performed.
- $E_1$ (left triangular factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): The invertible lower triangular matrix on the left of the factorization of A; E_2 is the one on the right.
- $\Pi$ (partial permutation), bound on [Matrix shear by triangular factorization](matrix-shear.md): The matrix with exactly a ones, at most one per row and column, in the factorization of A.
- $a$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, a coefficient of the kernel.
- $b$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, a coefficient of the kernel; not a bit index.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix swapping the two entries of a pair.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The two-point kernel aI + bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1,i) multiplying the second entry of a pair by i.
- $H_0$ (averaging step matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix of the two-point averaging and differencing step.
- $H$ (normalized Hadamard), bound on [Two-point kernel C](phase-kernel.md): The Hadamard matrix sqrt(2) H_0.
- $L$ (linear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A map linear in each of its two operands.
- $u'$ (computed input), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed input that replaces the exact input u.
- $f'$ (computed first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing f.
- $g'$ (computed second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The computed operand replacing g.
- $F_q$ (normalized transform), bound on [Contractions and bilinear contractions](contraction-maps.md): The normalized discrete Fourier transform on sequences of q entries.
- $f$ (first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The first operand of the bilinear map.
- $g$ (second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The second operand of the bilinear map.
- $i$ (axis index), bound on [Multidimensional transforms](multidim-transform.md): The index of an axis of the array, from 1 to d.
- $q_i$ (axis position count), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $j$ (index tuple), bound on [Multidimensional transforms](multidim-transform.md): The tuple of coordinates (j_1,...,j_d) of an entry of the array.
- $k$ (output index tuple), bound on [Multidimensional transforms](multidim-transform.md): An output index tuple shaped like j.
- $G_i$ (axis operator), bound on [Multidimensional transforms](multidim-transform.md): An operator on sequences of length q_i, applied to every line along axis i.
- $\delta$ (time-bound slack), bound on [Multidimensional transforms](multidim-transform.md): A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
- $\alpha$ (resampling parameter), bound on [Multidimensional transforms](multidim-transform.md): An integer resampling parameter with 2<=alpha<sqrt p.
- $\boldsymbol s$ (source lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of source axis lengths (s_1,...,s_d).
- $\boldsymbol t$ (padded lengths), bound on [Multidimensional transforms](multidim-transform.md): The tuple of padded power-of-two axis lengths (t_1,...,t_d).
- $\gamma$ (scalar exponent), bound on [Multidimensional transforms](multidim-transform.md): The total exponent 2d alpha^2 of the power of two multiplying the tensored identity.
- $R$ (source permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the source index permutations P_{s_i}; here not the scalar ring.
- $Q$ (padded permutation), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the index permutations P_{t_i}.
- $\mathcal A$ (input map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional input maps A_i.
- $\mathcal B_0$ (output map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-dimensional output maps B_{0,i}.
- $P_{s_i}$ (source axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of source axis i.
- $P_{t_i}$ (padded axis permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation of padded axis i.
- $A_i$ (axis input map), bound on [Multidimensional transforms](multidim-transform.md): The linear input map of axis i.
- $B_{0,i}$ (axis output map), bound on [Multidimensional transforms](multidim-transform.md): The linear output map of axis i.
- $F_{q_i}$ (axis transform), bound on [Multidimensional transforms](multidim-transform.md): The one-dimensional normalized discrete Fourier transform of length q_i.
- $F_{\boldsymbol q}$ (multidimensional transform), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the axis transforms F_{q_i}.
- $X_i$ (axis operator X), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $Y_i$ (axis operator Y), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of cyclic axis i of the source; the lengths are pairwise coprime.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths s_j with j<i.
- $\mu_i$ (axis exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i, used as the exponent of x_i.
- $\Phi$ (Chinese-remainder map), bound on [Chinese-remainder address map](crt-map.md): The algebra isomorphism from the cyclic ring of length S to the product of cyclic axes.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The polynomial variable of axis i, with x_i^{s_i}=1.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): A single coefficient index, an exponent of x, not an index tuple.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The digit of k in position j of its mixed-radix expression, with 0 <= a_j < s_j.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The coordinate in axis i of the image of x^k.
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of an axis of length r, with r = 2^ell.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the axis lengths t_i.
- $\tau$ (interchange exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the chunk-interchange time bound.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis, from 1 to d.
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i after zero padding, either r/2 or r.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the prime-length Fourier transform being re-expressed.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative excess t/s-1 of the padded length over the source length.
- $\mathsf S$ (input resampling), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted map from length-s to length-t complex vectors applied before the power-of-two transform.
- $\mathsf T$ (output resampling), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian-weighted map from length-s to length-t complex vectors on the transform side of the identity.
- $q_j$ (nearest coordinate), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest tj/s, the coordinate of the length-t vector selected for index j.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The difference tj/s-q_j between tj/s and its nearest integer.
- $C$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-t to length-s vectors that picks coordinate q_j for each j.
- $\mathsf D$ (Gaussian diagonal), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map multiplying coordinate j by e^{pi alpha^2 beta_j^2}.
- $N$ (approximate identity), bound on [Gaussian resampling](gaussian-resampling.md): The map C T D on length-s vectors, close to the identity.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single coordinate index of a vector, not an index tuple.
- $j$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single coordinate index of a vector, not an index tuple.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer with 2<=alpha<sqrt p setting the width of the Gaussian weights.
- $t$ (padded length), bound on [Gaussian resampling](gaussian-resampling.md): The nearby larger transform length, a power of two, into which the length-s transform is resampled.
- $z$ (input vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries to which the transform is applied.
- $F_q^+$ (opposite transform), bound on [Retained permutation cancellation](retained-permutations.md): The discrete Fourier transform of length q with the sign of the exponent reversed.
- $\beta$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): A unit modulo q, used to define the index permutation R_beta.
- $w$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The summation index in the Fourier sum.
- $w'$ (new summation index), bound on [Retained permutation cancellation](retained-permutations.md): The summation index obtained as beta times w.
- $\nu$ (setup exponent), bound on [Retained permutation cancellation](retained-permutations.md): The fixed exponent of p bounding the setup work per line.
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer, transformed along the axes.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer, transformed along the axes.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The spacing $2^{-p}$ of the fixed-point grid.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length $T$; not the linear map $L$ of the contractions page.
- $a$ (error size), bound on [Error tracking and exact recovery](precision-recovery.md): The size of an error, counted in grid spacings $h_p$.
- $e$ (unit phase), bound on [Error tracking and exact recovery](precision-recovery.md): A phase of modulus one that multiplies an array.
- $\widetilde e$ (phase approximation), bound on [Error tracking and exact recovery](precision-recovery.md): A grid approximation of the unit phase $e$ within $2h_p$.
- $x$ (disk operand), bound on [Error tracking and exact recovery](precision-recovery.md): An array in the unit disk to which a phase or chirp transform is applied; not the digit-polynomial variable.
- $E_{\rm ring}$ (ring convolution error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound $M(3L+2)$ of the returned ring convolution, in units of $h_p$.
- $E_s$ (source transform error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound $9\cdot2^\gamma TL$ of the computed source transform, in units of $h_p$.
- $\widetilde{\mathscr C}$ (computed chirp transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed chirp transform built from phase products and a complex convolution.
- $\widetilde{\mathscr F}$ (computed source transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed source transform: expansion, chirp transform, compression, then scaling by $2^\gamma$.
- $u$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the first input, each digit stored as its value times $2^{-b-2}$; not the integer.
- $v$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled radix digits of the second input, each digit stored as its value times $2^{-b-2}$; not the integer.
- $U$ (exact first transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact source transform of the first digit array.
- $V_1$ (exact second transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact source transform of the second digit array.
- $\widetilde U$ (computed first transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed source transform of the first digit array.
- $\widetilde V_1$ (computed second transform), bound on [Error tracking and exact recovery](precision-recovery.md): The computed source transform of the second digit array.
- $z$ (truncated product), bound on [Error tracking and exact recovery](precision-recovery.md): The truncated pointwise product of the two computed source transforms.
- $G$ (exact opposite transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact opposite-sign source transform $RF_{\boldsymbol s}^+$, a contraction.
- $w$ (first scaled result), bound on [Error tracking and exact recovery](precision-recovery.md): The convolution $(u*v)/S$ of the digit arrays divided by $S$, whose scaling by $2^{2b+4}S$ gives the integer coefficients.
- $\widetilde w$ (computed first scaled result), bound on [Error tracking and exact recovery](precision-recovery.md): The computed approximation of $w$ after exact multiplication by $S$.
- $E_w$ (scaled error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound $S(3E_s+2)$ of $\widetilde w$, in units of $h_p$.
- $Q_0$ (radix), bound on [Error tracking and exact recovery](precision-recovery.md): The radix $2^b$ of the digits used in carry propagation.
- $k_j$ (carry), bound on [Error tracking and exact recovery](precision-recovery.md): The carry into position $j$ in carry propagation.
- $d_j$ (output digit), bound on [Error tracking and exact recovery](precision-recovery.md): The $j$-th radix-$2^b$ digit of the product.
- $\tau$ (chunk-interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (recursion growth exponent), bound on [Parameter and prime-length choice](parameter-choice.md): An upper bound on the growth exponent of recursive calls (a new meaning of sigma).
- $\beta$ (handling threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent setting the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent.
- $\lambda'$ (layer-cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the layer cost V d^{lambda'}.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The bit volume on which the layer cost is measured.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width (a new meaning of c).
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count.
- $C_1$ (guard exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The slack in the resampling cost exponent.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk.
- $\eta$ (prime offset), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
- $x$ (interval scale), bound on [Parameter and prime-length choice](parameter-choice.md): A real number above e^{2/eta} scaling the interval searched for primes.
- $q$ (interval integer), bound on [Parameter and prime-length choice](parameter-choice.md): An integer in the interval (1-2eta)x < q <= (1-eta)x.
- $a_d$ (d lower constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the lower bound on d.
- $b_d$ (d upper constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the upper bound on d.
- $a_r$ (r lower constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the lower bound on r.
- $b_r$ (r upper constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the upper bound on r.
- $C_\ell$ (d-ell constant), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed positive constant in the bound d l <= C_l p.
- $E$ (first space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The first of the two finite-dimensional vector spaces being tensored.
- $G$ (second space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The second of the two finite-dimensional vector spaces being tensored.
- $A$ (ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace P.
- $C$ (second ambient space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A subspace of C.
- $B$ (orthogonal complement), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The orthogonal complement of P in A.
- $F$ (base space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $s$ (number of smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration.
- $U$ (a label subspace), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A subspace of the label space, such as the label of a vertex.
- $F$ (one-factor label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $x$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the first argument of the bilinear form.
- $y$ (vector of F), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A vector of $F$, the second argument of the bilinear form.
- $t_S$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of the triple $S$.
- $\mathcal F$ (ambient label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $F^{\otimes3}$, of dimension $m=h^3$, in which all labels lie.
- $X$ (X bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $X_a$.
- $Y$ (Y bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $Y_a$.
- $U_a$ (terminal line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of dimensions lost on decreasing edges.
- $j$ (stage number), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $P$ (earlier tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $A'$ (next exposed space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $A$, equal to $A\otimes F$.
- $P'$ (next earlier line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $P$, equal to $P\otimes\langle t_{a_j}\rangle$.
- $B'$ (next complement), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $B$, the orthogonal complement of $P'$ in $A'$.
- $K'$ (next later line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The next stage's $K$, with $K=\langle t_{a_{j+1}}\rangle\otimes K'$.
- $t_X$ (X-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the X-bank triple of a gate or side wire in one invocation.
- $t_Y$ (Y-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the Y-bank triple of a gate or side wire in one invocation.
- $L_{\rm b}$ (bit dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the bit network.
- $L_{\rm c}$ (complex dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the complex network.
- $\Pi_U$ (projection onto a label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The rational projection onto the label $U$ along $U^\perp$, the matrix of a bit-network vertex labelled $U$.
- $V$ (larger label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A label containing the label $U$ at the other end of an edge.
- $s_{\rm b}$ (bit smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total rational rank of edge matrix differences, in the bit network.
- $s_{\rm c}$ (complex smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total number of phase kernels, in the complex network.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes of a layer.
- $F$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter, divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels below the top call, indexing the terms of the unrolled sum.
- $\eta$ (relative rank deficit), bound on [Recursive power saving](rank-recurrence.md): The relative deficit (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two chunks.
- $V$ (array volume), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits stored in the array.
- $\tau$ (saving exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below 1 in the cost of the interchange.
- $p$ (address prefix), bound on [Fast address-chunk interchange](address-interchange.md): The prefix part of an address, before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The first of the two address chunks to be interchanged.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The second of the two address chunks to be interchanged.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The part of the address between the two chunks.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The part of the address after the second chunk.
- $q$ (digit radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime radix of the digits.
- $H$ (first chunk value), bound on [Fast address-chunk interchange](address-interchange.md): The value of the first chunk, the target of the shear.
- $D$ (second chunk value), bound on [Fast address-chunk interchange](address-interchange.md): The value of the second chunk, the source of the shear.
- $e$ (chunk digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of digits in each chunk.
- $k$ (recursion levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational m by m matrix carried by a vertex of the network.
- $i$ (edge index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an edge of the network.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of an input wire of the network.
- $\rho$ (output role map), bound on [Fast address-chunk interchange](address-interchange.md): The map sending input wire w to its output role rho(w).
- $I_m$ (identity matrix), bound on [Fast address-chunk interchange](address-interchange.md): The m by m identity matrix.
- $\Phi$ (address-shear permutation), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address (H,D) to (H+MD,D) for a matrix M.
- $x$ (stream row number), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $f_w$ (input array), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $F_k$ (time per unit volume), bound on [Fast address-chunk interchange](address-interchange.md): The running time divided by the volume for chunks of m^k digits.
- $j$ (level index), bound on [Fast address-chunk interchange](address-interchange.md): An index of recursion levels in the unrolled sum.
- $k'$ (levels needed), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels needed for chunks of e digits.
- $\nu$ (set-aside digit count), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk set aside to form the row field.
- $h^+$ (top digits of h), bound on [Fast address-chunk interchange](address-interchange.md): The top digits of h after splitting each chunk into its top digits and rest.
- $h^-$ (rest of h), bound on [Fast address-chunk interchange](address-interchange.md): The rest of h after splitting each chunk into its top digits and rest.
- $d^+$ (top digits of d), bound on [Fast address-chunk interchange](address-interchange.md): The top digits of d after splitting each chunk into its top digits and rest.
- $d^-$ (rest of d), bound on [Fast address-chunk interchange](address-interchange.md): The rest of d after splitting each chunk into its top digits and rest.
- $\Lambda$ (row field range), bound on [Fast address-chunk interchange](address-interchange.md): The range of the row field formed by the two sets of top digits.
- $\Lambda'$ (padded row count), bound on [Fast address-chunk interchange](address-interchange.md): The row count after padding with zero rows to a multiple of W^{k'}.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j into which each remaining chunk is cut, a base-m digit.
- $v$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m; on this page v is not a number of triples.
- $E$ (edge residual), bound on [Binary phase frames](phase-frames.md): The orthogonal complement of the tail label inside the head label of an edge; not a tensor factor.
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns of data, tensored together; not a depth.
- $u$ (binary vector), bound on [Binary phase frames](phase-frames.md): A binary vector in F_2^m.
- $w$ (binary vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m.
- $z$ (binary vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m.
- $\operatorname{supp}(z)$ (support), bound on [Binary phase frames](phase-frames.md): The set of coordinates where the vector z is 1.
- $\operatorname{wt}(x)$ (Hamming weight), bound on [Binary phase frames](phase-frames.md): The number of coordinates of x equal to 1, an integer.
- $[b]$ (integer representative), bound on [Binary phase frames](phase-frames.md): The integer 0 or 1 representing b in F_2.
- $P_U$ (projection onto a label), bound on [Binary phase frames](phase-frames.md): The projection onto the label U, taken over F_2.
- $X_v$ (translation by v), bound on [Binary phase frames](phase-frames.md): The operator (X_v f)(x)=f(x+v).
- $q_U$ (weight phase exponent), bound on [Binary phase frames](phase-frames.md): The Hamming weight of P_U x modulo 4, the exponent of i in the phase of label U.
- $\mathcal C_U$ (phase frame), bound on [Binary phase frames](phase-frames.md): The operator H^{\otimes m} diag(i^{q_U(x)}) H^{\otimes m} attached to the label U.
- $\mathcal B$ (orthonormal basis), bound on [Binary phase frames](phase-frames.md): An orthonormal basis of the edge residual E.
- $\varepsilon$ (edge sign), bound on [Binary phase frames](phase-frames.md): The sign +1 or -1 (modulo four) of a basis vector's phase coefficient, including the edge direction.
- $Z$ (sign matrix), bound on [Binary phase frames](phase-frames.md): The 2 by 2 diagonal matrix diag(1,-1).
- $Z_{a,k}$ (sign operator), bound on [Binary phase frames](phase-frames.md): Z on the 27 coordinates of supp(u) in every column, identity elsewhere.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected address chunks, at most d.
- $e$ (selected axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of selected axes in a group, e = mf.
- $z$ (array), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An array on which the diagonal operator acts.
- $\xi$ (residual index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The index of a residual basis vector and its slot.
- $\Gamma$ (basis-change matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An invertible F_2 matrix whose first columns are the residual basis vectors.
- $\mathcal P_\Gamma$ (address permutation), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The address permutation sending x to Gamma x.
- $\mathbf 1_\xi$ (standard basis vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The xi-th standard basis vector.
- $q_0$ (individual chunks), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of leading chunks given individual C kernels, whose bits form the row index.
- $\chi$ (chain operation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound on the operations on a chain from an input to an intermediate coefficient.
- $E$ (invocation operation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A bound on the operations in one invocation of the network.
- $\Psi$ (level factor), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sum s + psi, the factor by which the chain bound grows per level.
- $\varphi$ (chain bound value), bound on [Simultaneous butterfly layer](simultaneous-layer.md): Any bound of at least one on a chain length.
- $\vartheta$ (exponent of m), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The least j at least 1 with m^j at least Psi; an exponent, not a digit count.
- $C_0$ (guard constant), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The constant 128 m Psi^2 in the guard width Delta.
- $D$ (transformed axes), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of transformed axes, d-1.
- $\tau$ (interchange exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The exponent below 1 in the cost O(V u^tau) of a chunk interchange.
- $\lambda'$ (layer exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The exponent below 1 in the cost of a simultaneous butterfly layer.
- $B$ (bit reversal), bound on [Tape layout for synthetic transforms](transform-layout.md): The bit-reversal permutation applied along every axis.
- $b$ (leftover low bits), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of leftover low bits of an axis after whole chunks.
- $q$ (whole chunks), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of whole K-bit chunks of an axis.
- $L$ (layout permutation), bound on [Tape layout for synthetic transforms](transform-layout.md): The record permutation defined by the prefix moves and chunk exchanges.
- $z$ (round input), bound on [Tape layout for synthetic transforms](transform-layout.md): The array entering a round.
- $P$ (pointwise product), bound on [Convolution from the retained transform layout](ring-convolution.md): The pointwise product $uv/r$ of two arrays of ring elements, not a prefix count or a subspace.
- $L$ (layout permutation), bound on [Convolution from the retained transform layout](ring-convolution.md): The permutation of records made by the tape layout, not a linear map, a loss or a chunk length.
- $B$ (bit-reversal order), bound on [Convolution from the retained transform layout](ring-convolution.md): The bit-reversal order of records, not a complement, a level factor or a row length.
- $\ell$ (log of record length), bound on [Convolution from the retained transform layout](ring-convolution.md): The base-2 logarithm of the record length r; not a depth.
- $\delta$ (forward error bound), bound on [Convolution from the retained transform layout](ring-convolution.md): The bound on the error of each forward or opposite transform procedure, $\sqrt2\ell 2^{-p}$.
- $\eta$ (truncation error bound), bound on [Convolution from the retained transform layout](ring-convolution.md): The bound $\sqrt2\,2^{-p}$ on the change made by one truncation; not a relative deficit.
- $K$ (layout chunk width), bound on [Convolution from the retained transform layout](ring-convolution.md): The width in bits of an address chunk in the tape layout; not a tensor line or a segment spacing.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multiplication as radix-digit convolution](radix-digit-reduction.md): Splitting each integer into radix-2^b digits turns the product into a convolution of short integer coefficients, which carry propagation turns back into a binary number.
  Shown as: The multiplication algorithm *<predicate>* Multiplication as radix-digit convolution
- [Chinese-remainder address map](crt-map.md): An isomorphism that places a cyclic convolution of length S = s₁⋯s_d on pairwise coprime prime axes, implemented as triangular controlled shifts.
  Shown as: The multiplication algorithm *<predicate>* Chinese-remainder address map
- [Retained permutation cancellation](retained-permutations.md): Leaving the coordinate permutations of resampling inside the transform identity, so the source permutation cancels across the two forward transforms and the opposite one and none is executed as a sort.
  Shown as: The multiplication algorithm *<predicate>* Retained permutation cancellation
- [Phase twist](phase-twist.md): Multiplying coefficient k by e^{πik/r}, which converts the cyclic coordinate modulo x^r − 1 into the negacyclic ring modulo y^r + 1 and is removed afterwards.
  Shown as: The multiplication algorithm *<predicate>* Phase twist
- [Convolution from the retained transform layout](ring-convolution.md): Convolution over the ring modulo y^r + 1 on the remaining axes by two forward synthetic transforms, pointwise polynomial products and the opposite transform, normalized by 1/(rM).
  Shown as: The multiplication algorithm *<predicate>* Convolution from the retained transform layout
- [Parameter and prime-length choice](parameter-choice.md): Fixed rational exponents and sizes (precision p = 6b, d axes, K = d^c, T and r powers of two, prime lengths s_i just below t_i) making every hypothesis of the lemmas hold.
  Shown as: The multiplication algorithm *<predicate>* Parameter and prime-length choice
- [Error tracking and exact recovery](precision-recovery.md): Each normalized transform and product is a contraction with a bounded rounding error, and the total error on the recovered convolution coefficients is below 1/2, so rounding gives exact integers.
  Shown as: The multiplication algorithm *<predicate>* Error tracking and exact recovery

## Pages that build on this one

- Cost accounting and the exponent κ: Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}).
- Power-saving integer multiplication: A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
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
- [Gaussian resampling](gaussian-resampling.md)
- [Retained frequency order](frequency-order.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "The multiplication algorithm" (paper)

  > \subsection{The multiplication algorithm}

- "The two occurrences of $S$ in this algorithm undo different normalizations." (paper)

  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $b$ means digit width here, but field digit count on [Controlled shifts and rational scalings](controlled-shifts.md), which this page builds on: On this page $b$ means the digit width in bits, but the controlled-shifts page uses $b$ for the number of base-q digits of a field. Use another letter here, or say that $b$ means the digit width in bits here, not the number of base-q digits of a field as on the controlled-shifts page.
- $b$ means digit width here, but lowest bit on [Butterflies and the fast transform](butterfly.md), which this page builds on: On this page $b$ means the digit width in bits, but the butterfly page uses $b$ for the lowest bit of the output index. Use another letter here, or say that $b$ means the digit width in bits here, not the lowest bit of the output index as on the butterfly page.
- $b$ means digit width here, but leftover low bits on [Tape layout for synthetic transforms](transform-layout.md), which this page builds on: On this page $b$ means the digit width in bits, but the tape-layout page uses $b$ for the number of leftover low bits. Use another letter here, or say that $b$ means the digit width in bits here, not the number of leftover low bits as on the tape-layout page.
- $b$ means digit width here, but digits per field on [Matrix shear by triangular factorization](matrix-shear.md), which this page builds on: On this page $b$ means the digit width in bits, but the matrix-shear page uses $b$ for the number of base-q digits per field. Use another letter here, or say that $b$ means the digit width in bits here, not the number of base-q digits per field as on the matrix-shear page.
- $b$ means digit width here, but kernel coefficient on [Two-point kernel C](phase-kernel.md), which this page builds on: On this page $b$ means the digit width in bits, but the phase-kernel page uses $b$ for the kernel coefficient. Use another letter here, or say that $b$ means the digit width in bits here, not the kernel coefficient as on the phase-kernel page.
- $u$ means first source array here, but first input on [Multiplication as radix-digit convolution](radix-digit-reduction.md), which this page builds on: On this page $u$ means the first source array, but the radix-digit page uses $u$ for the first input integer. Use another letter here, or say that $u$ means the first source array here, not the first input integer as on the radix-digit page.
- $u$ means first source array here, but chunk width on [Fast address-chunk interchange](address-interchange.md), which this page builds on: On this page $u$ means the first source array, but the address-interchange page uses $u$ for the chunk width. Use another letter here, or say that $u$ means the first source array here, not the chunk width as on the address-interchange page.
- $u$ means first source array here, but binary vector on [Binary phase frames](phase-frames.md), which this page builds on: On this page $u$ means the first source array, but the binary phase frames page uses $u$ for a binary vector. Use another letter here, or say that $u$ means the first source array here, not a binary vector as on the binary phase frames page.
- $v$ means second source array here, but second input on [Multiplication as radix-digit convolution](radix-digit-reduction.md), which this page builds on: On this page $v$ means the second source array, but the radix-digit page uses $v$ for the second input integer. Use another letter here, or say that $v$ means the second source array here, not the second input integer as on the radix-digit page.
- $v$ means second source array here, but number of triples on [Linear exchange network with restored scratch wires](exchange-network.md), which this page builds on: On this page $v$ means the second source array, but the exchange-network page uses $v$ for the number of triples. Use another letter here, or say that $v$ means the second source array here, not the number of triples as on the exchange-network page.
- $v$ means second source array here, but binary vector on [Binary phase frames](phase-frames.md), which this page builds on: On this page $v$ means the second source array, but the binary phase frames page uses $v$ for a binary vector. Use another letter here, or say that $v$ means the second source array here, not a binary vector as on the binary phase frames page.
- $z$ means pointwise product array here, but round input on [Tape layout for synthetic transforms](transform-layout.md), which this page builds on: On this page $z$ means the pointwise product array, but the tape-layout page uses $z$ for the array entering a round. Use another letter here, or say that $z$ means the pointwise product array here, not the array entering a round as on the tape-layout page.
- $z$ means pointwise product array here, but suffix on [Fast address-chunk interchange](address-interchange.md), which this page builds on: On this page $z$ means the pointwise product array, but the address-interchange page uses $z$ for the suffix of an address. Use another letter here, or say that $z$ means the pointwise product array here, not the suffix of an address as on the address-interchange page.
- $z$ means pointwise product array here, but array on [Simultaneous butterfly layer](simultaneous-layer.md), which this page builds on: On this page $z$ means the pointwise product array, but the simultaneous-layer page uses $z$ for the array acted on by the diagonal operator. Use another letter here, or say that $z$ means the pointwise product array here, not the array acted on by the diagonal operator as on the simultaneous-layer page.
- $z$ means pointwise product array here, but binary vector on [Binary phase frames](phase-frames.md), which this page builds on: On this page $z$ means the pointwise product array, but the binary phase frames page uses $z$ for a binary vector. Use another letter here, or say that $z$ means the pointwise product array here, not a binary vector as on the binary phase frames page.
- $w$ means scaled exact array here, but wire index on [Fast address-chunk interchange](address-interchange.md), which this page builds on: On this page $w$ means the scaled exact array (u*v)/S, but the address-interchange page uses $w$ for the wire index. Use another letter here, or say that $w$ means the scaled exact array (u*v)/S here, not the wire index as on the address-interchange page.
- $w$ means scaled exact array here, but binary vector on [Binary phase frames](phase-frames.md), which this page builds on: On this page $w$ means the scaled exact array (u*v)/S, but the binary phase frames page uses $w$ for a binary vector. Use another letter here, or say that $w$ means the scaled exact array (u*v)/S here, not a binary vector as on the binary phase frames page.
- $w$ means scaled exact array here, but summation index on [Retained permutation cancellation](retained-permutations.md), which this page builds on: On this page $w$ means the scaled exact array (u*v)/S, but the retained-permutations page uses $w$ for the summation index. Use another letter here, or say that $w$ means the scaled exact array (u*v)/S here, not the summation index as on the retained-permutations page.
- $R$ means retained permutation here, but row count on [Elementary stream operations](stream-ops.md), which this page builds on: On this page $R$ means the retained permutation, but the stream-operations page uses $R$ for the row count. Use another letter here, or say that $R$ means the retained permutation here, not the row count as on the stream-operations page.
- $R$ means retained permutation here, but scalar ring on [Frames on wire arrays](array-frames.md), which this page builds on: On this page $R$ means the retained permutation, but the array-frames page uses $R$ for the scalar ring. Use another letter here, or say that $R$ means the retained permutation here, not the scalar ring as on the array-frames page.

## Previous version (revise it)

It has 499 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 623 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The multiplication algorithm chains the reductions of the earlier pages to turn two $n$-bit integers into their exact $2n$-bit product.

It takes its sizes from [Parameter and prime-length choice](parameter-choice.md): $b=\lceil\log_2 n\rceil$ is the digit width (the number of bits in one radix digit, not a lowest bit or kernel coefficient), $p=6b$ is the number of fractional bits, $s_i$ are distinct odd prime axis lengths with product $S$, and $t_i$ are power-of-two axis lengths with product $T$. Each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$, and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](radix-digit-reduction.md). The convolution is placed on the prime axes by the [Chinese-remainder address map](crt-map.md) $\Phi$.

## The source transform

Let $F_{\boldsymbol s}$ be the discrete Fourier transform on the axes $s_i$, normalized by $1/S$. $F_{\boldsymbol s}^+$ is the same with the opposite sign in the exponent, and $F_{\boldsymbol t}$ is the transform on the axes $t_i$, normalized by $1/T$.

Let $\mathcal M_{\mathbb C}(f,g)=f*g/T$ be the normalized cyclic convolution, computed through the [Phase twist](phase-twist.md) and [Convolution from the retained transform layout](ring-convolution.md). With the chirp array $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ and the target permutation $Q$, the [Bluestein chirp identity](chirp.md) gives $QF_{\boldsymbol t}x=\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)$: phase, convolution with the chirp, phase. The computed version uses an approximation $\widetilde a$ of $a$ and truncation $Q_p$ to $p$ fractional bits. It forms the operand $x_0=Q_p(\overline{\widetilde a}\cdot x)$ after the first phase, then $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$, the computed convolution, and returns $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$.

The computed source transform $\widetilde{\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) map $\mathcal A$, then $\widetilde{\mathscr C}$, then the output map $\mathcal B_0$, then multiplies exactly by $2^\gamma$, where $\gamma$ is the exponent of the power-of-two scale that resampling introduces, not the initial central values of the exchange network. Its exact counterpart $\mathscr F$ replaces each numerical routine by the exact map it approximates, so $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, where $R$ is a retained permutation of coordinates, not a scalar ring or row count. For an array $z$ (not a round input or suffix), the opposite-sign procedure is $\widetilde{\mathscr F}^{+}(z)=\overline{\widetilde{\mathscr F}(\overline z)}$; $R$ is real and conjugation flips the exponent sign, so its exact counterpart is $RF_{\boldsymbol s}^{+}$.

## The algorithm

Digit $a_j$ is stored as the grid value $a_j2^{-b-2}$, so inputs have norm below $1/4$, and the digits are padded with zero records to length $S$. Then:

1. Apply $\Phi$ to obtain source arrays $u,v$ (arrays, not integers or DFT inputs).
2. Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
3. Multiply corresponding coefficients and truncate to $p$ fractional bits, obtaining the array $z$.
4. Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply by $S$, obtaining $\widetilde w$, which approximates the exact array $w=(u*v)/S$.
5. Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\Phi^{-1}$.
6. Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.

The two scalings by $S$ undo different normalizations. Each of $F_{\boldsymbol s}$ and $F_{\boldsymbol s}^{+}$ carries $1/S$, so $F_{\boldsymbol s}(u*v)=S\,F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v$ and $F_{\boldsymbol s}^{+}F_{\boldsymbol s}$ is the identity divided by $S$; hence $F_{\boldsymbol s}^{+}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$. Permutations commute with pointwise products, and $RF_{\boldsymbol s}^{+}R=F_{\boldsymbol s}^{+}$ by [Retained permutation cancellation](retained-permutations.md), so $R$ drops out. Steps 2 to 4 have exact counterpart $(u*v)/S^2$, and after the scale in step 4 it is $w$. Step 5 gives $2^{2b+4}(u*v)$. Each stored operand carries $2^{-b-2}$, so $u*v$ carries $2^{-2b-4}$, which the factor $2^{2b+4}$ cancels; $\Phi^{-1}$ then returns the integer digit convolution <cite data-source="paper">The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution.</cite>.

Exactness is shown by [Error tracking and exact recovery](precision-recovery.md): the error on these coefficients is below $1/2$, so rounding is exact.

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

Write the body to `exegenius/tasks/0313-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0313-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0313-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0313-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
