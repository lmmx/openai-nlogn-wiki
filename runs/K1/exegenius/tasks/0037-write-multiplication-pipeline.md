# exegenius task 0037-write-multiplication-pipeline

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
- Chinese remainder axis layout (also: CRT layout, prime-axis layout)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Sort-free Gaussian resampling (also: resampling with retained permutations)
- Bluestein's chirp identity (also: chirp identity)
- Permutation cancellation
- Signed Kronecker packing (also: Kronecker substitution, signed packing)
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic transform)
- Phase twist to negacyclic wrap (also: last-coordinate twist)
- Normalized convolution over the polynomial ring (also: normalized ring product)
- Rounding and carry recovery (also: exact recovery)
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

Concept: Transform pipeline for integer product
Gloss: The sequence of reductions (digit packing, Chinese remainder layout, sort-free Gaussian resampling, chirps, phase twist, normalized ring convolution, cancellation and carry recovery) that computes the exact product of two integers.
Also called: multiplication algorithm

## This page in the argument

The step: The exact product of two $n$-bit integers is computed by the transform reductions in order: radix-digit input, source transforms, pointwise product, opposite transform, rounding, and carry propagation.
How: compose the reductions of the convolution route in the order of the algorithm, and recover the exact integer coefficients by rounding and carries
Why: Each reduction preserves the convolution it computes, so composing them computes the product. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The source-transform procedures supply the three transforms needed for the radix-digit convolution.
- Reading each operand in groups of $b$ bits gives the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. (on [Radix-digit convolution](radix-digit-convolution.md))
- The coefficient-address map $\Phi$ gives source arrays $u,v$ whose exact $p$-bit grid values have norm less than $1/4$.
- The pointwise product of the two computed transforms is truncated to the common component format, giving the array $z$.
- The opposite transform of $z$ multiplied by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$.
- The scaled coefficients round to integers and carries propagate, so the output is exactly the $2n$-bit product. (on [Rounding and carry recovery](rounding-carry-recovery.md))

It serves these steps, from the main result down:

- A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.; how: reduce the product to a transform pipeline whose tape-costly layers each save a power of their width, then fix rational exponents so that every cost term is within the bound (on [Sub-linearithmic integer multiplication on a fixed tape machine](sub-linearithmic-integer-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S9.1, S9.3, S9.4, S9.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S9.1**: The source-transform procedures supply the three transforms needed for the radix-digit convolution.
Source: "The source-transform procedures now supply the three transforms needed" (paper)
> The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

**S9.3**: The coefficient-address map $\Phi$ gives source arrays $u,v$ whose exact $p$-bit grid values have norm less than $1/4$.
Source: "Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ ex

**S9.4**: The pointwise product of the two computed transforms is truncated to the common component format, giving the array $z$.
Source: "Multiply corresponding complex coefficients exactly and truncate" (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(

**S9.5**: The opposite transform of $z$ multiplied by $S$ gives $\widetilde w$ approximating $w=(u*v)/S$.
Source: "Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid" (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient o

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S9.2 (on [Radix-digit convolution](radix-digit-convolution.md)): Reading each operand in groups of $b$ bits gives the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order.
- S9.6 (on [Rounding and carry recovery](rounding-carry-recovery.md)): The scaled coefficients round to integers and carries propagate, so the output is exactly the $2n$-bit product.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Gaussian resampling](gaussian-resampling.md)
- [Truncation to a fixed-point grid](truncation.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Radix-digit convolution](radix-digit-convolution.md): The reduction of an integer product to the cyclic convolution of its base-2^b digit sequences, whose coefficients are short integers before carries are propagated.
  Shown as: Transform pipeline for integer product *<predicate>* Radix-digit convolution
- [Chinese remainder axis layout](chinese-remainder-axes.md): The algebra isomorphism that places a cyclic convolution of pairwise coprime length S on a product of cyclic axes, so that the change of coefficient order is a sequence of controlled shifts.
  Shown as: Transform pipeline for integer product *<predicate>* Chinese remainder axis layout
- [Sort-free Gaussian resampling](sort-free-resampling.md): Gaussian resampling in which the source and target coordinate permutations remain inside the transform formula, so they are never executed as separate full sorts.
  Shown as: Transform pipeline for integer product *<predicate>* Sort-free Gaussian resampling
- [Bluestein's chirp identity](bluestein-chirp.md): The identity that writes a transform with quadratic phase factors (chirps) as a pointwise multiplication by a chirp, a cyclic convolution, and a second pointwise multiplication by the conjugate chirp.
  Shown as: Transform pipeline for integer product *<predicate>* Bluestein's chirp identity
- [Phase twist to negacyclic wrap](phase-twist.md): A phase multiplication of the last cyclic coordinate that turns the cyclic wrap-around into the negative wrap of the polynomial ring, so that the original cyclic product is recovered once the twist is removed.
  Shown as: Transform pipeline for integer product *<predicate>* Phase twist to negacyclic wrap
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md): The bilinear map sending arrays f and g of ring elements to (f * g)/T, computed from the retained transform layout and bounded in the maximum-coefficient norm.
  Shown as: Transform pipeline for integer product *<predicate>* Normalized convolution over the polynomial ring
- [Permutation cancellation](permutation-cancellation.md): The identity that the retained source permutation cancels across the two forward transforms, their pointwise product and the inverse transform, leaving a plain cyclic convolution.
  Shown as: Transform pipeline for integer product *<predicate>* Permutation cancellation
- [Rounding and carry recovery](rounding-carry-recovery.md): The step that removes the known normalizations and digit scales, rounds each recovered coefficient (with error below 1/2), and propagates carries to obtain the exact binary product.
  Shown as: Transform pipeline for integer product *<predicate>* Rounding and carry recovery

## Pages that build on this one

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
- [Fast address-chunk interchange](fast-address-interchange.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Approximate contraction](approximate-contraction.md)
- [Truncation to a fixed-point grid](truncation.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Normalized discrete Fourier transform](fourier-transform.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Parameter choice and cost accounting](parameter-choice-cost.md)
- [Sub-linearithmic integer multiplication on a fixed tape machine](sub-linearithmic-integer-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "The source-transform procedures now supply the three transforms needed" (paper)

  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.


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

Write the body to `exegenius/tasks/0037-write-multiplication-pipeline.answer.md` and the JSON to `exegenius/tasks/0037-write-multiplication-pipeline.answer.json`, then run `exegenius submit 0037-write-multiplication-pipeline` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0037-write-multiplication-pipeline`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
