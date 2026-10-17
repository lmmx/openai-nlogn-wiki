# exegenius task 0257-write-exchange-network

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
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
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

## This page

Concept: Linear exchange network with restored scratch wires
Gloss: A fixed network of linear gates on wires holding values that swaps two banks with a prescribed sign while undoing the effect of arbitrary initial scratch values, built from three-element subsets.
Also called: finite network, motif

## This page in the argument

The step: There is a fixed linear network of $W$ wires on two banks $X_a,Y_a$ ($a\in\mathcal T^3$, $\mathcal T$ the three-element subsets of $[h]$) that sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restores every scratch wire whatever its initial value, in a bit version (wires $W_{\rm b}$) and a complex version (wires $W_{\rm c}$).
How: Build one forward invocation $y_S\gets y_S+x_S$ from three-element subsets of $[h]$: a central route through gather and scatter wires whose coefficient depends on the intersection size, plus side wires that cancel the unwanted coefficients, bracketed by subtract and undo rows; then chain three stages, the middle one run inverted.
Why: Gather and scatter through a few central wires give a low-rank route, but their coefficient depends on how two triples intersect; the side wires correct exactly the unwanted intersection sizes, and the subtract and undo rows make the result independent of the arbitrary scratch contents. (the sources say so: "on intersection size, and auxiliary wires cancel the unwanted" (paper))

Its sub-steps, in order:

- Fix the ground-set size $h=100$ and let $v=\binom h3=161700$ be the number of three-element subsets of $[h]$.
- Set $N=v^3=4227952113000000$ for the size of each data bank and $m=h^3=1000000$ for the dimension of the label space used later.
- There are $I=3v^2=78440670000$ invocations: three stages, each running $v^2$ invocations with their own scratch wires.
- In the bit construction two triples $S,T$ are neighbours when $|S\cap T|=1$.
- In the complex construction the neighbours of a triple are the distinct triples with even intersection (zero or two).
- For arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.
- Running a forward invocation $X\to Y$ at stage 1, the inverse forward schedule $Y\to X$ at stage 2 and a forward invocation $X\to Y$ at stage 3 gives $(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x)$, i.e. $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring every scratch wire.
- A fixed triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction.
- A fixed triple has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus intersection two).
- There are $c_{\rm b}=100$ central wires per invocation in the bit network and $c_{\rm c}=101$ in the complex one.
- The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires (ordered neighbour pairs are counted, so $vz_{\rm b}$ side wires per invocation).
- The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires; all these numbers are fixed, independent of the input length.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.; how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). (on [Recursive power saving](rank-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.1.1, S1.1.2, S1.1.3, S1.1.4a, S1.1.4b, S1.1.5, S1.1.6, S1.1.7a, S1.1.7b, S1.1.7c, S1.1.8a, S1.1.8b). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.1.1**: Fix the ground-set size $h=100$ and let $v=\binom h3=161700$ be the number of three-element subsets of $[h]$.
Source: "h=100,\qquad v=\binom h3=161700,\qquad" (paper)
> Put \[ h=100,\qquad v=\binom h3=161700,\qquad N=v^3=4227952113000000,\qquad m=h^3=1000000. \] Let $\mathcal T$ be the set of three-element subsets of $[h]$. There are two data banks $X_a,Y_a$, indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. A wire carries one scalar. A gate is a fixed linear map on a specified set of wires; untouched wires retain their values. The vertices on a wire are its source, the gates that touch it in time order, and its sink; its edges join consecutive vertices. We call the name of a wire its \emph{role}, so that we can distinguish a fixed place in the network from the value currently carried there.

**S1.1.2**: Set $N=v^3=4227952113000000$ for the size of each data bank and $m=h^3=1000000$ for the dimension of the label space used later.
Source: "N=v^3=4227952113000000,\qquad m=h^3=1000000." (paper)
> Put \[ h=100,\qquad v=\binom h3=161700,\qquad N=v^3=4227952113000000,\qquad m=h^3=1000000. \] Let $\mathcal T$ be the set of three-element subsets of $[h]$. There are two data banks $X_a,Y_a$, indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. A wire carries one scalar. A gate is a fixed linear map on a specified set of wires; untouched wires retain their values. The vertices on a wire are its source, the gates that touch it in time order, and its sink; its edges join consecutive vertices. We call the name of a wire its \emph{role}, so that we can distinguish a fixed place in the network from the value currently carried there.

**S1.1.3**: There are $I=3v^2=78440670000$ invocations: three stages, each running $v^2$ invocations with their own scratch wires.
Source: "I=3v^2=78440670000" (paper)
> There are three stages. At stage $j$, fix the other two coordinates and operate on the $v$ values in each bank obtained by varying coordinate $j$. Thus there are $v^2$ separate invocations at each stage. Each such invocation has its own auxiliary wires, distinct from all other invocations, including those in other stages. There are \[ I=3v^2=78440670000 \] invocations. In a forward invocation, write $x_T$ for the data used as controls and $y_S$ for the data to be updated; $S,T\in\mathcal T$ are their varying $j$th coordinates. These are the logical source and target banks of the invocation. For each ordered pair $(S,T)$ that is neighboring under the rule below, there is an auxiliary wire $A_{ST}$. There are also central wires $C_i$, $i\in[h]$, and in the second construction a wire $C_\ast$. We call all these auxiliary wires \emph{scratch wires}; their initial values may be arbitrary.

**S1.1.4a**: In the bit construction two triples $S,T$ are neighbours when $|S\cap T|=1$.
Source: "$S,T$ are neighbors when $|S\cap T|=1$." (paper)
> The following maps specify the construction. \begin{itemize} \item In the bit construction, scalars lie in $\mathbb F_2$, and $S,T$ are neighbors when $|S\cap T|=1$. The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair. The side injection adds $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$. The gather adds $\sum_{T\ni i}x_T$ to $C_i$, and the scatter adds $\sum_{i\in S}C_i$ to $y_S$. \item In the complex construction, scalars lie in $\mathbb Z[i,1/2]$, and neighbors are distinct triples with even intersection. Copy is unchanged. Side injection adds \[ -\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST} \] to $y_S$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scr

