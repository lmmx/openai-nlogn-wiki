# exegenius task 0018-write-packed-bit-addition

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
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
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)

## This page

Concept: Packed selected-bit addition
Gloss: XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast address-chunk interchange](address-interchange.md): The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
  Shown as: Packed selected-bit addition *<predicate>* Fast address-chunk interchange
- [Controlled shifts and rational scalings](controlled-shifts.md): Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume.
  Shown as: Packed selected-bit addition *<predicate>* Controlled shifts and rational scalings

## Pages that build on this one

- Simultaneous butterfly layer: The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Multidimensional transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](chirp.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
- [Two-point kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Parameter and prime-length choice](parameter-choice.md)
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

Write the body to `exegenius/tasks/0018-write-packed-bit-addition.answer.md` and the JSON to `exegenius/tasks/0018-write-packed-bit-addition.answer.json`, then run `exegenius submit 0018-write-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0018-write-packed-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
