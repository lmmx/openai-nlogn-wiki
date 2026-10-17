# exegenius task 0028-write-gaussian-resampling

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
- Butterflies and the fast transform
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Error tracking and exact recovery
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Packed selected-bit addition
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

Concept: Gaussian resampling
Gloss: Re-expressing a Fourier transform of prime length s through a transform of nearby power-of-two length t using Gaussian weights, so that only power-of-two transforms are needed.

## This page in the argument

The step: For coprime $s<t$ with $\theta=t/s-1>p/\alpha^4$ and permutations $(P_su)_j=u_{tj}$, $(P_tv)_k=v_{-sk}$ there are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed with error less than $p^2$ in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$.
How: Use the two Gaussian resampling maps $\mathsf S$, $\mathsf T$ of Harvey and van der Hoeven with $\mathsf TP_sF_s=P_tF_t\mathsf S$ and $N=C\mathsf T\mathsf D\approx I$, invert $N$ by a Neumann series, and normalise so that $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$ are contractions.
Why: The Fourier transform of prime length $s$ must be expressed through transforms of power-of-two length $t$; Gaussian resampling does this approximately, and the transform identity can hold exactly once the resampling is inverted through a convergent Neumann series. (the sources say so: "this convolution by multidimensional transforms whose axis lengths are" (paper))

Its sub-steps, in order:

- Assume $\theta:=t/s-1>p/\alpha^4$ with $2\le\alpha<\sqrt p$, $\gcd(s,t)=1$.
- Define the permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$.
- There are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.
- From the Gaussian identity and estimate, $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$ where $N=C\mathsf T\mathsf D$ and $C$ selects the nearest coordinates.
- Since $\alpha^2<p$ and $\theta>p/\alpha^4$, $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.
- Set $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, which are contractions (norms below $3/4$, $7/8$, $1$); $A=\mathsf S'$, $B_0=\mathsf D'\mathsf J'C$.
- The normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.
- The three ordered numerical maps $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ have errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$.
- The selection $C$ picks an ordered subsequence (since $t/s>1$), and the indices are generated in order with $O(p)$ work each, so $C$ takes $O(tp)$ time with zero error.
- Contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$, and the costs add to $O(tp^{3/2+\delta}\alpha)$.
- The Neumann series with $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$ is evaluated as $\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}$ with every iterate kept in $\mathbb D_p$.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- The Fourier transforms of pairwise coprime prime lengths $s_i$ that the integer product needs are computed through power-of-two lengths $t_i$ by Gaussian resampling and Bluestein chirps, with the source and target coordinate permutations left inside the transform identities, so that none is executed as a sort.; how: Retain both permutations of Gaussian resampling in the transform formula: the target permutation $Q$ is absorbed by the chirp convolution, and the source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite transform. (on [Retained permutation cancellation](retained-permutations.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.1.1, S4.1.2, S4.1.3, S4.1.4, S4.1.4b, S4.1.4c, S4.1.4d, S4.1.5, S4.1.6, S4.1.7, S4.1.8). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.1.1**: Assume $\theta:=t/s-1>p/\alpha^4$ with $2\le\alpha<\sqrt p$, $\gcd(s,t)=1$.
Source: "\theta:=t/s-1>p/\alpha^4." (paper)
> \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

**S4.1.2**: Define the permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$.
Source: "(P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}." (paper)
> \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

**S4.1.3**: There are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.
Source: "P_sF_s=2^{2\alpha^2}B_0P_tF_tA." (paper)
> \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}

**S4.1.4**: From the Gaussian identity and estimate, $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$ where $N=C\mathsf T\mathsf D$ and $C$ selects the nearest coordinates.
Source: "\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}." (paper)
> }+\frac12\right\rfloor, \qquad \beta_j=\frac{tj}{s}-q_j. \] Thus $q_j$ is an integer nearest to $tj/s$, with ties rounded upward. Let $C:\mathbb C^t\to\mathbb C^s$ select these coordinates, and let $\mathsf D:\mathbb C^s\to\mathbb C^s$ be the diagonal map \[ (Cv)_j=v_{q_j},\qquad (\mathsf D u)_j=e^{\pi\alpha^2\beta_j^2}u_j. \] Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$. The other summands form $((N-I)u)_j$. The exact Gaussian identity and inverse estimate proved in \cite[Theorem~4.2 and Lemma~4.6]{HarveyHoeven2021} give \begin{equation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagon

**S4.1.4b**: Since $\alpha^2<p$ and $\theta>p/\alpha^4$, $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series.
Source: "$\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible" (paper)
> \] Set $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$. The other summands form $((N-I)u)_j$. The exact Gaussian identity and inverse estimate proved in \cite[Theorem~4.2 and Lemma~4.6]{HarveyHoeven2021} give \begin{equation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$

**S4.1.4c**: Set $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, which are contractions (norms below $3/4$, $7/8$, $1$); $A=\mathsf S'$, $B_0=\mathsf D'\mathsf J'C$.
Source: "\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D." (paper)
> t the selected coordinate $q_j$. The other summands form $((N-I)u)_j$. The exact Gaussian identity and inverse estimate proved in \cite[Theorem~4.2 and Lemma~4.6]{HarveyHoeven2021} give \begin{equation} \mathsf T P_sF_s=P_tF_t\mathsf S, \qquad \|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}. \label{eq:gaussian-public-facts} \end{equation} The first identity uses the negative Fourier sign in our definition of $F_q$; its right-hand permutation is consequently multiplication of the frequency by $-s$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$. Thus $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series. Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$, and $\mathsf S'$ have product $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence \[ B_0P_tF_tA =2^{-2\alpha^2}\mathsf D N^{-1}CP_tF_t\math

