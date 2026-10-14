# exegenius task 0014-write-power-width-interchange

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Arrays and elementary stream operations on tape
- Controlled shifts and rational scalings
- Bank-exchange network with restored scratch wires
- Frames on network wires
- Nested subspace labels and orthogonal residuals
- Strict rank saving
- Lower-triangular factorization of a matrix
- Cost of a matrix shear on address fields
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(...), Ω, Θ, asymptotically smaller, worst-case running time)
- Limits and limit inferior (also: liminf, limsup, limit of a ratio, lim inf, eventually, for all sufficiently large n)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, log_2, natural logarithm, floor function, ceiling function, powers of two, iterated logarithm, log star)
- Recurrences and geometric sums (also: recurrence relation, solving recurrences, geometric series, geometric sum, unrolling a recurrence, divide and conquer)
- Positional number systems and carries (also: binary representation, radix representation, base-b digits, bit string, most significant bit, carry propagation, schoolbook addition, padding with leading zeros)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, divide-and-conquer multiplication, Toom-Cook, quadratic multiplication)
- Bitwise operations and XOR (also: exclusive or, XOR, bitwise exclusive or, addition modulo 2, bit flip, parity, bit shift, bit mask)
- Modular arithmetic (also: integers modulo q, Z/qZ, congruence, residues, units modulo q, invertible residues, arithmetic mod q, Chinese remainder theorem for integers)
- Primes, coprimality and the extended Euclidean algorithm (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, Euclid's algorithm, Bezout identity, modular inverse, odd primes, primality testing by trial division)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit complex numbers, complex exponential, Euler's formula, twiddle factor, N-th root of unity)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear operator, linear transformation, identity matrix, diagonal matrix, unitary or involution matrix, matrix-vector product, linear combination)
- Vector spaces, subspaces, dimension and rank (also: subspace, span, basis, linear independence, dimension, rank of a matrix, rank-nullity, kernel, image, column space, direct sum, quotient space)
- Inner products, bilinear forms and orthogonal complements (also: bilinear form, dot product, orthogonality, orthogonal complement, orthogonal subspace, nondegenerate pairing, inner product space, pairing)
- Gaussian elimination and triangular matrices (also: row reduction, LU decomposition, lower triangular matrix, upper triangular matrix, elementary row operations, back substitution, unit triangular matrix, row echelon form)
- Permutations, bijections and permutation matrices (also: permutation, bijection, one-to-one correspondence, inverse permutation, partial permutation, reordering of an array, sorting network, transposition of indices, permutation matrix)
- Arithmetic modulo 2 and linear algebra over F_2 (also: F_2, GF(2), binary field, field with two elements, matrices over F_2, GL(m, F_2), mod 2 arithmetic, boolean linear algebra)
- Finite sets, subsets and counting (also: Cartesian product, subset intersection, set cardinality, binomial coefficient, inclusion-exclusion, product of index sets, power set, three-element subsets, pigeonhole)
- Circuits and directed acyclic graphs (also: arithmetic circuit, linear circuit, wires and gates, directed graph, DAG, network of gates, fan-in, source and sink nodes, layered network)
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, ‖·‖_∞, modulus bound, triangle inequality, operator norm, error bound, disk bound)
- Fixed-point numbers, dyadic rationals and rounding (also: fixed point arithmetic, dyadic rational, binary fraction, rounding to nearest integer, truncation, round-off error, precision in bits, numbers with p fractional bits, grid of spacing 2^{-p})
- Row-major order and matrix transposition (also: row-major layout, array layout, transposing a matrix, matrix transpose, k×k binary matrix, lexicographic address, two-dimensional array as a list)
- Subroutines and reductions between problems (also: black-box subroutine, reduction, calling a subroutine, oracle call, problem reduction, conditional lower bound, composition of algorithms, uniform algorithm)
- Convolution of sequences (also: linear convolution, polynomial multiplication as convolution, product of coefficient sequences, discrete convolution, convolution theorem)

## This page

Concept: Power-width chunk interchange
Gloss: Interchanging two address chunks of m^k digits by running the bit network on W cyclic role streams, with one smaller interchange per unit of edge rank, giving the recurrence F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ).

## This page in the argument

