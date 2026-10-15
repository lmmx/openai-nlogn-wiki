# exegenius task 0015-write-subset-intersection-labels

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WMP14` (paths below are relative to it)

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
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
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

Concept: Subspace labels from three-element subsets
Gloss: Attaching nested nondegenerate subspaces of F^{⊗3} (spanned by indicator vectors of 3-element subsets, with ⟨t_S,t_T⟩ = |S∩T|−1) to gates and terminals so that gather/scatter coefficients depend on intersection size and unwanted ones are cancelled by side wires; the total rank change of all edges is less than Wm.
Also called: rank saving construction, orthogonal residual labels

## This page in the argument

The step: Nested nondegenerate subspace labels, spanned by indicator vectors of 3-element subsets and attached to gates and terminals, give the networks total edge rank $s_{\rm b}<W_{\rm b}m$ and $s_{\rm c}<W_{\rm c}m$ because the total dimension $L$ lost on decreasing edges is $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, below $N/2$.
How: Label every vertex with a subspace of $F^{\otimes3}$ built from the indicators $t_T$ of triples, so that neighboring triples are orthogonal and labels nest along every edge; then the orthogonal residual of an edge has dimension equal to the label change, and the edge cost (its rank) equals that dimension.
Why: The sources say the saving will come from keeping the total dimension lost on decreasing edges small relative to $N$. (the sources say so: "The saving will come from keeping the total dimension lost on decreasing" (paper))
Striking feature: The dimension lost on decreasing edges is only a fraction $100/539$ (bit) or $101/539$ (complex) of $N$, below $1/2$, so total rank falls strictly below $Wm$ even after the $N$ extra source ranks. (explain why it holds, from the method)

Its sub-steps, in order:

- Bilinear spaces: $F=\mathbb Q^h$ with $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ (bit network) or $F=\mathbb F_2^h$ with the dot product (complex network); triple indicators satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$, so every triple line is nondegenerate and neighboring triple lines are orthogonal; labels live in $\mathcal F=F^{\otimes3}$ of dimension $m$ with $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$.
- Terminal labels: source $U_a$ and sink $\mathcal F$ for $X_a$, source $0$ and sink $U_a^\perp$ for $Y_a$, source $0$ and sink $\mathcal F$ for each scratch role; source dimensions sum to $N$ and sink dimensions to $Wm-N$.
- Stage transitions expose one tensor factor at a time: with $A=F^{\otimes(j-1)}$, $P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$, $B=P^\perp\subset A$, the next stage has $A'=A\otimes F$, $P'=P\otimes\langle t\rangle$, $B'=(P')^\perp_{A'}$, so outgoing labels equal the next incoming labels.
- Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to time 4 (each losing exactly $h$ dimensions), so $L=Ich$ and the sum of absolute dimension changes is $Wm-2N+2L$.
- Loss ratios: $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ (with $L=Ich$), both smaller than $1/2$; the rational interface adds only $N$ more source ranks, so a strict saving remains in both constructions.
- Bit network, rational interface: assign to each vertex the projection matrix $P_U$ onto its label (and $-P_{U_a}$ at the source of $X_a$); then $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role and the sum of rational ranks of edge differences is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.
- Complex network, binary phase interface: with frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$ ($q_U(x)=\operatorname{wt}(P_Ux)\bmod4$), each edge change factors into one two-point kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of its residual, the total count is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and after source/sink corrections every role receives $C^{\otimes m}$.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- Both tape procedures cost a power of their parameter below one, because each runs a fixed linear exchange network on $W$ wires whose edge changes are smaller calls on role streams of volume $V/W$, with total number of calls $s<Wm$, so that each level of recursion multiplies the cost per volume by $s/W<m^\tau$ while the parameter shrinks by $m$.; how: Build a finite linear exchange network that restores its scratch wires, give its vertices frames so that only endpoint operators matter, attach nested subspace labels so that the total rank $s$ of all edge changes is below $Wm$, and unroll the resulting recursion once with bit gates (address-chunk interchange) and once with Gaussian-dyadic phase gates (simultaneous butterfly layer). (on [Recursive rank saving](rank-saving-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.3.1, S4.3.2, S4.3.3, S4.3.4, S4.3.5, S4.3.6, S4.3.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.3.1**: Bilinear spaces: $F=\mathbb Q^h$ with $\langle x,y\rangle=x^{\mathsf T}(I-J/9)y$ (bit network) or $F=\mathbb F_2^h$ with the dot product (complex network); triple indicators satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$, so every triple line is nondegenerate and neighboring triple lines are orthogonal; labels live in $\mathcal F=F^{\otimes3}$ of dimension $m$ with $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$.
Source: "\langle t_S,t_T\rangle=|S\cap T|-1," (paper)
> For the bit network, let $F=\mathbb Q^h$ with bilinear form \[ \langle x,y\rangle=x^{\mathsf T}(I-J/9)y, \] where $J$ is the all-one matrix. This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate. For a triple $T$ let $t_T$ be its indicator vector. Then \[ \langle t_S,t_T\rangle=|S\cap T|-1, \qquad \langle t_T,t_T\rangle=2. \] For the complex network, take instead $F=\mathbb F_2^h$ with the ordinary dot product; here $t_T\cdot t_T=1$. Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction. The scalar domain need not equal the label field. These degree-one intersection formulas specialize the construction described by Alon~\cite[Section~3, remark after Theorem~1.1]{Alon1998} to the prime $2$, with the ground-set size changed to $h=100$.

**S4.3.2**: Terminal labels: source $U_a$ and sink $\mathcal F$ for $X_a$, source $0$ and sink $U_a^\perp$ for $Y_a$, source $0$ and sink $\mathcal F$ for each scratch role; source dimensions sum to $N$ and sink dimensions to $Wm-N$.
Source: "The source dimensions sum to $N$ and the sink dimensions to $Wm-N$." (paper)
> The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor bilinear form. It has dimension $m$ and is nondegenerate. Write \[ u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3},\qquad U_a=\langle u_a\rangle. \] The prescribed terminal labels are \[ \begin{array}{c|cc} \text{role}&\text{source label}&\text{sink label}\\ \hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{each scratch role}&0&\mathcal F. \end{array} \] Write $W$ for the wire count in the construction under consideration. The source dimensions sum to $N$ and the sink dimensions to $Wm-N$. Thus the signed dimension changes will sum to $Wm-2N$, because the contributions at gates cancel. If decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$. We will obtain $L<N/2$. The rational interface below will require an additional $N$ source ranks, so this inequality will leave a strict saving in both constructions.

**S4.3.3**: Stage transitions expose one tensor factor at a time: with $A=F^{\otimes(j-1)}$, $P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$, $B=P^\perp\subset A$, the next stage has $A'=A\otimes F$, $P'=P\otimes\langle t\rangle$, $B'=(P')^\perp_{A'}$, so outgoing labels equal the next incoming labels.
Source: "A'=A\otimes F,\qquad" (paper)
> ensor product at stage 3. Since $P$ is nondegenerate, $A=B\mathbin{\perp}P$. We prescribe the following transition for each data wire in the stage, where $t$ is the indicator of that wire's $j$th triple: \[ \begin{array}{c|c|c} &\text{incoming label}&\text{outgoing label}\\ \hline X&A\otimes\langle t\rangle\otimes Q&(A\otimes F)\otimes Q\\ Y&B\otimes\langle t\rangle\otimes Q& \bigl((B\otimes F)\mathbin{\perp}(P\otimes t^\perp)\bigr)\otimes Q. \end{array} \] The outgoing $Y$ label can also be written $(P\otimes\langle t\rangle)^\perp_{A\otimes F}\otimes Q$. These transitions expose one tensor factor at each stage. To see that they fit together, for $j<3$ write $Q=\langle t_{a_{j+1}}\rangle\otimes Q'$. The next stage has \[ A'=A\otimes F,\qquad P'=P\otimes\langle t\rangle,\qquad B'=(P')^\perp_{A'} =(B\otimes F)\mathbin{\perp}(P\otimes t^\perp). \] Thus the prescribed outgoing labels are $A'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$ on $X$ and $B'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$ on $Y$, exactly the next incoming labels. At stage 1 they start at $U_a$ on $X_a$ and zero on $Y_a$; at stage 3 they end at $\mathcal F$ on $X_a$ and $U_a^\perp$ on $Y_a$, as prescribed at the terminals.

**S4.3.4**: Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to time 4 (each losing exactly $h$ dimensions), so $L=Ich$ and the sum of absolute dimension changes is $Wm-2N+2L$.
How: Tabulate the orthogonal residual of every edge from the stage transitions and the gate-label table, observe where dimension drops, and telescope the signed changes through the gates.
- S4.3.4.1: Gate labels by time in an invocation (suppressing the factor $Q$): time 0 $B\otimes\langle t\rangle$ on $Y$ side wires, time 1 $B\otimes F$ on $Y$ and central wires, time 2 $(B\otimes F)\perp(P\otimes\langle t\rangle)$ on $X$ side wires, time 3 $A\otimes F$ on $X$ and central wires, time 4 $B\otimes F$, time 5 $(B\otimes F)\perp(P\otimes t^\perp)$, time 6 $A\otimes F$, time 7 $A\otimes F$.
  Source: "0&Y,\ \text{its side wires}&B\otimes\langle t\rangle\\" (paper)
  > \begin{equation} \begin{array}{c|l|l} \text{time}&\text{physical wires}&\text{common gate label}\\ \hline 0&Y,\ \text{its side wires}&B\otimes\langle t\rangle\\ 1&Y,\ \text{all center wires}&B\otimes F\\ 2&X,\ \text{its side wires}&(B\otimes F)\mathbin{\perp}(P\otimes\langle t\rangle)\\ 3&X,\ \text{all center wires}&A\otimes F\\ 4&Y,\ \text{all center wires}&B\otimes F\\ 5&Y,\ \text{its side wires}&(B\otimes F)\mathbin{\perp}(P\otimes t^\perp)\\ 6&X,\ \text{all center wires}&A\otimes F\\ 7&X,\ \text{its side wires}&A\otimes F. \end{array} \label{eq:motif-labels} \end{equation} All labels are tensored by $Q$ and viewed as subspaces of $\mathcal F$. Every displayed summand is nondegenerate.
- S4.3.4.2: The side edge from time 2 to time 5 uses the neighbor relation essentially: neighbors have orthogonal indicators $t_X\perp t_Y$, hence $\langle t_X\rangle\subset t_Y^\perp$ and the labels are nested, with residual $P\otimes\langle t_X,t_Y\rangle^\perp$ of dimension $h-2$.
  Source: "The side edge $2\to5$ uses the neighbor relation" (paper)
  > \ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label $(A\otimes F)\otimes Q$. Enlarging it to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses the neighbor relation essentially. Since $t_X\perp t_Y$, we have $\langle t_X\rangle\subset t_Y^\perp$. Hence its two labels satisfy \[ (B\otimes F)\mathbin{\perp}(P\otimes\langle t_X\rangle) \ \subset\ (B\otimes F)\mathbin{\perp}(P\otimes t_Y^\perp). \] The complement of $\langle t_X\rangle$ inside $t_Y^\perp$ is $\langle t_X,t_Y\rangle^\perp$, of dimension $h-2$; tensoring by $P$ and then by $Q$ gives the residual in the table. The other entries follow directly by splitting $A=B\mathbin{\perp}P$ and $F=\langle t\rangle\mathbin{\perp}t^\perp$. Label dimension is nondecreasing along every edge except center $3\to4$, which removes $P\otimes F\otimes Q$. The table includes the interstage edges through $\mathrm{in}$, and the initial
- S4.3.4.3: Label dimension is nondecreasing along every edge except the central edge $3\to4$, which removes $P\otimes F\otimes Q$, of dimension $h$; there are $Ic$ such edges ($c$ central wires per invocation), so $L=Ich$.
  Source: "Label dimension is nondecreasing along every edge except center $3\to4$, which removes" (paper)
  > to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses the neighbor relation essentially. Since $t_X\perp t_Y$, we have $\langle t_X\rangle\subset t_Y^\perp$. Hence its two labels satisfy \[ (B\otimes F)\mathbin{\perp}(P\otimes\langle t_X\rangle) \ \subset\ (B\otimes F)\mathbin{\perp}(P\otimes t_Y^\perp). \] The complement of $\langle t_X\rangle$ inside $t_Y^\perp$ is $\langle t_X,t_Y\rangle^\perp$, of dimension $h-2$; tensoring by $P$ and then by $Q$ gives the residual in the table. The other entries follow directly by splitting $A=B\mathbin{\perp}P$ and $F=\langle t\rangle\mathbin{\perp}t^\perp$. Label dimension is nondecreasing along every edge except center $3\to4$, which removes $P\otimes F\otimes Q$. The table includes the interstage edges through $\mathrm{in}$, and the initial and final data labels match their terminals, so no other dimension changes occur.
- S4.3.4.4: The signed sum of dimension changes telescopes at every gate (each touched wire has one incoming and one outgoing incidence with the same gate label); sources total $N$ and sinks $Wm-N$, so the signed increase is $Wm-2N$, and using absolute values adds $2L$.
  Source: "The signed sum of dimension changes telescopes at every gate: each" (paper)
  > The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label. The sum of source dimensions is $N$, while the sum of sink dimensions is $Wm-N$. The signed increase is therefore $Wm-2N$. There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$.
- S4.3.4.5: Over $\mathbb F_2$ every nonzero residual is nondegenerate and nonalternating (it contains a coordinate unit vector of norm one), hence has an orthonormal basis, which the complex phase interface needs.
  Source: "is nonalternating precisely when it contains a vector of norm one." (paper)
  > Now work over $\mathbb F_2$. A nondegenerate symmetric bilinear space is nonalternating precisely when it contains a vector of norm one. The lines $P,Q$ have such vectors. If $B\ne0$, a coordinate unit outside the support of the earlier tensor vector belongs to $B$: that support has size $3^{j-1}<h^{j-1}$ when $j>1$. The same argument gives a unit vector in $Q^\perp$ when it is nonzero. A triple complement, and the complement of two neighboring triple lines, contain coordinate units outside supports of sizes at most three and six, respectively. Full tensor spaces contain coordinate units as well. In each nonzero tensor summand, tensoring these chosen norm-one vectors gives a norm-one vector; placing it in that orthogonal summand gives one in the whole residual. Each residual is nondegenerate by the decompositions above. Thus every nonzero residual is nonalternating.

**S4.3.5**: Loss ratios: $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ (with $L=Ich$), both smaller than $1/2$; the rational interface adds only $N$ more source ranks, so a strict saving remains in both constructions.
Source: "\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad" (paper)
> The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.

**S4.3.6**: Bit network, rational interface: assign to each vertex the projection matrix $P_U$ onto its label (and $-P_{U_a}$ at the source of $X_a$); then $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role and the sum of rational ranks of edge differences is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.
How: Use the frame $\Phi_M:(H,D)\mapsto(H+MD,D)$ with $M_v=P_{U_v}$: the rank of $P_V-P_U$ equals the dimension change, except for the $N$ negative source projections, each costing one extra rank.
- S4.3.6.1: Endpoint identity required by the tape application: $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role $w$, so every role receives the same shear $H\gets H+D$.
  Source: "M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m" (paper)
  > \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}
- S4.3.6.2: The total rank is $s_{\rm b}=\sum_e\operatorname{rank}_{\mathbb Q}(M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})=W_{\rm b}m-N+2L_{\rm b}=177176569088785861287000000<W_{\rm b}m$.
  Source: "&=W_{\rm b}m-N+2L_{\rm b}" (paper)
  > \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}
- S4.3.6.3: For nondegenerate $U\subset V$, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$, and reversing an edge only negates it.
  Source: "$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its" (paper)
  > \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.
- S4.3.6.4: The only exceptions are the $N$ source edges: at stage 1, $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so its first edge matrix $2P_{U_a}$ has rank one although the dimension change is zero; this adds $N$ to the dimension count.
  Source: "Its first edge matrix is therefore $2P_{U_a}$, of rational rank one," (paper)
  > \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.
- S4.3.6.5: Endpoint check: for $X_a$ the difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$, and every other role has source matrix zero and sink matrix identity.
  Source: "For an input $X_a$ the endpoint difference is" (paper)
  > For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$. Every other role has zero source matrix and identity sink matrix. This proves the interface. \end{proof}

**S4.3.7**: Complex network, binary phase interface: with frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$ ($q_U(x)=\operatorname{wt}(P_Ux)\bmod4$), each edge change factors into one two-point kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of its residual, the total count is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$, and after source/sink corrections every role receives $C^{\otimes m}$.
How: Use Hamming-weight additivity modulo 4 for orthogonal vectors to turn the phase difference of an edge into a sum over residual basis vectors, each of which is a kernel $C=aI+bX$; fix up the one pair $X_a\to Y_a$ with $C=iZC^{-1}Z$.
- S4.3.7.1: Definition of the phase frame: $q_U(x)=\operatorname{wt}(P_Ux)\pmod4$ (projection over $\mathbb F_2$), with $C=H\operatorname{diag}(1,i)H=aI+bX$, $a=(1+i)/2$, $b=(1-i)/2$, and $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$ with Gaussian-dyadic entries.
  Source: "q_U(x)=\operatorname{wt}(P_Ux)\pmod4." (paper)
  > Use the complex scalar network and binary labels. For a binary vector $x$, let $\operatorname{wt}(x)$ denote its integer Hamming weight, and write $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$. For a label $U$, let \[ q_U(x)=\operatorname{wt}(P_Ux)\pmod4. \] The projection here is over $\mathbb F_2$. Let \[ H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad C=H\begin{pmatrix}1&0\\0&i\end{pmatrix}H =aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}, \] where $X$ interchanges the two coordinates. On functions of $x\in\mathbb F_2^m$ define \[ \mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}. \] The use of $H$ in this definition is an identity of matrices. Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$, so both preserve arrays over $\mathbb Z[i,1/2]$. The kernels implemented below have Gaussian dyadic coefficients.
- S4.3.7.2: The sum of residual-basis lengths over all edges is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$ (deficit $2N-2L_{\rm c}>0$).
  Source: "s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}" (paper)
  > \begin{proposition}\label{prop:complex-motif-interface} For each edge of the complex network, write $U,V$ for its tail and head labels. Its phase-frame difference $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual. Here $(X_vf)(x)=f(x+v)$. The sum of these basis lengths is \[ s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c} =1873807244636671267308000000<W_{\rm c}m. \] After source and sink diagonal corrections, and undoing the signed bank exchange, telescoping these phase frames gives $C^{\otimes m}$ on every role, including auxiliary roles. The same assertion holds on any positive number of columns by taking tensor products over columns. \end{proposition}
- S4.3.7.3: For binary $z,w$, $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$, and for $z\cdot w=0$ the intersection is even, so weight is additive modulo four.
  Source: "=\operatorname{wt}(z)+\operatorname{wt}(w)" (paper)
  > \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.
- S4.3.7.4: For $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$: $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod4$ (negated on a decreasing edge), and each $\operatorname{wt}(v)$ is odd since $v$ has norm one.
  Source: "q_V(x)-q_U(x)=\sum_{v\in\mathcal B}" (paper)
  > \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.
- S4.3.7.5: Each factor $i^{\varepsilon[v\cdot x]}$ equals $\frac{1+i^\varepsilon}{2}+\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}$, and $H\operatorname{diag}(1,-1)H=X$ turns the character $(-1)^{v\cdot x}$ into the translation $X_v$, giving the kernel $aI+bX_v$ or its inverse.
  Source: "\frac{1+i^\varepsilon}{2}" (paper)
  > \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.
- S4.3.7.6: The pair $X_a\to Y_a$ gets $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u_a)$ and $C$ elsewhere; the identity $C=iZC^{-1}Z$ (with $Z=\operatorname{diag}(1,-1)$) converts each inverse factor to $C$ using signs $Z_{a,k}$ before the network and $i^{27k}Z_{a,k}$ after it.
  Source: "C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ." (paper)
  > ero label has frame $I$, while the full label has frame $C^{\otimes m}$ because $q_{\mathcal F}(x)=\operatorname{wt}(x)$. Every pair except $X_a\to Y_a$ has these zero and full labels. For the remaining pair, write $u=u_a$. Its binary norm is one and its weight is $3^3=27$. Orthogonal weight additivity yields \begin{align*} q_{U_a^\perp}(x)-q_{U_a}(x) &=\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]\\ &=\operatorname{wt}(x)+2[u\cdot x]\pmod4. \end{align*} Since $2[u\cdot x]\equiv2\sum_{j\in\operatorname{supp}(u)}x_j \pmod4$, the operator on $X_a\to Y_a$ is the tensor of $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere. Put $Z=\operatorname{diag}(1,-1)$. Direct multiplication gives \[ C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ. \] For $k$ columns, let $Z_{a,k}$ be the tensor product of $Z$ on those 27 coordinates in every column and the identity elsewhere. Apply $Z_{a,k}$ before the network at $X_a$, and apply $i^{27k}Z_{a,k}$ after the network at $Y_a$; the latter scalar is applied once to the whole role. There are $27k$ inverse factors, so the identity $C=iZC^{-1}Z$ turns each of them into $C$. The operator on this pair is therefore $C^{\otimes mk}$ as well. Only the physical $X$ outputs still carry the minus sign of the scalar exchange. Negate those outputs and send output role $\rho(w)$ back to role $w$. Every role, including every scratch role, now has the required forward tensor product. \end{proof}
- S4.3.7.7: After negating the physical $X$ outputs and sending output role $\rho(w)$ back to $w$, every role, scratch roles included, carries the forward tensor product $C^{\otimes m}$ (and $C^{\otimes mk}$ on $k$ columns).
  Source: "Negate those outputs and send output role $\rho(w)$" (paper)
  > a$ is the tensor of $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere. Put $Z=\operatorname{diag}(1,-1)$. Direct multiplication gives \[ C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ. \] For $k$ columns, let $Z_{a,k}$ be the tensor product of $Z$ on those 27 coordinates in every column and the identity elsewhere. Apply $Z_{a,k}$ before the network at $X_a$, and apply $i^{27k}Z_{a,k}$ after the network at $Y_a$; the latter scalar is applied once to the whole role. There are $27k$ inverse factors, so the identity $C=iZC^{-1}Z$ turns each of them into $C$. The operator on this pair is therefore $C^{\otimes mk}$ as well. Only the physical $X$ outputs still carry the minus sign of the scalar exchange. Negate those outputs and send output role $\rho(w)$ back to role $w$. Every role, including every scratch role, now has the required forward tensor product. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear exchange network with restored scratch wires](linear-network.md): A fixed network of linear gates on wires (each with a role) that, for arbitrary initial scratch values, exchanges two banks of values with prescribed signs and restores every scratch wire; run in eight rows of copy, gather, scatter and side-injection steps.
  Shown as: Subspace labels from three-element subsets *<predicate>* Linear exchange network with restored scratch wires
- [Frames on wire arrays](common-frame-principle.md): Replacing each scalar by an array and giving every vertex an invertible linear operator D_v (its frame) lets pointwise gates commute with frames, so intermediate frames cancel and only the endpoint operator D_out·D_in⁻¹ is applied to each role while each edge pays only the change of frame D_v D_u⁻¹.
  Shown as: Subspace labels from three-element subsets *<predicate>* Frames on wire arrays
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md): Matrix rank, subspaces, projections, bilinear forms and the orthogonal complement of a subspace inside a larger one, including over the two-element field F₂.
  Shown as: Subspace labels from three-element subsets *<predicate>* Rank, subspaces and orthogonal complements

## Pages that build on this one

- Recursive rank saving: Running the linear network with edge changes implemented by smaller calls on role streams of volume V/W gives a cost-per-volume recurrence F_k ≤ (s/W)F_{k−1}+O(1); because the number s of smaller calls satisfies s < Wm, this yields F_k = O(e^τ) with τ<1, a power saving in the parameter.
- Phase frames and the two-point kernel C: The complex version of the network uses frames built from Hamming-weight phases i^{wt(x) mod 4}; each edge change factors into two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), so a simultaneous C-layer on e=mf axes needs s smaller layers on f axes, and H₀^{⊗D} = b^D S_D C^{⊗D} S_D.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Address shear and lower-triangular factorization](address-shear.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Fast address-chunk interchange](address-chunk-interchange.md)
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

- "three-element subsets: gather and scatter create coefficients depending" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "A label is a nondegenerate subspace of a fixed bilinear space." (paper)

  > The scalar network already has the required signed exchange. We now choose its intermediate labels to make the changes of frame inexpensive. A label is a nondegenerate subspace of a fixed bilinear space. On every edge one label will contain the other. For such an edge, the \emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one; its dimension is the absolute change in label dimension. The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.

- "\langle t_S,t_T\rangle=|S\cap T|-1," (paper)

  > For the bit network, let $F=\mathbb Q^h$ with bilinear form \[ \langle x,y\rangle=x^{\mathsf T}(I-J/9)y, \] where $J$ is the all-one matrix. This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate. For a triple $T$ let $t_T$ be its indicator vector. Then \[ \langle t_S,t_T\rangle=|S\cap T|-1, \qquad \langle t_T,t_T\rangle=2. \] For the complex network, take instead $F=\mathbb F_2^h$ with the ordinary dot product; here $t_T\cdot t_T=1$. Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction. The scalar domain need not equal the label field. These degree-one intersection formulas specialize the construction described by Alon~\cite[Section~3, remark after Theorem~1.1]{Alon1998} to the prime $2$, with the ground-set size changed to $h=100$.


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

Write the body to `exegenius/tasks/0015-write-subset-intersection-labels.answer.md` and the JSON to `exegenius/tasks/0015-write-subset-intersection-labels.answer.json`, then run `exegenius submit 0015-write-subset-intersection-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0015-write-subset-intersection-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
