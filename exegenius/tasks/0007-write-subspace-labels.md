# exegenius task 0007-write-subspace-labels

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
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

Concept: Nested subspace labels and rank deficit
Gloss: Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m.
Also called: rank saving

## This page in the argument

The step: Attaching to the gates nondegenerate subspaces of an $m$-dimensional space, nested along every edge, the number of smaller calls (the total rank of the edge changes) is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ for the bit network and $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ for the complex network, both strictly less than $Wm$, because $L/N<1/2$.
How: Choose labels in $\mathcal F=F^{\otimes3}$ built from the triple indicator vectors, with terminal labels $U_a\to\mathcal F$ on $X_a$ and $0\to U_a^\perp$ on $Y_a$; expose one tensor factor per stage; tabulate dimension changes edge by edge to find that all decreases are the central wires' return from time 3 to 4; then convert the dimension count into rational rank (bit) and Gaussian-dyadic phase kernels (complex).
Why: Total dimension is conserved by telescoping at gates, so the sum of changes is fixed by the terminal labels; the saving is whatever the unavoidable decreases $L$ leave of the budget $N$, so the labels are designed to confine every decrease to one small edge. (the sources say so: "The saving will come from keeping the total dimension lost on decreasing" (paper))
Striking feature: The saving is minuscule but strictly positive: $s_{\rm b}/W_{\rm b}=m(1-\eta_{\rm b})$ with relative deficit $\eta_{\rm b}=339/22587335000000\approx1.5\cdot10^{-11}$, because $L_{\rm b}/N=100/539<1/2$. (explain why it holds, from the method)

Its sub-steps, in order:

- Over $F=\mathbb Q^h$ (form $x^{\mathsf T}(I-J/9)y$) for the bit network, and $F=\mathbb F_2^h$ (dot product) for the complex one, the triple indicators satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$, so every triple line is nondegenerate and neighbouring triple lines are orthogonal.
- The terminal labels fix the budget: the source dimensions sum to $N$ and the sink dimensions to $Wm-N$.
- Hence the signed dimension changes sum to $Wm-2N$ because the contributions at gates cancel.
- Writing $A=F^{\otimes(j-1)}$, $P$ the span of the earlier tensor factors, $B=P^\perp$ in $A$, the outgoing labels of stage $j$ are exactly the incoming labels of stage $j+1$, with $A'=A\otimes F$.
- The gate order confines all decreases to the single return of each central wire from label $A\otimes F$ to $B\otimes F$, losing exactly $P\otimes F$ of dimension $h$.
- Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to time 4 (each losing dimension $h$), so $L=Ic\,h$ and the sum of absolute dimension changes is $Wm-2N+2L$.
- The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.
- Bit network: assigning the projection $P_U$ to each vertex with label $U$ and $-P_{U_a}$ to the source of $X_a$ gives endpoint difference $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ on every input role, and total rational rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.
- Complex network: with binary labels and the phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$, every edge difference is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual; the total number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ and, after endpoint corrections, the network applies $C^{\otimes m}$ on every role. (on [Binary phase frames](phase-frames.md))

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.; how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). (on [Recursive power saving](rank-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.3.1, S1.3.2, S1.3.3, S1.3.4, S1.3.5, S1.3.6, S1.3.9, S1.3.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.3.1**: Over $F=\mathbb Q^h$ (form $x^{\mathsf T}(I-J/9)y$) for the bit network, and $F=\mathbb F_2^h$ (dot product) for the complex one, the triple indicators satisfy $\langle t_S,t_T\rangle=|S\cap T|-1$, so every triple line is nondegenerate and neighbouring triple lines are orthogonal.
Source: "\langle t_S,t_T\rangle=|S\cap T|-1," (paper)
> For the bit network, let $F=\mathbb Q^h$ with bilinear form \[ \langle x,y\rangle=x^{\mathsf T}(I-J/9)y, \] where $J$ is the all-one matrix. This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate. For a triple $T$ let $t_T$ be its indicator vector. Then \[ \langle t_S,t_T\rangle=|S\cap T|-1, \qquad \langle t_T,t_T\rangle=2. \] For the complex network, take instead $F=\mathbb F_2^h$ with the ordinary dot product; here $t_T\cdot t_T=1$. Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction. The scalar domain need not equal the label field. These degree-one intersection formulas specialize the construction described by Alon~\cite[Section~3, remark after Theorem~1.1]{Alon1998} to the prime $2$, with the ground-set size changed to $h=100$.

**S1.3.2**: The terminal labels fix the budget: the source dimensions sum to $N$ and the sink dimensions to $Wm-N$.
Source: "The source dimensions sum to $N$ and the sink dimensions to $Wm-N$." (paper)
> The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor bilinear form. It has dimension $m$ and is nondegenerate. Write \[ u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3},\qquad U_a=\langle u_a\rangle. \] The prescribed terminal labels are \[ \begin{array}{c|cc} \text{role}&\text{source label}&\text{sink label}\\ \hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{each scratch role}&0&\mathcal F. \end{array} \] Write $W$ for the wire count in the construction under consideration. The source dimensions sum to $N$ and the sink dimensions to $Wm-N$. Thus the signed dimension changes will sum to $Wm-2N$, because the contributions at gates cancel. If decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$. We will obtain $L<N/2$. The rational interface below will require an additional $N$ source ranks, so this inequality will leave a strict saving in both constructions.

**S1.3.3**: Hence the signed dimension changes sum to $Wm-2N$ because the contributions at gates cancel.
Source: "Thus the signed dimension changes will sum to $Wm-2N$, because the" (paper)
> The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor bilinear form. It has dimension $m$ and is nondegenerate. Write \[ u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3},\qquad U_a=\langle u_a\rangle. \] The prescribed terminal labels are \[ \begin{array}{c|cc} \text{role}&\text{source label}&\text{sink label}\\ \hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{each scratch role}&0&\mathcal F. \end{array} \] Write $W$ for the wire count in the construction under consideration. The source dimensions sum to $N$ and the sink dimensions to $Wm-N$. Thus the signed dimension changes will sum to $Wm-2N$, because the contributions at gates cancel. If decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$. We will obtain $L<N/2$. The rational interface below will require an additional $N$ source ranks, so this inequality will leave a strict saving in both constructions.

