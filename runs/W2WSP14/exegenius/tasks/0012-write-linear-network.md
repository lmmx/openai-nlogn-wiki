# exegenius task 0012-write-linear-network

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

Concept: Linear exchange network with restored scratch wires
Gloss: A fixed network of linear gates on wires (each with a role) that, for arbitrary initial scratch values, exchanges two banks of values with prescribed signs and restores every scratch wire; run in eight rows of copy, gather, scatter and side-injection steps.
Also called: bank exchange, finite network, role

## This page in the argument

The step: A fixed linear network on $W$ wires, built from three stages of an eight-row schedule per invocation, sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$ (a pure exchange of the two data banks over $\mathbb F_2$) and restores every scratch wire, whatever its initial value.
How: Give each invocation copy, gather, scatter and side-injection gates whose net effect on a target is $y_S\gets y_S+x_S$ independent of the scratch values (subtract the old scratch effect, add the new one, undo it), then chain three such updates $y\gets y+x$, $x\gets x-y$, $y\gets y+x$ to exchange the banks.
Why: The sources say the schedule first cancels the arbitrary old scratch values, then adds the source values' effect, then restores the scratch values. (the sources say so: "the following schedule remove the effect of the old scratch values;" (paper))

Its sub-steps, in order:

- Fixed constants of the construction: ground set size $h=100$, number of 3-subsets $v=\binom h3=161700$, number of index triples $N=v^3=4227952113000000$, label-space dimension $m=h^3=1000000$.
- The three stages (one per coordinate $j$ of $a\in\mathcal T^3$) comprise $I=3v^2=78440670000$ invocations, each with its own scratch wires, so that each invocation updates $v$ values of a bank at a time.
- Bit construction over $\mathbb F_2$: triples $S,T$ are neighbors when $|S\cap T|=1$; copy adds $x_T$ to the scratch wire $A_{ST}$, side injection adds $\sum_{T:|S\cap T|=1}A_{ST}$ to $y_S$, gather adds $\sum_{T\ni i}x_T$ to a central wire $C_i$ and scatter adds $\sum_{i\in S}C_i$ to $y_S$.
- Complex construction over $\mathbb Z[i,1/2]$: neighbors are distinct triples with even intersection, the side injection has coefficient $-(|S\cap T|-1)/2$, and an extra central wire $C_\ast$ makes the scatter add $(\sum_{i\in S}C_i-C_\ast)/2$.
- The eight-row forward schedule is: subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy; the first two rows remove the effect of the old scratch values and the last two restore them.
- The net change of the target is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ (side injection times copy plus scatter times gather), independent of the initial scratch values $a,c$, because rows 0-1 subtract exactly the old contribution.
- Bit case: the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$; the side injection cancels the intersection-one cases, intersection zero or two already give zero, and the self coefficient is one, so the net map is $y\gets y+x$.
- Complex case: the central coefficient is $(|S\cap T|-1)/2$; the side wires cancel it for distinct triples with intersection zero or two, intersection one contributes zero, and the self coefficient is one, so again the net map is $y\gets y+x$.
- Three stages starting from $(x,y)$ give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$: the signed exchange $(X_a,Y_a)\mapsto(-Y_a,X_a)$, with every invocation restoring its own scratch wires.
- Wire counts: a triple has $z_{\rm b}=3\binom{97}{2}=13968$ bit-neighbors and $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ complex neighbors, with $c_{\rm b}=100$, $c_{\rm c}=101$ central wires per invocation, giving $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ and $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- Both tape procedures cost a power of their parameter below one, because each runs a fixed linear exchange network on $W$ wires whose edge changes are smaller calls on role streams of volume $V/W$, with total number of calls $s<Wm$, so that each level of recursion multiplies the cost per volume by $s/W<m^\tau$ while the parameter shrinks by $m$.; how: Build a finite linear exchange network that restores its scratch wires, give its vertices frames so that only endpoint operators matter, attach nested subspace labels so that the total rank $s$ of all edge changes is below $Wm$, and unroll the resulting recursion once with bit gates (address-chunk interchange) and once with Gaussian-dyadic phase gates (simultaneous butterfly layer). (on [Recursive rank saving](rank-saving-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.1.1, S4.1.2, S4.1.3, S4.1.4, S4.1.5, S4.1.6, S4.1.7, S4.1.8, S4.1.9, S4.1.10). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.1.1**: Fixed constants of the construction: ground set size $h=100$, number of 3-subsets $v=\binom h3=161700$, number of index triples $N=v^3=4227952113000000$, label-space dimension $m=h^3=1000000$.
Source: "h=100,\qquad v=\binom h3=161700,\qquad" (paper)
> Put \[ h=100,\qquad v=\binom h3=161700,\qquad N=v^3=4227952113000000,\qquad m=h^3=1000000. \] Let $\mathcal T$ be the set of three-element subsets of $[h]$. There are two data banks $X_a,Y_a$, indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. A wire carries one scalar. A gate is a fixed linear map on a specified set of wires; untouched wires retain their values. The vertices on a wire are its source, the gates that touch it in time order, and its sink; its edges join consecutive vertices. We call the name of a wire its \emph{role}, so that we can distinguish a fixed place in the network from the value currently carried there.

**S4.1.2**: The three stages (one per coordinate $j$ of $a\in\mathcal T^3$) comprise $I=3v^2=78440670000$ invocations, each with its own scratch wires, so that each invocation updates $v$ values of a bank at a time.
Source: "I=3v^2=78440670000" (paper)
> There are three stages. At stage $j$, fix the other two coordinates and operate on the $v$ values in each bank obtained by varying coordinate $j$. Thus there are $v^2$ separate invocations at each stage. Each such invocation has its own auxiliary wires, distinct from all other invocations, including those in other stages. There are \[ I=3v^2=78440670000 \] invocations. In a forward invocation, write $x_T$ for the data used as controls and $y_S$ for the data to be updated; $S,T\in\mathcal T$ are their varying $j$th coordinates. These are the logical source and target banks of the invocation. For each ordered pair $(S,T)$ that is neighboring under the rule below, there is an auxiliary wire $A_{ST}$. There are also central wires $C_i$, $i\in[h]$, and in the second construction a wire $C_\ast$. We call all these auxiliary wires \emph{scratch wires}; their initial values may be arbitrary.

**S4.1.3**: Bit construction over $\mathbb F_2$: triples $S,T$ are neighbors when $|S\cap T|=1$; copy adds $x_T$ to the scratch wire $A_{ST}$, side injection adds $\sum_{T:|S\cap T|=1}A_{ST}$ to $y_S$, gather adds $\sum_{T\ni i}x_T$ to a central wire $C_i$ and scatter adds $\sum_{i\in S}C_i$ to $y_S$.
Source: "The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair." (paper)
> The following maps specify the construction. \begin{itemize} \item In the bit construction, scalars lie in $\mathbb F_2$, and $S,T$ are neighbors when $|S\cap T|=1$. The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair. The side injection adds $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$. The gather adds $\sum_{T\ni i}x_T$ to $C_i$, and the scatter adds $\sum_{i\in S}C_i$ to $y_S$. \item In the complex construction, scalars lie in $\mathbb Z[i,1/2]$, and neighbors are distinct triples with even intersection. Copy is unchanged. Side injection adds \[ -\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST} \] to $y_S$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source va

