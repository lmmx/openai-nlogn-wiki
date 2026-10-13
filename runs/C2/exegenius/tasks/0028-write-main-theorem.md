# exegenius task 0028-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/C2` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithm design (divide and conquer, recurrences), discrete mathematics (sets, subsets, binary representation, modular arithmetic, primes, gcd), and linear algebra (vector spaces, subspaces, matrices, rank, orthogonal projection, invertible matrices). They have met complex numbers, polynomials and basic Turing machines, but not the fast-multiplication literature, Fourier analysis beyond basics, or advanced algebra and coding theory.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Integer multiplication complexity and the n log n conjecture
- Convolution
- Discrete Fourier transform and butterflies
- Multiplication by radix-digit convolution
- Chinese-remainder map to prime cyclic axes
- Multidimensional transform
- Gaussian resampling
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The indeterminate whose powers serve as roots of unity.
  - $r$ (ring size): The power of two giving the number of coefficients in a polynomial; y^r+1 = 0.
- Last-coordinate phase twist
- Synthetic polynomial transforms
- Packed polynomial products
- Tape scans and address layout
- Address rearrangement cost
- Linear networks, roles and frames
- Finite network from three-element subsets
- Recursive saving giving a power of log
- Rational matrix shear and lower-triangular factorization
- Controlled shifts and rational scalings
- Packed selected-bit addition
- Fast address-field interchange
  - $V$ (stored bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (cost exponent): A fixed constant below 1 giving the power saving.
- Fixed-point complex dyadics
- Simultaneous butterfly layers
  - $H_0$ (butterfly map): The map sending (u,v) to ((u+v)/2,(u-v)/2).
  - $V$ (stored bit volume): The number of stored bits in the arrays.
  - $d$ (chunk count): The number of equal-width address chunks in which one bit position is selected.
  - $\lambda'$ (cost exponent): A fixed constant below 1 giving the power saving.
- Precision analysis and exact recovery
- Recurrence relations and the master theorem (also: recurrence, divide and conquer recurrence, master theorem)
- Binary representation of integers (also: bits, binary expansion, bit strings, radix representation)
- Modular arithmetic (also: congruence, residues, mod, remainder)
- Chinese remainder theorem (also: CRT)
- Prime numbers, gcd and Euclidean algorithm (also: coprime, relatively prime, extended Euclidean algorithm, gcd, modular inverse)
- Vector spaces, subspaces and linear maps (also: linear algebra, subspace, basis, dimension, linear map, orthogonal complement)
- Matrices, rank and invertibility (also: matrix rank, invertible matrix, diagonal matrix, GL, projection matrix, permutation matrix, matrix product)
- Gaussian elimination (also: row reduction, row operations)
- Sets, subsets, functions and permutations (also: bijection, index set, finite set, cardinality, support)
- Floor, ceiling, logarithms and rounding (also: floor, ceiling, lg, log base 2, rounding to nearest integer)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2 pi i/n})
- Cyclic groups and products of groups (also: Z/nZ, cyclic axis, direct product, abelian group)
- Multidimensional arrays and mixed-radix indexing (also: tensor, array indexing, row-major order, index tuple)
- Basic probability and counting bounds (also: averaging argument, pigeonhole principle, counting)
- Norms, error bounds and triangle inequality (also: absolute value of complex number, modulus, max norm, error analysis, rounding error)
- Fixed-point and finite precision arithmetic (also: truncation, dyadic rationals, binary fraction)
- Integer addition, multiplication and carry propagation (also: schoolbook multiplication, carry, long multiplication, linear-time addition)
- Sorting and linear tape scans (also: tape sorting, merge sort, sequential scan)
- Constants, asymptotic functions and polylog factors (also: polylogarithm, log log n, little-o, Theta, Omega)
- XOR and bitwise operations (also: exclusive or, bitwise addition mod 2, GF(2))

## This page

Concept: Integer multiplication in O(n (lg n)^(1-κ)) time
Gloss: Deterministic multitape TM multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, disproving the n log n conjecture in that model.
Heading: Multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits of each integer.
- $\kappa$ (saving exponent): The constant 2^{-182} giving the power saving in the log factor.

## This page in the argument

The step: A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: reduce to convolution, accelerate transforms by two network-based tape procedures, then recover the product
Why: Beating n log n needs a power saving in the log factor, which requires cheaper transform levels (S3) inside the standard multiplication-by-convolution reduction (S2, S4) with exact recovery (S5). (the sources do not say this: give the reader the reason)
Striking feature: $\kappa=2^{-182}$ is an astronomically small exponent; it is the product of the saving exponents from the recursions, so only a tiny power of log is saved. (explain why it holds, from the method)

Its sub-steps, in order:

