# exegenius task 0375-write-gaussian-resampling

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
- Bluestein chirp identity (also: chirp transform)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Two-point kernel C (also: phase network kernel)
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
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
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
- [Chinese-remainder address map](crt-map.md)
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

- "Gaussian resampling then expresses each source Fourier transform through a" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.

- "Resampling without executing the two permutations" (paper)

  > \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "They satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$.": The identity T P_s F_s = P_t F_t S is cited to Harvey and van der Hoeven and not proved on this page. I took it as a given fact, and the Gaussian resampling identity P_sF_s = 2^{2alpha^2} B_0 P_tF_t A depends on it. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "The cited estimate gives": The bound on ||N-I|| is cited, not shown. I could check the later algebra (D N^{-1} C is a left inverse of T, so applying it to T P_s F_s gives P_s F_s), but I could not tell whether the norm bound holds, so I could not verify that N is invertible by the Neumann series. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "To undo $\mathsf T$, let $q_j$ be the integer nearest $tj/s$": I followed each step of the construction (C selects, D cancels the Gaussian factor at the selected coordinate, N = CTD), but I could not see why this particular choice of Gaussian weights and rounding to the nearest index is the right way to invert T. I accepted it as a construction. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "Harvey and van der Hoeven's maps": The maps S and T come from a literature I do not know. I could not tell whether the identity T P_s F_s = P_t F_t S is a proved claim on this page or an imported fact, so its status is unclear to me. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" got stuck at "The cited estimate gives": The bound on the norm of N minus I is only cited, and the Neumann-series step that depends on it is then taken as given. I could not tell whether this bound is assumed or established here. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "The cited estimate gives": The bound on the norm of N minus I is taken from a cited estimate that the page does not show. I could not check it, and the exact construction depends on it. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "from the cited Lemma 4.11": The approximation of E and its error bound are taken from a cited lemma, and the 'Computing it' section says cited algorithms give bounds. I could not tell whether these are proved on the page or assumed. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "The cited estimate gives $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$.": This bound and the Lemma it relies on are cited, not proved on this page, so I could not tell whether the claimed status (proved or assumed) holds. The Gaussian weights and the condition on theta were also not motivated for me. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage." got stuck at "There are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.": I followed the construction of N and its inverse, but I could not see how the normalizing factors combine to give exactly this identity. The earlier maps are attributed to other authors and not explained here. (the reader followed the steps but not why they lead where they do: say what this step is for)
- A simulated reader (reader) trying to answer "Summarise in a few sentences what the main theorem says about multiplying two n-bit integers, in which machine model it holds, which earlier conjecture it refutes, and the overall plan the proof follows to get there." got stuck at "The cited estimate gives $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$.": The estimate has no source on the page. I could not tell whether it is an assumption or a proved claim, and I could not check the constant 2.01. I accepted the inequality. (stuck at the statement level)
- A simulated reader (reader) trying to answer "Summarise in a few sentences what the main theorem says about multiplying two n-bit integers, in which machine model it holds, which earlier conjecture it refutes, and the overall plan the proof follows to get there." got stuck at "The cited algorithms give approximations $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ with errors $16p$, $3p^2/4$, $4$ and times": The algorithms and their error and time bounds are imported without a source. I cannot tell whether they are assumptions or results, so the claim that the computed transform is fast rests on something I could not verify. (stuck at the statement level)
- Simulated readers trying to answer "Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?" could not work out: Executing the permutations would mean sorting data on a tape, costing about t p log t per line, which would cancel the power saving.. A reader with the stated background should be able to get this from this page and the pages it builds on.

## Previous version (revise it)

It has 443 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 553 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling expresses a Fourier transform of length $s$, the source length, through one of a nearby larger length $t$ (a power of two there), so that only power-of-two transforms need a fast algorithm. Several letters are reused here with new meanings: $j$ and $k$ are single coordinate indices, not index tuples as on the multidimensional-transform page.

Let $s<t<2^p$ be coprime integers, where $p>100$ counts the fractional bits of each real and imaginary component, and let $\alpha$, the width parameter of the Gaussian weights below, be an integer with $2\le\alpha<\sqrt p$. Assume $\theta:=t/s-1>p/\alpha^4$. Here $F_q$ is the normalised [Discrete Fourier transform](dft.md) of length $q$, and the resampling re-expresses $F_s$ through $F_t$. Define the permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ (coordinate indices $j$, $k$ taken modulo $s$, $t$), which stay in the identity, never executed as sorts. There are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$. Applied along each axis of a [Multidimensional transforms](multidim-transform.md), it replaces $s$ by $t$.