**S4.1.4**: Complex construction over $\mathbb Z[i,1/2]$: neighbors are distinct triples with even intersection, the side injection has coefficient $-(|S\cap T|-1)/2$, and an extra central wire $C_\ast$ makes the scatter add $(\sum_{i\in S}C_i-C_\ast)/2$.
Source: "-\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST}" (paper)
> The following maps specify the construction. \begin{itemize} \item In the bit construction, scalars lie in $\mathbb F_2$, and $S,T$ are neighbors when $|S\cap T|=1$. The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair. The side injection adds $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$. The gather adds $\sum_{T\ni i}x_T$ to $C_i$, and the scatter adds $\sum_{i\in S}C_i$ to $y_S$. \item In the complex construction, scalars lie in $\mathbb Z[i,1/2]$, and neighbors are distinct triples with even intersection. Copy is unchanged. Side injection adds \[ -\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST} \] to $y_S$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values. This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation in Buhrman, Cleve, Kouck\'y, Loff and Speelman~\cite[Section~3]{BuhrmanCleveKouckyLoffSpeelman2014}. The forward schedule is \begin{equation} \begin{array}{c|l|l} \text{row}&\t

**S4.1.5**: The eight-row forward schedule is: subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy; the first two rows remove the effect of the old scratch values and the last two restore them.
Source: "0&\text{subtract side injection}&\text{one gate per target}\\" (paper)
> o $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values. This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation in Buhrman, Cleve, Kouck\'y, Loff and Speelman~\cite[Section~3]{BuhrmanCleveKouckyLoffSpeelman2014}. The forward schedule is \begin{equation} \begin{array}{c|l|l} \text{row}&\text{operation}&\text{gate grouping}\\ \hline 0&\text{subtract side injection}&\text{one gate per target}\\ 1&\text{subtract scatter}&\text{one gate on targets and center}\\ 2&\text{copy}&\text{one gate per source}\\ 3&\text{gather}&\text{one gate on sources and center}\\ 4&\text{scatter}&\text{one gate on targets and center}\\ 5&\text{side injection}&\text{one gate per target}\\ 6&\text{undo gather}&\text{one gate on sources and center}\\ 7&\text{undo copy}&\text{one gate per source}. \end{array} \label{eq:motif-schedule} \end{equation}

