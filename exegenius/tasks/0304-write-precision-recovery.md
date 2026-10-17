# exegenius task 0304-write-precision-recovery

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

Concept: Error tracking and exact recovery
Gloss: Each normalized transform and product is a contraction with a bounded rounding error, and the total error on the recovered convolution coefficients is below 1/2, so rounding gives exact integers.
Also called: synthetic transform error, source transform error

## This page in the argument

The step: The error on the recovered integer coefficients is below $1/2$, so rounding gives the exact integer coefficients, and carry propagation yields the exact binary product.
How: Track errors in units of $h_p=2^{-p}$ through every contraction and bilinear map (each computed array also stays in the disk), obtain $E_{\rm ring}<5TL$, chirp error $<8TLh_p$, source error $E_s=9\cdot2^\gamma TL$, product error $(2E_s+2)$, opposite error $(3E_s+2)$, scaled error $E_w<28\cdot2^\gamma T^2L$, and finally the coefficient error $<448b\,2^{-3b/4}<1/2$.
Why: Each normalized transform and product is a contraction, so errors add rather than multiply; the final multiplication by the factors $2^{2b+4}S$ amplifies the error by at most $2^{2b+4}S\cdot2^{-p}$ which stays small only because $p=6b$ leaves $4b$ spare bits. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Each synthetic transform has error less than $\sqrt2\ell\,2^{-p}<L2^{-p}$ with $L=\log_2T$.
- Use $h_p=2^{-p}$ and the sup norm throughout; an error of $a$ means error less than $ah_p$.
- For a bilinear contraction, replacing operands changes the output by at most $\|f'-f\|\|g'\|+\|f\|\|g'-g\|$.
- Hence, for disk operands, the two input errors add.
- A computed phase product satisfies $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$ and $\|Q_p(\widetilde ex)\|\le\|x\|$.
- The ring convolution error is $E_{\rm ring}:=M(3L+2)<5TL$, and its output has norm below $.701$ when one operand has norm at most $.7$.
- The computed complex convolution has error less than $(E_{\rm ring}+4+4+4)h_p<6TLh_p$: two input twists, the ring approximation and the output untwist.
- The chirp transform has error $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p$.
- The source transform (error $2dp^2+8TL$ before scaling, then multiplied by $2^\gamma$) has error less than $E_sh_p$ with $E_s=9\cdot2^\gamma TL$, using $2dp^2<TL$ eventually.
- The computed product $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has $\|z-U\cdot V_1\|<(2E_s+2)h_p$: two terms of norm below $E_sh_p$ each, plus truncation.
- The opposite transform gives error less than $(3E_s+2)h_p$ relative to $G(U\cdot V_1)=(u*v)/S^2$.
- After the first exact multiplication by $S$: $\widetilde w$ approximates $w=(u*v)/S$ with error less than $E_wh_p$, $E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L$.
- After the second scaling by $2^{2b+4}S$ the absolute error is $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}$.
- Using $S\le T<2^b$, $L<b$ it is less than $448b\,2^{-b+\gamma}$.
- Since $\gamma\le b/4$ for $b\ge2^{24}$ it is at most $448b\,2^{-3b/4}<1/2$.
- The true coefficients are integers, so the strict error below $1/2$ makes the nearest integer to the represented value the unique correct coefficient.
- The carries obey $k_0=0$, $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ with $Q_0=2^b$.
- The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$: if this holds at $j$, then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$.
- The invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ shows the first $j$ radix digits are fixed.
- The exact product is less than $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$.; how: Reduce the integer product to a cyclic convolution of $S$ short coefficients and compute it through the chain of reductions (digits, CRT address map, Gaussian resampling with chirps, twist to the polynomial ring, synthetic-transform convolution); recover exact integers because the accumulated error is below $1/2$. (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.7.1, S5.7.2, S5.7.3, S5.7.4, S5.7.5, S5.7.6, S5.7.7, S5.7.8, S5.7.9, S5.7.10, S5.7.11, S5.7.12, S5.7.13, S5.7.14, S5.7.15, S5.7.16, S5.7.17, S5.7.18, S5.7.19, S5.7.20). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.7.1**: Each synthetic transform has error less than $\sqrt2\ell\,2^{-p}<L2^{-p}$ with $L=\log_2T$.
Source: "$\sqrt2\ell\,2^{-p}<L2^{-p}$, where $L=\log_2T$, for all" (paper)
> Proposition~\ref{prop:simultaneous-layer} uses $C_1=20$, so $\epsilon C_1<1$ makes its coefficient width $O(p)$. Lemma~\ref{lem:synthetic-transform-cost} therefore applies to every synthetic transform here, with error less than $\sqrt2\ell\,2^{-p}<L2^{-p}$, where $L=\log_2T$, for all sufficiently large $n$.

