# exegenius task 0034-write-synthetic-convolution

Project directory: `/home/user/openai-nlogn-wiki/runs/G1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis and recurrences, discrete mathematics (sets, functions, permutations, modular arithmetic, primes, gcd), a first course in linear algebra (vectors, matrices, rank, bases, subspaces, orthogonality, dot products), complex numbers and polynomial algebra, and basic multitape Turing machine computation including binary arithmetic. They have seen schoolbook multiplication and basic divide-and-conquer, but not the FFT's number-theoretic refinements, abstract algebra beyond rings of polynomials, tensor products, bilinear forms over finite fields, or the analytic number theory used for prime estimates.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machines
- The n log n conjecture and multiplication history (also: Schönhage–Strassen conjecture)
- Harvey–van der Hoeven O(n log n) multiplier
- Discrete Fourier transform (also: Fourier transform)
- Cyclic convolution (also: convolution)
- Convolution theorem
- FFT butterflies (decimation in frequency) (also: butterfly, two-point butterfly)
- Integer multiplication as radix-digit convolution
- Multidimensional (tensor) transform (also: tensor transform)
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Fixed-point and Gaussian dyadic arithmetic (also: disk grid array, Gaussian dyadics)
- Bluestein chirp identity (also: chirp)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials, subject to the relation y^r + 1 = 0.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic roots of unity
- Synthetic polynomial transform (also: polynomial transform)
- Coefficient phase twist
- Signed Kronecker packing of polynomial products (also: Kronecker substitution)
- Array layout and elementary tape streams (also: address fields)
- Controlled cyclic shifts of an address field
- Three-element subset gates (copy, gather, scatter, side wires)
- Scratch-restoring bank-exchange network
- Frames: changing representation along a network (also: frame, role)
- Subspace labels and the rank deficit (also: rank saving)
- Recursive power saving
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Address-chunk interchange (also: chunk swap, address rearrangement)
- Phase frames and the C kernel (also: complex phase network)
- Packed selected-bit addition
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout of synthetic transforms (also: retained frequency order)
- Logarithms and exponents (also: log, lg, log base 2, powers of two, iterated logarithm, exponent laws)
- Floor and ceiling functions (also: floor, ceiling, rounding up, rounding down, integer part)
- Binary and radix integer representation (also: positional notation, base-B digits, bit strings, binary expansion, radix, digits in base B, carries)
- Schoolbook multiplication (also: grade-school multiplication, long multiplication, quadratic multiplication, naive multiplication)
- Modular arithmetic and congruences (also: residues, mod, congruence modulo q, residue ring, integers mod q, remainder)
- Primes, gcd and coprimality (also: prime numbers, greatest common divisor, relatively prime, pairwise coprime, extended Euclidean algorithm, modular inverse, trial division, divisibility)
- Sets, functions, bijections and permutations (also: bijection, permutation, injective map, index set, Cartesian product, subset, finite sets, partial permutation)
- Counting and binomial coefficients (also: combinations, n choose k, subset counting, Hamming weight, popcount, number of ones in a bit string)
- XOR and mod 2 arithmetic (also: exclusive or, addition mod 2, bitwise XOR, F_2, GF(2), parity, bitwise operations)
- Vectors, matrices and linear maps (also: matrix multiplication, matrix-vector product, identity matrix, invertible matrix, linear transformation, standard basis vector, linear combination, transpose)
- Rank, bases and subspaces (also: matrix rank, linear independence, basis, span, dimension, subspace, vector space, Gaussian elimination, row reduction, elementary matrices, nested subspaces)
- Dot product and orthogonality (also: inner product, orthogonal vectors, orthonormal basis, orthogonal complement, norm of a vector, orthogonal projection, indicator vector)
- Special matrices: triangular, diagonal and permutation matrices (also: lower triangular matrix, upper triangular matrix, diagonal matrix, permutation matrix, diag, projection matrix)
- Rational numbers and the number systems Q, R, C (also: rationals, real numbers, rational matrices, denominators, integers Z)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2 pi i / n}, unit circle, Euler's formula, complex exponential)
- Triangle inequality and absolute value (also: modulus bound, maximum norm, sup norm, infinity norm, disk bound, error bound, |a+b| <= |a|+|b|)
- Geometric series and recurrences (also: geometric sum, recurrence relation, solving recurrences, unrolling a recurrence, master theorem, divide and conquer, recursion tree)
- Induction and proof by contradiction (also: mathematical induction, inductive proof, proof technique, lemma, pigeonhole principle)
- Tape scans and constant-factor simulation on Turing machines (also: linear-time scan, tape head sweep, work tape, tape reversal, copying a tape, finite control with counter, multitape simulation)
- Schoolbook and Karatsuba-style divide-and-conquer multiplication (also: Karatsuba, Toom-Cook, splitting integers into halves)
- Polynomial evaluation and interpolation (also: evaluation at points, Horner's rule, coefficient list, degree of a polynomial, polynomial division with remainder, polynomial modulo x^q - 1)
- Newton iteration for reciprocals (also: Newton's method, Newton reduction, reciprocal approximation, division by Newton iteration)

## This page

Concept: Convolution over the polynomial ring
Gloss: Two forward synthetic transforms, polynomial products of each record by signed packing, and the opposite transform consuming the same stored frequency order give the normalized ring convolution.

## This page in the argument

The step: Convolution of two arrays over $\mathbb C[y]/(y^r+1)$ is approximated with small error by two forward synthetic transforms, polynomial products and the opposite transform in cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
How: lay the selected bits of the axes out so that simultaneous layers and chunk interchanges evaluate the synthetic transforms, multiply each record by signed packing, and apply the opposite transform to the same stored frequency order
Why: The source says the remaining work is to apply the layers on a suitable layout and keep the frequency order through the convolution. (the sources say so: "layout and retain the resulting frequency order through convolution." (paper))
Striking feature: The same frequency order is consumed by the opposite transform after a pointwise product, so no sorting back to natural order is ever executed. (explain why it holds, from the method)

Its sub-steps, in order:

- The synthetic transforms on a layout that places the selected bits at a common offset in consecutive $K$-bit chunks cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ and keep a fixed frequency order. (on [Tape layout of synthetic transforms](synthetic-transform-layout.md))
- Two polynomials of $\mathbb C[y]/(y^r+1)$ with disk-grid coefficients are multiplied exactly by signed Kronecker packing into four integer products, then divided by $r$ and truncated. (on [Signed Kronecker packing of polynomial products](kronecker-packing.md))
- The normalized ring convolution $\mathcal M_r(f,g)=(f*g)/T$ has an approximation with error below $\sqrt2M(3\ell+1)2^{-p}$ built from the retained transform layout.

It serves these steps, from the main result down:

- A deterministic fixed-tape Turing machine multiplies $n$-bit integers in $T_A(n)=O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: reduce the product to a digit convolution computed by synthetic transforms, replace the address rearrangement and butterfly layers inside those transforms by two faster recursive tape procedures, then assemble, round and bound the cost (on [Integer multiplication below n log n](sub-nlogn-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3**: The normalized ring convolution $\mathcal M_r(f,g)=(f*g)/T$ has an approximation with error below $\sqrt2M(3\ell+1)2^{-p}$ built from the retained transform layout.
Source: "$\mathcal M_r$ on disk grid operands has an approximation with error" (paper)
> \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Tape layout of synthetic transforms](synthetic-transform-layout.md)): The synthetic transforms on a layout that places the selected bits at a common offset in consecutive $K$-bit chunks cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ and keep a fixed frequency order.
- S2.2 (on [Signed Kronecker packing of polynomial products](kronecker-packing.md)): Two polynomials of $\mathbb C[y]/(y^r+1)$ with disk-grid coefficients are multiplied exactly by signed Kronecker packing into four integer products, then divided by $r$ and truncated.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Tape layout of synthetic transforms](synthetic-transform-layout.md): A layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that simultaneous layers and chunk interchanges evaluate the synthetic transform while keeping a fixed frequency order.
  Shown as: Convolution over the polynomial ring *<predicate>* Tape layout of synthetic transforms
- [Signed Kronecker packing of polynomial products](kronecker-packing.md): Evaluating integer-coefficient polynomials at a large base B_0 packs them into integers so that one large integer multiplication yields all coefficients of the product, with signs handled by centered residues.
  Shown as: Convolution over the polynomial ring *<predicate>* Signed Kronecker packing of polynomial products

## Pages that build on this one

- The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by Gaussian-resampled, chirped, synthetic transforms, multiplied pointwise, transformed back, rescaled, rounded and carried to give the exact product.

## Other pages you may link to

- [The n log n conjecture and multiplication history](nlogn-conjecture.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-arithmetic.md)
- [Three-element subset gates (copy, gather, scatter, side wires)](subset-intersection-gates.md)
- [Scratch-restoring bank-exchange network](bank-exchange-network.md)
- [Frames: changing representation along a network](frames-network.md)
- [Subspace labels and the rank deficit](subspace-rank-saving.md)
- [Recursive power saving](recursive-power-saving.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Array layout and elementary tape streams](stream-operations.md)
- [Controlled cyclic shifts of an address field](controlled-shifts.md)
- [Phase frames and the C kernel](binary-phase-interface.md)
- [Lower triangular (Bruhat-type) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic roots of unity](synthetic-roots.md)
- [FFT butterflies (decimation in frequency)](fft-butterfly.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as radix-digit convolution](integer-mult-as-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient phase twist](phase-twist.md)
- [Convolution theorem](convolution-theorem.md)
- [Multidimensional (tensor) transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Linear contractions and error accumulation](contraction-error.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Prime source lengths near powers of two](prime-axis-lengths.md)
- [Parameter choice and time bound](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication below n log n](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "The two forward synthetic transforms retain the same frequency order through their pointwise product" (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.


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

Write the body to `exegenius/tasks/0034-write-synthetic-convolution.answer.md` and the JSON to `exegenius/tasks/0034-write-synthetic-convolution.answer.json`, then run `exegenius submit 0034-write-synthetic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0034-write-synthetic-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
