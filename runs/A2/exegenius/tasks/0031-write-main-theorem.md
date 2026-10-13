# exegenius task 0031-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/A2` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: asymptotic notation and recurrences, discrete mathematics (sets, products, permutations, modular arithmetic, the Chinese remainder theorem, logarithms, floor and ceiling), and introductory linear algebra (matrices, bases, subspaces, inner products, norms, Kronecker products). They know polynomials, complex numbers and roots of unity, basic Turing machines with tapes, and sorting and divide-and-conquer. They have not studied FFT-based multiplication in depth, abstract ring theory beyond basics, numerical error analysis, or any research on integer multiplication complexity.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Binary integers
- Fixed-tape Turing machine model
- Convolution
- Multiplication as digit convolution
- Discrete Fourier transform
- Fast transforms and butterflies
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Polynomial ring modulo y^r + 1
  - $r$ (ring size): A power of two giving the number of complex coefficients in each polynomial record.
  - $y$ (ring variable): The polynomial variable, whose r-th power equals -1 in the ring.
- Synthetic polynomial transform
- Chinese-remainder map to prime axes
- Gaussian resampling
- Bluestein chirp identity
- Last-coordinate phase twist
- Fixed-point dyadic arithmetic and contractions
- Signed packing (Kronecker substitution)
- Linear network with roles and frames
- Three-subset intersection construction
- Recursive rank saving
- Triangular factorization of address shears
- Fast interchange of address chunks
- Simultaneous butterfly layer
- Retained transform layout
- Exact normalized ring convolution
- Resampling with permutations left in the transform
- Precision and exact recovery
- Fixed rational parameter choice
- The multiplication algorithm
- Linear maps and matrices (also: matrix, linear transformation, matrix-vector product, invertible matrix, identity matrix)
- Subspaces, bases and dimension (also: vector subspace, linear span, basis, coordinates, direct sum)
- Tensor (Kronecker) product of vectors and matrices (also: tensor product, Kronecker product, otimes, product of operators on separate coordinates)
- Vector norms and the sup norm (also: infinity norm, max norm, Euclidean norm, operator norm, contraction)
- Inner product and orthogonality (also: orthogonal complement, orthogonal vectors, perp, bra-ket notation, Hermitian inner product)
- Triangular matrices and permutation matrices (also: lower triangular, upper triangular, permutation matrix, unit triangular matrix)
- Modular arithmetic (also: congruence, mod, residues, pmod)
- Chinese remainder theorem (also: CRT, coprime moduli decomposition)
- Prime numbers and coprimality (also: gcd, relatively prime, prime factorization, distinct primes)
- Cyclic groups and indices mod m (also: Z/mZ, cyclic index set, cyclic indexing, wraparound indices)
- Finite field F_2 and XOR (also: bitwise XOR, GF(2), exclusive or, mod 2 addition)
- Bit operations and address fields (also: bit strings, bit fields, concatenation of bit strings, binary expansion of indices, bitwise representation of indices)
- Permutations (also: bijection of indices, rearrangement, reordering of an array, permutation of coordinates)
- Cartesian products and multidimensional arrays (also: product set, multi-index, d-dimensional array, axes, coordinates)
- Floor, ceiling and logarithms (also: lceil, lfloor, lg, log base 2, rounding to nearest integer)
- Powers of two and dyadic rationals (also: dyadic numbers, binary fractions, 2^-p grid, power-of-two denominators)
- Rings and the identity y^r = -1 (also: commutative ring, quotient ring, ring modulo polynomial, ring homomorphism)
- Recurrences and recursion cost analysis (also: divide and conquer, recursion tree, master theorem, solving T(n)=aT(n/b)+f(n))
- Sorting and sequential scans on tapes (also: merge sort, sorting by tape, linear scan, passes over a tape)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, carry propagation, Karatsuba algorithm)
- Symbols for asymptotics: Theta and Omega (also: Theta, Omega, little-o, tilde O, soft-O)
- Real and imaginary parts, conjugates and modulus bounds (also: complex conjugate, Re and Im, triangle inequality, absolute value of complex numbers)
- Gaussian function and Gaussian integers (also: bell curve exp(-x^2), Gaussian weight, Gaussian dyadic, Z[i])
- Subsets, binomial counts and combinatorial counting (also: k-element subsets, binomial coefficient, pigeonhole, counting arguments)
- Fixed finite alphabet and worst-case time (also: worst-case running time, deterministic algorithm, input length n, time complexity)
- Linear independence and rank (also: rank of a matrix, linearly independent, kernel, null space, image)
- Cyclic and negacyclic indices as polynomial wrap (also: x^n - 1, wrap-around product, polynomial modulo x^n-1)