- Schönhage and Strassen conjectured that $n\log n$ is the optimal order of multiplication cost, and Harvey and van der Hoeven reached $O(n\log n)$, so only a power saving in the log factor can beat it. (on [Integer multiplication complexity and the n log n conjecture](multiplication-history.md))
- Splitting both integers into radix digits reduces multiplication to convolution of short integer coefficient lists. (on [Multiplication by radix-digit convolution](digit-convolution-reduction.md))
- Two tape procedures, a fast address-field interchange and a simultaneous butterfly layer, cheapen both data movement and arithmetic of the transform levels.
- The digit convolution reduces, by a chain of changes of problem and representation, to convolution over $\mathbb C[y]/(y^r+1)$.
- The approximate transforms recover the exact integer product, and the total cost is $O(n(\lg n)^{1-\kappa})$.
- The power saving gives a limit of zero for $T_A(n)/(n\lg n)$, so the $n\log n$ lower bound conjecture fails in this model.

## Steps this page derives

The argument gives this page these sub-steps of its step (S3, S4, S5, S6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3**: Two tape procedures, a fast address-field interchange and a simultaneous butterfly layer, cheapen both data movement and arithmetic of the transform levels.
How: supply two fast procedures from one linear-network construction
- S3.2: Both tape procedures come from a fixed linear network whose total number $s$ of smaller calls is less than $Wm$, and the recursion on it saves a power of the parameter.
  How: build a finite network with a rank deficit, then recurse on it
- S3.3: Two disjoint contiguous address fields of $u$ bits in an array of volume $V$ can be interchanged in time $O(Vu^\tau)$ with a fixed $\tau<1$.
  How: instantiate the bit network with rational subspaces and implement edges by address shears

**S4**: The digit convolution reduces, by a chain of changes of problem and representation, to convolution over $\mathbb C[y]/(y^r+1)$.
How: chain of reductions: prime cyclic axes, power-of-two axes, polynomial ring
- S4.5: Convolution over the remaining axes is computed over $\mathbb C[y]/(y^r+1)$ by forward synthetic transforms, pointwise ring products and the opposite transform.
  How: transform, multiply pointwise, transform back

**S5**: The approximate transforms recover the exact integer product, and the total cost is $O(n(\lg n)^{1-\kappa})$.
How: bound the rounding error below 1/2 and then add up costs
- S5.2: A compatible choice of rational parameters makes all terms in the cost table fit $O(n(\lg n)^{1-\kappa})$.
  Source: "\subsection{The complete time bound}" (paper)
  > \subsection{The complete time bound}

**S6**: The power saving gives a limit of zero for $T_A(n)/(n\lg n)$, so the $n\log n$ lower bound conjecture fails in this model.
Source: "The power saving proved here gives a limit of zero through all input lengths," (paper)
> Sch\"onhage and Strassen conjectured $n\log n$ as the optimal order of multiplication cost~\cite[Section~1]{SchonhageStrassen1971}. In the present fixed-tape model, an eventual lower bound for every multiplication machine means that, for each fixed machine $A$, there are constants $c_A>0$ and $N_A$ such that $T_A(n)\ge c_A n\lg n$ whenever $n\ge N_A$. Its negation requires one machine satisfying $\liminf_{n\to\infty}T_A(n)/(n\lg n)=0$. The power saving proved here gives a limit of zero through all input lengths, which is a stronger conclusion.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Integer multiplication complexity and the n log n conjecture](multiplication-history.md)): Schönhage and Strassen conjectured that $n\log n$ is the optimal order of multiplication cost, and Harvey and van der Hoeven reached $O(n\log n)$, so only a power saving in the log factor can beat it.
- S2 (on [Multiplication by radix-digit convolution](digit-convolution-reduction.md)): Splitting both integers into radix digits reduces multiplication to convolution of short integer coefficient lists.
- S3.1 (on [Address rearrangement cost](address-interchange-bottleneck.md)): Moving data between $\Theta(\log n)$ transform levels costs $\Theta(n\log n)$ by plain scanning, so both movement and arithmetic must be made cheaper.
- S3.2.1 (on [Linear networks, roles and frames](linear-network-roles.md)): A fixed linear network exchanges two banks of values with signs and restores auxiliary values; each wire has a role and invertible frames $D_v$ change its stored representation, cancelling across the network.
- S3.2.2 (on [Finite network from three-element subsets](finite-subset-network.md)): A fixed finite network with nested subspaces attached to gates, built from three-element subsets with gather/scatter and cancelling auxiliary wires, makes the total number $s$ of smaller calls satisfy $s<Wm$.
- S3.2.3 (on [Recursive saving giving a power of log](recursive-saving.md)): A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ each, so cost per volume grows by $s/W<m$ per multiplication of the parameter by $m$, a power saving.
- S3.3.1 (on [Rational matrix shear and lower-triangular factorization](address-shear-factorization.md)): Every rational matrix factors as lower-triangular times partial permutation times lower-triangular, so an address shear $(H,D)\mapsto(H+D,D)$ costs by rank.
- S3.3.2 (on [Fast address-field interchange](fast-address-interchange.md)): Interchanging two address fields via XOR combinations of data and address shears costs $O(Vu^\tau)$ with $\tau<1$, the final effect being an exact permutation.
- S3.4 (on [Simultaneous butterfly layers](fast-butterfly-layers.md)): Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ simultaneously to selected coordinate bits of numerical arrays costs $O(Vd^{\lambda'})$ with a fixed $\lambda'<1$.
- S4.1 (on [Chinese-remainder map to prime cyclic axes](cyclic-crt-axes.md)): The radix-digit list is placed on a product of cyclic axes of distinct prime lengths by a Chinese-remainder address map that preserves convolution.
- S4.2 (on [Gaussian resampling](gaussian-resampling.md)): Gaussian resampling expresses each prime-length Fourier transform through a power-of-two tensor transform with source and target permutations retained.
- S4.3 (on [Bluestein chirp identity](bluestein-chirp.md)): Bluestein's chirp identity turns the middle transform into a normalized cyclic convolution multiplied by chirp phases.
- S4.4 (on [Last-coordinate phase twist](phase-twist.md)): A last-coordinate phase twist turns a cyclic coordinate into a polynomial coordinate modulo $y^r+1$; removing the twist restores the cyclic wrap.
- S4.5.1 (on [Synthetic polynomial transforms](synthetic-transforms.md)): Synthetic polynomial transforms use powers of $y$ as roots of unity, so twiddles are signed shifts, and two forward transforms retain one frequency order through the pointwise product.
- S4.5.2 (on [Packed polynomial products](normalized-ring-products.md)): Pointwise polynomial products in the ring are computed by signed packing (Kronecker substitution) and the standard $O(n\log n)$ multiplier as an ordinary subroutine.
- S5.1 (on [Precision analysis and exact recovery](precision-exact-recovery.md)): The known normalizations and digit scales are removed, the recovered coefficient error is strictly below $1/2$, and carries are propagated to give the exact binary product.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Recursive saving giving a power of log](recursive-saving.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Convolution](convolution.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Integer multiplication complexity and the n log n conjecture](multiplication-history.md): Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Integer multiplication complexity and the n log n conjecture
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven identity expressing a Fourier transform of prime-length axes through a power-of-two tensor transform, with source and target permutations.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Gaussian resampling
- [Bluestein chirp identity](bluestein-chirp.md): Rewrites a Fourier transform of arbitrary length as a convolution multiplied by chirp phases.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Bluestein chirp identity
- [Last-coordinate phase twist](phase-twist.md): Multiplying by diagonal phases so a cyclic coordinate becomes a negative-wrap (mod y^r+1) coordinate; removing the twist restores cyclic wrap.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Last-coordinate phase twist
- [Synthetic polynomial transforms](synthetic-transforms.md): Nussbaumer-style transforms using powers of y as roots of unity so each twiddle multiplication is a shift.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Synthetic polynomial transforms
- [Packed polynomial products](normalized-ring-products.md): Pointwise polynomial products in the ring computed via signed packing (Kronecker substitution) and the standard O(n log n) multiplier as a subroutine.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Packed polynomial products
- [Fast address-field interchange](fast-address-interchange.md): Interchanges two contiguous address fields via XOR combinations of data and address shears, with an exact final permutation.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Fast address-field interchange
- [Simultaneous butterfly layers](fast-butterfly-layers.md): Applies H_0(u,v)=((u+v)/2,(u-v)/2) to selected coordinate bits of numerical arrays, via the linear network, at cost O(V d^λ').
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Simultaneous butterfly layers
- [Precision analysis and exact recovery](precision-exact-recovery.md): Bounds the rounding error of the whole fixed-point pipeline strictly below 1/2, removes normalizations and propagates carries.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Precision analysis and exact recovery
- [Multiplication by radix-digit convolution](digit-convolution-reduction.md): Split each integer into radix digits, convolve digit lists, then recover exact integer by rounding, rescaling and carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Multiplication by radix-digit convolution

## Other pages you may link to

- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring-negacyclic.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Multidimensional transform](multidim-transform.md)
- [Fixed-point complex dyadics](fixed-point-dyadics.md)
- [Chinese-remainder map to prime cyclic axes](cyclic-crt-axes.md)
- [Tape scans and address layout](tape-streams.md)
- [Address rearrangement cost](address-interchange-bottleneck.md)
- [Linear networks, roles and frames](linear-network-roles.md)
- [Finite network from three-element subsets](finite-subset-network.md)
- [Recursive saving giving a power of log](recursive-saving.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Rational matrix shear and lower-triangular factorization](address-shear-factorization.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)

## Evidence from the sources, with the paragraph around each quote

- "The complete time bound" (paper)

  > \subsection{The complete time bound}

- "These constants are deliberately conservative; no optimization is claimed." (paper)

  > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "disproves the $n\log n$ optimality conjecture" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


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

Write the body to `exegenius/tasks/0028-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0028-write-main-theorem.answer.json`, then run `exegenius submit 0028-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0028-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
