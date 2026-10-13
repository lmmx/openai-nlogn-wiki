# exegenius task 0031-write-synthetic-convolution

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: discrete mathematics (modular arithmetic, primes and gcd, sets, induction, recurrences and asymptotics), basic linear algebra over the reals and complex numbers (matrices, inverses, norms), polynomials and complex roots of unity, and algorithms including divide and conquer and Karatsuba multiplication. On the machine side they know basic single- and multi-tape Turing machines and the idea of counting steps. They have not studied the Fourier transform, FFT-based multiplication, Schonhage-Strassen, Harvey-van der Hoeven, numerical error analysis, abstract algebra beyond rings of residues, finite-field linear algebra, or any lower-bound or advanced tape-algorithm technique, so those must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- Elementary stream operations on tape arrays
- Controlled shifts and rational scalings
- Convolution
- Discrete Fourier transform
- Radix-2 butterflies and FFT
- Subspaces, rank and orthogonal complements
- Fixed-point disk arithmetic and truncation error
- Established O(n log n) integer multiplier
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Signed packing of polynomial products
- Two-point kernel C and phase frames
- Frames on pointwise linear networks
- Subset-intersection exchange network
- Subspace labels and the rank budget
- Recursive power saving from a rank deficit
- Bit network shear interface
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Power-width address interchange
- Fast chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform layout and cost
- Bluestein chirp identity
- Modular arithmetic and residue rings (also: congruence, Z/qZ, integers mod q, residue classes, modular inverse)
- Primes, coprimality and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, extended Euclidean algorithm, coprime)
- Positional (radix) number representation (also: base-b expansion, binary representation, digits, binary integers, mixed radix)
- Signed binary numbers and rounding (also: two's complement, sign-magnitude, floor, ceiling, rounding to nearest integer, truncation toward zero)
- Dyadic rationals (also: binary fractions, fractions with power-of-two denominator, fixed-point binary fractions)
- Bitwise operations and Hamming weight (also: XOR, exclusive or, bit string, popcount, Hamming weight, parity)
- Permutations and bijections (also: permutation of indices, bijection, inverse permutation, bit-reversal permutation, transposition)
- Lexicographic order and multi-index addressing (also: row-major order, dictionary order, multidimensional array indexing, mixed-radix address, tuple indices)
- Matrix algebra (also: matrix multiplication, matrix inverse, identity matrix, transpose, invertible matrix, 2x2 matrices, diagonal matrix, matrix-vector product)
- Vector norms and the triangle inequality (also: sup norm, max norm, infinity norm, absolute value bound, modulus bound, triangle inequality)
- Logarithms, exponentials and floor/ceiling in analysis (also: log base 2, lg, powers of two, exponent laws, iterated logarithm, real exponent)
- Theta, Omega and little-o notation (also: big-Theta, big-Omega, little-o, liminf, asymptotic lower bound, tight bound)
- Summations and geometric series (also: geometric sum, telescoping sum, sum of powers, series bound)
- Recurrence relations and divide and conquer (also: recurrence, unrolling a recurrence, master theorem, recursion tree, recursive algorithm, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, quadratic multiplication)
- Stacks and call stacks (also: stack, recursion stack, call stack, program counter, subroutine call)
- Pointwise operations on lists and vectors (also: componentwise product, Hadamard product, elementwise map, coordinatewise operation)
- Sets, subsets and counting (also: subset, cardinality, intersection, binomial coefficient, ground set, indicator vector, power set)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, contradiction, proof techniques)
- Euler's formula and complex exponentials (also: e^{i theta}, Euler formula, unit circle, phase factor, twiddle factor, modulus of e^{i theta})

## This page

Concept: Convolution from the retained transform layout
Gloss: Normalized convolution over the polynomial ring by two forward synthetic transforms, pointwise ring products via signed packing, and the opposite transform consuming the same stored order.

## This page in the argument

The step: Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays of $M$ ring records over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ has error below $\sqrt2\,M(3\ell+1)2^{-p}$ and costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$, using two forward synthetic transforms, pointwise ring products and the opposite transform.
How: Apply the convolution theorem in the ring: transform both operands, multiply pointwise with signed packing, and transform back, keeping the same frequency order throughout so that no permutation is executed.
Why: The opposite transform can consume the stored bit-reversed order, so the two forward transforms and the pointwise product never need the frequencies sorted. (the sources say so: "retain the same frequency order through their pointwise product, and" (paper))
Striking feature: Both forward transforms keep the same bit-reversed frequency order through the pointwise product, and the opposite transform consumes that order, so the permutation never has to be undone. (explain why it holds, from the method)

Its sub-steps, in order:

- A forward synthetic transform of $M$ ring records, after a positional layout permutation $L$ of the record addresses, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ and leaves the frequencies in bit-reversed order $B$, which the opposite transform consumes. (on [Synthetic transform layout and cost](synthetic-transform-layout.md))
- Two disk-grid ring polynomials $f,g$ modulo $y^r+1$ are multiplied exactly and returned as $Q_p(fg/r)$ in $O(rp\log(rp))$ time, by evaluating at $B_0=2^{4p}$, multiplying four pairs of integers with the established multiplier, and reading coefficients back by centered residues. (on [Signed packing of polynomial products](signed-packing.md))
- Perform both forward transforms, retain their common $LB$ order, multiply corresponding records, apply the opposite procedure and scale exactly by $M=T/r$.
- Expanding the finite sums gives $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, so the scaled result is $(f*g)/(rM)$.
- The three transform errors and the product truncation add to an error below $\sqrt2\,M(3\ell+1)2^{-p}$ after scaling by $M$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost. (on [Sub-n log n integer multiplication](sub-nlogn-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.3, S4.4, S4.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.3**: Perform both forward transforms, retain their common $LB$ order, multiply corresponding records, apply the opposite procedure and scale exactly by $M=T/r$.
Source: "Perform both forward transforms and retain their common $LB$ order." (paper)
> \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.

**S4.4**: Expanding the finite sums gives $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, so the scaled result is $(f*g)/(rM)$.
Source: "To check normalization, expansion of the finite sums gives" (paper)
> To check normalization, expansion of the finite sums gives \[ F_{\boldsymbol t}^-(f*g) =M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g). \] As $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, it follows that \[ M F_{\boldsymbol t}^+ \left(\frac{(F_{\boldsymbol t}^-f) (F_{\boldsymbol t}^-g)}r\right) =\frac{f*g}{rM}. \] Let $P(u,v)$ denote the exact pointwise product $uv/r$, and put $\mathcal T_+=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$. Thus $\mathcal T_+$ applied to the pointwise product of the exact stored forward outputs equals $F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$. The displayed normalization identity identifies its exact scaling by $M$ with $\mathcal M_r(f,g)$.

**S4.5**: The three transform errors and the product truncation add to an error below $\sqrt2\,M(3\ell+1)2^{-p}$ after scaling by $M$.
Source: "The final exact multiplication by $M$ therefore gives error less than" (paper)
> For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.1 (on [Synthetic transform layout and cost](synthetic-transform-layout.md)): A forward synthetic transform of $M$ ring records, after a positional layout permutation $L$ of the record addresses, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ and leaves the frequencies in bit-reversed order $B$, which the opposite transform consumes.
- S4.2 (on [Signed packing of polynomial products](signed-packing.md)): Two disk-grid ring polynomials $f,g$ modulo $y^r+1$ are multiplied exactly and returned as $Q_p(fg/r)$ in $O(rp\log(rp))$ time, by evaluating at $B_0=2^{4p}$, multiplying four pairs of integers with the established multiplier, and reading coefficients back by centered residues.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic transform layout and cost](synthetic-transform-layout.md): Placing the selected bits of all axes at a common offset in K-bit chunks so each transform round is a simultaneous layer, with the output frequency order retained for reuse.
  Shown as: Convolution from the retained transform layout *<predicate>* Synthetic transform layout and cost
- [Signed packing of polynomial products](signed-packing.md): Kronecker substitution: evaluating ring polynomials at 2^{4p} to multiply them with the integer multiplier, then reading coefficients back by centered residues.
  Shown as: Convolution from the retained transform layout *<predicate>* Signed packing of polynomial products

## Pages that build on this one

- Coefficient twist to the negacyclic ring: The map x_d ↦ ζy with ζ = e^{πi/r} that turns cyclic convolution in the last coordinate into convolution modulo y^r + 1, so complex cyclic convolution reduces to the synthetic one.
- Complete time bound: Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most p^{1−2κ}, to get O(n (log n)^{1−κ}).

## Other pages you may link to

- [Convolution](convolution.md)
- [Recursive power saving from a rank deficit](recursive-power-saving.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Elementary stream operations on tape arrays](elementary-stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, rank and orthogonal complements](linear-subspaces.md)
- [Frames on pointwise linear networks](frames-on-arrays.md)
- [Subset-intersection exchange network](exchange-network.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Bit network shear interface](bit-network-interface.md)
- [Lower triangular (Bruhat-type) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](synthetic-ring.md)
- [Fixed-point disk arithmetic and truncation error](fixed-point-precision.md)
- [Discrete Fourier transform](dft.md)
- [Radix-2 butterflies and FFT](fft-butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Two-point kernel C and phase frames](phase-kernel-c.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Multidimensional resampling on a padded box](tensor-resampling.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Exact recovery of the integer product](exact-recovery.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Parameter choices](parameter-choices.md)
- [Coefficient twist to the negacyclic ring](convolution-twist.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](cost-accounting.md)
- [Sub-n log n integer multiplication](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}." (paper)

  > For arrays on $\prod_i\mathbb Z/t_i\mathbb Z$ with values in $\mathcal R_r$, let $*$ denote cyclic convolution in the displayed axes and define \[ \mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}. \] For a fixed output coefficient, each of the $M$ first cyclic addresses determines one second address, and each of the $r$ first polynomial indices determines one second index modulo $r$. The negacyclic wrap supplies the sign. Thus that coefficient averages $rM$ signed scalar products, and $\mathcal M_r$ is a bilinear contraction: \[ \|\mathcal M_r(f,g)\|_\infty \leq\|f\|_\infty\|g\|_\infty. \] If the other operand is a disk array, replacing one operand changes the output by at most the norm distance between its two values.

- "Perform both forward transforms and retain their common $LB$ order." (paper)

  > \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.


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

Write the body to `exegenius/tasks/0031-write-synthetic-convolution.answer.md` and the JSON to `exegenius/tasks/0031-write-synthetic-convolution.answer.json`, then run `exegenius submit 0031-write-synthetic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0031-write-synthetic-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
