# exegenius task 0108-write-address-interchange

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
- Two-point kernel C (also: phase network kernel)
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

Concept: Fast address-chunk interchange
Gloss: The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
Also called: chunk swap, tape interchange

## This page in the argument

The step: Bit variant: two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$, although the intermediate steps form XOR combinations of data.
How: Run the bit network on the digits of the chunks: an edge whose matrix has rank $a$ costs $a$ interchanges of fields of $1/m$ the width (matrix shear), the $W$ role streams carry $1/W$ of the volume each, so the cost per unit volume satisfies $F_k\le(s/W)F_{k-1}+O(1)$; then remove the restrictions on width and rows.
Why: The sum of the edge ranks is less than the number of wires times $m$, so the recurrence saves a power of the chunk width. (the sources say so: "An edge matrix of rank $a$ will require $a$ smaller interchanges." (paper))
Striking feature: The saving is a power $u^\tau$ with $\tau=1-2^{-50}$ only barely below 1, although the interchange has no data-dependent arithmetic. (explain why it holds, from the method)

Its sub-steps, in order:

- For a rational $m\times m$ matrix $A$ of rank $a$ and fields over $\mathbb Z/q^b\mathbb Z$, the shear $(H,D)\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. (on [Matrix shear by triangular factorization](matrix-shear.md))
- Power-width interchange: if the circuit data satisfy the shear contract with $s<Wm$ and $s/W<m^\tau$, two disjoint chunks of $e=m^k$ radix-$q$ digits each (with a row field of length divisible by $W^k$ before both) can be interchanged in $O(Ve^\tau)$ time.
- For arbitrary widths $u$, prefixes, gaps and suffixes (including one-bit payloads) the interchange $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ of two $u$-bit chunks costs $O(Vu^\tau)$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.; how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). (on [Recursive power saving](rank-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.5.2, S1.5.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.5.2**: Power-width interchange: if the circuit data satisfy the shear contract with $s<Wm$ and $s/W<m^\tau$, two disjoint chunks of $e=m^k$ radix-$q$ digits each (with a row field of length divisible by $W^k$ before both) can be interchanged in $O(Ve^\tau)$ time.
How: Reduce the interchange to the shear $H\gets H+D$, implement the shear by the bit network run on $W$ role streams of volume $V/W$ with frame $\Phi_{A_e}$ on each edge, each edge being $\operatorname{rank}(A_e)$ smaller interchanges, obtain the recurrence $F_k\le(s/W)F_{k-1}+O(1)$ and solve it.
- S1.5.2.1: Write each chunk as $m$ consecutive $b=e/m$ digit fields, giving vectors $H,D$ over $\mathbb Z/q^b\mathbb Z$, and first construct the shear $H\gets H+D$.
  Source: "consecutive $b=e/m$ digit fields, giving vectors $H,D$ over" (paper)
  > \begin{proof} For $k=0$ apply the single-digit operation of Lemma~\ref{lem:elementary-streams}. For $k>0$, write each chunk as $m$ consecutive $b=e/m$ digit fields, giving vectors $H,D$ over $\mathbb Z/q^b\mathbb Z$. We first construct the shear $H\leftarrow H+D$.
- S1.5.2.2: Split whole rows cyclically into $W$ role streams within each prefix; row $r=Wg+(w-1)$ goes to stream $w$ as row $g$.
  Source: "Split whole rows cyclically into $W$ role streams within each prefix" (paper)
  > Split whole rows cyclically into $W$ role streams within each prefix preceding the row field. Write the original row number as $r=Wg+(w-1)$ with $1\le w\le W$; stream $w$ has row number $g$. These streams have exactly the same remaining shape, including the full ranges of $H$ and $D$. Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$.
- S1.5.2.3: Each role stream has logical volume $V/W$ and its row count is divisible by $W^{k-1}$, so the same argument applies one level down.
  Source: "logical volume $V/W$, and its row count is divisible by $W^{k-1}$." (paper)
  > Split whole rows cyclically into $W$ role streams within each prefix preceding the row field. Write the original row number as $r=Wg+(w-1)$ with $1\le w\le W$; stream $w$ has row number $g$. These streams have exactly the same remaining shape, including the full ranges of $H$ and $D$. Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$.
- S1.5.2.4: On every circuit edge apply $\Phi_{A_e}$ to that role stream, implemented by the matrix-shear lemma, recursively interchanging each pivot pair of $b$-digit fields.
  Source: "Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair" (paper)
  > For a rational matrix $M$, let $\Phi_M$ act on an array by moving its entry at address $(H,D)$ to $(H+MD,D)$, with every spectator unchanged. Thus $\Phi_M$ is the array permutation induced by that address map. Its inverse is $\Phi_{-M}$ and $\Phi_{M'}\Phi_M=\Phi_{M'+M}$. On every circuit edge apply $\Phi_{A_e}$ to that role stream; implement it by Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair of $b$-digit fields. Execute each circuit gate pointwise at matching addresses of its role streams.
- S1.5.2.5a: The frame at a vertex with matrix $M$ is the address permutation $\Phi_M$ and every edge changes it by $\Phi_{M'-M}$; a common address permutation commutes with every pointwise bit gate.
  Source: "vertex with matrix $M$ is the address permutation $\Phi_M$, and every" (paper)
  > The row split supplies the common address set used in the frame identity~\eqref{eq:common-frame-identity}. Here the frame at a vertex with matrix $M$ is the address permutation $\Phi_M$, and every edge changes it by $\Phi_{M'-M}$. The same invariant proof applies because a common address permutation commutes with every pointwise bit gate. For the physical input arrays $f_w$, the logical arrays are $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$; this only specifies their interpretation, with no initial tape operation. The logical circuit routes $g_w$ to role $\rho(w)$. Thus its physical output satisfies \[ f'_{\rho(w)} =\Phi_{M_{\mathrm{out}(\rho(w))}} \Phi_{-M_{\mathrm{in}(w)}}f_w =\Phi_{I_m}f_w, \] by~\eqref{eq:finite-shear-contract}. Merge by returning row $g$ of output role $\rho(w)$ to the original row $Wg+(w-1)$ within the same preceding prefix. This undoes $\rho$ and restores row order. The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary.
- S1.5.2.5b: By the endpoint contract the physical output is $f'_{\rho(w)}=\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$.
  Source: "=\Phi_{I_m}f_w," (paper)
  > The row split supplies the common address set used in the frame identity~\eqref{eq:common-frame-identity}. Here the frame at a vertex with matrix $M$ is the address permutation $\Phi_M$, and every edge changes it by $\Phi_{M'-M}$. The same invariant proof applies because a common address permutation commutes with every pointwise bit gate. For the physical input arrays $f_w$, the logical arrays are $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$; this only specifies their interpretation, with no initial tape operation. The logical circuit routes $g_w$ to role $\rho(w)$. Thus its physical output satisfies \[ f'_{\rho(w)} =\Phi_{M_{\mathrm{out}(\rho(w))}} \Phi_{-M_{\mathrm{in}(w)}}f_w =\Phi_{I_m}f_w, \] by~\eqref{eq:finite-shear-contract}. Merge by returning row $g$ of output role $\rho(w)$ to the original row $Wg+(w-1)$ within the same preceding prefix. This undoes $\rho$ and restores row order. The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary.
- S1.5.2.5c: Merging row $g$ of role $\rho(w)$ back to the original row undoes $\rho$, and the result is $H\gets H+D$ on every original row, including rows assigned to scratch roles whose initial values were arbitrary.
  Source: "is $H\leftarrow H+D$ on every original row, including rows assigned" (paper)
  > The row split supplies the common address set used in the frame identity~\eqref{eq:common-frame-identity}. Here the frame at a vertex with matrix $M$ is the address permutation $\Phi_M$, and every edge changes it by $\Phi_{M'-M}$. The same invariant proof applies because a common address permutation commutes with every pointwise bit gate. For the physical input arrays $f_w$, the logical arrays are $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$; this only specifies their interpretation, with no initial tape operation. The logical circuit routes $g_w$ to role $\rho(w)$. Thus its physical output satisfies \[ f'_{\rho(w)} =\Phi_{M_{\mathrm{out}(\rho(w))}} \Phi_{-M_{\mathrm{in}(w)}}f_w =\Phi_{I_m}f_w, \] by~\eqref{eq:finite-shear-contract}. Merge by returning row $g$ of output role $\rho(w)$ to the original row $Wg+(w-1)$ within the same preceding prefix. This undoes $\rho$ and restores row order. The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary.
- S1.5.2.5d: The interchange of the two full chunks is $D\gets D-H$, then $H\gets H+D$ (the circuit), then $D\gets H-D$, componentwise; only the middle shear uses the circuit.
  Source: "D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D," (paper)
  > To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.
- S1.5.2.5e: The number of recursive calls is the sum of the edge ranks, exactly $s$, each on one role stream of volume $V/W$.
  Source: "The number of recursive calls is the sum of the edge ranks, exactly $s$." (paper)
  > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- S1.5.2.5g: Therefore $F_0=O(1)$ (single-digit operation) and $F_k\le(s/W)F_{k-1}+O(1)$, where the factor $s/W$ is the number of calls $s$ times the volume fraction $1/W$ of each.
  Source: "F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)." (paper)
  > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- S1.5.2.6: From $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\tau$ it follows that $F_k=O(e^\tau)$ for $e=m^k$.
  How: Unroll the recurrence to a geometric sum $\sum_{j=0}^{k}a^j$ with $a=s/W$ and bound it separately for $a\le1$ and $a>1$.
  - S1.5.2.6.1: Unrolling $F_k\le aF_{k-1}+O(1)$ gives $F_k=O(\sum_{j=0}^k a^j)$ with $a=s/W<m^\tau$.
    Source: "For $a=s/W<m^\tau$ the geometric sum" (paper)
    > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
  - S1.5.2.6.2: Case $a\le1$: every term is at most $1$, so $\sum_{j=0}^k a^j\le k+1=O(m^{k\tau})$.
    Source: "If $a\le1$, the sum is at" (paper)
    > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
  - S1.5.2.6.3: Case $a>1$: by the geometric series $\sum_{j=0}^k a^j=(a^{k+1}-1)/(a-1)$ the sum is $O(a^k)$, and $a^k<m^{k\tau}$.
    Source: "if $a>1$, it is $O(a^k)$." (paper)
    > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
  - S1.5.2.6.4: Hence, since $e=m^k$, $F_k=O(e^\tau)$.
    Source: "Hence $F_k=O(e^\tau)$." (paper)
    > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- S1.5.2.5f: Splitting, merging, gates, triangular operations and the parking-stack scheduling of the $s$ calls cost $O(V)$ at the node (a fixed number of operations on the node's own volume), not on the volume of the children.
  Source: "symbols at a parent node.  There are only the fixed number $s$ of child" (paper)
  > Each push, pop, copy, positioning operation, or erasure moves $O(V)$ symbols at a parent node. There are only the fixed number $s$ of child calls. This gives precisely the additional $O(V)$ term claimed above, even though each child itself has volume $V/W$. Temporary storage is therefore not substituted for logical volume in the factor $s/W$.

**S1.5.3**: For arbitrary widths $u$, prefixes, gaps and suffixes (including one-bit payloads) the interchange $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ of two $u$-bit chunks costs $O(Vu^\tau)$.
How: Supply the required rows from the chunks' own $\rho=O(\log e)$ high digits, pad the rows to a multiple of $W^k$, split the remaining width $e-\rho$ in base $m$ into $a_j$ pieces of width $m^j$, interchange each piece by the power-width case, and sum the geometric series.
- S1.5.3.1: There exist a fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure performing the address permutation $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ on arbitrary bit arrays in $O(Vu^\tau)$ steps.
  Source: "There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape" (paper)
  > \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}
- S1.5.3.2: For chunks of range $[q^e]$ put $k=\lceil\log_me\rceil$.
  Source: "k=\lceil\log_m e\rceil,\qquad" (paper)
  > \begin{proof} First suppose the two ranges are $[q^e]$, where $q$ is the fixed prime already chosen. Set \[ k=\lceil\log_m e\rceil,\qquad \rho=\left\lceil\frac{k\log W}{2\log q}\right\rceil. \] For all sufficiently large $e$, $1\le\rho<e$ and $\rho=O(\log(2e))$. Handle the bounded remaining set of widths by $e$ individual digit interchanges; the constant in $O(Ve^\tau)$ absorbs their cost.
- S1.5.3.3: Put $\rho=\lceil k\log W/(2\log q)\rceil$ so that $q^{2\rho}\ge W^k$; for large $e$, $1\le\rho<e$ and $\rho=O(\log(2e))$.
  Source: "\rho=\left\lceil\frac{k\log W}{2\log q}\right\rceil." (paper)
  > \begin{proof} First suppose the two ranges are $[q^e]$, where $q$ is the fixed prime already chosen. Set \[ k=\lceil\log_m e\rceil,\qquad \rho=\left\lceil\frac{k\log W}{2\log q}\right\rceil. \] For all sufficiently large $e$, $1\le\rho<e$ and $\rho=O(\log(2e))$. Handle the bounded remaining set of widths by $e$ individual digit interchanges; the constant in $O(Ve^\tau)$ absorbs their cost.
- S1.5.3.4: Interchange the top $\rho$ digits of the two chunks one pair at a time and join them, so the two middle field orders have a row field of the two high parts before both remaining chunks.
  Source: "the corresponding high digits one pair at a time.  The high positions" (paper)
  > Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.
- S1.5.3.5: This row field has range $R=q^{2\rho}\ge W^k$.
  Source: "R=q^{2\rho}\ge W^k" (paper)
  > Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.
- S1.5.3.6: Pad with zero rows, separately within each prefix, to $R'=W^k\lceil R/W^k\rceil<2R$ rows, so the padded volume is below $2V$ and the row count is divisible by each needed $W^j$.
  Source: "R'=W^k\left\lceil R/W^k\right\rceil<2R." (paper)
  > Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.
- S1.5.3.7: Write the remaining width in base $m$: $e-\rho=\sum_{j=0}^ka_jm^j$ with $0\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case, all using the same row field.
  Source: "e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m." (paper)
  > Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.
- S1.5.3.8: The total cost is $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$.
  Source: "O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)." (paper)
  > Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.
- S1.5.3.9: The bound $a_j<m$ and $m^k<me$ make this a geometric sum of order $e^\tau$.
  Source: "The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a" (paper)
  > Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.
- S1.5.3.10: For binary chunks of width $u$ pad each range from $[2^u]$ to $[q^e]$ with the least $e$ with $q^e\ge2^u$, a fixed factor in volume, so the cost is $O(Vu^\tau)$ since $e=O(u)$.
  Source: "Finally, for binary chunks let $e$ be the least integer with" (paper)
  > Finally, for binary chunks let $e$ be the least integer with $q^e\ge2^u$. Pad each of the two chunk ranges numerically from $[2^u]$ to $[q^e]$, putting zero in an entry if either chunk coordinate is invalid. The increase in volume is less than $q^2$, a fixed factor. The padding is a nested scan through consecutive valid and invalid intervals, with their lengths prepared from the shape. It costs $O(V)$ with a constant depending on $q$. Lexicographic radix-$q$ order of $[q^e]$ is its numerical order, just as binary order of $[2^u]$ is its numerical order. Padding therefore preserves the order of the existing entries without converting the digits of every address. The completed interchange preserves the set on which both chunk coordinates lie below $2^u$. Scan away the other entries to recover the desired binary array. Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$. \end{proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.5.1 (on [Matrix shear by triangular factorization](matrix-shear.md)): For a rational $m\times m$ matrix $A$ of rank $a$ and fields over $\mathbb Z/q^b\mathbb Z$, the shear $(H,D)\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Frames on wire arrays](array-frames.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving](rank-recurrence.md): Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving.
  Shown as: Fast address-chunk interchange *<predicate>* Recursive power saving
- [Matrix shear by triangular factorization](matrix-shear.md): Factoring a rational matrix as A = E₁ΠE₂ with lower triangular E₁, E₂ and partial permutation Π lets the shear (H,D)→(H+AD,D) be done with exactly rank(A) field interchanges.
  Shown as: Fast address-chunk interchange *<predicate>* Matrix shear by triangular factorization
- [Elementary stream operations](stream-ops.md): Linear-time scans on arrays stored in lexicographic order: swapping two digits, moving a digit, splitting into streams, applying a pointwise map and merging back.
  Shown as: Fast address-chunk interchange *<predicate>* Elementary stream operations

## Pages that build on this one

- Packed selected-bit addition: XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.
- Tape layout for synthetic transforms: Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes.
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
- [Bluestein chirp identity](chirp.md)
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
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
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "The first procedure interchanges two disjoint contiguous address" (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "Arbitrary-width interchange" (paper)

  > \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "By the endpoint contract the physical output is" (The condition called the endpoint contract is never stated on the page (the paper's condition M_out(rho(w)) - M_in(w) = I_m, line 1467, plus s<Wm), nor the composition rule Phi_{M'}Phi_M = Phi_{M'+M} (paper line 1508), so the reader cannot check that the product of frames equals Phi_{I_m}.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Each stream has volume $V/W$ and row count divisible by $W^{k-1}$" (The page never introduces a row field preceding both chunks, nor the hypothesis that its length is divisible by W^k (paper lines 1482-1484, 1502). Without it the cyclic split and the divisibility by W^{k-1} do not follow; the reader cannot tell what rows are.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Joining them, the high parts form a row field of range $R=q^{2\rho}\ge W^{k'}$ before both remaining chunks." (The page never gives the field-order construction (paper lines 1660-1676): split each chunk into top rho digits and rest, exchange the high digits, move h+ next to d+. Nor does it say that padded rows are scanned away and the joining moves reversed at the end (lines 1708-1713), nor that this movement costs O(V rho) = O(V log(2e)), absorbed into O(V e^tau). The reader cannot see how the pieces give the full interchange or why the total is O(V e^tau).). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Write $e-\rho=\sum_{j=0}^{k'} a_jm^j$, $0\le a_j<m$" (This needs 1 <= rho < e, which the paper (line 1656) only gets for sufficiently large e, handling the bounded set of small widths by individual digit interchanges (line 1657). The page states it for every e, where e-rho could be negative.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $M'$ denotes where it is first used (for a size or count, what it counts): "edges change it by $\Phi_{M'-M}$" (The page never says what M' is (presumably the matrix at the other end of the edge); it is not bound on an earlier page.)
- Say what $w$ denotes where it is first used: the page uses it before saying so in "$f_w$ is wire $w$'s input"
- Say what $g$ denotes where it is first used: the page uses it before saying so in "(prefix $p$, chunks $h,d$, gap $g$, suffix $z$)"

## Previous version (revise it)

It has 346 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 432 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Fast address-chunk interchange swaps two disjoint $u$-bit address fields of an array with $V$ entries (volume) in time $O(Vu^\tau)$ <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>, with $\tau=1-2^{-50}$ fixed.

With radix-$q$ digits, $q$ a fixed prime, let $H,D$ be the chunk values. Then $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ sends $(H,D)$ to $(D,H)$; only the middle shear needs the network.

Let chunks have $e=m^k$ digits ($m$ fields, $k$ levels), each field $b=e/m$ digits, so $H,D$ are vectors over $\mathbb Z/q^b\mathbb Z$. Each shear is performed by [Matrix shear by triangular factorization](matrix-shear.md): rank $\alpha$ costs $\alpha$ interchanges of $b$-digit fields <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite>. The [exchange network](exchange-network.md) has $W$ wires and edge matrices $A_\epsilon$ of total rank $s<Wm$ (a [rank deficit](subspace-labels.md)), with $s/W<m^\tau$.

Split whole rows cyclically into $W$ role streams; row $r=Wg+(w-1)$ goes to stream $w$ as row $g$. Each stream has volume $V/W$ and row count divisible by $W^{k-1}$; streams are split and merged by [stream scans](stream-ops.md).

A [frame](array-frames.md) at a vertex with matrix $M$ is the address permutation $\Phi_M$, $(H,D)\mapsto(H+MD,D)$; edges change it by $\Phi_{M'-M}$, and a common address permutation commutes with every pointwise bit gate. Each edge applies $\Phi_{A_\epsilon}$ to its role stream.

By the endpoint contract the physical output is $f'_{\sigma(w)}=\Phi_{M_{\mathrm{out}(\sigma(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$ ($f_w$ is wire $w$'s input, $\sigma(w)$ its role, $M_{\mathrm{in}(w)},M_{\mathrm{out}(\sigma(w))}$ the frame matrices). Merging rows back undoes $\sigma$; so $H\gets H+D$ holds on every original row, scratch rows included.

The calls number exactly $s$, the sum of the edge ranks <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite>, each on volume $V/W$; other work costs $O(V)$. With $F_k$ the bound on time per unit volume at width $m^k$, $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, so it satisfies the recurrence of [Recursive power saving](rank-recurrence.md).

Then $F_k=O(\sum_{j=0}^k a^j)$, $a=s/W<m^\tau$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$. If $a>1$, it is $O(a^k)$ with $a^k<m^{k\tau}$. So $F_k=O(e^\tau)$. Only rank deficit saves, so $\tau$ is barely below $1$.

In general the permutation is $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ (prefix $p$, chunks $h,d$, gap $g$, suffix $z$), one-bit payloads included <cite data-source="paper">In particular, $B=1$ is allowed.</cite>. Put $k'=\lceil\log_m e\rceil$ and let $\rho=\lceil k'\log W/(2\log q)\rceil$ be the number of top digits interchanged first, so $q^{2\rho}\ge W^{k'}$. Joining them, the high parts form a row field of range $R=q^{2\rho}\ge W^{k'}$ before both remaining chunks. Pad with zero rows to $R'=W^{k'}\lceil R/W^{k'}\rceil<2R$ rows.

Write $e-\rho=\sum_{j=0}^{k'} a_jm^j$, $0\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case. The cost $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$ is geometric since $a_j<m$ and $m^{k'}<me$. Padding $[2^u]$ to $[q^e]$ costs a fixed factor and gives $O(Vu^\tau)$ <cite data-source="paper">Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.</cite>.

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

Write the body to `exegenius/tasks/0108-write-address-interchange.answer.md` and the JSON to `exegenius/tasks/0108-write-address-interchange.answer.json`, then run `exegenius submit 0108-write-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0108-write-address-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
