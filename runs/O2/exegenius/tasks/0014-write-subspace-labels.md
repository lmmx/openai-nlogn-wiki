# exegenius task 0014-write-subspace-labels

Project directory: `/home/user/openai-nlogn-wiki/runs/O2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, induction, modular arithmetic, gcd, primes, the Chinese remainder theorem, binary representation and XOR), a first linear algebra course (vector spaces, matrices, rank, Gaussian elimination, eigenvalues, mostly over the reals but with arithmetic mod 2 seen in discrete math), single-variable calculus (limits, exponentials and logarithms, geometric series, simple inequalities, Newton's method), and an algorithms and theory sequence (asymptotic notation, recurrences, sorting, binary search, Turing machines and time complexity, schoolbook multiplication with carries). They have not studied fast Fourier transform based multiplication, the Schönhage–Strassen/Harvey–van der Hoeven line of work, polynomial transforms over quotient rings, tensor products, bilinear forms over finite fields, or the extremal set-theory constructions the paper borrows; those are what the wiki explains.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Polynomials
- Complex numbers
- Multitape Turing machine (also: multitape Turing model)
- Nondegenerate bilinear spaces (also: orthogonal complement, bilinear form)
- Tensor products
- Fixed finite-tape machine model and stream operations (also: logical volume, elementary streams, row split)
- Controlled shifts and rational scalings (also: controlled cyclic shift)
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input length): The number of bits in each integer being multiplied.
  - $\log$ (logarithm): The logarithm function, so n log n is the conjectured optimal growth of multiplication time.
- Gaussian dyadic fixed-point arithmetic (also: disk grid, Z[i,1/2], fixed-point coefficients)
- Polynomial ring ℂ[y]/(y^r + 1) (also: R_r, synthetic roots of unity)
  - $\mathbb C$ (complex numbers): The field of complex numbers supplying the polynomial coefficients.
  - $y$ (indeterminate): The polynomial variable, whose powers serve as roots of unity because y^r = −1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Bank-exchange linear network (also: finite network, role, scratch wires, transparent computation)
- Three-element subset intersection construction (also: Frankl–Wilson construction, index-code decoding, gather and scatter)
- Frames and the common-frame identity (also: frame, endpoint operator, change of frame)
- Binary representation of integers (also: base-2 representation, bit string, most significant bit, leading zeroes, n-bit integer)
- Positional (radix) number systems (also: radix, base b digits, radix-2^b digits, mixed-radix representation, digit)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, carry propagation, quadratic multiplication)
- Two's complement and signed integers (also: signed binary integer, sign bit, sign-magnitude, signed word)
- Floor, ceiling and rounding (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, round to nearest integer, truncation toward zero)
- Integer division with remainder (also: division algorithm, quotient and remainder, a div b, a mod b)
- Logarithms and exponentials (also: log, log_2, lg, natural logarithm, exp, exponential function, powers of two)
- Theta, Omega and little-o notation (also: Θ, Ω, o(f), little-o, asymptotically tight bound, lower bound notation)
- Limits of sequences, lim inf (also: limit, liminf, limit inferior, tends to infinity, eventually, for sufficiently large n)
- Geometric series (also: geometric sum, sum of a geometric progression, geometrically increasing)
- Bernoulli's inequality (also: (1+x)^n ≥ 1+nx)
- Triangle inequality and absolute value (also: |a + b| ≤ |a| + |b|, modulus, absolute error)
- Gaussian function (also: Gaussian, bell curve, e^{-x^2}, Gaussian kernel)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Roots of unity (also: n-th root of unity, primitive root of unity, e^{2πi/n}, ω)
- Modular arithmetic (also: congruence, residues modulo q, mod, ≡ (mod q), Z/qZ, residue ring, reduction modulo q)
- Greatest common divisor and modular inverses (also: gcd, coprime, relatively prime, pairwise coprime, unit modulo q, modular inverse, extended Euclidean algorithm)
- Prime numbers and trial division (also: prime, odd prime, primality test by trial division)
- Chinese remainder theorem (also: CRT, Chinese remainder)
- XOR and arithmetic modulo 2 (also: exclusive or, ⊕, bitwise XOR, parity, addition in F_2, the field with two elements, GF(2), F_2)
- Hamming weight (also: weight of a binary vector, wt(x), popcount, number of ones)
- Sets, subsets and Cartesian products (also: Cartesian product, [a] = {0, …, a−1}, 3-element subset, intersection size, |S ∩ T|, indicator vector, characteristic vector)
- Lexicographic order (also: row-major order, dictionary order, first coordinate most significant)
- Permutations (also: bijection, permutation of addresses, permutation matrix, rearrangement)
- Vector spaces, subspaces, basis and dimension (also: vector space, subspace, basis, dimension, span, linear independence, F_2^m)
- Linear maps and matrices (also: linear operator, linear transformation, matrix product, identity matrix, diagonal matrix, all-one matrix, transpose, kernel, image)
- Rank of a matrix (also: rank, rational rank, rank-one matrix, low-rank)
- Invertible matrices (also: nonsingular matrix, inverse matrix, GL(m, F), general linear group, singular matrix)
- Gaussian elimination (also: row reduction, elimination, row operations, pivoting)
- Triangular matrices (also: lower triangular matrix, upper triangular matrix, unit triangular)
- Eigenvalues (also: eigenvalue, eigenvector, spectrum)
- Max norm (also: infinity norm, ‖·‖_∞, sup norm, maximum absolute entry)
- Mathematical induction (also: induction, proof by induction, strong induction)
- Recurrence relations (also: recurrence, divide-and-conquer recurrence, unrolling a recurrence, recursion tree, master theorem)
- Binary search (also: bisection search)
- Stable sorting and radix sort (also: stable sort, radix sort, LSD radix sort, bucket sort, counting sort, sorting)
- Binary counter (also: incrementing a counter, ripple counting, ripple-carry increment)
- Deterministic worst-case time complexity (also: worst-case running time, deterministic algorithm, time complexity, T(n), lower bound)
- Cyclic shift (also: rotation, circular shift, cyclic rotation of a list)

## This page

Concept: Subspace labels and orthogonal residuals
Gloss: Nested nondegenerate subspaces of the m-dimensional space F^{⊗3} attached to gates and terminals; on each edge the orthogonal residual's dimension counts the smaller operations needed for that edge's frame change.
Also called: labels, orthogonal residual, label space

## This page in the argument

The step: Labelling every vertex by a nondegenerate subspace of $\mathcal F=F^{\otimes3}$, of dimension $m=10^6$, makes adjacent labels nested, with the only decreases on central wires, so the residual dimensions sum to $Wm-2N+2L$ with $L/N=100/539$ or $101/539$, below $1/2$.
How: choose bilinear forms in which triple indicator vectors are nondegenerate and neighbouring ones orthogonal, expose one tensor factor per stage, and tabulate the orthogonal residual of every edge
Why: Edge costs are measured by residual dimensions, so the labels must grow along edges except for a small total loss, which is kept small relative to $N$. (the sources say so: "The saving will come from keeping the total dimension lost on decreasing
edges small relative to $N$." (paper))

Its sub-steps, in order:

- With $\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$ or the dot product over $\mathbb F_2$, every triple line is nondegenerate and neighbouring triple lines are orthogonal.
- Every edge joins comparable labels, the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$ dimensions, and the absolute dimension changes sum to $Wm-2N+2L$ with $L=Ich$.
- The loss ratios are $L_b/N=100/539$ and $L_c/N=101/539$, both smaller than $1/2$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: build two linear-network tape procedures, fast address interchange and simultaneous butterfly layers, from fixed networks with a strict rank saving; use them in synthetic transforms; place these in the Harvey–van der Hoeven reduction through radix digits, a CRT map, Gaussian resampling with retained permutations, Bluestein chirps and a phase twist; and bound every cost term (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two fixed linear networks, a bit network over $\mathbb F_2$ and a complex network over $\mathbb Z[i,1/2]$, exchange two data banks while restoring every scratch value, and the total number $s$ of smaller operations their frame changes need is strictly below $Wm$, with $s/W<m^{1-2^{-50}}$.; how: build a three-stage bank-exchange network on three-element subsets of a 100-element set, carry arrays through it in frames that commute with the gates, label vertices by nested nondegenerate subspaces whose residual dimensions count the smaller calls, and check both interfaces and the explicit deficits (on [Rank saving s < Wm](rank-saving.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3.1, S2.3.2, S2.3.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3.1**: With $\langle t_S,t_T\rangle=|S\cap T|-1$ over $\mathbb Q$ or the dot product over $\mathbb F_2$, every triple line is nondegenerate and neighbouring triple lines are orthogonal.
Source: "Thus every triple line is nondegenerate, and neighboring triple lines
are orthogonal, in the label field belonging to either construction." (paper)
> For the bit network, let $F=\mathbb Q^h$ with bilinear form \[ \langle x,y\rangle=x^{\mathsf T}(I-J/9)y, \] where $J$ is the all-one matrix. This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate. For a triple $T$ let $t_T$ be its indicator vector. Then \[ \langle t_S,t_T\rangle=|S\cap T|-1, \qquad \langle t_T,t_T\rangle=2. \] For the complex network, take instead $F=\mathbb F_2^h$ with the ordinary dot product; here $t_T\cdot t_T=1$. Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction. The scalar domain need not equal the label field. These degree-one intersection formulas specialize the construction described by Alon~\cite[Section~3, remark after Theorem~1.1]{Alon1998} to the prime $2$, with the ground-set size changed to $h=100$.

**S2.3.2**: Every edge joins comparable labels, the only decreasing edges are the central-wire edges from time 3 to time 4, each losing $h$ dimensions, and the absolute dimension changes sum to $Wm-2N+2L$ with $L=Ich$.
Source: "The only decreasing
edges are the central-wire edges from time 3 to time 4; their dimension
loss is $h$." (paper)
> \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}

**S2.3.3**: The loss ratios are $L_b/N=100/539$ and $L_c/N=101/539$, both smaller than $1/2$.
Source: "In particular, both are smaller than $1/2$." (paper)
> The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Tensor products](tensor-products.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Frames and the common-frame identity](frames.md): Assigning each network vertex an invertible operator D_v on wire arrays so that stored data is D_v g; pointwise gates commute with a common frame, so a route from role w to ρ(w) applies only D_sink D_source^{−1} and intermediate frames cancel.
  Shown as: Subspace labels and orthogonal residuals *<predicate>* Frames and the common-frame identity
- [Three-element subset intersection construction](triple-intersection-construction.md): Indexing data by 3-element subsets of a 100-element set so that gather/scatter through central wires yields coefficients depending on |S ∩ T| (mod 2 or minus one), with side wires cancelling unwanted neighbor terms, as in Frankl–Wilson/Alon and index-code decoding.
  Shown as: Subspace labels and orthogonal residuals *<predicate>* Three-element subset intersection construction
- [Nondegenerate bilinear spaces](linear-algebra-bilinear.md): A vector space with a symmetric bilinear form having no nonzero vector orthogonal to everything, so each nondegenerate subspace U splits the space as U ⊥ U^⊥ with an orthogonal projection P_U.
  Shown as: Subspace labels and orthogonal residuals *<predicate>* Nondegenerate bilinear spaces

## Pages that build on this one

- Address shears (H, D) ↦ (H + MD, D): Array permutations Φ_M that add a rational matrix M times one address-field vector D to another H modulo q^b; the bit network's rational matrix interface makes the endpoint operator the shear H ← H + D on every role.
- Rank saving s < Wm: The decisive inequality that the total number s of smaller calls over all edges (sum of residual dimensions or ranks) is strictly less than the wire count W times the label dimension m.
- Binary phase frames: The complex network's frames 𝒞_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels U, whose edge changes factor into one two-point kernel C = aI + bX per orthonormal residual vector and telescope to C^{⊗m} on every role.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Polynomial ring ℂ[y]/(y^r + 1)](ring-y-r-plus-1.md)
- [Fixed finite-tape machine model and stream operations](fixed-tape-model.md)
- [Gaussian dyadic fixed-point arithmetic](gaussian-dyadics.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Bank-exchange linear network](bank-exchange-network.md)
- [Tensor products](tensor-products.md)
- [Address shears (H, D) ↦ (H + MD, D)](address-shears.md)
- [Rank saving s < Wm](rank-saving.md)
- [Volume-normalized recursion](power-saving-recursion.md)
- [Lower triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Fast address-chunk interchange in O(V u^τ)](fast-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Discrete Fourier transform](dft.md)
- [Normalized butterfly H₀](butterfly-h0.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Binary phase frames](phase-frames.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication by radix-digit convolution](radix-digit-convolution.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Coefficient phase twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Disk-grid approximation and error accounting](error-accounting.md)
- [Simultaneous butterfly layer in O(V d^λ′)](simultaneous-butterfly-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Synthetic transform tape layout and cost](synthetic-transform-layout.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The subspaces at adjacent vertices are nested." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "the
\emph{orthogonal residual} is the orthogonal complement of the smaller label inside
the larger one" (paper)

  > The scalar network already has the required signed exchange. We now choose its intermediate labels to make the changes of frame inexpensive. A label is a nondegenerate subspace of a fixed bilinear space. On every edge one label will contain the other. For such an edge, the \emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one; its dimension is the absolute change in label dimension. The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.


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

Write the body to `exegenius/tasks/0014-write-subspace-labels.answer.md` and the JSON to `exegenius/tasks/0014-write-subspace-labels.answer.json`, then run `exegenius submit 0014-write-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0014-write-subspace-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