**S1.1.4b**: In the complex construction the neighbours of a triple are the distinct triples with even intersection (zero or two).
Source: "$\mathbb Z[i,1/2]$, and neighbors are distinct triples with even" (paper)
> The following maps specify the construction. \begin{itemize} \item In the bit construction, scalars lie in $\mathbb F_2$, and $S,T$ are neighbors when $|S\cap T|=1$. The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair. The side injection adds $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$. The gather adds $\sum_{T\ni i}x_T$ to $C_i$, and the scatter adds $\sum_{i\in S}C_i$ to $y_S$. \item In the complex construction, scalars lie in $\mathbb Z[i,1/2]$, and neighbors are distinct triples with even intersection. Copy is unchanged. Side injection adds \[ -\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST} \] to $y_S$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values. This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation in Buhrman, Cleve, Kouck\'y, Loff and Speelman~\cite[Sec

**S1.1.5**: For arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.
How: Compute the net change of the target as (side injection)(copy) + (scatter)(gather) applied to $x$, showing it does not depend on the initial side and central values $a,c$, then compare its coefficients with the identity case by case (bit and complex).
- S1.1.5.1: The first two rows of the schedule remove the effect of the old scratch values, the next four add the source's effect to the target, and the last two restore the scratch values.
  Source: "the following schedule remove the effect of the old scratch values;" (paper)
  > d $S,T$ are neighbors when $|S\cap T|=1$. The copy map adds $x_T$ to $A_{ST}$ for each neighbor pair. The side injection adds $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$. The gather adds $\sum_{T\ni i}x_T$ to $C_i$, and the scatter adds $\sum_{i\in S}C_i$ to $y_S$. \item In the complex construction, scalars lie in $\mathbb Z[i,1/2]$, and neighbors are distinct triples with even intersection. Copy is unchanged. Side injection adds \[ -\sum_{T\text{ neighboring }S}\frac{|S\cap T|-1}{2}A_{ST} \] to $y_S$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$ and $\sum_Tx_T$ to $C_\ast$. Scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. \end{itemize} Each update leaves its control wires unchanged. The first two rows of the following schedule remove the effect of the old scratch values; the next four introduce the source values and add their effect to the target; the last two restore the scratch values. This cancellation of arbitrary initial scratch values is a linear instance of the restoration construction for transparent computation in Buhrman, Cleve, Kouck\'y, Loff and Speelman~\cite[Section~3]{BuhrmanCleveKouckyLoffSpeelman2014}. The forward schedule is \begin{equation} \begin{array}{c|l|l} \text{row}&\text{operation}&\text{gate grouping}\\ \hline 0&\text{subtract side injection}&\text{one gate per target}\\ 1&\text{subtract scatter}&\text{one gate on targets and center}\\ 2&\text{copy}&\text{one gate per source}\\ 3&\text{gather}&\text{one gate on sources and center}\\ 4&\text{scatt
