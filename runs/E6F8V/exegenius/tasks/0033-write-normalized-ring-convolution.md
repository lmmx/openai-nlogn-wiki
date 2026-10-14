# exegenius task 0033-write-normalized-ring-convolution

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: algorithm analysis with big-O, divide and conquer and sorting, discrete mathematics (sets, permutations, modular arithmetic, primes, induction), and introductory linear algebra (matrices, linear maps, invertibility, triangular and permutation matrices). They know polynomials and complex numbers including roots of unity and Euler's formula, basic calculus functions, and basic Turing machines with several tapes and head movements. They have probably met schoolbook and Karatsuba multiplication and the idea of the FFT, but have not studied abstract algebra beyond basics, finite-field theory, numerical analysis of error, multidimensional Fourier methods, or the Schönhage–Strassen line of fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n barrier
- Convolution
- Discrete Fourier transform
- Fast Fourier transform with butterflies
- Fixed-point complex grid and truncation
- Contractions and error accounting
- Subspaces, rank and orthogonal complements
- Arrays as address fields on tape
- Controlled cyclic shift
- Scratch-restoring bank exchange
- Frames: changing representation along a network
- Triple-subset labels and the rank budget
- Address shear and triangular factorization
- Recursive rank saving
- Power-width chunk interchange
- Address chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal polynomial variable whose powers act as roots of unity because y^r=−1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Retained frequency order
- Transform layout on tape
- Signed packing (Kronecker substitution)
- Cyclic-to-negacyclic coefficient twist
- Bluestein chirp identity
- Gaussian resampling
- Retained permutation cancellation
- Chinese-remainder address map
- Binary numerals and bit strings (also: binary representation, bit string, binary expansion, most significant bit, bits)
- Positional notation in any radix (also: base-b representation, radix, digits in base b, mixed radix)
- Integer division with remainder, floor and ceiling (also: Euclidean division, quotient and remainder, floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, residues mod m, integers mod m, Z/mZ, clock arithmetic)
- Arithmetic modulo 2 and XOR (also: XOR, exclusive or, bitwise XOR, parity, F_2, GF(2), addition mod 2)
- Primes, coprimality and gcd (also: prime number, relatively prime, greatest common divisor, pairwise coprime, Euclid's algorithm)
- Roots of unity and Euler's formula (also: e^{i theta}, primitive root of unity, nth roots of unity, unit circle, complex exponential)
- Exponential, logarithm and Gaussian function (also: exp, log base 2, lg, natural logarithm, e^{-x^2}, bell curve)
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, liminf, limit inferior, omega notation)
- Geometric series and sums (also: geometric sum, geometric progression, summation, telescoping)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba algorithm, O(n^2) multiplication, integer multiplication)
- Sorting and its cost (also: merge sort, comparison sorting, O(n log n) sorting, sorting algorithms)
- Permutations and bijections (also: permutation, bijection, one-to-one correspondence, inverse permutation, reordering)
- Sets, subsets and Cartesian products (also: subset, Cartesian product, indicator vector, characteristic vector, tuples, set intersection, intersection size)
- Multidimensional arrays and row-major order (also: lexicographic order, row-major order, array indexing, nested loops, matrix as array)
- Matrices, vectors and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear transformation, linear operator, linear combination, vector space, linear independence, basis, dimension)
- Triangular and permutation matrices (also: lower-triangular matrix, upper-triangular matrix, permutation matrix, LU decomposition, identity matrix, diagonal matrix)
- Dot product, inner product and orthogonality (also: inner product, scalar product, orthogonal vectors, orthonormal, bilinear form)
- Dyadic rationals and fixed-width numerators (also: dyadic fraction, binary fraction, number over a power of two, binary point)
- Matrix transposition (also: transpose, row-major to column-major, transposing an array)
- Triangle inequality and norms (also: maximum norm, sup norm, modulus inequality, |a+b|<=|a|+|b|, error bound)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, proof techniques)
- Cyclic shifts and rotations of lists (also: circular shift, rotation of array, wrap-around shift, cyclic rotation)
- Subroutines and composition of algorithms (also: calling a procedure, black box subroutine, reduction, algorithm composition)

## This page

Concept: Normalized convolution over the polynomial ring
Gloss: Convolving arrays of ring elements by two forward synthetic transforms, a pointwise polynomial product divided by r, and the opposite transform, giving (f*g)/T with a bounded error.

## This page in the argument

