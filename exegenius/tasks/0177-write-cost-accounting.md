# exegenius task 0177-write-cost-accounting

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
- The multiplication algorithm
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

Concept: Cost accounting and the exponent κ
Gloss: Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}).

## This page in the argument

The step: The total time of the machine is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$: after dividing each cost by $V=Tp=\Theta(n)$ the dominant terms are powers of $p$ below one, with minimum margin $2^{-181}=2\kappa$.
How: Divide each cost by the volume, list the dominant terms with their powers of $p$, compute their margins below one from the fixed rational parameters, justify each row from the lemmas, show setup is negligible, and add.
Why: Taking the margin to be twice $\kappa$ leaves room for any remaining fixed power of $\log p$. (the sources say so: "This explicit slack will cover" (paper))
Striking feature: The final exponent is only $2^{-182}$ below one: it is set by the least of seven margins, the chunk-exchange row $g_2=\epsilon c(1-\tau)=2^{-181}$. (explain why it holds, from the method)

Its sub-steps, in order:

- Dividing each cost by $V=Tp=\Theta(n)$, seven operations dominate, each a power of $p$ with exponent $1-g_i$ for a margin $g_i>0$ listed row by row.
- The seven margins are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so the minimum is $2^{-181}=2\kappa$.
- Each of the seven normalized costs is justified from the lemmas: the layout exchanges cost $O(pK^{\tau-1})$, axis moves $O(d^2(1+\ell^\tau))$, Gaussian lines $O(dp^{1/2+\delta}\alpha)$, chirps $O(dp^{1+\delta})$ per entry, and polynomial products $O(Tp\log(rp))$ in total.
- Setup at recursion nodes, exceptional-address repair, global setup and prime search together cost $o(V)$.
- Each of the seven displayed powers is at most $1-2\kappa$, any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, and with schoolbook multiplication below a fixed cutoff the single machine runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S6.1, S6.2, S6.3, S6.4, S6.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6.1**: Dividing each cost by $V=Tp=\Theta(n)$, seven operations dominate, each a power of $p$ with exponent $1-g_i$ for a margin $g_i>0$ listed row by row.
How: Tabulate the normalized cost of each operation of the algorithm and read off its power of $p$ from the sizes $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$, $\alpha=\Theta(p^{1/4+\epsilon/2})$; the last two rows (final scaling, input and output) are absorbed.
- S6.1.1: Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $p^{\epsilon(1+c)}$ since $d=\Theta(p^\epsilon)$ and $K=\Theta(p^{\epsilon c})$; margin $g_1=1-\epsilon(1+c)>1/2$.
  Source: "Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\" (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}
- S6.1.2: Chunk exchanges for the transform layout cost $pK^{\tau-1}$, a power $p^{1-\epsilon c(1-\tau)}$ since $K=\Theta(p^{\epsilon c})$; margin $g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}$ (the smallest).
  Source: "Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\" (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}