The step: Two address chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time by running the bit network on $W$ cyclic role streams, with one smaller interchange per unit of edge rank.
How: Run the exchange network on arrays: give each vertex an address-shear frame, split the rows among the $W$ roles so every gate acts pointwise, make each edge cost one smaller interchange per unit of its rank, and solve the resulting recurrence.
Why: Each recursive call handles a stream of volume $V/W$ at width $e/m$, so after dividing by volume the width multiplies the cost by $s/W$, which is less than the factor $m$ in the width itself. (the sources say so: "After dividing cost by volume, multiplying the parameter by $m$
increases the recursive contribution by $s/W<m$. This strict inequality
is the source of the power saving." (paper))
Striking feature: The final effect is an exact permutation of the stored bits, although the intermediate steps are XOR combinations of data, and it is correct whatever the initial contents of the scratch roles. (explain why it holds, from the method)

Its sub-steps, in order:

- A fixed network of $W$ wires built from three-element subsets, run in three stages, sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ and returns every scratch wire to its arbitrary initial value. (on [Bank-exchange network with restored scratch wires](exchange-network.md))
- If every vertex carries an invertible frame $D_v$ on its array and all incidences of a pointwise linear gate share it, the gate commutes with the frame, so intermediate frames cancel and a route from input role $w$ to output role $\rho(w)$ applies only $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ with its sign. (on [Frames on network wires](frames.md))
- In the bit network the total rank $s$ of all edge changes $M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)}$ is strictly less than $Wm$, the endpoint matrices differ by the identity on every role, and consequently $s/W<m^\tau$ for $\tau=1-2^{-50}$. (on [Strict rank saving](rank-saving.md))
- Every rational $m\times m$ matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones. (on [Lower-triangular factorization of a matrix](matrix-factorization.md))
- For a rational $m\times m$ matrix $A$ of rank $a$ and fields over $\mathbb Z/q^b\mathbb Z$, the map $(H,D)\mapsto(H+AD,D)$ is performed with exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work. (on [Cost of a matrix shear on address fields](matrix-shear.md))
- Splitting whole rows cyclically into $W$ role streams gives streams of identical shape, each of logical volume $V/W$, on which every gate acts pointwise.
- Applying the shear $\Phi_{A_e}$ on every edge and the gates pointwise, the endpoint identity makes the physical output of role $\rho(w)$ equal to $\Phi_{I_m}f_w$, that is the shear $H\leftarrow H+D$ on every row, scratch rows included.
- Three updates $D\leftarrow D-H$, $H\leftarrow H+D$ (through the network) and $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the network.
- With $F_k$ the time per unit volume at width $e=m^k$, one run of the network makes $s$ smaller interchanges, each on a stream of volume $V/W$, so $F_k\le(s/W)F_{k-1}+O(1)$ and, since $s/W<m^\tau$, $F_k=O(e^\tau)$.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term. (on [Sub-n-log-n integer multiplication](main-theorem.md))
- Two disjoint equal-width bit chunks of $u$ bits in an address array of volume $V$ can be interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$, by XOR combinations whose final effect is an exact permutation.; how: First interchange chunks whose width is a power of $m$ and which have enough rows (the key construction), then remove those restrictions by taking rows from a few high digits of the chunks, cutting the remaining width into base-$m$ pieces, and padding binary chunks to the working radix. (on [Address chunk interchange](chunk-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (K.6, K.7, K.8, K.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**K.6**: Splitting whole rows cyclically into $W$ role streams gives streams of identical shape, each of logical volume $V/W$, on which every gate acts pointwise.
Source: "Split whole rows cyclically into $W$ role streams within each prefix
preceding the row field.  Write the original row number as
$r=Wg+(w-1)$ with $1\le w\le W$; stream $w$ has row number $g$.
These streams have exactly the same remaining shape, including the
full ranges of $H$ and $D$.  Each has
logical volume $V/W$" (paper)
> Split whole rows cyclically into $W$ role streams within each prefix preceding the row field. Write the original row number as $r=Wg+(w-1)$ with $1\le w\le W$; stream $w$ has row number $g$. These streams have exactly the same remaining shape, including the full ranges of $H$ and $D$. Each has logical volume $V/W$, and its row count is divisible by $W^{k-1}$.

**K.7**: Applying the shear $\Phi_{A_e}$ on every edge and the gates pointwise, the endpoint identity makes the physical output of role $\rho(w)$ equal to $\Phi_{I_m}f_w$, that is the shear $H\leftarrow H+D$ on every row, scratch rows included.
Source: "Thus its physical output satisfies
\[
 f'_{\rho(w)}
 =\Phi_{M_{\mathrm{out}(\rho(w))}}
   \Phi_{-M_{\mathrm{in}(w)}}f_w
 =\Phi_{I_m}f_w,
\]
by~\eqref{eq:finite-shear-contract}." (paper)
> The row split supplies the common address set used in the frame identity~\eqref{eq:common-frame-identity}. Here the frame at a vertex with matrix $M$ is the address permutation $\Phi_M$, and every edge changes it by $\Phi_{M'-M}$. The same invariant proof applies because a common address permutation commutes with every pointwise bit gate. For the physical input arrays $f_w$, the logical arrays are $g_w=\Phi_{-M_{\mathrm{in}(w)}}f_w$; this only specifies their interpretation, with no initial tape operation. The logical circuit routes $g_w$ to role $\rho(w)$. Thus its physical output satisfies \[ f'_{\rho(w)} =\Phi_{M_{\mathrm{out}(\rho(w))}} \Phi_{-M_{\mathrm{in}(w)}}f_w =\Phi_{I_m}f_w, \] by~\eqref{eq:finite-shear-contract}. Merge by returning row $g$ of output role $\rho(w)$ to the original row $Wg+(w-1)$ within the same preceding prefix. This undoes $\rho$ and restores row order. The result is $H\leftarrow H+D$ on every original row, including rows assigned to scratch roles, whose initial values were arbitrary.

**K.8**: Three updates $D\leftarrow D-H$, $H\leftarrow H+D$ (through the network) and $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the network.
Source: "To interchange the two full chunks, perform
\[
 D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,
\]
componentwise.  Only the middle shear uses the circuit.  The other two
updates target the later group and have linear cost.  The transformation
sends $(H,D)$ to $(D,H)$." (paper)
> To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.

**K.9**: With $F_k$ the time per unit volume at width $e=m^k$, one run of the network makes $s$ smaller interchanges, each on a stream of volume $V/W$, so $F_k\le(s/W)F_{k-1}+O(1)$ and, since $s/W<m^\tau$, $F_k=O(e^\tau)$.
How: Count the recursive calls (one per unit of edge rank, $s$ in all), divide by the current volume to get the factor $s/W$ per level, and sum the resulting geometric series over the $k=\log_m e$ levels.
- K.9.1: The number of recursive calls is the sum of the edge ranks, exactly $s$, and each acts on one role stream of volume $V/W$.
  Source: "The number of recursive calls is the sum of the edge ranks, exactly $s$.
Each acts on one role stream of volume $V/W$, retaining all other
fields as spectators." (paper)
  > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- K.9.2: If $F_k$ bounds time divided by logical volume, then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.
  Source: "F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)." (paper)
  > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- K.9.3: For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^ka^j$ is $O(m^{k\tau})$, hence $F_k=O(e^\tau)$.
  Source: "For $a=s/W<m^\tau$ the geometric sum
$\sum_{j=0}^k a^j$ is $O(m^{k\tau})$.  If $a\le1$, the sum is at
most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$.
Hence $F_k=O(e^\tau)$." (paper)
  > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.
- K.9.4: On a fixed number of tapes the $W-1$ inactive role streams are parked on a stack before a recursive call, so each node pays only an extra $O(V)$ and temporary storage is not substituted for volume in the factor $s/W$.
  Source: "Before a recursive call, append the $W-1$ inactive role streams to the
parking stack in a fixed order, with separators.  Copy the active stream
to the child I/O area, and erase the parent role tapes while traversing
their current contents." (paper)
  > Before a recursive call, append the $W-1$ inactive role streams to the parking stack in a fixed order, with separators. Copy the active stream to the child I/O area, and erase the parent role tapes while traversing their current contents. Push the parent descriptor and its finite program counter to the descriptor stack. The role and work tapes are now available to the child, using the same tapes at every depth. On return, copy the child output into the designated active role. Pop the inactive streams in reverse order. To recover a stream in its original direction, prepare its destination to the known length and write the popped symbols from the destination's right end toward its left end. Erase the popped stack cells as they are left. This uses linear time and ends with the parking head at the previously saved top. No scan passes through a parked ancestor. Cleanup is always limited to the region visited by the current call; a reused tape is not swept to the largest position ever visited by an ancestor.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- K.1 (on [Bank-exchange network with restored scratch wires](exchange-network.md)): A fixed network of $W$ wires built from three-element subsets, run in three stages, sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ and returns every scratch wire to its arbitrary initial value.
- K.2 (on [Frames on network wires](frames.md)): If every vertex carries an invertible frame $D_v$ on its array and all incidences of a pointwise linear gate share it, the gate commutes with the frame, so intermediate frames cancel and a route from input role $w$ to output role $\rho(w)$ applies only $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ with its sign.
- K.3 (on [Strict rank saving](rank-saving.md)): In the bit network the total rank $s$ of all edge changes $M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)}$ is strictly less than $Wm$, the endpoint matrices differ by the identity on every role, and consequently $s/W<m^\tau$ for $\tau=1-2^{-50}$.
- K.4 (on [Lower-triangular factorization of a matrix](matrix-factorization.md)): Every rational $m\times m$ matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones.
- K.5 (on [Cost of a matrix shear on address fields](matrix-shear.md)): For a rational $m\times m$ matrix $A$ of rank $a$ and fields over $\mathbb Z/q^b\mathbb Z$, the map $(H,D)\mapsto(H+AD,D)$ is performed with exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Controlled shifts and rational scalings](controlled-shift.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Strict rank saving](rank-saving.md): The total rank s of all edge changes in the fixed network is strictly less than W·m (wires times label dimension), which makes each recursive level cost a factor s/W < m.
  Shown as: Power-width chunk interchange *<predicate>* Strict rank saving
