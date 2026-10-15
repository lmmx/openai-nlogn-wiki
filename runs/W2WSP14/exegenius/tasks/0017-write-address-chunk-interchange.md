# exegenius task 0017-write-address-chunk-interchange

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WSP14` (paths below are relative to it)

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

Concept: Fast address-chunk interchange
Gloss: The first tape procedure: swapping two disjoint contiguous address fields of u bits, (p,h,g,d,z) ↦ (p,d,g,h,z), in O(V u^τ) for a fixed τ<1 by building the swap from address shears executed through the bit network, with XOR combinations of intermediate data.
Also called: chunk swap, tape interchange

## This page in the argument

The step: Fast address-chunk interchange: swapping two disjoint contiguous address fields of $u$ bits, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, takes $O(Vu^\tau)$ time with $\tau=1-2^{-50}$.
How: Run the bit network with address-shear frames, so that an edge matrix of rank $a$ costs $a$ smaller interchanges on role streams of volume $V/W$; solve the resulting recurrence, then remove the power-width and row restrictions.
Why: The sources say an edge matrix of rank $a$ requires $a$ smaller interchanges, and the rank sum is below $Wm$, which saves a power of the chunk width. (the sources say so: "An edge matrix of rank $a$ will require $a$ smaller interchanges." (paper))

Its sub-steps, in order:

- A rational shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ by a rank-$a$ matrix $A$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work. (on [Address shear and lower-triangular factorization](address-shear.md))
- Power-width interchange: for $e=m^k$ and a row field divisible by $W^k$, two chunks of $e$ radix-$q$ digits are interchanged in $O(Ve^\tau)$ time.
- Any equal-width interchange $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ of two $u$-bit chunks costs $O(Vu^\tau)$, $\tau=1-2^{-50}$, for arbitrary $P,G,B$ and $u\ge1$ (including $B=1$).

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- Both tape procedures cost a power of their parameter below one, because each runs a fixed linear exchange network on $W$ wires whose edge changes are smaller calls on role streams of volume $V/W$, with total number of calls $s<Wm$, so that each level of recursion multiplies the cost per volume by $s/W<m^\tau$ while the parameter shrinks by $m$.; how: Build a finite linear exchange network that restores its scratch wires, give its vertices frames so that only endpoint operators matter, attach nested subspace labels so that the total rank $s$ of all edge changes is below $Wm$, and unroll the resulting recursion once with bit gates (address-chunk interchange) and once with Gaussian-dyadic phase gates (simultaneous butterfly layer). (on [Recursive rank saving](rank-saving-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.5.2, S4.5.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.5.2**: Power-width interchange: for $e=m^k$ and a row field divisible by $W^k$, two chunks of $e$ radix-$q$ digits are interchanged in $O(Ve^\tau)$ time.
How: Induct on $k$: split rows cyclically into $W$ role streams of volume $V/W$, run the bit network with the frame $\Phi_{M_v}$ so that each edge $e$ applies the shear $\Phi_{A_e}$ via Lemma on matrix shears (smaller interchanges), and obtain the full interchange from three shears.
- S4.5.2.1: Split whole rows cyclically into $W$ role streams within each prefix, writing the row number as $r=Wg+(w-1)$; all streams have the same shape and volume $V/W$, and row counts divisible by $W^{k-1}$.
  Source: "Split whole rows cyclically into $W$ role streams within each prefix" (paper)
  > Split whole rows cyclically into $W$ role streams within each prefix preceding the row field. Write the original row number as $r=Wg+(w-1)$ with $1\le w\le W$; stream $w$ has row number $g$. These streams have exactly the same remaining shape, including the full ranges of $H$ and $D$. Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$.
- S4.5.2.2: Apply $\Phi_{A_e}$ to each edge's role stream (implemented by the shear lemma with recursive interchanges of pivot pairs of $b=e/m$ digit fields) and run every circuit gate pointwise at matching addresses.
  Source: "$\Phi_{A_e}$ to that role stream; implement it by" (paper)
  > For a rational matrix $M$, let $\Phi_M$ act on an array by moving its entry at address $(H,D)$ to $(H+MD,D)$, with every spectator unchanged. Thus $\Phi_M$ is the array permutation induced by that address map. Its inverse is $\Phi_{-M}$ and $\Phi_{M'}\Phi_M=\Phi_{M'+M}$. On every circuit edge apply $\Phi_{A_e}$ to that role stream; implement it by Lemma~\ref{lem:matrix-shear}, recursively interchanging each pivot pair of $b$-digit fields. Execute each circuit gate pointwise at matching addresses of its role streams.
- S4.5.2.3: By the frame identity with $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$, the physical output is $f'_{\rho(w)}=\Phi_{I_m}f_w$, i.e. $H\gets H+D$ on every row, including rows serving as scratch roles with arbitrary contents; merging returns each row to its original place.
  Source: "=\Phi_{I_m}f_w," (paper)
  > The row split supplies the common address set used in the frame identity~\eqref{eq:common-frame-identity}. Here the frame at a vertex with matrix $M$ is the address permutation $\Phi_M$, and every edge changes it by $\Phi_{M'-M}$. The same invariant proof applies because a common address permutation commutes with every pointwise bit gate. For the physical input arrays $f_w$, the logical arrays are $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$; this only specifies their interpretation, with no initial tape operation. The logical circuit routes $g_w$ to role $\rho(w)$. Thus its physical output satisfies \[ f'_{\rho(w)} =\Phi_{M_{\mathrm{out}(\rho(w))}} \Phi_{-M_{\mathrm{in}(w)}}f_w =\Phi_{I_m}f_w, \] by~\eqref{eq:finite-shear-contract}. Merge by returning row $g$ of output role $\rho(w)$ to the original row $Wg+(w-1)$ within the same preceding prefix. This undoes $\rho$ and restores row order. The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary.
- S4.5.2.4: The interchange is $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ componentwise, and only the middle shear uses the circuit; the other two updates target the later group and cost $O(V)$.
  Source: "updates target the later group and have linear cost." (paper)
  > To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.
- S4.5.2.5: The number of recursive calls equals the sum of the edge ranks, exactly $s$, each on one role stream of volume $V/W$.
  Source: "The number of recursive calls is the sum of the edge ranks, exactly $s$." (paper)
  > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- S4.5.2.7: The recurrence $F_0=O(1)$, $F_k\le(s/W)F_{k-1}+O(1)$ with $s/W<m^\tau$ solves to $F_k=O(e^\tau)$.
  How: Unroll it into the geometric sum $\sum_{j=0}^k a^j$ with $a=s/W$ and bound it separately for $a\le1$ and $a>1$.
  - S4.5.2.7.1: Each of the $s$ recursive calls acts on one role stream of volume $V/W$, so dividing by $V$ gives $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.
    Source: " F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)." (paper)
    > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
  - S4.5.2.7.2: For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$: at most $k+1=O(m^{k\tau})$ if $a\le1$, and $O(a^k)$ if $a>1$.
    Source: "For $a=s/W<m^\tau$ the geometric sum" (paper)
    > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
  - S4.5.2.7.3: Hence $F_k=O(e^\tau)$ for $e=m^k$, i.e. time $O(Ve^\tau)$.
    Source: "Hence $F_k=O(e^\tau)$." (paper)
    > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- S4.5.2.8: Scheduling the recursive calls on a fixed number of tapes costs only $O(V)$ at each node, so the additive term of the recurrence is valid and temporary storage is not charged to volume.
  How: Keep role streams on a parking stack and descriptors on a separate stack, so each call moves only its own volume; bound descriptor work by a power of $\log V_j$.
  - S4.5.2.8.1: Reserve $W$ role tapes, work tapes, a parking stack and a descriptor stack; before a recursive call park the $W-1$ inactive streams, copy the active stream to the child I/O area, and restore afterwards, never sweeping parked ancestors.
    Source: "Reserve $W$ role tapes, a fixed set of" (paper)
    > \paragraph{A fixed-tape depth-first schedule.} Here we complete the implementation assertion used in \eqref{eq:swap-recurrence}. Reserve $W$ role tapes, a fixed set of I/O and elementary-operation work tapes, one parking stack tape, and a separate descriptor stack. Although $W$ is large, it is fixed. At a call boundary all reusable work tapes, other than the current I/O and local descriptor, are empty and their heads are at their origins. The parking and descriptor heads are at the tops of their stacks.
  - S4.5.2.8.2: Each push, pop, copy, positioning or erasure moves $O(V)$ symbols at a parent node and there are only the fixed number $s$ of child calls, giving precisely the extra $O(V)$ term.
    Source: "Each push, pop, copy, positioning operation, or erasure moves $O(V)$" (paper)
    > Each push, pop, copy, positioning operation, or erasure moves $O(V)$ symbols at a parent node. There are only the fixed number $s$ of child calls. This gives precisely the additional $O(V)$ term claimed above, even though each child itself has volume $V/W$. Temporary storage is therefore not substituted for logical volume in the factor $s/W$.
  - S4.5.2.8.3: Descriptor processing fits too: with $V_j=V_0/W^j$ and $j\le\log_m e_0$ we have $V_j\ge q^{2e_0}$ and $j\log W=O(e_0)=O(\log V_j)$, so $\log V_0=O(\log(2V_j))$ and descriptor work $(\log(2V_0))^{O(1)}=O(V_j)$.
    Source: "V_j\ge q^{2e_0},\qquad" (paper)
    > For completeness, descriptor processing also fits this term when the payload is one bit. Let $V_0$ be the volume at the root of one power-width call with width $e_0=m^{k_0}$, and $V_j=V_0/W^j$ the volume of any depth-$j$ child. Here $j\le k_0=\log_m e_0$. The root row count is at least $W^{k_0}$, so at depth $j$ it is still at least one. Both original chunk ranges remain present: digits outside the current subchunks become spectators rather than being removed. Hence \[ V_j\ge q^{2e_0},\qquad j\log W\le(\log_m e_0)\log W=O(e_0)=O(\log V_j). \] It follows that $\log V_0=\log V_j+j\log W=O(\log(2V_j))$. A local descriptor lists the row field, at most the current $m+m$ fields, and a fixed number of intervals formed from intervening spectator fields. Computing products of their lengths, subdividing target fields, copying lengths, and storing the current instruction take $(\log(2V_0))^{O(1)}=O(V_j)$ time at that child, since every fixed power of $\log(2V_j)$ is $O(V_j)$. Before descending, construct the child's descriptor by retaining its two target fields and combining each consecutive group of spectator fields into one interval. The ancestor's subdivision need not remain active in the child. Stack entries contain finite instructions and binary integers, not new alphabet symbols. These observations establish one finite machine for every recursion depth and every choice of spectator lengths.

**S4.5.3**: Any equal-width interchange $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ of two $u$-bit chunks costs $O(Vu^\tau)$, $\tau=1-2^{-50}$, for arbitrary $P,G,B$ and $u\ge1$ (including $B=1$).
How: Take the top $\rho$ digits of both chunks as an ad-hoc row field, pad rows to a multiple of $W^k$, split the remaining width into base-$m$ pieces handled by the power-width interchange, and pad binary ranges up to $q^e$.
- S4.5.3.1: Set $k=\lceil\log_m e\rceil$ and $\rho=\lceil k\log W/(2\log q)\rceil$, so $1\le\rho<e$ and $\rho=O(\log(2e))$ for all large $e$; the bounded remaining widths use $e$ single-digit interchanges.
  Source: "k=\lceil\log_m e\rceil,\qquad" (paper)
  > \begin{proof} First suppose the two ranges are $[q^e]$, where $q$ is the fixed prime already chosen. Set \[ k=\lceil\log_m e\rceil,\qquad \rho=\left\lceil\frac{k\log W}{2\log q}\right\rceil. \] For all sufficiently large $e$, $1\le\rho<e$ and $\rho=O(\log(2e))$. Handle the bounded remaining set of widths by $e$ individual digit interchanges; the constant in $O(Ve^\tau)$ absorbs their cost.
- S4.5.3.2: Exchange the top $\rho$ digits of the two chunks and join them: field orders $(h^+,h^-,g,d^+,d^-)\to(d^+,h^+,h^-,g,d^-)\to(d^+,h^+,d^-,g,h^-)\to(d^+,d^-,g,h^+,h^-)$, costing $O(V\rho)$.
  Source: "\text{after exchanging and joining the high parts}" (paper)
  > Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.
- S4.5.3.3: In the two middle orders the first two fields form a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks.
  Source: "R=q^{2\rho}\ge W^k" (paper)
  > Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.
- S4.5.3.4: Pad zero rows within each prefix to $R'=W^k\lceil R/W^k\rceil<2R$, so the row count is divisible by $W^k$ and padded volume is less than $2V$.
  Source: "R'=W^k\left\lceil R/W^k\right\rceil<2R." (paper)
  > Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.
- S4.5.3.5: Write the remaining width in base $m$: $e-\rho=\sum_{j=0}^k a_jm^j$ with $0\le a_j<m$, and split each chunk into $a_j$ consecutive pieces of width $m^j$.
  Source: "e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m." (paper)
  > Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.
- S4.5.3.6: Applying the power-width interchange to each piece pair costs $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, a geometric sum since $a_j<m$ and $m^k<me$.
  Source: "O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)." (paper)
  > Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.
- S4.5.3.7: For binary chunks, pad each range $[2^u]$ up to $[q^e]$ with $q^e\ge2^u$ minimal (volume grows by less than $q^2$, a fixed factor), interchange, and scan the invalid entries away; since $e=O(u)$ the cost is $O(Vu^\tau)$.
  Source: "Finally, for binary chunks let $e$ be the least integer with" (paper)
  > Finally, for binary chunks let $e$ be the least integer with $q^e\ge2^u$. Pad each of the two chunk ranges numerically from $[2^u]$ to $[q^e]$, putting zero in an entry if either chunk coordinate is invalid. The increase in volume is less than $q^2$, a fixed factor. The padding is a nested scan through consecutive valid and invalid intervals, with their lengths prepared from the shape. It costs $O(V)$ with a constant depending on $q$. Lexicographic radix-$q$ order of $[q^e]$ is its numerical order, just as binary order of $[2^u]$ is its numerical order. Padding therefore preserves the order of the existing entries without converting the digits of every address. The completed interchange preserves the set on which both chunk coordinates lie below $2^u$. Scan away the other entries to recover the desired binary array. Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$. \end{proof}
- S4.5.3.8: Chunks differing by one bit in width are handled by one single-bit move ($O(V)$) before or after an equal-width interchange.
  Source: "For widths differing by one bit, choose the leading bit of the longer" (paper)
  > The lemma permits arbitrary prefix, gap, and suffix lengths. Thus every later interchange of equal bit chunks is an instance of its stated layout, after multiplying the irrelevant contiguous lengths. For widths differing by one bit, choose the leading bit of the longer chunk as the extra bit. Suppress the outer prefix and suffix, and write $g$ for the intervening address field. If the first chunk is longer, write it as $(h_0,H)$, so $H$ and the second chunk $D$ have equal width. The physical orders are \[ (h_0,H,g,D)\longmapsto(h_0,D,g,H) \longmapsto(D,g,h_0,H). \] The first step interchanges $H,D$ by the lemma; the second moves the single bit $h_0$ immediately before $H$. If the second chunk is longer, write it as $(d_0,D)$, with $H$ the first chunk. Use \[ (H,g,d_0,D)\longmapsto(d_0,H,g,D) \longmapsto(d_0,D,g,H). \] Here the first step moves $d_0$ immediately before $H$, and the second interchanges $H,D$. In each case $g$ remains between the two full chunks in the final order. If $H,D$ are empty, the indicated equal-width interchange is the identity. Each case uses one single-bit move, costing $O(V)$ by Lemma~\ref{lem:elementary-streams}, in addition to the equal-width interchange. No unrestricted array transpose is being used in these operations. \section{Fast simultaneous synthetic butterfly layers} \label{sec:fast-butterfly-layers}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.5.1 (on [Address shear and lower-triangular factorization](address-shear.md)): A rational shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ by a rank-$a$ matrix $A$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Address shear and lower-triangular factorization](address-shear.md): The address permutation (H,D) ↦ (H+AD, D) on two vectors of fields; a rank-a matrix factors as E₁ΠE₂ with lower-triangular E₁,E₂ so that it costs a single-pair swaps plus linear-time updates, and three shears D←D−H, H←H+D, D←H−D interchange H and D.
  Shown as: Fast address-chunk interchange *<predicate>* Address shear and lower-triangular factorization
- [Recursive rank saving](rank-saving-recurrence.md): Running the linear network with edge changes implemented by smaller calls on role streams of volume V/W gives a cost-per-volume recurrence F_k ≤ (s/W)F_{k−1}+O(1); because the number s of smaller calls satisfies s < Wm, this yields F_k = O(e^τ) with τ<1, a power saving in the parameter.
  Shown as: Fast address-chunk interchange *<predicate>* Recursive rank saving
- [Frames on wire arrays](common-frame-principle.md): Replacing each scalar by an array and giving every vertex an invertible linear operator D_v (its frame) lets pointwise gates commute with frames, so intermediate frames cancel and only the endpoint operator D_out·D_in⁻¹ is applied to each role while each edge pays only the change of frame D_v D_u⁻¹.
  Shown as: Fast address-chunk interchange *<predicate>* Frames on wire arrays
- [Arrays, addresses and volume on tapes](tape-address-model.md): An array on address set [a₁]×…×[a_t] is stored on a tape in lexicographic order with the address implicit in position; its logical volume V is the number of stored data bits, and an adjacent group of address bits is an address field or chunk.
  Shown as: Fast address-chunk interchange *<predicate>* Arrays, addresses and volume on tapes

## Pages that build on this one

- Packed selected-bit addition: A binary row addition y_j ← y_j ⊕ x_j on the same bit position in f address chunks at once, done with eight chunk-wide cyclic shifts whose segments cannot carry into each other except at a small explicit set of exceptional addresses, which are then repaired deterministically; it restores the third chunk's arbitrary contents.
- Fast simultaneous butterfly layer: The second tape procedure: applying H₀ at the same bit offset in d address chunks of a polynomial-record array in cost O(V d^λ') with λ'<1, by evaluating the layer exactly through the phase-frame network with packed chunk moves before a single truncation.
- Convolution over the polynomial ring: Normalized convolution on d−1 axes of arrays with entries in C[y]/(y^r+1): two forward synthetic transforms keeping the same frequency order, pointwise polynomial products (by signed packing) divided by r, and the opposite transform, all using the fast layers and chunk swaps.
- Cost accounting and the saving κ: Dividing every cost by V = Tp = Θ(n) gives a table of seven dominant powers of p (layout moves, chunk exchanges, simultaneous butterfly rounds, CRT layout, Gaussian line maps, chirps, packed products), each at most 1−2κ with κ = 2^{−182}, giving total O(n (lg n)^{1−κ}).

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Subspace labels from three-element subsets](subset-intersection-labels.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
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

- "The first procedure interchanges two disjoint contiguous address" (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "(p,h,g,d,z)\longmapsto(p,d,g,h,z)" (paper)

  > \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}


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

Write the body to `exegenius/tasks/0017-write-address-chunk-interchange.answer.md` and the JSON to `exegenius/tasks/0017-write-address-chunk-interchange.answer.json`, then run `exegenius submit 0017-write-address-chunk-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0017-write-address-chunk-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