**S5.7.2**: Use $h_p=2^{-p}$ and the sup norm throughout; an error of $a$ means error less than $ah_p$.
Source: "Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this" (paper)
> Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.

**S5.7.3**: For a bilinear contraction, replacing operands changes the output by at most $\|f'-f\|\|g'\|+\|f\|\|g'-g\|$.
Source: "\|\mathcal M(f',g')-\mathcal M(f,g)\|" (paper)
> Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.

**S5.7.4**: Hence, for disk operands, the two input errors add.
Source: "\le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|." (paper)
> Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.

**S5.7.5**: A computed phase product satisfies $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$ and $\|Q_p(\widetilde ex)\|\le\|x\|$.
Source: "<(2\|x\|+\sqrt2)h_p<4h_p," (paper)
> We also need the norm as well as the error of a computed phase product. Let $e$ be a unit phase, let $\widetilde e$ be a disk-grid approximation with $|\widetilde e-e|<2h_p$, and let $x$ be a disk operand. The truncation bound in \eqref{eq:transform-truncate} gives \[ \|Q_p(\widetilde e x)-ex\| <(2\|x\|+\sqrt2)h_p<4h_p, \qquad \|Q_p(\widetilde e x)\|\le\|x\|. \] The second inequality follows from $|\widetilde e|\le1$ and the fact that $Q_p$ does not increase the norm. It preserves every smaller operand norm through a twist or an endpoint phase multiplication. The same bounds hold coordinatewise for arrays of phases.

**S5.7.6**: The ring convolution error is $E_{\rm ring}:=M(3L+2)<5TL$, and its output has norm below $.701$ when one operand has norm at most $.7$.
Source: "E_{\rm ring}:=M(3L+2)<5TL." (paper)
> For disk-grid ring arrays $f,g$, put $M=T/r$. Two normalized synthetic forwards, pointwise polynomial multiplication divided by $r$, and the normalized opposite transform give $(f*g)/(rM^2)$. The exact multiplication by $M$ in Proposition~\ref{prop:synthetic-convolution} then gives $\mathcal M_r(f,g)=(f*g)/T$. Before that multiplication, the three transform errors and the polynomial-product truncation total less than $3L+2$. Thus the error of the returned normalized convolution is bounded by \[ E_{\rm ring}:=M(3L+2)<5TL. \] If one operand has norm at most $.7$, bilinear contraction gives $\|\mathcal M_r(f,g)\|\le.7$. Its computed grid output consequently has norm less than $.7+5TLh_p<.701$ for large $n$. This proves the disk margin after the scale $M$, without clipping the output.

**S5.7.7**: The computed complex convolution has error less than $(E_{\rm ring}+4+4+4)h_p<6TLh_p$: two input twists, the ring approximation and the output untwist.
Source: "<(E_{\rm ring}+4+4+4)h_p<6TLh_p." (paper)
> To compare it with $\mathcal M_{\mathbb C}(f,g)$, insert the exact normalized $\mathcal M_r$ at $\iota f'$ and $\iota g'$. Its bilinear contraction bound propagates the two input twist errors, each less than $4$. Its approximation contributes $E_{\rm ring}$, and the output untwist contributes less than $4$. All these comparisons are at the normalized $\mathcal M_r$ interface, after its factor $M$. They give \[ \|\widetilde{\mathcal M}_{\mathbb C}(f,g) -\mathcal M_{\mathbb C}(f,g)\| <(E_{\rm ring}+4+4+4)h_p<6TLh_p. \]

