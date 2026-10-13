# exegenius task 0024-write-main-multiplication

Project directory: `/home/user/openai-nlogn-wiki/runs/M4` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who knows asymptotic notation, algorithm analysis and recursion, discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, sets, permutations, binary representation), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know polynomials and complex numbers including roots of unity, and basic multitape Turing machines. They have not met the fast Fourier transform in depth, convolution theory, Gaussian analysis, fixed-point error control, or the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Convolution (also: cyclic convolution)
- Discrete Fourier transform (also: Fourier transform)
- The n log n optimality conjecture and prior bounds (also: Schönhage–Strassen conjecture)
- Reduction of integer multiplication to convolution (also: radix-digit convolution)
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling (also: Gaussian-resampling reduction)
- Bluestein chirp identity (also: chirp)
- Polynomial ring modulo y^r + 1 (also: C[y]/(y^r+1))
  - $y$ (ring variable): The polynomial variable whose powers serve as roots of unity.
  - $r$ (ring size): The number of complex coefficients in a polynomial of the ring, a power of two.
- Phase twist to the negacyclic ring
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Butterfly map H_0 (also: two-point butterfly)
  - $H_0$ (butterfly map): The map sending a pair (u,v) to ((u+v)/2,(u-v)/2), applied coefficientwise.