- [Frames on network wires](frames.md): Choosing an invertible operator D_v on the array carried by a wire at each gate, so a pointwise linear gate commutes with it and the intermediate frames cancel, leaving only the endpoint operator on every role.
  Shown as: Power-width chunk interchange *<predicate>* Frames on network wires
- [Cost of a matrix shear on address fields](matrix-shear.md): The map (H,D) ↦ (H+AD,D) over Z/q^b for a rational matrix A of rank a is done with exactly a interchanges of b-digit fields plus linear extra work.
  Shown as: Power-width chunk interchange *<predicate>* Cost of a matrix shear on address fields
- [Arrays and elementary stream operations on tape](tape-stream-operations.md): Arrays stored in lexicographic address order, with linear-time scans that split on a digit, apply a pointwise map and merge, or distribute whole rows among streams.
  Shown as: Power-width chunk interchange *<predicate>* Arrays and elementary stream operations on tape

## Pages that build on this one

- Address chunk interchange: Swapping two disjoint equal-width bit chunks of an address array in O(V u^τ) steps for a fixed τ < 1, by XOR combinations whose final effect is an exact permutation.

## Other pages you may link to

- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hh-multiplier.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Address chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Contractions and error accumulation](contraction-error.md)
- [Exact dyadic intermediates with one truncation](guard-bits.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Stored bit-reversed frequency order](bit-reversed-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancel in a convolution](permutation-cancellation.md)
- [Chinese-remainder map to prime axes](crt-axis-map.md)
- [Prime axis lengths near powers of two](prime-axis-lengths.md)
- [Parameter choice for the multiplier](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](time-bound.md)
- [Sub-n-log-n integer multiplication](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every" (paper)

  > \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

- "F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)." (paper)

  > The number of recursive calls is the sum of the edge ranks, exactly $s$. Each acts on one role stream of volume $V/W$, retaining all other fields as spectators. Splitting, merging, gates, and triangular operations have total cost $O(V)$ because their number is fixed. Below we verify that scheduling the recursive calls on fixed tapes also costs $O(V)$ at this node. Thus if $F_k$ is a uniform upper bound for time divided by logical volume, then \begin{equation} \label{eq:swap-recurrence} F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1). \end{equation} For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$; if $a>1$, it is $O(a^k)$. Hence $F_k=O(e^\tau)$.


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

Write the body to `exegenius/tasks/0014-write-power-width-interchange.answer.md` and the JSON to `exegenius/tasks/0014-write-power-width-interchange.answer.json`, then run `exegenius submit 0014-write-power-width-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0014-write-power-width-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
