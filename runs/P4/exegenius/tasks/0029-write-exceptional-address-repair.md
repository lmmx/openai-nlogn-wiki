# exegenius task 0029-write-exceptional-address-repair

Project directory: `/home/user/openai-nlogn-wiki/runs/P4` (paths below are relative to it)

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

For these sources: The reader has finished a standard undergraduate computer science degree: discrete mathematics (induction, counting, modular arithmetic, primes, gcd, permutations, basic graphs), algorithms (asymptotic notation, divide and conquer, recurrences, sorting including radix sort, the idea of the FFT and Karatsuba multiplication at survey level), calculus and basic real analysis (limits, logarithms, exponentials, floors and ceilings, inequalities), introductory linear algebra and probability, and the basics of Turing machines and complexity. They have not studied abstract algebra beyond arithmetic mod n, coding theory, or number-theoretic transforms in depth, and have not met the multitape fast-multiplication literature (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), Gaussian resampling, or Nussbaumer polynomial transforms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- The n log n optimality conjecture
- Established near-linear integer multiplier
- Matrices, rank, subspaces and projections
- Tensor products of vectors, spaces and operators
- Binary vectors, XOR and Hamming weight
- Nondegenerate bilinear forms and orthogonal complements
- Streaming fixed-point and Gaussian dyadic arithmetic
- Arrays, address fields, rows and logical volume
- Linear-time stream operations
- Controlled cyclic shifts and rational scalings
- Depth-first recursion schedule on fixed tapes
- Triple-intersection pairing formulas
- Linear network exchanging two banks with restored scratch
- Frames and the common-frame identity
- Nested subspace labels and the rank deficit
- Address shear
- Bit network and rational shear interface
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Strict rank deficit gives a power saving
- Rows distributed cyclically among wire roles
- Power-width interchange with rows
- Fast address-chunk interchange
- Carry-free packed controlled rotations
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, Θ, Ω, o(1), liminf, eventual lower bound)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, floor, ceiling, change of base, iterated logarithm)
- Binary and radix-b representation of integers (also: positional notation, base-b digits, mixed radix, bit length, val(x))
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba-Ofman, Toom-Cook)
- Divisibility, primes and gcd (also: coprime, relatively prime, greatest common divisor, Euclidean algorithm, trial division, prime number)
- Modular arithmetic and residue classes (also: integers mod n, Z/nZ, congruence, mod Q, remainder, division with remainder, residue ring)
- Roots of unity (also: primitive root of unity, n-th roots of unity, e^{2πi/n}, twiddle factors)
- Recurrences and geometric series (also: divide-and-conquer recurrence, master theorem, solving recurrences, geometric sum, T(n) = aT(n/b) + f(n))
- Induction and elementary proof technique (also: proof by induction, structural induction, contradiction, pigeonhole principle)
- Elementary counting and the union bound (also: binomial coefficients, counting subsets, inclusion–exclusion, union bound, fraction of a finite set, Boole's inequality)
- Sorting and radix sort (also: stable sort, radix sort, counting sort, sorting by key, bucket sort)
- Permutations and bijections (also: index permutation, bit reversal, inverse permutation, permutation matrix, one-to-one correspondence)
- Sets, products of ranges and lexicographic order (also: Cartesian product, index set [n], multi-index, lexicographic order, row-major order)
- Matrix transposition and row-major storage (also: transpose, k×k binary matrix, row-major matrix)
- Triangle inequality and error bounds (also: absolute error, rounding error, approximation error, supremum, modulus inequality, rounding to nearest integer)
- Boolean and arithmetic circuits as networks (also: logic gates, XOR gate, circuit, wires and gates, directed acyclic graph, fan-in and fan-out)
- Graphs, paths and neighbors (also: directed graph, edges and vertices, adjacent vertices, route in a graph)
- Stacks and recursion (also: call stack, LIFO, push and pop, depth-first traversal, recursive procedure)
- Fast Fourier transform and Karatsuba as survey knowledge (also: FFT multiplication, Schönhage–Strassen, polynomial multiplication via evaluation, evaluation and interpolation)
- Real and imaginary parts, rounding and truncation (also: Re and Im, truncate toward zero, nearest integer, fixed-point numbers)
- Dot product, vectors over the rationals and orthonormal bases (also: inner product, orthogonal vectors, standard basis, Gram–Schmidt, bilinear pairing)

## This page

Concept: Deterministic repair of exceptional addresses
Gloss: The packed rotations fail only on a set of addresses whose guard values are near the segment boundary, a fraction at most 80(f−1)2^{−K} of all addresses; these records are extracted, sorted by destination rank with stable radix sort, and reinserted, keeping the bound worst-case.

## This page in the argument

The step: The packed rotations fail only on a set $\mathcal B$ of addresses whose guard values lie near a segment boundary, a fraction at most $80(f-1)2^{-K}$ of all addresses; extracting these records, sorting them by destination rank with a stable radix sort and reinserting them repairs the result in the worst case.
How: Bound the exceptional set by a union bound over the guards, observe that the ideal map and the rotations are bijections that agree off the set, then compute each exceptional record's destination, sort and reinsert.
Why: The exceptional set is defined by addresses alone and is a tiny fraction of them, so handling it by a deterministic sort costs little and keeps the bound worst-case over all payloads. (the sources leave this for the reader to work out: spell it out)
Striking feature: The bad fraction $80(f-1)2^{-K}$ is tiny because $K$ grows faster than $\log p$, so the repair costs only a negligible term although it is executed deterministically. (explain why it holds, from the method)

Its sub-steps, in order:

- The bad set $\mathcal B$ consists of the addresses at which some guard value leaves the interval $[10,2^{K-1}-11]$.
- Twenty values are excluded for each guard, so a union bound over the $2(f-1)$ guards bounds the bad fraction independently of the records.
- Stable binary radix sorting of the extracted records by destination rank, followed by one forward scan that reinserts them, implements the ideal map on $\mathcal B$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to convolution over $\mathbb C[y]/(y^r+1)$ through radix digits, Chinese-remainder axes, Gaussian resampling and chirps, speed up the data movement and the butterfly arithmetic with two network-based tape procedures with a strict rank saving, recover the exact product by rounding and carries, and add up the costs. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Two tape procedures exist for fixed exponents $\tau,\lambda'<1$: one interchanges two disjoint address chunks of $u$ bits in $O(Vu^\tau)$ time, and one applies a normalized butterfly layer on up to $d$ address chunks in $O(Vd^{\lambda'})$ time, where $V$ is the logical bit volume.; how: Obtain both from one fixed linear network that exchanges two banks of values and restores every auxiliary value, whose edge frame changes are smaller calls of the same procedure; the strict inequality $s<Wm$ on their number gives a recursion with a power saving.
- The normalized butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ can be applied at once to the same bit offset of $D\le d$ address chunks of every polynomial record in $O(Vd^{\lambda'})$ time with $\lambda'<1$, exactly up to one final truncation.; how: Write $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, compute $C^{\otimes D}$ by the recursive phase-frame layer on rows split among the wire roles, evaluate everything exactly with guard bits and truncate once at the end. (on [Simultaneous normalized butterfly layer](simultaneous-layer.md))
- To apply $C^{\otimes e}$ on $e=mf$ selected bits, group them into $m$ slots of $f$ chunks, change the binary basis by packed row additions, apply the $f$-fold forward child on each of the $s_{\rm c}$ residual-basis slots, and change back; inverse children cost no extra call because $C^{-1}=-iZCZ$.; how: Write each edge's frame change as $\mathcal P_M\bigl(\prod_j C_{e_j}^{\epsilon_j}\bigr)\mathcal P_M^{-1}$, implement the invertible matrix $M$ by elementary row additions on corresponding bits of whole slots, and recurse on the slots. (on [Recursive phase-frame layer on slots](phase-frame-layer.md))
- One fixed multitape procedure XORs the selected bit at offset $\rho$ of each of the $f$ chunks of $K$ bits of chunk $x$ into chunk $y$ while restoring chunk $z$, in time $O(V(L^\tau+1))$ plus negligible repair terms.; how: Apply the eight packed rotations, each as a chunk interchange, a controlled shift and the undoing interchange, then repair the exceptional addresses deterministically, and finish with the top selected position by a direct two-bit XOR. (on [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (L1.3.2.1, L1.3.2.2, L1.3.2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**L1.3.2.1**: The bad set $\mathcal B$ consists of the addresses at which some guard value leaves the interval $[10,2^{K-1}-11]$.
Source: "Let $\mathcal B$ consist of the addresses for which" (paper)
> Let $\mathcal B$ consist of the addresses for which at least one used guard value, in either $y$ or $z$, fails \begin{equation} \label{eq:packed-guard-interval} 10\le g\le 2^{K-1}-11. \end{equation} At an address outside $\mathcal B$, each segment initially lies in $[20,2^K-21]$. Even displacement eight keeps it inside $[0,2^K-1]$. Inductively, each packed addition therefore agrees with all the independent segment additions: no segment carries into or borrows from the next segment. When $f>1$, the bits below $j_0$ and above the highest used segment are untouched as well. By \eqref{eq:eight-packed-result}, $S_0$ then agrees with the ideal permutation $T_0$ that performs the required XORs at $j_0,\ldots,j_{f-2}$ and fixes all other address coordinates.

**L1.3.2.2**: Twenty values are excluded for each guard, so a union bound over the $2(f-1)$ guards bounds the bad fraction independently of the records.
Source: "There are exactly twenty excluded values for each guard in" (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**L1.3.2.3**: Stable binary radix sorting of the extracted records by destination rank, followed by one forward scan that reinserts them, implements the ideal map on $\mathcal B$.
Source: "while stable binary radix sorting scans only the extracted records and" (paper)
> If $q_h,q'_h$ are the current and destination values of chunk $h\in\{x,y,z\}$ and $\sigma_h$ is its record stride, the fixed spectator coordinates give \[ \operatorname{rank}(q')=\operatorname{rank}(q)+ \sum_{h\in\{x,y,z\}}(q'_h-q_h)\sigma_h. \] The differences are signed. Attach this destination rank, padded to $\lceil\log_2M\rceil\le A_{\rm rect}$ bits, to the extracted record, and mark its hole on a fixed track of the full stream. Hold the full stream untouched while stable binary radix sorting scans only the extracted records and keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes $\mathcal B$, these keys are distinct and are exactly the ranks of the marked holes. One forward full-stream scan reinserts the sorted records. This implements $T_0$ everywhere.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Carry-free packed controlled rotations](packed-rotations.md): Eight cyclic shifts of whole chunk ranges, conditioned on parities and a control bit, flip the parity of u when the control is 1 and restore the auxiliary w, so that XORs on f selected bit positions can be done at once as long as the K-bit segments have unused guard room.
  Shown as: Deterministic repair of exceptional addresses *<predicate>* Carry-free packed controlled rotations
- [Linear-time stream operations](stream-ops.md): Splitting a stream on a digit, applying a fixed pointwise map to aligned streams, merging, moving one digit, and splitting rows cyclically into W streams all cost O(V) on a fixed number of tapes.
  Shown as: Deterministic repair of exceptional addresses *<predicate>* Linear-time stream operations

## Pages that build on this one

- Packed selected-bit addition on one rectangle: One fixed multitape procedure XORs the selected bit (offset ρ of each of f chunks of K bits) of chunk x into chunk y while restoring chunk z, in time O(V(L^τ+1)) plus negligible repair terms; this performs a binary row addition used for change of basis.

## Other pages you may link to

- [Fixed-tape Turing machine model](multitape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Streaming fixed-point and Gaussian dyadic arithmetic](fixed-point-arithmetic.md)
- [Established near-linear integer multiplier](established-multiplier.md)
- [Arrays, address fields, rows and logical volume](address-fields-volume.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrices, rank, subspaces and projections](linear-algebra-basics.md)
- [Tensor products of vectors, spaces and operators](tensor-products.md)
- [Address shear](address-shear.md)
- [Binary vectors, XOR and Hamming weight](f2-vectors.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-orthogonality.md)
- [Triple-intersection pairing formulas](subset-pairing-formulas.md)
- [Linear network exchanging two banks with restored scratch](scalar-exchange-network.md)
- [Frames and the common-frame identity](network-frames.md)
- [Rows distributed cyclically among wire roles](row-splitting-roles.md)
- [Nested subspace labels and the rank deficit](subspace-labels-rank-saving.md)
- [Strict rank deficit gives a power saving](rank-deficit-recurrence.md)
- [Bit network and rational shear interface](bit-network-interface.md)
- [Lower-triangular factorization of a matrix](lower-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Depth-first recursion schedule on fixed tapes](fixed-tape-dfs-schedule.md)
- [Power-width interchange with rows](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-negacyclic.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic root of unity ω_t = y^{2r/t}](synthetic-roots.md)
- [Butterfly step and decimation-in-frequency recursion](fft-butterfly.md)
- [Phase kernel C = aI + bX](phase-kernel.md)
- [Complex phase network interface](complex-network-interface.md)
- [Recursive phase-frame layer on slots](phase-frame-layer.md)
- [Multidimensional transform and cyclic convolution on a product of axes](multidim-dft.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained stored frequency order](frequency-order.md)
- [Max-modulus norm, contractions and error propagation](contraction-error-budget.md)
- [Disk grid and truncation](disk-grid-truncation.md)
- [Guard width for exact intermediate values](guard-width.md)
- [Simultaneous normalized butterfly layer](simultaneous-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Signed Kronecker packing for ring products](signed-packing.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Tensor interface for resampling](tensor-resampling.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Integer multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the source permutation](source-permutation-cancel.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Size parameters of the algorithm](parameter-choice.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Distinct prime source lengths near powers of two](prime-lengths.md)
- [Coefficient twist from cyclic to negacyclic](coefficient-twist.md)
- [Middle transform computed by chirp and complex convolution](chirp-transform.md)
- [Source transform procedure](source-transform.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [The complete multiplication algorithm](multiplication-algorithm.md)
- [Cost analysis and the exponent κ](cost-analysis.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "stable binary radix sorting scans only the extracted records and
keys" (paper)

  > If $q_h,q'_h$ are the current and destination values of chunk $h\in\{x,y,z\}$ and $\sigma_h$ is its record stride, the fixed spectator coordinates give \[ \operatorname{rank}(q')=\operatorname{rank}(q)+ \sum_{h\in\{x,y,z\}}(q'_h-q_h)\sigma_h. \] The differences are signed. Attach this destination rank, padded to $\lceil\log_2M\rceil\le A_{\rm rect}$ bits, to the extracted record, and mark its hole on a fixed track of the full stream. Hold the full stream untouched while stable binary radix sorting scans only the extracted records and keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes $\mathcal B$, these keys are distinct and are exactly the ranks of the marked holes. One forward full-stream scan reinserts the sorted records. This implements $T_0$ everywhere.

- "10\le g\le 2^{K-1}-11." (paper)

  > Let $\mathcal B$ consist of the addresses for which at least one used guard value, in either $y$ or $z$, fails \begin{equation} \label{eq:packed-guard-interval} 10\le g\le 2^{K-1}-11. \end{equation} At an address outside $\mathcal B$, each segment initially lies in $[20,2^K-21]$. Even displacement eight keeps it inside $[0,2^K-1]$. Inductively, each packed addition therefore agrees with all the independent segment additions: no segment carries into or borrows from the next segment. When $f>1$, the bits below $j_0$ and above the highest used segment are untouched as well. By \eqref{eq:eight-packed-result}, $S_0$ then agrees with the ideal permutation $T_0$ that performs the required XORs at $j_0,\ldots,j_{f-2}$ and fixes all other address coordinates.


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

Write the body to `exegenius/tasks/0029-write-exceptional-address-repair.answer.md` and the JSON to `exegenius/tasks/0029-write-exceptional-address-repair.answer.json`, then run `exegenius submit 0029-write-exceptional-address-repair` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-exceptional-address-repair`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
