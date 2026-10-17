# exegenius task 0175-write-packed-bit-addition

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

Concept: Packed selected-bit addition
Gloss: XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.
Also called: exceptional addresses

## This page in the argument

The step: Selected bits of two chunks can be XORed (with a third chunk as restored scratch) by eight cyclic shifts of whole chunk ranges plus a repair of an explicitly bounded exceptional set of addresses, in time $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$.
How: Apply eight packed parity-conditioned additions (a composition of two three-cycles) simultaneously to $f-1$ disjoint $K$-bit segments, so it equals the ideal XORs away from addresses where a guard value is too close to a segment boundary, then repair those addresses by extracting them and sorting.
Why: Parity-conditioned additions flip the target parity and restore the auxiliary integer, and they can be applied to all segments at once as one cyclic shift of a whole chunk range, costing linear time per rotation; carries between packed segments only occur at a small, address-determined set of exceptional addresses. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$ the time of the procedure is bounded as stated.
- The eight parity-conditioned additions induce, for $c=1$, the cycle $(00\ 01\ 10)$ and then $(01\ 10\ 11)$ on parities of $(u,w)$, whose composition is $(00\ 10)(01\ 11)$: it flips the parity of $u$ and restores $w$.
- The complete output is $(u',w')=(u+c(1-2(u\bmod2)),w)$, with quotients preserved and the arbitrary auxiliary integer $w$ restored.
- For $f-1$ disjoint $K$-bit segments write $u_i=2g_i+a_i$, $w_i=2h_i+b_i$; the guard values satisfy $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$.
- Each line of the eight additions, applied to all segments at once, is a single cyclic shift of a whole target chunk by an offset that does not depend on the target chunk, hence a bijection of the rectangle.
- Away from the set $\mathcal B$ of addresses where some guard fails $10\le g\le2^{K-1}-11$, no segment carries into or borrows from its neighbour (even displacement eight stays inside $[0,2^K-1]$), so the packed shifts agree with the ideal XORs.
- There are exactly twenty excluded values for each guard.
- A union bound over the $2(f-1)$ guards, with the same guard distribution at every choice of spectator coordinates, gives the bound on the exceptional set.
- Hence $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of record values.
- Both the ideal map $T_0$ and the packed map $S_0$ are bijections agreeing off $\mathcal B$, so $T_0S_0^{-1}$ fixes the complement of $\mathcal B$ and permutes $\mathcal B$.
- The packed map uses at most sixteen chunk swaps and eight rotations (rotations by controlled shifts in linear time, swaps by the chunk-interchange lemma).
- The correction extracts the exceptional records with destination-rank keys (distinct, since $T_0S_0^{-1}$ permutes $\mathcal B$), stably radix-sorts them by key, and reinserts them in one scan.
- The movement costs $O(V(L^\tau+1))$ and a fixed number of record scans costs $O(MA_{\rm rect}^3+V)$.
- Dividing by $V$, the extra terms are $A_{\rm rect}^3/R\to0$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)=o(1)$ under $A_{\rm rect}=O(p)$, $R$ above every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, so the cost is $O(V(L^\tau+1))$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.; how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). (on [Recursive power saving](rank-recurrence.md))
- Complex variant: the tensor product of $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ on one bit of each of $D\le d$ address chunks (each of $K$ bits, selected at a common offset), acting coefficientwise on polynomial records with $r$ complex $p$-bit coefficients, is computed exactly followed by one truncation $Q_p$, in $O(Vd^{\lambda'})$ time with $\lambda'<1$, rather than $D$ whole-array passes.; how: Rewrite $H_0^{\otimes D}$ as $b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with the kernel $C$, apply $C^{\otimes e}$ to a group of $e=mf$ axes by the complex network with column phase frames (the binary changes of basis done by packed selected-bit additions), so that each of the $s_{\rm c}$ edge-residual vectors is one child on $f=e/m$ axes of volume $V/W$, and unroll the resulting recurrence with an exact-width guard bound. (on [Simultaneous butterfly layer](simultaneous-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.6.3.1, S1.6.3.2, S1.6.3.3, S1.6.3.4, S1.6.3.5, S1.6.3.6, S1.6.3.7, S1.6.3.8, S1.6.3.9, S1.6.3.10, S1.6.3.11, S1.6.3.12, S1.6.3.13, S1.6.3.14). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.6.3.1**: With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$ the time of the procedure is bounded as stated.
Source: "With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is" (paper)
> times[2^L]_{\chi_3}\times[N_3]. \] The subscript names the chunk at that position. The input supplies $N_0,\ldots,N_3,R,K,f,\rho$ as a fixed number of canonical binary integers, together with the finite permutation of the chunk names, as in Section~\ref{sec:streams}. Put \[ M=2^{3L}\prod_{h=0}^3N_h,\qquad V=MR,\qquad A_{\rm rect}=\lceil\log_2(2V)\rceil. \] At the selected positions $j_i=\rho+iK$, numbered from the least significant bit, one fixed multitape procedure performs \[ y_{j_i}\longleftarrow y_{j_i}\mathbin\oplus x_{j_i} \quad(0\le i<f). \] It preserves the spectator coordinates, all other chunk bits, and every record payload; in particular, it restores the entire chunk $z$ for every initial value. With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is \begin{equation} \label{eq:packed-rectangle-time} O\!\left(V(L^\tau+1)+MA_{\rm rect}^3+ \delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect})\right). \end{equation} When $A_{\rm rect}=O(p)$, $R$ exceeds every fixed polynomial in $p$, $f\le d\le p$, and $K/\log p\to\infty$, this is $O(V(L^\tau+1))$, uniformly over the permitted lengths and payloads in the fixed family. \end{lemma}

