# exegenius task 0021-write-packed-bit-addition

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Theta, Omega), recursion and induction, discrete mathematics (sets, functions, permutations, graphs, modular arithmetic, primes and gcd, elementary combinatorics), and single-variable calculus. They have taken linear algebra at the level of vectors, matrices, bases, dimension and dot products, and have met complex numbers, polynomials, binary representation, Boolean gates and basic multitape Turing machines. They have not studied abstract algebra beyond residues and the two-element field, Fourier analysis, the FFT, fast integer multiplication, tensor products, or any research-level algorithms or complexity.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model
- The n log n optimality conjecture
- Established O(n log n) multiplier (Harvey–van der Hoeven)
- Arrays in lexicographic tape order with address fields
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Matrix rank, subspaces and orthogonal complements
- Linear exchange network with restored scratch wires
- Frames and the common-frame identity
- Three-element-subset subspace labels
- Rank deficit s < Wm
- Bit exchange network with shear interface
- Lower-triangular factorization of matrices
- Rational matrix shear as field interchanges
- Power-saving recurrence
- Power-width address interchange with rows
- Fast interchange of address chunks
  - $u$ (chunk width): The number of bits in each of the two address chunks being interchanged.
  - $V$ (stored bit volume): The number of data bits stored in the array.
  - $\tau$ (interchange exponent): A fixed constant with 0 < τ < 1 (here 1 − 2^{-50}) in the exponent of the cost.
