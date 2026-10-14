# exegenius task 0042-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2B` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent in asymptotic analysis, discrete mathematics (sets, functions, modular arithmetic, primes and gcd, permutations, induction and recursion), first-course linear algebra (matrices, invertibility, rank, basis, dimension, linear maps over the rationals and the complex numbers), complex arithmetic with Euler's formula, and the basic Turing machine model with tapes and step counting. They have seen binary representation, bit operations such as XOR, and perhaps the idea of multiplying integers by divide and conquer, but have not been taught the discrete Fourier transform, the FFT, polynomial transforms, Schönhage–Strassen, abstract ring theory beyond the basic definition, tensor products, or numerical error analysis, and these are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- The n log n optimality conjecture
- Fixed finite-tape Turing machine model
- Arrays, address fields and elementary scans
- Controlled cyclic shifts and rational scalings
- Integer multiplication as digit convolution
- Normalized DFT and cyclic convolution
- Multidimensional (tensor) Fourier transform
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Fixed-point disk-grid arithmetic and contractions
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomials, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Synthetic Fourier transform modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomial ring, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Radix-2 butterfly layers and stored frequency order
- Twist from cyclic to negacyclic convolution
- Established n log n multiplier as a subroutine
- Signed Kronecker packing of polynomial products
- Bluestein's chirp identity
- Resampling with the permutations left in the transform
- Chirp identity and source-permutation cancellation
- Three-element subset intersection gadget
- Linear network that exchanges two banks and restores scratch values
- Frames and the common-frame identity
- Orthogonal complements and projections in a bilinear space
- Nested subspace labels and the rank saving
- Lower-triangular rank factorization
- Cost of a rational matrix shear
- Power-width chunk interchange in O(Ve^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $e$ (chunk width): the number of radix digits in each of the two interchanged chunks, a power of a fixed integer m.
  - $\tau$ (interchange exponent): a fixed rational constant strictly between 0 and 1.
- Chunk interchange in O(Vu^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $u$ (chunk width): the number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-50}.
- Two-point kernel C and the complex phase network
- Packed XOR of selected bits across address chunks
- Simultaneous butterfly layer in O(Vd^λ') time
  - $V$ (stored bit volume): the number of data bits stored in the array of records.
  - $d$ (axis count): the number of equal-width address chunks (transform axes) whose selected bit is butterflied simultaneously.
  - $\lambda'$ (layer exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-54}.
- Layout and cost of the synthetic transform
- Convolution over the polynomial ring from the retained layout
- Source transform via resampling, chirp and ring convolution
- Choice of sizes, precision and prime axis lengths
- Exact recovery: scaling, rounding and carries
- The multiplication algorithm
- Cost accounting and the saving exponent κ
  - $\kappa$ (saving exponent): the fixed constant 2^{-182} by which the power of the logarithm is reduced below 1.
- Modular arithmetic and residues (also: congruence, mod q, Z/qZ, integers modulo q, remainder)
- Primes, divisibility, gcd and coprimality (also: prime number, coprime, relatively prime, pairwise coprime, greatest common divisor, odd prime, units mod q, invertible residue)
- Binary representation of integers (also: bit string, radix 2, binary expansion, most significant bit, val(x), bin_k(z), padding with zeros, base-2 digits)
- Bitwise XOR (also: exclusive or, XOR combination, addition mod 2, parity)
- Logarithms, floors, ceilings and powers of two (also: lg, log base 2, floor, ceiling, power of two, exponent rules)
- Matrices, invertibility and rank (also: invertible matrix, matrix inverse, matrix product, rank of a matrix, linear map, linear transformation, Gaussian elimination, row operations)
- Vector spaces, basis and dimension (also: subspace, span, linear independence, linear combination, vector space over the rationals, dimension, standard basis, direct sum)
- Permutations and permutation matrices (also: bijection, reordering of indices, sorting by a permutation, permutation of coordinates, identity matrix)
- Lexicographic order and index tuples (also: dictionary order, Cartesian product of index sets, multi-index, mixed-radix positional notation, row-major order)
- Euler's formula and roots of unity as points on the unit circle (also: e^{i theta}, cos and sin form, unit circle, primitive root of unity, modulus of a complex number, complex conjugate, real and imaginary parts)
- Geometric series and orthogonality of sums of roots of unity (also: geometric sum, sum of powers of a root of unity vanishes, summation manipulation, Kronecker delta, indicator function)
- Norms and the triangle inequality (also: absolute value bound, sup norm, maximum norm, Euclidean norm, error bound, triangle inequality, operator norm)
- Rational numbers, dyadic rationals and exact arithmetic (also: dyadic number, dyadic rational, power-of-two denominator, Gaussian rational, Gaussian integer, rounding to nearest integer, truncation toward zero)
- Algebraic structures: groups, rings and isomorphisms (also: ring, commutative ring, algebra, ring isomorphism, group, cyclic group, zero divisor, unit, field)
- Discrete-math proof techniques (also: induction, recursion, recurrence relation, divide and conquer, proof by cases, pigeonhole principle, counting arguments)
- Schoolbook multiplication and divide-and-conquer multiplication (also: long multiplication, quadratic-time multiplication, Karatsuba, carry propagation, digit-by-digit addition)
- Multitape machine cost model and linear-time scans (also: sequential tape access, tape scan, head movement cost, one-pass copy, linear-time tape operations, sorting by merging, bit-level time complexity)
- Complex polynomial evaluation and interpolation (also: evaluating a polynomial at points, coefficient list, degree, polynomial identity, Horner's rule, coefficient extraction)
- Gaussian function (also: bell curve, exp(-x^2), normal density, Gaussian weight)
- Convolution as polynomial multiplication (also: convolution of sequences, sum over i+j=k, linear convolution, Cauchy product, coefficient of a product)
- Quantifiers, sets and basic asymptotic notation beyond big-O (also: little-o, Theta, Omega, sufficiently large n, for all n, worst-case time, lower bound versus upper bound)

## This page

Concept: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time
Gloss: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, using fast address-chunk interchange and simultaneous butterfly layers to speed synthetic transforms inside a Gaussian-resampling multiplication.
Heading: Multiplying $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): the number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent): the fixed constant 2^{-182} by which the power of the logarithm is reduced below 1.

## This page in the argument

The step: A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.
How: Start from the Gaussian-resampling reduction of integer multiplication to convolution; replace the two costly operations of the synthetic transforms (address rearrangement and butterfly layers) by faster procedures built from one recursive linear-network exchange, assemble the exact algorithm, and account for its cost.
Why: Scanning the whole array at each of the logarithmically many transform levels already costs $n\log n$, so both movement and arithmetic must be sped up. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The saving $\kappa=2^{-182}$ is minuscule but positive: every one of the many cost terms is a power of $p$ below $p^{1-2\kappa}$, so a fixed power of $\log n$ is saved rather than any larger factor. (explain why it holds, from the method)

Its sub-steps, in order:

- Elementary address manipulations on a fixed-tape machine cost time linear in the stored volume $V$.
- There are two fixed linear networks that exchange two banks of values, restore every scratch value, and allow subspace labels whose edge changes total fewer than $Wm$ smaller operations.
- Two disjoint address chunks of $u$ bits in any bit array can be interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$. (on [Chunk interchange in O(Vu^τ) time](chunk-swap.md))
- One normalized butterfly $H_0$ applied to the same bit position in each of $d$ address chunks of polynomial records is computed exactly, then truncated once, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$. (on [Simultaneous butterfly layer in O(Vd^λ') time](simultaneous-butterfly-layer.md))
- Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ is computed from the retained transform layout with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time. (on [Convolution over the polynomial ring from the retained layout](ring-convolution.md))
- Gaussian resampling can express the transforms of pairwise coprime lengths through power-of-two transforms while the source and target permutations are never executed as separate sorts.
- The multiplication algorithm, run on $x\#y$, outputs exactly the $2n$-bit product of the two $n$-bit integers. (on [The multiplication algorithm](multiplication-algorithm.md))
- The total running time of the machine is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$. (on [Cost accounting and the saving exponent κ](cost-accounting.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1, S2, S6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: Elementary address manipulations on a fixed-tape machine cost time linear in the stored volume $V$.
How: State the two linear-time primitives that every later procedure calls: scans that split and merge streams, and controlled cyclic shifts of a later field.

**S2**: There are two fixed linear networks that exchange two banks of values, restore every scratch value, and allow subspace labels whose edge changes total fewer than $Wm$ smaller operations.
How: Build the three-stage bank-exchange network from the subset-intersection gadgets, state the common-frame invariant for arrays on wires, attach nested subspace labels, and read off the bit (matrix) and complex (phase) interfaces.

**S6**: Gaussian resampling can express the transforms of pairwise coprime lengths through power-of-two transforms while the source and target permutations are never executed as separate sorts.
How: Keep the source and target permutations inside the tensor transform identity, then use a chirp identity for the middle power-of-two transform and cancel the source permutation across the product.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3 (on [Chunk interchange in O(Vu^τ) time](chunk-swap.md)): Two disjoint address chunks of $u$ bits in any bit array can be interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$.
- S4 (on [Simultaneous butterfly layer in O(Vd^λ') time](simultaneous-butterfly-layer.md)): One normalized butterfly $H_0$ applied to the same bit position in each of $d$ address chunks of polynomial records is computed exactly, then truncated once, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.
- S5 (on [Convolution over the polynomial ring from the retained layout](ring-convolution.md)): Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ is computed from the retained transform layout with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time.
- S7 (on [The multiplication algorithm](multiplication-algorithm.md)): The multiplication algorithm, run on $x\#y$, outputs exactly the $2n$-bit product of the two $n$-bit integers.
- S8 (on [Cost accounting and the saving exponent κ](cost-accounting.md)): The total running time of the machine is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.
- S1.1 (on [Arrays, address fields and elementary scans](stream-arrays.md)): Fixed digit permutations, digit moves, pointwise maps on split streams and cyclic row splits each take $O(V)$ steps for $V$ stored bits.
- S1.2 (on [Controlled cyclic shifts and rational scalings](controlled-shifts.md)): Adding an offset computed from earlier control fields to a later target field modulo $q^b$, or multiplying it by a fixed unit, costs $O(V)$.
- S2.1 (on [Linear network that exchanges two banks and restores scratch values](bank-exchange-network.md)): Three stages of forward invocations send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ and restore every auxiliary scratch value, whatever its initial contents.
- S2.2 (on [Frames and the common-frame identity](frames.md)): If every wire's array is stored in a frame $D_v$ common to all incidences of a gate, pointwise linear gates commute with the frame, so the network implements $D_{\rm out}\,\mathsf S\,D_{\rm in}^{-1}$ and only edge changes $D_vD_u^{-1}$ cost anything.
- S2.3 (on [Nested subspace labels and the rank saving](subspace-labels.md)): Subspaces of an $m$-dimensional space can be attached to the gates and terminals so adjacent labels are nested and the total number $s$ of smaller operations on edges is strictly below $Wm$.
- S2.4 (on [Two-point kernel C and the complex phase network](phase-kernel-network.md)): On the complex network with binary labels each edge's phase-frame change is a product of translation kernels $aI+bX_v$, one per residual basis vector, and the total number of such factors is $s_{\rm c}<W_{\rm c}m$; telescoping gives $C^{\otimes m}$ on every role.
- S6.1 (on [Resampling with the permutations left in the transform](resampling-no-sort.md)): For coprime lengths $s<t$ the coordinate permutations $P_s,P_t$ stay inside the identity $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, and tensoring it over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with line-wise maps costing $O(dTp^{3/2+\delta}\alpha)$.
- S6.2 (on [Chirp identity and source-permutation cancellation](chirp-permutation-cancel.md)): The chirp identity $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$ evaluates the target-permuted transform without applying $Q$, and the source permutation cancels: $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Three-element subset intersection gadget](triple-gadget.md)
- [Gaussian resampling](gaussian-resampling.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Split into radix digits, map by Φ to prime axes, take two source transforms, multiply pointwise, apply the opposite-sign transform with the two scalings by S, round, undo Φ, and propagate carries to output the 2n-bit product.
  Shown as: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time *<predicate>* The multiplication algorithm
- [Cost accounting and the saving exponent κ](cost-accounting.md): A table of costs divided by Tp, each at most p^{1−2κ} thanks to the slack in the chosen exponents (seven dominant margins, the smallest 2^{-181} = 2κ), giving O(n (log n)^{1−κ}) overall.
  Shown as: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time *<predicate>* Cost accounting and the saving exponent κ
- [The n log n optimality conjecture](n-log-n-conjecture.md): Schönhage and Strassen's conjecture that n log n is the optimal order of growth for the time to multiply two n-bit integers on a multitape Turing machine.
  Shown as: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time *<predicate>* The n log n optimality conjecture
- [Fixed finite-tape Turing machine model](fixed-tape-model.md): One machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads and writes one cell per tape and moves each head by at most one cell, and cost is the number of steps.
  Shown as: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time *<predicate>* Fixed finite-tape Turing machine model

## Other pages you may link to

- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Three-element subset intersection gadget](triple-gadget.md)
- [Linear network that exchanges two banks and restores scratch values](bank-exchange-network.md)
- [Established n log n multiplier as a subroutine](nlogn-subroutine.md)
- [Arrays, address fields and elementary scans](stream-arrays.md)
- [Frames and the common-frame identity](frames.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Orthogonal complements and projections in a bilinear space](bilinear-orthogonal.md)
- [Nested subspace labels and the rank saving](subspace-labels.md)
- [Lower-triangular rank factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width chunk interchange in O(Ve^τ) time](power-width-interchange.md)
- [Chunk interchange in O(Vu^τ) time](chunk-swap.md)
- [Packed XOR of selected bits across address chunks](packed-selected-bits.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing of polynomial products](signed-kronecker-packing.md)
- [Fixed-point disk-grid arithmetic and contractions](fixed-point-disk-grid.md)
- [Normalized DFT and cyclic convolution](dft-cyclic-convolution.md)
- [Multidimensional (tensor) Fourier transform](multidim-transform.md)
- [Chinese-remainder map to prime cyclic axes](crt-axis-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Twist from cyclic to negacyclic convolution](coefficient-twist.md)
- [Synthetic Fourier transform modulo y^r + 1](synthetic-transform.md)
- [Radix-2 butterfly layers and stored frequency order](butterfly-layers.md)
- [Two-point kernel C and the complex phase network](phase-kernel-network.md)
- [Simultaneous butterfly layer in O(Vd^λ') time](simultaneous-butterfly-layer.md)
- [Layout and cost of the synthetic transform](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Resampling with the permutations left in the transform](resampling-no-sort.md)
- [Chirp identity and source-permutation cancellation](chirp-permutation-cancel.md)
- [Choice of sizes, precision and prime axis lengths](parameter-choice.md)
- [Source transform via resampling, chirp and ring convolution](source-transform.md)
- [Exact recovery: scaling, rounding and carries](exact-recovery.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


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

Write the body to `exegenius/tasks/0042-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0042-write-main-theorem.answer.json`, then run `exegenius submit 0042-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0042-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