- S1.1.5.2: Writing $\mathcal V,\mathcal G,\mathcal J,\mathcal R$ for copy, gather, side injection and scatter, the net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independent of the initial side and central vectors $a,c$.
  Source: "Rows 6 and 7 restore $c,a$.  The net target change is" (paper)
  > \begin{proof} Write $\mathcal V$ for copy, $\mathcal G$ for gather, $\mathcal J$ for side injection and $\mathcal R$ for scatter. If the initial side and central vectors are $a,c$, the first two rows subtract $\mathcal J a+\mathcal R c$ from $y$. Rows 2 and 3 change them to $a+\mathcal Vx,c+\mathcal Gx$. Rows 4 and 5 therefore add $\mathcal R(c+\mathcal Gx)+\mathcal J(a+\mathcal Vx)$. Rows 6 and 7 restore $c,a$. The net target change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, independently of $a,c$.
- S1.1.5.3: Bit case (scalars in $\mathbb F_2$, neighbours $|S\cap T|=1$): the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod 2$.
  Source: "In the bit case, the central coefficient from $x_T$ to $y_S$ is" (paper)
  > In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$. The side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one. In the complex case, the central coefficient is $(|S\cap T|-1)/2$. The side cancels it for distinct triples with intersection zero or two; intersection one contributes zero, and the self coefficient is one. Thus both net maps are $y\gets y+x$.
- S1.1.5.4: In the bit case the side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one, so the net map is $y\gets y+x$.
  Source: "intersection-one cases; distinct triples with intersection zero or two" (paper)
  > In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$. The side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one. In the complex case, the central coefficient is $(|S\cap T|-1)/2$. The side cancels it for distinct triples with intersection zero or two; intersection one contributes zero, and the self coefficient is one. Thus both net maps are $y\gets y+x$.
- S1.1.5.5: Complex case (scalars in $\mathbb Z[i,1/2]$, neighbours are distinct triples with even intersection): the central coefficient is $(|S\cap T|-1)/2$.
  Source: "In the complex case, the central coefficient is $(|S\cap T|-1)/2$." (paper)
  > In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$. The side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one. In the complex case, the central coefficient is $(|S\cap T|-1)/2$. The side cancels it for distinct triples with intersection zero or two; intersection one contributes zero, and the self coefficient is one. Thus both net maps are $y\gets y+x$.
- S1.1.5.6: In the complex case the side wires cancel the coefficient for distinct triples with intersection zero or two, intersection one contributes zero, and the self coefficient is one, so again the net map is $y\gets y+x$.
  Source: "intersection one contributes zero, and the self coefficient is one." (paper)
  > In the bit case, the central coefficient from $x_T$ to $y_S$ is $|S\cap T|\bmod2$. The side contribution cancels exactly the intersection-one cases; distinct triples with intersection zero or two already have coefficient zero, and the self coefficient is one. In the complex case, the central coefficient is $(|S\cap T|-1)/2$. The side cancels it for distinct triples with intersection zero or two; intersection one contributes zero, and the self coefficient is one. Thus both net maps are $y\gets y+x$.