**S5.7.8**: The chirp transform has error $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p$.
Source: "<(6TL+2+4+4)h_p<8TLh_p." (paper)
> For its error, the exact operands $a$ and $\overline a\cdot x$ are in the disk because every entry of $a$ has modulus one. The kernel approximation contributes less than $2$ and the first endpoint multiplication contributes less than $4$ when inserted into the exact bilinear contraction $\mathcal M_{\mathbb C}$. The computed convolution contributes less than $6TL$, and the last endpoint multiplication less than $4$. Equation~\eqref{eq:permuted-chirp} identifies the exact result, so \[ \|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\| <(6TL+2+4+4)h_p<8TLh_p. \]

**S5.7.9**: The source transform (error $2dp^2+8TL$ before scaling, then multiplied by $2^\gamma$) has error less than $E_sh_p$ with $E_s=9\cdot2^\gamma TL$, using $2dp^2<TL$ eventually.
Source: "E_s=9\,2^\gamma TL," (paper)
> Finally let the input to a source transform have norm at most $.5$. The computed expansion has error less than $dp^2$ and norm less than $.5+dp^2h_p<.51$. It is therefore a permitted chirp input. The chirp output is in the disk by the preceding argument, so each compression call is defined and returns another disk-grid array. Insert the exact contractions $\mathcal A$, $QF_{\boldsymbol t}$, and $\mathcal B_0$ at the computed inputs. The error before the source scale is less than $2dp^2+8TL$. Multiplication by $2^\gamma$ therefore gives error less than $2^\gamma(2dp^2+8TL)h_p$, which is bounded by $E_sh_p$ with \begin{equation}\label{eq:source-error} E_s=9\,2^\gamma TL, \end{equation} because $2dp^2<TL$ eventually. The exact source transform $RF_{\boldsymbol s}$ is a contraction, so the scaled approximation has norm at most $.5+E_sh_p<.501$. Its exact numerator scaling therefore also leaves a disk-grid output without clipping. Conjugation preserves the grid and norm, so the opposite procedure has the same error and disk guarantee. All these margins may be enforced by one fixed cutoff. For example, $b\ge2^{24}$, together with the other eventual construction conditions, makes $dp^2h_p$, $8TLh_p$, $E_sh_p$ and $28\,2^\gamma T^2Lh_p$ smaller than $10^{-3}$.

**S5.7.10**: The computed product $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has $\|z-U\cdot V_1\|<(2E_s+2)h_p$: two terms of norm below $E_sh_p$ each, plus truncation.
Source: "Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$." (paper)
> The scaled radix digits in $u,v$ are exact $p$-bit grid values of norm strictly less than $1/4$. Put \[ \begin{aligned} U&=RF_{\boldsymbol s}u,&\qquad V_1&=RF_{\boldsymbol s}v,\\ \widetilde U&=\widetilde{\mathscr F}(u),& \widetilde V_1&=\widetilde{\mathscr F}(v). \end{aligned} \] The exact arrays have norm less than $1/4$, and the computed arrays have norm less than $1/4+E_sh_p<.26$. Hence $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm at most $.26^2<.5$. To estimate its error, write \[ \widetilde U\cdot\widetilde V_1-U\cdot V_1 =(\widetilde U-U)\cdot\widetilde V_1 +U\cdot(\widetilde V_1-V_1). \] The factors $\widetilde V_1$ and $U$ are in the disk. The two terms have total norm less than $2E_sh_p$, and truncation adds less than $2h_p$. Thus $\|z-U\cdot V_1\|<(2E_s+2)h_p$.