## Exact construction

Harvey and van der Hoeven's maps $\mathsf S,\mathsf T$ from length-$s$ to length-$t$ complex vectors are, for $0\le k<t$, with $u$ extended periodically and $j$ over all integers,
$$(\mathsf Su)_k=\frac1\alpha\sum_j e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (\mathsf Tu)_k=\sum_j e^{-\pi\alpha^2(tj/s-k)^2}u_j.$$
They satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$ <cite data-source="paper">\mathsf T P_sF_s=P_tF_t\mathsf S,</cite>.

To undo $\mathsf T$, let $q_j$ be the integer nearest $tj/s$ and $\beta_j=tj/s-q_j$. Let $C$ select coordinates from length-$t$ to length-$s$ vectors, $(Cv)_j=v_{q_j}$, and $(\mathsf Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$. Put $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$, because $tj/s-q_j=\beta_j$. The other summands form $((N-I)u)_j$. The cited estimate gives $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$ <cite data-source="paper">\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}.</cite>.

Since $\alpha^2<p$ and $\theta>p/\alpha^4$, $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series $N^{-1}=\sum_i(-1)^i(N-I)^i$.

Set $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, and put $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$; these are contractions, since $\|C\|=1$ and the three factors have norms below $3/4$, $7/8$, $1$ <cite data-source="paper">\|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1.</cite>.

As $C\mathsf T=N\mathsf D^{-1}$, the map $\mathsf DN^{-1}C$ is a left inverse of $\mathsf T$; applying it to the identity gives $\mathsf DN^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.

## Computing it

Let $\mathbb D_p$ be the grid of [Fixed-point Gaussian dyadic records](fixed-point.md). An approximation $\widetilde L$ of a contraction $L$ has error below a bound if $2^p\|\widetilde Lu-Lu\|$ is less than it for all inputs $u\in\mathbb D_p$. Fix $0<\delta<1/8$, the time-exponent slack. The cited algorithms give approximations $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ with errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$ <cite data-source="paper">\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\</cite><cite data-source="paper">\widetilde{\mathsf J}'&3p^2/4&O(tp^{3/2+\delta}\alpha)\\</cite><cite data-source="paper">\widetilde{\mathsf D}'&4&O(tp^{1+\delta}).</cite>.

The selection $C$ picks an ordered subsequence (since $t/s>1$), and the indices are generated in order with $O(p)$ work each, so $C$ takes $O(tp)$ time with zero error <cite data-source="paper">also cost $O(tp)$, so $C$ takes $O(tp)$ time with zero numerical error.</cite>.

Take $\widetilde A=\widetilde{\mathsf S}'$ and $\widetilde B_0=\widetilde{\mathsf D}'\widetilde{\mathsf J}'C$. Contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$ (as $p>100$), and the costs add to $O(tp^{3/2+\delta}\alpha)$.

Let $E=N-I$ and $K=\lceil p/(\alpha^2\theta)\rceil$, the number of series terms kept. As $\|E\|<2^{-\alpha^2\theta}$ and $\alpha^2\theta>1$, the omitted terms sum to less than $2\cdot2^{-p}$. Let $\widetilde E$ be the approximation of $E$ on $\mathbb D_p$ from the cited Lemma 4.11: for every $z\in\mathbb D_p^s$ we have $\widetilde Ez\in\mathbb D_p^s$ and $\|\widetilde Ez\|<0.42\|z\|+(p/3)2^{-p}<1$ <cite data-source="paper">\|\widetilde E z\|<0.42\|z\|+(p/3)2^{-p}<1</cite>. Start from $\widetilde v^{(0)}$, the rounding of $u/2$, and set $\widetilde v^{(i)}=\widetilde E\widetilde v^{(i-1)}$. The Neumann series with $E=N-I$ and $K=\lceil p/(\alpha^2\theta)\rceil$ is evaluated as $\widetilde{\mathsf J}'u=\sum_{i=0}^{K-1}(-1)^i\widetilde v^{(i)}$ with every iterate kept in $\mathbb D_p$.

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

Write the body to `exegenius/tasks/0375-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0375-write-gaussian-resampling.answer.json`, then run `exegenius submit 0375-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0375-write-gaussian-resampling`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
