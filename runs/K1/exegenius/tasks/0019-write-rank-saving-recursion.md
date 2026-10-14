# exegenius task 0019-write-rank-saving-recursion

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
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring; its powers serve as roots of unity in the synthetic transforms.
  - $r$ (record length): The number of complex coefficients in a record, which is a power of two.
- Gaussian dyadic numbers (also: dyadic complex numbers)
- Bank-exchange network (also: linear exchange network)
- Three-element subset construction (also: triple labels)
- Scratch-restoring exchange (also: forward invocation)
- Frame change for linear gates (also: frame, common frame)
- Address shear (also: shear)
- Complex phase network (also: complex network)
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

Concept: Rank-saving recursion
Gloss: The fact that the total rank s of the edge changes is less than W times m, so that multiplying the recursion parameter by m multiplies the recursive cost by s/W < m, a strict power saving.
Also called: power saving

## This page in the argument

The step: The total rank $s$ of the edge differences satisfies $s<Wm$, so multiplying the recursion parameter by $m$ multiplies the recursive cost by $s/W<m$.
How: bound each edge's rank change by the dimension of an orthogonal residual of nested subspace labels, then sum over all edges so that the gate contributions telescope
Why: The strict inequality $s/W<m$ per level is the power saving, so the rank total must be bounded. (the sources say so: "is the source of the power saving." (paper))
Striking feature: the total rank $s$ of all edge differences is strictly less than $Wm$, so each recursion level saves a factor $m$ on the recursive cost (explain why it holds, from the method)

Its sub-steps, in order:

- Every edge joins comparable nondegenerate labels, so each edge residual is the orthogonal complement of the smaller label inside the larger one.
- The signed sum of dimension changes over all edges equals $Wm-2N$, because the gate contributions cancel, and the absolute sum is $Wm-2N+2L$.
- The loss ratios are $L_b/N=100/539$ and $L_c/N=101/539$, both smaller than $1/2$.
- The total rank $s$ of the edge differences of the bit network equals $W_bm-N+2L_b$, which is less than $W_bm$.
- Each complex edge's phase-frame difference is a product of one translation kernel per vector of an orthonormal basis of its residual, so the complex network has total count $s_c<W_cm$. (on [Complex phase network](complex-phase-network.md))
- The relative rank deficits exceed $20\cdot 2^{-50}$, so $s/W<m^\tau$ with $\tau=\sigma=1-2^{-50}$ for both networks.

It serves these steps, from the main result down:

- A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$.; how: reduce the product to a transform pipeline whose tape-costly layers each save a power of their width, then fix rational exponents so that every cost term is within the bound (on [Sub-linearithmic integer multiplication on a fixed tape machine](sub-linearithmic-integer-multiplication.md))
- Two disjoint equal-width address chunks of $u$ bits in an array of stored volume $V$ are interchanged in $O(Vu^{\tau})$ time for a fixed exponent $\tau<1$.; how: write the interchange as a shear realized by a fixed bit network, implement each network edge by a smaller interchange, and count the recursion (on [Fast address-chunk interchange](fast-address-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.3.1, S1.3.2, S1.3.3, S1.3.4, S1.3.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.3.1**: Every edge joins comparable nondegenerate labels, so each edge residual is the orthogonal complement of the smaller label inside the larger one.
Source: "Every edge joins comparable nondegenerate labels." (paper)
> \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}

**S1.3.2**: The signed sum of dimension changes over all edges equals $Wm-2N$, because the gate contributions cancel, and the absolute sum is $Wm-2N+2L$.
Source: "The signed sum of dimension changes telescopes at every gate: each" (paper)
> The signed sum of dimension changes telescopes at every gate: each touched wire has one incoming and one outgoing incidence with the same gate label. The sum of source dimensions is $N$, while the sum of sink dimensions is $Wm-N$. The signed increase is therefore $Wm-2N$. There are $Ic$ decreasing edges, each of loss $h$; replacing signed changes by absolute changes adds $2L$.

**S1.3.3**: The loss ratios are $L_b/N=100/539$ and $L_c/N=101/539$, both smaller than $1/2$.
Source: "The loss ratios have the exact values" (paper)
> The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.

**S1.3.4**: The total rank $s$ of the edge differences of the bit network equals $W_bm-N+2L_b$, which is less than $W_bm$.
Source: "The sum of the rational ranks of all edge differences is" (paper)
> \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}

**S1.3.6**: The relative rank deficits exceed $20\cdot 2^{-50}$, so $s/W<m^\tau$ with $\tau=\sigma=1-2^{-50}$ for both networks.
Source: "Both exact deficits displayed above are greater than" (paper)
> The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.3.5 (on [Complex phase network](complex-phase-network.md)): Each complex edge's phase-frame difference is a product of one translation kernel per vector of an orthonormal basis of its residual, so the complex network has total count $s_c<W_cm$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Subspaces, rank and orthogonal complement](linear-subspaces.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Frame change for linear gates](frames.md): An invertible operator D_v attached to each gate, source and sink, so that a wire's stored array is D_v applied to its logical array and a pointwise linear gate commutes with a common frame.
  Shown as: Rank-saving recursion *<predicate>* Frame change for linear gates
- [Scratch-restoring exchange](scratch-restoring-exchange.md): A three-stage gate schedule built from copy, gather, side-injection and scatter gates that adds one bank into another and exchanges two banks with a sign, leaving any initial scratch values unchanged.
  Shown as: Rank-saving recursion *<predicate>* Scratch-restoring exchange
- [Three-element subset construction](three-element-subsets.md): The set of three-element subsets of a fixed ground set together with the intersection-size relation that decides which triples are joined by a wire.
  Shown as: Rank-saving recursion *<predicate>* Three-element subset construction

## Pages that build on this one

- Fast address-chunk interchange: A tape procedure that swaps two disjoint equal-width address chunks of u bits in a stored array of volume V in O(V u^τ) time for a fixed τ < 1, by recursive calls to the bit network.

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
- [Address shear](address-shear.md)
- [Complex phase network](complex-phase-network.md)
- [Bruhat factorization for shears](bruhat-factorization.md)
- [Fast address-chunk interchange](fast-address-interchange.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Approximate contraction](approximate-contraction.md)
- [Truncation to a fixed-point grid](truncation.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
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

- "The decisive property is that the total" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "is the source of the power saving" (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.


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

Write the body to `exegenius/tasks/0019-write-rank-saving-recursion.answer.md` and the JSON to `exegenius/tasks/0019-write-rank-saving-recursion.answer.json`, then run `exegenius submit 0019-write-rank-saving-recursion` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0019-write-rank-saving-recursion`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
