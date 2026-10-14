# exegenius task 0028-write-synthetic-polynomial-transform

Project directory: `/home/user/openai-nlogn-wiki/runs/K1` (paths below are relative to it)

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

For these sources: The reader has the standard undergraduate computer science core: discrete mathematics (Cartesian products, permutations, induction, binomial coefficients, graphs, modular arithmetic, gcd, primes and division with remainder), linear algebra over the real and rational numbers (vector spaces, bases, matrices, eigenvalues, dot products, Gaussian elimination), calculus-level analysis (logarithms, exponentials, limits, geometric sums, roots of unity and Euler's formula), and algorithms and computer organization (Omega, Theta and little-o notation, recurrences, positional notation, two's-complement words). Not assumed are fields other than F_2, tensor products, bilinear forms, Gaussian integers, rings and groups, the integer Chinese remainder theorem, limit inferior and Newton iteration.

The reader already understands these concepts:

- Big-O notation (also: O notation)
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication (also: n-bit integer multiplication)
- Schönhage–Strassen optimality conjecture (also: n log n conjecture, n log n optimality conjecture)
- Harvey–van der Hoeven multiplier (also: established O(n log n) multiplier)
- Subspaces, rank and orthogonal complement (also: nondegenerate subspace)
- Linear-time tape stream operations (also: elementary stream operations)
- Cyclic convolution
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring; its powers serve as roots of unity in the synthetic transforms.
  - $r$ (record length): The number of complex coefficients in a record, which is a power of two.
- Gaussian dyadic numbers (also: dyadic complex numbers)
- Approximate contraction (also: error-tracked approximation)
- Truncation to a fixed-point grid (also: grid truncation)
- Bank-exchange network (also: linear exchange network)
- Three-element subset construction (also: triple labels)
- Scratch-restoring exchange (also: forward invocation)
- Frame change for linear gates (also: frame, common frame)
- Rank-saving recursion (also: power saving)
- Address shear (also: shear)
- Bruhat factorization for shears (also: Grigor'ev factorization)
- Fast address-chunk interchange (also: power-width interchange)
- Complex phase network (also: complex network)
- Simultaneous butterfly layer (also: parallel butterfly layer, H_0 layer)
- Radix-digit convolution (also: digit convolution)
- Normalized discrete Fourier transform (also: DFT, normalized Fourier transform)
- Signed Kronecker packing (also: Kronecker substitution, signed packing)
- Logarithms and exponentials (also: binary logarithm, lg, log base 2, natural logarithm, ln, exp, e^x)
- Floor and ceiling functions (also: integer part, floor, ceiling, round down, round up)
- Geometric series (also: geometric sum, finite geometric sum, sum of powers of a ratio)
- Mathematical induction (also: induction, induction on n, strong induction, inductive proof)
- Recurrence relations for running times (also: recurrence, recurrence equation, unrolling a recurrence, divide-and-conquer recurrence)
- Cartesian product of sets (also: product set, direct product, ordered tuples of sets)
- Permutation of a finite set (also: bijection of a finite set, rearrangement, reordering, address permutation)
- Binomial coefficients (also: n choose k, C(n,k), combinations)
- Lexicographic order (also: dictionary order, lex order, row-major order)
- Graphs, vertices and edges (also: graph, vertex, edge, adjacency, neighbouring vertices, intersection graph)
- Modular arithmetic and congruences (also: congruence modulo m, residue class, residues mod m, Z/mZ, modular inverse, arithmetic mod m)
- Greatest common divisor and coprime integers (also: gcd, highest common factor, relatively prime, coprime, Euclidean algorithm, extended Euclidean algorithm)
- Prime numbers (also: primes, primality, trial division, prime factorization)
- Division with remainder (also: Euclidean division, quotient and remainder, integer division, floor division)
- Limits of sequences and functions (also: limit as n tends to infinity, tends to zero, convergence)
- Nth roots of unity and polar form (also: roots of unity, n-th roots of unity, Euler's formula, de Moivre's formula, polar form, unit circle)
- Vector spaces, bases and linear maps (also: linear space, vector space over a field, basis, linear independence, span, linear transformation)
- Matrices, inverses and triangular matrices (also: matrix, matrix product, transpose, identity matrix, invertible matrix, nonsingular matrix, singular matrix, lower-triangular matrix, upper-triangular matrix)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, spectrum)
- Gaussian elimination and elementary row operations (also: row reduction, elementary row operation, elementary matrix, row echelon form)
- Dot product and orthogonality (also: inner product, scalar product, orthogonal vectors, perpendicular vectors)
- Indicator vector of a subset (also: characteristic vector, 0-1 vector of a set, indicator function)
- Arithmetic modulo 2 and XOR (also: exclusive or, XOR, parity, F_2, GF(2), field of two elements, mod-2 arithmetic)
- Dyadic rational numbers (also: dyadic rationals, dyadic fractions, binary fractions)
- Positional (radix) notation (also: base-b representation, radix-b digits, binary representation, digit expansion)
- Two's-complement integers (also: two's complement, signed binary words, signed fixed-width integers)