**S1.1.6**: Running a forward invocation $X\to Y$ at stage 1, the inverse forward schedule $Y\to X$ at stage 2 and a forward invocation $X\to Y$ at stage 3 gives $(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x)$, i.e. $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring every scratch wire.
Source: "$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$." (paper)
> The inverse schedule with logical source $Y$ and target $X$ effects $X\gets X-Y$. Starting from $(x,y)$, the three stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$. Each invocation restores its own auxiliary wires. \end{proof}

**S1.1.7a**: A fixed triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction.
Source: "z_{\rm b}=3\binom{97}{2}=13968,\qquad" (paper)
> A fixed triple has \[ z_{\rm b}=3\binom{97}{2}=13968,\qquad z_{\rm c}=\binom{97}{3}+3\cdot97=147731 \] neighbors in the two constructions, respectively. The second count separates intersection zero and intersection two. Ordered pairs must be counted: there are $vz$ side wires in each invocation, not $vz/2$. With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation, the total wire counts are \begin{align} W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b}) =177176569091445000000,\label{eq:bit-wire-count}\\ W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c}) =1873807244643542670000.\label{eq:complex-wire-count} \end{align} All these numbers are fixed, independently of any eventual input length.

**S1.1.7b**: A fixed triple has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus intersection two).
Source: "z_{\rm c}=\binom{97}{3}+3\cdot97=147731" (paper)
> A fixed triple has \[ z_{\rm b}=3\binom{97}{2}=13968,\qquad z_{\rm c}=\binom{97}{3}+3\cdot97=147731 \] neighbors in the two constructions, respectively. The second count separates intersection zero and intersection two. Ordered pairs must be counted: there are $vz$ side wires in each invocation, not $vz/2$. With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation, the total wire counts are \begin{align} W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b}) =177176569091445000000,\label{eq:bit-wire-count}\\ W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c}) =1873807244643542670000.\label{eq:complex-wire-count} \end{align} All these numbers are fixed, independently of any eventual input length.

**S1.1.7c**: There are $c_{\rm b}=100$ central wires per invocation in the bit network and $c_{\rm c}=101$ in the complex one.
Source: "With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation," (paper)
> A fixed triple has \[ z_{\rm b}=3\binom{97}{2}=13968,\qquad z_{\rm c}=\binom{97}{3}+3\cdot97=147731 \] neighbors in the two constructions, respectively. The second count separates intersection zero and intersection two. Ordered pairs must be counted: there are $vz$ side wires in each invocation, not $vz/2$. With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation, the total wire counts are \begin{align} W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b}) =177176569091445000000,\label{eq:bit-wire-count}\\ W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c}) =1873807244643542670000.\label{eq:complex-wire-count} \end{align} All these numbers are fixed, independently of any eventual input length.

**S1.1.8a**: The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires (ordered neighbour pairs are counted, so $vz_{\rm b}$ side wires per invocation).
Source: "W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})" (paper)
> A fixed triple has \[ z_{\rm b}=3\binom{97}{2}=13968,\qquad z_{\rm c}=\binom{97}{3}+3\cdot97=147731 \] neighbors in the two constructions, respectively. The second count separates intersection zero and intersection two. Ordered pairs must be counted: there are $vz$ side wires in each invocation, not $vz/2$. With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation, the total wire counts are \begin{align} W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b}) =177176569091445000000,\label{eq:bit-wire-count}\\ W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c}) =1873807244643542670000.\label{eq:complex-wire-count} \end{align} All these numbers are fixed, independently of any eventual input length.