The step: On arrays of ring elements, two forward synthetic transforms, a pointwise polynomial product divided by $r$, and the opposite transform followed by a scaling by $M$ compute $(f*g)/T$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$.
How: Multiply the forward outputs in their retained order, pass them to the opposite procedure, and track the normalization and the accumulated truncation errors by contraction bounds.
Why: Pointwise multiplication commutes with applying the same record permutation to both operands, so the forward outputs can be multiplied in the retained order and passed straight to the opposite procedure. (the sources say so: "permutation $LB$ to both operands.  We may therefore multiply the" (paper))
Striking feature: No permutation of the frequency order is ever executed between the forward transforms, the pointwise product and the opposite transform. (explain why it holds, from the method)

Its sub-steps, in order:

- Two polynomials in $\mathcal R_r$ with small signed Gaussian integer coefficients can be multiplied exactly, and $Q_p(fg/r)$ returned, in $O(rp\log(rp))$ time with the $O(N\log N)$ integer multiplier. (on [Signed packing (Kronecker substitution)](signed-packing.md))
- Expanding the finite sums, $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, so $MF^+_{\boldsymbol t}$ of the pointwise product divided by $r$ is $(f*g)/(rM)$.
- Since $LB$ permutes records and leaves their polynomial suffixes intact, the opposite procedure applied to the pointwise product of the stored outputs gives the exact convolution.
- Each forward error is below $\delta=\sqrt2\ell2^{-p}$, the product adds $2\delta+\eta$, the opposite transform is a contraction, and the final scaling by $M$ gives error below $\sqrt2\,M(3\ell+1)2^{-p}$.
- There are $M=T/r$ pointwise polynomial products, costing $O(Tp\log(rp))$ in total, in addition to the three transforms.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Build two faster tape procedures (address chunk interchange and simultaneous butterfly layers) from rank-saving linear networks, use them in synthetic polynomial transforms and resampled source transforms for a convolution, reduce integer multiplication to that convolution, then prove exactness and add up costs. (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (E.2, E.3, E.4, E.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**E.2**: Expanding the finite sums, $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, so $MF^+_{\boldsymbol t}$ of the pointwise product divided by $r$ is $(f*g)/(rM)$.
Source: "=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)." (paper)
> To check normalization, expansion of the finite sums gives \[ F_{\boldsymbol t}^-(f*g) =M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g). \] As $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, it follows that \[ M F_{\boldsymbol t}^+ \left(\frac{(F_{\boldsymbol t}^-f) (F_{\boldsymbol t}^-g)}r\right) =\frac{f*g}{rM}. \] Let $P(u,v)$ denote the exact pointwise product $uv/r$, and put $\mathcal T_+=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$. Thus $\mathcal T_+$ applied to the pointwise product of the exact stored forward outputs equals $F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$. The displayed normalization identity identifies its exact scaling by $M$ with $\mathcal M_r(f,g)$.

**E.3**: Since $LB$ permutes records and leaves their polynomial suffixes intact, the opposite procedure applied to the pointwise product of the stored outputs gives the exact convolution.
Source: "Since $LB$ permutes records and leaves their polynomial suffixes" (paper)
> To check normalization, expansion of the finite sums gives \[ F_{\boldsymbol t}^-(f*g) =M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g). \] As $F_{\boldsymbol t}^+F_{\boldsymbol t}^-=I/M$, it follows that \[ M F_{\boldsymbol t}^+ \left(\frac{(F_{\boldsymbol t}^-f) (F_{\boldsymbol t}^-g)}r\right) =\frac{f*g}{rM}. \] Let $P(u,v)$ denote the exact pointwise product $uv/r$, and put $\mathcal T_+=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Since $LB$ permutes records and leaves their polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$. Thus $\mathcal T_+$ applied to the pointwise product of the exact stored forward outputs equals $F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$. The displayed normalization identity identifies its exact scaling by $M$ with $\mathcal M_r(f,g)$.