**S4.1.4d**: The normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.
Source: "$2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence" (paper)
> Put \[ \mathsf S'=\mathsf S/2,\qquad \mathsf J'=N^{-1}/2,\qquad \mathsf D'=2^{-(2\alpha^2-2)}\mathsf D. \] The proof of Proposition~4.7(i) in the cited paper gives \[ \|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1. \] Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. Because $\|C\|=1$, both are contractions. The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so \[ (\mathsf D N^{-1}C)\mathsf T =\mathsf D N^{-1}(N\mathsf D^{-1})=I. \] Applying this left inverse to the first identity in \eqref{eq:gaussian-public-facts} gives $\mathsf D N^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations in $\mathsf D'$, $\mathsf J'$, and $\mathsf S'$ have product $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$. Hence \[ B_0P_tF_tA =2^{-2\alpha^2}\mathsf D N^{-1}CP_tF_t\mathsf S =2^{-2\alpha^2}P_sF_s, \] which is \eqref{eq:no-sort-one-dimensional}.

**S4.1.5**: The three ordered numerical maps $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ have errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$.
How: Quote the guarantees of the cited Gaussian-resampling algorithms (Harvey and van der Hoeven's Lemmas 4.8, 4.9, 4.12) row by row and compose them with the exact selection $C$.
- S4.1.5.1: $\widetilde{\mathsf S}'$ has error $16p$ and time $O(tp^{3/2+\delta}\alpha)$.
  Source: "\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\" (paper)
  > \paragraph{Ordered numerical maps.} Lemmas~4.8, 4.9 and 4.12 of \cite{HarveyHoeven2021} supply the following algorithms. Their inputs and outputs are in increasing coordinate order, and every output is in the disk grid. The record conversions and tape movement needed to use these routines in our format are accounted for below. Their numerical guarantees are \[ \begin{array}{c|c|c} \text{map}&\text{error bound}&\text{time bound}\\ \hline \widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf J}'&3p^2/4&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf D}'&4&O(tp^{1+\delta}). \end{array} \] For $C$, observe that $q_0=0$, $q_{s-1}<t$, and $q_{j+1}>q_j$, because $t/s>1$. Thus $C$ selects an ordered subsequence. A forward scan, with the current input coordinate stored on a work tape, copies a record exactly when that coordinate equals the next $q_j$.
- S4.1.5.2: $\widetilde{\mathsf J}'$ (the Neumann inverse) has error $3p^2/4$ and time $O(tp^{3/2+\delta}\alpha)$.
  Source: "\widetilde{\mathsf J}'&3p^2/4&O(tp^{3/2+\delta}\alpha)\\" (paper)
  > \paragraph{Ordered numerical maps.} Lemmas~4.8, 4.9 and 4.12 of \cite{HarveyHoeven2021} supply the following algorithms. Their inputs and outputs are in increasing coordinate order, and every output is in the disk grid. The record conversions and tape movement needed to use these routines in our format are accounted for below. Their numerical guarantees are \[ \begin{array}{c|c|c} \text{map}&\text{error bound}&\text{time bound}\\ \hline \widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf J}'&3p^2/4&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf D}'&4&O(tp^{1+\delta}). \end{array} \] For $C$, observe that $q_0=0$, $q_{s-1}<t$, and $q_{j+1}>q_j$, because $t/s>1$. Thus $C$ selects an ordered subsequence. A forward scan, with the current input coordinate stored on a work tape, copies a record exactly when that coordinate equals the next $q_j$.
- S4.1.5.3: $\widetilde{\mathsf D}'$ has error $4$ and time $O(tp^{1+\delta})$.
  Source: "\widetilde{\mathsf D}'&4&O(tp^{1+\delta})." (paper)
  > \paragraph{Ordered numerical maps.} Lemmas~4.8, 4.9 and 4.12 of \cite{HarveyHoeven2021} supply the following algorithms. Their inputs and outputs are in increasing coordinate order, and every output is in the disk grid. The record conversions and tape movement needed to use these routines in our format are accounted for below. Their numerical guarantees are \[ \begin{array}{c|c|c} \text{map}&\text{error bound}&\text{time bound}\\ \hline \widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf J}'&3p^2/4&O(tp^{3/2+\delta}\alpha)\\ \widetilde{\mathsf D}'&4&O(tp^{1+\delta}). \end{array} \] For $C$, observe that $q_0=0$, $q_{s-1}<t$, and $q_{j+1}>q_j$, because $t/s>1$. Thus $C$ selects an ordered subsequence. A forward scan, with the current input coordinate stored on a work tape, copies a record exactly when that coordinate equals the next $q_j$.