## This page

Concept: Integer multiplication in O(n (lg n)^(1-κ)) time
Gloss: A deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1-κ)) time, refuting the n log n optimality conjecture in this model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent): The fixed tiny constant 2^-182 giving the power saving in the logarithmic factor.

## This page in the argument

The step: A deterministic fixed-tape machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: reduce multiplication to ring convolution evaluated by fast synthetic transforms, built from two power-saving tape procedures, then recover the exact product and total the cost
Why: The conjectured n log n comes from n bits times log n transform levels; a power saving in the log factor needs cheaper layers and cheaper data movement, then an exact reduction from multiplication to those layers. (the sources leave this for the reader to work out: spell it out)
Striking feature: kappa=2^-182 is an astronomically small but strictly positive saving. (explain why it holds, from the method)

Its sub-steps, in order:

- The model: one fixed finite alphabet and finitely many one-dimensional tapes, where time counts steps and moving growing fields costs scans. (on [Fixed-tape Turing machine model](fixed-tape-model.md))
- Two tape procedures save a power of the logarithm: fast address interchange costs $O(Vu^\tau)$ and simultaneous butterfly layers cost $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.
- Normalized convolution over the ring modulo $y^r+1$ on the remaining axes is computed accurately within the target cost. (on [Exact normalized ring convolution](ring-convolution.md))
- The Fourier transforms of pairwise coprime lengths needed for the product are evaluated through power-of-two synthetic transforms without executing separate full sorts. (on [Resampling with permutations left in the transform](resampling-no-sort.md))
- Fixed rational parameters $\tau,\lambda,c,\epsilon,\delta$ and others are compatible across all procedures and give $\kappa=2^{-182}$. (on [Fixed rational parameter choice](parameter-choice.md))
- The radix-digit coefficient list is re-indexed by a Chinese-remainder map onto pairwise coprime prime cyclic axes, preserving cyclic convolution. (on [Chinese-remainder map to prime axes](crt-prime-axes.md))
- A last-coordinate phase twist maps cyclic convolution in one coordinate to a polynomial ring modulo $y^r+1$, whose negative wrap gives the cyclic wrap once the twist is removed. (on [Last-coordinate phase twist](phase-twist.md))
- The algorithm: digits to source arrays by the address map, two forward transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation. (on [The multiplication algorithm](multiplication-algorithm.md))
- Rounding errors are bounded so recovered coefficients lie within $1/2$ of integers; rounding and carries give the exact product. (on [Precision and exact recovery](precision-recovery.md))
- The total cost sums to $O(n(\lg n)^{1-\kappa})$ worst-case time on one fixed-alphabet, fixed-tape machine for all $n$, using schoolbook multiplication below a cutoff.

## Steps this page derives

The argument gives this page these sub-steps of its step (S2a, S12). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2a**: Two tape procedures save a power of the logarithm: fast address interchange costs $O(Vu^\tau)$ and simultaneous butterfly layers cost $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.
How: derive both from linear networks with a recursive rank saving