**S1.3.4**: Writing $A=F^{\otimes(j-1)}$, $P$ the span of the earlier tensor factors, $B=P^\perp$ in $A$, the outgoing labels of stage $j$ are exactly the incoming labels of stage $j+1$, with $A'=A\otimes F$.
Source: "A'=A\otimes F,\qquad" (paper)
> ensor product at stage 3. Since $P$ is nondegenerate, $A=B\mathbin{\perp}P$. We prescribe the following transition for each data wire in the stage, where $t$ is the indicator of that wire's $j$th triple: \[ \begin{array}{c|c|c} &\text{incoming label}&\text{outgoing label}\\ \hline X&A\otimes\langle t\rangle\otimes Q&(A\otimes F)\otimes Q\\ Y&B\otimes\langle t\rangle\otimes Q& \bigl((B\otimes F)\mathbin{\perp}(P\otimes t^\perp)\bigr)\otimes Q. \end{array} \] The outgoing $Y$ label can also be written $(P\otimes\langle t\rangle)^\perp_{A\otimes F}\otimes Q$. These transitions expose one tensor factor at each stage. To see that they fit together, for $j<3$ write $Q=\langle t_{a_{j+1}}\rangle\otimes Q'$. The next stage has \[ A'=A\otimes F,\qquad P'=P\otimes\langle t\rangle,\qquad B'=(P')^\perp_{A'} =(B\otimes F)\mathbin{\perp}(P\otimes t^\perp). \] Thus the prescribed outgoing labels are $A'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$ on $X$ and $B'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$ on $Y$, exactly the next incoming labels. At stage 1 they start at $U_a$ on $X_a$ and zero on $Y_a$; at stage 3 they end at $\mathcal F$ on $X_a$ and $U_a^\perp$ on $Y_a$, as prescribed at the terminals.

**S1.3.5**: The gate order confines all decreases to the single return of each central wire from label $A\otimes F$ to $B\otimes F$, losing exactly $P\otimes F$ of dimension $h$.
Source: "$P\otimes F$. The gate order below confines all decreases to this" (paper)
> The gate labels are organized by the decomposition \[ A\otimes F=(B\otimes F)\mathbin{\perp}(P\otimes F), \] with the common summand $B\otimes F$ and the remaining summand $P\otimes F$ of dimension $h$. Suppress the one-dimensional factor $Q$ for the moment. On a side wire joining neighboring physical triples with indicators $t_X,t_Y$, the common component grows to $B\otimes F$, while the remaining component passes through \[ P\otimes\langle t_X\rangle \ \subset\ P\otimes t_Y^\perp \ \subset\ P\otimes F. \] The first inclusion is possible because $t_X\perp t_Y$. For the central gates we assign $A\otimes F$ on the physical $X$ bank and $B\otimes F$ on the physical $Y$ bank. A central wire returns once from the former label to the latter, losing exactly $P\otimes F$. The gate order below confines all decreases to this return, while the other edges realize the prescribed stage transitions.

**S1.3.6**: Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to time 4 (each losing dimension $h$), so $L=Ic\,h$ and the sum of absolute dimension changes is $Wm-2N+2L$.
How: Tabulate the orthogonal residual of every edge type of the gate schedule and its dimension, observe that dimension is nondecreasing except on centre wires from time 3 to 4, then sum signed changes by telescoping at each gate and convert signed to absolute changes.
- S1.3.6.1: The residuals are tabulated per edge type, with $a=\dim A=h^{j-1}$ and $f=h^{3-j}$; the claim is that the loss on decreasing edges totals $L=Ich$.
  Source: "L=Ich,\qquad" (paper)
  > \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}
