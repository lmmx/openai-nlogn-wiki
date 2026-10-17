# exegenius task 0115-write-cost-accounting

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
- Fast address-chunk interchange (also: chunk swap, tape interchange)
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

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials, satisfying y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm in the running time is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations applied since the layer began.
- $\Delta$ (extra reserved bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the number of operations charged to the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set $[h]$ whose three-element subsets index the banks.
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of $[h]$.
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.
- $R$ (scalar ring), bound on [Frames on wire arrays](array-frames.md): The ring of scalars carried by the wires.
- $\Omega$ (address set), bound on [Frames on wire arrays](array-frames.md): A finite set of addresses indexing every wire's array.
- $\mathsf S_\Omega$ (pointwise network), bound on [Frames on wire arrays](array-frames.md): The network obtained by applying every scalar gate pointwise at each address, acting on all wire arrays together.
- $D_v$ (frame), bound on [Frames on wire arrays](array-frames.md): An invertible R-linear operator on R^Omega assigned to a source, gate or sink v.
- $D_{\rm in}$ (input frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the source frames over the input roles.
- $D_{\rm out}$ (output frame), bound on [Frames on wire arrays](array-frames.md): The direct sum of the sink frames over the output roles.
- $\rho$ (role permutation), bound on [Frames on wire arrays](array-frames.md): The map sending each input role to its output role in a signed role permutation.
- $\varepsilon_w$ (route sign), bound on [Frames on wire arrays](array-frames.md): The scalar sign of the route from input role w.
- $q$ (sequence length), bound on [Cyclic convolution](convolution.md): The number of entries in each of the two sequences being convolved.
- $t_i$ (axis length), bound on [Cyclic convolution](convolution.md): The length of axis i of the array.
- $M$ (cyclic addresses), bound on [Cyclic convolution](convolution.md): The number of cyclic addresses on the first d-1 axes, the product of t_i for i<d.
- $T$ (total coefficients), bound on [Cyclic convolution](convolution.md): The total number of complex coefficients in an array, rM.
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
- $x_d$ (last-axis variable), bound on [Phase twist](phase-twist.md): The variable of the last cyclic axis, with x_d^r = 1.
- $\zeta$ (twist phase), bound on [Phase twist](phase-twist.md): The number e^{\pi i/r}, a primitive 2r-th root of unity with \zeta^r = -1.
- $\Theta$ (twist map), bound on [Phase twist](phase-twist.md): The ring isomorphism from C[x_d]/(x_d^r-1) to the negacyclic ring sending x_d to \zeta y.
- $d$ (number of axes), bound on [Phase twist](phase-twist.md): The number of axes of the array f.
- $T$ (total entries), bound on [Phase twist](phase-twist.md): The number of entries of the array f in all.
- $M$ (number of records), bound on [Phase twist](phase-twist.md): The number of lines along the last axis, T/r.
- $\iota$ (record identification), bound on [Phase twist](phase-twist.md): Reads each line along the last axis as a polynomial in the negacyclic ring.
- $D_\pm$ (diagonal twist), bound on [Phase twist](phase-twist.md): Multiplies entry k of each line by \zeta^{\pm k}.
- $\mathcal M_r$ (ring convolution), bound on [Phase twist](phase-twist.md): The ring convolution that convolves the first d-1 axes over the negacyclic ring and includes the division by T.
- $\mathcal M_{\mathbb C}$ (normalized cyclic convolution), bound on [Phase twist](phase-twist.md): The composite D_-\iota^{-1}\mathcal M_r(\iota D_+ f,\iota D_+ g), equal to f*g/T.
- $q$ (sequence length), bound on [Discrete Fourier transform](dft.md): The number of complex entries in the sequences the transform acts on.
- $u$ (input sequence), bound on [Discrete Fourier transform](dft.md): A sequence of q complex numbers to which the transform is applied.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](dft.md): The primitive q-th root of unity e^{2 pi i/q} whose powers are the transform weights.
- $t$ (transform length), bound on [Butterflies and the fast transform](butterfly.md): The number of values in the transform, a power of two.
- $z_k$ (input values), bound on [Butterflies and the fast transform](butterfly.md): The input value at position k, for 0 <= k < t.
- $k$ (input position), bound on [Butterflies and the fast transform](butterfly.md): The position of an input value, 0 <= k < t.
- $\omega_t$ (root of unity), bound on [Butterflies and the fast transform](butterfly.md): The primitive t-th root of unity e^{2 pi i/t}.
- $b$ (lowest output bit), bound on [Butterflies and the fast transform](butterfly.md): The lowest bit of the output index, 0 or 1.
- $h$ (remaining output index), bound on [Butterflies and the fast transform](butterfly.md): The output index with its lowest bit removed.
- $t$ (transform length), bound on [Synthetic polynomial transform](synthetic-transform.md): The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $\omega_t$ (ring root of unity), bound on [Synthetic polynomial transform](synthetic-transform.md): The power y^{2r/t} of the ring variable, used as the root of unity of the length-t synthetic transform.
- $V$ (array volume), bound on [Elementary stream operations](stream-ops.md): The number of radix-q digits stored in the array.
- $q$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (number of streams), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which whole rows are dealt cyclically.
- $d$ (number of axes), bound on [Bluestein chirp identity](chirp.md): The number of axes (coordinates) of an index.
- $t_i$ (axis length), bound on [Bluestein chirp identity](chirp.md): The even number of entries along axis i.
- $s_i$ (coprime integer), bound on [Bluestein chirp identity](chirp.md): An integer coprime to t_i, scaling the frequency read along axis i.
- $T$ (total entries), bound on [Bluestein chirp identity](chirp.md): The total number of entries, the product of the t_i.
- $Q$ (target permutation), bound on [Bluestein chirp identity](chirp.md): The target permutation, reading frequency (-s_i j_i)_i at output position j.
- $a$ (chirp), bound on [Bluestein chirp identity](chirp.md): The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i).
- $t$ (transform length), bound on [Retained frequency order](frequency-order.md): The number of ring elements transformed along one axis, a power of two dividing 2r.
- $a$ (number of rounds), bound on [Retained frequency order](frequency-order.md): The number log_2 t of rounds of the fast algorithm.
- $\omega_t$ (root of unity), bound on [Retained frequency order](frequency-order.md): The power y^{2r/t} of the ring variable used as the t-th root of unity.
- $H_0$ (two-point butterfly), bound on [Retained frequency order](frequency-order.md): The 2x2 matrix (1/2)[[1,1],[1,-1]] applied to each pair of entries.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation of records moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The butterfly layer applying H_0 on every participating axis at once.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The operation multiplying the record at each address by y^E.
- $u_i$ (current length), bound on [Retained frequency order](frequency-order.md): The current recursive length of axis i.
- $b_i$ (branch bit), bound on [Retained frequency order](frequency-order.md): The newly written branch bit of axis i.
- $k_i$ (encoded index), bound on [Retained frequency order](frequency-order.md): The index encoded by the still unprocessed slots of axis i.
- $N$ (bit length), bound on [Established O(n log n) multiplier](hvdh-multiplier.md): The number of bits in each of the two integers being multiplied.
- $p$ (precision bits), bound on [Signed packing](signed-packing.md): The number of fractional bits in each coefficient component.
- $B_0$ (packing base), bound on [Signed packing](signed-packing.md): The power of two $2^{4p}$ at which the polynomials are evaluated.
- $A_u$ (evaluation integer), bound on [Signed packing](signed-packing.md): The signed integer obtained by evaluating the polynomial u at B_0.
- $H_j$ (numerator coefficient), bound on [Signed packing](signed-packing.md): The Gaussian integer coefficient of y^j after reduction modulo y^r+1.
- $q$ (prime), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The prime base of the field arithmetic.
- $b$ (field digits), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-$q$ digits of a field.
- $Q$ (field size), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can hold, Q = q^b.
- $V$ (array volume), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of stored data bits in the array.
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of bits following the target field.
- $c$ (scaling integer), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the target is multiplied.
- $A$ (shear matrix), bound on [Matrix shear by triangular factorization](matrix-shear.md): The fixed rational m by m matrix whose action AD is added to H.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $H$ (H group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields H_1..H_m that receives the update.
- $D$ (D group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The ordered group of m fields D_1..D_m that is added into H.
- $q$ (base prime), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime; fields are residues modulo q^b.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in a field.
- $V$ (data volume), bound on [Matrix shear by triangular factorization](matrix-shear.md): The volume of data being processed.
- $E_1$ (left factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $E_2$ (right factor), bound on [Matrix shear by triangular factorization](matrix-shear.md): An invertible lower triangular factor of A.
- $\Pi$ (partial permutation), bound on [Matrix shear by triangular factorization](matrix-shear.md): A matrix with exactly a ones, at most one per row and column, and zeros elsewhere.
- $i$ (row index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The row of a one of Pi.
- $j$ (column index), bound on [Matrix shear by triangular factorization](matrix-shear.md): The column of a one of Pi.
- $h$ (value of H_i), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field H_i.
- $d$ (value of D_j), bound on [Matrix shear by triangular factorization](matrix-shear.md): The initial value of the field D_j.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2x2 matrix that swaps the two entries of a pair.
- $a$ (kernel coefficient a), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2, the coefficient of I in C.
- $b$ (kernel coefficient b), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1-i)/2, the coefficient of X in C.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The matrix aI + bX, a square root of the bit flip.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1, i) that multiplies the second entry of a pair by i.
- $H_0$ (butterfly matrix), bound on [Two-point kernel C](phase-kernel.md): The matrix of the averaging and differencing step (u,v) -> ((u+v)/2, (u-v)/2).
- $d$ (number of axes), bound on [Multidimensional transforms](multidim-transform.md): The number of axes (coordinates) of the array.
- $q_i$ (axis length), bound on [Multidimensional transforms](multidim-transform.md): The number of positions along axis i.
- $N$ (number of entries), bound on [Multidimensional transforms](multidim-transform.md): The number of entries of the array, the product of the axis lengths.
- $S$ (convolution length), bound on [Chinese-remainder address map](crt-map.md): The length of the cyclic convolution, the product of the axis lengths.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i; the lengths are pairwise coprime.
- $d$ (number of axes), bound on [Chinese-remainder address map](crt-map.md): The number of axes.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the lengths of axes before axis i.
- $\mu_i$ (axis exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The variable of axis i in the target ring.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The j-th mixed-radix digit of the index k.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of the image of x^k.
- $t_i$ (padded length), bound on [Chinese-remainder address map](crt-map.md): The padded length of axis i, a power of two at least s_i.
- $\ell$ (axis bit width), bound on [Chinese-remainder address map](crt-map.md): The number of bits of the widest axis.
- $T$ (padded array size), bound on [Chinese-remainder address map](crt-map.md): The number of records in the padded array.
- $p$ (record precision), bound on [Chinese-remainder address map](crt-map.md): The number of bits of precision per record.
- $\tau$ (chunk-swap exponent), bound on [Chinese-remainder address map](crt-map.md): The fixed exponent in (0,1) governing the cost of a chunk interchange.
- $s$ (prime length), bound on [Gaussian resampling](gaussian-resampling.md): The prime length of the Fourier transform to be resampled, the number of complex coordinates it acts on.
- $t$ (power-of-two length), bound on [Gaussian resampling](gaussian-resampling.md): The power-of-two length of the nearby transform, the number of complex coordinates it acts on.
- $p$ (precision bits), bound on [Gaussian resampling](gaussian-resampling.md): The number of bits of precision of each real and imaginary component.
- $\alpha$ (Gaussian parameter), bound on [Gaussian resampling](gaussian-resampling.md): An integer with 2 <= alpha < sqrt p that sets the Gaussian width.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s - 1 between t and s, assumed larger than p/alpha^4.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): An index of a coordinate of a vector in C^t, taken modulo t.
- $d$ (number of axes), bound on [Retained permutation cancellation](retained-permutations.md): The number of coordinate axes.
- $s_i$ (prime length), bound on [Retained permutation cancellation](retained-permutations.md): The prime length of axis i.
- $t_i$ (power-of-two length), bound on [Retained permutation cancellation](retained-permutations.md): The power-of-two length of axis i.
- $S$ (product of prime lengths), bound on [Retained permutation cancellation](retained-permutations.md): The product of the prime lengths.
- $T$ (padded box size), bound on [Retained permutation cancellation](retained-permutations.md): The number of entries in the padded box, the product of the power-of-two lengths.
- $p$ (bit precision), bound on [Retained permutation cancellation](retained-permutations.md): The number of bits of precision of each coordinate.
- $\alpha$ (Gaussian width), bound on [Retained permutation cancellation](retained-permutations.md): An integer width parameter of the Gaussian weights.
- $\delta$ (time exponent), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent in the time bound.
- $R$ (source permutation), bound on [Retained permutation cancellation](retained-permutations.md): The source coordinate permutation, tensor product of the one-axis permutations P_{s_i}.
- $Q$ (target permutation), bound on [Retained permutation cancellation](retained-permutations.md): The target coordinate permutation, tensor product of the one-axis permutations P_{t_i}.
- $w$ (chunk width), bound on [Retained permutation cancellation](retained-permutations.md): The width in bits of the chunks swapped.
- $V$ (total bits), bound on [Retained permutation cancellation](retained-permutations.md): The total number of bits within which chunks are swapped.
- $\tau$ (chunk-swap exponent), bound on [Retained permutation cancellation](retained-permutations.md): The fixed exponent below 1 in the chunk-swap time bound.
- $b$ (digit width), bound on [Error tracking and exact recovery](precision-recovery.md): The number of bits in a radix digit.
- $p$ (fractional bits), bound on [Error tracking and exact recovery](precision-recovery.md): The number of fractional bits of the fixed-point grid, equal to $6b$.
- $T$ (padded array size), bound on [Error tracking and exact recovery](precision-recovery.md): The number of records in the padded array.
- $S$ (convolution length), bound on [Error tracking and exact recovery](precision-recovery.md): The length of the cyclic convolution.
- $L$ (log of T), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of $T$.
- $\gamma$ (source scale exponent), bound on [Error tracking and exact recovery](precision-recovery.md): The exponent of the source-transform scale $2^\gamma$.
- $d$ (axis count), bound on [Error tracking and exact recovery](precision-recovery.md): The number of transform axes.
- $h_p$ (grid step), bound on [Error tracking and exact recovery](precision-recovery.md): The grid step $2^{-p}$.
- $\ell$ (log of r), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the record length $r$.
- $M$ (ring record count), bound on [Error tracking and exact recovery](precision-recovery.md): The ratio $T/r$, the number of ring records.
- $q$ (digit count), bound on [Error tracking and exact recovery](precision-recovery.md): The number of radix digits of an $n$-bit input.
- $Q_0$ (radix), bound on [Error tracking and exact recovery](precision-recovery.md): The radix $2^b$ of the digits.
- $n$ (input bits), bound on [Parameter and prime-length choice](parameter-choice.md): The number of bits of each of the two input integers.
- $d$ (number of axes), bound on [Parameter and prime-length choice](parameter-choice.md): The number of axes of the padded box.
- $T$ (padded box size), bound on [Parameter and prime-length choice](parameter-choice.md): The number of positions of the padded box.
- $t_i$ (axis length), bound on [Parameter and prime-length choice](parameter-choice.md): The length of axis i of the padded box.
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed exponent setting the number of axes.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): Fixed exponent setting the chunk width.
- $\lambda'$ (layer cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The cost exponent of a butterfly layer.
- $\kappa$ (saving exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The saving exponent of the final running time.
- $\tau$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\sigma$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\beta$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\delta$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $\lambda$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $C_1$ (lemma constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed rational constant entering the lemmas inequalities.
- $b$ (bit length), bound on [Parameter and prime-length choice](parameter-choice.md): The bit length of n.
- $K$ (chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The address-chunk width in bits.
- $\ell$ (address bits), bound on [Parameter and prime-length choice](parameter-choice.md): The number of address bits of the longest axis.
- $p$ (precision), bound on [Parameter and prime-length choice](parameter-choice.md): The precision in bits, setting the 2^{-p} grid of the fixed-point records.
- $a_d$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $a_r$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $b_d$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $b_r$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $C_\ell$ (comparison constant), bound on [Parameter and prime-length choice](parameter-choice.md): A fixed constant with which the lemmas bound d, r and l.
- $\alpha$ (Gaussian width), bound on [Parameter and prime-length choice](parameter-choice.md): The width of the Gaussian weights in the resampling.
- $\gamma$ (total scaling), bound on [Parameter and prime-length choice](parameter-choice.md): The total scaling of the Gaussian weights over the axes.
- $\eta$ (relative gap), bound on [Parameter and prime-length choice](parameter-choice.md): The relative gap of each prime below its power of two.
- $x$ (interval scale), bound on [Parameter and prime-length choice](parameter-choice.md): A real number, the scale of the prime interval.
- $q$ (candidate), bound on [Parameter and prime-length choice](parameter-choice.md): An integer in the prime interval.
- $s_i$ (prime axis length), bound on [Parameter and prime-length choice](parameter-choice.md): The prime axis length of axis i near t_i.
- $S$ (convolution length), bound on [Parameter and prime-length choice](parameter-choice.md): The product of the s_i, the cyclic convolution length.
- $\theta_i$ (relative gap), bound on [Parameter and prime-length choice](parameter-choice.md): The relative gap t_i/s_i - 1 of axis i.
- $m$ (label-space dimension), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The dimension of the ambient label space, $m=h^3=10^6$.
- $W$ (wire count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of wires of the network under consideration.
- $s$ (number of smaller calls), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total number of smaller calls that the network's edges cost.
- $h$ (ground-set size), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The size of the ground set whose three-element subsets index the network, $h=100$.
- $F$ (one-factor label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $\mathbb Q^h$ (bit network) or $\mathbb F_2^h$ (complex network) with its bilinear form.
- $t_T$ (triple indicator), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The indicator vector in $F$ of a triple $T$.
- $\mathcal F$ (ambient label space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The space $F^{\otimes3}$ of $h\times h\times h$ arrays, of dimension $m$, in which all labels lie.
- $N$ (bank size), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of index tuples $a$ of triples, so the number of wires in each data bank.
- $U_a$ (terminal line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The total dimension lost on decreasing edges.
- $j$ (stage number), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The stage, 1, 2 or 3, whose invocations vary coordinate $a_j$.
- $A$ (exposed factor space), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The tensor product $F^{\otimes(j-1)}$ of the factors already exposed before stage $j$.
- $P$ (earlier tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $I$ (invocation count), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of invocations over all three stages.
- $\gamma$ (central wires per invocation), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The number of central wires in one invocation: 100 in the bit network, 101 in the complex one.
- $\Pi_U$ (projection onto a label), bound on [Nested subspace labels and rank deficit](subspace-labels.md): The rational projection onto the label $U$ along $U^\perp$, the matrix given to a bit-network vertex labelled $U$.
- $f$ (call parameter), bound on [Recursive power saving](rank-recurrence.md): The parameter of a call: the number of digits in each of the two interchanged chunks, or the number of axes the butterfly layer acts on.
- $V$ (volume), bound on [Recursive power saving](rank-recurrence.md): The volume of a call: the number of data symbols it processes.
- $m$ (block count), bound on [Recursive power saving](rank-recurrence.md): The number of size-f blocks into which a call at parameter mf cuts its parameter, equal to 10^6 (also the dimension of the label space).
- $W$ (wire count), bound on [Recursive power saving](rank-recurrence.md): The number of wires of the fixed network, and so the number of streams a call splits its data into.
- $s$ (number of smaller calls), bound on [Recursive power saving](rank-recurrence.md): The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (normalized cost), bound on [Recursive power saving](rank-recurrence.md): F(f) is the running time of a call at parameter f divided by its volume.
- $k$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of levels of recursion: the number of factors m in a parameter m^k.
- $\tau$ (saving exponent), bound on [Recursive power saving](rank-recurrence.md): A fixed exponent below 1 with s/W < m^tau, which makes a call cost O(V f^tau); here tau = 1 - 2^{-50}.
- $\eta$ (relative deficit), bound on [Recursive power saving](rank-recurrence.md): The fraction (Wm - s)/(Wm) by which the number of smaller calls s falls short of Wm.
- $u$ (chunk width), bound on [Fast address-chunk interchange](address-interchange.md): The number of bits in each of the two address chunks.
- $V$ (volume), bound on [Fast address-chunk interchange](address-interchange.md): The number of entries of the array.
- $\tau$ (time exponent), bound on [Fast address-chunk interchange](address-interchange.md): The fixed exponent below 1 in the time bound, 1-2^{-50}.
- $q$ (radix), bound on [Fast address-chunk interchange](address-interchange.md): The fixed prime used as digit radix.
- $H$ (first chunk), bound on [Fast address-chunk interchange](address-interchange.md): The value of the first chunk.
- $D$ (second chunk), bound on [Fast address-chunk interchange](address-interchange.md): The value of the second chunk.
- $e$ (chunk digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of radix-q digits in each chunk.
- $m$ (fields per chunk), bound on [Fast address-chunk interchange](address-interchange.md): The number of fields each chunk is split into.
- $k$ (levels), bound on [Fast address-chunk interchange](address-interchange.md): The number of recursion levels, with e = m^k.
- $b$ (field width), bound on [Fast address-chunk interchange](address-interchange.md): The number of digits in each field.
- $W$ (wires), bound on [Fast address-chunk interchange](address-interchange.md): The number of wires of the exchange network.
- $A_\epsilon$ (edge matrix), bound on [Fast address-chunk interchange](address-interchange.md): The matrix attached to a network edge.
- $s$ (total edge rank), bound on [Fast address-chunk interchange](address-interchange.md): The sum of the ranks of the edge matrices.
- $\Phi_M$ (frame permutation), bound on [Fast address-chunk interchange](address-interchange.md): The address permutation moving the entry at (H,D) to (H+MD,D).
- $M$ (vertex matrix), bound on [Fast address-chunk interchange](address-interchange.md): The matrix attached to a network vertex, determining its frame.
- $f_w$ (wire input), bound on [Fast address-chunk interchange](address-interchange.md): The physical input array of wire w.
- $\sigma$ (role assignment), bound on [Fast address-chunk interchange](address-interchange.md): The map sending wire w to its role sigma(w).
- $F_k$ (cost per volume), bound on [Fast address-chunk interchange](address-interchange.md): A uniform upper bound on time divided by logical volume at width m^k.
- $k'$ (chunk level), bound on [Fast address-chunk interchange](address-interchange.md): The least integer with m^{k'} at least e, the recursion depth for width e.
- $\rho$ (high digits), bound on [Fast address-chunk interchange](address-interchange.md): The number of top digits of each chunk interchanged first.
- $R$ (row range), bound on [Fast address-chunk interchange](address-interchange.md): The range of the row field formed by the two high parts.
- $a_j$ (piece count), bound on [Fast address-chunk interchange](address-interchange.md): The number of pieces of width m^j in the base-m expansion of e minus rho.
- $m$ (address length), bound on [Binary phase frames](phase-frames.md): The number of binary coordinates of an address.
- $U$ (label), bound on [Binary phase frames](phase-frames.md): A subspace of the binary address space.
- $W_{\rm c}$ (complex wire count), bound on [Binary phase frames](phase-frames.md): The number of wires of the complex network.
- $k$ (column count), bound on [Binary phase frames](phase-frames.md): The number of columns, parallel copies of the array.
- $d$ (chunk bound), bound on [Packed selected-bit addition](packed-bit-addition.md): Maximum number of chunks a layer acts on.
- $c$ (control), bound on [Packed selected-bit addition](packed-bit-addition.md): Boolean control of the eight additions.
- $u$ (target integer), bound on [Packed selected-bit addition](packed-bit-addition.md): Integer whose parity is flipped by the eight additions.
- $w$ (auxiliary integer), bound on [Packed selected-bit addition](packed-bit-addition.md): Arbitrary auxiliary integer restored by the eight additions.
- $L$ (bits per chunk), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of bits in each address chunk.
- $f$ (selected bits), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of selected bits in each chunk.
- $K$ (spacing), bound on [Packed selected-bit addition](packed-bit-addition.md): Spacing between consecutive selected positions, which is also the bit length of a segment.
- $\rho$ (offset), bound on [Packed selected-bit addition](packed-bit-addition.md): Offset of the lowest selected position.
- $M$ (address count), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of addresses.
- $R$ (record length), bound on [Packed selected-bit addition](packed-bit-addition.md): Number of bits in a record.
- $V$ (volume), bound on [Packed selected-bit addition](packed-bit-addition.md): Total number of bits, M times R.
- $A_{\rm rect}$ (counter length), bound on [Packed selected-bit addition](packed-bit-addition.md): Bit length of counters.
- $\tau$ (interchange exponent), bound on [Packed selected-bit addition](packed-bit-addition.md): Fixed exponent below one in the cost of the chunk interchange.
- $\mathcal B$ (exceptional set), bound on [Packed selected-bit addition](packed-bit-addition.md): Set of addresses where some guard fails the interval test.
- $S_0$ (packed map), bound on [Packed selected-bit addition](packed-bit-addition.md): Composition of the eight packed cyclic-shift lines.
- $\delta_{\rm bad}$ (bad fraction), bound on [Packed selected-bit addition](packed-bit-addition.md): Upper bound on the fraction of exceptional addresses.
- $p$ (coefficient precision), bound on [Packed selected-bit addition](packed-bit-addition.md): Bit precision of the record coefficients.
- $V$ (stream volume), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of bits of the stream.
- $K$ (chunk width), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of bits in an address chunk.
- $p$ (fractional bits), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of fractional bits of each coefficient.
- $D$ (selected chunks), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of address chunks whose selected bit is butterflied.
- $d$ (chunk bound), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The maximum number of chunks, D at most d.
- $e$ (axis count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of axes in a group handled by the network.
- $m$ (slot count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of slots into which the e axes are arranged.
- $f$ (slot width), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of bits in each slot.
- $s$ (child count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of children, the total of residual dimensions over the network.
- $W$ (wire count), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The number of wires of the network.
- $F(e)$ (normalized time), bound on [Simultaneous butterfly layer](simultaneous-layer.md): The time divided by the stream volume.
- $\ell$ (address bits per record), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of address bits within a record, log base 2 of r.
- $D$ (number of axes), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of axes, d-1.
- $d$ (size parameter), bound on [Tape layout for synthetic transforms](transform-layout.md): A size parameter one more than the number of axes, with d times ell of order p.
- $t_i$ (axis length), bound on [Tape layout for synthetic transforms](transform-layout.md): The length of axis i, either 2^(ell-1) or 2^ell.
- $M$ (record count), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of polynomial records, the product of the axis lengths.
- $T$ (coefficient count), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of complex coefficients, r times M.
- $p$ (precision), bound on [Tape layout for synthetic transforms](transform-layout.md): The precision in bits: coefficient parts are multiples of 2^-p.
- $K$ (chunk width), bound on [Tape layout for synthetic transforms](transform-layout.md): The width in bits of an address chunk.
- $\tau$ (interchange exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the cost of chunk interchange.
- $\lambda'$ (layer exponent), bound on [Tape layout for synthetic transforms](transform-layout.md): The fixed exponent below 1 in the cost of the simultaneous layer.
- $B$ (bit reversal), bound on [Tape layout for synthetic transforms](transform-layout.md): The bit-reversal order in which forward outputs are written.
- $L$ (layout permutation), bound on [Tape layout for synthetic transforms](transform-layout.md): The permutation of records built by the prefix moves and chunk exchanges.
- $j$ (frequency address), bound on [Tape layout for synthetic transforms](transform-layout.md): A frequency address of an output entry.
- $b$ (low-bit remainder), bound on [Tape layout for synthetic transforms](transform-layout.md): (ell-1) mod K, the number of low bits per axis beyond whole chunks.
- $q$ (chunks per axis), bound on [Tape layout for synthetic transforms](transform-layout.md): The number of whole K-bit chunks in ell-1 bits.
- $\mathcal H$ (round contraction), bound on [Tape layout for synthetic transforms](transform-layout.md): The contraction applied by one round.
- $J_E$ (signed permutation), bound on [Tape layout for synthetic transforms](transform-layout.md): The signed coefficient permutation applied in a round.
- $Q_p$ (truncation), bound on [Tape layout for synthetic transforms](transform-layout.md): Truncation toward zero of real and imaginary parts to the 2^-p grid.
- $M$ (number of records), bound on [Convolution from the retained transform layout](ring-convolution.md): The number of polynomial records, one per cyclic address of the remaining axes.
- $T$ (number of coefficients), bound on [Convolution from the retained transform layout](ring-convolution.md): The number of complex coefficients in an array, T = rM.
- $\ell$ (log of record length), bound on [Convolution from the retained transform layout](ring-convolution.md): The base-2 logarithm of the record length r.
- $K$ (layout chunk width), bound on [Convolution from the retained transform layout](ring-convolution.md): The width of the address chunks used by the tape layout.
- $P$ (pointwise product), bound on [Convolution from the retained transform layout](ring-convolution.md): The pointwise product of records, P(u,v) = uv/r.
- $\delta$ (transform error), bound on [Convolution from the retained transform layout](ring-convolution.md): The error bound sqrt2 * l * 2^{-p} for each forward transform.
- $\eta$ (truncation error), bound on [Convolution from the retained transform layout](ring-convolution.md): The error bound sqrt2 * 2^{-p} for one truncation.
- $b$ (digit width), bound on [The multiplication algorithm](multiplication-algorithm.md): The number of bits in each radix digit, $\lceil\log_2 n\rceil$.
- $p$ (precision), bound on [The multiplication algorithm](multiplication-algorithm.md): The number of fractional bits kept, $6b$.
- $s_i$ (prime axis length), bound on [The multiplication algorithm](multiplication-algorithm.md): The length of the i-th prime axis; their product is S.
- $S$ (cyclic length), bound on [The multiplication algorithm](multiplication-algorithm.md): The product of the prime axis lengths, the length of the cyclic convolution.
- $t_i$ (padded axis length), bound on [The multiplication algorithm](multiplication-algorithm.md): The padded power-of-two length of the i-th axis; their product is T.
- $T$ (padded size), bound on [The multiplication algorithm](multiplication-algorithm.md): The product of the padded axis lengths.
- $q$ (digit count), bound on [The multiplication algorithm](multiplication-algorithm.md): The number of radix-$2^b$ digits of each input, $\lceil n/b\rceil$.
- $a_j$ (radix digit), bound on [The multiplication algorithm](multiplication-algorithm.md): The j-th radix-$2^b$ digit of an input.
- $\widetilde a$ (stored chirp), bound on [The multiplication algorithm](multiplication-algorithm.md): The stored approximation of the chirp array a.
- $\gamma$ (scale exponent), bound on [The multiplication algorithm](multiplication-algorithm.md): The number of zero bits appended to each word by the exact scale $2^\gamma$.

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

- The reader cannot follow this step: "Prefix moves" (The table gives the normalized cost dK for prefix moves, but the page never says what a prefix move is or why it costs dK per bit. The paper (around line 4930) derives it from O(dK) linear scans in the synthetic-transform cost lemma; the page only derives the chunk-exchange and simultaneous-round rows.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Axis layouts" (The row d^2(1+l^tau) is stated without derivation. It comes from O(d^2) adjacent axis moves each costing O(V(1+l^tau)) (peeling one excess bit, exchanging equal-width parts), which the page does not mention.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Chirps" (The row dp^delta is given with no account of how chirps are computed or why they cost d p^delta per coefficient. The paper derives it from products on O(p)-bit numerators with the O(N log N) multiplier, costing O(d p^{1+delta}) per entry.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "so the total is small (cited)" (The page gives no reason that p^{A+C} visits-times-setup is o(V). The paper needs that r exceeds every fixed power of p, so that setup per record or per line is o(Tp). The page does not say what is cited or why it applies.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- "exceptional addresses" is the concept [Packed selected-bit addition](packed-bit-addition.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 349 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 436 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Cost accounting totals the running time of every step of [The multiplication algorithm](multiplication-algorithm.md) and shows that it is $O(n(\lg n)^{1-\kappa})$, where $\kappa=2^{-182}$ is the saved exponent.

Let $T$ be the number of coefficients in the array, $p$ the precision in bits per coefficient, and $V=Tp=\Theta(n)$ the volume. Here $d$ is the number of transform axes, $K$ the width of an exchanged address chunk, $\ell=\log_2 r$ the number of address bits of a record, $\alpha$ the Gaussian window width, and $t_i$ the length of axis $i$. The fixed exponents of [Parameter and prime-length choice](parameter-choice.md) are $\epsilon=2^{-75}$, $c=2^{-56}$, $\delta=1/16$, $\tau=1-2^{-50}$ and $\lambda'=1-2^{-54}$, giving $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $\alpha=\Theta(p^{1/4+\epsilon/2})$.

Dividing by $V$ and substituting these sizes makes each normalized cost a power $p^{1-g_i}$ with margin $g_i$ below one. Seven dominate.

| Operation | Cost$/V$ | Power of $p$ | Margin |
|---|---|---|---|
| Prefix moves | $dK$ | $\epsilon(1+c)$ | $g_1=1-\epsilon(1+c)$ |
| Chunk exchanges | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ | $g_2=\epsilon c(1-\tau)$ |
| Simultaneous rounds | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ | $g_3=\epsilon(1-\lambda')$ |
| Axis layouts | $d^2(1+\ell^\tau)$ | $\tau+\epsilon(2-\tau)$ | $g_4=1-\tau-\epsilon(2-\tau)$ |
| Gaussian lines | $dp^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ | $g_5=1/4-\delta-3\epsilon/2$ |
| Chirps | $dp^\delta$ | $\epsilon+\delta$ | $g_6=1-\delta-\epsilon$ |
| Products | $\log(rp)$ | $1-\epsilon$ | $g_7=\epsilon$ |

Substituting the fixed rationals gives $g_1>1/2$, $g_2=2^{-75}2^{-56}2^{-50}=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$, so the smallest margin is $2^{-181}=2\kappa$ <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite> This slack covers any fixed power of $\log p$.

The layout needs $O(p/K)$ chunk exchanges, since $d\ell=O(p)$, each cost bounded by $O(VK^\tau)$ in [Fast address-chunk interchange](address-interchange.md), so the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$. Each of at most $\ell$ rounds is bounded by $O(Vd^{\lambda'})$ in [Simultaneous butterfly layer](simultaneous-layer.md). [Gaussian resampling](gaussian-resampling.md) handles at most $T/t_i$ lines on axis $i$, each costing $O(t_ip^{3/2+\delta}\alpha)$, totalling $O(dTp^{3/2+\delta}\alpha)$. The $T/r$ ring-product records need integer products on $O(rp)$ bits, $O(Tp\log(rp))$ in total.

Fixed exponents $A$ and $C$ bound the recursion visits by $p^A$ and the setup per visit by $p^C$, so the total is small <cite data-source="paper">costs at most $p^{A+C}=o(Tp)$.</cite> Repairing the fraction $O(d2^{-K})$ of exceptional addresses costs $o(V)$ since $K=\Theta(p^{\epsilon c})$, as do global setup and prime search.

Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ <cite data-source="paper">O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).</cite> Schoolbook multiplication below a fixed cutoff is absorbed into the constant <cite data-source="paper">many smaller lengths are included by enlarging the implicit constant.</cite> So one machine runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

The exponent is only $2^{-182}$ below one because $g_2$ multiplies three small exponents: $\epsilon$ (few axes), $c$ (narrow chunks) and $1-\tau$ (small interchange saving).

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

Write the body to `exegenius/tasks/0115-write-cost-accounting.answer.md` and the JSON to `exegenius/tasks/0115-write-cost-accounting.answer.json`, then run `exegenius submit 0115-write-cost-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0115-write-cost-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
