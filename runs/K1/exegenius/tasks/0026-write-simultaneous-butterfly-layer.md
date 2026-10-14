# exegenius task 0026-write-simultaneous-butterfly-layer

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
- Radix-digit convolution (also: digit convolution)
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

Concept: Simultaneous butterfly layer
Gloss: The operation that applies the two-point butterfly H_0(u, v) = ((u + v)/2, (u − v)/2) to D selected address bits at once on arrays of complex polynomial records, at cost O(V d^λ′) with λ′ < 1.
Also called: parallel butterfly layer, H_0 layer

## This page in the argument

The step: A common butterfly layer $H_0$ on $D\le d$ selected bits of complex polynomial records runs in $O(Vd^{\lambda'})$ time with $\lambda'<1$.
How: apply the complex phase network to the layer, whose phase frames telescope to tensor products of two-point kernels, and truncate once after the completed layer
Why: Intermediate values stay exact Gaussian dyadics, so a single truncation after the contractive layer suffices. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The phase identities express each edge's residual operator as a product of two-point kernels on the selected directions.
- For $p\ge p_0$ the simultaneous normalized butterfly layer is one fixed finite-alphabet procedure with cost $O(Vd^{\lambda'})$.

It serves these steps, from the main result down:

- A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.; how: reduce the product to a transform pipeline whose tape-costly layers each save a power of their width, then fix rational exponents so that every cost term is within the bound (on [Sub-linearithmic integer multiplication on a fixed tape machine](sub-linearithmic-integer-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.1, S2.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.1**: The phase identities express each edge's residual operator as a product of two-point kernels on the selected directions.
Source: "Hold the unselected address bits fixed and regard the stored complex" (paper)
> Hold the unselected address bits fixed and regard the stored complex values on one wire role as a function of the selected bits. The phase identities below express an edge's residual operator as a product of two-point kernels on selected directions.

**S2.2**: For $p\ge p_0$ the simultaneous normalized butterfly layer is one fixed finite-alphabet procedure with cost $O(Vd^{\lambda'})$.
Source: "there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure," (paper)
> \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice of positive integers $p,d,r$ with $p\ge p_0$ and \[ a_dp^\epsilon\le d\le b_dp^\epsilon,\qquad 2^{a_rp/d}\le r\le 2^{b_rp/d}, \] put $K=\lfloor d^c\rfloor$, and let $1\le D\le d$, $P,S\ge1$, and $0\le\rho<K$ be integers. Let $w\ge1$ be an integer component width. The input supplies on a descriptor tape the self-delimiting header \[ \mathcal E= \Gamma(p)\Gamma(d)\Gamma(r)\Gamma(D)\Gamma(P)\Gamma(S) \Gamma(K)\Gamma(\rho+1)\Gamma(w), \] using the integer code from \eqref{eq:integer-descriptor-code}. Assume that this header is valid wi

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Complex phase network](complex-phase-network.md): The fixed linear network over Gaussian dyadic values and binary subspaces that exchanges complex coefficients while restoring every scratch value.
  Shown as: Simultaneous butterfly layer *<predicate>* Complex phase network
- [Truncation to a fixed-point grid](truncation.md): Rounding each real and imaginary coefficient part toward zero onto a grid of spacing 2^−p, which does not increase the maximum-coefficient norm.
  Shown as: Simultaneous butterfly layer *<predicate>* Truncation to a fixed-point grid
- [Linear-time tape stream operations](stream-scans.md): Scans that permute, split, merge, or shift the entries of an array with V stored data bits in O(V) steps, where addresses are implicit in the position of each entry.
  Shown as: Simultaneous butterfly layer *<predicate>* Linear-time tape stream operations
- [Fast address-chunk interchange](fast-address-interchange.md): A tape procedure that swaps two disjoint equal-width address chunks of u bits in a stored array of volume V in O(V u^τ) time for a fixed τ < 1, by recursive calls to the bit network.
  Shown as: Simultaneous butterfly layer *<predicate>* Fast address-chunk interchange

## Pages that build on this one

- Synthetic polynomial transform: A transform over the polynomial ring in which the roots of unity are powers of y, so that multiplying by a root is a signed shift of a coefficient list, computed with radix-two butterflies.
- Parameter choice and cost accounting: The fixing of rational exponents, including τ = σ = 1 − 2^−50 and κ = 2^−182, so that every term of the cost table is within the bound O(n(lg n)^(1−κ)) after division by the stored volume V.
- Sub-linearithmic integer multiplication on a fixed tape machine: A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, with κ = 2^−182, disproving the n log n optimality conjecture in this model.

## Other pages you may link to

- [Exact integer multiplication](integer-multiplication-problem.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Harvey–van der Hoeven multiplier](harvey-hoeven-multiplier.md)
- [Signed Kronecker packing](signed-kronecker-packing.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Schönhage–Strassen optimality conjecture](sch-conjecture.md)
- [Subspaces, rank and orthogonal complement](linear-subspaces.md)
- [Bank-exchange network](bank-exchange-network.md)
- [Frame change for linear gates](frames.md)
- [Address shear](address-shear.md)
- [Three-element subset construction](three-element-subsets.md)
- [Scratch-restoring exchange](scratch-restoring-exchange.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Bruhat factorization for shears](bruhat-factorization.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Approximate contraction](approximate-contraction.md)
- [Normalized discrete Fourier transform](fourier-transform.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
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

- "simultaneously on selected coordinate bits of the numerical arrays" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


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

Write the body to `exegenius/tasks/0026-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0026-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0026-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0026-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