## This page

Concept: Synthetic polynomial transform
Gloss: A transform over the polynomial ring in which the roots of unity are powers of y, so that multiplying by a root is a signed shift of a coefficient list, computed with radix-two butterflies.
Also called: Nussbaumer transform, synthetic transform

## This page in the argument

The step: The normalized transforms $F_t^\pm$ over $\mathcal R_r$ are contractions computed by radix-two butterflies, and the stored frequency order is consumed exactly by the inverse.
How: radix-two decimation steps whose roots of unity are powers of $y$, with the inverse traversing the same recursion in reverse
Why: Multiplication by a root of unity is then a signed shift of the coefficient list. (the sources say so: "such a root is a signed shift of the coefficient list." (paper))

Its sub-steps, in order:

- Every power of $\omega_t$ is an isometry and each transform entry averages $t$ such images, so $F_t^\pm$ are contractions.
- The root sums cancel, so $F_t^+F_t^-=t^{-1}I$ holds without dividing by $\omega_t^j-1$.
- The two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$, so the inverse consumes the stored frequency order.
- A round is a parallel butterfly $\mathcal H$ followed by a recordwise monomial $J_E$, and each completed round is a contraction.
- The selected bits of the participating axes are placed at a common offset in consecutive $K$-bit chunks, using single-bit moves and chunk interchanges.

It serves these steps, from the main result down:

- A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.; how: reduce the product to a transform pipeline whose tape-costly layers each save a power of their width, then fix rational exponents so that every cost term is within the bound (on [Sub-linearithmic integer multiplication on a fixed tape machine](sub-linearithmic-integer-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1, S3.2, S3.3, S3.4, S3.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1**: Every power of $\omega_t$ is an isometry and each transform entry averages $t$ such images, so $F_t^\pm$ are contractions.
Source: "Every power of $\omega_t$ is an isometry, and each transform entry is" (paper)
> For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$. For $z\in\mathcal R_r^t$ and $0\leq j<t$, set \[ (F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k, \qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k. \] Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images. Thus both transforms are contractions. The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$.

**S3.2**: The root sums cancel, so $F_t^+F_t^-=t^{-1}I$ holds without dividing by $\omega_t^j-1$.
Source: "The ring has zero divisors, so we verify character cancellation" (paper)
> For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$. For $z\in\mathcal R_r^t$ and $0\leq j<t$, set \[ (F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k, \qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k. \] Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images. Thus both transforms are contractions. The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$.

**S3.3**: The two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$, so the inverse consumes the stored frequency order.
Source: "The procedure consuming this stored order traverses the recursion in" (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

**S3.4**: A round is a parallel butterfly $\mathcal H$ followed by a recordwise monomial $J_E$, and each completed round is a contraction.
Source: "A round applies one current $H_0$ on each participating axis." (paper)
> For $D$ axes of lengths $t_1,\ldots,t_D$, put \[ M=\prod_{i=1}^D t_i,\qquad F_{\boldsymbol t}^\pm=\bigotimes_{i=1}^D F_{t_i}^\pm, \qquad B=\bigotimes_{i=1}^D B_{t_i}. \] A round applies one current $H_0$ on each participating axis. The twiddle for axis $i$ depends only on that axis's address bits. The two entries paired by another axis's butterfly have the same axis-$i$ address, so that twiddle commutes with the other butterfly. Consequently the individual axis steps may be grouped as a parallel butterfly $\mathcal H$, followed by one recordwise monomial operation $J_E$. At each address, $J_E$ multiplies the record by \begin{equation} y^{E},\qquad E=-\sum_{i\ \mathrm{participating}} \frac{2r}{u_i}\,b_i k_i\pmod{2r}. \label{eq:combined-twiddle} \end{equation} Here $u_i$ is that axis's current recursive length, $b_i$ its newly written branch bit, and $0\leq k_i<u_i/2$ is encoded by its still unprocessed named slots. The exponent depends on the address, not on coefficient values. In the opposite direction the grouped round is $\mathcal HJ_E^{-1}$: apply $y^{-E}$ first and the parallel butterfly second. Each $\mathcal H$ is a contraction and each $J_E$ is an isometry, so every completed round is a contraction.

**S3.5**: The selected bits of the participating axes are placed at a common offset in consecutive $K$-bit chunks, using single-bit moves and chunk interchanges.
Source: "To apply Proposition~\ref{prop:simultaneous-layer} in a transform round," (paper)
> To apply Proposition~\ref{prop:simultaneous-layer} in a transform round, we must place the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks. We now construct that layout, keeping each polynomial's coefficients in a contiguous suffix. The layout uses the single-bit moves of Lemma~\ref{lem:elementary-streams} and the chunk interchanges of Lemma~\ref{lem:chunk-swap}; each movement is included in the transform cost. The layer then supplies one truncated contraction per round, and its temporary rows and work streams are removed before the next round begins.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Linear-time tape stream operations](stream-scans.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md): The ring of complex polynomials in y reduced modulo y^r + 1, so that y^r equals −1 and products that overflow degree r wrap around with a sign.
  Shown as: Synthetic polynomial transform *<predicate>* Polynomial ring modulo y^r + 1
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The operation that applies the two-point butterfly H_0(u, v) = ((u + v)/2, (u − v)/2) to D selected address bits at once on arrays of complex polynomial records, at cost O(V d^λ′) with λ′ < 1.
  Shown as: Synthetic polynomial transform *<predicate>* Simultaneous butterfly layer
- [Fast address-chunk interchange](fast-address-interchange.md): A tape procedure that swaps two disjoint equal-width address chunks of u bits in a stored array of volume V in O(V u^τ) time for a fixed τ < 1, by recursive calls to the bit network.
  Shown as: Synthetic polynomial transform *<predicate>* Fast address-chunk interchange
- [Normalized discrete Fourier transform](fourier-transform.md): The map on length-q vectors whose k-th output is (1/q) times the sum over j of u_j e^(−2πijk/q), which is a contraction in the maximum-modulus norm.
  Shown as: Synthetic polynomial transform *<predicate>* Normalized discrete Fourier transform

## Pages that build on this one

- Normalized convolution over the polynomial ring: The bilinear map sending arrays f and g of ring elements to (f * g)/T, computed from the retained transform layout and bounded in the maximum-coefficient norm.
- Parameter choice and cost accounting: The fixing of rational exponents, including τ = σ = 1 − 2^−50 and κ = 2^−182, so that every term of the cost table is within the bound O(n(lg n)^(1−κ)) after division by the stored volume V.

## Other pages you may link to

- [Exact integer multiplication](integer-multiplication-problem.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Harvey–van der Hoeven multiplier](harvey-hoeven-multiplier.md)
- [Signed Kronecker packing](signed-kronecker-packing.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Schönhage–Strassen optimality conjecture](sch-conjecture.md)
- [Linear-time tape stream operations](stream-scans.md)
- [Subspaces, rank and orthogonal complement](linear-subspaces.md)
- [Bank-exchange network](bank-exchange-network.md)
- [Frame change for linear gates](frames.md)
- [Address shear](address-shear.md)
- [Three-element subset construction](three-element-subsets.md)
- [Complex phase network](complex-phase-network.md)
- [Scratch-restoring exchange](scratch-restoring-exchange.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Bruhat factorization for shears](bruhat-factorization.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Approximate contraction](approximate-contraction.md)
- [Truncation to a fixed-point grid](truncation.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Phase twist to negacyclic wrap](phase-twist.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Chinese remainder axis layout](chinese-remainder-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Sort-free Gaussian resampling](sort-free-resampling.md)
- [Permutation cancellation](permutation-cancellation.md)
- [Rounding and carry recovery](rounding-carry-recovery.md)
- [Transform pipeline for integer product](multiplication-pipeline.md)
- [Parameter choice and cost accounting](parameter-choice-cost.md)
- [Sub-linearithmic integer multiplication on a fixed tape machine](sub-linearithmic-integer-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "synthetic polynomial transforms of Nussbaumer and Quandalle" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.


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

Write the body to `exegenius/tasks/0028-write-synthetic-polynomial-transform.answer.md` and the JSON to `exegenius/tasks/0028-write-synthetic-polynomial-transform.answer.json`, then run `exegenius submit 0028-write-synthetic-polynomial-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0028-write-synthetic-polynomial-transform`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
