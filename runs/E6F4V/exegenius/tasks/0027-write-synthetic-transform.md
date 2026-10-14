# exegenius task 0027-write-synthetic-transform

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4V` (paths below are relative to it)

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
- Cyclic convolution (also: convolution)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Multidimensional (tensor) transform (also: tensor transform)
- Two-point butterfly (also: H₀, butterfly operation)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed packing of polynomial products (also: Kronecker substitution)
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Frames on wire arrays (also: frame, common-frame identity)
- Subspace labels from three-element subsets (also: rank saving construction, orthogonal residual labels)
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
- Recursive rank saving (also: power saving recurrence)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Packed selected-bit addition (also: packed XOR, exceptional address repair)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Coefficient (phase) twist (also: twist)
- Integer product as digit convolution (also: radix-2^b digits)
- Rounding and carry propagation (also: exact recovery, carry propagation)
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

Concept: Synthetic polynomial transform
Gloss: A Fourier-type transform whose entries lie in C[y]/(y^r+1) and whose root of unity ω_t = y^{2r/t} acts as a signed coefficient shift, computed by radix-two butterfly rounds with twiddle monomials, leaving outputs in bit-reversed (retained) frequency order that the opposite transform consumes.
Also called: Nussbaumer polynomial transform, stored frequency order

## This page in the argument

The step: A normalized Fourier-type transform over $\mathbb C[y]/(y^r+1)$ with roots $\omega_t=y^{2r/t}$ is computed by radix-two butterfly rounds in bit-reversed frequency order, in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
How: define the transform with signed-shift roots, compute it by decimation in frequency, store outputs in retained order, and lay the axes out so the simultaneous layers apply
Why: Powers of $y$ are exact roots of unity that act as signed shifts, so no multiplications by complex roots are needed; the rounds can then be grouped across axes into the simultaneous layers of the previous section, provided the participating bits are placed at a common offset of consecutive chunks. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The synthetic transforms satisfy $F_t^+F_t^-=t^{-1}I$ despite zero divisors in $\mathbb C[y]/(y^r+1)$, by a direct character cancellation.
- The decimation-in-frequency recursion writes the entry of frequency $j$ in slot $\operatorname{rev}_a(j)$ without moving whole indices.
- The two procedures implement exactly $B_tF_t^-$ and $F_t^+B_t^{-1}$, so the opposite transform consumes the stored order.
- On $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^{\ell}\}$ the layout-restoring transform costs $O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right)$ with error below $\sqrt2\ell 2^{-p}$.
- Moving the at most $D(b+1)$ slots to a prefix costs $O(TpdK)$, and the rounds on prefix slots are done as individual butterflies.
- Exchanging the $Dq-1$ width-$K$ chunks to make the participating bits consecutive costs $O(Tp\,pK^{\tau-1})$ by the chunk-swap bound.
- The simultaneous layer then handles all remaining rounds in $O(Tp\ell d^{\lambda'})$ total.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture.; how: reduce integer multiplication to convolution over a polynomial ring, and speed up the data movement and the butterfly layers of its transforms with two new tape procedures that each save a power of the logarithm (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (R4a, R4b, R4c, R4d, R4e, R4f, R4g). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**R4a**: The synthetic transforms satisfy $F_t^+F_t^-=t^{-1}I$ despite zero divisors in $\mathbb C[y]/(y^r+1)$, by a direct character cancellation.
Source: "F_t^+F_t^-=t^{-1}I." (paper)
> \begin{lemma}[Synthetic character cancellation] \label{lem:synthetic-characters} If $j$ is an integer, then \[ \sum_{k=0}^{t-1}\omega_t^{jk} =\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases} \qquad F_t^+F_t^-=t^{-1}I. \] \end{lemma} \begin{proof} Only the second case needs proof. Write $j=2^v j_0$ with $j_0$ odd and $0\leq v<\log_2t$. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$. Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion. Expanding the composite transforms and applying this identity proves the final formula. \end{proof}

**R4b**: The decimation-in-frequency recursion writes the entry of frequency $j$ in slot $\operatorname{rev}_a(j)$ without moving whole indices.
Source: "entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$." (paper)
> After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.

**R4c**: The two procedures implement exactly $B_tF_t^-$ and $F_t^+B_t^{-1}$, so the opposite transform consumes the stored order.
Source: "B_tF_t^-,\qquad F_t^+B_t^{-1}," (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

**R4d**: On $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^{\ell}\}$ the layout-restoring transform costs $O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right)$ with error below $\sqrt2\ell 2^{-p}$.
Source: "O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right)." (paper)
> The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite procedure. \end{lemma} \begin{proof} Put $D=d-1$ and write $a_i=\log_2t_i$. The supplied encoding has $2w=\Theta(p)$ bits per coefficient, so the logical bit volume is $\Theta(Tp)$. Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bm

**R4e**: Moving the at most $D(b+1)$ slots to a prefix costs $O(TpdK)$, and the rounds on prefix slots are done as individual butterflies.
Source: "listed slots, so the moves cost $O(TpdK)$." (paper)
> long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$. A descriptor records the physical position of every named slot. The part of each axis left outside the prefix now consists of $q$ consecutive $K$-bit chunks.

**R4f**: Exchanging the $Dq-1$ width-$K$ chunks to make the participating bits consecutive costs $O(Tp\,pK^{\tau-1})$ by the chunk-swap bound.
Source: "=O\bigl(Tp\,pK^{\tau-1}\bigr)." (paper)
> Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.

**R4g**: The simultaneous layer then handles all remaining rounds in $O(Tp\ell d^{\lambda'})$ total.
Source: "$O(Tp\ell d^{\lambda'})$ in total." (paper)
> For a position $h$ in the remaining chunks, the selected bit has offset $(h-b)\bmod K$, counted from the least significant bit, in each of the $D$ consecutive chunks with the same chunk index $j$. Let $n_P$ and $n_S$ be the numbers of record-address bits before and after that group. Every combination of those bits occurs, so the layer sees the complete address set \[ [P]\times[2^K]^D\times[S],\qquad P=2^{n_P},\quad S=2^{n_S},\quad n_P+DK+n_S=\sum_i a_i\leq D\ell=O(p). \] Thus its record count is $PS2^{DK}=M$ and $\log_2(2M)\leq(C_\ell+1)p=C_Mp$. The current transform parameters supply $p,d,r,K,w$, and the round determines $D,P,S$ and the selected offset $\rho$. Encode these values as the header $\mathcal E$ of Proposition~\ref{prop:simultaneous-layer}. The same fixed descriptor bound covers every axis choice and round. Indeed $|\Gamma(v)|\leq2\log_2v+1$, and $\ell+n_P+n_S\leq d\ell\leq C_\ell p$. Also $d,D\leq\max\{C_\ell,1\}p$, $K,\rho+1\leq p$, and $w\leq C_wp$. Adding the nine code lengths therefore gives \[ |\mathcal E| \leq 2C_\ell p+12\log_2p+ 4\log_2\max\{C_\ell,1\}+2\log_2C_w+9 \leq C_{\rm desc}p. \] The last inequality uses $p\geq1$, $\log_2p\leq p$, and $\log_2x\leq x$ for $x\geq1$. This is the descriptor passed to the layer; the longer table locating named slots remains separate for the transform's address calculations. The simultaneous-layer procedure therefore applies at cost $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](dft.md): The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}, with an opposite-sign inverse F⁺ satisfying F⁺F = I/q, which turns cyclic convolution into a pointwise product: F(u*v) = q·(Fu)(Fv).
  Shown as: Synthetic polynomial transform *<predicate>* Discrete Fourier transform
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md): The ring of complex polynomials of degree < r with y^r = −1, in which multiplying by a power of y permutes the coefficients up to sign, so that powers of y serve as exact roots of unity.
  Shown as: Synthetic polynomial transform *<predicate>* Polynomial ring modulo y^r + 1
- [Two-point butterfly](butterfly.md): The 2×2 averaging step H₀(u,v) = ((u+v)/2, (u−v)/2) from which a power-of-two transform is built by pairing entries k and k+t/2 (decimation in frequency), with the second output multiplied by a twiddle root.
  Shown as: Synthetic polynomial transform *<predicate>* Two-point butterfly
- [Multidimensional (tensor) transform](multidimensional-dft.md): The tensor product F_t = ⊗ F_{t_i} of one-dimensional transforms applied along each axis of an array with axis lengths t₁,…,t_D; moving to many axes of power-of-two length is why the algorithm can use cheap butterflies.
  Shown as: Synthetic polynomial transform *<predicate>* Multidimensional (tensor) transform

## Pages that build on this one

- Convolution over the polynomial ring: Normalized convolution on d−1 axes of arrays with entries in C[y]/(y^r+1): two forward synthetic transforms keeping the same frequency order, pointwise polynomial products (by signed packing) divided by r, and the opposite transform, all using the fast layers and chunk swaps.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
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

- "such a root is a signed shift of the coefficient list." (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$." (paper)

  > For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$. For $z\in\mathcal R_r^t$ and $0\leq j<t$, set \[ (F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k, \qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k. \] Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images. Thus both transforms are contractions. The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$.

- "entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$." (paper)

  > After all $a$ rounds, the named slots from high to low therefore contain the frequency bits from low to high. If $\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$. Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$. The recursion writes its outputs directly in this order; it does not move whole frequency indices.


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

Write the body to `exegenius/tasks/0027-write-synthetic-transform.answer.md` and the JSON to `exegenius/tasks/0027-write-synthetic-transform.answer.json`, then run `exegenius submit 0027-write-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0027-write-synthetic-transform`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