**S1.1.8b**: The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires; all these numbers are fixed, independent of the input length.
Source: "W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c})" (paper)
> A fixed triple has \[ z_{\rm b}=3\binom{97}{2}=13968,\qquad z_{\rm c}=\binom{97}{3}+3\cdot97=147731 \] neighbors in the two constructions, respectively. The second count separates intersection zero and intersection two. Ordered pairs must be counted: there are $vz$ side wires in each invocation, not $vz/2$. With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation, the total wire counts are \begin{align} W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b}) =177176569091445000000,\label{eq:bit-wire-count}\\ W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c}) =1873807244643542670000.\label{eq:complex-wire-count} \end{align} All these numbers are fixed, independently of any eventual input length.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $c$ (machine constant), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A positive constant, depending on the machine, in the lower bound c n log n.
- $\kappa$ (power saving), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations in sequence since the layer began that produced a value.
- $\Delta$ (reserved extra bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed-point Gaussian dyadic records](fixed-point.md): Complex values stored as signed two's-complement integers over a power-of-two denominator 2^{-p}; intermediate values are exact and one truncation Q_p rounds back to the p-bit grid.
  Shown as: Linear exchange network with restored scratch wires *<predicate>* Fixed-point Gaussian dyadic records

## Pages that build on this one

