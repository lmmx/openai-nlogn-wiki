# exegenius task 0025-write-transform-layout-cost

Project directory: `/home/user/openai-nlogn-wiki/runs/D5` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science background: asymptotic analysis and recurrences, discrete mathematics (modular arithmetic, primes, gcd, permutations, binary representation), introductory linear algebra (matrices, rank, invertibility, vector spaces), and basic algebra with polynomials and complex numbers. They know algorithms such as schoolbook multiplication, divide and conquer and sorting, and basic Turing machines with tapes. They have not studied the FFT or Schönhage–Strassen in depth, rings and finite fields beyond basics, tensor products, or the specialist multitape-complexity and fast-multiplication literature.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Multiplication history and the n log n conjecture
- Convolution and the discrete Fourier transform
- Multiplication as convolution of radix digits
- FFT butterflies
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable of the polynomial, whose powers play the role of roots of unity.
  - $r$ (ring length): The number of complex coefficients in a polynomial; a power of two and the degree bound of the ring elements.
- Synthetic polynomial transforms
- Multidimensional transforms with tensor structure
- Gaussian resampling
- Bluestein chirp conversion
- Phase twist from cyclic to negacyclic
- Signed packing of polynomial products
- Dyadic fixed-point arithmetic and rounding
- Array order and elementary stream operations
- Controlled shifts and rational scalings
- Linear networks with frames
- Finite networks from three-element subsets
- Recursive power saving
- Lower triangular factorization and matrix shear
- Fast address-field interchange
  - $V$ (stored bit volume): The number of stored data bits in the array.
  - $u$ (field width): The number of radix digits in each of the two interchanged address fields.
  - $\tau$ (interchange exponent): A fixed constant strictly less than one controlling the cost.
- Fast simultaneous butterfly layer
  - $V$ (stored bit volume): The number of stored data bits in the array.
  - $d$ (number of chunks): The number of equal-width address chunks (axes) whose selected bit gets a butterfly simultaneously.
  - $\lambda'$ (layer exponent): A fixed constant strictly less than one controlling the cost.
- Schoolbook multiplication and divide and conquer (also: grade-school multiplication, quadratic multiplication, Karatsuba idea, recursion on halves)
- Recurrences and geometric sums (also: recurrence relations, master theorem, geometric series)
- Logarithms, floors and ceilings (also: lg n, log base 2, floor and ceiling, powers of two)
- Binary representation and bitwise operations (also: bits, XOR, exclusive or, binary digits, base-2 expansion, radix representation)
- Modular arithmetic (also: congruences, residues mod n, remainder, units mod q)
- Divisibility, primes and coprimality (also: gcd, greatest common divisor, relatively prime, pairwise coprime, prime numbers)
- Permutations and sorting (also: bijections of a finite set, sorting algorithms, reordering an array)
- Linear algebra over a field (also: matrices, matrix multiplication, invertible matrix, rank, vector space, subspace, dimension, linear map, basis)
- Triangular matrices and elementary operations (also: lower triangular matrix, row operations, Gaussian elimination, identity matrix)
- The field with two elements (also: F_2, GF(2), Z/2Z, binary field, mod 2 arithmetic)
- Rational numbers and dyadic fractions (also: rationals, Q, dyadic rationals, fixed-point numbers, binary fractions)
- Rounding and approximation error (also: truncation, nearest integer, absolute error, error bound, triangle inequality)
- Cyclic groups and powers of a generator (also: Z/nZ, cyclic group, additive group mod n, order of an element)
- Array indexing by tuples and mixed radix (also: multi-index, lexicographic order, row-major order, mixed-radix representation, multidimensional array)
- Sums, products and indicator notation (also: summation notation, Kronecker delta, indicator function, sigma notation)
- Basic complexity of tape computation (also: linear-time scan, one pass over a tape, copying a tape, deterministic algorithm)
- Euclidean norm and inequalities (also: absolute value of complex number, modulus, contraction, Cauchy–Schwarz, norm)
- Gaussian integers (also: Z[i], complex integers, integer complex numbers)

## This page