**S1.6.3.2**: The eight parity-conditioned additions induce, for $c=1$, the cycle $(00\ 01\ 10)$ and then $(01\ 10\ 11)$ on parities of $(u,w)$, whose composition is $(00\ 10)(01\ 11)$: it flips the parity of $u$ and restores $w$.
Source: "$(00\ 10)(01\ 11)$. These facts follow by substituting the four parity" (paper)
> {\qquad}l} u&\leftarrow&u-c[\,w\equiv0\pmod2\,],&(1)\\ w&\leftarrow&w-c[\,u\equiv0\pmod2\,],&(2)\\ u&\leftarrow&u+c[\,w\equiv0\pmod2\,],&(3)\\ w&\leftarrow&w+c[\,u\equiv0\pmod2\,],&(4)\\ w&\leftarrow&w+c[\,u\equiv1\pmod2\,],&(5)\\ u&\leftarrow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Each coordinate is updated four times by at most one, so its displacement from its initial value is at most four, even if an intermediate point leaves its starting quotient square. The weaker bound eight will suffice below.

**S1.6.3.3**: The complete output is $(u',w')=(u+c(1-2(u\bmod2)),w)$, with quotients preserved and the arbitrary auxiliary integer $w$ restored.
Source: "\bigl(u+c(1-2(u\bmod2)),\ w\bigr)." (paper)
> ow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Each coordinate is updated four times by at most one, so its displacement from its initial value is at most four, even if an intermediate point leaves its starting quotient square. The weaker bound eight will suffice below.

**S1.6.3.4**: For $f-1$ disjoint $K$-bit segments write $u_i=2g_i+a_i$, $w_i=2h_i+b_i$; the guard values satisfy $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$.
Source: "The values $g_i,h_i\in\{0,\ldots,2^{K-1}-1\}$ are the guard values. The" (paper)
> Omit the most significant selected position $j_{f-1}$ temporarily. For each $0\le i<f-1$, the bits in positions $j_i,\ldots,j_i+K-1$ form a $K$-bit segment. When $f>1$, these segments are disjoint, and the highest one ends immediately below $j_{f-1}$. Write their initial values in $y$ and $z$ as \[ u_i=2g_i+a_i,\qquad w_i=2h_i+b_i, \qquad a_i,b_i\in\{0,1\}. \] The values $g_i,h_i\in\{0,\ldots,2^{K-1}-1\}$ are the guard values. The control for this pair of segments is the selected bit $c_i=x_{j_i}$.

**S1.6.3.5**: Each line of the eight additions, applied to all segments at once, is a single cyclic shift of a whole target chunk by an offset that does not depend on the target chunk, hence a bijection of the rectangle.
Source: "The shift offset never depends on its target chunk, so each line is a" (paper)
> Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all these segment pairs. Physically, a line updating $y$ by sign $\varepsilon$ and testing parity $b$ of $z$ is the single cyclic shift \begin{equation} \label{eq:packed-cyclic-shift} y\longleftarrow y+ \varepsilon\sum_{i=0}^{f-2}2^{j_i} [\,x_{j_i}=1\,][\,z_{j_i}=b\,] \pmod{2^L}. \end{equation} For a line updating $z$, interchange $y$ and $z$ in this formula. The shift offset never depends on its target chunk, so each line is a bijection of the rectangle. Let $S_0$ be their composition. It fixes the spectator coordinates.