- Asymptotic notation beyond big-O (also: Theta notation, Omega notation, little-o, Big-Theta, Big-Omega, Θ, Ω, o(1))
- Logarithms and exponentials (also: lg, log base 2, log n, log log n, powers of two, exponent laws)
- Floor, ceiling and rounding (also: floor function, ceiling function, round to nearest integer, truncation toward zero, integer part)
- Proof by induction and recursion (also: mathematical induction, recursive definition, recurrence relation, geometric series, divide and conquer)
- Sets, subsets and basic combinatorics (also: subset, intersection of sets, cardinality, binomial coefficient, counting, indicator vector, characteristic vector, pigeonhole)
- Functions, bijections and permutations (also: permutation, bijection, composition of functions, inverse function, permutation matrix, one-to-one correspondence)
- Graphs (also: vertices and edges, graph, neighbors, adjacency, directed edge, path in a graph)
- Modular arithmetic (also: residues, congruence, integers mod n, Z/nZ, mod q, remainder, cyclic group of residues)
- Primes, coprimality and gcd (also: prime number, relatively prime, coprime, greatest common divisor, Euclidean algorithm, modular inverse, Chinese remainder theorem, prime factorization)
- Binary field F2 and XOR (also: GF(2), F_2, exclusive or, XOR, mod 2 arithmetic, bitwise xor, parity)
- Positional number representation and carries (also: radix, base-b digits, binary representation, digit expansion, carry propagation, schoolbook multiplication, bit length, most significant digit)
- Dyadic rationals and binary fractions (also: dyadic numbers, binary fraction, fixed-point number, fixed-point arithmetic, scaling by a power of two, shift)
- Exponential function and Gaussian function (also: e^x, Euler's formula, Gaussian function, e^{-x^2}, bell curve, exponential decay, calculus bounds, Taylor series)
- Vectors, matrices and linear maps (also: matrix multiplication, invertible matrix, linear transformation, dot product, inner product, linear independence, basis, dimension, identity matrix, diagonal matrix, transpose, lower triangular matrix, linear combination)
- Vector norms and error bounds (also: norm, Euclidean norm, triangle inequality, operator norm, contraction, sup norm, absolute error, modulus of a complex number)
- Boolean gates and circuits (also: logic gate, wire, circuit, XOR gate, AND gate, fan-out, gate network)
- Determinism and exact versus approximate computation (also: deterministic algorithm, exact arithmetic, rational arithmetic, approximation error, worst-case running time, constant-factor overhead)

## This page

Concept: Packed selected-bit addition with deterministic repair
Gloss: Performs y←y⊕x on the same bit position of f chunks at once using eight cyclic shifts of whole chunk ranges (a three-chunk rotation trick that restores a scratch chunk), then corrects the small explicitly identified set of addresses where guard values fail.

## This page in the argument

The step: The XOR $y\leftarrow y\oplus x$ on the same bit position of $f$ chunks at once, restoring a third scratch chunk, takes $O(V(L^\tau+1))$ time using eight cyclic shifts of whole chunk ranges plus a deterministic repair.
How: Perform eight carry-free cyclic shifts that act correctly away from a small set of addresses whose guard values fail, then fix that set by sorting.
Why: A whole-chunk shift adds the same offset to $f$ packed segments at once, but carries between segments are only avoided when guard values stay in range; the few addresses where they fail are exactly identified by their addresses and corrected by sorting. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The eight conditional additions to $u$ and $w$ flip the parity of $u$ exactly when $c=1$ and restore $w$.
- The excluded guard values number twenty per guard, so the bad addresses are at most a fraction $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.
- The exceptional records are extracted, stably radix-sorted by destination rank and reinserted, which costs little because the bad fraction is tiny.

It serves these steps, from the main result down:

- There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce the product to a digit convolution computed with Fourier-type transforms on power-of-two axes, and accelerate the transforms' address rearrangements and butterfly layers by a power of the logarithm. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- There are two fixed-tape procedures whose cost beats a full scan per level by a power: an address-chunk interchange in $O(Vu^\tau)$ and a simultaneous butterfly layer in $O(Vd^{\lambda'})$.; how: Build each procedure from a fixed linear network that exchanges two banks of values and restores its scratch values, and apply it recursively with a strict rank deficit.
- Applying $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ at one bit position in each of $D\le d$ equal-width address chunks costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, with one final truncation.; how: Rewrite $H_0^{\otimes D}$ through the phase kernel $C$, evaluate $C^{\otimes D}$ by the complex phase network whose edge calls are smaller layers on $1/W$-volume row streams, and implement the binary basis changes by packed address-bit additions. (on [Simultaneous butterfly layer](simultaneous-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (R2.4.1, R2.4.2, R2.4.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**R2.4.1**: The eight conditional additions to $u$ and $w$ flip the parity of $u$ exactly when $c=1$ and restore $w$.
Source: "Consequently the complete output is" (paper)
> eftarrow&w+c[\,u\equiv0\pmod2\,],&(4)\\ w&\leftarrow&w+c[\,u\equiv1\pmod2\,],&(5)\\ u&\leftarrow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are preserved, and the arbitrary auxiliary integer $w$ is restored. Each coordinate is updated four times by at most one, so its displacement from its initial value is at most four, even if an intermediate point leaves its starting quotient square. The weaker bound eight will suffice below.

**R2.4.2**: The excluded guard values number twenty per guard, so the bad addresses are at most a fraction $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.
Source: "There are exactly twenty excluded values for each guard in" (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**R2.4.3**: The exceptional records are extracted, stably radix-sorted by destination rank and reinserted, which costs little because the bad fraction is tiny.
Source: "while stable binary radix sorting scans only the extracted records and" (paper)
> If $q_h,q'_h$ are the current and destination values of chunk $h\in\{x,y,z\}$ and $\sigma_h$ is its record stride, the fixed spectator coordinates give \[ \operatorname{rank}(q')=\operatorname{rank}(q)+ \sum_{h\in\{x,y,z\}}(q'_h-q_h)\sigma_h. \] The differences are signed. Attach this destination rank, padded to $\lceil\log_2M\rceil\le A_{\rm rect}$ bits, to the extracted record, and mark its hole on a fixed track of the full stream. Hold the full stream untouched while stable binary radix sorting scans only the extracted records and keys, least significant key bit first. Since $T_0S_0^{-1}$ permutes $\mathcal B$, these keys are distinct and are exactly the ranks of the marked holes. One forward full-stream scan reinserts the sorted records. This implements $T_0$ everywhere.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast interchange of address chunks](chunk-interchange.md): Exchanges two disjoint address chunks of u bits in an array (any prefix, gap and suffix) in O(V u^τ) tape steps for a fixed τ < 1, by padding rows and splitting the width in base m; the final effect is an exact permutation although intermediate steps form XOR combinations.
  Shown as: Packed selected-bit addition with deterministic repair *<predicate>* Fast interchange of address chunks
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md): In linear time, update a target address field by adding an offset computed from earlier control fields modulo q^b (a cyclic shift of blocks), or multiply it by a fixed rational unit.
  Shown as: Packed selected-bit addition with deterministic repair *<predicate>* Controlled cyclic shifts and rational scalings

## Pages that build on this one

- Simultaneous butterfly layer: Applies the two-point butterfly H₀ at one bit position in each of D address chunks at once in O(V d^{λ'}) time, by recursing on the complex phase network with packed basis changes, exact Gaussian-dyadic arithmetic and one final truncation.

## Other pages you may link to

- [Fixed finite-tape machine model](fixed-tape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Established O(n log n) multiplier (Harvey–van der Hoeven)](nlogn-multiplier.md)
- [Arrays in lexicographic tape order with address fields](array-order.md)
- [Elementary stream operations](stream-ops.md)
- [Matrix rank, subspaces and orthogonal complements](matrix-basics.md)
- [Linear exchange network with restored scratch wires](network.md)
- [Frames and the common-frame identity](frames.md)
- [Three-element-subset subspace labels](subset-labels.md)
- [Rank deficit s < Wm](rank-saving.md)
- [Bit exchange network with shear interface](bit-network.md)
- [Lower-triangular factorization of matrices](lower-triangular.md)
- [Rational matrix shear as field interchanges](matrix-shear.md)
- [Power-saving recurrence](power-saving-recurrence.md)
- [Power-width address interchange with rows](power-interchange.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Signed packing (Kronecker substitution)](kronecker-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](int-as-convolution.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-2 FFT order](butterfly-fft.md)
- [Complex phase network](phase-network.md)
- [Fixed-point disk grid and error propagation](fixed-point-disk-grid.md)
- [Coefficient twist to negacyclic ring](negacyclic-twist.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Convolution theorem for normalized transforms](convolution-theorem.md)
- [Multidimensional (tensor) transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Source-permutation cancellation](permutation-cancellation.md)
- [Synthetic transform layout and stored frequency order](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Choice of prime source lengths](prime-lengths.md)
- [Complex cyclic convolution by coefficient twist](complex-convolution.md)
- [Source transform procedure](source-transform.md)
- [Rounding and carry propagation to the exact product](exact-recovery.md)
- [The multiplication algorithm](mult-algorithm.md)
- [Parameter choice and cost balance](parameter-balance.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Packed selected-bit addition on one rectangle" (paper)

  > \begin{lemma}[Packed selected-bit addition on one rectangle] \label{lem:packed-selected-bit-rectangle} Let $R\ge1$, $K\ge6$, $f\ge1$, $L=fK$, and $0\le\rho<K$. Let $N_0,N_1,N_2,N_3$ be positive integers, and let $(\chi_1,\chi_2,\chi_3)$ be a permutation of $(x,y,z)$. Consider $R$-bit records in lexicographic order on \[ [N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2} \times[N_2]\times[2^L]_{\chi_3}\times[N_3]. \] The subscript names the chunk at that position. The input supplies $N_0,\ldots,N_3,R,K,f,\rho$ as a fixed number of canonical binary integers, together with the finite permutation of the chunk names, as in Section~\ref{sec:streams}. Put \[ M=2^{3L}\prod_{h=0}^3N_h,\qquad V=MR,\qquad A_{\rm rect}=\lceil\log_2(2V)\rceil. \] At the selected positions $j_i=\


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

Write the body to `exegenius/tasks/0021-write-packed-bit-addition.answer.md` and the JSON to `exegenius/tasks/0021-write-packed-bit-addition.answer.json`, then run `exegenius submit 0021-write-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0021-write-packed-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
