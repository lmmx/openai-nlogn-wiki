# exegenius task 0043-write-ring-convolution

Project directory: `/home/user/openai-nlogn-wiki/runs/O1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: algorithms and data structures (asymptotic analysis, recurrences and divide-and-conquer, sorting including stable radix sort, amortized counting, schoolbook and Karatsuba multiplication, and the textbook FFT for polynomial multiplication), theory of computation (Turing machines, tapes, deterministic machines, Boolean circuits, worst-case time and lower bounds), and discrete mathematics (sets, permutations, subsets and counting, induction, graphs, modular arithmetic, gcd, primes and the Chinese remainder theorem). From the supporting mathematics they have first-year calculus (limits, logarithms and exponentials, geometric series, Newton's method), introductory linear algebra (matrices, inverses, transposes, triangular and permutation matrices, eigenvalues, dot products and orthonormal bases) and complex numbers, plus the machine-level number representations of computer organization (binary and radix digits, two's complement, bitwise XOR, carries). They have not studied the research literature on fast integer multiplication, Gaussian resampling, synthetic polynomial transforms, multilinear algebra beyond the basics, bilinear-form theory, analytic number theory, or index coding.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Linear maps, matrices and rank (also: rank, F2-linear algebra)
- Tensor product
- Nondegenerate bilinear forms and orthogonal complements (also: orthogonal complement, orthonormal basis)
- n log n optimality conjecture
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- Harvey–van der Hoeven multiplier (also: established multiplier)
- Lexicographic array layout and logical volume (also: address field, row, logical volume)
- Elementary stream operations
- Controlled shifts (also: prefix-controlled cyclic shift)
- Scratch restoration (also: transparent computation)
- Three-element-subset intersection construction (also: Frankl–Wilson construction, gather and scatter)
- Bank-exchange linear network (also: finite network, role, bit network, complex network)
- Row splitting into role streams
- Frames and the common-frame identity
- Subspace labels and orthogonal residuals (also: labels, rank budget)
- Rank deficit and recursive power saving
- Lower triangular factorization (also: Bruhat factorization)
- Rational address shear (also: matrix shear)
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Normalized discrete Fourier transform (also: DFT)
- Cyclic convolution
- Multidimensional Fourier transform
- Radix-digit reduction to convolution
- Disk-grid fixed-point arithmetic (also: Gaussian dyadic, truncation Q_p)
- Error accounting through contractions
- Gaussian resampling
- Resampling with retained permutations
- Bluestein chirp identity (also: Bluestein's algorithm)
- Source-permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The formal polynomial variable, whose powers act as roots of unity in the ring.
  - $r$ (record length): The number of complex coefficients in one ring element, a power of two.
- Coefficient phase twist
- Normalized butterfly (also: H_0, two-point butterfly)
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic roots of unity)
- Binary phase frames (also: phase kernel C)
- Packed selected-bit addition (also: deterministic repair)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Synthetic transform layout and cost
- Signed Kronecker packing (also: Kronecker substitution)
- Exact recovery by rounding and carries
- Parameter choice and cost table
- Asymptotic notation beyond big-O (also: Big-Theta, Big-Omega, little-o, Θ, Ω, o(·), eventually, for sufficiently large n)
- Logarithms and exponentials (also: log, lg, log_2, natural logarithm, ln, exp, e)
- Floor and ceiling (also: ⌊x⌋, ⌈x⌉, integer part, rounding down, rounding up)
- Limits and liminf (also: limit, lim, liminf, limit inferior, tends to infinity, → ∞)
- Geometric series (also: geometric sum, geometrically increasing precisions)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Recurrences and divide-and-conquer analysis (also: recurrence relation, recursion, recursion tree, master theorem, divide and conquer, recursive call)
- Worst-case running time (also: time complexity, worst-case time, T_A(n), bit complexity, running time)
- Lower bounds for computational problems (also: lower bound, optimality, Ω(n log n) lower bound)
- Deterministic algorithm (also: deterministic machine, deterministic Turing machine)
- Binary and radix representation (also: binary representation, base-q digits, radix, positional notation, most significant bit, bit string, n-bit integer)
- Schoolbook addition and multiplication with carries (also: long multiplication, carry propagation, carries, grade-school multiplication, quadratic multiplication)
- Karatsuba multiplication (also: Karatsuba algorithm, Karatsuba–Ofman, O(n^{log_2 3}) multiplication)
- Fast Fourier transform (also: FFT, Cooley–Tukey FFT, radix-2 FFT, FFT polynomial multiplication)
- Two's complement and signed integer representation (also: two's complement, sign-extended two's complement, sign and magnitude, signed integers)
- Fixed-point binary fractions (also: fixed-point arithmetic, dyadic rationals, binary fractions, precision p, truncation)
- Bitwise XOR (also: XOR, exclusive or, addition mod 2, ⊕)
- Modular arithmetic (also: congruence, mod, ≡ (mod q), residues, residue ring, Z/qZ, unit modulo q, modular inverse)
- Greatest common divisor and coprimality (also: gcd, coprime, relatively prime, pairwise coprime, prime to q, Euclidean algorithm)
- Prime numbers (also: primes, odd prime, trial division, primality test)
- Chinese remainder theorem (also: CRT, Chinese remainder, Chinese-remainder theorem)
- Integer division and integer square root (also: quotient and remainder, Euclidean division, floor division, ⌊a/b⌋, ⌊√a⌋, integer square root)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Sets, Cartesian products and cardinality (also: Cartesian product, product set, intersection, |S ∩ T|, cardinality, ×)
- Subsets and binomial coefficients (also: k-subsets, three-element subsets, triples, binomial coefficient, n choose k)
- Indicator vector (also: characteristic vector, 0/1 vector of a subset, indicator function)
- Permutations (also: permutation, bijection, inverse permutation, composition of permutations, address permutation, reordering)
- Lexicographic order (also: lexicographic order, dictionary order, row-major order, most significant coordinate first)
- Sorting and stable radix sort (also: sorting, stable sort, radix sort, merge, merging sorted streams)
- Binary counters and amortized analysis (also: binary counter, increment, amortized cost, countdown)
- Stack (also: stack, push and pop, LIFO, depth-first scheduling)
- Directed graphs and acyclic networks (also: directed graph, DAG, directed acyclic graph, vertex, edge, source, sink, path)
- Boolean and arithmetic circuits (also: circuit, logical network, circuit size, gates, wires)
- Matrix inverse, transpose and identity (also: inverse matrix, invertible matrix, transpose, x^T, identity matrix, I, matrix transposition)
- Special matrices (also: diagonal matrix, diag, triangular matrix, lower triangular, upper triangular, permutation matrix, all-ones matrix, J)
- Eigenvalues (also: eigenvalue, eigenvector, spectrum)
- Sup norm and the triangle inequality (also: maximum norm, infinity norm, ‖·‖_∞, coefficient sup norm, absolute error, triangle inequality)
- Number systems and their notation (also: Z, Q, R, C, integers, rationals, reals, ℤ, ℚ, ℂ)
- Fields and rings (also: field, ring, finite field, commutative ring, unit of a ring)
- Gaussian function (also: Gaussian, e^{-x^2}, bell curve)

## This page

Concept: Normalized convolution over the polynomial ring
Gloss: Computing normalized cyclic convolution of arrays of ring elements by two forward synthetic transforms, pointwise packed products in the retained order, and the opposite transform.

## This page in the argument

The step: Normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes has error below $\sqrt2M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
How: compute two forward synthetic transforms, multiply records pointwise in their retained stored order with signed packing, and apply the opposite transform to that order
Why: Pointwise multiplication commutes with the common record permutation of both forward outputs, so the bit-reversed and layout order never has to be undone before the opposite transform. (the sources say so: "Pointwise multiplication commutes with applying the same record" (paper))

Its sub-steps, in order:

- Radix-two butterflies and monomial twiddles compute $B_tF_t^-$, storing frequency $j$ at the bit-reversed slot, and the reversed procedure computes $F_t^+B_t^{-1}$. (on [Synthetic polynomial transform](synthetic-transform.md))
- With a layout placing selected bits at common offsets in consecutive $K$-bit chunks, each multidimensional synthetic transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\ell 2^{-p}$. (on [Synthetic transform layout and cost](synthetic-layout.md))
- Each normalized ring product $Q_p(fg/r)$ is computed exactly by signed Kronecker packing and four calls to the $O(N\log N)$ multiplier in $O(rp\log(rp))$ time. (on [Signed Kronecker packing](signed-packing.md))
- Errors add through the contractions, giving total error below $M(3\delta+\eta)=\sqrt2M(3\ell+1)2^{-p}$.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: reduce the product to a cyclic convolution of radix digits, move it by a Chinese-remainder map and Gaussian resampling to power-of-two axes, compute that convolution with synthetic polynomial transforms accelerated by two network-based tape procedures, recover the exact coefficients by rounding, and bound every cost term (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.4**: Errors add through the contractions, giving total error below $M(3\delta+\eta)=\sqrt2M(3\ell+1)2^{-p}$.
Source: "$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed." (paper)
> For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Synthetic polynomial transform](synthetic-transform.md)): Radix-two butterflies and monomial twiddles compute $B_tF_t^-$, storing frequency $j$ at the bit-reversed slot, and the reversed procedure computes $F_t^+B_t^{-1}$.
- S2.2 (on [Synthetic transform layout and cost](synthetic-layout.md)): With a layout placing selected bits at common offsets in consecutive $K$-bit chunks, each multidimensional synthetic transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\ell 2^{-p}$.
- S2.3 (on [Signed Kronecker packing](signed-packing.md)): Each normalized ring product $Q_p(fg/r)$ is computed exactly by signed Kronecker packing and four calls to the $O(N\log N)$ multiplier in $O(rp\log(rp))$ time.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic transform layout and cost](synthetic-layout.md): The tape layout that places the selected bits of all axes at common offsets in consecutive chunks, so each synthetic transform round is one simultaneous layer, with frequencies left in a retained bit-reversed order.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Synthetic transform layout and cost
- [Signed Kronecker packing](signed-packing.md): Multiplying polynomials with signed coefficients by evaluating them at a large power of two, multiplying the resulting integers, and extracting centered coefficients.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Signed Kronecker packing
- [Cyclic convolution](cyclic-convolution.md): Multiplication modulo x^S − 1 on coefficient arrays, which the Fourier transform turns into pointwise multiplication.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Cyclic convolution
- [Error accounting through contractions](contraction-error.md): Since every exact map used is a contraction, errors of approximate subroutines add when composed, which bounds the final numerical error.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Error accounting through contractions

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture in that model.

## Other pages you may link to

- [n log n optimality conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Disk-grid fixed-point arithmetic](disk-grid.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled shifts](controlled-shifts.md)
- [Linear maps, matrices and rank](linear-algebra.md)
- [Scratch restoration](scratch-restoration.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-form.md)
- [Three-element-subset intersection construction](triple-intersection.md)
- [Bank-exchange linear network](bank-exchange-network.md)
- [Row splitting into role streams](role-streams.md)
- [Frames and the common-frame identity](frames.md)
- [Tensor product](tensor-product.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit and recursive power saving](rank-deficit.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Rational address shear](address-shear.md)
- [Fast address-chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit.md)
- [Normalized discrete Fourier transform](dft.md)
- [Multidimensional Fourier transform](multidim-dft.md)
- [Normalized butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Binary phase frames](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with retained permutations](resampling-retained-permutations.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Radix-digit reduction to convolution](radix-digit-reduction.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Coefficient phase twist](coefficient-twist.md)
- [Source-permutation cancellation](permutation-cancellation.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Prime source lengths](prime-lengths.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Convolution from the retained transform layout" (paper)

  > \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.

- "Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands." (paper)

  > Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands. We may therefore multiply the forward outputs in their retained order and pass that order directly to the opposite procedure. The following polynomial product implements this operation with an established integer multiplier.


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

Write the body to `exegenius/tasks/0043-write-ring-convolution.answer.md` and the JSON to `exegenius/tasks/0043-write-ring-convolution.answer.json`, then run `exegenius submit 0043-write-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0043-write-ring-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