**S1.6.3.6**: Away from the set $\mathcal B$ of addresses where some guard fails $10\le g\le2^{K-1}-11$, no segment carries into or borrows from its neighbour (even displacement eight stays inside $[0,2^K-1]$), so the packed shifts agree with the ideal XORs.
Source: "10\le g\le 2^{K-1}-11." (paper)
> Let $\mathcal B$ consist of the addresses for which at least one used guard value, in either $y$ or $z$, fails \begin{equation} \label{eq:packed-guard-interval} 10\le g\le 2^{K-1}-11. \end{equation} At an address outside $\mathcal B$, each segment initially lies in $[20,2^K-21]$. Even displacement eight keeps it inside $[0,2^K-1]$. Inductively, each packed addition therefore agrees with all the independent segment additions: no segment carries into or borrows from the next segment. When $f>1$, the bits below $j_0$ and above the highest used segment are untouched as well. By \eqref{eq:eight-packed-result}, $S_0$ then agrees with the ideal permutation $T_0$ that performs the required XORs at $j_0,\ldots,j_{f-2}$ and fixes all other address coordinates.

**S1.6.3.7**: There are exactly twenty excluded values for each guard.
Source: "There are exactly twenty excluded values for each guard in" (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**S1.6.3.8**: A union bound over the $2(f-1)$ guards, with the same guard distribution at every choice of spectator coordinates, gives the bound on the exceptional set.
Source: "the union bound over the $2(f-1)$ guards gives" (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**S1.6.3.9**: Hence $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of record values.
Source: "|\mathcal B|\le\delta_{\rm bad}M." (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**S1.6.3.10**: Both the ideal map $T_0$ and the packed map $S_0$ are bijections agreeing off $\mathcal B$, so $T_0S_0^{-1}$ fixes the complement of $\mathcal B$ and permutes $\mathcal B$.
Source: "Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$." (paper)
> The ideal map $T_0$ preserves all guard values and therefore preserves $\mathcal B$. Both $T_0$ and $S_0$ are bijections, and they agree off $\mathcal B$. Taking complements in the finite rectangle gives \[ S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c, \qquad S_0(\mathcal B)=\mathcal B. \] Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$. It remains to implement the rotations and this correction on tapes.

**S1.6.3.11**: The packed map uses at most sixteen chunk swaps and eight rotations (rotations by controlled shifts in linear time, swaps by the chunk-interchange lemma).
Source: "There are at most sixteen swaps and eight rotations in $S_0$." (paper)
> The equal chunk lengths leave the field-length list unchanged by a completed swap. Keep the permutation of the logical names $x,y,z$ in finite local state. With the target now after its two controls, collapse the remaining intervals to obtain \[ [\Lambda_0]\times[2^L]_{\rm control\,1}\times[\Lambda_1] \times[2^L]_{\rm control\,2}\times[\Lambda_2] \times[2^L]_{\rm target}\times[B_{\rm rot}], \] where $B_{\rm rot}$ includes the payload and every displayed spectator length is positive. Their product with the chunk lengths is $V$. Together with $K,f,\rho$ and the finite name permutation, these fixed canonical lengths form an $O(A_{\rm rect})$-bit local descriptor. The offset routine receives the two current $L$-bit logical control values. A scan of at most $f\le L$ selected positions evaluates \eqref{eq:packed-cyclic-shift} in $L^{O(1)}$ time, without reading the target or spectator values. Lemma~\ref{lem:ordered-affine-streams} therefore gives an $O(V)$ rotation: its offset work is absorbed by the $2^L$ nonempty target blocks in each fiber. Undo the swap after the rotation. The local descriptors and name permutation are updated at completed swap boundaries; the primitives use their own descriptors inside padded layouts. There are at most sixteen swaps and eight rotations in $S_0$.

**S1.6.3.12**: The correction extracts the exceptional records with destination-rank keys (distinct, since $T_0S_0^{-1}$ permutes $\mathcal B$), stably radix-sorts them by key, and reinserts them in one scan.
Source: "keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes" (paper)
> If $q_h,q'_h$ are the current and destination values of chunk $h\in\{x,y,z\}$ and $\sigma_h$ is its record stride, the fixed spectator coordinates give \[ \operatorname{rank}(q')=\operatorname{rank}(q)+ \sum_{h\in\{x,y,z\}}(q'_h-q_h)\sigma_h. \] The differences are signed. Attach this destination rank, padded to $\lceil\log_2M\rceil\le A_{\rm rect}$ bits, to the extracted record, and mark its hole on a fixed track of the full stream. Hold the full stream untouched while stable binary radix sorting scans only the extracted records and keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes $\mathcal B$, these keys are distinct and are exactly the ranks of the marked holes. One forward full-stream scan reinserts the sorted records. This implements $T_0$ everywhere.

**S1.6.3.13**: The movement costs $O(V(L^\tau+1))$ and a fixed number of record scans costs $O(MA_{\rm rect}^3+V)$.
Source: "The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans" (paper)
> The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty. The initial descriptor has a fixed number of canonical integers of $O(A_{\rm rect})$ bits, so its preparation is covered by $O(MA_{\rm rect}^3)$. All counters, positioning, rewinds, and cleanup are included. Equation~\eqref{eq:packed-bad-fraction} proves \eqref{eq:packed-rectangle-time} on a fixed number of tapes. After division by $V=MR$, its additional terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion. \end{proof}

**S1.6.3.14**: Dividing by $V$, the extra terms are $A_{\rm rect}^3/R\to0$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)=o(1)$ under $A_{\rm rect}=O(p)$, $R$ above every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, so the cost is $O(V(L^\tau+1))$.
Source: "$80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds" (paper)
> The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty. The initial descriptor has a fixed number of canonical integers of $O(A_{\rm rect})$ bits, so its preparation is covered by $O(MA_{\rm rect}^3)$. All counters, positioning, rewinds, and cleanup are included. Equation~\eqref{eq:packed-bad-fraction} proves \eqref{eq:packed-rectangle-time} on a fixed number of tapes. After division by $V=MR$, its additional terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion. \end{proof}

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
- $h_p$ (grid step), bound on [Error tracking and exact recovery](precision-recovery.md): The grid step, 2^{-p}.
- $L$ (log of padded size), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of T.
- $E_{\rm ring}$ (ring convolution error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound of the ring convolution, M(3L+2).
- $\boldsymbol t$ (axis lengths), bound on [Error tracking and exact recovery](precision-recovery.md): The tuple of axis lengths.
- $F_{\boldsymbol t}$ (exact Fourier transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact Fourier transform with axis lengths t.
- $\gamma$ (source scale exponent), bound on [Error tracking and exact recovery](precision-recovery.md): The exponent of the source scale 2^gamma.
- $E_s$ (source transform error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound, in units of h_p, of a source transform.
- $u$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled digits of the first input.
- $v$ (scaled digit array), bound on [Error tracking and exact recovery](precision-recovery.md): The array of scaled digits of the second input.
- $U$ (exact transform of u), bound on [Error tracking and exact recovery](precision-recovery.md): The exact source transform of u.
- $V_1$ (exact transform of v), bound on [Error tracking and exact recovery](precision-recovery.md): The exact source transform of v.
- $G$ (exact opposite transform), bound on [Error tracking and exact recovery](precision-recovery.md): The exact opposite source transform.
- $E_w$ (first-scaling error), bound on [Error tracking and exact recovery](precision-recovery.md): The error bound, in units of h_p, after multiplying by S.
- $Q_0$ (radix), bound on [Error tracking and exact recovery](precision-recovery.md): The radix 2^b of the digits.
- $d_j$ (output digit), bound on [Error tracking and exact recovery](precision-recovery.md): The j-th output digit.
- $k_j$ (carry), bound on [Error tracking and exact recovery](precision-recovery.md): The carry into position j.
- $\tau$ (chunk-swap exponent), bound on [Parameter and prime-length choice](parameter-choice.md): An exponent bounding the cost of an equal-width chunk interchange.
- $\sigma$ (recursion exponent), bound on [Parameter and prime-length choice](parameter-choice.md): An exponent bounding the growth of the layer's recursion.
- $\beta$ (threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the threshold d^beta of active chunks handled singly.
- $\lambda$ (node overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the per-node overhead in the butterfly layer.
- $\lambda'$ (layer cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the final layer cost O(V d^lambda').
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent giving the chunk width K = floor(d^c).
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent giving the axis count d = floor(b^epsilon).
- $C_1$ (guard-bit exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of d in the number of reserved guard bits.
- $\delta$ (resampling-cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent delta in the cost of the Gaussian resampling maps.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The logical bit volume of the data the layer acts on.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The number of bits in an address chunk.
- $a_d$ (lower axis constant), bound on [Parameter and prime-length choice](parameter-choice.md): The constant in the lower bound a_d p^epsilon <= d.
- $b_d$ (upper axis constant), bound on [Parameter and prime-length choice](parameter-choice.md): The constant in the upper bound d <= b_d p^epsilon.
- $a_r$ (lower record constant), bound on [Parameter and prime-length choice](parameter-choice.md): The constant in the lower bound 2^{a_r p/d} <= r.
- $b_r$ (upper record constant), bound on [Parameter and prime-length choice](parameter-choice.md): The constant in the upper bound r <= 2^{b_r p/d}.
- $C_\ell$ (address-bit constant), bound on [Parameter and prime-length choice](parameter-choice.md): The constant in the bound d*ell <= C_ell p on the total address bits.
- $\eta$ (relative distance), bound on [Parameter and prime-length choice](parameter-choice.md): The relative distance 1/(4d) of each prime s_i below t_i.
- $\theta_i$ (axis relative gap), bound on [Parameter and prime-length choice](parameter-choice.md): The relative gap t_i/s_i - 1 of axis i.
- $x$ (real argument), bound on [Parameter and prime-length choice](parameter-choice.md): A real number, the length at which the prime interval is taken.
- $q$ (integer in interval), bound on [Parameter and prime-length choice](parameter-choice.md): An integer, in the prime interval.
- $E$ (first space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The first of the two vector spaces being tensored.
- $G$ (second space), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): The second of the two vector spaces being tensored.
- $\xi$ (vector in E), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A vector of the first space E.
- $\eta$ (vector in G), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A vector of the second space G.
- $\phi$ (operator on E), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A linear map from E to itself.
- $\psi$ (operator on G), bound on [Tensor products of subspaces](tensor-product-of-spaces.md): A linear map from G to itself.
- $s$ (number of smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration.
- $F$ (one-factor label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $S$ (a triple), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A three-element subset of $[h]$, used with $T$ to state the indicator inner products.
- $T$ (a triple), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A three-element subset of $[h]$ (not the padded size used on other pages).
- $t_T$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of the triple $T$.
- $\mathcal F$ (ambient label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $F^{\otimes3}$, of dimension $m=h^3$, in which all labels lie.
- $X$ (X bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $X_a$.
- $Y$ (Y bank), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The bank of data wires $Y_a$.
- $a$ (triple tuple), bound on [Nested subspace labels and rank deficit](subspace-labels.md): A tuple $(a_1,a_2,a_3)$ of triples indexing one data wire in each bank.
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
- $t_X$ (X-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the X-bank triple of a gate or wire in one invocation.
- $t_Y$ (Y-bank indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator of the Y-bank triple of a gate or wire in one invocation.
- $L_{\rm b}$ (bit dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the bit network.
- $L_{\rm c}$ (complex dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges of the complex network.
- $\Pi_U$ (projection onto a label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The rational projection onto the label $U$ along $U^\perp$, the matrix of a bit-network vertex labelled $U$.
- $s_{\rm b}$ (bit smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total rational rank of edge matrix changes, in the bit network.
- $s_{\rm c}$ (complex smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of smaller calls, the total number of phase kernels, in the complex network.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes in a butterfly layer.
- $m$ (slot count), bound on [Recursive power saving](rank-recurrence.md): The number of size-f slots into which a call at parameter mf cuts its parameter, equal to 10^6, the label-space dimension.
- $s$ (number of smaller calls), bound on [Recursive power saving](rank-recurrence.md): The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (cost per unit volume), bound on [Recursive power saving](rank-recurrence.md): F(f) is the running time of a call at parameter f divided by the volume of its data.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels between the top call and the nodes considered.
- $\tau$ (saving exponent), bound on [Recursive power saving](rank-recurrence.md): A fixed exponent below 1 with s/W < m^tau, which makes an interchange cost O(V f^tau); here tau = 1 - 2^{-50}.
- $\eta$ (relative rank deficit), bound on [Recursive power saving](rank-recurrence.md): The fraction (Wm - s)/(Wm) by which the number of smaller calls s falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two address chunks.
- $V$ (volume), bound on [Fast address-chunk interchange](address-interchange.md): The number of stored bits of the array.
- $\tau$ (time exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below 1 in the time bound, 1-2^{-50}.
- $p$ (prefix), bound on [Fast address-chunk interchange](address-interchange.md): The address field before the first chunk.
- $h$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The address field of the first chunk.
- $d$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The address field of the second chunk.
- $g$ (gap), bound on [Fast address-chunk interchange](address-interchange.md): The address field between the chunks.
- $z$ (suffix), bound on [Fast address-chunk interchange](address-interchange.md): The address field after the second chunk.
- $q$ (radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime used as digit radix.
- $H$ (first chunk value), bound on [Fast address-chunk interchange](address-interchange.md): The value of the first chunk, a vector of m fields.
- $D$ (second chunk value), bound on [Fast address-chunk interchange](address-interchange.md): The value of the second chunk, a vector of m fields.
- $e$ (chunk digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-q digits in each chunk.
- $k$ (level count), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e=m^k.
- $b$ (field digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of digits in each of the m fields of a chunk.
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The rational m by m matrix assigned to a terminal or gate.
- $i$ (edge index), bound on [Fast address-chunk interchange](address-interchange.md): Index of an edge of the network.
- $A_i$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The difference of the matrices at the head and tail of edge i.
- $I_m$ (identity matrix), bound on [Fast address-chunk interchange](address-interchange.md): The m by m identity matrix.
- $w$ (wire index), bound on [Fast address-chunk interchange](address-interchange.md): The index of a wire of the network, 1 to W.
- $\Phi_M$ (shear permutation), bound on [Fast address-chunk interchange](address-interchange.md): The array permutation moving the entry at address (H,D) to (H+MD,D).
- $M'$ (other matrix), bound on [Fast address-chunk interchange](address-interchange.md): Another rational m by m matrix.
- $x$ (stream row), bound on [Fast address-chunk interchange](address-interchange.md): The row number within a role stream.
- $f_w$ (input array), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array on wire w.
- $f'_{\rho(w)}$ (output array), bound on [Fast address-chunk interchange](address-interchange.md): The physical output array at role rho(w).
- $j$ (level), bound on [Fast address-chunk interchange](address-interchange.md): Index of a level of the unrolled recurrence.
- $F_k$ (normalized cost), bound on [Fast address-chunk interchange](address-interchange.md): The time per unit volume of the interchange at width m^k.
- $k'$ (level count), bound on [Fast address-chunk interchange](address-interchange.md): The least integer with m^{k'} at least e.
- $\nu$ (top digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk interchanged first.
- $h^+$ (high part of h), bound on [Fast address-chunk interchange](address-interchange.md): The top nu digits of the first chunk.
- $h^-$ (rest of h), bound on [Fast address-chunk interchange](address-interchange.md): The remaining digits of the first chunk.
- $d^+$ (high part of d), bound on [Fast address-chunk interchange](address-interchange.md): The top nu digits of the second chunk.
- $d^-$ (rest of d), bound on [Fast address-chunk interchange](address-interchange.md): The remaining digits of the second chunk.
- $\Lambda$ (row range), bound on [Fast address-chunk interchange](address-interchange.md): The range of the row field formed by the two high parts.
- $\Lambda'$ (padded row range), bound on [Fast address-chunk interchange](address-interchange.md): The row count after padding with zero rows.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j, the j-th base-m digit of e minus nu.
- $u$ (vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m on this page.
- $v$ (vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m on this page.
- $w$ (vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m on this page.
- $z$ (vector), bound on [Binary phase frames](phase-frames.md): A vector of F_2^m on this page.
- $x$ (address), bound on [Binary phase frames](phase-frames.md): An address, an element of F_2^m indexing the arrays.
- $q_U$ (phase exponent), bound on [Binary phase frames](phase-frames.md): The Hamming weight of the projection of x onto the label U, modulo 4.
- $P_U$ (projection), bound on [Binary phase frames](phase-frames.md): The projection onto the label U over F_2.
- $E$ (residual), bound on [Binary phase frames](phase-frames.md): The part of V orthogonal to U on an edge from U to V.
- $\mathcal B$ (residual basis), bound on [Binary phase frames](phase-frames.md): An orthonormal basis of the residual E.
- $\varepsilon$ (phase sign), bound on [Binary phase frames](phase-frames.md): The sign +1 or -1 of the phase coefficient of a basis vector, including the edge direction.
- $L_{\rm c}$ (dimension loss), bound on [Binary phase frames](phase-frames.md): The total dimension lost on decreasing edges of the complex network.
- $s_{\rm c}$ (kernel count), bound on [Binary phase frames](phase-frames.md): The number of translation-kernel factors over the complex network.
- $X_a$ (data bank X), bound on [Binary phase frames](phase-frames.md): The data-bank role indexed by a, with source label U_a and sink label the full space.
- $Y_a$ (data bank Y), bound on [Binary phase frames](phase-frames.md): The data-bank role indexed by a, with source label 0 and sink label U_a^perp.
- $u_a$ (generator of U_a), bound on [Binary phase frames](phase-frames.md): The vector t_{a_1} tensor t_{a_2} tensor t_{a_3} spanning the line U_a.
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns, an address being a k-tuple of addresses.
- $Z$ (sign matrix), bound on [Binary phase frames](phase-frames.md): The diagonal matrix diag(1,-1).
- $Z_{a,k}$ (column sign correction), bound on [Binary phase frames](phase-frames.md): The tensor product of Z on the 27 coordinates of supp(u) in every column, identity elsewhere.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast address-chunk interchange](address-interchange.md): The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
  Shown as: Packed selected-bit addition *<predicate>* Fast address-chunk interchange
- [Controlled shifts and rational scalings](controlled-shifts.md): Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume.
  Shown as: Packed selected-bit addition *<predicate>* Controlled shifts and rational scalings

## Pages that build on this one

- Simultaneous butterfly layer: The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.
- Cost accounting and the exponent κ: Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}).

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
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
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Binary phase frames](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "Packed selected-bit addition on one rectangle" (paper)

  > \begin{lemma}[Packed selected-bit addition on one rectangle] \label{lem:packed-selected-bit-rectangle} Let $R\ge1$, $K\ge6$, $f\ge1$, $L=fK$, and $0\le\rho<K$. Let $N_0,N_1,N_2,N_3$ be positive integers, and let $(\chi_1,\chi_2,\chi_3)$ be a permutation of $(x,y,z)$. Consider $R$-bit records in lexicographic order on \[ [N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2} \times[N_2]\times[2^L]_{\chi_3}\times[N_3]. \] The subscript names the chunk at that position. The input supplies $N_0,\ldots,N_3,R,K,f,\rho$ as a fixed number of canonical binary integers, together with the finite permutation of the chunk names, as in Section~\ref{sec:streams}. Put \[ M=2^{3L}\prod_{h=0}^3N_h,\qquad V=MR,\qquad A_{\rm rect}=\lceil\log_2(2V)\rceil. \] At the selected positions $j_i=\

- "We implement a binary row addition on corresponding selected bits in two" (paper)

  > We implement a binary row addition on corresponding selected bits in two address chunks. A third chunk supplies temporary address bits; its arbitrary initial value must be restored. The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses. The correction depends only on addresses, so the time bound is worst-case over all payloads.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Guards are equidistributed at every spectator choice" (The page never says what a spectator choice is (the remaining address coordinates) nor why each guard is equidistributed: this holds because the y and z chunks range over all their values at every fixed choice of the other coordinates. The count of exceptional addresses rests on this and the reader cannot check it from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "$S_0$ has at most eight rotations and sixteen swaps (cited)." (The page never says why a rotation needs swaps. In the paper (line 2117) the target chunk is moved to the rightmost of the three chunk positions by a swap and the swap is undone after the rotation, giving two swaps per rotation and so sixteen. The page states only the count, with no role or reason, and the count stands in for how the construction works.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "its rank (current rank plus signed chunk differences times strides) is the key, and its hole is marked" (Record rank, strides and marking a hole are never defined, and the page does not say how reversing the eight additions gives the destination or why the rank formula holds. The reader cannot check that the keys equal the holes' ranks or that sorting and refilling apply T_0.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Schoolbook arithmetic on counters costs $O(A_{\rm rect}^3)$ per record" (The page never says which counters or which arithmetic is performed (a record-rank counter, division into mixed-radix field values, reversing eight modular additions over up to f selected positions with f at most A_rect). Schoolbook operations on A-bit integers cost O(A^2), so the reader cannot see why the exponent is three.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- Say what $g$ denotes where it is first used: the page uses it before saying so in "Let $\mathcal B$ (exceptional addresses) be those where a guard of $y$ or $z$ fails $10\le g\le2^{K-1}-11$."

## Previous version (revise it)

It has 429 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 536 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Packed selected-bit addition XORs chosen bits of a chunk $x$ into chunk $y$ (chunks here), restoring a scratch chunk $z$; the [simultaneous butterfly layer](simultaneous-layer.md) on $d$ address chunks needs it.

For a Boolean control $c$ and integers $u,w$, $c[P]$ is $c$ if $P$ holds, else $0$. Do, in order:

$$\begin{array}{llll}
(1)\ u\leftarrow u-c[w\bmod2=0] & (2)\ w\leftarrow w-c[u\bmod2=0] & (3)\ u\leftarrow u+c[w\bmod2=0] & (4)\ w\leftarrow w+c[u\bmod2=0]\\
(5)\ w\leftarrow w+c[u\bmod2=1] & (6)\ u\leftarrow u+c[w\bmod2=1] & (7)\ w\leftarrow w-c[u\bmod2=1] & (8)\ u\leftarrow u-c[w\bmod2=1]
\end{array}$$

For $c=1$, substituting the four parity pairs shows the first four lines induce $(00\ 01\ 10)$ on the parities of $(u,w)$ and the last four induce $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$: it flips the parity of $u$ and restores $w$'s. So $(u',w')=(u+c(1-2(u\bmod2)),w)$, keeping quotients by two. Each variable is changed four times by at most one, so moves at most four, hence eight.

Records have $R$ bits. A chunk has $L=fK$ bits (segment length $K\ge6$); the $f$ selected bits lie at $j_i=\rho+iK$, $0\le i<f$, with offset $\rho<K$; the goal is $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$. Let $M$ count addresses, $V=MR$, and $A_{\rm rect}=\lceil\log_2(2V)\rceil$ bound counter lengths.

Omit $j_{f-1}$ first. For $0\le i<f-1$, the $K$ bits of $y$ from $j_i$ give a segment $u_i=2g_i+a_i$ and those of $z$ give $w_i=2h_i+b_i$, with bits $a_i,b_i$, guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$, and control $c_i=x_{j_i}$. Line (1) on all segments is
$$y\leftarrow y-\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=0]\pmod{2^L}.$$
Other lines vary the sign, tested parity or roles of $y,z$. Each is a cyclic shift of a whole chunk by an offset independent of the target chunk, hence a bijection of the addresses; $S_0$ composes the eight.

Let $\mathcal B$ (exceptional addresses) be those where a guard of $y$ or $z$ fails $10\le g\le2^{K-1}-11$. Off $\mathcal B$ each segment lies in $[20,2^K-21]$, so displacement eight stays in $[0,2^K-1]$: no segment carries into or borrows from a neighbour, and $S_0$ equals the ideal map $T_0$ XORing at $j_0,\dots,j_{f-2}$.

Ten values fall on each side of the interval ($2^{K-1}\ge32$): twenty per guard <cite data-source="paper">There are exactly twenty excluded values for each guard in</cite>. Guards are equidistributed at every spectator choice, so a union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.

$T_0$ flips only the bits $a_i$, preserving guards and so $\mathcal B$. Two bijections agreeing off $\mathcal B$ give $S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$, so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.

A scan extracts records at $\mathcal B$, computing each destination $T_0S_0^{-1}$ by reversing the eight additions; its rank (current rank plus signed chunk differences times strides) is the key, and its hole is marked. As $T_0S_0^{-1}$ permutes $\mathcal B$, the keys are exactly the holes' ranks, so a stable radix sort and one scan refilling holes in order apply $T_0$. $j_{f-1}$ is then XORed by an [elementary stream operation](stream-ops.md), $O(V)$.

$S_0$ has at most eight rotations and sixteen swaps <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>. It performs rotations as [controlled shifts](controlled-shifts.md) costing $O(V)$ and swaps as [chunk interchanges](address-interchange.md) costing $O(VL^\tau)$ for fixed exponent $\tau<1$. Schoolbook arithmetic on counters costs $O(A_{\rm rect}^3)$ per record; at most $A_{\rm rect}$ radix passes sort $|\mathcal B|$ records of $R+A_{\rm rect}$ bits. The time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ <cite data-source="paper">With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is</cite>.

Per $V$ the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. With $p$ the precision bits, both vanish when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, so the cost is $O(V(L^\tau+1))$.

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

Write the body to `exegenius/tasks/0175-write-packed-bit-addition.answer.md` and the JSON to `exegenius/tasks/0175-write-packed-bit-addition.answer.json`, then run `exegenius submit 0175-write-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0175-write-packed-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