**S4.1.6**: The net change of the target is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ (side injection times copy plus scatter times gather), independent of the initial scratch values $a,c$, because rows 0-1 subtract exactly the old contribution.
Source: "$(\mathcal J\mathcal V+\mathcal R\mathcal G)x$" (paper)
> \begin{proof} Write $\mathcal V$ for copy, $\mathcal G$ for gather, $\mathcal J$ for side injection and $\mathcal R$ for scatter. If the initial side and central vectors are $a,c$, the first two rows subtract $\mathcal J a+\mathcal R c$ from $y$. Rows 2 and 3 change them to $a+\mathcal Vx,c+\mathcal Gx$. Rows 4 and 5 therefore add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$. Rows 6 and 7 restore $c,a$. The net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$.

**S4.1.7**: Bit case: the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$; the side injection cancels the intersection-one cases, intersection zero or two already give zero, and the self coefficient is one, so the net map is $y\gets y+x$.
Source: "In the bit case, the central coefficient from $x_T$ to $y_S$ is" (paper)
> In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$. The side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one. In the complex case, the central coefficient is $(|S\cap T|-1)/2$. The side cancels it for distinct triples with intersection zero or two; intersection one contributes zero, and the self coefficient is one. Thus both net maps are $y\gets y+x$.

**S4.1.8**: Complex case: the central coefficient is $(|S\cap T|-1)/2$; the side wires cancel it for distinct triples with intersection zero or two, intersection one contributes zero, and the self coefficient is one, so again the net map is $y\gets y+x$.
Source: "In the complex case, the central coefficient is $(|S\cap T|-1)/2$." (paper)
> In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$. The side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one. In the complex case, the central coefficient is $(|S\cap T|-1)/2$. The side cancels it for distinct triples with intersection zero or two; intersection one contributes zero, and the self coefficient is one. Thus both net maps are $y\gets y+x$.

**S4.1.9**: Three stages starting from $(x,y)$ give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$: the signed exchange $(X_a,Y_a)\mapsto(-Y_a,X_a)$, with every invocation restoring its own scratch wires.
Source: "$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$." (paper)
> The inverse schedule with logical source $Y$ and target $X$ effects $X\gets X-Y$. Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$. Each invocation restores its own auxiliary wires. \end{proof}