**S5.7.11**: The opposite transform gives error less than $(3E_s+2)h_p$ relative to $G(U\cdot V_1)=(u*v)/S^2$.
Source: "&<(3E_s+2)h_p." (paper)
> Let $G:=RF_{\boldsymbol s}^+$ be the exact opposite contraction. Lemma~\ref{lem:chirp-permutation}, applied to $U=RF_{\boldsymbol s}u$ and $V_1=RF_{\boldsymbol s}v$, gives \[ G(U\cdot V_1)=(u*v)/S^2. \] The computed opposite transform may be applied to $z$ because $\|z\|<.5$. Insert $G$ at that computed input: \[ \begin{aligned} \|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\| &\le \|\widetilde{\mathscr F}^{+}(z)-Gz\|\\ &\qquad+\|G(z-U\cdot V_1)\|\\ &<(3E_s+2)h_p. \end{aligned} \] The first exact numerator multiplication by $S$ gives $\widetilde w$, approximating $w=(u*v)/S$ with error less than $E_wh_p$, where \[ E_w:=S(3E_s+2)<28\,2^\gamma T^2L. \] Each coefficient of $w$ is an average of $S$ products of coefficients of $u$ and $v$, so $\|w\|<1/16$. The earlier cutoff therefore gives \[ \|\widetilde w\|<1/16+E_wh_p<1/16+10^{-3}<1. \] This proves the disk bound for the computed first scaled result.

**S5.7.12**: After the first exact multiplication by $S$: $\widetilde w$ approximates $w=(u*v)/S$ with error less than $E_wh_p$, $E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L$.
Source: "E_w:=S(3E_s+2)<28\,2^\gamma T^2L." (paper)
> Let $G:=RF_{\boldsymbol s}^+$ be the exact opposite contraction. Lemma~\ref{lem:chirp-permutation}, applied to $U=RF_{\boldsymbol s}u$ and $V_1=RF_{\boldsymbol s}v$, gives \[ G(U\cdot V_1)=(u*v)/S^2. \] The computed opposite transform may be applied to $z$ because $\|z\|<.5$. Insert $G$ at that computed input: \[ \begin{aligned} \|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\| &\le \|\widetilde{\mathscr F}^{+}(z)-Gz\|\\ &\qquad+\|G(z-U\cdot V_1)\|\\ &<(3E_s+2)h_p. \end{aligned} \] The first exact numerator multiplication by $S$ gives $\widetilde w$, approximating $w=(u*v)/S$ with error less than $E_wh_p$, where \[ E_w:=S(3E_s+2)<28\,2^\gamma T^2L. \] Each coefficient of $w$ is an average of $S$ products of coefficients of $u$ and $v$, so $\|w\|<1/16$. The earlier cutoff therefore gives \[ \|\widetilde w\|<1/16+E_wh_p<1/16+10^{-3}<1. \] This proves the disk bound for the computed first scaled result.

