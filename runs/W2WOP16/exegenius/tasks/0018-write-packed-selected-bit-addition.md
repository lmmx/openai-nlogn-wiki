# exegenius task 0018-write-packed-selected-bit-addition

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WOP16` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (modular arithmetic, primes and coprimality, the Chinese remainder theorem, permutations, induction, recurrences), calculus-level analysis (logarithms, floor and ceiling, norms and rounding errors), linear algebra (vectors, matrices, invertibility, rank, over the reals, complex numbers and F2), and algorithms (asymptotic notation, schoolbook multiplication, divide and conquer, sorting) with a first look at the FFT. They know basic multitape Turing machines and tapes, polynomials and complex numbers including roots of unity. They have not met Schoenhage-Strassen or Karatsuba-level multiplication algorithms in depth, ring and group-algebra language beyond polynomials, tensor products, numerical error analysis of fixed-point transforms, or any research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture for integer multiplication (also: n log n optimality conjecture, Schönhage–Strassen conjecture)
- Established n log n multiplier
- Arrays, addresses and volume on tapes (also: address field, logical volume)
- Elementary stream operations (also: split and merge, row splitting)
- Controlled cyclic shifts (also: controlled shifts, ordered affine streams)
- Rank, subspaces and orthogonal complements (also: nondegenerate subspace, orthogonal residual)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Frames on wire arrays (also: frame, common-frame identity)
- Subspace labels from three-element subsets (also: rank saving construction, orthogonal residual labels)
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
- Recursive rank saving (also: power saving recurrence)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Logarithms and iterated logarithm notation (also: log, lg, log base 2, log2, powers of the logarithm, (lg n)^c)
- Big-Omega, Theta and little-o notation (also: Omega, Theta, Ω, Θ, little-o, asymptotic lower bound, tight bound)
- Binary representation and bit operations (also: binary strings, bits, XOR, exclusive or, bitwise operations, two's complement, Hamming weight, bit length)
- Modular arithmetic (also: congruence, residues mod m, Z/mZ, integers modulo m, centered residue, mod, wraparound)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, Euclidean algorithm, prime number theorem, primes just below a number)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, Euler's formula, twiddle factor, ω)
- Vectors, matrices and invertibility (also: matrix multiplication, matrix inverse, invertible matrix, linear map, linear combination, lower-triangular matrix, permutation matrix, identity matrix, transpose, linear operator)
- Finite field F2 arithmetic (also: GF(2), binary field, mod 2 arithmetic, Z/2Z, F_2)
- Permutations and Cartesian products (also: bijection, permutation of indices, index set, product set, multi-index, coordinate permutation, lexicographic order, mixed-radix indexing, row-major order)
- Floor, ceiling and summation notation (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, sigma notation, geometric series, indicator vector)
- Recurrences and induction (also: recurrence relation, solving recurrences, unrolling a recurrence, proof by induction, master theorem, divide and conquer recurrence)
- Norms, absolute values and error bounds (also: max norm, sup norm, infinity norm, triangle inequality, modulus bound, rounding error, truncation error, round to nearest integer, unit disk)
- Fast Fourier transform and divide and conquer (also: FFT, Cooley-Tukey, fast Fourier transform, O(n log n) transform, convolution theorem, multiplying polynomials by FFT)
- Sorting and data movement on tapes (also: sorting, merge, scan, linear scan, stream, sequential access)
- Finite alphabet encodings and constant-factor simulation (also: alphabet, constant overhead, constant factor slowdown, encoding data as tape symbols, fixed finite state control, Turing machine simulation)
- Ring and group notions for polynomials (also: commutative ring, ring with identity, quotient ring, isomorphism, ring homomorphism, unit of a ring)

## This page

Concept: Packed selected-bit addition
Gloss: A binary row addition y_j ← y_j ⊕ x_j on the same bit position in f address chunks at once, done with eight chunk-wide cyclic shifts whose segments cannot carry into each other except at a small explicit set of exceptional addresses, which are then repaired deterministically; it restores the third chunk's arbitrary contents.
Also called: packed XOR, exceptional address repair

## This page in the argument

The step: Packed selected-bit addition: for $L=fK$, a binary row addition $y_{j_i}\gets y_{j_i}\oplus x_{j_i}$ ($j_i=\rho+iK$, $0\le i<f$) on chunks $x,y$ with an arbitrary third chunk $z$ restored costs $O(V(L^\tau+1))$.
How: Realize the XORs as eight whole-chunk cyclic shifts (in which $K$-bit segments cannot carry into each other except at a small set $\mathcal B$ of addresses), compute the exact correction on $\mathcal B$ by extraction, radix sorting and reinsertion, and bound $|\mathcal B|$ by a union bound.
Why: The sources say they use a constant number of cyclic shifts of whole chunk ranges and then correct an explicitly bounded set of addresses. (the sources say so: "cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of" (paper))
Striking feature: Eight additions of at most one on integers whose parity tests are mutually dependent compose to a pure parity flip of $u$ that leaves the other integer $w$ unchanged for every initial value. (explain why it holds, from the method)

Its sub-steps, in order:

- For a Boolean control $c$ and integers $u,w$, eight conditional $\pm c$ updates (tested on parities of the other integer) act, for $c=1$, as the cycle $(00\ 01\ 10)$ on parity pairs $(u,w)$ in every $2\times2$ square for the first four, and $(01\ 10\ 11)$ for the last four.
- Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$.
- Hence the output is $(u',w')=(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are preserved, and the auxiliary integer $w$ is restored; each coordinate moves by at most eight.
- Write segment values as $u_i=2g_i+a_i$, $w_i=2h_i+b_i$ with guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$ for the $f-1$ disjoint $K$-bit segments below the top selected position, with control $c_i=x_{j_i}$.
- Each of the eight lines for all segments at once is one cyclic shift of the target chunk $y\gets y+\varepsilon\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^L}$, whose offset does not depend on the target, so each line is a bijection.
- Let $\mathcal B$ be the addresses where some used guard fails $10\le g\le2^{K-1}-11$; outside $\mathcal B$ every segment lies in $[20,2^K-21]$ and even displacement eight stays within $[0,2^K-1]$, so no segment carries into the next and the shifts $S_0$ agree with the ideal XOR permutation $T_0$.
- Each guard has exactly twenty excluded values among $2^{K-1}$, so the union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of record values.
- Since $T_0$ and $S_0$ are bijections agreeing off $\mathcal B$, $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$, so the correction is a permutation of the exceptional records.
- Each rotation moves its target to the rightmost chunk position by one chunk swap of width $L$ (cost $O(VL^\tau)$ by the arbitrary-width interchange), then uses the controlled-shift lemma in $O(V)$ and undoes the swap; $S_0$ uses at most sixteen swaps and eight rotations.
- Extract the records of $\mathcal B$ with destination ranks as keys, stably radix-sort only those records, and reinsert them in one forward scan, which implements $T_0$ everywhere deterministically (the keys are distinct and equal the marked holes).
- Total movement is $O(V(L^\tau+1))$, scans of the full stream $O(MA_{\rm rect}^3+V)$ and the radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$.
- After dividing by $V=MR$ the extra terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$; with $A_{\rm rect}=O(p)$, $R$ above every fixed polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$ they are $o(1)$, so the cost is $O(V(L^\tau+1))$.
- A fixed invertible binary change of basis on $e=mf$ axes (and its inverse) therefore costs $O(V((eK)^\tau+1))$, since slot width is $L=(e/m)K$.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- Both tape procedures cost a power of their parameter below one, because each runs a fixed linear exchange network on $W$ wires whose edge changes are smaller calls on role streams of volume $V/W$, with total number of calls $s<Wm$, so that each level of recursion multiplies the cost per volume by $s/W<m^\tau$ while the parameter shrinks by $m$.; how: Build a finite linear exchange network that restores its scratch wires, give its vertices frames so that only endpoint operators matter, attach nested subspace labels so that the total rank $s$ of all edge changes is below $Wm$, and unroll the resulting recursion once with bit gates (address-chunk interchange) and once with Gaussian-dyadic phase gates (simultaneous butterfly layer). (on [Recursive rank saving](rank-saving-recurrence.md))
- Fast simultaneous butterfly layer: $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied coefficientwise at the same bit offset in $D\le d$ address chunks of a polynomial-record array costs $O(Vd^{\lambda'})$ with $\lambda'=1-2^{-54}$, evaluating the whole layer exactly before a single truncation.; how: Express the layer through the complex phase network (kernels $C$ on smaller groups of selected bits separated by binary changes of basis), implement the basis changes by whole-chunk moves and packed selected-bit additions, split complete rows among the $W$ roles for volume $V/W$ per recursive call, and bound the intermediate dyadic values. (on [Fast simultaneous butterfly layer](fast-butterfly-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.6.2.1, S4.6.2.2, S4.6.2.3, S4.6.2.4, S4.6.2.5, S4.6.2.6, S4.6.2.7, S4.6.2.8, S4.6.2.9, S4.6.2.10, S4.6.2.11, S4.6.2.12, S4.6.2.13). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.6.2.1**: For a Boolean control $c$ and integers $u,w$, eight conditional $\pm c$ updates (tested on parities of the other integer) act, for $c=1$, as the cycle $(00\ 01\ 10)$ on parity pairs $(u,w)$ in every $2\times2$ square for the first four, and $(01\ 10\ 11)$ for the last four.
Source: "induce the cycle $(00\ 01\ 10)$ in every square" (paper)
> et. For a Boolean control $c$ and arbitrary integers $u,w$, perform the following eight operations in the displayed chronological order. Every predicate uses the current values of the integers. \begin{equation} \label{eq:eight-packed-additions} \begin{array}{rcl@{\qquad}l} u&\leftarrow&u-c[\,w\equiv0\pmod2\,],&(1)\\ w&\leftarrow&w-c[\,u\equiv0\pmod2\,],&(2)\\ u&\leftarrow&u+c[\,w\equiv0\pmod2\,],&(3)\\ w&\leftarrow&w+c[\,u\equiv0\pmod2\,],&(4)\\ w&\leftarrow&w+c[\,u\equiv1\pmod2\,],&(5)\\ u&\leftarrow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Ea

**S4.6.2.2**: Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$.
Source: "Applying the first cycle and then the second gives" (paper)
> quation} \label{eq:eight-packed-additions} \begin{array}{rcl@{\qquad}l} u&\leftarrow&u-c[\,w\equiv0\pmod2\,],&(1)\\ w&\leftarrow&w-c[\,u\equiv0\pmod2\,],&(2)\\ u&\leftarrow&u+c[\,w\equiv0\pmod2\,],&(3)\\ w&\leftarrow&w+c[\,u\equiv0\pmod2\,],&(4)\\ w&\leftarrow&w+c[\,u\equiv1\pmod2\,],&(5)\\ u&\leftarrow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Each coordinate is updated four times by at most one, so its displacement from its initial value is at most four, even if an intermediate point leaves its starting quotient square. The weaker bound eight w

**S4.6.2.3**: Hence the output is $(u',w')=(u+c(1-2(u\bmod2)),w)$: the parity of $u$ flips exactly when $c=1$, both quotients by two are preserved, and the auxiliary integer $w$ is restored; each coordinate moves by at most eight.
Source: "\bigl(u+c(1-2(u\bmod2)),\ w\bigr)." (paper)
> ow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Each coordinate is updated four times by at most one, so its displacement from its initial value is at most four, even if an intermediate point leaves its starting quotient square. The weaker bound eight will suffice below.

**S4.6.2.4**: Write segment values as $u_i=2g_i+a_i$, $w_i=2h_i+b_i$ with guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$ for the $f-1$ disjoint $K$-bit segments below the top selected position, with control $c_i=x_{j_i}$.
Source: "u_i=2g_i+a_i,\qquad w_i=2h_i+b_i," (paper)
> Omit the most significant selected position $j_{f-1}$ temporarily. For each $0\le i<f-1$, the bits in positions $j_i,\ldots,j_i+K-1$ form a $K$-bit segment. When $f>1$, these segments are disjoint, and the highest one ends immediately below $j_{f-1}$. Write their initial values in $y$ and $z$ as \[ u_i=2g_i+a_i,\qquad w_i=2h_i+b_i, \qquad a_i,b_i\in\{0,1\}. \] The values $g_i,h_i\in\{0,\ldots,2^{K-1}-1\}$ are the guard values. The control for this pair of segments is the selected bit $c_i=x_{j_i}$.

**S4.6.2.5**: Each of the eight lines for all segments at once is one cyclic shift of the target chunk $y\gets y+\varepsilon\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=b]\pmod{2^L}$, whose offset does not depend on the target, so each line is a bijection.
Source: "\varepsilon\sum_{i=0}^{f-2}2^{j_i}" (paper)
> Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all these segment pairs. Physically, a line updating $y$ by sign $\varepsilon$ and testing parity $b$ of $z$ is the single cyclic shift \begin{equation} \label{eq:packed-cyclic-shift} y\longleftarrow y+ \varepsilon\sum_{i=0}^{f-2}2^{j_i} [\,x_{j_i}=1\,][\,z_{j_i}=b\,] \pmod{2^L}. \end{equation} For a line updating $z$, interchange $y$ and $z$ in this formula. The shift offset never depends on its target chunk, so each line is a bijection of the rectangle. Let $S_0$ be their composition. It fixes the spectator coordinates.

**S4.6.2.6**: Let $\mathcal B$ be the addresses where some used guard fails $10\le g\le2^{K-1}-11$; outside $\mathcal B$ every segment lies in $[20,2^K-21]$ and even displacement eight stays within $[0,2^K-1]$, so no segment carries into the next and the shifts $S_0$ agree with the ideal XOR permutation $T_0$.
Source: "10\le g\le 2^{K-1}-11." (paper)
> Let $\mathcal B$ consist of the addresses for which at least one used guard value, in either $y$ or $z$, fails \begin{equation} \label{eq:packed-guard-interval} 10\le g\le 2^{K-1}-11. \end{equation} At an address outside $\mathcal B$, each segment initially lies in $[20,2^K-21]$. Even displacement eight keeps it inside $[0,2^K-1]$. Inductively, each packed addition therefore agrees with all the independent segment additions: no segment carries into or borrows from the next segment. When $f>1$, the bits below $j_0$ and above the highest used segment are untouched as well. By \eqref{eq:eight-packed-result}, $S_0$ then agrees with the ideal permutation $T_0$ that performs the required XORs at $j_0,\ldots,j_{f-2}$ and fixes all other address coordinates.

**S4.6.2.7**: Each guard has exactly twenty excluded values among $2^{K-1}$, so the union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of record values.
Source: "There are exactly twenty excluded values for each guard in" (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**S4.6.2.8**: Since $T_0$ and $S_0$ are bijections agreeing off $\mathcal B$, $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$, so the correction is a permutation of the exceptional records.
Source: "Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$." (paper)
> The ideal map $T_0$ preserves all guard values and therefore preserves $\mathcal B$. Both $T_0$ and $S_0$ are bijections, and they agree off $\mathcal B$. Taking complements in the finite rectangle gives \[ S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c, \qquad S_0(\mathcal B)=\mathcal B. \] Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$. It remains to implement the rotations and this correction on tapes.

**S4.6.2.9**: Each rotation moves its target to the rightmost chunk position by one chunk swap of width $L$ (cost $O(VL^\tau)$ by the arbitrary-width interchange), then uses the controlled-shift lemma in $O(V)$ and undoes the swap; $S_0$ uses at most sixteen swaps and eight rotations.
Source: "There are at most sixteen swaps and eight rotations in $S_0$." (paper)
> The equal chunk lengths leave the field-length list unchanged by a completed swap. Keep the permutation of the logical names $x,y,z$ in finite local state. With the target now after its two controls, collapse the remaining intervals to obtain \[ [\Lambda_0]\times[2^L]_{\rm control\,1}\times[\Lambda_1] \times[2^L]_{\rm control\,2}\times[\Lambda_2] \times[2^L]_{\rm target}\times[B_{\rm rot}], \] where $B_{\rm rot}$ includes the payload and every displayed spectator length is positive. Their product with the chunk lengths is $V$. Together with $K,f,\rho$ and the finite name permutation, these fixed canonical lengths form an $O(A_{\rm rect})$-bit local descriptor. The offset routine receives the two current $L$-bit logical control values. A scan of at most $f\le L$ selected positions evaluates \eqref{eq:packed-cyclic-shift} in $L^{O(1)}$ time, without reading the target or spectator values. Lemma~\ref{lem:ordered-affine-streams} therefore gives an $O(V)$ rotation: its offset work is absorbed by the $2^L$ nonempty target blocks in each fiber. Undo the swap after the rotation. The local descriptors and name permutation are updated at completed swap boundaries; the primitives use their own descriptors inside padded layouts. There are at most sixteen swaps and eight rotations in $S_0$.

**S4.6.2.10**: Extract the records of $\mathcal B$ with destination ranks as keys, stably radix-sort only those records, and reinsert them in one forward scan, which implements $T_0$ everywhere deterministically (the keys are distinct and equal the marked holes).
Source: "while stable binary radix sorting scans only the extracted records and" (paper)
> If $q_h,q'_h$ are the current and destination values of chunk $h\in\{x,y,z\}$ and $\sigma_h$ is its record stride, the fixed spectator coordinates give \[ \operatorname{rank}(q')=\operatorname{rank}(q)+ \sum_{h\in\{x,y,z\}}(q'_h-q_h)\sigma_h. \] The differences are signed. Attach this destination rank, padded to $\lceil\log_2M\rceil\le A_{\rm rect}$ bits, to the extracted record, and mark its hole on a fixed track of the full stream. Hold the full stream untouched while stable binary radix sorting scans only the extracted records and keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes $\mathcal B$, these keys are distinct and are exactly the ranks of the marked holes. One forward full-stream scan reinserts the sorted records. This implements $T_0$ everywhere.

**S4.6.2.11**: Total movement is $O(V(L^\tau+1))$, scans of the full stream $O(MA_{\rm rect}^3+V)$ and the radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$.
Source: "The movement costs $O(V(L^\tau+1))$." (paper)
> The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty. The initial descriptor has a fixed number of canonical integers of $O(A_{\rm rect})$ bits, so its preparation is covered by $O(MA_{\rm rect}^3)$. All counters, positioning, rewinds, and cleanup are included. Equation~\eqref{eq:packed-bad-fraction} proves \eqref{eq:packed-rectangle-time} on a fixed number of tapes. After division by $V=MR$, its additional terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion. \end{proof}

**S4.6.2.12**: After dividing by $V=MR$ the extra terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$; with $A_{\rm rect}=O(p)$, $R$ above every fixed polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$ they are $o(1)$, so the cost is $O(V(L^\tau+1))$.
Source: "After division by $V=MR$, its additional terms are bounded by" (paper)
> The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty. The initial descriptor has a fixed number of canonical integers of $O(A_{\rm rect})$ bits, so its preparation is covered by $O(MA_{\rm rect}^3)$. All counters, positioning, rewinds, and cleanup are included. Equation~\eqref{eq:packed-bad-fraction} proves \eqref{eq:packed-rectangle-time} on a fixed number of tapes. After division by $V=MR$, its additional terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion. \end{proof}

**S4.6.2.13**: A fixed invertible binary change of basis on $e=mf$ axes (and its inverse) therefore costs $O(V((eK)^\tau+1))$, since slot width is $L=(e/m)K$.
Source: "$O(V((eK)^\tau+1))$ on a stream of volume $V$." (paper)
> Under the asymptotic hypotheses in the final assertion of that lemma, the complete change of basis and its inverse therefore cost $O(V((eK)^\tau+1))$ on a stream of volume $V$. Here $e$ counts axis chunks, while $eK$ counts address bits; the fixed factor $m$ between $eK$ and the slot width does not affect the bound. The same conclusion holds after the row padding and splitting below, because every role stream retains a complete suffix with the same fixed field lengths in every row.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Controlled cyclic shifts](controlled-shift.md): An update y ↦ y + a(controls) mod Q of a target field that follows its control fields on tape, done in O(V) by splitting each fiber at the offset and merging the two pieces in the opposite order; also multiplication by a fixed unit and negation of the target.
  Shown as: Packed selected-bit addition *<predicate>* Controlled cyclic shifts
- [Fast address-chunk interchange](address-chunk-interchange.md): The first tape procedure: swapping two disjoint contiguous address fields of u bits, (p,h,g,d,z) ↦ (p,d,g,h,z), in O(V u^τ) for a fixed τ<1 by building the swap from address shears executed through the bit network, with XOR combinations of intermediate data.
  Shown as: Packed selected-bit addition *<predicate>* Fast address-chunk interchange

## Pages that build on this one

- Fast simultaneous butterfly layer: The second tape procedure: applying H₀ at the same bit offset in d address chunks of a polynomial-record array in cost O(V d^λ') with λ'<1, by evaluating the layer exactly through the phase-frame network with packed chunk moves before a single truncation.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Address shear and lower-triangular factorization](address-shear.md)
- [Frames on wire arrays](common-frame-principle.md)
- [Subspace labels from three-element subsets](subset-intersection-labels.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient (phase) twist](phase-twist.md)
- [Rounding and carry propagation](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional (tensor) transform](multidimensional-dft.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase frames and the two-point kernel C](phase-frame-kernel.md)
- [Fast simultaneous butterfly layer](fast-butterfly-layer.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choices and prime source lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "We implement a binary row addition on corresponding selected bits in two" (paper)

  > We implement a binary row addition on corresponding selected bits in two address chunks. A third chunk supplies temporary address bits; its arbitrary initial value must be restored. The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses. The correction depends only on addresses, so the time bound is worst-case over all payloads.

- "Let $\mathcal B$ consist of the addresses for which" (paper)

  > Let $\mathcal B$ consist of the addresses for which at least one used guard value, in either $y$ or $z$, fails \begin{equation} \label{eq:packed-guard-interval} 10\le g\le 2^{K-1}-11. \end{equation} At an address outside $\mathcal B$, each segment initially lies in $[20,2^K-21]$. Even displacement eight keeps it inside $[0,2^K-1]$. Inductively, each packed addition therefore agrees with all the independent segment additions: no segment carries into or borrows from the next segment. When $f>1$, the bits below $j_0$ and above the highest used segment are untouched as well. By \eqref{eq:eight-packed-result}, $S_0$ then agrees with the ideal permutation $T_0$ that performs the required XORs at $j_0,\ldots,j_{f-2}$ and fixes all other address coordinates.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

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

Write the body to `exegenius/tasks/0018-write-packed-selected-bit-addition.answer.md` and the JSON to `exegenius/tasks/0018-write-packed-selected-bit-addition.answer.json`, then run `exegenius submit 0018-write-packed-selected-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0018-write-packed-selected-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