**S4.1.10**: Wire counts: a triple has $z_{\rm b}=3\binom{97}{2}=13968$ bit-neighbors and $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ complex neighbors, with $c_{\rm b}=100$, $c_{\rm c}=101$ central wires per invocation, giving $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ and $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$.
Source: "W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})" (paper)
> A fixed triple has \[ z_{\rm b}=3\binom{97}{2}=13968,\qquad z_{\rm c}=\binom{97}{3}+3\cdot97=147731 \] neighbors in the two constructions, respectively. The second count separates intersection zero and intersection two. Ordered pairs must be counted: there are $vz$ side wires in each invocation, not $vz/2$. With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation, the total wire counts are \begin{align} W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b}) =177176569091445000000,\label{eq:bit-wire-count}\\ W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c}) =1873807244643542670000.\label{eq:complex-wire-count} \end{align} All these numbers are fixed, independently of any eventual input length.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md): Matrix rank, subspaces, projections, bilinear forms and the orthogonal complement of a subspace inside a larger one, including over the two-element field F₂.
  Shown as: Linear exchange network with restored scratch wires *<predicate>* Rank, subspaces and orthogonal complements

## Pages that build on this one

- Frames on wire arrays: Replacing each scalar by an array and giving every vertex an invertible linear operator D_v (its frame) lets pointwise gates commute with frames, so intermediate frames cancel and only the endpoint operator D_out·D_in⁻¹ is applied to each role while each edge pays only the change of frame D_v D_u⁻¹.
- Subspace labels from three-element subsets: Attaching nested nondegenerate subspaces of F^{⊗3} (spanned by indicator vectors of 3-element subsets, with ⟨t_S,t_T⟩ = |S∩T|−1) to gates and terminals so that gather/scatter coefficients depend on intersection size and unwanted ones are cancelled by side wires; the total rank change of all edges is less than Wm.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Address shear and lower-triangular factorization](address-shear.md)
- [Frames on wire arrays](common-frame-principle.md)
- [Subspace labels from three-element subsets](subset-intersection-labels.md)
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

- "Each procedure arises from its own fixed linear network that exchanges two" (paper)

  > Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value. A wire's fixed place in the network is called its role. To use the network on an array, regard a row as the complete ordered suffix, including all active address fields, at a fixed prefix and row index. Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$. Let $V$ now denote the node volume after padding. All role streams have the same local address set and each contains $V/W$ bits. A scalar gate is then applied pointwise to matching addresses on the roles that it touches.

- "the following schedule remove the effect of the old scratch values;" (paper)

  > d $S,T$ are neighbors when $|S\cap T|=1$. The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair. The side injection adds $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$. The gather adds $\sum_{T\ni i}x_T$ to $C_i$, and the scatter adds $\sum_{i\in S}C_i$ to $y_S$. \item In the complex construction, scalars lie in $\mathbb Z[i,1/2]$, and neighbors are distinct triples with even intersection. Copy is unchanged. Side injection adds \[ -\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST} \] to $y_S$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values. This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation in Buhrman, Cleve, Kouck\'y, Loff and Speelman~\cite[Section~3]{BuhrmanCleveKouckyLoffSpeelman2014}. The forward schedule is \begin{equation} \begin{array}{c|l|l} \text{row}&\text{operation}&\text{gate grouping}\\ \hline 0&\text{subtract side injection}&\text{one gate per target}\\ 1&\text{subtract scatter}&\text{one gate on targets and center}\\ 2&\text{copy}&\text{one gate per source}\\ 3&\text{gather}&\text{one gate on sources and center}\\ 4&\text{scatt

- "(X_a,Y_a)\longmapsto(-Y_a,X_a)" (paper)

  > \begin{lemma}\label{lem:scalar-motifs} For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged. Performing a forward invocation from $X$ to $Y$ at stage 1, the inverse forward schedule from $Y$ to $X$ at stage 2, and a forward invocation from $X$ to $Y$ at stage 3 sends \[ (X_a,Y_a)\longmapsto(-Y_a,X_a) \] and restores every auxiliary value. In the bit construction this is the permutation exchanging $X_a$ and $Y_a$. \end{lemma}


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

Write the body to `exegenius/tasks/0012-write-linear-network.answer.md` and the JSON to `exegenius/tasks/0012-write-linear-network.answer.json`, then run `exegenius submit 0012-write-linear-network` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0012-write-linear-network`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