**S5.7.13**: After the second scaling by $2^{2b+4}S$ the absolute error is $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}$.
Source: "2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b}" (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S5.7.14**: Using $S\le T<2^b$, $L<b$ it is less than $448b\,2^{-b+\gamma}$.
Source: "<448b\,2^{-b+\gamma}" (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S5.7.15**: Since $\gamma\le b/4$ for $b\ge2^{24}$ it is at most $448b\,2^{-3b/4}<1/2$.
Source: "\le448b\,2^{-3b/4}<\frac12." (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S5.7.16**: The true coefficients are integers, so the strict error below $1/2$ makes the nearest integer to the represented value the unique correct coefficient.
Source: "$H_j/2^p$.  The strict error below $1/2$ makes the nearest integer to" (paper)
> In tensor order, the unscaled integer coefficient array is $2^{2b+4}S w$. This second occurrence of $S$ reverses the normalization still present in $w$, and $2^{2b+4}$ reverses the two input scales. Both multiplications act exactly on grid numerators. Since $S\le T<2^b$ and $L<b$ eventually, the final absolute error is less than \begin{equation}\label{eq:final-error} 2^{2b+4}S\cdot28\,2^\gamma T^2L\cdot2^{-6b} <448b\,2^{-b+\gamma} \le448b\,2^{-3b/4}<\frac12. \end{equation} The true coefficients are real integers. If $H_j$ is the real numerator after the second scaling, its represented value is $H_j/2^p$. The strict error below $1/2$ makes the nearest integer to that value the unique correct coefficient.

**S5.7.17**: The carries obey $k_0=0$, $d_j=(c_j+k_j)\bmod Q_0$, $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ with $Q_0=2^b$.
Source: "k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0," (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

**S5.7.18**: The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$: if this holds at $j$, then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$.
Source: "The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$.  If this holds at" (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

**S5.7.19**: The invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ shows the first $j$ radix digits are fixed.
Source: "\sum_{h<j}c_hQ_0^h" (paper)
> To propagate carries, let $Q_0=2^b$. The recovered ordinary coefficients are the $c_j$ in \eqref{eq:capacity}; they are zero for $2q-2<j<S$. With $q=\lceil n/b\rceil$ as above, use the recurrence for $0\le j<S$: \[ k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\left\lfloor\frac{c_j+k_j}{Q_0}\right\rfloor. \] The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$. If this holds at $j$, then \[ c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1), \] which proves the next carry bound. The defining relation $c_j+k_j=d_j+Q_0k_{j+1}$ also gives the exact invariant \[ \sum_{h<j}c_hQ_0^h =\sum_{h<j}d_hQ_0^h+k_jQ_0^j. \] It holds for $j=0$, and the defining relation proves its next instance. The unprocessed terms are multiples of $Q_0^j$, so the identity fixes the first $j$ radix digits of the full product. The value $k_j$ is the carry from the processed coefficients into the remaining positions.

**S5.7.20**: The exact product is less than $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.
Source: "than $2^{2n}$; all bits above position $2n-1$ are therefore zero." (paper)
> After $\Phi^{-1}$ the coefficients occur in increasing ordinary index, so this carry scan proceeds from least to most significant. Carry storage and work per coefficient are $O(b)$ bits and steps. Write each digit's bits from low to high on a work tape, and drain the final $O(b)$-bit carry in the same order. Copy the completed stream backward once to obtain most-significant-first order. The stream has length $O(Sb)=O(Tp)$, including chunk padding and the final carry, so this reversal is a charged linear tape pass. The exact product is less than $2^{2n}$; all bits above position $2n-1$ are therefore zero. Remove only those zero padding bits and retain leading zeros as needed to produce exactly $2n$ bits. Zero inputs obey the same invariant and output rule.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed-point Gaussian dyadic records](fixed-point.md): Complex values stored as signed two's-complement integers over a power-of-two denominator 2^{-p}; intermediate values are exact and one truncation Q_p rounds back to the p-bit grid.
  Shown as: Error tracking and exact recovery *<predicate>* Fixed-point Gaussian dyadic records
- [Multiplication as radix-digit convolution](radix-digit-reduction.md): Splitting each integer into radix-2^b digits turns the product into a convolution of short integer coefficients, which carry propagation turns back into a binary number.
  Shown as: Error tracking and exact recovery *<predicate>* Multiplication as radix-digit convolution
- [Contractions and bilinear contractions](contraction-maps.md): A linear map that never increases the norm of a vector, and a bilinear map whose output norm is at most the product of the input norms, so errors in the inputs do not grow beyond a controlled bound.
  Shown as: Error tracking and exact recovery *<predicate>* Contractions and bilinear contractions
- [Bluestein chirp identity](chirp.md): An identity that rewrites a (permuted) Fourier transform as a pointwise chirp phase, a cyclic convolution, and another chirp phase.
  Shown as: Error tracking and exact recovery *<predicate>* Bluestein chirp identity

## Pages that build on this one

- The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
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

- "proves that the recovered coefficient error is strictly below $1/2$" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

- "Precision and exact recovery" (paper)

  > \subsection{Precision and exact recovery}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $L$ means log of padded length here, but linear map on [Contractions and bilinear contractions](contraction-maps.md), which this page builds on: On this page $L$ means the base-2 logarithm of the padded length, but the contraction-maps page uses $L$ for a linear map. Use another letter here, or say that $L$ means the base-2 logarithm of the padded length here, not a linear map as on the contraction-maps page.
- $a$ means error size here, but chirp on [Bluestein chirp identity](chirp.md), which this page builds on: On this page $a$ means the size of an error in grid spacings, but the chirp page uses $a$ for the chirp. Use another letter here, or say that $a$ means the size of an error in grid spacings here, not the chirp as on the chirp page.
- $x$ means disk operand here, but polynomial variable on [Multiplication as radix-digit convolution](radix-digit-reduction.md), which this page builds on: On this page $x$ means an array in the unit disk to which a phase or chirp transform is applied, but the radix-digit page uses $x$ for the polynomial variable. Use another letter here, or say that $x$ means an array in the unit disk to which a phase or chirp transform is applied here, not the polynomial variable as on the radix-digit page.
- $u$ means scaled digit array here, but first input on [Multiplication as radix-digit convolution](radix-digit-reduction.md), which this page builds on: On this page $u$ means the scaled digit array of the first input, but the radix-digit page uses $u$ for the first input integer. Use another letter here, or say that $u$ means the scaled digit array of the first input here, not the first input integer as on the radix-digit page.
- $v$ means scaled digit array here, but second input on [Multiplication as radix-digit convolution](radix-digit-reduction.md), which this page builds on: On this page $v$ means the scaled digit array of the second input, but the radix-digit page uses $v$ for the second input integer. Use another letter here, or say that $v$ means the scaled digit array of the second input here, not the second input integer as on the radix-digit page.

## Previous version (revise it)

It has 554 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 692 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Error tracking and exact recovery shows that the computed convolution coefficients lie within $1/2$ of the true integers, so rounding recovers them.

The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits, where $b=\lceil\log_2n\rceil$ is the digit width. Write $h_p=2^{-p}$ and $L=\log_2T$ (this $L$ is not the linear map $L$ of the contractions page). Norms are sup norms, an error of $a$ means error below $ah_p$, and every array stays in the unit disk (norm $\le1$). For large $n$, $S\le T<2^b$ and $L<b$. Each [synthetic transform](synthetic-transform.md) has error below $L$ <cite data-source="paper">$\sqrt2\ell\,2^{-p}<L2^{-p}$</cite>.

Errors add through the [Contractions and bilinear contractions](contraction-maps.md) making up each transform and product. For a bilinear contraction $\mathcal M$, replacing operands $f,g$ by $f',g'$ gives
$$\|\mathcal M(f',g')-\mathcal M(f,g)\|=\|\mathcal M(f'-f,g')+\mathcal M(f,g'-g)\|\le\|f'-f\|\|g'\|+\|f\|\|g'-g\|,$$
so for disk operands the two input errors add.

For a unit phase $e$, an approximation $\widetilde e$ with $|\widetilde e-e|<2h_p$ and a disk operand $x$, the product differs by under $2\|x\|h_p$ and truncation $Q_p$ adds under $\sqrt2h_p$, so $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$. Also $\|Q_p(\widetilde ex)\|\le\|x\|$, since $|\widetilde e|\le1$.

The ring convolution $\mathcal M_r$ of [Phase twist](phase-twist.md) applies two forward synthetic transforms, a pointwise polynomial product divided by $r$ (truncation under $2$) and one opposite transform. Together they err by under $3L+2$. An exact multiplication by $M=T/r$ then gives $(f*g)/T$ and
$$E_{\rm ring}:=M(3L+2)<5TL$$
<cite data-source="paper">E_{\rm ring}:=M(3L+2)<5TL.</cite> With an operand of norm at most $.7$, the output norm stays below $.701$. The complex convolution adds two input twists and one output untwist, each under $4$, so it errs by under
$$(E_{\rm ring}+4+4+4)h_p<6TLh_p.$$

The computed chirp transform $\widetilde{\mathscr C}$ is built from the [Bluestein chirp identity](chirp.md): a phase product, a complex convolution with the chirp kernel, and a last phase product. With $\boldsymbol t$ the axis lengths, $F_{\boldsymbol t}$ the exact transform and $Q$ the target permutation, the errors $2$ (kernel), $4$, $6TL$ and $4$ give
$$\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p.$$

The computed source transform $\widetilde{\mathscr F}$ applies the expansion map $\mathcal A$ of [Gaussian resampling](gaussian-resampling.md), then $\widetilde{\mathscr C}$, then the compression map $\mathcal B_0$, then an exact scaling by $2^\gamma$. Each of $\mathcal A,\mathcal B_0$ is a contraction implemented along $d$ axes with error under $p^2$ each, so under $dp^2$. The error before scaling is under $2dp^2+8TL$. As $2dp^2<TL$ eventually, scaling gives error under $E_sh_p$ with
$$E_s=9\cdot2^\gamma TL$$
<cite data-source="paper">E_s=9\,2^\gamma TL,</cite> where $b\ge2^{24}$ gives $\gamma\le b/4$ <cite data-source="paper">$b\ge2^{24}$ implies $\gamma\le b/4$</cite> and keeps $E_sh_p<10^{-3}$.

Now $u,v$ are scaled digit arrays, not the integers of the radix-digit page: each digit is stored as its value times $2^{-b-2}$, so norms are below $1/4$. Let $U=RF_{\boldsymbol s}u$ and $V_1=RF_{\boldsymbol s}v$ be the exact source transforms and $\widetilde U,\widetilde V_1$ the computed ones, of norm under $1/4+E_sh_p<.26$. Then $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm under $.26^2<.5$, and
$$\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1)$$
has two terms under $E_sh_p$; truncation adds under $2h_p$. So $\|z-U\cdot V_1\|<(2E_s+2)h_p$.

With $F_{\boldsymbol s}$ the transform with factor $1/S$ and $F_{\boldsymbol s}^+$ its opposite-sign version, the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)) and the exact opposite transform $G=RF_{\boldsymbol s}^+$ gives $G(U\cdot V_1)=(u*v)/S^2$ <cite data-source="paper">=\frac{u*v}{S^2}.</cite> The computed opposite transform is within $E_sh_p$ of $Gz$ and $G$ is a contraction, so
$$\|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\|\le\|\widetilde{\mathscr F}^{+}(z)-Gz\|+\|G(z-U\cdot V_1)\|<(3E_s+2)h_p.$$
Exact multiplication by $S$ makes $\widetilde w$ approximate $w=(u*v)/S$ with error under $E_wh_p$, where
$$E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L.$$

The integer coefficients are $2^{2b+4}Sw$: $2^{2b+4}$ undoes the two digit scales and $S$ the remaining $1/S$. With $h_p=2^{-6b}$, $S\le T<2^b$, $L<b$ and $\gamma\le b/4$, the absolute error is under
$$2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12$$
<cite data-source="paper">\le448b\,2^{-3b/4}<\frac12.</cite> Here $2^{2b+4}ST^2<2^{5b+4}$ uses about $5b$ of the $6b$ fractional bits. The true coefficients are integers, so error strictly below $1/2$ makes the nearest integer the unique correct coefficient.

Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), indexed by $j$, with $c_j\le q(2^b-1)^2$ and $q\le2^b$. Put $Q_0=2^b$ and $k_0=0$; $k_j$ is the carry into position $j$ and $d_j$ the $j$-th output digit:
$$d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor.$$
Then $0\le k_j\le q(Q_0-1)<Q_0^2$: if this holds at $j$, then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$. Since $c_j+k_j=d_j+Q_0k_{j+1}$, adding $c_jQ_0^j$ carries the invariant
$$\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$$
from $j$ to $j+1$ (it holds at $j=0$). Unprocessed terms are multiples of $Q_0^j$, so the first $j$ radix digits are fixed. The product is below $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.

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

Write the body to `exegenius/tasks/0304-write-precision-recovery.answer.md` and the JSON to `exegenius/tasks/0304-write-precision-recovery.answer.json`, then run `exegenius submit 0304-write-precision-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0304-write-precision-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
