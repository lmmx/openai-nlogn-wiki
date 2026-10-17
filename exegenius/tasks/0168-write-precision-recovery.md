# exegenius task 0168-write-precision-recovery

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
- $j$ (excess degree), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on [Polynomial ring modulo y^r + 1](ring-y.md): An integer exponent of y by which an element is multiplied.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $c$ (machine constant), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A positive constant, depending on the machine, in the lower bound c n log n.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set [h] whose three-element subsets index the values.
- $v$ (triple count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of [h].
- $\mathcal T$ (triple set), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The set of three-element subsets of [h].
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of each data bank.
- $m$ (label dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $S$ (triple), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A three-element subset of [h], indexing a value in a bank.
- $x$ (source vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The vector of all values x_S.
- $y$ (target vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The vector of all values y_S.
- $S'$ (other triple), bound on [Linear exchange network with restored scratch wires](exchange-network.md): A second triple, the index of a source value x_{S'}.
- $a$ (bank index), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The index of a value in a data bank, a triple of triples.
- $\sigma$ (side scratch vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the side scratch wires.
- $\gamma$ (central scratch vector), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The initial values of the central scratch wires.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbours), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbours), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires of the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires of the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every array.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): The invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $t$ (gate input count), bound on [Frames on wire arrays](array-frames.md): The number of input arrays of a gate.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each sequence being convolved.
- $d$ (axis count), bound on [Cyclic convolution](convolution.md): One more than the number of cyclic axes of an array.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of cyclic axis i.
- $M$ (cyclic address count), bound on [Cyclic convolution](convolution.md): The number of addresses on the cyclic axes of an array.
- $T$ (total coefficient count), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array.
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
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits an array stores.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $P$ (prefix values), bound on [Elementary stream operations](stream-ops.md): The number of prefix values indexing the first axis of the array.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in the array of item 4.
- $B$ (entries per row), bound on [Elementary stream operations](stream-ops.md): The number of entries in each row.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams the rows are dealt into.
- $\boldsymbol j$ (output index), bound on [Bluestein chirp identity](chirp.md): The index tuple (j_1,...,j_d) of an entry of the data and of the output position.
- $s_i$ (source length), bound on [Bluestein chirp identity](chirp.md): An integer coprime to t_i attached to axis i, the multiplier of the frequency read.
- $\boldsymbol f$ (frequency), bound on [Bluestein chirp identity](chirp.md): The frequency tuple (f_1,...,f_d) labelling an output entry of the transform.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The permutation of the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The array of phases a_j = exp(-pi i sum s_i j_i^2/t_i), quadratic in the index.
- $\mathcal R_r$ (negacyclic ring), bound on [Retained frequency order](frequency-order.md): The ring of polynomials in y with r complex coefficients, modulo y^r+1.
- $a$ (number of rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds, log base 2 of the transform length t.
- $F_t^-$ (forward synthetic transform), bound on [Retained frequency order](frequency-order.md): The forward length-t synthetic transform on t ring elements.
- $H_0$ (two-point butterfly), bound on [Retained frequency order](frequency-order.md): The 2x2 butterfly matrix (1/2)[[1,1],[1,-1]].
- $B_t$ (bit-reversal record permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\operatorname{rev}_a$ (bit reversal), bound on [Retained frequency order](frequency-order.md): The map reversing the a binary digits of j.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $i$ (axis index), bound on [Retained frequency order](frequency-order.md): Index of an axis of the array.
- $u_i$ (current axis length), bound on [Retained frequency order](frequency-order.md): The current length of axis i.
- $b_i$ (new bit), bound on [Retained frequency order](frequency-order.md): The bit newly written by the latest round on axis i.
- $k_i$ (twiddle index), bound on [Retained frequency order](frequency-order.md): The number formed by the bits in axis i's unprocessed slots below the paired slot, with 0<=k_i<u_i/2.
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The operation applying H_0 on every participating axis at once.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The operation multiplying the record at each address by y^E.
- $E$ (combined exponent), bound on [Retained frequency order](frequency-order.md): The exponent of y by which the record at an address is multiplied, determined by that address.
- $j_0$ (odd part), bound on [Retained frequency order](frequency-order.md): The odd part of j, so j=2^v j_0.
- $v$ (two-adic exponent), bound on [Retained frequency order](frequency-order.md): The exponent of 2 in j, with 0<=v<a.
- $N$ (factor bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers of one product given to the established multiplier (not the bank size).
- $p$ (fractional bits), bound on [Signed packing](signed-packing.md): The number of fractional bits of each coefficient component.
- $\mathcal R_r$ (ring), bound on [Signed packing](signed-packing.md): The ring of polynomials of degree below r modulo y^r+1.
- $f$ (first polynomial), bound on [Signed packing](signed-packing.md): A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $a$ (integer polynomial), bound on [Signed packing](signed-packing.md): Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The base 2^{4p} at which polynomials are evaluated.
- $A_u$ (signed evaluation integer), bound on [Signed packing](signed-packing.md): The integer u(B_0) for u among a, b, c, e.
- $u_j$ (coefficient of u), bound on [Signed packing](signed-packing.md): The coefficient of y^j in u.
- $\gamma_j$ (packing carry), bound on [Signed packing](signed-packing.md): The carry into block j when forming A_u, in {-1,0}.
- $d_j$ (packed block), bound on [Signed packing](signed-packing.md): The j-th block of 4p bits of the encoding of A_u, in [0,B_0).
- $h_j$ (product coefficient), bound on [Signed packing](signed-packing.md): The coefficient of y^j in an ordinary integer-polynomial product such as h=ac.
- $Z$ (product integer), bound on [Signed packing](signed-packing.md): One of the four product integers, equal to the sum of h_j B_0^j for its ordinary product h.
- $q_j$ (block of Z), bound on [Signed packing](signed-packing.md): The j-th block of Z in sign-extended two's complement, in [0,B_0).
- $\varepsilon$ (sign extension), bound on [Signed packing](signed-packing.md): The sign-extension digit of Z, in {-1,0}.
- $\rho_j$ (extraction carry), bound on [Signed packing](signed-packing.md): The carry into block j during extraction, in {0,1}.
- $\widehat h_j$ (extracted coefficient), bound on [Signed packing](signed-packing.md): The centered residue of q_j+rho_j modulo B_0, equal to h_j.
- $H_j$ (numerator coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $j_1$ (first-factor index), bound on [Signed packing](signed-packing.md): The index of a coefficient of the first factor.
- $j_2$ (second-factor index), bound on [Signed packing](signed-packing.md): The index of a coefficient of the second factor.
- $q$ (prime), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The prime base of the digits of a field.
- $b$ (digits per field), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-q digits of a field.
- $Q$ (field values), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take, q^b.
- $y$ (target value), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The value of the target field, in [Q].
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target, prepared from the control values.
- $B$ (suffix bits), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of bits following the target field.
- $c$ (multiplier), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the target is multiplied.
- $j$ (piece index), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The index of the increasing piece of y -> cy mod Q containing y.
- $y'$ (output coordinate), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The output coordinate of the target after scaling, running from 0 to Q-1.
- $c'$ (denominator), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The positive integer denominator, prime to q, of a rational unit.
- $V$ (array volume), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of stored data bits in the array.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): The fixed rational matrix whose product with D is added to H.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the rational matrix A.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $H$ (target group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields that receives the sum.
- $D$ (source group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields that is added in and left unchanged.
- $E_1$ (left factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular rational matrix in the factorization of A.
- $E_2$ (right factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular rational matrix in the factorization of A.
- $\Pi$ (partial permutation), bound on [Matrix shear by triangular factorization](matrix-shear.md): The matrix with exactly a ones, at most one per row and column, in the factorization of A.
- $a$ (kernel coefficient a), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix swapping the two entries of a pair.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The 2 by 2 matrix aI+bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1,i) multiplying the second entry of a pair by i.
- $H$ (normalized Hadamard matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix sqrt(2) H_0, symmetric with H squared equal to the identity.
- $H_0$ (two-point butterfly), bound on [Two-point kernel C](phase-kernel.md): The matrix (1/2)[[1,1],[1,-1]] of the averaging and differencing step on a pair.
- $L$ (linear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on [Contractions and bilinear contractions](contraction-maps.md): A map linear in each of its two operands.
- $f$ (first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The first operand of the bilinear map.
- $g$ (second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): The second operand of the bilinear map.
- $u'$ (computed input), bound on [Contractions and bilinear contractions](contraction-maps.md): A computed approximation replacing the exact input u.
- $f'$ (perturbed first operand), bound on [Contractions and bilinear contractions](contraction-maps.md): A perturbed replacement for the operand f.
- $g'$ (perturbed second operand), bound on [Contractions and bilinear contractions](contraction-maps.md): A perturbed replacement for the operand g.
- $F_q$ (normalized transform), bound on [Contractions and bilinear contractions](contraction-maps.md): The normalized discrete Fourier transform on sequences of q entries.
- $q_i$ (axis length), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i of the array.
- $j$ (index tuple), bound on [Multidimensional transforms](multidim-transform.md): The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $G_i$ (axis operator), bound on [Multidimensional transforms](multidim-transform.md): An operator acting on sequences of length q_i, applied along axis i.
- $F_{q_i}$ (one-axis transform), bound on [Multidimensional transforms](multidim-transform.md): The one-dimensional normalized discrete Fourier transform of length q_i.
- $F_{\boldsymbol q}$ (multidimensional transform), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the one-axis transforms F_{q_i}.
- $k$ (output index tuple), bound on [Multidimensional transforms](multidim-transform.md): An output index tuple of the same shape as j.
- $\alpha$ (resampling parameter), bound on [Multidimensional transforms](multidim-transform.md): An integer parameter of the Gaussian resampling with 2 <= alpha < sqrt p.
- $\delta$ (time exponent slack), bound on [Multidimensional transforms](multidim-transform.md): A fixed constant with 0 < delta < 1/8 in the exponent of the running time.
- $P_{s_i}$ (source permutation), bound on [Multidimensional transforms](multidim-transform.md): The index permutation on length s_i sequences in the resampling identity.
- $A_i$ (input resampling map), bound on [Multidimensional transforms](multidim-transform.md): A linear contraction from sequences of length s_i to length t_i.
- $B_{0,i}$ (output resampling map), bound on [Multidimensional transforms](multidim-transform.md): A linear contraction from sequences of length t_i to length s_i.
- $\gamma$ (scalar exponent), bound on [Multidimensional transforms](multidim-transform.md): The exponent 2d alpha^2 of the scalar in the tensored identity.
- $R$ (source permutation product), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the permutations P_{s_i}; here R is not the scalar ring.
- $Q$ (target permutation product), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the permutations P_{t_i}.
- $\mathcal A$ (tensored input map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the maps A_i.
- $\mathcal B_0$ (tensored output map), bound on [Multidimensional transforms](multidim-transform.md): The tensor product of the maps B_{0,i}.
- $X_i$ (axis operator), bound on [Multidimensional transforms](multidim-transform.md): An operator on axis i in the mixed-product rule.
- $Y_i$ (axis operator), bound on [Multidimensional transforms](multidim-transform.md): A second operator on axis i in the mixed-product rule.
- $S$ (convolution length), bound on [Chinese-remainder address map](crt-map.md): The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on [Chinese-remainder address map](crt-map.md): The number of axes of the target ring.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis, from 1 to d.
- $s_i$ (axis source length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i, pairwise coprime with the others; unrelated to the s_i of the chirp page.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths s_j of the axes before axis i.
- $\mu_i$ (coordinate exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The polynomial variable of axis i, with x_i^{s_i}=1.
- $\Phi$ (Chinese-remainder map), bound on [Chinese-remainder address map](crt-map.md): The ring isomorphism sending x to the product of x_i^{mu_i}.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): The index of a coefficient of the length-S sequence.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The j-th digit of k in mixed radix, 0 <= a_j < s_j.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of Phi(x^k).
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The padded length of axis i, either r/2 or r.
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the t_i.
- $V$ (stream volume), bound on [Chinese-remainder address map](crt-map.md): The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the cost of a chunk interchange.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the Fourier transform to be replaced.
- $\alpha$ (Gaussian width parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer, with 2 <= alpha < sqrt p, that is the width parameter of the Gaussian weights.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s - 1 between the two lengths.
- $C$ (coordinate selection), bound on [Gaussian resampling](gaussian-resampling.md): The map from C^t to C^s that selects coordinate q_j into position j.
- $\delta$ (exponent slack), bound on [Gaussian resampling](gaussian-resampling.md): A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
- $k$ (output coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $\widetilde E$ (approximate E), bound on [Gaussian resampling](gaussian-resampling.md): The numerical approximation of E = N - I computed on D_p records.
- $\boldsymbol s$ (axis-length tuple), bound on [Retained permutation cancellation](retained-permutations.md): The tuple $(s_1,\dots,s_d)$ of prime axis lengths, one per axis.
- $\boldsymbol t$ (padded-length tuple), bound on [Retained permutation cancellation](retained-permutations.md): The tuple $(t_1,\dots,t_d)$ of power-of-two axis lengths.
- $\boldsymbol q$ (axis-length tuple), bound on [Retained permutation cancellation](retained-permutations.md): A generic tuple of axis lengths.
- $F_{\boldsymbol q}$ (multidimensional transform), bound on [Retained permutation cancellation](retained-permutations.md): The normalized discrete Fourier transform applied along every axis of an array with axis lengths q.
- $\delta$ (time exponent), bound on [Retained permutation cancellation](retained-permutations.md): The fixed exponent in the time bound of Gaussian resampling.
- $u$ (complex array), bound on [Retained permutation cancellation](retained-permutations.md): Here a complex array, not an integer; changes meaning from the multiplication page.
- $v$ (complex array), bound on [Retained permutation cancellation](retained-permutations.md): Here a complex array, not an integer; changes meaning from the multiplication page.
- $R$ (source permutation), bound on [Retained permutation cancellation](retained-permutations.md): The tensor product of the source permutations P_{s_i}; a permutation, not the scalar ring.
- $\gamma$ (power-of-two exponent), bound on [Retained permutation cancellation](retained-permutations.md): The exponent 2 d alpha^2 of the total scalar factor 2^gamma.
- $t_{\max}$ (largest axis length), bound on [Retained permutation cancellation](retained-permutations.md): The largest axis length, a power of two 2^l.
- $g$ (setup exponent), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent bounding per-line setup work by p^g.
- $\boldsymbol j$ (entry multi-index), bound on [Retained permutation cancellation](retained-permutations.md): The index (j_1,...,j_d) of an entry of the array.
- $c$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): An integer that is a unit (invertible) modulo q.
- $z$ (complex vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries.
- $X_i$ (axis operator), bound on [Retained permutation cancellation](retained-permutations.md): An operator acting on vectors of length q_i, applied along axis i.
- $Y_i$ (second axis operator), bound on [Retained permutation cancellation](retained-permutations.md): A further operator acting on vectors of length q_i, applied along axis i.

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
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
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

- The reader cannot follow this step: "leaves margin $2^{-b}$ against amplification up to $2^{5b+4}$" (Not in the paper and not supported by the page's own bound. The amplification is 2^{2b+4}S with errors up to about 28*2^gamma*T^2*L, so 2^{5b+4}*2^{-6b}=2^{-b+4}, not 2^{-b}; the displayed bound actually obtained is 448 b 2^{-b+gamma}, which exceeds 2^{-b}. The correct statement is the displayed bound 448 b 2^{-b+gamma} <= 448 b 2^{-3b/4} < 1/2 (paper lines 4722-4727).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Its transforms and truncation err by under $3L+2$ before a final exact multiplication by $M=T/r$" (The page never says what the ring convolution consists of (two forward synthetic transforms, a pointwise polynomial product with truncation under 2, one opposite transform), so the reader cannot check that three transforms at L each plus 2 gives 3L+2.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "a chirp transform (error under $2dp^2+8TL$)" (The page gives no source for the 2dp^2 term (computed expansion and compression maps of Gaussian resampling, error under dp^2 each side); the reader cannot check it from what is given.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "the computed ones, of norm under $.26$" (Needs 1/4+E_s h_p<.26, i.e. E_s h_p<.01, which the page never states (it only states 5TLh_p<10^{-3} for the ring convolution); the cutoff making E_s h_p small is not given.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $M$ denotes where it is first used: the page uses it before saying so in "a final exact multiplication by $M=T/r$"
- Say what $F$ denotes where it is first used: the page uses it before saying so in "Both source Fourier transforms, $F$ and $F^+$, carry $1/S$"
- Say what $j$ denotes where it is first used: the page uses it before saying so in "With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy"

## Previous version (revise it)

It has 435 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 543 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Error tracking and exact recovery shows the computed coefficients lie within $1/2$ of the integers, so rounding is exact.

The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits; $b=\lceil\log_2n\rceil$ is the digit width. Let $h_p=2^{-p}$, $L=\log_2T$, $S\le T$; for large $n$, $T<8n/b$ gives $T<2^b$ and $L<b$. Error $a$ means sup-norm error under $ah_p$; arrays stay in the disk (norm $\le1$). Each [Synthetic polynomial transform](synthetic-transform.md) has error below $L$ <cite data-source="paper">$\sqrt2\ell\,2^{-p}<L2^{-p}$</cite>.

It adds errors through the [Contractions and bilinear contractions](contraction-maps.md) making up each transform and product. A bilinear $\mathcal M$ with $\|\mathcal M(f,g)\|\le\|f\|\|g\|$ satisfies
$$\|\mathcal M(f',g')-\mathcal M(f,g)\|=\|\mathcal M(f'-f,g')+\mathcal M(f,g'-g)\|\le\|f'-f\|\|g'\|+\|f\|\|g'-g\|,$$
so for disk operands input errors add.

For a unit phase $e$, a disk-grid approximation $\widetilde e$ with $|\widetilde e-e|<2h_p$ and a disk operand $x$, truncation $Q_p$ adds under $\sqrt2h_p$, so $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$; and $|\widetilde e|\le1$ gives $\|Q_p(\widetilde ex)\|\le\|x\|$.

The ring convolution $\mathcal M_r$ of [Phase twist](phase-twist.md) returns $(f*g)/T$. Its transforms and truncation err by under $3L+2$ before a final exact multiplication by $M=T/r$, giving $E_{\rm ring}:=M(3L+2)<5TL$.
If an operand has norm at most $.7$, so does the exact output, by contraction; adding error $5TLh_p<10^{-3}$ gives norm below $.701$. Two twists and an untwist add $4$ each, so the complex convolution errs by under
$$(E_{\rm ring}+4+4+4)h_p<6TLh_p.$$

The chirp transform $\widetilde{\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md), with $\boldsymbol t$ the axis lengths, $F_{\boldsymbol t}$ the exact Fourier transform and $Q$ the target permutation:
$$\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p.$$

A source transform applies [Gaussian resampling](gaussian-resampling.md) maps and a chirp transform (error under $2dp^2+8TL$), then scales exactly by the source scale $2^\gamma$ ($b\ge2^{24}$ gives $\gamma\le b/4$ <cite data-source="paper">$b\ge2^{24}$ implies $\gamma\le b/4$</cite>). As $2dp^2<TL$ eventually, error is under $E_sh_p$, $E_s=9\cdot2^\gamma TL$.

Here $u,v$ denote the scaled digit arrays (letters redefined): a digit $a$ is stored as $a2^{-b-2}$, norm under $1/4$. Let $U,V_1$ be their exact source transforms and $\widetilde U,\widetilde V_1$ the computed ones, of norm under $.26$. Then $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm under $.5$, and
$$\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1)$$
has two terms under $E_sh_p$; truncation adds under $2h_p$. So $\|z-U\cdot V_1\|<(2E_s+2)h_p$.

Both source Fourier transforms, $F$ and $F^+$, carry $1/S$, so $F(u*v)=S\,Fu\cdot Fv$ and $F^+F=I/S$; the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)), so the exact opposite transform $G$ gives $G(U\cdot V_1)=(u*v)/S^2$ <cite data-source="paper">=\frac{u*v}{S^2}.</cite> The computed one is within $E_sh_p$ of $Gz$, and $G$ is a contraction, so the total is under $(3E_s+2)h_p$. Multiplying exactly by $S$, $\widetilde w$ approximates $w=(u*v)/S$ within $E_wh_p$:
$$E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L.$$

The integer coefficients are $2^{2b+4}Sw$, undoing digit scales and $1/S$. With $S\le T<2^b$ and $L<b$ the absolute error is under
$$2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12.$$
Here $p=6b$ leaves margin $2^{-b}$ against amplification up to $2^{5b+4}$. The coefficients are integers, so error below $1/2$ makes the nearest integer to the represented value correct.

Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), where $c_j\le q(2^b-1)^2$ and $q=\lceil n/b\rceil\le2^b$. With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy
$$d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor.$$
Then $0\le k_j\le q(Q_0-1)<Q_0^2$: if so at $j$, then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$. As $c_j+k_j=d_j+Q_0k_{j+1}$, adding $c_jQ_0^j$ carries the invariant
$$\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$$
from $j$ to $j+1$. Unprocessed terms are multiples of $Q_0^j$, so the first $j$ radix digits are fixed. The product is below $2^{2n}$, so bits above position $2n-1$ are zero and $2n$ bits are output.

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

Write the body to `exegenius/tasks/0168-write-precision-recovery.answer.md` and the JSON to `exegenius/tasks/0168-write-precision-recovery.answer.json`, then run `exegenius submit 0168-write-precision-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0168-write-precision-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