**S12**: The total cost sums to $O(n(\lg n)^{1-\kappa})$ worst-case time on one fixed-alphabet, fixed-tape machine for all $n$, using schoolbook multiplication below a cutoff.
Source: "Each of the seven displayed powers is at most $1-2\kappa$ by" (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Fixed-tape Turing machine model](fixed-tape-model.md)): The model: one fixed finite alphabet and finitely many one-dimensional tapes, where time counts steps and moving growing fields costs scans.
- S5 (on [Exact normalized ring convolution](ring-convolution.md)): Normalized convolution over the ring modulo $y^r+1$ on the remaining axes is computed accurately within the target cost.
- S6 (on [Resampling with permutations left in the transform](resampling-no-sort.md)): The Fourier transforms of pairwise coprime lengths needed for the product are evaluated through power-of-two synthetic transforms without executing separate full sorts.
- S7 (on [Fixed rational parameter choice](parameter-choice.md)): Fixed rational parameters $\tau,\lambda,c,\epsilon,\delta$ and others are compatible across all procedures and give $\kappa=2^{-182}$.
- S8 (on [Chinese-remainder map to prime axes](crt-prime-axes.md)): The radix-digit coefficient list is re-indexed by a Chinese-remainder map onto pairwise coprime prime cyclic axes, preserving cyclic convolution.
- S9 (on [Last-coordinate phase twist](phase-twist.md)): A last-coordinate phase twist maps cyclic convolution in one coordinate to a polynomial ring modulo $y^r+1$, whose negative wrap gives the cyclic wrap once the twist is removed.
- S10 (on [The multiplication algorithm](multiplication-algorithm.md)): The algorithm: digits to source arrays by the address map, two forward transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation.
- S11 (on [Precision and exact recovery](precision-recovery.md)): Rounding errors are bounded so recovered coefficients lie within $1/2$ of integers; rounding and carries give the exact product.
- S2 (on [Recursive rank saving](recursive-power-saving.md)): A recursive linear network gives a power saving: with $W$ roles, $m$-fold parameter growth and $s$ smaller calls, $s<Wm$ makes the recursion cost per unit volume $V$ grow like a power below $m$ per factor.
- S3 (on [Fast interchange of address chunks](address-interchange.md)): Address chunks of $u$ digits are interchanged in $O(Vu^\tau)$ time for some $\tau<1$.
- S4 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ on one bit in each of up to $d$ address chunks at once costs $O(Vd^{\lambda'})$ with $\lambda'<1$, using the complex network and phase frames.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fixed-tape Turing machine model](fixed-tape-model.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Digits to source arrays via address map, two forward transforms, pointwise product, opposite transform, rescale, round, carry.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* The multiplication algorithm
- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md): The 1971 O(n log n log log n) multitape multiplication and the conjecture that n log n is the optimal order of multiplication cost.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Schönhage–Strassen optimality conjecture

## Other pages you may link to

- [Convolution](convolution.md)
- [Multiplication as digit convolution](multiplication-via-convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring.md)
- [Fixed-point dyadic arithmetic and contractions](fixed-point-contraction.md)
- [Chinese-remainder map to prime axes](crt-prime-axes.md)
- [Precision and exact recovery](precision-recovery.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Linear network with roles and frames](linear-network.md)
- [Three-subset intersection construction](subset-network.md)
- [Recursive rank saving](recursive-power-saving.md)
- [Triangular factorization of address shears](matrix-shear.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Discrete Fourier transform](dft.md)
- [Fast transforms and butterflies](fft-butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing (Kronecker substitution)](kronecker-packing.md)
- [Retained transform layout](transform-layout.md)
- [Exact normalized ring convolution](ring-convolution.md)
- [Resampling with permutations left in the transform](resampling-no-sort.md)
- [Fixed rational parameter choice](parameter-choice.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite alphabet" (paper)

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

Write the body to `exegenius/tasks/0031-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0031-write-main-theorem.answer.json`, then run `exegenius submit 0031-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
