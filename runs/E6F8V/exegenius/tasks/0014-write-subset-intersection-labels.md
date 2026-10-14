# exegenius task 0014-write-subset-intersection-labels

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
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal polynomial variable whose powers act as roots of unity because y^r=−1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed packing (Kronecker substitution)
- Cyclic-to-negacyclic coefficient twist
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

Concept: Triple-subset labels and the rank budget
Gloss: Subspaces of a fixed space attached to gates and terminals, built from indicator vectors of three-element subsets so that adjacent labels are nested and the total edge rank s is strictly less than the wire count W times the dimension m.

## This page in the argument

The step: Attaching nested nondegenerate subspaces built from indicator vectors of three-element subsets to the gates and terminals of the bit network gives a total edge rank $s_{\rm b}$ strictly less than $W_{\rm b}m$.
How: Choose labels as tensor products of triple lines so that neighbouring labels are nested, count the dimension change of every edge, and show that only the central edges from time 3 to 4 decrease, losing $L<N/2$ in total.
Why: The saving must come from keeping the total dimension lost on decreasing edges small relative to $N$; the sources promise $L<N/2$ so that the extra $N$ source ranks still leave a strict saving. (the sources say so: "We will obtain $L<N/2$. The rational interface below will require" (paper))
Striking feature: The rank budget is strictly below the trivial value $Wm$: the deficit is $N-2L>0$ because the loss ratio $L/N$ is only $100/539$ (bit network) and $101/539$ (complex network), both under $1/2$. (explain why it holds, from the method)

Its sub-steps, in order:

- The signed dimension changes over all edges sum to $Wm-2N$; if decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$.
- Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to 4 (loss $h$ each), and hence $L=Ich$.
- The loss ratio is $L_{\rm b}/N=100/539<1/2$ (and $101/539$ for the complex network).
- With the projection matrices as frames, every input role sees endpoint difference $I_m$, and the rank sum $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ falls short of $W_{\rm b}m$ by $N-2L_{\rm b}>0$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Build two faster tape procedures (address chunk interchange and simultaneous butterfly layers) from rank-saving linear networks, use them in synthetic polynomial transforms and resampled source transforms for a convolution, reduce integer multiplication to that convolution, then prove exactness and add up costs. (on [Integer multiplication below n log n](main-theorem.md))
- There are two fixed linear networks on $W$ wires with labels of dimension $m$ whose edge changes cost $s<Wm$ smaller operations in total, one acting by bit address shears and one by phase kernels.; how: Design a scalar network that exchanges banks and restores scratch, lift it to arrays through frames, then choose subspace labels so each edge change is cheap and the total rank $s$ is below $Wm$.

## Steps this page derives

The argument gives this page these sub-steps of its step (A.3.1, A.3.2, A.3.3, A.3.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**A.3.1**: The signed dimension changes over all edges sum to $Wm-2N$; if decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$.
Source: "dimension $L$, the sum of absolute changes is $Wm-2N+2L$." (paper)
> The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor bilinear form. It has dimension $m$ and is nondegenerate. Write \[ u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3},\qquad U_a=\langle u_a\rangle. \] The prescribed terminal labels are \[ \begin{array}{c|cc} \text{role}&\text{source label}&\text{sink label}\\ \hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{each scratch role}&0&\mathcal F. \end{array} \] Write $W$ for the wire count in the construction under consideration. The source dimensions sum to $N$ and the sink dimensions to $Wm-N$. Thus the signed dimension changes will sum to $Wm-2N$, because the contributions at gates cancel. If decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$. We will obtain $L<N/2$. The rational interface below will require an additional $N$ source ranks, so this inequality will leave a strict saving in both constructions.

**A.3.2**: Every edge joins comparable nondegenerate labels, the only decreasing edges are the central-wire edges from time 3 to 4 (loss $h$ each), and hence $L=Ich$.
Source: "The only decreasing" (paper)
> \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}

**A.3.3**: The loss ratio is $L_{\rm b}/N=100/539<1/2$ (and $101/539$ for the complex network).
Source: "\frac{L_{\rm b}}{N}=\frac{100}{539}" (paper)
> The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.

**A.3.4**: With the projection matrices as frames, every input role sees endpoint difference $I_m$, and the rank sum $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ falls short of $W_{\rm b}m$ by $N-2L_{\rm b}>0$.
Source: "Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$." (paper)
> \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Scratch-restoring bank exchange](scratch-restoring-exchange.md): A fixed linear network of copy, gather, scatter and side-injection gates that swaps two banks of values in three stages while returning every auxiliary (scratch) wire to its arbitrary initial value.
  Shown as: Triple-subset labels and the rank budget *<predicate>* Scratch-restoring bank exchange
- [Subspaces, rank and orthogonal complements](rank-and-orthogonal-subspaces.md): Matrix rank, subspaces with a bilinear form, nondegenerate subspaces, orthogonal complements and orthonormal bases, as used to label a network.
  Shown as: Triple-subset labels and the rank budget *<predicate>* Subspaces, rank and orthogonal complements
- [Frames: changing representation along a network](array-frames.md): Replacing each scalar wire by an array and storing it as D_v g for an invertible operator D_v (a frame), so that a pointwise linear gate commutes with the frame and only the endpoint operator remains.
  Shown as: Triple-subset labels and the rank budget *<predicate>* Frames: changing representation along a network

## Pages that build on this one

- Recursive rank saving: Splitting rows among the W network roles makes each recursive call a 1/W-volume stream, so the cost per volume grows by s/W<m when the parameter is multiplied by m, giving a power saving.
- Complex phase network: The second network over Gaussian dyadics with binary labels, whose frames are built from the two-point kernel C=HSH=aI+bX, so each edge is a product of translation kernels and the endpoint operator is C^{⊗m} on every role.

## Other pages you may link to

- [The n log n barrier](n-log-n-barrier.md)
- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays as address fields on tape](tape-address-model.md)
- [Controlled cyclic shift](controlled-cyclic-shift.md)
- [Address shear and triangular factorization](address-shear-factorization.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](address-chunk-interchange.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
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

- "The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


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

Write the body to `exegenius/tasks/0014-write-subset-intersection-labels.answer.md` and the JSON to `exegenius/tasks/0014-write-subset-intersection-labels.answer.json`, then run `exegenius submit 0014-write-subset-intersection-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0014-write-subset-intersection-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