- S6.1.3: Simultaneous butterfly rounds cost $\ell d^{\lambda'}$ with $\ell=\Theta(p^{1-\epsilon})$, a power $p^{1-\epsilon(1-\lambda')}$; margin $g_3=\epsilon(1-\lambda')=2^{-75}\cdot2^{-54}=2^{-129}$.
  Source: "Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\" (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}
- S6.1.4: CRT and axis layouts cost $d^2(1+\ell^\tau)$, a power $p^{\tau+\epsilon(2-\tau)}$ (as $d^2\ell^\tau=p^{2\epsilon}p^{(1-\epsilon)\tau}$); margin $g_4=1-\tau-\epsilon(2-\tau)>2^{-51}$.
  Source: "CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\" (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}
- S6.1.5: Gaussian line maps cost $dp^{1/2+\delta}\alpha$, a power $p^{3/4+\delta+3\epsilon/2}$ since $\alpha=\Theta(p^{1/4+\epsilon/2})$; margin $g_5=1/4-\delta-3\epsilon/2>1/8$.
  Source: "Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\" (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}
- S6.1.6: Chirps, twists and scalar products cost $dp^\delta$, a power $p^{\epsilon+\delta}$; margin $g_6=1-\delta-\epsilon>1/2$.
  Source: "Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\" (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}
- S6.1.7: Packed polynomial products cost $\log(rp)$, a power $p^{1-\epsilon}$ (since $\log(rp)=O(p^{1-\epsilon})$); margin $g_7=\epsilon=2^{-75}$.
  Source: "Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\" (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}

**S6.2**: The seven margins are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$, so the minimum is $2^{-181}=2\kappa$.
How: Substitute the fixed rational parameters $\epsilon=2^{-75}$, $c=2^{-56}$, $1-\tau=2^{-50}$, $1-\lambda'=2^{-54}$, $\delta=1/16$ into the seven margin expressions.
- S6.2.1: Direct substitution gives $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$.
  Source: "g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad" (paper)
  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.
- S6.2.2: Likewise $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$, $g_7=2^{-75}$.
  Source: "g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}." (paper)
  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.
- S6.2.3: Thus $\min_ig_i=2^{-181}=2\kappa$, explicit slack that covers any remaining fixed power of $\log p$.
  Source: "Thus $\min_i g_i=2^{-181}=2\kappa$.  This explicit slack will cover" (paper)
  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

**S6.3**: Each of the seven normalized costs is justified from the lemmas: the layout exchanges cost $O(pK^{\tau-1})$, axis moves $O(d^2(1+\ell^\tau))$, Gaussian lines $O(dp^{1/2+\delta}\alpha)$, chirps $O(dp^{1+\delta})$ per entry, and polynomial products $O(Tp\log(rp))$ in total.
How: Combine the costs of the lemmas: $O(p/K)$ exchanges each costing $O(VK^\tau)$, $O(d^2)$ axis moves each $O(V(1+\ell^\tau))$, at most $T/t_i$ lines per axis, per-entry chirp arithmetic, and $T/r$ ring products of $O(rp)$ bits each.
- S6.3.1: Each width-$K$ chunk exchange costs $O(VK^\tau)$ by the chunk-interchange lemma.
  Source: "$O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is" (paper)
  > Here $d^2$ is absorbed by $d^2\ell^\tau$, and $\log(rp)=O(p^{1-\epsilon}+\log p)=O(p^{1-\epsilon})$. The first three rows are the terms in \eqref{eq:synthetic-transform-cost}. The prefix-slot moves and individual butterfly rounds in Lemma~\ref{lem:synthetic-transform-cost} use $O(dK)$ linear scans. Its positional layout uses $O(p/K)$ exchanges of width-$K$ chunks, because $d\ell=O(p)$. Each exchange costs $O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is \[ O(p/K)\,K^\tau=O(pK^{\tau-1}). \] For the at most $\ell$ simultaneous rounds, Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$ per round. Its bound already includes the binary basis changes, deterministic repair, row padding and removal, all base-$m$ groups, and fixed-tape cleanup.
- S6.3.2: With $O(p/K)$ exchanges (since $d\ell=O(p)$) the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$.
  Source: "O(p/K)\,K^\tau=O(pK^{\tau-1})." (paper)
  > Here $d^2$ is absorbed by $d^2\ell^\tau$, and $\log(rp)=O(p^{1-\epsilon}+\log p)=O(p^{1-\epsilon})$. The first three rows are the terms in \eqref{eq:synthetic-transform-cost}. The prefix-slot moves and individual butterfly rounds in Lemma~\ref{lem:synthetic-transform-cost} use $O(dK)$ linear scans. Its positional layout uses $O(p/K)$ exchanges of width-$K$ chunks, because $d\ell=O(p)$. Each exchange costs $O(VK^\tau)$ by Lemma~\ref{lem:chunk-swap}, so the normalized total is \[ O(p/K)\,K^\tau=O(pK^{\tau-1}). \] For the at most $\ell$ simultaneous rounds, Proposition~\ref{prop:simultaneous-layer} supplies $O(Vd^{\lambda'})$ per round. Its bound already includes the binary basis changes, deterministic repair, row padding and removal, all base-$m$ groups, and fixed-tape cleanup.
- S6.3.3: Axis exposure and restoration take $O(d^2)$ adjacent axis moves, each costing $O(V(1+\ell^\tau))$ by peeling a single excess bit when widths differ by one, exchanging the equal-width parts and restoring the bit.
  Source: "Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths" (paper)
  > Axis exposure and restoration require $O(d^2)$ adjacent axis moves. Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths differ by one, exchange their equal-width parts, and restore the bit. The $d$ CRT rotations copy valid and invalid intervals in $O(dV)$ time. Their offset setup was bounded above by $O(dTp^C/r)=o(Tp)$, using at most $T/t_i$ control prefixes for target $i$.
- S6.3.4: Axis $i$ has at most $T/t_i$ processed lines, so Gaussian line-machine costs sum to $\sum_iT/t_i\cdot O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.
  Source: "The line-machine costs therefore sum to" (paper)
  > For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines. The line-machine costs therefore sum to \[ \sum_{i=1}^d\frac{T}{t_i} O(t_i p^{3/2+\delta}\alpha) =O(dTp^{3/2+\delta}\alpha). \] Dividing by $V=Tp$ gives the fifth row. The factor $\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$.
- S6.3.5: Dividing by $V=Tp$ gives the fifth row, since $\alpha=\Theta(p^{1/4+\epsilon/2})$.
  Source: "$\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$." (paper)
  > For Gaussian resampling, axis $i$ has at most $T/t_i$ processed lines. The line-machine costs therefore sum to \[ \sum_{i=1}^d\frac{T}{t_i} O(t_i p^{3/2+\delta}\alpha) =O(dTp^{3/2+\delta}\alpha). \] Dividing by $V=Tp$ gives the fifth row. The factor $\alpha=\Theta(p^{1/4+\epsilon/2})$ explains its displayed power of $p$.
- S6.3.6: Chirp numerators are computed with the established multiplier in $O(dp^{1+\delta})$ per entry.
  Source: "then generating the exponentials, costs $O(dp^{1+\delta})$ per entry." (paper)
  > Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as sums of $d$ terms $s_i j_i^2(r/t_i)$. Computing their squares and products with the previously established $O(N\log(2N))$ multiplier on $N$-bit inputs, then generating the exponentials, costs $O(dp^{1+\delta})$ per entry. The smaller twist and scalar pointwise-product costs fit the same row: they use a fixed number of exact products on $O(p)$-bit component numerators, followed by linear truncation scans. The two final products by $S$ also cost $O(p\log p)$ per entry, so their normalized cost is $O(\log p)=O(p^\delta)$ as listed separately. There are $T/r$ polynomial records in each pointwise ring product. Four integer products on $O(rp)$ bits per record therefore cost $O(Tp\log(rp))$ in total. Signed packing, centered extraction, negacyclic wrapping, and copying are linear stream passes. These calls use the previously established multiplier on records of length $O(rp)=o(n)$; they do not call the improved algorithm being constructed. The exact source scaling by $2^\gamma$ is a shift of $O(p)$-bit numerators by $\gamma=O(p)$ places, so it is a linear scan per entry and fits the final-scaling row. The scalar-format adapters and the exact removal of sign-extension bits after the ring and source scales also use linear scans of their $O(p)$-bit components, within the listed scan costs.
- S6.3.7: There are $T/r$ polynomial records in each pointwise ring product; four integer products on $O(rp)$ bits per record cost $O(Tp\log(rp))$ in total, and these calls use the established multiplier on records of length $O(rp)=o(n)$.
  Source: "products on $O(rp)$ bits per record therefore cost" (paper)
  > Chirp numerators have $O(p)$ bits and can be computed modulo $2r$ as sums of $d$ terms $s_i j_i^2(r/t_i)$. Computing their squares and products with the previously established $O(N\log(2N))$ multiplier on $N$-bit inputs, then generating the exponentials, costs $O(dp^{1+\delta})$ per entry. The smaller twist and scalar pointwise-product costs fit the same row: they use a fixed number of exact products on $O(p)$-bit component numerators, followed by linear truncation scans. The two final products by $S$ also cost $O(p\log p)$ per entry, so their normalized cost is $O(\log p)=O(p^\delta)$ as listed separately. There are $T/r$ polynomial records in each pointwise ring product. Four integer products on $O(rp)$ bits per record therefore cost $O(Tp\log(rp))$ in total. Signed packing, centered extraction, negacyclic wrapping, and copying are linear stream passes. These calls use the previously established multiplier on records of length $O(rp)=o(n)$; they do not call the improved algorithm being constructed. The exact source scaling by $2^\gamma$ is a shift of $O(p)$-bit numerators by $\gamma=O(p)$ places, so it is a linear scan per entry and fits the final-scaling row. The scalar-format adapters and the exact removal of sign-extension bits after the ring and source scales also use linear scans of their $O(p)$-bit components, within the listed scan costs.

**S6.4**: Setup at recursion nodes, exceptional-address repair, global setup and prime search together cost $o(V)$.
How: Separate per-visit setup from per-record work: the recursions have constant branching and depth $O(\log p)$ with polynomially many visits ($\le p^A$ visits each of cost $p^C$), per-record or per-line polynomial work is $o(Tp)$ because $r$ exceeds every power of $p$, and exceptional streams are a fraction $O(d2^{-K})$ of the volume.
- S6.4.1: Total setup over at most $p^A$ visits each costing $p^C$ is at most $p^{A+C}=o(Tp)$.
  Source: "costs at most $p^{A+C}=o(Tp)$." (paper)
  > \paragraph{Setup and exceptional streams across all calls.} We next separate setup at recursion nodes from work repeated for every polynomial record or every Gaussian line. Here a visit means a node of the layer or address-layout recursions, or one of their round and group invocations. The internal recursion of the established integer multiplier and the iterations of the quoted Gaussian algorithms are already included in their separately charged running times. The layer and address-layout recursions have constant branching and depth $O(\log p)$, and the number of their rounds and base-$m$ groups is polynomial in $p$. Choose a fixed exponent $A$ so that their total number of visits is at most $p^A$, and a fixed $C$ bounding descriptor setup performed once per visit by $p^C$ steps. This setup then costs at most $p^{A+C}=o(Tp)$.
- S6.4.2: The compact exceptional stream of a packed change of basis has length $O\left(\frac{V_{\rm call}}{rp}d2^{-K}(rp+p)\right)=O(V_{\rm call}d2^{-K})$.
  Source: "O\!\left(\frac{V_{\rm call}}{rp}\,d2^{-K}(rp+p)\right)" (paper)
  > For one packed change of basis, let $V_{\rm call}$ be its current logical volume. The bad-address fraction is $O(d2^{-K})$, independently of the payload. Each polynomial record has $\Theta(rp)$ payload bits, and an exceptional record adds an $O(p)$-bit destination key. Thus the compact exceptional stream has length \[ O\!\left(\frac{V_{\rm call}}{rp}\,d2^{-K}(rp+p)\right) =O(V_{\rm call}d2^{-K}). \] Stable bit sorting makes $O(p)$ scans of this stream, for one-call cost $O(V_{\rm call}dp2^{-K})$. Extraction and reinsertion use a constant number of scans of the full current volume; those scans are already in the node overhead. Since there are at most $p^A$ visits, each of volume $O(V)$, the compact sorting costs sum to at most \[ O\!\left(dp2^{-K}\sum_{\rm calls}V_{\rm call}\right) =O(Vp^{A'}2^{-K})=o(V) \] for another fixed exponent $A'$. Here $d=O(p^\epsilon)$ and $K=\Theta(p^{\epsilon c})$ with $\epsilon c>0$. Predicate and key arithmetic is the polynomial work per record counted above. This is a deterministic worst-case bound.
- S6.4.3: Stable bit sorting makes $O(p)$ scans of it; summed over the visits the compact sorting costs $O(Vp^{A'}2^{-K})=o(V)$ since $K=\Theta(p^{\epsilon c})$ with $\epsilon c>0$ (a deterministic worst-case bound).
  Source: "=O(Vp^{A'}2^{-K})=o(V)" (paper)
  > For one packed change of basis, let $V_{\rm call}$ be its current logical volume. The bad-address fraction is $O(d2^{-K})$, independently of the payload. Each polynomial record has $\Theta(rp)$ payload bits, and an exceptional record adds an $O(p)$-bit destination key. Thus the compact exceptional stream has length \[ O\!\left(\frac{V_{\rm call}}{rp}\,d2^{-K}(rp+p)\right) =O(V_{\rm call}d2^{-K}). \] Stable bit sorting makes $O(p)$ scans of this stream, for one-call cost $O(V_{\rm call}dp2^{-K})$. Extraction and reinsertion use a constant number of scans of the full current volume; those scans are already in the node overhead. Since there are at most $p^A$ visits, each of volume $O(V)$, the compact sorting costs sum to at most \[ O\!\left(dp2^{-K}\sum_{\rm calls}V_{\rm call}\right) =O(Vp^{A'}2^{-K})=o(V) \] for another fixed exponent $A'$. Here $d=O(p^\epsilon)$ and $K=\Theta(p^{\epsilon c})$ with $\epsilon c>0$. Predicate and key arithmetic is the polynomial work per record counted above. This is a deterministic worst-case bound.

**S6.5**: Each of the seven displayed powers is at most $1-2\kappa$, any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$, and with schoolbook multiplication below a fixed cutoff the single machine runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.
How: Combine the margin bound $\min g_i=2\kappa$ with the absorption of logarithmic factors into one margin $\kappa$, and absorb finitely many small lengths into the constant.
- S6.5.1: Each of the seven displayed powers is at most $1-2\kappa$ by the margin list.
  Source: "Each of the seven displayed powers is at most $1-2\kappa$ by" (paper)
  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}
- S6.5.2: Any fixed power of $\log p$ is at most $p^\kappa$ eventually.
  Source: "\eqref{eq:margin-list}.  Any fixed power of $\log p$ is at most $p^\kappa$" (paper)
  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}
- S6.5.3: The complete large-input bound is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.
  Source: "O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})." (paper)
  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}
- S6.5.4: Beyond one cutoff past all size, precision, margin and layout conditions use schoolbook multiplication; the finitely many smaller lengths are included by enlarging the implicit constant.
  Source: "many smaller lengths are included by enlarging the implicit constant." (paper)
  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Parameter and prime-length choice](parameter-choice.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](chirp.md)
- [Signed packing](signed-packing.md)

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
- $x$ (source chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The address chunk whose selected bits are XORed into y.
- $y$ (target chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The address chunk that receives the XORs (not the ring variable).
- $z$ (scratch chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): The third address chunk, used as scratch and restored.
- $d$ (chunk count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of address chunks the butterfly layer acts on.
- $R$ (record bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in a record (not the scalar ring).
- $L$ (chunk bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in an address chunk, L=fK.
- $K$ (segment length), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits in a segment, and the spacing of selected positions.
- $f$ (selected bits), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of selected bit positions in a chunk.
- $\rho$ (offset), bound on [Packed selected-bit addition](packed-bit-addition.md): The position of the lowest selected bit, 0 <= rho < K.
- $j_i$ (selected position), bound on [Packed selected-bit addition](packed-bit-addition.md): The position j_i = rho + iK of the i-th selected bit.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of addresses.
- $V$ (volume), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of bits stored, MR.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): The bit length of counters, ceil(log2(2V)).
- $c$ (control), bound on [Packed selected-bit addition](packed-bit-addition.md): A Boolean control.
- $u$ (first integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The integer on which the parity-conditioned additions act first (a segment of y).
- $w$ (second integer), bound on [Packed selected-bit addition](packed-bit-addition.md): The auxiliary integer to be restored (a segment of z).
- $g_i$ (guard of y), bound on [Packed selected-bit addition](packed-bit-addition.md): The segment value of y divided by two, rounded down.
- $h_i$ (guard of z), bound on [Packed selected-bit addition](packed-bit-addition.md): The segment value of z divided by two, rounded down.
- $a_i$ (low bit of y), bound on [Packed selected-bit addition](packed-bit-addition.md): The lowest bit of the i-th segment of y.
- $b_i$ (low bit of z), bound on [Packed selected-bit addition](packed-bit-addition.md): The lowest bit of the i-th segment of z.
- $c_i$ (segment control), bound on [Packed selected-bit addition](packed-bit-addition.md): The selected bit of x at j_i, controlling the i-th segment pair.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): The composition of the eight packed cyclic shifts.
- $\mathcal B$ (exceptional set), bound on [Packed selected-bit addition](packed-bit-addition.md): The addresses where some guard of y or z lies outside [10, 2^{K-1}-11].
- $T_0$ (ideal map), bound on [Packed selected-bit addition](packed-bit-addition.md): The permutation that performs the required XORs at j_0..j_{f-2}.
- $\delta_{\rm bad}$ (bad fraction), bound on [Packed selected-bit addition](packed-bit-addition.md): The bound min{1, 80(f-1)2^{-K}} on the fraction of exceptional addresses.
- $\tau$ (swap exponent), bound on [Packed selected-bit addition](packed-bit-addition.md): The fixed exponent below 1 in the chunk interchange cost.
- $p$ (precision), bound on [Packed selected-bit addition](packed-bit-addition.md): The number of precision bits of the records.
- $D$ (selected chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of address chunks carrying a selected bit.
- $d$ (chunk bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An upper bound on the number of chunks a layer acts on.
- $z$ (record array), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The array of records, a function of the address x.
- $x$ (address), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An address of the array, with selected bits x_1,...,x_D.
- $\mathcal S_D$ (phase diagonal), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The diagonal operator multiplying the record at address x by i^{x_1+...+x_D}.
- $e$ (group axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of axes in a group, e = mf.
- $h$ (slot index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): Index of a slot, and of the residual basis vector placed on it.
- $v_h$ (residual vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A vector of a basis of the edge's residual space, in F_2^m.
- $\eta_h$ (edge sign), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sign +1 or -1 of the kernel exponent attached to residual vector v_h.
- $C_v$ (shifted kernel), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The matrix aI+bX_v, the kernel C applied along the column direction v.
- $X_v$ (column shift), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The operator shifting the address of a column by v.
- $G$ (basis matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): An invertible binary m by m matrix whose first columns are the residual vectors v_h.
- $\mathcal P_G$ (basis permutation), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The address permutation moving a column value x to Gx.
- $e_h$ (standard basis vector), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The h-th standard basis vector of F_2^m.
- $Z$ (sign matrix), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The diagonal matrix diag(1,-1).
- $q$ (row quotient), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The quotient of a row index on division by W.
- $w$ (row remainder), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The remainder of a row index modulo W, which is the wire role.
- $q_0$ (row chunk count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of leading chunks whose bits form the row index.
- $\gamma$ (step ratio), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The ratio s/W, at most m^sigma.
- $j$ (level index), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The index of a recursion level, counted from 0.
- $u$ (leaf chunks), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of active chunks in a leaf at level j, e/m^j.
- $a_j$ (piece digit), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The base-m digit of D-q_0 at position j, the number of pieces of m^j chunks.
- $A$ (chain bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A(e) bounds the number of arithmetic operations on a chain from an input to an intermediate coefficient in a group of e axes.
- $E$ (invocation bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The bound 64(W+m+1)^3 on operations added on a chain by one network invocation.
- $\xi$ (bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): Any bound of at least 1 on the chain operation count.
- $B$ (recurrence base), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The sum s+E.
- $\nu$ (depth exponent), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The least j at least 1 with m^j at least B.
- $C_0$ (guard constant), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The constant 128mB^2 in the guard width.
- $\ell$ (chain depth), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of operations along a chain, the depth of a value.
- $\epsilon$ (axis exponent), bound on [Simultaneous butterfly layer](simultaneous-layer.md): A fixed exponent with d = Theta(p^epsilon).
- $D$ (transformed axes), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of transformed axes, d-1.
- $K$ (chunk width), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of bits in an address chunk.
- $\tau$ (interchange exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the cost of the chunk interchange.
- $\lambda'$ (layer exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the cost of the simultaneous layer.
- $\ell$ (long-axis address bits), bound on [Tape layout for synthetic transforms](transform-layout.md): The base-2 logarithm of r, the number of address bits of a long axis.
- $\boldsymbol t$ (axis lengths), bound on [Tape layout for synthetic transforms](transform-layout.md): The tuple (t_1,...,t_D) of the axis lengths.
- $F_{\boldsymbol t}^-$ (forward synthetic transform), bound on [Tape layout for synthetic transforms](transform-layout.md): The forward synthetic transform along all D axes, axis i having length t_i.
- $F_{\boldsymbol t}^+$ (opposite transform), bound on [Tape layout for synthetic transforms](transform-layout.md): The opposite of the forward synthetic transform along all D axes.
- $B$ (bit reversal), bound on [Tape layout for synthetic transforms](transform-layout.md): The bit-reversal permutation applied along every axis.
- $b$ (leftover low bits), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of low address bits of an axis left over after whole K-bit chunks.
- $q$ (whole chunks), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of whole K-bit chunks per axis.
- $L$ (layout permutation), bound on [Tape layout for synthetic transforms](transform-layout.md): The record permutation made by the prefix moves and chunk exchanges.
- $z$ (round input), bound on [Tape layout for synthetic transforms](transform-layout.md): The array entering a round.
- $M$ (number of records), bound on [Convolution from the retained transform layout](ring-convolution.md): The number of polynomial records, one per cyclic address of the remaining axes.
- $T$ (number of coefficients), bound on [Convolution from the retained transform layout](ring-convolution.md): The number of complex coefficients in an array, T = rM.
- $F^-$ (forward transform), bound on [Convolution from the retained transform layout](ring-convolution.md): The forward synthetic transform.
- $F^+$ (opposite transform), bound on [Convolution from the retained transform layout](ring-convolution.md): The opposite synthetic transform.
- $P$ (pointwise product), bound on [Convolution from the retained transform layout](ring-convolution.md): The pointwise product of records, P(u,v) = uv/r.
- $L$ (layout permutation), bound on [Convolution from the retained transform layout](ring-convolution.md): The permutation of records produced by the tape layout.
- $B$ (bit-reversal order), bound on [Convolution from the retained transform layout](ring-convolution.md): The bit-reversal order in which forward outputs are written.
- $\mathcal T_+$ (opposite map), bound on [Convolution from the retained transform layout](ring-convolution.md): The exact counterpart F^+ B^{-1} L^{-1} of the opposite procedure.
- $\ell$ (log of record length), bound on [Convolution from the retained transform layout](ring-convolution.md): The base-2 logarithm of the record length r.
- $\delta$ (transform error), bound on [Convolution from the retained transform layout](ring-convolution.md): The error bound sqrt2 * l * 2^{-p} of each forward or opposite procedure.
- $\eta$ (truncation error), bound on [Convolution from the retained transform layout](ring-convolution.md): The error bound sqrt2 * 2^{-p} for one truncation.
- $K$ (layout chunk width), bound on [Convolution from the retained transform layout](ring-convolution.md): The width of the address chunks used by the tape layout.
- $b$ (digit width), bound on [The multiplication algorithm](multiplication-algorithm.md): The number of bits in one radix digit, the ceiling of log2 n.
- $t_i$ (padded axis length), bound on [The multiplication algorithm](multiplication-algorithm.md): The power-of-two length of axis i; their product is T.
- $F_{\boldsymbol s}$ (prime-axis transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The discrete Fourier transform on the axes s_i, normalized by 1/S.
- $F_{\boldsymbol t}$ (padded-axis transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The discrete Fourier transform on the axes t_i, normalized by 1/T.
- $\mathcal M_{\mathbb C}$ (normalized convolution), bound on [The multiplication algorithm](multiplication-algorithm.md): The normalized cyclic convolution f*g/T.
- $a_{\boldsymbol j}$ (chirp), bound on [The multiplication algorithm](multiplication-algorithm.md): The chirp array, a quadratic phase in the index.
- $\widetilde a$ (computed chirp), bound on [The multiplication algorithm](multiplication-algorithm.md): The stored approximation of the chirp a.
- $x_0$ (data operand), bound on [The multiplication algorithm](multiplication-algorithm.md): The data operand after the first chirp phase.
- $y_0$ (computed convolution), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed convolution of the chirp with the data operand.
- $\widetilde{\mathcal M}_{\mathbb C}$ (computed convolution map), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed approximate version of the normalized cyclic convolution.
- $\widetilde{\mathscr C}$ (computed chirp transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed chirp transform.
- $\widetilde{\mathscr F}$ (computed source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed source transform: resample, chirp transform, resample, scale.
- $\mathcal A$ (input resampling map), bound on [The multiplication algorithm](multiplication-algorithm.md): The Gaussian resampling map applied first in the source transform.
- $\mathcal B_0$ (output resampling map), bound on [The multiplication algorithm](multiplication-algorithm.md): The resampling map applied after the chirp transform.
- $\gamma$ (resampling scale exponent), bound on [The multiplication algorithm](multiplication-algorithm.md): The exponent of the exact scale 2^gamma applied at the end of the source transform.
- $\mathscr F$ (exact source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The exact counterpart of the computed source transform.
- $R$ (retained permutation), bound on [The multiplication algorithm](multiplication-algorithm.md): The retained coordinate permutation of the source axes.
- $z$ (pointwise product array), bound on [The multiplication algorithm](multiplication-algorithm.md): An array to which the opposite-sign source transform is applied.
- $\widetilde{\mathscr F}^{+}$ (opposite-sign source transform), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed source transform with the opposite sign, conjugating input and output.
- $\widetilde w$ (scaled computed array), bound on [The multiplication algorithm](multiplication-algorithm.md): The computed array after the first scaling by S.
- $w$ (scaled exact array), bound on [The multiplication algorithm](multiplication-algorithm.md): The exact array (u*v)/S that the computed array approximates.
- $u$ (first source array), bound on [The multiplication algorithm](multiplication-algorithm.md): In this page, the first source array obtained by applying Phi to the digits, not the integer.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.
  Shown as: Cost accounting and the exponent κ *<predicate>* The multiplication algorithm
- [Fast address-chunk interchange](address-interchange.md): The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
  Shown as: Cost accounting and the exponent κ *<predicate>* Fast address-chunk interchange
- [Simultaneous butterfly layer](simultaneous-layer.md): The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.
  Shown as: Cost accounting and the exponent κ *<predicate>* Simultaneous butterfly layer
- [Packed selected-bit addition](packed-bit-addition.md): XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.
  Shown as: Cost accounting and the exponent κ *<predicate>* Packed selected-bit addition

## Pages that build on this one

- Power-saving integer multiplication: A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

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
- [Controlled shifts and rational scalings](controlled-shifts.md)
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
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "Thus $\min_i g_i=2^{-181}=2\kappa$." (paper)

  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.

- "The complete time bound" (paper)

  > \subsection{The complete time bound}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The recursions have constant branching and depth $O(\log p)$" (The page never says which recursions are meant (the paper, around line 4920, means the butterfly-layer and address-layout recursions), what a visit is, or what setup is performed per visit. The reader cannot check that the number of visits is at most p^A with setup p^C, nor that the per-record and per-line setup (the paper's O(T p^{A+C}/r) and O(d T p^C / r) terms, lines 4927-4937) is also o(Tp).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "repaired by sorting a compact stream" (The page states the repair cost O(V p^{O(1)} 2^{-K}) but not why: the paper (lines 4951-4973) shows the compact exceptional stream has length O(V_call d 2^{-K}), is sorted with O(p) scans, and is summed over at most p^A visits. The reader is not told these facts, so cannot check the p^{O(1)} factor.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.

## Previous version (revise it)

It has 436 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 545 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Cost accounting totals the running time of every step of [The multiplication algorithm](multiplication-algorithm.md) and shows that it is $O(n(\lg n)^{1-\kappa})$, where $\kappa=2^{-182}$ is the saved exponent.

Let $V=Tp=\Theta(n)$ be the volume of $T$ coefficients of $p$ bits. Here $d$ is the number of axes, $K$ the chunk width, $\ell$ the address bits per axis, $\alpha$ the Gaussian width and $t_i$ the length of axis $i$. The fixed exponents of [Parameter and prime-length choice](parameter-choice.md) are $\epsilon=2^{-75}$, $c=2^{-56}$, $\delta=1/16$, $\tau=1-2^{-50}$ and $\lambda'=1-2^{-54}$, giving $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $\alpha=\Theta(p^{1/4+\epsilon/2})$.

Dividing by $V$, seven operations dominate. Each is a power $p^{1-g_i}$, where $g_i>0$ is its margin below one.

| Operation | Cost$/V$ | Power of $p$ | Margin |
|---|---|---|---|
| Prefix moves | $dK$ | $\epsilon(1+c)$ | $g_1=1-\epsilon(1+c)$ |
| Chunk exchanges | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ | $g_2=\epsilon c(1-\tau)$ |
| Layer rounds | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ | $g_3=\epsilon(1-\lambda')$ |
| Axis layouts | $d^2(1+\ell^\tau)$ | $\tau+\epsilon(2-\tau)$ | $g_4=1-\tau-\epsilon(2-\tau)$ |
| Gaussian lines | $dp^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ | $g_5=1/4-\delta-3\epsilon/2$ |
| Chirps | $dp^\delta$ | $\epsilon+\delta$ | $g_6=1-\delta-\epsilon$ |
| Products | $\log(rp)$ | $1-\epsilon$ | $g_7=\epsilon$ |

- Prefix moves and single butterfly rounds are $O(dK)$ linear scans, each costing $O(V)$, in [Tape layout for synthetic transforms](transform-layout.md).
- The layout needs $O(p/K)$ chunk exchanges, as $d\ell=O(p)$, each costing $O(VK^\tau)$ by [Fast address-chunk interchange](address-interchange.md). The total is $O(p/K)K^\tau=O(pK^{\tau-1})$.
- Each of at most $\ell$ rounds costs $O(Vd^{\lambda'})$ by [Simultaneous butterfly layer](simultaneous-layer.md).
- The [Chinese-remainder address map](crt-map.md) needs $O(d^2)$ adjacent axis moves. Each move peels one excess bit, exchanges the equal-width parts at cost $O(V\ell^\tau)$ and restores it, so it costs $O(V(1+\ell^\tau))$ <cite data-source="paper">Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths</cite>. Here $d^2\ell^\tau=p^{2\epsilon}p^{(1-\epsilon)\tau}$.
- In [Gaussian resampling](gaussian-resampling.md), axis $i$ has at most $T/t_i$ lines of cost $O(t_ip^{3/2+\delta}\alpha)$ each, totalling $O(dTp^{3/2+\delta}\alpha)$.
- A chirp numerator of the [Bluestein chirp identity](chirp.md) has $O(p)$ bits and sums $d$ terms. The [Established O(n log n) multiplier](hvdh-multiplier.md), at cost $O(N\log 2N)$ on $N$ bits, computes their squares and products in $O(dp^{1+\delta})$ per entry, so $dp^\delta$ per bit.
- The $T/r$ ring-product records each need four products on $O(rp)$ bits after [Signed packing](signed-packing.md), by the established multiplier at length $o(n)$. The total is $O(Tp\log(rp))$ and $\log(rp)=O(p^{1-\epsilon})$.

Substitution gives $g_1>1/2$, $g_2=2^{-75}2^{-56}2^{-50}=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$, so the smallest margin is $2^{-181}=2\kappa$ <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite>

The recursions have constant branching and depth $O(\log p)$, so fix exponents $A$ and $C$ with at most $p^A$ visits, each with setup of at most $p^C$ steps. The total is $o(Tp)$ <cite data-source="paper">costs at most $p^{A+C}=o(Tp)$.</cite> because $T\ge r$ and $r$ exceeds every fixed power of $p$. Exceptional addresses, where the packed shifts of [Packed selected-bit addition](packed-bit-addition.md) fail, are a fraction $O(d2^{-K})$ of addresses, repaired by sorting a compact stream, cost $O(Vp^{O(1)}2^{-K})=o(V)$, since $K=\Theta(p^{\epsilon c})$ beats any power of $p$.

Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually. The total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ <cite data-source="paper">O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).</cite> Schoolbook multiplication below a fixed cutoff is absorbed <cite data-source="paper">many smaller lengths are included by enlarging the implicit constant.</cite> One machine thus runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

The exponent is only $2^{-182}$ below one because $g_2$ multiplies three small numbers: $\epsilon$ (few axes), $c$ (narrow chunks) and $1-\tau$ (an exchange saves only $K^{-(1-\tau)}$).

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

Write the body to `exegenius/tasks/0177-write-cost-accounting.answer.md` and the JSON to `exegenius/tasks/0177-write-cost-accounting.answer.json`, then run `exegenius submit 0177-write-cost-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0177-write-cost-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