Concept: Synthetic transform layout and convolution cost
Gloss: Arranging the array so the simultaneous layers apply with frequency order retained, giving a convolution over the ring from two forward transforms, a pointwise product (via signed packing) and an opposite transform at cost O(Tp[dK+pK^{τ-1}+ℓd^{λ'}+log(rp)]).

## This page in the argument

The step: Convolution over $\mathbb C[y]/(y^r+1)$ on $T$ entries is computed at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
How: transform both operands, multiply pointwise, transform back
Why: The convolution theorem turns convolution into pointwise products after a transform; the synthetic transforms are the ones the fast layers accelerate, and the opposite transform must consume the stored frequency order. (the sources do not say this: give the reader the reason)

Its sub-steps, in order:

- Synthetic Fourier transforms over $\mathbb C[y]/(y^r+1)$ use powers of $y$ as roots, are invertible up to $1/t$, and keep frequency order. (on [Synthetic polynomial transforms](synthetic-transforms.md))
- Arranging the array so the simultaneous layers apply gives a transform at the stated layout cost.
- Ring elements with Gaussian-integer coefficients are multiplied exactly by signed Kronecker packing into long integers and the established $O(N\log N)$ multiplier. (on [Signed packing of polynomial products](signed-packing-products.md))
- Two forward transforms, a pointwise packed product and the opposite transform give the convolution over the ring at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.

It serves these steps, from the main result down:

- A deterministic fixed multitape Turing machine multiplies two $n$-bit integers in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: reduce multiplication to a convolution over $\mathbb C[y]/(y^r+1)$ via CRT, Gaussian resampling, chirps and a twist, and evaluate its transforms with fast interchange and butterfly layers (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2, S2.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2**: Arranging the array so the simultaneous layers apply gives a transform at the stated layout cost.
Source: "\begin{lemma}[Transform layout and cost]" (paper)
> \begin{lemma}[Transform layout and cost] \label{lem:synthetic-transform-cost} Fix the rational parameters and positive comparison constants $a_d\leq b_d$, $a_r\leq b_r$ of Proposition~\ref{prop:simultaneous-layer}. Fix constants $C_\ell>0$ and $C_w>1$, and choose the layer constants once as \[ C_M=C_\ell+1,\qquad C_{\rm desc}=32(C_\ell+C_w+1). \] Use these constants and $C_w$ in Proposition~\ref{prop:simultaneous-layer}. These fixed choices determine a cutoff $p_1$, one fixed-tape procedure, and an implicit time constant with the following guarantee. For every choice of positive integers $p,d,r$ with $p\geq p_1$ and \[ a_dp^\epsilon\leq d\leq b_dp^\epsilon,\qquad 2^{a_rp/d}\leq r\leq2^{b_rp/d}, \] suppose $d\geq2$ and $r=2^\ell$ with an integer $2\leq\ell<p$, and require \[ d\ell\leq C_\ell p,\qquad 1\leq K=\lfloor d^c\rfloor\leq\ell-1. \] Let $t_i\in\{2^{\ell-1},2^\ell\}$ for $1\leq i\leq d-1$, put $M=\prod_{i=1}^{d-1}t_i$ and $T=rM$, and let $w$ be an integer with $p+2\leq w\leq C_wp$. The cutoff and time constant are independent of $p,d,r$, these axis choices, the round headers constructed from them, and $w$ within the displayed bounds.

**S2.4**: Two forward transforms, a pointwise packed product and the opposite transform give the convolution over the ring at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
Source: "\begin{proposition}[Convolution from the retained transform layout]" (paper)
> \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Synthetic polynomial transforms](synthetic-transforms.md)): Synthetic Fourier transforms over $\mathbb C[y]/(y^r+1)$ use powers of $y$ as roots, are invertible up to $1/t$, and keep frequency order.
- S2.3 (on [Signed packing of polynomial products](signed-packing-products.md)): Ring elements with Gaussian-integer coefficients are multiplied exactly by signed Kronecker packing into long integers and the established $O(N\log N)$ multiplier.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Array order and elementary stream operations](stream-scans.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transforms](synthetic-transforms.md): Nussbaumer-style Fourier transforms over the negacyclic ring in which roots of unity are powers of y, so multiplications by roots are signed shifts and only butterflies and shifts remain; forward transforms keep the same frequency order and the opposite transform consumes it.
  Shown as: Synthetic transform layout and convolution cost *<predicate>* Synthetic polynomial transforms
- [Fast simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying the H_0 butterfly on the same bit position of d address chunks at once, using phase frames, binary changes of basis by chunk moves and the recursive saving, in time O(V d^λ') instead of d whole-array passes.
  Shown as: Synthetic transform layout and convolution cost *<predicate>* Fast simultaneous butterfly layer
- [Fast address-field interchange](address-interchange.md): Interchange of two disjoint contiguous address fields of u digits in time O(V u^τ) with a fixed τ<1, via XOR combinations of intermediate streams that finally give an exact permutation for arbitrary auxiliary values.
  Shown as: Synthetic transform layout and convolution cost *<predicate>* Fast address-field interchange
- [Signed packing of polynomial products](signed-packing-products.md): Kronecker-substitution style packing of ring elements with Gaussian-integer coefficients into long integers, multiplied by the established O(n log n) multiplier used as an ordinary subroutine.
  Shown as: Synthetic transform layout and convolution cost *<predicate>* Signed packing of polynomial products

## Pages that build on this one

- Parameter choice and total cost accounting: Choosing b=⌈log n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log T/d⌉} and fixed rational exponents with κ=2^{-182}, then summing the normalized cost table, every row of which is a power of p below 1.

## Other pages you may link to

- [Fixed multitape Turing machine model](multitape-model.md)
- [Multiplication history and the n log n conjecture](nlogn-conjecture.md)
- [Convolution and the discrete Fourier transform](convolution-dft.md)
- [Multiplication as convolution of radix digits](radix-digit-convolution.md)
- [Multidimensional transforms with tensor structure](multidimensional-transform.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [FFT butterflies](fft-butterfly.md)
- [Dyadic fixed-point arithmetic and rounding](fixed-point-precision.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Array order and elementary stream operations](stream-scans.md)
- [Linear networks with frames](linear-network-frames.md)
- [Finite networks from three-element subsets](subset-subspace-networks.md)
- [Recursive power saving](recursive-saving.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Lower triangular factorization and matrix shear](lower-triangular-shear.md)
- [Resampling without executing the permutations](resampling-no-sort.md)
- [Chinese-remainder coefficient address map](crt-address-map.md)
- [Parameter choice and total cost accounting](parameter-choice-cost.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "\begin{lemma}[Transform layout and cost]" (paper)

  > \begin{lemma}[Transform layout and cost] \label{lem:synthetic-transform-cost} Fix the rational parameters and positive comparison constants $a_d\leq b_d$, $a_r\leq b_r$ of Proposition~\ref{prop:simultaneous-layer}. Fix constants $C_\ell>0$ and $C_w>1$, and choose the layer constants once as \[ C_M=C_\ell+1,\qquad C_{\rm desc}=32(C_\ell+C_w+1). \] Use these constants and $C_w$ in Proposition~\ref{prop:simultaneous-layer}. These fixed choices determine a cutoff $p_1$, one fixed-tape procedure, and an implicit time constant with the following guarantee. For every choice of positive integers $p,d,r$ with $p\geq p_1$ and \[ a_dp^\epsilon\leq d\leq b_dp^\epsilon,\qquad 2^{a_rp/d}\leq r\leq2^{b_rp/d}, \] suppose $d\geq2$ and $r=2^\ell$ with an integer $2\leq\ell<p$, and require \[ d\ell\leq C_\ell p,\qquad 1\leq K=\lfloor d^c\rfloor\leq\ell-1. \] Let $t_i\in\{2^{\ell-1},2^\ell\}$ for $1\leq i\leq d-1$, put $M=\prod_{i=1}^{d-1}t_i$ and $T=rM$, and let $w$ be an integer with $p+2\leq w\leq C_wp$. The cutoff and time constant are independent of $p,d,r$, these axis choices, the round headers constructed from them, and $w$ within the displayed bounds.

- "\begin{proposition}[Convolution from the retained transform layout]" (paper)

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

Write the body to `exegenius/tasks/0025-write-transform-layout-cost.answer.md` and the JSON to `exegenius/tasks/0025-write-transform-layout-cost.answer.json`, then run `exegenius submit 0025-write-transform-layout-cost` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0025-write-transform-layout-cost`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
