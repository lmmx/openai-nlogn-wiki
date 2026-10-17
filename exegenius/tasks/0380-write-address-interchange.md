# exegenius task 0380-write-address-interchange

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
Also called: chunk swap, tape interchange, costly recursive primitive

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
- $u$ (first input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The first of the two n-bit integers being multiplied.
- $v$ (second input), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The second of the two n-bit integers being multiplied (not the number of triples).
- $b$ (digit bits), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of bits in one radix-2^b digit.
- $T$ (padded length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The padded length, a power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The length of the cyclic convolution, with T/2<S<T.
- $q$ (digit count), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The number of digits in each input, not the sequence length of the convolution page.
- $x$ (polynomial variable), bound on [Multiplication as radix-digit convolution](radix-digit-reduction.md): The indeterminate of the digit polynomials, evaluated at 2^b to recover the integers.
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
- $\beta$ (radix), bound on [Elementary stream operations](stream-ops.md): The number of values one digit can take.
- $W$ (stream count), bound on [Elementary stream operations](stream-ops.md): The fixed number of streams into which rows are dealt.
- $P$ (prefix count), bound on [Elementary stream operations](stream-ops.md): The number of prefix values of the array in item 4.
- $R$ (row count), bound on [Elementary stream operations](stream-ops.md): The number of rows in item 4; here R is not the scalar ring.
- $B$ (row length), bound on [Elementary stream operations](stream-ops.md): The number of entries per row in item 4.
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
- $q$ (prime radix), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The radix of the stored digits, a prime (not a sequence length).
- $b$ (field digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of base-q digits of a field.
- $Q$ (field value count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of values a field can take.
- $y$ (field value), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The value of the target field, an integer from 0 to Q-1 (not the ring variable).
- $a$ (offset), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The offset added to the target field, prepared from the control values.
- $B$ (suffix digit count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of digits following the target field.
- $c$ (scaling multiplier), bound on [Controlled shifts and rational scalings](controlled-shifts.md): A fixed positive integer prime to q by which the field is multiplied.
- $j$ (wrap count), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The number of times cy wraps past Q.
- $y'$ (scaled position), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The position cy - jQ to which the block at position y is sent.
- $c'$ (unit denominator), bound on [Controlled shifts and rational scalings](controlled-shifts.md): The positive integer denominator of a rational unit, prime to q.
- $q$ (field base), bound on [Matrix shear by triangular factorization](matrix-shear.md): A fixed odd prime, the base of the digits.
- $b$ (digits per field), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of base-q digits in one field.
- $a$ (rank), bound on [Matrix shear by triangular factorization](matrix-shear.md): The rank of the matrix A.
- $m$ (fields per group), bound on [Matrix shear by triangular factorization](matrix-shear.md): The number of fields in each of the groups H and D.
- $I$ (identity matrix), bound on [Two-point kernel C](phase-kernel.md): The 2x2 identity matrix.
- $X$ (bit flip), bound on [Two-point kernel C](phase-kernel.md): The 2x2 matrix swapping the two entries of a pair.
- $a$ (kernel constant), bound on [Two-point kernel C](phase-kernel.md): The complex constant (1+i)/2.
- $b$ (kernel coefficient), bound on [Two-point kernel C](phase-kernel.md): The complex coefficient (1-i)/2 of the bit flip in the kernel.
- $C$ (two-point kernel), bound on [Two-point kernel C](phase-kernel.md): The matrix aI + bX.
- $\mathsf S$ (phase matrix), bound on [Two-point kernel C](phase-kernel.md): The diagonal matrix diag(1, i) multiplying the second entry of a pair by i.
- $H_0$ (averaging step), bound on [Two-point kernel C](phase-kernel.md): The matrix of the two-point averaging and differencing step.
- $H$ (Hadamard matrix), bound on [Two-point kernel C](phase-kernel.md): The normalized Hadamard matrix sqrt(2) H_0.
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
- $d$ (axis count), bound on [Chinese-remainder address map](crt-map.md): The number of prime cyclic axes, with no coefficient axis counted.
- $s_i$ (axis length), bound on [Chinese-remainder address map](crt-map.md): The length of prime cyclic axis i; the s_i are pairwise coprime.
- $P_i$ (prefix product), bound on [Chinese-remainder address map](crt-map.md): The product of the axis lengths s_j with j<i.
- $\mu_i$ (coordinate exponent), bound on [Chinese-remainder address map](crt-map.md): The inverse of P_i modulo s_i, the exponent of x_i in the image of x.
- $\Phi$ (address map), bound on [Chinese-remainder address map](crt-map.md): The ring isomorphism sending x to the product of x_i^{mu_i}.
- $x_i$ (axis variable), bound on [Chinese-remainder address map](crt-map.md): The variable of axis i in the multi-axis ring.
- $k$ (coefficient index), bound on [Chinese-remainder address map](crt-map.md): A single coefficient index, an exponent of x; not an output index tuple as on the multidimensional-transform page.
- $a_j$ (mixed-radix digit), bound on [Chinese-remainder address map](crt-map.md): The digit of k of weight P_j, with 0<=a_j<s_j.
- $j$ (digit index), bound on [Chinese-remainder address map](crt-map.md): The index of an axis before axis i, in the product defining P_i, and later the index of a mixed-radix digit.
- $b_i$ (axis coordinate), bound on [Chinese-remainder address map](crt-map.md): The axis-i coordinate of Phi(x^k).
- $\ell$ (address bits), bound on [Chinese-remainder address map](crt-map.md): The number of address bits of an axis of length r.
- $T$ (padded record count), bound on [Chinese-remainder address map](crt-map.md): The number of padded records, the product of the padded axis lengths t_i.
- $\tau$ (interchange exponent), bound on [Chinese-remainder address map](crt-map.md): A fixed exponent below 1 in the chunk-interchange cost.
- $i$ (axis index), bound on [Chinese-remainder address map](crt-map.md): The index of a prime cyclic axis, from 1 to d.
- $t_i$ (padded axis length), bound on [Chinese-remainder address map](crt-map.md): The length of axis i after zero padding, a power of two between r/2 and r.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The length of the Fourier transform being re-expressed, coprime to t.
- $t$ (transform length), bound on [Gaussian resampling](gaussian-resampling.md): The larger length, a power of two, of the transform through which the length-s transform is expressed.
- $\alpha$ (width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer width parameter of the Gaussian weights, with 2<=alpha<sqrt p.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The relative gap t/s-1 between the target and source lengths.
- $j$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $k$ (coordinate index), bound on [Gaussian resampling](gaussian-resampling.md): A single integer coordinate index.
- $q_j$ (nearest coordinate), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest to tj/s.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The signed distance tj/s-q_j from tj/s to the nearest integer.
- $E$ (Neumann error), bound on [Gaussian resampling](gaussian-resampling.md): The map N-I, whose norm is small.
- $K$ (series term count), bound on [Gaussian resampling](gaussian-resampling.md): The number of terms of the Neumann series that are kept.
- $\beta$ (unit), bound on [Retained permutation cancellation](retained-permutations.md): A unit modulo q, an integer coprime to q, used as the multiplier of the index permutation R_beta.
- $R_\beta$ (index scaling), bound on [Retained permutation cancellation](retained-permutations.md): The permutation of a length-q vector sending z to the vector with entries z_{beta j}.
- $w$ (summation index), bound on [Retained permutation cancellation](retained-permutations.md): The index of the sum defining the transform of R_beta z.
- $w'$ (new summation index), bound on [Retained permutation cancellation](retained-permutations.md): The summation index after the substitution w' = beta w.
- $\nu$ (setup degree), bound on [Retained permutation cancellation](retained-permutations.md): A fixed exponent such that setup work per line is O(p^nu).
- $F_q^+$ (opposite transform), bound on [Retained permutation cancellation](retained-permutations.md): The discrete Fourier transform of length q with the sign of the exponent reversed.
- $z$ (transformed vector), bound on [Retained permutation cancellation](retained-permutations.md): A vector of q complex entries.
- $A$ (axis input contraction), bound on [Retained permutation cancellation](retained-permutations.md): The linear contraction applied to the input of one axis in the resampling identity.
- $B_0$ (axis output contraction), bound on [Retained permutation cancellation](retained-permutations.md): The linear contraction applied to the output of one axis in the resampling identity.
- $P_s$ (source permutation), bound on [Retained permutation cancellation](retained-permutations.md): The permutation (P_s u)_j = u_{tj} of a length-s vector.
- $P_t$ (target permutation), bound on [Retained permutation cancellation](retained-permutations.md): The permutation (P_t v)_k = v_{-sk} of a length-t vector.
- $u$ (first array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer here.
- $v$ (second array), bound on [Retained permutation cancellation](retained-permutations.md): A complex array, not an integer here.
- $a$ (round count), bound on [Retained frequency order](frequency-order.md): The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on [Retained frequency order](frequency-order.md): The position of an output of the transform.
- $s$ (completed rounds), bound on [Retained frequency order](frequency-order.md): The number of rounds completed so far.
- $B_t$ (bit-reversal permutation), bound on [Retained frequency order](frequency-order.md): The permutation moving the entry at j to rev_a(j).
- $\mathcal H$ (parallel butterfly), bound on [Retained frequency order](frequency-order.md): The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on [Retained frequency order](frequency-order.md): The recordwise operation multiplying each record by y^E.
- $h_p$ (grid spacing), bound on [Error tracking and exact recovery](precision-recovery.md): The grid spacing 2^{-p} of the fixed-point records.
- $L$ (log of padded length), bound on [Error tracking and exact recovery](precision-recovery.md): The base-2 logarithm of the padded length T.
- $a$ (error size), bound on [Error tracking and exact recovery](precision-recovery.md): The size of an error in grid spacings.
- $x$ (disk array), bound on [Error tracking and exact recovery](precision-recovery.md): An array in the unit disk to which a phase or chirp transform is applied.
- $u$ (scaled first digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the first input.
- $v$ (scaled second digits), bound on [Error tracking and exact recovery](precision-recovery.md): The scaled digit array of the second input.
- $\tau$ (interchange exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent in the cost of a chunk interchange.
- $\sigma$ (growth exponent bound), bound on [Parameter and prime-length choice](parameter-choice.md): An exponent bounding the growth of recursive calls.
- $\beta$ (threshold exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent setting the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The final exponent of the layer cost V d^lambda' on bit volume V.
- $V$ (bit volume), bound on [Parameter and prime-length choice](parameter-choice.md): The bit volume of the data on which the layer acts.
- $c$ (chunk-width exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the address-chunk width; not the scaling integer of controlled shifts.
- $\epsilon$ (axis-count exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the axis count.
- $C_1$ (guard-bit exponent), bound on [Parameter and prime-length choice](parameter-choice.md): The exponent of the guard bits.
- $\delta$ (resampling slack), bound on [Parameter and prime-length choice](parameter-choice.md): The resampling-cost slack.
- $K$ (address-chunk width), bound on [Parameter and prime-length choice](parameter-choice.md): The width in bits of an address chunk, floor of d^c.
- $\eta$ (relative prime distance), bound on [Parameter and prime-length choice](parameter-choice.md): The smallest relative distance at which a prime s_i may lie below t_i.
- $q$ (interval integer), bound on [Parameter and prime-length choice](parameter-choice.md): An integer in the prime-interval lemma, not a radix or sequence length.
- $a_d$ (a_d constant), bound on [Parameter and prime-length choice](parameter-choice.md): Lower constant in the bound a_d p^epsilon <= d.
- $b_d$ (b_d constant), bound on [Parameter and prime-length choice](parameter-choice.md): Upper constant in the bound d <= b_d p^epsilon.
- $a_r$ (a_r constant), bound on [Parameter and prime-length choice](parameter-choice.md): Lower constant in the bound 2^(a_r p/d) <= r.
- $b_r$ (b_r constant), bound on [Parameter and prime-length choice](parameter-choice.md): Upper constant in the bound r <= 2^(b_r p/d).
- $C_\ell$ (C_ell constant), bound on [Parameter and prime-length choice](parameter-choice.md): Constant in the bound d ell <= C_ell p.
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
- $\mathcal C$ (time per unit volume), bound on [Recursive power saving](rank-recurrence.md): The running time of a call at a given parameter, divided by the volume of its stream.
- $j$ (recursion depth), bound on [Recursive power saving](rank-recurrence.md): The number of recursion levels below the top call, indexing the terms of the unrolled sum; here not the stage number of the subspace-labels page.
- $\eta$ (relative rank deficit), bound on [Recursive power saving](rank-recurrence.md): The relative deficit (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm.

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
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
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

- A simulated reader (reader) trying to answer "Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?" got stuck at "so $\tau\approx1$": The page only says that some tau with s/W < m^tau is chosen, and that tau is close to 1. The page does not say why tau = 1 - 2^-50 specifically. That value appears only on the parameter page, where it is a fixed choice, so I could not tell whether it is a derived value or a chosen one. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Why can the log n factor in n log n only be beaten here by making address movement and butterfly arithmetic cheaper, rather than by some other tweak of a standard FFT-style multiplier? What accounting of a standard transform on a tape machine leads to this?" got stuck at "The saving is a power of $e$ since $s/W$ is a fixed constant below $m$ but near it, so $\tau\approx1$.": I did not see why a ratio s/W that is a constant just below m gives a saving that is a power of e. I got past it by guessing from the earlier geometric sum. (stuck at the step level)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes": This page builds the interchange from a linear network with XOR steps, frames and rank bounds that I could not follow. I used only its cost claim and could not connect the tape-level interchange to the coordinate permutations of the transform. (stuck at the beyond level)
- A simulated reader (reader) trying to answer "Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?" got stuck at "The saving is a power of $e$ since $s/W$ is a fixed constant below $m$ but near it, so $\tau\approx1$.": I could not see from this page why the near-m ratio gives exactly tau = 1-2^-50. I went to the Recursive power saving page, which checks the inequality s/W < m^tau, but the choice of 2^-50 itself is not derived there. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "The two tape primitives get a saving that is tiny yet strictly positive (an exponent just below 1). Explain why the recursive construction produces a genuine power saving, and why the whole thing hinges on one strict inequality between the number of smaller calls s and W times m." got stuck at "since $s/W$ is a fixed constant below $m$ but near it, so $\tau\approx1$": The page says that s/W being near m makes tau near 1, but never shows how the exponent follows from the ratio. The fixed tau = 1 - 2^-50 only appears later, on the Recursive power saving page, so I could not tell where the closeness claim comes from. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "The two tape primitives get a saving that is tiny yet strictly positive (an exponent just below 1). Explain why the recursive construction produces a genuine power saving, and why the whole thing hinges on one strict inequality between the number of smaller calls s and W times m." got stuck at "so there are exactly $s$ smaller calls": I could follow the count only by trusting the Matrix shear by triangular factorization page, which says a shear of rank a costs exactly a interchanges. The page itself does not say why the frame change of each edge is a shear of the right rank. (stuck at the step level)

## Previous version (revise it)

It has 709 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 886 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Fast address-chunk interchange is the first tape primitive for the main result: it swaps two disjoint address fields, chunks, of $u$ bits each (here $u$ is the chunk width in bits, not the input sequence as on the [Discrete Fourier transform](dft.md) page) in an array of $V$ stored bits (a volume, not a label) in $O(Vu^\tau)$ time on fixed tapes <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>, where $\tau=1-2^{-50}$ is the saving exponent. Its intermediate steps XOR data, yet the result is an exact permutation.

An address is $(p,h,g,d,z)$ with prefix $p$ (here $p$ means the address prefix, not the number of fractional bits as on the [Fixed-point Gaussian dyadic records](fixed-point.md) page), chunks $h$ and $d$ (here $h$ means the first address chunk, not the remaining index as on the [Butterflies and the fast transform](butterfly.md) page nor the ground-set size as on the exchange-network page, and $d$ means the second address chunk, not the number of axes as on the [Cyclic convolution](convolution.md) page), gap $g$, suffix $z$; the goal is $(p,h,g,d,z)\mapsto(p,d,g,h,z)$. Digits are radix $q$, a fixed prime (here $q$ means the digit radix, not a sequence length as on the discrete Fourier transform and cyclic convolution pages). Letters from earlier pages change meaning here.

For chunk values $H,D$, the updates $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ send $(H,D)$ to $(H,D-H)$, then $(D,D-H)$, then $(D,H)$. Only the middle one, the shear $H\gets H+D$, needs the circuit; the others are scans.

Let each chunk have $e=m^k$ digits, with $k$ recursion levels (not the depth of a value). Cut it into $m$ fields of $b=e/m$ digits, so $H,D$ become vectors over $\mathbb Z/q^b\mathbb Z$. The [Linear exchange network with restored scratch wires](exchange-network.md) has $W$ wires; each terminal and gate carries a rational $m\times m$ matrix $M$ (here $M$ means the vertex matrix of the network, not the number of cyclic addresses as on the cyclic convolution page), and edge $i$ carries $A_i=M_{\mathrm{head}(i)}-M_{\mathrm{tail}(i)}$, with $s=\sum_i\operatorname{rank}A_i$. The shear contract: input wire $w$ is routed to an output role $\rho(w)$ with $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$, the identity, and $s<Wm$ by [Nested subspace labels and rank deficit](subspace-labels.md). Choose $\tau$ with $s/W<m^\tau$.

Let $\Phi_M$ move the entry at address $(H,D)$ to $(H+MD,D)$; then $\Phi_{M'}\Phi_M=\Phi_{M'+M}$. The [Frames on wire arrays](array-frames.md) assign each vertex with matrix $M$ the frame $\Phi_M$, so an edge changes the frame by $\Phi_{M'-M}=\Phi_{A_i}$. A common address permutation commutes with every pointwise bit gate. The interchange performs each edge shear by [Matrix shear by triangular factorization](matrix-shear.md): if $A_i$ has rank $a$, then $\Phi_{A_i}$ costs $a$ interchanges of $b$-digit fields <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite>, so there are exactly $s$ smaller calls <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite>.

Suppose a row field ahead of both chunks has length divisible by $W^k$. Rows are split into role streams by [Elementary stream operations](stream-ops.md): row $Wx+w-1$ goes to stream $w$ as row $x$ (here $x$ means the stream row number, not a vector of $F$ as on the nested-subspace-labels page). Each stream has volume $V/W$ and row count divisible by $W^{k-1}$. Read wire $w$'s input $f_w$ as the logical array $\Phi_{-M_{\mathrm{in}(w)}}f_w$. By the composition rule and the contract, the output is $f'_{\rho(w)}=\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$. Merging rows back undoes $\rho$, giving $H\gets H+D$ on every original row.

Each smaller call acts on volume $V/W$; splitting, merging, gates and scheduling cost $O(V)$ here. So the time per unit volume $F_k$ at width $m^k$ obeys $F_0=O(1)$, $F_k\le(s/W)F_{k-1}+O(1)$, the recurrence of [Recursive power saving](rank-recurrence.md). Unrolled over the recursion levels $j$ (here $j$ means a recursion level index, not a digit value as on the elementary-stream-operations page, a wrap count as on the controlled-shifts page, or a stage number as on the nested-subspace-labels page), $F_k=O(\sum_{j=0}^k (s/W)^j)$. If $s/W\le1$ this is at most $k+1=O(m^{k\tau})$; otherwise it is $O((s/W)^k)$, below $m^{k\tau}$. So $F_k=O(e^\tau)$. The saving is a power of $e$ since $s/W$ is a fixed constant below $m$ but near it, so $\tau\approx1$.

For large $e$, put $k'=\lceil\log_m e\rceil$, the number of levels needed, and let $\nu=\lceil k'\log W/(2\log q)\rceil$ be the number of top digits of each chunk set aside, so $q^{2\nu}\ge W^{k'}$, $1\le\nu<e$ and $\nu=O(\log 2e)$. Split each chunk into its top digits and rest, $h^+,h^-$ and $d^+,d^-$. Interchange the high digits and move $h^+$ next to $d^+$: $(h^+,h^-,g,d^+,d^-)$ becomes $(d^+,h^+,h^-,g,d^-)$. Now $d^+,h^+$ form a row field of range $\Lambda=q^{2\nu}\ge W^{k'}$ before both remaining chunks. Pad with zero rows to $\Lambda'=W^{k'}\lceil \Lambda/W^{k'}\rceil<2\Lambda$ rows, so the volume stays below $2V$.

Write the remaining width in base $m$: $e-\nu=\sum_{j=0}^{k'}a_jm^j$ with $0\le a_j<m$, where the base-$m$ digit $a_j$ is the number of pieces of width $m^j$ into which each remaining chunk is cut. Interchange corresponding pieces. The total is $O(V)\sum_ja_jm^{j\tau}\le O(V)\,m\sum_jm^{j\tau}=O(Ve^\tau)$, since $m^{k'}<me$ makes $\sum_jm^{j\tau}$ a geometric sum. Scan away padded rows and reverse the joining, giving $(d^+,d^-,g,h^+,h^-)$ at cost $O(V\nu)=O(Ve^\tau)$.

For $u$-bit chunks, pad $[2^u]$ to $[q^e]$ with $e$ least such that $q^e\ge2^u$, and scan the padding away. Since $e=O(u)$ the cost is $O(Vu^\tau)$ <cite data-source="paper">Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.</cite>.

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

Write the body to `exegenius/tasks/0380-write-address-interchange.answer.md` and the JSON to `exegenius/tasks/0380-write-address-interchange.answer.json`, then run `exegenius submit 0380-write-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0380-write-address-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
