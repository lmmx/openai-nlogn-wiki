# exegenius task 0020-write-packed-selected-bit-addition

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
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal polynomial variable whose powers act as roots of unity because y^r=−1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed packing (Kronecker substitution)
- Cyclic-to-negacyclic coefficient twist
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

Concept: Packed selected-bit addition
Gloss: XORing corresponding selected bits of many chunks at once by a constant number of whole-chunk cyclic shifts that are correct away from a small set of guard-violating addresses, which are then repaired deterministically by sorting.

## This page in the argument

The step: A binary row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on the selected bits of $f$ chunks, with a third chunk restored, costs $O(V(L^\tau+1))$ in the family of parameters used here.
How: Apply eight whole-chunk cyclic shifts that are correct away from a small guard-violating set of addresses, then repair that set deterministically by extracting, sorting by destination and reinserting.
Why: Whole-chunk cyclic shifts are cheap but fail only where a segment carries into its neighbour, which happens for few addresses, so a cheap exact repair of those addresses suffices. (the sources say so: "from a small set of addresses. We then correct exactly that set." (paper))
Striking feature: Only a tiny fraction (at most $80(f-1)2^{-K}$) of addresses violates the guard condition, so repairing them by sorting costs $o(V)$ and the bound is worst-case over all payloads. (explain why it holds, from the method)

Its sub-steps, in order:

- Eight conditional additions induce, for a Boolean control, a flip of the parity of $u$ and restore the auxiliary integer $w$: $(u',w')=(u+c(1-2(u\bmod2)),w)$.
- Each line is a single cyclic shift of a whole chunk whose offset does not depend on its target chunk, so it costs $O(V)$ after chunk swaps.
- Outside the guard-violating set $\mathcal B$ the packed shifts agree with the ideal XOR permutation, and $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.
- The exceptional records are extracted with destination ranks and stably radix-sorted, then reinserted, which implements the ideal permutation everywhere.
- The movement costs $O(V(L^\tau+1))$ and the extra terms vanish after division by $V$ in the stated family of parameters.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Build two faster tape procedures (address chunk interchange and simultaneous butterfly layers) from rank-saving linear networks, use them in synthetic polynomial transforms and resampled source transforms for a convolution, reduce integer multiplication to that convolution, then prove exactness and add up costs. (on [Integer multiplication below n log n](main-theorem.md))
- Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position in each of $D\le d$ address chunks of $K$ bits at once, on polynomial records with complex fixed-point coefficients, costs $O(Vd^{\lambda'})$ with one final truncation.; how: Run the complex phase network on groups of $e=mf$ chunks, implement its binary changes of basis by packed selected-bit additions, split rows among the $W$ roles, and unroll the resulting recurrence with exact dyadic arithmetic. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (C.2.1, C.2.2, C.2.3, C.2.4, C.2.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**C.2.1**: Eight conditional additions induce, for a Boolean control, a flip of the parity of $u$ and restore the auxiliary integer $w$: $(u',w')=(u+c(1-2(u\bmod2)),w)$.
Source: "\bigl(u+c(1-2(u\bmod2)),\ w\bigr)." (paper)
> ow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Each coordinate is updated four times by at most one, so its displacement from its initial value is at most four, even if an intermediate point leaves its starting quotient square. The weaker bound eight will suffice below.

**C.2.2**: Each line is a single cyclic shift of a whole chunk whose offset does not depend on its target chunk, so it costs $O(V)$ after chunk swaps.
Source: "The shift offset never depends on its target chunk, so each line is a" (paper)
> Apply each line of \eqref{eq:eight-packed-additions} simultaneously to all these segment pairs. Physically, a line updating $y$ by sign $\varepsilon$ and testing parity $b$ of $z$ is the single cyclic shift \begin{equation} \label{eq:packed-cyclic-shift} y\longleftarrow y+ \varepsilon\sum_{i=0}^{f-2}2^{j_i} [\,x_{j_i}=1\,][\,z_{j_i}=b\,] \pmod{2^L}. \end{equation} For a line updating $z$, interchange $y$ and $z$ in this formula. The shift offset never depends on its target chunk, so each line is a bijection of the rectangle. Let $S_0$ be their composition. It fixes the spectator coordinates.

**C.2.3**: Outside the guard-violating set $\mathcal B$ the packed shifts agree with the ideal XOR permutation, and $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.
Source: "There are exactly twenty excluded values for each guard in" (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**C.2.4**: The exceptional records are extracted with destination ranks and stably radix-sorted, then reinserted, which implements the ideal permutation everywhere.
Source: "while stable binary radix sorting scans only the extracted records and" (paper)
> If $q_h,q'_h$ are the current and destination values of chunk $h\in\{x,y,z\}$ and $\sigma_h$ is its record stride, the fixed spectator coordinates give \[ \operatorname{rank}(q')=\operatorname{rank}(q)+ \sum_{h\in\{x,y,z\}}(q'_h-q_h)\sigma_h. \] The differences are signed. Attach this destination rank, padded to $\lceil\log_2M\rceil\le A_{\rm rect}$ bits, to the extracted record, and mark its hole on a fixed track of the full stream. Hold the full stream untouched while stable binary radix sorting scans only the extracted records and keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes $\mathcal B$, these keys are distinct and are exactly the ranks of the marked holes. One forward full-stream scan reinserts the sorted records. This implements $T_0$ everywhere.

**C.2.5**: The movement costs $O(V(L^\tau+1))$ and the extra terms vanish after division by $V$ in the stated family of parameters.
Source: "The movement costs $O(V(L^\tau+1))$." (paper)
> The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty. The initial descriptor has a fixed number of canonical integers of $O(A_{\rm rect})$ bits, so its preparation is covered by $O(MA_{\rm rect}^3)$. All counters, positioning, rewinds, and cleanup are included. Equation~\eqref{eq:packed-bad-fraction} proves \eqref{eq:packed-rectangle-time} on a fixed number of tapes. After division by $V=MR$, its additional terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Address chunk interchange](address-chunk-interchange.md): Interchanging two disjoint contiguous address fields of u bits of an array in O(V u^τ) time for a fixed τ<1, using XOR combinations of intermediate data although the final effect is an exact permutation.
  Shown as: Packed selected-bit addition *<predicate>* Address chunk interchange
- [Controlled cyclic shift](controlled-cyclic-shift.md): Adding to a target address field an offset computed from earlier control fields, modulo a range, in O(V) time by splitting and re-merging blocks.
  Shown as: Packed selected-bit addition *<predicate>* Controlled cyclic shift

## Pages that build on this one

- Simultaneous butterfly layer: Applying H₀ to the same bit position in each of D≤d address chunks at once, on polynomial records of complex fixed-point coefficients, in O(V d^{λ'}) time with one final truncation.

## Other pages you may link to

- [The n log n barrier](n-log-n-barrier.md)
- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays as address fields on tape](tape-address-model.md)
- [Scratch-restoring bank exchange](scratch-restoring-exchange.md)
- [Frames: changing representation along a network](array-frames.md)
- [Subspaces, rank and orthogonal complements](rank-and-orthogonal-subspaces.md)
- [Triple-subset labels and the rank budget](subset-intersection-labels.md)
- [Address shear and triangular factorization](address-shear-factorization.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Fixed-point complex grid and truncation](fixed-point-complex-arithmetic.md)
- [Complex phase network](phase-frame-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Fast Fourier transform with butterflies](fft-butterflies.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained frequency order](stored-frequency-order.md)
- [Transform layout on tape](transform-tape-layout.md)
- [Contractions and error accounting](contraction-error-propagation.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Parameter regime for the multiplier](parameter-regime.md)
- [Radix-digit convolution](radix-digit-reduction.md)
- [Source transform on the padded box](tensor-source-transform.md)
- [Precision and exact recovery](precision-exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses" (paper)

  > We implement a binary row addition on corresponding selected bits in two address chunks. A third chunk supplies temporary address bits; its arbitrary initial value must be restored. The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses. The correction depends only on addresses, so the time bound is worst-case over all payloads.


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

Write the body to `exegenius/tasks/0020-write-packed-selected-bit-addition.answer.md` and the JSON to `exegenius/tasks/0020-write-packed-selected-bit-addition.answer.json`, then run `exegenius submit 0020-write-packed-selected-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0020-write-packed-selected-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