- Frames on wire arrays: Replacing each wire scalar by an array and assigning an invertible operator D_v (a frame) at each gate so the pointwise gate commutes with the frame and only the endpoint frames matter.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
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
- [Retained frequency order](frequency-order.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value." (paper)

  > Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value. A wire's fixed place in the network is called its role. To use the network on an array, regard a row as the complete ordered suffix, including all active address fields, at a fixed prefix and row index. Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$. Let $V$ now denote the node volume after padding. All role streams have the same local address set and each contains $V/W$ bits. A scalar gate is then applied pointwise to matching addresses on the roles that it touches.

- "For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged." (paper)

  > \begin{lemma}\label{lem:scalar-motifs} For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged. Performing a forward invocation from $X$ to $Y$ at stage 1, the inverse forward schedule from $Y$ to $X$ at stage 2, and a forward invocation from $X$ to $Y$ at stage 3 sends \[ (X_a,Y_a)\longmapsto(-Y_a,X_a) \] and restores every auxiliary value. In the bit construction this is the permutation exchanging $X_a$ and $Y_a$. \end{lemma}

- "The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "At every $a$,
$$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring all scratch wires" cites "Performing a forward invocation from $X$ to $Y$ at stage 1,": Quotation only says a forward invocation from X to Y is performed at stage 1; it does not give the sequence of maps, the final (-Y,X) result or the restoration of scratch wires. Say only what the source supports, or cite the passage that supports the claim.

## Previous version (revise it)

It has 530 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 662 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A linear exchange network is a fixed circuit of linear gates on wires, each carrying one scalar, that swaps two banks of values with a sign and restores every scratch wire to its initial value, whatever that was; it is the finite building block of the later tape procedures.

Fix the ground-set size $h=100$ and write $[h]=\{1,\dots,h\}$. Let $\mathcal T$ be the set of three-element subsets of $[h]$, so that $v=\binom h3=161700$ counts them. There are two data banks $X=(X_a)$ and $Y=(Y_a)$, indexed by $a\in\mathcal T^3$ ($a$ here is a triple of triples, not a shift exponent). Set $N=v^3=4227952113000000$ for the size of each bank, and $m=h^3=1000000$ for the dimension of the label space used later.

## One invocation

Fix two coordinates of $a$ and let the third, $S\in\mathcal T$, vary. A forward invocation $X\to Y$ takes the slices $x_S$ of $X$ and $y_S$ of $Y$ and must perform $y_S\gets y_S+x_S$ with linear gates, using scratch wires with arbitrary initial values.

Through central wires $C_i$, $i\in[h]$, gather adds $\sum_{S'\ni i}x_{S'}$ to $C_i$, for $S'$ another triple, and scatter adds $\sum_{i\in S}C_i$ to $y_S$. But $x_{S'}$ reaches $y_S$ with a coefficient depending on $|S\cap S'|$ <cite data-source="paper">on intersection size, and auxiliary wires cancel the unwanted</cite>. Side wires $A_{SS'}$, one per ordered neighbour pair, cancel it: copy adds $x_{S'}$ to $A_{SS'}$, and side injection adds a multiple of $A_{SS'}$ to $y_S$.

In the bit construction, scalars lie in $\mathbb F_2$ and $S,S'$ are neighbours when $|S\cap S'|=1$. The central coefficient $|S\cap S'|\bmod 2$ is 1 for $S'=S$ and intersection one, else 0. Injection adds $\sum_{S':|S\cap S'|=1}A_{SS'}$, cancelling intersection one since $1+1=0$.

In the complex construction the network keeps its scalars in $\mathbb Z[i,1/2]$, the values of [Fixed-point Gaussian dyadic records](fixed-point.md), and the neighbours of a triple are the distinct triples with even intersection (zero or two). A further central wire $C_\ast$ gathers $\sum_{S'}x_{S'}$, and scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$. The central coefficient is $(|S\cap S'|-1)/2$, which is $-\frac12,0,\frac12,1$ for intersection $0,1,2,3$. Injection adds $-\sum_{S'}\frac{|S\cap S'|-1}{2}A_{SS'}$ over neighbours $S'$ of $S$, cancelling intersections zero and two through the copy. Intersection one is already 0, and the self coefficient is $(3-1)/2=1$, as a triple is not its own neighbour.

Let $\sigma,\gamma$ be the initial side and central values, and $\mathcal V,\mathcal G,\mathcal J,\mathcal R$ the copy, gather, injection and scatter maps. The schedule subtracts $\mathcal J\sigma+\mathcal R\gamma$ from $y$; copies and gathers, making the scratch values $\sigma+\mathcal Vx$, $\gamma+\mathcal Gx$; scatters and injects, adding $\mathcal R(\gamma+\mathcal Gx)+\mathcal J(\sigma+\mathcal Vx)$ to $y$; then undoes gather and copy, restoring $\gamma,\sigma$. The net change of $y$ is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, free of $\sigma,\gamma$; by the coefficients above it is $y\gets y+x$. So for arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged <cite data-source="paper">invocation changes $y_S$ to $y_S+x_S$ and leaves every other value</cite>.

## Three stages

Stage 1 lets the first coordinate of $a$ vary, stage 2 the second, stage 3 the third. A stage covers all $v^2$ choices of the other two coordinates, each with its own invocation and scratch wires, so there are $I=3v^2=78440670000$ invocations.

The inverse schedule, the forward one with target updates negated, performs $X\gets X-Y$ when $Y$ is the source bank and $X$ the target. Run forward $X\to Y$ at stage 1, inverse $Y\to X$ at stage 2 and forward $X\to Y$ at stage 3. At every $a$,
$$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring all scratch wires <cite data-source="paper">Performing a forward invocation from $X$ to $Y$ at stage 1,</cite>.

## Counting wires

A triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction <cite data-source="paper">z_{\rm b}=3\binom{97}{2}=13968</cite>. It has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus two) <cite data-source="paper">z_{\rm c}=\binom{97}{3}+3\cdot97=147731</cite>. There are $c_{\rm b}=100$ central wires per invocation in the bit network and $c_{\rm c}=101$ in the complex one.

Ordered pairs are counted: $vz_{\rm b}$ side wires per invocation. The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires <cite data-source="paper">W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})</cite>. The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires <cite data-source="paper">W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c})</cite>. All these numbers are fixed, independent of input length.

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

Write the body to `exegenius/tasks/0257-write-exchange-network.answer.md` and the JSON to `exegenius/tasks/0257-write-exchange-network.answer.json`, then run `exegenius submit 0257-write-exchange-network` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0257-write-exchange-network`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