- Signed packing of polynomial products (also: Kronecker substitution)
- Linear networks with roles and frames (also: roles, frames)
- Finite network from three-element subsets (also: rank-saving network)
- Recursive power saving
- Fast interchange of address chunks (also: address shear)
- Fast simultaneous butterfly layers
- Precision and exact recovery of the product
- Elementary stream operations and controlled shifts
- Rational matrix shear and triangular factorization
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling)
- Modular arithmetic (also: congruence, residues mod n, Z/nZ)
- Prime numbers and prime powers (also: primes, prime factorization, coprime)
- Chinese remainder theorem (also: CRT)
- Roots of unity (also: nth roots of unity, primitive root of unity, Euler's formula, e^{2 pi i/n})
- Binary representation and bit operations (also: bits, XOR, bit strings, binary expansion)
- Radix (base-b) representation (also: digits in base b, positional notation)
- Schoolbook multiplication and carries (also: long multiplication, carry propagation, grade-school algorithm)
- Recursion and recurrences (also: divide and conquer, recurrence relation, recursive algorithm)
- Matrices and linear maps (also: matrix multiplication, linear transformation, invertible matrix, matrix inverse)
- Rank of a matrix (also: matrix rank, linear independence)
- Triangular matrices (also: lower-triangular matrix, LU factorization)
- Vector spaces and subspaces (also: subspace, dimension, vector space over a field)
- Rational numbers and fields (also: rationals, field, finite field)
- Permutations (also: bijection, partial permutation, index reordering)
- Multidimensional arrays (also: tensors, multi-index arrays, d-dimensional array)
- Finite sets and subsets (also: intersection, union, subset, cardinality)
- Cyclic groups (also: Z_n, cyclic indices, indices modulo n, wraparound)
- Complex magnitude and conjugate (also: absolute value of a complex number, modulus, norm)
- Fixed-point and rounding error (also: rounding, approximation error, precision, bit precision)
- Gaussian function (also: Gaussian, exp(-x^2), bell curve)
- Time and space on tapes (also: tape head movement, linear-time scan, sorting on tapes)
- Inequalities and exponent arithmetic (also: power functions, polynomial in lg n, constants in exponents)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, via radix digits, Chinese-remainder axes, Gaussian resampling, chirps, the twist to the polynomial ring, synthetic transforms accelerated by fast address interchange and butterfly layers, then exact recovery.
Also called: main theorem
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each input integer.
- $\kappa$ (power saving exponent): The fixed constant 2^{-182} giving the saving in the logarithmic factor.

## This page in the argument

The step: A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.
How: reduce the product through a chain of changes of representation down to convolution over a polynomial ring, speed up the transforms with two tape procedures, then recover the exact integer
Why: Each reduction turns the problem into one for which the next fast tool applies, and only the transform data movement and arithmetic need to beat n log n; exactness is restored at the end by known rescalings and rounding. (the sources leave this for the reader to work out: spell it out)
Striking feature: The saving is a strict power $(\lg n)^{-\kappa}$ of the logarithmic factor, with a tiny fixed exponent $\kappa=2^{-182}$, below the conjectured $n\log n$ optimum. (explain why it holds, from the method)

Its sub-steps, in order:

- Splitting the $n$-bit inputs into short radix digits reduces the product to a convolution of digit lists, followed by carry propagation. (on [Reduction of integer multiplication to convolution](radix-digit-reduction.md))
- Address rearrangement of a stored array of volume $V$ and the butterfly layers of the transforms can each be done in time $O(V f^{\theta})$ for a fixed $\theta<1$ in the parameter $f$, instead of linear in $f$.
- Convolution on the remaining axes over $\mathbb C[y]/(y^r+1)$ can be computed with synthetic transforms and polynomial products by an ordinary $O(n\log n)$ multiplier.
- Gaussian resampling expresses each prime-length source Fourier transform through a power-of-two tensor transform, with the coordinate permutations kept in the identity. (on [Gaussian resampling](gaussian-resampling.md))
- Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. (on [Bluestein chirp identity](bluestein-chirp.md))
- The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md))
- A phase twist $x_d\mapsto\zeta y$ changes the last cyclic coordinate into a polynomial modulo $y^r+1$ whose negative wrap gives the original cyclic wrap once the twist is removed. (on [Phase twist to the negacyclic ring](phase-twist.md))
- Known normalizations and digit scales are removed, the coefficient error is strictly below $1/2$, and rounding and carry propagation give the exact binary product. (on [Precision and exact recovery of the product](exact-recovery.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2, S3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2**: Address rearrangement of a stored array of volume $V$ and the butterfly layers of the transforms can each be done in time $O(V f^{\theta})$ for a fixed $\theta<1$ in the parameter $f$, instead of linear in $f$.
How: build each procedure from a fixed linear network applied on role arrays under frames, then use a recursive call that makes $s<Wm$ smaller calls to get a power saving

**S3**: Convolution on the remaining axes over $\mathbb C[y]/(y^r+1)$ can be computed with synthetic transforms and polynomial products by an ordinary $O(n\log n)$ multiplier.
How: evaluate by synthetic transforms using powers of $y$ as roots of unity, multiply pointwise, and compute the polynomial products by signed packing

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Reduction of integer multiplication to convolution](radix-digit-reduction.md)): Splitting the $n$-bit inputs into short radix digits reduces the product to a convolution of digit lists, followed by carry propagation.
- S4 (on [Gaussian resampling](gaussian-resampling.md)): Gaussian resampling expresses each prime-length source Fourier transform through a power-of-two tensor transform, with the coordinate permutations kept in the identity.
- S5 (on [Bluestein chirp identity](bluestein-chirp.md)): Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution.
- S6 (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)): The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- S7 (on [Phase twist to the negacyclic ring](phase-twist.md)): A phase twist $x_d\mapsto\zeta y$ changes the last cyclic coordinate into a polynomial modulo $y^r+1$ whose negative wrap gives the original cyclic wrap once the twist is removed.
- S8 (on [Precision and exact recovery of the product](exact-recovery.md)): Known normalizations and digit scales are removed, the coefficient error is strictly below $1/2$, and rounding and carry propagation give the exact binary product.
- S2.0 (on [Elementary stream operations and controlled shifts](elementary-streams.md)): Permuting, moving, splitting and merging digit streams on a fixed number of tapes takes $O(V)$ steps for volume $V$.
- S2.1 (on [Linear networks with roles and frames](linear-network-frames.md)): A fixed linear network exchanging two banks of values and restoring auxiliary values is applied pointwise on role arrays under invertible frames that cancel along routes, leaving an endpoint operator.
- S2.2 (on [Finite network from three-element subsets](subset-network.md)): A network labelled by nested subspaces from three-element subset intersections has total number $s$ of smaller calls with $s<Wm$.
- S2.3 (on [Recursive power saving](recursive-power-saving.md)): A recursive call at parameter $mf$ using $s<Wm$ calls at parameter $f$ on volume $V/W$ makes the cost per volume grow as a power $m^{\tau}$ less than linear in the parameter.
- S2.4 (on [Fast interchange of address chunks](address-interchange.md)): Two disjoint address fields of $u$ bits of an array of volume $V$ can be interchanged in time $O(Vu^{\tau})$ with $\tau<1$, although only XOR combinations are formed on the way.
- S2.5 (on [Fast simultaneous butterfly layers](fast-butterfly-layers.md)): The map $H_0$ can be applied to the same bit of up to $d$ address chunks of an array of volume $V$ at once, at cost $O(Vd^{\lambda'})$ with $\lambda'<1$.
- S3.1 (on [Polynomial ring modulo y^r + 1](polynomial-ring-y-r.md)): Over $\mathbb C[y]/(y^r+1)$ with $r$ a power of two, multiplying by $y^a$ permutes coefficients and changes some signs, so powers of $y$ act as roots of unity.
- S3.2 (on [Synthetic polynomial transforms](synthetic-transforms.md)): Synthetic transforms use $\omega_t=y^{2r/t}$ as roots, built from signed shifts and two-point butterflies, and the same stored frequency order is retained through pointwise product and inverse.
- S3.3 (on [Signed packing of polynomial products](signed-packing.md)): Polynomial products use signed packing of coefficients into long integers and an ordinary $O(N\log N)$ integer multiplier as a subroutine.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Convolution](convolution.md)
- [Discrete Fourier transform](fourier-transform.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The n log n optimality conjecture and prior bounds](nlogn-conjecture.md): Schönhage and Strassen proposed n log n as the optimal multiplication time; Harvey and van der Hoeven reached O(n log n) in the multitape model.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The n log n optimality conjecture and prior bounds
- [Reduction of integer multiplication to convolution](radix-digit-reduction.md): Split each integer into short radix digits so the product becomes a convolution of digit lists, followed by carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Reduction of integer multiplication to convolution
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md): Index re-mapping that turns a long cyclic convolution into a multidimensional one over axes of distinct prime lengths.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder map to prime cyclic axes
- [Gaussian resampling](gaussian-resampling.md): Expresses a Fourier transform of prime length through a multidimensional transform with power-of-two axis lengths.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Gaussian resampling
- [Bluestein chirp identity](bluestein-chirp.md): Rewrites a Fourier transform as a convolution with a chirp (quadratic-phase) sequence.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein chirp identity
- [Phase twist to the negacyclic ring](phase-twist.md): A diagonal phase multiplication turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap once the twist is removed.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Phase twist to the negacyclic ring
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier-type transforms over the polynomial ring using powers of y as roots of unity, built from signed shifts and two-point butterflies.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Synthetic polynomial transforms
- [Signed packing of polynomial products](signed-packing.md): Packing coefficients into long integers with signs so a polynomial product is computed by an ordinary O(n log n) integer multiplier.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Signed packing of polynomial products
- [Fast interchange of address chunks](address-interchange.md): Exchanging two address fields of u bits by XOR-combinations (address shears) at cost O(V u^τ) with τ<1, though the final effect is an exact permutation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fast interchange of address chunks
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md): Applying the butterfly map to the same bit of up to d address chunks at once on numerical arrays, at cost O(V d^λ') with λ'<1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fast simultaneous butterfly layers
- [Precision and exact recovery of the product](exact-recovery.md): Fixed-point arithmetic with controlled error: removing known normalizations leaves coefficient error below 1/2, so rounding and carry propagation give the exact binary product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Precision and exact recovery of the product
- [Elementary stream operations and controlled shifts](elementary-streams.md): Linear-time tape scans that permute, move, split and merge digit streams, and add controlled offsets modulo a prime power.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Elementary stream operations and controlled shifts

## Other pages you may link to

- [Convolution](convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-y-r.md)
- [Butterfly map H_0](butterfly-h0.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Finite network from three-element subsets](subset-network.md)
- [Recursive power saving](recursive-power-saving.md)
- [Rational matrix shear and triangular factorization](matrix-shear.md)

## Evidence from the sources, with the paragraph around each quote

- "in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "The complete time bound" (paper)

  > \subsection{The complete time bound}

- "These constants are deliberately conservative; no optimization is claimed." (paper)

  > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.


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

Write the body to `exegenius/tasks/0024-write-main-multiplication.answer.md` and the JSON to `exegenius/tasks/0024-write-main-multiplication.answer.json`, then run `exegenius submit 0024-write-main-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0024-write-main-multiplication`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