**S4.1.6**: The selection $C$ picks an ordered subsequence (since $t/s>1$), and the indices are generated in order with $O(p)$ work each, so $C$ takes $O(tp)$ time with zero error.
Source: "also cost $O(tp)$, so $C$ takes $O(tp)$ time with zero numerical error." (paper)
> The selected indices can themselves be generated in order using only $O(p)$ work per index. Precompute $t=hs+\rho$ with $0\leq\rho<s$. Start with $f_0=e_0=0$, and maintain $tj=sf_j+e_j$ with $0\leq e_j<s$. At index $j$, first use $q_j=f_j+\mathbf1_{2e_j\geq s}$. If $j<s-1$, after copying that record form the values for index $j+1$ by \[ c_j=\mathbf1_{e_j+\rho\geq s},\qquad e_{j+1}=e_j+\rho-c_js,\qquad f_{j+1}=f_j+h+c_j. \] Here $e_j+\rho<2s$, so $c_j$ is the only possible carry; the displayed update gives $t(j+1)=sf_{j+1}+e_{j+1}$. All these counters have $O(p)$ bits. Elementary division computes $h,\rho$ in $O((\log t)^2)=O(tp)$ time. The record scan and its coordinate counter also cost $O(tp)$, so $C$ takes $O(tp)$ time with zero numerical error.

**S4.1.7**: Contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$, and the costs add to $O(tp^{3/2+\delta}\alpha)$.
Source: "Contraction of the exact maps yields errors less than $16p<p^2$ and" (paper)
> Consequently we may take \[ \widetilde A=\widetilde{\mathsf S}', \qquad \widetilde B_0=\widetilde{\mathsf D}'\, \widetilde{\mathsf J}'\,C. \] Contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$, respectively. The costs add to the claimed bound.

**S4.1.8**: The Neumann series with $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$ is evaluated as $\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}$ with every iterate kept in $\mathbb D_p$.
Source: "\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}" (paper)
> The Neumann evaluation also keeps its computed records bounded. Put $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$. Under the present hypotheses, Lemma~4.11 gives, for every $z\in\mathbb D_p^s$, \[ \widetilde E z\in\mathbb D_p^s,\qquad 2^p\|\widetilde E z-Ez\|<p/3. \] Its proof establishes the rounded output bound \[ \|\widetilde E z\|<0.42\|z\|+(p/3)2^{-p}<1. \] For $u\in\mathbb D_p^s$, Lemma~4.12 rounds the real and imaginary parts of each coordinate of $u/2$ toward zero at precision $p$, obtaining $\widetilde v^{(0)}\in\mathbb D_p^s$. It then computes $\widetilde v^{(j)}=\widetilde E\widetilde v^{(j-1)}$ for $1\leq j<k$. Induction therefore keeps every iterate in $\mathbb D_p^s$. The approximation is $\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}$. Since $k\leq\alpha^2+1<p+1$, each component of any signed partial numerator sum has magnitude at most $k2^p$ and needs $p+\lceil\log_2(k+1)\rceil+O(1)=O(p)$ bits. Inside one $\widetilde E$ row, the $2m$ disk-grid summands of Lemma~4.11 likewise need $p+\lceil\log_2(2m+1)\rceil+O(1)=O(p)$ accumulator bits, where $m=\lceil\sqrt p/(2\alpha)\rceil$. These partial sums are accumulated exactly on separate tapes; only completed iterates are fed into $\widetilde E$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](dft.md): The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns convolution into pointwise multiplication.
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Multidimensional transforms](multidim-transform.md): A transform over several axes at once, the tensor product of one-dimensional transforms, applied to an array one axis at a time.
  Shown as: Gaussian resampling *<predicate>* Multidimensional transforms

## Pages that build on this one

- Retained permutation cancellation: Leaving the coordinate permutations of resampling inside the transform identity, so the source permutation cancels across the two forward transforms and the opposite one and none is executed as a sort.
- Parameter and prime-length choice: Fixed rational exponents and sizes (precision p = 6b, d axes, K = d^c, T and r powers of two, prime lengths s_i just below t_i) making every hypothesis of the lemmas hold.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
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
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder address map](crt-map.md)
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

- "Gaussian resampling then expresses each source Fourier transform through a" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.

- "Resampling without executing the two permutations" (paper)

  > \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}


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

Write the body to `exegenius/tasks/0028-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0028-write-gaussian-resampling.answer.json`, then run `exegenius submit 0028-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0028-write-gaussian-resampling`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