- S1.3.6.2: Data wire $X$, edge in$\to$2: residual $B\otimes t_X^\perp$, dimension $(a-1)(h-1)$ (the $X$ edges 2$\to$3 add $P\otimes t_X^\perp$ of dimension $h-1$, and 3$\to$6, 6$\to$7 add nothing).
  Source: "X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\" (paper)
  > \begin{proof} Write $a=\dim A=h^{j-1}$ and $f=h^{3-j}$. In the table below, $\mathrm{in}$ denotes the preceding vertex on that data wire: its source at stage 1, and its last gate in the preceding stage otherwise. The interstage calculation above gives its label. The table lists the orthogonal residual and its dimension for every edge except the final data edges to their sinks, whose labels agree and whose residuals are zero. Tensor each residual by $Q$, except in the last row. The symbols $t_X,t_Y$ are the indicators of the neighboring physical triples joined by a side wire. \[ \begin{array}{l|l|r} \text{wire and edge}&\text{orthogonal residual}&\text{dimension}\\ \hline X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\ X:\ 2\to3&P\otimes t_X^\perp&h-1\\ X:\ 3\to6,\ 6\to7&0&0\\ Y:\ \mathrm{in}\to0&0&0\\ Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\ Y:\ 1\to4&0&0\\ Y:\ 4\to5&P\otimes t_Y^\perp&h-1\\ \mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\ \mathrm{center}:\ 1\to3&P\otimes F&h\\ \mathrm{center}:\ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&a
- S1.3.6.3: Data wire $Y$, edge 0$\to$1: residual $B\otimes t_Y^\perp$, dimension $(a-1)(h-1)$ (in$\to$0 and 1$\to$4 add nothing, 4$\to$5 adds $P\otimes t_Y^\perp$ of dimension $h-1$).
  Source: "Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\" (paper)
  > enotes the preceding vertex on that data wire: its source at stage 1, and its last gate in the preceding stage otherwise. The interstage calculation above gives its label. The table lists the orthogonal residual and its dimension for every edge except the final data edges to their sinks, whose labels agree and whose residuals are zero. Tensor each residual by $Q$, except in the last row. The symbols $t_X,t_Y$ are the indicators of the neighboring physical triples joined by a side wire. \[ \begin{array}{l|l|r} \text{wire and edge}&\text{orthogonal residual}&\text{dimension}\\ \hline X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\ X:\ 2\to3&P\otimes t_X^\perp&h-1\\ X:\ 3\to6,\ 6\to7&0&0\\ Y:\ \mathrm{in}\to0&0&0\\ Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\ Y:\ 1\to4&0&0\\ Y:\ 4\to5&P\otimes t_Y^\perp&h-1\\ \mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\ \mathrm{center}:\ 1\to3&P\otimes F&h\\ \mathrm{center}:\ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label
- S1.3.6.4: Centre wire, edge source$\to$1: residual $B\otimes F$, dimension $(a-1)h$ (increasing).
  Source: "\mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\" (paper)
  > ing stage otherwise. The interstage calculation above gives its label. The table lists the orthogonal residual and its dimension for every edge except the final data edges to their sinks, whose labels agree and whose residuals are zero. Tensor each residual by $Q$, except in the last row. The symbols $t_X,t_Y$ are the indicators of the neighboring physical triples joined by a side wire. \[ \begin{array}{l|l|r} \text{wire and edge}&\text{orthogonal residual}&\text{dimension}\\ \hline X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\ X:\ 2\to3&P\otimes t_X^\perp&h-1\\ X:\ 3\to6,\ 6\to7&0&0\\ Y:\ \mathrm{in}\to0&0&0\\ Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\ Y:\ 1\to4&0&0\\ Y:\ 4\to5&P\otimes t_Y^\perp&h-1\\ \mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\ \mathrm{center}:\ 1\to3&P\otimes F&h\\ \mathrm{center}:\ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label $(A\otimes F)\otimes Q$. Enlarging it to $\mathcal F$ at the sink gives the last residual in the ta
- S1.3.6.5: Centre wire, edge 3$\to$4: residual $P\otimes F$ of dimension $h$, the only decreasing edge (edges 1$\to$3 and 4$\to$6 also have residual $P\otimes F$ but are increasing).
  Source: "\mathrm{center}:\ 3\to4&P\otimes F&h\\" (paper)
  > s the orthogonal residual and its dimension for every edge except the final data edges to their sinks, whose labels agree and whose residuals are zero. Tensor each residual by $Q$, except in the last row. The symbols $t_X,t_Y$ are the indicators of the neighboring physical triples joined by a side wire. \[ \begin{array}{l|l|r} \text{wire and edge}&\text{orthogonal residual}&\text{dimension}\\ \hline X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\ X:\ 2\to3&P\otimes t_X^\perp&h-1\\ X:\ 3\to6,\ 6\to7&0&0\\ Y:\ \mathrm{in}\to0&0&0\\ Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\ Y:\ 1\to4&0&0\\ Y:\ 4\to5&P\otimes t_Y^\perp&h-1\\ \mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\ \mathrm{center}:\ 1\to3&P\otimes F&h\\ \mathrm{center}:\ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label $(A\otimes F)\otimes Q$. Enlarging it to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses
- S1.3.6.6: Side wire, edge source$\to$0: residual $B\otimes\langle t_Y\rangle$, dimension $a-1$ (edge 0$\to$2 adds $(a-1)(h-1)+1$).
  Source: "\mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\" (paper)
  > ir sinks, whose labels agree and whose residuals are zero. Tensor each residual by $Q$, except in the last row. The symbols $t_X,t_Y$ are the indicators of the neighboring physical triples joined by a side wire. \[ \begin{array}{l|l|r} \text{wire and edge}&\text{orthogonal residual}&\text{dimension}\\ \hline X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\ X:\ 2\to3&P\otimes t_X^\perp&h-1\\ X:\ 3\to6,\ 6\to7&0&0\\ Y:\ \mathrm{in}\to0&0&0\\ Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\ Y:\ 1\to4&0&0\\ Y:\ 4\to5&P\otimes t_Y^\perp&h-1\\ \mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\ \mathrm{center}:\ 1\to3&P\otimes F&h\\ \mathrm{center}:\ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label $(A\otimes F)\otimes Q$. Enlarging it to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses the neighbor relation essentially. Since $t_X\perp t_Y$, we have $\langle t_X\rangle\subset
- S1.3.6.7: Side wire, edge 2$\to$5: residual $P\otimes\langle t_X,t_Y\rangle^\perp$, dimension $h-2$ (edge 5$\to$7 adds $P\otimes\langle t_Y\rangle$ of dimension $1$).
  Source: "\mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\" (paper)
  > ng physical triples joined by a side wire. \[ \begin{array}{l|l|r} \text{wire and edge}&\text{orthogonal residual}&\text{dimension}\\ \hline X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\ X:\ 2\to3&P\otimes t_X^\perp&h-1\\ X:\ 3\to6,\ 6\to7&0&0\\ Y:\ \mathrm{in}\to0&0&0\\ Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\ Y:\ 1\to4&0&0\\ Y:\ 4\to5&P\otimes t_Y^\perp&h-1\\ \mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\ \mathrm{center}:\ 1\to3&P\otimes F&h\\ \mathrm{center}:\ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label $(A\otimes F)\otimes Q$. Enlarging it to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses the neighbor relation essentially. Since $t_X\perp t_Y$, we have $\langle t_X\rangle\subset t_Y^\perp$. Hence its two labels satisfy \[ (B\otimes F)\mathbin{\perp}(P\otimes\langle t_X\rangle) \ \subset\ (B\otimes F)\mathbin{\perp}(P\otimes t_Y^\perp). \] The
- S1.3.6.8: Scratch role, last gate$\to$sink: residual $(A\otimes F)\otimes Q^\perp$, dimension $ah(f-1)$ (increasing, enlarging the label to $\mathcal F$).
  Source: "\mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink}" (paper)
  > ual}&\text{dimension}\\ \hline X:\ \mathrm{in}\to2&B\otimes t_X^\perp&(a-1)(h-1)\\ X:\ 2\to3&P\otimes t_X^\perp&h-1\\ X:\ 3\to6,\ 6\to7&0&0\\ Y:\ \mathrm{in}\to0&0&0\\ Y:\ 0\to1&B\otimes t_Y^\perp&(a-1)(h-1)\\ Y:\ 1\to4&0&0\\ Y:\ 4\to5&P\otimes t_Y^\perp&h-1\\ \mathrm{center}:\ \mathrm{source}\to1&B\otimes F&(a-1)h\\ \mathrm{center}:\ 1\to3&P\otimes F&h\\ \mathrm{center}:\ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label $(A\otimes F)\otimes Q$. Enlarging it to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses the neighbor relation essentially. Since $t_X\perp t_Y$, we have $\langle t_X\rangle\subset t_Y^\perp$. Hence its two labels satisfy \[ (B\otimes F)\mathbin{\perp}(P\otimes\langle t_X\rangle) \ \subset\ (B\otimes F)\mathbin{\perp}(P\otimes t_Y^\perp). \] The complement of $\langle t_X\rangle$ inside $t_Y^\perp$ is $\langle t_X,t_Y\rangle^\perp$, of dimension $h-2$;
- S1.3.6.9: The side edge 2$\to$5 is comparable only because neighbouring triples are orthogonal: $t_X\perp t_Y$ gives $\langle t_X\rangle\subset t_Y^\perp$.
  Source: "The side edge $2\to5$ uses the neighbor relation" (paper)
  > \ 3\to4&P\otimes F&h\\ \mathrm{center}:\ 4\to6&P\otimes F&h\\ \mathrm{side}:\ \mathrm{source}\to0&B\otimes\langle t_Y\rangle&a-1\\ \mathrm{side}:\ 0\to2&(B\otimes t_Y^\perp)\mathbin{\perp}(P\otimes\langle t_X\rangle) &(a-1)(h-1)+1\\ \mathrm{side}:\ 2\to5&P\otimes\langle t_X,t_Y\rangle^\perp&h-2\\ \mathrm{side}:\ 5\to7&P\otimes\langle t_Y\rangle&1\\ \mathrm{scratch}:\ \mathrm{last}\to\mathrm{sink} &(A\otimes F)\otimes Q^\perp&ah(f-1). \end{array} \] The last gate on a central wire is at time 6, and the last gate on a side wire is at time 7. Both have label $(A\otimes F)\otimes Q$. Enlarging it to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses the neighbor relation essentially. Since $t_X\perp t_Y$, we have $\langle t_X\rangle\subset t_Y^\perp$. Hence its two labels satisfy \[ (B\otimes F)\mathbin{\perp}(P\otimes\langle t_X\rangle) \ \subset\ (B\otimes F)\mathbin{\perp}(P\otimes t_Y^\perp). \] The complement of $\langle t_X\rangle$ inside $t_Y^\perp$ is $\langle t_X,t_Y\rangle^\perp$, of dimension $h-2$; tensoring by $P$ and then by $Q$ gives the residual in the table. The other entries follow directly by splitting $A=B\mathbin{\perp}P$ and $F=\langle t\rangle\mathbin{\perp}t^\perp$. Label dimension is nondecreasing along every edge except center $3\to4$, which removes $P\otimes F\otimes Q$. The table includes the interstage edges through $\mathrm{in}$, and the initial
- S1.3.6.10: Label dimension is nondecreasing along every edge except centre 3$\to$4, which removes $P\otimes F\otimes Q$.
  Source: "Label dimension is nondecreasing along every edge except center $3\to4$, which removes" (paper)
  > to $\mathcal F$ at the sink gives the last residual in the table, with $Q^\perp$ taken in the entire future tensor space. The side edge $2\to5$ uses the neighbor relation essentially. Since $t_X\perp t_Y$, we have $\langle t_X\rangle\subset t_Y^\perp$. Hence its two labels satisfy \[ (B\otimes F)\mathbin{\perp}(P\otimes\langle t_X\rangle) \ \subset\ (B\otimes F)\mathbin{\perp}(P\otimes t_Y^\perp). \] The complement of $\langle t_X\rangle$ inside $t_Y^\perp$ is $\langle t_X,t_Y\rangle^\perp$, of dimension $h-2$; tensoring by $P$ and then by $Q$ gives the residual in the table. The other entries follow directly by splitting $A=B\mathbin{\perp}P$ and $F=\langle t\rangle\mathbin{\perp}t^\perp$. Label dimension is nondecreasing along every edge except center $3\to4$, which removes $P\otimes F\otimes Q$. The table includes the interstage edges through $\mathrm{in}$, and the initial and final data labels match their terminals, so no other dimension changes occur.
- S1.3.6.11: The signed sum of dimension changes telescopes at every gate (each touched wire enters and leaves with the same gate label), so it equals the sink total $Wm-N$ minus the source total $N$, namely $Wm-2N$.
  Source: "The signed sum of dimension changes telescopes at every gate: each" (paper)
  > The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label. The sum of source dimensions is $N$, while the sum of sink dimensions is $Wm-N$. The signed increase is therefore $Wm-2N$. There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$.
- S1.3.6.12: There are $Ic$ decreasing edges each of loss $h$, so $L=Ich$; replacing signed changes by absolute changes adds $2L$, giving $Wm-2N+2L$.
  Source: "There are $Ic$ decreasing edges, each of loss $h$; replacing signed" (paper)
  > The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label. The sum of source dimensions is $N$, while the sum of sink dimensions is $Wm-N$. The signed increase is therefore $Wm-2N$. There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$.
- S1.3.6.13: Over $\mathbb F_2$ every nonzero residual is nondegenerate and contains a norm-one vector, hence is nonalternating.
  Source: "Thus every nonzero residual is nonalternating." (paper)
  > Now work over $\mathbb F_2$. A nondegenerate symmetric bilinear space is nonalternating precisely when it contains a vector of norm one. The lines $P,Q$ have such vectors. If $B\ne0$, a coordinate unit outside the support of the earlier tensor vector belongs to $B$: that support has size $3^{j-1}<h^{j-1}$ when $j>1$. The same argument gives a unit vector in $Q^\perp$ when it is nonzero. A triple complement, and the complement of two neighboring triple lines, contain coordinate units outside supports of sizes at most three and six, respectively. Full tensor spaces contain coordinate units as well. In each nonzero tensor summand, tensoring these chosen norm-one vectors gives a norm-one vector; placing it in that orthogonal summand gives one in the whole residual. Each residual is nondegenerate by the decompositions above. Thus every nonzero residual is nonalternating.
- S1.3.6.14: Every nondegenerate nonalternating binary symmetric space has an orthonormal basis (split off unit lines, then absorb alternating planes using $w+a$, $w+b$, $w+a+b$); so every nonzero residual of the binary label space has an orthonormal basis.
  Source: "For completeness, every nondegenerate nonalternating binary symmetric" (paper)
  > For completeness, every nondegenerate nonalternating binary symmetric space has an orthonormal basis. Split off unit lines until the remaining space is alternating. A nonzero nondegenerate alternating space splits into planes with bases $a,b$ satisfying $a\cdot a=b\cdot b=0$, $a\cdot b=1$; this follows by choosing a nonzero $a$, choosing $b$ with $a\cdot b=1$, and taking the orthogonal complement of their nondegenerate plane. Retain one unit vector $w$ from the lines already split off. A plane orthogonal to $w$ can be absorbed into that line: the three vectors \[ w+a,\qquad w+b,\qquad w+a+b \] are independent, pairwise orthogonal, and have norm one. Use one of these new unit vectors in place of $w$ for the next plane; the remaining planes are still orthogonal to it. Repeating this operation absorbs every alternating plane. \end{proof}

**S1.3.9**: The loss ratios are exactly $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.
Source: "\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad" (paper)
> The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.

**S1.3.7**: Bit network: assigning the projection $P_U$ to each vertex with label $U$ and $-P_{U_a}$ to the source of $X_a$ gives endpoint difference $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ on every input role, and total rational rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$.
How: Use projections along the labels as the rational frames: an edge between nested labels changes the matrix by a projection difference of rank equal to the dimension change, except at the $N$ negative source projections, which cost one extra rank each.
- S1.3.7.1: Assign the matrix $P_U$ (projection onto $U$ along $U^\perp$) to each gate or sink with label $U$ and the matrix $-P_{U_a}$ to the source of $X_a$; every other source gets zero.
  Source: "each gate or sink with label $U$.  Assign the source matrix $-P_{U_a}$" (paper)
  > For a nondegenerate rational subspace $U\subset\mathcal F$, write $P_U$ for the projection onto $U$ along $U^\perp$. Assign $P_U$ to each gate or sink with label $U$. Assign the source matrix $-P_{U_a}$ to $X_a$ and zero to every other source. These are fixed rational $m\times m$ matrices; write $M_v$ for the matrix at vertex $v$. Define $\rho(X_a)=Y_a$, $\rho(Y_a)=X_a$, and let $\rho$ fix every auxiliary wire.
- S1.3.7.2: The required endpoint identity is $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role $w$.
  Source: "M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m" (paper)
  > \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}
- S1.3.7.3: The total rank is $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$.
  Source: "=W_{\rm b}m-N+2L_{\rm b}" (paper)
  > \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}
- S1.3.7.9: Numerically $s_{\rm b}=177176569088785861287000000<W_{\rm b}m$.
  Source: "=177176569088785861287000000<W_{\rm b}m." (paper)
  > \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}
- S1.3.7.4: For nondegenerate $U\subset V$ the difference $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement, so its rank is $\dim V-\dim U$ and reversing the edge does not change it.
  Source: "$P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its" (paper)
  > \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.
- S1.3.7.5: The only exceptions to rank equal to dimension change are the $N$ negative source projections.
  Source: "The only exceptions are the $N$ negative source projections." (paper)
  > \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.
- S1.3.7.6: At stage 1, $B=0$ and the first gate on $X_a$ has label exactly $U_a$, so the first edge matrix is $2P_{U_a}$, of rational rank one where the dimension change is zero.
  Source: "Its first edge matrix is therefore $2P_{U_a}$, of rational rank one," (paper)
  > \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.
- S1.3.7.7: Hence the deficit of $s_{\rm b}$ from $W_{\rm b}m$ is $N-2L_{\rm b}>0$, because $L_{\rm b}/N<1/2$.
  Source: "Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$." (paper)
  > \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.
- S1.3.7.8: For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$; every other role has zero source matrix and identity sink matrix.
  Source: "For an input $X_a$ the endpoint difference is" (paper)
  > For an input $X_a$ the endpoint difference is $P_{U_a^\perp}-(-P_{U_a})=I_m$. Every other role has zero source matrix and identity sink matrix. This proves the interface. \end{proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.3.8 (on [Binary phase frames](phase-frames.md)): Complex network: with binary labels and the phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$, every edge difference is a product of one translation kernel $aI+bX_v$ (or its inverse) per vector of an orthonormal basis of the edge residual; the total number of kernels is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ and, after endpoint corrections, the network applies $C^{\otimes m}$ on every role.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Frames on wire arrays](array-frames.md): Replacing each wire scalar by an array and assigning an invertible operator D_v (a frame) at each gate so the pointwise gate commutes with the frame and only the endpoint frames matter.
  Shown as: Nested subspace labels and rank deficit *<predicate>* Frames on wire arrays

## Pages that build on this one

- Recursive power saving: Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving.
- Binary phase frames: Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} whose edge differences are products of translation kernels aI + bX_v, one per vector of an orthonormal residual basis.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Recursive power saving](rank-recurrence.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition](packed-bit-addition.md)
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

- "The subspaces at adjacent vertices are nested." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "The decisive property is that the total" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


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

Write the body to `exegenius/tasks/0007-write-subspace-labels.answer.md` and the JSON to `exegenius/tasks/0007-write-subspace-labels.answer.json`, then run `exegenius submit 0007-write-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0007-write-subspace-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