**E.4**: Each forward error is below $\delta=\sqrt2\ell2^{-p}$, the product adds $2\delta+\eta$, the opposite transform is a contraction, and the final scaling by $M$ gives error below $\sqrt2\,M(3\ell+1)2^{-p}$.
Source: "The final exact multiplication by $M$ therefore gives error less than" (paper)
> For the error estimate, put $\delta=\sqrt2\ell\,2^{-p}$ and $\eta=\sqrt2\,2^{-p}$. Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones. All four are disk arrays, and each forward error is less than $\delta$. The exact map $P$ is bilinear and satisfies $\|P(x,y)\|_\infty\leq\|x\|_\infty\|y\|_\infty$ by the coefficient bound in Lemma~\ref{lem:signed-ring-product}. Hence \[ \begin{split} P(\widetilde u,\widetilde v)-P(u,v) &=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v),\\ \|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty &<2\delta, \end{split} \] where the first term uses the disk bound on $\widetilde v$ and the second uses it on $u$. Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. The product lemma makes $\widetilde z$ a disk grid array and gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$. If $\widetilde h$ is the returned opposite output, its approximation bound applies to $\widetilde z$. Since $\mathcal T_+$ is a contraction, \[ \|\widetilde h-\mathcal T_+ z_*\|_\infty \leq\|\widetilde h-\mathcal T_+\widetilde z\|_\infty +\|\mathcal T_+(\widetilde z-z_*)\|_\infty <3\delta+\eta. \] The final exact multiplication by $M$ therefore gives error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed. If one original operand has norm at most $\rho$, then $\|\mathcal M_r(f,g)\|_\infty\leq\rho$. Under the stated error margin, the returned norm is less than $\rho+(1-\rho)=1$.

**E.5**: There are $M=T/r$ pointwise polynomial products, costing $O(Tp\log(rp))$ in total, in addition to the three transforms.
Source: "There are $M=T/r$ pointwise polynomial products." (paper)
> There are $M=T/r$ pointwise polynomial products. Their total cost is $O(Tp\log(rp))$; the three transform costs are as stated, and the last exact scaling is linear in $Tp$. All data movement uses the previously specified scans, swaps, and layout restoration. \end{proof} \section{Resampling with the permutations left in the transform} \label{sec:resampling}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- E.1 (on [Signed packing (Kronecker substitution)](signed-packing.md)): Two polynomials in $\mathcal R_r$ with small signed Gaussian integer coefficients can be multiplied exactly, and $Q_p(fg/r)$ returned, in $O(rp\log(rp))$ time with the $O(N\log N)$ integer multiplier.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Transform layout on tape](transform-tape-layout.md): Placing the selected bit of each participating axis at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so that each transform round is one simultaneous butterfly layer.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Transform layout on tape
- [Retained frequency order](stored-frequency-order.md): The forward transform writes outputs in bit-reversed order; the pointwise product and the opposite transform both use this order, so no permutation is ever executed.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Retained frequency order
- [Signed packing (Kronecker substitution)](signed-packing.md): Multiplying two polynomials with small signed integer coefficients by evaluating them at a large power of two, multiplying the resulting integers with the O(n log n) multiplier, and extracting coefficients with centered carries.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Signed packing (Kronecker substitution)
- [Contractions and error accounting](contraction-error-propagation.md): Linear maps that do not increase the maximum-modulus norm; composing approximations adds their errors, which is how the accumulated numerical error is bounded.
  Shown as: Normalized convolution over the polynomial ring *<predicate>* Contractions and error accounting

## Pages that build on this one

- Source transform on the padded box: The approximate source Fourier transform formed by linewise Gaussian maps A, the chirp convolution of length T on the padded power-of-two box, linewise B₀ and an exact 2^γ scale, equal to R F_s on the prime-length source.

## Other pages you may link to

- [The n log n barrier](n-log-n-barrier.md)
- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Arrays as address fields on tape](tape-address-model.md)
- [Controlled cyclic shift](controlled-cyclic-shift.md)
- [Scratch-restoring bank exchange](scratch-restoring-exchange.md)
- [Frames: changing representation along a network](array-frames.md)
- [Subspaces, rank and orthogonal complements](rank-and-orthogonal-subspaces.md)
- [Triple-subset labels and the rank budget](subset-intersection-labels.md)
- [Address shear and triangular factorization](address-shear-factorization.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](address-chunk-interchange.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point complex grid and truncation](fixed-point-complex-arithmetic.md)
- [Complex phase network](phase-frame-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Fast Fourier transform with butterflies](fft-butterflies.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Parameter regime for the multiplier](parameter-regime.md)
- [Radix-digit convolution](radix-digit-reduction.md)
- [Source transform on the padded box](tensor-source-transform.md)
- [Precision and exact recovery](precision-exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

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

Write the body to `exegenius/tasks/0033-write-normalized-ring-convolution.answer.md` and the JSON to `exegenius/tasks/0033-write-normalized-ring-convolution.answer.json`, then run `exegenius submit 0033-write-normalized-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0033-write-normalized-ring-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
